#!/usr/bin/env python3
from pathlib import Path
import json, subprocess, zipfile, re
import xml.etree.ElementTree as ET

root = Path('/home/nandev/Documentos/projects/espaciGo/ES2/informe_docskill')
pandoc_bin = root.parent / 'docskill/.tools/pandoc/bin/pandoc'

# 1. Obtenemos el AST de build/assembled.md
cmd = [str(pandoc_bin), str(root / 'build/assembled.md'), '-t', 'json']
res = subprocess.run(cmd, capture_output=True, text=True, check=True)
ast = json.loads(res.stdout)

# 2. Leemos style-profile-inacap.json
profile = json.loads((root / 'templates/style-profile-inacap.json').read_text())
style_ids = profile['roles']['body']['word_styles']
# Recordar que en template_adapter o en Word, Normal o FirstParagraph o BodyText pueden tener ID de estilo en Word
print('profile body styles:', style_ids)

# 3. Leemos los parrafos y sus style_id de build/Informe_Desarrollo_e_Implementacion_espaciGo.docx
docx_path = root / 'build/Informe_Desarrollo_e_Implementacion_espaciGo.docx'
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
with zipfile.ZipFile(docx_path) as package:
    doc_xml = ET.fromstring(package.read('word/document.xml'))
    paragraphs = []
    for p in doc_xml.findall(f'.//{W}p'):
        pPr = p.find(f'{W}pPr')
        pStyle = pPr.find(f'{W}pStyle') if pPr is not None else None
        s_val = pStyle.get(f'{W}val') if pStyle is not None else 'Normal'
        text = ''.join(node.text or '' for node in p.findall(f'.//{W}t'))
        paragraphs.append((text.strip(), s_val))

def _inline_text(value):
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return ''.join(_inline_text(item) for item in value)
    if isinstance(value, dict):
        t = value.get('t')
        c = value.get('c')
        if t in {'Str', 'Code', 'Math'}:
            return str(c if not isinstance(c, list) else c[-1])
        if t == 'Space':
            return ' '
        if t in {'SoftBreak', 'LineBreak'}:
            return '\n'
        return _inline_text(c)
    return ''

# Buscamos bloques Para o Plain
expected_texts = []
for block in ast.get('blocks', []):
    if block.get('t') in {'Para', 'Plain'}:
        txt = _inline_text(block.get('c')).strip()
        if txt:
            expected_texts.append(txt)

print(f'Total body texts in assembled.md: {len(expected_texts)}')

def has_expected_style(text):
    prefix = text[:40].strip()
    words = re.findall(r"[\w'-]+", text.casefold())
    phrases = [' '.join(words[index:index + size]) for size in (4, 3, 2) for index in range(max(0, len(words) - size + 1))]
    for actual, s_id in paragraphs:
        if s_id not in style_ids:
            continue
        rendered = re.sub(r'\s+', ' ', actual.casefold())
        if actual == text or (prefix and actual.startswith(prefix)):
            return True
        if any(phrase and phrase in rendered for phrase in phrases):
            return True
    return False

failing = []
for t in expected_texts:
    if not has_expected_style(t):
        failing.append(t)

print(f'Failing body paragraphs count: {len(failing)}')
for f in failing[:10]:
    print('FAILING:', repr(f[:100]))
    # Buscar que estilo tiene en docx
    matches = [p for p in paragraphs if f[:25] in p[0]]
    print('  in docx:', matches[:2])
