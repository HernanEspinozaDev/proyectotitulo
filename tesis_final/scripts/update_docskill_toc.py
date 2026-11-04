#!/usr/bin/env python3
"""Actualiza el TOC con páginas reales y exporta usando el LibreOffice aislado."""
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unicodedata
import uuid
import xml.etree.ElementTree as ET
import zipfile

BASE_DIR = Path(__file__).resolve().parent.parent
DOCX_PATH = BASE_DIR / 'build' / 'Informe_Desarrollo_e_Implementacion_espaciGo.docx'
PDF_PATH = BASE_DIR / 'build' / 'Informe_Desarrollo_e_Implementacion_espaciGo.pdf'
SOFFICE = Path(os.environ.get('ES2_SOFFICE', '/home/nandev/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/program/soffice'))
PDFTOTEXT = Path('/usr/bin/pdftotext')
WNS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
ET.register_namespace('w', WNS)
W = f'{{{WNS}}}'

def normalize(value):
    value = unicodedata.normalize('NFKD', value).casefold()
    value = ''.join(c for c in value if not unicodedata.combining(c))
    return ' '.join(re.findall(r'[a-z0-9]+', value))

def page_text(pdf):
    result = subprocess.run([str(PDFTOTEXT), '-layout', str(pdf), '-'], check=True, capture_output=True, text=True)
    pages = result.stdout.split('\f')
    if pages and not pages[-1].strip(): pages.pop()
    return pages

def render_pdf():
    if not SOFFICE.is_file(): raise FileNotFoundError(f'LibreOffice del runtime documental no encontrado: {SOFFICE}')
    with tempfile.TemporaryDirectory(prefix='es2-render-') as tmp:
        out = Path(tmp) / 'out'; profile = Path(tmp) / 'profile'; out.mkdir(); profile.mkdir()
        args = [str(SOFFICE), f'-env:UserInstallation={profile.as_uri()}', '--headless', '--nologo', '--nodefault', '--convert-to', 'pdf:writer_pdf_Export', '--outdir', str(out), str(DOCX_PATH)]
        result = subprocess.run(args, cwd=BASE_DIR, capture_output=True, text=True, timeout=360)
        candidate = out / (DOCX_PATH.stem + '.pdf')
        if result.returncode or not candidate.is_file() or candidate.stat().st_size == 0:
            raise RuntimeError('LibreOffice no exportó el PDF: ' + (result.stderr or result.stdout))
        fd, temp_path = tempfile.mkstemp(prefix='es2-rendered-', suffix='.pdf')
        os.close(fd); saved = Path(temp_path)
        shutil.copyfile(candidate, saved)
        return saved

def read_headings():
    with zipfile.ZipFile(DOCX_PATH) as z:
        root = ET.fromstring(z.read('word/document.xml'))
    headings = []
    for p in root.iter(f'{W}p'):
        style = p.find(f'{W}pPr/{W}pStyle')
        if style is None: continue
        sid = style.get(f'{W}val', '')
        level = {'Ttulo10':1, 'Heading1':1, 'Ttulo1':1, 'Ttulo2':2, 'Heading2':2, 'Ttulo3':3, 'Heading3':3}.get(sid)
        if not level: continue
        title = ''.join((t.text or '') for t in p.iter(f'{W}t')).strip()
        if not title: continue
        marks = [b.get(f'{W}name') for b in p.iter(f'{W}bookmarkStart') if b.get(f'{W}name') and not b.get(f'{W}name').startswith('_Toc')]
        headings.append({'title':title, 'level':level, 'anchor':marks[0] if marks else ''})
    if not headings: raise RuntimeError('No se encontraron títulos 1–3 en el DOCX.')
    return headings

def map_heading_pages(headings, pages):
    first = normalize(headings[0]['title'])
    occurrences = [i for i,p in enumerate(pages) if first and first in normalize(p)]
    if not occurrences: raise RuntimeError(f'El PDF no contiene el capítulo inicial: {headings[0]["title"]}')
    # La última aparición del primer título es su encabezado en el cuerpo; las
    # apariciones anteriores pertenecen al índice que se está actualizando.
    cursor = occurrences[-1]
    page_numbers = []
    missing = []
    for heading in headings:
        key = normalize(heading['title'])
        found = next((i for i in range(cursor, len(pages)) if key and key in normalize(pages[i])), None)
        if found is None:
            missing.append(heading['title'])
        else:
            page_numbers.append(found + 1); cursor = found
    if missing:
        raise RuntimeError(f'No se localizaron {len(missing)} encabezados del cuerpo en el PDF; primeros: {missing[:8]}')
    return page_numbers

