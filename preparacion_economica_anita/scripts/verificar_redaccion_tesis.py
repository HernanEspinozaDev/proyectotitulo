"""Verifica la edición académica frente a las cifras ya auditadas."""
from pathlib import Path
from decimal import Decimal
import hashlib
import json
import re
import zipfile
from lxml import etree as E
from preparar_redaccion_tesis import source_table, money

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '07_texto_para_tesis'


def rows(text, number):
    return [[c.strip() for c in row.strip('|').split('|')] for row in source_table(text, number).strip().splitlines()[2:]]


def main():
    body = (OUT / 'capitulo_xiv_evaluacion_economica.md').read_text()
    annex = (OUT / 'anexo_h_evaluacion_economica.md').read_text()
    oldbody = (ROOT / '03_propuesta/capitulo_xiv_borrador.md').read_text()
    oldannex = (ROOT / '03_propuesta/anexo_h_tablas_fuente.md').read_text()
    text = body + '\n' + annex
    # Se revisa el contenido del capítulo/anexo; los nombres de autores de portada se conservan.
    for expression in [r'\bAnita\b', r'\bErick\b', r'\bExcel\b', r'\bGCP\b', r'\bpropietario\b', r'\bpendiente\w*\b', r'\bsupuesto\w*\b', r'\bratific\w*\b', r'\btranscrip\w*\b', r'\bprovisional\w*\b', r'\b(?:hicimos|nuestro|nuestra)\b']:
        assert not re.search(expression, text, re.I), expression
    ids = re.findall(r'\*\*Tabla ([\d.H]+)\*\*', text)
    assert len(ids) == 27 and len(set(ids)) == 27
    assert text.count('*Nota.* Elaboración propia.') == 27
    for ref in re.findall(r'\bTabla ((?:14|H)\.[\d.]+)', text):
        assert ref.rstrip('.') in ids, ref
    sections = re.findall(r'^## (H\.\d+)\.', annex, re.M)
    assert sections == [f'H.{i}' for i in range(1, 15)]
    for ref in re.findall(r'\bAnexo (H\.\d+)', text):
        assert ref in sections, ref
    mapping_body = {'14.1': '14', '14.3': '24', '14.4': '18', '14.5': '19', '14.6': '20', '14.7': '21', '14.8': '22', '14.9': '23', '14.10': '25', '14.11': '26'}
    mapping_annex = {'H.3.1': 'H.32.1', 'H.4.1': 'H.32.2', 'H.6.1': 'H.33.1', 'H.7.1': 'H.34.1', 'H.10.1': 'H.36.1', 'H.10.2': 'H.36.3', 'H.11.1': 'H.36.2', 'H.11.2': 'H.40.1', 'H.12.1': 'H.37.1', 'H.12.2': 'H.37.2', 'H.13.1': 'H.38.1', 'H.13.2': 'H.38.2'}
    def numeric_cells(grid):
        return [[re.findall(r'-?\d[\d.,]*', cell) for cell in row[1:]] for row in grid]
    for new, old, source, original in [(k, v, body, oldbody) for k, v in mapping_body.items()] + [(k, v, annex, oldannex) for k, v in mapping_annex.items()]:
        assert numeric_cells(rows(source, new)) == numeric_cells(rows(original, old)), new
    data = json.loads((ROOT / '06_escenario_adoptado/resultados.json').read_text())['condicionada_puro']
    losses = Decimal(0)
    taxrows = rows(annex, 'H.8.1')
    for actual, expected in zip(data['anual'], taxrows):
        losses += max(-Decimal(actual['ebt_clp']), 0)
        assert expected == [str(actual['anio']), money(actual['ebt_clp']), money(losses), money(actual['impuesto_clp'])]
    docx = OUT / 'build/Evaluacion_economica_espaciGo.docx'
    w = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    with zipfile.ZipFile(docx) as z:
        tree = E.fromstring(z.read('word/document.xml'))
    tables = list(tree.iter(w+'tbl'))
    assert len(tables) == 27
    for tbl in tables:
        borders = tbl.find(w+'tblPr/'+w+'tblBorders')
        assert borders is not None and len(borders) == 6
        for edge in borders:
            assert edge.get(w+'sz') == '4' and edge.get(w+'color') == '000000'
        assert all(c.find(w+'tcPr/'+w+'shd') is not None for c in tbl.find(w+'tr').findall(w+'tc'))
    record = {'estado': 'correcto', 'tablas': 27, 'tablas_con_cifras_comparadas': 23, 'notas_elaboracion_propia': 27,
              'criterios': ['voz académica del proyecto, sin atribuciones personales', 'decisiones adoptadas expresadas como criterios y presupuestos', 'proyecciones diferenciadas de resultados observados', 'referencias cuerpo/anexo resueltas', 'cifras del escenario financiero conservadas', 'bordes y encabezados nativos de Word', 'antecedentes originales conservados fuera del texto publicable'],
              'docx_sha256': hashlib.sha256(docx.read_bytes()).hexdigest(), 'revision_visual': 'por registrar tras render'}
    (OUT / 'verificacion_editorial.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(record, ensure_ascii=False))


if __name__ == '__main__':
    main()
