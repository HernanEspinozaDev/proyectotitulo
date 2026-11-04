#!/usr/bin/env python3
"""Convierte matrices multicriterio anchas en fichas legibles para página carta."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parent.parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT.parent/'docskill'))
from docskill import DocSkillProject
project=DocSkillProject.open(ROOT)
path='appendices/a-anexo.md'
text=project.read_markdown(path)
lines=text.splitlines()
out=[]; i=0; tables=0
labels=['Rendimiento','Seguridad','Costo Cloud','Ecosistema','Dominio Legal']
while i<len(lines):
    if lines[i].startswith('| Alternativa Evaluada |'):
        block=[]
        while i<len(lines) and lines[i].startswith('|'):
            block.append(lines[i]); i+=1
        rows=[]
        for raw in block[2:]:
            cells=[c.strip() for c in raw.strip().strip('|').split('|')]
            if len(cells)<8: continue
            name,s1,s2,s3,s4,s5,score,judgment=cells[:8]
            name=name.replace('**','').replace('[Seleccionada]','').strip()
            selected=' [seleccionada]' if '[Seleccionada]' in cells[0] else ''
            score=score.replace('**','')
            vals=[c.replace('**','') for c in (s1,s2,s3,s4,s5)]
            rows.append((name+selected, vals, score, judgment))
        if len(rows)!=3: raise SystemExit(f'Matriz inesperada: {len(rows)} alternativas en sección {tables+1}')
        tables+=1
        out.append('**Criterios y pesos:** Rendimiento 30%; seguridad 25%; costo cloud 20%; ecosistema 15%; dominio legal 10%. Escala de 1,0 a 5,0.')
        out.append('')
        for name,vals,score,judgment in rows:
            out.append(f'#### {name}')
            out.append('')
            out.append('**Puntajes:** '+ '; '.join(f'{lab} {val}' for lab,val in zip(labels,vals)) + f'; ponderado **{score}/5**.')
            out.append('')
            out.append('**Dictamen:** '+judgment)
            out.append('')
        continue
    out.append(lines[i]); i+=1
if tables!=4: raise SystemExit(f'Se esperaban 4 matrices y se encontraron {tables}')
project.write_markdown(path,'\n'.join(out).rstrip()+'\n')
print(f'{tables} matrices convertidas a fichas comparativas legibles.')
