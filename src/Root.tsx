import React from "react";
import { Composition, CalculateMetadataFunction } from "remotion";
import { LongVideo, LongVideoProps } from "./compositions/LongVideo";
import { ChapterComposition, ChapterCompositionProps } from "./compositions/ChapterComposition";
import { CapituloGuion, GuionLargoCompleto } from "./types";
import rawGuionData from "./data/guion.json";
import "./style.css";

const FPS = 30;
const WIDTH = 1920;
const HEIGHT = 1080;

const guionData = rawGuionData as unknown as GuionLargoCompleto;
const capitulos: CapituloGuion[] = guionData?.capitulos || [];

// Cálculo dinámico de duración para el video completo
const calculateLongVideoMetadata: CalculateMetadataFunction<LongVideoProps> = async ({
  props,
}) => {
  const totalFrames = (props.guion.capitulos || []).reduce((accCap, cap) => {
    const framesCap = (cap.escenas || []).reduce((accEsc, esc) => {
      const seg = esc.duracionSegundos ?? 5;
      return accEsc + Math.max(1, Math.round(seg * FPS));
    }, 0);
    return accCap + framesCap;
  }, 0);

  return {
    durationInFrames: Math.max(1, totalFrames),
    fps: FPS,
    width: WIDTH,
    height: HEIGHT,
  };
};

// Cálculo dinámico de duración para cada capítulo independiente
const calculateChapterMetadata: CalculateMetadataFunction<ChapterCompositionProps> = async ({
  props,
}) => {
  const totalFrames = (props.capitulo.escenas || []).reduce((acc, esc) => {
    const seg = esc.duracionSegundos ?? 5;
    return acc + Math.max(1, Math.round(seg * FPS));
  }, 0);

  return {
    durationInFrames: Math.max(1, totalFrames),
    fps: FPS,
    width: WIDTH,
    height: HEIGHT,
  };
};

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* 1. Composición de Video Completo (para Remotion Studio / Previsualización) */}
      <Composition
        id="VideoCompleto"
        component={LongVideo}
        durationInFrames={FPS * 60}
        fps={FPS}
        width={WIDTH}
        height={HEIGHT}
        defaultProps={{
          guion: guionData,
        }}
        calculateMetadata={calculateLongVideoMetadata}
      />

      {/* 2. Composiciones individuales por capítulo (para renderizado segmentado) */}
      {capitulos.map((cap) => (
        <Composition
          key={`Capitulo-${cap.numero}`}
          id={`Capitulo-${cap.numero}`}
          component={ChapterComposition}
          durationInFrames={FPS * 30}
          fps={FPS}
          width={WIDTH}
          height={HEIGHT}
          defaultProps={{
            capitulo: cap,
          }}
          calculateMetadata={calculateChapterMetadata}
        />
      ))}
    </>
  );
};
