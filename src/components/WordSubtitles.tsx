import React, { useMemo } from "react";
import {
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { PalabraTiming } from "../types";

export interface WordSubtitlesProps {
  palabras: PalabraTiming[];
  palabrasClave?: string[];
}

interface PalabraConIndice extends PalabraTiming {
  index: number;
}

function agruparEnBloques16x9(palabras: PalabraTiming[]): PalabraConIndice[][] {
  const conIndice: PalabraConIndice[] = palabras.map((p, index) => ({
    ...p,
    index,
  }));

  // En 16:9 disponemos de 1920px horizontales. Bloques de 4-5 palabras y ~36 caracteres
  const MAX_PALABRAS = 4;
  const MAX_CARACTERES = 36;
  const bloques: PalabraConIndice[][] = [];
  let actual: PalabraConIndice[] = [];
  let caracteres = 0;

  for (const p of conIndice) {
    if (
      actual.length > 0 &&
      (actual.length >= MAX_PALABRAS || caracteres + p.palabra.length > MAX_CARACTERES)
    ) {
      bloques.push(actual);
      actual = [];
      caracteres = 0;
    }
    actual.push(p);
    caracteres += p.palabra.length;
  }
  if (actual.length > 0) bloques.push(actual);

  return bloques;
}

export const WordSubtitles: React.FC<WordSubtitlesProps> = ({
  palabras,
  palabrasClave = [],
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const bloques = useMemo(() => agruparEnBloques16x9(palabras), [palabras]);

  if (!palabras || palabras.length === 0) {
    return null;
  }

  const currentTimeMs = (frame / fps) * 1000;

  // Determinar el bloque actual de forma monótona
  let currentBlockIndex = 0;
  for (let b = 0; b < bloques.length; b++) {
    const primerInicio = bloques[b][0]?.inicioMs ?? 0;
    if (currentTimeMs >= primerInicio) {
      currentBlockIndex = b;
    } else {
      break;
    }
  }

  const bloqueActual =
    bloques[currentBlockIndex] ?? bloques[bloques.length - 1] ?? bloques[0];

  // Determinar palabra activa dentro de su ventana temporal
  let activeWordIndex = -1;
  for (let i = 0; i < palabras.length; i++) {
    const p = palabras[i];
    if (currentTimeMs >= p.inicioMs && currentTimeMs <= p.finMs + 80) {
      activeWordIndex = i;
      break;
    }
  }

  const lastFinMs = palabras[palabras.length - 1]?.finMs ?? 0;
  if (lastFinMs > 0 && currentTimeMs > lastFinMs + 650) {
    return null;
  }

  return (
    <div className="w-full flex items-center justify-center px-12 pointer-events-none select-none">
      <div
        className="flex flex-wrap justify-center items-center text-center"
        style={{ columnGap: 34, rowGap: 10, maxWidth: 1660 }}
      >
        {bloqueActual.map((item) => {
          const isActive =
            item.index === activeWordIndex &&
            currentTimeMs >= item.inicioMs &&
            currentTimeMs <= item.finMs + 80;

          // Animación de pulso con spring al activarse la palabra
          const wordProgress = spring({
            frame: Math.max(0, frame - Math.round((item.inicioMs / 1000) * fps)),
            fps,
            config: {
              damping: 12,
              stiffness: 240,
              mass: 0.5,
            },
          });

          const scale = isActive
            ? interpolate(wordProgress, [0, 1], [1.0, 1.08], {
                extrapolateRight: "clamp",
              })
            : 1.0;

          const textoLimpio = item.palabra
            .toLowerCase()
            .replace(/[.,/#!$%^&*;:{}=\-_`~()¿?¡!]/g, "");

          const esClave = palabrasClave.some(
            (k) =>
              k.toLowerCase() === textoLimpio ||
              textoLimpio.includes(k.toLowerCase())
          );

          // Estilo de color: amarillo activo, azul cian clave, blanco por defecto
          const textColor = isActive
            ? "#FFE600"
            : esClave
            ? "#38BDF8"
            : "#FFFFFF";

          return (
            <span
              key={`${item.index}_${item.palabra}`}
              className="inline-block uppercase tracking-wide"
              style={{
                fontFamily:
                  "'Arial Black', 'Impact', 'Montserrat', system-ui, sans-serif",
                fontWeight: 900,
                fontSize: 54,
                lineHeight: 1.15,
                color: textColor,
                WebkitTextStroke: "7px #000000",
                paintOrder: "stroke fill",
                textShadow: "6px 6px 0px #000000",
                paddingInline: isActive ? 10 : 2,
                transform: `scale(${scale})`,
                transition: "color 0.05s ease-out",
              }}
            >
              {item.palabra}
            </span>
          );
        })}
      </div>
    </div>
  );
};
