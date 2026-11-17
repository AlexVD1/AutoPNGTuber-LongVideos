import React, { useEffect, useMemo } from "react";
import {
  Img,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import {
  AnimacionEntradaStickman,
  OrientacionStickman,
  PalabraTiming,
  StickmanPropsAttachment,
} from "../types";
import { EfectoAmbienteFestivo } from "../stickman/festiveLibrary";
import {
  ArquetipoStickman,
  TipoAccesorioCabeza,
  TipoPeinado,
  TipoRopaTorso,
} from "../stickman/wardrobeLibrary";
import {
  buildDynamicStickmanSvgString,
  resolveStickmanConfig,
} from "../stickman/composites";
import { obtenerRecursoPorId } from "../stickman/catalog";

export interface StickmanProps {
  poseId?: string;
  prevPoseId?: string;
  poseTransitionProgress?: number;
  pose?: string;
  expresion?: string;
  prop?: string;
  props?: StickmanPropsAttachment;
  efectoAmbiente?: EfectoAmbienteFestivo;
  orientacion?: OrientacionStickman;
  escala?: number;
  posicion?: { x?: number; y?: number };
  animacionEntrada?: AnimacionEntradaStickman;
  palabras?: PalabraTiming[];
  headTiltOffset?: number;
  vibrationOffset?: number;
  overrideIsSpeaking?: boolean;
  halo?: boolean;
  proceduralMode?: string;
  esHolograma?: boolean;
  colorRim?: string;
  arquetipo?: ArquetipoStickman;
  ropaTorso?: TipoRopaTorso;
  colorTorso?: string;
  colorSecundarioTorso?: string;
  colorPantalones?: string;
  colorZapatos?: string;
  peinado?: TipoPeinado;
  colorPelo?: string;
  accesorioCabeza?: TipoAccesorioCabeza;
  colorAccesorio?: string;
}

const ALERT_KEYWORDS = [
  "sorprendido",
  "shock",
  "shocked",
  "scared",
  "fear",
  "trembling",
  "hiding",
  "danger",
  "warning",
  "backing_away",
  "tripping",
  "explosion",
  "worried",
  "surprised",
  "alert",
];

export const Stickman: React.FC<StickmanProps> = ({
  pose,
  poseId,
  prevPoseId,
  poseTransitionProgress,
  expresion,
  prop,
  props,
  efectoAmbiente,
  orientacion = "derecha",
  escala = 1,
  posicion,
  animacionEntrada = "rebote",
  palabras,
  headTiltOffset = 0,
  vibrationOffset = 0,
  overrideIsSpeaking,
  halo = false,
  proceduralMode,
  esHolograma = false,
  colorRim,
  arquetipo,
  ropaTorso,
  colorTorso,
  colorSecundarioTorso,
  colorPantalones,
  colorZapatos,
  peinado,
  colorPelo,
  accesorioCabeza,
  colorAccesorio,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const targetPoseKey = poseId || pose || "standing_relaxed";

  // Detección determinista de habla sincrónica
  const currentTimeMs = (frame / fps) * 1000;
  const isSpeaking = useMemo(() => {
    if (overrideIsSpeaking !== undefined) {
      return overrideIsSpeaking;
    }
    if (!palabras || palabras.length === 0) {
      return frame > 4;
    }
    return palabras.some(
      (p) => currentTimeMs >= p.inicioMs && currentTimeMs <= p.finMs + 60
    );
  }, [overrideIsSpeaking, palabras, currentTimeMs, frame]);

  const resolved = useMemo(
    () =>
      resolveStickmanConfig({
        poseId: targetPoseKey,
        expressionId: expresion,
        rightProp: props?.derecha ?? prop,
        leftProp: props?.izquierda,
        overheadProp: props?.arriba,
        hatProp: props?.sombrero,
        faceProp: props?.cara,
        neckProp: props?.cuello,
        waistProp: props?.cintura,
        efectoAmbiente,
      }),
    [
      targetPoseKey,
      expresion,
      prop,
      props?.derecha,
      props?.izquierda,
      props?.arriba,
      props?.sombrero,
      props?.cara,
      props?.cuello,
      props?.cintura,
      efectoAmbiente,
    ]
  );

  useEffect(() => {
    if (resolved.usedFallback && resolved.warningMessage) {
      console.warn(resolved.warningMessage);
    }
  }, [resolved.usedFallback, resolved.warningMessage]);

  const catalogItem = useMemo(
    () => obtenerRecursoPorId(targetPoseKey),
    [targetPoseKey]
  );

  // Animación física de entrada
  const entranceProgress = spring({
    frame,
    fps,
    config: {
      damping: 12,
      stiffness: 160,
      mass: 0.8,
    },
  });

  let animTranslateX = 0;
  let animTranslateY = 0;
  let animScaleX = 1;
  let animScaleY = 1;

  if (animacionEntrada === "rebote") {
    animTranslateY = interpolate(entranceProgress, [0, 1], [40, 0]);
    animScaleY = interpolate(entranceProgress, [0, 0.6, 1], [0.88, 1.05, 1]);
    animScaleX = interpolate(entranceProgress, [0, 0.6, 1], [1.1, 0.97, 1]);
  } else if (animacionEntrada === "zoom") {
    animScaleX = interpolate(entranceProgress, [0, 1], [0.2, 1]);
    animScaleY = interpolate(entranceProgress, [0, 1], [0.2, 1]);
  } else if (animacionEntrada === "deslizar") {
    animTranslateX = interpolate(entranceProgress, [0, 1], [-180, 0]);
  }

  // Micro-movimiento continuo de respiración y vida
  const breathCycle = Math.sin(frame / 9);
  const breathTranslateY = -breathCycle * 3.0;
  const breathScaleY = 1 + breathCycle * 0.02;

  // Temblor de sorpresa/impacto en frames iniciales
  const isAlertPose = ALERT_KEYWORDS.some(
    (k) =>
      targetPoseKey.toLowerCase().includes(k) ||
      (expresion && expresion.toLowerCase().includes(k))
  );

  let vibrationX = 0;
  if (isAlertPose && frame < 20) {
    const vibrationDecay = interpolate(frame, [0, 20], [1, 0], {
      extrapolateRight: "clamp",
    });
    vibrationX = Math.sin(frame * 0.45) * 4.5 * vibrationDecay;
  }

  const flipMultiplier = orientacion === "izquierda" ? -1 : 1;
  const finalTranslateX =
    (posicion?.x ?? 0) + animTranslateX + vibrationX + vibrationOffset;
  const finalTranslateY =
    (posicion?.y ?? 0) + animTranslateY + breathTranslateY;
  const finalScaleX = animScaleX * escala * flipMultiplier;
  const finalScaleY = animScaleY * escala * breathScaleY;

  const svgMarkup = useMemo(
    () =>
      buildDynamicStickmanSvgString({
        poseId: targetPoseKey,
        prevPoseId,
        poseTransitionProgress,
        expressionId: expresion,
        rightProp: props?.derecha ?? prop,
        leftProp: props?.izquierda,
        overheadProp: props?.arriba,
        hatProp: props?.sombrero,
        faceProp: props?.cara,
        neckProp: props?.cuello,
        waistProp: props?.cintura,
        efectoAmbiente,
        frame,
        fps,
        isSpeaking,
        headTiltOffset,
        proceduralMode,
        esHolograma,
        colorRim,
        arquetipo,
        ropaTorso,
        colorTorso,
        colorSecundarioTorso,
        colorPantalones,
        colorZapatos,
        peinado,
        colorPelo,
        accesorioCabeza,
        colorAccesorio,
      }),
    [
      targetPoseKey,
      prevPoseId,
      poseTransitionProgress,
      expresion,
      prop,
      props?.derecha,
      props?.izquierda,
      props?.arriba,
      props?.sombrero,
      props?.cara,
      props?.cuello,
      props?.cintura,
      efectoAmbiente,
      frame,
      fps,
      isSpeaking,
      headTiltOffset,
      proceduralMode,
      esHolograma,
      colorRim,
      arquetipo,
      ropaTorso,
      colorTorso,
      colorSecundarioTorso,
      colorPantalones,
      colorZapatos,
      peinado,
      colorPelo,
      accesorioCabeza,
      colorAccesorio,
    ]
  );

  const usePngFile = catalogItem?.formato === "png";
  const stickmanFilter = esHolograma
    ? "drop-shadow(0px 0px 12px #22D3EE) drop-shadow(0px 0px 4px #06B6D4)"
    : halo
    ? "drop-shadow(0px 0px 6px #FFFFFF) drop-shadow(0px 0px 3px #FFFFFF)"
    : undefined;

  return (
    <div
      className="flex items-center justify-center select-none"
      style={{
        width: 500 * escala,
        height: 620 * escala,
        transform: `translate(${finalTranslateX}px, ${finalTranslateY}px)`,
      }}
    >
      <div
        style={{
          width: 500,
          height: 620,
          transform: `scale(${finalScaleX}, ${finalScaleY})`,
          transformOrigin: "center bottom",
          flexShrink: 0,
          filter: stickmanFilter,
        }}
      >
        {usePngFile && catalogItem ? (
          <Img
            src={staticFile(catalogItem.ruta)}
            style={{
              height: 620,
              width: 500,
              objectFit: "contain",
            }}
          />
        ) : (
          <div
            style={{ width: 500, height: 620 }}
            dangerouslySetInnerHTML={{ __html: svgMarkup }}
          />
        )}
      </div>
    </div>
  );
};
