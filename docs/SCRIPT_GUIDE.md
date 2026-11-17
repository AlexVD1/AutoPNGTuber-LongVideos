# Guía de Creación de Guiones Narrativos Largos

Esta guía detalla cómo estructurar guiones completos para **AutoPNGTuber-LongVideos**. Los guiones se redactan en formato JSON dentro de `src/data/guion.json` (o archivos en `src/data/`).

---

## 1. Estructura General del Guion

Un guion largo consta de dos bloques principales: `meta` y `capitulos`.

```json
{
  "meta": {
    "id": "doc_001_senal_wow",
    "slug": "misterio_senal_wow",
    "titulo": "El Misterio de la Señal Wow!",
    "premisa": "Explicación del mayor enigma de la radioastronomía.",
    "gancho": "¿Qué escuchamos realmente en agosto de 1977?",
    "categoria": "Science & Technology",
    "duracionObjetivo": [495, 570],
    "fps": 30,
    "dimensiones": { "width": 1920, "height": 1080 },
    "idioma": "es",
    "voz": "alex.conds.pt",
    "musicaPrincipal": "bgm/bgm.mp3",
    "volumenMusica": 0.12,
    "fuentes": ["Paper científico 1", "Libro histórico 2"],
    "tags": ["ciencia", "espacio", "astronomia"]
  },
  "capitulos": [
    {
      "id": "cap_1",
      "numero": 1,
      "titulo": "El Descubrimiento Inesperado",
      "resumen": "La noche del 15 de agosto de 1977 en el observatorio Big Ear.",
      "escenas": [ ... ]
    }
  ]
}
```

> **Regla para Monetización Mid-Roll en YouTube ($\ge$ 8:15 minutos / 495+ segundos)**:
> Con Chatterbox TTS (`alex.conds.pt`) y compactación de pausas `v3_sentence_tailcut`, la velocidad de locución es de **~2.55 palabras por segundo (~153 palabras/minuto)**. Para garantizar una duración final de **al menos 8:15 minutos (`>= 495 s`)**:
> - Configura `duracionObjetivo: [495, 570]`.
> - Estructura el guion en **7 a 8 capítulos** (`capitulos`) con **14 a 16 escenas** (`escenas`) en total.
> - Cada escena debe tener entre **88 y 105 palabras habladas** en `texto` (escribe los números en letras para cálculo exacto), sumando entre **1,320 y 1,500 palabras totales** en todo el guion.

---

## 2. Definición de Escenas (`escenas`)

Cada elemento dentro de `capitulo.escenas` describe un evento visual, físico y sonoro sincronizado con las palabras del narrador:

