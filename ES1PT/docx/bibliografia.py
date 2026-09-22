"""Sistema de citas y fuentes bibliográficas nativas de Word.

Word no administra las citas como texto: las guarda en dos lugares del paquete
DOCX,

  1. la parte <customXml/item1.xml> con raíz <b:Sources>, que es la que alimenta
     Referencias > Administrar fuentes; y
  2. campos CITATION en el cuerpo y un campo BIBLIOGRAPHY para la lista.

Pandoc (citeproc) no escribe ninguna de las dos cosas: solo produce texto. Este
módulo traduce el archivo referencias.bib a esas estructuras, tomando como
plantilla un documento real generado por Word (ver calibrar_word.py).

Estructura de las fuentes y de los campos verificada en:
  docx/calibracion/calibracion.md
  - raíz <b:Sources SelectedStyle="..." StyleName="APA" Version="6">
    (la calibración se hizo con \\APASixthEditionOfficeOnline.xsl; hoy se emite
    \\APASeventhEdition.xsl, que Word ya reconoce en esta máquina)
  - campo de cita:  CITATION <Tag> \\l 13322
  - campo de lista: BIBLIOGRAPHY \\l 13322
  - el esquema de <b:Source> no impone un orden fijo de elementos
  - elementos válidos comprobados en los XSL de Word: DOI, Issue, Volume,
    Pages, JournalArticle (tipo de fuente para @article)

Uso:
    python bibliografia.py            # escribe build/sources.xml y la auditoría
"""
import os
import re
import sys
import unicodedata
import uuid

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

BASE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(BASE, "build")
BIB = os.path.join(BASE, "referencias.bib")

NS_B = "http://schemas.openxmlformats.org/officeDocument/2006/bibliography"
# Valores tomados del documento real de Word (no inventados). El estilo es
# APASeventhEdition.xsl, instalado por el usuario en
# %APPDATA%\Microsoft\Bibliography\Style (Word lo reconoce porque enumera
# esa carpeta). Antes era \APASixthEditionOfficeOnline.xsl.
ESTILO_WORD = "\\APASeventhEdition.xsl"
ROOT_ATTRS = ('xmlns:b="%s" xmlns="%s" SelectedStyle="%s" '
              'StyleName="APA" Version="6"' % (NS_B, NS_B, ESTILO_WORD))

# marcas de acento LaTeX -> caracter combinante Unicode (ver _sin_latex)
_COMBINANTES = {"`": "\u0300", "'": "\u0301", "^": "\u0302",
                '"': "\u0308", "~": "\u0303"}

# Corpus de claves del .bib -> tipo de fuente de Word
TIPO_WORD = {
    "book": "Book",
    "inbook": "BookSection",
    "article": "JournalArticle",
    "inproceedings": "ConferenceProceedings",
    "techreport": "Report",
    "report": "Report",
    "misc": "InternetSite",       # se ajusta luego según el contenido
    "online": "InternetSite",
    "thesis": "Thesis",
}

# Campos obligatorios (mínimos) para que la fuente sea identificable en Word
OBLIGATORIOS = {
    "Book": ["author", "title", "year"],
    "BookSection": ["author", "title", "year"],
    "JournalArticle": ["author", "title", "year"],
    "ConferenceProceedings": ["author", "title", "year"],
    "Report": ["author", "title", "year"],
    "Thesis": ["author", "title", "year"],
    "InternetSite": ["author", "title", "url"],
}


