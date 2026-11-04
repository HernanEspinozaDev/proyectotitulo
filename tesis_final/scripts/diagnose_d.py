import re
from pathlib import Path

BASE_DIR = Path('/home/nandev/Documentos/projects/espaciGo/ES2/informe_docskill')
b_lines = (BASE_DIR / 'appendices' / 'b-anexo.md').read_text(encoding='utf-8').splitlines()
trunc_checks = [l for l in b_lines if l.strip().endswith('AND siz') or l.strip().endswith('...') or (l.startswith('- `CONSTRAINT') and len(l.strip()) == 122)]
print('Total trunc_checks:', len(trunc_checks))
for tc in trunc_checks:
    print(len(tc.strip()), repr(tc))
