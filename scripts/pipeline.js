const path = require("path");
const { spawnSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");

function ejecutarPaso(nombre, comando, args = []) {
  console.log(`\n======================================================================`);
  console.log(`🚀 [PIPELINE] PASO: ${nombre.toUpperCase()}`);
  console.log(`   Comando: ${comando} ${args.join(" ")}`);
  console.log(`======================================================================\n`);

  const startTime = Date.now();
  const res = spawnSync(comando, args, {
    stdio: "inherit",
    cwd: ROOT,
  });

  if (res.status !== 0) {
    console.error(`\n[PIPELINE] ❌ Error crítico en el paso "${nombre}" (código ${res.status}). Abortando.`);
    process.exit(res.status ?? 1);
  }

  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`\n[PIPELINE] ✅ Paso "${nombre}" completado en ${elapsed}s.`);
}

function main() {
  const args = process.argv.slice(2);
  const skipTTS = args.includes("--skip-tts");
  const skipQA = args.includes("--skip-qa");
  const force = args.includes("--force");

  console.log("\n🎬 ====================================================================");
  console.log("   GENERADOR AUTÓNOMO DE VIDEOS LARGOS PARA YOUTUBE (16:9 1920x1080)");
  console.log("====================================================================\n");

  const pythonCmd = process.platform === "win32" ? "python" : "python3";
  const nodeCmd = process.execPath;

  // 1. Validar guion
  ejecutarPaso(
    "1. Validación de Guion y Recursos",
    nodeCmd,
    [path.join(__dirname, "validar_guion.js")]
  );

  // 2. TTS y alineación
  if (!skipTTS) {
    const ttsArgs = [path.join(__dirname, "tts_engine.py")];
    if (force) ttsArgs.push("--force");
    ejecutarPaso("2. Síntesis Neural de Voz y Alineación", pythonCmd, ttsArgs);
  } else {
    console.log("\n[PIPELINE] ⏩ Omitiendo síntesis TTS (--skip-tts activo).");
  }

  // 3. Renderizado de Segmentos
  const renderArgs = [path.join(__dirname, "render_segments.js")];
  if (force) renderArgs.push("--force");
  ejecutarPaso("3. Renderizado Segmentado de Capítulos (16:9)", nodeCmd, renderArgs);

  // 4. Ensamble, Mezcla Continua de BGM y Ducking
  ejecutarPaso(
    "4. Ensamble con FFmpeg, BGM y Ducking",
    pythonCmd,
    [path.join(__dirname, "assemble_video.py")]
  );

  // 5. Generar Capítulos de YouTube y Metadatos
  ejecutarPaso(
    "5. Generación de Capítulos y Metadatos de Publicación",
    nodeCmd,
    [path.join(__dirname, "generar_capitulos.js")]
  );

  // 6. Control de Calidad e Inspección
  if (!skipQA) {
    let videoFile = path.join(ROOT, "out/video_largo.mp4");
    try {
      const fs = require("fs");
      const guion = JSON.parse(fs.readFileSync(path.join(ROOT, "src/data/guion.json"), "utf-8"));
      const slug = guion?.meta?.slug;
      if (slug) videoFile = path.join(ROOT, `out/${slug}.mp4`);
    } catch {}

    ejecutarPaso(
      "6. Control de Calidad Audiovisual (QA)",
      nodeCmd,
      [path.join(__dirname, "qa_video.js"), videoFile]
    );
  }

  console.log("\n🎉 ====================================================================");
  console.log("   ¡PRODUCCIÓN COMPLETADA EXITOSAMENTE! VIDEO DISPONIBLE EN /out");
  console.log("====================================================================\n");
}

main();