# --------------------------------------------------------------------------- #
# lectura del .bib
# --------------------------------------------------------------------------- #
def leer_bib(ruta=BIB):
    """Devuelve la lista de entradas del .bib como diccionarios."""
    if not os.path.exists(ruta):
        return []
    with open(ruta, encoding="utf-8-sig") as f:
        texto = f.read()
    entradas = []
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", texto):
        tipo, clave = m.group(1).lower(), m.group(2)
        i = m.end()
        campos, nota = {}, None
        while i < len(texto):
            c = texto[i]
            if c == "}":
                break
            if c in " \t\r\n,":
                i += 1
                continue
            mf = re.match(r"([A-Za-z]+)\s*=\s*", texto[i:])
            if not mf:
                i += 1
                continue
            nombre = mf.group(1).lower()
            j = i + mf.end()
            if j < len(texto) and texto[j] == "{":
                valor, prof = "", 0
                k = j
                while k < len(texto):
                    if texto[k] == "{":
                        prof += 1
                        if prof > 1:
                            valor += "{"
                    elif texto[k] == "}":
                        prof -= 1
                        if prof == 0:
                            break
                        valor += "}"
                    else:
                        valor += texto[k]
                    k += 1
                i = k + 1
            else:
                mc = re.match(r'"?([^",\n]*)"?', texto[j:])
                valor = mc.group(1) if mc else ""
                i = j + (mc.end() if mc else 0)
            if nombre == "note":
                nota = valor.strip()
            else:
                campos[nombre] = valor.strip()
        entradas.append({"tipo": tipo, "clave": clave, "campos": campos, "nota": nota})
    return entradas


def tipo_word(entrada):
    """Decide el tipo de fuente de Word para una entrada del .bib."""
    tipo = entrada["tipo"]
    campos = entrada["campos"]
    if tipo == "misc":
        titulo = campos.get("title", "").lower()
        publicacion = (campos.get("howpublished", "") or "").lower()
        if ("iso" in publicacion or "iec" in publicacion or "standard" in titulo
                or publicacion.startswith("version")):
            return "Report"    # norma técnica (ISO/IEC, PCI-DSS)
        if "ley" in titulo:
            return "Misc"      # norma legal: Word no tiene tipo propio (ver auditoría)
        if campos.get("url"):
            return "InternetSite"
        return "Misc"
    return TIPO_WORD.get(tipo, "Misc")


# --------------------------------------------------------------------------- #
# construcción de la parte de fuentes
# --------------------------------------------------------------------------- #
def _sin_latex(texto):
    """Traduce los acentos LaTeX del .bib a UTF-8.

    Word no interpreta LaTeX: si el valor llega como `Mazi{\\`e}res` lo imprime
    literal en la bibliografía. Pandoc (citeproc) sí lo interpreta, así que la
    conversión debe hacerse antes de escribir <b:Last>, <b:Title>, etc.
    """
    t = str(texto)
    if "\\" not in t:
        return t.replace("{", "").replace("}", "")
    # {"e} -> "e   (llave que envuelve el comando de acento)
    t = re.sub(r"\{\s*(\\[`'\"^~cvu=.])\s*([A-Za-z])\s*\}", r"\1\2", t)

    def _rep(m):
        marca, letra = m.group(1), m.group(2)
        combinante = _COMBINANTES.get(marca)
        if combinante:
            return unicodedata.normalize("NFC", letra + combinante)
        return letra

    t = re.sub(r"\\([`'\"^~])[ ]?\{?([A-Za-z])\}?", _rep, t)
    return t.replace("{", "").replace("}", "")


