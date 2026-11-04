import re

lines = open('/home/nandev/Documentos/projects/espaciGo/ES2/informe_docskill/appendices/b-anexo.md').readlines()

# 1. Filas con PK y NULL
pk_null = [f'{i+1}: {l.strip()}' for i, l in enumerate(lines) if re.search(r'\bPK\b.*\(NULL\)', l)]
print(f'1. Total filas PK con nulabilidad NULL: {len(pk_null)}')
if pk_null:
    print(pk_null[:5])

# 2. sesion.id
sesion_lines = [l.strip() for l in lines if 'public.sesion`' in l or 'Tabla `public.sesion`' in l]
print('2. Tabla sesion presente:', len(sesion_lines))
for i, l in enumerate(lines):
    if '### B.' in l and 'public.sesion`' in l:
        for sub in lines[i:i+15]:
            if '`id`' in sub:
                print('   sesion.id:', sub.strip())

# 3. rol_usuario.rol
for i, l in enumerate(lines):
    if '### B.' in l and 'public.rol_usuario`' in l:
        for sub in lines[i:i+15]:
            if '`rol`' in sub or '`usuario_id`' in sub:
                print('   rol_usuario col:', sub.strip())

# 4. rol_usuario_evento.id
for i, l in enumerate(lines):
    if '### B.' in l and 'public.rol_usuario_evento`' in l:
        for sub in lines[i:i+15]:
            if '`id`' in sub:
                print('   rol_usuario_evento.id:', sub.strip())

# 5. Restricciones CHECK truncadas (terminando en AND siz)
trunc = [l.strip() for l in lines if l.strip().endswith('AND siz') or l.strip().endswith('AND siz`')]
print(f'5. Restricciones CHECK truncadas (AND siz): {len(trunc)}')
