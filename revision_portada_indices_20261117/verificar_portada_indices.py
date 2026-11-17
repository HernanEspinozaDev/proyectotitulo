"""Verifica el título autorizado y los rótulos sobre la entrega exportada."""
from pathlib import Path
import hashlib
import json
import zipfile
from lxml import etree as E
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'tesis_final/build'
TITLE = 'Diseño de una plataforma web transaccional para la intermediación y gestión del arriendo flexible de espacios en Chile: espaciGo'
manifest = json.loads((ROOT / 'tesis_final/document.json').read_text())
assert manifest['metadata']['title'] == TITLE
with zipfile.ZipFile(BUILD / 'Tesis_Final_espaciGo.docx') as package:
    document = E.fromstring(package.read('word/document.xml'))
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    paragraphs = [''.join(p.itertext()) for p in document.findall('w:body/w:p', ns)]
    assert paragraphs.count(TITLE) == 2
    core = E.fromstring(package.read('docProps/core.xml'))
    assert core.find('{http://purl.org/dc/elements/1.1/}title').text == TITLE
pdf = PdfReader(BUILD / 'Tesis_Final_espaciGo.pdf')
pages = [p.extract_text() or '' for p in pdf.pages]
normalize = lambda value: ' '.join(value.split())
assert all(TITLE in normalize(page) for page in pages[:2])
assert 'Firma' in pages[1] and 'Calificación' in pages[1]
assert pages[2].startswith('Dedicatoria'), 'La página de aprobación se desborda.'
earlier = json.loads((ROOT / 'revision_cierre_cinco_detalles_20261117/VERIFICACION_FINAL.json').read_text())
for extension in ['docx', 'pdf']:
    digest = hashlib.sha256((BUILD / ('Tesis_Final_espaciGo.' + extension)).read_bytes()).hexdigest()
    assert earlier[extension + '_sha256'] == digest, 'Debe actualizarse la comprobación de índices.'
result = {
    'estado': 'verificado',
    'titulo': TITLE,
    'portadas': 'Título completo en las dos páginas; firma y calificación en la segunda; dedicatoria en la tercera.',
    'rotulos_e_indices': earlier['entradas_verificadas'],
    'contenido_rnf': earlier['tabla_contenido_rnf'],
    'paginas_pdf': len(pages),
    'docx_sha256': earlier['docx_sha256'],
    'pdf_sha256': earlier['pdf_sha256'],
}
(Path(__file__).parent / 'VERIFICACION_FINAL.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(result, ensure_ascii=False))
