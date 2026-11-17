import { interpolate, spring, Easing } from "remotion";
import {
  AccionPersonaje,
  OrientacionStickman,
  PalabraTiming,
  PasoAccion,
  PersonajeEscena,
  StickmanPropsAttachment,
  TipoCurvaMovimiento,
  TipoMovimientoProcedural,
} from "../types";

export interface EvaluatedCharacterState {
  poseId: string;
  prevPoseId?: string;
  poseTransitionProgress?: number;
  expresion: string;
  x: number;
  y: number;
  escala: number;
  orientacion: OrientacionStickman;
  prop?: string;
  props?: StickmanPropsAttachment;
  headTilt: number;
  /** Impulso de impacto o contacto si ocurre en este frame */
  isContactImpact: boolean;
  /** Intensidad de vibración procedural */
  vibrationX: number;
  /** Si está en ciclo de caminata activo */
  isWalking: boolean;
  /** Modo procedural activo para articulación de brazos/piernas */
  proceduralMode?: TipoMovimientoProcedural;
  /** Modo holograma/fantasma predictivo */
  esHolograma?: boolean;
  /** Color de contraluz 2.5D (rim-light) */
  colorRim?: string;
  /** Opacidad dinámica 0..1 */
  opacidad?: number;
  /** Si el personaje está dentro de su ventana temporal activa */
  visible?: boolean;
}

/**
 * Mapeo de curvas de aceleración para movimientos orgánicos
 */
export function getEasingFunction(curva?: TipoCurvaMovimiento): (t: number) => number {
  switch (curva) {
    case "suave":
      return Easing.bezier(0.25, 0.1, 0.25, 1);
    case "anticipacion":
      return Easing.bezier(0.4, -0.2, 0.2, 1);
    case "rebote":
      return Easing.bounce;
    case "impacto":
      return Easing.bezier(0.05, 0.9, 0.2, 1);
    case "lineal":
    default:
      return Easing.linear;
  }
}

function normalizeToken(s: string): string {
  return s
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9]/g, "");
}

/**
 * Busca el tiempo en milisegundos de una palabra o frase corta dentro de la alineación Whisper.
 */
export function resolveWordMs(
  query: string | undefined,
  palabras?: PalabraTiming[],
  pickEnd = false
): number | undefined {
  if (!query || !palabras || palabras.length === 0) return undefined;
  const parts = query
    .trim()
    .split(/\s+/)
    .map(normalizeToken)
    .filter(Boolean);
  if (parts.length === 0) return undefined;

  for (let i = 0; i <= palabras.length - parts.length; i++) {
    let match = true;
    for (let j = 0; j < parts.length; j++) {
      const wNorm = normalizeToken(palabras[i + j].palabra);
      if (wNorm !== parts[j] && !wNorm.includes(parts[j])) {
        match = false;
        break;
      }
    }
    if (match) {
      return pickEnd
        ? palabras[i + parts.length - 1].finMs
        : palabras[i].inicioMs;
    }
  }
  return undefined;
}

export interface TimeRangeSpec {
  inicioFrame?: number;
  finFrame?: number;
  inicioProgreso?: number;
  finProgreso?: number;
  inicioSegundos?: number;
  finSegundos?: number;
  desdePalabra?: string;
  hastaPalabra?: string;
}

/**
 * Resuelve un rango temporal (frames, segundos, progreso 0..1 o palabras narradas) a [startFrame, endFrame].
 */
export function resolveTimeRangeFrames(
  item: TimeRangeSpec,
  totalFrames: number,
  fps: number,
  palabras?: PalabraTiming[]
): { startFrame: number; endFrame: number } {
  let startF = item.inicioFrame;
  let endF = item.finFrame;

  if (startF === undefined && item.desdePalabra) {
    const ms = resolveWordMs(item.desdePalabra, palabras, false);
    if (ms !== undefined) startF = Math.round((ms / 1000) * fps);
  }
  if (endF === undefined && item.hastaPalabra) {
    const ms = resolveWordMs(item.hastaPalabra, palabras, true);
    if (ms !== undefined) endF = Math.round((ms / 1000) * fps);
  }

  if (startF === undefined && item.inicioSegundos !== undefined) {
    startF = Math.round(item.inicioSegundos * fps);
  }
  if (endF === undefined && item.finSegundos !== undefined) {
    endF = Math.round(item.finSegundos * fps);
  }

  if (startF === undefined && item.inicioProgreso !== undefined) {
    startF = Math.round(item.inicioProgreso * totalFrames);
  }
  if (endF === undefined && item.finProgreso !== undefined) {
    endF = Math.round(item.finProgreso * totalFrames);
  }

  const clampedStart = Math.max(0, Math.min(totalFrames, startF ?? 0));
  const clampedEnd = Math.max(clampedStart, Math.min(totalFrames, endF ?? totalFrames));
  return { startFrame: clampedStart, endFrame: clampedEnd };
}

