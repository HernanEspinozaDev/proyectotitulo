from pathlib import Path

b_text = Path('/home/nandev/Documentos/projects/espaciGo/ES2/informe_docskill/appendices/b-anexo.md').read_text(encoding='utf-8')

for tname in ['rol_usuario', 'tarifa_espacio', 'categoria_perfil_atributos', 'region_publica', 'comuna_publica']:
    idx = b_text.find(f'Tabla `public.{tname}`')
    if idx != -1:
        end_idx = b_text.find('### B.', idx + 10)
        if end_idx == -1:
            end_idx = idx + 1000
        print(f'=== {tname} ===')
        print(b_text[idx:end_idx].strip())
        print('\n')
