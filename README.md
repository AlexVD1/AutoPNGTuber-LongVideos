# AutoPNGTuber-LongVideos

> **Generador Autónomo de Documentales Animados Largos (16:9, 1920×1080 @ 30 FPS) para YouTube con Remotion, Rig Esquelético IK/FK de 2 Huesos, Chatterbox CUDA + Faster-Whisper y FFmpeg.**

---

## 1. Características Principales

- **Formato Widescreen 16:9 (1920 × 1080 @ 30 FPS)**: Dirección cinematográfica horizontal con 3 planos de profundidad, iluminación volumétrica, profundidad de campo (DoF) y escenarios reactivos.
- **Animación Esquelética Continua (IK/FK de 2 Huesos + Cabeza 2.5D)**: Motor en `src/stickman/skeletalRig.ts` que interpola hombros, codos, muñecas, rodillas y tobillos de forma continua entre poses, con giro de cabeza 2.5D, torso volumétrico con luz de recorte (*rim light*), sombra proyectada dinámica y modo holograma cian (`esHolograma`) para hipótesis y predicciones.
- **Dirección de Micro-Planos Cinematográficos (`planos`)**: Cortes automáticos dentro de cada escena (`general`, `plano_medio`, `primer_plano`, `sobre_hombro` con silueta desenfocada en primer plano, y `detalle_mano` con manos articuladas en macro) más desenfoque de fondo (`blurFondo`).
- **Cotas Vectoriales Diegéticas y Emisores Físicos**: Líneas de medición punteadas y etiquetas técnicas (`cotasVectoriales`) ancladas directamente sobre las máquinas con margen seguro garantizado, flechas de trayectoria en el suelo (`trayectoriaSuelo`) y emisores de partículas con física balística (`emisoresParticulas`).
- **Voz Clonada Neural Local + Alineación por Palabra**: Síntesis en GPU con **Chatterbox TTS** (`public/voices/alex.conds.pt`), normalización fonética de cifras (`scripts/normalizador_numeros.py`), poda inteligente de silencios (`v3_sentence_tailcut`) y alineación temporal exacta palabra por palabra con **Faster-Whisper** (`desdePalabra` / `hastaPalabra`).
- **Renderizado Segmentado con Tolerancia a Fallos**: Renderiza cada capítulo como un segmento de video independiente (`out/segments/capitulo_{n}.mp4`). Si el proceso se interrumpe, se reanuda instantáneamente reutilizando los segmentos válidos.
- **Música Continua y Audio Ducking (Sidechain)**: La música de fondo no se corta ni se reinicia entre capítulos. Mediante FFmpeg `sidechaincompress`, se atenúa automáticamente cuando habla el narrador y se normaliza a **-14 LUFS / -1.5 dB True Peak**.
- **Marcas de Tiempo y Metadatos Automáticos**: Generación de capítulos para YouTube (`out/{slug}_capitulos.txt`) y metadatos SEO (`out/{slug}.metadata.json`) medidos sobre la duración real con `ffprobe`.
- **Control de Calidad Audiovisual (QA)**: Inspección automatizada de códecs, resolución, FPS, niveles de sonoridad y extracción de fotogramas clave en `out/snapshots/`.
- **Totalmente Aislado**: Proyecto 100% independiente ubicado en su propio directorio; nunca modifica el generador de Shorts original.

---

## 2. Requisitos del Sistema

1. **Node.js**: v18 o superior (v24 compatible).
2. **Python**: 3.10 o superior con entorno virtual CUDA (`voice-lab/.venv`):
   - `chatterbox-tts` y `faster-whisper` (síntesis de voz clonada y alineación en GPU)
   - `mutagen` (medición de duración MP3)
3. **FFmpeg & FFprobe**: Versión 5.0 o superior disponible en el PATH del sistema.

---

## 3. Instalación Rápida

```bash
# 1. Clonar o acceder al directorio del proyecto
cd "c:\Users\villa\GIT DESKTOP\AutoPNGTuber-LongVideos"

# 2. Instalar dependencias de Node.js
npm install

# 3. Ejecutar suite de pruebas automatizadas
npm test
```

---

## 4. Comandos de Producción

| Comando | Acción |
| :--- | :--- |
| `npm run render` | **Pipeline Completo**: Valida el guion, sintetiza la voz, renderiza los capítulos, ensambla el video con BGM y ducking, genera capítulos y ejecuta QA. |
| `npm run tts` | Sintetiza únicamente los audios de narración y actualiza `guion.json` con los timings. |
| `npm run render:chapters` | Renderiza los segmentos de video de cada capítulo en `out/segments/`. |
| `npm run assemble` | Concatena los segmentos con FFmpeg y mezcla música con sidechain ducking. |
| `npm run capitulos` | Genera las marcas de tiempo para YouTube a partir de los segmentos reales. |
| `npm run validar` | Comprueba la estructura Zod del guion y los recursos en disco. |
| `npm run qa` | Inspecciona el video generado y extrae capturas de prueba. |
| `npm run dev` | Inicia Remotion Studio para previsualización interactiva en el navegador. |
| `npm test` | Ejecuta la suite de pruebas unitarias y de integración. |

---

## 5. Estructura del Proyecto

