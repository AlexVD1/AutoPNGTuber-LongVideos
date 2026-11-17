const fs = require("fs");
const path = require("path");
const { z } = require("zod");

const ROOT = path.resolve(__dirname, "..");
const GUION_PATH = path.join(ROOT, "src/data/guion.json");
const EJEMPLO_PATH = path.join(ROOT, "src/data/guion_ejemplo_completo.json");

// Importar esquema básico
const EscenaSchema = z.object({
  id: z.union([z.number(), z.string()]),
  texto: z.string().min(1),
  tituloVisual: z.string().optional(),
  layout: z.string().optional(),
  composicionVisual: z.string().optional(),
  escenario: z.string().optional(),
  poseId: z.string().optional(),
});

const CapituloSchema = z.object({
  id: z.union([z.number(), z.string()]),
  numero: z.number().int().positive(),
  titulo: z.string().min(1),
  escenas: z.array(EscenaSchema).min(1),
});

const GuionSchema = z.object({
  meta: z.object({
    id: z.string(),
    slug: z.string(),
    titulo: z.string(),
    duracionObjetivo: z.tuple([z.number(), z.number()]).optional(),
  }),
  capitulos: z.array(CapituloSchema).min(1),
});

function testFile(filepath, label) {
  console.log(`[TEST-SCHEMA] Verificando ${label}...`);
  if (!fs.existsSync(filepath)) {
    throw new Error(`Archivo no encontrado: ${filepath}`);
  }
  const data = JSON.parse(fs.readFileSync(filepath, "utf-8"));
  const res = GuionSchema.safeParse(data);
  if (!res.success) {
    console.error(`[TEST-SCHEMA] ❌ Error en ${label}:`, res.error.issues);
    process.exit(1);
  }
  console.log(`[TEST-SCHEMA] ✅ ${label} validado con éxito (${data.capitulos.length} capítulos).`);
}

function run() {
  testFile(GUION_PATH, "guion.json (activo)");
  testFile(EJEMPLO_PATH, "guion_ejemplo_completo.json (documental completo)");
  console.log("[TEST-SCHEMA] ✅ Todas las pruebas de esquema pasaron exitosamente.\n");
}

run();
