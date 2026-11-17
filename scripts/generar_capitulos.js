const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const GUION_PATH = path.join(ROOT, "src/data/guion.json");
const SEGMENTS_DIR = path.join(ROOT, "out/segments");
const OUT_DIR = path.join(ROOT, "out");

const STOP_WORDS = new Set([
  "un", "una", "unos", "unas", "de", "del", "al", "en", "el", "la", "los", "las",
  "y", "e", "o", "u", "a", "por", "con", "para", "sin", "sobre", "tras", "desde",
  "hasta", "hacia", "pero", "mas", "como", "cuando", "donde", "quien", "cual", "que",
  "este", "esta", "estos", "estas", "ese", "esa", "esos", "esas", "aquel", "aquella",
  "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez",
  "mil", "millon", "millones", "primer", "primero", "segundo", "tercero",
  "cada", "todo", "toda", "todos", "todas", "otro", "otra", "otros", "otras",
  "muy", "mucho", "poco", "tanto", "tambien", "tampoco", "nada", "algo", "asi",
  "bien", "mal", "aqui", "alla", "alli", "ahora", "despues", "luego", "antes",
]);

/**
 * Normaliza un término a formato hashtag (#termino) sin tildes ni caracteres extraños.
 */
function normalizarHashtag(str) {
  if (!str) return null;
  const limpio = str
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]/g, "");

  if (!limpio || limpio.length < 3) return null;
  if (/^\d+$/.test(limpio)) return null;
  if (STOP_WORDS.has(limpio)) return null;

  return `#${limpio}`;
}

/**
 * Genera entre 6 y 12 hashtags estratégicos para YouTube combinando meta.tags,
 * palabras clave de escenas y nicho temático.
 */
function generarHashtags(meta, capitulos) {
  const tagsSet = new Set();

  // 1. Tags explícitos de metadatos
  if (Array.isArray(meta.tags)) {
    for (const t of meta.tags) {
      const h = normalizarHashtag(t);
      if (h) tagsSet.add(h);
    }
  }

  // 2. Palabras clave de escenas de todos los capítulos
  if (Array.isArray(capitulos)) {
    for (const cap of capitulos) {
      const escenas = cap.escenas || [];
      for (const esc of escenas) {
        if (Array.isArray(esc.palabrasClave)) {
          for (const kw of esc.palabrasClave) {
            const h = normalizarHashtag(kw);
            if (h && tagsSet.size < 12) {
              tagsSet.add(h);
            }
          }
        }
      }
    }
  }

  // 3. Nicho temático según categoría
  const categoria = (meta.categoria || "").toLowerCase();
  const nicho = [
    "#documental",
    "#ciencia",
    "#educacion",
    "#curiosidades",
    "#misterios",
    "#divulgacion",
    "#historia",
  ];

  for (const n of nicho) {
    if (tagsSet.size >= 10) break;
    if (!tagsSet.has(n)) {
      tagsSet.add(n);
    }
  }

  return Array.from(tagsSet).slice(0, 12);
}

function medirDuracionSegmento(rutaMp4) {
  if (!fs.existsSync(rutaMp4)) {
    return null;
  }
  const cmd = `ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "${rutaMp4}"`;
  const res = spawnSync(cmd, { shell: true, encoding: "utf-8" });
  if (res.status === 0 && res.stdout.trim()) {
    const val = parseFloat(res.stdout.trim());
    if (!isNaN(val)) return val;
  }
  return null;
}

function formatearTimestamp(segundosTotales) {
  const s = Math.floor(segundosTotales);
  const horas = Math.floor(s / 3600);
  const minutos = Math.floor((s % 3600) / 60);
  const segundos = s % 60;

  const mm = String(minutos).padStart(2, "0");
  const ss = String(segundos).padStart(2, "0");

  if (horas > 0) {
    const hh = String(horas).padStart(2, "0");
    return `${hh}:${mm}:${ss}`;
  }
  return `${mm}:${ss}`;
}

