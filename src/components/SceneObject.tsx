import React from "react";
import { interpolate } from "remotion";
import { ObjetoEscena, PalabraTiming, TipoAnimacionObjeto } from "../types";
import {
  getEasingFunction,
  resolveTimeRangeFrames,
} from "../stickman/actionSequences";
import { findPropById } from "../stickman/composites";

export interface SceneObjectProps {
  objeto: ObjetoEscena;
  frame: number;
  fps?: number;
  totalFrames?: number;
  palabras?: PalabraTiming[];
}

export const SceneObject: React.FC<SceneObjectProps> = ({
  objeto,
  frame,
  fps = 30,
  totalFrames = 900,
  palabras,
}) => {
  // 1. Ventana de visibilidad opcional del objeto
  const hasVisibilitySpec =
    objeto.inicioProgreso !== undefined ||
    objeto.finProgreso !== undefined ||
    objeto.inicioSegundos !== undefined ||
    objeto.finSegundos !== undefined ||
    objeto.desdePalabra !== undefined ||
    objeto.hastaPalabra !== undefined;

  if (hasVisibilitySpec) {
    const { startFrame, endFrame } = resolveTimeRangeFrames(
      objeto,
      totalFrames,
      fps,
      palabras
    );
    if (frame < startFrame || frame > endFrame) {
      return null;
    }
  }

  let currentX = objeto.posicion.x;
  let currentY = objeto.posicion.y;
  let currentScale = objeto.escala ?? 1;
  let currentRot = objeto.rotacion ?? 0;
  let currentOpacity = objeto.opacidad ?? 1;
  let currentState = objeto.estado;
  let currentPropId = objeto.propId;
  let currentAnimType: TipoAnimacionObjeto | undefined = objeto.animacion?.tipo;
  let stepProgress = 0;
  let stepStartFrame = objeto.animacion?.inicioFrame ?? 0;
  let stepEndFrame = objeto.animacion?.finFrame ?? totalFrames;

  // 2. Evaluación determinista de pasos secuenciales del objeto (interacción y cambio de estado)
  if (objeto.pasos && objeto.pasos.length > 0) {
    for (const paso of objeto.pasos) {
      const { startFrame: sF, endFrame: eF } = resolveTimeRangeFrames(
        paso,
        totalFrames,
        fps,
        palabras
      );

      if (frame >= sF && frame <= eF) {
        stepStartFrame = sF;
        stepEndFrame = eF;
        stepProgress =
          eF > sF ? Math.min(1, Math.max(0, (frame - sF) / (eF - sF))) : 1;
        const easing = getEasingFunction(paso.curva);
        const eased = easing(stepProgress);

        const prevX = paso.desdePosicion?.x ?? currentX;
        const prevY = paso.desdePosicion?.y ?? currentY;

        if (paso.posicion) {
          currentX = interpolate(eased, [0, 1], [prevX, paso.posicion.x]);
          currentY = interpolate(eased, [0, 1], [prevY, paso.posicion.y]);
        } else if (paso.desdePosicion) {
          currentX = prevX;
          currentY = prevY;
        }

        if (paso.escala !== undefined) {
          currentScale = interpolate(eased, [0, 1], [currentScale, paso.escala]);
        }
        if (paso.rotacion !== undefined) {
          currentRot = interpolate(eased, [0, 1], [currentRot, paso.rotacion]);
        }
        if (paso.opacidad !== undefined) {
          currentOpacity = interpolate(eased, [0, 1], [currentOpacity, paso.opacidad]);
        }
        if (paso.estado !== undefined) currentState = paso.estado;
        if (paso.propId !== undefined) currentPropId = paso.propId;
        if (paso.animacion !== undefined) currentAnimType = paso.animacion;
        break;
      } else if (frame > eF) {
        if (paso.posicion) {
          currentX = paso.posicion.x;
          currentY = paso.posicion.y;
        }
        if (paso.escala !== undefined) currentScale = paso.escala;
        if (paso.rotacion !== undefined) currentRot = paso.rotacion;
        if (paso.opacidad !== undefined) currentOpacity = paso.opacidad;
        if (paso.estado !== undefined) currentState = paso.estado;
        if (paso.propId !== undefined) currentPropId = paso.propId;
        if (paso.animacion !== undefined) currentAnimType = paso.animacion;
        stepProgress = 1;
      }
    }
  } else {
    stepProgress = Math.min(1, Math.max(0, frame / Math.max(1, totalFrames)));
  }

  const propDef = findPropById(currentPropId);
  if (!propDef || currentOpacity <= 0.01) {
    return null;
  }

  let animDeltaY = 0;
  let animDeltaX = 0;
  let animScale = 1;
  let animRot = currentRot;

  if (currentAnimType) {
    const startF = stepStartFrame;
    const endF = stepEndFrame;

    if (frame >= startF && frame <= endF) {
      const relFrame = frame - startF;

      if (currentAnimType === "flotar") {
        animDeltaY = Math.sin(relFrame / 14) * 8;
      } else if (currentAnimType === "vibrar") {
        animDeltaX = Math.sin(relFrame * 0.35) * 2.5;
      } else if (currentAnimType === "pulso") {
        animScale = 1 + Math.sin(relFrame / 10) * 0.06;
      } else if (currentAnimType === "caer") {
        const fallDist = objeto.animacion?.deltaY ?? 120;
        const t = Math.min(1, relFrame / Math.max(1, endF - startF));
        animDeltaY = t * fallDist;
        animRot += t * 15;
      } else if (currentAnimType === "rodar") {
        const rollDist = objeto.animacion?.deltaX ?? 260;
        const t = Math.min(1, relFrame / Math.max(1, endF - startF));
        animDeltaX = t * rollDist;
        animRot += t * 540;
      } else if (currentAnimType === "rebotar") {
        animDeltaY = -Math.abs(Math.sin(relFrame / 9)) * 16;
      }
    }
  }

  const finalX = currentX + animDeltaX;
  const finalY = currentY + animDeltaY;
  const finalScale = currentScale * animScale;

  // Centro en 16:9 es 960 (ancho / 2), 540 (alto / 2)
  // zIndex >= 26 garantiza que props y elementos flotantes queden SIEMPRE delante de las infografías (zIndex: 14)
  return (
    <div
      className="absolute pointer-events-none select-none flex items-center justify-center"
      style={{
        left: 960 + finalX,
        top: 540 + finalY,
        width: 310,
        height: 310,
        opacity: currentOpacity,
        transform: `translate(-50%, -50%) rotate(${animRot}deg) scale(${finalScale})`,
        zIndex: Math.max(26, objeto.capaZ ?? 28),
        filter: "drop-shadow(8px 8px 0px #000000)",
      }}
    >
      <svg
        viewBox="-55 -55 110 110"
        width="310"
        height="310"
        style={{ overflow: "visible" }}
        dangerouslySetInnerHTML={{
          __html:
            "animatedSvg" in propDef && propDef.animatedSvg
              ? propDef.animatedSvg(frame, stepProgress, currentState)
              : propDef.svg,
        }}
      />
    </div>
  );
};