/**
 * Resuelve un instante puntual (para SFX o eventos discretos) en frames.
 */
export function resolvePointFrame(
  item: { tiempoSegundos?: number; enSegundo?: number; progreso?: number; desdePalabra?: string },
  totalFrames: number,
  fps: number,
  palabras?: PalabraTiming[]
): number {
  if (item.desdePalabra) {
    const ms = resolveWordMs(item.desdePalabra, palabras, false);
    if (ms !== undefined) {
      return Math.max(0, Math.min(totalFrames - 1, Math.round((ms / 1000) * fps)));
    }
  }
  const sec = item.tiempoSegundos ?? item.enSegundo;
  if (sec !== undefined) {
    return Math.max(0, Math.min(totalFrames - 1, Math.round(sec * fps)));
  }
  if (item.progreso !== undefined) {
    return Math.max(0, Math.min(totalFrames - 1, Math.round(item.progreso * totalFrames)));
  }
  return 0;
}

/**
 * Convierte acciones predefinidas de alto nivel en una secuencia de pasos deterministas.
 */
export function expandActionToSteps(
  accion: AccionPersonaje,
  totalFrames: number,
  initialPos: { x: number; y: number },
  fps = 30,
  palabras?: PalabraTiming[]
): PasoAccion[] {
  if (accion.pasos && accion.pasos.length > 0) {
    return accion.pasos.map((p) => {
      const { startFrame, endFrame } = resolveTimeRangeFrames(p, totalFrames, fps, palabras);
      return {
        ...p,
        inicioFrame: startFrame,
        finFrame: endFrame,
      };
    });
  }

  const startFrame = accion.inicioFrame ?? 0;
  const dur = accion.duracionFrames ?? totalFrames - startFrame;
  const endFrame = startFrame + dur;
  const fromX = accion.desdeX ?? initialPos.x;
  const toX = accion.haciaX ?? fromX;
  const fromY = accion.desdeY ?? initialPos.y;
  const toY = accion.haciaY ?? fromY;

  switch (accion.tipo) {
    case "caminar_hacia": {
      const walkDuration = Math.round(dur * 0.82);
      const settleDuration = dur - walkDuration;
      return [
        {
          inicioFrame: startFrame,
          finFrame: startFrame + walkDuration,
          poseId: "walking",
          expresion: "talking",
          posicion: { x: toX, y: toY },
          curva: "suave",
          procedural: "caminar",
        },
        {
          inicioFrame: startFrame + walkDuration,
          finFrame: endFrame,
          poseId: "standing_relaxed",
          expresion: "talking",
          posicion: { x: toX, y: toY },
          curva: "suave",
          procedural: "estatico",
        },
      ];
    }

    case "sonambulo_avanzar": {
      return [
        {
          inicioFrame: startFrame,
          finFrame: endFrame,
          poseId: "walking",
          expresion: "bored",
          posicion: { x: toX, y: toY },
          curva: "lineal",
          procedural: "caminar",
        },
      ];
    }

    case "acercarse_y_tocar": {
      const walkDur = Math.round(dur * 0.55);
      const reachDur = Math.round(dur * 0.25);
      const holdDur = dur - walkDur - reachDur;

      const midX = fromX + (toX - fromX) * 0.88;

      return [
        // Fase 1: Caminata hacia el objetivo
        {
          inicioFrame: startFrame,
          finFrame: startFrame + walkDur,
          poseId: "walking",
          expresion: "talking_enthusiastic",
          posicion: { x: midX, y: fromY },
          curva: "suave",
          procedural: "caminar",
        },
        // Fase 2: Extensión de brazo y toque directo
        {
          inicioFrame: startFrame + walkDur,
          finFrame: startFrame + walkDur + reachDur,
          poseId: "pointing_right",
          expresion: "smile_soft",
          posicion: { x: toX, y: toY },
          curva: "impacto",
          procedural: "recoil",
        },
        // Fase 3: Detenerse y sostener la interacción
        {
          inicioFrame: startFrame + walkDur + reachDur,
          finFrame: endFrame,
          poseId: "pointing_right",
          expresion: "talking",
          posicion: { x: toX, y: toY },
          curva: "suave",
          procedural: "estatico",
        },
      ];
    }

    case "despertar_asustado":
    case "sorpresa_y_retroceso": {
      const reactionFrame = Math.round(dur * 0.35);
      const shockDur = Math.round(dur * 0.3);
      const settleDur = dur - reactionFrame - shockDur;

      const recoilX = toX + (toX > fromX ? 80 : -80);

      return [
        // Fase 1: Estado inicial (dormido o tranquilo antes del estímulo)
        {
          inicioFrame: startFrame,
          finFrame: startFrame + reactionFrame,
          poseId: "walking",
          expresion: "bored",
          posicion: { x: fromX, y: fromY },
          curva: "lineal",
          procedural: "caminar",
        },
        // Fase 2: IMPACTO Y SOBRESALTO INMEDIATO (Retroceso brusco + temblor)
        {
          inicioFrame: startFrame + reactionFrame,
          finFrame: startFrame + reactionFrame + shockDur,
          poseId: "shock_explosion",
          expresion: "shocked",
          posicion: { x: recoilX, y: fromY - 18 },
          curva: "impacto",
          procedural: "temblar",
        },
        // Fase 3: Desorientado y confundido recuperando balance
        {
          inicioFrame: startFrame + reactionFrame + shockDur,
          finFrame: endFrame,
          poseId: "backing_away_scared",
          expresion: "confused",
          posicion: { x: recoilX, y: fromY },
          curva: "suave",
          procedural: "estatico",
        },
      ];
    }

    case "guiar_amigo": {
      return [
        {
          inicioFrame: startFrame,
          finFrame: endFrame,
          poseId: "explaining_both_hands",
          expresion: "smile_soft",
          posicion: { x: toX, y: toY },
          curva: "suave",
          procedural: "caminar",
        },
      ];
    }

    case "mirar_y_reaccionar": {
      const turnFrame = Math.round(dur * 0.4);
      return [
        {
          inicioFrame: startFrame,
          finFrame: startFrame + turnFrame,
          poseId: "standing_relaxed",
          expresion: "thinking",
          posicion: { x: fromX, y: fromY },
          curva: "suave",
          procedural: "estatico",
        },
        {
          inicioFrame: startFrame + turnFrame,
          finFrame: endFrame,
          poseId: "scratching_head",
          expresion: "confused",
          posicion: { x: toX, y: toY },
          curva: "suave",
          procedural: "estatico",
        },
      ];
    }

    case "tropezar_y_reaccionar": {
      const tripFrame = Math.round(dur * 0.4);
      return [
        {
          inicioFrame: startFrame,
          finFrame: startFrame + tripFrame,
          poseId: "walking",
          expresion: "neutral",
          posicion: { x: fromX, y: fromY },
          curva: "lineal",
          procedural: "caminar",
        },
        {
          inicioFrame: startFrame + tripFrame,
          finFrame: endFrame,
          poseId: "tripping_falling",
          expresion: "scared",
          posicion: { x: toX, y: toY + 20 },
          curva: "impacto",
          procedural: "temblar",
        },
      ];
    }

    default:
      return [
        {
          inicioFrame: startFrame,
          finFrame: endFrame,
          poseId: "standing_relaxed",
          expresion: "talking",
          posicion: { x: toX, y: toY },
          curva: "lineal",
          procedural: "estatico",
        },
      ];
  }
}

