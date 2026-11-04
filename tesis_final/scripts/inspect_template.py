import zipfile, xml.etree.ElementTree as ET

z = zipfile.ZipFile('ES2/informe_docskill/templates/reference-inacap.docx')
print('Files in reference docx:', z.namelist())
xml_content = z.read('word/document.xml').decode('utf-8')
print('Document length:', len(xml_content))
root = ET.fromstring(xml_content)
# Find text elements
texts = [t.text for t in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
print('Sample texts in template:', texts[:30])
