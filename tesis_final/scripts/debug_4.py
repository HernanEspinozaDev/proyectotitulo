#!/usr/bin/env python3
from pathlib import Path
import re, subprocess

BASE_DIR = Path('/home/nandev/Documentos/projects/espaciGo/ES2/informe_docskill')
pdf_path = BASE_DIR / 'build' / 'Informe_Desarrollo_e_Implementacion_espaciGo.pdf'

# D02
res_t1 = subprocess.run(['pdftotext', '-f', '11', '-l', '15', str(pdf_path), '-'], capture_output=True, text=True)
print('D02: Tabla 1:', 'Tabla 1' in res_t1.stdout, '4,86:', '4,86' in res_t1.stdout, '4,31:', '4,31' in res_t1.stdout)
if not ('4,86' in res_t1.stdout):
    for line in res_t1.stdout.splitlines():
        if any(c in line for c in ['4,', 'GCP', 'Java', 'Go', 'AWS']):
            print('  t1 line:', line)

# D04
b_lines = (BASE_DIR / 'appendices' / 'b-anexo.md').read_text(encoding='utf-8').splitlines()
pk_null = any(re.search(r'\bPK\b.*\(NULL\)', l) for l in b_lines)
has_sesion_id_pk = any('| `id` | `uuid` | PK (NOT NULL)' in l for l in b_lines)
has_rol_ck = any('CONSTRAINT rol_usuario_rol_ck CHECK' in l for l in b_lines)
trunc_checks = [l for l in b_lines if l.strip().endswith('AND siz') or l.strip().endswith('...') or (l.startswith('- `CONSTRAINT') and len(l.strip()) == 122)]
print('D04: pk_null:', pk_null, 'has_sesion_id_pk:', has_sesion_id_pk, 'has_rol_ck:', has_rol_ck, 'trunc_checks:', len(trunc_checks))

# D07
b_text = (BASE_DIR / 'appendices' / 'b-anexo.md').read_text(encoding='utf-8')
g_text = (BASE_DIR / 'appendices' / 'g-anexo.md').read_text(encoding='utf-8')
print('D07: in b_text:', '110 tablas físicas consolidadas' in b_text, 'in g_text:', '110 tablas físicas' in g_text)

# D08
sec03_text = (BASE_DIR / 'sections' / '03-kpi-sla.md').read_text(encoding='utf-8')
d_anexo_text = (BASE_DIR / 'appendices' / 'd-anexo.md').read_text(encoding='utf-8')
f_anexo_text = (BASE_DIR / 'appendices' / 'f-anexo.md').read_text(encoding='utf-8')
print('D08 sec03 no Consejo:', 'Consejo de Protección' not in sec03_text, 'sec03 Agencia:', 'Agencia de Protección de Datos Personales' in sec03_text, 'sec03 15d:', '15 días corridos' in sec03_text)
print('D08 d_anexo:', 'sin dilación indebida' in d_anexo_text, 'Art. 14 sexies' in d_anexo_text)
print('D08 f_anexo:', '15 días corridos' in f_anexo_text, 'Agencia:' in f_anexo_text)
