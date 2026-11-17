import { SkeletalPose } from "./skeletalRig";

export type TipoRopaTorso =
  | "ninguna"
  | "sudadera"
  | "chaqueta"
  | "abrigo"
  | "vestido"
  | "camisa"
  | "bata"
  | "chaleco"
  | "manto_real";

export type TipoPeinado =
  | "ninguno"
  | "corto_clasico"
  | "mono_alto"
  | "coleta"
  | "melena_bob"
  | "canoso_anciano"
  | "canoso_mono"
  | "nino_despeinado";

export type TipoAccesorioCabeza =
  | "ninguno"
  | "gorra"
  | "gorra_atras"
  | "gorro_beanie"
  | "gafas_redondas"
  | "gafas_pasta"
  | "corona"
  | "gorra_aviador";

export type ArquetipoStickman =
  | "protagonista"
  | "nino"
  | "nina"
  | "adulto_m"
  | "adulto_f"
  | "anciano"
  | "anciana"
  | "rey"
  | "cientifico";

export interface ConfiguracionVestuario {
  arquetipo?: ArquetipoStickman;
  ropaTorso?: TipoRopaTorso;
  colorTorso?: string;
  colorSecundarioTorso?: string;
  colorPantalones?: string;
  colorZapatos?: string;
  peinado?: TipoPeinado;
  colorPelo?: string;
  accesorioCabeza?: TipoAccesorioCabeza;
  colorAccesorio?: string;
  escalaRecomendada?: number;
}

export const PRESETS_ARQUETIPOS: Record<ArquetipoStickman, ConfiguracionVestuario> = {
  protagonista: {
    arquetipo: "protagonista",
    ropaTorso: "sudadera",
    colorTorso: "#FFFFFF",
    colorSecundarioTorso: "#E2E8F0",
    colorPantalones: "#1E293B",
    colorZapatos: "#F8FAFC",
    peinado: "ninguno",
    accesorioCabeza: "ninguno",
    escalaRecomendada: 1.0,
  },
  nino: {
    arquetipo: "nino",
    ropaTorso: "sudadera",
    colorTorso: "#EA580C", // Naranja vibrante
    colorSecundarioTorso: "#C2410C",
    colorPantalones: "#0284C7", // Jeans azul
    colorZapatos: "#FFFFFF",
    peinado: "nino_despeinado",
    colorPelo: "#1E293B",
    accesorioCabeza: "gorra",
    colorAccesorio: "#DC2626", // Gorra roja
    escalaRecomendada: 0.75,
  },
  nina: {
    arquetipo: "nina",
    ropaTorso: "sudadera",
    colorTorso: "#0D9488", // Teal/Verde azulado
    colorSecundarioTorso: "#0F766E",
    colorPantalones: "#F43F5E", // Rosa/magenta
    colorZapatos: "#FFFFFF",
    peinado: "coleta",
    colorPelo: "#1E293B",
    accesorioCabeza: "ninguno",
    escalaRecomendada: 0.74,
  },
  adulto_m: {
    arquetipo: "adulto_m",
    ropaTorso: "chaqueta",
    colorTorso: "#D97706", // Mostaza/camel cálido
    colorSecundarioTorso: "#FFFFFF", // Camiseta blanca debajo
    colorPantalones: "#334155", // Pantalón oscuro
    colorZapatos: "#78350F", // Calzado marrón cuero
    peinado: "corto_clasico",
    colorPelo: "#1E293B",
    accesorioCabeza: "ninguno",
    escalaRecomendada: 1.02,
  },
  adulto_f: {
    arquetipo: "adulto_f",
    ropaTorso: "vestido",
    colorTorso: "#7C3AED", // Púrpura elegante
    colorSecundarioTorso: "#6D28D9",
    colorPantalones: "transparent",
    colorZapatos: "#1E1B4B",
    peinado: "mono_alto",
    colorPelo: "#1E293B",
    accesorioCabeza: "ninguno",
    escalaRecomendada: 0.98,
  },
  anciano: {
    arquetipo: "anciano",
    ropaTorso: "chaleco",
    colorTorso: "#4B5563", // Chaleco gris/carbón
    colorSecundarioTorso: "#F3F4F6", // Camisa clara
    colorPantalones: "#1F2937",
    colorZapatos: "#374151",
    peinado: "canoso_anciano",
    colorPelo: "#E2E8F0", // Blanco canoso
    accesorioCabeza: "gafas_redondas",
    colorAccesorio: "#D97706", // Montura carey/dorada
    escalaRecomendada: 0.95,
  },
  anciana: {
    arquetipo: "anciana",
    ropaTorso: "abrigo",
    colorTorso: "#047857", // Verde bosque sobrio
    colorSecundarioTorso: "#D1FAE5",
    colorPantalones: "#064E3B",
    colorZapatos: "#1F2937",
    peinado: "canoso_mono",
    colorPelo: "#E2E8F0",
    accesorioCabeza: "gafas_redondas",
    colorAccesorio: "#94A3B8",
    escalaRecomendada: 0.93,
  },
  rey: {
    arquetipo: "rey",
    ropaTorso: "manto_real",
    colorTorso: "#581C87", // Púrpura regio
    colorSecundarioTorso: "#FDE047", // Broche oro
    colorPantalones: "#1E1B4B",
    colorZapatos: "#B45309",
    peinado: "corto_clasico",
    colorPelo: "#1E293B",
    accesorioCabeza: "corona",
    colorAccesorio: "#EAB308", // Corona dorada
    escalaRecomendada: 1.05,
  },
  cientifico: {
    arquetipo: "cientifico",
    ropaTorso: "bata",
    colorTorso: "#F8FAFC", // Blanco puro
    colorSecundarioTorso: "#0284C7", // Cuello azul
    colorPantalones: "#334155",
    colorZapatos: "#0F172A",
    peinado: "corto_clasico",
    colorPelo: "#334155",
    accesorioCabeza: "gafas_pasta",
    colorAccesorio: "#0284C7",
    escalaRecomendada: 1.0,
  },
};