def _xml(texto):
    return (_sin_latex(texto).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;"))


def _paginas(valor):
    """Normaliza el rango LaTeX '50--58' a '50–58' (guion de rango).

    Word no interpreta '--' del .bib y lo imprime tal cual, por lo que la
    normalización se hace aquí y no en el .bib.
    """
    if not valor:
        return valor
    return re.sub(r"\s*-{1,2}\s*", "\u2013", valor.strip())


def _guids(clave):
    """GUID estable derivado de la clave: re-ejecutar no duplica fuentes."""
    return "{%s}" % str(uuid.uuid5(uuid.NAMESPACE_URL, "espacigo:bib:" + clave)).upper()


def _autor_xml(valor):
    """Convierte 'Apellido, Nombre and Apellido2, Nombre2' al XML de autores."""
    personas = []
    for parte in re.split(r"\s+and\s+", valor):
        parte = parte.strip()
        if not parte:
            continue
        if "," in parte:
            apellido, nombre = [p.strip() for p in parte.split(",", 1)]
        else:
            trozos = parte.split()
            apellido, nombre = trozos[-1], " ".join(trozos[:-1])
        personas.append((apellido, nombre))
    if not personas:
        return ""
    lista = "".join(
        "<b:Person><b:Last>%s</b:Last>%s</b:Person>"
        % (_xml(ap), "<b:First>%s</b:First>" % _xml(nm) if nm else "")
        for ap, nm in personas)
    return ("<b:Author><b:Author><b:NameList>%s</b:NameList></b:Author></b:Author>" % lista)


def _autor_corporativo_xml(nombre):
    return ("<b:Author><b:Author><b:Corporate>%s</b:Corporate></b:Author></b:Author>"
            % _xml(nombre))


def fuente_xml(entrada):
    """Devuelve el XML <b:Source> de una entrada."""
    c = entrada["campos"]
    tipo = tipo_word(entrada)
    trozos = ["<b:Tag>%s</b:Tag>" % _xml(entrada["clave"]),
              "<b:SourceType>%s</b:SourceType>" % tipo,
              "<b:Guid>%s</b:Guid>" % _guids(entrada["clave"])]

    # autores: doble llave en el .bib = autor corporativo / institucional
    autor = c.get("author", "")
    if autor.startswith("{") or autor.endswith("}"):
        trozos.append(_autor_corporativo_xml(autor.strip("{}")))
    elif autor:
        trozos.append(_autor_xml(autor))

    def add(etiqueta, valor):
        if valor:
            trozos.append("<b:%s>%s</b:%s>" % (etiqueta, _xml(valor), etiqueta))

    add("Title", c.get("title"))
    if tipo == "InternetSite":
        add("InternetSiteTitle", c.get("howpublished") or c.get("publisher"))
    if tipo == "ConferenceProceedings":
        add("ConferenceName", c.get("journal") or c.get("booktitle"))
    if tipo == "BookSection":
        add("BookTitle", c.get("booktitle"))
    add("JournalName", c.get("journal") if tipo not in ("ConferenceProceedings",) else "")
    add("Edition", c.get("edition"))
    add("Volume", c.get("volume"))
    add("Issue", c.get("number"))
    add("Pages", _paginas(c.get("pages")))
    add("Year", c.get("year"))
    add("Publisher", c.get("publisher"))
    add("City", c.get("address") or c.get("location"))
    add("Institution", c.get("institution"))
    add("DOI", c.get("doi"))
    add("StandardNumber", c.get("howpublished") if tipo == "Report" else "")
    add("ThesisType", c.get("type") if tipo == "Thesis" else "")
    add("URL", c.get("url"))
    # fecha de consulta: se toma de urldate (AAAA-MM-DD) cuando está declarada
    if c.get("urldate"):
        partes = re.split(r"[-/]", c["urldate"])
        if len(partes) == 3:
            add("YearAccessed", partes[0])
            add("MonthAccessed", MESES.get(partes[1].lstrip("0"), partes[1]))
            add("DayAccessed", str(int(partes[2])))
    add("YearAccessed", "" if c.get("urldate") else c.get("yearaccessed"))
    add("MonthAccessed", "" if c.get("urldate") else c.get("monthaccessed"))
    add("DayAccessed", "" if c.get("urldate") else c.get("dayaccessed"))
    return "<b:Source>%s</b:Source>" % "".join(trozos)


def parte_sources(entradas):
    """Devuelve el contenido completo de customXml/item1.xml."""
    fuentes = "".join(fuente_xml(e) for e in entradas)
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n'
            '<b:Sources %s>%s</b:Sources>' % (ROOT_ATTRS, fuentes))


def parte_itemprops(id_almacen):
    """Devuelve el contenido de customXml/itemProps1.xml (igual que Word)."""
    return ('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\r\n'
            '<ds:datastoreItem ds:itemID="%s" '
            'xmlns:ds="http://schemas.openxmlformats.org/officeDocument/2006/customXml">'
            '<ds:schemaRefs><ds:schemaRef '
            'ds:uri="http://schemas.microsoft.com/sharepoint/v3/contenttype/forms"/>'
            '</ds:schemaRefs></ds:datastoreItem>' % id_almacen)


