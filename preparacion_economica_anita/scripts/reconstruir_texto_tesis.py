"""Reconstruye la edición académica sin modificar el cálculo económico."""
from pathlib import Path
import argparse
import subprocess
import sys
import shutil

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--render', action='store_true')
parser.add_argument('--output-dir', default='/tmp/espacigo-redaccion-tesis')
args = parser.parse_args()
for script in ['verificar_fuentes_economicas.py', 'verificar_escenario_adoptado.py', 'preparar_redaccion_tesis.py']:
    subprocess.run([sys.executable, str(ROOT/'scripts'/script)], check=True)
subprocess.run([sys.executable, str(ROOT/'scripts/build_preview.py'), '--project-dir', str(ROOT/'07_texto_para_tesis')], check=True)
subprocess.run([sys.executable, str(ROOT/'scripts/verificar_redaccion_tesis.py')], check=True)
if args.render:
    output = Path(args.output_dir).resolve()
    docx = ROOT/'07_texto_para_tesis/build/Evaluacion_economica_espaciGo.docx'
    renderer = '/home/nandev/.codex/plugins/cache/openai-primary-runtime/documents/26.1112.11217/skills/documents/render_docx.py'
    subprocess.run([sys.executable, renderer, str(docx), '--output_dir', str(output), '--dpi', '100', '--emit_pdf'], check=True)
    shutil.copyfile(output/docx.with_suffix('.pdf').name, docx.with_suffix('.pdf'))