```text
AutoPNGTuber-LongVideos/
├── docs/
│   ├── ARCHITECTURE.md          # Especificación técnica detallada
│   ├── SCRIPT_GUIDE.md          # Guía para redactar guiones narrativos
│   └── WORKFLOW.md              # Flujo de trabajo operativo paso a paso
├── public/
│   ├── audios/                  # Audios generados por escena (.mp3)
│   ├── bgm/                     # Pistas de música de fondo (.mp3)
│   ├── poses/                   # Catálogo de SVGs del personaje Stickman
│   └── sfx/                     # Efectos de sonido procedurales (.wav)
├── out/
│   ├── segments/                # Segmentos MP4 independientes por capítulo
│   ├── snapshots/               # Capturas de inspección visual de calidad
│   ├── {slug}.mp4               # Video final ensamblado y masterizado
│   ├── {slug}_capitulos.txt     # Marcas de tiempo listas para YouTube
│   └── {slug}.metadata.json     # Metadatos completos para publicación
├── scripts/
│   ├── pipeline.js              # Orquestador del pipeline end-to-end
│   ├── normalizador_numeros.py  # Expansión fonética de cifras y unidades a palabras
│   ├── tts_engine.py            # Motor Chatterbox CUDA + Faster-Whisper + caché SHA-256
│   ├── render_segments.js       # Renderizado de capítulos con Remotion CLI
│   ├── assemble_video.py        # Ensamble FFmpeg, música continua y audio ducking
│   ├── generar_capitulos.js     # Cálculo de timestamps y metadatos SEO de YouTube
│   ├── generar_sfx.py           # Síntesis procedural de SFX en Python
│   ├── validar_guion.js         # Validador de esquemas Zod, catálogos y dicción
│   └── qa_video.js              # Chequeos de calidad ffprobe y volumen
├── src/
│   ├── components/
│   │   ├── CameraRig.tsx        # Cámara cinemática (micro-planos, OTS, insertos de manos)
│   │   ├── ChapterHeader.tsx    # Insignia superior de capítulo y progreso
│   │   ├── DiegeticCallout.tsx  # Cotas vectoriales diegéticas y trayectorias en el suelo
│   │   ├── InfographicCard.tsx  # Tarjetas de datos y comparativas 16:9
│   │   ├── NarrativeElements.tsx# Efectos vectoriales (velocímetro, viñetas, conectores)
│   │   ├── NarrativeStage16x9.tsx# Escenarios panorámicos 1920x1080 en SVG
│   │   ├── ParticleEmitter.tsx  # Emisores de partículas balísticas y rayos volumétricos
│   │   ├── Scene.tsx            # Coordinador maestro 16:9 (DoF, planos, actores, HUD)
│   │   ├── SceneObject.tsx      # Props multi-estado e interactivos en escena
│   │   ├── SplitScreen.tsx      # Layout de pantalla dividida
│   │   ├── Stickman.tsx         # Personaje con rig IK/FK continuo, cabeza 2.5D y holograma
│   │   └── WordSubtitles.tsx    # Subtítulos activos en franja segura inferior
│   ├── compositions/
│   │   ├── ChapterComposition.tsx # Composición individual de capítulo
│   │   └── LongVideo.tsx        # Composición global de previsualización
│   ├── data/
│   │   ├── guion.json           # Guion activo en producción
│   │   ├── guion_ejemplo_completo.json # Guion documental de ejemplo
│   │   └── poses.json           # Catálogo de poses corporales y expresiones
│   ├── stickman/
│   │   ├── skeletalRig.ts       # Solver IK de 2 huesos e interpolación articular continua
│   │   ├── actionSequences.ts   # Sincronización por palabras (desdePalabra/hastaPalabra)
│   │   ├── composites.ts        # Evaluación de secuencias de personaje y caminata
│   │   ├── bodyPoses.ts         # Catálogo de poses vectoriales
│   │   ├── expressions.ts       # Catálogo de expresiones faciales
│   │   └── propsLibrary.ts      # Props ilustrados neo-brutalistas y máquinas reactivas
│   ├── Root.tsx                 # Raíz de Remotion con registro de composiciones
│   ├── schema.ts                # Esquema de validación Zod
│   ├── types.ts                 # Interfaces TypeScript del sistema
│   └── style.css                # Estilos base neo-brutalistas y Tailwind
├── tests/
│   ├── test_schema.js           # Pruebas de esquemas JSON y Zod
│   ├── test_timestamps.js       # Pruebas de marcas de tiempo YouTube
│   ├── test_tts.py              # Pruebas de síntesis neural y WordBoundary
│   └── test_runner.js           # Ejecutor centralizado de pruebas
├── package.json
├── remotion.config.ts
├── tailwind.config.js
└── tsconfig.json
```

---

## 6. Ejemplo de Publicación en YouTube

El archivo `out/{slug}_capitulos.txt` generado automáticamente sigue las especificaciones oficiales de YouTube:

```text
00:00 El Descubrimiento Inesperado
00:16 La Frecuencia 1420 Megahercios
00:32 El Enigma Sin Resolver
```

Al pegar este bloque en la descripción del video en YouTube, la plataforma habilita automáticamente los capítulos interactivos en la barra de reproducción.
