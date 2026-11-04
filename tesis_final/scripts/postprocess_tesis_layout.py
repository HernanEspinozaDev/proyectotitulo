#!/usr/bin/env python3
"""
postprocess_tesis_layout.py
Aplica post-procesamiento fino sobre el documento DOCX final:
1. Saltos de página automáticos (<w:pageBreakBefore/>) antes de cada Capítulo (I al XIV),
   Anexo (A al H) y secciones preliminares mayores.
2. keepWithNext en todos los encabezados (Ttulo10, Ttulo2, Ttulo3, Heading1-3).
3. Bordes de cuadrícula completos y visibles en TODAS las tablas (tblBorders: top, bottom, left, right, insideH, insideV).
4. Sombreado elegante en filas de encabezado de tabla (#EDEDED) y repetición de encabezado (tblHeader).
5. Títulos de Figuras APA 7 arriba: estilo oficial ImageCaption y keepNext (pegado a la imagen).
6. Centrado de imágenes y eliminación de cualquier título o pie duplicado abajo de la imagen.
"""

import json
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
import tempfile
import shutil
import re

ROOT = Path(__file__).resolve().parent.parent
DOCX_PATH = ROOT / 'build/Tesis_Final_espaciGo.docx'

W_NAMESPACE = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
ET.register_namespace('w', W_NAMESPACE)
W = f'{{{W_NAMESPACE}}}'

