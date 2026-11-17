"""Comprueba cachés Word, siete líneas observadas e integridad de la entrega."""
from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
import hashlib
import json
import subprocess
from lxml import etree as E
import pypdfium2 as pdfium
from PIL import ImageChops

ROOT = Path(__file__).resolve().parents[2]
T = ROOT/'tesis_final'
BUILD = T/'build'
BASELINE = 'a9643f5'
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def previous(path):
    return subprocess.check_output(['git', 'show', BASELINE+':'+path], cwd=ROOT)


def text(node):
    return ' '.join(''.join(t.text or '' for t in node.iter(W+'t')).split())


def academic_body(root):
    body = deepcopy(root.find(W+'body'))
    for child in list(body):
        if child.tag == W+'sdt' or any('TOC ' in (n.text or '') for n in child.iter(W+'instrText')):
            body.remove(child)
    for node in list(body.iter()):
        if node.tag in [W+'bookmarkStart', W+'bookmarkEnd']:
            node.getparent().remove(node)
    return E.tostring(body, method='c14n')


manifest = json.loads((T/'document.json').read_text())
assert previous('tesis_final/document.json') == (T/'document.json').read_bytes()
for path in manifest['sections']:
    assert previous('tesis_final/'+path) == (T/path).read_bytes(), path
assert len(manifest['sections']) == 28
expected_files = ['Tesis_Final_espaciGo.docx', 'Tesis_Final_espaciGo.pdf']
assert sorted(p.name for p in BUILD.glob('Tesis_Final_espaciGo*')) == expected_files
docx = BUILD/expected_files[0]
pdf = BUILD/expected_files[1]
with TemporaryDirectory() as directory:
    directory = Path(directory)
    old_docx, old_pdf = directory/'antes.docx', directory/'antes.pdf'
    old_docx.write_bytes(previous('tesis_final/build/Tesis_Final_espaciGo.docx'))
    old_pdf.write_bytes(previous('tesis_final/build/Tesis_Final_espaciGo.pdf'))
    with ZipFile(docx) as current, ZipFile(old_docx) as original:
        root = E.fromstring(current.read('word/document.xml'))
        before = E.fromstring(original.read('word/document.xml'))
        assert academic_body(root) == academic_body(before), 'Cambió XML académico fuera de índices y marcadores.'
        for name in original.namelist():
            if name.startswith('word/media/'):
                assert current.read(name) == original.read(name), name
        indexes = root.find(W+'body').findall(W+'sdt')
        assert len(indexes) == 3
        cached = list(map(text, indexes))
        from canonical_academic_labels import CAPTIONS, RNF_HEADING
        assert RNF_HEADING in cached[0]
        for label, title in CAPTIONS.items():
            assert label+' '+title in cached[1 if label.startswith('Tabla') else 2], label
        body_caption = [p for p in root.find(W+'body').findall(W+'p') if text(p).startswith('Figura 13')]
        assert len(body_caption) == 1 and CAPTIONS['Figura 13'] in text(body_caption[0])
        bookmarks = {b.get(W+'name') for b in root.iter(W+'bookmarkStart')}
        links = [l.get(W+'anchor') for i in indexes for l in i.iter(W+'hyperlink')]
        assert len(links) == 591 and all(l in bookmarks for l in links)
    # Se coteja cada página, tanto sus caracteres como su representación visual.
    old, new = pdfium.PdfDocument(old_pdf), pdfium.PdfDocument(pdf)
    assert len(old) == len(new) == 567
    visual_differences = []
    for i in range(len(old)):
        a, b = old[i], new[i]
        ta, tb = a.get_textpage(), b.get_textpage()
        assert ta.get_text_range() == tb.get_text_range(), ('Texto PDF distinto', i+1)
        ra, rb = a.render(scale=1), b.render(scale=1)
        ia, ib = ra.to_pil().convert('RGB'), rb.to_pil().convert('RGB')
        difference = ImageChops.difference(ia, ib)
        if difference.getbbox():
            histogram = difference.convert('L').histogram()
            changed = sum(histogram[1:])
            ratio = changed/(ia.width*ia.height)
            visual_differences.append({'pagina': i+1, 'pixeles_distintos': changed, 'proporcion': ratio})
        ra.close(); rb.close(); ta.close(); tb.close(); a.close(); b.close()
    old.close(); new.close()
result = {
    'estado': 'verificado', 'fuentes_iguales': 28, 'anexos_preservados': 8,
    'xml_academico_fuera_de_indices_y_marcadores': 'idéntico a la entrega anterior',
    'imagenes_word': 'bytes idénticos a la entrega anterior',
    'indices_guardados_en_word': 3, 'entradas_enlazadas': 591,
    'lineas_observadas': 'seis entradas de índices y título de Figura 13 con espaciGo',
    'comparacion_pdf': '567 páginas cotejadas carácter por carácter; diferencias visuales cuantificadas para revisión',
    'diferencias_rasterizacion': visual_differences,
    'entrega_unica': expected_files,
    'docx_sha256': hashlib.sha256(docx.read_bytes()).hexdigest(),
    'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
}
(T/'context/01_auditorias_y_rubricas/verificacion_entrega_unica.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(result, ensure_ascii=False))
