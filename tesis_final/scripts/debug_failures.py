import re
import subprocess
from pathlib import Path

BASE_DIR = Path('/home/nandev/Documentos/projects/espaciGo/ES2/informe_docskill')

# Check D01
pdf_path = BASE_DIR / 'build' / 'Informe_Desarrollo_e_Implementacion_espaciGo.pdf'
p1 = subprocess.run(['pdftotext', '-f', '1', '-l', '1', str(pdf_path), '-'], capture_output=True, text=True).stdout
p2 = subprocess.run(['pdftotext', '-f', '2', '-l', '2', str(…