# --------------------------------------------------------------------------- #
# campos de Word
# --------------------------------------------------------------------------- #
LCID = 13322      # es-CL (valor observado en el documento real de Word)

MESES = {"1": "Enero", "2": "Febrero", "3": "Marzo", "4": "Abril", "5": "Mayo",
         "6": "Junio", "7": "Julio", "8": "Agosto", "9": "Septiembre",
         "10": "Octubre", "11": "Noviembre", "12": "Diciembre"}


def campo_cita(texto_cache, tag):
    """Campo CITATION de una sola fuente, con su texto en caché."""
    return ('<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
            '<w:r><w:instrText xml:space="preserve"> CITATION %s \\l %d </w:instrText></w:r>'
            '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
            '<w:r><w:t xml:space="preserve">%s</w:t></w:r>'
            '<w:r><w:fldChar w:fldCharType="end"/></w:r>' % (tag, LCID, _xml(texto_cache)))


def abrir_campo_bibliografia():
    return ('<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
            '<w:r><w:instrText xml:space="preserve"> BIBLIOGRAPHY \\l %d </w:instrText></w:r>'
            '<w:r><w:fldChar w:fldCharType="separate"/></w:r>' % LCID)


def cerrar_campo_bibliografia():
    return '<w:r><w:fldChar w:fldCharType="end"/></w:r>'


