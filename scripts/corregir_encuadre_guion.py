#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Corrección Quirúrgica de Encuadres y Posicionamiento de Stickman / Props / Cámaras.
Garantiza que el Stickman esté 100% visible dentro del encuadre 16:9 con sus pies en la línea del suelo.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUION_PATH = ROOT / "src" / "data" / "guion.json"

def corregir_encuadres():
    with open(GUION_PATH, "r", encoding="utf-8") as f:
        guion = json.load(f)

    for cap in guion.get("capitulos", []):
        for esc in cap.get("escenas", []):
            has_info = bool(esc.get("infografia"))

            # 1. Corregir personajes
            for p in esc.get("personajes", []):
                if "posicion" in p and isinstance(p["posicion"], dict):
                    p["posicion"]["y"] = 50
                for ac in p.get("acciones", []):
                    for paso in ac.get("pasos", []):
                        if "posicion" in paso and isinstance(paso["posicion"], dict):
                            paso["posicion"]["y"] = 50
                        if "desdePosicion" in paso and isinstance(paso["desdePosicion"], dict):
                            paso["desdePosicion"]["y"] = 50
                        if "trayectoriaSuelo" in paso and isinstance(paso["trayectoriaSuelo"], dict):
                            paso["trayectoriaSuelo"]["y"] = 790

            # 2. Corregir objetos
            for obj in esc.get("objetos", []):
                if "posicion" in obj and isinstance(obj["posicion"], dict):
                    if has_info:
                        obj["posicion"]["x"] = -105
                        obj["posicion"]["y"] = 40
                    else:
                        obj["posicion"]["y"] = 40
                for paso in obj.get("pasos", []):
                    if "posicion" in paso and isinstance(paso["posicion"], dict):
                        if has_info:
                            paso["posicion"]["x"] = -105
                        paso["posicion"]["y"] = 40
                    if "desdePosicion" in paso and isinstance(paso["desdePosicion"], dict):
                        if has_info:
                            paso["desdePosicion"]["x"] = -105
                        paso["desdePosicion"]["y"] = 40

            # 3. Corregir planos de cámara
            for pl in esc.get("planos", []):
                tipo = pl.get("tipo", "general")
                cur_x = pl.get("x", 0)

                if tipo == "general":
                    pl["x"] = 0
                    pl["y"] = 0
                    pl["zoom"] = 1.0
                    pl["blurFondo"] = 0

                elif tipo == "primer_plano":
                    pl["zoom"] = 1.35
                    pl["blurFondo"] = 5.0
                    pl["y"] = 5
                    pl["x"] = -220 if cur_x < 0 else 220

                elif tipo == "plano_medio":
                    if has_info:
                        pl["zoom"] = 1.08
                        pl["blurFondo"] = 1.5
                        pl["x"] = -80
                        pl["y"] = 15
                    else:
                        pl["zoom"] = 1.20
                        pl["blurFondo"] = 2.5
                        pl["y"] = 15
                        pl["x"] = -150 if cur_x < 0 else 150

                elif tipo == "sobre_hombro":
                    pl["zoom"] = 1.25
                    pl["blurFondo"] = 3.5
                    pl["y"] = 15
                    pl["x"] = -130 if cur_x < 0 else 130

                elif tipo == "detalle_mano":
                    pl["zoom"] = 1.30
                    pl["blurFondo"] = 6.5
                    pl["x"] = 0
                    pl["y"] = 0

            # 4. Corregir cotas vectoriales
            for cota in esc.get("cotasVectoriales", []):
                cota["origenY"] = 580
                cota["destinoY"] = 240
                cota["destinoX"] = 960

    with open(GUION_PATH, "w", encoding="utf-8") as f:
        json.dump(guion, f, ensure_ascii=False, indent=2)

    print("[CORRECCION] [OK] Posiciones de Stickman, objetos, planos y cotas corregidas al 100%.")

if __name__ == "__main__":
    corregir_encuadres()
