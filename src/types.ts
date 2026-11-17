import { EfectoAmbienteFestivo } from "./stickman/festiveLibrary";
import {
  ArquetipoStickman,
  TipoAccesorioCabeza,
  TipoPeinado,
  TipoRopaTorso,
} from "./stickman/wardrobeLibrary";

export type {
  ArquetipoStickman,
  TipoAccesorioCabeza,
  TipoPeinado,
  TipoRopaTorso,
};

export type OrientacionStickman = "derecha" | "izquierda";
export type AnimacionEntradaStickman =
  | "rebote"
  | "zoom"
  | "deslizar"
  | "ninguna";

export interface StickmanPropsAttachment {
  derecha?: string;
  izquierda?: string;
  arriba?: string;
  sombrero?: string;
  cara?: string;
  cuello?: string;
  cintura?: string;
}

export interface PalabraTiming {
  palabra: string;
  inicioMs: number;
  finMs: number;
}

export type TipoElementoNarrativo =
  | "speed_counter"
  | "speed_lines"
  | "flying_debris"
  | "giant_waves"
  | "shockwave_burst"
  | "orbital_peace"
  | "danger_vignette"
  | "sparks_explosion"
  | "steam_vent"
  | "chemical_bubbles";

export interface ElementoNarrativo {
  tipo: TipoElementoNarrativo;
  valorNumerico?: number;
  unidad?: string;
  subtitulo?: string;
  color?: string;
  direccion?: "este" | "oeste" | "arriba" | "abajo";
  intensidad?: number;
  x?: number;
  y?: number;
  inicioProgreso?: number;
  finProgreso?: number;
  inicioSegundos?: number;
  finSegundos?: number;
  desdePalabra?: string;
  hastaPalabra?: string;
}

export type TipoTransicion =
  | "zoom_in"
  | "whip_right"
  | "whip_left"
  | "flash"
  | "corte"
  | "fundido_negro";

export type EstiloLayout16x9 =
  | "panoramica_central"
  | "dialogo_dual"
  | "infografia_derecha"
  | "infografia_izquierda"
  | "split_screen"
  | "primer_plano"
  | "cifras_concepto"
  | "clasico";

export type TipoComposicionVisual =
  | "minimalista"
  | "escenario_ilustrado"
  | "primer_plano"
  | "plano_general"
  | "plano_medio"
  | "cifras_concepto";

export type TipoCurvaMovimiento =
  | "lineal"
  | "suave"
  | "anticipacion"
  | "rebote"
  | "impacto";

export type TipoMovimientoProcedural =
  | "caminar"
  | "correr"
  | "temblar"
  | "rebotar"
  | "flotar"
  | "recoil"
  | "manipular"
  | "esfuerzo"
  | "agachar_recoger"
  | "estatico";

export type AccionPredefinidaTipo =
  | "caminar_hacia"
  | "detenerse_y_mirar"
  | "acercarse_y_tocar"
  | "sorpresa_y_retroceso"
  | "tropezar_y_reaccionar"
  | "mirar_y_reaccionar"
  | "sonambulo_avanzar"
  | "despertar_asustado"
  | "guiar_amigo"
  | "explicar_calma";

