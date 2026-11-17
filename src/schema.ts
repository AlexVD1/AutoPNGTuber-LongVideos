import { z } from "zod";

export const PalabraTimingSchema = z.object({
  palabra: z.string(),
  inicioMs: z.number().min(0),
  finMs: z.number().min(0),
});

export const InfografiaConfigSchema = z.object({
  tipo: z.enum([
    "dato_clave",
    "comparacion",
    "tarjeta_concepto",
    "grafico_barras",
    "linea_tiempo",
    "cita",
  ]),
  titulo: z.string().min(1),
  subtitulo: z.string().optional(),
  valorPrincipal: z.union([z.string(), z.number()]).optional(),
  unidad: z.string().optional(),
  items: z
    .array(
      z.object({
        etiqueta: z.string(),
        valor: z.union([z.string(), z.number()]).optional(),
        color: z.string().optional(),
        porcentaje: z.number().min(0).max(100).optional(),
      })
    )
    .optional(),
  colorAcento: z.string().optional(),
  posicion: z.object({ x: z.number(), y: z.number() }).optional(),
  icono: z.string().optional(),
  compacta: z.boolean().optional(),
  inicioProgreso: z.number().optional(),
  finProgreso: z.number().optional(),
  inicioSegundos: z.number().optional(),
  finSegundos: z.number().optional(),
  desdePalabra: z.string().optional(),
  hastaPalabra: z.string().optional(),
});

export const PasoAccionSchema = z.object({
  inicioFrame: z.number().optional(),
  finFrame: z.number().optional(),
  inicioProgreso: z.number().optional(),
  finProgreso: z.number().optional(),
  inicioSegundos: z.number().optional(),
  finSegundos: z.number().optional(),
  desdePalabra: z.string().optional(),
  hastaPalabra: z.string().optional(),
  poseId: z.string().optional(),
  expresion: z.string().optional(),
  desdePosicion: z.object({ x: z.number().optional(), y: z.number().optional() }).optional(),
  posicion: z.object({ x: z.number().optional(), y: z.number().optional() }).optional(),
  deltaPosicion: z.object({ x: z.number().optional(), y: z.number().optional() }).optional(),
  escala: z.number().optional(),
  orientacion: z.enum(["derecha", "izquierda"]).optional(),
  curva: z.enum(["lineal", "suave", "anticipacion", "rebote", "impacto"]).optional(),
  prop: z.string().optional(),
  props: z
    .object({
      derecha: z.string().optional(),
      izquierda: z.string().optional(),
      arriba: z.string().optional(),
      sombrero: z.string().optional(),
      cara: z.string().optional(),
      cuello: z.string().optional(),
      cintura: z.string().optional(),
    })
    .optional(),
  procedural: z
    .enum([
      "caminar",
      "correr",
      "temblar",
      "rebotar",
      "flotar",
      "recoil",
      "manipular",
      "esfuerzo",
      "agachar_recoger",
      "estatico",
    ])
    .optional(),
  esHolograma: z.boolean().optional(),
  opacidad: z.number().optional(),
  arquetipo: z.string().optional(),
  ropaTorso: z.string().optional(),
  colorTorso: z.string().optional(),
  colorSecundarioTorso: z.string().optional(),
  colorPantalones: z.string().optional(),
  colorZapatos: z.string().optional(),
  peinado: z.string().optional(),
  colorPelo: z.string().optional(),
  accesorioCabeza: z.string().optional(),
  colorAccesorio: z.string().optional(),
});

export const AccionPersonajeSchema = z.object({
  tipo: z
    .enum([
      "caminar_hacia",
      "detenerse_y_mirar",
      "acercarse_y_tocar",
      "sorpresa_y_retroceso",
      "tropezar_y_reaccionar",
      "mirar_y_reaccionar",
      "sonambulo_avanzar",
      "despertar_asustado",
      "guiar_amigo",
      "explicar_calma",
      "personalizada",
    ])
    .optional(),
  pasos: z.array(PasoAccionSchema).optional(),
  desdeX: z.number().optional(),
  haciaX: z.number().optional(),
  desdeY: z.number().optional(),
  haciaY: z.number().optional(),
  inicioFrame: z.number().optional(),
  duracionFrames: z.number().optional(),
  objetivoId: z.string().optional(),
});

