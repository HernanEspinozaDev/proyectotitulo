"""Conserva PCI-DSS con guion ASCII y completo en las celdas del Anexo A."""
from copy import deepcopy
from lxml import etree as E
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
XML='{http://www.w3.org/XML/1998/namespace}'

def format_final_typography(body):
    active=False;count=0
    for node in body:
        label=''.join(node.itertext()).strip()
        if node.tag==W+'p' and label.startswith(('CAPÍTULO ','ANEXO ','Material Complementario')):active=label.startswith('ANEXO A:')
        if not active or node.tag!=W+'tbl':continue
        for paragraph in node.iter(W+'p'):
            value=''.join(t.text or '' for t in paragraph.iter(W+'t'))
            if 'PCI-DSS' not in value:continue
            if not value.startswith(('Cumplimiento ','Estándares ')):continue
            start=value.index('PCI-DSS');end=start+len('PCI-DSS')
            if start and value[start-1]=='(':
                start-=1
                if value[end:end+1]==')':end+=1
            pr=paragraph.find(W+'pPr')
            if pr is None:pr=E.Element(W+'pPr');paragraph.insert(0,pr)
            hyphens=pr.find(W+'suppressAutoHyphens')
            if hyphens is None:hyphens=E.SubElement(pr,W+'suppressAutoHyphens')
            hyphens.set(W+'val','1')
            runpr=paragraph.find(W+'r/'+W+'rPr')
            runpr=deepcopy(runpr) if runpr is not None else E.Element(W+'rPr')
            for child in list(paragraph):
                if child.tag!=W+'pPr':paragraph.remove(child)
            def run(text):
                r=E.SubElement(paragraph,W+'r');r.append(deepcopy(runpr));t=E.SubElement(r,W+'t');t.set(XML+'space','preserve');t.text=text
            run(value[:start]);E.SubElement(E.SubElement(paragraph,W+'r'),W+'br')
            run(value[start:end]);run(value[end:]);count+=1
    if count!=2:raise ValueError(f'Se esperaban dos celdas PCI-DSS: {count}')
    return count
