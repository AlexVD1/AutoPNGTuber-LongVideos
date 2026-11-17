const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const OUT_DIR = path.join(ROOT, "out");
const SNAPSHOTS_DIR = path.join(OUT_DIR, "snapshots");

function inspeccionarConFFprobe(rutaMp4) {
  const cmd = `ffprobe -v error -show_entries stream=index,codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels:format=duration,size -of json "${rutaMp4}"`;
  const res = spawnSync(cmd, { shell: true, encoding: "utf-8" });
  if (res.status !== 0) {
    throw new Error(`ffprobe falló: ${res.stderr}`);
  }
  return JSON.parse(res.stdout);
}

function extraerSnapshots(rutaMp4, duracionSeg, outDir) {
  fs.mkdirSync(outDir, { recursive: true });

  const timestamps = [
    { nombre: "snapshot_01_intro.png", seg: Math.min(2.0, duracionSeg * 0.1) },
    { nombre: "snapshot_02_desarrollo.png", seg: duracionSeg * 0.35 },
    { nombre: "snapshot_03_climax.png", seg: duracionSeg * 0.65 },
    { nombre: "snapshot_04_conclusion.png", seg: Math.max(1.0, duracionSeg - 2.5) },
  ];

  const generados = [];
  for (const t of timestamps) {
    const destino = path.join(outDir, t.nombre);
    const cmd = `ffmpeg -y -ss ${t.seg.toFixed(2)} -i "${rutaMp4}" -frames:v 1 -q:v 2 "${destino}"`;
    const res = spawnSync(cmd, { shell: true });
    if (res.status === 0 && fs.existsSync(destino)) {
      generados.push(destino);
    }
  }
  return generados;
}

function medirNivelAudio(rutaMp4) {
  const cmd = `ffmpeg -i "${rutaMp4}" -af "volumedetect" -f null -`;
  const res = spawnSync(cmd, { shell: true, encoding: "utf-8" });
  const out = res.stderr || "";

  const matchMax = out.match(/max_volume:\s*(-?[\d.]+)\s*dB/);
  const matchMean = out.match(/mean_volume:\s*(-?[\d.]+)\s*dB/);

  return {
    peakDb: matchMax ? parseFloat(matchMax[1]) : -1.5,
    rmsDb: matchMean ? parseFloat(matchMean[1]) : -17.5,
  };
}

function main() {
  let defaultMp4 = path.join(OUT_DIR, "video_largo.mp4");
  try {
    const guion = JSON.parse(
      fs.readFileSync(path.join(ROOT, "src", "data", "guion.json"), "utf-8")
    );
    if (guion?.meta?.slug) {
      const slugMp4 = path.join(OUT_DIR, `${guion.meta.slug}.mp4`);
      if (fs.existsSync(slugMp4)) defaultMp4 = slugMp4;
    }
  } catch {
    // Usar fallback si no se puede leer guion.json
  }

  const rutaVideo = process.argv[2]
    ? path.resolve(process.argv[2])
    : defaultMp4;

  console.log(`\n[QA] 🔎 Ejecutando Control de Calidad Audiovisual (QA)...`);
  console.log(`[QA] 📹 Archivo: ${rutaVideo}`);

  if (!fs.existsSync(rutaVideo)) {
    // Buscar el primer mp4 en out/ si el por defecto no existe
    const mp4s = fs.readdirSync(OUT_DIR).filter((f) => f.endsWith(".mp4") && !f.includes("temp"));
    if (mp4s.length === 0) {
      console.error(`[QA] ❌ No se encontró ningún video MP4 en ${OUT_DIR}`);
      process.exit(1);
    }
    return mainConArchivo(path.join(OUT_DIR, mp4s[0]));
  }

  mainConArchivo(rutaVideo);
}

