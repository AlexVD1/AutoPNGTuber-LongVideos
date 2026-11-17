# scripts/reparar_props_svg.py

props_path = "src/stickman/propsLibrary.ts"
with open(props_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. pluma_microestructura_velcro: SVG limpio sin JS embebido
velcro_clean = '''  pluma_microestructura_velcro: {
    id: "pluma_microestructura_velcro",
    name: "Microestructura de Bárbulas y Ganchillos (Hamuli)",
    family: "educacion_ciencia",
    defaultPlacement: "right",
    svg: `<g>
      <line x1="-40" y1="0" x2="40" y2="0" stroke="#38BDF8" stroke-width="6"/>
    </g>`,
    animatedSvg: (f: number, progress = 0, state = "malla_sellada") => {
      const isTorn = state === "rasgadura_viento";
      const isRepair = state === "auto_reparacion_clic";
      const tearY = isTorn ? 22 : 0;
      const S = "#0F172A";

      return `<g transform="scale(1.2)">
        <!-- 1. BARBA SUPERIOR (Tallo cilíndrico de queratina) -->
        <g transform="translate(0, -32)">
          <path d="M -70 0 C -30 -6, 30 -6, 70 0 L 70 8 C 30 2, -30 2, -70 8 Z" fill="#334155" stroke="${S}" stroke-width="3"/>
          <line x1="-65" y1="2" x2="65" y2="2" stroke="#94A3B8" stroke-width="2"/>
          <text x="-65" y="-8" fill="#94A3B8" font-size="8" font-family="'Arial Black', sans-serif" font-weight="900">BARBA SUPERIOR</text>
        </g>

        <!-- 2. BÁRBULAS DISTALES CON GANCHILLOS (HÁMULI) -->
        <g transform="translate(0, -24)">
          <g transform="translate(-45, 0)">
            <path d="M 0 0 C 4 8, 8 16, 12 24" fill="none" stroke="#38BDF8" stroke-width="3.5" stroke-linecap="round"/>
            <path d="M 12 24 C 14 28, 18 30, 16 34 C 14 36, 10 34, 11 31" fill="none" stroke="#FFE600" stroke-width="3" stroke-linecap="round"/>
          </g>
          <g transform="translate(-20, 0)">
            <path d="M 0 0 C 4 8, 8 16, 12 24" fill="none" stroke="#38BDF8" stroke-width="3.5" stroke-linecap="round"/>
            <path d="M 12 24 C 14 28, 18 30, 16 34 C 14 36, 10 34, 11 31" fill="none" stroke="#FFE600" stroke-width="3" stroke-linecap="round"/>
          </g>
          <g transform="translate(5, 0)">
            <path d="M 0 0 C 4 8, 8 16, 12 24" fill="none" stroke="#38BDF8" stroke-width="3.5" stroke-linecap="round"/>
            <path d="M 12 24 C 14 28, 18 30, 16 34 C 14 36, 10 34, 11 31" fill="none" stroke="#FFE600" stroke-width="3" stroke-linecap="round"/>
          </g>
          <g transform="translate(30, 0)">
            <path d="M 0 0 C 4 8, 8 16, 12 24" fill="none" stroke="#38BDF8" stroke-width="3.5" stroke-linecap="round"/>
            <path d="M 12 24 C 14 28, 18 30, 16 34 C 14 36, 10 34, 11 31" fill="none" stroke="#FFE600" stroke-width="3" stroke-linecap="round"/>
          </g>
          <g transform="translate(55, 0)">
            <path d="M 0 0 C 4 8, 8 16, 12 24" fill="none" stroke="#38BDF8" stroke-width="3.5" stroke-linecap="round"/>
            <path d="M 12 24 C 14 28, 18 30, 16 34 C 14 36, 10 34, 11 31" fill="none" stroke="#FFE600" stroke-width="3" stroke-linecap="round"/>
          </g>
        </g>

        <!-- 3. BARBA INFERIOR (Tallo receptor) -->
        <g transform="translate(0, ${32 + tearY})">
          <path d="M -70 0 C -30 -6, 30 -6, 70 0 L 70 8 C 30 2, -30 2, -70 8 Z" fill="#334155" stroke="${S}" stroke-width="3"/>
          <line x1="-65" y1="2" x2="65" y2="2" stroke="#94A3B8" stroke-width="2"/>
          <text x="-65" y="20" fill="#94A3B8" font-size="8" font-family="'Arial Black', sans-serif" font-weight="900">BARBA INFERIOR</text>
        </g>

        <!-- 4. BÁRBULAS PROXIMALES CON CANALES RECEPTORES -->
        <g transform="translate(0, ${32 + tearY})">
          <g transform="translate(-37, 0)">
            <path d="M 0 0 C -4 -8, -8 -16, -10 -24" fill="none" stroke="#818CF8" stroke-width="3.5" stroke-linecap="round"/>
            <path d="M -10 -24 C -12 -28, -8 -30, -5 -28 C -3 -26, -5 -24, -8 -24" fill="none" stroke="#C084FC" stroke-width="3" stroke-linecap="round"/>
          </g>
          <g transform="translate(-12, 0)">
            <path d="M 0 0 C -4 -8, -8 -16, -10 -24" fill="none" stroke="#818CF8" stroke-width="3.5" stroke-linecap="round"/>
            <path d="M -10 -24 C -12 -28, -8 -30, -5 -28 C -3 -26, -5 -24, -8 -24" fill="none" stroke="#C084FC" stroke-width="3" stroke-linecap="round"/>
          </g>
          <g transform="translate(13, 0)">
            <path d="M 0 0 C -4 -8, -8 -16, -10 -24" fill="none" stroke="#818CF8" stroke-width="3.5" stroke-linecap="round"/>
            <path d="M -10 -24 C -12 -28, -8 -30, -5 -28 C -3 -26, -5 -24, -8 -24" fill="none" stroke="#C084FC" stroke-width="3" stroke-linecap="round"/>
          </g>
          <g transform="translate(38, 0)">
            <path d="M 0 0 C -4 -8, -8 -16, -10 -24" fill="none" stroke="#818CF8" stroke-width="3.5" stroke-linecap="round"/>
            <path d="M -10 -24 C -12 -28, -8 -30, -5 -28 C -3 -26, -5 -24, -8 -24" fill="none" stroke="#C084FC" stroke-width="3" stroke-linecap="round"/>
          </g>
          <g transform="translate(63, 0)">
            <path d="M 0 0 C -4 -8, -8 -16, -10 -24" fill="none" stroke="#818CF8" stroke-width="3.5" stroke-linecap="round"/>
            <path d="M -10 -24 C -12 -28, -8 -30, -5 -28 C -3 -26, -5 -24, -8 -24" fill="none" stroke="#C084FC" stroke-width="3" stroke-linecap="round"/>
          </g>
        </g>

        <!-- 5. EFECTO DE ZONA DE ENGANCHE / SELLO VELCRO -->
        ${!isTorn ? `
          <g transform="translate(0, 2)">
            <rect x="-64" y="-10" width="128" height="20" rx="4" fill="#000000" stroke="#10B981" stroke-width="2" opacity="0.9"/>
            <text x="0" y="4" fill="#10B981" font-size="8.5" font-family="'Arial Black', sans-serif" font-weight="900" text-anchor="middle">
              ${isRepair ? "RE-ENGANCHE AUTOMÁTICO (CLIC)" : "ENCLAVAMIENTO HÁMULI 100%"}
            </text>
          </g>
        ` : `
          <g transform="translate(0, 10)">
            <rect x="-55" y="-10" width="110" height="20" rx="4" fill="#000000" stroke="#EF4444" stroke-width="2" opacity="0.9"/>
            <text x="0" y="4" fill="#EF4444" font-size="8.5" font-family="'Arial Black', sans-serif" font-weight="900" text-anchor="middle">
              RUPTURA ELÁSTICA PASIVA
            </text>
          </g>
        `}
      </g>`;
    },
    tags: ["velcro", "barbula", "hamuli", "queratina", "nanomaterial", "microscopio"],
  },'''

import re
text = re.sub(r'  pluma_microestructura_velcro: \{[\s\S]*?tags: \["velcro", "barbula", "hamuli", "queratina", "nanomaterial", "microscopio"\],\n  \},', velcro_clean, text)

# 2. plumas_asimetricas_persiana
persiana_clean = '''  plumas_asimetricas_persiana: {
    id: "plumas_asimetricas_persiana",
    name: "Persiana Aerodinámica Asimétrica de Plumas",
    family: "educacion_ciencia",
    defaultPlacement: "right",
    svg: `<rect x="-30" y="-12" width="60" height="24" rx="4" fill="#1E293B" stroke="#000" stroke-width="3"/>`,
    animatedSvg: (f: number, progress = 0, state = "bajada_sellada") => {
      const isDown = state === "bajada_sellada";
      const isUp = state === "subida_persiana_45";
      const rot = isDown ? 0 : (isUp ? 42 : 20);
      const S = "#0F172A";

      return `<g transform="scale(1.2)">
        <!-- 4 PLUMAS REMERAS SUPERPUESTAS EN CORTE TRANSVERSAL -->
        <g transform="translate(-48, 0) rotate(${rot})">
          <ellipse cx="6" cy="0" rx="4.5" ry="4" fill="#FFFFFF" stroke="${S}" stroke-width="2.5"/>
          <path d="M 6 -3.5 C -6 -5, -20 -3, -28 3 C -20 5, -6 3, 6 3.5 Z" fill="${isDown ? '#334155' : '#0284C7'}" stroke="${S}" stroke-width="2.5" stroke-linejoin="round"/>
          <path d="M 6 -3.5 C 10 -4, 14 -2, 16 0 C 14 2, 10 3, 6 3.5 Z" fill="${isDown ? '#1E293B' : '#0369A1'}" stroke="${S}" stroke-width="2"/>
        </g>
        <g transform="translate(-16, 0) rotate(${rot})">
          <ellipse cx="6" cy="0" rx="4.5" ry="4" fill="#FFFFFF" stroke="${S}" stroke-width="2.5"/>
          <path d="M 6 -3.5 C -6 -5, -20 -3, -28 3 C -20 5, -6 3, 6 3.5 Z" fill="${isDown ? '#334155' : '#0284C7'}" stroke="${S}" stroke-width="2.5" stroke-linejoin="round"/>
          <path d="M 6 -3.5 C 10 -4, 14 -2, 16 0 C 14 2, 10 3, 6 3.5 Z" fill="${isDown ? '#1E293B' : '#0369A1'}" stroke="${S}" stroke-width="2"/>
        </g>
        <g transform="translate(16, 0) rotate(${rot})">
          <ellipse cx="6" cy="0" rx="4.5" ry="4" fill="#FFFFFF" stroke="${S}" stroke-width="2.5"/>
          <path d="M 6 -3.5 C -6 -5, -20 -3, -28 3 C -20 5, -6 3, 6 3.5 Z" fill="${isDown ? '#334155' : '#0284C7'}" stroke="${S}" stroke-width="2.5" stroke-linejoin="round"/>
          <path d="M 6 -3.5 C 10 -4, 14 -2, 16 0 C 14 2, 10 3, 6 3.5 Z" fill="${isDown ? '#1E293B' : '#0369A1'}" stroke="${S}" stroke-width="2"/>
        </g>
        <g transform="translate(48, 0) rotate(${rot})">
          <ellipse cx="6" cy="0" rx="4.5" ry="4" fill="#FFFFFF" stroke="${S}" stroke-width="2.5"/>
          <path d="M 6 -3.5 C -6 -5, -20 -3, -28 3 C -20 5, -6 3, 6 3.5 Z" fill="${isDown ? '#334155' : '#0284C7'}" stroke="${S}" stroke-width="2.5" stroke-linejoin="round"/>
          <path d="M 6 -3.5 C 10 -4, 14 -2, 16 0 C 14 2, 10 3, 6 3.5 Z" fill="${isDown ? '#1E293B' : '#0369A1'}" stroke="${S}" stroke-width="2"/>
        </g>

        <!-- FLUJO DE AIRE SEGÚN ESTADO DE LA BATIDA -->
        ${isDown ? `
          <line x1="-55" y1="5" x2="55" y2="5" stroke="#10B981" stroke-width="3" stroke-dasharray="6 3"/>
          <g transform="translate(-30, 28)">
            <line x1="0" y1="0" x2="0" y2="-18" stroke="#10B981" stroke-width="3.5"/>
            <polygon points="0,-24 -5,-16 5,-16" fill="#10B981"/>
          </g>
          <g transform="translate(0, 28)">
            <line x1="0" y1="0" x2="0" y2="-18" stroke="#10B981" stroke-width="3.5"/>
            <polygon points="0,-24 -5,-16 5,-16" fill="#10B981"/>
          </g>
          <g transform="translate(30, 28)">
            <line x1="0" y1="0" x2="0" y2="-18" stroke="#10B981" stroke-width="3.5"/>
            <polygon points="0,-24 -5,-16 5,-16" fill="#10B981"/>
          </g>

          <g transform="translate(0, -22)">
            <rect x="-65" y="-11" width="130" height="18" rx="4" fill="#064E3B" stroke="#10B981" stroke-width="1.5"/>
            <text x="0" y="2" fill="#6EE7B7" font-size="8" font-family="'Arial Black', sans-serif" font-weight="900" text-anchor="middle">
              DOWNSTROKE: SELLADO 100%
            </text>
          </g>
        ` : `
          <g transform="translate(-30, -22)">
            <path d="M 0 0 L 0 44" stroke="#38BDF8" stroke-width="3" stroke-dasharray="6 4"/>
            <polygon points="0,48 -4,40 4,40" fill="#38BDF8"/>
          </g>
          <g transform="translate(0, -22)">
            <path d="M 0 0 L 0 44" stroke="#38BDF8" stroke-width="3" stroke-dasharray="6 4"/>
            <polygon points="0,48 -4,40 4,40" fill="#38BDF8"/>
          </g>
          <g transform="translate(30, -22)">
            <path d="M 0 0 L 0 44" stroke="#38BDF8" stroke-width="3" stroke-dasharray="6 4"/>
            <polygon points="0,48 -4,40 4,40" fill="#38BDF8"/>
          </g>

          <g transform="translate(0, -32)">
            <rect x="-68" y="-11" width="136" height="18" rx="4" fill="#0C4A6E" stroke="#38BDF8" stroke-width="1.5"/>
            <text x="0" y="2" fill="#7DD3FC" font-size="8" font-family="'Arial Black', sans-serif" font-weight="900" text-anchor="middle">
              UPSTROKE: PERSIANA ABIERTA
            </text>
          </g>
        `}
      </g>`;
    },
    tags: ["persiana", "asimetria", "aleteo", "valvula", "downstroke", "plumas"],
  },'''

text = re.sub(r'  plumas_asimetricas_persiana: \{[\s\S]*?tags: \["persiana", "asimetria", "aleteo", "valvula", "downstroke", "plumas"\],\n  \},', persiana_clean, text)

# 3. pluma_aguila_metamaterial
pluma_clean = '''  pluma_aguila_metamaterial: {
    id: "pluma_aguila_metamaterial",
    name: "Pluma de Águila Metamaterial Viscoelástico",
    family: "educacion_ciencia",
    defaultPlacement: "right",
    svg: `<path d="M 0 -45 C 16 -15, 14 25, 0 45 C -12 25, -8 -15, 0 -45 Z" fill="#78350F" stroke="#000" stroke-width="3"/>`,
    animatedSvg: (f: number, progress = 0, state = "brisa_ondulacion") => {
      const bend = Math.sin(f * 0.12) * 8;
      const S = "#0F172A";

      return `<g transform="scale(1.25)">
        <!-- 1. CÁLAMO / CAÑÓN (Tubo basal cilíndrico de queratina translúcida) -->
        <path d="M -3 65 L -3 95 C -3 100, 3 100, 3 95 L 3 65 Z" fill="#FEF3C7" stroke="${S}" stroke-width="3"/>
        <line x1="0" y1="68" x2="0" y2="92" stroke="#FDE68A" stroke-width="2"/>
        <circle cx="0" cy="94" r="1.5" fill="#D97706"/>

        <!-- 2. VEXILO EXTERNO / BORDE DE ATAQUE (Estrecho y rígido) -->
        <path d="M 0 65 C 12 35, ${(16 + bend * 0.4).toFixed(1)} -5, ${(14 + bend * 0.7).toFixed(1)} -45 C ${(10 + bend).toFixed(1)} -72, ${(5 + bend * 1.1).toFixed(1)} -90, 0 -95 C 0 -95, 0 65, 0 65 Z" fill="#78350F" stroke="${S}" stroke-width="3.5" stroke-linejoin="round"/>
        
        <!-- Franjas de melanina en borde externo -->
        <path d="M 0 -30 L ${11 + bend * 0.6} -42" stroke="#451A03" stroke-width="3" stroke-linecap="round"/>
        <path d="M 0 -5 L ${11 + bend * 0.6} -17" stroke="#451A03" stroke-width="3" stroke-linecap="round"/>
        <path d="M 0 20 L 11 8" stroke="#451A03" stroke-width="3" stroke-linecap="round"/>
        <path d="M 0 45 L 11 33" stroke="#451A03" stroke-width="3" stroke-linecap="round"/>

        <!-- 3. VEXILO INTERNO / BORDE DE FUGA (Ancho, flexible, franjeado) -->
        <path d="M 0 65 C -25 40, ${(-38 + bend * 0.5).toFixed(1)} 5, ${(-34 + bend * 0.8).toFixed(1)} -35 C ${(-24 + bend).toFixed(1)} -65, ${(-12 + bend * 1.1).toFixed(1)} -85, 0 -95 C 0 -95, 0 65, 0 65 Z" fill="#92400E" stroke="${S}" stroke-width="3.5" stroke-linejoin="round"/>

        <!-- Franjas transversales leonadas de rapaz -->
        <path d="M 0 -50 C -12 -56, -24 -62, ${-30 + bend * 0.6} -64" stroke="#B45309" stroke-width="4.5" stroke-linecap="round"/>
        <path d="M 0 -25 C -12 -31, -24 -37, ${-30 + bend * 0.6} -39" stroke="#B45309" stroke-width="4.5" stroke-linecap="round"/>
        <path d="M 0 0 C -12 -6, -24 -12, -30 -14" stroke="#B45309" stroke-width="4.5" stroke-linecap="round"/>
        <path d="M 0 25 C -12 19, -24 13, -30 11" stroke="#B45309" stroke-width="4.5" stroke-linecap="round"/>

        <!-- Barbas individuales finas a 45° -->
        <line x1="0" y1="-70" x2="${-22 + bend * 0.5}" y2="-86" stroke="#FDE68A" stroke-width="1.2" opacity="0.65"/>
        <line x1="0" y1="-40" x2="${-22 + bend * 0.5}" y2="-56" stroke="#FDE68A" stroke-width="1.2" opacity="0.65"/>
        <line x1="0" y1="-10" x2="${-22 + bend * 0.5}" y2="-26" stroke="#FDE68A" stroke-width="1.2" opacity="0.65"/>
        <line x1="0" y1="20" x2="-22" y2="4" stroke="#FDE68A" stroke-width="1.2" opacity="0.65"/>

        <!-- 4. RAQUIS CENTRAL (Viga cónica de queratina blanca con surco) -->
        <path d="M -2.5 65 Q ${(bend * 0.5).toFixed(1)} -15, ${(bend * 1.1).toFixed(1)} -95 L ${(1.5 + bend * 1.1).toFixed(1)} -95 Q ${(2 + bend * 0.5).toFixed(1)} -15, 2.5 65 Z" fill="#FFFFFF" stroke="${S}" stroke-width="2.5"/>
        <line x1="0" y1="65" x2="${(bend * 0.8).toFixed(1)}" y2="-92" stroke="#CBD5E1" stroke-width="1.5"/>

        <!-- Rótulo anatómico -->
        <g transform="translate(44, -50)">
          <rect x="-4" y="-10" width="88" height="15" rx="3" fill="#0F172A" stroke="#FBBF24" stroke-width="1.5"/>
          <text x="40" y="0" fill="#FBBF24" font-size="7.5" font-family="'Arial Black', sans-serif" font-weight="900" text-anchor="middle">RAQUIS ASIMÉTRICO</text>
        </g>
      </g>`;
    },
    tags: ["pluma", "aguila", "metamaterial", "viscoelastico", "raquis", "vexilo"],
  },'''

text = re.sub(r'  pluma_aguila_metamaterial: \{[\s\S]*?tags: \["pluma", "aguila", "metamaterial", "viscoelastico", "raquis", "vexilo"\],\n  \},', pluma_clean, text)

# 4. sensor_herbst_corpúsculo
sensor_clean = '''  "sensor_herbst_corpúsculo": {
    id: "sensor_herbst_corpúsculo",
    name: "Corpúsculo de Herbst en Folículo Plumoso",
    family: "educacion_ciencia",
    defaultPlacement: "right",
    svg: `<ellipse cx="0" cy="0" rx="30" ry="20" fill="#F472B6" stroke="#000" stroke-width="3"/>`,
    animatedSvg: (f: number, progress = 0, state = "disparo_bioelectrico") => {
      const pulse = (f * 18) % 100;
      const S = "#0F172A";

      return `<g transform="scale(1.15)">
        <!-- 1. CAPA DE PIEL / EPIDERMIS Y DERMIS -->
        <rect x="-80" y="-45" width="160" height="20" fill="#475569" stroke="${S}" stroke-width="3"/>
        <line x1="-75" y1="-35" x2="75" y2="-35" stroke="#94A3B8" stroke-width="2" stroke-dasharray="6 4"/>
        <text x="-70" y="-48" fill="#94A3B8" font-size="8" font-family="'Arial Black', sans-serif" font-weight="900">EPIDERMIS AVIAR</text>

        <!-- 2. FOLÍCULO Y CÁLAMO DE LA PLUMA -->
        <g transform="translate(-25, -25) rotate(-15)">
          <path d="M -6 -50 L -6 45 C -6 52, 6 52, 6 45 L 6 -50 Z" fill="#F8FAFC" stroke="${S}" stroke-width="3.5"/>
          <line x1="0" y1="-45" x2="0" y2="40" stroke="#CBD5E1" stroke-width="2"/>
          <text x="-5" y="-55" fill="#F8FAFC" font-size="8" font-family="'Arial Black', sans-serif" font-weight="900" text-anchor="middle">CÁLAMO DE LA PLUMA</text>
        </g>
        <path d="M -42 -25 C -42 20, -18 35, -5 20 C -5 -15, -15 -25, -20 -25" fill="#64748B" opacity="0.4"/>

        <!-- 3. CORPÚSCULO DE HERBST LAMINADO -->
        <g transform="translate(25, 5)">
          <ellipse cx="0" cy="0" rx="41.6" ry="32" fill="none" stroke="#FBBF24" stroke-width="1.8" opacity="0.4"/>
          <ellipse cx="0" cy="0" rx="33.8" ry="26" fill="none" stroke="#FBBF24" stroke-width="1.8" opacity="0.55"/>
          <ellipse cx="0" cy="0" rx="26" ry="20" fill="none" stroke="#FBBF24" stroke-width="1.8" opacity="0.7"/>
          <ellipse cx="0" cy="0" rx="18.2" ry="14" fill="none" stroke="#FBBF24" stroke-width="1.8" opacity="0.85"/>
          <ellipse cx="0" cy="0" rx="10.4" ry="8" fill="#EC4899" stroke="#F43F5E" stroke-width="3" opacity="1"/>
          <circle cx="0" cy="0" r="3.5" fill="#FFFFFF" stroke="${S}" stroke-width="1.5"/>

          <g transform="translate(0, -38)">
            <rect x="-48" y="-10" width="96" height="15" rx="3" fill="#0F172A" stroke="#EC4899" stroke-width="1.5"/>
            <text x="0" y="0" fill="#F472B6" font-size="7.5" font-family="'Arial Black', sans-serif" font-weight="900" text-anchor="middle">CORPÚSCULO HERBST</text>
          </g>
        </g>

        <!-- 4. NERVIO AFERENTE DISPARANDO IMPULSOS BIOELÉCTRICOS (> 800 HZ) -->
        <path d="M 25 15 C 35 40, 50 48, 75 45" fill="none" stroke="#FACC15" stroke-width="4" stroke-dasharray="8 4"/>
        <circle cx="${(25 + pulse * 0.5).toFixed(1)}" cy="${(15 + pulse * 0.3).toFixed(1)}" r="6" fill="#FFE600"/>
        <circle cx="${(25 + pulse * 0.5).toFixed(1)}" cy="${(15 + pulse * 0.3).toFixed(1)}" r="12" fill="#FFE600" opacity="0.3"/>

        <g transform="translate(48, 25)">
          <rect x="-5" y="-9" width="42" height="14" rx="2" fill="#000000" stroke="#FFE600" stroke-width="1.2"/>
          <text x="16" y="1" fill="#FFE600" font-size="7" font-family="'Arial Black', sans-serif" font-weight="900" text-anchor="middle">&gt; 800 Hz</text>
        </g>
      </g>`;
    },
    tags: ["herbst", "sensor", "foliculo", "pluma", "mecanoreceptor"],
  },'''

text = re.sub(r'  "sensor_herbst_corpúsculo": \{[\s\S]*?tags: \["herbst", "sensor", "foliculo", "pluma", "mecanoreceptor"\],\n  \},', sensor_clean, text)

with open(props_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Props reparados exitosamente sin JS embebido!")
