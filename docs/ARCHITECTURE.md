# Arquitectura Técnica — AutoPNGTuber-LongVideos

## 1. Visión General del Sistema

**AutoPNGTuber-LongVideos** es un generador autónomo de producciones audiovisuales narrativas largas para **YouTube en formato panorámico 16:9 (1920 × 1080 @ 30 FPS)**.

A diferencia del proyecto de Shorts (orientado a formato vertical 9:16 y secuencias de corta duración), este sistema está diseñado para manejar metrajes extensos (**8 a 10 minutos** o configurables) con una estructura narrativa dividida en **capítulos y escenas**, renderizado segmentado con tolerancia a fallos, música continua sin cortes bruscos, compresión sidechain (audio ducking) y generación automática de marcas de tiempo para YouTube.

```
+-------------------------------------------------------------------------+
|                           PIPELINE MASTER                               |
|                         scripts/pipeline.js                             |
+-------------------------------------------------------------------------+
        |
        +---> 1. VALIDACIÓN (scripts/validar_guion.js)
        |        - Validación Zod del esquema GuionLargoCompleto
        |        - Verificación de catálogos (poses, expresiones, props)
        |        - Chequeo de archivos en disco (SFX, BGM)
        |
        +---> 2. SÍNTESIS DE VOZ Y ALINEACIÓN (scripts/tts_engine.py)
        |        - Chatterbox TTS en GPU (CUDA) con voz clonada (alex.conds.pt)
        |        - Normalización fonética de números (scripts/normalizador_numeros.py)
        |        - Pipeline v3_sentence_tailcut + alineación palabra por palabra con Faster-Whisper
        |        - Caché determinista SHA-256 (.tts_cache.json)
        |        - Inyección de 'duracionSegundos' y 'palabras' en guion.json
        |
        +---> 3. RENDERIZADO SEGMENTADO (scripts/render_segments.js)
        |        - Remotion CLI renderiza cada capítulo como segmento independiente
        |        - Detección de segmentos previos válidos (tolerancia y reanudación)
        |        - Salida: out/segments/capitulo_{n}.mp4 (1920x1080 @ 30fps)
        |
        +---> 4. ENSAMBLE, MEZCLA Y DUCKING (scripts/assemble_video.py)
        |        - Concat demuxer de FFmpeg para ensamblar los capítulos
        |        - Pista de música ambiental continua (sin cortes en cambios de bloque)
        |        - Sidechain compression: atenúa la música cuando la voz suena
        |        - Normalización broadcast YouTube (-14 LUFS / -1.5 dB True Peak)
        |        - Salida: out/{slug}.mp4
        |
        +---> 5. CAPÍTULOS Y METADATOS YOUTUBE (scripts/generar_capitulos.js)
        |        - Medición precisa de duración real de cada segmento con ffprobe
        |        - Formateo de marcas de tiempo compatibles con YouTube (00:00 ...)
        |        - Exportación de {slug}_capitulos.txt y {slug}.metadata.json
        |
        +---> 6. CONTROL DE CALIDAD Y SNAPSHOTS (scripts/qa_video.js)
                 - Validación técnica con ffprobe (1920x1080, 30fps, h264, aac)
                 - Análisis de volumen con volumedetect
                 - Extracción de fotogramas clave para inspección visual
```

---

## 2. Aislamiento y Relación con AutoPNGTuber

Este proyecto reside en su propio espacio de trabajo:
`c:\Users\villa\GIT DESKTOP\AutoPNGTuber-LongVideos`.

### Principio de No Invasión
- **Cero modificaciones en el repositorio original**: `AutoPNGTuber` no sufre ninguna alteración, instalación ni cambio de configuración.
- **Independencia de dependencias**: `AutoPNGTuber-LongVideos` posee su propio `package.json`, `tsconfig.json`, `remotion.config.ts` y árbol de `node_modules`.

### Componentes Reutilizados vs. Desarrollados

