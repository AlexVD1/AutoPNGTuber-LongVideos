# Flujo de Trabajo — AutoPNGTuber-LongVideos

Guía operativa paso a paso para producir episodios largos de YouTube de principio a fin.

---

## 1. Comandos Rápidos

| Acción | Comando | Descripción |
| :--- | :--- | :--- |
| **Pipeline Completo** | `npm run render` | Ejecuta validación, síntesis TTS, renderizado por capítulos, ensamble FFmpeg, marcas de tiempo y QA. |
| **Validar Guion** | `npm run validar` | Comprueba tipos Zod, catálogos, dicción fonética y referencias sin renderizar. |
| **Generar Audios TTS** | `npm run tts` | Sintetiza voz clonada con Chatterbox CUDA + Faster-Whisper y actualiza `guion.json`. |
| **Renderizar Capítulos** | `npm run render:chapters` | Renderiza cada capítulo como segmento independiente en `out/segments/`. |
| **Ensamblar Video** | `npm run assemble` | Concatena capítulos con FFmpeg, integra BGM continua y audio ducking. |
| **Marcas de Tiempo** | `npm run capitulos` | Genera `out/{slug}_capitulos.txt` y metadatos SEO de YouTube. |
| **Control de Calidad** | `npm run qa` | Comprueba resolución, FPS, loudness y extrae snapshots. |
| **Previsualización en Vivo**| `npm run dev` | Abre Remotion Studio en `http://localhost:3000`. |
| **Suite de Pruebas** | `npm test` | Ejecuta los tests automatizados de esquema, timestamps y TTS. |

---

## 2. Flujo de Producción de un Nuevo Episodio

### Paso 1: Redactar o Cargar el Guion ($\ge$ 8:15 min para Monetización Mid-Roll)
1. Abre `src/data/guion.json`.
2. Define `meta` con `duracionObjetivo: [495, 570]` y `voz: "alex.conds.pt"`.
3. Estructura la historia en **7 a 8 capítulos** (`capitulos`) y **14 a 16 escenas** (`escenas`), asegurando entre **88 y 105 palabras habladas por escena** (**1,320 a 1,500 palabras totales** en la suma de `escenas[].texto`) para superar con holgura los **8:15 minutos (495+ segundos)** tras el recorte de silencios de Chatterbox.
4. En cada escena, configura la dirección cinematográfica sincronizada con `desdePalabra` / `hastaPalabra`:
   - `planos`: 2 a 4 cortes por escena (`general`, `plano_medio`, `primer_plano`, `sobre_hombro`, `detalle_mano`) con `blurFondo`.
   - `personajes`: Secuencias `acciones[].pasos[]` con modos procedurales (`caminar`, `manipular`, `esfuerzo`), `colorRim`, y `esHolograma: true` + `trayectoriaSuelo` para hipótesis.
   - `objetos`: Props y máquinas multi-estado con `pasos[]`.
   - `cotasVectoriales` y `emisoresParticulas`: Mediciones técnicas en margen seguro (`X ∈ [420, 1140]`) y partículas físicas.
5. Ejecuta:
   ```bash
   npm run validar
   ```

### Paso 2: Generar Voz y Sincronía
Ejecuta:
```bash
npm run tts
```
- Sintetiza la narración de cada escena.
- Mide la duración exacta de cada archivo de audio.
- Calcula las marcas de tiempo para cada palabra.
- Actualiza automáticamente `duracionSegundos` y `palabras` en `src/data/guion.json`.

### Paso 3: Renderizado y Ensamble (Automatizado)
Ejecuta:
```bash
npm run render
```
El pipeline maestro ejecutará automáticamente:
1. Renderizado de los capítulos a `out/segments/capitulo_{n}.mp4`.
2. Detección y reutilización de capítulos ya completados.
3. Ensamble con FFmpeg preservando audio de voz y video.
4. Mezcla de música de fondo continua con compresión sidechain (ducking).
5. Normalización de volumen a estándar broadcast (-14 LUFS).
6. Generación de marcas de tiempo compatibles con YouTube.
7. Extracción de fotogramas clave en `out/snapshots/`.
8. Verificación de QA.

### Paso 4: Publicación en YouTube
En la carpeta `out/` encontrarás:
1. **`{slug}.mp4`**: El archivo de video final listo para subir a YouTube.
2. **`{slug}_capitulos.txt`**: Marcas de tiempo formateadas para pegar directamente en la descripción de YouTube.
3. **`{slug}.metadata.json`**: Metadatos completos con título optimizado, descripción estructurada, fuentes y etiquetas.
4. **`snapshots/`**: Fotogramas para revisar el encuadre o usarlos como base para la miniatura.
