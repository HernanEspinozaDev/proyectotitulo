"""Reconstruye rótulos académicos desde textos canónicos antes de generar índices."""
from lxml import etree as E
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
CAPTIONS={
 'Tabla 4':'Lienzo del modelo de negocio de espaciGo',
 'Tabla H.2.1':'Categorías de espacios de espaciGo',
 'Tabla H.10.2':'Escenarios de volumen y ticket de espaciGo',
 'Figura 10':'Componentes de aplicación y adaptadores de espaciGo',
 'Figura 13':'Topología objetivo y ruta de entrega de espaciGo en AWS',
}
RNF_HEADING='Requerimientos No Funcionales (RNF) — Sistema espaciGo'

def canonical_academic_labels(body):
    found={label:0 for label in CAPTIONS};rnf=0
    for paragraph in body.findall(W+'p'):
        text=''.join(t.text or '' for t in paragraph.iter(W+'t')).strip()
        key=next((label for label,title in CAPTIONS.items()
                  if text.startswith(label) and text[len(label):].lstrip().startswith(title.split()[0])),None)
        heading=text.startswith('Requerimientos No Funcionales (RNF)') and 'Sistema ' in text
        if key is None and not heading:continue
        for child in list(paragraph):
            if child.tag in [W+'r',W+'hyperlink']:paragraph.remove(child)
        def run(value,bold=False,italic=False):
            r=E.SubElement(paragraph,W+'r');p=E.SubElement(r,W+'rPr');E.SubElement(p,W+'noProof')
            if bold:E.SubElement(p,W+'b')
            if italic:E.SubElement(p,W+'i')
            E.SubElement(r,W+'t').text=value
        if heading:
            run(RNF_HEADING);rnf+=1
        else:
            run(key,bold=True);E.SubElement(E.SubElement(paragraph,W+'r'),W+'br');run(CAPTIONS[key],italic=True);found[key]+=1
    assert all(n==1 for n in found.values()),found
    assert rnf==1,rnf
    return len(found)+rnf
