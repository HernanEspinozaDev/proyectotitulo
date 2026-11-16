"""Comprueba la integridad de los insumos y de su extracción, sin modificarlos."""
from pathlib import Path
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[1]
def main():
    manifest=json.loads((ROOT/'01_extraccion/manifest.json').read_text())
    for item in manifest['fuentes']:
        p=Path(item['archivo']);assert p.stat().st_size==item['bytes'];assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256']
    book=json.loads((ROOT/'01_extraccion/excel/libro_completo.json').read_text());assert len(book)==26
    assert sum(len(s['celdas']) for s in book)==2081
    assert sum(c['tipo']=='f' for s in book for c in s['celdas'])==294
    for s in manifest['hojas']:
        for suffix in ['.json','.md','-valores.csv','-formulas.csv']:assert (ROOT/'01_extraccion/excel'/f"{s['archivo']}{suffix}").exists()
    report=json.loads((ROOT/'01_extraccion/informe/informe_completo.json').read_text());assert sum(x['tipo']=='parrafo' for x in report)==219
    imgs=json.loads((ROOT/'01_extraccion/informe/imagenes_manifest.json').read_text());assert len(imgs)==17
    for im in imgs:assert (ROOT/'01_extraccion/informe/imagenes'/im['archivo']).exists()
    annex=(ROOT/'03_propuesta/anexo_h_tablas_fuente.md').read_text()
    for i,s in enumerate(book,1):assert f"## H.{i}. {s['hoja'].strip()}" in annex
    source=json.loads((ROOT/'02_contraste/sapag2008_fuente.json').read_text());assert hashlib.sha256(Path(source['archivo']).read_bytes()).hexdigest()==source['sha256']
    print('Originales intactos por SHA-256; 26 hojas, 2081 celdas, 294 fórmulas, 219 párrafos y 17 imágenes conservados.')
if __name__=='__main__':main()
