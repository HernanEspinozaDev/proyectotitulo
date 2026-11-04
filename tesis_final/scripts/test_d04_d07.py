import re
from pathlib import Path

BASE_DIR = Path('/home/nandev/Documentos/projects/espaciGo/ES2/informe_docskill')

b_lines = (BASE_DIR / 'appendices' / 'b-anexo.md').read_text(encoding='utf-8').splitlines()
pk_null = any(re.search(r'\bPK\b.*\(NULL\)', l) for l in b_lines)
has_sesion_id_pk = any('| `id` | `uuid` | PK (NOT NULL)' in l for l in b_lines)
has_rol_ck = any('CONSTRAINT rol_usuario_rol_ck CHECK' in l for l in b_lines)
trunc_checks = [l for l in b_lines if l.strip().endswith('AND siz') or l.strip().endswith('...') or (l.startswith('- `CONSTRAINT') and len(l.strip()) == 122)]

print('D04: pk_null =', pk_null)
print('D04: has_sesion_id_pk =', has_sesion_id_pk)
print('D04: has_rol_ck =', has_rol_ck)
print('D04: trunc_checks =', len(trunc_checks))
print('D04 overall =', (not pk_null) and has_sesion_id_pk and has_rol_ck and (len(trunc_checks) == 0))

b_text = (BASE_DIR / 'appendices' / 'b-anexo.md').read_text(encoding='utf-8')
g_text = (BASE_DIR / 'appendices' / 'g-anexo.md').read_text(encoding='utf-8')
print('D07 b has phrase =', '110 tablas físicas consolidadas' in b_text)
print('D07 g has phrase =', '110 tablas físicas' in g_text)
print('D07 overall =', '110 tablas físicas consolidadas' in b_text and '110 tablas físicas' in g_text)
