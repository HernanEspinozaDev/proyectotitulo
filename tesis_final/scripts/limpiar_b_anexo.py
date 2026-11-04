#!/usr/bin/env python3
"""Limpia artefactos del diccionario de datos en appendices/b-anexo.md"""
from pathlib import Path
import re

b_p = Path('/home/nandev/Documentos/projects/espaciGo/ES2/informe_docskill/appendices/b-anexo.md')
text = b_p.read_text(encoding='utf-8')

# 1. Reemplazar PK (NULL) y FK/PK (NULL) por NOT NULL
text = text.replace('PK (NULL)', 'PK (NOT NULL)')
text = text.replace('FK/PK (NULL)', 'FK/PK (NOT NULL)')

# 2. Reemplazar ON DELETE RES truncado
text = re.sub(r'ON DELETE RES\b', 'ON DELETE RESTRICT', text)

b_p.write_text(text, encoding='utf-8')
print('appendices/b-anexo.md limpiado exitosamente.')
