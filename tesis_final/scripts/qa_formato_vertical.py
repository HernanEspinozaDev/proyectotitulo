#!/usr/bin/env python3
"""Comprueba reglas de tablas, geometría BPMN, orientación y copias finales.

Produce imágenes de todas las páginas y hojas de contacto para revisión humana;
no declara una aceptación académica por superar controles estructurales.
"""
from pathlib import Path
from zipfile import ZipFile
import hashlib
import json
import math
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
from pypdf import PdfReader
import pypdfium2 as pdfium

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT.parent/'.revision/qa_bordes_bpmn_vertical_final'
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
DOCX=ROOT/'build/Informe_Desarrollo_e_Implementacion_espaciGo.docx'
PDF=ROOT/'build/Informe_Desarrollo_e_Implementacion_espaciGo.pdf'


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    with ZipFile(DOCX) as z:
        body=ET.fromstring(z.read('word/document.xml')).find(W+'body')
        tables=list(body.iter(W+'tbl'))
        for table in tables:
            borders=table.find(W+'tblPr/'+W+'tblBorders')
            assert borders is not None
            for edge in ['top','bottom']:assert borders.find(W+edge).get(W+'val')=='single'
            for edge in ['left','right','insideH','insideV']:assert borders.find(W+edge).get(W+'val')=='nil'
            rows=table.findall(W+'tr');assert rows[0].find(W+'trPr/'+W+'tblHeader') is not None
            for cell in rows[0].findall(W+'tc'):
                assert cell.find(W+'tcPr/'+W+'tcBorders/'+W+'bottom').get(W+'val')=='single'
            grid=table.find(W+'tblGrid')
            if grid is not None:assert sum(int(c.get(W+'w')) for c in grid)<=12240-2836
    bpmn=[]
    for path in sorted((ROOT/'assets/figuras/fuentes').glob('fig0[123]_*.layout.json')):
        model=json.loads(path.read_text())
        for key,node in model['nodes'].items():
            x,y,w,h=node['bounds'];assert x>=25 and y>=77 and x+w<=975 and y+h<=1238,(path,key)
        # Detecta conectores que atraviesen una actividad ajena al flujo.
        for flow in model['flows']:
            for a,b in zip(flow['points'],flow['points'][1:]):
                for key,node in model['nodes'].items():
                    if key in [flow['source'],flow['target']]:continue
                    x,y,w,h=node['bounds']
                    if a[0]==b[0]:
                        crosses=x<a[0]<x+w and max(min(a[1],b[1]),y)<min(max(a[1],b[1]),y+h)
                    else:
                        crosses=y<a[1]<y+h and max(min(a[0],b[0]),x)<min(max(a[0],b[0]),x+w)
                    assert not crosses,(path.name,flow['source'],flow['target'],key)
        ET.parse(path.with_name(path.name.replace('.layout.json','.bpmn')))
        bpmn.append({'source':path.name,'nodes':len(model['nodes']),'flows':len(model['flows'])})
    reader=PdfReader(PDF)
    assert all(float(p.mediabox.width)<float(p.mediabox.height) for p in reader.pages)
    text=[p.extract_text() or '' for p in reader.pages]
    figure_pages={}
    for n in range(1,4):
        matches=[i+1 for i,t in enumerate(text) if f'Figura {n}\n' in t]
        assert len(matches)==1,(n,matches)
        page=reader.pages[matches[0]-1]
        assert len(page.images)>1,(n,'No hay imagen en la página del número de figura')
        assert 'Nota.' in text[matches[0]-1],(n,'Nota separada de la imagen')
        figure_pages[str(n)]=matches[0]
    manifest=json.loads((ROOT/'build/manifest.json').read_text())
    assert manifest['output']['sha256']==sha(DOCX)
    for kind in ['docx','pdf','markdown']:
        source=ROOT/manifest['final_artifacts'][kind]['path']
        assert manifest['final_artifacts'][kind]['sha256']==sha(source)
        ext='md' if kind=='markdown' else kind
        assert sha(ROOT.parent/f'Informe_Desarrollo_e_Implementacion_espaciGo_ES2.{ext}')==sha(source)
    pdf=pdfium.PdfDocument(str(PDF))
    contacts=[]
    for start in range(0,len(pdf),12):
        sheet=Image.new('RGB',(1488,1660),'#D9DDE3');draw=ImageDraw.Draw(sheet)
        for idx in range(start,min(start+12,len(pdf))):
            page=pdf[idx];bitmap=page.render(scale=1.3);img=bitmap.to_pil().convert('RGB')
            img.save(OUT/f'pagina-{idx+1:03}.png')
            thumb=img.copy();thumb.thumbnail((350,510))
            local=idx-start;x=(local%4)*372+11;y=(local//4)*550+28
            draw.text((x,y-20),f'Página {idx+1}',fill='black');sheet.paste(thumb,(x,y))
            bitmap.close();page.close()
        target=OUT/f'contacto-{start//12+1:02}.png';sheet.save(target);contacts.append(target.name)
    result={'pages':len(pdf),'orientation':'portrait in every page','tables_with_APA_rules':len(tables),
            'bpmn':bpmn,'figure_pages':figure_pages,'word_sha256':sha(DOCX),'pdf_sha256':sha(PDF),
            'copies_and_manifest_match':True,'contact_sheets':contacts,
            'scope':'Control técnico de formato; la inspección visual se registra por separado.'}
    (OUT/'resultado.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
