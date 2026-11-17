import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";

export interface SplitScreenProps {
  ladoIzquierdo: {
    titulo: string;
    colorFondo?: string;
    contenido?: React.ReactNode;
  };
  ladoDerecho: {
    titulo: string;
    colorFondo?: string;
    contenido?: React.ReactNode;
  };
}

export const SplitScreen: React.FC<SplitScreenProps> = ({
  ladoIzquierdo,
  ladoDerecho,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const splitProgress = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 140 },
  });

  const dividerHeight = interpolate(splitProgress, [0, 1], [0, 1080]);

  return (
    <div className="absolute inset-0 pointer-events-none z-10 flex">
      {/* Panel Izquierdo */}
      <div
        className="w-1/2 h-full relative p-8 flex flex-col justify-start items-center"
        style={{
          backgroundColor: ladoIzquierdo.colorFondo || "rgba(241, 245, 249, 0.4)",
        }}
      >
        <div className="bg-black text-white px-6 py-2 rounded-xl border-3 border-black shadow-[6px_6px_0px_#FFE600] mt-16">
          <span
            className="text-2xl font-black uppercase tracking-wide"
            style={{ fontFamily: "'Arial Black', 'Impact', system-ui" }}
          >
            {ladoIzquierdo.titulo}
          </span>
        </div>
        {ladoIzquierdo.contenido && (
          <div className="mt-8">{ladoIzquierdo.contenido}</div>
        )}
      </div>

      {/* Divisor Central Neo-Brutal */}
      <div
        className="w-2 bg-black z-30 self-center"
        style={{
          height: dividerHeight,
          boxShadow: "0 0 12px rgba(0,0,0,0.5)",
        }}
      />

      {/* Panel Derecho */}
      <div
        className="w-1/2 h-full relative p-8 flex flex-col justify-start items-center"
        style={{
          backgroundColor: ladoDerecho.colorFondo || "rgba(254, 243, 199, 0.4)",
        }}
      >
        <div className="bg-white text-black px-6 py-2 rounded-xl border-3 border-black shadow-[6px_6px_0px_#000000] mt-16">
          <span
            className="text-2xl font-black uppercase tracking-wide"
            style={{ fontFamily: "'Arial Black', 'Impact', system-ui" }}
          >
            {ladoDerecho.titulo}
          </span>
        </div>
        {ladoDerecho.contenido && (
          <div className="mt-8">{ladoDerecho.contenido}</div>
        )}
      </div>
    </div>
  );
};
