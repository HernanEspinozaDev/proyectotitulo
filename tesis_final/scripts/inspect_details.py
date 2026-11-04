#!/usr/bin/env python3
from pathlib import Path
BASE_DIR = Path('/home/nandev/Documentos/projects/espaciGo/ES2/informe_docskill')

# 1. D04 trunc_checks
b_lines = (BASE_DIR / 'appendices' / 'b-anexo.md').read_text(encoding='utf-8').splitlines()
trunc = [f'{i+1}: {l}' for i, l in enumerate(b_lines) if l.strip().endswith('AND siz') or l.strip().endswith('...') or (l.startswith('- `CONSTRAINT') and len(l.strip()) == 122)]
print('=== D04 TRUNC CHECKS ===')
for t in trunc:
    print(t)

# 2. D07 intro in b-anexo
print('=== D07 B INTRO ===')
for l in b_lines[:15]:
    print(l)

# 3. D08 d_anexo exact notification
d_text = (BASE_DIR / 'appendices' / 'd-anexo.md').read_text(encoding='utf-8')
print('=== D08 D ANEXO ===')
for l in d_text.splitlines():
    if any(k in l for k in ['14', 'indebida', 'dilaci', 'Agencia', 'notific']):
        print('  d_anexo:', l)

# 4. D08 f_anexo
f_text = (BASE_DIR / 'appendices' / 'f-anexo.md').read_text(encoding='utf-8')
print('=== D08 F ANEXO ===')
for l in f_text.splitlines():
    if any(k in l for k in ['días', 'dias', 'Agencia', '14', 'corridos']):
        print('  f_anexo:', l)
