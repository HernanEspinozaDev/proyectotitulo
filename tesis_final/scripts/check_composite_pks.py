import re
from pathlib import Path

mig_dir = Path('/home/nandev/Documentos/projects/espaciGo/db/migrations')
composite_pks = []

for f in sorted(mig_dir.glob('V*.sql')):
    txt = f.read_text(encoding='utf-8')
    for m in re.finditer(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?(?:public\.)?([a-zA-Z0-9_]+)\s*\((.*?)\);', txt, re.DOTALL | re.I):
        tname = m.group(1).lower()
        body = m.group(2)
        # find composite PK
        m_pk = re.search(r'PRIMARY\s+KEY\s*\(([^)]+)\)', body, re.I)
        if m_pk:
            cols = [c.strip().strip('"') for c in m_pk.group(1).split(',') if c.strip()]
            if len(cols) > 1:
                composite_pks.append((f.name, tname, cols))

print(f'Total composite PK tables found: {len(composite_pks)}')
for f_name, tname, cols in composite_pks:
    print(f'{tname} ({f_name}): {cols}')
