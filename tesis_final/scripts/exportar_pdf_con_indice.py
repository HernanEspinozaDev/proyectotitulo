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
                indexes = document.getDocumentIndexes()
                for index in range(indexes.getCount()):
                    indexes.getByIndex(index).update()
                output = temporary / target.name
                document.storeToURL(
                    output.as_uri(), properties(FilterName='writer_pdf_Export')
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
