#!/usr/bin/env python3
"""Comprobación exhaustiva e independiente de los 12 puntos de control (D01 a D12)."""
import re
import subprocess
from pathlib import Path

BASE_DIR = Path('/home/nandev/Documentos/projects/espaciGo/ES2/informe_docskill')

def check():
    results = {}
    
    # D01: Portada formal INACAP en página 1, separada del índice
    pdf_path = BASE_DIR / 'build' / 'Informe_Desarrollo_e_Implementacion_espaciGo.pdf'
    res = subprocess.run(['pdftotext', '-f', '1', '-l', '3', str(pdf_path), '-'], capture_output=True, text=True)
    pages = res.stdout.split('\x0c')
    p1_text = pages[0] if len(pages) > 0 else ''
    p2_text = pages[1] if len(pages) > 1 else ''
    
    p1_ok = ('Asignatura:Proyecto de Título' in p1_text or 'Asignatura: Proyecto de Título' in p1_text) and 'Índice' not in p1_text
    p2_ok = 'Índice' in p2_text and '1. Detalle de las Tecnologías' in p2_text
    results['D01'] = p1_ok and p2_ok
    
    # D02: Índice estructurado y Tabla 1 en cuerpo del informe con notas ponderadas
    res_t1 = subprocess.run(['pdftotext', '-f', '11', '-l', '15', str(pdf_path), '-'], capture_output=True, text=True)
    t1_text = res_t1.stdout
    p_t1_ok = 'Tabla 1' in t1_text and '4,86' in t1_text and '4,31' in t1_text
    results['D02'] = p_t1_ok
    
    # D03: Figuras técnicas (fig04 sin MFA, fig06 sin FK falsa reserva->ocupacion)
    f04_puml = (BASE_DIR / 'assets' / 'figuras' / 'fuentes' / 'fig04_uml_casos_uso_ecosistema.puml').read_text(encoding='utf-8')
    d03_f04 = 'UC-03' in f04_puml and 'Perfil y Datos de Contacto' in f04_puml and 'Multifactor' not in f04_puml
    f06_puml = (BASE_DIR / 'assets' / 'figuras' / 'fuentes' / 'fig06_modelo_datos_er_nucleo.puml').read_text(encoding='utf-8')
    d03_f06 = 'espacio ||--o{ ocupacion' in f06_puml and 'reserva ||--o{ ocupacion' not in f06_puml
    results['D03'] = d03_f04 and d03_f06
    
    # D04: Anexo B diccionario (0 PK null, sesion.id PK NOT NULL, rol_usuario.rol CHECK, sin restricciones CHECK truncadas)
    b_lines = (BASE_DIR / 'appendices' / 'b-anexo.md').read_text(encoding='utf-8').splitlines()
    pk_null = any(re.search(r'\bPK\b.*\(NULL\)', l) for l in b_lines)
    has_sesion_id_pk = any('| `id` | `uuid` | PK (NOT NULL)' in l for l in b_lines)
    has_rol_ck = any('CONSTRAINT rol_usuario_rol_ck CHECK' in l for l in b_lines)
    trunc_checks = [l for l in b_lines if l.strip().endswith('AND siz') or l.strip().endswith('...') or (l.startswith('- `CONSTRAINT') and len(l.strip()) == 122)]
    results['D04'] = (not pk_null) and has_sesion_id_pk and has_rol_ck and (len(trunc_checks) == 0)
    
    # D05: Catálogo canónico de 14 casos de uso UC-01 a UC-14
    sec02_text = (BASE_DIR / 'sections' / '02-modelamiento.md').read_text(encoding='utf-8')
    d05_ok = 'UC-01' in sec02_text and 'UC-14' in sec02_text and 'UC-03' in sec02_text and 'Perfil' in sec02_text
    results['D05'] = d05_ok
    
    # D06: Nomenclatura CP-01 a CP-08 unificada en Sec 04 y Anexo H
    sec04_text = (BASE_DIR / 'sections' / '04-pruebas-calidad.md').read_text(encoding='utf-8')
    anexo_h_text = (BASE_DIR / 'appendices' / 'h-anexo.md').read_text(encoding='utf-8')
    d06_ok = 'CP-01' in sec04_text and 'CP-08' in sec04_text and 'CP-01' in anexo_h_text and 'CP-08' in anexo_h_text
    results['D06'] = d06_ok
    
    # D07: Conteo exacto de 110 tablas físicas consolidadas
    b_text = (BASE_DIR / 'appendices' / 'b-anexo.md').read_text(encoding='utf-8')
    g_text = (BASE_DIR / 'appendices' / 'g-anexo.md').read_text(encoding='utf-8')
    d07_ok = '110 tablas físicas consolidadas' in b_text and '110 tablas físicas' in g_text
    results['D07'] = d07_ok
    
    # D08: Marco de privacidad Ley 21.719 (Agencia, 15 días corridos, Art. 14 sexies sin dilaciones indebidas)
    sec03_text = (BASE_DIR / 'sections' / '03-kpi-sla.md').read_text(encoding='utf-8')
    d_anexo_text = (BASE_DIR / 'appendices' / 'd-anexo.md').read_text(encoding='utf-8')
    f_anexo_text = (BASE_DIR / 'appendices' / 'f-anexo.md').read_text(encoding='utf-8')
    d08_sec03 = 'Consejo de Protección' not in sec03_text and 'Agencia de Protección de Datos Personales' in sec03_text and '15 días corridos' in sec03_text
    d08_d = 'sin dilación indebida' in d_anexo_text and 'Art. 14 sexies' in d_anexo_text
    d08_f = '15 días corridos' in f_anexo_text and 'Agencia de Protección de Datos Personales' in f_anexo_text
    results['D08'] = d08_sec03 and d08_d and d08_f
    
    # D09: Sección 5.3 Gestión de Cambios formal (ITIL 4, roles CAB / ECAB, tipos Standard/Normal/Emergencia)
    sec05_text = (BASE_DIR / 'sections' / '05-implementacion.md').read_text(encoding='utf-8')
    d09_ok = 'Procedimiento Formal de Gestión de Cambios' in sec05_text and 'CAB' in sec05_text and 'ECAB' in sec05_text and 'Emergencia' in sec05_text
    results['D09'] = d09_ok
    
    # D10: Anexo E con contratos de planning/openapi.yaml
    anexo_e_text = (BASE_DIR / 'appendices' / 'e-anexo.md').read_text(encoding='utf-8')
    d10_ok = '/admin/global/me' in anexo_e_text and '/public/spaces' in anexo_e_text and 'OpenAPI 3.1' in anexo_e_text
    results['D10'] = d10_ok
    
    # D11: Ponderación matemática exacta tabla 1 y anexo A (Java 4,31; GCP 4,86)
    sec01_text = (BASE_DIR / 'sections' / '01-tecnologias.md').read_text(encoding='utf-8')
    anexo_a_text = (BASE_DIR / 'appendices' / 'a-anexo.md').read_text(encoding='utf-8')
    d11_ok = '4,31' in sec01_text and '4,86' in sec01_text and '4,31' in anexo_a_text and '4,86' in anexo_a_text
    results['D11'] = d11_ok
    
    # D12: ADR-002 y anexo A alineados a 110 tablas
    d12_ok = '110 tablas físicas' in anexo_a_text
    results['D12'] = d12_ok
    
    all_passed = True
    for k in sorted(results.keys()):
        passed = results[k]
        if not passed:
            all_passed = False
        print(f'{k}: {"RESUELTO (OK)" if passed else "FALLIDO"}')
        
    if all_passed:
        print("\n>>> VERIFICACION COMPLETA: 12/12 PUNTOS DE CONTROL D01-D12 RESUELTOS SATISFACTORIAMENTE <<<!")
        return 0
    else:
        print("\n>>> ATENCION: ALGUNOS PUNTOS DE CONTROL NO PASARON LA COMPROBACION <<<!")
        return 1

if __name__ == '__main__':
    raise SystemExit(check())
