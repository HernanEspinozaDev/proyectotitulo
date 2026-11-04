#!/usr/bin/env python3
"""Script maestro de compilación de la Memoria de Título espaciGo.

Ejecución típica:
    python3 build_thesis.py

Opciones:
    --no-pdf       Omite la exportación a PDF vía LibreOffice.
    --diagrams     Regenera todos los diagramas PlantUML y Mermaid antes de compilar.
    --validate     Solo ejecuta validación sintáctica y estructural con DocSkill.
"""
import argparse
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
TESIS_DIR = ROOT / "tesis_final"
DOCSKILL_DIR = ROOT / "docskill"

# Configurar path de DocSkill y Pandoc embebido
sys.path.insert(0, str(DOCSKILL_DIR))
os.environ.setdefault("DOCSKILL_PANDOC", str(DOCSKILL_DIR / ".tools/pandoc/bin/pandoc"))

from docskill.api import DocSkillProject


def render_diagrams():
    print("🎨 [1/4] Renderizando diagramas de arquitectura y modelado...")
    render_script = TESIS_DIR / "scripts" / "render_all_diagrams.py"
    if render_script.is_file():
        res = subprocess.run([sys.executable, str(render_script)], cwd=TESIS_DIR)
        if res.returncode != 0:
            print("⚠️ Advertencia: Error durante el renderizado de diagramas.")
    else:
        print("⚠️ No se encontró scripts/render_all_diagrams.py, saltando renderizado.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-pdf", action="store_true", help="Omitir exportación a PDF")
    parser.add_argument("--diagrams", action="store_true", help="Regenerar diagramas antes de compilar")
    parser.add_argument("--validate", action="store_true", help="Solo validar estructura")
    args = parser.parse_args()

    if args.diagrams:
        render_diagrams()

    print("📖 Abriendo proyecto DocSkill en tesis_final...")
    project = DocSkillProject.open(TESIS_DIR)

    print("🔍 Validando secciones, metadatos y plantilla institucional...")
    val_res = project.validate()
    if not val_res.success:
        print(f"❌ Error de validación DocSkill: {val_res.to_dict()}")
        return 1
    print("✅ Validación estructural exitosa.")

    if args.validate:
        return 0

    print("⚙️ [2/4] Compilando capítulos y anexos con DocSkill (Pandoc + OOXML)...")
    build_res = project.build()
    if not build_res.success:
        print(f"❌ Error al construir el documento: {build_res.to_dict()}")
        return 1

    docx_path = TESIS_DIR / "build" / "Tesis_Final_espaciGo.docx"
    print(f"✅ DOCX base compilado: {docx_path} ({docx_path.stat().st_size / (1024*1024):.2f} MB)")

    print("📐 [3/4] Aplicando postprocesamiento de maquetación APA 7 e INACAP...")
    postproc_script = TESIS_DIR / "scripts" / "postprocess_tesis_layout.py"
    res = subprocess.run([sys.executable, str(postproc_script)], cwd=TESIS_DIR)
    if res.returncode != 0:
        print("❌ Error en postprocesamiento de maquetación.")
        return 1

    if not args.no_pdf:
        print("📄 [4/4] Exportando a PDF de alta fidelidad vía LibreOffice headless...")
        build_dir = TESIS_DIR / "build"
        res = subprocess.run(
            ["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", str(build_dir), str(docx_path)],
            cwd=TESIS_DIR,
            capture_output=True,
            text=True
        )
        pdf_path = build_dir / "Tesis_Final_espaciGo.pdf"
        if pdf_path.is_file():
            print(f"✅ PDF exportado con éxito: {pdf_path} ({pdf_path.stat().st_size / (1024*1024):.2f} MB)")
            # Informar páginas
            pages_res = subprocess.run(["pdfinfo", str(pdf_path)], capture_output=True, text=True)
            for line in pages_res.stdout.splitlines():
                if "Pages:" in line:
                    print(f"📄 Total de páginas: {line.split()[-1]}")
        else:
            print("⚠️ Advertencia: LibreOffice terminó pero no se generó el PDF:")
            print(res.stderr)

    print("\n🎉 Compilación completada con éxito.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