/**
 * Resuelve la configuración final combinando el arquetipo base con overrides específicos.
 */
export function resolverVestuario(
  arquetipo?: ArquetipoStickman,
  overrides?: Partial<ConfiguracionVestuario>
): ConfiguracionVestuario {
  const base = arquetipo && PRESETS_ARQUETIPOS[arquetipo]
    ? { ...PRESETS_ARQUETIPOS[arquetipo] }
    : { ...PRESETS_ARQUETIPOS.protagonista };

  return {
    ...base,
    ...overrides,
    ropaTorso: overrides?.ropaTorso ?? base.ropaTorso ?? "sudadera",
    colorTorso: overrides?.colorTorso ?? base.colorTorso ?? "#FFFFFF",
    peinado: overrides?.peinado ?? base.peinado ?? "ninguno",
    accesorioCabeza: overrides?.accesorioCabeza ?? base.accesorioCabeza ?? "ninguno",
  };
}

/**
 * Genera el SVG del vestuario corporal (torso, abrigo/vestido, piernas y zapatos)
 * anclado a la cinemática del esqueleto.
 */
export function renderizarRopaCuerpo(
  skel: SkeletalPose,
  vestuario: ConfiguracionVestuario,
  strokeColor: string = "#111827"
): string {
  const { ropaTorso, colorTorso, colorSecundarioTorso, colorPantalones, colorZapatos } = vestuario;
  if (!ropaTorso || ropaTorso === "ninguna") return "";

  const n = skel.torso[0]; // Cuello / hombros
  const m = skel.torso[1]; // Mitad torso / pecho
  const p = skel.torso[2]; // Pelvis / cintura
  const lKnee = skel.leftLeg[1];
  const rKnee = skel.rightLeg[1];
  const lFoot = skel.leftLeg[2];
  const rFoot = skel.rightLeg[2];

  let cuerpoSvg = "";

  // 1. Pantalones sobre las piernas (si no es transparente)
  if (colorPantalones && colorPantalones !== "transparent") {
    cuerpoSvg += `
      <!-- Pantalón izquierdo -->
      <path d="M ${p.x.toFixed(1)} ${p.y.toFixed(1)} L ${lKnee.x.toFixed(1)} ${lKnee.y.toFixed(1)} L ${lFoot.x.toFixed(1)} ${(lFoot.y - 10).toFixed(1)}" stroke="${colorPantalones}" stroke-width="17" stroke-linecap="round" stroke-linejoin="round" />
      <!-- Pantalón derecho -->
      <path d="M ${p.x.toFixed(1)} ${p.y.toFixed(1)} L ${rKnee.x.toFixed(1)} ${rKnee.y.toFixed(1)} L ${rFoot.x.toFixed(1)} ${(rFoot.y - 10).toFixed(1)}" stroke="${colorPantalones}" stroke-width="17" stroke-linecap="round" stroke-linejoin="round" />
    `;
  }

  // 2. Calzado / Zapatillas en los pies
  if (colorZapatos) {
    cuerpoSvg += `
      <!-- Zapato izquierdo -->
      <g transform="translate(${lFoot.x.toFixed(1)}, ${lFoot.y.toFixed(1)})">
        <ellipse cx="4" cy="4" rx="14" ry="7" fill="${colorZapatos}" stroke="${strokeColor}" stroke-width="3" />
        <rect x="-10" y="6" width="28" height="4" rx="2" fill="#FFFFFF" opacity="0.9" />
      </g>
      <!-- Zapato derecho -->
      <g transform="translate(${rFoot.x.toFixed(1)}, ${rFoot.y.toFixed(1)})">
        <ellipse cx="4" cy="4" rx="14" ry="7" fill="${colorZapatos}" stroke="${strokeColor}" stroke-width="3" />
        <rect x="-10" y="6" width="28" height="4" rx="2" fill="#FFFFFF" opacity="0.9" />
      </g>
    `;
  }

  // 3. Prendas de Torso
  const shoulderW = 34;
  const waistW = 28;

  switch (ropaTorso) {
    case "sudadera": {
      // Sudadera deportiva tipo hoodie con bolsillo de canguro
      const pathSudadera = `
        M ${(n.x - shoulderW).toFixed(1)} ${(n.y + 6).toFixed(1)}
        Q ${n.x.toFixed(1)} ${(n.y + 16).toFixed(1)} ${(n.x + shoulderW).toFixed(1)} ${(n.y + 6).toFixed(1)}
        L ${(p.x + waistW + 2).toFixed(1)} ${(p.y + 4).toFixed(1)}
        Q ${p.x.toFixed(1)} ${(p.y + 12).toFixed(1)} ${(p.x - waistW - 2).toFixed(1)} ${(p.y + 4).toFixed(1)}
        Z
      `;
      cuerpoSvg += `
        <!-- Sudadera con sombra y bolsillo -->
        <path d="${pathSudadera}" fill="${colorTorso}" stroke="${strokeColor}" stroke-width="4.5" stroke-linejoin="round" />
        <!-- Cuello elástico -->
        <ellipse cx="${n.x.toFixed(1)}" cy="${(n.y + 12).toFixed(1)}" rx="18" ry="8" fill="${colorSecundarioTorso || "#FFFFFF"}" stroke="${strokeColor}" stroke-width="3" />
        <!-- Bolsillo de canguro -->
        <path d="M ${(m.x - 18).toFixed(1)} ${(m.y + 14).toFixed(1)} L ${(m.x + 18).toFixed(1)} ${(m.y + 14).toFixed(1)} L ${(p.x + 15).toFixed(1)} ${(p.y - 2).toFixed(1)} L ${(p.x - 15).toFixed(1)} ${(p.y - 2).toFixed(1)} Z" fill="${colorSecundarioTorso || "#E2E8F0"}" stroke="${strokeColor}" stroke-width="2.5" />
      `;
      break;
    }

    case "chaqueta": {
      // Chaqueta abierta con camiseta interior
      const pathFondo = `
        M ${(n.x - shoulderW).toFixed(1)} ${(n.y + 8).toFixed(1)}
        L ${(n.x + shoulderW).toFixed(1)} ${(n.y + 8).toFixed(1)}
        L ${(p.x + waistW).toFixed(1)} ${(p.y + 2).toFixed(1)}
        L ${(p.x - waistW).toFixed(1)} ${(p.y + 2).toFixed(1)}
        Z
      `;
      cuerpoSvg += `
        <!-- Camiseta interior -->
        <path d="${pathFondo}" fill="${colorSecundarioTorso || "#FFFFFF"}" stroke="${strokeColor}" stroke-width="4" />
        <!-- Panel izquierdo chaqueta -->
        <path d="M ${(n.x - shoulderW).toFixed(1)} ${(n.y + 8).toFixed(1)} L ${(n.x - 6).toFixed(1)} ${(n.y + 18).toFixed(1)} L ${(p.x - 10).toFixed(1)} ${(p.y + 2).toFixed(1)} L ${(p.x - waistW).toFixed(1)} ${(p.y + 2).toFixed(1)} Z" fill="${colorTorso}" stroke="${strokeColor}" stroke-width="3.5" />
        <!-- Panel derecho chaqueta -->
        <path d="M ${(n.x + shoulderW).toFixed(1)} ${(n.y + 8).toFixed(1)} L ${(n.x + 6).toFixed(1)} ${(n.y + 18).toFixed(1)} L ${(p.x + 10).toFixed(1)} ${(p.y + 2).toFixed(1)} L ${(p.x + waistW).toFixed(1)} ${(p.y + 2).toFixed(1)} Z" fill="${colorTorso}" stroke="${strokeColor}" stroke-width="3.5" />
        <!-- Solapa de cuello -->
        <polygon points="${(n.x - 18).toFixed(1)},${(n.y + 8).toFixed(1)} ${(n.x - 6).toFixed(1)},${(n.y + 24).toFixed(1)} ${(n.x - 22).toFixed(1)},${(n.y + 26).toFixed(1)}" fill="${colorTorso}" stroke="${strokeColor}" stroke-width="2.5" />
        <polygon points="${(n.x + 18).toFixed(1)},${(n.y + 8).toFixed(1)} ${(n.x + 6).toFixed(1)},${(n.y + 24).toFixed(1)} ${(n.x + 22).toFixed(1)},${(n.y + 26).toFixed(1)}" fill="${colorTorso}" stroke="${strokeColor}" stroke-width="2.5" />
      `;
      break;
    }

    case "vestido": {
      // Vestido acampanado femenino
      const dressBottomY = Math.min(lKnee.y, rKnee.y) + 12;
      const flareW = 54;
      const pathTop = `
        M ${(n.x - shoulderW + 6).toFixed(1)} ${(n.y + 10).toFixed(1)}
        Q ${n.x.toFixed(1)} ${(n.y + 22).toFixed(1)} ${(n.x + shoulderW - 6).toFixed(1)} ${(n.y + 10).toFixed(1)}
        L ${(p.x + 20).toFixed(1)} ${p.y.toFixed(1)}
        L ${(p.x - 20).toFixed(1)} ${p.y.toFixed(1)}
        Z
      `;
      const pathFalda = `
        M ${(p.x - 20).toFixed(1)} ${p.y.toFixed(1)}
        L ${(p.x + 20).toFixed(1)} ${p.y.toFixed(1)}
        L ${(p.x + flareW).toFixed(1)} ${dressBottomY.toFixed(1)}
        Q ${p.x.toFixed(1)} ${(dressBottomY + 12).toFixed(1)} ${(p.x - flareW).toFixed(1)} ${dressBottomY.toFixed(1)}
        Z
      `;
      cuerpoSvg += `
        <!-- Falda en campana -->
        <path d="${pathFalda}" fill="${colorTorso}" stroke="${strokeColor}" stroke-width="4.5" stroke-linejoin="round" />
        <!-- Pliegue de vuelo -->
        <path d="M ${p.x.toFixed(1)} ${p.y.toFixed(1)} Q ${(p.x + 6).toFixed(1)} ${(dressBottomY - 14).toFixed(1)} ${p.x.toFixed(1)} ${(dressBottomY + 6).toFixed(1)}" fill="none" stroke="${colorSecundarioTorso || "#4C1D95"}" stroke-width="3" opacity="0.6" />
        <!-- Top vestido -->
        <path d="${pathTop}" fill="${colorTorso}" stroke="${strokeColor}" stroke-width="4.5" stroke-linejoin="round" />
        <!-- Cinturón decorativo -->
        <rect x="${(p.x - 22).toFixed(1)}" y="${(p.y - 4).toFixed(1)}" width="44" height="8" rx="3" fill="${colorSecundarioTorso || "#FDE047"}" stroke="${strokeColor}" stroke-width="2.5" />
      `;
      break;
    }

    case "abrigo": {
      // Abrigo largo o gabardina
      const coatBottomY = Math.min(lKnee.y, rKnee.y) + 6;
      const pathCoat = `
        M ${(n.x - shoulderW - 4).toFixed(1)} ${(n.y + 6).toFixed(1)}
        L ${(n.x + shoulderW + 4).toFixed(1)} ${(n.y + 6).toFixed(1)}
        L ${(p.x + waistW + 12).toFixed(1)} ${coatBottomY.toFixed(1)}
        L ${(p.x - waistW - 12).toFixed(1)} ${coatBottomY.toFixed(1)}
        Z
      `;
      cuerpoSvg += `
        <!-- Abrigo largo -->
        <path d="${pathCoat}" fill="${colorTorso}" stroke="${strokeColor}" stroke-width="4.5" stroke-linejoin="round" />
        <!-- Solapa central y botones -->
        <line x1="${n.x.toFixed(1)}" y1="${(n.y + 12).toFixed(1)}" x2="${p.x.toFixed(1)}" y2="${coatBottomY.toFixed(1)}" stroke="${strokeColor}" stroke-width="3.5" />
        <circle cx="${(p.x + 8).toFixed(1)}" cy="${(m.y - 6).toFixed(1)}" r="4" fill="${colorSecundarioTorso || "#FFFFFF"}" stroke="${strokeColor}" stroke-width="2" />
        <circle cx="${(p.x + 8).toFixed(1)}" cy="${(m.y + 16).toFixed(1)}" r="4" fill="${colorSecundarioTorso || "#FFFFFF"}" stroke="${strokeColor}" stroke-width="2" />
        <circle cx="${(p.x + 8).toFixed(1)}" cy="${(p.y + 2).toFixed(1)}" r="4" fill="${colorSecundarioTorso || "#FFFFFF"}" stroke="${strokeColor}" stroke-width="2" />
      `;
      break;
    }

    case "chaleco": {
      // Chaleco de punto sobre camisa
      const pathCamisa = `
        M ${(n.x - shoulderW).toFixed(1)} ${(n.y + 8).toFixed(1)}
        L ${(n.x + shoulderW).toFixed(1)} ${(n.y + 8).toFixed(1)}
        L ${(p.x + waistW).toFixed(1)} ${p.y.toFixed(1)}
        L ${(p.x - waistW).toFixed(1)} ${p.y.toFixed(1)}
        Z
      `;
      cuerpoSvg += `
        <!-- Camisa fondo -->
        <path d="${pathCamisa}" fill="${colorSecundarioTorso || "#F8FAFC"}" stroke="${strokeColor}" stroke-width="4" />
        <!-- Chaleco con cuello V -->
        <path d="M ${(n.x - shoulderW).toFixed(1)} ${(n.y + 10).toFixed(1)} L ${(n.x - 12).toFixed(1)} ${(n.y + 10).toFixed(1)} L ${m.x.toFixed(1)} ${(m.y + 10).toFixed(1)} L ${(n.x + 12).toFixed(1)} ${(n.y + 10).toFixed(1)} L ${(n.x + shoulderW).toFixed(1)} ${(n.y + 10).toFixed(1)} L ${(p.x + waistW - 2).toFixed(1)} ${p.y.toFixed(1)} L ${(p.x - waistW + 2).toFixed(1)} ${p.y.toFixed(1)} Z" fill="${colorTorso}" stroke="${strokeColor}" stroke-width="3.5" />
        <!-- Corbata sutil o botones -->
        <circle cx="${m.x.toFixed(1)}" cy="${(m.y + 24).toFixed(1)}" r="3" fill="#E2E8F0" stroke="${strokeColor}" stroke-width="1.5" />
        <circle cx="${p.x.toFixed(1)}" cy="${(p.y - 6).toFixed(1)}" r="3" fill="#E2E8F0" stroke="${strokeColor}" stroke-width="1.5" />
      `;
      break;
    }

    case "bata": {
      // Bata blanca de laboratorio
      const labBottomY = Math.min(lKnee.y, rKnee.y) + 4;
      const pathBata = `
        M ${(n.x - shoulderW - 2).toFixed(1)} ${(n.y + 6).toFixed(1)}
        L ${(n.x + shoulderW + 2).toFixed(1)} ${(n.y + 6).toFixed(1)}
        L ${(p.x + waistW + 8).toFixed(1)} ${labBottomY.toFixed(1)}
        L ${(p.x - waistW - 8).toFixed(1)} ${labBottomY.toFixed(1)}
        Z
      `;
      cuerpoSvg += `
        <!-- Bata blanca -->
        <path d="${pathBata}" fill="#FFFFFF" stroke="${strokeColor}" stroke-width="4.5" stroke-linejoin="round" />
        <!-- Cuello solapa -->
        <polygon points="${(n.x - 14).toFixed(1)},${(n.y + 6).toFixed(1)} ${n.x.toFixed(1)},${(n.y + 24).toFixed(1)} ${(n.x + 14).toFixed(1)},${(n.y + 6).toFixed(1)}" fill="${colorSecundarioTorso || "#0284C7"}" stroke="${strokeColor}" stroke-width="2.5" />
        <!-- Bolsillo pecho con bolígrafos -->
        <rect x="${(m.x - 24).toFixed(1)}" y="${(m.y - 8).toFixed(1)}" width="14" height="18" rx="2" fill="#F1F5F9" stroke="${strokeColor}" stroke-width="2" />
        <line x1="${(m.x - 20).toFixed(1)}" y1="${(m.y - 12).toFixed(1)}" x2="${(m.x - 20).toFixed(1)}" y2="${(m.y - 4).toFixed(1)}" stroke="#EF4444" stroke-width="2.5" />
        <line x1="${(m.x - 16).toFixed(1)}" y1="${(m.y - 10).toFixed(1)}" x2="${(m.x - 16).toFixed(1)}" y2="${(m.y - 4).toFixed(1)}" stroke="#0284C7" stroke-width="2.5" />
      `;
      break;
    }

    case "manto_real": {
      // Manto de terciopelo real con armiño (estilo reyes Habsburgo del video)
      const mantleBottomY = Math.min(lKnee.y, rKnee.y) + 24;
      const pathMantle = `
        M ${(n.x - shoulderW - 12).toFixed(1)} ${(n.y + 4).toFixed(1)}
        Q ${n.x.toFixed(1)} ${(n.y + 20).toFixed(1)} ${(n.x + shoulderW + 12).toFixed(1)} ${(n.y + 4).toFixed(1)}
        L ${(p.x + waistW + 28).toFixed(1)} ${mantleBottomY.toFixed(1)}
        Q ${p.x.toFixed(1)} ${(mantleBottomY + 14).toFixed(1)} ${(p.x - waistW - 28).toFixed(1)} ${mantleBottomY.toFixed(1)}
        Z
      `;
      cuerpoSvg += `
        <!-- Manto regio morado -->
        <path d="${pathMantle}" fill="${colorTorso}" stroke="${strokeColor}" stroke-width="5" stroke-linejoin="round" />
        <!-- Cuello de armiño blanco moteado -->
        <path d="M ${(n.x - shoulderW - 12).toFixed(1)} ${(n.y + 4).toFixed(1)} Q ${n.x.toFixed(1)} ${(n.y + 28).toFixed(1)} ${(n.x + shoulderW + 12).toFixed(1)} ${(n.y + 4).toFixed(1)} Q ${n.x.toFixed(1)} ${(n.y + 12).toFixed(1)} ${(n.x - shoulderW - 12).toFixed(1)} ${(n.y + 4).toFixed(1)} Z" fill="#F8FAFC" stroke="${strokeColor}" stroke-width="3" />
        <circle cx="${(n.x - 14).toFixed(1)}" cy="${(n.y + 16).toFixed(1)}" r="2.5" fill="#1E293B" />
        <circle cx="${n.x.toFixed(1)}" cy="${(n.y + 20).toFixed(1)}" r="2.5" fill="#1E293B" />
        <circle cx="${(n.x + 14).toFixed(1)}" cy="${(n.y + 16).toFixed(1)}" r="2.5" fill="#1E293B" />
        <!-- Cinta dorada vertical -->
        <rect x="${(p.x - 7).toFixed(1)}" y="${(n.y + 24).toFixed(1)}" width="14" height="${(mantleBottomY - n.y - 20).toFixed(1)}" fill="#FACC15" stroke="${strokeColor}" stroke-width="2.5" />
      `;
      break;
    }

    default:
      break;
  }

  return cuerpoSvg;
}

