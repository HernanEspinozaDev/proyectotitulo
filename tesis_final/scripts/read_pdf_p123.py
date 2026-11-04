import subprocess

res = subprocess.run(['pdftotext', '-f', '1', '-l', '4', 'ES2/informe_docskill/build/Informe_Desarrollo_e_Implementacion_espaciGo.pdf', '-'], capture_output=True, text=True)
print('--- PAGES 1-4 OF DOCSKILL PDF ---')
print(res.stdout)
