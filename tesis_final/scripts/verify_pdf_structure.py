#!/usr/bin/env python3
"""Inspecciona la estructura de paginas y figuras del PDF generado con poppler/pdfinfo"""
import subprocess
from pathlib import Path

pdf_p = Path('/home/nandev/Documentos/projects/espaciGo/ES2/informe_docskill/build/Informe_Desarrollo_e_Implementacion_espaciGo.pdf')

# Extraemos texto de cada pagina y buscamos encabezados y figuras
cmd = ['pdftotext', str(pdf_p), '-']
res = subprocess.run(cmd, capture_output=True, text=True, check=True)
pages = res.stdout.split('\x0c')
print(f'Total paginas extraidas: {len(pages)}')

# Buscamos figuras y capitulos
for p_num, p_txt in enumerate(pages, 1):
    for fig in range(1, 12):
        tag = f'Figura {fig}.'
        if tag in p_txt:
            print(f'Pagina {p_num:3d}: {tag}')
    for cap in [
        '1. Detalle de las Tecnologías a Implementar',
        '2. Modelamiento de la solución',
        '3. Implementación de KPI y SLA',
        '4. Plan de Pruebas y Aseguramiento de Calidad',
        '5. Plan de Implementación y Operación',
        'Anexo A', 'Anexo B', 'Anexo C', 'Anexo D', 'Anexo E', 'Anexo F', 'Anexo G', 'Anexo H'
    ]:
        if cap in p_txt:
            print(f'Pagina {p_num:3d}: [SECCION] {cap}')
