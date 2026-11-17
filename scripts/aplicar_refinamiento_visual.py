# scripts/aplicar_refinamiento_visual.py
import re

# 1. ACTUALIZAR propsLibrary.ts
props_path = "src/stickman/propsLibrary.ts"
with open(props_path, "r", encoding="utf-8") as f:
    text = f.read()

# alula_morfologia_activa sin agujeros óseos que parezcan ojos
alula_clean = '''  alula_morfologia_activa: {
    id: "alula_morfologia_activa",
    name: "Morfología Activa del Álula (Tobera Venturi)",
    family: "educacion_ciencia",
    defaultPlacement: "right",
    svg: `<g>
      <path d="M -50 15 C -25 -25, 25 -25, 50 15 Z" fill="#38BDF8" stroke="#000000" stroke-width="3"/>
    </g>`,
    animatedSvg: (f: number, progress = 0, state = "alula_desplegada_tobera") => {
      const isDeployed = state === "alula_desplegada_tobera" || state === "inyeccion_chorro" || state === "apertura_activa";
      const alulaAngle = isDeployed ? -24 : -4;
      const S = "#0F172A";

      return `<g transform="scale(1.15)">
        <!-- 1. PLUMAS REMERAS DE VUELO (Borde de fuga del ala) -->
        <g>
          <path d="M -75 22 C -95 10, -98 -10, -78 -18 C -62 -22, -50 -12, -54 18 Z" fill="#1E293B" stroke="${S}" stroke-width="3"/>
          <line x1="-75" y1="20" x2="-62" y2="-16" stroke="#F8FAFC" stroke-width="2"/>
          <path d="M -85 2 C -88 -6, -82 -12, -74 -15" stroke="#FBBF24" stroke-width="1.8" fill="none"/>

          <path d="M -54 24 C -72 12, -74 -8, -56 -16 C -42 -20, -32 -10, -36 20 Z" fill="#334155" stroke="${S}" stroke-width="3"/>
          <line x1="-54" y1="22" x2="-42" y2="-14" stroke="#F8FAFC" stroke-width="2"/>
          <path d="M -64 4 C -68 -4, -62 -10, -54 -13" stroke="#FBBF24" stroke-width="1.8" fill="none"/>

          <path d="M -34 26 C -48 14, -50 -6, -34 -14 C -22 -16, -14 -8, -18 22 Z" fill="#475569" stroke="${S}" stroke-width="3"/>
          <line x1="-34" y1="24" x2="-24" y2="-12" stroke="#F8FAFC" stroke-width="1.8"/>
        </g>

        <!-- 2. COBERTERAS Y ANATOMÍA ALAR (Plumaje estratificado natural) -->
        <path d="M -60 16 C -35 -26, 25 -30, 68 8 C 55 24, -15 28, -60 16 Z" fill="#334155" stroke="${S}" stroke-width="4" stroke-linejoin="round"/>
        <path d="M -42 10 C -24 -16, 18 -20, 52 4 C 40 16, -10 18, -42 10 Z" fill="#475569" stroke="${S}" stroke-width="2.8"/>
        <path d="M -22 6 C -8 -10, 22 -12, 48 2 C 38 12, -4 14, -22 6 Z" fill="#64748B" stroke="${S}" stroke-width="2.5"/>
        <path d="M 0 0 C 14 -6, 32 -6, 44 2" stroke="#94A3B8" stroke-width="2" fill="none" stroke-linecap="round"/>

        <!-- Borde de ataque redondeado carnoso (la muñeca / carpo) -->
        <path d="M 44 2 C 60 4, 68 12, 58 18 C 48 22, 36 16, 44 2 Z" fill="#94A3B8" stroke="${S}" stroke-width="2.8"/>

        <!-- 3. EL ÁLULA (3 PLUMAS ALULARES PROPIAS ARTICULADAS EN EL PULGAR) -->
        <g transform="translate(48, -2) rotate(${alulaAngle})">
          <path d="M 4 -2 C 16 -10, 30 -12, 40 -6 C 30 -3, 16 0, 4 0 Z" fill="#CBD5E1" stroke="${S}" stroke-width="2"/>
          <line x1="4" y1="-1" x2="38" y2="-7" stroke="#FFFFFF" stroke-width="1.5"/>

          <path d="M 6 -5 C 20 -15, 40 -17, 54 -9 C 40 -4, 22 -1, 6 -2 Z" fill="#FFE600" stroke="${S}" stroke-width="2.5"/>
          <path d="M 38 -12 C 45 -11, 50 -10, 54 -9 C 47 -6, 40 -5, 36 -7 Z" fill="#0F172A"/>
          <line x1="6" y1="-3.5" x2="48" y2="-10" stroke="#FFFFFF" stroke-width="1.8"/>

          <path d="M 4 -8 C 14 -16, 28 -18, 38 -12 C 28 -9, 16 -6, 4 -5 Z" fill="#FBBF24" stroke="${S}" stroke-width="2"/>
          <line x1="4" y1="-6.5" x2="34" y2="-13" stroke="#FFFFFF" stroke-width="1.2"/>

          <g transform="translate(26, -20)">
            <rect x="-24" y="-8" width="48" height="13" rx="3" fill="#0F172A" stroke="#FFE600" stroke-width="1.2"/>
            <text x="0" y="2" fill="#FFE600" font-size="7" font-family="'Arial Black', sans-serif" font-weight="900" text-anchor="middle">ÁLULA</text>
          </g>
        </g>

        <!-- 4. CHORRO VENTURI Y RANURA DE FLUJO ACELERADO -->
        ${isDeployed ? `
          <path d="M 65 2 C 45 -18, 10 -22, -45 -8 Q -60 -2, -75 12" fill="none" stroke="#10B981" stroke-width="3.5" stroke-dasharray="8 4" stroke-linecap="round"/>
          <path d="M 58 7 C 40 -12, 12 -16, -38 -4 Q -52 2, -66 16" fill="none" stroke="#38BDF8" stroke-width="2.5" stroke-linecap="round"/>
          <polygon points="12,-19 2,-14 8,-10" fill="#10B981"/>

          <g transform="translate(12, -30)">
            <rect x="-35" y="-8" width="70" height="13" rx="3" fill="#064E3B" stroke="#10B981" stroke-width="1.2"/>
            <text x="0" y="2" fill="#6EE7B7" font-size="7" font-family="'Arial Black', sans-serif" font-weight="900" text-anchor="middle">TOBERA VENTURI</text>
          </g>
        ` : `
          <path d="M 45 -6 Q 20 -20, -10 -10" fill="none" stroke="#EF4444" stroke-width="2.5" stroke-dasharray="4 3"/>
        `}
      </g>`;
    },
    tags: ["alula", "pulgar", "venturi", "tobera", "plumas", "ala"],
  },'''

