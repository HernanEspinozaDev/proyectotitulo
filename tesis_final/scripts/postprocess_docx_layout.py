#!/usr/bin/env python3
"""Aplica layout reproducible al DOCX generado, sin modificar plantilla/fuentes.
- Portada técnica limpia, bajo el encabezado gráfico INACAP, y salto al Índice.
- Bloque TOC (w:sdt) en la página 2 con salto de página hacia el Capítulo 1.
- Capítulo 1 iniciando limpio en la página 3.
- Saltos de página antes de cada Capítulo principal (Ttulo10) y Anexo.
"""
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
import os
import tempfile
import re

DOCX_PATH = Path('/home/nandev/Documentos/projects/espaciGo/ES2/informe_docskill/build/Informe_Desarrollo_e_Implementacion_espaciGo.docx')
W_NAMESPACE = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
ET.register_namespace('w', W_NAMESPACE)
W = f'{{{W_NAMESPACE}}}'

def apa_table_rules(body):
    """Reglas APA visibles: superior, inferior y debajo del encabezado.

    Se eliminan bordes verticales/celda heredados para evitar que la referencia
    institucional deje tablas sin líneas o convierta la salida en una cuadrícula.
    """
    total = 0
    for table in body.iter(f'{W}tbl'):
        pr = table.find(f'{W}tblPr')
        if pr is None:
            pr=ET.Element(f'{W}tblPr');table.insert(0,pr)
        for old in list(pr.findall(f'{W}tblBorders')):pr.remove(old)
        borders=ET.SubElement(pr,f'{W}tblBorders')
        for edge in ['top','left','bottom','right','insideH','insideV']:
            line=ET.SubElement(borders,f'{W}{edge}')
            line.set(f'{W}val','single' if edge in ['top','bottom'] else 'nil')
            if edge in ['top','bottom']:
                line.set(f'{W}sz','8');line.set(f'{W}color','202020');line.set(f'{W}space','0')
        # Evita cambios de ancho fuera de los márgenes y deja el ancho disponible
        # a la cuadrícula de columnas que Pandoc ya calculó.
        width=pr.find(f'{W}tblW')
        if width is not None:width.set(f'{W}type','pct');width.set(f'{W}w','5000')
        for row_index,row in enumerate(table.findall(f'{W}tr')):
            rpr=row.find(f'{W}trPr')
            is_header=row_index==0 or (rpr is not None and rpr.find(f'{W}tblHeader') is not None)
            if is_header:
                if rpr is None:rpr=ET.Element(f'{W}trPr');row.insert(0,rpr)
                if rpr.find(f'{W}tblHeader') is None:ET.SubElement(rpr,f'{W}tblHeader')
            for cell in row.findall(f'{W}tc'):
                cp=cell.find(f'{W}tcPr')
                if cp is None:cp=ET.Element(f'{W}tcPr');cell.insert(0,cp)
                for old in list(cp.findall(f'{W}tcBorders')):cp.remove(old)
                cb=ET.SubElement(cp,f'{W}tcBorders')
                for edge in ['top','left','bottom','right']:
                    line=ET.SubElement(cb,f'{W}{edge}')
                    draw=(row_index==0 and edge=='top') or (is_header and edge=='bottom') or (row_index==len(table.findall(f'{W}tr'))-1 and edge=='bottom')
                    line.set(f'{W}val','single' if draw else 'nil')
                    if draw:line.set(f'{W}sz','8' if edge=='top' or not is_header else '6');line.set(f'{W}color','202020')
        total+=1
    print(f'{total} tablas con reglas horizontales APA explícitas y encabezados repetibles.')

def portrait_bpmn_blocks(body):
    """Mantiene número, título, gráfico y nota en una hoja vertical, sin duplicar pie."""
    WP='{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}'
    children=list(body)
    remove=[]
    for index,p in enumerate(children):
        desc=p.find(f'.//{WP}docPr')
        if desc is None or not desc.get('descr','').startswith('Diagrama BPMN vertical'):
            continue
        # La leyenda automática de Pandoc duplica el título APA escrito antes.
        for after in children[index+1:index+3]:
            if after.tag!=f'{W}p':continue
            style=after.find(f'{W}pPr/{W}pStyle')
            if style is not None and style.get(f'{W}val') in ['ImageCaption','Caption','PIEDEFOTO']:
                remove.append(after)
            break
        preceding=[c for c in children[max(0,index-7):index] if c.tag==f'{W}p']
        for before in preceding[-2:]:
            pp=before.find(f'{W}pPr')
            if pp is None:pp=ET.Element(f'{W}pPr');before.insert(0,pp)
            if pp.find(f'{W}keepNext') is None:ET.SubElement(pp,f'{W}keepNext')
            text=''.join(t.text or '' for t in before.iter(f'{W}t')).strip()
            if re.fullmatch(r'Figura [123]',text) and pp.find(f'{W}pageBreakBefore') is None:
                ET.SubElement(pp,f'{W}pageBreakBefore')
        pp=p.find(f'{W}pPr')
        if pp is None:pp=ET.Element(f'{W}pPr');p.insert(0,pp)
        if pp.find(f'{W}keepNext') is None:ET.SubElement(pp,f'{W}keepNext')
        jc=pp.find(f'{W}jc')
        if jc is None:jc=ET.SubElement(pp,f'{W}jc')
        jc.set(f'{W}val','center')
    for p in remove:body.remove(p)
    print(f'BPMN verticales: retirados {len(remove)} pies automáticos duplicados.')

def make_page_break():
    p = ET.Element(f'{W}p')
    r = ET.SubElement(p, f'{W}r')
    br = ET.SubElement(r, f'{W}br')
    br.set(f'{W}type', 'page')
    return p

