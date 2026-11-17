"""Audita cifras, estructura y formato de la integración económica en la tesis."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import zipfile
from lxml import etree as E

ROOT = Path(__file__).resolve().parents[2]
TESIS = ROOT/'tesis_final'
SOURCE = ROOT/'preparacion_economica_anita/07_texto_para_tesis'
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def text(node):
    return ''.join(x.text or '' for x in node.iter(W+'t')).strip()


def tables(markdown):
    result = {}
    for match in re.finditer(r'\*\*Tabla ([\d.H]+)\*\*.*?(\|[^\n]+\n(?:\|[^\n]+\n)+)', markdown, re.S):
        result[match[1]] = [[x.strip() for x in line.strip('|').split('|')] for line in match[2].strip().splitlines()]
    return result


def main():
    body = (TESIS/'sections/14-capitulo-xiv.md').read_text()
    annex = (TESIS/'appendices/h-evaluacion-economica-detallada.md').read_text()
    source_body = tables((SOURCE/'capitulo_xiv_evaluacion_economica.md').read_text())
    source_annex = tables((SOURCE/'anexo_h_evaluacion_economica.md').read_text())
    current_body, current_annex = tables(body), tables(annex)
    assert len(current_body) == 11 and len(current_annex) == 16
    assert list(current_body) == [str(i) for i in range(14, 25)]
    for i in range(1, 12):
        assert current_body[str(13+i)] == source_body[f'14.{i}']
    assert current_annex == source_annex
    expected = ['14.1. Estudio de Mercado', '14.2. Costos del Proyecto', '14.2.1. Recursos', '14.2.2. Adquisiciones', '14.3. Flujo de Caja', '14.4. Indicadores de Rentabilidad Financiera (VAN, TIR y Payback)', '14.5. Análisis de Sensibilidad y Escenarios']
    headings = [re.sub(r'^#+ ', '', x) for x in body.splitlines() if x.startswith('#')]
    assert all(x in headings for x in expected)
    assert body.count('*Nota.* Elaboración propia.') == 11
    assert annex.count('*Nota.* Elaboración propia.') == 16
    for value in ['RESERVADA', 'Anita', 'Erick', 'Excel', 'GCP']:
        assert value not in body+annex, value
    for number in range(17, 21):
        grid = current_body[str(number)]
        assert grid[0] == ['Partida / período', 'Año 0', 'Año 1', 'Año 2', 'Año 3', 'Año 4']
        assert len(grid) == 18  # encabezado, separadores y 16 partidas
    all_ids = set(current_body) | set(current_annex)
    for match in re.finditer(r'\bTabla ((?:H\.)?\d+(?:\.\d+)?)', body+annex):
        assert match[1] in all_ids, match[0]
    baseline = '2d410cd'
    protected = ['tesis_final/document.json', 'tesis_final/templates/reference-tihi84.docx', 'tesis_final/templates/style-profile-inacap.json']
    preserved = {}
    for name in protected:
        before = subprocess.check_output(['git', 'show', baseline+':'+name], cwd=ROOT)
        after = (ROOT/name).read_bytes()
        if name.endswith('document.json'):
            previous,current=json.loads(before),json.loads(after)
            assert current['metadata']['title']=='Diseño de una plataforma web transaccional para la intermediación y gestión del arriendo flexible de espacios en Chile: espaciGo'
            previous['metadata']['title']=current['metadata']['title']
            assert previous==current,name
        else:
            assert before == after, name
        preserved[name] = hashlib.sha256(after).hexdigest()
    docx = TESIS/'build/Tesis_Final_espaciGo.docx'
    with zipfile.ZipFile(docx) as z:
        xml = E.fromstring(z.read('word/document.xml')).find(W+'body')
    active = False
    economic = []
    captions = []
    for node in xml:
        value = text(node)
        if node.tag == W+'p':
            if value.startswith(('CAPÍTULO ', 'ANEXO ', 'Material Complementario')):
                active = value.startswith(('CAPÍTULO XIV:', 'ANEXO H:'))
            if active and re.match(r'^Tabla (?:\d+|H\.\d+\.\d+)', value):
                assert node.find(W+'pPr/'+W+'pStyle').get(W+'val') == 'TableCaption'
                captions.append(value.split('\n')[0])
        if active and node.tag == W+'tbl':
            economic.append(node)
    assert len(economic) == len(captions) == 27
    for tbl in economic:
        borders = tbl.find(W+'tblPr/'+W+'tblBorders')
        assert len(borders) == 6
        assert all(edge.get(W+'sz') == '4' and edge.get(W+'color') == '000000' for edge in borders)
        for row in tbl.findall(W+'tr'):
            assert row.find(W+'trPr/'+W+'cantSplit') is not None
    result = {'estado': 'correcto', 'tablas_cuerpo': 11, 'tablas_anexo': 16,
              'flujos_completos_plantilla': 4, 'partidas_por_flujo': 16,
              'estructura_y_plantilla_conservadas': True,
              'cifras_iguales_edicion_aprobada': True, 'referencias_y_notas_verificadas': True,
              'archivos_protegidos_sha256': preserved,
              'docx_sha256': hashlib.sha256(docx.read_bytes()).hexdigest()}
    from pypdf import PdfReader
    pdf_path = TESIS/'build/Tesis_Final_espaciGo.pdf'
    reader = PdfReader(pdf_path)
    pages = [p.extract_text() or '' for p in reader.pages]
    actual_captions = {}
    for i, page in enumerate(pages):
        for number in re.findall(r'^Tabla (\d+|H\.\d+\.\d+)\s*\n', page, re.M):
            if number in all_ids:
                assert number not in actual_captions
                actual_captions[number] = i+1
    assert set(actual_captions) == all_ids
    for number in ['17', '18', '19', '20']:
        value = pages[actual_captions[number]-1]
        assert 'Flujo de caja proyectado' in value
        assert 'Elaboración propia.' in value
        assert 'Año 0' in value and 'Año 4' in value
    table_index = next(i for i, page in enumerate(pages) if '\nÍndice de Tablas\n' in page)
    figure_index = next(i for i, page in enumerate(pages) if '\nÍndice de Figuras\n' in page)
    destinations = set()
    for page in reader.pages[table_index:figure_index]:
        for reference in page.get('/Annots', []):
            annotation = reference.get_object()
            dest = annotation.get('/Dest')
            if dest and isinstance(dest, list):
                destinations.add(reader.get_page_number(dest[0].get_object())+1)
    assert set(actual_captions.values()) <= destinations
    assert '@es2sapag2008' not in '\n'.join(pages)
    result.update(paginas_pdf=len(pages), paginas_tablas=actual_captions,
                  flujos_completos_en_una_pagina=True,
                  destinos_indice_tablas_verificados=True,
                  total_tablas_word=len(list(xml.iter(W+'tbl'))),
                  pdf_sha256=hashlib.sha256(pdf_path.read_bytes()).hexdigest())
    target = TESIS/'context/01_auditorias_y_rubricas/verificacion_integracion_economica.json'
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