| Componente | Origen | Adaptación / Transformación para Widescreen 16:9 |
| :--- | :--- | :--- |
| **Biblioteca de Poses y Props** | AutoPNGTuber (`src/stickman/`) | Portada y ampliada con máquinas reactivas multi-estado (`celluloid_press`, `bakelizer_autoclave`, `paperclip_polymer_chain`, `mesa_quimica_celuloide`). |
| **Rig Esquelético IK/FK y 2.5D** | Nuevo (`skeletalRig.ts`, `Stickman.tsx`) | Solver IK analítico de 2 huesos, interpolación continua entre poses, cabeza 2.5D con parallax, torso volumétrico con luz de recorte (`colorRim`) y modo holograma (`esHolograma`). |
| **Composición y Micro-Planos** | Nuevo (`CameraRig.tsx`, `Scene.tsx`) | Cortes de cámara (`general`, `plano_medio`, `primer_plano`, `sobre_hombro`, `detalle_mano`), desenfoque de fondo DoF (`blurFondo`), siluetas OTS e insertos macro de manos. |
| **Cotas Diegéticas y Partículas** | Nuevo (`DiegeticCallout.tsx`, `ParticleEmitter.tsx`) | Cotas vectoriales ancladas a objetos con margen seguro, trayectorias en el suelo y emisores de partículas balísticas + rayos volumétricos. |
| **Escenarios Widescreen** | Nuevo (`NarrativeStage16x9.tsx`) | Fondos panorámicos SVG con perspectiva horizontal, monitores de laboratorio en extremos y campo estelar amplio. |
| **Infografías Widescreen** | Nuevo (`InfographicCard.tsx`) | Tarjetas de datos, comparativas y cifras científicas flotantes en laterales o modo compacto. |
| **Pantalla Dividida** | Nuevo (`SplitScreen.tsx`) | Layouts comparativos duales con división neo-brutalista. |
| **Subtítulos 16:9** | Adaptado (`WordSubtitles.tsx`) | Franja inferior centrada (`y ≈ 920-1020`), bloques de 4-5 palabras con jerarquía tipográfica y resaltado en `#FFE600`. |
| **Header de Capítulo** | Nuevo (`ChapterHeader.tsx`) | Insignia superior con indicador de progreso de capítulo y escena. |
| **Pipeline Segmentado** | Nuevo (`render_segments.js`) | Render por capítulos independientes para mitigar uso de memoria y permitir reanudación instantánea. |
| **Ensamble y Ducking** | Nuevo (`assemble_video.py`) | FFmpeg sidechain compression y normalización -14 LUFS para YouTube. |
| **Marcas de Tiempo** | Nuevo (`generar_capitulos.js`) | Cálculo basado en la duración real de los segmentos MP4 finales. |

---

## 3. Renderizado Segmentado vs. Monolítico

Un video de 8 a 10 minutos a 30 FPS representa **14,400 a 18,000 fotogramas**. Renderizar este volumen en un único proceso monolítico de Chromium/Remotion presenta riesgos severos:
1. Saturación progresiva de memoria RAM.
2. Si ocurre un fallo en el minuto 9, todo el render previo se pierde.
3. Imposibilidad de paralelizar o actualizar únicamente un capítulo corregido.

### Solución Implementada:
El sistema define una composición dinámica para cada capítulo: `Capitulo-{n}`.
- Cada capítulo se renderiza a `out/segments/capitulo_{n}.mp4`.
- El script de ensamble comprueba la validez del archivo. Si ya fue renderizado y no hubo cambios, se reutiliza en **0.1 segundos**.
- La concatenación final toma menos de 3 segundos mediante `ffmpeg -f concat -c copy`.

---

## 4. Pipeline de Audio y Ducking Profesional

