# scripts/actualizar_zoombox_biologico.py
import re

zoombox_path = "src/components/EducationalZoomBox.tsx"
with open(zoombox_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. UPGRADE alula_tobera_venturi
alula_old = r'  if \(tipo === "alula_tobera_venturi"\) \{[\s\S]*?if \(tipo === "microestructura_velcro_barbula"\) \{'

alula_new = '''  if (tipo === "alula_tobera_venturi") {
    // Alula levantándose e inyectando un chorro de aire de alta velocidad Venturi sobre perfil aviar
    const alulaOpen = 18 + Math.sin(f * 0.15) * 6; // Ángulo de apertura del álula

    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#050C1A" />

        {/* Flujo general de aire incidente a alto ángulo de ataque (42°) */}
        <path d="M 20 185 C 90 165, 140 100, 380 45" fill="none" stroke="#10B981" strokeWidth="2" strokeDasharray="5 3" />
        <path d="M 20 205 C 100 185, 160 130, 380 75" fill="none" stroke="#10B981" strokeWidth="1.5" strokeDasharray="5 3" />

        {/* 1. PERFIL ALAR AVIAR ANATÓMICO A ALTO ÁNGULO DE ATAQUE (32°) */}
        <g transform="translate(180, 135) rotate(-32)">
          <!-- Plumas remeras de vuelo (borde de fuga a la izquierda) -->
          <path d="M -85 10 C -105 2, -110 -12, -90 -16 C -75 -18, -65 -10, -70 12 Z" fill="#1E293B" stroke="#000000" strokeWidth="3" />
          <line x1="-85" y1="8" x2="-68" y2="-14" stroke="#F8FAFC" strokeWidth="1.8" />
          
          <path d="M -65 14 C -82 6, -85 -10, -68 -16 C -54 -18, -45 -8, -50 14 Z" fill="#334155" stroke="#000000" strokeWidth="3" />
          <line x1="-65" y1="12" x2="-50" y2="-14" stroke="#F8FAFC" strokeWidth="1.8" />

          <!-- Cuerpo carnoso del ala con coberteras -->
          <path d="M -75 12 C -50 -26, 25 -30, 85 8 C 70 24, -20 28, -75 12 Z" fill="#475569" stroke="#000000" strokeWidth="4" strokeLinejoin="round" />
          
          <!-- Plumaje de coberteras medianas -->
          <path d="M -50 6 C -35 -14, 10 -18, 55 4 C 42 16, -10 18, -50 6 Z" fill="#64748B" stroke="#000000" strokeWidth="2.5" />
          
          <!-- Hueso alar interno (Carpometacarpo) en corte anatómico -->
          <ellipse cx="14" cy="4" rx="9" ry="7" fill="#F8FAFC" stroke="#000000" strokeWidth="2.5" />
          <circle cx="14" cy="4" r="3" fill="#CBD5E1" />
          <ellipse cx="-16" cy="6" rx="7" ry="5.5" fill="#F8FAFC" stroke="#000000" strokeWidth="2" />
        </g>

        {/* 2. EL ÁLULA (PULGAR AVIAR ARTICULADO FORMANDO LA TOBERA) */}
        <g transform={`translate(108, 115) rotate(${-32 - alulaOpen})`}>
          <!-- Falange del pulgar -->
          <ellipse cx="0" cy="0" rx="4" ry="2.5" fill="#F8FAFC" stroke="#000000" strokeWidth="2" />

          <!-- 3 Plumas alulares con raquis visible -->
          <path d="M 4 -3 C 16 -12, 32 -14, 44 -8 C 32 -4, 18 -1, 4 -1 Z" fill="#CBD5E1" stroke="#000000" strokeWidth="2.2" />
          <line x1="4" y1="-2" x2="40" y2="-9" stroke="#F8FAFC" strokeWidth="1.5" />

          <path d="M 6 -7 C 22 -18, 44 -20, 60 -11 C 46 -5, 26 -1, 6 -3 Z" fill="#FFE600" stroke="#000000" strokeWidth="2.8" />
          <path d="M 46 -15 C 52 -13, 56 -12, 60 -11 C 53 -7, 46 -6, 42 -8 Z" fill="#0F172A" />
          <line x1="6" y1="-5" x2="54" y2="-12" stroke="#FFFFFF" strokeWidth="2" />

          <path d="M 4 -10 C 16 -20, 30 -22, 42 -15 C 32 -11, 18 -7, 4 -6 Z" fill="#FBBF24" stroke="#000000" strokeWidth="2.2" />
          <line x1="4" y1="-9" x2="38" y2="-16" stroke="#FFFFFF" strokeWidth="1.5" />

          <!-- Etiqueta sobre el álula -->
          <g transform="translate(24, -26)">
            <rect x="-35" y="-11" width="70" height="15" rx="3" fill="#0F172A" stroke="#FFE600" strokeWidth="1.5" />
            <text x="0" y="0" fill="#FFE600" fontSize="7.5" fontFamily="'Arial Black', sans-serif" fontWeight="900" textAnchor="middle">ÁLULA (DÍGITO I)</text>
          </g>
        </g>

        {/* 3. CHORRO VENTURI DE ALTA VELOCIDAD INYECTADO SOBRE EL EXTRADÓS */}
        <path
          d="M 102 108 Q 135 78 190 74 Q 270 70 365 82"
          fill="none"
          stroke="#10B981"
          strokeWidth="4.5"
          strokeDasharray="10 4"
        />
        <path
          d="M 96 114 Q 130 84 185 80 Q 265 76 360 88"
          fill="none"
          stroke="#38BDF8"
          strokeWidth="3.2"
        />
        <polygon points="372,83 358,76 358,89" fill="#10B981" />

        <!-- 4. VÓRTICE DE BORDE DE ATAQUE ESTABLE (LEV) -->
        <g transform="translate(195, 68)">
          <circle cx="0" cy="0" r="16" fill="#38BDF8" opacity="0.3" />
          <circle cx="0" cy="0" r="9" fill="none" stroke="#38BDF8" strokeWidth="2.5" strokeDasharray="4 2" />
          <text x="0" y="-14" fill="#38BDF8" fontSize="8" fontFamily="'Arial Black', sans-serif" fontWeight="900" textAnchor="middle">VÓRTICE LEV</text>
        </g>

        <!-- Rótulos técnicos diegéticos -->
        <rect x="20" y="16" width="210" height="24" rx="4" fill="#000000" stroke="#FFE600" strokeWidth="1.5" />
        <text x="26" y="32" fill="#FFE600" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          TOBERA VENTURI BIOLÓGICA (ÁLULA)
        </text>

        <rect x="240" y="16" width="145" height="24" rx="4" fill="#064E3B" stroke="#10B981" strokeWidth="1.5" />
        <text x="246" y="32" fill="#6EE7B7" fontSize="9.5" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          FLUJO ADHERIDO: α = 42°
        </text>
      </svg>
    );
  }

  if (tipo === "microestructura_velcro_barbula") {'''

code, n_alula = re.subn(alula_old, alula_new, code)
print(f"alula_tobera_venturi en EducationalZoomBox reemplazada: {n_alula > 0}")

# 2. UPGRADE microestructura_velcro_barbula
velcro_old = r'  if \(tipo === "microestructura_velcro_barbula"\) \{[\s\S]*?if \(tipo === "valvula_aleteo_persiana"\) \{'

velcro_new = '''  if (tipo === "microestructura_velcro_barbula") {
    // Microestructura nanoscópica de pluma: Raquis, Barbas y Ganchillos (Hamuli)
    const hookCycle = (Math.sin(f * 0.12) + 1) / 2;
    const hookSeparation = interpolate(hookCycle, [0, 1], [0, 16]);

    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#08070F" />

        {/* 1. BARBA SUPERIOR (Tallo cilíndrico de queratina con ramificación de bárbulas) */}
        <g transform="translate(180, 52)">
          <path d="M -160 0 L 190 0 L 190 12 L -160 12 Z" fill="#1E293B" stroke="#94A3B8" strokeWidth="2.5" />
          <line x1="-155" y1="4" x2="185" y2="4" stroke="#F8FAFC" strokeWidth="2" />
          <text x="-150" y="-6" fill="#94A3B8" fontSize="8" fontFamily="'Arial Black', sans-serif" fontWeight="900">BARBA SUPERIOR</text>

          {/* Micro-bárbulas distales con ganchillos curvos hacia abajo (Hámuli) */}
          {[-120, -70, -20, 30, 80, 130].map((bx, i) => (
            <g key={`hook-top-${i}`} transform={`translate(${bx}, 12)`}>
              <!-- Tallo de la bárbula -->
              <path d="M 0 0 C 8 14, 16 28, 22 42" fill="none" stroke="#38BDF8" strokeWidth="4" strokeLinecap="round" />
              <!-- Ganchillos microscópicos dobles (Hámuli) en oro brillante -->
              <path
                d={`M 22 42 C 24 ${48 + hookSeparation * 0.4}, 30 ${52 + hookSeparation * 0.4}, 28 ${58 + hookSeparation * 0.4} C 26 ${62 + hookSeparation * 0.4}, 20 ${58 + hookSeparation * 0.4}, 21 ${52 + hookSeparation * 0.4}`}
                fill="none"
                stroke="#FFE600"
                strokeWidth="3.5"
                strokeLinecap="round"
              />
              <path
                d={`M 17 32 C 19 ${38 + hookSeparation * 0.4}, 25 ${42 + hookSeparation * 0.4}, 23 ${48 + hookSeparation * 0.4} C 21 ${52 + hookSeparation * 0.4}, 16 ${48 + hookSeparation * 0.4}, 17 ${42 + hookSeparation * 0.4}`}
                fill="none"
                stroke="#FFE600"
                strokeWidth="2.8"
                strokeLinecap="round"
              />
            </g>
          ))}
        </g>

        {/* 2. BARBA INFERIOR (Tallo receptor) */}
        <g transform={`translate(180, ${145 + hookSeparation * 0.6})`}>
          <path d="M -160 0 L 190 0 L 190 12 L -160 12 Z" fill="#1E293B" stroke="#94A3B8" strokeWidth="2.5" />
          <line x1="-155" y1="4" x2="185" y2="4" stroke="#F8FAFC" strokeWidth="2" />
          <text x="-150" y="24" fill="#94A3B8" fontSize="8" fontFamily="'Arial Black', sans-serif" fontWeight="900">BARBA INFERIOR</text>

          {/* Micro-bárbulas proximales con canales receptores curvados hacia arriba */}
          {[-120, -70, -20, 30, 80, 130].map((bx, i) => (
            <g key={`hook-bot-${i}`} transform={`translate(${bx + 16}, 0)`}>
              <path d="M 0 0 C -6 -14, -12 -28, -16 -42" fill="none" stroke="#818CF8" strokeWidth="4" strokeLinecap="round" />
              <!-- Canal receptáculo de enganche -->
              <path
                d="M -16 -42 C -20 -50, -12 -54, -8 -50 C -5 -46, -8 -42, -14 -42"
                fill="none"
                stroke="#C084FC"
                strokeWidth="3.5"
                strokeLinecap="round"
              />
            </g>
          ))}
        </g>

        {/* 3. RÓTULOS Y ESCALA NANOMÉTRICA */}
        <rect x="20" y="14" width="225" height="24" rx="4" fill="#000000" stroke="#38BDF8" strokeWidth="1.5" />
        <text x="26" y="30" fill="#38BDF8" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          NANOMALLA VELCRO: HÁMULI Y BÁRBULAS
        </text>

        <rect x="255" y="14" width="130" height="24" rx="4" fill="#000000" stroke="#FFE600" strokeWidth="1.5" />
        <text x="261" y="30" fill="#FFE600" fontSize="9" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          ESCALA: 10 µm (SEM)
        </text>

        <g transform="translate(20, 195)">
          <rect x="0" y="-12" width="180" height="18" rx="3" fill="#064E3B" stroke="#10B981" strokeWidth="1.2" />
          <text x="6" y="0" fill="#6EE7B7" fontSize="8.5" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            AUTO-SELLADO SIN ADHESIVOS
          </text>
        </g>
      </svg>
    );
  }

  if (tipo === "valvula_aleteo_persiana") {'''

code, n_velcro = re.subn(velcro_old, velcro_new, code)
print(f"microestructura_velcro_barbula en EducationalZoomBox reemplazada: {n_velcro > 0}")

with open(zoombox_path, "w", encoding="utf-8") as f:
    f.write(code)

print("EducationalZoomBox.tsx actualizado con éxito!")
