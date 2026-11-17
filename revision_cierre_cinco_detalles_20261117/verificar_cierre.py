"""Comprueba los cinco detalles en fuentes, XML e índices renderizados del PDF."""
from pathlib import Path
import hashlib,json,re,zipfile
from lxml import etree as E
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1];T=ROOT/'tesis_final';OUT=Path(__file__).resolve().parent
phrase='La modalidad sin firma informa “Este contrato se guarda sin firma electrónica de las partes”.'
assert phrase in (T/'sections/10-capitulo-x.md').read_text()
assert '| Entorno local de emulación compatible con AWS |' in (T/'sections/09-capitulo-ix.md').read_text()
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
with zipfile.ZipFile(T/'build/Tesis_Final_espaciGo.docx') as z:
 d=E.fromstring(z.read('word/document.xml'));word=''.join(d.itertext())
 assert phrase in word
 assert 'partes .' not in word
 cells=[]
 for p in d.iter(W+'p'):
  text=''.join(t.text or '' for t in p.iter(W+'t'))
  if text.startswith(('Cumplimiento PCI-DSS','Estándares (PCI-DSS)')):
   assert p.find('.//'+W+'br') is not None
   assert any((t.text or '') in ['PCI-DSS','(PCI-DSS)'] for t in p.iter(W+'t'))
   cells.append(text)
 assert len(cells)==2
 settings=E.fromstring(z.read('word/settings.xml'));assert settings.find(W+'updateFields') is not None
reader=PdfReader(T/'build/Tesis_Final_espaciGo.pdf');pages=[p.extract_text() or '' for p in reader.pages]
flat=lambda s:' '.join(s.split())
assert phrase in flat('\n'.join(pages))
assert 'Entorno local de emulación compatible con AWS' in flat('\n'.join(pages))
# Aislar índices: no se admite que una coincidencia solo en el cuerpo cierre el caso.
ti=next(i for i,p in enumerate(pages) if '\nÍndice de Tablas\n' in p)
fi=next(i for i,p in enumerate(pages) if '\nÍndice de Figuras\n' in p)
ri=next(i for i,p in enumerate(pages) if i>fi and p.startswith('Resumen'))
contents=flat('\n'.join(pages[:ti]));tables=flat('\n'.join(pages[ti:fi]));figures=flat('\n'.join(pages[fi:ri]))
expected={
 'Tabla 4':'Lienzo del modelo de negocio de espaciGo',
 'Tabla H.2.1':'Categorías de espacios de espaciGo',
 'Tabla H.10.2':'Escenarios de volumen y ticket de espaciGo',
 'Figura 10':'Componentes de aplicación y adaptadores de espaciGo',
 'Figura 13':'Topología objetivo y ruta de entrega de espaciGo en AWS',
}
result_entries={}
for label,title in expected.items():
 index=tables if label.startswith('Tabla') else figures
 assert label+' '+title in index,(label,'índice incorrecto')
 body=[i+1 for i,p in enumerate(pages) if re.search(r'^'+re.escape(label)+r'\s*\n',p,re.M) and title in flat(p)]
 assert len(body)==1,(label,body)
 dests=set()
 for page in reader.pages[ti:ri]:
  for ref in page.get('/Annots',[]):
   dest=ref.get_object().get('/Dest')
   if dest and isinstance(dest,list):dests.add(reader.get_page_number(dest[0].get_object())+1)
 assert body[0] in dests,(label,'destino ausente')
 result_entries[label]={'titulo':title,'indice_correcto':True,'pagina_pdf_cuerpo':body[0],'destino_enlazado':True}
rnf='Requerimientos No Funcionales (RNF) — Sistema espaciGo';assert rnf in contents
assert not re.search(r'Sistema espacio\b',contents)
assert not re.search(r'(?:negocio|espacios|ticket|adaptadores|entrega) de espacio\b',tables+' '+figures)
# Las dos celdas del Anexo A deben mostrar el término completo en una línea.
pci=[]
for i,p in enumerate(pages):
 if 'Cumplimiento' in p and 'RNF-025' in p or 'Requerimientos' in p and 'Legislativos' in p and '025, 026, 027' in p:
  if 'PCI-DSS' in p:
   assert not re.search(r'PCI-\s*\n\s*DSS',p)
   pci.append(i+1)
assert len(pci)>=2,pci
result={'estado':'verificado','paginas_pdf':len(pages),'comillas_y_punto':'comillas dobles tipográficas y punto unido al cierre en fuente, Word y PDF','capitalizacion_tabla_10':'Entorno con mayúscula','pci_dss':'guion ASCII, término íntegro en una línea en detalle y resumen','paginas_pci_dss':pci,'tabla_contenido_rnf':'espaciGo comprobado dentro del índice','entradas_verificadas':result_entries,'docx_sha256':hashlib.sha256((T/'build/Tesis_Final_espaciGo.docx').read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256((T/'build/Tesis_Final_espaciGo.pdf').read_bytes()).hexdigest()}
(OUT/'VERIFICACION_FINAL.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
