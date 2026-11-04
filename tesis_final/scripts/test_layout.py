#!/usr/bin/env python3
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
import os
import tempfile
import subprocess

BASE_DIR = Path('/home/nandev/Documentos/projects/espaciGo/ES2/informe_docskill')
DOCX_PATH = BASE_DIR / 'build' / 'Informe_Desarrollo_e_Implementacion_espaciGo.docx'
PDF_PATH = BASE_DIR / 'build' / 'Informe_Desarrollo_e_Implementacion_espaciGo.pdf'

W_NAMESPACE = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
ET.register_namespace('w', W_NAMESPACE)
W = f'{{{W_NAMESPACE}}}'

def make_page_break():
    p = ET.Element(f'{W}p')
    r = ET.SubElement(p, f'{W}r')
    br = ET.SubElement(r, f'{W}br')
    br.set(f'{W}type', 'page')
    return p

def make_meta_p(label, value, space_after=120):
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

def make_space_p(height=400):
    p = ET.Element(f'{W}p')
    pPr = ET.SubElement(p, f'{W}pPr')
    spacing = ET.SubElement(pPr, f'{W}spacing')
    spacing.set(f'{W}after', str(height))
    return p

def adjust_layout():
    temp_dir = tempfile.mkdtemp()
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
                    elif child.tag == f'{W}p':
                        pStyle = child.find(f'{W}pPr/{W}pStyle')
                        val = pStyle.get(f'{W}val') if pStyle is not None else ''
                        if val in ('Heading1', 'Ttulo1') or 'Heading' in val or 'Ttulo' in val:
                            if first_h1_idx is None and (sdt_idx is not None and idx > sdt_idx):
                                first_h1_idx = idx
                            elif first_h1_idx is None and sdt_idx is None and idx > 1:
                                # Si no hay sdt pero hay Heading 1
                                first_h1_idx = idx
                                
                print(f'Detected: sdt_idx={sdt_idx}, first_h1_idx={first_h1_idx}')
                
                cutoff = sdt_idx if sdt_idx is not None else first_h1_idx
                new_children = []
                
                # Portada INACAP
                for idx in range(0, cutoff):
                    new_children.append(children[idx])
                    
                new_children.append(make_space_p(600))
                new_children.append(make_meta_p('Asignatura', 'Proyecto de Título — TIHI84'))
                new_children.append(make_meta_p('Carrera', 'Ingeniería en Informática'))
                new_children.append(make_meta_p('Institución', 'INACAP — Dirección Sectorial de Tecnologías de Información'))
                new_children.append(make_meta_p('Autor', 'Equipo de Desarrollo espaciGo'))
                new_children.append(make_meta_p('Fecha de Entrega', '3 de noviembre de 2026'))
                new_children.append(make_meta_p('Sede y Ubicación', 'Santiago de Chile'))
                new_children.append(make_page_break())
                
                if sdt_idx is not None:
                    new_children.append(children[sdt_idx])
                    new_children.append(make_page_break())
                    
                start_rest = first_h1_idx if first_h1_idx is not None else (sdt_idx + 1 if sdt_idx is not None else cutoff)
                for idx in range(start_rest, len(children)):
                    child = children[idx]
                    if child.tag == f'{W}p':
                        pStyle = child.find(f'{W}pPr/{W}pStyle')
                        val = pStyle.get(f'{W}val') if pStyle is not None else ''
                        if (val in ('Heading1', 'Ttulo1') or val.startswith('Heading1')) and idx > start_rest:
                            new_children.append(make_page_break())
                    new_children.append(child)
                    
                body.clear()
                for c in new_children:
                    body.append(c)
                content = ET.tostring(root, encoding='utf-8')
            zout.writestr(item, content)
            
    os.replace(temp_docx, DOCX_PATH)
    print('DOCX portada y saltos ajustados.')

if __name__ == '__main__':
    adjust_layout()
