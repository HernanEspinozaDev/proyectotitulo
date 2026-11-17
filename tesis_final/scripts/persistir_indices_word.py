"""Transfiere exclusivamente los índices calculados por Writer al Word de DocSkill.

No se sustituye el cuerpo por la conversión de Writer: se conservan sus tablas,
imágenes, estilos existentes y XML. Se agregan los marcadores de navegación que
necesitan los resultados de los campos y los estilos nuevos de esos resultados.
"""
from copy import deepcopy
from difflib import SequenceMatcher
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree as E

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def text(node):
    return ' '.join(''.join(t.text or '' for t in node.iter(W+'t')).split())


def outside_indexes(root):
    return [p for p in root.iter(W+'p')
            if not any(a.tag == W+'sdt' for a in p.iterancestors())]


def persist_indexes(source, calculated):
    with ZipFile(source) as original, ZipFile(calculated) as saved:
        parts = {item.filename: original.read(item.filename) for item in original.infolist()}
        root = E.fromstring(parts['word/document.xml'])
        donor = E.fromstring(saved.read('word/document.xml'))
        indexes = list(donor.find(W+'body').findall(W+'sdt'))
        assert len(indexes) == 3, 'Se esperan contenido, tablas y figuras.'
        assert all(n.find('.//'+W+'instrText') is not None for n in indexes)
        originals, donors = outside_indexes(root), outside_indexes(donor)
        original_text, donor_text = list(map(text, originals)), list(map(text, donors))
        # La correspondencia secuencial desambigua títulos repetidos, por ejemplo
        # «Criterios de Aceptación», sin depender de los IDs privados de Writer.
        aligned = {}
        for block in SequenceMatcher(None, donor_text, original_text, autojunk=False).get_matching_blocks():
            for offset in range(block.size):
                aligned[donors[block.a+offset]] = originals[block.b+offset]
        required = {link.get(W+'anchor') for index in indexes
                    for link in index.iter(W+'hyperlink') if link.get(W+'anchor')}
        known = {b.get(W+'name') for b in root.iter(W+'bookmarkStart')}
        next_id = max(int(b.get(W+'id')) for b in root.iter(W+'bookmarkStart')) + 1
        added = 0
        for bookmark in donor.iter(W+'bookmarkStart'):
            name = bookmark.get(W+'name')
            if name not in required or name in known:
                continue
            paragraph = next((p for p in bookmark.iterancestors() if p.tag == W+'p'), None)
            assert paragraph in aligned, ('Marcador sin correspondencia', name, text(paragraph))
            target = aligned[paragraph]
            start = E.Element(W+'bookmarkStart', {W+'id': str(next_id), W+'name': name})
            end = E.Element(W+'bookmarkEnd', {W+'id': str(next_id)})
            position = 1 if len(target) and target[0].tag == W+'pPr' else 0
            target.insert(position, start)
            target.append(end)
            next_id += 1; added += 1; known.add(name)
        assert required <= known, sorted(required-known)
        body = root.find(W+'body')
        content = next(node for node in body.findall(W+'sdt')
                       if node.find('.//'+W+'instrText') is not None)
        body.replace(content, deepcopy(indexes[0]))
        for index, title in zip(indexes[1:], ['Índice de Tablas', 'Índice de Figuras']):
            heading = next(p for p in body.findall(W+'p') if text(p) == title)
            field = body[list(body).index(heading)+1]
            assert field.find('.//'+W+'instrText') is not None, title
            body.replace(field, deepcopy(index))
        styles = E.fromstring(parts['word/styles.xml'])
        names = {s.get(W+'styleId') for s in styles}
        for style in E.fromstring(saved.read('word/styles.xml')):
            if style.tag == W+'style' and style.get(W+'styleId') not in names:
                styles.append(deepcopy(style))
                names.add(style.get(W+'styleId'))
        parts['word/document.xml'] = E.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
        parts['word/styles.xml'] = E.tostring(styles, xml_declaration=True, encoding='UTF-8', standalone=True)
    temporary = Path(str(source)+'.tmp')
    with ZipFile(temporary, 'w', ZIP_DEFLATED) as output:
        for name, data in parts.items():
            output.writestr(name, data)
    temporary.replace(source)
    return {'indices_guardados': len(indexes), 'marcadores_agregados': added,
            'entradas_enlazadas': sum(1 for i in indexes for _ in i.iter(W+'hyperlink'))}
