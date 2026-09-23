"""Calibración del sistema bibliográfico de Word.

Extrae de un documento .docx real (creado por Word) la información necesaria
para generar fuentes y citas nativas desde Python:

  - la parte de fuentes (customXml/itemN.xml con raíz <b:Sources>);
  - sus atributos reales (SelectedStyle, StyleName, Version);
  - el orden exacto de los elementos de cada tipo de fuente;
  - las propiedades del almacén (itemPropsN.xml), las relaciones y los
    content types que Word declara para esas partes;
  - los conmutadores reales de los campos de cita (w:instrText) y del campo
    de bibliografía.

Uso:
    python calibrar_word.py "ruta\\al\\documento.docx"

Salida (en docx/calibracion/):
    sources.xml           parte de fuentes tal cual la escribió Word
    itemProps.xml         propiedades del almacén
    partes.md             relaciones y content types de las partes
    campos_cita.txt       todos los campos de cita distintos encontrados
    calibracion.md        informe legible con la plantilla a reutilizar
"""
import os
import re
import sys
import zipfile

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, "calibracion")


def escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def extraer(docx_path):
    os.makedirs(SALIDA, exist_ok=True)
    z = zipfile.ZipFile(docx_path)
    nombres = z.namelist()

    # 1. localizar la parte de fuentes
    fuentes = [n for n in nombres
               if n.lower().startswith("customxml/")
               and n.lower().endswith(".xml")
               and "itemprops" not in n.lower()]
    parte, xml = None, None
    for n in fuentes:
        dato = z.read(n).decode("utf-8", "ignore")
        if "b:Sources" in dato:
            parte, xml = n, dato
            break
    if parte is None:
        return None, "el documento no contiene una parte de fuentes (<b:Sources>)"

    escribir(os.path.join(SALIDA, "sources.xml"), xml)

    # 2. propiedades del almacén
    props = [n for n in nombres if n.lower().startswith("customxml/")
             and "itemprops" in n.lower()]
    texto_props = ""
    if props:
        texto_props = z.read(props[0]).decode("utf-8", "ignore")
        escribir(os.path.join(SALIDA, "itemProps.xml"), texto_props)

    # 3. relaciones y content types
    rels = []
    for n in nombres:
        if n.endswith(".rels") and ("customxml" in n.lower() or n == "_rels/.rels"):
            rels.append((n, z.read(n).decode("utf-8", "ignore")))
    ct = z.read("[Content_Types].xml").decode("utf-8", "ignore") if "[Content_Types].xml" in nombres else ""
    lineas = ["# Relaciones y content types de las partes bibliográficas\n"]
    for n, dato in rels:
        lineas.append("## %s\n" % n)
        for m in re.finditer(r"<Relationship[^>]*>", dato):
            if "customXml" in m.group(0) or "bibliography" in m.group(0).lower():
                lineas.append("    " + m.group(0))
        lineas.append("")
    lineas.append("## [Content_Types].xml (entradas customXml)\n")
    for m in re.finditer(r"<(?:Default|Override)[^>]*>", ct):
        if "customxml" in m.group(0).lower() or "bibliograph" in m.group(0).lower():
            lineas.append("    " + m.group(0))
    escribir(os.path.join(SALIDA, "partes.md"), "\n".join(lineas))

    # 4. campos de cita y de bibliografía del documento
    doc = z.read("word/document.xml").decode("utf-8", "ignore")
    campos = re.findall(r"<w:instrText[^>]*>(.*?)</w:instrText>", doc, re.S)
    distintos = sorted(set(c.strip() for c in campos))
    escribir(os.path.join(SALIDA, "campos_cita.txt"),
             "\n".join(distintos) if distintos else "(sin campos)")

    # 5. informe legible
    cab = re.search(r"<b:Sources\b[^>]*>", xml)
    inf = ["# Plantilla real del sistema bibliográfico de Word\n",
           "Documento de origen: `%s`\n" % docx_path,
           "Parte de fuentes: `%s`\n" % parte]
    inf.append("## Atributos de la raíz <b:Sources>\n")
    inf.append("```xml\n%s\n```\n" % (cab.group(0) if cab else "(no encontrada)"))
    inf.append("## Propiedades del almacén (itemProps)\n")
    inf.append("```xml\n%s\n```\n" % (texto_props.strip()[:600] if texto_props else "(no encontradas)"))

    inf.append("## Orden real de los elementos por tipo de fuente\n")
    por_tipo = {}
    for m in re.finditer(r"<b:Source>(.*?)</b:Source>", xml, re.S):
        cuerpo = m.group(1)
        tipo = re.search(r"<b:SourceType>([^<]*)</b:SourceType>", cuerpo)
        tipo = tipo.group(1) if tipo else "?"
        orden = re.findall(r"<b:([A-Za-z]+)[ >]", cuerpo)
        # se conserva el primer orden observado para cada tipo
        por_tipo.setdefault(tipo, orden)
    for tipo, orden in sorted(por_tipo.items()):
        inf.append("- **%s** (%d elementos): `%s`" % (tipo, len(orden), " → ".join(orden)))
    inf.append("")
    inf.append("## Plantilla completa de la primera fuente de cada tipo\n")
    vistos = set()
    for m in re.finditer(r"<b:Source>.*?</b:Source>", xml, re.S):
        bloque = m.group(0)
        tipo = re.search(r"<b:SourceType>([^<]*)</b:SourceType>", bloque)
        tipo = tipo.group(1) if tipo else "?"
        if tipo in vistos:
            continue
        vistos.add(tipo)
        inf.append("### %s\n```xml\n%s\n```\n" % (tipo, bloque))
    inf.append("## Campos de cita encontrados (w:instrText)\n")
    for c in distintos:
        inf.append("    %s" % c)
    escribir(os.path.join(SALIDA, "calibracion.md"), "\n".join(inf))
    return por_tipo, distintos


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    por_tipo, campos = extraer(sys.argv[1])
    if por_tipo is None:
        print("ERROR: %s" % campos)
        return 1
    print("Tipos de fuente encontrados: %d" % len(por_tipo))
    for t in sorted(por_tipo):
        print("  - %s" % t)
    print("Campos de cita distintos: %d" % len(campos))
    print("Reporte: %s" % os.path.join(SALIDA, "calibracion.md"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