/**
 * Renderiza el peinado y los accesorios de cabeza en el sistema de coordenadas local de la cabeza
 * (centro en x=200, y=115, radio=68).
 */
export function renderizarCabezaYPeinado(
  vestuario: ConfiguracionVestuario,
  strokeColor: string = "#111827"
): { peinadoAtrasSvg: string; peinadoFrenteSvg: string; accesorioSvg: string } {
  const { peinado, colorPelo = "#1E293B", accesorioCabeza, colorAccesorio = "#DC2626" } = vestuario;

  let peinadoAtrasSvg = "";
  let peinadoFrenteSvg = "";
  let accesorioSvg = "";

  // 1. PEINADOS
  switch (peinado) {
    case "mono_alto": {
      // Moño alto femenino estilizado
      peinadoAtrasSvg = `
        <circle cx="200" cy="38" r="28" fill="${colorPelo}" stroke="${strokeColor}" stroke-width="5" />
        <rect x="186" y="52" width="28" height="8" rx="4" fill="#FACC15" stroke="${strokeColor}" stroke-width="2.5" />
      `;
      break;
    }

    case "coleta": {
      // Coleta lateral / hacia atrás
      peinadoAtrasSvg = `
        <path d="M 245 105 Q 285 125 295 185 Q 265 175 240 135 Z" fill="${colorPelo}" stroke="${strokeColor}" stroke-width="4.5" stroke-linejoin="round" />
        <circle cx="242" cy="118" r="8" fill="#EC4899" stroke="${strokeColor}" stroke-width="2.5" />
      `;
      break;
    }

    case "melena_bob": {
      // Melena estilo bob que enmarca la cabeza por detrás sin obstruir el rostro
      peinadoAtrasSvg = `
        <path d="M 124 115 C 120 35 280 35 276 115 C 276 175 258 190 244 185 C 236 150 248 115 246 100 C 240 64 160 64 154 100 C 152 115 164 150 156 185 C 142 190 124 175 124 115 Z" fill="${colorPelo}" stroke="${strokeColor}" stroke-width="4.5" stroke-linejoin="round" />
      `;
      peinadoFrenteSvg = `
        <!-- Mechón sutil en la parte alta de la frente, por encima de las cejas -->
        <path d="M 156 68 Q 185 55 218 64" fill="none" stroke="${colorPelo}" stroke-width="5" stroke-linecap="round" />
      `;
      break;
    }

    case "canoso_anciano": {
      // Mechones canosos laterales y nuca
      peinadoAtrasSvg = `
        <!-- Mechón izquierdo esponjoso -->
        <circle cx="138" cy="120" r="18" fill="${colorPelo}" stroke="${strokeColor}" stroke-width="4" />
        <circle cx="134" cy="138" r="14" fill="${colorPelo}" stroke="${strokeColor}" stroke-width="3.5" />
        <!-- Mechón derecho esponjoso -->
        <circle cx="262" cy="120" r="18" fill="${colorPelo}" stroke="${strokeColor}" stroke-width="4" />
        <circle cx="266" cy="138" r="14" fill="${colorPelo}" stroke="${strokeColor}" stroke-width="3.5" />
      `;
      peinadoFrenteSvg = `
        <!-- Cejas pobladas canosas -->
        <line x1="168" y1="84" x2="190" y2="86" stroke="${colorPelo}" stroke-width="6" stroke-linecap="round" />
        <line x1="210" y1="86" x2="232" y2="84" stroke="${colorPelo}" stroke-width="6" stroke-linecap="round" />
      `;
      break;
    }

    case "canoso_mono": {
      // Moño blanco/grisáceo de abuela
      peinadoAtrasSvg = `
        <circle cx="200" cy="36" r="26" fill="${colorPelo}" stroke="${strokeColor}" stroke-width="4.5" />
        <circle cx="200" cy="36" r="12" fill="none" stroke="${strokeColor}" stroke-width="2.5" opacity="0.4" />
        <line x1="175" y1="46" x2="225" y2="28" stroke="#D97706" stroke-width="3.5" stroke-linecap="round" />
      `;
      break;
    }

    case "nino_despeinado": {
      // Mechones despeinados infantiles
      peinadoFrenteSvg = `
        <path d="M 175 52 L 185 34 L 195 50 L 210 32 L 218 52 Z" fill="${colorPelo}" stroke="${strokeColor}" stroke-width="3" stroke-linejoin="round" />
      `;
      break;
    }

    case "corto_clasico": {
      // Pelo corto masculino con volumen superior
      peinadoFrenteSvg = `
        <path d="M 142 98 Q 155 48 205 48 Q 248 50 258 98 Q 235 68 200 68 Q 165 68 142 98 Z" fill="${colorPelo}" stroke="${strokeColor}" stroke-width="3.5" stroke-linejoin="round" />
      `;
      break;
    }

    default:
      break;
  }

  // 2. ACCESORIOS DE CABEZA
  switch (accesorioCabeza) {
    case "gorra": {
      // Gorra de béisbol con visera frontal
      accesorioSvg = `
        <!-- Corona de la gorra -->
        <path d="M 140 96 C 142 46 258 46 260 96 Z" fill="${colorAccesorio}" stroke="${strokeColor}" stroke-width="5" stroke-linejoin="round" />
        <!-- Botón superior -->
        <circle cx="200" cy="52" r="5" fill="#FFFFFF" stroke="${strokeColor}" stroke-width="2" />
        <!-- Visera hacia la derecha -->
        <path d="M 235 90 C 265 92 295 106 305 116 C 285 118 245 104 228 100 Z" fill="${colorAccesorio}" stroke="${strokeColor}" stroke-width="4.5" stroke-linejoin="round" />
      `;
      break;
    }

    case "gorra_atras": {
      // Gorra con visera hacia atrás
      accesorioSvg = `
        <path d="M 140 96 C 142 46 258 46 260 96 Z" fill="${colorAccesorio}" stroke="${strokeColor}" stroke-width="5" stroke-linejoin="round" />
        <circle cx="200" cy="52" r="5" fill="#FFFFFF" stroke="${strokeColor}" stroke-width="2" />
        <path d="M 165 92 C 135 92 105 106 95 116 C 115 118 155 104 172 100 Z" fill="${colorAccesorio}" stroke="${strokeColor}" stroke-width="4.5" stroke-linejoin="round" />
      `;
      break;
    }

    case "gafas_redondas": {
      // Gafas circulares estilo intelectual o anciano
      accesorioSvg = `
        <!-- Lente izquierda -->
        <circle cx="178" cy="112" r="21" fill="rgba(255, 255, 255, 0.45)" stroke="${colorAccesorio}" stroke-width="4.5" />
        <!-- Lente derecha -->
        <circle cx="222" cy="112" r="21" fill="rgba(255, 255, 255, 0.45)" stroke="${colorAccesorio}" stroke-width="4.5" />
        <!-- Puente nasal -->
        <path d="M 199 110 Q 200 106 201 110" fill="none" stroke="${colorAccesorio}" stroke-width="4" stroke-linecap="round" />
        <!-- Patillas -->
        <line x1="157" y1="112" x2="135" y2="108" stroke="${colorAccesorio}" stroke-width="3.5" stroke-linecap="round" />
        <line x1="243" y1="112" x2="265" y2="108" stroke="${colorAccesorio}" stroke-width="3.5" stroke-linecap="round" />
        <!-- Brillo en cristales -->
        <line x1="168" y1="102" x2="178" y2="96" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" />
        <line x1="212" y1="102" x2="222" y2="96" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" />
      `;
      break;
    }

    case "gafas_pasta": {
      // Gafas rectangulares modernas de pasta
      accesorioSvg = `
        <rect x="156" y="98" width="38" height="26" rx="6" fill="rgba(255, 255, 255, 0.35)" stroke="${colorAccesorio}" stroke-width="4.5" />
        <rect x="206" y="98" width="38" height="26" rx="6" fill="rgba(255, 255, 255, 0.35)" stroke="${colorAccesorio}" stroke-width="4.5" />
        <line x1="194" y1="110" x2="206" y2="110" stroke="${colorAccesorio}" stroke-width="4" />
      `;
      break;
    }

    case "corona": {
      // Corona real dorada con gemas
      accesorioSvg = `
        <polygon points="152,64 162,24 182,46 200,16 218,46 238,24 248,64" fill="${colorAccesorio}" stroke="${strokeColor}" stroke-width="4" stroke-linejoin="round" />
        <circle cx="162" cy="24" r="4" fill="#EF4444" stroke="${strokeColor}" stroke-width="1.5" />
        <circle cx="200" cy="16" r="5" fill="#38BDF8" stroke="${strokeColor}" stroke-width="1.5" />
        <circle cx="238" cy="24" r="4" fill="#EF4444" stroke="${strokeColor}" stroke-width="1.5" />
        <rect x="152" y="60" width="96" height="8" rx="2" fill="#CA8A04" stroke="${strokeColor}" stroke-width="2" />
      `;
      break;
    }

    case "gorra_aviador": {
      // Gorra de aviador retro de cuero: ajustada en la parte superior del cráneo sin tapar ojos ni cejas
      const capColor = colorAccesorio || "#78350F"; // Cuero marrón clásico
      accesorioSvg = `
        <!-- Casquete superior de cuero (abovedado en la coronilla, y: 18 a 72) -->
        <path d="M 136 74 C 132 18 268 18 264 74 C 248 64 152 64 136 74 Z" fill="${capColor}" stroke="${strokeColor}" stroke-width="4.5" stroke-linejoin="round" />
        <!-- Costuras decorativas de cuero -->
        <path d="M 200 22 L 200 64" stroke="#451A03" stroke-width="2.5" stroke-dasharray="4 3" />
        <path d="M 158 36 Q 200 48 242 36" stroke="#451A03" stroke-width="2" stroke-dasharray="3 3" fill="none" />
        
        <!-- Orejera izquierda con borrego (lateral exterior, no invade rostro) -->
        <path d="M 136 70 C 122 78 118 108 126 126 C 132 132 142 130 140 118 C 138 102 137 84 136 70 Z" fill="${capColor}" stroke="${strokeColor}" stroke-width="4" stroke-linejoin="round" />
        <circle cx="130" cy="122" r="4.5" fill="#FEF3C7" stroke="${strokeColor}" stroke-width="2" />
        
        <!-- Orejera derecha con borrego (lateral exterior) -->
        <path d="M 264 70 C 278 78 282 108 274 126 C 268 132 258 130 260 118 C 262 102 263 84 264 70 Z" fill="${capColor}" stroke="${strokeColor}" stroke-width="4" stroke-linejoin="round" />
        <circle cx="270" cy="122" r="4.5" fill="#FEF3C7" stroke="${strokeColor}" stroke-width="2" />

        <!-- Cinta elástica de las gafas de aviador -->
        <path d="M 138 52 Q 200 42 262 52" fill="none" stroke="#1E293B" stroke-width="5" stroke-linecap="round" />
        
        <!-- Gafas de aviador reposadas arriba en el casquete (y: 44, dejando la frente y ojos 100% libres) -->
        <!-- Ocular izquierdo -->
        <circle cx="178" cy="46" r="12" fill="#0EA5E9" stroke="#D97706" stroke-width="3.5" />
        <circle cx="178" cy="46" r="9.5" fill="#38BDF8" opacity="0.85" />
        <line x1="172" y1="41" x2="180" y2="37" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" />
        
        <!-- Ocular derecho -->
        <circle cx="222" cy="46" r="12" fill="#0EA5E9" stroke="#D97706" stroke-width="3.5" />
        <circle cx="222" cy="46" r="9.5" fill="#38BDF8" opacity="0.85" />
        <line x1="216" y1="41" x2="224" y2="37" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" />
        
        <!-- Puente metálico entre lentes -->
        <rect x="192" y="44" width="16" height="4" rx="1.5" fill="#B45309" stroke="${strokeColor}" stroke-width="1.5" />

        <!-- Auriculares de radioaficionado acolchados sobre las orejas (laterales a 124 y 276) -->
        <ellipse cx="122" cy="106" rx="8" ry="15" fill="#1E293B" stroke="${strokeColor}" stroke-width="3.5" />
        <ellipse cx="122" cy="106" rx="4" ry="9" fill="#475569" />
        <ellipse cx="278" cy="106" rx="8" ry="15" fill="#1E293B" stroke="${strokeColor}" stroke-width="3.5" />
        <ellipse cx="278" cy="106" rx="4" ry="9" fill="#475569" />
      `;
      break;
    }

    default:
      break;
  }

  return { peinadoAtrasSvg, peinadoFrenteSvg, accesorioSvg };
}
