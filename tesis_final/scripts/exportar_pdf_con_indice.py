#!/usr/bin/env python3
"""Exporta el DOCX de DocSkill a PDF tras actualizar sus índices en LibreOffice."""
import subprocess
import sys
import tempfile
import time
import uuid
from pathlib import Path

import uno
from com.sun.star.beans import PropertyValue
from com.sun.star.connection import NoConnectException


def properties(**values):
    return tuple(PropertyValue(key, 0, value, 0) for key, value in values.items())


def update_indexes(document):
    indexes = document.getDocumentIndexes()
    existing = [indexes.getByIndex(index) for index in range(indexes.getCount())]
    visual_index_style = 'Entradas del índice visual'
    styles = document.getStyleFamilies().getByName('ParagraphStyles')
    entry_style = document.createInstance('com.sun.star.style.ParagraphStyle')
    styles.insertByName(visual_index_style, entry_style)
    entry_style.ParentStyle = 'Contents 1'
    entry_style.ParaTopMargin = 0
    entry_style.ParaBottomMargin = 45
    entry_style.CharHeight = 10.5
    spacing = uno.createUnoStruct('com.sun.star.style.LineSpacing')
    spacing.Mode = 0
    spacing.Height = 100
    entry_style.ParaLineSpacing = spacing

    # Writer can omit imported Word indexes based on named paragraph styles.
    for title, style in (
        ('Índice de Tablas', 'Table Caption'),
        ('Índice de Figuras', 'Image Caption'),
    ):
        imported = next(
            (item for item in existing if style in item.LevelParagraphStyles.getByIndex(0)), None
        )
        if imported is not None:
            imported.ParaStyleLevel1 = visual_index_style
            continue
        search = document.createSearchDescriptor()
        search.SearchString = title
        heading = document.findFirst(search)
        if heading is None:
            raise RuntimeError(f'No se encontró el marcador de {title}.')
        text = heading.getText()
        cursor = text.createTextCursorByRange(heading.getEnd())
        if not cursor.goRight(1, False):
            raise RuntimeError(f'No se encontró el párrafo del {title}.')
        index = document.createInstance('com.sun.star.text.ContentIndex')
        index.Title = ''
        index.Level = 1
        index.ParaStyleLevel1 = visual_index_style
        index.CreateFromOutline = False
        index.CreateFromMarks = False
        index.CreateFromLevelParagraphStyles = True
        uno.invoke(index.LevelParagraphStyles, 'replaceByIndex', (0, uno.Any('[]string', (style,))))
        text.insertTextContent(cursor, index, False)
    # A second pass accounts for the page shifts caused by the indexes themselves.
    for _ in range(2):
        for position in range(indexes.getCount()):
            indexes.getByIndex(position).update()


def export_pdf(source, target):
    pipe = f'espacigo_{uuid.uuid4().hex}'
    local = uno.getComponentContext()
    resolver = local.ServiceManager.createInstanceWithContext(
        'com.sun.star.bridge.UnoUrlResolver', local
    )
    with tempfile.TemporaryDirectory(dir=target.parent) as directory:
        temporary = Path(directory)
        process = subprocess.Popen([
            'libreoffice', '--headless', '--norestore',
            f'-env:UserInstallation={(temporary / "profile").as_uri()}',
            f'--accept=pipe,name={pipe};urp;StarOffice.ComponentContext',
        ])
        try:
            for _ in range(100):
                try:
                    remote = resolver.resolve(
                        f'uno:pipe,name={pipe};urp;StarOffice.ComponentContext'
                    )
                    break
                except NoConnectException:
                    if process.poll() is not None:
                        raise RuntimeError('LibreOffice terminó antes de abrir la conexión.')
                    time.sleep(0.2)
            else:
                raise RuntimeError('LibreOffice no abrió la conexión para exportar.')
            desktop = remote.ServiceManager.createInstanceWithContext(
                'com.sun.star.frame.Desktop', remote
            )
            document = desktop.loadComponentFromURL(
                source.as_uri(), '_blank', 0, properties(Hidden=True, ReadOnly=True)
            )
            if document is None:
                raise RuntimeError(f'LibreOffice no pudo abrir {source.name}.')
            try:
                update_indexes(document)
                output = temporary / target.name
                document.storeToURL(
                    output.as_uri(), properties(
                        FilterName='writer_pdf_Export',
                        FilterData=uno.Any('[]com.sun.star.beans.PropertyValue', properties(
                            UseLosslessCompression=True,
                        )),
                    )
                )
            finally:
                document.close(True)
            output.replace(target)
        finally:
            process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()


if __name__ == '__main__':
    export_pdf(Path(sys.argv[1]).resolve(strict=True), Path(sys.argv[2]).resolve())
