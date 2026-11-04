import subprocess
from pathlib import Path

pdf_path = Path('/home/nandev/Documentos/projects/espaciGo/ES2/informe_docskill/build/Informe_Desarrollo_e_Implementacion_espaciGo.pdf')

info = subprocess.run(['pdfinfo', str(pdf_path)], capture_output=True, text=True)
for line in info.stdout.splitlines():
    if 'Pages:' in line:
        print(line)

print('--- PÁGINA 1 (PORTADA) ---')
p1 = subprocess.run(['pdftotext', '-f', '1', '-l', '1', str(pdf_path), '-'], capture_output=True, text=True).stdout
print(p1.strip()[:400])

print('\n--- PÁGINA 2 (ÍNDICE) ---')
p2 = subprocess.run(['pdftotext', '-f', '2', '-l', '2', str(pdf_path), '-'], capture_output=True, text=True).stdout
print(p2.strip()[:400])

print('\n--- PÁGINAS TRANSICIÓN ---')
for p in range(8, 12):
    txt = subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), str(pdf_path), '-'], capture_output=True, text=True).stdout
    print(f'=== PÁGINA {p} ===')
    print(txt.strip()[:250])
