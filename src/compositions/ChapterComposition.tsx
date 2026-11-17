import React from "react";
import { AbsoluteFill, Series, useVideoConfig } from "remotion";
import { CapituloGuion } from "../types";
import { Scene } from "../components/Scene";

export interface ChapterCompositionProps extends Record<string, unknown> {
  capitulo: CapituloGuion;
}

export const ChapterComposition: React.FC<ChapterCompositionProps> = ({
  capitulo,
}) => {
  const { fps } = useVideoConfig();
  const totalEscenas = capitulo.escenas.length;

  return (
    <AbsoluteFill className="bg-[#0F172A]">
      <Series>
        {capitulo.escenas.map((escena, idx) => {
          const durationFrames = Math.max(
            1,
            Math.round((escena.duracionSegundos ?? 5) * fps)
          );

          return (
            <Series.Sequence key={escena.id} durationInFrames={durationFrames}>
              <Scene
                escena={escena}
                capituloNumero={capitulo.numero}
                capituloTitulo={capitulo.titulo}
                escenaIndice={idx + 1}
                totalEscenas={totalEscenas}
              />
            </Series.Sequence>
          );
        })}
      </Series>
    </AbsoluteFill>
  );
};
