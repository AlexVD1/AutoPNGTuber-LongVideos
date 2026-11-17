import React from "react";
import {
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import {
  CuadrantePantalla,
  PalabraTiming,
  RecuadroEducativoConfig,
  TipoAnimacionEducativa,
} from "../types";
import { resolveTimeRangeFrames } from "../stickman/actionSequences";

export interface EducationalZoomBoxProps {
  config: RecuadroEducativoConfig;
  palabras?: PalabraTiming[];
  durationInFrames: number;
}

export function resolveQuadrantCoordinates(
  posicion: CuadrantePantalla | { x: number; y: number } | undefined,
  boxWidth = 460,
  boxHeight = 310
): { left: number; top: number; origin: string } {
  if (typeof posicion === "object" && "x" in posicion && "y" in posicion) {
    return {
      left: 960 + posicion.x - boxWidth / 2,
      top: 540 + posicion.y - boxHeight / 2,
      origin: "center center",
    };
  }

  const padX = 64;
  const padY = 56;

  switch (posicion) {
    case "superior_izquierda":
      return { left: padX, top: padY, origin: "top left" };
    case "inferior_izquierda":
      return { left: padX, top: 1080 - boxHeight - padY - 70, origin: "bottom left" };
    case "inferior_derecha":
      return { left: 1920 - boxWidth - padX, top: 1080 - boxHeight - padY - 70, origin: "bottom right" };
    case "centro_izquierda":
      return { left: padX, top: (1080 - boxHeight) / 2 - 20, origin: "center left" };
    case "centro":
      return { left: (1920 - boxWidth) / 2, top: (1080 - boxHeight) / 2, origin: "center center" };
    case "centro_derecha":
      return { left: 1920 - boxWidth - padX, top: (1080 - boxHeight) / 2 - 20, origin: "center right" };
    case "superior_derecha":
    default:
      return { left: 1920 - boxWidth - padX, top: padY, origin: "top right" };
  }
}

interface SvgAnimationProps {
  tipo?: TipoAnimacionEducativa;
  localFrame: number;
  width: number;
  height: number;
}

const SimulationSvg: React.FC<SvgAnimationProps> = ({
  tipo,
  localFrame,
  width,
  height,
}) => {
  const f = localFrame;

  if (tipo === "elasticidad_espaciotiempo") {
    // Malla tridimensional de espaciotiempo curvándose bajo una masa
    const dip = 26 + Math.sin(f * 0.12) * 4;
    const orbAngle = f * 0.06;
    const orbX = 200 + Math.cos(orbAngle) * 90;
    const orbY = 110 + Math.sin(orbAngle) * 35;

    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <defs>
          <radialGradient id="sinkGrad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="#0284C7" stopOpacity="0.8" />
            <stop offset="70%" stopColor="#0F172A" stopOpacity="0.2" />
            <stop offset="100%" stopColor="#020617" stopOpacity="0" />
          </radialGradient>
        </defs>

        {/* Fondo de vacío */}
        <rect width="400" height="220" fill="#070D1A" />

        {/* Embudo gravitacional central */}
        <ellipse cx="200" cy={110 + dip * 0.4} rx="120" ry={40 + dip * 0.5} fill="url(#sinkGrad)" />

        {/* Malla espaciotemporal deformable (Líneas horizontales en perspectiva) */}
        {[-3, -2, -1, 0, 1, 2, 3].map((row) => {
          const baseY = 110 + row * 24;
          const curveY = baseY + Math.max(0, 1 - Math.abs(row) * 0.35) * dip;
          return (
            <path
              key={`row-${row}`}
              d={`M 20 ${baseY - row * 4} Q 200 ${curveY} 380 ${baseY - row * 4}`}
              fill="none"
              stroke="#38BDF8"
              strokeWidth={row === 0 ? "2.5" : "1.2"}
              strokeOpacity={row === 0 ? "0.9" : "0.55"}
              strokeDasharray={row === 0 ? "none" : "4 2"}
            />
          );
        })}

        {/* Líneas verticales geodésicas convergiendo al pozo */}
        {[-4, -3, -2, -1, 0, 1, 2, 3, 4].map((col) => {
          const startX = 200 + col * 36;
          const midX = 200 + col * (16 - Math.min(10, Math.abs(col) * 2));
          return (
            <path
              key={`col-${col}`}
              d={`M ${startX} 20 Q ${midX} ${110 + dip * 0.6} ${startX} 200`}
              fill="none"
              stroke="#0284C7"
              strokeWidth="1.2"
              strokeOpacity="0.5"
            />
          );
        })}

        {/* Masa central deformadora */}
        <circle cx="200" cy={110 + dip * 0.5} r="20" fill="#0F172A" stroke="#38BDF8" strokeWidth="3" />
        <circle cx="200" cy={110 + dip * 0.5} r="14" fill="#000000" />
        <circle cx="196" cy={106 + dip * 0.5} r="3" fill="#FFFFFF" opacity="0.8" />

        {/* Partícula de prueba orbitando la geodésica */}
        <circle cx={orbX} cy={orbY} r="5" fill="#FFE600" stroke="#000000" strokeWidth="1.5" />
        <line
          x1={orbX}
          y1={orbY}
          x2={orbX - Math.sin(orbAngle) * 16}
          y2={orbY + Math.cos(orbAngle) * 7}
          stroke="#FFE600"
          strokeWidth="2"
          strokeDasharray="2 2"
        />

        {/* Rótulo vectorial diegético */}
        <rect x="18" y="14" width="168" height="22" rx="4" fill="#0F172A" stroke="#38BDF8" strokeWidth="1.5" />
        <text x="24" y="29" fill="#38BDF8" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          POZO GRAVITATORIO: g = ∇Φ
        </text>
      </svg>
    );
  }

  if (tipo === "orbita_fotones_esfera") {
    // Fotones orbitando y curvándose en r = 1.5 Rs
    const ang = f * 0.08;
    const fotonX = 200 + Math.cos(ang) * 62;
    const fotonY = 110 + Math.sin(ang) * 62;
    const rayProgress = (f * 0.035) % 1;

    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#050B14" />

        {/* Órbita crítica r = 1.5 Rs */}
        <circle
          cx="200"
          cy="110"
          r="62"
          fill="none"
          stroke="#F59E0B"
          strokeWidth="2.5"
          strokeDasharray="6 4"
          className="animate-spin"
        />

        {/* Horizonte de sucesos r = 1.0 Rs */}
        <circle cx="200" cy="110" r="42" fill="#000000" stroke="#EF4444" strokeWidth="3" />
        <circle cx="200" cy="110" r="40" fill="#000000" />

        {/* Rayo de luz exterior desviado por gravedad extrema */}
        <path
          d={`M 40 30 Q 150 90 200 ${110 - 62} Q 250 90 360 30`}
          fill="none"
          stroke="#38BDF8"
          strokeWidth="2"
          strokeDasharray="4 3"
        />

        {/* Rayo de luz cayendo sin retorno */}
        <path
          d="M 50 180 Q 150 150 185 130"
          fill="none"
          stroke="#EF4444"
          strokeWidth="2"
          strokeDasharray="3 3"
        />

        {/* Fotón orbitando en bucle cerrado */}
        <circle cx={fotonX} cy={fotonY} r="6" fill="#FBBF24" stroke="#FFFFFF" strokeWidth="1.5" />
        <circle cx={fotonX} cy={fotonY} r="12" fill="#FBBF24" opacity="0.3" />

        {/* Indicadores vectoriales */}
        <rect x="250" y="165" width="134" height="22" rx="4" fill="#000000" stroke="#F59E0B" strokeWidth="1.5" />
        <text x="256" y="180" fill="#F59E0B" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          RADIO FOTÓNICO: 1.5 Rs
        </text>
        <text x="175" y="114" fill="#EF4444" fontSize="11" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          Rs
        </text>
      </svg>
    );
  }

  if (tipo === "espaguetificacion_marea") {
    // Objeto estirándose verticalmente y comprimiéndose lateralmente
    const stretchProgress = (Math.sin(f * 0.1) + 1) / 2; // 0 .. 1
    const ovalWidth = interpolate(stretchProgress, [0, 1], [38, 14]);
    const ovalHeight = interpolate(stretchProgress, [0, 1], [40, 105]);

    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#0F0914" />

        {/* Dirección gravitacional hacia abajo */}
        <line x1="200" y1="20" x2="200" y2="200" stroke="#475569" strokeWidth="1.5" strokeDasharray="4 4" />
        <polygon points="200,208 193,196 207,196" fill="#EF4444" />

        {/* Objeto deformable bajo gradiente diferencial dF/dr */}
        <ellipse
          cx="200"
          cy="110"
          rx={ovalWidth}
          ry={ovalHeight}
          fill="#38BDF8"
          stroke="#000000"
          strokeWidth="3"
        />

        {/* Esferas moleculares internas estirándose */}
        <circle cx="200" cy={110 - ovalHeight * 0.55} r="7" fill="#FFE600" stroke="#000000" strokeWidth="2" />
        <circle cx="200" cy="110" r="7" fill="#FFE600" stroke="#000000" strokeWidth="2" />
        <circle cx="200" cy={110 + ovalHeight * 0.55} r="7" fill="#FFE600" stroke="#000000" strokeWidth="2" />

        {/* Flechas de estiramiento vertical (Tensión de marea) */}
        <line x1="200" y1={110 - ovalHeight - 8} x2="200" y2={110 - ovalHeight - 28} stroke="#EF4444" strokeWidth="3" />
        <polygon points="200,110 - ovalHeight - 32 194,110 - ovalHeight - 22 206,110 - ovalHeight - 22" fill="#EF4444" />

        <line x1="200" y1={110 + ovalHeight + 8} x2="200" y2={110 + ovalHeight + 28} stroke="#EF4444" strokeWidth="3" />
        <polygon points="200,110 + ovalHeight + 32 194,110 + ovalHeight + 22 206,110 + ovalHeight + 22" fill="#EF4444" />

        {/* Flechas de compresión lateral (Spaghettification lateral squeeze) */}
        <line x1={200 - ovalWidth - 24} y1="110" x2={200 - ovalWidth - 4} y2="110" stroke="#38BDF8" strokeWidth="2.5" />
        <line x1={200 + ovalWidth + 24} y1="110" x2={200 + ovalWidth + 4} y2="110" stroke="#38BDF8" strokeWidth="2.5" />

        {/* Ecuación diferencial de marea */}
        <rect x="225" y="16" width="160" height="26" rx="4" fill="#000000" stroke="#EF4444" strokeWidth="1.5" />
        <text x="232" y="33" fill="#EF4444" fontSize="11" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          dF/dr = 2GMm / r³
        </text>
      </svg>
    );
  }

  if (tipo === "dilatacion_temporal_relatividad") {
    // Reloj exterior vs Reloj en el horizonte con inclinación de cono de luz
    const extAngle = (f * 8) % 360;
    // El reloj que cae se ralentiza asintóticamente
    const inHandAngle = Math.min(270, f * 1.2);
    const coneTilt = Math.min(45, f * 0.28);

    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#0B132B" />

        {/* Reloj Observador Lejano (Tiempo T_coord) */}
        <g transform="translate(100, 105)">
          <circle cx="0" cy="0" r="42" fill="#1E293B" stroke="#38BDF8" strokeWidth="3" />
          {/* Marcas de reloj */}
          {[0, 90, 180, 270].map((deg) => (
            <line
              key={deg}
              x1={Math.cos((deg * Math.PI) / 180) * 32}
              y1={Math.sin((deg * Math.PI) / 180) * 32}
              x2={Math.cos((deg * Math.PI) / 180) * 38}
              y2={Math.sin((deg * Math.PI) / 180) * 38}
              stroke="#94A3B8"
              strokeWidth="2"
            />
          ))}
          {/* Manecilla girando rápido */}
          <line
            x1="0"
            y1="0"
            x2={Math.cos((extAngle * Math.PI) / 180) * 28}
            y2={Math.sin((extAngle * Math.PI) / 180) * 28}
            stroke="#FFE600"
            strokeWidth="3.5"
            strokeLinecap="round"
          />
          <circle cx="0" cy="0" r="4" fill="#FFFFFF" />
          <text x="-40" y="60" fill="#38BDF8" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            OBSERVADOR (t)
          </text>
        </g>

        {/* Reloj Cayendo en Horizonte (Tiempo Propio τ se congela ante el exterior) */}
        <g transform="translate(290, 105)">
          <circle cx="0" cy="0" r="42" fill="#1E293B" stroke="#EF4444" strokeWidth="3" />
          {[0, 90, 180, 270].map((deg) => (
            <line
              key={deg}
              x1={Math.cos((deg * Math.PI) / 180) * 32}
              y1={Math.sin((deg * Math.PI) / 180) * 32}
              x2={Math.cos((deg * Math.PI) / 180) * 38}
              y2={Math.sin((deg * Math.PI) / 180) * 38}
              stroke="#94A3B8"
              strokeWidth="2"
            />
          ))}
          {/* Manecilla ralentizada/detenida */}
          <line
            x1="0"
            y1="0"
            x2={Math.cos((inHandAngle * Math.PI) / 180) * 28}
            y2={Math.sin((inHandAngle * Math.PI) / 180) * 28}
            stroke="#EF4444"
            strokeWidth="3.5"
            strokeLinecap="round"
          />
          <circle cx="0" cy="0" r="4" fill="#FFFFFF" />
          <text x="-38" y="60" fill="#EF4444" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            HORIZONTE (Δt→∞)
          </text>
        </g>

        {/* Cono de luz inclinándose */}
        <path
          d={`M 195 70 L ${195 + Math.tan((coneTilt * Math.PI) / 180) * 50} 140`}
          stroke="#F59E0B"
          strokeWidth="3"
        />
        <text x="165" y="175" fill="#F59E0B" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          CONO 45°
        </text>
      </svg>
    );
  }

  if (tipo === "vortice_arrastre_kerr") {
    // Agujero negro en rotación: arrastre de marco de referencia (frame dragging)
    const rotSpeed = f * 0.12;

    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#030712" />

        {/* Ergosfera exterior oblata */}
        <ellipse cx="200" cy="110" rx="90" ry="55" fill="none" stroke="#A855F7" strokeWidth="2.5" strokeDasharray="5 3" />

        {/* Horizonte de sucesos interior */}
        <circle cx="200" cy="110" r="34" fill="#000000" stroke="#38BDF8" strokeWidth="3" />

        {/* Eje de rotación angular J */}
        <line x1="200" y1="20" x2="200" y2="200" stroke="#FBBF24" strokeWidth="2.5" />
        <polygon points="200,12 194,26 206,26" fill="#FBBF24" />
        <text x="210" y="24" fill="#FBBF24" fontSize="11" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          J ≠ 0
        </text>

        {/* Espirales del vórtice espaciotemporal */}
        {[0, 1, 2, 3].map((idx) => {
          const a = rotSpeed + idx * (Math.PI / 2);
          const r1 = 38;
          const r2 = 85;
          return (
            <path
              key={`spiral-${idx}`}
              d={`M ${200 + Math.cos(a) * r1} ${110 + Math.sin(a) * (r1 * 0.6)} Q ${
                200 + Math.cos(a + 0.9) * 60
              } ${110 + Math.sin(a + 0.9) * 35} ${200 + Math.cos(a + 1.6) * r2} ${
                110 + Math.sin(a + 1.6) * (r2 * 0.6)
              }`}
              fill="none"
              stroke="#C084FC"
              strokeWidth="2"
              strokeOpacity="0.8"
            />
          );
        })}

        {/* Etiqueta Ergosfera */}
        <rect x="25" y="16" width="140" height="22" rx="4" fill="#000000" stroke="#A855F7" strokeWidth="1.5" />
        <text x="32" y="31" fill="#A855F7" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          ERGOSFERA OBLATA
        </text>
      </svg>
    );
  }

  if (tipo === "espuma_cuantica_planck") {
    // Fluctuaciones topológicas a la escala de Planck 10^-35 m
    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#090514" />

        {/* Burbujas y fluctuaciones topológicas */}
        {[
          { x: 120, y: 80, r: 24, p: 0.15 },
          { x: 200, y: 110, r: 35, p: 0.22 },
          { x: 280, y: 90, r: 28, p: 0.18 },
          { x: 160, y: 145, r: 20, p: 0.25 },
          { x: 250, y: 155, r: 22, p: 0.19 },
        ].map((bubble, i) => {
          const oscR = bubble.r + Math.sin(f * bubble.p + i) * 6;
          return (
            <g key={`b-${i}`}>
              <circle
                cx={bubble.x}
                cy={bubble.y}
                r={oscR}
                fill="none"
                stroke="#A855F7"
                strokeWidth="2"
                strokeDasharray="4 3"
              />
              <circle
                cx={bubble.x}
                cy={bubble.y}
                r={Math.max(4, oscR * 0.45)}
                fill="#C084FC"
                opacity="0.35"
              />
            </g>
          );
        })}

        {/* Enlaces de red de espín / bucles cuánticos */}
        <line x1="120" y1="80" x2="200" y2="110" stroke="#38BDF8" strokeWidth="2" strokeDasharray="3 2" />
        <line x1="200" y1="110" x2="280" y2="90" stroke="#38BDF8" strokeWidth="2" strokeDasharray="3 2" />
        <line x1="160" y1="145" x2="200" y2="110" stroke="#38BDF8" strokeWidth="2" strokeDasharray="3 2" />
        <line x1="250" y1="155" x2="200" y2="110" stroke="#38BDF8" strokeWidth="2" strokeDasharray="3 2" />

        <rect x="20" y="16" width="170" height="24" rx="4" fill="#000000" stroke="#C084FC" strokeWidth="1.5" />
        <text x="26" y="32" fill="#C084FC" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          ESCALA PLANCK: 10⁻³⁵ M
        </text>
      </svg>
    );
  }

  if (tipo === "radiacion_hawking_pares") {
    // Creación de pares de vacío en el horizonte de sucesos
    const cycle = (f * 0.05) % 1;
    const pairSeparation = cycle * 45;

    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        {/* Interior del agujero negro */}
        <rect x="0" y="0" width="180" height="220" fill="#000000" />
        {/* Exterior (vacío cuántico) */}
        <rect x="180" y="0" width="220" height="220" fill="#0B132B" />

        {/* Línea del horizonte de sucesos */}
        <line x1="180" y1="0" x2="180" y2="220" stroke="#EF4444" strokeWidth="4" />

        {/* Partícula cayendo (energía negativa) */}
        <circle cx={180 - pairSeparation} cy="110" r="7" fill="#EF4444" stroke="#FFFFFF" strokeWidth="1.5" />
        <text x={170 - pairSeparation} y="130" fill="#EF4444" fontSize="9" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          -E
        </text>

        {/* Partícula escapando (radiación térmica positiva) */}
        <circle cx={180 + pairSeparation} cy="110" r="7" fill="#38BDF8" stroke="#FFFFFF" strokeWidth="1.5" />
        <text x={185 + pairSeparation} y="130" fill="#38BDF8" fontSize="9" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          +E (HAWKING)
        </text>

        {/* Onda de probabilidad cuántica */}
        <path
          d={`M 150 110 Q 180 ${110 - 20 * Math.sin(f * 0.2)} 210 110`}
          fill="none"
          stroke="#FFE600"
          strokeWidth="2"
          strokeDasharray="3 2"
        />

        <rect x="195" y="18" width="190" height="24" rx="4" fill="#000000" stroke="#38BDF8" strokeWidth="1.5" />
        <text x="202" y="34" fill="#38BDF8" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          PARES CUÁNTICOS DE VACÍO
        </text>
      </svg>
    );
  }

  if (tipo === "ala_desprendimiento_stall") {
    // Desprendimiento de la capa límite y entrada en pérdida (Stall a α > 15°) - Flujo de DERECHA a IZQUIERDA
    const angleOfAttack = 12 + Math.sin(f * 0.1) * 8; // Oscila entre 4° y 20°
    const isStall = angleOfAttack > 15;
    const stallBubbleSize = Math.max(0, (angleOfAttack - 15) * 6);
    const streamDash = (f * 10) % 24;

    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#060C18" />

        {/* Líneas de corriente del túnel de viento de DERECHA a IZQUIERDA con menor opacidad */}
        {[-3, -1.5, 0, 1.5, 3].map((row, i) => {
          const yBase = 110 + row * 24;
          const streamColor = isStall && row < 0 ? "#EF4444" : "#10B981";
          const streamPath = isStall && row < 0
            ? `M 380 ${yBase} C 280 ${yBase - 15}, 220 ${yBase - 55}, 140 ${yBase - 25} C 90 ${yBase + 10}, 50 ${yBase - 40}, 20 ${yBase - 10}`
            : `M 380 ${yBase} C 270 ${yBase - 10}, 210 ${yBase - (row <= 0 ? 30 : -10)}, 20 ${yBase + 5}`;

          return (
            <path
              key={`stream-${i}`}
              d={streamPath}
              fill="none"
              stroke={streamColor}
              strokeWidth={row === 0 ? "2" : "1.2"}
              strokeOpacity={isStall && row < 0 ? "0.65" : "0.35"}
              strokeDasharray={isStall && row < 0 ? "6 4" : "none"}
              strokeDashoffset={-streamDash}
            />
          );
        })}

        {/* Remolino caótico de recirculación sobre el extradós en pérdida (borde de fuga izquierdo) */}
        {isStall && (
          <g transform="translate(170, 75)">
            <ellipse
              cx="0"
              cy="0"
              rx={18 + stallBubbleSize}
              ry={12 + stallBubbleSize * 0.6}
              fill="#EF4444"
              opacity="0.25"
            />
            <path
              d="M 15 -8 Q 0 -18 -15 -6 Q -20 12 0 14 Q 18 10 10 -4"
              fill="none"
              stroke="#EF4444"
              strokeWidth="2"
              strokeDasharray="4 2"
            />
            <text x="0" y="4" fill="#EF4444" fontSize="9" fontFamily="'Arial Black', sans-serif" fontWeight="900" textAnchor="middle">
              VÓRTICE STALL
            </text>
          </g>
        )}

        {/* Perfil alar rotando con el ángulo de ataque - Borde de ataque a la DERECHA (+90), Borde de fuga a la IZQUIERDA (-90) */}
        <g transform={`translate(230, 120) rotate(${angleOfAttack})`}>
          <path
            d="M 90 0 C 70 -26, -30 -24, -90 0 C -30 8, 60 10, 90 0 Z"
            fill="#1E293B"
            stroke={isStall ? "#EF4444" : "#38BDF8"}
            strokeWidth="3.5"
          />
          {/* Vector de sustentación (L) */}
          <line
            x1="0"
            y1="-10"
            x2="0"
            y2={isStall ? "-22" : "-52"}
            stroke={isStall ? "#EF4444" : "#10B981"}
            strokeWidth="3.5"
          />
          <polygon
            points={isStall ? "0,-28 -5,-20 5,-20" : "0,-58 -6,-48 6,-48"}
            fill={isStall ? "#EF4444" : "#10B981"}
          />
        </g>

        {/* Marcador de ángulo de ataque y estado */}
        <rect x="20" y="16" width="180" height="24" rx="4" fill="#000000" stroke={isStall ? "#EF4444" : "#10B981"} strokeWidth="1.5" />
        <text x="26" y="32" fill={isStall ? "#EF4444" : "#10B981"} fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          {isStall ? `STALL ACTIVO: α = ${angleOfAttack.toFixed(1)}° > 15°` : `FLUJO LAMINAR: α = ${angleOfAttack.toFixed(1)}°`}
        </text>
      </svg>
    );
  }

  if (tipo === "alula_tobera_venturi") {
    // Alula levantándose e inyectando un chorro de aire de alta velocidad Venturi (Flujo de DERECHA a IZQUIERDA)
    const alulaOpen = 18 + Math.sin(f * 0.15) * 6; // Ángulo de apertura del álula
    const streamDash = (f * 12) % 30;

    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#050C1A" />

        {/* Flujo general de aire incidente a alto ángulo de ataque (42°) de DERECHA a IZQUIERDA */}
        <path d="M 380 185 C 310 165, 260 100, 20 45" fill="none" stroke="#10B981" strokeWidth="1.8" strokeDasharray="6 4" strokeDashoffset={streamDash} opacity="0.45" />
        <path d="M 380 205 C 300 185, 240 130, 20 75" fill="none" stroke="#10B981" strokeWidth="1.4" strokeDasharray="6 4" strokeDashoffset={streamDash} opacity="0.35" />

        {/* 1. PERFIL ALAR AVIAR ANATÓMICO A ALTO ÁNGULO DE ATAQUE (32°) - Borde de ataque a la DERECHA */}
        <g transform="translate(220, 135) rotate(32)">
          {/* Plumas remeras de vuelo (borde de fuga a la izquierda) */}
          <path d="M 85 10 C 105 2, 110 -12, 90 -16 C 75 -18, 65 -10, 70 12 Z" fill="#1E293B" stroke="#000000" strokeWidth="3" />
          <line x1="85" y1="8" x2="68" y2="-14" stroke="#F8FAFC" strokeWidth="1.8" />
          
          <path d="M 65 14 C 82 6, 85 -10, 68 -16 C 54 -18, 45 -8, 50 14 Z" fill="#334155" stroke="#000000" strokeWidth="3" />
          <line x1="65" y1="12" x2="50" y2="-14" stroke="#F8FAFC" strokeWidth="1.8" />

          {/* Cuerpo carnoso del ala con coberteras */}
          <path d="M 75 12 C 50 -26, -25 -30, -85 8 C -70 24, 20 28, 75 12 Z" fill="#475569" stroke="#000000" strokeWidth="4" strokeLinejoin="round" />
          
          {/* Plumaje de coberteras medianas */}
          <path d="M 50 6 C 35 -14, -10 -18, -55 4 C -42 16, 10 18, 50 6 Z" fill="#64748B" stroke="#000000" strokeWidth="2.5" />
          
          {/* Hueso alar interno (Carpometacarpo) en corte anatómico */}
          <ellipse cx="-14" cy="4" rx="9" ry="7" fill="#F8FAFC" stroke="#000000" strokeWidth="2.5" />
          <circle cx="-14" cy="4" r="3" fill="#CBD5E1" />
          <ellipse cx="16" cy="6" rx="7" ry="5.5" fill="#F8FAFC" stroke="#000000" strokeWidth="2" />
        </g>

        {/* 2. EL ÁLULA (PULGAR AVIAR ARTICULADO FORMANDO LA TOBERA) EN EL BORDE DE ATAQUE DERECHO */}
        <g transform={`translate(292, 115) rotate(${32 + alulaOpen})`}>
          {/* Falange del pulgar */}
          <ellipse cx="0" cy="0" rx="4" ry="2.5" fill="#F8FAFC" stroke="#000000" strokeWidth="2" />

          {/* 3 Plumas alulares con raquis visible orientadas contra el viento */}
          <path d="M -4 -3 C -16 -12, -32 -14, -44 -8 C -32 -4, -18 -1, -4 -1 Z" fill="#CBD5E1" stroke="#000000" strokeWidth="2.2" />
          <line x1="-4" y1="-2" x2="-40" y2="-9" stroke="#F8FAFC" strokeWidth="1.5" />

          <path d="M -6 -7 C -22 -18, -44 -20, -60 -11 C -46 -5, -26 -1, -6 -3 Z" fill="#FFE600" stroke="#000000" strokeWidth="2.8" />
          <path d="M -46 -15 C -52 -13, -56 -12, -60 -11 C -53 -7, -46 -6, -42 -8 Z" fill="#0F172A" />
          <line x1="-6" y1="-5" x2="-54" y2="-12" stroke="#FFFFFF" strokeWidth="2" />

          <path d="M -4 -10 C -16 -20, -30 -22, -42 -15 C -32 -11, -18 -7, -4 -6 Z" fill="#FBBF24" stroke="#000000" strokeWidth="2.2" />
          <line x1="-4" y1="-9" x2="-38" y2="-16" stroke="#FFFFFF" strokeWidth="1.5" />

          {/* Etiqueta sobre el álula */}
          <g transform="translate(-24, -26)">
            <rect x="-35" y="-11" width="70" height="15" rx="3" fill="#0F172A" stroke="#FFE600" strokeWidth="1.5" />
            <text x="0" y="0" fill="#FFE600" fontSize="7.5" fontFamily="'Arial Black', sans-serif" fontWeight="900" textAnchor="middle">ÁLULA (DÍGITO I)</text>
          </g>
        </g>

        {/* 3. CHORRO VENTURI DE ALTA VELOCIDAD INYECTADO SOBRE EL EXTRADÓS (DE DERECHA A IZQUIERDA) */}
        <path
          d="M 298 108 Q 265 78 210 74 Q 130 70 35 82"
          fill="none"
          stroke="#10B981"
          strokeWidth="4"
          strokeDasharray="10 4"
          strokeDashoffset={-f * 8}
          opacity="0.85"
        />
        <path
          d="M 304 114 Q 270 84 215 80 Q 135 76 40 88"
          fill="none"
          stroke="#38BDF8"
          strokeWidth="2.8"
          strokeDashoffset={-f * 10}
          opacity="0.7"
        />
        {/* Punta de flecha apuntando a la IZQUIERDA */}
        <polygon points="28,82 42,75 42,89" fill="#10B981" />

        {/* 4. VÓRTICE DE BORDE DE ATAQUE ESTABLE (LEV) */}
        <g transform="translate(205, 68)">
          <circle cx="0" cy="0" r="16" fill="#38BDF8" opacity="0.25" />
          <circle cx="0" cy="0" r="9" fill="none" stroke="#38BDF8" strokeWidth="2.2" strokeDasharray="4 2" />
          <text x="0" y="-14" fill="#38BDF8" fontSize="8" fontFamily="'Arial Black', sans-serif" fontWeight="900" textAnchor="middle">VÓRTICE LEV</text>
        </g>

        {/* Rótulos técnicos diegéticos */}
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

  if (tipo === "microestructura_velcro_barbula") {
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
              {/* Tallo de la bárbula */}
              <path d="M 0 0 C 8 14, 16 28, 22 42" fill="none" stroke="#38BDF8" strokeWidth="4" strokeLinecap="round" />
              {/* Ganchillos microscópicos dobles (Hámuli) en oro brillante */}
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
              {/* Canal receptáculo de enganche */}
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

  if (tipo === "valvula_aleteo_persiana") {
    // Válvula unidireccional: Sellado en downstroke vs Apertura 45° en upstroke
    const isDownstroke = Math.sin(f * 0.15) >= 0;

    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#0A0F1D" />

        {/* División comparativa */}
        <line x1="200" y1="45" x2="200" y2="205" stroke="#334155" strokeWidth="2" strokeDasharray="4 3" />

        {/* LADO IZQUIERDO: BATIDA DESCENDENTE (DOWNSTROKE) */}
        <g transform="translate(100, 120)">
          <text x="-80" y="-55" fill="#10B981" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            BAJADA: SELLADO 100%
          </text>
          {/* Plumas solapadas planas herméticas */}
          {[-45, -15, 15, 45].map((x, i) => (
            <g key={`down-feather-${i}`} transform={`translate(${x}, 0)`}>
              <rect x="-18" y="-4" width="36" height="8" rx="3" fill="#1E293B" stroke="#10B981" strokeWidth="2" />
              <circle cx="-10" cy="0" r="2.5" fill="#FFE600" />
            </g>
          ))}
          {/* Empuje hacia abajo */}
          <line x1="0" y1="18" x2="0" y2="45" stroke="#10B981" strokeWidth="3" />
          <polygon points="0,52 -6,42 6,42" fill="#10B981" />
          <text x="-48" y="68" fill="#10B981" fontSize="9" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            EMPUJE POSITIVO
          </text>
        </g>

        {/* LADO DERECHO: BATIDA ASCENDENTE (UPSTROKE) */}
        <g transform="translate(300, 120)">
          <text x="-80" y="-55" fill="#38BDF8" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            SUBIDA: PERSIANA 45°
          </text>
          {/* Plumas rotadas 45 grados sobre su raquis asimétrico */}
          {[-45, -15, 15, 45].map((x, i) => (
            <g key={`up-feather-${i}`} transform={`translate(${x}, 0) rotate(45)`}>
              <rect x="-18" y="-4" width="36" height="8" rx="3" fill="#1E293B" stroke="#38BDF8" strokeWidth="2" />
              <circle cx="-10" cy="0" r="2.5" fill="#FFE600" />
            </g>
          ))}
          {/* Aire pasando libremente entre las ranuras */}
          {[-30, 0, 30].map((x, i) => (
            <path
              key={`air-up-${i}`}
              d={`M ${x} 40 L ${x} -35`}
              stroke="#38BDF8"
              strokeWidth="2"
              strokeDasharray="4 3"
            />
          ))}
          <text x="-48" y="68" fill="#38BDF8" fontSize="9" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            CERO RESISTENCIA
          </text>
        </g>

        <rect x="20" y="14" width="230" height="22" rx="4" fill="#000000" stroke="#10B981" strokeWidth="1.5" />
        <text x="26" y="29" fill="#10B981" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          AEROELASTICIDAD ASIMÉTRICA: VÁLVULA
        </text>
      </svg>
    );
  }

  if (tipo === "herbst_mecanoreceptor_impulso") {
    // Corpúsculo de Herbst en la dermis con pulsos bioeléctricos a > 800 Hz
    const pulseOffset = (f * 14) % 100;

    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#0A0612" />

        {/* Superficie de la dermis y epidermis */}
        <line x1="20" y1="75" x2="380" y2="75" stroke="#64748B" strokeWidth="2" strokeDasharray="6 3" />
        <text x="25" y="70" fill="#94A3B8" fontSize="8" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          SUPERFICIE DÉRMICA
        </text>

        {/* Tallo de la pluma entrando al folículo */}
        <g transform="translate(140, 75) rotate(-15)">
          <line x1="0" y1="-65" x2="0" y2="30" stroke="#F8FAFC" strokeWidth="7" strokeLinecap="round" />
          <line x1="0" y1="-65" x2="0" y2="30" stroke="#000000" strokeWidth="2" />
        </g>

        {/* Corpúsculo de Herbst (cápsula laminada en forma de capas concéntricas) */}
        <g transform="translate(132, 115)">
          {[28, 22, 16, 10, 5].map((r, i) => (
            <ellipse
              key={`herbst-layer-${i}`}
              cx="0"
              cy="0"
              rx={r * 1.3}
              ry={r}
              fill="none"
              stroke="#FACC15"
              strokeWidth={i === 4 ? "3" : "1.5"}
              strokeOpacity={0.4 + i * 0.15}
            />
          ))}
          <circle cx="0" cy="0" r="4" fill="#FFFFFF" />
        </g>

        {/* Axón nervioso transmitiendo impulsos bioeléctricos rápidos hacia el cráneo */}
        <path
          d="M 132 125 C 160 160, 220 170, 280 145 C 320 125, 350 150, 380 140"
          fill="none"
          stroke="#FACC15"
          strokeWidth="3.5"
          strokeDasharray="8 4"
        />

        {/* Chispas de acción sináptica */}
        <circle cx={140 + pulseOffset * 2.2} cy={140 + Math.sin(pulseOffset) * 15} r="5" fill="#FFE600" />
        <circle cx={140 + pulseOffset * 2.2} cy={140 + Math.sin(pulseOffset) * 15} r="10" fill="#FACC15" opacity="0.3" />

        <rect x="20" y="16" width="220" height="24" rx="4" fill="#000000" stroke="#FACC15" strokeWidth="1.5" />
        <text x="26" y="32" fill="#FACC15" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          CORPÚSCULO HERBST: LATENCIA &lt; 5 MS
        </text>
        <text x="260" y="32" fill="#FACC15" fontSize="9" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          SENSIBILIDAD &gt; 800 HZ
        </text>
      </svg>
    );
  }

  if (tipo === "cinematica_ocho_aleteo") {
    // Cinemática 3D del aleteo en forma de ocho (infinito ∞)
    const t = f * 0.12;
    // Curva paramétrica en forma de ocho: x = a*sin(t), y = b*sin(2t)
    const px = 200 + Math.sin(t) * 90;
    const py = 110 + Math.sin(2 * t) * 45;

    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#050B14" />

        {/* Trayectoria continua en forma de ocho */}
        <path
          d="M 200 110 C 260 70, 290 150, 200 110 C 110 70, 140 150, 200 110 Z"
          fill="none"
          stroke="#38BDF8"
          strokeWidth="3"
          strokeDasharray="5 3"
        />

        {/* Punto de la punta del ala moviéndose a lo largo del ocho */}
        <circle cx={px} cy={py} r="8" fill="#FFE600" stroke="#000000" strokeWidth="2" />
        <circle cx={px} cy={py} r="16" fill="#FFE600" opacity="0.3" />

        {/* Vectores simultáneos de Sustentación (vertical) y Empuje (horizontal) */}
        <line x1={px} y1={py} x2={px} y2={py - 35} stroke="#10B981" strokeWidth="3" />
        <polygon points={`${px},${py - 42} ${px - 5},${py - 33} ${px + 5},${py - 33}`} fill="#10B981" />

        <line x1={px} y1={py} x2={px + 35} y2={py} stroke="#38BDF8" strokeWidth="3" />
        <polygon points={`${px + 42},${py} ${px + 33},${py - 5} ${px + 33},${py + 5}`} fill="#38BDF8" />

        <rect x="20" y="16" width="180" height="24" rx="4" fill="#000000" stroke="#38BDF8" strokeWidth="1.5" />
        <text x="26" y="32" fill="#38BDF8" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          TRAYECTORIA EN 8 (∞)
        </text>
        <rect x="215" y="16" width="165" height="24" rx="4" fill="#000000" stroke="#10B981" strokeWidth="1.5" />
        <text x="221" y="32" fill="#10B981" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          L + T INTEGRADOS (LEV)
        </text>
      </svg>
    );
  }

  if (tipo === "dispersion_acustica_peines") {
    // Silencio aeroacústico de la lechuza vs paloma: Osciloscopio a 0 dB
    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#05080F" />

        {/* Cuadrícula de osciloscopio verde fósforo */}
        <defs>
          <pattern id="gridOsc" width="20" height="20" patternUnits="userSpaceOnUse">
            <line x1="0" y1="0" x2="20" y2="0" stroke="#10B981" strokeWidth="0.5" strokeOpacity="0.2" />
            <line x1="0" y1="0" x2="0" y2="20" stroke="#10B981" strokeWidth="0.5" strokeOpacity="0.2" />
          </pattern>
        </defs>
        <rect x="20" y="45" width="360" height="150" fill="url(#gridOsc)" stroke="#10B981" strokeWidth="1.5" />

        {/* CANAL SUPERIOR: PALOMA / AVIÓN (RUIDO TURBULENTO > 60 dB) */}
        <path
          d={`M 25 90 Q 60 ${90 + Math.sin(f * 0.8) * 28} 100 90 Q 140 ${90 - Math.sin(f * 0.7) * 32} 180 90 Q 220 ${90 + Math.sin(f * 0.9) * 25} 260 90 Q 300 ${90 - Math.sin(f * 0.6) * 30} 375 90`}
          fill="none"
          stroke="#EF4444"
          strokeWidth="2.5"
        />
        <text x="35" y="75" fill="#EF4444" fontSize="9" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          PALOMA / AVIÓN: RUIDO DE VÓRTICES (&gt; 60 dB)
        </text>

        {/* CANAL INFERIOR: LECHUZA (PEINES Y FLECOS ABSORBENTES = 0 dB) */}
        <line x1="25" y1="155" x2="375" y2="155" stroke="#10B981" strokeWidth="3" />
        <text x="35" y="145" fill="#10B981" fontSize="9" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          LECHUZA: PEINES DE ATAQUE + FLECOS = 0 dB
        </text>

        <rect x="20" y="16" width="210" height="22" rx="4" fill="#000000" stroke="#10B981" strokeWidth="1.5" />
        <text x="26" y="31" fill="#10B981" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          DISPERSIÓN AEROACÚSTICA TOTAL
        </text>
      </svg>
    );
  }

  if (tipo === "colapso_schwarzschild_masa") {
    const collapseR = Math.max(8, 70 - ((f * 0.8) % 65));
    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#070714" />
        <circle cx="200" cy="110" r="50" fill="none" stroke="#EF4444" strokeWidth="2" strokeDasharray="5 3" />
        <circle cx="200" cy="110" r={collapseR} fill="#EF4444" opacity="0.4" />
        <circle cx="200" cy="110" r={Math.min(20, collapseR)} fill="#000000" stroke="#FFFFFF" strokeWidth="2" />

        {/* Flechas de colapso hacia el centro r=0 */}
        {[0, 45, 90, 135, 180, 225, 270, 315].map((ang) => {
          const rad = (ang * Math.PI) / 180;
          return (
            <line
              key={ang}
              x1={200 + Math.cos(rad) * 75}
              y1={110 + Math.sin(rad) * 75}
              x2={200 + Math.cos(rad) * (collapseR + 6)}
              y2={110 + Math.sin(rad) * (collapseR + 6)}
              stroke="#FFE600"
              strokeWidth="2"
            />
          );
        })}

        <rect x="25" y="16" width="165" height="24" rx="4" fill="#000000" stroke="#EF4444" strokeWidth="1.5" />
        <text x="32" y="32" fill="#EF4444" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          COLAPSO INELUDIBLE: r → 0
        </text>
      </svg>
    );
  }

  if (tipo === "balance_energetico_cerebro_20") {
    const pulse = 1 + Math.sin(f * 0.2) * 0.05;
    const flowOffset = -(f * 2.5) % 24;
    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#080C16" />
        <g transform="translate(26, 52)">
          <text x="0" y="0" fill="#94A3B8" fontSize="9.5" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            MASA CORPORAL DEL CEREBRO (2%)
          </text>
          <rect x="0" y="6" width="340" height="18" rx="5" fill="#1E293B" stroke="#475569" strokeWidth="1.5" />
          <rect x="2" y="8" width="22" height="14" rx="3" fill="#38BDF8" />
          <text x="32" y="19" fill="#38BDF8" fontSize="11" fontFamily="'Arial Black', sans-serif" fontWeight="900">2%</text>
        </g>

        <g transform="translate(26, 102)">
          <text x="0" y="0" fill="#F97316" fontSize="9.5" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            CONSUMO DE GLUCOSA EN REPOSO ADULTO (20%)
          </text>
          <rect x="0" y="6" width="340" height="22" rx="5" fill="#1E293B" stroke="#F97316" strokeWidth="1.5" />
          <rect x="2" y="8" width={115 * pulse} height="18" rx="3" fill="#F97316" />
          <line x1="8" y1="17" x2="110" y2="17" stroke="#FEF08A" strokeWidth="2.5" strokeDasharray="8 6" strokeDashoffset={flowOffset} />
          <text x="126" y="21" fill="#FFE600" fontSize="12" fontFamily="'Arial Black', sans-serif" fontWeight="900">20% ATP</text>
        </g>

        <g transform="translate(26, 156)">
          <text x="0" y="0" fill="#EF4444" fontSize="9.5" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            RECIÉN NACIDO HUMANO (60% DEL METABOLISMO)
          </text>
          <rect x="0" y="6" width="340" height="22" rx="5" fill="#1E293B" stroke="#EF4444" strokeWidth="1.5" />
          <rect x="2" y="8" width={235 * pulse} height="18" rx="3" fill="#EF4444" />
          <text x="246" y="21" fill="#FCA5A5" fontSize="12" fontFamily="'Arial Black', sans-serif" fontWeight="900">60% NEONATO</text>
        </g>

        <rect x="24" y="12" width="250" height="22" rx="4" fill="#000000" stroke="#F97316" strokeWidth="1.5" />
        <text x="30" y="27" fill="#FFE600" fontSize="9.5" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          DESPROPORCIÓN METABÓLICA 10:1
        </text>
      </svg>
    );
  }

  if (tipo === "hipotesis_tejido_caro_aiello") {
    const t = Math.min(1, localFrame / 55);
    const gutScale = interpolate(t, [0, 1], [1.18, 0.62]);
    const brainScale = interpolate(t, [0, 1], [0.72, 1.25]);
    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#090D16" />
        <line x1="200" y1="44" x2="200" y2="205" stroke="#334155" strokeWidth="2" strokeDasharray="5 4" />
        <g transform="translate(100, 122)">
          <text x="0" y="-62" textAnchor="middle" fill="#10B981" fontSize="9.5" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            GORILA (DIETA CRUDA 9H)
          </text>
          <circle cx="0" cy="-34" r="15" fill="#475569" stroke="#94A3B8" strokeWidth="2" />
          <ellipse cx="0" cy="22" rx="46" ry="38" fill="#065F46" stroke="#10B981" strokeWidth="3" />
          <path d="M -26 12 Q 0 -2 26 12 Q -24 26 24 34 Q 0 48 -24 36" fill="none" stroke="#6EE7B7" strokeWidth="4" />
          <text x="0" y="75" textAnchor="middle" fill="#6EE7B7" fontSize="9" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            INTESTINO MASIVO
          </text>
        </g>
        <g transform="translate(300, 122)">
          <text x="0" y="-62" textAnchor="middle" fill="#38BDF8" fontSize="9.5" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            HOMO + COCINA TÉRMICA
          </text>
          <g transform={`translate(0, -32) scale(${brainScale})`}>
            <ellipse cx="0" cy="0" rx="24" ry="19" fill="#0284C7" stroke="#FFE600" strokeWidth="2.5" />
          </g>
          <g transform={`translate(0, 24) scale(${gutScale})`}>
            <ellipse cx="0" cy="0" rx="34" ry="26" fill="#1E293B" stroke="#38BDF8" strokeWidth="2.5" />
          </g>
          <text x="0" y="75" textAnchor="middle" fill="#FFE600" fontSize="9" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            INTESTINO -45% / CEREBRO x3
          </text>
        </g>
        <rect x="20" y="12" width="285" height="22" rx="4" fill="#000000" stroke="#FFE600" strokeWidth="1.5" />
        <text x="26" y="27" fill="#FFE600" fontSize="9.5" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          AIELLO &amp; WHEELER (1995): TEJIDO CARO
        </text>
      </svg>
    );
  }

  if (tipo === "dilema_obstetrico_pelvis") {
    const chimpY = -36 + ((f * 1.4) % 76);
    const humanJamY = -26 + Math.abs(Math.sin(f * 0.16)) * 12;
    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#070B14" />
        <line x1="200" y1="45" x2="200" y2="205" stroke="#334155" strokeWidth="2" strokeDasharray="5 4" />
        <g transform="translate(100, 125)">
          <text x="0" y="-64" textAnchor="middle" fill="#10B981" fontSize="9.5" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            CHIMPANCÉ (CUADRÚPEDO)
          </text>
          <ellipse cx="0" cy="0" rx="44" ry="52" fill="none" stroke="#94A3B8" strokeWidth="8" />
          <circle cx="0" cy={chimpY} r="22" fill="#10B981" stroke="#FFFFFF" strokeWidth="2.5" />
          <text x="0" y="72" textAnchor="middle" fill="#10B981" fontSize="9" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            PASO HOLGADO
          </text>
        </g>
        <g transform="translate(300, 125)">
          <text x="0" y="-64" textAnchor="middle" fill="#EF4444" fontSize="9.5" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            HUMANO (BÍPEDO + CRÁNEO)
          </text>
          <ellipse cx="0" cy="6" rx="48" ry="26" fill="none" stroke="#CBD5E1" strokeWidth="10" />
          <circle cx="0" cy={humanJamY} r="31" fill="#EF4444" stroke="#FFE600" strokeWidth="3" opacity="0.92" />
          <line x1="-54" y1="6" x2="-34" y2="6" stroke="#FFE600" strokeWidth="3.5" />
          <line x1="54" y1="6" x2="34" y2="6" stroke="#FFE600" strokeWidth="3.5" />
          <text x="0" y="72" textAnchor="middle" fill="#EF4444" fontSize="9" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            BLOQUEO GEOMÉTRICO
          </text>
        </g>
        <rect x="20" y="12" width="290" height="22" rx="4" fill="#000000" stroke="#EF4444" strokeWidth="1.5" />
        <text x="26" y="27" fill="#EF4444" fontSize="9.5" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          ROSENBERG &amp; TREVATHAN: CANAL PÉLVICO
        </text>
      </svg>
    );
  }

  if (tipo === "homunculo_motor_pinza") {
    const spark = 0.65 + Math.sin(f * 0.22) * 0.35;
    return (
      <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
        <rect width="400" height="220" fill="#060A14" />
        <g transform="translate(92, 126)">
          <circle cx="0" cy="0" r="46" fill="#0F172A" stroke="#FFE600" strokeWidth="2.5" />
          <path d="M -22 22 Q -8 -4 6 -8" fill="none" stroke="#FDE047" strokeWidth="8" strokeLinecap="round" />
          <path d="M 18 22 Q 14 -6 6 -8" fill="none" stroke="#38BDF8" strokeWidth="8" strokeLinecap="round" />
          <circle cx="6" cy="-8" r="6" fill="#EF4444" />
          <text x="0" y="64" textAnchor="middle" fill="#FFE600" fontSize="9" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            PINZA PULGAR-ÍNDICE
          </text>
        </g>
        <path d="M 145 108 C 185 82, 215 82, 252 106" fill="none" stroke="#FFE600" strokeWidth="3" strokeDasharray="7 4" />
        <path d="M 252 138 C 215 162, 185 162, 145 138" fill="none" stroke="#38BDF8" strokeWidth="3" strokeDasharray="7 4" />
        <g transform="translate(308, 124)">
          <path
            d="M -46 18 C -52 -24, -18 -48, 16 -44 C 48 -40, 56 -8, 44 22 C 26 36, -24 36, -46 18 Z"
            fill="#1E293B"
            stroke="#38BDF8"
            strokeWidth="3"
          />
          <ellipse cx="-6" cy="-12" rx="18" ry="26" fill="#FFE600" opacity={spark} />
          <text x="0" y="66" textAnchor="middle" fill="#38BDF8" fontSize="9" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            CORTEZA MOTORA (M1)
          </text>
        </g>
        <rect x="20" y="12" width="305" height="22" rx="4" fill="#000000" stroke="#38BDF8" strokeWidth="1.5" />
        <text x="26" y="27" fill="#38BDF8" fontSize="9.5" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          HOMÚNCULO DE PENFIELD: BUCLE MANO-CEREBRO
        </text>
      </svg>
    );
  }

  // Fallback didáctico neutral si no coincide ningún tipo específico (aerodinámica de fluidos)
  return (
    <svg width={width} height={height} viewBox="0 0 400 220" className="w-full h-full">
      <rect width="400" height="220" fill="#0A0F1D" />
      {[-2, -1, 0, 1, 2].map((i) => (
        <path
          key={i}
          d={`M 20 ${110 + i * 28} Q 200 ${110 + i * 16 + Math.sin(f * 0.12 + i) * 10} 380 ${110 + i * 28}`}
          fill="none"
          stroke="#38BDF8"
          strokeWidth="2"
          strokeDasharray="6 3"
        />
      ))}
      <rect x="25" y="16" width="180" height="24" rx="4" fill="#000000" stroke="#38BDF8" strokeWidth="1.5" />
      <text x="32" y="32" fill="#38BDF8" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
        SIMULACIÓN DE FLUIDOS
      </text>
    </svg>
  );
};