# --------------------------------------------------------------------------- #
# auditoría
# --------------------------------------------------------------------------- #
def auditar(entradas, citas, cache=None, ocurrencias=None):
    """Audita el sistema de citas y devuelve (markdown, resumen)."""
    cache = cache or {}
    claves_bib = [e["clave"] for e in entradas]
    usadas = sorted(set(citas))
    sin_cita = [k for k in claves_bib if k not in usadas]
    sin_fuente = [k for k in usadas if k not in claves_bib]

    incompletas, pendientes, tipos, informativas = [], [], {}, []
    for e in entradas:
        tipo = tipo_word(e)
        tipos[tipo] = tipos.get(tipo, 0) + 1
        faltan = [f for f in OBLIGATORIOS.get(tipo, []) if not e["campos"].get(f)]
        if faltan:
            incompletas.append((e["clave"], tipo, faltan))
        if e["nota"] and e["nota"].strip().upper().startswith("PENDIENTE"):
            pendientes.append((e["clave"], e["nota"]))
        elif e["nota"]:
            informativas.append((e["clave"], e["nota"]))

    # duplicados: mismo autor+año+título normalizado
    vistos, duplicados = {}, []
    for e in entradas:
        firma = (re.sub(r"\W+", "", e["campos"].get("author", "").lower()),
                 e["campos"].get("year", ""),
                 re.sub(r"\W+", "", e["campos"].get("title", "").lower())[:60])
        if firma in vistos and firma != ("", "", ""):
            duplicados.append((vistos[firma], e["clave"]))
        vistos[firma] = e["clave"]

    lineas = ["# Auditoría de citas y fuentes bibliográficas\n",
              "| Métrica | Valor |", "| :--- | :--- |",
              "| Fuentes encontradas en `referencias.bib` | %d |" % len(entradas),
              "| Fuentes convertidas a fuente de Word | %d |" % len(entradas),
              "| Tipos de fuente de Word utilizados | %s |"
              % ", ".join("%s (%d)" % kv for kv in sorted(tipos.items())),
              "| Citas detectadas en el texto | %d |" % len(citas),
              "| Campos de cita (citas con varias fuentes cuentan una vez por fuente) | %s |"
              % (ocurrencias if ocurrencias is not None else "no calculado"),
              "| Claves distintas citadas | %d |" % len(usadas),
              "| Textos de cita en caché obtenidos | %d |" % len(cache),
              "| Fuentes duplicadas | %d |" % len(duplicados),
              "| Fuentes incompletas para su tipo | %d |" % len(incompletas),
              "| Citas sin fuente en el catálogo | %d |" % len(sin_fuente),
              "| Fuentes del catálogo sin cita en el texto | %d |" % len(sin_cita),
              "| Fuentes con datos por verificar | %d |" % len(pendientes),
              "| Fuentes con nota informativa (fecha de publicación, edición vigente) | %d |"
              % len(informativas),
              "|"]

    if sin_fuente:
        lineas += ["## Citas sin fuente en el catálogo\n"] + \
                  ["- `%s`" % k for k in sin_fuente] + [""]
    if sin_cita:
        lineas += ["## Fuentes del catálogo que no se citan en el texto\n"] + \
                  ["- `%s`" % k for k in sin_cita] + [""]
    if duplicados:
        lineas += ["## Fuentes duplicadas\n"] + \
                  ["- `%s` y `%s`" % d for d in duplicados] + [""]
    if incompletas:
        lineas += ["## Fuentes incompletas (falta un campo obligatorio de su tipo)\n",
                   "| Clave | Tipo Word | Campos faltantes |", "| :--- | :--- | :--- |"]
        for clave, tipo, faltan in incompletas:
            lineas.append("| `%s` | %s | %s |" % (clave, tipo, ", ".join(faltan)))
        lineas.append("")
    if pendientes:
        lineas += ["## Datos por verificar (no se inventan: quedan marcados)\n",
                   "| Clave | Qué falta verificar |", "| :--- | :--- |"]
        for clave, nota in pendientes:
            lineas.append("| `%s` | %s |" % (clave, nota.replace("|", "/")))
        lineas.append("")
    lineas += ["## Limitaciones registradas\n",
               "- Pandoc no genera campos ni fuentes nativas de Word: la conversión se hace "
               "por post-proceso sobre el OOXML.",
               "- El texto de las citas y de la lista se genera con `apa.csl` (APA 7) y se "
               "guarda como caché del campo. Al pulsar `F9`, Word recompone con su propia "
               "implementación de APA, que puede diferir en detalles.",
               "- El estilo seleccionado en la parte de fuentes es "
               "`\\APASeventhEdition.xsl` (APA 7), instalado por el usuario en la "
               "carpeta de estilos de Word; Word lo aplica al actualizar los campos.",
               "- Las normas legales chilenas se registran como `Misc` porque Word no tiene "
               "un tipo propio para legislación.",
               "- Las citas con más de una fuente llevan un campo por fuente: el texto en "
               "caché reproduce el formato APA de un solo paréntesis, pero al pulsar `F9` "
               "Word puede componer cada campo con sus propios paréntesis.",
               "- La fecha de consulta de las fuentes en línea no se escribe mientras no "
               "esté verificada.",
               ""]
    resumen = {"entradas": len(entradas), "citas": len(citas), "cache": len(cache),
               "duplicados": len(duplicados), "incompletas": len(incompletas),
               "sin_fuente": len(sin_fuente), "sin_cita": len(sin_cita),
               "pendientes": len(pendientes), "tipos": tipos}
    return "\n".join(lineas), resumen


def main():
    entradas = leer_bib()
    os.makedirs(BUILD, exist_ok=True)
    with open(os.path.join(BUILD, "sources.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write(parte_sources(entradas))
    texto, resumen = auditar(entradas, [])
    with open(os.path.join(BUILD, "auditoria_citas.md"), "w", encoding="utf-8",
              newline="\n") as f:
        f.write(texto)
    print("Entradas del .bib: %d" % resumen["entradas"])
    for tipo, n in sorted(resumen["tipos"].items()):
        print("  %-24s %d" % (tipo, n))
    print("Sin cita en el texto (aún no calculado): %s" % (resumen["sin_cita"]))
    print("Parte de fuentes: %s" % os.path.join(BUILD, "sources.xml"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