def toc_template(level):
    p = ET.Element(f'{W}p'); ppr = ET.SubElement(p, f'{W}pPr')
    style = ET.SubElement(ppr, f'{W}pStyle'); style.set(f'{W}val', f'TOC{level}')
    tabs = ET.SubElement(ppr, f'{W}tabs')
    tab = ET.SubElement(tabs, f'{W}tab'); tab.set(f'{W}val','right'); tab.set(f'{W}pos','9403'); tab.set(f'{W}leader','dot')
    return p

def hyperlink_run(parent, text):
    run = ET.SubElement(parent, f'{W}r'); rp = ET.SubElement(run, f'{W}rPr')
    style = ET.SubElement(rp, f'{W}rStyle'); style.set(f'{W}val','Enlacedelindice')
    t = ET.SubElement(run, f'{W}t'); t.set('{http://www.w3.org/XML/1998/namespace}space','preserve'); t.text = text
    return run

def make_entry(heading, page):
    p = toc_template(heading['level'])
    link = ET.SubElement(p, f'{W}hyperlink')
    if heading['anchor']: link.set(f'{W}anchor', heading['anchor'])
    hyperlink_run(link, heading['title'])
    tab = ET.SubElement(link, f'{W}r'); ET.SubElement(tab, f'{W}tab')
    hyperlink_run(link, str(page))
    return p

def replace_toc_entries(headings, pages):
    with zipfile.ZipFile(DOCX_PATH, 'r') as zin:
        items = [(i, zin.read(i.filename)) for i in zin.infolist()]
    out = Path(tempfile.mkstemp(prefix='.toc-', suffix='.docx', dir=DOCX_PATH.parent)[1])
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as zout:
        for info, data in items:
            if info.filename == 'word/document.xml':
                root = ET.fromstring(data)
                sdt = next((x for x in root.iter(f'{W}sdt') if any('TOC' in (n.text or '') for n in x.iter(f'{W}instrText'))), None)
                if sdt is None: raise RuntimeError('No se encontró el campo TOC en el DOCX.')
                content = sdt.find(f'{W}sdtContent'); children = list(content)
                field_idx = next(i for i,x in enumerate(children) if x.tag == f'{W}p' and any('TOC' in (n.text or '') for n in x.iter(f'{W}instrText')))
                field_p = children[field_idx]
                # El resultado del campo ocupa los párrafos siguientes; quitamos
                # salidas previas para que el procedimiento sea idempotente.
                for child in children[field_idx+1:]:
                    style = child.find(f'{W}pPr/{W}pStyle') if child.tag == f'{W}p' else None
                    if style is not None and style.get(f'{W}val') in ('TOC1','TOC2','TOC3'): content.remove(child)
                end_marks = [x for x in field_p.iter(f'{W}fldChar') if x.get(f'{W}fldCharType') == 'end']
                for mark in end_marks:
                    parent = next((p for p in field_p.iter() if mark in list(p)), None)
                    if parent is not None: parent.remove(mark)
                insert_at = list(content).index(field_p) + 1
                entries = [make_entry(h, n) for h,n in zip(headings,pages)]
                for offset, entry in enumerate(entries): content.insert(insert_at+offset, entry)
                if entries:
                    end_p = entries[-1]; r = ET.SubElement(end_p, f'{W}r'); ET.SubElement(r, f'{W}fldChar').set(f'{W}fldCharType','end')
                data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
            zout.writestr(info, data)
    os.replace(out, DOCX_PATH)

def update_and_export():
    headings = read_headings()
    first_pdf = render_pdf()
    try:
        current = first_pdf
        stable = False
        history = []
        for iteration in range(1, 5):
            before = map_heading_pages(headings, page_text(current))
            replace_toc_entries(headings, before)
            rendered = render_pdf()
            after = map_heading_pages(headings, page_text(rendered))
            history.append({'iteration':iteration, 'entries':len(headings), 'stable':after == before, 'pages':max(after)})
            current.unlink(missing_ok=True)
            current = rendered
            if after == before:
                stable = True; break
        if not stable: raise RuntimeError('Los números del índice no se estabilizaron tras cuatro renderizados.')
        # Confirmar que las páginas guardadas en el campo coinciden con el PDF
        # estable, y copiar únicamente el PDF de esta misma ejecución.
        check = map_heading_pages(headings, page_text(current))
        if check != after: raise RuntimeError('El mapa de títulos cambió después de estabilizar el TOC.')
        shutil.copyfile(current, PDF_PATH)
        print(f'Índice TOC con {len(headings)} títulos y páginas verificadas; renderizado estable en {len(history)} iteración(es).')
        for item in history: print(f'  iteración {item["iteration"]}: {item["entries"]} títulos; estable={item["stable"]}; última página de cuerpo={item["pages"]}')
        print(f'PDF final: {PDF_PATH.stat().st_size} bytes.')
    finally:
        first_pdf.unlink(missing_ok=True)
        if 'current' in locals() and current != first_pdf: current.unlink(missing_ok=True)

if __name__ == '__main__': update_and_export()
