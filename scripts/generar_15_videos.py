#!/usr/bin/env python3
"""
Orquestador Autónomo para la Producción de los 15 Documentales Largos (16:9, 1920x1080).
Carga el catálogo maestro de 15 documentales de src/data/guiones_largos/ (duración 6-8.5 min),
ejecutando desatendidamente el pipeline completo:
1. Validación Zod y Recursos
2. Síntesis Neural de Voz Clonada (Chatterbox + Faster-Whisper en GPU CUDA)
3. Renderizado Segmentado de Capítulos (Remotion 16:9)
4. Ensamble FFmpeg + BGM Continua + Ducking Sidechain (-14 LUFS)
5. Generación de Capítulos de YouTube y Metadatos con Hashtags
6. Control de Calidad Audiovisual (QA) con FFprobe y Snapshots
"""

import argparse
import io
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

ROOT_DIR = Path(__file__).resolve().parent.parent
GUION_PATH = ROOT_DIR / "src" / "data" / "guion.json"
GUIONES_LARGOS_DIR = ROOT_DIR / "src" / "data" / "guiones_largos"
SEGMENTS_DIR = ROOT_DIR / "out" / "segments"
OUT_DIR = ROOT_DIR / "out"


def obtener_python_cmd() -> str:
    venv_cand = ROOT_DIR.parent / "AIO" / "KidsAnimationStudio" / "voice-lab" / ".venv" / "Scripts" / "python.exe"
    if venv_cand.exists():
        return str(venv_cand.resolve())
    return sys.executable


def limpiar_segmentos():
    """Elimina segmentos MP4 previos para garantizar que cada capítulo sea fresco y exacto."""
    if SEGMENTS_DIR.exists():
        for f in SEGMENTS_DIR.glob("*.mp4"):
            try:
                f.unlink()
            except Exception:
                pass


def ejecutar_comando(cmd: list[str], descripcion: str) -> None:
    t0 = time.time()
    print(f"  [PASO] 🚀 {descripcion}...")
    res = subprocess.run(cmd, cwd=ROOT_DIR)
    if res.returncode != 0:
        raise RuntimeError(f"Fallo en paso '{descripcion}' con código {res.returncode}")
    print(f"  [PASO] ✅ {descripcion} finalizado en {time.time() - t0:.1f}s")


def cargar_catalogo_documentales() -> list[dict]:
    archivos = sorted(GUIONES_LARGOS_DIR.glob("doc_*.json"))
    if not archivos:
        raise FileNotFoundError(f"No se encontraron guiones largos en {GUIONES_LARGOS_DIR}")
    catalogo = []
    for f in archivos:
        with open(f, "r", encoding="utf-8") as fp:
            catalogo.append(json.load(fp))
    return catalogo


def verificar_video_largo_existente(slug: str) -> tuple[bool, float, float]:
    """Comprueba si el video ya existe y es un verdadero documental largo (>= 300s y >= 40 MB)."""
    video_mp4 = OUT_DIR / f"{slug}.mp4"
    meta_json = OUT_DIR / f"{slug}.metadata.json"
    cap_txt = OUT_DIR / f"{slug}_capitulos.txt"

    if not (video_mp4.exists() and meta_json.exists() and cap_txt.exists()):
        return False, 0.0, 0.0

    tamano_bytes = video_mp4.stat().st_size
    tamano_mb = tamano_bytes / (1024 * 1024)

    if tamano_mb < 40.0:  # Menos de 40MB indica un clip corto de prueba
        return False, 0.0, tamano_mb

    try:
        cmd = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{video_mp4}"'
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=ROOT_DIR)
        duracion = float(res.stdout.strip() or "0")
        if duracion >= 300.0:  # Al menos 5 minutos
            return True, duracion, tamano_mb
    except Exception:
        pass

    return False, 0.0, tamano_mb


