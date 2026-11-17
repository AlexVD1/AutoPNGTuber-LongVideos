export type EyeStyle =
  | "normal"
  | "closed"
  | "happy_arc"
  | "wide"
  | "squint"
  | "teary"
  | "looking_up"
  | "looking_down"
  | "looking_side"
  | "wink"
  | "nervous"
  | "deadpan"
  | "star";

export type EyebrowStyle =
  | "neutral"
  | "raised"
  | "worried"
  | "angry"
  | "asymmetric"
  | "high_arch"
  | "flat";

export type MouthStyle =
  | "neutral"
  | "smile_soft"
  | "smile_wide"
  | "laugh"
  | "surprised_o"
  | "talking"
  | "worried"
  | "sad"
  | "angry"
  | "fear"
  | "confused"
  | "shush"
  | "smirk"
  | "sigh";

export type FaceExtra =
  | "none"
  | "tears"
  | "sweat"
  | "blush"
  | "anger_vein"
  | "sparkles"
  | "zzz";

export interface ExpressionDef {
  id: string;
  name: string;
  emotion: string;
  eyes: EyeStyle;
  eyebrows: EyebrowStyle;
  mouth: MouthStyle;
  extra: FaceExtra;
  tags: string[];
}

export const EXPRESSIONS: Record<string, ExpressionDef> = {
  neutral: {
    id: "neutral",
    name: "Neutra relajada",
    emotion: "neutral",
    eyes: "normal",
    eyebrows: "neutral",
    mouth: "neutral",
    extra: "none",
    tags: ["neutral", "calma", "base"],
  },
  smile_soft: {
    id: "smile_soft",
    name: "Sonrisa leve",
    emotion: "happy",
    eyes: "normal",
    eyebrows: "neutral",
    mouth: "smile_soft",
    extra: "none",
    tags: ["sonrisa", "amable", "normal", "positivo"],
  },
  smile_wide: {
    id: "smile_wide",
    name: "Sonrisa amplia",
    emotion: "happy",
    eyes: "happy_arc",
    eyebrows: "raised",
    mouth: "smile_wide",
    extra: "blush",
    tags: ["feliz", "alegre", "sonrisa", "positivo"],
  },
  laugh: {
    id: "laugh",
    name: "Carcajada",
    emotion: "happy",
    eyes: "happy_arc",
    eyebrows: "high_arch",
    mouth: "laugh",
    extra: "sparkles",
    tags: ["risa", "carcajada", "humor", "felicidad"],
  },
  talking: {
    id: "talking",
    name: "Hablando y explicando",
    emotion: "explaining",
    eyes: "normal",
    eyebrows: "raised",
    mouth: "talking",
    extra: "none",
    tags: ["hablando", "explicando", "enseñando"],
  },
  talking_enthusiastic: {
    id: "talking_enthusiastic",
    name: "Explicando con entusiasmo",
    emotion: "enthusiastic",
    eyes: "wide",
    eyebrows: "high_arch",
    mouth: "laugh",
    extra: "sparkles",
    tags: ["entusiasmo", "explicando", "descubrimiento"],
  },
  thinking: {
    id: "thinking",
    name: "Pensativo mirando arriba",
    emotion: "thinking",
    eyes: "looking_up",
    eyebrows: "asymmetric",
    mouth: "confused",
    extra: "none",
    tags: ["pensando", "duda", "analisis", "curiosidad"],
  },
  analytical: {
    id: "analytical",
    name: "Analizando con atención",
    emotion: "focused",
    eyes: "squint",
    eyebrows: "asymmetric",
    mouth: "neutral",
    extra: "none",
    tags: ["analisis", "observando", "concentrado"],
  },
  confused: {
    id: "confused",
    name: "Confundido",
    emotion: "confused",
    eyes: "looking_side",
    eyebrows: "asymmetric",
    mouth: "confused",
    extra: "sweat",
    tags: ["confundido", "duda", "extrañado"],
  },
  eureka: {
    id: "eureka",
    name: "Idea repentina (Eureka)",
    emotion: "excited",
    eyes: "star",
    eyebrows: "high_arch",
    mouth: "smile_wide",
    extra: "sparkles",
    tags: ["idea", "eureka", "descubrimiento", "genial"],
  },
  surprised: {
    id: "surprised",
    name: "Sorprendido con boca abierta",
    emotion: "surprised",
    eyes: "wide",
    eyebrows: "high_arch",
    mouth: "surprised_o",
    extra: "none",
    tags: ["sorprendido", "asombro", "impacto"],
  },
  shocked: {
    id: "shocked",
    name: "En estado de shock",
    emotion: "shocked",
    eyes: "wide",
    eyebrows: "high_arch",
    mouth: "fear",
    extra: "sweat",
    tags: ["shock", "impactado", "explosion", "susto"],
  },
  scared: {
    id: "scared",
    name: "Asustado con miedo",
    emotion: "scared",
    eyes: "nervous",
    eyebrows: "worried",
    mouth: "fear",
    extra: "sweat",
    tags: ["miedo", "terror", "nervioso", "peligro"],
  },
  worried: {
    id: "worried",
    name: "Preocupado",
    emotion: "worried",
    eyes: "looking_side",
    eyebrows: "worried",
    mouth: "worried",
    extra: "sweat",
    tags: ["preocupado", "tension", "ansiedad"],
  },
  sad: {
    id: "sad",
    name: "Triste y decepcionado",
    emotion: "sad",
    eyes: "looking_down",
    eyebrows: "worried",
    mouth: "sad",
    extra: "none",
    tags: ["triste", "decepcionado", "bajo_animo"],
  },
  crying: {
    id: "crying",
    name: "Llorando",
    emotion: "crying",
    eyes: "teary",
    eyebrows: "worried",
    mouth: "sad",
    extra: "tears",
    tags: ["llorando", "lagrimas", "tristeza"],
  },
  angry: {
    id: "angry",
    name: "Enfadado",
    emotion: "angry",
    eyes: "squint",
    eyebrows: "angry",
    mouth: "angry",
    extra: "anger_vein",
    tags: ["enfadado", "enojo", "furia", "molesto"],
  },
  frustrated: {
    id: "frustrated",
    name: "Frustrado e impaciente",
    emotion: "frustrated",
    eyes: "closed",
    eyebrows: "angry",
    mouth: "worried",
    extra: "anger_vein",
    tags: ["frustrado", "impaciente", "estres"],
  },
  exhausted: {
    id: "exhausted",
    name: "Agotado y sin energía",
    emotion: "exhausted",
    eyes: "closed",
    eyebrows: "flat",
    mouth: "sigh",
    extra: "sweat",
    tags: ["agotado", "cansado", "rendido"],
  },
  bored: {
    id: "bored",
    name: "Aburrido",
    emotion: "bored",
    eyes: "deadpan",
    eyebrows: "flat",
    mouth: "neutral",
    extra: "zzz",
    tags: ["aburrido", "sueño", "indiferente"],
  },
  embarrassed: {
    id: "embarrassed",
    name: "Avergonzado",
    emotion: "embarrassed",
    eyes: "looking_side",
    eyebrows: "worried",
    mouth: "smile_soft",
    extra: "blush",
    tags: ["avergonzado", "pena", "rubor"],
  },
  proud: {
    id: "proud",
    name: "Orgulloso y confiado",
    emotion: "proud",
    eyes: "closed",
    eyebrows: "raised",
    mouth: "smirk",
    extra: "sparkles",
    tags: ["orgulloso", "confiado", "logro", "exito"],
  },
  skeptical: {
    id: "skeptical",
    name: "Incrédulo y escéptico",
    emotion: "skeptical",
    eyes: "squint",
    eyebrows: "asymmetric",
    mouth: "smirk",
    extra: "none",
    tags: ["incredulo", "esceptico", "sospecha"],
  },
  shushing: {
    id: "shushing",
    name: "Pidiendo silencio / Secreto",
    emotion: "secretive",
    eyes: "wink",
    eyebrows: "raised",
    mouth: "shush",
    extra: "none",
    tags: ["silencio", "secreto", "misterio"],
  },
};