export interface PasoAccion {
  inicioFrame?: number;
  finFrame?: number;
  inicioProgreso?: number;
  finProgreso?: number;
  inicioSegundos?: number;
  finSegundos?: number;
  desdePalabra?: string;
  hastaPalabra?: string;
  poseId?: string;
  expresion?: string;
   desdePosicion?: { x?: number; y?: number };
  posicion?: { x?: number; y?: number };
  deltaPosicion?: { x?: number; y?: number };
  escala?: number;
  orientacion?: OrientacionStickman;
  curva?: TipoCurvaMovimiento;
  prop?: string;
  props?: StickmanPropsAttachment;
  mirarHacia?: { x: number; y: number } | "objetivo";
  procedural?: TipoMovimientoProcedural;
  esHolograma?: boolean;
  opacidad?: number;
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

export interface AccionPersonaje {
  tipo?: AccionPredefinidaTipo | "personalizada";
  pasos?: PasoAccion[];
  desdeX?: number;
  haciaX?: number;
  desdeY?: number;
  haciaY?: number;
  inicioFrame?: number;
  duracionFrames?: number;
  objetivoId?: string;
}

export interface TrayectoriaSuelo {
  desdeX: number;
  hastaX: number;
  y?: number;
  etiqueta?: string;
  color?: string;
}

export interface PersonajeEscena {
  id: string;
  nombre?: string;
  poseId?: string;
  expresion?: string;
  prop?: string;
  props?: StickmanPropsAttachment;
  efectoAmbiente?: EfectoAmbienteFestivo;
  posicion?: { x?: number; y?: number };
  escala?: number;
  orientacion?: OrientacionStickman;
  animacionEntrada?: AnimacionEntradaStickman;
  acciones?: AccionPersonaje[];
  habla?: boolean;
  capaZ?: number;
  opacidad?: number;
  espectral?: boolean;
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
  trayectoriaSuelo?: TrayectoriaSuelo;
  inicioProgreso?: number;
  finProgreso?: number;
  inicioSegundos?: number;
  finSegundos?: number;
  desdePalabra?: string;
  hastaPalabra?: string;
}

export type TipoAnimacionObjeto =
  | "caer"
  | "flotar"
  | "vibrar"
  | "pulso"
  | "fijo"
  | "rodar"
  | "rebotar";

export interface PasoObjeto {
  inicioFrame?: number;
  finFrame?: number;
  inicioProgreso?: number;
  finProgreso?: number;
  inicioSegundos?: number;
  finSegundos?: number;
  desdePalabra?: string;
  hastaPalabra?: string;
  desdePosicion?: { x: number; y: number };
  posicion?: { x: number; y: number };
  escala?: number;
  rotacion?: number;
  opacidad?: number;
  estado?: string;
  propId?: string;
  curva?: TipoCurvaMovimiento;
  animacion?: TipoAnimacionObjeto;
}

export interface ObjetoEscena {
  id: string;
  propId: string;
  posicion: { x: number; y: number };
  escala?: number;
  rotacion?: number;
  opacidad?: number;
  capaZ?: number;
  estado?: string;
  inicioProgreso?: number;
  finProgreso?: number;
  inicioSegundos?: number;
  finSegundos?: number;
  desdePalabra?: string;
  hastaPalabra?: string;
  pasos?: PasoObjeto[];
  animacion?: {
    tipo: TipoAnimacionObjeto;
    inicioFrame?: number;
    finFrame?: number;
    deltaY?: number;
    deltaX?: number;
  };
}

export interface InfografiaConfig {
  tipo:
    | "dato_clave"
    | "comparacion"
    | "tarjeta_concepto"
    | "grafico_barras"
    | "linea_tiempo"
    | "cita";
  titulo: string;
  subtitulo?: string;
  valorPrincipal?: string | number;
  unidad?: string;
  items?: Array<{
    etiqueta: string;
    valor?: string | number;
    color?: string;
    porcentaje?: number;
  }>;
  colorAcento?: string;
  posicion?: { x: number; y: number };
  icono?: string;
  compacta?: boolean;
  inicioProgreso?: number;
  finProgreso?: number;
  inicioSegundos?: number;
  finSegundos?: number;
  desdePalabra?: string;
  hastaPalabra?: string;
}

export interface EventoSfx {
  sfx: string;
  tiempoSegundos?: number;
  enSegundo?: number;
  progreso?: number;
  desdePalabra?: string;
  volumen?: number;
}

export interface FocoCamaraKeyframe {
  inicioProgreso?: number;
  finProgreso?: number;
  inicioSegundos?: number;
  finSegundos?: number;
  desdePalabra?: string;
  hastaPalabra?: string;
  x: number;
  y: number;
  escala?: number;
  curva?: TipoCurvaMovimiento;
}

export type TipoPlanoCamara =
  | "general"
  | "plano_medio"
  | "primer_plano"
  | "sobre_hombro"
  | "detalle_mano"
  | "zoom_cuadrante";

export type CuadrantePantalla =
  | "superior_derecha"
  | "superior_izquierda"
  | "inferior_derecha"
  | "inferior_izquierda"
  | "centro_derecha"
  | "centro_izquierda"
  | "centro";

export type TipoAnimacionEducativa =
  | "elasticidad_espaciotiempo"
  | "orbita_fotones_esfera"
  | "espaguetificacion_marea"
  | "dilatacion_temporal_relatividad"
  | "vortice_arrastre_kerr"
  | "espuma_cuantica_planck"
  | "radiacion_hawking_pares"
  | "colapso_schwarzschild_masa"
  | "ala_desprendimiento_stall"
  | "alula_tobera_venturi"
  | "microestructura_velcro_barbula"
  | "valvula_aleteo_persiana"
  | "herbst_mecanoreceptor_impulso"
  | "cinematica_ocho_aleteo"
  | "dispersion_acustica_peines"
  | "balance_energetico_cerebro_20"
  | "hipotesis_tejido_caro_aiello"
  | "dilema_obstetrico_pelvis"
  | "homunculo_motor_pinza";

export interface RecuadroEducativoConfig {
  tipo?: TipoAnimacionEducativa;
  tipoAnimacion?: TipoAnimacionEducativa;
  titulo?: string;
  subtitulo?: string;
  posicion?: CuadrantePantalla | { x: number; y: number };
  ancho?: number;
  alto?: number;
  desdePalabra?: string;
  hastaPalabra?: string;
  inicioSegundos?: number;
  finSegundos?: number;
  colorAcento?: string;
  dimmingEscenario?: boolean;
}

export interface PlanoCamara {
  tipo: TipoPlanoCamara;
  x?: number;
  y?: number;
  zoom?: number;
  blurFondo?: number;
  cuadrante?: CuadrantePantalla;
  hombroLado?: "izquierda" | "derecha";
  accionMano?:
    | "verter_acido"
    | "prensar_palanca"
    | "estirar_cadena"
    | "girar_valvula"
    | "tocar_esfera"
    | "apilar_bloques"
    | "medir_compas"
    | "tensar_cable_acero"
    | "bajar_interruptor"
    | "ajustar_telescopio"
    | "girar_dial_radio"
    | "escribir_tiza_pizarra"
    | "pulsar_boton_casino"
    | "encender_cerilla"
    | "tallar_pedernal_silex"
    | "proteger_brasa_manos";
  etiquetaInsert?: string;
  inicioProgreso?: number;
  finProgreso?: number;
  inicioSegundos?: number;
  finSegundos?: number;
  desdePalabra?: string;
  hastaPalabra?: string;
}

export interface CotaVectorial {
  id?: string;
  origenX: number;
  origenY: number;
  destinoX: number;
  destinoY: number;
  valor: string;
  etiqueta?: string;
  color?: string;
  inicioProgreso?: number;
  finProgreso?: number;
  inicioSegundos?: number;
  finSegundos?: number;
  desdePalabra?: string;
  hastaPalabra?: string;
}

export type TipoParticulaEscena =
  | "chispas_quimicas"
  | "gotas_acido"
  | "vapor_presion"
  | "eslabones_polimero"
  | "fragmentos_marfil"
  | "escombros_piedra"
  | "rafagas_viento"
  | "fotones_luz"
  | "polvo_estelar";

export interface EmisorParticulas {
  id?: string;
  tipo: TipoParticulaEscena;
  x: number;
  y: number;
  cantidad?: number;
  color?: string;
  inicioProgreso?: number;
  finProgreso?: number;
  inicioSegundos?: number;
  finSegundos?: number;
  desdePalabra?: string;
  hastaPalabra?: string;
}

export interface BadgeCalendarioConfig {
  texto: string;
  subtexto?: string;
  colorCabecera?: string;
  x?: number;
  y?: number;
}

export interface PildoraMetricaConfig {
  etiqueta?: string;
  valor: string;
  colorBorde?: string;
  posicion?: "superior_izquierda" | "inferior_centro" | "superior_derecha" | "personalizada";
  x?: number;
  y?: number;
}

export interface EscenaLargaGuion {
  id: number | string;
  globalIndex?: number;
  capituloId?: number | string;
  texto: string;
  tituloVisual?: string;
  layout?: EstiloLayout16x9;
  composicionVisual?: TipoComposicionVisual;
  escenario?: string;
  personajes?: PersonajeEscena[];
  objetos?: ObjetoEscena[];
  infografia?: InfografiaConfig;
  elementosNarrativos?: ElementoNarrativo[];
  efectosCamara?: ("shake" | "punch" | "drift" | "pan_left" | "pan_right")[];
  focoCamara?: FocoCamaraKeyframe[];
  planos?: PlanoCamara[];
  cotasVectoriales?: CotaVectorial[];
  emisoresParticulas?: EmisorParticulas[];
  iluminacionVolumetrica?: boolean;
  transicion?: TipoTransicion;
  sfx?: string;
  volumenSfx?: number;
  eventosSfx?: EventoSfx[];
  palabrasClave?: string[];
  duracionSegundos?: number;
  palabras?: PalabraTiming[];
  personajeHablaId?: string;
  voz?: string;
  badgeCalendario?: BadgeCalendarioConfig;
  pildoraMetrica?: PildoraMetricaConfig;
  recuadroEducativo?: RecuadroEducativoConfig;
  recuadrosEducativos?: RecuadroEducativoConfig[];
  dimmingManual?: boolean;
  silencioFinalSegundos?: number;
  fadeOutFinalSegundos?: number;
  // Compatibilidad con props en raíz de escena
  poseId?: string;
  expresion?: string;
  prop?: string;
  props?: StickmanPropsAttachment;
  efectoAmbiente?: EfectoAmbienteFestivo;
  orientacion?: OrientacionStickman;
  escala?: number;
  posicion?: { x?: number; y?: number };
  animacionEntrada?: AnimacionEntradaStickman;
  icono?: string;
  colorIcono?: string;
}

export interface CapituloGuion {
  id: number | string;
  numero: number;
  titulo: string;
  resumen?: string;
  musicaOverride?: string;
  volumenMusicaOverride?: number;
  escenas: EscenaLargaGuion[];
  duracionSegundos?: number;
}

export interface LongVideoMeta {
  id: string;
  slug: string;
  titulo: string;
  premisa?: string;
  gancho?: string;
  categoria?: string;
  duracionObjetivo?: [number, number];
  fps?: number;
  dimensiones?: { width: number; height: number };
  idioma?: string;
  voz?: string;
  musicaPrincipal?: string;
  volumenMusica?: number;
  fuentes?: string[];
  tags?: string[];
}

export interface GuionLargoCompleto {
  meta: LongVideoMeta;
  capitulos: CapituloGuion[];
}

export interface VideoChapterTimestamp {
  seconds: number;
  timestamp: string;
  title: string;
}

export interface YouTubePublicationMetadata {
  id: string;
  slug: string;
  title: string;
  description: string;
  chapters: VideoChapterTimestamp[];
  chaptersText: string;
  tags: string[];
  category: string;
  language: string;
  targetDurationSeconds: [number, number];
  actualDurationSeconds: number;
  resolution: { width: number; height: number };
  fps: number;
  codecVideo: string;
  codecAudio: string;
  ttsVoice: string;
  bgmTrack: string;
  sources: string[];
  outputFile: string;
  renderedAt: string;
}
