"""Verifica texto y destino reales de los dos enlaces señalados por el revisor."""
from pathlib import Path
from lxml import etree as E
from pypdf import PdfReader
import json,zipfile
from format_reference_links import URLS,W
ROOT=Path(__file__).resolve().parents[1]
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
with zipfile.ZipFile(ROOT/'build/Tesis_Final_espaciGo.docx') as z:
    document=E.fromstring(z.read('word/document.xml'))
    rels=E.fromstring(z.read('word/_rels/document.xml.rels'))
    targets={r.get('Id'):r.get('Target') for r in rels}
    found={}
    for paragraph in document.iter(W+'p'):
        for link in paragraph.findall(W+'hyperlink'):
            label=''.join(t.text or '' for t in link.iter(W+'t'))
            if label not in URLS:continue
            assert len(link.findall(W+'r'))==len(list(link.iter(W+'t')))==1
            assert targets[link.get(R+'id')]==label
            if label.endswith('/ST_DWithin.html'):assert link.find(W+'r/'+W+'rPr/'+W+'u').get(W+'val')=='none'
            assert paragraph.find(W+'pPr/'+W+'keepLines').get(W+'val')=='1'
            assert link.getprevious().find(W+'br') is not None
            assert label not in found
            found[label]={'xml_texto_integro':True,'destino_correcto':True,'referencia_sin_division_de_pagina':True}
    assert set(found)==set(URLS)
reader=PdfReader(ROOT/'build/Tesis_Final_espaciGo.pdf')
page_texts=[page.extract_text() or '' for page in reader.pages]
for url in URLS:
    matches=[]
    for i,page in enumerate(reader.pages):
        text=page_texts[i]
        lines=[line.strip() for line in text.splitlines()]
        if url in lines:
            assert '=1209272' not in lines
            assert 'https://postgis.net/docs/ST DWithin.html' not in text
            uris=[]
            for ref in page.get('/Annots',[]):
                action=ref.get_object().get('/A')
                if action:uris.append(str(action.get('/URI','')))
            assert url in uris,(url,'destino PDF ausente')
            matches.append(i+1)
    assert len(matches)==1,(url,matches)
    found[url].update(pagina_pdf=matches[0],url_completo_en_una_linea=True,destino_pdf_correcto=True)
result={'estado':'verificado','alcance':'dos referencias bibliográficas señaladas en la revisión de la versión 9; comprobación sobre la tesis actual','enlaces':found}
target=ROOT/'context/01_auditorias_y_rubricas/verificacion_enlaces_bibliograficos.json';target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
