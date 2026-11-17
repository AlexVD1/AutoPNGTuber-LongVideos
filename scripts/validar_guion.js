const fs = require("fs");
const path = require("path");
const { z } = require("zod");

const ROOT = path.resolve(__dirname, "..");
const GUION_PATH = path.join(ROOT, "src/data/guion.json");
const POSES_PATH = path.join(ROOT, "src/data/poses.json");

// Cargar catálogo de poses
let catalogo = [];
if (fs.existsSync(POSES_PATH)) {
  try {
    catalogo = JSON.parse(fs.readFileSync(POSES_PATH, "utf-8")).recursos || [];
  } catch (e) {
    console.warn(`[VALIDAR] ⚠️ No se pudo leer poses.json: ${e.message}`);
  }
}

const POSES = new Set(catalogo.map((r) => r.id));
const EXPRESIONES = new Set(
  catalogo
    .filter((r) => r.categoria === "expresiones")
    .flatMap((r) => [r.id, r.id.replace(/^expr_/, "")])
);
const PROPS = new Set(
  catalogo
    .filter((r) => r.categoria === "props" || r.categoria === "props_festivos")
    .flatMap((r) => [r.id, r.id.replace(/^prop_/, "")])
);

// Esquema Zod
const PalabraSchema = z.object({
  palabra: z.string(),
  inicioMs: z.number().min(0),
  finMs: z.number().min(0),
});

const EscenaSchema = z.object({
  id: z.union([z.number(), z.string()]),
  texto: z.string().min(1, "El texto no puede estar vacío"),
  tituloVisual: z.string().optional(),
  layout: z.string().optional(),
  composicionVisual: z.string().optional(),
  escenario: z.string().optional(),
  poseId: z.string().optional(),
  expresion: z.string().optional(),
  prop: z.string().optional(),
  sfx: z.string().optional(),
  volumenSfx: z.number().min(0).max(1).optional(),
  duracionSegundos: z.number().positive().optional(),
  palabras: z.array(PalabraSchema).optional(),
  personajes: z.array(z.any()).optional(),
  objetos: z.array(z.any()).optional(),
  infografia: z.any().optional(),
  eventosSfx: z.array(z.any()).optional(),
}).passthrough();

const CapituloSchema = z.object({
  id: z.union([z.number(), z.string()]),
  numero: z.number().int().positive(),
  titulo: z.string().min(1, "Título de capítulo requerido"),
  resumen: z.string().optional(),
  escenas: z.array(EscenaSchema).min(1, "Capítulo debe tener al menos una escena"),
  duracionSegundos: z.number().optional(),
});

const GuionSchema = z.object({
  meta: z.object({
    id: z.string().min(1),
    slug: z.string().min(1),
    titulo: z.string().min(1),
    duracionObjetivo: z.tuple([z.number().positive(), z.number().positive()]).optional(),
    voz: z.string().optional(),
    fuentes: z.array(z.string()).optional(),
  }),
  capitulos: z.array(CapituloSchema).min(1, "Debe tener al menos un capítulo"),
});

