#!/usr/bin/env python3
"""
Ensamblador y Mezclador Audiovisual Final con FFmpeg.
- Concatena los segmentos de video de cada capítulo.
- Integra música de fondo ambiental continua en loop (sin cortes entre capítulos).
- Aplica audio ducking dinámico (sidechain compression) para atenuar la música cuando habla el narrador.
- Normaliza el volumen según estándares de YouTube (-14 LUFS).
- Genera el archivo MP4 final en 1920x1080 H.264 + AAC.
"""

import argparse
import io
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

ROOT_DIR = Path(__file__).resolve().parent.parent
GUION_PATH = ROOT_DIR / "src" / "data" / "guion.json"
SEGMENTS_DIR = ROOT_DIR / "out" / "segments"
OUT_DIR = ROOT_DIR / "out"


def limpiar_slug(texto: str) -> str:
    import unicodedata
    if not texto:
        return "long_video"
    norm = unicodedata.normalize("NFD", texto)
    clean = "".join(c for c in norm if unicodedata.category(c) != "Mn")
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", clean).strip("_").lower()
    return slug[:50] or "long_video"


def ensamblar_video(guion_path: Path, sin_ducking: bool = False):
    import re
    if not guion_path.exists():
        print(f"[ENSAMBLE] ❌ Guion no encontrado en {guion_path}")
        sys.exit(1)

    with open(guion_path, "r", encoding="utf-8") as f:
        guion = json.load(f)

    meta = guion.get("meta", {})
    slug = meta.get("slug") or limpiar_slug(meta.get("titulo", "video_largo"))
    capitulos = guion.get("capitulos", [])

    if not capitulos:
        print("[ENSAMBLE] ❌ No hay capítulos para ensamblar.")
        sys.exit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    salida_final_mp4 = OUT_DIR / f"{slug}.mp4"

    # 1. Comprobar existencia de todos los segmentos
    archivos_segmentos = []
    for cap in capitulos:
        num = cap.get("numero")
        seg_file = SEGMENTS_DIR / f"capitulo_{num}.mp4"
        if not seg_file.exists():
            print(f"[ENSAMBLE] ❌ Falta el archivo de segmento: {seg_file}")
            print(f"            Ejecuta primero: node scripts/render_segments.js")
            sys.exit(1)
        archivos_segmentos.append(seg_file)

    print(f"\n[ENSAMBLE] 🎞️  Ensamblando {len(archivos_segmentos)} capítulos para \"{slug}\"...")

    # 2. Crear archivo de lista concat para FFmpeg
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8") as concat_file:
        for seg in archivos_segmentos:
            # Escapar rutas para FFmpeg concat demuxer
            clean_path = str(seg.resolve()).replace("\\", "/")
            concat_file.write(f"file '{clean_path}'\n")
        concat_list_path = Path(concat_file.name)

    temp_concat_mp4 = OUT_DIR / f"{slug}_concat_temp.mp4"

    try:
        # Paso A: Concatenar rápidamente los MP4 con concat demuxer
        print("[ENSAMBLE] 🔗 Concatenando pistas de video y voz de capítulos...")
        cmd_concat = [
            "ffmpeg",
            "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", str(concat_list_path),
            "-c", "copy",
            str(temp_concat_mp4),
        ]
        res = subprocess.run(cmd_concat, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if res.returncode != 0:
            print(f"[ENSAMBLE] ❌ Error al concatenar segmentos:\n{res.stderr}")
            sys.exit(1)

        # Paso B: Integración de música de fondo continua + ducking
        bgm_rel = meta.get("musicaPrincipal", "bgm/bgm.mp3")
        bgm_path = ROOT_DIR / "public" / bgm_rel
        volumen_bgm = meta.get("volumenMusica", 0.12)

        if not bgm_path.exists():
            # Buscar cualquier mp3 en public/bgm/
            candidatos_bgm = list((ROOT_DIR / "public" / "bgm").glob("*.mp3"))
            if candidatos_bgm:
                bgm_path = candidatos_bgm[0]

        if bgm_path.exists() and not sin_ducking:
            print(f"[ENSAMBLE] 🎵 Integrando BGM continua ({bgm_path.name}) con Sidechain Ducking...")
            # Filtergraph para sidechain ducking profesional:
            # 1. BGM en loop atenuada inicialmente por volumen base.
            # 2. Sidechain compression: cuando la voz [0:a] suena, la música se comprime automáticamente.
            # 3. amix junta ambas pistas sin saturación.
            # 4. loudnorm normaliza el master a -14 LUFS para YouTube.
            filter_complex = (
                "[0:a]asplit=2[vox_sc][vox_main];"
                f"[1:a]volume={volumen_bgm}[bgm_raw];"
                "[bgm_raw][vox_sc]sidechaincompress="
                "threshold=0.03:ratio=5:attack=40:release=350[bgm_ducked];"
                "[vox_main][bgm_ducked]amix=inputs=2:duration=first:dropout_transition=2:weights='1 1'[a_mixed];"
                "[a_mixed]loudnorm=I=-14:TP=-1.5:LRA=11[a_out]"
            )

            cmd_mix = [
                "ffmpeg",
                "-y",
                "-i", str(temp_concat_mp4),
                "-stream_loop", "-1",
                "-i", str(bgm_path),
                "-filter_complex", filter_complex,
                "-map", "0:v",
                "-map", "[a_out]",
                "-c:v", "copy",
                "-c:a", "aac",
                "-b:a", "192k",
                "-shortest",
                str(salida_final_mp4),
            ]
        else:
            print("[ENSAMBLE] ℹ️  Generando video final sin mezcla adicional de música...")
            cmd_mix = [
                "ffmpeg",
                "-y",
                "-i", str(temp_concat_mp4),
                "-c:v", "copy",
                "-c:a", "aac",
                "-b:a", "192k",
                str(salida_final_mp4),
            ]

        res_mix = subprocess.run(cmd_mix, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if res_mix.returncode != 0:
            print(f"[ENSAMBLE] ⚠️  Fallo en mezcla avanzada. Reintentando ensamble directo sin ducking...")
            cmd_fallback = [
                "ffmpeg",
                "-y",
                "-i", str(temp_concat_mp4),
                "-c", "copy",
                str(salida_final_mp4),
            ]
            subprocess.run(cmd_fallback, check=True)

        print(f"\n[ENSAMBLE] ✅ Video final ensamblado exitosamente:")
        print(f"           📁 {salida_final_mp4.resolve()}")

    finally:
        concat_list_path.unlink(missing_ok=True)
        temp_concat_mp4.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description="Ensamblador de video final con FFmpeg")
    parser.add_argument("--script", default=str(GUION_PATH), help="Ruta al guion JSON")
    parser.add_argument("--no-ducking", action="store_true", help="Omitir compresión sidechain")
    args = parser.parse_args()

    ensamblar_video(Path(args.script), args.no_ducking)


if __name__ == "__main__":
    main()
