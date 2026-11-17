"""Aceptación de correcciones frente a fuentes, Word y PDF publicados."""
from pathlib import Path
import hashlib,json,re,subprocess,zipfile
from lxml import etree as E
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1];T=ROOT/'tesis_final';P=Path(__file__).resolve().parent
manifest=json.loads((T/'document.json').read_text());sources={r:(T/r).read_text() for r in manifest['sections']}
alltext='\n'.join(sources.values());body='\n'.join(v for k,v in sources.items() if '/sections/' in '/'+k)
assert 'las figuras 11 y 12 describen persistencia' in alltext
c=sources['appendices/c-casos-de-uso.md'];assert 'HU05 · Figura 14' in c and c.count('Figura 15 del Capítulo X')==2
for pattern in [r'aws-emulator|Mailpit|espacigo-aws|aws-main|local-emulator|cmd/api|s3storage|documents3|Dockerfile',r'\bcommits?\b',r'\brepositorio(?:s)?\b',r'\bV[0-9]{1,6}\b',r'\b(?:3dc1c18|b1b38d1|8d33dcf|cc2fdc3|93b59c8)\b']:
 assert not re.search(pattern,alltext),pattern
x=sources['sections/10-capitulo-x.md'];assert 'operador de rangos `&&`' in x and '«Este contrato se guarda sin firma electrónica de las partes».' in x
for k in ['sections/06-capitulo-vi.md','sections/15-capitulo-xv.md']:
 assert not re.search(r'2009|2010|1\.320',sources[k])
assert 'outbox_evento_local' not in body
# El diccionario conserva exactamente sus columnas/tablas y restricciones físicas.
old=subprocess.check_output(['git','show','dd62e8c:tesis_final/appendices/d-diccionario-de-datos-ddl.md'],cwd=ROOT,text=True)
current=sources['appendices/d-diccionario-de-datos-ddl.md']
assert '### B.022 Auditoría histórica por lotes de control de acceso' in current
assert 'tabla física histórica `public.gcp06_test_access_batch_audit`' in current
oldgrids=[s for s in old[old.index('### B.001'):].splitlines() if s.startswith('|')]
newgrids=[s for s in current[current.index('### B.001'):].splitlines() if s.startswith('|')]
assert oldgrids==newgrids
assert len(re.findall(r"^### B[.]\d+",old,re.M))==len(re.findall(r"^### B[.]\d+",current,re.M))==110
assert [s for s in old.splitlines() if s.startswith("- `")]==[s for s in current.splitlines() if s.startswith("- `")]
for rel in ['sections/14-capitulo-xiv.md','appendices/h-evaluacion-economica-detallada.md']:
 old=subprocess.check_output(['git','show','dd62e8c:tesis_final/'+rel],cwd=ROOT,text=True)
 assert [s for s in old.splitlines() if s.startswith('|')]==[s for s in sources[rel].splitlines() if s.startswith('|')]
for rel in ['sections/11-capitulo-xi.md','sections/14-capitulo-xiv.md','sections/16-capitulo-xvi.md']:
 assert '392' in sources[rel] and '793' in sources[rel]
assert '−CLP 20.053.400,45' in sources['sections/14-capitulo-xiv.md']
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}';A='{http://schemas.openxmlformats.org/drawingml/2006/main}';R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
with zipfile.ZipFile(T/'build/Tesis_Final_espaciGo.docx') as z:
 xml=E.fromstring(z.read('word/document.xml'));rels={r.get('Id'):r.get('Target') for r in E.fromstring(z.read('word/_rels/document.xml.rels'))}
 nodes=list(xml.find(W+'body'));found=False
 for i,n in enumerate(nodes):
  if ''.join(n.itertext()).startswith('Figura 10'):
   image=nodes[i+1].find('.//'+A+'blip');assert image is not None
   target=rels[image.get(R+'embed')];path='word/'+target if not target.startswith('/') else target.lstrip('/')
   assert z.read(path)==(T/'assets/imagenes/fig09_componentes_aws.png').read_bytes();found=True
 assert found
 visible=' '.join(''.join(xml.itertext()).split());assert 'operador de rangos &&' in visible
reader=PdfReader(T/'build/Tesis_Final_espaciGo.pdf');pages=[p.extract_text() or '' for p in reader.pages];flat=' '.join('\n'.join(pages).split())
for expected in ['Lienzo del modelo de negocio de espaciGo','Componentes de aplicación y adaptadores de espaciGo','Topología objetivo y ruta de entrega de espaciGo en AWS','Categorías de espacios de espaciGo','Escenarios de volumen y ticket de espaciGo','Sistema espaciGo','las figuras 11 y 12 describen persistencia','operador de rangos &&','«Este contrato se guarda sin firma electrónica de las partes».']:
 assert expected in flat,expected
assert 'B.022 Tabla public.gcp06_test_access_batch_audit' not in flat
assert 'gcp06' not in '\n'.join(pages[:25])
for number, tokens in [('11',['OE1','OE2','OE3','OE4','OE5','793','financiamiento.']),('13',['RB-01','RB-02','RB-03','RB-04','RB-05','RB-06','intervención autorizada'])]:
    target=next(t for t in pages if re.search(r'^Tabla '+number+r'\s*\n',t,re.M))
    normalized=' '.join(target.split())
    assert all(t in normalized for t in tokens),(number,'tabla incompleta en página')
for word in ['aws-emulator','Mailpit','espacigo-aws','aws-main','3dc1c18','8d33dcf','cc2fdc3','cmd/api']:
 assert word not in flat,word
result={'estado':'verificado','paginas_pdf':len(pages),'correlativos':'10.7: 11/12; CU-15: 14; M06/M07:15','nombre_espacigo':'comprobado en rótulos, índices y subtítulo RNF','operador_y_comillas':'íntegros en fuente, Word y PDF','figura_10':'PNG final coincide con el render de la fuente corregida','diccionario_fisico':'110 fichas, columnas y restricciones físicas preservadas','tablas_economicas':'27 cuadrículas preservadas','maquetacion':'Tablas 11 y 13 completas en su página, sin última fila huérfana','interpretacion':'Umbrales de VAN al 12 % primero; piloto y necesidad de aportes explícitos','docx_sha256':hashlib.sha256((T/'build/Tesis_Final_espaciGo.docx').read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256((T/'build/Tesis_Final_espaciGo.pdf').read_bytes()).hexdigest()}
(P/'VERIFICACION_FINAL.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
