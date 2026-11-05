"""Transfer the presentation pages and section furniture from the TIHI84 reference."""
from copy import deepcopy
from pathlib import PurePosixPath
from lxml import etree as ET
from zipfile import ZipFile

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
REL = '{http://schemas.openxmlformats.org/package/2006/relationships}'
CT = '{http://schemas.openxmlformats.org/package/2006/content-types}'
XML_SPACE = '{http://www.w3.org/XML/1998/namespace}space'


def paragraph_text(element):
    return ''.join(node.text or '' for node in element.iter(f'{W}t')).strip()


def apply_frontmatter(body, package, reference, metadata):
    """Return replacements and additional parts for the generated DOCX package."""
    relationships = 'word/_rels/document.xml.rels'
    content_types = '[Content_Types].xml'
    rels = ET.fromstring(package.read(relationships))
    types = ET.fromstring(package.read(content_types))
    extra = {}

    def register_type(path, content_type):
        ET.SubElement(types, f'{CT}Override', PartName='/'+path, ContentType=content_type)

    with ZipFile(reference) as donor:
        source = ET.fromstring(donor.read('word/document.xml')).find(f'{W}body')
        source_rels = ET.fromstring(donor.read(relationships))
        donor_types = ET.fromstring(donor.read(content_types))

        def copy_media(target):
            path = PurePosixPath(target)
            new_target = str(path.with_name('tihi84-'+path.name))
            key = 'word/'+new_target
            if key not in extra:
                extra[key] = donor.read('word/'+target)
                ext = path.suffix.removeprefix('.')
                mime = next(x.get('ContentType') for x in donor_types if x.get('Extension') == ext)
                register_type(key, mime)
            return new_target

        def copy_relationship(id_):
            relation = next(item for item in source_rels if item.get('Id') == id_)
            target = relation.get('Target')
            kind = relation.get('Type').rsplit('/', 1)[-1]
            new_id = 'rIdTIHI84'+id_.removeprefix('rId')
            if any(item.get('Id') == new_id for item in rels):
                return new_id
            if kind == 'image':
                destination = copy_media(target)
            else:
                destination = 'tihi84-'+target
                original = 'word/'+target
                copied = 'word/'+destination
                extra[copied] = donor.read(original)
                mime = next(x.get('ContentType') for x in donor_types if x.get('PartName') == '/'+original)
                register_type(copied, mime)
                sidecar = 'word/_rels/'+target+'.rels'
                if sidecar in donor.namelist():
                    dependencies = ET.fromstring(donor.read(sidecar))
                    for child in dependencies:
                        child.set('Target', copy_media(child.get('Target')))
                    extra['word/_rels/'+destination+'.rels'] = ET.tostring(dependencies)
            ET.SubElement(rels, f'{REL}Relationship', Id=new_id,
                          Type=relation.get('Type'), Target=destination)
            return new_id

        def remap(node):
            for child in node.iter():
                for key, value in list(child.attrib.items()):
                    if key in (f'{R}id', f'{R}embed'):
                        child.set(key, copy_relationship(value))

        replacement = {'Subtítulo: Nombre del proyecto': 'espaciGo — Arriendo flexible de espacios',
                       'Diciembre, 2025': metadata['date'],
                       'Autor(a)(es)(as)': 'Autores'}
        replacement.update({f'APELLIDOS, NOMBRES AUTOR {i}': author
                            for i, author in enumerate(metadata['authors'], 1)})
        cover = []
        for item in source:
            if paragraph_text(item) == 'Dedicatoria':
                break
            item = deepcopy(item)
            key = paragraph_text(item)
            if key in replacement:
                runs = list(item.iter(f'{W}t'))
                runs[0].text = replacement[key]
                runs[0].set(XML_SPACE, 'preserve')
                for node in runs[1:]:
                    node.text = ''
            remap(item)
            cover.append(item)

        toc = next(item for item in body.findall(f'{W}sdt')
                   if any((n.text or '').lstrip().startswith('TOC') for n in item.iter(f'{W}instrText')))
        for item in list(body)[:list(body).index(toc)]:
            body.remove(item)
        body.remove(toc)
        for index, item in enumerate(cover):
            body.insert(index, item)
        summary = next(p for p in body.findall(f'{W}p') if paragraph_text(p) == 'Resumen')
        summary_index = list(body).index(summary)
        while summary_index and body[summary_index-1].tag == f'{W}bookmarkStart':
            summary_index -= 1
        body.insert(summary_index, toc)
        first = next(p for p in body.findall(f'{W}p') if paragraph_text(p).startswith('CAPÍTULO I:'))
        end = body.find(f'{W}sectPr')

        def configure_section(section, number, start, header):
            for item in list(section):
                if item.tag in (f'{W}headerReference', f'{W}footerReference', f'{W}pgNumType', f'{W}type', f'{W}titlePg'):
                    section.remove(item)
            numbering = {f'{W}fmt': number}
            if start is not None:
                numbering[f'{W}start'] = start
            ET.SubElement(section, f'{W}pgNumType', numbering)
            for kind, id_ in [('header', header), ('footer', 'rId14')]:
                node = ET.Element(f'{W}{kind}Reference', {f'{W}type': 'default', f'{R}id': copy_relationship(id_)})
                section.insert(0, node)

        for before, start, header in (
            (toc, '3', 'rId13'), (summary, None, 'rId15'), (first, None, 'rId16')
        ):
            section = deepcopy(end)
            configure_section(section, 'lowerRoman', start, header)
            position = list(body).index(before)
            while position and body[position-1].tag == f'{W}bookmarkStart':
                position -= 1
            separator = ET.Element(f'{W}p')
            ET.SubElement(separator, f'{W}pPr').append(section)
            body.insert(position, separator)
        configure_section(end, 'decimal', '1', 'rId13')
    extra[relationships] = ET.tostring(rels)
    extra[content_types] = ET.tostring(types)
    return extra
