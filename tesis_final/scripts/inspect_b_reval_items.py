import re
from pathlib import Path

b_text = Path('/home/nandev/Documentos/projects/espaciGo/ES2/informe_docskill/appendices/b-anexo.md').read_text(encoding='utf-8')

print('=== verificacion_estado_ck matches ===')
for m in re.finditer(r'- `CONSTRAINT verificacion_estado_ck[^`]+`', b_text):
    print(m.group(0))

print('=== bloqueo_cuenta_administrativo_local lines ===')
for l in b_text.splitlines():
    if 'bloqueada_por' in l:
        print(l)

print('=== bloqueo_cuenta_historial_local actor_id lines ===')
for l in b_text.splitlines():
    if 'actor_id' in l and 'historial' in b_text[max(0, b_text.find(l)-300):b_text.find(l)]:
        print(l)
