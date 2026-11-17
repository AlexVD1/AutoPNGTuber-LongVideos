#!/usr/bin/env python3
"""
Generador de Guiones Largos Expandidos (6.5 a 8.5 minutos).
Reescribe doc_004 a doc_015 con 6 capítulos y 12 escenas detalladas por documental,
alcanzando entre 7,500 y 9,000 caracteres de texto narrativo por documental
(equivalente a 420-500 segundos / 7-8.5 minutos de locución en Chatterbox TTS).
"""

import json
import io
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

ROOT_DIR = Path(__file__).resolve().parent.parent
GUIONES_DIR = ROOT_DIR / "src" / "data" / "guiones_largos"


def actualizar_guion(numero_doc: str, capitulos_nuevos: list, duracion_objetivo: list = [420, 500]):
    archivo = list(GUIONES_DIR.glob(f"doc_{numero_doc}_*.json"))[0]
    with open(archivo, "r", encoding="utf-8") as f:
        data = json.load(f)

    data["meta"]["duracionObjetivo"] = duracion_objetivo
    data["capitulos"] = capitulos_nuevos

    # Limpiar duraciones precalculadas residuales para permitir síntesis fresca
    for c in data["capitulos"]:
        c.pop("duracionSegundos", None)
        for s in c.get("escenas", []):
            s.pop("duracionSegundos", None)
            s.pop("audio", None)
            s.pop("palabras", None)
            s.pop("palabrasAlineadas", None)

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    total_chars = sum(len(s.get("texto", "")) for c in capitulos_nuevos for s in c.get("escenas", []))
    total_scenes = sum(len(c.get("escenas", [])) for c in capitulos_nuevos)
    print(f"✅ {archivo.name}: {len(capitulos_nuevos)} caps, {total_scenes} escenas, {total_chars} chars (~{total_chars/18.5/60:.1f} min)")


if __name__ == "__main__":
    print("Módulo base de redacción listo.")
