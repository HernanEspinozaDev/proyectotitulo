"""Extrae el orden real de elementos de <b:Source> por tipo de fuente, a partir
de varios documentos .docx escritos por Word.

Uso:
    python calibrar_tipos.py "carpeta_o_documento" ["otra" ...]

Recorre los .docx indicados, localiza las partes de fuentes (<b:Sources>) y
muestra, para cada tipo de fuente (Book, JournalArticle, InternetSite, ...),
el orden de los elementos tal como los escribió Word. Con eso se construyen
plantillas de fuente válidas sin tener que adivinar el esquema.
"""
import os
import re
import sys
import zipfile

MAX = 800

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def bloques_de(docx_path):
    """Devuelve la lista de bloques <b:Source> de un documento."""
    try:
        z = zipfile.ZipFile(docx_path)
    except Exception:
        return []
    salida = []
    for n in z.namelist():
        if not n.lower().startswith("customxml/") or not n.lower().endswith(".xml"):
            continue
        if "itemprops" in n.lower():
            continue
        try:
            dato = z.read(n).decode("utf-8", "ignore")
        except Exception:
            continue
        if "b:Sources" in dato:
            salida.extend(re.findall(r"<b:Source>.*?</b:Source>", dato, re.S))
    return salida


def orden_de(bloque):
    """Orden de los elementos de primer nivel y de segundo nivel del bloque."""
    tipo = re.search(r"<b:SourceType>([^<]*)</b:SourceType>", bloque)
    tipo = tipo.group(1) if tipo else "?"
    # elementos de primer nivel (se elimina el contenido anidado antes de buscar)
    sin_anidar = re.sub(r"<b:Author>.*?</b:Author>", "<b:Author/>", bloque, flags=re.S)
    orden = re.findall(r"<b:([A-Za-z]+)(?:/|>|[ ])", sin_anidar)
    return tipo, orden


def recorrer(raices):
    for raiz in raices:
        if os.path.isfile(raiz) and raiz.lower().endswith(".docx"):
            yield raiz
            continue
        for dirpath, dirs, files in os.walk(raiz):
            dirs[:] = [d for d in dirs if d.lower() not in
                       (".git", "node_modules", ".venv", "__pycache__", ".vscode")]
            for f in files:
                if f.lower().endswith(".docx") and not f.startswith("~$"):
                    yield os.path.join(dirpath, f)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    ordenes = {}
    autores = {}
    revisados = 0
    for p in recorrer(sys.argv[1:]):
        revisados += 1
        if revisados > MAX:
            break
        for bloque in bloques_de(p):
            tipo, orden = orden_de(bloque)
            clave = tuple(orden)
            ordenes.setdefault(tipo, {}).setdefault(clave, 0)
            ordenes[tipo][clave] += 1
            if tipo not in autores:
                m = re.search(r"<b:Author>.*?</b:Author>", bloque, re.S)
                if m:
                    autores[tipo] = m.group(0)
    print("documentos revisados: %d" % min(revisados, MAX))
    print("tipos de fuente encontrados: %d" % len(ordenes))
    for tipo in sorted(ordenes):
        print("\n=== %s ===" % tipo)
        for orden, veces in sorted(ordenes[tipo].items(), key=lambda x: -x[1]):
            print("  (%d veces) %s" % (veces, " → ".join(orden)))
        if tipo in autores:
            print("  autor: %s" % autores[tipo][:300])
    return 0


if __name__ == "__main__":
    sys.exit(main())