/**
 * Evalúa deterministamente el estado cinemático de un personaje en un frame exacto.
 */
export function evaluateCharacterState(
  personaje: PersonajeEscena,
  frame: number,
  fps: number,
  totalFrames: number,
  palabras?: PalabraTiming[]
): EvaluatedCharacterState {
  const basePos = personaje.posicion ?? { x: 0, y: 0 };
  const baseScale = personaje.escala ?? 1;
  const baseOrientation = personaje.orientacion ?? "derecha";
  const basePose = personaje.poseId ?? "standing_relaxed";
  const baseExpr = personaje.expresion ?? "talking";
  const baseHolograma = personaje.esHolograma ?? false;
  const baseOpacity = personaje.opacidad ?? (personaje.espectral ? 0.45 : baseHolograma ? 0.65 : 1);

  const hasWindow =
    personaje.inicioProgreso !== undefined ||
    personaje.finProgreso !== undefined ||
    personaje.inicioSegundos !== undefined ||
    personaje.finSegundos !== undefined ||
    personaje.desdePalabra !== undefined ||
    personaje.hastaPalabra !== undefined;

  let visible = true;
  if (hasWindow) {
    const { startFrame: wStart, endFrame: wEnd } = resolveTimeRangeFrames(
      personaje,
      totalFrames,
      fps,
      palabras
    );
    visible = frame >= wStart && frame <= wEnd;
  }

  // Si no tiene acciones definidas, generar micro-dinamismo procedural comunicativo
  if (!personaje.acciones || personaje.acciones.length === 0) {
    const isSpeaking = personaje.habla !== false;
    const communicativeTilt = isSpeaking ? Math.sin(frame / 6) * 3.5 : 0;
    const weightShiftX = Math.sin(frame / 18) * 4;

    return {
      poseId: basePose,
      prevPoseId: basePose,
      poseTransitionProgress: 1,
      expresion: baseExpr,
      x: (basePos.x ?? 0) + weightShiftX,
      y: basePos.y ?? 0,
      escala: baseScale,
      orientacion: baseOrientation,
      prop: personaje.prop,
      props: personaje.props,
      headTilt: communicativeTilt,
      isContactImpact: false,
      vibrationX: 0,
      isWalking: false,
      proceduralMode: "estatico",
      esHolograma: baseHolograma,
      colorRim: personaje.colorRim,
      opacidad: baseOpacity,
      visible,
    };
  }

  // Aplanar todos los pasos de todas las acciones del personaje
  let currentPos = { x: basePos.x ?? 0, y: basePos.y ?? 0 };
  let currentPose = basePose;
  let prevPoseId = basePose;
  let poseTransitionProgress = 1;
  let currentExpr = baseExpr;
  let currentScale = baseScale;
  let currentOrientation = baseOrientation;
  let currentProp = personaje.prop;
  let currentProps = personaje.props;
  let currentHolograma = baseHolograma;
  let currentOpacity = baseOpacity;
  let headTilt = 0;
  let isContactImpact = false;
  let vibrationX = 0;
  let isWalking = false;
  let proceduralMode: TipoMovimientoProcedural = "estatico";

  for (const accion of personaje.acciones) {
    const steps = expandActionToSteps(accion, totalFrames, currentPos, fps, palabras);

    for (let i = 0; i < steps.length; i++) {
      const step = steps[i];
      const startF = step.inicioFrame ?? 0;
      const endF = step.finFrame ?? totalFrames;

      if (frame >= startF && frame <= endF) {
        const stepProgress =
          endF > startF ? Math.min(1, Math.max(0, (frame - startF) / (endF - startF))) : 1;

        const easing = getEasingFunction(step.curva);
        const easedProgress = easing(stepProgress);

        const prevX = step.desdePosicion?.x ?? currentPos.x;
        const prevY = step.desdePosicion?.y ?? currentPos.y;

        // Interpolación de posición si se especificó destino o delta
        if (step.posicion) {
          const targetX = step.posicion.x ?? prevX;
          const targetY = step.posicion.y ?? prevY;
          currentPos.x = interpolate(easedProgress, [0, 1], [prevX, targetX]);
          currentPos.y = interpolate(easedProgress, [0, 1], [prevY, targetY]);
        } else if (step.deltaPosicion) {
          const targetX = prevX + (step.deltaPosicion.x ?? 0);
          const targetY = prevY + (step.deltaPosicion.y ?? 0);
          currentPos.x = interpolate(easedProgress, [0, 1], [prevX, targetX]);
          currentPos.y = interpolate(easedProgress, [0, 1], [prevY, targetY]);
        } else if (step.desdePosicion) {
          currentPos.x = prevX;
          currentPos.y = prevY;
        }

        prevPoseId = currentPose;
        if (step.poseId) {
          currentPose = step.poseId;
          poseTransitionProgress = Math.min(1, Math.max(0, (frame - startF) / 14));
        }
        if (step.expresion) currentExpr = step.expresion;
        if (step.escala !== undefined) {
          currentScale = interpolate(easedProgress, [0, 1], [currentScale, step.escala]);
        }
        if (step.orientacion) currentOrientation = step.orientacion;
        if (step.prop !== undefined) currentProp = step.prop || undefined;
        if (step.props) currentProps = step.props;
        if (step.esHolograma !== undefined) currentHolograma = step.esHolograma;
        if (step.opacidad !== undefined) {
          currentOpacity = interpolate(easedProgress, [0, 1], [currentOpacity, step.opacidad]);
        }
        proceduralMode = step.procedural ?? "estatico";

        // Modificadores cinemáticos y procedimentales
        if (step.procedural === "caminar" || step.procedural === "correr") {
          isWalking = true;
          const isRun = step.procedural === "correr";
          const strideSpeed = isRun ? 2.8 : 4.6;
          const walkBob = Math.abs(Math.sin((frame - startF) / strideSpeed)) * (isRun ? 16 : 12);
          currentPos.y -= walkBob;
          headTilt = Math.sin((frame - startF) / strideSpeed) * (isRun ? 6.0 : 4.0);
        } else if (step.procedural === "manipular") {
          // Acción manual rítmica (remover ácido, rallar alcanfor, ensamblar piezas, girar válvula)
          const workCycle = Math.sin((frame - startF) / 6.5);
          currentPos.y += Math.abs(workCycle) * 4;
          currentPos.x += workCycle * 2.5;
          headTilt = workCycle * 3.5;
        } else if (step.procedural === "esfuerzo") {
          // Tensión física (prensar palanca, estirar polímero, sellar escotilla a presión)
          const strain = Math.sin(frame * 0.32);
          vibrationX = strain * 1.8;
          currentPos.y += Math.abs(Math.sin((frame - startF) / 8)) * 5;
          headTilt = -5 + strain * 1.8;
        } else if (step.procedural === "agachar_recoger") {
          // Agacharse a recoger/depositar un objeto y reincorporarse
          const crouch = Math.sin(stepProgress * Math.PI);
          currentPos.y += crouch * 36;
          headTilt = crouch * 14;
        } else if (step.procedural === "temblar") {
          const decay = interpolate(stepProgress, [0, 1], [1, 0.1]);
          vibrationX = Math.sin(frame * 0.45) * 4 * decay;
          headTilt = Math.sin(frame * 0.35) * 3 * decay;
        } else if (step.procedural === "recoil") {
          if (frame - startF < 6) {
            isContactImpact = true;
          }
          currentPos.y += Math.sin(stepProgress * Math.PI) * -10;
        } else if (step.procedural === "rebotar") {
          const hopCycle = Math.abs(Math.sin((frame - startF) / 4)) * -14;
          currentPos.y += hopCycle;
          headTilt = Math.sin((frame - startF) / 4) * 4;
        } else if (step.procedural === "flotar") {
          currentPos.y += Math.sin((frame - startF) / 9) * 10;
          headTilt = Math.cos((frame - startF) / 9) * 2.5;
        } else {
          // Dinamismo sutil de reposo y conversación natural
          const isSpeaking = personaje.habla !== false;
          const communicativeTilt = isSpeaking ? Math.sin(frame / 6) * 3.2 : 0;
          const weightShift = Math.sin(frame / 16) * 3.0;
          const breath = Math.sin(frame / 10) * 2.0;
          headTilt = communicativeTilt;
          currentPos.x += weightShift;
          currentPos.y += breath;
        }

        break;
      } else if (frame > endF) {
        // Persistir estado acumulado tras finalizar el paso
        if (step.posicion) {
          currentPos.x = step.posicion.x ?? currentPos.x;
          currentPos.y = step.posicion.y ?? currentPos.y;
        } else if (step.deltaPosicion) {
          const baseX = step.desdePosicion?.x ?? currentPos.x;
          const baseY = step.desdePosicion?.y ?? currentPos.y;
          currentPos.x = baseX + (step.deltaPosicion.x ?? 0);
          currentPos.y = baseY + (step.deltaPosicion.y ?? 0);
        }
        if (step.poseId) currentPose = step.poseId;
        if (step.expresion) currentExpr = step.expresion;
        if (step.escala !== undefined) currentScale = step.escala;
        if (step.orientacion) currentOrientation = step.orientacion;
        if (step.prop !== undefined) currentProp = step.prop || undefined;
        if (step.props) currentProps = step.props;
        if (step.esHolograma !== undefined) currentHolograma = step.esHolograma;
        if (step.opacidad !== undefined) currentOpacity = step.opacidad;
      }
    }
  }

  return {
    poseId: currentPose,
    prevPoseId,
    poseTransitionProgress,
    expresion: currentExpr,
    x: currentPos.x,
    y: currentPos.y,
    escala: currentScale,
    orientacion: currentOrientation,
    prop: currentProp,
    props: currentProps,
    headTilt,
    isContactImpact,
    vibrationX,
    isWalking,
    proceduralMode,
    esHolograma: currentHolograma,
    colorRim: personaje.colorRim,
    opacidad: currentOpacity,
    visible,
  };
}
