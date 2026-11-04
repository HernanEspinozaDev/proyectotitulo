#!/usr/bin/env python3
"""
render_all_diagrams.py
Automatiza el renderizado de diagramas fuente (.mmd y .puml) hacia imágenes PNG
de alta resolución (300 DPI) en assets/figuras/.

Uso:
  python3 scripts/render_all_diagrams.py             # Genera los que falten
  python3 scripts/render_all_diagrams.py --force     # Regenera diagramas Mermaid
  python3 scripts/render_all_diagrams.py fig01       # Regenera solo los que coincidan con fig01
"""

import os
import sys
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = BASE_DIR / "assets" / "diagramas_src"
OUT_DIR = BASE_DIR / "assets" / "figuras"
PUPPETEER_CONFIG = BASE_DIR / "scripts" / "puppeteer-config.json"

def render_mermaid(src_path: Path, out_path: Path, scale: int = 2):
    cmd = [
        "npx", "-y", "@mermaid-js/mermaid-cli",
        "-p", str(PUPPETEER_CONFIG),
        "-i", str(src_path),
        "-o", str(out_path),
        "-s", str(scale),
        "-b", "white"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[ERROR] Mermaid rendering failed for {src_path.name}:", file=sys.stderr)
        print(res.stderr, file=sys.stderr)
        return False
    return True

def render_plantuml(src_path: Path, out_path: Path):
    jar = os.environ.get("ESPACIGO_PLANTUML_JAR")
    if jar:
        cmd = [
            "java", "-jar", jar, "-failfast2", "-charset", "UTF-8",
            "-o", str(out_path.parent), str(src_path),
        ]
    else:
        cmd = ["npx", "-y", "node-plantuml", "generate", str(src_path), "-o", str(out_path)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[ERROR] PlantUML rendering failed for {src_path.name}:", file=sys.stderr)
        print(res.stderr, file=sys.stderr)
        return False
    return True

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    force_mermaid = "--force" in sys.argv
    force_puml = "--force-plantuml" in sys.argv
    only = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    print("==================================================")
    print(" Compilador Automático de Diagramas de Tesis")
    print(f" Origen:  {SRC_DIR}")
    print(f" Destino: {OUT_DIR}")
    print("==================================================")

    # 1. Procesar Mermaid (.mmd)
    mmd_files = sorted(SRC_DIR.glob("*.mmd"))
    count_mmd = 0
    failures = 0
    for mmd in mmd_files:
        if only and not any(o in mmd.stem for o in only):
            continue
        out_png = OUT_DIR / f"{mmd.stem}.png"
        if out_png.exists() and not force_mermaid and not only:
            print(f"[OMITIDO] {out_png.name} ya existe.")
            continue
        print(f"[RENDER] Mermaid: {mmd.name} -> {out_png.name}...")
        ok = render_mermaid(mmd, out_png)
        if ok:
            count_mmd += 1
        else:
            failures += 1

    # 2. Procesar PlantUML (.puml)
    puml_files = sorted(SRC_DIR.rglob("*.puml"))
    count_puml = 0
    for puml in puml_files:
        if only and not any(o in puml.stem for o in only):
            continue
        out_png = OUT_DIR / puml.relative_to(SRC_DIR).with_suffix(".png")
        out_png.parent.mkdir(parents=True, exist_ok=True)
        if out_png.exists() and not force_puml and not only:
            continue
        print(f"[RENDER] PlantUML: {puml.name} -> {out_png.name}...")
        ok = render_plantuml(puml, out_png)
        if ok:
            count_puml += 1
        else:
            failures += 1

    print("--------------------------------------------------")
    print(f"Finalizado: {count_mmd} diagramas Mermaid y {count_puml} PlantUML generados.")
    print("==================================================")

    return int(failures > 0)


if __name__ == "__main__":
    sys.exit(main())
