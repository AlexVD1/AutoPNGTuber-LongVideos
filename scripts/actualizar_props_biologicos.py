# scripts/actualizar_props_biologicos.py
import re

print("Actualizando props biológicos anatómicos y recuadros educativos...")

# 1. ACTUALIZAR PROPS EN propsLibrary.ts
props_path = "src/stickman/propsLibrary.ts"
with open(props_path, "r", encoding="utf-8") as f:
    props_code = f.read()

# Reemplazo de alula_morfologia_activa
alula_old = r'  alula_morfologia_activa: \{[\s\S]*?tags: \["alula", "pulgar", "venturi", "tobera"\],\n  \},'
alula_new = '''  alula_morfologia_activa: {
    id: "alula_morfologia_activa",
    name: "Morfología Activa del Álula (Tobera Venturi)",
    family: "educacion_ciencia",
    defaultPlacement: "right",
    svg: `<g>
      <path d="M -50 15 C -25 -25, 25 -25, 50 15 Z" fill="#38BDF8" stroke="#000000" stroke-width="3"/>
    </g>`,
    animatedSvg: (f: number, progress = 0, state = "alula_desplegada_tobera") => {
        const isDeployed = state === "alula_desplegada_tobera" || state === "inyeccion_chorro" || state === "apertura_activa";
        const alulaAngle = isDeployed ? -28 : -6;

        return `<g transform="scale(1.3)">
          <!-- 1. PLUMAS REMERAS DE VUELO (Borde de fuga hacia atrás) -->
          <g opacity="0.95">
            <path d="M -60 16 C -75 8, -78 -6, -60 -12 C -46 -15, -38 -8, -42 14 Z" fill="#1E293B" stroke="#0F172A" stroke-width="3"/>
            <line x1="-60" y1="14" x2="-48" y2="-10" stroke="#F8FAFC" stroke-width="1.8"/>
            
            <path d="M -44 18 C -58 10, -56 -6, -40 -14 C -28 -16, -18 -8, -24 16 Z" fill="#334155" stroke="#0F172A" stroke-width="3"/>
            <line x1="-44" y1="16" x2="-30" y2="-12" stroke="#F8FAFC" stroke-width="1.8"/>
          </g>

          <!-- 2. PERFIL ANATÓMICO DEL ALA (Corte sagital con plumaje superpuesto) -->
          <path d="M -55 14 C -35 -20, 15 -24, 55 6 C 42 20, -15 24, -55 14 Z" fill="#475569" stroke="#0F172A" stroke-width="4" stroke-linejoin="round"/>
          
          <!-- Coberteras medianas y mayores (plumaje en escamas) -->
          <path d="M -38 8 C -26 -12, 6 -16, 38 2 C 26 14, -12 16, -38 8 Z" fill="#64748B" stroke="#0F172A" stroke-width="2.5"/>
          <path d="M -20 4 C -10 -8, 12 -10, 32 3" fill="none" stroke="#94A3B8" stroke-width="2" stroke-linecap="round"/>
          
          <!-- Borde de ataque redondeado carnoso -->
          <path d="M 38 2 C 55 4, 58 12, 48 18 C 40 20, 30 14, 38 2 Z" fill="#94A3B8" stroke="#0F172A" stroke-width="2.5"/>

          <!-- Huesos alares en corte anatómico (Cúbito y Radio) -->
          <ellipse cx="8" cy="4" rx="7" ry="5.5" fill="#F8FAFC" stroke="#0F172A" stroke-width="2.2"/>
          <circle cx="8" cy="4" r="2.2" fill="#CBD5E1"/>
          <ellipse cx="-15" cy="6" rx="5.5" ry="4.5" fill="#F8FAFC" stroke="#0F172A" stroke-width="2"/>
          <circle cx="-15" cy="6" r="1.8" fill="#CBD5E1"/>

          <!-- 3. EL ÁLULA (DÍGITO I / PULGAR AVIAR MÓVIL) -->
          <g transform="translate(42, -4) rotate(${alulaAngle})">
            <!-- Falange ósea del pulgar -->
            <ellipse cx="0" cy="0" rx="3.5" ry="2.2" fill="#F8FAFC" stroke="#0F172A" stroke-width="1.8"/>

            <!-- 3 Plumas alulares escalonadas -->
            <!-- Pluma 1 inferior -->
            <path d="M 4 -3 C 14 -10, 26 -12, 34 -7 C 25 -4, 15 -1, 4 -1 Z" fill="#CBD5E1" stroke="#0F172A" stroke-width="2"/>
            <line x1="4" y1="-2" x2="32" y2="-8" stroke="#F8FAFC" stroke-width="1.5"/>

            <!-- Pluma 2 principal (con punta oscura característica de rapaz) -->
            <path d="M 6 -6 C 18 -15, 34 -17, 46 -10 C 35 -5, 20 -2, 6 -3 Z" fill="#FFE600" stroke="#0F172A" stroke-width="2.5"/>
            <path d="M 34 -13 C 39 -12, 43 -11, 46 -10 C 41 -7, 36 -6, 32 -8 Z" fill="#0F172A"/>
            <line x1="6" y1="-4" x2="42" y2="-11" stroke="#FFFFFF" stroke-width="1.8"/>

            <!-- Pluma 3 superior de apoyo -->
            <path d="M 4 -8 C 13 -16, 24 -18, 32 -13 C 24 -10, 14 -7, 4 -5 Z" fill="#FBBF24" stroke="#0F172A" stroke-width="2"/>
            <line x1="4" y1="-7" x2="28" y2="-14" stroke="#FFFFFF" stroke-width="1.2"/>

            <!-- Rótulo técnico diegético sobre el pulgar -->
            <g transform="translate(20, -22)">
              <rect x="-32" y="-10" width="64" height="13" rx="3" fill="#0F172A" stroke="#FFE600" stroke-width="1.2"/>
              <text x="0" y="-1" fill="#FFE600" font-size="7" font-family="'Arial Black', sans-serif" font-weight="900" text-anchor="middle">ÁLULA (PULGAR)</text>
            </g>
          </g>

          <!-- 4. CHORRO VENTURI ACELERADO Y RANURA BIOLÓGICA -->
          ${isDeployed ? `
            <path d="M 58 0 C 42 -18, 8 -22, -40 -8 Q -52 -2, -65 10" fill="none" stroke="#10B981" stroke-width="4" stroke-dasharray="8 4" stroke-linecap="round"/>
            <path d="M 52 5 C 38 -12, 10 -16, -34 -4 Q -46 2, -58 14" fill="none" stroke="#38BDF8" stroke-width="2.8" stroke-linecap="round"/>
            <polygon points="10,-20 0,-15 6,-11" fill="#10B981"/>

            <!-- Rótulo de Tobera Venturi -->
            <g transform="translate(14, -34)">
              <rect x="-38" y="-10" width="76" height="14" rx="3" fill="#064E3B" stroke="#10B981" stroke-width="1.2"/>
              <text x="0" y="0" fill="#6EE7B7" font-size="7.5" font-family="'Arial Black', sans-serif" font-weight="900" text-anchor="middle">RANURA VENTURI</text>
            </g>
          ` : `
            <path d="M 40 -8 Q 15 -22, -15 -12" fill="none" stroke="#EF4444" stroke-width="2.5" stroke-dasharray="4 3"/>
          `}
        </g>`;
      },
    tags: ["alula", "pulgar", "venturi", "tobera", "plumas", "ala"],
  },'''

