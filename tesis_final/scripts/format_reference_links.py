"""Conserva dos enlaces bibliográficos completos y separados del texto de la referencia."""
from copy import deepcopy
from lxml import etree as E
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
URLS=(
    'https://www.bcn.cl/leychile/navegar?idNorma=1209272',
    'https://postgis.net/docs/ST_DWithin.html',
)

def format_reference_links(body):
    count=0
    for paragraph in body.findall(W+'p'):
        for link in paragraph.findall(W+'hyperlink'):
            url=''.join(t.text or '' for t in link.iter(W+'t'))
            if url not in URLS:continue
            props=paragraph.find(W+'pPr')
            if props is None:props=E.Element(W+'pPr');paragraph.insert(0,props)
            for name in ['keepLines','suppressAutoHyphens']:
                element=props.find(W+name)
                if element is None:element=E.SubElement(props,W+name)
                element.set(W+'val','1')
            # La referencia permanece en una página; el URL ocupa su propia línea.
            previous=link.getprevious()
            if previous is None or previous.find(W+'br') is None:
                br=E.Element(W+'r');E.SubElement(br,W+'br');paragraph.insert(list(paragraph).index(link),br)
            original=link.find(W+'r/'+W+'rPr')
            original=deepcopy(original) if original is not None else E.Element(W+'rPr')
            if url.endswith('/ST_DWithin.html'):
                # El subrayado del hipervínculo puede confundirse con el guion bajo.
                underline=original.find(W+'u')
                if underline is None:underline=E.SubElement(original,W+'u')
                underline.set(W+'val','none')
            for node in list(link):link.remove(node)
            run=E.SubElement(link,W+'r');run.append(original)
            # Un único nodo visible, con el guion bajo ASCII original intacto.
            E.SubElement(run,W+'t').text=url
            count+=1
    if count!=len(URLS):raise ValueError(f'Se esperaban {len(URLS)} enlaces bibliográficos; se encontraron {count}.')
    return count