export const EducationalZoomBox: React.FC<EducationalZoomBoxProps> = ({
  config,
  palabras,
  durationInFrames,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const { startFrame, endFrame } = resolveTimeRangeFrames(
    config,
    durationInFrames,
    fps,
    palabras
  );

  if (frame < startFrame || frame > endFrame) {
    return null;
  }

  const localFrame = frame - startFrame;
  const shotDuration = Math.max(1, endFrame - startFrame);

  // Animación de entrada spring con elasticidad neo-brutalista
  const entranceSpring = spring({
    frame: localFrame,
    fps,
    config: {
      damping: 14,
      stiffness: 170,
      mass: 0.7,
    },
  });

  // Animación de salida en los últimos 8 frames
  const exitProgress = interpolate(
    localFrame,
    [shotDuration - 8, shotDuration],
    [1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  const scale = entranceSpring * exitProgress;
  const opacity = interpolate(localFrame, [0, 4], [0, 1], {
    extrapolateRight: "clamp",
  }) * exitProgress;

  const boxWidth = config.ancho ?? 470;
  const boxHeight = config.alto ?? 320;
  const { left, top, origin } = resolveQuadrantCoordinates(
    config.posicion,
    boxWidth,
    boxHeight
  );

  const accentColor = config.colorAcento ?? "#38BDF8";

  return (
    <div
      className="absolute pointer-events-none select-none"
      style={{
        left,
        top,
        width: boxWidth,
        height: boxHeight,
        zIndex: 42,
        transform: `scale(${scale})`,
        transformOrigin: origin,
        opacity,
      }}
    >
      {/* Contenedor principal estilo recuadro Kurzgesagt / Veritasium */}
      <div
        className="w-full h-full bg-[#0B0F19] rounded-2xl border-4 border-black overflow-hidden flex flex-col"
        style={{
          boxShadow: `8px 8px 0px #000000, 0 0 24px ${accentColor}44`,
        }}
      >
        {/* Barra superior de título estilo monitor didáctico */}
        <div className="bg-black px-4 py-2 flex items-center justify-between border-b-3 border-black">
          <div className="flex items-center gap-2">
            <span
              className="w-3 h-3 rounded-full animate-ping"
              style={{ backgroundColor: accentColor }}
            />
            <span className="text-[11px] font-black tracking-widest uppercase text-white">
              {config.titulo || "SIMULACIÓN DIDÁCTICA"}
            </span>
          </div>
          <span
            className="text-[9px] font-black uppercase px-2 py-0.5 rounded border border-white/20"
            style={{ color: accentColor }}
          >
            AMPLIACIÓN ZOOM
          </span>
        </div>

        {/* Lienzo de animación SVG */}
        <div className="flex-1 w-full relative overflow-hidden bg-black/40">
          <SimulationSvg
            tipo={config.tipo || config.tipoAnimacion}
            localFrame={localFrame}
            width={boxWidth}
            height={boxHeight - 65}
          />
        </div>

        {/* Subtítulo o leyenda explicativa al pie */}
        {config.subtitulo && (
          <div className="bg-[#030712] px-3.5 py-1.5 border-t border-white/10 flex items-center justify-between">
            <span className="text-[11px] font-bold text-slate-300 truncate">
              {config.subtitulo}
            </span>
            <span className="text-[9px] font-black text-yellow-400 uppercase tracking-wider ml-2">
              ESTUDIO 1:1
            </span>
          </div>
        )}
      </div>

      {/* Esquinas técnicas decorativas */}
      <div
        className="absolute -top-2 -left-2 w-4 h-4 border-t-2 border-l-2"
        style={{ borderColor: accentColor }}
      />
      <div
        className="absolute -top-2 -right-2 w-4 h-4 border-t-2 border-r-2"
        style={{ borderColor: accentColor }}
      />
      <div
        className="absolute -bottom-2 -left-2 w-4 h-4 border-b-2 border-l-2"
        style={{ borderColor: accentColor }}
      />
      <div
        className="absolute -bottom-2 -right-2 w-4 h-4 border-b-2 border-r-2"
        style={{ borderColor: accentColor }}
      />
    </div>
  );
};