export const PersonajeEscenaSchema = z.object({
  id: z.string().min(1),
  nombre: z.string().optional(),
  poseId: z.string().optional(),
  expresion: z.string().optional(),
  prop: z.string().optional(),
  props: z
    .object({
      derecha: z.string().optional(),
      izquierda: z.string().optional(),
      arriba: z.string().optional(),
      sombrero: z.string().optional(),
      cara: z.string().optional(),
      cuello: z.string().optional(),
      cintura: z.string().optional(),
    })
    .optional(),
  efectoAmbiente: z.string().optional(),
  posicion: z.object({ x: z.number().optional(), y: z.number().optional() }).optional(),
  escala: z.number().optional(),
  orientacion: z.enum(["derecha", "izquierda"]).optional(),
  animacionEntrada: z.enum(["rebote", "zoom", "deslizar", "ninguna"]).optional(),
  acciones: z.array(AccionPersonajeSchema).optional(),
  habla: z.boolean().optional(),
  capaZ: z.number().optional(),
  opacidad: z.number().optional(),
  espectral: z.boolean().optional(),
  esHolograma: z.boolean().optional(),
  colorRim: z.string().optional(),
  arquetipo: z.string().optional(),
  ropaTorso: z.string().optional(),
  colorTorso: z.string().optional(),
  colorSecundarioTorso: z.string().optional(),
  colorPantalones: z.string().optional(),
  colorZapatos: z.string().optional(),
  peinado: z.string().optional(),
  colorPelo: z.string().optional(),
  accesorioCabeza: z.string().optional(),
  colorAccesorio: z.string().optional(),
  trayectoriaSuelo: z
    .object({
      desdeX: z.number(),
      hastaX: z.number(),
      y: z.number().optional(),
      etiqueta: z.string().optional(),
      color: z.string().optional(),
    })
    .optional(),
  inicioProgreso: z.number().optional(),
  finProgreso: z.number().optional(),
  inicioSegundos: z.number().optional(),
  finSegundos: z.number().optional(),
  desdePalabra: z.string().optional(),
  hastaPalabra: z.string().optional(),
});

export const PasoObjetoSchema = z.object({
  inicioFrame: z.number().optional(),
  finFrame: z.number().optional(),
  inicioProgreso: z.number().optional(),
  finProgreso: z.number().optional(),
  inicioSegundos: z.number().optional(),
  finSegundos: z.number().optional(),
  desdePalabra: z.string().optional(),
  hastaPalabra: z.string().optional(),
  desdePosicion: z.object({ x: z.number(), y: z.number() }).optional(),
  posicion: z.object({ x: z.number(), y: z.number() }).optional(),
  escala: z.number().optional(),
  rotacion: z.number().optional(),
  opacidad: z.number().optional(),
  estado: z.string().optional(),
  propId: z.string().optional(),
  curva: z.enum(["lineal", "suave", "anticipacion", "rebote", "impacto"]).optional(),
  animacion: z
    .enum(["caer", "flotar", "vibrar", "pulso", "fijo", "rodar", "rebotar"])
    .optional(),
});

export const ObjetoEscenaSchema = z.object({
  id: z.string().min(1),
  propId: z.string().min(1),
  posicion: z.object({ x: z.number(), y: z.number() }),
  escala: z.number().optional(),
  rotacion: z.number().optional(),
  opacidad: z.number().optional(),
  capaZ: z.number().optional(),
  estado: z.string().optional(),
  inicioProgreso: z.number().optional(),
  finProgreso: z.number().optional(),
  inicioSegundos: z.number().optional(),
  finSegundos: z.number().optional(),
  desdePalabra: z.string().optional(),
  hastaPalabra: z.string().optional(),
  pasos: z.array(PasoObjetoSchema).optional(),
  animacion: z
    .object({
      tipo: z.enum(["caer", "flotar", "vibrar", "pulso", "fijo", "rodar", "rebotar"]),
      inicioFrame: z.number().optional(),
      finFrame: z.number().optional(),
      deltaY: z.number().optional(),
      deltaX: z.number().optional(),
    })
    .optional(),
});

export const EventoSfxSchema = z.object({
  sfx: z.string().min(1),
  tiempoSegundos: z.number().optional(),
  enSegundo: z.number().optional(),
  progreso: z.number().optional(),
  desdePalabra: z.string().optional(),
  volumen: z.number().min(0).max(1).optional(),
});

export const FocoCamaraKeyframeSchema = z.object({
  inicioProgreso: z.number().optional(),
  finProgreso: z.number().optional(),
  inicioSegundos: z.number().optional(),
  finSegundos: z.number().optional(),
  desdePalabra: z.string().optional(),
  hastaPalabra: z.string().optional(),
  x: z.number(),
  y: z.number(),
  escala: z.number().optional(),
  curva: z.enum(["lineal", "suave", "anticipacion", "rebote", "impacto"]).optional(),
});