text = re.sub(r'  alula_morfologia_activa: \{[\s\S]*?tags: \["alula", "pulgar", "venturi", "tobera", "plumas", "ala"\],\n  \},', alula_clean, text)

# pluma_microestructura_velcro sin letreros gigantes que tapen
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
      const tearY = isTorn ? 20 : 0;
      const S = "#0F172A";

      return `<g transform="scale(1.05)">
        <!-- 1. BARBA SUPERIOR (Tallo de queratina) -->
        <g transform="translate(0, -28)">
          <path d="M -60 0 C -25 -5, 25 -5, 60 0 L 60 7 C 25 2, -25 2, -60 7 Z" fill="#334155" stroke="${S}" stroke-width="2.5"/>
          <line x1="-55" y1="2" x2="55" y2="2" stroke="#94A3B8" stroke-width="1.8"/>
        </g>

        <!-- 2. BÁRBULAS DISTALES CON GANCHILLOS (HÁMULI) -->
        <g transform="translate(0, -21)">
          <g transform="translate(-40, 0)">
            <path d="M 0 0 C 3 7, 7 14, 10 20" fill="none" stroke="#38BDF8" stroke-width="3" stroke-linecap="round"/>
            <path d="M 10 20 C 12 24, 15 25, 14 29 C 12 30, 9 29, 9 26" fill="none" stroke="#FFE600" stroke-width="2.8" stroke-linecap="round"/>
          </g>
          <g transform="translate(-20, 0)">
            <path d="M 0 0 C 3 7, 7 14, 10 20" fill="none" stroke="#38BDF8" stroke-width="3" stroke-linecap="round"/>
            <path d="M 10 20 C 12 24, 15 25, 14 29 C 12 30, 9 29, 9 26" fill="none" stroke="#FFE600" stroke-width="2.8" stroke-linecap="round"/>
          </g>
          <g transform="translate(0, 0)">
            <path d="M 0 0 C 3 7, 7 14, 10 20" fill="none" stroke="#38BDF8" stroke-width="3" stroke-linecap="round"/>
            <path d="M 10 20 C 12 24, 15 25, 14 29 C 12 30, 9 29, 9 26" fill="none" stroke="#FFE600" stroke-width="2.8" stroke-linecap="round"/>
          </g>
          <g transform="translate(20, 0)">
            <path d="M 0 0 C 3 7, 7 14, 10 20" fill="none" stroke="#38BDF8" stroke-width="3" stroke-linecap="round"/>
            <path d="M 10 20 C 12 24, 15 25, 14 29 C 12 30, 9 29, 9 26" fill="none" stroke="#FFE600" stroke-width="2.8" stroke-linecap="round"/>
          </g>
          <g transform="translate(40, 0)">
            <path d="M 0 0 C 3 7, 7 14, 10 20" fill="none" stroke="#38BDF8" stroke-width="3" stroke-linecap="round"/>
            <path d="M 10 20 C 12 24, 15 25, 14 29 C 12 30, 9 29, 9 26" fill="none" stroke="#FFE600" stroke-width="2.8" stroke-linecap="round"/>
          </g>
        </g>

        <!-- 3. BARBA INFERIOR (Tallo receptor) -->
        <g transform="translate(0, ${28 + tearY})">
          <path d="M -60 0 C -25 -5, 25 -5, 60 0 L 60 7 C 25 2, -25 2, -60 7 Z" fill="#334155" stroke="${S}" stroke-width="2.5"/>
          <line x1="-55" y1="2" x2="55" y2="2" stroke="#94A3B8" stroke-width="1.8"/>
        </g>

        <!-- 4. BÁRBULAS PROXIMALES CON CANALES RECEPTORES -->
        <g transform="translate(0, ${28 + tearY})">
          <g transform="translate(-32, 0)">
            <path d="M 0 0 C -3 -7, -7 -14, -8 -20" fill="none" stroke="#818CF8" stroke-width="3" stroke-linecap="round"/>
            <path d="M -8 -20 C -10 -24, -6 -26, -4 -24 C -2 -22, -4 -20, -7 -20" fill="none" stroke="#C084FC" stroke-width="2.8" stroke-linecap="round"/>
          </g>
          <g transform="translate(-12, 0)">
            <path d="M 0 0 C -3 -7, -7 -14, -8 -20" fill="none" stroke="#818CF8" stroke-width="3" stroke-linecap="round"/>
            <path d="M -8 -20 C -10 -24, -6 -26, -4 -24 C -2 -22, -4 -20, -7 -20" fill="none" stroke="#C084FC" stroke-width="2.8" stroke-linecap="round"/>
          </g>
          <g transform="translate(8, 0)">
            <path d="M 0 0 C -3 -7, -7 -14, -8 -20" fill="none" stroke="#818CF8" stroke-width="3" stroke-linecap="round"/>
            <path d="M -8 -20 C -10 -24, -6 -26, -4 -24 C -2 -22, -4 -20, -7 -20" fill="none" stroke="#C084FC" stroke-width="2.8" stroke-linecap="round"/>
          </g>
          <g transform="translate(28, 0)">
            <path d="M 0 0 C -3 -7, -7 -14, -8 -20" fill="none" stroke="#818CF8" stroke-width="3" stroke-linecap="round"/>
            <path d="M -8 -20 C -10 -24, -6 -26, -4 -24 C -2 -22, -4 -20, -7 -20" fill="none" stroke="#C084FC" stroke-width="2.8" stroke-linecap="round"/>
          </g>
          <g transform="translate(48, 0)">
            <path d="M 0 0 C -3 -7, -7 -14, -8 -20" fill="none" stroke="#818CF8" stroke-width="3" stroke-linecap="round"/>
            <path d="M -8 -20 C -10 -24, -6 -26, -4 -24 C -2 -22, -4 -20, -7 -20" fill="none" stroke="#C084FC" stroke-width="2.8" stroke-linecap="round"/>
          </g>
        </g>

        <!-- 5. ETIQUETA DISCRETA DE ESTADO -->
        ${!isTorn ? `
          <g transform="translate(0, 2)">
            <rect x="-50" y="-8" width="100" height="16" rx="3" fill="#064E3B" stroke="#10B981" stroke-width="1.2" opacity="0.9"/>
            <text x="0" y="3" fill="#6EE7B7" font-size="7.5" font-family="'Arial Black', sans-serif" font-weight="900" text-anchor="middle">
              ${isRepair ? "AUTO-REPARACIÓN (CLIC)" : "HÁMULI ENGANCHADOS"}
            </text>
          </g>
        ` : `
          <g transform="translate(0, 10)">
            <rect x="-45" y="-8" width="90" height="16" rx="3" fill="#450A0A" stroke="#EF4444" stroke-width="1.2" opacity="0.9"/>
            <text x="0" y="3" fill="#FCA5A5" font-size="7.5" font-family="'Arial Black', sans-serif" font-weight="900" text-anchor="middle">
              RUPTURA ELÁSTICA
            </text>
          </g>
        `}
      </g>`;
    },
    tags: ["velcro", "barbula", "hamuli", "queratina", "nanomaterial", "microscopio"],
  },'''

text = re.sub(r'  pluma_microestructura_velcro: \{[\s\S]*?tags: \["velcro", "barbula", "hamuli", "queratina", "nanomaterial", "microscopio"\],\n  \},', velcro_clean, text)

with open(props_path, "w", encoding="utf-8") as f:
    f.write(text)
print("Props actualizados limpiamente en propsLibrary.ts!")

# 2. ACTUALIZAR POSICIONES EN guion.json PARA CAP 2 ESC 4 Y CAP 3 ESC 5
import json

with open("src/data/guion.json", "r", encoding="utf-8") as f:
    guion = json.load(f)

# Cap 2 Esc 4: Mover alula_morfologia_activa a x: 140, y: 15 para no colisionar con la paloma ni con el zoombox
for c in guion["capitulos"]:
    if c["numero"] == 2:
        for e in c["escenas"]:
            if e["id"] == 4:
                for obj in e.get("objetos", []):
                    if obj["propId"] == "alula_morfologia_activa":
                        obj["posicion"] = {"x": 120, "y": 30}
                        obj["escala"] = 1.05
                    elif obj["propId"] == "paloma_aterrizaje_turbulento":
                        obj["posicion"] = {"x": -160, "y": -20}
                        obj["escala"] = 0.95

# Cap 3 Esc 5: Separar la pluma y la microestructura
for c in guion["capitulos"]:
    if c["numero"] == 3:
        for e in c["escenas"]:
            if e["id"] == 5:
                for obj in e.get("objetos", []):
                    if obj["propId"] == "pluma_aguila_metamaterial":
                        obj["posicion"] = {"x": -90, "y": 0}
                        obj["escala"] = 1.0
                    elif obj["propId"] == "pluma_microestructura_velcro":
                        obj["posicion"] = {"x": 160, "y": 20}
                        obj["escala"] = 1.05

with open("src/data/guion.json", "w", encoding="utf-8") as f:
    json.dump(guion, f, indent=2, ensure_ascii=False)

print("Posiciones de escena optimizadas en guion.json!")