def postprocess():
    if not DOCX_PATH.exists():
        print(f"ERROR: {DOCX_PATH} no existe.")
        return

    with zipfile.ZipFile(DOCX_PATH, 'r') as zin:
        doc_xml = zin.read('word/document.xml')
        root = ET.fromstring(doc_xml)
        body = root.find(f'{W}body')

        metadata = json.loads((ROOT / 'document.json').read_text())['metadata']
        cover_title = next(
            (p for p in body.findall(f'{W}p') if
             ''.join(t.text or '' for t in p.iter(f'{W}t')) == metadata['title']),
            None,
        )
        if cover_title is not None:
            title_properties = cover_title.find(f'{W}pPr')
            if title_properties is None:
                title_properties = ET.Element(f'{W}pPr')
                cover_title.insert(0, title_properties)
            spacing = title_properties.find(f'{W}spacing')
            if spacing is None:
                spacing = ET.SubElement(title_properties, f'{W}spacing')
            spacing.set(f'{W}before', '1800')
            date_paragraph = next(
                (p for p in body.findall(f'{W}p') if
                 ''.join(t.text or '' for t in p.iter(f'{W}t')) == metadata['date']),
                None,
            )
            if date_paragraph is not None:
                authors = ' · '.join(metadata['authors'])
                if not any(''.join(t.text or '' for t in p.iter(f'{W}t')) == authors
                           for p in body.findall(f'{W}p')):
                    paragraph = ET.Element(f'{W}p')
                    run = ET.SubElement(paragraph, f'{W}r')
                    ET.SubElement(run, f'{W}t').text = authors
                    body.insert(list(body).index(date_paragraph), paragraph)

        modified_h1 = 0
        modified_tables = 0
        modified_captions = 0
        removed_duplicates = 0
        
        # 1. Page breaks and keepNext
        for p in body.iter(f'{W}p'):
            pPr = p.find(f'{W}pPr')
            pStyle = pPr.find(f'{W}pStyle') if pPr is not None else None
            sval = pStyle.get(f'{W}val') if pStyle is not None else ''
            text = ''.join(node.text or '' for node in p.findall(f'.//{W}t')).strip()
            
            is_chapter = text.startswith('CAPÍTULO ')
            is_annex = text.startswith('ANEXO ')
            is_major_prelim = text in [
                'Hoja de Aprobación Institucional',
                'Dedicatoria',
                'Agradecimientos',
                'Resumen ejecutivo',
                'Índice de Contenidos'
            ]
            
            if is_chapter or is_annex or (sval == 'Ttulo2' and is_major_prelim) or text == 'Índice de Contenidos':
                if pPr is None:
                    pPr = ET.Element(f'{W}pPr')
                    p.insert(0, pPr)
                if pPr.find(f'{W}pageBreakBefore') is None:
                    ET.SubElement(pPr, f'{W}pageBreakBefore')
                    modified_h1 += 1
            
            if sval in ['Ttulo10', 'Ttulo2', 'Ttulo3', 'Heading1', 'Heading2', 'Heading3']:
                if pPr is None:
                    pPr = ET.Element(f'{W}pPr')
                    p.insert(0, pPr)
                if pPr.find(f'{W}keepNext') is None:
                    ET.SubElement(pPr, f'{W}keepNext')

        # 2. ALL BORDERS MARKED for tables + shaded headers + full cell borders
        for tbl in body.iter(f'{W}tbl'):
            modified_tables += 1
            tblPr = tbl.find(f'{W}tblPr')
            if tblPr is None:
                tblPr = ET.Element(f'{W}tblPr')
                tbl.insert(0, tblPr)
            
            # Remove old borders
            for old in list(tblPr.findall(f'{W}tblBorders')):
                tblPr.remove(old)
            
            borders = ET.SubElement(tblPr, f'{W}tblBorders')
            for edge in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
                line = ET.SubElement(borders, f'{W}{edge}')
                line.set(f'{W}val', 'single')
                line.set(f'{W}sz', '4')
                line.set(f'{W}color', '000000')
                line.set(f'{W}space', '0')
            
            # Cell padding
            tblCellMar = tblPr.find(f'{W}tblCellMar')
            if tblCellMar is None:
                tblCellMar = ET.SubElement(tblPr, f'{W}tblCellMar')
                for m, val in [('top', '120'), ('bottom', '120'), ('left', '160'), ('right', '160')]:
                    m_el = ET.SubElement(tblCellMar, f'{W}{m}')
                    m_el.set(f'{W}w', val)
                    m_el.set(f'{W}type', 'dxa')

            # Rows: repeat header and shade first row
            rows = tbl.findall(f'{W}tr')
            for r_idx, row in enumerate(rows):
                trPr = row.find(f'{W}trPr')
                if trPr is None:
                    trPr = ET.Element(f'{W}trPr')
                    row.insert(0, trPr)
                
                if r_idx == 0:
                    if trPr.find(f'{W}tblHeader') is None:
                        ET.SubElement(trPr, f'{W}tblHeader')
                    
                    # Header cells shading and bold
                    for tc in row.findall(f'{W}tc'):
                        tcPr = tc.find(f'{W}tcPr')
                        if tcPr is None:
                            tcPr = ET.Element(f'{W}tcPr')
                            tc.insert(0, tcPr)
                        shd = tcPr.find(f'{W}shd')
                        if shd is None:
                            shd = ET.SubElement(tcPr, f'{W}shd')
                        shd.set(f'{W}val', 'clear')
                        shd.set(f'{W}color', 'auto')
                        shd.set(f'{W}fill', 'EDEDED')

        # Give the legal reference its own link line without changing the destination.
        for paragraph in body.findall(f'{W}p'):
            for link in paragraph.findall(f'{W}hyperlink'):
                label = ''.join(node.text or '' for node in link.iter(f'{W}t'))
                if label == 'https://www.bcn.cl/leychile/navegar?idNorma=1178004':
                    line_break = ET.Element(f'{W}r')
                    ET.SubElement(line_break, f'{W}br')
                    paragraph.insert(list(paragraph).index(link), line_break)

        # 3. Figure Titles above: assign ImageCaption style + keepNext; eliminate duplicate titles below
        children = list(body)
        paras_to_remove = set()
        
        for i, child in enumerate(children):
            if child.tag != f'{W}p':
                continue
            text = ''.join(child.itertext()).strip()

            # Keep the table label and title on the same page as the table.
            label = next(child.iter(f'{W}t'), None)
            if (label is not None
                    and re.fullmatch(r'Tabla (?:[A-Z]\.)?\d+(?:\.\d+)?', label.text or '')
                    and i + 1 < len(children)
                    and children[i + 1].tag == f'{W}tbl'):
                properties = child.find(f'{W}pPr')
                if properties is None:
                    properties = ET.Element(f'{W}pPr')
                    child.insert(0, properties)
                if properties.find(f'{W}keepNext') is None:
                    ET.SubElement(properties, f'{W}keepNext')
            
            # If paragraph starts with "Figura X" or "Figura C.X" -> assign ImageCaption + keepNext
            if re.match(r'^Figura\s+(\d+|[A-Z]\.\d+)', text):
                pPr = child.find(f'{W}pPr')
                if pPr is None:
                    pPr = ET.Element(f'{W}pPr')
                    child.insert(0, pPr)
                pStyle = pPr.find(f'{W}pStyle')
                if pStyle is None:
                    pStyle = ET.SubElement(pPr, f'{W}pStyle')
                pStyle.set(f'{W}val', 'ImageCaption')
                if pPr.find(f'{W}keepNext') is None:
                    ET.SubElement(pPr, f'{W}keepNext')
                modified_captions += 1
            
            # If paragraph contains an image/drawing
            if child.find(f'.//{W}drawing') is not None:
                pPr = child.find(f'{W}pPr')
                if pPr is None:
                    pPr = ET.Element(f'{W}pPr')
                    child.insert(0, pPr)
                if pPr.find(f'{W}keepNext') is None:
                    ET.SubElement(pPr, f'{W}keepNext')
                jc = pPr.find(f'{W}jc')
                if jc is None:
                    jc = ET.SubElement(pPr, f'{W}jc')
                jc.set(f'{W}val', 'center')
                
                # Check next 2 paragraphs for any duplicate caption below image
                for next_idx in range(i + 1, min(i + 3, len(children))):
                    next_el = children[next_idx]
                    if next_el.tag != f'{W}p':
                        continue
                    nxt_style = next_el.find(f'{W}pPr/{W}pStyle')
                    nxt_val = nxt_style.get(f'{W}val') if nxt_style is not None else ''
                    nxt_text = ''.join(next_el.itertext()).strip()
                    if nxt_val in ['ImageCaption', 'Caption', 'PIEDEFOTO'] and re.match(r'^Figura\s+(\d+|[A-Z]\.\d+)', nxt_text):
                        paras_to_remove.add(next_el)

        for p_rem in paras_to_remove:
            if p_rem in body:
                body.remove(p_rem)
                removed_duplicates += 1

        print(f"Postprocesamiento: {modified_h1} saltos de página antes de encabezados mayores.")
        print(f"Postprocesamiento: {modified_tables} tablas configuradas con bordes de cuadrícula completos y encabezados sombreados.")
        print(f"Postprocesamiento: {modified_captions} títulos de figuras formateados con estilo oficial ImageCaption y keepNext.")
        print(f"Postprocesamiento: {removed_duplicates} títulos duplicados debajo de imágenes eliminados.")

        new_doc_xml = ET.tostring(root, encoding='utf-8', xml_declaration=True)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as tmp_file:
            tmp_path = Path(tmp_file.name)

        with zipfile.ZipFile(DOCX_PATH, 'r') as zin, zipfile.ZipFile(tmp_path, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename == 'word/document.xml':
                    zout.writestr(item, new_doc_xml)
                else:
                    zout.writestr(item, zin.read(item.filename))

        shutil.move(str(tmp_path), str(DOCX_PATH))
        print("DOCX final actualizado con éxito!")

if __name__ == '__main__':
    postprocess()
