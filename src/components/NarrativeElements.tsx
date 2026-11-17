import React from "react";
import {
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { ElementoNarrativo, PalabraTiming } from "../types";
import { resolveTimeRangeFrames } from "../stickman/actionSequences";

export interface NarrativeElementsProps {
  elementos?: ElementoNarrativo[];
  totalFrames?: number;
  palabras?: PalabraTiming[];
}

export const NarrativeElements: React.FC<NarrativeElementsProps> = ({
  elementos,
  totalFrames = 900,
  palabras,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  if (!elementos || elementos.length === 0) {
    return null;
  }

  return (
    <div className="absolute inset-0 pointer-events-none overflow-hidden z-30">
      {elementos.map((el, idx) => {
        const hasWindow =
          el.inicioProgreso !== undefined ||
          el.finProgreso !== undefined ||
          el.inicioSegundos !== undefined ||
          el.finSegundos !== undefined ||
          el.desdePalabra !== undefined ||
          el.hastaPalabra !== undefined;
        const { startFrame, endFrame } = hasWindow
          ? resolveTimeRangeFrames(el, totalFrames, fps, palabras)
          : { startFrame: 0, endFrame: totalFrames };

        if (frame < startFrame || frame > endFrame) {
          return null;
        }
        const relFrame = frame - startFrame;

        switch (el.tipo) {
          case "speed_counter":
            return <SpeedCounter key={idx} elemento={el} frame={relFrame} fps={fps} />;
          case "speed_lines":
            return <SpeedLines key={idx} elemento={el} frame={relFrame} />;
          case "flying_debris":
            return <FlyingDebris key={idx} frame={relFrame} fps={fps} />;
          case "giant_waves":
            return <GiantWaves key={idx} frame={relFrame} />;
          case "shockwave_burst":
            return <ShockwaveBurst key={idx} elemento={el} frame={relFrame} fps={fps} />;
          case "orbital_peace":
            return <OrbitalPeace key={idx} frame={relFrame} />;
          case "danger_vignette":
            return <DangerVignette key={idx} frame={relFrame} />;
          case "sparks_explosion":
            return <SparksExplosion key={idx} elemento={el} frame={relFrame} />;
          case "steam_vent":
            return <SteamVent key={idx} elemento={el} frame={relFrame} />;
          case "chemical_bubbles":
            return <ChemicalBubbles key={idx} elemento={el} frame={relFrame} />;
          default:
            return null;
        }
      })}
    </div>
  );
};

const SpeedCounter: React.FC<{
  elemento: ElementoNarrativo;
  frame: number;
  fps: number;
}> = ({ elemento, frame, fps }) => {
  const targetVal = elemento.valorNumerico ?? 1600;
  const unit = elemento.unidad ?? "KM/H";

  const countProgress = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 100, mass: 0.8 },
  });

  const currentNumber = Math.round(
    interpolate(countProgress, [0, 1], [0, targetVal])
  );
  const needleAngle = interpolate(countProgress, [0, 1], [-110, 85]);

  return (
    <div
      className="absolute top-[120px] left-1/2 -translate-x-1/2 flex flex-col items-center justify-center p-6 bg-white border-4 border-black rounded-3xl"
      style={{
        boxShadow: "10px 10px 0px #000000",
        transform: `translate(-50%, ${Math.sin(frame / 6) * 4}px)`,
      }}
    >
      <div className="relative w-[340px] h-[170px] overflow-hidden flex items-end justify-center">
        <svg width="320" height="160" viewBox="0 0 320 160">
          <path
            d="M 20 150 A 140 140 0 0 1 300 150"
            fill="none"
            stroke="#E2E8F0"
            strokeWidth="24"
            strokeLinecap="round"
          />
          <path
            d="M 20 150 A 140 140 0 0 1 300 150"
            fill="none"
            stroke="#F59E0B"
            strokeWidth="24"
            strokeDasharray="440"
            strokeDashoffset={interpolate(countProgress, [0, 1], [440, 60])}
            strokeLinecap="round"
          />
          <g transform={`translate(160, 150) rotate(${needleAngle})`}>
            <line x1="0" y1="0" x2="0" y2="-125" stroke="#EF4444" strokeWidth="8" strokeLinecap="round" />
            <circle cx="0" cy="0" r="16" fill="#000000" />
            <circle cx="0" cy="0" r="8" fill="#FFFFFF" />
          </g>
        </svg>
      </div>
      <div className="flex items-baseline gap-2 mt-2">
        <span
          className="text-6xl font-black text-black"
          style={{ fontFamily: "'Arial Black', 'Impact', system-ui" }}
        >
          {currentNumber}
        </span>
        <span className="text-xl font-bold text-slate-500 uppercase">{unit}</span>
      </div>
      {elemento.subtitulo && (
        <span className="text-sm font-bold text-slate-700 uppercase mt-1">
          {elemento.subtitulo}
        </span>
      )}
    </div>
  );
};

