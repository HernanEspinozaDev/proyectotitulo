import re
from pathlib import Path

mig_dir = Path('/home/nandev/Documentos/projects/espaciGo/db/migrations')
sql_files = sorted(list(mig_dir.glob('V*.sql')))

print(f'Total migration files: {len(sql_files)}')

alters = []
for f in sql_files:
    text = f.read_text(encoding='utf-8')
    # remove comments
    text_nocomments = re.sub(r'--.*?$', '', text, flags=re.MULTILINE)
    for m in re.finditer(r'ALTER\s+TABLE\s+(?:IF\s+EXISTS\s+)?(?:public\.)?([a-zA-Z0-9_]+)\s+([^;]+);', text_nocomments, re.IGNORECASE):
        tname = m.group(1).lower()
        body = m.group(2).strip()
        alters.append((f.name, tname, body))

print(f'Total ALTER TABLE statements: {len(alters)}')
for f_name, tname, body in alters[:30]:
    print(f'{f_name} | {tname} | {repr(body[:80])}')
