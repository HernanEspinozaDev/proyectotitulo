import zipfile, xml.etree.ElementTree as ET

z = zipfile.ZipFile('ES2/informe_docskill/build/Informe_Desarrollo_e_Implementacion_espaciGo.docx')
root = ET.fromstring(z.read('word/document.xml'))
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
body = root.find(f'{W}body')
print('Total child elements in body:', len(list(body)))
for i, child in enumerate(list(body)[:20]):
    tag = child.tag.replace(W, 'w:')
    texts = [t.text for t in child.iter(f'{W}t') if t.text]
    pStyle = child.find(f'{W}pPr/{W}pStyle')
    style_val = pStyle.get(f'{W}val') if pStyle is not None else None
    print(f'{i+1:2d}: {tag} [style={style_val}] -> {" ".join(texts)[:80]}')
