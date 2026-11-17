import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";

export interface BadgeCalendarioProps {
  texto: string;
  subtexto?: string;
  colorCabecera?: string;
  x?: number;
  y?: number;
}

export const BadgeCalendario: React.FC<BadgeCalendarioProps> = () => {
  // Desactivado para eliminar bloques de calendario encimados en documentales científicos
  return null;
};

export interface PildoraMetricaProps {
  etiqueta?: string; // ej: "POBLACIÓN" o "COEFICIENTE"
  valor: string; // ej: "8,599,999,999" o "0.025"
  colorBorde?: string;
  posicion?: "superior_izquierda" | "inferior_centro" | "superior_derecha" | "personalizada";
  x?: number;
  y?: number;
}

export const PildoraMetrica: React.FC<PildoraMetricaProps> = ({
  etiqueta,
  valor,
  colorBorde = "#FACC15", // Dorado elegante
  posicion = "inferior_centro",
  x,
  y,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const entrance = spring({
    frame,
    fps,
    config: { damping: 13, stiffness: 150 },
  });

  const scale = interpolate(entrance, [0, 1], [0.85, 1]);
  const opacity = interpolate(entrance, [0, 1], [0, 1]);

  let stylePos: React.CSSProperties = {};
  if (posicion === "inferior_centro") {
    stylePos = {
      bottom: y ?? 130,
      left: "50%",
      transform: `translateX(-50%) scale(${scale})`,
    };
  } else if (posicion === "superior_izquierda") {
    stylePos = {
      top: y ?? 52,
      left: x ?? 70,
      transform: `scale(${scale})`,
    };
  } else if (posicion === "superior_derecha") {
    stylePos = {
      top: y ?? 52,
      right: 70,
      transform: `scale(${scale})`,
    };
  } else {
    stylePos = {
      left: x ?? 100,
      top: y ?? 100,
      transform: `scale(${scale})`,
    };
  }

  return (
    <div
      className="absolute z-40 select-none pointer-events-none"
      style={{
        ...stylePos,
        opacity,
      }}
    >
      <div
        className="px-8 py-3.5 rounded-3xl bg-[#09101D]/90 backdrop-blur-md shadow-2xl flex flex-col items-center justify-center"
        style={{
          border: `2.5px solid ${colorBorde}`,
          boxShadow: `0 10px 30px -5px rgba(0,0,0,0.6), 0 0 16px ${colorBorde}33`,
        }}
      >
        {etiqueta && (
          <span
            className="text-xs font-extrabold tracking-widest uppercase mb-0.5"
            style={{ color: colorBorde }}
          >
            {etiqueta}
          </span>
        )}
        <span className="text-3xl font-black text-white tracking-wide font-sans">
          {valor}
        </span>
      </div>
    </div>
  );
};
