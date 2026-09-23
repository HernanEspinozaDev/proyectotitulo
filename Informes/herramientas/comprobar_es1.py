"""Regresión no destructiva contra los seis Word conservados de ES1."""
import difflib
import hashlib
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from herramientas.configuracion import RAIZ, cargar
from herramientas.validacion import inspeccionar_docx, W


def contenido(ruta):
    with zipfile.ZipFile(ruta) as z:
        doc = ET.fromstring(z.read("word/document.xml"))
    # Excluir portada e índices, conservando párrafos y tablas del cuerpo.
    textos, iniciado = [], False
    for p in doc.iter(W + "p"):
        texto = "".join(t.text or "" for t in p.iter(W + "t"))
        estilo = p.find("./" + W + "pPr/" + W + "pStyle")
        sid = estilo.get(W + "val", "") if estilo is not None else ""
        if sid in {"Ttulo1", "Ttulo10", "Heading1"} and (texto.strip() == "Introducción" or texto.startswith("Anexo ")):
            iniciado = True
        if iniciado:
            texto = re.sub(r"\s+", " ", texto).strip()
            if texto:
                textos.append(texto)
    return textos


def main():
    cfg = cargar("recursos/compatibilidad_es1.json")
    reporte, errores = {}, []
    base = RAIZ / "ES1PT/docx/build"
    for nombre in ["Informe_Final.docx"] + [a["salida"] for a in cfg.anexos]:
        fuente, nuevo = base / nombre, cfg.salida(nombre)
        fallos, antes = inspeccionar_docx(fuente)
        fallos_n, despues = inspeccionar_docx(nuevo)
        if fallos or fallos_n:
            errores += [f"{nombre}: {f}" for f in fallos + fallos_n]
        if not antes or not despues:
            continue
        a, b = contenido(fuente), contenido(nuevo)
        diferencias = list(difflib.unified_diff(a, b, fromfile="ES1 conservado", tofile="Motor común", lineterm=""))
        cambios = {k: [antes[k], despues[k]] for k in ("tablas", "imagenes", "citas", "bibliografias", "fuentes", "indices", "capitulos", "titulos") if antes[k] != despues[k]}
        if diferencias or cambios or not a or not b:
            errores.append(f"{nombre}: diferencias de contenido o estructura; revisar reporte.")
        reporte[nombre] = {"antes": antes, "despues": despues, "cambios": cambios,
                           "parrafos_cuerpo": [len(a), len(b)], "diferencias": diferencias}
    ruta_hash = RAIZ / "build/normalizacion/es1_antes.json"
    if ruta_hash.exists():
        previo = json.loads(ruta_hash.read_text(encoding="utf-8-sig"))
        actual = {p.relative_to(RAIZ / "ES1PT").as_posix(): hashlib.sha256(p.read_bytes()).hexdigest().upper()
                  for p in (RAIZ / "ES1PT").rglob("*") if p.is_file()}
        alterados = sorted(k for k in previo.keys() | actual.keys() if previo.get(k) != actual.get(k))
        reporte["conservacion"] = {"archivos": len(previo), "alterados": alterados}
        if alterados:
            errores.append("ES1 cambió: " + ", ".join(alterados))
    else:
        errores.append("Falta el manifiesto local de conservación es1_antes.json.")
    reporte["errores"] = errores
    destino = RAIZ / "build/normalizacion/comparacion_es1.json"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(reporte, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for e in errores:
        print(e)
    print(destino)
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
