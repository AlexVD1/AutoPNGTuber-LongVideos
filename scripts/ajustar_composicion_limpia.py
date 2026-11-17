# scripts/ajustar_composicion_limpia.py
import json, re

# 1. Limpiar textos redundantes de los props en propsLibrary.ts
props_path = "src/stickman/propsLibrary.ts"
with open(props_path, "r", encoding="utf-8") as f:
    text = f.read()

# En alula_morfologia_activa: quitar los carteles de texto flotantes dentro del SVG
# Dejar solo el ala limpia con el álula articulada y el chorro verde
text = re.sub(
    r'<g transform="translate\(26, -20\)">[\s\S]*?</g>\s*</g>\s*<!-- 4\. CHORRO',
    '</g>\n        <!-- 4. CHORRO',
    text
)
text = re.sub(
    r'<g transform="translate\(12, -30\)">[\s\S]*?</g>',
    '',
    text
)

# En pluma_aguila_metamaterial: quitar el cartelito "RAQUIS ASIMÉTRICO" del prop para que no colisione
text = re.sub(
    r'<!-- Rótulo anatómico -->[\s\S]*?</g>\s*</g>`',
    '</g>`',
    text
)

with open(props_path, "w", encoding="utf-8") as f:
    f.write(text)
print("Cartelitos flotantes redundantes eliminados de los props!")

# 2. Ajustar posiciones espaciales en guion.json
with open("src/data/guion.json", "r", encoding="utf-8") as f:
    guion = json.load(f)

# Cap 2 Esc 4: Separación perfecta de la paloma y el ala anatómica
for c in guion["capitulos"]:
    if c["numero"] == 2:
        for e in c["escenas"]:
            if e["id"] == 4:
                for obj in e.get("objetos", []):
                    if obj["propId"] == "paloma_aterrizaje_turbulento":
                        obj["posicion"] = {"x": -180, "y": -10}
                        obj["escala"] = 0.9
                    elif obj["propId"] == "alula_morfologia_activa":
                        obj["posicion"] = {"x": 190, "y": 80}
                        obj["escala"] = 0.95

# Cap 3 Esc 5: Separación limpia entre la pluma y la microestructura
for c in guion["capitulos"]:
    if c["numero"] == 3:
        for e in c["escenas"]:
            if e["id"] == 5:
                for obj in e.get("objetos", []):
                    if obj["propId"] == "pluma_aguila_metamaterial":
                        obj["posicion"] = {"x": -110, "y": 0}
                        obj["escala"] = 0.95
                    elif obj["propId"] == "pluma_microestructura_velcro":
                        obj["posicion"] = {"x": 160, "y": 140}
                        obj["escala"] = 0.95

with open("src/data/guion.json", "w", encoding="utf-8") as f:
    json.dump(guion, f, indent=2, ensure_ascii=False)

print("Coordenadas espaciales pulidas en guion.json!")
