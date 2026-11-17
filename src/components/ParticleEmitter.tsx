import React from "react";
import { interpolate, random, useCurrentFrame, useVideoConfig } from "remotion";
import { EmisorParticulas, PalabraTiming } from "../types";
import { resolveTimeRangeFrames } from "../stickman/actionSequences";

interface ParticleEmitterLayerProps {
  emisores?: EmisorParticulas[];
  palabras?: PalabraTiming[];
}

export const ParticleEmitterLayer: React.FC<ParticleEmitterLayerProps> = ({
  emisores = [],
  palabras,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  if (emisores.length === 0) return null;

  return (
    <div
      style={{
        position: "absolute",
        inset: 0,
        pointerEvents: "none",
        zIndex: 32,
      }}
    >
      <svg width="1920" height="1080" viewBox="0 0 1920 1080" fill="none">
        {emisores.map((emisor, eIdx) => {
          const { startFrame, endFrame } = resolveTimeRangeFrames(
            emisor,
            durationInFrames,
            fps,
            palabras
          );
          if (frame < startFrame || frame > endFrame) return null;

          const localFrame = frame - startFrame;
          const totalDur = Math.max(1, endFrame - startFrame);
          const count = emisor.cantidad ?? 18;
          const seedBase = `${emisor.id ?? eIdx}-${emisor.tipo}`;

          return (
            <g key={seedBase}>
              {Array.from({ length: count }).map((_, i) => {
                const s1 = random(`${seedBase}-a-${i}`);
                const s2 = random(`${seedBase}-b-${i}`);
                const s3 = random(`${seedBase}-c-${i}`);

                // Ciclo continuo o balístico según el tipo
                const isContinuous =
                  emisor.tipo === "vapor_presion" ||
                  emisor.tipo === "rafagas_viento" ||
                  emisor.tipo === "fotones_luz" ||
                  emisor.tipo === "polvo_estelar";
                const cycleLen = isContinuous ? 50 : Math.min(75, totalDur);
                const particleAge = isContinuous
                  ? (localFrame + Math.floor(s3 * 50)) % cycleLen
                  : localFrame;
                const t = particleAge / fps; // tiempo en segundos

                if (emisor.tipo === "fotones_luz") {
                  const p = particleAge / cycleLen;
                  const vx = (s1 - 0.5) * 80;
                  const vy = -90 - s2 * 70;
                  const px = emisor.x + vx * t + Math.sin(t * 3 + i) * 15;
                  const py = emisor.y + vy * t;
                  const radius = 5 + s3 * 6;
                  const opacity = interpolate(
                    p,
                    [0, 0.15, 0.75, 1],
                    [0, 0.85, 0.6, 0]
                  );
                  const col = emisor.color ?? (i % 2 === 0 ? "#FDE047" : "#38BDF8");
                  return (
                    <g key={i}>
                      <circle
                        cx={px}
                        cy={py}
                        r={radius * 1.8}
                        fill={col}
                        opacity={opacity * 0.35}
                      />
                      <circle
                        cx={px}
                        cy={py}
                        r={radius}
                        fill={col}
                        stroke="#000"
                        strokeWidth="1.5"
                        opacity={opacity}
                      />
                    </g>
                  );
                }

                if (emisor.tipo === "polvo_estelar") {
                  const p = particleAge / cycleLen;
                  const px = emisor.x + (s1 - 0.5) * 480;
                  const py = emisor.y + (s2 - 0.5) * 320;
                  const twinkle = 0.4 + Math.sin(particleAge * 0.25 + i * 1.8) * 0.55;
                  const col = emisor.color ?? (i % 3 === 0 ? "#FFE600" : i % 2 === 0 ? "#38BDF8" : "#FFFFFF");
                  return (
                    <g key={i} transform={`translate(${px.toFixed(1)}, ${py.toFixed(1)}) scale(${twinkle.toFixed(2)})`}>
                      <polygon points="0,-9 3,-3 9,0 3,3 0,9 -3,3 -9,0 -3,-3" fill={col} stroke="#000" strokeWidth="1.2" />
                    </g>
                  );
                }

                if (emisor.tipo === "rafagas_viento") {
                  const p = particleAge / cycleLen;
                  // Flujo dinámico de DERECHA a IZQUIERDA con menor opacidad para sensación aerodinámica fluida
                  const startX = emisor.x + 380 - s1 * 140;
                  const startY = emisor.y - 120 + s2 * 240;
                  const px = startX - p * 760;
                  const py = startY + Math.sin(p * Math.PI * 2.5 + i) * 18;
                  const opacity = interpolate(
                    p,
                    [0, 0.15, 0.85, 1],
                    [0, 0.35, 0.28, 0]
                  );
                  return (
                    <path
                      key={i}
                      d={`M ${px.toFixed(1)} ${py.toFixed(1)} Q ${(px + 45).toFixed(1)} ${(py - 12).toFixed(1)} ${(px + 90).toFixed(1)} ${py.toFixed(1)} T ${(px + 160).toFixed(1)} ${py.toFixed(1)}`}
                      fill="none"
                      stroke={emisor.color ?? (i % 2 === 0 ? "#38BDF8" : "#E0F2FE")}
                      strokeWidth={i % 3 === 0 ? "2.8" : "1.8"}
                      strokeLinecap="round"
                      opacity={opacity}
                    />
                  );
                }

                if (emisor.tipo === "vapor_presion") {
                  const p = particleAge / cycleLen;
                  const vx = (s1 - 0.5) * 90;
                  const vy = -110 - s2 * 80;
                  const px = emisor.x + vx * t + Math.sin(t * 4 + i) * 12;
                  const py = emisor.y + vy * t;
                  const radius = 14 + p * 34;
                  const opacity = interpolate(
                    p,
                    [0, 0.2, 0.8, 1],
                    [0, 0.55, 0.35, 0]
                  );
                  return (
                    <circle
                      key={i}
                      cx={px}
                      cy={py}
                      r={radius}
                      fill={emisor.color ?? "#E2E8F0"}
                      opacity={opacity}
                    />
                  );
                }

                // Trayectoria balística determinista: x(t) = x0 + vx*t, y(t) = y0 + vy*t + 0.5*g*t^2
                const angle = -Math.PI * (0.15 + s1 * 0.7);
                const speed =
                  emisor.tipo === "eslabones_polimero"
                    ? 160 + s2 * 260
                    : 180 + s2 * 320;
                const vx = Math.cos(angle) * speed * (s3 > 0.5 ? 1 : -1);
                const vy = Math.sin(angle) * speed;
                const gravity =
                  emisor.tipo === "eslabones_polimero" ? 310 : 480;

                const px = emisor.x + vx * t;
                const py = emisor.y + vy * t + 0.5 * gravity * t * t;
                const rotDeg = (s1 * 360 + t * (240 + s2 * 300)) % 360;
                const flip3D = Math.cos(t * (4 + s3 * 5));
                const fade = interpolate(
                  localFrame,
                  [0, 5, totalDur - 8, totalDur],
                  [0, 1, 1, 0],
                  { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
                );

                if (emisor.tipo === "eslabones_polimero") {
                  const linkColor =
                    i % 3 === 0
                      ? "#FFE600"
                      : i % 2 === 0
                      ? "#38BDF8"
                      : "#E2E8F0";
                  return (
                    <g
                      key={i}
                      transform={`translate(${px.toFixed(1)}, ${py.toFixed(1)}) rotate(${rotDeg.toFixed(1)}) scale(${flip3D.toFixed(2)}, 1)`}
                      opacity={fade * 0.9}
                    >
                      <rect
                        x="-18"
                        y="-9"
                        width="36"
                        height="18"
                        rx="9"
                        fill="none"
                        stroke="#0F172A"
                        strokeWidth="6"
                      />
                      <rect
                        x="-18"
                        y="-9"
                        width="36"
                        height="18"
                        rx="9"
                        fill="none"
                        stroke={emisor.color ?? linkColor}
                        strokeWidth="3.5"
                      />
                    </g>
                  );
                }

                if (emisor.tipo === "gotas_acido") {
                  return (
                    <circle
                      key={i}
                      cx={px}
                      cy={py}
                      r={5 + s1 * 5}
                      fill={emisor.color ?? "#84CC16"}
                      stroke="#0F172A"
                      strokeWidth="2"
                      opacity={fade}
                    />
                  );
                }

                if (emisor.tipo === "fragmentos_marfil") {
                  return (
                    <polygon
                      key={i}
                      points="-8,-6 9,-4 5,8 -7,6"
                      fill={emisor.color ?? "#FEFCE8"}
                      stroke="#0F172A"
                      strokeWidth="2.5"
                      transform={`translate(${px.toFixed(1)}, ${py.toFixed(1)}) rotate(${rotDeg.toFixed(1)})`}
                      opacity={fade}
                    />
                  );
                }

                if (emisor.tipo === "escombros_piedra") {
                  const stoneColor =
                    i % 3 === 0
                      ? "#94A3B8"
                      : i % 2 === 0
                      ? "#64748B"
                      : "#CBD5E1";
                  return (
                    <polygon
                      key={i}
                      points="-12,-9 10,-11 14,7 -8,11"
                      fill={emisor.color ?? stoneColor}
                      stroke="#0F172A"
                      strokeWidth="3.5"
                      transform={`translate(${px.toFixed(1)}, ${py.toFixed(1)}) rotate(${rotDeg.toFixed(1)})`}
                      opacity={fade}
                    />
                  );
                }

                // Default: "chispas_quimicas"
                const sparkColor =
                  s1 > 0.5 ? emisor.color ?? "#FFE600" : "#F97316";
                return (
                  <g
                    key={i}
                    transform={`translate(${px.toFixed(1)}, ${py.toFixed(1)}) rotate(${rotDeg.toFixed(1)})`}
                    opacity={fade}
                  >
                    <line
                      x1="-10"
                      y1="0"
                      x2="10"
                      y2="0"
                      stroke={sparkColor}
                      strokeWidth="4"
                      strokeLinecap="round"
                    />
                    <circle cx="0" cy="0" r="4" fill="#FFFFFF" />
                  </g>
                );
              })}
            </g>
          );
        })}
      </svg>
    </div>
  );
};

/**
 * Iluminación volumétrica (haces de luz cenitales + partículas de polvo en suspensión)
 * como en las escenas de laboratorio y calle nocturna del video de referencia.
 */
export const LightRaysOverlay: React.FC<{ active?: boolean }> = ({
  active = true,
}) => {
  const frame = useCurrentFrame();
  if (!active) return null;

  return (
    <div
      style={{
        position: "absolute",
        inset: 0,
        pointerEvents: "none",
        zIndex: 12,
        mixBlendMode: "screen",
      }}
    >
      <svg width="1920" height="1080" viewBox="0 0 1920 1080" fill="none">
        <defs>
          <linearGradient id="volumetricRay" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#38BDF8" stopOpacity="0.16" />
            <stop offset="65%" stopColor="#FEF08A" stopOpacity="0.06" />
            <stop offset="100%" stopColor="#0F172A" stopOpacity="0" />
          </linearGradient>
        </defs>

        {/* Conos de luz cenitales suaves */}
        <polygon
          points="420,0 620,0 820,980 220,980"
          fill="url(#volumetricRay)"
        />
        <polygon
          points="1180,0 1380,0 1620,980 960,980"
          fill="url(#volumetricRay)"
        />

        {/* Motas de polvo suspendidas en los haces de luz */}
        {Array.from({ length: 18 }).map((_, i) => {
          const sx = random(`dust-x-${i}`);
          const sy = random(`dust-y-${i}`);
          const baseX = (i % 2 === 0 ? 340 : 1080) + sx * 380;
          const baseY = 120 + sy * 720;
          const dx = Math.sin(frame / (24 + (i % 7) * 3) + i) * 22;
          const dy = -((frame * (0.35 + (i % 4) * 0.12)) % 180);
          const pulse = 0.25 + Math.abs(Math.sin(frame / 18 + i)) * 0.45;
          return (
            <circle
              key={i}
              cx={baseX + dx}
              cy={baseY + dy}
              r={2 + (i % 3)}
              fill="#FEF9C3"
              opacity={pulse}
            />
          );
        })}
      </svg>
    </div>
  );
};
