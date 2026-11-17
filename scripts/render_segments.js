const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const { spawnSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const GUION_PATH = path.join(ROOT, "src/data/guion.json");
const SEGMENTS_DIR = path.join(ROOT, "out/segments");
const SEGMENTS_META_PATH = path.join(SEGMENTS_DIR, ".segments_meta.json");

function calcularFirmaCapitulo(slug, cap) {
  return crypto
    .createHash("sha256")
    .update(JSON.stringify({ slug: slug || "video_largo", cap }))
    .digest("hex");
}

function cargarMetaSegmentos() {
  if (!fs.existsSync(SEGMENTS_META_PATH)) return { slug: null, chapters: {} };
  try {
    return JSON.parse(fs.readFileSync(SEGMENTS_META_PATH, "utf-8"));
  } catch {
    return { slug: null, chapters: {} };
  }
}

function guardarMetaSegmentos(meta) {
  fs.mkdirSync(SEGMENTS_DIR, { recursive: true });
  fs.writeFileSync(SEGMENTS_META_PATH, JSON.stringify(meta, null, 2), "utf-8");
}

function verificarSegmentoValido(rutaMp4, duracionEsperadaSeg) {
  if (!fs.existsSync(rutaMp4)) return false;
  try {
    const stats = fs.statSync(rutaMp4);
    if (stats.size < 50000) return false; // Menos de 50KB es inválido
    if (duracionEsperadaSeg && duracionEsperadaSeg > 0) {
      const cmd = `ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "${rutaMp4}"`;
      const res = spawnSync(cmd, { shell: true, encoding: "utf-8" });
      if (res.status === 0 && res.stdout.trim()) {
        const durReal = parseFloat(res.stdout.trim());
        if (!isNaN(durReal) && Math.abs(durReal - duracionEsperadaSeg) > 1.5) {
          return false;
        }
      }
    }
    return true;
  } catch {
    return false;
  }
}

function main() {
  const args = process.argv.slice(2);
  let targetChapter = null;
  let force = false;
  let port = "3004";

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if (arg === "--force") force = true;
    else if (arg.startsWith("--chapter=")) targetChapter = parseInt(arg.split("=")[1], 10);
    else if (arg === "--chapter" && args[i + 1]) targetChapter = parseInt(args[++i], 10);
    else if (arg.startsWith("--port=")) port = arg.split("=")[1];
    else if (arg === "--port" && args[i + 1]) port = args[++i];
  }

  if (!fs.existsSync(GUION_PATH)) {
    console.error(`[RENDER] ❌ No existe el guion en ${GUION_PATH}`);
    process.exit(1);
  }

  const guion = JSON.parse(fs.readFileSync(GUION_PATH, "utf-8"));
  const capitulos = guion.capitulos || [];

  if (capitulos.length === 0) {
    console.error("[RENDER] ❌ El guion no contiene capítulos.");
    process.exit(1);
  }

  fs.mkdirSync(SEGMENTS_DIR, { recursive: true });

  const slug = guion.meta?.slug || "video_largo";
  let metaSegmentos = cargarMetaSegmentos();
  const numerosValidos = new Set(capitulos.map((c) => c.numero));

  // Si cambió de episodio (slug distinto) o hay capítulos sobrantes de un episodio anterior, purgar MP4 obsoletos
  if (targetChapter === null) {
    if (metaSegmentos.slug && metaSegmentos.slug !== slug) {
      console.log(`[RENDER] 🔄 Nuevo episodio detectado (${metaSegmentos.slug} -> ${slug}). Purgando segmentos anteriores...`);
      for (const file of fs.readdirSync(SEGMENTS_DIR)) {
        if (/^capitulo_\d+\.mp4$/i.test(file)) {
          fs.unlinkSync(path.join(SEGMENTS_DIR, file));
        }
      }
      metaSegmentos = { slug, chapters: {} };
    } else {
      for (const file of fs.readdirSync(SEGMENTS_DIR)) {
        const m = file.match(/^capitulo_(\d+)\.mp4$/i);
        if (m && !numerosValidos.has(parseInt(m[1], 10))) {
          fs.unlinkSync(path.join(SEGMENTS_DIR, file));
        }
      }
      metaSegmentos.slug = slug;
    }
    guardarMetaSegmentos(metaSegmentos);
  }

  console.log(`\n[RENDER] 🎬 Iniciando renderizado segmentado en 16:9 (1920x1080 @ 30fps)`);
  console.log(`[RENDER] 📁 Directorio de segmentos: ${SEGMENTS_DIR}\n`);

  let renderizados = 0;
  let reutilizados = 0;

  for (const cap of capitulos) {
    const num = cap.numero;
    if (targetChapter !== null && num !== targetChapter) {
      continue;
    }

    const compositionId = `Capitulo-${num}`;
    const salidaMp4 = path.join(SEGMENTS_DIR, `capitulo_${num}.mp4`);
    const rutaRelativa = path.relative(ROOT, salidaMp4).replace(/\\/g, "/");
    const firmaCap = calcularFirmaCapitulo(slug, cap);

    const yaExiste =
      !force &&
      metaSegmentos.slug === slug &&
      metaSegmentos.chapters?.[num] === firmaCap &&
      verificarSegmentoValido(salidaMp4, cap.duracionSegundos);

    if (yaExiste) {
      console.log(`[RENDER] ⚡ Capítulo ${num}: "${cap.titulo}" ya existe y coincide con el guion actual. Omitiendo.`);
      reutilizados++;
      continue;
    }

    console.log(`[RENDER] 🎥 Renderizando Capítulo ${num}: "${cap.titulo}"...`);
    const startTime = Date.now();

    // Puerto dinámico y concurrencia controlada para evitar net::ERR_NO_BUFFER_SPACE en Windows
    const chapterPort = parseInt(port, 10) + ((num * 13) % 2000) + Math.floor(Math.random() * 20);
    const comando = `npx remotion render ${compositionId} "${rutaRelativa}" --port ${chapterPort} --concurrency=4`.trim();

    let resultado = spawnSync(comando, {
      shell: true,
      stdio: "inherit",
      cwd: ROOT,
    });

    if (resultado.status !== 0) {
      console.warn(`\n[RENDER] ⚠️ Primer intento falló para Capítulo ${num}. Esperando 3s y reintentando con puerto alterno...`);
      const retryWait = (ms) => {
        const end = Date.now() + ms;
        while (Date.now() < end) {}
      };
      retryWait(3000);
      const retryPort = chapterPort + 50 + Math.floor(Math.random() * 50);
      const retryCmd = `npx remotion render ${compositionId} "${rutaRelativa}" --port ${retryPort} --concurrency=2`.trim();
      resultado = spawnSync(retryCmd, {
        shell: true,
        stdio: "inherit",
        cwd: ROOT,
      });
    }

    if (resultado.status !== 0) {
      console.error(`\n[RENDER] ❌ Falló el render del Capítulo ${num} tras reintento (código ${resultado.status}).`);
      process.exit(resultado.status ?? 1);
    }

    const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
    console.log(`[RENDER] ✅ Capítulo ${num} renderizado con éxito en ${elapsed}s.\n`);
    metaSegmentos.slug = slug;
    metaSegmentos.chapters = metaSegmentos.chapters || {};
    metaSegmentos.chapters[num] = firmaCap;
    guardarMetaSegmentos(metaSegmentos);
    renderizados++;

    // Pausa preventiva de 1.5s para liberar sockets en Windows
    const pauseEnd = Date.now() + 1500;
    while (Date.now() < pauseEnd) {}
  }

  console.log(`[RENDER] 🏁 Renderizado de segmentos concluido: ${renderizados} procesados, ${reutilizados} reutilizados.\n`);
}

main();