function generarCapitulosYMetadata(guionPath = GUION_PATH) {
  if (!fs.existsSync(guionPath)) {
    console.error(`[CAPÍTULOS] ❌ Guion no encontrado en ${guionPath}`);
    process.exit(1);
  }

  const guion = JSON.parse(fs.readFileSync(guionPath, "utf-8"));
  const meta = guion.meta || {};
  const capitulos = guion.capitulos || [];
  const slug = meta.slug || "video_largo";

  if (capitulos.length === 0) {
    console.error("[CAPÍTULOS] ❌ No hay capítulos en el guion.");
    process.exit(1);
  }

  console.log(`\n[CAPÍTULOS] ⏱️  Calculando marcas de tiempo a partir de segmentos reales...`);

  let tiempoAcumuladoSeg = 0.0;
  const listaCapitulos = [];

  for (let i = 0; i < capitulos.length; i++) {
    const cap = capitulos[i];
    const segPath = path.join(SEGMENTS_DIR, `capitulo_${cap.numero}.mp4`);

    let duracionSeg = medirDuracionSegmento(segPath);
    if (duracionSeg === null) {
      duracionSeg = cap.duracionSegundos || 30.0;
      console.warn(
        `[CAPÍTULOS] ⚠️ Segmento ${segPath} no encontrado en disco; usando duración estimada de guion (${duracionSeg}s).`
      );
    }

    const timestampStr = formatearTimestamp(tiempoAcumuladoSeg);

    listaCapitulos.push({
      numero: cap.numero,
      title: cap.titulo,
      timestamp: timestampStr,
      seconds: Math.round(tiempoAcumuladoSeg),
      durationSeconds: round(duracionSeg, 2),
    });

    tiempoAcumuladoSeg += duracionSeg;
  }

  // Formato para descripción de YouTube
  const lineasCapitulos = listaCapitulos.map((c) => `${c.timestamp} ${c.title}`);
  const textoCapitulos = lineasCapitulos.join("\n");

  const archivoTxt = path.join(OUT_DIR, `${slug}_capitulos.txt`);
  fs.writeFileSync(archivoTxt, textoCapitulos, "utf-8");

  // Generación enriquecida de hashtags
  const hashtags = generarHashtags(meta, capitulos);
  const hashtagsString = hashtags.join(" ");
  const tagsLimpios = hashtags.map((h) => h.replace(/^#/, ""));
  const fuentes = meta.fuentes || [];

  const descripcionCompleta = [
    meta.premisa || meta.titulo,
    "",
    "⏱️ MARCAS DE TIEMPO / CAPÍTULOS:",
    textoCapitulos,
    "",
    "🔬 FUENTES Y REFERENCIAS CIENTÍFICAS:",
    ...fuentes.map((f) => `• ${f}`),
    "",
    "🔔 ¡Suscríbete para más análisis científicos y animaciones narrativas!",
    "",
    hashtagsString,
  ].join("\n");

  const metadataJson = {
    id: meta.id,
    slug,
    title: meta.titulo,
    description: descripcionCompleta,
    chapters: listaCapitulos,
    chaptersText: textoCapitulos,
    hashtags: hashtags,
    hashtags_string: hashtagsString,
    hashtagsString: hashtagsString,
    tags: tagsLimpios,
    category: meta.categoria || "Science & Technology",
    language: meta.idioma || "es",
    aspectRatio: "16:9",
    resolution: meta.dimensiones || { width: 1920, height: 1080 },
    fps: meta.fps || 30,
    targetDurationSeconds: meta.duracionObjetivo || [480, 600],
    actualDurationSeconds: round(tiempoAcumuladoSeg, 2),
    videoFile: path.join(OUT_DIR, `${slug}.mp4`),
    generatedAt: new Date().toISOString(),
  };

  if (!fs.existsSync(OUT_DIR)) {
    fs.mkdirSync(OUT_DIR, { recursive: true });
  }

  // Exportar con ambas nomenclaturas para máxima compatibilidad
  const archivoMetadataJson = path.join(OUT_DIR, `${slug}.metadata.json`);
  const archivoDirectoJson = path.join(OUT_DIR, `${slug}.json`);

  fs.writeFileSync(archivoMetadataJson, JSON.stringify(metadataJson, null, 2), "utf-8");
  fs.writeFileSync(archivoDirectoJson, JSON.stringify(metadataJson, null, 2), "utf-8");

  console.log(`\n[CAPÍTULOS] ✅ Marcas de tiempo de YouTube generadas:`);
  console.log("--------------------------------------------------");
  console.log(textoCapitulos);
  console.log("--------------------------------------------------");
  console.log(`[CAPÍTULOS] 🏷️  Hashtags generados: ${hashtagsString}`);
  console.log(`[CAPÍTULOS] 📁 Archivo TXT: ${archivoTxt}`);
  console.log(`[CAPÍTULOS] 📁 Archivo Metadata: ${archivoMetadataJson}`);
  console.log(`[CAPÍTULOS] 📁 Archivo JSON: ${archivoDirectoJson}\n`);

  return metadataJson;
}

function round(val, dec) {
  return Number(Math.round(val + "e" + dec) + "e-" + dec);
}

if (require.main === module) {
  const customScript = process.argv[2] ? path.resolve(process.argv[2]) : GUION_PATH;
  generarCapitulosYMetadata(customScript);
}

module.exports = { generarCapitulosYMetadata, formatearTimestamp, generarHashtags, normalizarHashtag };
