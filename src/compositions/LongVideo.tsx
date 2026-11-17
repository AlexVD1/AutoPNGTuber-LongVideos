import React, { useMemo } from "react";
import {
  AbsoluteFill,
  Audio,
  getStaticFiles,
  Series,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { GuionLargoCompleto } from "../types";
import { Scene } from "../components/Scene";

export interface LongVideoProps extends Record<string, unknown> {
  guion: GuionLargoCompleto;
}

function fileExistsInStatic(targetRelativePath: string): boolean {
  try {
    const files = getStaticFiles();
    if (!files || files.length === 0) return true;
    const normTarget = targetRelativePath.replace(/\\/g, "/").toLowerCase();
    return files.some((f) => {
      const name = (f.name || "").replace(/\\/g, "/").toLowerCase();
      const src = (f.src || "").replace(/\\/g, "/").toLowerCase();
      return name.endsWith(normTarget) || src.includes(normTarget);
    });
  } catch {
    return false;
  }
}

export const LongVideo: React.FC<LongVideoProps> = ({ guion }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const bgmTrack = guion.meta.musicaPrincipal || "bgm/bgm.mp3";
  const bgmVolume = guion.meta.volumenMusica ?? 0.08;
  const hasBgm = useMemo(() => fileExistsInStatic(bgmTrack), [bgmTrack]);

  // Barra de progreso superior neo-brutalista sutil
  const progressRatio = Math.min(
    1,
    Math.max(0, (frame + 1) / Math.max(1, durationInFrames))
  );

  return (
    <AbsoluteFill className="bg-[#0F172A]">
      {/* Música de fondo ambiental en loop (en modo vista previa) */}
      {hasBgm && <Audio src={staticFile(bgmTrack)} volume={bgmVolume} loop />}

      {/* Barra de progreso global del video (8px) */}
      <div
        className="absolute top-0 left-0 right-0 z-50 overflow-hidden"
        style={{ height: 8, backgroundColor: "rgba(0,0,0,0.4)" }}
      >
        <div
          style={{
            width: `${progressRatio * 100}%`,
            height: 8,
            backgroundColor: "#FFE600",
            borderBottom: "2px solid #000000",
            borderRight: "2px solid #000000",
          }}
        />
      </div>

      {/* Secuencia cronológica de capítulos y escenas */}
      <Series>
        {guion.capitulos.map((cap) => {
          const totalEscenasCap = cap.escenas.length;
          return cap.escenas.map((escena, idx) => {
            const durFrames = Math.max(
              1,
              Math.round((escena.duracionSegundos ?? 5) * fps)
            );
            return (
              <Series.Sequence
                key={`${cap.id}_${escena.id}`}
                durationInFrames={durFrames}
              >
                <Scene
                  escena={escena}
                  capituloNumero={cap.numero}
                  capituloTitulo={cap.titulo}
                  escenaIndice={idx + 1}
                  totalEscenas={totalEscenasCap}
                />
              </Series.Sequence>
            );
          });
        })}
      </Series>
    </AbsoluteFill>
  );
};