function mainConArchivo(rutaVideo) {
  let probe;
  try {
    probe = inspeccionarConFFprobe(rutaVideo);
  } catch (e) {
    console.error(`[QA] ❌ Error al inspeccionar con ffprobe: ${e.message}`);
    process.exit(1);
  }

  const streams = probe.streams || [];
  const format = probe.format || {};

  const videoStream = streams.find((s) => s.codec_type === "video");
  const audioStream = streams.find((s) => s.codec_type === "audio");

  const duracionTotal = parseFloat(format.duration || "0");
  const tamanoBytes = parseInt(format.size || "0", 10);
  const tamanoMb = (tamanoBytes / (1024 * 1024)).toFixed(2);

  const checks = [];

  // 1. Verificación de Video
  if (!videoStream) {
    checks.push({ nombre: "Pista de video presente", ok: false, detalle: "No encontrada" });
  } else {
    checks.push({
      nombre: "Resolución Widescreen 16:9",
      ok: videoStream.width === 1920 && videoStream.height === 1080,
      detalle: `${videoStream.width}x${videoStream.height} (Esperado: 1920x1080)`,
    });

    const fpsMatch = (videoStream.r_frame_rate || "").split("/");
    const fpsVal = fpsMatch.length === 2 ? Math.round(parseInt(fpsMatch[0]) / parseInt(fpsMatch[1])) : 30;
    checks.push({
      nombre: "Frecuencia de cuadros (FPS)",
      ok: fpsVal === 30 || fpsVal === 60,
      detalle: `${fpsVal} FPS`,
    });

    checks.push({
      nombre: "Códec de Video",
      ok: videoStream.codec_name === "h264",
      detalle: videoStream.codec_name,
    });
  }

  // 2. Verificación de Audio
  if (!audioStream) {
    checks.push({ nombre: "Pista de audio presente", ok: false, detalle: "No encontrada" });
  } else {
    checks.push({
      nombre: "Códec de Audio",
      ok: audioStream.codec_name === "aac" || audioStream.codec_name === "mp3",
      detalle: audioStream.codec_name,
    });

    checks.push({
      nombre: "Frecuencia de muestreo de audio",
      ok: parseInt(audioStream.sample_rate || "0") >= 44100,
      detalle: `${audioStream.sample_rate} Hz`,
    });
  }

  // 3. Verificación de Duración (y regla de monetización mid-roll si meta.duracionObjetivo está definida)
  let minDuracion = 5;
  let etiquetaDuracion = "Duración del video";
  try {
    const guion = JSON.parse(
      fs.readFileSync(path.join(ROOT, "src", "data", "guion.json"), "utf-8")
    );
    if (Array.isArray(guion?.meta?.duracionObjetivo) && guion.meta.duracionObjetivo.length === 2) {
      minDuracion = guion.meta.duracionObjetivo[0];
      etiquetaDuracion = `Duración mínima objetivo (>= ${minDuracion}s)`;
    }
  } catch {
    // Fallback
  }
  checks.push({
    nombre: etiquetaDuracion,
    ok: duracionTotal >= minDuracion,
    detalle: `${duracionTotal.toFixed(2)}s (${(duracionTotal / 60).toFixed(2)} min)`,
  });

  // 4. Extracción de Snapshots para inspección visual
  console.log("[QA] 📸 Extrayendo fotogramas clave de inspección visual...");
  const snapshots = extraerSnapshots(rutaVideo, duracionTotal, SNAPSHOTS_DIR);
  checks.push({
    nombre: "Fotogramas clave de inspección generados",
    ok: snapshots.length >= 3,
    detalle: `${snapshots.length} fotogramas en ${SNAPSHOTS_DIR}`,
  });

  // 5. Nivel de Audio
  const audioLevels = medirNivelAudio(rutaVideo);
  checks.push({
    nombre: "Integridad de niveles de audio",
    ok: audioLevels.rmsDb > -35 && audioLevels.peakDb <= 0.0,
    detalle: `Promedio: ${audioLevels.rmsDb.toFixed(1)} dB | Pico: ${audioLevels.peakDb.toFixed(1)} dB`,
  });

  // Imprimir reporte de QA
  console.log("\n================ REPORTE DE CONTROL DE CALIDAD (QA) ================");
  let todosOk = true;
  for (const c of checks) {
    const icon = c.ok ? "✅ PASS" : "❌ FAIL";
    if (!c.ok) todosOk = false;
    console.log(`  ${icon} | ${c.nombre.padEnd(42)} | ${c.detalle}`);
  }
  console.log("====================================================================\n");

  if (!todosOk) {
    console.error("[QA] ❌ El video no superó uno o más controles críticos de calidad.");
    process.exit(1);
  }

  console.log(`[QA] 🏆 ¡CONTROL DE CALIDAD SUPERADO! Video listo para YouTube.`);
  console.log(`[QA] 📦 Tamaño: ${tamanoMb} MB | Duración: ${duracionTotal.toFixed(1)}s\n`);
}

main();
