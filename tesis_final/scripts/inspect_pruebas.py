print('=== SECCIÓN 04 ===')
with open('ES2/informe_docskill/sections/04-pruebas-calidad.md') as f:
    for i, l in enumerate(f):
        if 'CP-' in l or 'PT-' in l or '| **CP' in l or '| **PT' in l or 'RPO' in l:
            print(f'{i+1:3d}: {l.strip()}')
            if i > 120: break

print('\n=== ANEXO C ===')
with open('ES2/informe_docskill/appendices/c-anexo.md') as f:
    for i, l in enumerate(f):
        if 'PT-11' in l or 'PT-09' in l or 'KPI-09' in l or 'CU-29' in l or 'RPO' in l:
            print(f'{i+1:3d}: {l.strip()}')
            if i > 140: break
