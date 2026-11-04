with open('ES2/informe_docskill/sections/02-modelamiento.md') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if '### UC-' in l or '| **UC-' in l or '| `UC-' in l:
        print(f'{i+1:3d}: {l.strip()}')