export function renderFaceMarkup(
  expr: ExpressionDef,
  stroke = "#111827"
): string {
  const parts: string[] = [];

  // 1. Extras detrás o en las mejillas (blush)
  if (expr.extra === "blush") {
    parts.push(
      `<ellipse cx="156" cy="122" rx="12" ry="7" fill="#FCA5A5" opacity="0.75" />`,
      `<ellipse cx="244" cy="122" rx="12" ry="7" fill="#FCA5A5" opacity="0.75" />`
    );
  }

  // 2. Cejas
  switch (expr.eyebrows) {
    case "neutral":
      parts.push(
        `<path d="M 162 84 Q 176 79 190 84 M 210 84 Q 224 79 238 84" stroke="${stroke}" stroke-width="6" stroke-linecap="round" fill="none" />`
      );
      break;
    case "raised":
      parts.push(
        `<path d="M 162 79 Q 176 69 190 79 M 210 79 Q 224 69 238 79" stroke="${stroke}" stroke-width="6" stroke-linecap="round" fill="none" />`
      );
      break;
    case "high_arch":
      parts.push(
        `<path d="M 160 74 Q 175 60 190 74 M 210 74 Q 225 60 240 74" stroke="${stroke}" stroke-width="6" stroke-linecap="round" fill="none" />`
      );
      break;
    case "worried":
      parts.push(
        `<path d="M 160 88 L 190 78 M 240 88 L 210 78" stroke="${stroke}" stroke-width="6" stroke-linecap="round" fill="none" />`
      );
      break;
    case "angry":
      parts.push(
        `<path d="M 160 76 L 192 90 M 240 76 L 208 90" stroke="${stroke}" stroke-width="7" stroke-linecap="round" fill="none" />`
      );
      break;
    case "asymmetric":
      parts.push(
        `<path d="M 162 86 L 188 90" stroke="${stroke}" stroke-width="6" stroke-linecap="round" />`,
        `<path d="M 212 78 Q 225 66 238 80" stroke="${stroke}" stroke-width="6" stroke-linecap="round" fill="none" />`
      );
      break;
    case "flat":
      parts.push(
        `<path d="M 162 86 L 190 86 M 210 86 L 238 86" stroke="${stroke}" stroke-width="6" stroke-linecap="round" />`
      );
      break;
  }

  // 3. Ojos
  switch (expr.eyes) {
    case "normal":
      parts.push(
        `<circle cx="176" cy="104" r="7" fill="${stroke}" />`,
        `<circle cx="224" cy="104" r="7" fill="${stroke}" />`
      );
      break;
    case "closed":
      parts.push(
        `<path d="M 164 106 Q 176 114 188 106 M 212 106 Q 224 114 236 106" stroke="${stroke}" stroke-width="6" stroke-linecap="round" fill="none" />`
      );
      break;
    case "happy_arc":
      parts.push(
        `<path d="M 164 108 Q 176 92 188 108 M 212 108 Q 224 92 236 108" stroke="${stroke}" stroke-width="7" stroke-linecap="round" fill="none" />`
      );
      break;
    case "wide":
      parts.push(
        `<circle cx="175" cy="103" r="13" fill="#FFFFFF" stroke="${stroke}" stroke-width="6" />`,
        `<circle cx="175" cy="103" r="5" fill="${stroke}" />`,
        `<circle cx="225" cy="103" r="13" fill="#FFFFFF" stroke="${stroke}" stroke-width="6" />`,
        `<circle cx="225" cy="103" r="5" fill="${stroke}" />`
      );
      break;
    case "nervous":
      parts.push(
        `<circle cx="175" cy="103" r="13" fill="#FFFFFF" stroke="${stroke}" stroke-width="6" />`,
        `<circle cx="175" cy="103" r="3.5" fill="${stroke}" />`,
        `<circle cx="225" cy="103" r="13" fill="#FFFFFF" stroke="${stroke}" stroke-width="6" />`,
        `<circle cx="225" cy="103" r="3.5" fill="${stroke}" />`
      );
      break;
    case "squint":
      parts.push(
        `<path d="M 164 99 L 186 104 L 164 109 M 236 99 L 214 104 L 236 109" stroke="${stroke}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none" />`
      );
      break;
    case "teary":
      parts.push(
        `<circle cx="176" cy="104" r="9" fill="${stroke}" />`,
        `<circle cx="173" cy="101" r="3" fill="#FFFFFF" />`,
        `<circle cx="224" cy="104" r="9" fill="${stroke}" />`,
        `<circle cx="221" cy="101" r="3" fill="#FFFFFF" />`
      );
      break;
    case "looking_up":
      parts.push(
        `<circle cx="180" cy="98" r="7" fill="${stroke}" />`,
        `<circle cx="228" cy="96" r="7" fill="${stroke}" />`
      );
      break;
    case "looking_down":
      parts.push(
        `<circle cx="176" cy="112" r="7" fill="${stroke}" />`,
        `<circle cx="224" cy="112" r="7" fill="${stroke}" />`
      );
      break;
    case "looking_side":
      parts.push(
        `<circle cx="184" cy="104" r="7" fill="${stroke}" />`,
        `<circle cx="232" cy="104" r="7" fill="${stroke}" />`
      );
      break;
    case "wink":
      parts.push(
        `<path d="M 164 105 Q 176 95 188 105" stroke="${stroke}" stroke-width="7" stroke-linecap="round" fill="none" />`,
        `<circle cx="224" cy="104" r="7" fill="${stroke}" />`
      );
      break;
    case "deadpan":
      parts.push(
        `<line x1="164" y1="102" x2="188" y2="102" stroke="${stroke}" stroke-width="6" stroke-linecap="round" />`,
        `<circle cx="176" cy="107" r="5" fill="${stroke}" />`,
        `<line x1="212" y1="102" x2="236" y2="102" stroke="${stroke}" stroke-width="6" stroke-linecap="round" />`,
        `<circle cx="224" cy="107" r="5" fill="${stroke}" />`
      );
      break;
    case "star":
      parts.push(
        `<polygon points="176,91 179,99 188,99 181,104 184,113 176,108 168,113 171,104 164,99 173,99" fill="#F59E0B" stroke="${stroke}" stroke-width="2" />`,
        `<polygon points="224,91 227,99 236,99 229,104 232,113 224,108 216,113 219,104 212,99 221,99" fill="#F59E0B" stroke="${stroke}" stroke-width="2" />`
      );
      break;
  }

  // 4. Boca
  switch (expr.mouth) {
    case "neutral":
      parts.push(
        `<line x1="182" y1="140" x2="218" y2="140" stroke="${stroke}" stroke-width="7" stroke-linecap="round" />`
      );
      break;
    case "smile_soft":
      parts.push(
        `<path d="M 175 135 Q 200 154 225 135" stroke="${stroke}" stroke-width="7" stroke-linecap="round" fill="none" />`
      );
      break;
    case "smile_wide":
      parts.push(
        `<path d="M 168 132 Q 200 162 232 132" stroke="${stroke}" stroke-width="8" stroke-linecap="round" fill="none" />`
      );
      break;
    case "laugh":
      parts.push(
        `<path d="M 168 128 Q 200 172 232 128 Z" fill="#EF4444" stroke="${stroke}" stroke-width="6" stroke-linejoin="round" />`,
        `<path d="M 175 130 L 225 130" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round" />`
      );
      break;
    case "talking":
      parts.push(
        `<path d="M 174 130 Q 200 165 226 130 Z" fill="${stroke}" stroke="${stroke}" stroke-width="5" stroke-linejoin="round" />`
      );
      break;
    case "surprised_o":
      parts.push(
        `<ellipse cx="200" cy="142" rx="16" ry="20" fill="${stroke}" />`
      );
      break;
    case "worried":
      parts.push(
        `<path d="M 176 145 Q 188 135 200 145 Q 212 155 224 145" stroke="${stroke}" stroke-width="6" stroke-linecap="round" fill="none" />`
      );
      break;
    case "sad":
      parts.push(
        `<path d="M 174 150 Q 200 130 226 150" stroke="${stroke}" stroke-width="7" stroke-linecap="round" fill="none" />`
      );
      break;
    case "angry":
      parts.push(
        `<path d="M 172 146 Q 200 128 228 146 Z" fill="#FFFFFF" stroke="${stroke}" stroke-width="6" stroke-linejoin="round" />`,
        `<line x1="186" y1="138" x2="186" y2="146" stroke="${stroke}" stroke-width="4" />`,
        `<line x1="200" y1="136" x2="200" y2="146" stroke="${stroke}" stroke-width="4" />`,
        `<line x1="214" y1="138" x2="214" y2="146" stroke="${stroke}" stroke-width="4" />`
      );
      break;
    case "fear":
      parts.push(
        `<rect x="176" y="130" width="48" height="24" rx="10" fill="${stroke}" />`,
        `<path d="M 184 134 L 216 134" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" />`
      );
      break;
    case "confused":
      parts.push(
        `<path d="M 180 142 L 214 135" stroke="${stroke}" stroke-width="7" stroke-linecap="round" />`
      );
      break;
    case "shush":
      parts.push(
        `<circle cx="200" cy="140" r="8" fill="none" stroke="${stroke}" stroke-width="6" />`
      );
      break;
    case "smirk":
      parts.push(
        `<path d="M 178 140 Q 205 148 224 130" stroke="${stroke}" stroke-width="7" stroke-linecap="round" fill="none" />`
      );
      break;
    case "sigh":
      parts.push(
        `<ellipse cx="200" cy="142" rx="12" ry="8" fill="none" stroke="${stroke}" stroke-width="6" />`
      );
      break;
  }

  // 5. Extras frontales (lágrimas, gota de sudor, vena de enojo, brillos, zzz)
  if (expr.extra === "tears") {
    parts.push(
      `<path d="M 164 114 Q 156 132 164 142 Q 172 132 164 114 Z" fill="#3B82F6" />`,
      `<path d="M 236 114 Q 228 132 236 142 Q 244 132 236 114 Z" fill="#3B82F6" />`
    );
  } else if (expr.extra === "sweat") {
    parts.push(
      `<path d="M 252 76 C 244 90 246 102 252 102 C 258 102 260 90 252 76 Z" fill="#38BDF8" stroke="${stroke}" stroke-width="3" />`
    );
  } else if (expr.extra === "anger_vein") {
    parts.push(
      `<path d="M 238 58 L 246 68 L 256 60 M 240 76 L 248 66 L 258 74" stroke="#EF4444" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none" />`
    );
  } else if (expr.extra === "sparkles") {
    parts.push(
      `<path d="M 118 70 L 122 82 L 134 86 L 122 90 L 118 102 L 114 90 L 102 86 L 114 82 Z" fill="#FACC15" />`,
      `<path d="M 282 65 L 285 74 L 294 77 L 285 80 L 282 89 L 279 80 L 270 77 L 279 74 Z" fill="#FACC15" />`
    );
  } else if (expr.extra === "zzz") {
    parts.push(
      `<text x="262" y="75" fill="#6B7280" font-size="28" font-weight="900" font-family="sans-serif">Zzz</text>`
    );
  }

  return parts.join("\n");
}