function main() {
  console.log("\n[VALIDAR] 🔍 Verificando integridad del guion...");
  if (!fs.existsSync(GUION_PATH)) {
    console.error(`[VALIDAR] ❌ No se encontró el archivo: ${GUION_PATH}`);
    process.exit(1);
  }

  let raw;
  try {
    raw = JSON.parse(fs.readFileSync(GUION_PATH, "utf-8"));
  } catch (e) {
    console.error(`[VALIDAR] ❌ Error sintáctico en JSON: ${e.message}`);
    process.exit(1);
  }

  const parseResult = GuionSchema.safeParse(raw);
  if (!parseResult.success) {
    console.error("\n[VALIDAR] ❌ Errores en la estructura del guion:");
    for (const issue of parseResult.error.issues) {
      console.error(`  - [${issue.path.join(".")}] ${issue.message}`);
    }
    process.exit(1);
  }

  const guion = parseResult.data;
  const errores = [];
  const avisos = [];

  // Validaciones semánticas de catálogo y recursos
  let escenaCount = 0;
  for (const cap of guion.capitulos) {
    for (const esc of cap.escenas) {
      escenaCount++;
      const tag = `Cap ${cap.numero} - Esc ${esc.id}`;

      // Verificar poses
      if (esc.poseId && !POSES.has(esc.poseId)) {
        avisos.push(`${tag}: poseId "${esc.poseId}" no está en poses.json (se usará fallback suave)`);
      }
      if (esc.expresion && !EXPRESIONES.has(esc.expresion)) {
        avisos.push(`${tag}: expresión "${esc.expresion}" no encontrada en catálogo`);
      }
      if (esc.prop && esc.prop.startsWith("lucide:")) {
        errores.push(`${tag}: prop "${esc.prop}" usa prefijo prohibido "lucide:"`);
      } else if (esc.prop && !PROPS.has(esc.prop) && !esc.prop.startsWith("svg:") && !esc.prop.startsWith("<")) {
        avisos.push(`${tag}: prop "${esc.prop}" no encontrado en poses.json (verificar en propsLibrary.ts)`);
      }

      if (Array.isArray(esc.personajes)) {
        for (const p of esc.personajes) {
          if (p?.prop && String(p.prop).startsWith("lucide:")) {
            errores.push(`${tag}: personaje "${p.id}" usa prop prohibido "${p.prop}"`);
          }
          if (p?.props && typeof p.props === "object") {
            for (const val of Object.values(p.props)) {
              if (typeof val === "string" && val.startsWith("lucide:")) {
                errores.push(`${tag}: personaje "${p.id}" usa prop prohibido "${val}"`);
              }
            }
          }
        }
      }

      if (Array.isArray(esc.objetos)) {
        for (const obj of esc.objetos) {
          if (obj?.propId && String(obj.propId).startsWith("lucide:")) {
            errores.push(`${tag}: objeto "${obj.id}" usa propId prohibido "${obj.propId}"`);
          }
        }
      }

      // Verificar SFX en disco si fue especificado
      if (esc.sfx) {
        const sfxFile = path.join(ROOT, "public", esc.sfx);
        if (!fs.existsSync(sfxFile)) {
          avisos.push(`${tag}: archivo SFX "${esc.sfx}" no existe en public/`);
        }
      }
      if (Array.isArray(esc.eventosSfx)) {
        for (const ev of esc.eventosSfx) {
          if (ev && ev.sfx) {
            const evFile = path.join(ROOT, "public", ev.sfx);
            if (!fs.existsSync(evFile)) {
              avisos.push(`${tag}: archivo eventosSfx "${ev.sfx}" no existe en public/`);
            }
          }
        }
      }

      // Verificación de cifras numéricas para dicción fonética óptima
      if (/\b\d+\b/.test(esc.texto) || /\b(MHz|GHz|kHz|km\/h)\b/i.test(esc.texto)) {
        avisos.push(`${tag}: 🗣️ Contiene cifras numéricas o abreviaturas en el texto narrado. El normalizador fonético (scripts/normalizador_numeros.py) las expandirá a palabras en español para asegurar una dicción natural y perfecta en el TTS.`);
      }
    }
  }

  // Reporte final
  console.log(`[VALIDAR] 📋 Capítulos: ${guion.capitulos.length} | Escenas: ${escenaCount}`);
  if (avisos.length > 0) {
    console.log("\n[VALIDAR] ⚠️ Advertencias encontradas:");
    avisos.forEach((a) => console.log(`  - ${a}`));
  }

  if (errores.length > 0) {
    console.error("\n[VALIDAR] ❌ Errores críticos:");
    errores.forEach((e) => console.error(`  - ${e}`));
    process.exit(1);
  }

  console.log("[VALIDAR] ✅ Guion 100% válido y listo para producción.\n");
}

main();
