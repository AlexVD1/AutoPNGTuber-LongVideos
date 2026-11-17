import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { InfografiaConfig, PalabraTiming } from "../types";
import { resolveTimeRangeFrames } from "../stickman/actionSequences";

export interface InfographicCardProps {
  config: InfografiaConfig;
  frame?: number;
  totalFrames?: number;
  palabras?: PalabraTiming[];
}

export const InfographicCard: React.FC<InfographicCardProps> = ({
  config,
  totalFrames = 900,
  palabras,
}) => {
  const currentFrame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const hasWindow =
    config.inicioProgreso !== undefined ||
    config.finProgreso !== undefined ||
    config.inicioSegundos !== undefined ||
    config.finSegundos !== undefined ||
    config.desdePalabra !== undefined ||
    config.hastaPalabra !== undefined;

  const { startFrame, endFrame } = hasWindow
    ? resolveTimeRangeFrames(config, totalFrames, fps, palabras)
    : { startFrame: 0, endFrame: totalFrames };

  if (currentFrame < startFrame || currentFrame > endFrame) {
    return null;
  }

  const localFrame = Math.max(0, currentFrame - startFrame);

  const entrance = spring({
    frame: localFrame,
    fps,
    config: {
      damping: 14,
      stiffness: 140,
      mass: 0.8,
    },
  });

  const exitOpacity =
    hasWindow && endFrame - currentFrame < 12
      ? interpolate(endFrame - currentFrame, [0, 12], [0, 1], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
        })
      : 1;

  // Animación de entrada dinámica: slide + micro-bounce + escala elástica
  const translateY = interpolate(entrance, [0, 1], [40, 0]);
  const opacity = interpolate(entrance, [0, 0.4, 1], [0, 0.8, 1]) * exitOpacity;
  const scale = interpolate(entrance, [0, 1], [0.92, 1]);

  // Sutil flotación orgánica continua (nunca estático ni plano)
  const organicFloatY = Math.sin(localFrame * 0.08) * 3.5;

  const posX = config.posicion?.x ?? (config.compacta ? 460 : 410);
  const posY = config.posicion?.y ?? 0;
  const accentColor = config.colorAcento || "#38BDF8";
  const cardWidth = config.compacta ? 480 : 580;

  // Pulso del indicador LED telemétrico
  const ledPulse = Math.sin(localFrame * 0.22) * 0.3 + 0.7;

  return (
    <div
      className="absolute pointer-events-none select-none"
      style={{
        zIndex: 14,
        left: 960 + posX,
        top: 540 + posY,
        transform: `translate(-50%, -50%) translateY(${translateY + organicFloatY}px) scale(${scale})`,
        opacity,
        width: cardWidth,
      }}
    >
      {/* Tarjeta Neo-Brutalista de Alto Impacto Editorial / Tecnológico */}
      <div
        className="rounded-2xl p-6 border-4 border-black relative overflow-hidden"
        style={{
          background: "linear-gradient(145deg, #0B1329 0%, #111E38 50%, #0F172A 100%)",
          boxShadow: `12px 12px 0px #000000, 0 0 30px ${accentColor}33`,
        }}
      >
        {/* Línea decorativa superior estilo escáner técnico */}
        <div
          className="absolute top-0 left-0 right-0 h-1.5"
          style={{
            background: `linear-gradient(90deg, #FFE600 0%, ${accentColor} 50%, #10B981 100%)`,
          }}
        />

        {/* HUD Crosshairs / Esquinas técnicas */}
        <div className="absolute top-2.5 left-2.5 text-[10px] font-mono text-slate-500 select-none">
          +--
        </div>
        <div className="absolute top-2.5 right-2.5 text-[10px] font-mono text-slate-500 select-none">
          --+
        </div>

        {/* Encabezado con píldora telemétrica animada */}
        <div className="flex items-center justify-between pb-3 mb-3 border-b-2 border-slate-700/80">
          <div className="flex items-center gap-2.5">
            {/* Indicador LED con pulso activo */}
            <span
              className="inline-flex items-center gap-1.5 px-2.5 py-1 text-[11px] font-black uppercase tracking-wider rounded-md border-2 border-black"
              style={{
                backgroundColor: accentColor,
                color: "#000000",
                boxShadow: "3px 3px 0px #000000",
              }}
            >
              <span
                className="w-2 h-2 rounded-full bg-black inline-block"
                style={{ opacity: ledPulse }}
              />
              {config.tipo.replace("_", " ")}
            </span>

            <span className="text-[10px] font-mono font-bold text-slate-400 tracking-wider">
              TELEMETRÍA // LIVE
            </span>
          </div>

          <span className="text-xs font-mono font-bold px-2 py-0.5 rounded bg-slate-800 text-sky-400 border border-slate-700">
            {`F:${localFrame.toString().padStart(4, "0")}`}
          </span>
        </div>

        {/* Título de la infografía */}
        <h3
          className="text-2xl font-black uppercase tracking-tight text-white mb-1"
          style={{
            fontFamily: "'Arial Black', 'Impact', system-ui, sans-serif",
            textShadow: "2px 2px 0px #000000",
          }}
        >
          {config.titulo}
        </h3>

        {/* Subtítulo descriptivo */}
        {config.subtitulo && (
          <p className="text-xs font-semibold text-slate-300 mb-3.5 leading-snug">
            {config.subtitulo}
          </p>
        )}

        {/* Valor numérico principal animado si existe */}
        {config.valorPrincipal !== undefined && (
          <div
            className="my-3 p-4 rounded-xl border-2 border-black flex items-baseline justify-between"
            style={{
              background: "linear-gradient(135deg, #1E293B 0%, #0F172A 100%)",
              boxShadow: "4px 4px 0px #000000",
            }}
          >
            <div>
              <span className="text-[10px] font-black uppercase tracking-wider text-slate-400 block mb-0.5">
                VARIABLE CRÍTICA
              </span>
              <div className="flex items-baseline gap-2">
                <span
                  className="text-4xl font-black text-white"
                  style={{
                    fontFamily: "'Arial Black', 'Impact', system-ui, sans-serif",
                    color: accentColor,
                    textShadow: "0 0 16px " + accentColor + "66",
                  }}
                >
                  {config.valorPrincipal}
                </span>
                {config.unidad && (
                  <span className="text-lg font-extrabold text-slate-300 uppercase">
                    {config.unidad}
                  </span>
                )}
              </div>
            </div>
            <span className="px-2.5 py-1 text-[10px] font-black uppercase bg-[#10B981] text-black rounded border border-black shadow-[2px_2px_0px_#000]">
              VERIFICADO
            </span>
          </div>
        )}

        {/* Lista de elementos o barras de comparación dinámicas */}
        {config.items && config.items.length > 0 && (
          <div className="space-y-2.5 mt-3">
            {config.items.map((item, idx) => {
              const itemProgress = spring({
                frame: Math.max(0, localFrame - idx * 5),
                fps,
                config: { damping: 12, stiffness: 150 },
              });

              const basePct = item.porcentaje ?? 70;
              // Micro-fluctuación dinámica que hace que las barras parezcan lecturas vivas en tiempo real
              const fluctuation = Math.sin(localFrame * 0.15 + idx * 1.6) * 1.5;
              const animatedPct = Math.min(
                100,
                Math.max(4, basePct * itemProgress + (itemProgress > 0.95 ? fluctuation : 0))
              );
              const barWidth = `${animatedPct.toFixed(1)}%`;
              const itemColor =
                item.color || (idx === 0 ? "#EF4444" : idx === 1 ? "#10B981" : "#38BDF8");

              // Patrón diagonal animado en movimiento continuo
              const stripeOffset = ((localFrame * 1.5) % 32).toFixed(1);

              return (
                <div
                  key={idx}
                  className="p-3 rounded-xl border-2 border-black"
                  style={{
                    backgroundColor: "rgba(15, 23, 42, 0.85)",
                    boxShadow: "3px 3px 0px #000000",
                  }}
                >
                  {/* Etiqueta superior y valor numérico */}
                  <div className="flex justify-between items-center mb-1.5">
                    <div className="flex items-center gap-1.5">
                      <span
                        className="w-2 h-2 rounded-full inline-block border border-black"
                        style={{ backgroundColor: itemColor }}
                      />
                      <span className="text-xs font-black text-slate-200 uppercase tracking-tight">
                        {item.etiqueta}
                      </span>
                    </div>

                    {item.valor !== undefined && (
                      <span
                        className="text-xs font-black px-2 py-0.5 rounded border border-black"
                        style={{
                          backgroundColor: "#020617",
                          color: itemColor,
                          boxShadow: "1.5px 1.5px 0px #000000",
                        }}
                      >
                        {item.valor}
                      </span>
                    )}
                  </div>

                  {/* Barra animada con textura estroboscópica y punta brillante */}
                  {item.porcentaje !== undefined && (
                    <div className="w-full h-4 bg-slate-900 rounded-full border-2 border-black overflow-hidden relative">
                      <div
                        className="h-full rounded-full transition-all relative flex items-center justify-end pr-1"
                        style={{
                          width: barWidth,
                          background: `repeating-linear-gradient(45deg, ${itemColor}, ${itemColor} 8px, rgba(0, 0, 0, 0.25) 8px, rgba(0, 0, 0, 0.25) 16px)`,
                          backgroundPosition: `${stripeOffset}px 0px`,
                          boxShadow: `0 0 12px ${itemColor}80`,
                        }}
                      >
                        {/* Indicador LED luminoso en la cabeza de la barra */}
                        <span
                          className="w-2 h-2 rounded-full bg-white inline-block border border-black"
                          style={{
                            boxShadow: "0 0 6px #FFFFFF",
                          }}
                        />
                      </div>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        )}

        {/* Footer técnico */}
        <div className="mt-3.5 pt-2 border-t border-slate-800 flex items-center justify-between text-[9px] font-mono font-bold text-slate-400">
          <span>SRC: AERONAUTICAL DYNAMICS // BIOMIMETICS</span>
          <span className="text-emerald-400">STATUS: ACTIVE</span>
        </div>
      </div>
    </div>
  );
};
