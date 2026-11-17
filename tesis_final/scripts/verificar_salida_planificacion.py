"""Comprueba rótulos, destinos e imágenes en los entregables Word/PDF."""
from pathlib import Path
import hashlib,json,re,zipfile
from lxml import etree as E
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[2];T=ROOT/'tesis_final';OUT=ROOT/'preparacion_planificacion_pmbok/04_ejecucion';W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
reader=PdfReader(T/'build/Tesis_Final_espaciGo.pdf');pages=[p.extract_text() or '' for p in reader.pages]
sources=(T/'sections/06-capitulo-vi.md').read_text()+(T/'appendices/g-carta-gantt-detallada.md').read_text()
expected_tables=set(re.findall(r'\*\*Tabla ((?:G\.)?\d+(?:\.\d+)?)\*\*',sources));expected_figures=set(re.findall(r'\*\*Figura ((?:G\.)?\d+)\*\*',sources))
found={'Tabla':{},'Figura':{}}
for i,text in enumerate(pages):
    for kind,expected in [('Tabla',expected_tables),('Figura',expected_figures)]:
        for key in re.findall(r'^'+kind+r' ((?:G\.)?\d+(?:\.\d+)?)\s*\n',text,re.M):
            if key in expected:
                assert key not in found[kind],(kind,key)
                found[kind][key]=i+1
                if kind=='Figura':assert len(list(reader.pages[i].images))>=2,(key,'imagen ausente')
assert set(found['Tabla'])==expected_tables and set(found['Figura'])==expected_figures
# Los índices de captions deben enlazar a todas las páginas de planificación.
destinations=set()
for page in reader.pages[:35]:
    for ref in page.get('/Annots',[]):
        annot=ref.get_object();dest=annot.get('/Dest')
        if dest and isinstance(dest,list):destinations.add(reader.get_page_number(dest[0].get_object())+1)
assert set(found['Tabla'].values())|set(found['Figura'].values()) <= destinations
with zipfile.ZipFile(T/'build/Tesis_Final_espaciGo.docx') as z:
    xml=E.fromstring(z.read('word/document.xml'));b=xml.find(W+'body');paras=list(b)
    for i,node in enumerate(paras):
        text=''.join(node.itertext()).strip()
        if node.tag==W+'p' and re.match(r'^EDT 1\.\d\.\d',text):assert node.find(W+'pPr/'+W+'keepNext') is not None
    settings=E.fromstring(z.read('word/settings.xml'));assert settings.find(W+'updateFields') is not None
assert not re.search(r'@(pmbok|es2sapag)', '\n'.join(pages))
result={'estado':'verificado','paginas_pdf':len(pages),'paginas_tablas':found['Tabla'],'paginas_figuras':found['Figura'],'indices_enlazados':True,'figuras_con_imagen_en_pagina':True,'fichas_edt_sin_titulo_huerfano':True,'docx_sha256':hashlib.sha256((T/'build/Tesis_Final_espaciGo.docx').read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256((T/'build/Tesis_Final_espaciGo.pdf').read_bytes()).hexdigest(),'revision_visual':'Word renderizado con render_docx.py; PDF completo renderizado y páginas modificadas inspeccionadas en paneles y figuras ampliadas.'}
(OUT/'verificacion_word_pdf.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
