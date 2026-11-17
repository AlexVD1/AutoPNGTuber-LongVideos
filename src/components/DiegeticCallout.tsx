import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import {
  CotaVectorial,
  PalabraTiming,
  PersonajeEscena,
  PlanoCamara,
} from "../types";
import { resolveTimeRangeFrames } from "../stickman/actionSequences";

interface DiegeticCalloutProps {
  cotas?: CotaVectorial[];
  personajes?: PersonajeEscena[];
  palabras?: PalabraTiming[];
}

export const DiegeticCalloutsLayer: React.FC<DiegeticCalloutProps> = ({
  cotas = [],
  personajes = [],
  palabras,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const floorTrajectories = personajes.filter((p) => p.trayectoriaSuelo);

  if (cotas.length === 0 && floorTrajectories.length === 0) {
    return null;
  }

  return (
    <div
      style={{
        position: "absolute",
        inset: 0,
        pointerEvents: "none",
        zIndex: 34,
      }}
    >
      <svg width="1920" height="1080" viewBox="0 0 1920 1080" fill="none">
        {/* Vectores tácticos de trayectoria en el suelo (estilo holograma metro/Bolt) */}
        {floorTrajectories.map((p, idx) => {
          const { startFrame, endFrame } = resolveTimeRangeFrames(
            p,
            durationInFrames,
            fps,
            palabras
          );
          if (frame < startFrame || frame > endFrame) return null;

          const tr = p.trayectoriaSuelo!;
          const x1 = 960 + tr.desdeX;
          const x2 = 960 + tr.hastaX;
          const y = tr.y ?? 815;
          const color = tr.color ?? "#22D3EE";
          const drawP = interpolate(
            frame,
            [startFrame, startFrame + 18],
            [0, 1],
            { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
          );
          const curX = x1 + (x2 - x1) * drawP;
          const dashOffset = -(frame * 3.5);

          return (
            <g key={`traj-${p.id}-${idx}`}>
              <ellipse
                cx={x1}
                cy={y}
                rx="26"
                ry="8"
                fill="rgba(34,211,238,0.2)"
                stroke={color}
                strokeWidth="3"
              />
              <line
                x1={x1}
                y1={y}
                x2={curX}
                y2={y}
                stroke={color}
                strokeWidth="5"
                strokeDasharray="16 10"
                strokeDashoffset={dashOffset}
                strokeLinecap="round"
              />
              <ellipse
                cx={curX}
                cy={y}
                rx="32"
                ry="10"
                fill="rgba(34,211,238,0.25)"
                stroke={color}
                strokeWidth="3.5"
              />
              {tr.etiqueta && (
                <text
                  x={(x1 + curX) * 0.5}
                  y={y + 32}
                  textAnchor="middle"
                  fill={color}
                  fontSize="22"
                  fontWeight="900"
                  fontFamily="Inter, system-ui, sans-serif"
                  style={{
                    filter: "drop-shadow(0px 3px 6px rgba(0,0,0,0.85))",
                  }}
                >
                  {tr.etiqueta}
                </text>
              )}
            </g>
          );
        })}

        {/* Cotas vectoriales diegéticas en el espacio del escenario */}
        {cotas.map((cota, idx) => {
          const { startFrame, endFrame } = resolveTimeRangeFrames(
            cota,
            durationInFrames,
            fps,
            palabras
          );
          if (frame < startFrame || frame > endFrame) return null;

          const drawProgress = interpolate(
            frame,
            [startFrame, startFrame + 14],
            [0, 1],
            { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
          );
          const fadeOut = interpolate(
            frame,
            [Math.max(startFrame + 15, endFrame - 10), endFrame],
            [1, 0],
            { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
          );

          const safeDestX = Math.max(540, Math.min(1320, cota.destinoX));
          const safeDestY = Math.max(185, Math.min(720, cota.destinoY));
          const curX =
            cota.origenX + (safeDestX - cota.origenX) * drawProgress;
          const curY =
            cota.origenY + (safeDestY - cota.origenY) * drawProgress;
          const color = cota.color ?? "#22D3EE";
          const dashOffset = -(frame * 2.2);
          const isTopBanner = safeDestY <= 280;
          const alignRight = safeDestX >= cota.origenX;
          const textAnchor = isTopBanner ? "middle" : alignRight ? "start" : "end";
          const textOffsetX = isTopBanner ? 0 : alignRight ? 16 : -16;
          const textOffsetY = isTopBanner ? -18 : 14;
          const labelOffsetY = isTopBanner ? -56 : -28;

          return (
            <g key={cota.id ?? `cota-${idx}`} opacity={fadeOut}>
              {/* Punto de anclaje en el objeto/personaje */}
              <circle
                cx={cota.origenX}
                cy={cota.origenY}
                r={7}
                fill={color}
                stroke="#0F172A"
                strokeWidth="3"
              />
              <circle
                cx={cota.origenX}
                cy={cota.origenY}
                r={13 + Math.sin(frame / 4) * 3}
                fill="none"
                stroke={color}
                strokeWidth="2.5"
                opacity="0.65"
              />

              {/* Línea punteada animada */}
              <line
                x1={cota.origenX}
                y1={cota.origenY}
                x2={curX}
                y2={curY}
                stroke="#0F172A"
                strokeWidth="7"
                strokeLinecap="round"
              />
              <line
                x1={cota.origenX}
                y1={cota.origenY}
                x2={curX}
                y2={curY}
                stroke={color}
                strokeWidth="4"
                strokeDasharray="10 8"
                strokeDashoffset={dashOffset}
                strokeLinecap="round"
              />

              {/* Nodo extremo y lectura tipográfica diegética (sin caja pesada) */}
              {drawProgress > 0.65 && (
                <g
                  transform={`translate(${safeDestX}, ${safeDestY})`}
                  opacity={interpolate(drawProgress, [0.65, 1], [0, 1])}
                >
                  <circle
                    cx={0}
                    cy={0}
                    r={5}
                    fill="#FFFFFF"
                    stroke={color}
                    strokeWidth="3"
                  />
                  {cota.etiqueta && (
                    <text
                      x={textOffsetX}
                      y={labelOffsetY}
                      textAnchor={textAnchor}
                      fill="#E2E8F0"
                      fontSize="21"
                      fontWeight="800"
                      letterSpacing="2"
                      fontFamily="Inter, system-ui, sans-serif"
                      style={{
                        filter:
                          "drop-shadow(0px 2px 4px rgba(0,0,0,0.95)) drop-shadow(0px 0px 8px rgba(0,0,0,0.85))",
                      }}
                    >
                      {cota.etiqueta.toUpperCase()}
                    </text>
                  )}
                  <text
                    x={textOffsetX}
                    y={textOffsetY}
                    textAnchor={textAnchor}
                    fill={color}
                    fontSize="44"
                    fontWeight="900"
                    fontFamily="Inter, system-ui, sans-serif"
                    style={{
                      filter:
                        "drop-shadow(0px 4px 8px rgba(0,0,0,0.95)) drop-shadow(0px 0px 14px rgba(0,0,0,0.85))",
                    }}
                  >
                    {cota.valor}
                  </text>
                </g>
              )}
            </g>
          );
        })}
      </svg>
    </div>
  );
};

/**
 * Silueta desenfocada en primerísimo plano para encuadres "sobre_hombro" (Over-The-Shoulder).
 */
export const OverTheShoulderForeground: React.FC<{
  lado: "izquierda" | "derecha";
  colorRim?: string;
}> = ({ lado, colorRim = "#38BDF8" }) => {
  const frame = useCurrentFrame();
  const breathY = Math.sin(frame / 10) * 4;
  const isLeft = lado === "izquierda";

  return (
    <div
      style={{
        position: "absolute",
        inset: 0,
        pointerEvents: "none",
        zIndex: 42,
        overflow: "hidden",
      }}
    >
      <svg
        width="1920"
        height="1080"
        viewBox="0 0 1920 1080"
        style={{
          filter: "blur(10px)",
          transform: `translateY(${breathY}px)`,
        }}
      >
        {isLeft ? (
          <g>
            {/* Hombro y cabeza en primer plano izquierdo */}
            <path
              d="M -80 1120 Q 120 760 360 880 L 420 1120 Z"
              fill="#090D16"
              stroke={colorRim}
              strokeWidth="8"
            />
            <circle
              cx="125"
              cy="560"
              r="210"
              fill="#090D16"
              stroke={colorRim}
              strokeWidth="7"
            />
          </g>
        ) : (
          <g>
            {/* Hombro y cabeza en primer plano derecho */}
            <path
              d="M 2000 1120 Q 1800 760 1560 880 L 1500 1120 Z"
              fill="#090D16"
              stroke={colorRim}
              strokeWidth="8"
            />
            <circle
              cx="1795"
              cy="560"
              r="210"
              fill="#090D16"
              stroke={colorRim}
              strokeWidth="7"
            />
          </g>
        )}
      </svg>
    </div>
  );
};

/**
 * Insert Cinemático de Mano Articulada en Primer Plano (Macro Detail Shot).
 * Se activa cuando un PlanoCamara tiene tipo === "detalle_mano".
 */
export const HandInsertOverlay: React.FC<{
  plano: PlanoCamara;
  localFrame: number;
  durationFrames: number;
}> = ({ plano, localFrame, durationFrames }) => {
  const { fps } = useVideoConfig();
  const enter = spring({
    frame: localFrame,
    fps,
    config: { damping: 14, stiffness: 160, mass: 0.7 },
  });
  const exit = interpolate(
    localFrame,
    [Math.max(1, durationFrames - 8), durationFrames],
    [1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );
  const progress = Math.min(1, Math.max(0, localFrame / Math.max(1, durationFrames)));
  const accion = plano.accionMano ?? "verter_acido";

  // Ángulos articulados de dedos y muñeca según la acción
  const wristAngle = Math.sin(progress * Math.PI) * 14;
  const fingerCurl = Math.sin(localFrame / 4) * 6;

  return (
    <div
      style={{
        position: "absolute",
        inset: 0,
        zIndex: 44,
        pointerEvents: "none",
        opacity: Math.min(enter, exit),
        background:
          "radial-gradient(circle at 50% 50%, rgba(15,23,42,0.52) 0%, rgba(2,6,23,0.88) 100%)",
        backdropFilter: "blur(10px)",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <svg width="1920" height="1080" viewBox="0 0 1920 1080" fill="none">
        {/* Marco cinemático de plano detalle */}
        <circle
          cx="960"
          cy="520"
          r="360"
          fill="#0F172A"
          stroke="#38BDF8"
          strokeWidth="6"
          opacity="0.92"
        />
        <circle
          cx="960"
          cy="520"
          r="342"
          fill="none"
          stroke="#E2E8F0"
          strokeWidth="2"
          strokeDasharray="12 10"
          opacity="0.35"
        />

        {accion === "verter_acido" && (
          <g>
            {/* Cuba de algodón al fondo del insert */}
            <rect
              x="760"
              y="620"
              width="400"
              height="160"
              rx="22"
              fill="#1E293B"
              stroke="#000"
              strokeWidth="7"
            />
            <path
              d="M 780 680 Q 860 650 960 680 Q 1060 705 1140 675 L 1140 765 L 780 765 Z"
              fill="#84CC16"
              opacity="0.85"
            />
            {/* Gotas cayendo */}
            <circle
              cx="940"
              cy={470 + ((localFrame * 11) % 180)}
              r="11"
              fill="#A3E635"
              stroke="#000"
              strokeWidth="3"
            />
            <circle
              cx="965"
              cy={510 + ((localFrame * 11 + 85) % 160)}
              r="9"
              fill="#BEF264"
              stroke="#000"
              strokeWidth="3"
            />
            {/* Brazo y mano articulada inclinando matraz */}
            <g
              transform={`translate(${1180 - enter * 120}, 390) rotate(${-18 - wristAngle})`}
            >
              {/* Manga */}
              <path
                d="M 120 -40 L 380 -110 L 410 -10 L 145 55 Z"
                fill="#0284C7"
                stroke="#000"
                strokeWidth="7"
              />
              {/* Palma y dedos articulados */}
              <rect
                x="45"
                y="-32"
                width="92"
                height="78"
                rx="24"
                fill="#0F172A"
                stroke="#38BDF8"
                strokeWidth="4"
              />
              <rect
                x="18"
                y="-26"
                width="54"
                height="18"
                rx="9"
                fill="#0F172A"
                stroke="#38BDF8"
                strokeWidth="3.5"
                transform={`rotate(${fingerCurl})`}
              />
              <rect
                x="14"
                y="-4"
                width="58"
                height="18"
                rx="9"
                fill="#0F172A"
                stroke="#38BDF8"
                strokeWidth="3.5"
              />
              <rect
                x="18"
                y="18"
                width="52"
                height="18"
                rx="9"
                fill="#0F172A"
                stroke="#38BDF8"
                strokeWidth="3.5"
              />
              {/* Matraz sujetado */}
              <path
                d="M -65 -55 L -15 -55 L 15 45 L -95 45 Z"
                fill="rgba(226,232,240,0.3)"
                stroke="#F8FAFC"
                strokeWidth="5"
              />
              <path
                d="M -82 10 L 4 10 L 12 40 L -90 40 Z"
                fill="#84CC16"
              />
            </g>
          </g>
        )}

        {accion === "prensar_palanca" && (
          <g>
            {/* Engranaje y manómetro de prensa */}
            <circle
              cx="830"
              cy="530"
              r="95"
              fill="#1E293B"
              stroke="#000"
              strokeWidth="8"
            />
            <circle
              cx="830"
              cy="530"
              r="72"
              fill="#FEF2F2"
              stroke="#EF4444"
              strokeWidth="5"
            />
            <line
              x1="830"
              y1="530"
              x2={830 + Math.cos(-1.8 + progress * 2.6) * 56}
              y2={530 + Math.sin(-1.8 + progress * 2.6) * 56}
              stroke="#DC2626"
              strokeWidth="6"
              strokeLinecap="round"
            />
            {/* Palanca bajando con mano articulada */}
            <g
              transform={`translate(930, 530) rotate(${-28 + progress * 56})`}
            >
              <rect
                x="0"
                y="-14"
                width="260"
                height="28"
                rx="12"
                fill="#94A3B8"
                stroke="#000"
                strokeWidth="6"
              />
              <circle
                cx="250"
                cy="0"
                r="26"
                fill="#EF4444"
                stroke="#000"
                strokeWidth="6"
              />
              {/* Mano agarrando el pomo rojo */}
              <g transform="translate(230, -35)">
                <path
                  d="M 45 -5 L 220 -65 L 245 25 L 65 75 Z"
                  fill="#0284C7"
                  stroke="#000"
                  strokeWidth="6"
                />
                <rect
                  x="-10"
                  y="0"
                  width="74"
                  height="66"
                  rx="22"
                  fill="#0F172A"
                  stroke="#38BDF8"
                  strokeWidth="4"
                />
                <rect
                  x="-18"
                  y="10"
                  width="36"
                  height="16"
                  rx="8"
                  fill="#0F172A"
                  stroke="#38BDF8"
                  strokeWidth="3"
                />
                <rect
                  x="-18"
                  y="28"
                  width="38"
                  height="16"
                  rx="8"
                  fill="#0F172A"
                  stroke="#38BDF8"
                  strokeWidth="3"
                />
              </g>
            </g>
          </g>
        )}

        {accion === "estirar_cadena" && (
          <g>
            {/* Eslabones metálicos tensándose en primer plano */}
            {[-2, -1, 0, 1, 2].map((i) => {
              const stretch = 1 + progress * 0.16;
              const cx = 960 + i * 76 * stretch;
              return (
                <rect
                  key={i}
                  x={cx - 38}
                  y={496}
                  width={76}
                  height={42}
                  rx="20"
                  fill="none"
                  stroke={i === 0 ? "#FFE600" : "#38BDF8"}
                  strokeWidth="10"
                />
              );
            })}
            {/* Mano izquierda y derecha tirando de los extremos */}
            <g transform={`translate(${660 - progress * 34}, 485)`}>
              <path
                d="M -190 -20 L -20 0 L -20 68 L -190 55 Z"
                fill="#0284C7"
                stroke="#000"
                strokeWidth="6"
              />
              <rect
                x="-30"
                y="-4"
                width="76"
                height="72"
                rx="20"
                fill="#0F172A"
                stroke="#22D3EE"
                strokeWidth="4"
              />
            </g>
            <g transform={`translate(${1260 + progress * 34}, 485)`}>
              <path
                d="M 190 -20 L 20 0 L 20 68 L 190 55 Z"
                fill="#0284C7"
                stroke="#000"
                strokeWidth="6"
              />
              <rect
                x="-46"
                y="-4"
                width="76"
                height="72"
                rx="20"
                fill="#0F172A"
                stroke="#22D3EE"
                strokeWidth="4"
              />
            </g>
          </g>
        )}

        {accion === "girar_valvula" && (
          <g>
            {/* Volante rojo del Bakelizador girando con mano articulada */}
            <g
              transform={`translate(960, 520) rotate(${progress * 165})`}
            >
              <circle
                cx="0"
                cy="0"
                r="135"
                fill="none"
                stroke="#EF4444"
                strokeWidth="24"
              />
              <circle
                cx="0"
                cy="0"
                r="135"
                fill="none"
                stroke="#000"
                strokeWidth="6"
              />
              <line
                x1="-125"
                y1="0"
                x2="125"
                y2="0"
                stroke="#EF4444"
                strokeWidth="18"
              />
              <line
                x1="0"
                y1="-125"
                x2="0"
                y2="125"
                stroke="#EF4444"
                strokeWidth="18"
              />
              <circle
                cx="0"
                cy="0"
                r="34"
                fill="#F59E0B"
                stroke="#000"
                strokeWidth="6"
              />
            </g>
            {/* Mano sujetando el borde superior del volante */}
            <g
              transform={`translate(${960 + Math.cos(-1.57 + progress * 2.8) * 125}, ${520 + Math.sin(-1.57 + progress * 2.8) * 125})`}
            >
              <path
                d="M 35 -35 L 240 -140 L 275 -55 L 65 30 Z"
                fill="#F8FAFC"
                stroke="#000"
                strokeWidth="6"
              />
              <rect
                x="-36"
                y="-36"
                width="74"
                height="68"
                rx="22"
                fill="#0F172A"
                stroke="#F97316"
                strokeWidth="4"
              />
            </g>
          </g>
        )}

        {accion === "tocar_esfera" && (
          <g>
            {/* Esfera de celuloide / acero brillante sobre pedestal y mano con dedos tocándola */}
            <circle
              cx="910"
              cy="540"
              r="110"
              fill="#FACC15"
              stroke="#000"
              strokeWidth="8"
            />
            <circle cx="875" cy="500" r="32" fill="#FEF08A" opacity="0.9" />
            <g transform={`translate(${1080 - progress * 45}, 490)`}>
              <path
                d="M 110 -10 L 340 -60 L 360 30 L 125 68 Z"
                fill="#0284C7"
                stroke="#000"
                strokeWidth="6"
              />
              <rect
                x="28"
                y="-12"
                width="90"
                height="74"
                rx="22"
                fill="#0F172A"
                stroke="#38BDF8"
                strokeWidth="4"
              />
              {/* Dedo índice extendido tocando la esfera */}
              <rect
                x="-38"
                y="2"
                width="76"
                height="20"
                rx="10"
                fill="#0F172A"
                stroke="#38BDF8"
                strokeWidth="4"
              />
            </g>
          </g>
        )}

        {accion === "apilar_bloques" && (
          <g>
            {/* Base de mampostería agrietándose bajo el peso */}
            <rect
              x="760"
              y="620"
              width="400"
              height="90"
              rx="10"
              fill="#475569"
              stroke="#000"
              strokeWidth="7"
            />
            <rect
              x="800"
              y="535"
              width="320"
              height="85"
              rx="8"
              fill="#64748B"
              stroke="#000"
              strokeWidth="7"
            />
            {/* Grietas amarillas/rojas apareciendo en el cimiento */}
            <path
              d="M 920 620 L 940 665 L 915 708 M 1020 620 L 1000 670 L 1030 708"
              stroke="#EF4444"
              strokeWidth="6"
              fill="none"
              opacity={0.4 + progress * 0.6}
            />
            {/* Mano articulada descendiendo con un pesado sillar de piedra */}
            <g
              transform={`translate(960, ${410 + progress * 68})`}
            >
              <rect
                x="-120"
                y="-45"
                width="240"
                height="80"
                rx="8"
                fill="#94A3B8"
                stroke="#000"
                strokeWidth="7"
              />
              <text
                x="0"
                y="5"
                textAnchor="middle"
                fill="#0F172A"
                fontSize="24"
                fontWeight="900"
              >
                CARGA +10 t
              </text>
              {/* Mano sujetando desde arriba */}
              <path
                d="M 80 -80 L 280 -160 L 310 -75 L 110 -15 Z"
                fill="#0284C7"
                stroke="#000"
                strokeWidth="6"
              />
              <rect
                x="30"
                y="-70"
                width="84"
                height="60"
                rx="18"
                fill="#0F172A"
                stroke="#38BDF8"
                strokeWidth="4"
              />
            </g>
          </g>
        )}

        {accion === "medir_compas" && (
          <g>
            {/* Diagrama de viga 1x vs 2x en pergamino técnico */}
            <rect
              x="730"
              y="420"
              width="460"
              height="220"
              rx="14"
              fill="#1E293B"
              stroke="#38BDF8"
              strokeWidth="5"
            />
            <rect
              x="775"
              y="510"
              width="70"
              height="70"
              fill="#0284C7"
              stroke="#000"
              strokeWidth="5"
            />
            <rect
              x="920"
              y="445"
              width="140"
              height="140"
              fill="#F59E0B"
              stroke="#000"
              strokeWidth="6"
            />
            <line
              x1="990"
              y1="445"
              x2="990"
              y2="585"
              stroke="#000"
              strokeWidth="4"
            />
            <line
              x1="920"
              y1="515"
              x2="1060"
              y2="515"
              stroke="#000"
              strokeWidth="4"
            />
            {/* Mano con compás de latón abriéndose al doble */}
            <g transform={`translate(${1080 - progress * 40}, 430)`}>
              <line
                x1="0"
                y1="0"
                x2={-60 - progress * 50}
                y2="130"
                stroke="#FACC15"
                strokeWidth="8"
                strokeLinecap="round"
              />
              <line
                x1="0"
                y1="0"
                x2="30"
                y2="130"
                stroke="#FACC15"
                strokeWidth="8"
                strokeLinecap="round"
              />
              <circle cx="0" cy="0" r="14" fill="#F59E0B" stroke="#000" strokeWidth="4" />
              <path
                d="M 30 -30 L 220 -90 L 245 -10 L 50 35 Z"
                fill="#0284C7"
                stroke="#000"
                strokeWidth="6"
              />
              <rect
                x="-15"
                y="-28"
                width="74"
                height="62"
                rx="18"
                fill="#0F172A"
                stroke="#FFE600"
                strokeWidth="4"
              />
            </g>
          </g>
        )}

        {accion === "tensar_cable_acero" && (
          <g>
            {/* Cable trenzado de acero estructural sometido a tracción límite */}
            <line
              x1="660"
              y1="520"
              x2="1260"
              y2="520"
              stroke="#64748B"
              strokeWidth={28 - progress * 10}
              strokeLinecap="round"
            />
            <line
              x1="660"
              y1="520"
              x2="1260"
              y2="520"
              stroke="#EF4444"
              strokeWidth="8"
              strokeDasharray="18 12"
              opacity={progress}
            />
            {/* Hebras rompiéndose en el centro */}
            {progress > 0.45 && (
              <g>
                <path
                  d="M 940 505 L 915 470 M 980 535 L 1010 570 M 960 500 L 965 460"
                  stroke="#FFE600"
                  strokeWidth="5"
                  strokeLinecap="round"
                />
              </g>
            )}
            {/* Mordazas y manos tensando */}
            <g transform={`translate(${680 - progress * 35}, 485)`}>
              <rect
                x="-30"
                y="-4"
                width="76"
                height="72"
                rx="16"
                fill="#0F172A"
                stroke="#38BDF8"
                strokeWidth="4"
              />
            </g>
            <g transform={`translate(${1240 + progress * 35}, 485)`}>
              <rect
                x="-46"
                y="-4"
                width="76"
                height="72"
                rx="16"
                fill="#0F172A"
                stroke="#38BDF8"
                strokeWidth="4"
              />
            </g>
          </g>
        )}

        {accion === "bajar_interruptor" && (
          <g>
            {/* Base del cuadro industrial de corte eléctrico */}
            <rect
              x="760"
              y="380"
              width="400"
              height="300"
              rx="18"
              fill="#1E293B"
              stroke="#000000"
              strokeWidth="7"
            />
            {/* Contactos de cobre y cuchilla */}
            <rect x="920" y="420" width="80" height="40" rx="6" fill="#F59E0B" stroke="#000" strokeWidth="4" />
            <rect x="920" y="580" width="80" height="40" rx="6" fill="#F59E0B" stroke="#000" strokeWidth="4" />
            {/* Palanca de corte industrial que desciende con progress */}
            <g transform={`translate(960, 440) rotate(${progress * 72})`}>
              <rect x="-14" y="0" width="28" height="150" rx="10" fill="#EF4444" stroke="#000" strokeWidth="5" />
              <circle cx="0" cy="150" r="22" fill="#DC2626" stroke="#000" strokeWidth="5" />
            </g>
            {/* Chispas eléctricas que se extinguen al bajar el interruptor */}
            {progress < 0.6 && (
              <g>
                <line x1="930" y1="440" x2="905" y2="415" stroke="#FFE600" strokeWidth="4" />
                <line x1="990" y1="440" x2="1025" y2="420" stroke="#38BDF8" strokeWidth="4" />
                <circle cx="960" cy="440" r="14" fill="#FEF08A" opacity="0.7" />
              </g>
            )}
            {/* Mano del Stickman tirando firmemente de la palanca */}
            <g transform={`translate(${1020 + progress * 60}, ${540 + progress * 70})`}>
              <path d="M 0 -20 L 160 -50 L 180 15 L 20 40 Z" fill="#0284C7" stroke="#000" strokeWidth="6" />
              <rect x="-40" y="-18" width="75" height="65" rx="18" fill="#0F172A" stroke="#38BDF8" strokeWidth="4" />
            </g>
          </g>
        )}

        {accion === "ajustar_telescopio" && (
          <g>
            {/* Tubo óptico de precisión del telescopio */}
            <rect
              x="680"
              y="470"
              width="480"
              height="110"
              rx="16"
              fill="#0F172A"
              stroke="#38BDF8"
              strokeWidth="6"
            />
            {/* Anillos de graduación micrométrica */}
            <line x1="840" y1="470" x2="840" y2="580" stroke="#FFE600" strokeWidth="5" />
            <line x1="980" y1="470" x2="980" y2="580" stroke="#FFE600" strokeWidth="5" />
            {/* Rueda dentada de enfoque micrométrico */}
            <g transform={`translate(910, 525) rotate(${localFrame * 4})`}>
              <circle cx="0" cy="0" r="44" fill="#334155" stroke="#000" strokeWidth="5" />
              {[0, 45, 90, 135, 180, 225, 270, 315].map((ang) => (
                <line
                  key={`sp-${ang}`}
                  x1="0"
                  y1="0"
                  x2={Math.cos((ang * Math.PI) / 180) * 44}
                  y2={Math.sin((ang * Math.PI) / 180) * 44}
                  stroke="#94A3B8"
                  strokeWidth="3.5"
                />
              ))}
            </g>
            {/* Mano ajustando la rueda de enfoque */}
            <g transform={`translate(970, 505)`}>
              <path d="M 40 -10 L 190 -35 L 205 25 L 50 45 Z" fill="#0284C7" stroke="#000" strokeWidth="6" />
              <rect x="-24" y="-2" width="70" height="55" rx="16" fill="#0F172A" stroke="#38BDF8" strokeWidth="4" />
            </g>
          </g>
        )}

        {accion === "girar_dial_radio" && (
          <g>
            {/* Macro dial de sintonizador analógico */}
            <rect x="680" y="440" width="460" height="180" rx="18" fill="#78350F" stroke="#000" strokeWidth="7" />
            <rect x="710" y="465" width="280" height="70" rx="10" fill="#FEF08A" stroke="#000" strokeWidth="4" />
            <line x1="730" y1="500" x2="970" y2="500" stroke="#000" strokeWidth="3" />
            <line x1="860" y1="470" x2="860" y2="530" stroke="#DC2626" strokeWidth="5" />
            <text x="860" y="490" fill="#DC2626" fontSize="16" fontWeight="900" fontFamily="sans-serif" textAnchor="middle">1420 MHz</text>
            
            {/* Gran perilla estriada girando */}
            <g transform={`translate(1040, 530) rotate(${localFrame * 3})`}>
              <circle cx="0" cy="0" r="65" fill="#1E293B" stroke="#000" strokeWidth="6" />
              <circle cx="0" cy="0" r="48" fill="#0F172A" stroke="#64748B" strokeWidth="3" />
              <line x1="0" y1="-45" x2="0" y2="-20" stroke="#FFFFFF" strokeWidth="5" strokeLinecap="round" />
            </g>
            {/* Mano con dedos sobre la perilla */}
            <g transform="translate(1080, 510)">
              <path d="M 50 -30 L 190 -50 L 210 30 L 70 50 Z" fill="#1E293B" stroke="#000" strokeWidth="6" />
              <rect x="-25" y="-15" width="80" height="60" rx="18" fill="#0F172A" stroke="#38BDF8" strokeWidth="4" />
              <circle cx="-10" cy="15" r="14" fill="#38BDF8" opacity="0.4" />
            </g>
          </g>
        )}

        {accion === "escribir_tiza_pizarra" && (
          <g>
            {/* Superficie de pizarra verde oscuro */}
            <rect x="660" y="430" width="540" height="200" rx="16" fill="#064E3B" stroke="#78350F" strokeWidth="8" />
            <text x="880" y="540" fill="#FDE047" fontSize="48" fontWeight="bold" fontFamily="serif" textAnchor="middle">
              N = R* · fp
            </text>
            {/* Mano sosteniendo tiza blanca */}
            <g transform={`translate(${930 + Math.sin(localFrame * 0.2) * 20}, ${510 + Math.cos(localFrame * 0.2) * 10})`}>
              {/* Tiza blanca */}
              <rect x="-35" y="10" width="40" height="12" rx="3" fill="#FFFFFF" stroke="#000" strokeWidth="2.5" transform="rotate(-30)" />
              {/* Chispas de polvo de tiza */}
              <circle cx="-35" cy="22" r="3" fill="#FFFFFF" opacity="0.8" />
              <circle cx="-42" cy="18" r="2.5" fill="#FEF08A" opacity="0.7" />
              {/* Manga y dedos */}
              <path d="M 30 -20 L 170 -40 L 190 40 L 40 40 Z" fill="#FFFFFF" stroke="#000" strokeWidth="6" />
              <rect x="-10" y="-8" width="65" height="50" rx="14" fill="#0F172A" stroke="#38BDF8" strokeWidth="4" />
            </g>
          </g>
        )}

        {accion === "pulsar_boton_casino" && (
          <g>
            {/* Carcasa cromada de palanca */}
            <rect x="740" y="420" width="220" height="220" rx="20" fill="#1F2937" stroke="#000" strokeWidth="7" />
            <circle cx="850" cy="530" r="60" fill="#374151" stroke="#000" strokeWidth="5" />
            {/* Palanca metálica con bola roja */}
            <g transform={`translate(850, 530) rotate(${-25 + Math.sin(progress * Math.PI) * 55})`}>
              <line x1="0" y1="0" x2="0" y2="-120" stroke="#94A3B8" strokeWidth="16" strokeLinecap="round" />
              <circle cx="0" cy="-120" r="32" fill="#DC2626" stroke="#000" strokeWidth="5" />
              <circle cx="-8" cy="-128" r="10" fill="#F87171" />
            </g>
            {/* Mano accionando */}
            <g transform="translate(850, 410)">
              <path d="M 40 -10 L 180 -30 L 195 40 L 50 40 Z" fill="#1E293B" stroke="#000" strokeWidth="6" />
              <rect x="-15" y="-15" width="70" height="55" rx="16" fill="#0F172A" stroke="#38BDF8" strokeWidth="4" />
            </g>
          </g>
        )}

        {accion === "encender_cerilla" && (
          <g>
            {/* Cerilla de madera */}
            <line x1="820" y1="560" x2="980" y2="480" stroke="#D97706" strokeWidth="10" strokeLinecap="round" />
            <circle cx="980" cy="480" r="12" fill="#991B1B" stroke="#000" strokeWidth="3" />
            {/* Llama encendiéndose y luego apagándose con humo */}
            {progress < 0.65 ? (
              <g transform="translate(985, 465)">
                <path d="M 0 0 C 14 -10, 16 -35, 0 -50 C -16 -35, -14 -10, 0 0 Z" fill="#F59E0B" stroke="#DC2626" strokeWidth="3" />
                <path d="M 0 -5 C 8 -12, 8 -28, 0 -36 C -8 -28, -8 -12, 0 -5 Z" fill="#FEF08A" />
              </g>
            ) : (
              <g transform="translate(985, 455)">
                {/* Humo gris disipándose */}
                <circle cx="0" cy="-10" r="14" fill="#94A3B8" opacity="0.6" />
                <circle cx="8" cy="-28" r="18" fill="#64748B" opacity="0.4" />
                <circle cx="-6" cy="-44" r="22" fill="#475569" opacity="0.25" />
              </g>
            )}
            {/* Dedos sosteniendo el fósforo */}
            <g transform="translate(790, 570)">
              <path d="M 20 10 L 160 -10 L 170 60 L 30 70 Z" fill="#1E293B" stroke="#000" strokeWidth="6" />
              <rect x="-10" y="5" width="60" height="48" rx="14" fill="#0F172A" stroke="#38BDF8" strokeWidth="4" />
            </g>
          </g>
        )}

        {accion === "tallar_pedernal_silex" && (
          <g>
            {/* Mano izquierda anatómica sosteniendo el núcleo de sílex con pinza de precisión */}
            <g transform="translate(835, 555)">
              {/* Antebrazo vestido con cuero paleolítico */}
              <path d="M -230 30 L -75 -8 L -58 62 L -215 96 Z" fill="#92400E" stroke="#111827" strokeWidth="7" strokeLinejoin="round" />
              <path d="M -90 -5 L -72 -8 L -56 62 L -74 66 Z" fill="#F59E0B" stroke="#111827" strokeWidth="5" />
              {/* Palma tenar cálida */}
              <ellipse cx="-52" cy="22" rx="44" ry="34" fill="#FDBA74" stroke="#111827" strokeWidth="6" />
              {/* Dedos medio y anular doblados bajo el núcleo */}
              <ellipse cx="-20" cy="42" rx="22" ry="11" fill="#FB923C" stroke="#111827" strokeWidth="5" />
              <ellipse cx="-26" cy="56" rx="19" ry="10" fill="#EA580C" stroke="#111827" strokeWidth="5" />

              {/* Núcleo bifacial de sílex / obsidiana con aristas concoideas */}
              <polygon
                points="6,-62 78,-40 94,20 38,70 -36,48 -52,-16"
                fill="#334155"
                stroke="#111827"
                strokeWidth="7"
                strokeLinejoin="round"
              />
              <polygon points="6,-62 78,-40 42,-4 -18,-18" fill="#64748B" />
              <polygon points="42,-4 78,-40 94,20 38,70" fill="#1E293B" opacity="0.55" />
              <polyline points="6,-62 42,-4 38,70" fill="none" stroke="#CBD5E1" strokeWidth="3" strokeLinecap="round" />

              {/* Pulgar oponible largo e índice haciendo pinza de precisión con uñas definidas */}
              <g transform="rotate(-14 -38 -14)">
                <rect x="-78" y="-26" width="76" height="24" rx="12" fill="#FED7AA" stroke="#111827" strokeWidth="6" />
                <ellipse cx="-12" cy="-14" rx="7" ry="6" fill="#FFEDD5" stroke="#111827" strokeWidth="2.5" />
              </g>
              <g transform="rotate(14 -36 24)">
                <rect x="-76" y="14" width="80" height="26" rx="13" fill="#FDBA74" stroke="#111827" strokeWidth="6" />
                <ellipse cx="-8" cy="27" rx="7.5" ry="6.5" fill="#FFEDD5" stroke="#111827" strokeWidth="2.5" />
              </g>
            </g>

            {/* Mano derecha empuñando percutor de cuarcita de río a 45 grados */}
            <g
              transform={`translate(${1075 - Math.min(1, progress * 2.1) * 145}, ${365 + Math.min(1, progress * 2.1) * 130}) rotate(${-45 + Math.min(1, progress * 2.1) * 22})`}
            >
              {/* Canto rodado percutor */}
              <ellipse cx="-14" cy="6" rx="56" ry="38" fill="#D97706" stroke="#111827" strokeWidth="7" />
              <ellipse cx="-26" cy="-4" rx="22" ry="10" fill="#FBBF24" opacity="0.55" />
              {/* Antebrazo derecho */}
              <path d="M 42 -26 L 215 -88 L 238 -10 L 62 36 Z" fill="#92400E" stroke="#111827" strokeWidth="7" strokeLinejoin="round" />
              {/* Puño articulado con 4 nudillos y pulgar */}
              <rect x="-4" y="-30" width="66" height="58" rx="18" fill="#FDBA74" stroke="#111827" strokeWidth="6" />
              <rect x="-12" y="-24" width="24" height="14" rx="7" fill="#FED7AA" stroke="#111827" strokeWidth="4" />
              <rect x="-14" y="-8" width="24" height="14" rx="7" fill="#FED7AA" stroke="#111827" strokeWidth="4" />
              <rect x="-14" y="8" width="24" height="14" rx="7" fill="#FED7AA" stroke="#111827" strokeWidth="4" />
            </g>

            {/* Impacto a 45°: chispas y lasca cortante saliendo despedida */}
            {progress > 0.46 && (
              <g transform={`translate(${915 + (progress - 0.46) * 220}, ${525 + (progress - 0.46) * 90}) rotate(${(progress - 0.46) * 140})`}>
                <polygon
                  points="0,-38 28,12 0,46 -20,10"
                  fill="#38BDF8"
                  stroke="#111827"
                  strokeWidth="5.5"
                  strokeLinejoin="round"
                />
                <polygon points="0,-38 28,12 0,46" fill="#BAE6FD" opacity="0.55" />
                <line x1="0" y1="-38" x2="0" y2="46" stroke="#F0F9FF" strokeWidth="3" />
              </g>
            )}
            {progress > 0.44 && progress < 0.76 && (
              <g transform="translate(908, 515)">
                <line x1="0" y1="0" x2="-40" y2="-44" stroke="#FFE600" strokeWidth="6" strokeLinecap="round" />
                <line x1="0" y1="0" x2="46" y2="-38" stroke="#F97316" strokeWidth="6" strokeLinecap="round" />
                <line x1="0" y1="0" x2="52" y2="14" stroke="#FFE600" strokeWidth="5" strokeLinecap="round" />
              </g>
            )}
          </g>
        )}

        {accion === "proteger_brasa_manos" && (
          <g>
            {/* Resplandor volumétrico cálido en medio de la noche glacial */}
            <circle
              cx="960"
              cy="545"
              r={145 + Math.sin(localFrame * 0.2) * 12}
              fill="#EA580C"
              opacity="0.22"
            />
            <circle
              cx="960"
              cy="550"
              r={88 + Math.sin(localFrame * 0.24) * 8}
              fill="#F59E0B"
              opacity="0.32"
            />

            {/* Lecho de piedras oscuras, ramitas carbonizadas y última brasa humana viva */}
            <ellipse cx="960" cy="610" rx="128" ry="30" fill="#1E293B" stroke="#111827" strokeWidth="6" />
            <line x1="885" y1="604" x2="1032" y2="592" stroke="#451A03" strokeWidth="16" strokeLinecap="round" />
            <line x1="898" y1="590" x2="1025" y2="608" stroke="#292524" strokeWidth="14" strokeLinecap="round" />
            {[-78, -36, 12, 58, 92].map((sx, idx) => (
              <ellipse key={idx} cx={960 + sx} cy={614 + (idx % 2) * 4} rx="22" ry="12" fill="#475569" stroke="#111827" strokeWidth="4.5" />
            ))}

            {/* Carbón incandescente y pequeña lengua de fuego temblorosa */}
            <polygon
              points="916,596 948,554 988,558 1008,596 945,604"
              fill="#DC2626"
              stroke="#111827"
              strokeWidth="5.5"
              strokeLinejoin="round"
            />
            <polygon points="935,590 956,564 984,568 982,592" fill="#F97316" />
            <path
              d={`M 946 578 C 942 548, 956 526, ${962 + Math.sin(localFrame * 0.22) * 6} 508 C 974 528, 982 550, 976 578 Z`}
              fill="#F97316"
              stroke="#111827"
              strokeWidth="4.5"
            />
            <path
              d={`M 953 578 Q 960 548 ${962 + Math.sin(localFrame * 0.22) * 4} 530 Q 969 552 969 578 Z`}
              fill="#FEF08A"
            />

            {/* Chispas ascendentes cálidas */}
            {[0, 1, 2, 3, 4].map((k) => {
              const cy = 535 - ((localFrame * 2.1 + k * 34) % 145);
              const cx = 940 + k * 11 + Math.sin(localFrame * 0.18 + k) * 11;
              return <circle key={k} cx={cx} cy={cy} r={4.8 - k * 0.55} fill="#FEF08A" />;
            })}

            {/* Mano izquierda ahuecada con dedos esculpidos e iluminación cálida en el borde */}
            <g transform={`translate(${Math.sin(localFrame * 0.16) * 2.5}, 0)`}>
              <path
                d="M 690 585 C 718 505, 792 468, 858 492 C 876 500, 882 522, 868 534 C 884 544, 886 566, 870 578 C 882 590, 878 612, 858 618 C 798 632, 728 622, 690 585 Z"
                fill="#7C2D12"
                stroke="#111827"
                strokeWidth="6.5"
                strokeLinejoin="round"
              />
              {/* Luz de recorte naranja sobre palma y dedos */}
              <path
                d="M 852 498 C 868 508, 868 526, 852 534 M 856 540 C 872 550, 872 568, 854 576 M 852 582 C 866 592, 864 608, 848 612"
                fill="none"
                stroke="#FDBA74"
                strokeWidth="5"
                strokeLinecap="round"
              />
              <path d="M 760 540 Q 805 532 848 536 M 766 574 Q 808 568 850 574" fill="none" stroke="#431407" strokeWidth="4" strokeLinecap="round" />
            </g>

            {/* Mano derecha ahuecada simétrica protegiendo la llama */}
            <g transform={`translate(${-Math.sin(localFrame * 0.16) * 2.5}, 0)`}>
              <path
                d="M 1230 585 C 1202 505, 1128 468, 1062 492 C 1044 500, 1038 522, 1052 534 C 1036 544, 1034 566, 1050 578 C 1038 590, 1042 612, 1062 618 C 1122 632, 1192 622, 1230 585 Z"
                fill="#7C2D12"
                stroke="#111827"
                strokeWidth="6.5"
                strokeLinejoin="round"
              />
              <path
                d="M 1068 498 C 1052 508, 1052 526, 1068 534 M 1064 540 C 1048 550, 1048 568, 1066 576 M 1068 582 C 1054 592, 1056 608, 1072 612"
                fill="none"
                stroke="#FDBA74"
                strokeWidth="5"
                strokeLinecap="round"
              />
              <path d="M 1160 540 Q 1115 532 1072 536 M 1154 574 Q 1112 568 1070 574" fill="none" stroke="#431407" strokeWidth="4" strokeLinecap="round" />
            </g>
          </g>
        )}

        {/* Etiqueta diegética inferior del insert */}
        <text
          x="960"
          y="835"
          textAnchor="middle"
          fill="#FFE600"
          fontSize="34"
          fontWeight="900"
          letterSpacing="3"
          fontFamily="Inter, system-ui, sans-serif"
          style={{
            filter: "drop-shadow(0px 4px 8px rgba(0,0,0,0.95))",
          }}
        >
          {plano.etiquetaInsert ?? "DETALLE DE ACCIÓN"}
        </text>
      </svg>
    </div>
  );
};