export const PlanoCamaraSchema = z.object({
  tipo: z.enum([
    "general",
    "plano_medio",
    "primer_plano",
    "sobre_hombro",
    "detalle_mano",
    "zoom_cuadrante",
  ]),
  x: z.number().optional(),
  y: z.number().optional(),
  zoom: z.number().optional(),
  blurFondo: z.number().optional(),
  cuadrante: z
    .enum([
      "superior_derecha",
      "superior_izquierda",
      "inferior_derecha",
      "inferior_izquierda",
      "centro_derecha",
      "centro_izquierda",
      "centro",
    ])
    .optional(),
  hombroLado: z.enum(["izquierda", "derecha"]).optional(),
  accionMano: z
    .enum([
      "verter_acido",
      "prensar_palanca",
      "estirar_cadena",
      "girar_valvula",
      "tocar_esfera",
      "apilar_bloques",
      "medir_compas",
      "tensar_cable_acero",
      "bajar_interruptor",
      "ajustar_telescopio",
      "girar_dial_radio",
      "escribir_tiza_pizarra",
      "pulsar_boton_casino",
      "encender_cerilla",
      "tallar_pedernal_silex",
      "proteger_brasa_manos",
    ])
    .optional(),
  etiquetaInsert: z.string().optional(),
  inicioProgreso: z.number().optional(),
  finProgreso: z.number().optional(),
  inicioSegundos: z.number().optional(),
  finSegundos: z.number().optional(),
  desdePalabra: z.string().optional(),
  hastaPalabra: z.string().optional(),
});

const TipoAnimacionEnum = z.enum([
  "elasticidad_espaciotiempo",
  "orbita_fotones_esfera",
  "espaguetificacion_marea",
  "dilatacion_temporal_relatividad",
  "vortice_arrastre_kerr",
  "espuma_cuantica_planck",
  "radiacion_hawking_pares",
  "colapso_schwarzschild_masa",
  "ala_desprendimiento_stall",
  "alula_tobera_venturi",
  "microestructura_velcro_barbula",
  "valvula_aleteo_persiana",
  "herbst_mecanoreceptor_impulso",
  "cinematica_ocho_aleteo",
  "dispersion_acustica_peines",
  "balance_energetico_cerebro_20",
  "hipotesis_tejido_caro_aiello",
  "dilema_obstetrico_pelvis",
  "homunculo_motor_pinza",
]);

export const RecuadroEducativoSchema = z.object({
  tipo: TipoAnimacionEnum.optional(),
  tipoAnimacion: TipoAnimacionEnum.optional(),
  titulo: z.string().optional(),
  subtitulo: z.string().optional(),
  posicion: z
    .union([
      z.enum([
        "superior_derecha",
        "superior_izquierda",
        "inferior_derecha",
        "inferior_izquierda",
        "centro_derecha",
        "centro_izquierda",
        "centro",
      ]),
      z.object({ x: z.number(), y: z.number() }),
    ])
    .optional(),
  ancho: z.number().optional(),
  alto: z.number().optional(),
  desdePalabra: z.string().optional(),
  hastaPalabra: z.string().optional(),
  inicioSegundos: z.number().optional(),
  finSegundos: z.number().optional(),
  colorAcento: z.string().optional(),
  dimmingEscenario: z.boolean().optional(),
});

export const CotaVectorialSchema = z.object({
  id: z.string().optional(),
  origenX: z.number(),
  origenY: z.number(),
  destinoX: z.number(),
  destinoY: z.number(),
  valor: z.string(),
  etiqueta: z.string().optional(),
  color: z.string().optional(),
  inicioProgreso: z.number().optional(),
  finProgreso: z.number().optional(),
  inicioSegundos: z.number().optional(),
  finSegundos: z.number().optional(),
  desdePalabra: z.string().optional(),
  hastaPalabra: z.string().optional(),
});

export const EmisorParticulasSchema = z.object({
  id: z.string().optional(),
  tipo: z.enum([
    "chispas_quimicas",
    "gotas_acido",
    "vapor_presion",
    "eslabones_polimero",
    "fragmentos_marfil",
    "escombros_piedra",
    "rafagas_viento",
    "fotones_luz",
    "polvo_estelar",
  ]),
  x: z.number(),
  y: z.number(),
  cantidad: z.number().optional(),
  color: z.string().optional(),
  inicioProgreso: z.number().optional(),
  finProgreso: z.number().optional(),
  inicioSegundos: z.number().optional(),
  finSegundos: z.number().optional(),
  desdePalabra: z.string().optional(),
  hastaPalabra: z.string().optional(),
});

