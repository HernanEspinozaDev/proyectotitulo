#!/usr/bin/env python3
from pathlib import Path
import sys, re, zipfile
import xml.etree.ElementTree as ET
sys.path.insert(0, '/home/nandev/Documentos/projects/espaciGo/ES2/docskill')
from docskill.api import DocSkillProject
from docskill.style_profile import load_style_profile, _role_texts
from docskill.pandoc_ast import load_ast

proj = DocSkillProject.open('/home/nandev/Documentos/projects/espaciGo/ES2/informe_docskill')
state, diags = load_style_profile(proj.root, proj.root / 'build', proj.document.to_dict())
print('load_style_profile diags:', diags)

asts = [load_ast(proj.root / s) for s in proj.document.sections]
expected_texts = [text for ast in asts for text in _role_texts(ast, 'body')]
style_ids = state.role_style_ids.get('body', [])
print('style_ids for body:', style_ids)

docx_path = proj.root / 'build/Informe_Desarrollo_e_Implementacion_espaciGo.docx'
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
with zipfile.ZipFile(docx_path) as package:
    document = ET.fromstring(package.read('word/document.xml'))
    paragraphs = []
    for paragraph in document.findall(f'.//{W}p'):
        p_style = paragraph.find(f'{W}pPr/{W}pStyle')
        style_id = p_style.get(f'{W}val') if p_style is not None else 'Normal'
        text = ''.join(node.text or '' for node in paragraph.findall(f'.//{W}t'))
        paragraphs.append((text.strip(), style_id))

def has_expected_style(text: str) -> bool:
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

unmatched = []
for t in expected_texts:
    if not has_expected_style(t):
        unmatched.append(t)
print(f'Total expected body: {len(expected_texts)}, unmatched: {len(unmatched)}')
for u in unmatched[:10]:
    # find where u is in paragraphs
    actual_match = [p for p in paragraphs if u[:30] in p[0]]
    print('UNMATCHED:', repr(u[:80]), 'actual match in docx:', actual_match)
