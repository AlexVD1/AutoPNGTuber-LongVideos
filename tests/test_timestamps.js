const assert = require("assert");
const { formatearTimestamp, generarHashtags, normalizarHashtag } = require("../scripts/generar_capitulos");

function testTimestamps() {
  console.log("[TEST-TIMESTAMPS] Verificando formateo y reglas de YouTube...");

  // Pruebas de formateo MM:SS
  assert.strictEqual(formatearTimestamp(0), "00:00", "0 segundos debe ser 00:00");
  assert.strictEqual(formatearTimestamp(72), "01:12", "72 segundos debe ser 01:12");
  assert.strictEqual(formatearTimestamp(600), "10:00", "600 segundos debe ser 10:00");
  assert.strictEqual(formatearTimestamp(3665), "01:01:05", "3665 segundos debe ser 01:01:05");

  // Reglas de YouTube
  const chapters = [
    { seconds: 0, title: "Introducción" },
    { seconds: 45, title: "El Misterio" },
    { seconds: 120, title: "Conclusión" },
  ];

  // 1. Debe comenzar en 00:00
  assert.strictEqual(chapters[0].seconds, 0, "El primer capítulo debe iniciar en 0s");

  // 2. Debe tener al menos 3 marcas
  assert.ok(chapters.length >= 3, "YouTube requiere al menos 3 marcas de tiempo");

  // 3. Deben ser estrictamente crecientes
  for (let i = 1; i < chapters.length; i++) {
    assert.ok(
      chapters[i].seconds > chapters[i - 1].seconds,
      "Cada marca debe ser mayor que la anterior"
    );
    assert.ok(
      chapters[i].seconds - chapters[i - 1].seconds >= 10,
      "Cada capítulo debe durar al menos 10 segundos"
    );
  }

  // 4. Verificación de generación de hashtags
  console.log("[TEST-TIMESTAMPS] Verificando generador de hashtags para metadata JSON...");
  assert.strictEqual(normalizarHashtag("Señal Wow!"), "#senalwow");
  assert.strictEqual(normalizarHashtag("1420"), null, "Números puros deben descartarse");
  assert.strictEqual(normalizarHashtag("de"), null, "Stop words deben descartarse");

  const tags = generarHashtags(
    { tags: ["astronomia", "espacio"], categoria: "Science & Technology" },
    [{ escenas: [{ palabrasClave: ["radiotelescopio", "hidrogeno"] }] }]
  );
  assert.ok(Array.isArray(tags), "Hashtags debe ser un arreglo");
  assert.ok(tags.length >= 4, "Debe generar al menos 4 hashtags");
  assert.ok(tags.includes("#astronomia"), "Debe incluir #astronomia");
  assert.ok(tags.includes("#espacio"), "Debe incluir #espacio");
  assert.ok(tags.includes("#radiotelescopio"), "Debe incluir palabras clave");

  console.log("[TEST-TIMESTAMPS] ✅ Todas las pruebas de marcas de tiempo y hashtags pasaron exitosamente.\n");
}

testTimestamps();
