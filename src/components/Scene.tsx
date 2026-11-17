import React, { useMemo } from "react";
import {
  AbsoluteFill,
  Audio,
  Sequence,
  getStaticFiles,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { EscenaLargaGuion, PersonajeEscena, RecuadroEducativoConfig } from "../types";
import {
  evaluateCharacterState,
  resolvePointFrame,
  resolveTimeRangeFrames,
} from "../stickman/actionSequences";
import { CameraRig, evaluateActiveCameraShot } from "./CameraRig";
import { EducationalZoomBox } from "./EducationalZoomBox";
import {
  DiegeticCalloutsLayer,
  HandInsertOverlay,
  OverTheShoulderForeground,
} from "./DiegeticCallout";
import { InfographicCard } from "./InfographicCard";
import { NarrativeElements } from "./NarrativeElements";
import {
  ESCENARIOS_OSCUROS_16X9,
  MesaComedorFamiliarForeground,
  DespachoEinsteinForeground,
  NarrativeStage16x9,
} from "./NarrativeStage16x9";
import { LightRaysOverlay, ParticleEmitterLayer } from "./ParticleEmitter";
import { SceneObject } from "./SceneObject";
import { Stickman } from "./Stickman";
import { WordSubtitles } from "./WordSubtitles";
import { BadgeCalendario, PildoraMetrica } from "./EditorialUI";

export interface SceneProps {
  escena: EscenaLargaGuion;
  capituloNumero?: number;
  capituloTitulo?: string;
  escenaIndice?: number;
  totalEscenas?: number;
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

export const Scene: React.FC<SceneProps> = ({
  escena,
  capituloNumero,
  capituloTitulo,
  escenaIndice,
  totalEscenas,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const sceneDurationFrames = Math.max(
    1,
    Math.round((escena.duracionSegundos ?? 5) * fps)
  );

  // SFX inteligente
  const sfxPath = escena.sfx || "sfx/pop.mp3";
  const sfxVolume = escena.volumenSfx ?? (escena.sfx ? 0.25 : 0.18);
  const hasSfx = useMemo(() => fileExistsInStatic(sfxPath), [sfxPath]);

  // Normalización de personajes para 16:9 horizontal
  const layout = escena.layout ?? "panoramica_central";

  const personajesList: PersonajeEscena[] = useMemo(() => {
    if (escena.personajes && escena.personajes.length > 0) {
      return escena.personajes;
    }

    // Posicionamiento adaptativo según el layout 16:9
    let defaultPosX = 0;
    let defaultPosY = 40;
    let defaultOrientacion: "derecha" | "izquierda" = "derecha";

    if (layout === "infografia_derecha" || (escena.infografia && layout !== "infografia_izquierda")) {
      defaultPosX = -440;
      defaultOrientacion = "derecha";
    } else if (layout === "infografia_izquierda") {
      defaultPosX = 440;
      defaultOrientacion = "izquierda";
    }

    return [
      {
        id: "principal",
        poseId: escena.poseId ?? "standing_relaxed",
        expresion: escena.expresion,
        prop: escena.prop,
        props: escena.props,
        efectoAmbiente: escena.efectoAmbiente,
        posicion: escena.posicion ?? { x: defaultPosX, y: defaultPosY },
        escala: escena.escala ?? 1,
        orientacion: escena.orientacion ?? defaultOrientacion,
        animacionEntrada: escena.animacionEntrada ?? "rebote",
        habla: true,
      },
    ];
  }, [
    escena.personajes,
    escena.poseId,
    escena.expresion,
    escena.prop,
    escena.props,
    escena.efectoAmbiente,
    escena.posicion,
    escena.escala,
    escena.orientacion,
    escena.animacionEntrada,
    escena.infografia,
    layout,
  ]);

  // Determinación estricta de qué personaje tiene el foco de habla (evita que hablen todos a la vez)
  const activeSpeakerId = useMemo(() => {
    if (escena.personajeHablaId) return escena.personajeHablaId;
    const explicit = (escena.personajes || []).find((p) => p.habla === true);
    if (explicit) return explicit.id;
    const narrator = (escena.personajes || []).find(
      (p) =>
        p.id.toLowerCase().includes("narrador") ||
        p.id.toLowerCase().includes("protagonista") ||
        p.arquetipo === "protagonista"
    );
    if (narrator) return narrator.id;
    return escena.personajes?.[0]?.id;
  }, [escena.personajeHablaId, escena.personajes]);

  // Evaluación procedural de cada personaje sincronizada con la locución
  const evaluatedCharacters = personajesList.map((p) => {
    const evalState = evaluateCharacterState(
      p,
      frame,
      fps,
      sceneDurationFrames,
      escena.palabras
    );
    return {
      ...p,
      evaluated: evalState,
    };
  });

  const resolvedSfxEvents = useMemo(() => {
    if (!escena.eventosSfx || escena.eventosSfx.length === 0) return [];
    return escena.eventosSfx
      .filter((ev) => ev.sfx && fileExistsInStatic(ev.sfx))
      .map((ev) => ({
        ...ev,
        startFrame: resolvePointFrame(
          ev,
          sceneDurationFrames,
          fps,
          escena.palabras
        ),
      }));
  }, [escena.eventosSfx, escena.palabras, sceneDurationFrames, fps]);

  const hasContactImpact = evaluatedCharacters.some(
    (c) => c.evaluated.isContactImpact
  );

  const escenario = escena.escenario || "vacio";
  const halo = ESCENARIOS_OSCUROS_16X9.has(escenario);
  const audioFile = `audios/escena_${escena.id}.mp3`;
  const hasAudio = useMemo(() => fileExistsInStatic(audioFile), [audioFile]);

  const cameraShot = evaluateActiveCameraShot(
    escena.planos,
    escena.focoCamara,
    frame,
    sceneDurationFrames,
    fps,
    escena.palabras
  );

  // 2b. Recuadros educativos didácticos (estilo Veritasium / Kurzgesagt PiP)
  const allRecuadros = useMemo(() => {
    const list: RecuadroEducativoConfig[] = [];
    if (escena.recuadroEducativo) list.push(escena.recuadroEducativo);
    if (escena.recuadrosEducativos) list.push(...escena.recuadrosEducativos);
    return list;
  }, [escena.recuadroEducativo, escena.recuadrosEducativos]);

  const activeRecuadro = allRecuadros.find((rec) => {
    const { startFrame, endFrame } = resolveTimeRangeFrames(
      rec,
      sceneDurationFrames,
      fps,
      escena.palabras
    );
    return frame >= startFrame && frame <= endFrame;
  });

  // Dimming: reduce brillo del escenario mientras se explica activamente un recuadro didáctico
  const isDimmingActive =
    (Boolean(activeRecuadro) && (activeRecuadro?.dimmingEscenario ?? true)) ||
    Boolean(escena.dimmingManual);

  return (
    <AbsoluteFill className="relative overflow-hidden bg-[#0F172A]">
      {/* 1. Audio de voz de la escena */}
      {hasAudio && <Audio src={staticFile(audioFile)} volume={1.0} />}

      {/* 2. Audio de SFX de entrada y eventos de SFX sincronizados con acciones */}
      {hasSfx && <Audio src={staticFile(sfxPath)} volume={sfxVolume} />}
      {resolvedSfxEvents.map((ev, idx) => (
        <Sequence
          key={`${ev.sfx}_${idx}_${ev.startFrame}`}
          from={Math.max(0, ev.startFrame)}
          layout="none"
        >
          <Audio src={staticFile(ev.sfx)} volume={ev.volumen ?? 0.3} />
        </Sequence>
      ))}

      {/* 3. MUNDO CINEMATOGRÁFICO 16:9 (Cámara, fondo con DoF, objetos, partículas y personajes) */}
      <div className="absolute inset-0 z-0">
        <CameraRig
          transicion={escena.transicion ?? "zoom_in"}
          efectosCamara={escena.efectosCamara ?? ["drift"]}
          focoCamara={escena.focoCamara}
          planos={escena.planos}
          palabras={escena.palabras}
          composicionVisual={escena.composicionVisual ?? "minimalista"}
          impactFrame={hasContactImpact ? frame : undefined}
          durationInFrames={sceneDurationFrames}
        >
          {/* Escenario horizontal 16:9 con Profundidad de Campo (DoF) y Dimming (brillo 40% al explicar diagramas) */}
          <div
            className="absolute inset-0"
            style={{
              filter: `${
                cameraShot.blurFondo > 0.2
                  ? `blur(${cameraShot.blurFondo.toFixed(1)}px) `
                  : ""
              }${isDimmingActive ? "brightness(0.55)" : "brightness(1.0)"}`,
              transform:
                cameraShot.blurFondo > 0.2 ? "scale(1.035)" : undefined,
              transition: "filter 0.25s ease",
            }}
          >
            <NarrativeStage16x9
              escenario={escenario}
              composicionVisual={escena.composicionVisual}
              frame={frame}
            />
          </div>

          {/* Dimming overlay estilo Veritasium: atenúa el fondo para resaltar diagramas sin oscurecer props ni personajes */}
          {isDimmingActive && (
            <div
              className="absolute inset-0 pointer-events-none"
              style={{
                backgroundColor: "rgba(0, 0, 0, 0.35)",
                zIndex: 8,
              }}
            />
          )}

          {/* Iluminación volumétrica (haces de luz y polvo en suspensión) */}
          <LightRaysOverlay active={escena.iluminacionVolumetrica ?? true} />

          {/* Infografía o tarjeta de datos widescreen (al fondo del plano medio, detrás de props y personajes) */}
          {escena.infografia && (
            <InfographicCard
              config={escena.infografia}
              frame={frame}
              totalFrames={sceneDurationFrames}
              palabras={escena.palabras}
            />
          )}

          {/* Elementos narrativos vectoriales (velocímetro, olas, partículas) */}
          <NarrativeElements
            elementos={escena.elementosNarrativos}
            totalFrames={sceneDurationFrames}
            palabras={escena.palabras}
          />

          {/* Props y objetos en el escenario (siempre al frente de infografías) */}
          {(escena.objetos || []).map((obj) => (
            <SceneObject
              key={obj.id}
              objeto={obj}
              frame={frame}
              fps={fps}
              totalFrames={sceneDurationFrames}
              palabras={escena.palabras}
            />
          ))}

          {/* Emisores de partículas balísticas deterministas */}
          <ParticleEmitterLayer
            emisores={escena.emisoresParticulas}
            palabras={escena.palabras}
          />

          {/* Cotas vectoriales diegéticas y trayectorias en el suelo */}
          <DiegeticCalloutsLayer
            cotas={escena.cotasVectoriales}
            personajes={personajesList}
            palabras={escena.palabras}
          />

          {/* Personajes actuando en el canvas 16:9 */}
          <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
            {evaluatedCharacters.map((char) => {
              const ev = char.evaluated;
              if (ev.visible === false) return null;

              const isAnima =
                char.id.toLowerCase().includes("fantasma") ||
                char.id.toLowerCase().includes("espectral") ||
                Boolean(char.espectral);

              return (
                <div
                  key={char.id}
                  className="absolute"
                  style={{
                    zIndex: Math.max(22, char.capaZ ?? 22),
                    transform: `translate(${ev.x}px, ${ev.y}px)`,
                    opacity: ev.opacidad ?? (isAnima ? 0.85 : 1),
                    filter: isAnima
                      ? "invert(1) drop-shadow(0 0 16px #38BDF8)"
                      : undefined,
                  }}
                >
                  <Stickman
                    poseId={ev.poseId}
                    prevPoseId={ev.prevPoseId}
                    poseTransitionProgress={ev.poseTransitionProgress}
                    expresion={ev.expresion}
                    prop={ev.prop}
                    props={ev.props}
                    efectoAmbiente={char.efectoAmbiente}
                    orientacion={ev.orientacion}
                    escala={ev.escala}
                    posicion={{ x: 0, y: 0 }}
                    headTiltOffset={ev.headTilt}
                    vibrationOffset={ev.vibrationX}
                    proceduralMode={ev.proceduralMode}
                    esHolograma={ev.esHolograma}
                    colorRim={ev.colorRim}
                    animacionEntrada={char.animacionEntrada ?? "ninguna"}
                    palabras={escena.palabras}
                    halo={halo && !isAnima}
                    arquetipo={char.arquetipo}
                    ropaTorso={char.ropaTorso}
                    colorTorso={char.colorTorso}
                    colorSecundarioTorso={char.colorSecundarioTorso}
                    colorPantalones={char.colorPantalones}
                    colorZapatos={char.colorZapatos}
                    peinado={char.peinado}
                    colorPelo={char.colorPelo}
                    accesorioCabeza={char.accesorioCabeza}
                    colorAccesorio={char.colorAccesorio}
                    overrideIsSpeaking={
                      char.habla !== undefined
                        ? char.habla
                          ? undefined
                          : false
                        : char.id === activeSpeakerId
                        ? undefined
                        : false
                    }
                  />
                </div>
              );
            })}
          </div>

          {/* Foreground de la mesa de banquete (queda por delante de las piernas y cintura de los comensales sentados) */}
          {(escena.escenario === "comedor_familiar" ||
            escena.escenario === "salon_comedor") && (
            <MesaComedorFamiliarForeground frame={frame} />
          )}

          {/* Foreground del escritorio de Albert Einstein (queda por delante del personaje sentado o actuando detrás) */}
          {escena.escenario === "despacho_einstein_1915" && (
            <DespachoEinsteinForeground frame={frame} />
          )}

          {/* Destello de impacto visual entre personajes */}
          {hasContactImpact && (
            <div
              className="absolute pointer-events-none z-40"
              style={{
                left: "50%",
                top: "50%",
                transform: "translate(-50%, -50%)",
              }}
            >
              <svg width="180" height="180" viewBox="0 0 140 140">
                <path
                  d="M 70 10 L 80 50 L 120 35 L 90 68 L 130 85 L 88 95 L 98 135 L 68 105 L 42 130 L 50 88 L 12 80 L 48 60 L 22 25 L 60 48 Z"
                  fill="#FFE600"
                  stroke="#000000"
                  strokeWidth="5"
                />
              </svg>
            </div>
          )}
        </CameraRig>
      </div>

      {/* 3b. Silueta desenfocada en primer plano (Over-the-Shoulder) o Insert de Mano */}
      {cameraShot.activePlano?.tipo === "sobre_hombro" && (
        <OverTheShoulderForeground
          lado={cameraShot.activePlano.hombroLado ?? "izquierda"}
        />
      )}
      {cameraShot.activePlano?.tipo === "detalle_mano" && (
        <HandInsertOverlay
          plano={cameraShot.activePlano}
          localFrame={cameraShot.planoLocalFrame}
          durationFrames={cameraShot.planoDurationFrames}
        />
      )}



      {/* 3c. RECUADROS EDUCATIVOS EN ZOOM (Estilo Veritasium / Kurzgesagt PiP) */}
      {allRecuadros.map((rec, idx) => (
        <EducationalZoomBox
          key={`edu-box-${idx}`}
          config={rec}
          palabras={escena.palabras}
          durationInFrames={sceneDurationFrames}
        />
      ))}

      {/* Badge de Calendario Editorial (Solo si no hay colisión con recuadros ni píldoras) */}
      {escena.badgeCalendario && allRecuadros.length === 0 && !escena.pildoraMetrica && (
        <BadgeCalendario {...escena.badgeCalendario} />
      )}

      {/* Píldora de métrica / cifra gigante con prevención de colisiones en cuadrante superior derecho */}
      {escena.pildoraMetrica && (() => {
        const pildora = { ...escena.pildoraMetrica };
        if (allRecuadros.length > 0 && (!pildora.posicion || pildora.posicion === "superior_derecha")) {
          pildora.posicion = "personalizada";
          pildora.x = 80;
          pildora.y = 780;
        }
        return <PildoraMetrica {...pildora} />;
      })()}

      {/* Título visual grande si la escena lo declara */}
      {escena.tituloVisual && frame < 68 && (() => {
        const len = escena.tituloVisual.length;
        const fontSize = len > 46 ? 38 : len > 32 ? 46 : len > 22 ? 54 : 62;
        return (
          <div
            className="absolute top-16 left-0 right-0 flex justify-center text-center pointer-events-none z-30 px-12"
            style={{
              opacity: interpolate(frame, [52, 68], [1, 0], {
                extrapolateLeft: "clamp",
                extrapolateRight: "clamp",
              }),
            }}
          >
            <span
              className="uppercase px-8 py-2.5 bg-yellow-300 text-black border-4 border-black shadow-[8px_8px_0px_#000000] rounded-2xl"
              style={{
                fontFamily: "'Arial Black', 'Impact', system-ui, sans-serif",
                fontWeight: 900,
                fontSize,
                lineHeight: 1.15,
                maxWidth: 1680,
                letterSpacing: "1px",
              }}
            >
              {escena.tituloVisual}
            </span>
          </div>
        );
      })()}

      {/* 5. CAPA HUD INFERIOR (Subtítulos en franja segura y≈920-1020) */}
      <div
        className="absolute left-0 right-0 bottom-8 flex items-center justify-center pointer-events-none z-40"
        style={{ minHeight: 110 }}
      >
        <WordSubtitles
          palabras={escena.palabras ?? []}
          palabrasClave={escena.palabrasClave}
        />
      </div>

      {/* 6. Fundido a negro final contemplativo si la escena lo solicita (ej. Epílogo 4s) */}
      {escena.fadeOutFinalSegundos && escena.fadeOutFinalSegundos > 0 && (() => {
        const fadeFrames = Math.min(
          sceneDurationFrames,
          Math.max(15, Math.round(escena.fadeOutFinalSegundos * fps))
        );
        const startFade = Math.max(0, sceneDurationFrames - fadeFrames);
        if (frame < startFade) return null;
        const fadeOpacity = interpolate(
          frame,
          [startFade, sceneDurationFrames - 1],
          [0, 1],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
        );
        return (
          <div
            className="absolute inset-0 bg-black pointer-events-none"
            style={{ zIndex: 55, opacity: fadeOpacity }}
          />
        );
      })()}
    </AbsoluteFill>
  );
};
