import posesCatalog from "../data/poses.json";

export interface RecursoCatalogo {
  id: string;
  nombre: string;
  categoria:
    | "base"
    | "emociones"
    | "acciones"
    | "expresiones"
    | "props"
    | "props_festivos"
    | "compuestas"
    | "compuestas_festivas";
  subcategoria?: string;
  festividad?: string;
  temporada?: string;
  paisCompatible?: string[];
  emocion: string;
  accion: string;
  propsAsociados: string[];
  ruta: string;
  formato: string;
  etiquetas: string[];
  compatibleComposicion: boolean;
}

export interface FiltroCatalogo {
  categoria?: RecursoCatalogo["categoria"];
  subcategoria?: string;
  festividad?: string;
  temporada?: string;
  pais?: string;
  emocion?: string;
  accion?: string;
  prop?: string;
  tema?: string;
}

const recursos = posesCatalog.recursos as RecursoCatalogo[];

export function obtenerRecursoPorId(id: string): RecursoCatalogo | undefined {
  return recursos.find((r) => r.id === id);
}

export function buscarRecursos(filtro: FiltroCatalogo): RecursoCatalogo[] {
  return recursos.filter((r) => {
    if (filtro.categoria && r.categoria !== filtro.categoria) return false;
    if (
      filtro.subcategoria &&
      r.subcategoria?.toLowerCase() !== filtro.subcategoria.toLowerCase()
    ) {
      return false;
    }
    if (
      filtro.festividad &&
      r.festividad?.toLowerCase() !== filtro.festividad.toLowerCase()
    ) {
      return false;
    }
    if (
      filtro.temporada &&
      r.temporada?.toLowerCase() !== filtro.temporada.toLowerCase()
    ) {
      return false;
    }
    if (
      filtro.pais &&
      r.paisCompatible &&
      !r.paisCompatible.some(
        (p) => p.toLowerCase() === filtro.pais!.toLowerCase()
      )
    ) {
      return false;
    }
    if (
      filtro.emocion &&
      r.emocion.toLowerCase() !== filtro.emocion.toLowerCase()
    ) {
      return false;
    }
    if (
      filtro.accion &&
      r.accion.toLowerCase() !== filtro.accion.toLowerCase()
    ) {
      return false;
    }
    if (
      filtro.prop &&
      !r.propsAsociados.some(
        (p) => p.toLowerCase() === filtro.prop!.toLowerCase()
      )
    ) {
      return false;
    }
    if (filtro.tema) {
      const q = filtro.tema.toLowerCase();
      const coincide =
        r.id.toLowerCase().includes(q) ||
        r.nombre.toLowerCase().includes(q) ||
        r.etiquetas.some((t) => t.toLowerCase().includes(q));
      if (!coincide) return false;
    }
    return true;
  });
}