const SpeedLines: React.FC<{ elemento: ElementoNarrativo; frame: number }> = ({
  elemento,
  frame,
}) => {
  const count = 28;
  const color = elemento.color ?? "#000000";
  return (
    <svg className="absolute inset-0 w-full h-full pointer-events-none" viewBox="0 0 1920 1080">
      {Array.from({ length: count }).map((_, i) => {
        const offset = (i * 97 + frame * 35) % 1920;
        const y = (i * 73) % 1080;
        const length = 180 + ((i * 37) % 300);
        const strokeW = 2 + ((i * 11) % 5);
        return (
          <line
            key={i}
            x1={offset}
            y1={y}
            x2={offset + length}
            y2={y}
            stroke={color}
            strokeWidth={strokeW}
            strokeOpacity={0.65}
            strokeLinecap="round"
          />
        );
      })}
    </svg>
  );
};

const FlyingDebris: React.FC<{ frame: number; fps: number }> = ({ frame }) => {
  const count = 24;
  return (
    <div className="absolute inset-0 pointer-events-none">
      {Array.from({ length: count }).map((_, i) => {
        const speed = 15 + (i % 7) * 4;
        const x = (i * 160 + frame * speed) % 2100 - 100;
        const y = ((i * 131) % 900) + Math.sin((frame + i * 15) / 8) * 40;
        const rot = (frame * 12 + i * 45) % 360;
        const size = 20 + (i % 5) * 8;
        return (
          <div
            key={i}
            className="absolute bg-black rounded-sm border-2 border-slate-700"
            style={{
              width: size,
              height: size * 0.7,
              transform: `translate(${x}px, ${y}px) rotate(${rot}deg)`,
              boxShadow: "4px 4px 0px rgba(0,0,0,0.4)",
            }}
          />
        );
      })}
    </div>
  );
};

const GiantWaves: React.FC<{ frame: number }> = ({ frame }) => {
  const f = frame;
  return (
    <div className="absolute inset-0 pointer-events-none">
      <svg className="absolute bottom-0 w-full h-[450px]" viewBox="0 0 1920 450" preserveAspectRatio="none">
        <path
          d={`M 0 450 L 0 250 Q 480 ${200 + Math.sin(f / 8) * 35} 960 250 T 1920 250 L 1920 450 Z`}
          fill="#0284C7"
          fillOpacity={0.5}
        />
        <path
          d={`M 0 450 L 0 280 Q 480 ${300 + Math.cos(f / 9) * 40} 960 280 T 1920 280 L 1920 450 Z`}
          fill="#0369A1"
          fillOpacity={0.7}
        />
        <path
          d={`M 0 450 L 0 320 Q 480 ${330 + Math.sin(f / 6) * 25} 960 320 T 1920 320 L 1920 450 Z`}
          fill="#075985"
        />
      </svg>
    </div>
  );
};

const ShockwaveBurst: React.FC<{
  elemento?: ElementoNarrativo;
  frame: number;
  fps: number;
}> = ({ elemento, frame, fps }) => {
  const progress = spring({
    frame,
    fps,
    config: { damping: 10, stiffness: 120, mass: 0.6 },
  });
  const radius = interpolate(progress, [0, 1], [0, 650]);
  const opacity = interpolate(progress, [0, 0.6, 1], [1, 0.7, 0]);
  const cx = 960 + (elemento?.x ?? 0);
  const cy = 540 + (elemento?.y ?? 0);

  return (
    <div className="absolute inset-0 pointer-events-none">
      <div
        className="absolute rounded-full border-8 border-yellow-400"
        style={{
          left: cx,
          top: cy,
          width: radius * 2,
          height: radius * 2,
          opacity,
          transform: "translate(-50%, -50%)",
          boxShadow: "0 0 30px #FFE600",
        }}
      />
    </div>
  );
};

const OrbitalPeace: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none overflow-hidden">
      {Array.from({ length: 45 }).map((_, i) => {
        const x = (i * 137.5) % 1920;
        const y = (i * 93.7) % 1080;
        const blink = Math.sin((frame + i * 20) / 12) * 0.5 + 0.5;
        return (
          <div
            key={i}
            className="absolute rounded-full bg-white"
            style={{
              left: x,
              top: y,
              width: (i % 3) + 2,
              height: (i % 3) + 2,
              opacity: 0.3 + blink * 0.7,
            }}
          />
        );
      })}
    </div>
  );
};

