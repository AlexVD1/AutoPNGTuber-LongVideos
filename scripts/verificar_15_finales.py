import json
import subprocess
from pathlib import Path

out_dir = Path("out")
guiones_dir = Path("src/data/guiones_largos")

print(f"{'No.':<3} | {'Titulo / Slug':<48} | {'Duracion':<14} | {'Tamano':<10} | {'Caps':<5} | {'TXT':<4} | {'JSON':<4}")
print("-" * 95)

total_dur = 0
guiones = sorted(guiones_dir.glob("doc_*.json"))

for i, gpath in enumerate(guiones, 1):
    with open(gpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    slug = data["meta"]["slug"]
    video = out_dir / f"{slug}.mp4"
    cap_txt = out_dir / f"{slug}_capitulos.txt"
    meta_json = out_dir / f"{slug}.metadata.json"

    dur_str = "N/A"
    size_str = "N/A"
    if video.exists():
        size_mb = video.stat().st_size / (1024 * 1024)
        size_str = f"{size_mb:.1f} MB"
        cmd = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{video}"'
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        try:
            d = float(res.stdout.strip())
            total_dur += d
            m = int(d // 60)
            s = int(d % 60)
            dur_str = f"{m}m {s:02d}s ({d:.0f}s)"
        except Exception:
            dur_str = "Error"

    num_caps = len(data.get("capitulos", []))
    has_txt = "SI" if cap_txt.exists() else "NO"
    has_meta = "SI" if meta_json.exists() else "NO"

    print(f"{i:<3} | {slug:<48} | {dur_str:<14} | {size_str:<10} | {num_caps:<5} | {has_txt:<4} | {has_meta:<4}")

tot_m = int(total_dur // 60)
tot_s = int(total_dur % 60)
print("=" * 95)
print(f"Total de videos: {len(guiones)} | Duracion total acumulada: {tot_m}m {tot_s:02d}s (~{total_dur/3600:.2f} horas)")