### Síntesis Neural Local (`tts_engine.py` + `normalizador_numeros.py`)
Utiliza **Chatterbox TTS** sobre CUDA condicionado con `public/voices/alex.conds.pt` y alineación forzada con **Faster-Whisper** (`float16`):
1. Normalización fonética previa de cifras, años y decimales a palabras en español para evitar tropiezos de dicción.
2. Segmentación por cláusulas sintácticas (`v3_sentence_tailcut`), compactación de pausas internas (>280 ms a 150 ms) y poda limpia de colas residuales.
3. Timings exactos de inicio y fin por palabra medidos en milisegundos (`inicioMs`, `finMs`) mediante Faster-Whisper.
4. Caché SHA-256 por escena (`.tts_cache.json`) para reutilización instantánea si el texto no cambió.

### Mezcla Continua y Sidechain Ducking (`assemble_video.py`)
Para evitar que la música de fondo se reinicie abruptamente en cada corte de capítulo, la pista ambiental (`bgm.mp3`) se mezcla sobre el video ya ensamblado mediante un filtergraph de FFmpeg:
```text
[1:a]volume=0.12[bgm_raw];
[bgm_raw][0:a]sidechaincompress=threshold=0.03:ratio=5:attack=40:release=350[bgm_ducked];
[0:a][bgm_ducked]amix=inputs=2:duration=first:dropout_transition=2[a_mixed];
[a_mixed]loudnorm=I=-14:TP=-1.5:LRA=11[a_out]
```
- Cuando el narrador habla (`[0:a]`), la música (`[bgm_raw]`) se comprime automáticamente en volumen.
- Durante pausas y silencios dramáticos, la música se eleva suavemente.
- El filtro `loudnorm` normaliza el resultado a `-14 LUFS`, estándar estricto de YouTube.

---

## 5. Control de Calidad Automático (`qa_video.js`)

Cada exportación pasa por una batería de inspección automática:
- **ffprobe**: Valida resolución 1920x1080, relación 16:9, códec h264, audio aac y 30 FPS.
- **volumedetect**: Comprueba que el volumen promedio no esté silenciado y que el pico no sature (`max_volume <= 0.0 dB`).
- **Extracción de Snapshots**: Extrae 4 fotogramas clave en `out/snapshots/` (intro, desarrollo, clímax y conclusión) para auditoría visual rápida.

---

## 6. Motor de Acción Narrativa y Sincronización con la Locución

Para evitar el efecto de presentación de diapositivas y priorizar la acción narrativa sincronizada con la voz:

### 6.1 Anclaje Temporal por Palabras (`actionSequences.ts`)
- Todos los actores de una escena (`PasoAccion`, `PasoObjeto`, `ObjetoEscena`, `ElementoNarrativo`, `InfografiaConfig`, `EventoSfx` y `FocoCamaraKeyframe`) admiten tres modos de sincronización resueltos por `resolveTimeRangeFrames` y `resolvePointFrame`:
  1. **Anclaje léxico (`desdePalabra` / `hastaPalabra`)**: Busca subcadenas normalizadas (sin tildes ni puntuación) en las marcas `palabras[]` de Faster-Whisper (`inicioMs` / `finMs`).
  2. **Segundos absolutos (`inicioSegundos` / `finSegundos`)**: Tiempos relativos al inicio de la escena.
  3. **Progreso normalizado (`inicioProgreso` / `finProgreso` en `[0, 1]`)**: Fallback porcentual sobre la duración total de la escena.