def procesar_documental(indice: int, total: int, guion: dict) -> dict:
    meta = guion["meta"]
    slug = meta["slug"]
    titulo = meta["titulo"]
    capitulos = guion.get("capitulos", [])
    total_escenas = sum(len(c.get("escenas", [])) for c in capitulos)

    print(f"\n{'='*80}")
    print(f"🎬 DOCUMENTAL [{indice}/{total}]: {titulo}")
    print(f"   Slug: {slug} | Capítulos: {len(capitulos)} | Escenas: {total_escenas}")
    print(f"{'='*80}\n")

    t_inicio = time.time()

    # 1. Guardar como guion activo
    with open(GUION_PATH, "w", encoding="utf-8") as f:
        json.dump(guion, f, ensure_ascii=False, indent=2)

    # 2. Limpiar segmentos previos
    limpiar_segmentos()

    python_cmd = obtener_python_cmd()
    node_cmd = "node"

    # 3. Validar guion
    ejecutar_comando([node_cmd, "scripts/validar_guion.js"], "1. Validación Zod y Recursos")

    # 4. Síntesis TTS y alineación Faster-Whisper
    ejecutar_comando([python_cmd, "scripts/tts_engine.py", "--force"], "2. Síntesis Neural de Voz y Alineación (GPU CUDA)")

    # 5. Renderizado segmentado 16:9
    ejecutar_comando([node_cmd, "scripts/render_segments.js", "--force"], "3. Renderizado de Capítulos Remotion 16:9")

    # 6. Ensamble FFmpeg con BGM y ducking
    ejecutar_comando([python_cmd, "scripts/assemble_video.py"], "4. Ensamble FFmpeg y Ducking Sidechain (-14 LUFS)")

    # 7. Marcas de tiempo y metadatos YouTube
    ejecutar_comando([node_cmd, "scripts/generar_capitulos.js"], "5. Marcas de Tiempo y Metadatos YouTube")

    # Guardar copia sincronizada con duraciones y audio en guiones_largos
    archivos_cat = sorted(GUIONES_LARGOS_DIR.glob(f"doc_{indice:03d}_*.json"))
    if archivos_cat:
        try:
            shutil.copy2(GUION_PATH, archivos_cat[0])
        except Exception:
            pass

    # 8. Control de Calidad QA
    video_mp4 = OUT_DIR / f"{slug}.mp4"
    ejecutar_comando([node_cmd, "scripts/qa_video.js", str(video_mp4)], "6. QA Audiovisual e Inspección")

    duracion_proceso = time.time() - t_inicio
    tamano_mb = video_mp4.stat().st_size / (1024 * 1024) if video_mp4.exists() else 0

    print(f"\n🎉 [OK] Documental '{slug}' completado en {duracion_proceso/60:.2f} min ({tamano_mb:.2f} MB)")

    return {
        "slug": slug,
        "titulo": titulo,
        "duracion_min": round(duracion_proceso / 60, 2),
        "tamano_mb": round(tamano_mb, 2),
        "archivo": str(video_mp4),
    }


def main():
    parser = argparse.ArgumentParser(description="Generador batch de los 15 documentales largos")
    parser.add_argument("--force", action="store_true", help="Forzar regeneración de documentales ya existentes")
    parser.add_argument("--start", type=int, default=1, help="Índice 1-based inicial")
    parser.add_argument("--end", type=int, default=15, help="Índice 1-based final")
    args = parser.parse_args()

    catalogo = cargar_catalogo_documentales()
    total = len(catalogo)

    print(f"\n{'='*80}")
    print(f"🔥 PRODUCCIÓN MAESTRA: {total} DOCUMENTALES LARGOS (6 a 8.5 MINUTOS)")
    print(f"   Rango: [{args.start} a {args.end}] | Modo Resume: {not args.force}")
    print(f"{'='*80}\n")

    t_total_inicio = time.time()
    resultados = []

    for idx in range(args.start, min(args.end + 1, total + 1)):
        cfg = catalogo[idx - 1]
        slug = cfg["meta"]["slug"]

        es_valido, duracion_seg, tamano_mb = verificar_video_largo_existente(slug)

        if not args.force and es_valido:
            print(f"⚡ [{idx}/{total}] Documental ya producido y verificado: '{slug}' ({duracion_seg/60:.1f} min, {tamano_mb:.2f} MB). Omitiendo.")
            resultados.append({
                "slug": slug,
                "titulo": cfg["meta"]["titulo"],
                "duracion_min": round(duracion_seg / 60, 2),
                "tamano_mb": round(tamano_mb, 2),
                "archivo": str(OUT_DIR / f"{slug}.mp4"),
                "reutilizado": True,
            })
            continue

        exito = False
        for intento in range(1, 3):
            try:
                res = procesar_documental(idx, total, cfg)
                res["reutilizado"] = False
                resultados.append(res)
                exito = True
                break
            except Exception as e:
                print(f"\n⚠️ [INTENTO {intento}/2] Fallo al procesar documental {idx} ({slug}): {e}")
                if intento < 2:
                    print("  Reintentando en 5 segundos...")
                    time.sleep(5)
                else:
                    print(f"❌ Error persistente en documental {idx} ({slug}). Continuando con el siguiente...")
                    resultados.append({
                        "slug": slug,
                        "titulo": cfg["meta"]["titulo"],
                        "duracion_min": 0,
                        "tamano_mb": 0,
                        "archivo": "",
                        "error": str(e),
                        "reutilizado": False,
                    })

    tiempo_total_min = (time.time() - t_total_inicio) / 60
    print(f"\n{'='*80}")
    print(f"🏆 PRODUCCIÓN FINALIZADA: {len(resultados)} DOCUMENTALES LARGOS LISTOS EN /out")
    print(f"⏱️ Tiempo total invertido: {tiempo_total_min:.2f} minutos")
    print(f"{'='*80}\n")

    print(f"{'No.':<4} | {'Slug':<44} | {'MB':<8} | {'Minutos':<8} | {'Estado'}")
    print("-" * 75)
    for i, r in enumerate(resultados, start=1):
        estado = "Reutilizado" if r.get("reutilizado") else "Generado"
        print(f"{i:<4} | {r['slug']:<44} | {r['tamano_mb']:<8.2f} | {r['duracion_min']:<8.2f} | {estado}")
    print("\nTodos los videos finales, metadatos y marcas de tiempo están en /out.\n")


if __name__ == "__main__":
    main()