props_code, n1 = re.subn(alula_old, alula_new, props_code)
print(f"alula_morfologia_activa reemplazada: {n1 > 0}")

# Reemplazo de pluma_microestructura_velcro
velcro_old = r'  pluma_microestructura_velcro: \{[\s\S]*?tags: \["velcro", "barbula", "hamuli", "queratina", "nanomaterial"\],\n  \},'
velcro_new = '''  pluma_microestructura_velcro: {
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
      const tearOffset = isTorn ? 22 : 0;
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
          {[-45, -20, 5, 30, 55].map((x, i) => `
            <g key="hook-${i}" transform="translate(${x}, 0)">
              <path d="M 0 0 C 4 8, 8 16, 12 24" fill="none" stroke="#38BDF8" stroke-width="3.5" stroke-linecap="round"/>
              <path d="M 12 24 C 14 28, 18 30, 16 34 C 14 36, 10 34, 11 31" fill="none" stroke="#FFE600" stroke-width="3" stroke-linecap="round"/>
              <path d="M 9 18 C 11 22, 15 24, 13 28 C 11 30, 8 28, 9 25" fill="none" stroke="#FFE600" stroke-width="2.5" stroke-linecap="round"/>
            </g>
          `).join("")}
        </g>

        <!-- 3. BARBA INFERIOR (Tallo receptor) -->
        <g transform="translate(0, ${32 + tearOffset})">
          <path d="M -70 0 C -30 -6, 30 -6, 70 0 L 70 8 C 30 2, -30 2, -70 8 Z" fill="#334155" stroke="${S}" stroke-width="3"/>
          <line x1="-65" y1="2" x2="65" y2="2" stroke="#94A3B8" stroke-width="2"/>
          <text x="-65" y="20" fill="#94A3B8" font-size="8" font-family="'Arial Black', sans-serif" font-weight="900">BARBA INFERIOR</text>
        </g>

        <!-- 4. BÁRBULAS PROXIMALES CON CANALES RECEPTORES -->
        <g transform="translate(0, ${32 + tearOffset})">
          {[-45, -20, 5, 30, 55].map((x, i) => `
            <g key="trough-${i}" transform="translate(${x + 8}, 0)">
              <path d="M 0 0 C -4 -8, -8 -16, -10 -24" fill="none" stroke="#818CF8" stroke-width="3.5" stroke-linecap="round"/>
              <path d="M -10 -24 C -12 -28, -8 -30, -5 -28 C -3 -26, -5 -24, -8 -24" fill="none" stroke="#C084FC" stroke-width="3" stroke-linecap="round"/>
            </g>
          `).join("")}
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

props_code, n2 = re.subn(velcro_old, velcro_new, props_code)
print(f"pluma_microestructura_velcro reemplazada: {n2 > 0}")

# Reemplazo de plumas_asimetricas_persiana
persiana_old = r'  plumas_asimetricas_persiana: \{[\s\S]*?tags: \["persiana", "asimetria", "aleteo", "valvula", "downstroke"\],\n  \},'
persiana_new = '''  plumas_asimetricas_persiana: {
    id: "plumas_asimetricas_persiana",
    name: "Persiana Aerodinámica Asimétrica de Plumas",
    family: "educacion_ciencia",
    defaultPlacement: "right",
    svg: `<rect x="-30" y="-12" width="60" height="24" rx="4" fill="#1E293B" stroke="#000" stroke-width="3"/>`,
    animatedSvg: (f: number, progress = 0, state = "bajada_sellada") => {
      const isDown = state === "bajada_sellada";
      const isUp = state === "subida_persiana_45";
      const featherRot = isDown ? 0 : (isUp ? 42 : 20);
      const S = "#0F172A";

      return `<g transform="scale(1.2)">
        <!-- 4 PLUMAS REMERAS SUPERPUESTAS EN CORTE TRANSVERSAL -->
        {[-48, -16, 16, 48].map((x, i) => `
          <g key="feather-${i}" transform="translate(${x}, 0) rotate(${featherRot})">
            <!-- Raquis cilíndrico blanco descentrado (asimétrico) -->
            <ellipse cx="6" cy="0" rx="4.5" ry="4" fill="#FFFFFF" stroke="${S}" stroke-width="2.5"/>
            <circle cx="6" cy="0" r="1.8" fill="#CBD5E1"/>

            <!-- Vexilo ancho aerodinámico (lámina curva de pluma) -->
            <path d="M 6 -3.5 C -6 -5, -20 -3, -28 3 C -20 5, -6 3, 6 3.5 Z" fill="${isDown ? '#334155' : '#0284C7'}" stroke="${S}" stroke-width="2.5" stroke-linejoin="round"/>
            <!-- Vexilo estrecho opuesto -->
            <path d="M 6 -3.5 C 10 -4, 14 -2, 16 0 C 14 2, 10 3, 6 3.5 Z" fill="${isDown ? '#1E293B' : '#0369A1'}" stroke="${S}" stroke-width="2"/>
            <path d="M -15 -1 C -8 -2, 0 -1, 4 0" stroke="#FBBF24" stroke-width="1.8" fill="none"/>
          </g>
        `).join("")}

        <!-- FLUJO DE AIRE SEGÚN ESTADO DE LA BATIDA -->
        ${isDown ? `
          <line x1="-55" y1="5" x2="55" y2="5" stroke="#10B981" stroke-width="3" stroke-dasharray="6 3"/>
          {[-32, 0, 32].map((x, i) => `
            <g key="lift-${i}" transform="translate(${x}, 28)">
              <line x1="0" y1="0" x2="0" y2="-18" stroke="#10B981" stroke-width="3.5"/>
              <polygon points="0,-24 -5,-16 5,-16" fill="#10B981"/>
            </g>
          `).join("")}

          <g transform="translate(0, -22)">
            <rect x="-65" y="-11" width="130" height="18" rx="4" fill="#064E3B" stroke="#10B981" stroke-width="1.5"/>
            <text x="0" y="2" fill="#6EE7B7" font-size="8" font-family="'Arial Black', sans-serif" font-weight="900" text-anchor="middle">
              DOWNSTROKE: SELLADO 100%
            </text>
          </g>
        ` : `
          {[-32, 0, 32].map((x, i) => `
            <g key="flow-${i}" transform="translate(${x}, -22)">
              <path d="M 0 0 L 0 44" stroke="#38BDF8" stroke-width="3" stroke-dasharray="6 4"/>
              <polygon points="0,48 -4,40 4,40" fill="#38BDF8"/>
            </g>
          `).join("")}

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

props_code, n3 = re.subn(persiana_old, persiana_new, props_code)
print(f"plumas_asimetricas_persiana reemplazada: {n3 > 0}")

# Reemplazo de pluma_aguila_metamaterial
pluma_old = r'  pluma_aguila_metamaterial: \{[\s\S]*?tags: \["pluma", "aguila", "metamaterial", "viscoelastico"\],\n  \},'
pluma_new = '''  pluma_aguila_metamaterial: {
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
        {[-30, -5, 20, 45].map((y, i) => `
          <path key="ext-${i}" d="M 0 ${y} L ${11 + (y < 0 ? bend * 0.6 : 0)} ${y - 12}" stroke="#451A03" stroke-width="3" stroke-linecap="round"/>
        `).join("")}

        <!-- 3. VEXILO INTERNO / BORDE DE FUGA (Ancho, flexible, franjeado) -->
        <path d="M 0 65 C -25 40, ${(-38 + bend * 0.5).toFixed(1)} 5, ${(-34 + bend * 0.8).toFixed(1)} -35 C ${(-24 + bend).toFixed(1)} -65, ${(-12 + bend * 1.1).toFixed(1)} -85, 0 -95 C 0 -95, 0 65, 0 65 Z" fill="#92400E" stroke="${S}" stroke-width="3.5" stroke-linejoin="round"/>

        <!-- Franjas transversales leonadas de rapaz -->
        {[-50, -25, 0, 25, 50].map((y, i) => `
          <path key="band-${i}" d="M 0 ${y} C -12 ${y - 6}, -24 ${y - 12}, ${-30 + (y < 0 ? bend * 0.6 : 0)} ${y - 14}" stroke="#B45309" stroke-width="4.5" stroke-linecap="round"/>
          <path key="dark-${i}" d="M 0 ${y + 8} C -10 ${y + 2}, -22 ${y - 4}, ${-26 + (y < 0 ? bend * 0.6 : 0)} ${y - 6}" stroke="#451A03" stroke-width="3.5" stroke-linecap="round"/>
        `).join("")}

        <!-- Barbas individuales finas a 45° -->
        {[-70, -40, -10, 15, 40].map((y, i) => `
          <line key="barba-${i}" x1="0" y1="${y}" x2="${-22 + (y < 0 ? bend * 0.5 : 0)}" y2="${y - 16}" stroke="#FDE68A" stroke-width="1.2" opacity="0.65"/>
          <line key="barba-ext-${i}" x1="0" y1="${y}" x2="${10 + (y < 0 ? bend * 0.4 : 0)}" y2="${y - 14}" stroke="#FDE68A" stroke-width="1.2" opacity="0.65"/>
        `).join("")}

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

props_code, n4 = re.subn(pluma_old, pluma_new, props_code)
print(f"pluma_aguila_metamaterial reemplazada: {n4 > 0}")

# Reemplazo de sensor_herbst_corpúsculo
sensor_old = r'  "sensor_herbst_corpúsculo": \{[\s\S]*?tags: \["herbst", "sensor"\],\n  \},'
sensor_new = '''  "sensor_herbst_corpúsculo": {
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
          {[32, 26, 20, 14, 8].map((r, i) => `
            <ellipse key="lamina-${i}" cx="0" cy="0" rx="${r * 1.3}" ry="${r}" fill="${i === 4 ? '#EC4899' : 'none'}" stroke="${i === 4 ? '#F43F5E' : '#FBBF24'}" stroke-width="${i === 4 ? '3' : '1.8'}" opacity="${0.4 + i * 0.15}"/>
          `).join("")}
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

props_code, n5 = re.subn(sensor_old, sensor_new, props_code)
print(f"sensor_herbst_corpúsculo reemplazado: {n5 > 0}")

# Reemplazo de vortice_borde_ataque_lev
lev_old = r'  vortice_borde_ataque_lev: \{[\s\S]*?tags: \["vortice", "lev", "succion", "espiral"\],\n  \},'
lev_new = '''  vortice_borde_ataque_lev: {
    id: "vortice_borde_ataque_lev",
    name: "Vórtice de Borde de Ataque (LEV)",
    family: "educacion_ciencia",
    defaultPlacement: "right",
    svg: `<circle cx="0" cy="0" r="22" fill="none" stroke="#10B981" stroke-width="4"/>`,
    animatedSvg: (f: number, progress = 0, state = "generacion_vortice") => {
      const rot = (f * 12) % 360;
      const S = "#0F172A";

      return `<g transform="scale(1.2)">
        <!-- 1. PUNTA DEL ALA DEL HALCÓN (WINGTIP) -->
        <g transform="translate(-25, 10)">
          <path d="M -30 20 C -20 -15, 10 -25, 35 -15 C 25 -5, 5 15, -15 25 Z" fill="#334155" stroke="${S}" stroke-width="3.5" stroke-linejoin="round"/>
          <path d="M 35 -15 C 48 -25, 54 -18, 42 -10 Z" fill="#1E293B" stroke="${S}" stroke-width="2.5"/>
          <line x1="-15" y1="18" x2="30" y2="-12" stroke="#F8FAFC" stroke-width="2"/>
        </g>

        <!-- 2. VÓRTICE LEV EN ESPIRAL -->
        <g transform="translate(15, -12)">
          <ellipse cx="0" cy="0" rx="26" ry="18" fill="#10B981" opacity="0.25"/>
          <ellipse cx="0" cy="0" rx="16" ry="10" fill="#38BDF8" opacity="0.35"/>

          <g transform="rotate(${rot.toFixed(1)})">
            <path d="M 0 0 C 8 10, 18 8, 20 -2 C 22 -14, 10 -20, -2 -18 C -14 -16, -20 -4, -14 8 C -8 18, 4 20, 14 14" fill="none" stroke="#FFE600" stroke-width="3.5" stroke-linecap="round"/>
            <polygon points="14,14 18,8 10,6" fill="#FFE600"/>
          </g>
          <circle cx="0" cy="0" r="4.5" fill="#FFFFFF" stroke="${S}" stroke-width="2"/>
        </g>

        <!-- 3. VECTOR SUSTENTACIÓN LEV -->
        <g transform="translate(15, -34)">
          <line x1="0" y1="0" x2="0" y2="-22" stroke="#10B981" stroke-width="3.5"/>
          <polygon points="0,-28 -5,-20 5,-20" fill="#10B981"/>
          <text x="8" y="-12" fill="#10B981" font-size="8" font-family="'Arial Black', sans-serif" font-weight="900">LEV LIFT (2.1x)</text>
        </g>

        <g transform="translate(0, 36)">
          <rect x="-55" y="-10" width="110" height="16" rx="3" fill="#064E3B" stroke="#10B981" stroke-width="1.5"/>
          <text x="0" y="2" fill="#6EE7B7" font-size="7.5" font-family="'Arial Black', sans-serif" font-weight="900" text-anchor="middle">VÓRTICE LEV EN PUNTA ALAR</text>
        </g>
      </g>`;
    },
    tags: ["vortice", "lev", "succion", "espiral", "punta_alar"],
  },'''

props_code, n6 = re.subn(lev_old, lev_new, props_code)
print(f"vortice_borde_ataque_lev reemplazado: {n6 > 0}")

with open(props_path, "w", encoding="utf-8") as f:
    f.write(props_code)

print("Props actualizados con éxito en propsLibrary.ts!")
