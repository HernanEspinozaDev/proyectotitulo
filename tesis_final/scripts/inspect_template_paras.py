import zipfile, xml.etree.ElementTree as ET

z = zipfile.ZipFile('ES2/informe_docskill/templates/reference-inacap.docx')
root = ET.fromstring(z.read('word/document.xml'))
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
for i, p in enumerate(root.iter(f'{W}p')):
    texts = [t.text for t in p.iter(f'{W}t') if t.text]
    if texts:
        print(f'P{i+1}:', ''.join(texts))
