"""Maquetación de tablas económicas dentro de la plantilla institucional.

Conserva las filas y columnas financieras. Limita los ajustes de tamaño y
paginación a Capítulo XIV y Anexo H; el resto de la tesis mantiene su estilo.
"""
from lxml import etree as E

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def child(parent, name):
    value = parent.find(W+name)
    if value is None:
        value = E.SubElement(parent, W+name)
    return value


def text(node):
    return ''.join(x.text or '' for x in node.iter(W+'t')).strip()


def format_economic_tables(body):
    section = body.find(W+'sectPr')
    page = section.find(W+'pgSz')
    margins = section.find(W+'pgMar')
    width = int(page.get(W+'w')) - int(margins.get(W+'left')) - int(margins.get(W+'right'))
    active = False
    count = 0
    for node in list(body):
        value = text(node)
        if node.tag == W+'p':
            if value.startswith(('CAPÍTULO ', 'ANEXO ', 'Material Complementario')):
                active = value.startswith(('CAPÍTULO XIV:', 'ANEXO H:'))
            continue
        if not active or node.tag != W+'tbl':
            continue
        count += 1
        rows = node.findall(W+'tr')
        columns = len(rows[0].findall(W+'tc'))
        first = text(rows[0].findall(W+'tc')[0])
        if columns == 6 and first.startswith('Partida'):
            weights = [.30]+[.14]*5
        elif columns == 6:
            weights = [.08]+[.184]*5
        elif columns == 5:
            weights = [.16]+[.21]*4
        elif columns == 4 and first == 'ID':
            weights = [.08, .30, .31, .31]
        elif columns == 4 and first.startswith('Modalidad'):
            weights = [.32, .18, .25, .25]
        elif columns == 4 and first == 'Variable':
            weights = [.26, .22, .26, .26]
        elif columns == 4 and first == 'Año':
            weights = [.12, .26, .36, .26]
        elif columns == 4:
            weights = [.28, .18, .27, .27]
        elif columns == 3 and first == 'Recurso':
            weights = [.30, .20, .50]
        elif columns == 3 and first == 'Concepto':
            weights = [.48, .26, .26]
        elif columns == 3:
            weights = [.45, .275, .275]
        elif columns == 2 and first in ['Componente', 'Cálculo']:
            weights = [.65, .35]
        elif columns == 2 and first == 'Categoría':
            weights = [.30, .70]
        else:
            weights = [.42, .58]
        widths = [round(width*x) for x in weights]
        widths[-1] += width-sum(widths)
        grid = node.find(W+'tblGrid')
        for col, size in zip(grid, widths):
            col.set(W+'w', str(size))
        pr = child(node, 'tblPr')
        child(pr, 'tblW').attrib.update({W+'w': str(width), W+'type': 'dxa'})
        padding = child(pr, 'tblCellMar')
        for edge, size in [('top', 30), ('bottom', 30), ('left', 70), ('right', 70)]:
            child(padding, edge).attrib.update({W+'w': str(size), W+'type': 'dxa'})
        for row in rows:
            child(child(row, 'trPr'), 'cantSplit')
            for cell, size in zip(row.findall(W+'tc'), widths):
                child(child(cell, 'tcPr'), 'tcW').attrib.update({W+'w': str(size), W+'type': 'dxa'})
                for para in cell.iter(W+'p'):
                    pp = child(para, 'pPr')
                    child(pp, 'spacing').attrib.update({W+'before': '0', W+'after': '0', W+'line': '240', W+'lineRule': 'auto'})
                    child(pp, 'keepNext')
                for run in cell.iter(W+'r'):
                    rp = child(run, 'rPr')
                    child(rp, 'sz').set(W+'val', '18')
                    child(rp, 'szCs').set(W+'val', '18')
        # El rótulo, el título, la tabla y su nota forman una unidad legible.
        caption = node.getprevious()
        if caption is not None and caption.tag == W+'p':
            child(child(caption, 'pPr'), 'keepNext')
        note = node.getnext()
        if note is not None and note.tag == W+'p' and text(note).startswith('Nota.'):
            child(child(note, 'pPr'), 'keepLines')
    return count