const DangerVignette: React.FC<{ frame: number }> = ({ frame }) => {
  const pulse = Math.sin(frame / 6) * 0.2 + 0.8;
  return (
    <div
      className="absolute inset-0 pointer-events-none"
      style={{
        boxShadow: `inset 0 0 120px rgba(239, 68, 68, ${0.45 * pulse})`,
        border: "12px solid rgba(239, 68, 68, 0.6)",
      }}
    />
  );
};

const SparksExplosion: React.FC<{
  elemento?: ElementoNarrativo;
  frame: number;
}> = ({ elemento, frame }) => {
  // Ráfagas cíclicas de chispas y fogonazos para colisiones e impactos
  const cycle = frame % 30;
  if (cycle > 22) return null;

  const count = 18;
  const burstOpacity = interpolate(cycle, [0, 5, 22], [1, 0.9, 0], {
    extrapolateRight: "clamp",
  });
  const cx = 960 + (elemento?.x ?? 0);
  const cy = 540 + (elemento?.y ?? 40);

  return (
    <div className="absolute inset-0 pointer-events-none overflow-hidden flex items-center justify-center">
      <svg width="1920" height="1080" viewBox="0 0 1920 1080">
        <g transform={`translate(${cx}, ${cy})`}>
          {/* Flash central */}
          <circle cx="0" cy="0" r={cycle * 7} fill="#FFE600" opacity={burstOpacity * 0.5} />
          <circle cx="0" cy="0" r={cycle * 3.5} fill="#FFFFFF" opacity={burstOpacity} />

          {/* Chispas disparadas en abanico */}
          {Array.from({ length: count }).map((_, i) => {
            const angle = (i * (360 / count)) * (Math.PI / 180);
            const speed = 12 + ((i * 7) % 15);
            const dist = cycle * speed;
            const x = Math.cos(angle) * dist;
            const y = Math.sin(angle) * dist;
            const sparkLength = 10 + (i % 8);
            const color = i % 2 === 0 ? "#FFE600" : "#F97316";

            return (
              <line
                key={i}
                x1={x}
                y1={y}
                x2={x + Math.cos(angle) * sparkLength}
                y2={y + Math.sin(angle) * sparkLength}
                stroke={color}
                strokeWidth={4}
                strokeLinecap="round"
                opacity={burstOpacity}
              />
            );
          })}
        </g>
      </svg>
    </div>
  );
};

const SteamVent: React.FC<{ elemento?: ElementoNarrativo; frame: number }> = ({
  elemento,
  frame,
}) => {
  const puffs = 10;
  const baseX = 960 + (elemento?.x ?? 0);
  const baseY = 540 + (elemento?.y ?? 140);
  return (
    <div className="absolute inset-0 pointer-events-none overflow-hidden">
      {Array.from({ length: puffs }).map((_, i) => {
        const offsetFrame = (frame + i * 16) % 110;
        const progress = offsetFrame / 110;
        const y = baseY - progress * 340;
        const x = baseX + Math.sin(progress * 4 + i) * 35 + ((i % 5) - 2) * 28;
        const radius = 16 + progress * 44;
        const opacity = Math.sin(progress * Math.PI) * 0.32;

        return (
          <div
            key={i}
            className="absolute rounded-full bg-white blur-sm border border-slate-200"
            style={{
              left: x,
              top: y,
              width: radius * 2,
              height: radius * 2,
              opacity,
              transform: "translate(-50%, -50%)",
            }}
          />
        );
      })}
    </div>
  );
};

const ChemicalBubbles: React.FC<{
  elemento?: ElementoNarrativo;
  frame: number;
}> = ({ elemento, frame }) => {
  const bubbleCount = 14;
  const baseX = 960 + (elemento?.x ?? 0);
  const baseY = 540 + (elemento?.y ?? 180);
  return (
    <div className="absolute inset-0 pointer-events-none overflow-hidden">
      {Array.from({ length: bubbleCount }).map((_, i) => {
        const offset = (frame * 3 + i * 35) % 450;
        const progress = offset / 450;
        const y = baseY - progress * 320;
        const x = baseX - 90 + ((i * 29) % 180) + Math.sin(frame / 7 + i) * 14;
        const size = 10 + ((i * 5) % 16);
        const color = elemento?.color ?? (i % 2 === 0 ? "#10B981" : "#047857");
        const opacity = (1 - progress) * 0.75;

        return (
          <div
            key={i}
            className="absolute rounded-full border-2 border-black flex items-center justify-center"
            style={{
              left: x,
              top: y,
              width: size,
              height: size,
              backgroundColor: color,
              opacity,
              boxShadow: "0 0 10px rgba(16, 185, 129, 0.6)",
              transform: "translate(-50%, -50%)",
            }}
          >
            <div
              className="rounded-full bg-white"
              style={{
                width: size * 0.3,
                height: size * 0.3,
                transform: "translate(-25%, -25%)",
              }}
            />
          </div>
        );
      })}
    </div>
  );
};
