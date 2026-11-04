print('=== ANEXO G ===')
with open('ES2/informe_docskill/appendices/g-anexo.md') as f:
    for i, l in enumerate(f):
        if 'UC-' in l or 'CU-' in l or 'tabla' in l.lower():
            print(f'{i+1:3d}: {l.strip()}')
            if i > 80: break

print('\n=== ANEXO H ===')
with open('ES2/informe_docskill/appendices/h-anexo.md') as f:
    for i, l in enumerate(f):
        if 'UC-' in l or 'CU-' in l:
            print(f'{i+1:3d}: {l.strip()}')
            if i > 80: break