| Campo | Tipo | Requerido | Descripción |
| :--- | :--- | :---: | :--- |
| `id` | `number` / `string` | Sí | Identificador secuencial único de la escena. Define el archivo `public/audios/escena_{id}.mp3`. |
| `texto` | `string` | Sí | Texto narrado por la voz clonada y mostrado en los subtítulos (escribir cifras en palabras o dejar que `normalizador_numeros.py` las expanda). |
| `tituloVisual` | `string` | No | Rótulo superior en mayúsculas visible durante los primeros segundos (conserva cifras arábigas grandes). |
| `layout` | `string` | No | Distribución espacial en 16:9 (`panoramica_central` recomendado para acción diegética, `infografia_derecha`, `infografia_izquierda`, `split_screen`, `primer_plano`). |
| `composicionVisual` | `string` | No | Tipo de encuadre base (`plano_general`, `plano_medio`, `primer_plano`, `escenario_ilustrado`, `minimalista`). |
| `escenario` | `string` | No | Fondo ilustrado 16:9 (`laboratorio`, `espacio_profundo`, `lunar`, `superficie_marte`, `habitacion_noche`, `abismo_oceanico`, `red_subterranea`, `cielo_dia`, `vacio`). |
| `iluminacionVolumetrica`| `boolean` | No | Activa haces de luz diagonal y partículas atmosféricas en suspensión (`LightRaysOverlay`). |
| `planos` | `PlanoCamara[]` | No | Secuencia de micro-cortes de cámara (`general`, `plano_medio`, `primer_plano`, `sobre_hombro`, `detalle_mano`) con `blurFondo` y `accionMano`. |
| `personajes` | `PersonajeEscena[]`| No | Lista de personajes en escena con secuencias `acciones[].pasos[]` articuladas por IK/FK de 2 huesos, `esHolograma` y `trayectoriaSuelo`. |
| `objetos` | `ObjetoEscena[]` | No | Lista de máquinas o props con secuencia de estados `pasos[]` (`estado`, `posicion`, `escala`, `capaZ`). |
| `cotasVectoriales` | `CotaVectorial[]` | No | Flechas técnicas punteadas y etiquetas diegéticas sobre las máquinas (`origenX/Y` $\rightarrow$ `destinoX/Y`). |
| `emisoresParticulas` | `EmisorParticulas[]`| No | Sistemas de partículas balísticas (`chispas_quimicas`, `gotas_acido`, `vapor_presion`, `eslabones_polimero`, `fragmentos_marfil`). |
| `eventosSfx` | `EventoSfx[]` | No | Efectos de sonido puntuales disparados en palabras específicas (`desdePalabra` o `enSegundo`). |
| `sfx` | `string` | No | Efecto sonoro de apertura de escena (`sfx/sfx_whoosh.wav`, `sfx/sfx_dramatic_hit.wav`, `sfx/sfx_impact.wav`, etc.). |
| `volumenSfx` | `number` | No | Volumen del SFX (`0.15` a `0.30`). |
| `palabrasClave` | `string[]` | No | Palabras destacadas en tipografía cian `#38BDF8` en los subtítulos. |
| `infografia` | `object` | No | Tarjeta gráfica opcional (preferir `cotasVectoriales` para no tapar la acción). |
| `efectosCamara` | `string[]` | No | Modificadores globales: `["drift"]`, `["shake"]`, `["punch"]`, `["pan_left"]`, `["pan_right"]`. |
| `transicion` | `string` | No | Entrada: `"zoom_in"`, `"whip_right"`, `"whip_left"`, `"flash"`, `"fundido_negro"`, `"corte"`. |

---

## 3. Dirección Cinematográfica Avanzada (Animación Fluida)

### 3.1 Micro-Planos, Profundidad de Campo (DoF) e Insertos de Mano (`planos`)
Divide cada escena de 35-40 s en 3 o 4 planos sincronizados con `desdePalabra` / `hastaPalabra`:

```json
"planos": [
  {
    "tipo": "general",
    "desdePalabra": "A finales del",
    "hastaPalabra": "cada jugada",
    "x": 960,
    "y": 540,
    "zoom": 1.0,
    "blurFondo": 0
  },
  {
    "tipo": "sobre_hombro",
    "desdePalabra": "Pero había un",
    "hastaPalabra": "dos mil dólares",
    "x": 760,
    "y": 490,
    "zoom": 1.24,
    "blurFondo": 4,
    "ladoHombro": "derecho"
  },
  {
    "tipo": "detalle_mano",
    "desdePalabra": "mezcló celulosa",
    "hastaPalabra": "bloque sólido",
    "x": 980,
    "y": 510,
    "zoom": 1.32,
    "blurFondo": 6,
    "accionMano": "verter_acido"
  }
]
```
- **`accionMano` disponibles**: `"verter_acido"`, `"prensar_palanca"`, `"estirar_cadena"`, `"girar_valvula"`, `"tocar_esfera"`.

### 3.2 Personajes Articulados (IK/FK 2 Huesos), Hologramas y Trayectorias (`personajes`)
Cada paso dentro de `personajes[].acciones[].pasos[]` interpola continuamente las articulaciones desde la pose previa hacia la nueva pose:

```json
"personajes": [
  {
    "id": "inventor",
    "rol": "John Wesley Hyatt",
    "posicion": { "x": 520, "y": 640 },
    "escala": 1.08,
    "capaZ": 20,
    "colorRim": "#38BDF8",
    "acciones": [
      {
        "pasos": [
          {
            "desdePalabra": "En su taller",
            "hastaPalabra": "ácido nítrico",
            "desdePosicion": { "x": 420, "y": 640 },
            "posicion": { "x": 680, "y": 640 },
            "poseId": "walking_right",
            "expresion": "determined",
            "orientacion": "derecha",
            "procedural": "caminar"
          },
          {
            "desdePalabra": "imaginó qué pasaría",
            "hastaPalabra": "presión extrema",
            "posicion": { "x": 740, "y": 640 },
            "poseId": "presenting_open",
            "expresion": "analytical",
            "orientacion": "derecha",
            "esHolograma": true,
            "trayectoriaSuelo": {
              "destinoX": 1060,
              "destinoY": 670,
              "etiqueta": "PROYECCIÓN DE IMPACTO",
              "color": "#38BDF8"
            }
          }
        ]
      }
    ]
  }
]
```