### 6.2 Rig Esquelético IK/FK de 2 Huesos y Articulación Continua (`skeletalRig.ts`, `composites.ts`, `Stickman.tsx`)
- `skeletalRig.ts` extrae las coordenadas articulares (`neck`, `hip`, `shoulderL/R`, `elbowL/R`, `wristL/R`, `kneeL/R`, `ankleL/R`) de cualquier pose del catálogo y aplica interpolación continua entre `prevPoseId` y `poseId` mediante `interpolateSkeletalPose` y el solver analítico de 2 huesos `solveTwoBoneIK`.
- El personaje cuenta con:
  - **Cabeza 2.5D (`lookOffset`)**: Desplazamiento interno del rostro y rasgos faciales hacia el punto de atención.
  - **Torso Volumétrico y Luz de Recorte (`colorRim`)**: Trapecio anatómico con borde iluminado direccional, articulaciones circulares en codos/rodillas y sombra proyectada en el suelo calculada según el centro de gravedad de los pies.
  - **Simulación Holográfica (`esHolograma: true`)**: Renderizado translúcido en cian (`#38BDF8`) con *scanlines* y parpadeo cuántico para representar proyecciones mentales, hipótesis o escenarios futuros.
  - **Modos Procedurales**: `"caminar"` (ciclo de zancada con flexión de rodilla/tobillo), `"manipular"` (alcance IK hacia el objeto activo), `"esfuerzo"` (tensión y vibración muscular) y `"agachar_recoger"`.

### 6.3 Objetos Multi-Estado y Props Reactivos (`SceneObject.tsx`, `propsLibrary.ts`)
- `SceneObject` evalúa una secuencia de `pasos: PasoObjeto[]` interpolando `posicion`, `escala`, `rotacion` y `opacidad`, y conmutando dinámicamente `propId` o `estado`.
- `PropDefinition.animatedSvg(frame, stepProgress, state)` recibe el progreso normalizado del paso activo (`0 → 1`) y el `estado` semántico, permitiendo máquinas con partes móviles progresivas (`celluloid_press`, `bakelizer_autoclave`, `mesa_quimica_celuloide`, `paperclip_polymer_chain`).

### 6.4 Dirección de Micro-Planos, Profundidad de Campo (DoF) e Insertos (`CameraRig.tsx`, `Scene.tsx`)
- `planos: PlanoCamara[]` divide cada escena en micro-cortes sincronizados con la voz (`desdePalabra`/`hastaPalabra`):
  - `"general"`, `"plano_medio"`, `"primer_plano"`: Ajustan encuadre (`x`, `y`, `zoom`) y aplican desenfoque óptico gaussiano (`blurFondo` en píxeles) sobre el escenario de fondo para separar al sujeto.
  - `"sobre_hombro"` (`OverTheShoulderForeground`): Superpone en primer plano una silueta oscura desenfocada de cabeza y hombro en el borde izquierdo o derecho para crear profundidad cinematográfica.
  - `"detalle_mano"` (`HandInsertOverlay`): Muestra una ventana macro neo-brutalista con manos mecánicas articuladas ejecutando acciones específicas (`"verter_acido"`, `"prensar_palanca"`, `"estirar_cadena"`, `"girar_valvula"`, `"tocar_esfera"`).
- `eventosSfx: EventoSfx[]`: Dispara efectos sonoros puntuales (`<Sequence from={triggerFrame}>`) sincronizados con impactos, explosiones o válvulas a mitad de escena.

### 6.5 Cotas Vectoriales Diegéticas y Emisores de Partículas (`DiegeticCallout.tsx`, `ParticleEmitter.tsx`)
- `cotasVectoriales: CotaVectorial[]`: Reemplazan las tarjetas estáticas tipo diapositiva por líneas de medición punteadas animadas que nacen en la máquina (`origenX`, `origenY`) y terminan en una etiqueta técnica (`destinoX`, `destinoY`, auto-contenida en el margen seguro `X ∈ [420, 1140]`, `Y ∈ [220, 720]` para evitar recortes durante zooms).
- `trayectoriaSuelo`: Dibuja arcos de proyección tácticos con marcadores de impacto en el suelo cuando un personaje evalúa un movimiento o hipótesis.
- `emisoresParticulas: EmisorParticulas[]` + `iluminacionVolumetrica`: Generador determinista de partículas con física balística (`"chispas_quimicas"`, `"gotas_acido"`, `"vapor_presion"`, `"eslabones_polimero"`, `"fragmentos_marfil"`) y haces de luz atmosférica (`LightRaysOverlay`).
