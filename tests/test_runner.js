const { spawnSync } = require("child_process");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const pythonCmd = process.platform === "win32" ? "python" : "python3";
const nodeCmd = process.execPath;

const tests = [
  { nombre: "Esquema y Validación Zod", cmd: nodeCmd, args: [path.join(__dirname, "test_schema.js")] },
  { nombre: "Marcas de Tiempo YouTube", cmd: nodeCmd, args: [path.join(__dirname, "test_timestamps.js")] },
  { nombre: "Síntesis TTS y WordBoundary", cmd: pythonCmd, args: [path.join(__dirname, "test_tts.py")] },
];

console.log("\n=======================================================");
console.log("🧪 EJECUTANDO SUITE DE PRUEBAS AUTOMATIZADAS");
console.log("=======================================================\n");

let passed = 0;
let failed = 0;

for (const t of tests) {
  console.log(`▶ Ejecutando: ${t.nombre}...`);
  const res = spawnSync(t.cmd, t.args, { stdio: "inherit", cwd: ROOT });
  if (res.status === 0) {
    passed++;
  } else {
    failed++;
    console.error(`❌ Falló la prueba: ${t.nombre}`);
  }
}

console.log("\n=======================================================");
console.log(`📊 RESULTADOS: ${passed} Pasadas | ${failed} Fallidas`);
console.log("=======================================================\n");

if (failed > 0) {
  process.exit(1);
}
console.log("🎉 ¡Todas las pruebas automatizadas pasaron con éxito!\n");