### 3.3 Máquinas Multi-Estado (`objetos[].pasos`) y Cotas Diegéticas (`cotasVectoriales`)
Los objetos cambian de estado y posición al compás de la narración (`capaZ: 28` para asegurar que siempre queden por delante de cualquier tarjeta infográfica, y oscilaciones suaves `Math.sin(f * 0.12..0.30)` en `propsLibrary.ts`), mientras las `cotasVectoriales` despliegan mediciones técnicas directamente sobre la máquina (manteniendo `destinoX` entre `740` y `1180` y `destinoY` entre `220` y `340` para no tapar nunca la cabeza del personaje):

```json
"objetos": [
  {
    "id": "autoclave",
    "propId": "bakelizer_autoclave",
    "posicion": { "x": 240, "y": 40 },
    "escala": 1.25,
    "capaZ": 28,
    "pasos": [
      { "desdePalabra": "cerró la caldera", "hastaPalabra": "ciento cincuenta", "estado": "abierto" },
      { "desdePalabra": "ciento cincuenta", "hastaPalabra": "resina ámbar", "estado": "presurizado" },
      { "desdePalabra": "resina ámbar", "hastaPalabra": "para siempre", "estado": "baquelita_lista" }
    ]
  }
],
"cotasVectoriales": [
  {
    "id": "cota_temp",
    "texto": "180 °C + ALTA PRESIÓN",
    "subtexto": "Polimerización fenol-formaldehído",
    "origenX": 1040,
    "origenY": 480,
    "destinoX": 820,
    "destinoY": 300,
    "color": "#FFE600",
    "desdePalabra": "ciento cincuenta",
    "hastaPalabra": "resina ámbar"
  }
],
"emisoresParticulas": [
  {
    "tipo": "vapor_presion",
    "x": 1040,
    "y": 430,
    "intensidad": 1.2,
    "desdePalabra": "ciento cincuenta",
    "hastaPalabra": "resina ámbar"
  }
]
```

---

## 3. Tarjetas Gráficas e Infografías (`infografia`)

Aprovechan el formato panorámico 16:9 para ilustrar conceptos científicos en un lateral de la pantalla mientras el Stickman explica:

```json
{
  "infografia": {
    "tipo": "dato_clave",
    "titulo": "Frecuencia Sagrada",
    "subtitulo": "Emisión del Hidrógeno Neutro (21 cm)",
    "valorPrincipal": "1420.4",
    "unidad": "MHz",
    "items": [
      { "etiqueta": "Señal Wow!", "valor": "Banda estrecha", "porcentaje": 100, "color": "#38BDF8" },
      { "etiqueta": "Ruido cósmico", "valor": "Banda ancha", "porcentaje": 20, "color": "#94A3B8" }
    ],
    "colorAcento": "#FFE600",
    "posicion": { "x": 300, "y": 0 }
  }
}
```

Tipos disponibles:
- `"dato_clave"`: Cifra numérica colosal con valor y porcentaje.
- `"comparacion"`: Dos o más barras de contraste visual.
- `"tarjeta_concepto"`: Explicación textual destacada con ítems.
- `"grafico_barras"`: Comparación métrica de progreso.

---

## 4. Layouts Panorámicos 16:9 (`layout`)

1. **`infografia_derecha`**: El personaje se coloca automáticamente a la izquierda (`x: -450`), dejando el espacio derecho para una tarjeta de datos o diagrama.
2. **`infografia_izquierda`**: El personaje se sitúa a la derecha (`x: 450`), mirando a la izquierda, con la tarjeta en el lado izquierdo.
3. **`panoramica_central`**: El personaje ocupa el centro del escenario con libertad para interactuar con el entorno.
4. **`primer_plano`**: Zoom dramático sobre el rostro y torso del personaje para reacciones enfáticas o revelaciones.
5. **`split_screen`**: División de pantalla en dos mitades (lado A vs lado B).

---

## 5. Ejemplo de Producción Completo

Revisa `src/data/guion_ejemplo_completo.json` para ver un guion de 5 capítulos y 13 escenas con narrativa completa, infografías, fuentes y diseño cinematográfico.