def make_meta_p(label, value, space_after=140):
    p = ET.Element(f'{W}p')
    pPr = ET.SubElement(p, f'{W}pPr')
    spacing = ET.SubElement(pPr, f'{W}spacing')
    spacing.set(f'{W}after', str(space_after))
    
    r1 = ET.SubElement(p, f'{W}r')
    rPr1 = ET.SubElement(r1, f'{W}rPr')
    ET.SubElement(rPr1, f'{W}b')
    sz1 = ET.SubElement(rPr1, f'{W}sz')
    sz1.set(f'{W}val', '22')
    t1 = ET.SubElement(r1, f'{W}t')
    t1.text = label + ': '
    
    r2 = ET.SubElement(p, f'{W}r')
    rPr2 = ET.SubElement(r2, f'{W}rPr')
    sz2 = ET.SubElement(rPr2, f'{W}sz')
    sz2.set(f'{W}val', '22')
    t2 = ET.SubElement(r2, f'{W}t')
    t2.text = value
    return p

def make_space_p(height=600):
    p = ET.Element(f'{W}p')
    pPr = ET.SubElement(p, f'{W}pPr')
    spacing = ET.SubElement(pPr, f'{W}spacing')
    spacing.set(f'{W}after', str(height))
    return p

def make_cover_line(text, size, bold=False, after=260):
    p = ET.Element(f'{W}p')
    pPr = ET.SubElement(p, f'{W}pPr')
    jc = ET.SubElement(pPr, f'{W}jc'); jc.set(f'{W}val', 'center')
    spacing = ET.SubElement(pPr, f'{W}spacing'); spacing.set(f'{W}after', str(after))
    r = ET.SubElement(p, f'{W}r'); rp = ET.SubElement(r, f'{W}rPr')
    if bold: ET.SubElement(rp, f'{W}b')
    sz = ET.SubElement(rp, f'{W}sz'); sz.set(f'{W}val', str(size))
    t = ET.SubElement(r, f'{W}t'); t.text = text
    return p

def adjust_layout():
    if not DOCX_PATH.exists():
        print('DOCX no existe')
        return
        
    # El reemplazo atómico debe ocurrir dentro del mismo sistema de archivos.
    temp_dir = tempfile.mkdtemp(prefix='.layout-', dir=DOCX_PATH.parent)
    temp_docx = Path(temp_dir) / 'adjusted.docx'
    
    with zipfile.ZipFile(DOCX_PATH, 'r') as zin, zipfile.ZipFile(temp_docx, 'w') as zout:
        for item in zin.infolist():
            content = zin.read(item.filename)
            if item.filename == 'word/document.xml':
                root = ET.fromstring(content)
                body = root.find(f'{W}body')
                children = list(body)
                
                sdt_idx = None
                first_h1_idx = None
                
                for idx, child in enumerate(children):
                    if child.tag == f'{W}sdt' and sdt_idx is None:
                        sdt_idx = idx
                    elif sdt_idx is not None and first_h1_idx is None and child.tag == f'{W}p':
                        pStyle = child.find(f'{W}pPr/{W}pStyle')
                        if pStyle is not None and pStyle.get(f'{W}val') in ('Ttulo10', 'Heading1', 'Ttulo1'):
                            first_h1_idx = idx
                            
                print(f'TOC sdt en index {sdt_idx}, primer Heading1 en index {first_h1_idx}')
                
                new_children = []
                
                # La plantilla aporta el encabezado gráfico; se descartan el título
                # automático de Pandoc (que invade el logotipo) y datos no confirmados.
                new_children.append(make_space_p(7200))
                new_children.append(make_cover_line('Desarrollo e implementación de la solución informática', 30, True, 300))
                new_children.append(make_cover_line('espaciGo — ES2', 26, False, 180))
                new_children.append(make_cover_line('Informe técnico · INACAP', 22, False, 300))
                
                # Salto de página entre Portada y TOC
                new_children.append(make_page_break())
                
                # 2. Bloque TOC y elementos intermedios (bookmarks) antes de primer h1
                for idx in range(sdt_idx, first_h1_idx):
                    new_children.append(children[idx])
                    
                # Salto de página entre TOC y Capítulo 1
                new_children.append(make_page_break())
                
                # 3. Capítulos y Anexos (saltos de página antes de cada Heading 1 posterior)
                for idx in range(first_h1_idx, len(children)):
                    child = children[idx]
                    if child.tag == f'{W}p' and idx > first_h1_idx:
                        pStyle = child.find(f'{W}pPr/{W}pStyle')
                        if pStyle is not None and pStyle.get(f'{W}val') in ('Ttulo10', 'Heading1', 'Ttulo1'):
                            new_children.append(make_page_break())
                    new_children.append(child)

                # Evita dividir filas largas entre páginas y conserva la fila
                # de cabecera repetible que produce Pandoc.
                for tr in body.iter(f'{W}tr'):
                    trpr = tr.find(f'{W}trPr')
                    if trpr is None:
                        trpr = ET.Element(f'{W}trPr'); tr.insert(0, trpr)
                    if trpr.find(f'{W}cantSplit') is None: ET.SubElement(trpr, f'{W}cantSplit')
                    
                body.clear()
                for c in new_children:
                    body.append(c)

                apa_table_rules(body)
                portrait_bpmn_blocks(body)
                    
                content = ET.tostring(root, encoding='utf-8')
                
            zout.writestr(item, content)
            
    os.replace(temp_docx, DOCX_PATH)
    print('DOCX portada y layout ajustados con éxito!')

if __name__ == '__main__':
    adjust_layout()