export const EscenaLargaGuionSchema = z.object({
  id: z.union([z.number(), z.string()]),
  globalIndex: z.number().optional(),
  capituloId: z.union([z.number(), z.string()]).optional(),
  texto: z.string().min(1, "El texto de la escena no puede estar vacío"),
  tituloVisual: z.string().optional(),
  layout: z
    .enum([
      "panoramica_central",
      "dialogo_dual",
      "infografia_derecha",
      "infografia_izquierda",
      "split_screen",
      "primer_plano",
      "cifras_concepto",
      "clasico",
    ])
    .optional(),
  composicionVisual: z
    .enum([
      "minimalista",
      "escenario_ilustrado",
      "primer_plano",
      "plano_general",
      "plano_medio",
      "cifras_concepto",
    ])
    .optional(),
  escenario: z.string().optional(),
  personajes: z.array(PersonajeEscenaSchema).optional(),
  objetos: z.array(ObjetoEscenaSchema).optional(),
  infografia: InfografiaConfigSchema.optional(),
  elementosNarrativos: z.array(z.any()).optional(),
  efectosCamara: z.array(z.enum(["shake", "punch", "drift", "pan_left", "pan_right"])).optional(),
  focoCamara: z.array(FocoCamaraKeyframeSchema).optional(),
  planos: z.array(PlanoCamaraSchema).optional(),
  cotasVectoriales: z.array(CotaVectorialSchema).optional(),
  emisoresParticulas: z.array(EmisorParticulasSchema).optional(),
  iluminacionVolumetrica: z.boolean().optional(),
  badgeCalendario: z
    .object({
      texto: z.string(),
      subtexto: z.string().optional(),
      colorCabecera: z.string().optional(),
      x: z.number().optional(),
      y: z.number().optional(),
    })
    .optional(),
  pildoraMetrica: z
    .object({
      etiqueta: z.string().optional(),
      valor: z.string(),
      colorBorde: z.string().optional(),
      posicion: z
        .enum([
          "superior_izquierda",
          "inferior_centro",
          "superior_derecha",
          "personalizada",
        ])
        .optional(),
      x: z.number().optional(),
      y: z.number().optional(),
    })
    .optional(),
  recuadroEducativo: RecuadroEducativoSchema.optional(),
  recuadrosEducativos: z.array(RecuadroEducativoSchema).optional(),
  dimmingManual: z.boolean().optional(),
  silencioFinalSegundos: z.number().min(0).max(20).optional(),
  fadeOutFinalSegundos: z.number().min(0).max(20).optional(),
  transicion: z
    .enum(["zoom_in", "whip_right", "whip_left", "flash", "corte", "fundido_negro"])
    .optional(),
  sfx: z.string().optional(),
  volumenSfx: z.number().min(0).max(1).optional(),
  eventosSfx: z.array(EventoSfxSchema).optional(),
  palabrasClave: z.array(z.string()).optional(),
  duracionSegundos: z.number().positive().optional(),
  palabras: z.array(PalabraTimingSchema).optional(),
  personajeHablaId: z.string().optional(),
  voz: z.string().optional(),
  poseId: z.string().optional(),
  expresion: z.string().optional(),
  prop: z.string().optional(),
  props: z.any().optional(),
  posicion: z.object({ x: z.number().optional(), y: z.number().optional() }).optional(),
  escala: z.number().optional(),
  orientacion: z.enum(["derecha", "izquierda"]).optional(),
  animacionEntrada: z.enum(["rebote", "zoom", "deslizar", "ninguna"]).optional(),
  icono: z.string().optional(),
  colorIcono: z.string().optional(),
});

export const CapituloGuionSchema = z.object({
  id: z.union([z.number(), z.string()]),
  numero: z.number().int().positive(),
  titulo: z.string().min(1, "El título del capítulo es requerido"),
  resumen: z.string().optional(),
  musicaOverride: z.string().optional(),
  volumenMusicaOverride: z.number().optional(),
  escenas: z.array(EscenaLargaGuionSchema).min(1, "Cada capítulo debe tener al menos una escena"),
  duracionSegundos: z.number().optional(),
});

export const LongVideoMetaSchema = z.object({
  id: z.string().min(1),
  slug: z.string().min(1),
  titulo: z.string().min(1),
  premisa: z.string().optional(),
  gancho: z.string().optional(),
  categoria: z.string().optional(),
  duracionObjetivo: z.tuple([z.number().positive(), z.number().positive()]).optional(),
  fps: z.number().int().positive().optional(),
  dimensiones: z
    .object({
      width: z.number().int().positive(),
      height: z.number().int().positive(),
    })
    .optional(),
  idioma: z.string().optional(),
  voz: z.string().optional(),
  musicaPrincipal: z.string().optional(),
  volumenMusica: z.number().min(0).max(1).optional(),
  fuentes: z.array(z.string()).optional(),
  tags: z.array(z.string()).optional(),
});

export const GuionLargoCompletoSchema = z.object({
  meta: LongVideoMetaSchema,
  capitulos: z.array(CapituloGuionSchema).min(1, "El guion debe incluir al menos un capítulo"),
});
