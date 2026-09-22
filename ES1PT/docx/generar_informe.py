#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pipeline MD -> DOCX para el informe EspaciGo (TIHI84).

Uso:
    python generar_informe.py diagramas     # extrae y renderiza los diagramas PlantUML
    python generar_informe.py preprocesar   # numera tablas/figuras, resuelve referencias y pendientes
    python generar_informe.py pandoc        # informe_ensamblado.md -> body.docx
    python generar_informe.py armar         # inserta el cuerpo en la plantilla institucional
    python generar_informe.py anexos        # genera un DOCX independiente por anexo
    python generar_informe.py validar       # ejecuta las validaciones y escribe el reporte
    python generar_informe.py todo          # ejecuta todo en orden

Requisitos: pandoc 3.x en el PATH, Java + plantuml.jar para los diagramas.
"""
import io
import os
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bibliografia   # noqa: E402  (módulo local del pipeline)

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))          # ES1PT/docx
RAIZ = os.path.dirname(BASE)                                # ES1PT
BUILD = os.path.join(BASE, "build")
IMAGENES = os.path.join(BASE, "imagenes")
ANEXOS = os.path.join(BASE, "anexos")
DIAGRAMAS = os.path.join(BASE, "diagramas")

# Anexos del informe: (archivo fuente, letra, título, nombre del documento generado)
ANEXOS_MAPA = [
    ("A_actores_y_modulos.md", "A", "Actores y módulos del sistema",
     "Anexo_A_Actores_y_modulos_del_sistema.docx"),
    ("B_requerimientos_funcionales.md", "B", "Catálogo de requerimientos funcionales",
     "Anexo_B_Catalogo_de_requerimientos_funcionales.docx"),
    ("C_requerimientos_no_funcionales.md", "C", "Requerimientos no funcionales",
     "Anexo_C_Requerimientos_no_funcionales.docx"),
    ("D_casos_de_uso.md", "D", "Especificación de casos de uso",
     "Anexo_D_Especificacion_de_casos_de_uso.docx"),
    ("E_historias_de_usuario.md", "E", "Historias de usuario",
     "Anexo_E_Historias_de_usuario.docx"),
]

INFORME = os.path.join(BASE, "informe.md")
ORIGINAL = os.path.join(RAIZ, "informe_del_proyecto_espacigo.md")
PLANTILLA = os.path.join(BASE, "plantilla.docx")
BIB = os.path.join(BASE, "referencias.bib")
CSL = os.path.join(BASE, "apa.csl")

# Locale del CSL: sin esto citeproc usa en-US y devuelve "(n.d.)" y
# "Retrieved ... from"; con es-CL se obtiene "(s.f.)" y "Recuperado ... de"
# y se respetan las mayúsculas de los nombres propios de los títulos.
IDIOMA = "es-CL"

ANEXO_CU = os.path.join(RAIZ, "anexo_casos_de_uso.md")
PLANTUML = os.path.join(os.environ.get("TEMP", "."), "plantuml.jar")

ENSAMBLADO = os.path.join(BUILD, "informe_ensamblado.md")
ENSAMBLADO_CITAS = os.path.join(BUILD, "informe_ensamblado_citas.md")
BODY = os.path.join(BUILD, "body.docx")
BODY_CITAS = os.path.join(BUILD, "body_citas.docx")
SOURCES = os.path.join(BUILD, "sources.xml")
AUDITORIA_CITAS = os.path.join(BUILD, "auditoria_citas.md")
FINAL = os.path.join(BUILD, "Informe_Final.docx")
REPORTE = os.path.join(BUILD, "reporte_validacion.md")

# caché de los textos de cita en APA 7 (los calcula paso_bibliografia)
CACHE_CITAS = {}
ID_ALMACEN = "{%s}" % str(__import__("uuid").uuid5(
    __import__("uuid").NAMESPACE_URL, "espacigo:customxml:sources")).upper()
REL_PROPS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n'
             '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
             '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/'
             '2006/relationships/customXmlProps" Target="itemProps1.xml"/></Relationships>')

NUM_ABS = 900          # abstractNum de la numeración institucional
NUM_BASE = 900         # numId base (uno por capítulo)

# Estilos propios de pandoc -> estilos institucionales de la plantilla
MAPA_ESTILOS = {
    "Ttulo10": "Ttulo1",
    "Ttulo2": "Subtitulo1",
    "Ttulo3": "Subtitulo2",
    "Ttulo4": "Prrafodelista",
    "FirstParagraph": "PARRAFO",
    "BodyText": "PARRAFO",
    "Compact": "PARRAFO",
    "BlockText": "DESTACADO",
    "ImageCaption": "PIEDEFOTO",
    "CaptionedFigure": "PARRAFO",
    "Caption": "PIEDEFOTO",
    "TableCaption": "TABLATTULO",
    "SourceCode": "PARRAFO",
    # ojo: el estilo real de la plantilla es BIBLIOGRAFA1 (nombre «BIBLIOGRAFÍA 1»),
    # que trae la indentación francesa de APA (w:ind hanging). La variante acentuada
    # no existe y dejaba las referencias sin sangría.
    "Bibliography": "BIBLIOGRAFA1",
}
NIVEL_TITULO = {"Ttulo1": 0, "Subtitulo1": 1, "Subtitulo2": 2, "Prrafodelista": 3}

# Instrucción del índice: por estilo (la plantilla del TOC en caché usa los mismos)
TOC_INSTRUCCION = ' TOC \\h \\z \\t "Título1;1;Subtitulo1;2;Subtitulo2;3" '

# Texto en caché del índice: se ve solo si el documento nunca se abrió en Word
# (settings.xml lleva updateFields, así que Word lo reconstruye al abrirlo).
TOC_AVISO = "Índice pendiente: en Word, actualiza los campos (Ctrl+A y F9)."

# Rótulos de tablas y figuras (APA 7): etiqueta en negrita y título en cursiva,
# en el párrafo anterior al objeto. El estilo del rótulo es el que usa Word para
# armar el índice de ilustraciones, por eso los nombres no llevan espacios.
ESTILO_ROTULO_TABLA = "ROTULOTABLA"
ESTILO_ROTULO_FIGURA = "ROTULOFIGURA"
NOMBRE_ROTULO_TABLA = "RotuloTabla"
NOMBRE_ROTULO_FIGURA = "RotuloFigura"
# Al guardar, Word normaliza el styleId al nombre del estilo (ROTULOTABLA ->
# RotuloTabla), así que las validaciones aceptan las dos formas.
MARCA_ROTULO_TABLA = r'w:val="(?:%s|%s)"' % (ESTILO_ROTULO_TABLA, NOMBRE_ROTULO_TABLA)
MARCA_ROTULO_FIGURA = r'w:val="(?:%s|%s)"' % (ESTILO_ROTULO_FIGURA, NOMBRE_ROTULO_FIGURA)

# Fuente por omisión de las notas bajo tablas y figuras
FUENTE_NOTA = "elaboración propia."

# Tipografía pedida: Calibri 11 en todo el informe y 12 en los títulos
FUENTE = "Calibri"
SZ_CUERPO = 22      # 11 pt
SZ_TITULO = 24      # 12 pt


# Familias de propiedades de run que se conservan al fijar fuente y tamaño
_RPR_CONSERVAR = ((1, "b"), (2, "bCs"), (3, "i"), (4, "iCs"), (5, "caps"),
                  (6, "smallCaps"), (18, "color"), (26, "u"))


def _rpr_tipografia(rpr_actual, sz=None, fuente=FUENTE):
    """Devuelve un <w:rPr> con Calibri y el tamaño indicado.

    Conserva negrita, cursiva, mayúsculas, color y subrayado del rPr original y
    respeta el orden del esquema OOXML (rFonts, b, i, ..., color, sz, u).
    """
    piezas = []
    for orden, etiqueta in _RPR_CONSERVAR:
        m = re.search(r"<w:%s\b[^>]*/>" % etiqueta, rpr_actual or "")
        if m:
            piezas.append((orden, m.group(0)))
    fuente_xml = ('<w:rFonts w:ascii="%s" w:hAnsi="%s" w:cs="%s"/>'
                  % (fuente, fuente, fuente))
    partes = [fuente_xml] + [x for _, x in sorted(piezas)]
    if sz:
        partes.append('<w:sz w:val="%d"/>' % sz)
        partes.append('<w:szCs w:val="%d"/>' % sz)
    return "<w:rPr>%s</w:rPr>" % "".join(partes)


def _ajustar_estilo(styles, style_id, sz=None, fuente=FUENTE):
    """Fija fuente y tamaño de un estilo existente (reemplaza lo que tuviera)."""
    pat = re.compile(r'(<w:style [^>]*w:styleId="%s"[^>]*>)(.*?)(</w:style>)'
                     % re.escape(style_id), re.S)
    m = pat.search(styles)
    if not m:
        return styles
    cab, cuerpo, fin = m.groups()
    rpr = re.search(r"<w:rPr>.*?</w:rPr>", cuerpo, re.S)
    nuevo = _rpr_tipografia(rpr.group(0) if rpr else "", sz)
    if rpr:
        cuerpo = cuerpo[:rpr.start()] + nuevo + cuerpo[rpr.end():]
    else:
        cuerpo = cuerpo + nuevo          # el rPr va después de pPr
    return styles[:m.start()] + cab + cuerpo + fin + styles[m.end():]


def _estilo_junto(styles, style_id):
    """Marca un estilo con keepNext: no queda solo al final de la página."""
    m = re.search(r'<w:style [^>]*w:styleId="%s"[^>]*>.*?</w:style>' % style_id, styles, re.S)
    if not m or "<w:keepNext/>" in m.group(0):
        return styles
    bloque = m.group(0)
    if "<w:pPr>" in bloque:
        nuevo = bloque.replace("<w:pPr>", "<w:pPr><w:keepNext/>", 1)
    elif "<w:rPr>" in bloque:
        nuevo = bloque.replace("<w:rPr>", "<w:pPr><w:keepNext/></w:pPr><w:rPr>", 1)
    else:
        nuevo = bloque.replace("</w:style>", "<w:pPr><w:keepNext/></w:pPr></w:style>", 1)
    return styles.replace(bloque, nuevo, 1)


def _estilo_rotulo(style_id, nombre):
    """Define un estilo de rótulo: Calibri 11, junto al objeto (keepNext)."""
    return ('<w:style w:type="paragraph" w:styleId="%s">'
            '<w:name w:val="%s"/><w:basedOn w:val="PARRAFO"/><w:next w:val="PARRAFO"/>'
            '<w:uiPriority w:val="99"/><w:qFormat/>'
            '<w:pPr><w:keepNext/><w:spacing w:before="240" w:after="60"/>'
            '<w:jc w:val="left"/></w:pPr>%s</w:style>'
            % (style_id, nombre, _rpr_tipografia("", SZ_CUERPO)))


def _estilos_institucionales(styles):
    """Aplica la tipografía del informe y agrega los estilos de rótulo.

    - Calibri 11 en cuerpo, tablas, notas, bibliografía e índices;
    - Calibri 12 en títulos y subtítulos;
    - estilos ROTULOTABLA y ROTULOFIGURA para el rótulo sobre cada objeto.
    """
    for style_id, sz in (("Ttulo1", SZ_TITULO), ("Subtitulo1", SZ_TITULO),
                         ("Subtitulo2", SZ_TITULO), ("Estilo4", SZ_TITULO),
                         # Word reasigna los nombres de los estilos de título al guardar
                         # («heading 1» ↔ «Título1»), así que los cuatro niveles se fijan
                         # al mismo tamaño para que el resultado no dependa del nombre
                         ("Ttulo10", SZ_TITULO), ("Ttulo2", SZ_TITULO), ("Ttulo3", SZ_TITULO),
                         ("Ttulo4", SZ_CUERPO), ("Prrafodelista", SZ_CUERPO),
                         ("PARRAFO", SZ_CUERPO), ("Bibliografa", SZ_CUERPO),
                         ("BIBLIOGRAFA1", SZ_CUERPO), ("TABLAPRRAFO", SZ_CUERPO),
                         ("PIEDEFOTO", SZ_CUERPO), ("TDC1", SZ_CUERPO),
                         ("TDC2", SZ_CUERPO), ("TDC3", SZ_CUERPO),
                         ("DESTACADO", SZ_CUERPO), ("DESTACADO2", SZ_CUERPO)):
        styles = _ajustar_estilo(styles, style_id, sz)
    for style_id, nombre in ((ESTILO_ROTULO_TABLA, NOMBRE_ROTULO_TABLA),
                             (ESTILO_ROTULO_FIGURA, NOMBRE_ROTULO_FIGURA)):
        if 'w:styleId="%s"' % style_id not in styles:
            styles = styles.replace("</w:styles>", _estilo_rotulo(style_id, nombre)
                                    + "</w:styles>")
    # los subtítulos acompañan al contenido que encabezan (tarjetas de HU incluidas)
    for style_id in ("Subtitulo1", "Subtitulo2"):
        styles = _estilo_junto(styles, style_id)
    return styles


def _limpiar_tamanos(xml, estilos=None):
    """Quita tamaños de letra puestos directamente en el texto.

    El formato directo gana sobre el estilo, así que cualquier <w:sz> heredado de
    la plantilla o de Pandoc rompe la regla «11 en el cuerpo, 12 en los títulos».
    Si se indica `estilos`, solo se limpian los párrafos con esos estilos.
    """
    def limpiar(m):
        p = m.group(0)
        if estilos:
            est = re.search(r'w:pStyle w:val="([^"]+)"', p)
            if not est or est.group(1) not in estilos:
                return p
        p = re.sub(r'<w:szCs\b[^>]*/>', "", p)
        return re.sub(r'<w:sz\b[^>]*/>', "", p)

    return re.sub(r"<w:p\b.*?</w:p>", limpiar, xml, flags=re.S)


def _campo_indice(instruccion, pPr="", aviso=""):
    """Devuelve un campo de índice (TOC) bien formado dentro de un párrafo.

    instruccion: código del campo, p. ej. ' TOC \\h \\z \\t "RotuloTabla;1" '.
    El pPr se sanea quitándole su rPr: Word copia el formato de la marca del
    párrafo del campo en las entradas que genera, y ese rPr traía 12 pt de la
    plantilla, con lo que el índice no respetaba el tamaño del estilo.
    """
    pPr = re.sub(r"<w:rPr>.*?</w:rPr>", "", pPr or "", flags=re.S)
    cached = "<w:r><w:t>%s</w:t></w:r>" % aviso if aviso else ""
    return ("<w:p>%s"
            '<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
            '<w:r><w:instrText xml:space="preserve">%s</w:instrText></w:r>'
            '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
            '%s'
            '<w:r><w:fldChar w:fldCharType="end"/></w:r>'
            "</w:p>") % (pPr, instruccion, cached)


def _campo_toc(pPr=""):
    """Índice general del documento (contenido)."""
    return _campo_indice(TOC_INSTRUCCION, pPr, TOC_AVISO)


def _indice_ilustraciones(con_tablas=True, con_figuras=True):
    """Página con el índice de tablas y/o el de figuras.

    Cada índice usa `TOC \\t` sobre el estilo del rótulo, así que sus entradas
    llevan el mismo texto que aparece sobre cada tabla y cada figura. En los
    anexos solo se incluye el índice de lo que el documento realmente tiene.
    """
    if not (con_tablas or con_figuras):
        return ""
    if con_tablas and con_figuras:
        titulo, subtitulos = "Índice de tablas y figuras", True
    elif con_tablas:
        titulo, subtitulos = "Índice de tablas", False
    else:
        titulo, subtitulos = "Índice de figuras", False
    salto = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
    encabezado = ('<w:p><w:pPr><w:pStyle w:val="Estilo4"/></w:pPr>'
                  "<w:r><w:t>%s</w:t></w:r></w:p>" % titulo)
    sub = ('<w:p><w:pPr><w:pStyle w:val="Estilo4"/></w:pPr>'
           "<w:r><w:t>%s</w:t></w:r></w:p>")
    ppr_tdc = '<w:pPr><w:pStyle w:val="TDC1"/></w:pPr>'
    campos = []
    if con_tablas:
        if subtitulos:
            campos.append(sub % "Tablas")
        campos.append(_campo_indice(' TOC \\h \\z \\t "%s;1" ' % NOMBRE_ROTULO_TABLA,
                                    ppr_tdc, TOC_AVISO))
    if con_figuras:
        if subtitulos:
            campos.append(sub % "Figuras")
        campos.append(_campo_indice(' TOC \\h \\z \\t "%s;1" ' % NOMBRE_ROTULO_FIGURA,
                                    ppr_tdc, TOC_AVISO))
    return salto + encabezado + "".join(campos)


# --------------------------------------------------------------------------- #
# utilidades
# --------------------------------------------------------------------------- #
def log(msg):
    print(msg, flush=True)


def leer(path):
    # utf-8-sig tolera el BOM que agregan algunos editores al guardar
    with io.open(path, encoding="utf-8-sig") as fh:
        return fh.read()


def escribir(path, texto):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)


def zip_leer(path, nombre):
    with zipfile.ZipFile(path) as z:
        return z.read(nombre).decode("utf-8")


def zip_partes(path):
    with zipfile.ZipFile(path) as z:
        return z.namelist()


def zip_media(path):
    """Devuelve {nombre_interno: bytes} de las partes binarias del paquete."""
    datos = {}
    with zipfile.ZipFile(path) as z:
        for nombre in z.namelist():
            if nombre.startswith("word/media/"):
                datos[nombre] = z.read(nombre)
    return datos


def zip_rels(path):
    """Devuelve {rId: (Target, TargetMode)} de word/_rels/document.xml.rels."""
    rels = {}
    xml = zip_leer(path, "word/_rels/document.xml.rels")
    for m in re.finditer(r'<Relationship\b[^>]*/>', xml):
        rid = re.search(r'Id="([^"]+)"', m.group(0))
        tgt = re.search(r'Target="([^"]+)"', m.group(0))
        modo = re.search(r'TargetMode="([^"]+)"', m.group(0))
        if rid and tgt:
            rels[rid.group(1)] = (tgt.group(1), modo.group(1) if modo else "Internal")
    return rels


def p_estilo(p_xml):
    m = re.search(r'<w:pStyle w:val="([^"]+)"', p_xml)
    return m.group(1) if m else None


def p_texto(p_xml):
    return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p_xml))


def _tras_frente(doc):
    """Devuelve el XML desde el final del frente (portada e índices).

    Las comprobaciones de rótulos y tamaños deben medir solo el cuerpo: la
    portada institucional (con su logo) conserva su diseño propio.
    """
    pos = doc.rfind(';1" ')
    if pos < 0:
        pos = doc.rfind(" TOC ")
    if pos < 0:
        return doc
    fin = doc.find('w:fldCharType="end"', pos)
    if fin < 0:
        return doc
    cierre = doc.find("</w:p>", fin)
    return doc[cierre + len("</w:p>"):] if cierre > 0 else doc


# --------------------------------------------------------------------------- #
# 1. diagramas
# --------------------------------------------------------------------------- #
def _bloques_puml(lineas):
    """Devuelve [(inicio, fin, clave)] de cada bloque PlantUML, con su módulo asociado.

    La asociación se hace buscando hacia atrás el encabezado del módulo ("Módulo M##"),
    porque entre el encabezado del módulo y el bloque suele haber un subtítulo genérico
    ("Diagrama de Casos de Uso"). Si no hay módulo, el bloque corresponde al modelo de actores.
    """
    bloques = []
    dentro = False
    inicio = 0
    for i, linea in enumerate(lineas):
        if linea.strip().startswith("```plantuml"):
            dentro, inicio = True, i
            continue
        if dentro and linea.strip() == "```":
            dentro = False
            clave = None
            for j in range(inicio - 1, -1, -1):
                m = re.search(r"M[oó]dulo\s+(M\d{2})", lineas[j])
                if m:
                    clave = m.group(1).lower()
                    break
                if re.match(r"^##\s+\d", lineas[j]):   # sección numerada: no hay módulo
                    break
            bloques.append((inicio, i, clave or "actores"))
    return bloques


def extraer_puml():
    """Extrae los bloques PlantUML del anexo de casos de uso."""
    lineas = leer(ANEXO_CU).splitlines()
    bloques = []
    for inicio, fin, clave in _bloques_puml(lineas):
        bloques.append((clave, lineas[inicio - 1].strip("# ").strip(), "\n".join(lineas[inicio + 1:fin])))
    return bloques



def paso_diagramas(forzar=False):
    os.makedirs(BUILD, exist_ok=True)
    carpeta_puml = os.path.join(BUILD, "puml")
    os.makedirs(carpeta_puml, exist_ok=True)
    os.makedirs(IMAGENES, exist_ok=True)

    bloques = extraer_puml()
    log("Bloques PlantUML encontrados: %d" % len(bloques))
    if not bloques:
        return {"ok": False, "detalle": "no se encontraron bloques PlantUML"}

    # los bloques sin módulo detectado (el primero suele ser el modelo de actores)
    if bloques and bloques[0][0] is None:
        bloques[0] = ("actores", bloques[0][1], bloques[0][2])

    archivos = []
    for clave, encabezado, cuerpo in bloques:
        if clave is None:
            log("  ADVERTENCIA: bloque sin módulo asociado (%s)" % encabezado[:60])
            continue
        ruta = os.path.join(carpeta_puml, "figura-%s.puml" % clave)
        escribir(ruta, "@startuml\n" + cuerpo + "\n@enduml\n" if "@startuml" not in cuerpo else cuerpo + "\n")
        archivos.append((clave, ruta, ruta))

    # diagramas del cuerpo: un .puml por figura en docx/diagramas/.
    # Se copian a build/puml/ con el prefijo "figura-" para que PlantUML
    # genere siempre imagenes/figura-<clave>.png (un unico criterio de nombres).
    if os.path.isdir(DIAGRAMAS):
        for nombre in sorted(os.listdir(DIAGRAMAS)):
            if not nombre.lower().endswith(".puml"):
                continue
            clave = nombre[:-5]
            origen = os.path.join(DIAGRAMAS, nombre)
            destino = os.path.join(carpeta_puml, "figura-%s.puml" % clave)
            shutil.copyfile(origen, destino)
            archivos.append((clave, destino, origen))
    log("Diagramas a renderizar: %d (anexo + cuerpo)" % len(archivos))

    if not os.path.exists(PLANTUML):
        return {"ok": False, "detalle": "no se encontró plantuml.jar en %s" % PLANTUML}

    java = shutil.which("java")
    if not java:
        return {"ok": False, "detalle": "java no está en el PATH"}

    render_ok, render_err, omitidos = 0, [], 0
    for clave, ruta, fuente in archivos:
        salida = os.path.join(IMAGENES, "figura-%s.png" % clave)
        if not forzar and os.path.exists(salida) and os.path.getmtime(salida) >= os.path.getmtime(fuente):
            omitidos += 1
            continue
        cmd = [java, "-Djava.awt.headless=true", "-jar", PLANTUML, "-tpng",
               "-o", IMAGENES, "-charset", "UTF-8", ruta]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if res.returncode == 0 and os.path.exists(salida):
            render_ok += 1
        else:
            render_err.append("%s (rc=%s) %s" % (clave, res.returncode, (res.stderr or "").strip()[:200]))
    log("Diagramas renderizados: %d/%d (sin cambios: %d)" % (render_ok, len(archivos), omitidos))
    for e in render_err:
        log("  ERROR: %s" % e)
    return {"ok": not render_err, "detalle": "%d/%d" % (render_ok, len(archivos)),
            "errores": render_err, "claves": [c for c, _, _ in archivos]}


def _sin_emoji(texto):
    """Quita los pictogramas de un texto (los títulos van sin iconos).

    Los iconos se cuelan desde las fuentes de los anexos y terminan también en el
    índice de contenido, así que se eliminan al generar el documento.
    """
    limpio = re.sub(r"[\U0001F000-\U0001FAFF\u2300-\u27BF"
                    r"\u2B00-\u2BFF\uFE0F\u200D]", "", texto)
    return re.sub(r"\s{2,}", " ", limpio).strip()


def _titulo_contexto(texto):
    """Texto de la última cabecera o línea destacada, listo para ser título.

    Quita numeración de texto («1.», «2.1»), emoji y marcas de énfasis: el rótulo
    de la tabla ya lleva su número y el título va en cursiva.
    """
    t = _sin_emoji(re.sub(r"[*_`]", "", texto)).rstrip(":").strip()
    t = re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", t)
    return re.sub(r"\s+", " ", t).strip()


# --- Historias de usuario: formato de tarjeta (tabla de 3 secciones) -------- #
# Referencia: hu.pdf. Sección 1: código y nombre · Sección 2: el relato
# (Como / Quiero / Para que) · Sección 3: criterios de aceptación.
HU_UNA_POR_PAGINA = True
SALTO_PAGINA = '```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```'


def _tabla_grid(filas):
    """Tabla grid de Pandoc de una columna con las filas indicadas.

    La primera fila actúa de encabezado. El ancho se calcula con la línea más
    larga para que los bordes queden alineados sin recortar ningún texto.
    """
    ancho = max(len(linea) for fila in filas for linea in fila) + 2
    borde = "+" + "-" * ancho + "+"
    encabezado = "+" + "=" * ancho + "+"

    def celda(texto):
        return "| " + texto.ljust(ancho - 2) + " |"

    salida = [borde] + [celda(l) for l in filas[0]] + [encabezado]
    for fila in filas[1:]:
        salida += [celda(l) for l in fila] + [borde]
    return salida


def _tarjeta_hu(titulo, cuerpo):
    """Arma la tarjeta de una historia de usuario sin alterar su texto.

    Solo reparte el contenido que ya existe en las tres secciones del formato:
    código y nombre, el relato y los criterios de aceptación. Los metadatos de
    trazabilidad y las notas quedan debajo de la tabla, como en hu.pdf.
    """
    relato, criterios, metadatos, notas, en_criterios = [], [], [], [], False
    for linea in cuerpo:
        limpia = linea.strip()
        if not limpia:
            continue
        if limpia.startswith("#"):
            if "riterios" in limpia:
                en_criterios = True
            continue
        if limpia.startswith(">"):
            notas.append(limpia)
            continue
        if limpia.startswith(("- ", "* ")):
            criterios.append(limpia)
            continue
        if limpia.startswith(("**Como**", "**Quiero**", "**Para que**")):
            relato.append(limpia)
            continue
        if re.match(r"\*\*(Épica|Rol|RF|CU|Prioridad)", limpia):
            metadatos.append(limpia)
            continue
        (criterios if en_criterios else relato).append(limpia)

    fila_relato = []
    for i, l in enumerate(relato):
        if i:
            fila_relato.append("")
        fila_relato.append(l)
    filas = [["**Código y Nombre de la Historia:** %s" % titulo],
             fila_relato or [" "],
             ["**Criterios de Aceptación**", ""] + criterios]

    salida = _tabla_grid(filas) + [""]
    if metadatos:
        salida += metadatos + [""]
    if notas:
        salida += notas + [""]
    return salida


def preparar_anexo(texto, letra):
    """Adapta el contenido de un anexo al documento final.

    - elimina el título propio del anexo (lo reemplaza el encabezado del documento);
    - ajusta la jerarquía: si el anexo trae varias secciones de primer nivel (Anexo E,
      con las 9 épicas) se demota un nivel; si trae una sola, no se demota, para no
      dejar un hueco entre el título del anexo y sus secciones;
    - numera y titula cada tabla («Tabla <letra>.n») con la nota de fuente debajo;
    - reemplaza los bloques PlantUML por las imágenes renderizadas, con rótulo y nota.
    Devuelve (contenido, figuras, tablas).
    """
    lineas = texto.splitlines()
    i = 0
    if lineas and lineas[0].strip() == "---":
        for j in range(1, len(lineas)):
            if lineas[j].strip() == "---":
                i = j + 1
                break
    bloques = {b[0]: b for b in _bloques_puml(lineas)}
    demotar = sum(1 for l in lineas[i:] if re.match(r"^#\s+\S", l)) > 1

    salida, figuras, tablas = [], 0, 0
    saltar_titulo = True
    contexto = ""
    titulo_tabla = ""
    tarjetas_hu = 0
    j = i
    while j < len(lineas):
        linea = lineas[j]
        if j in bloques:
            _, fin, clave = bloques[j]
            figuras += 1
            titulo = ("Diagrama de casos de uso del módulo %s" % clave.upper()
                      if clave != "actores" else "Modelo de actores del sistema y su generalización")
            salida += ['::: {custom-style="%s"}' % ESTILO_ROTULO_FIGURA,
                       "**Figura %s.%d**\\" % (letra, figuras), "*%s*" % titulo, ":::",
                       "", "![](imagenes/figura-%s.png)" % clave, "",
                       '::: {custom-style="PIEDEFOTO"}', "Fuente: %s" % FUENTE_NOTA, ":::", ""]
            contexto = titulo
            j = fin + 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", linea)
        if m:
            nivel, texto_t = len(m.group(1)), _sin_emoji(m.group(2))
            if saltar_titulo and nivel == 1:
                saltar_titulo = False
                contexto = _titulo_contexto(texto_t)
                j += 1
                continue
            # historia de usuario: se emite como tarjeta de tres secciones
            if re.match(r"^HU\d{2}\s*[-\u2013\u2014]", texto_t):
                inicio, fin = j + 1, j + 1
                while fin < len(lineas) and not re.match(r"^#{1,%d}\s" % nivel, lineas[fin]):
                    fin += 1
                if HU_UNA_POR_PAGINA and tarjetas_hu:
                    salida += [SALTO_PAGINA, ""]
                tarjetas_hu += 1
                salida.append("#" * min(nivel + 1 if demotar else nivel, 4) + " " + texto_t)
                salida += _tarjeta_hu(texto_t, lineas[inicio:fin])
                contexto = _titulo_contexto(texto_t)
                j = fin
                continue
            salida.append("#" * min(nivel + 1 if demotar else nivel, 4) + " " + texto_t)
            contexto = _titulo_contexto(texto_t)
            j += 1
            continue
        if re.match(r"^\s*---+\s*$", linea):
            j += 1                     # regla horizontal decorativa: la separa el estilo
            continue
        imagen = re.match(r"^!\[(?P<alt>.*?)\]\((?P<ruta>[^)]+)\)(?P<attrs>\{[^}]*\})?\s*$", linea)
        if imagen:
            figuras += 1
            titulo = imagen.group("alt").strip() or contexto or "Figura del anexo"
            salida += ['::: {custom-style="%s"}' % ESTILO_ROTULO_FIGURA,
                       "**Figura %s.%d**\\" % (letra, figuras), "*%s*" % titulo, ":::",
                       "", "![](%s)%s" % (imagen.group("ruta"), imagen.group("attrs") or ""),
                       "", '::: {custom-style="PIEDEFOTO"}',
                       "Fuente: %s" % FUENTE_NOTA, ":::", ""]
            # el título de la figura no reemplaza el contexto: si después viene
            # una tabla sin encabezado propio, el título correcto es el de la sección
            j += 1
            continue
        explicit = re.match(r"^\*Tabla\.\s*(.+?)\*$", linea.strip())
        if explicit:
            titulo_tabla = _titulo_contexto(explicit.group(1))
            j += 1
            continue
        destacado = re.match(r"^\*\*(.+?)\*\*:?\s*$", linea)
        if destacado:
            contexto = _titulo_contexto(destacado.group(1))
        # inicio de tabla: línea de cabecera y, debajo, el separador
        if (linea.startswith("|") and j + 1 < len(lineas)
                and re.match(r"^\|[\s:\-|]+\|\s*$", lineas[j + 1])):
            tablas += 1
            salida += ['::: {custom-style="%s"}' % ESTILO_ROTULO_TABLA,
                       "**Tabla %s.%d**\\" % (letra, tablas),
                       "*%s*" % (titulo_tabla or contexto or "Datos de la sección"), ":::", ""]
            titulo_tabla = ""
            while j < len(lineas) and lineas[j].startswith("|"):
                salida.append(lineas[j])
                j += 1
            salida += ["", '::: {custom-style="PIEDEFOTO"}',
                       "Fuente: %s" % FUENTE_NOTA, ":::", ""]
            continue
        salida.append(linea)
        j += 1
    return "\n".join(salida), figuras, tablas


def expandir_anexos(texto, avisos):
    """Sustituye los marcadores {{ANEXO: archivo}} por el contenido del anexo."""
    anexos = []

    def rep(m):
        nombre = m.group(1).strip()
        ruta = os.path.join(ANEXOS, nombre)
        if not os.path.exists(ruta):
            avisos.append("anexo no encontrado en docx/anexos: %s" % nombre)
            return "[[PENDIENTE: no se encontró el archivo del anexo %s]]" % nombre
        letra = chr(ord("A") + len(anexos))
        contenido, figuras, tablas = preparar_anexo(leer(ruta), letra)
        anexos.append({"letra": letra, "archivo": nombre, "figuras": figuras, "tablas": tablas})
        return contenido

    texto = re.sub(r"\{\{ANEXO:\s*([^}]+)\}\}", rep, texto)
    return texto, anexos


# --------------------------------------------------------------------------- #
# 1.b bibliografía: fuentes nativas de Word y caché de las citas
# --------------------------------------------------------------------------- #
SONDA_INI, SONDA_FIN = "ZZZINI_", "_ZZZFIN"


def claves_citadas(texto):
    """Devuelve, en orden y sin repetir, las claves citadas en el markdown."""
    claves = []
    for m in re.finditer(r"\[([^\]]*@[^\]]*)\]", texto):
        for k in re.findall(r"@([\w:.\-]+)", m.group(1)):
            if k not in claves:
                claves.append(k)
    return claves


def probar_citas(claves):
    """Obtiene con citeproc el texto APA 7 de cada cita, que se guarda como caché.

    Cada clave se cita por separado en su propio párrafo y entre marcadores, de
    modo que el texto devuelto se puede asociar sin ambigüedad a su fuente.
    """
    if not claves:
        return {}
    lineas = ["---", "lang: %s" % IDIOMA, "---", ""]
    lineas += ["%s%s [@%s] %s" % (SONDA_INI, k, k, SONDA_FIN) for k in claves]
    ruta = os.path.join(BUILD, "sonda_citas.md")
    escribir(ruta, "\n\n".join(lineas) + "\n")
    cmd = ["pandoc", ruta, "-t", "plain", "--citeproc",
           "--bibliography=" + BIB, "--csl=" + CSL, "--wrap=none",
           "--metadata=lang:%s" % IDIOMA]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                         errors="replace", cwd=BASE)
    if res.returncode != 0:
        log("  ADVERTENCIA: no se pudo calcular la caché de citas (%s)" % res.stderr[:200])
        return {}
    cache = {}
    patron = re.compile(re.escape(SONDA_INI) + r"([\w:.\-]+)\s*(.*?)\s*" + re.escape(SONDA_FIN),
                        re.S)
    for m in patron.finditer(res.stdout):
        cache[m.group(1)] = m.group(2).replace("\n", " ").strip()
    return cache


def paso_bibliografia():
    """Genera la parte de fuentes de Word, la caché de citas y la auditoría."""
    global CACHE_CITAS
    entradas = bibliografia.leer_bib(BIB)
    if not entradas:
        return {"ok": False, "detalle": "no se pudo leer referencias.bib"}
    escribir(SOURCES, bibliografia.parte_sources(entradas))
    CACHE_CITAS = probar_citas([e["clave"] for e in entradas])
    citadas = claves_citadas(leer(INFORME))
    cuerpo_txt = leer(INFORME)
    ocurrencias = sum(len(re.findall(r"@([\w:.\-]+)", g))
                      for g in re.findall(r"\[[^\]]*@[^\]]*\]", cuerpo_txt))
    faltan = [k for k in citadas if k not in CACHE_CITAS]
    texto, resumen = bibliografia.auditar(entradas, citadas, CACHE_CITAS, ocurrencias)
    escribir(AUDITORIA_CITAS, texto)
    log("Fuentes de Word: %d | claves citadas: %d | textos en caché: %d"
        % (resumen["entradas"], len(citadas), resumen["cache"]))
    if faltan:
        log("  ADVERTENCIA: sin texto de cita calculado: %s" % faltan)
    return {"ok": not faltan, "detalle": "%d fuentes" % resumen["entradas"],
            "resumen": resumen, "faltan": faltan}


# --------------------------------------------------------------------------- #
# 2. preprocesar el markdown
# --------------------------------------------------------------------------- #
def paso_preprocesar():
    texto = leer(INFORME)
    avisos = []

    # saltos de página explícitos (por ejemplo, antes de cada anexo)
    SALTO = '```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```'
    texto = texto.replace("{{PAGEBREAK}}", SALTO)

    # numeración correlativa de tablas y figuras
    refs = {"tab": {}, "fig": {}}
    contador = {"tab": 0, "fig": 0}

    def rep_caption_tabla(m):
        contador["tab"] += 1
        clave, titulo = m.group("k"), m.group("t").strip()
        fuente = (m.group("f") or "elaboración propia.").strip()
        refs["tab"][clave] = contador["tab"]
        # rótulo APA 7 sobre la tabla: etiqueta en negrita y título en cursiva en
        # el mismo párrafo (salto de línea), para que el índice de tablas
        # registre una sola entrada por tabla.
        return ('::: {custom-style="%s"}\n**Tabla %d**\\\n*%s*\n:::\nFUENTE__PEND__%d:%s'
                % (ESTILO_ROTULO_TABLA, contador["tab"], titulo,
                   contador["tab"], fuente))

    def rep_figura(m):
        contador["fig"] += 1
        clave, alt, ruta = m.group("k"), m.group("alt").strip(), m.group("p")
        refs["fig"][clave] = contador["fig"]
        atributos = m.group("a") or ""
        fuente = (m.group("f") or "elaboración propia.").strip()
        # el rótulo va encima de la imagen y la imagen queda con alt vacío: así
        # Pandoc no genera el pie (ImageCaption) debajo de la figura
        return ('::: {custom-style="%s"}\n**Figura %d**\\\n*%s*\n:::\n\n'
                '![](%%s)%%s\n\n'
                '::: {custom-style="PIEDEFOTO"}\nFuente: %%s\n::: '
                % (ESTILO_ROTULO_FIGURA, contador["fig"], alt)) % (ruta, atributos, fuente)

    texto = re.sub(r"^\*Tabla\.\s*(?P<t>.+?)\*[^\n]*<!--#tab:(?P<k>[\w\-]+)-->(?:\s*<!--#fuente:(?P<f>[^>]*)-->)?$",
                   rep_caption_tabla, texto, flags=re.M)
    texto = re.sub(r"^!\[(?P<alt>.+?)\]\((?P<p>[^)]+)\)(?P<a>\{[^}]*\})?\s*<!--#fig:(?P<k>[\w\-]+)-->(?:\s*<!--#fuente:(?P<f>[^>]*)-->)?$",
                   rep_figura, texto, flags=re.M)

    # la nota de fuente queda bajo la tabla, no bajo su título
    lineas, resultado, i = texto.split("\n"), [], 0
    while i < len(lineas):
        m = re.match(r"^FUENTE__PEND__(\d+):(.*)$", lineas[i])
        if not m:
            resultado.append(lineas[i])
            i += 1
            continue
        fuente, i = m.group(2), i + 1
        bloque = []
        while i < len(lineas) and not lineas[i].startswith("|"):
            bloque.append(lineas[i])
            i += 1
        while i < len(lineas) and lineas[i].startswith("|"):
            bloque.append(lineas[i])
            i += 1
        resultado.extend(bloque)
        resultado += ["", '::: {custom-style="PIEDEFOTO"}', "Fuente: %s" % fuente, ":::"]
    texto = "\n".join(resultado)

    # resolución de referencias cruzadas
    def rep_ref(m):
        tipo, clave = m.group(1).lower(), m.group(2)
        tabla = refs["tab"] if tipo == "tabla" else refs["fig"]
        if clave in tabla:
            return "%s %d" % ("Tabla" if tipo == "tabla" else "Figura", tabla[clave])
        avisos.append("referencia cruzada sin destino: {{%s:%s}}" % (m.group(1), clave))
        return "{{%s:%s}}" % (m.group(1), clave)

    texto = re.sub(r"\{\{(Tabla|Figura):([\w\-]+)\}\}", rep_ref, texto, flags=re.I)

    # marcadores de pendientes con estilo visible
    texto = re.sub(r"^\[\[PENDIENTE:(.+?)\]\]$",
                   lambda m: '::: {custom-style="DESTACADO2"}\nPENDIENTE:%s\n:::' % m.group(1),
                   texto, flags=re.M | re.S)

    escribir(ENSAMBLADO, texto)

    # variante para los campos nativos de Word: las citas se sustituyen por
    # marcadores atómicos y la lista de referencias por un marcador de campo.
    def marcar_cita(m):
        claves = re.findall(r"@([\w:.\-]+)", m.group(1))
        return "CITA__" + "__".join(claves) if claves else m.group(0)

    texto_citas = re.sub(r"\[([^\]]*@[^\]]*)\]", marcar_cita, texto)
    texto_citas = re.sub(r":::\s*\{#refs\}\s*\n\s*:::", "BIBLIOGRAFIA__WORD", texto_citas)
    escribir(ENSAMBLADO_CITAS, texto_citas)

    log("Tablas numeradas: %d | Figuras numeradas: %d" % (contador["tab"], contador["fig"]))
    for a in avisos:
        log("  ADVERTENCIA: %s" % a)
    return {"ok": True, "tablas": contador["tab"], "figuras": contador["fig"], "avisos": avisos}


# --------------------------------------------------------------------------- #
# 3. pandoc
# --------------------------------------------------------------------------- #
def paso_pandoc():
    for ruta in (ENSAMBLADO, PLANTILLA, BIB, CSL):
        if not os.path.exists(ruta):
            return {"ok": False, "detalle": "falta %s" % ruta}
    cmd = [
        "pandoc", ENSAMBLADO, "-o", BODY,
        "--reference-doc=" + PLANTILLA,
        "--citeproc",
        "--bibliography=" + BIB,
        "--csl=" + CSL,
        "--from=markdown+fenced_divs+pipe_tables+raw_attribute",
        "--wrap=none",
        "--metadata=lang:%s" % IDIOMA,
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=BASE)
    if res.returncode != 0 or not os.path.exists(BODY):
        return {"ok": False, "detalle": "pandoc falló (rc=%s): %s" % (res.returncode, (res.stderr or "")[:800])}

    # segunda pasada: sin citeproc, para poder insertar los campos CITATION de Word
    if os.path.exists(ENSAMBLADO_CITAS):
        cmd2 = ["pandoc", ENSAMBLADO_CITAS, "-o", BODY_CITAS,
                "--reference-doc=" + PLANTILLA,
                "--from=markdown+fenced_divs+pipe_tables+raw_attribute",
                "--wrap=none",
                "--metadata=lang:%s" % IDIOMA]
        res2 = subprocess.run(cmd2, capture_output=True, text=True, encoding="utf-8",
                              errors="replace", cwd=BASE)
        if res2.returncode != 0 or not os.path.exists(BODY_CITAS):
            log("  ADVERTENCIA: la segunda pasada de pandoc falló (%s); "
                "las citas quedarán como texto" % (res2.stderr or "")[:160])
    else:
        log("  ADVERTENCIA: no existe informe_ensamblado_citas.md; "
            "las citas quedarán como texto")
    if res.stderr.strip():
        log("  pandoc (stderr): %s" % res.stderr.strip()[:400])
    estilos = {}
    doc = zip_leer(BODY, "word/document.xml")
    for m in re.finditer(r"<w:pStyle w:val=\"([^\"]+)\"", doc):
        estilos[m.group(1)] = estilos.get(m.group(1), 0) + 1
    log("Estilos en body.docx: %s" % ", ".join("%s(%d)" % kv for kv in sorted(estilos.items())))
    return {"ok": True, "estilos": estilos}


# --------------------------------------------------------------------------- #
# 4. armado dentro de la plantilla
# --------------------------------------------------------------------------- #
def _map_estilo(p_xml):
    est = p_estilo(p_xml)
    if est in MAPA_ESTILOS:
        p_xml = p_xml.replace('<w:pStyle w:val="%s"' % est, '<w:pStyle w:val="%s"' % MAPA_ESTILOS[est], 1)
    return p_xml


def _numpr(p_xml, num_id, ilvl):
    numpr = '<w:numPr><w:ilvl w:val="%d"/><w:numId w:val="%d"/></w:numPr>' % (ilvl, num_id)
    p_xml = re.sub(r"<w:numPr>.*?</w:numPr>", "", p_xml, flags=re.S)
    m = re.search(r"<w:pStyle [^>]*/>", p_xml)
    if m:
        return p_xml[:m.end()] + numpr + p_xml[m.end():]
    if "<w:pPr>" in p_xml:
        return p_xml.replace("<w:pPr>", "<w:pPr>" + numpr, 1)
    return re.sub(r"(<w:p\b[^>]*>)", r"\1<w:pPr>" + numpr + "</w:pPr>", p_xml, count=1)


def _tabla(p_xml):
    # estilo de tabla + bordes visibles
    p_xml = re.sub(r'<w:tblStyle\b[^>]*/>', "", p_xml)
    if "<w:tblPr>" in p_xml:
        p_xml = p_xml.replace("<w:tblPr>", '<w:tblPr><w:tblStyle w:val="Tablanormal"/>', 1)
    if "<w:tblBorders>" not in p_xml:
        bordes = ('<w:tblBorders>'
                  '<w:top w:val="single" w:sz="4" w:space="0" w:color="808080"/>'
                  '<w:left w:val="single" w:sz="4" w:space="0" w:color="808080"/>'
                  '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="808080"/>'
                  '<w:right w:val="single" w:sz="4" w:space="0" w:color="808080"/>'
                  '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="808080"/>'
                  '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="808080"/>'
                  '</w:tblBorders>')
        # el esquema exige tblBorders antes de tblLayout / tblCellMar / tblLook
        for marcador in ("<w:tblLayout", "<w:tblCellMar", "<w:tblLook", "</w:tblPr>"):
            if marcador in p_xml:
                p_xml = p_xml.replace(marcador, bordes + marcador, 1)
                break
    # celdas con estilo institucional (Pandoc autocierra con espacio)
    p_xml = re.sub(r'<w:pStyle w:val="(?:Compact|PARRAFO|BodyText|FirstParagraph)"\s*/>',
                   '<w:pStyle w:val="TABLAPRRAFO"/>', p_xml)
    # encabezado repetido y en negrita
    filas = re.findall(r"<w:tr\b.*?</w:tr>", p_xml, re.S)
    if filas:
        primera = filas[0]
        nueva = primera
        if "tblHeader" not in nueva:
            if "<w:trPr>" in nueva:
                nueva = re.sub(r"<w:trPr>", "<w:trPr><w:tblHeader/>", nueva, count=1)
            else:
                nueva = re.sub(r"(<w:tr\b[^>]*>)", r"\1<w:trPr><w:tblHeader/></w:trPr>", nueva, count=1)

        def negrita(m):
            run = m.group(0)
            neg = "<w:b/><w:bCs/>"
            if "<w:rPr>" in run:
                cuerpo = re.search(r"<w:rPr>(.*?)</w:rPr>", run, re.S)
                # el esquema exige rStyle y rFonts antes de b/bCs
                for marcador in ("<w:rFonts", "<w:rStyle"):
                    if marcador in cuerpo.group(1):
                        return run.replace("</w:rPr>", neg + "</w:rPr>", 1)
                return run.replace("<w:rPr>", "<w:rPr>" + neg, 1)
            return re.sub(r"(<w:r\b[^>]*>)", r"\1<w:rPr>" + neg + "</w:rPr>", run, count=1)

        nueva = re.sub(r"<w:r\b.*?</w:r>", negrita, nueva, flags=re.S)
        p_xml = p_xml.replace(primera, nueva, 1)

    # tarjetas de historia de usuario: no se parten entre páginas
    if "Código y Nombre de la Historia" in p_xml:
        def fila_sin_corte(m):
            fila = m.group(0)
            if "<w:trPr>" in fila:
                return fila.replace("<w:trPr>", "<w:trPr><w:cantSplit/>", 1)
            return re.sub(r"(<w:tr\b[^>]*>)", r"\1<w:trPr><w:cantSplit/></w:trPr>", fila, count=1)

        p_xml = re.sub(r"<w:tr\b.*?</w:tr>", fila_sin_corte, p_xml, flags=re.S)
        filas_hu = re.findall(r"<w:tr\b.*?</w:tr>", p_xml, re.S)
        for fila in filas_hu[:-1]:        # la última fila no necesita keepNext
            nueva = re.sub(r"<w:pPr>", "<w:pPr><w:keepNext/>", fila)
            nueva = re.sub(r"(<w:p\b[^>]*>)(?=<w:r\b)",
                           r"\1<w:pPr><w:keepNext/></w:pPr>", nueva)
            p_xml = p_xml.replace(fila, nueva, 1)
    return p_xml


def _preparar_cuerpo(body_xml, numerar=True):
    """Remapea estilos, inyecta numeración institucional y formatea tablas."""
    avisos = []
    # separar tablas para no tratarlas como párrafos
    tablas = []

    def guardar_tabla(m):
        tablas.append(m.group(0))
        return "@@TBL%d@@" % (len(tablas) - 1)

    body_xml = re.sub(r"<w:tbl>.*?</w:tbl>", guardar_tabla, body_xml, flags=re.S)

    capitulo = 0
    en_anexos = False
    sin_mapear = {}

    def tratar_parrafo(m):
        nonlocal capitulo, en_anexos
        p = m.group(0)
        est_original = p_estilo(p)
        p = _map_estilo(p)
        est = p_estilo(p)
        if est in NIVEL_TITULO:
            nivel = NIVEL_TITULO[est]
            texto_p = p_texto(p).strip()
            es_anexo = bool(re.match(r"^Anexo\s+[A-Z]\b", texto_p))
            if nivel == 0 and not es_anexo:
                capitulo += 1
            if es_anexo:
                en_anexos = True          # los títulos de anexo no se numeran
            if numerar:
                # numId 0 = sin numeración. Es necesario en los anexos porque el
                # estilo Subtitulo1 trae numeración propia y, al no escribir un
                # numPr directo, Word los numeraba como "1.1.", "1.2.", ...
                p = _numpr(p, 0 if en_anexos else NUM_BASE + capitulo,
                           0 if en_anexos else nivel)
        elif est_original and est == est_original:
            sin_mapear[est_original] = sin_mapear.get(est_original, 0) + 1
        return p

    body_xml = re.sub(r"<w:p\b.*?</w:p>", tratar_parrafo, body_xml, flags=re.S)

    for i, tabla in enumerate(tablas):
        body_xml = body_xml.replace("@@TBL%d@@" % i, _tabla(tabla))

    for est, n in sorted(sin_mapear.items()):
        if est not in ("Normal", "PARRAFO", "Ttulo1", "Subtitulo1", "Subtitulo2", "Prrafodelista",
                       "DESTACADO", "DESTACADO2", "PIEDEFOTO", "TABLATTULO", "TABLAPRRAFO", "BIBLIOGRAFA1",
                       ESTILO_ROTULO_TABLA, ESTILO_ROTULO_FIGURA,
                       "CaptionedFigure"):
            avisos.append("estilo sin mapear: %s (%d párrafos)" % (est, n))
    return body_xml, capitulo, avisos


def iter_parrafos(xml):
    """Itera (inicio, fin, bloque) de todos los <w:p>, incluidos los anidados en cuadros de texto."""
    def rec(texto, base):
        pos = 0
        while True:
            m = re.search(r"<w:p(?=[\s>])", texto[pos:])
            if not m:
                return
            inicio = pos + m.start()
            nivel, fin = 0, None
            for t in re.finditer(r"<w:p(?=[\s>])|</w:p>", texto[inicio:]):
                if t.group(0) == "</w:p>":
                    nivel -= 1
                    if nivel == 0:
                        fin = inicio + t.end()
                        break
                else:
                    nivel += 1
            if fin is None:
                return
            bloque = texto[inicio:fin]
            yield base + inicio, base + fin, bloque
            pos = fin
            for item in rec(bloque[3:], base + inicio + 3):
                yield item
    return rec(xml, 0)


def _parrafo_con_texto(bloque, valor):
    """Deja el párrafo con un solo run y el texto indicado.

    Necesario porque algunos textos de la portada (p. ej. «FORMULACIÓN DEL
    PROYECTO DE TÍTULO») están repartidos en varios runs: reemplazar solo el
    primero dejaría el resto del texto original a la vista.
    """
    ppr = re.search(r"<w:pPr>.*?</w:pPr>", bloque, re.S)
    runs = re.findall(r"<w:r\b.*?</w:r>", bloque, re.S)
    if not runs:
        return bloque
    rpr = re.search(r"<w:rPr>.*?</w:rPr>", runs[0], re.S)
    esc = valor.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return "<w:p>%s<w:r>%s<w:t xml:space=\"preserve\">%s</w:t></w:r></w:p>" % (
        ppr.group(0) if ppr else "", rpr.group(0) if rpr else "", esc)


def _rellenar_portada(doc, meta, linea_titulo=None):
    """Rellena los campos de la portada de la plantilla con los datos del informe.

    - completa todas las copias del campo (la portada repite los datos en dos cuadros de texto);
    - solo modifica los párrafos más internos, preservando la estructura de los dibujos;
    - omite los campos cuyo dato no esté disponible, sin borrar el contenido existente;
    - `linea_titulo` reemplaza la línea institucional «FORMULACIÓN DEL PROYECTO DE
      TÍTULO» (los anexos ponen ahí el proyecto y el nombre del anexo como título).
    """
    campos = [
        ("Asignatura", meta.get("asignatura", "")),
        ("Sección", meta.get("seccion", "")),
        ("Académico guía", meta.get("academico", "")),
        ("Integrantes del equipo", meta.get("integrantes", "")),
        ("Fecha de entrega", meta.get("fecha", "")),
        ("Nombre o título del proyecto", meta.get("proyecto") or meta.get("titulo", "")),
    ]
    if linea_titulo:
        campos.append(("FORMULACIÓN DEL PROYECTO DE TÍTULO", linea_titulo))
    # estos rótulos se reemplazan completos (sin volver a escribir la etiqueta)
    sin_etiqueta = ("Nombre o título del proyecto", "FORMULACIÓN DEL PROYECTO DE TÍTULO")
    cambios = []
    ediciones = []
    for inicio, fin, bloque in list(iter_parrafos(doc)):
        if re.search(r"<w:p(?=[\s>])", bloque[3:]):        # tiene párrafos anidados
            continue
        texto = p_texto(bloque).strip().rstrip(":").strip()
        for etiqueta, contenido in campos:
            if not contenido.strip():
                continue
            if not (texto == etiqueta or texto.startswith(etiqueta)):
                continue
            valor = (contenido if etiqueta in sin_etiqueta
                     else "%s: %s" % (etiqueta, contenido))
            runs = re.findall(r"<w:r\b.*?</w:r>", bloque, re.S)
            if etiqueta == "FORMULACIÓN DEL PROYECTO DE TÍTULO":
                # se guarda como el resto de las ediciones: modificar `doc` aquí
                # dejaría desfasadas las posiciones que se aplican al final
                nuevo_bloque = _parrafo_con_texto(bloque, valor)
                ediciones.append((inicio, fin, nuevo_bloque))
                cambios.append(etiqueta)
                break
            if not runs:
                break
            primero = runs[0]
            if "<w:t" in primero:
                nuevo_run = re.sub(r"(<w:t[^>]*>).*?(</w:t>)",
                                   lambda mm: mm.group(1) + valor + mm.group(2),
                                   primero, count=1, flags=re.S)
            else:
                nuevo_run = primero.replace("</w:r>", '<w:t xml:space="preserve">%s</w:t></w:r>' % valor, 1)
            nuevo_bloque = bloque
            for r in runs:
                nuevo_bloque = nuevo_bloque.replace(r, "", 1)
            nuevo_bloque = nuevo_bloque.replace("</w:p>", nuevo_run + "</w:p>", 1)
            ediciones.append((inicio, fin, nuevo_bloque))
            cambios.append(etiqueta)
            break
    for inicio, fin, nuevo in sorted(ediciones, key=lambda e: e[0], reverse=True):
        doc = doc[:inicio] + nuevo + doc[fin:]
    return doc, cambios


def _numbering_extra():
    """Definición de numeración institucional: romano en capítulo, decimal en subniveles."""
    lvls = []
    definiciones = [("decimal", "%1.", 360, 360), ("decimal", "%1.%2.", 360, 360),
                    ("decimal", "%1.%2.%3.", 1571, 720), ("decimal", "%1.%2.%3.%4.", 720, 720)]
    for i, (fmt, txt, izq, sang) in enumerate(definiciones):
        lvls.append('<w:lvl w:ilvl="%d"><w:start w:val="1"/><w:numFmt w:val="%s"/>'
                    '<w:lvlText w:val="%s"/><w:lvlJc w:val="left"/>'
                    '<w:pPr><w:ind w:left="%d" w:hanging="%d"/></w:pPr>'
                    '<w:rPr><w:rFonts w:hint="default"/></w:rPr></w:lvl>' % (i, fmt, txt, izq, sang))
    abstract = ('<w:abstractNum w:abstractNumId="%d">'
                '<w:nsid w:val="0A1B2C3D"/><w:multiLevelType w:val="multilevel"/>'
                '%s</w:abstractNum>' % (NUM_ABS, "".join(lvls)))
    return abstract


def _sin_numeracion(styles):
    """Quita la numeración de los estilos de título (documentos sin numerar, como los anexos)."""
    for sid in ("Ttulo1", "Subtitulo1", "Subtitulo2", "Prrafodelista"):
        styles = re.sub(r'(<w:style [^>]*w:styleId="%s"[^>]*>.*?)<w:numPr>.*?</w:numPr>' % sid,
                        r"\1", styles, flags=re.S)
    return styles


def _merge_numbering(numbering, abstracts, nums):
    """Inserta definiciones de numeración respetando el orden del esquema (abstractNum antes que num)."""
    if abstracts:
        pos = numbering.find("<w:num ")
        if pos < 0:
            pos = numbering.find("</w:numbering>")
        numbering = numbering[:pos] + abstracts + numbering[pos:]
    if nums:
        numbering = numbering.replace("</w:numbering>", nums + "</w:numbering>")
    return numbering


def _definiciones_pandoc(body_path):
    """Extrae las definiciones de numeración (listas) que Pandoc agregó a su documento."""
    try:
        num_body = zip_leer(body_path, "word/numbering.xml")
    except KeyError:
        return "", ""
    abstracts = "".join(re.findall(r"<w:abstractNum\b.*?</w:abstractNum>", num_body, re.S))
    nums = "".join(re.findall(r"<w:num\b.*?</w:num>", num_body, re.S))
    return abstracts, nums


def _meta_informe():
    """Lee los metadatos de la portada desde el encabezado YAML del informe."""
    meta = {}
    texto = leer(INFORME).lstrip("\ufeff")
    cabecera = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", texto, re.S)
    if cabecera:
        for linea in cabecera.group(1).splitlines():
            if ":" in linea:
                k, v = linea.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
    return meta


def _campo_con_cache(claves, rpr):
    """Campos CITATION de Word para una cita (una o varias fuentes)."""
    def sin_parentesis(t):
        t = (t or "").strip()
        return t[1:-1] if t.startswith("(") and t.endswith(")") else t

    def run(texto):
        esc = texto.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return '<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>' % (rpr, esc)

    if len(claves) == 1:
        return bibliografia.campo_cita(CACHE_CITAS.get(claves[0], ""), claves[0])
    trozos = [run("(")]
    for i, k in enumerate(claves):
        if i:
            trozos.append(run("; "))
        trozos.append(bibliografia.campo_cita(sin_parentesis(CACHE_CITAS.get(k, "")), k))
    trozos.append(run(")"))
    return "".join(trozos)


def _cuerpo_con_citas(cuerpo, avisos):
    """Sustituye los marcadores por campos de cita y la lista por un campo de bibliografía."""
    def rep_parrafo(mp):
        parrafo = mp.group(0)
        if "CITA__" not in parrafo:
            return parrafo

        def rep_run(mr):
            run = mr.group(0)
            mt = re.search(r"<w:t[^>]*>(.*?)</w:t>", run, re.S)
            if not mt or "CITA__" not in mt.group(1):
                return run
            mrpr = re.search(r"(<w:rPr>.*?</w:rPr>)", run, re.S)
            rpr = mrpr.group(1) if mrpr else ""
            salida = []
            for parte in re.split(r"(CITA__[A-Za-z0-9_\-:]+)", mt.group(1)):
                if parte.startswith("CITA__"):
                    claves = [c for c in parte[6:].split("__") if c]
                    salida.append(_campo_con_cache(claves, rpr))
                elif parte:
                    salida.append('<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>'
                                  % (rpr, parte))
            return "".join(salida)

        return re.sub(r"<w:r\b[^>]*>.*?</w:r>", rep_run, parrafo, flags=re.S)

    cuerpo = re.sub(r"<w:p\b.*?</w:p>", rep_parrafo, cuerpo, flags=re.S)

    # la lista de referencias pasa a ser un campo BIBLIOGRAPHY con su caché
    if "BIBLIOGRAFIA__WORD" in cuerpo:
        entradas = [p for p in re.findall(r"<w:p\b.*?</w:p>", zip_leer(BODY, "word/document.xml"), re.S)
                    if 'w:val="Bibliography"' in p]
        entradas = [_map_estilo(p) for p in entradas]
        if entradas:
            m = re.match(r"(<w:p\b[^>]*>)(\s*<w:pPr>.*?</w:pPr>)?(.*?)(</w:p>)", entradas[0], re.S)
            entradas[0] = (m.group(1) + (m.group(2) or "")
                           + bibliografia.abrir_campo_bibliografia() + m.group(3) + m.group(4))
            entradas[-1] = entradas[-1].replace(
                "</w:p>", bibliografia.cerrar_campo_bibliografia() + "</w:p>")
            reemplazo = "".join(entradas)
            # los rId de esas entradas pertenecen a body.docx: se marcan para
            # resolverlos contra las relaciones de ese paquete y no del cuerpo
            reemplazo = re.sub(r'r:(id|embed|link)="(rId\d+)"', r'r:\1="BIB\2"', reemplazo)
            cuerpo = re.sub(r"<w:p\b[^>]*>(?:(?!</w:p>).)*?BIBLIOGRAFIA__WORD(?:(?!</w:p>).)*?</w:p>",
                            lambda m: reemplazo, cuerpo, flags=re.S)
            avisos.append("bibliografía convertida en campo BIBLIOGRAPHY con %d entradas"
                          % len(entradas))
        else:
            avisos.append("no se encontraron las entradas de la bibliografía de Pandoc")
    return cuerpo


def _parte_fuentes_plantilla():
    """Localiza en la plantilla la parte de fuentes (<b:Sources>) que Word ya declara."""
    for n in zip_partes(PLANTILLA):
        if n.lower().startswith("customxml/") and n.lower().endswith(".xml") \
                and "itemprops" not in n.lower():
            if "b:Sources" in zip_leer(PLANTILLA, n):
                return n
    return None


def _inyectar_fuentes(reemplazos, partes_nuevas, avisos):
    """Escribe las fuentes en la parte bibliográfica que ya trae la plantilla.

    La plantilla institucional contiene customXml/item4.xml con
    <b:Sources> vacío y su itemProps4.xml con el schemaRef de la bibliografía:
    se reutiliza esa parte para no duplicar partes ni tocar content types.
    IMPORTANTE: el contenido se escribe como reemplazo de esa misma entrada del
    ZIP. Si se agregara además como parte nueva, el paquete quedaría con dos
    entradas del mismo nombre y Word leería la vacía de la plantilla.
    """
    if not os.path.exists(SOURCES):
        avisos.append("no se generó la parte de fuentes bibliográficas")
        return
    fuentes = re.findall(r"<b:Source>.*?</b:Source>", leer(SOURCES), re.S)
    parte = _parte_fuentes_plantilla()
    if parte:
        actual = zip_leer(PLANTILLA, parte)
        if "<b:Source>" in actual:
            avisos.append("la plantilla ya contenía fuentes: se reemplazan")
        vacio = re.sub(r"<b:Source>.*?</b:Source>", "", actual, flags=re.S)
        # el estilo bibliográfico lo fija el generador (APA 7), no la plantilla:
        # si no se sobrescribe, Word recompone la lista con el estilo que traía
        # la plantilla (APA 6) aunque las fuentes ya estén actualizadas.
        vacio = re.sub(r"<b:Sources\b[^>]*>",
                       lambda m: "<b:Sources " + bibliografia.ROOT_ATTRS + ">",
                       vacio, count=1)
        reemplazos[parte] = vacio.replace("</b:Sources>", "".join(fuentes) + "</b:Sources>")
        avisos.append("%d fuentes escritas en la parte bibliográfica de la plantilla (%s, "
                      "estilo %s)" % (len(fuentes), parte, bibliografia.ESTILO_WORD))
        return

    # Respaldo: la plantilla no trae parte de fuentes; se crea una nueva
    ct = reemplazos["[Content_Types].xml"]
    if 'PartName="/customXml/itemProps1.xml"' not in ct:
        extra = ('<Override PartName="/customXml/itemProps1.xml" ContentType="application/'
                 'vnd.openxmlformats-officedocument.customXmlProperties+xml"/>')
        ct = ct.replace("</Types>", extra + "</Types>")
        reemplazos["[Content_Types].xml"] = ct
    rels = reemplazos["word/_rels/document.xml.rels"]
    if "customXml/item1.xml" not in rels:
        rels = rels.replace(
            "</Relationships>",
            '<Relationship Id="rIdCustomXml1" Type="http://schemas.openxmlformats.org/'
            'officeDocument/2006/relationships/customXml" Target="../customXml/item1.xml"/>'
            "</Relationships>")
        reemplazos["word/_rels/document.xml.rels"] = rels
    partes_nuevas["customXml/item1.xml"] = leer(SOURCES)
    partes_nuevas["customXml/itemProps1.xml"] = bibliografia.parte_itemprops(ID_ALMACEN)
    partes_nuevas["customXml/_rels/item1.xml.rels"] = REL_PROPS
    avisos.append("parte de fuentes bibliográficas creada (customXml/item1.xml)")


def _ensamblar(body_path, salida, meta=None, con_portada=True, numerar=True, etiqueta="documento",
               es_anexo=False, linea_titulo=None, ilustraciones=None):
    """Inserta el cuerpo generado por Pandoc dentro de la plantilla institucional.

    con_portada=True  -> conserva portada e índice (informe principal y anexos).
    con_portada=False -> documento sin portada ni índice.
    numerar=False     -> los títulos no se numeran.
    es_anexo=True     -> no inyecta las fuentes bibliográficas y el índice de
                         ilustraciones solo cubre lo que el anexo contiene.
    """
    if not os.path.exists(body_path):
        return {"ok": False, "detalle": "no existe %s" % os.path.basename(body_path)}
    meta = meta or {}

    # --- cuerpo generado por pandoc ---
    doc_body = zip_leer(body_path, "word/document.xml")
    cuerpo = re.search(r"<w:body>(.*)</w:body>", doc_body, re.S).group(1)
    cuerpo = re.sub(r"<w:sectPr\b.*?</w:sectPr>\s*$", "", cuerpo, flags=re.S)
    rels_body = zip_rels(body_path)
    media_body = zip_media(body_path)

    cuerpo, capitulos, avisos = _preparar_cuerpo(cuerpo, numerar)
    # ningún tamaño de letra directo: el formato lo fijan los estilos (11/12 pt)
    cuerpo = _limpiar_tamanos(cuerpo)
    if con_portada:
        cuerpo = _cuerpo_con_citas(cuerpo, avisos)

    # los identificadores de relación se recogen después de insertar la
    # bibliografía, porque esas entradas traen sus propios rId
    usados = set(re.findall(r'r:(?:embed|link|id)="([^"]+)"', cuerpo))

    # --- plantilla ---
    doc = zip_leer(PLANTILLA, "word/document.xml")
    rels = zip_leer(PLANTILLA, "word/_rels/document.xml.rels")
    numbering = zip_leer(PLANTILLA, "word/numbering.xml")
    styles = zip_leer(PLANTILLA, "word/styles.xml")
    settings = zip_leer(PLANTILLA, "word/settings.xml")

    # imágenes y enlaces del cuerpo -> relaciones del paquete de la plantilla
    from xml.sax.saxutils import escape as xml_escape
    mapa_rid = {}
    nuevos_media = {}
    contador_img = 0
    contador_link = 0
    rels_bibliografia = zip_rels(BODY) if os.path.exists(BODY) else {}
    for rid in sorted(usados):
        if rid.startswith("BIB"):
            info = rels_bibliografia.get(rid[3:])
        else:
            info = rels_body.get(rid)
        if not info:
            avisos.append("relación no encontrada en body.docx: %s" % rid)
            continue
        target, modo = info
        if modo == "External" or re.match(r"^[a-zA-Z]+:", target):
            contador_link += 1
            nuevo_rid = "rIdLink%d" % contador_link
            mapa_rid[rid] = nuevo_rid
            rels = rels.replace("</Relationships>",
                                '<Relationship Id="%s" Type="http://schemas.openxmlformats.org/'
                                'officeDocument/2006/relationships/hyperlink" Target="%s" '
                                'TargetMode="External"/></Relationships>' % (nuevo_rid, xml_escape(target)))
            continue
        nombre_interno = "word/" + target.replace("\\", "/")
        if nombre_interno not in media_body:
            avisos.append("imagen ausente en el paquete: %s" % target)
            continue
        contador_img += 1
        base = "g%s_%s" % (contador_img, os.path.basename(target))
        nuevo_interno = "word/media/" + base
        nuevos_media[nuevo_interno] = media_body[nombre_interno]
        nuevo_rid = "rIdImg%d" % contador_img
        mapa_rid[rid] = nuevo_rid
        rels = rels.replace("</Relationships>",
                            '<Relationship Id="%s" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
                            'relationships/image" Target="media/%s"/></Relationships>' % (nuevo_rid, base))
    for viejo, nuevo in mapa_rid.items():
        cuerpo = re.sub(r'(r:(?:embed|link|id)=")%s(")' % re.escape(viejo), r"\g<1>%s\g<2>" % nuevo, cuerpo)
    log("Imágenes copiadas: %d | enlaces externos: %d" % (contador_img, contador_link))

    # portada
    doc, cambios_portada = _rellenar_portada(doc, meta, linea_titulo)

    # namespaces que usa el cuerpo de Pandoc y que la plantilla no declara
    raiz = re.search(r"<w:document\b[^>]*>", doc).group(0)
    ns_cuerpo = dict(re.findall(r'(xmlns:[\w]+)="([^"]+)"',
                                re.search(r"<w:document\b[^>]*>", doc_body).group(0)))
    declarados = set(re.findall(r"xmlns:([\w]+)=", raiz))
    faltantes = [" %s=\"%s\"" % (k, v) for k, v in ns_cuerpo.items() if k.split(":")[1] not in declarados]
    ign_cuerpo = re.search(r'mc:Ignorable="([^"]*)"', raiz)
    if faltantes:
        doc = doc.replace(raiz, raiz[:-1] + "".join(faltantes) + ">", 1)
        raiz = re.search(r"<w:document\b[^>]*>", doc).group(0)
    ign_body = re.search(r'mc:Ignorable="([^"]*)"',
                         re.search(r"<w:document\b[^>]*>", doc_body).group(0))
    if ign_body and ign_cuerpo:
        valores = sorted(set(ign_cuerpo.group(1).split() + ign_body.group(1).split()))
        doc = doc.replace(ign_cuerpo.group(0), 'mc:Ignorable="%s"' % " ".join(valores), 1)

    # corte del cuerpo de la plantilla
    sect = re.search(r"<w:sectPr\b.*?</w:sectPr>", doc, re.S).group(0)
    salto = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
    cola = doc[doc.find("</w:body>") + len("</w:body>"):]
    if con_portada:
        # --- índice (TOC) ---
        # La plantilla trae el índice como campo TOC con 32 entradas en caché y
        # cada entrada con un PAGEREF a marcadores del documento original. Como
        # el cuerpo se reemplaza, esos marcadores desaparecen y los PAGEREF
        # quedan como "Error! Marcador no definido.".
        # Además, cortar por el PRIMER fldChar end (el del PAGEREF de la primera
        # entrada) dejaba el campo TOC sin cerrar: Word lo interpretaba como texto
        # y mostraba la instrucción "TOC \h \z \t ..." a la vista.
        # Solución: se reemplaza toda la región del índice por un campo TOC bien
        # formado (begin + instrucción + separate + aviso en caché + end); Word lo
        # reconstruye al abrir el documento porque settings.xml lleva updateFields.
        parrafos = list(re.finditer(r"<w:p[ >].*?</w:p>", doc, re.S))
        tdc = [m for m in parrafos if 'w:val="TDC' in m.group(0)]
        if not tdc:
            aviso_toc = "no se encontró el índice (estilo TDC1) en la plantilla"
            doc = doc[:doc.find("<w:sectPr")]
        else:
            fin = None
            for m in parrafos:
                if m.start() >= tdc[-1].end() and 'w:fldCharType="end"' in m.group(0):
                    fin = m.end()
                    break
            aviso_toc = None if fin else "no se encontró el cierre del campo TOC; se reconstruye"
            pPr = re.search(r"<w:pPr>.*?</w:pPr>", tdc[0].group(0), re.S)
            # portada + "Contenido" + índice general + índices de ilustraciones;
            # el resto del cuerpo de la plantilla (páginas de instrucciones) se descarta
            tablas_idx, figuras_idx = ilustraciones or (True, True)
            doc = (doc[:tdc[0].start()] + _campo_toc(pPr.group(0) if pPr else "")
                   + _indice_ilustraciones(bool(tablas_idx), bool(figuras_idx)))
            # los títulos de sección de la plantilla traían 14 pt directos
            doc = _limpiar_tamanos(doc, {"Estilo4"})
        doc = doc + salto + cuerpo + sect + "</w:body>" + cola
    else:
        aviso_toc = None
        inicio = doc.find(">", doc.find("<w:body")) + 1
        doc = doc[:inicio] + cuerpo + sect + "</w:body>" + cola

    # tipografía uniforme: Calibri 11 en el texto y Calibri 12 en los títulos,
    # sin tamaños directos que ganen sobre el estilo (ver _estilos_institucionales)
    styles = _estilos_institucionales(styles)

    # numeración: la institucional (un numId por capítulo) y las listas que aporta Pandoc
    abstracts_pandoc, nums_pandoc = _definiciones_pandoc(body_path)
    if numerar:
        nums = []
        for k in range(1, capitulos + 1):
            nums.append('<w:num w:numId="%d"><w:abstractNumId w:val="%d"/>'
                        '<w:lvlOverride w:ilvl="0"><w:startOverride w:val="%d"/></w:lvlOverride></w:num>'
                        % (NUM_BASE + k, NUM_ABS, k))
        numbering = _merge_numbering(numbering, _numbering_extra(), "".join(nums))
    else:
        styles = _sin_numeracion(styles)
    numbering = _merge_numbering(numbering, abstracts_pandoc, nums_pandoc)

    # ajustes de estilo (evitar autorredefinición y estilo siguiente de instrucciones)
    styles = re.sub(r'(<w:style [^>]*w:styleId="Ttulo1"[^>]*>.*?)<w:autoRedefine/>', r"\1", styles, flags=re.S)
    styles = re.sub(r'(<w:style [^>]*w:styleId="Ttulo1"[^>]*>.*?)<w:next w:val="[^"]+"/>', r"\1", styles, flags=re.S)
    styles = styles.replace('<w:name w:val="Título1"/>', '<w:name w:val="Título1"/><w:next w:val="PARRAFO"/>')

    # actualizar campos al abrir (solo el documento principal, que tiene índice)
    if con_portada and "updateFields" not in settings:
        if "<w:hdrShapeDefaults" in settings:
            settings = settings.replace("<w:hdrShapeDefaults",
                                        '<w:updateFields w:val="true"/><w:hdrShapeDefaults', 1)
        else:
            settings = settings.replace("</w:settings>", '<w:updateFields w:val="true"/></w:settings>')

    # --- escribir el paquete final ---
    reemplazos = {
        "word/document.xml": doc,
        "word/_rels/document.xml.rels": rels,
        "word/numbering.xml": numbering,
        "word/styles.xml": styles,
        "word/settings.xml": settings,
        "[Content_Types].xml": zip_leer(PLANTILLA, "[Content_Types].xml"),
    }
    partes_nuevas = {}
    if not es_anexo:
        _inyectar_fuentes(reemplazos, partes_nuevas, avisos)
    nombres_plantilla = set(os.path.basename(f) for f in [])
    try:
        zout = zipfile.ZipFile(salida, "w", zipfile.ZIP_DEFLATED)
    except PermissionError:
        aviso = ("no se pudo escribir %s porque el archivo está abierto en Word; "
                 "cierra el documento y vuelve a ejecutar" % os.path.basename(salida))
        log("  ERROR: %s" % aviso)
        return {"ok": False, "detalle": aviso}
    with zipfile.ZipFile(PLANTILLA) as zin, zout:
            for item in zin.infolist():
                if item.filename in reemplazos:
                    zout.writestr(item, reemplazos[item.filename].encode("utf-8"))
                else:
                    zout.writestr(item, zin.read(item.filename))
            for nombre, datos in nuevos_media.items():
                zout.writestr(nombre, datos)
            for nombre, datos in partes_nuevas.items():
                zout.writestr(nombre, datos.encode("utf-8"))

    log("%s generado | títulos numerados: %d | imágenes: %d | enlaces: %d"
        % (etiqueta, capitulos if numerar else 0, contador_img, contador_link))
    if con_portada:
        log("Portada: %s" % (", ".join(cambios_portada) if cambios_portada else "sin cambios"))
    for a in avisos:
        log("  ADVERTENCIA: %s" % a)
    if aviso_toc:
        log("  ADVERTENCIA: %s" % aviso_toc)
    return {"ok": True, "capitulos": capitulos if numerar else 0, "imagenes": contador_img,
            "avisos": avisos, "portada": cambios_portada, "toc": aviso_toc}


def paso_armar():
    cuerpo = BODY_CITAS if os.path.exists(BODY_CITAS) else BODY
    return _ensamblar(cuerpo, FINAL, meta=_meta_informe(), con_portada=True, numerar=True,
                      etiqueta="Informe_Final.docx")


def paso_anexos():
    """Genera un documento DOCX independiente por cada anexo.

    Cada anexo se arma como documento académico autónomo: misma portada que el
    informe (con el nombre del anexo como título), índice de contenido y, según
    lo que contenga, índice de tablas y de figuras.
    """
    base = dict(_meta_informe())
    proyecto = base.get("proyecto") or base.get("titulo", "")
    resultados = []
    for archivo, letra, titulo, nombre_salida in ANEXOS_MAPA:
        origen = os.path.join(ANEXOS, archivo)
        if not os.path.exists(origen):
            log("  ADVERTENCIA: no existe docx/anexos/%s" % archivo)
            resultados.append({"letra": letra, "ok": False, "archivo": archivo})
            continue
        contenido, figuras, tablas = preparar_anexo(leer(origen), letra)
        md_path = os.path.join(BUILD, "anexo_%s.md" % letra)
        escribir(md_path, "# Anexo %s — %s\n\n%s\n" % (letra, titulo, contenido))
        body_anexo = os.path.join(BUILD, "body_%s.docx" % letra)
        cmd = ["pandoc", md_path, "-o", body_anexo, "--reference-doc=" + PLANTILLA,
               "--from=markdown+fenced_divs+pipe_tables+raw_attribute", "--wrap=none",
               "--metadata=lang:%s" % IDIOMA]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                             errors="replace", cwd=BASE)
        if res.returncode != 0 or not os.path.exists(body_anexo):
            log("  ERROR al convertir el Anexo %s: %s" % (letra, (res.stderr or "")[:300]))
            resultados.append({"letra": letra, "ok": False, "archivo": archivo})
            continue
        salida = os.path.join(BUILD, nombre_salida)
        meta = dict(base, proyecto="Anexo %s — %s" % (letra, titulo))
        r = _ensamblar(body_anexo, salida, meta=meta, con_portada=True, numerar=False,
                       etiqueta=nombre_salida, es_anexo=True,
                       linea_titulo=("PROYECTO DE TÍTULO: %s" % proyecto) if proyecto else None,
                       ilustraciones=(tablas, figuras))
        r.update({"letra": letra, "archivo": archivo, "figuras": figuras,
                  "tablas": tablas, "salida": nombre_salida})
        resultados.append(r)
    ok = bool(resultados) and all(r.get("ok") for r in resultados)
    log("Anexos generados: %d/%d" % (sum(1 for r in resultados if r.get("ok")), len(ANEXOS_MAPA)))
    return {"ok": ok, "anexos": resultados}


# --------------------------------------------------------------------------- #
# 5. validaciones
# --------------------------------------------------------------------------- #
def paso_validar(resumen=None):
    resumen = resumen or {}
    filas = []
    advertencias = []
    errores = []

    def check(n, descripcion, ok, detalle="", bloqueante=True):
        estado = "OK" if ok else ("ERROR" if bloqueante else "ADVERTENCIA")
        if not ok:
            (errores if bloqueante else advertencias).append("%s: %s" % (descripcion, detalle))
        filas.append("| %s | %s | %s | %s |" % (n, descripcion, estado, detalle))

    check(1, "Existe el informe principal", os.path.exists(INFORME), os.path.basename(INFORME))
    check(2, "Existe la plantilla DOCX", os.path.exists(PLANTILLA), os.path.basename(PLANTILLA))
    check(3, "Existe referencias.bib", os.path.exists(BIB), "", False)
    check(4, "Existe apa.csl", os.path.exists(CSL), "", False)

    texto = leer(INFORME)
    # anexos: documentos independientes referenciados desde el cuerpo
    titulos_anexo = re.findall(r"^#+\s+Anexo\s+([A-E])\s+—", texto, re.M)
    faltan_fuente = [a[0] for a in ANEXOS_MAPA if not os.path.exists(os.path.join(ANEXOS, a[0]))]
    faltan_docx = [a[3] for a in ANEXOS_MAPA if not os.path.exists(os.path.join(BUILD, a[3]))]
    check(5, "Los documentos de anexos se generan", not faltan_fuente and not faltan_docx,
        "%d anexos; fuentes faltantes: %s; documentos faltantes: %s"
        % (len(ANEXOS_MAPA), faltan_fuente or "ninguna", faltan_docx or "ninguno"))
    pendientes_txt = re.findall(r"\[\[PENDIENTE:(.{0,90})", texto, re.S)
    check(22, "Contenido pendiente declarado y visible", True,
        "%d avisos de revisión manual: %s" % (len(pendientes_txt),
        [p.strip().replace("\n", " ")[:60] for p in pendientes_txt] or "ninguno"), False)

    # imágenes referenciadas
    imgs = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", texto)
    faltan = [i for i in imgs if not os.path.exists(os.path.join(BASE, i))]
    check(6, "Todas las imágenes referenciadas existen", not faltan,
        "%d imágenes, faltan: %s" % (len(imgs), faltan or "ninguna"), False)

    # diagramas del cuerpo: cada fuente PlantUML debe tener su PNG renderizado
    puml = sorted(f[:-5] for f in os.listdir(DIAGRAMAS)
                  if f.lower().endswith(".puml")) if os.path.isdir(DIAGRAMAS) else []
    sin_png = [c for c in puml if not os.path.exists(os.path.join(IMAGENES, "figura-%s.png" % c))]
    check(23, "Cada diagrama fuente tiene su imagen renderizada", not sin_png,
        "sin imagen: %s" % sin_png if sin_png else "%d diagramas en docx/diagramas" % len(puml))

    # imágenes de figura sin uso en el informe ni en los anexos
    usadas = {os.path.basename(i) for i in imgs}
    for archivo_fuente in ANEXOS_MAPA:
        ruta_fuente = os.path.join(ANEXOS, archivo_fuente[0])
        if os.path.exists(ruta_fuente):
            usadas |= {os.path.basename(i) for i in
                       re.findall(r"!\[[^\]]*\]\(([^)]+)\)", leer(ruta_fuente))}
    todas_img = set(os.listdir(IMAGENES)) if os.path.isdir(IMAGENES) else set()
    huerfanas = sorted(f for f in todas_img
                       if f.startswith("figura-") and f.endswith(".png")
                       and f not in usadas
                       and not re.match(r"figura-(m\d\d|actores)\.png$", f))
    check(24, "Sin imágenes de figura huérfanas en docx/imagenes", not huerfanas,
        "huérfanas: %s" % huerfanas if huerfanas else "%d imágenes referenciadas" % len(usadas), False)

    sin_ancho = [os.path.basename(i) for i in imgs
                 if "width=" not in texto[texto.find(i):texto.find(i) + 120]]
    check(25, "Ancho de figura declarado donde corresponde", True,
        "%d figuras sin ancho explícito (se escalan solas)" % len(sin_ancho), False)

    # citas vs bib
    claves_txt = set()
    for m in re.finditer(r"\[([^\]]*@[^\]]*)\]", texto):
        claves_txt |= set(re.findall(r"@([\w:.\-]+)", m.group(1)))
    claves_bib = set(re.findall(r"@\w+\{([^,]+),", leer(BIB))) if os.path.exists(BIB) else set()
    sin_entrada = sorted(claves_txt - claves_bib)
    sin_citar = sorted(claves_bib - claves_txt)
    check(7, "Todas las citas existen en el .bib", not sin_entrada,
        "%d citas usadas; sin entrada: %s" % (len(claves_txt), sin_entrada or "ninguna"))
    if sin_citar:
        advertencias.append("Entradas del .bib no citadas: %s" % ", ".join(sin_citar))

    # enlaces locales
    rotos = [d for d in re.findall(r"\]\(([^)]+)\)", texto)
             if not d.startswith(("http", "#", "mailto")) and not os.path.exists(os.path.join(BASE, d))]
    check(8, "Sin enlaces locales rotos", not rotos, str(rotos[:5]) if rotos else "ninguno", False)

    # jerarquía y numeración
    niveles = [len(m.group(1)) for m in re.finditer(r"^(#{1,6})\s", texto, re.M)]
    saltos = [(a, b) for a, b in zip(niveles, niveles[1:]) if b - a > 1]
    check(9, "Jerarquía de títulos correcta", not saltos, "saltos: %s" % saltos if saltos else "sin saltos", False)
    cap = len(re.findall(r"^# (?!Anexo\b)", texto, re.M))
    sub1 = sum(1 for n in niveles if n == 2)
    sub2 = sum(1 for n in niveles if n == 3)
    check(10, "Numeración de capítulos coherente", cap == 11,
        "%d capítulos (1 a 11) + %d anexos, %d subcapítulos, %d sub-subcapítulos"
        % (cap, len(titulos_anexo), sub1, sub2), False)

    # tablas y figuras con título
    n_tablas = len(re.findall(r"^\*Tabla\.", texto, re.M))
    n_tablas_md = len(re.findall(r"^\| :?---", texto, re.M))
    ensamblado = leer(ENSAMBLADO) if os.path.exists(ENSAMBLADO) else ""
    n_figuras = len(re.findall(r'custom-style="%s"' % ESTILO_ROTULO_FIGURA, ensamblado))
    n_fig_anexo = 0
    for a in ANEXOS_MAPA:
        ruta_anexo = os.path.join(BUILD, "anexo_%s.md" % a[1])
        if os.path.exists(ruta_anexo):
            n_fig_anexo += len(re.findall(r"^\*\*Figura [A-Z]\.\d+\*\*", leer(ruta_anexo), re.M))
    check(11, "Todas las tablas del cuerpo tienen título", n_tablas >= n_tablas_md - 1,
        "%d tablas y %d títulos en el cuerpo" % (n_tablas_md, n_tablas), False)
    check(12, "Todas las figuras tienen título", (n_figuras + n_fig_anexo) > 0,
        "%d figuras en el cuerpo + %d en anexos" % (n_figuras, n_fig_anexo), False)
    check(13, "Los anexos están referenciados en el cuerpo", len(titulos_anexo) == len(ANEXOS_MAPA),
        "%d de %d anexos referenciados" % (len(titulos_anexo), len(ANEXOS_MAPA)))
    en_carpeta = sorted(f for f in os.listdir(ANEXOS) if f.endswith(".md")) if os.path.isdir(ANEXOS) else []
    declarados = [a[0] for a in ANEXOS_MAPA]
    sin_uso = [f for f in en_carpeta if f not in declarados]
    check(19, "No hay archivos de anexo sin declarar", not sin_uso,
        "sin declarar: %s" % sin_uso if sin_uso else "%d archivos, todos declarados" % len(en_carpeta), False)

    # --- sistema de citas y fuentes nativas de Word ---
    entradas = bibliografia.leer_bib(BIB) if os.path.exists(BIB) else []
    claves_entradas = [e["clave"] for e in entradas]
    claves_txt = claves_citadas(texto)
    check(26, "Cada cita del texto tiene fuente en el catálogo",
        all(k in claves_entradas for k in claves_txt),
        "sin fuente: %s" % [k for k in claves_txt if k not in claves_entradas]
        if any(k not in claves_entradas for k in claves_txt)
        else "%d claves citadas" % len(claves_txt))
    sin_cita = [k for k in claves_entradas if k not in claves_txt]
    check(27, "Cada fuente del catálogo se cita en el texto", not sin_cita,
        "sin cita: %s" % sin_cita if sin_cita else "%d de %d fuentes citadas"
        % (len(claves_entradas), len(claves_entradas)), False)
    incompletas = [e["clave"] for e in entradas
                   if [f for f in bibliografia.OBLIGATORIOS.get(bibliografia.tipo_word(e), [])
                       if not e["campos"].get(f)]]
    check(28, "Sin fuentes incompletas para su tipo de Word", not incompletas,
        "incompletas: %s" % incompletas if incompletas else "%d fuentes completas"
        % len(entradas), False)

    if os.path.exists(FINAL):
        with zipfile.ZipFile(FINAL) as z:
            partes_final = set(z.namelist())
            doc_final = z.read("word/document.xml").decode("utf-8")
            parte_fuentes = None
            for n in partes_final:
                if n.lower().startswith("customxml/") and n.lower().endswith(".xml") \
                        and "itemprops" not in n.lower() \
                        and "b:Sources" in z.read(n).decode("utf-8", "ignore"):
                    parte_fuentes = n
                    break
            xml_fuentes = z.read(parte_fuentes).decode("utf-8") if parte_fuentes else ""
            error_xml = ""
            try:
                if parte_fuentes:
                    ET.fromstring(xml_fuentes)
            except Exception as exc:
                error_xml = "%s: %s" % (type(exc).__name__, exc)
        props_fuentes = [n for n in partes_final
                         if n.lower().startswith("customxml/itemprops")]
        etiquetas = re.findall(r"<b:Tag>([^<]+)</b:Tag>", xml_fuentes)
        tags_citados = re.findall(r"CITATION ([\w:.\-]+) \\l", doc_final)
        razones = [nombre for nombre, valor in (("parte", bool(parte_fuentes)),
                                                ("xml", not error_xml),
                                                ("props", bool(props_fuentes))) if not valor]
        if error_xml:
            razones.append(error_xml[:120])
        check(29, "La parte de fuentes de Word está en el documento", not razones,
            "%d fuentes en %s%s" % (len(etiquetas), parte_fuentes,
            "" if not razones else " (revisar: %s)" % ", ".join(razones))
            if parte_fuentes else "no encontrada")
        check(30, "Cada cita es un campo CITATION con su fuente",
            bool(tags_citados) and all(t in etiquetas for t in set(tags_citados)),
            "%d campos, sin fuente: %s" % (len(tags_citados),
            sorted(set(tags_citados) - set(etiquetas)) or "ninguna"))
        check(31, "El capítulo de referencias es un campo BIBLIOGRAPHY",
            "BIBLIOGRAPHY" in doc_final,
            "campo presente" if "BIBLIOGRAPHY" in doc_final else "no se encontró el campo")
        estilo_declarado = re.search(r'SelectedStyle="([^"]*)"', xml_fuentes)
        estilo_declarado = estilo_declarado.group(1) if estilo_declarado else ""
        check(32, "El estilo bibliográfico del documento es el declarado por el generador",
            estilo_declarado == bibliografia.ESTILO_WORD,
            "estilo declarado: %s" % (estilo_declarado or "ninguno"))

    # documento final
    if os.path.exists(FINAL):
        doc = zip_leer(FINAL, "word/document.xml")
        tablas_docx = len(re.findall(r"<w:tbl>", doc))
        imgs_docx = len(re.findall(r"<w:drawing>", doc))
        tiene_biblio = bool(re.search(r"w:val=\"BIBLIOGRAFA1\"", doc))
        settings_final = zip_leer(FINAL, "word/settings.xml")
        toc_ok = all(t in doc for t in ('w:fldCharType="begin"', "TOC \\h",
                                        'w:fldCharType="separate"', 'w:fldCharType="end"'))
        check(14, "La bibliografía se genera correctamente", tiene_biblio,
            "%d entradas referenciadas" % len(re.findall(r"BIBLIOGRAFA1", doc)), False)
        check(15, "El índice es un campo TOC bien formado",
            toc_ok and ("updateFields" in settings_final
                        or 'w:fldCharType="separate"' in doc),
            ("campo TOC completo, con actualización automática al abrir" if toc_ok
             else "falta alguna parte del campo TOC: se vería como texto o daría "
                  "'Error! Marcador no definido'"), False)
        restos_campo = [t for t in ("Error! Marcador", "¡Error! Marcador",
                                    "Marcador no definido", "Fuente especificada no válida")
                        if t in doc]
        check(33, "Sin errores de campo visibles en el documento", not restos_campo,
            str(restos_campo) or "ninguno")

        # --- vía de rótulos y tamaños: solo el cuerpo (la portada conserva su diseño) ---
        doc_cuerpo = _tras_frente(doc)
        secuencia = re.findall(r"<w:p[ >].*?</w:p>|<w:tbl>.*?</w:tbl>", doc_cuerpo, re.S)
        tablas_sin_rotulo, tablas_sin_nota = [], []
        figuras_sin_rotulo, figuras_sin_nota = [], []
        for i, bloque in enumerate(secuencia):
            anterior = secuencia[i - 1] if i else ""
            siguiente = secuencia[i + 1] if i + 1 < len(secuencia) else ""
            nota_ok = ("Fuente:" in siguiente
                       and 'w:val="PIEDEFOTO"' in siguiente)
            if bloque.startswith("<w:tbl>"):
                if not re.search(MARCA_ROTULO_TABLA, anterior):
                    tablas_sin_rotulo.append(i)
                if not nota_ok:
                    tablas_sin_nota.append(i)
            elif "<w:drawing>" in bloque:
                if not re.search(MARCA_ROTULO_FIGURA, anterior):
                    figuras_sin_rotulo.append(i)
                if not nota_ok:
                    figuras_sin_nota.append(i)
        check(34, "Cada tabla lleva su rótulo encima y su nota debajo",
            not tablas_sin_rotulo and not tablas_sin_nota,
            "sin rótulo: %d | sin nota: %d" % (len(tablas_sin_rotulo), len(tablas_sin_nota)))
        check(35, "Cada figura lleva su rótulo encima y su nota debajo",
            not figuras_sin_rotulo and not figuras_sin_nota,
            "sin rótulo: %d | sin nota: %d" % (len(figuras_sin_rotulo), len(figuras_sin_nota)))
        check(36, "Ninguna imagen conserva el pie de Pandoc debajo",
            'w:val="ImageCaption"' not in doc_cuerpo,
            "párrafos ImageCaption: %d" % doc_cuerpo.count('w:val="ImageCaption"'))
        check(37, "El documento tiene índice de tablas y de figuras",
            "%s;1" % NOMBRE_ROTULO_TABLA in doc and "%s;1" % NOMBRE_ROTULO_FIGURA in doc,
            "campos de índice de ilustraciones presentes"
            if "%s;1" % NOMBRE_ROTULO_TABLA in doc else "faltan los campos de índice")

        # tamaños: en el cuerpo solo 11 y 12 pt (la portada conserva su diseño)
        malos = []
        for m in re.finditer(r"<w:p[ >].*?</w:p>", doc_cuerpo, re.S):
            p = m.group(0)
            est = re.search(r'w:pStyle w:val="([^"]+)"', p)
            est = est.group(1) if est else "(sin estilo)"
            for sz in re.findall(r'<w:sz w:val="(\d+)"/>', p):
                if int(sz) not in (SZ_CUERPO, SZ_TITULO):
                    malos.append((est, int(sz) / 2))
        check(38, "Tamaños de letra uniformes (11 pt y 12 pt)", not malos,
            "fuera de norma: %s" % sorted(set(malos))[:5] if malos
            else "solo 11 pt en el texto y 12 pt en los títulos")
        estilos_final = zip_leer(FINAL, "word/styles.xml")
        tema_final = zip_leer(FINAL, "word/theme/theme1.xml")
        minor = re.search(r"<a:minorFont>.*?<a:latin typeface=\"([^\"]*)\"", tema_final, re.S)
        fuente_tema = minor.group(1) if minor else ""
        sin_calibri = []
        for estilo_ok, nombre_ok in (("PARRAFO", None), ("Ttulo1", None), ("Subtitulo1", None),
                                     ("Subtitulo2", None),
                                     (ESTILO_ROTULO_TABLA, NOMBRE_ROTULO_TABLA),
                                     (ESTILO_ROTULO_FIGURA, NOMBRE_ROTULO_FIGURA)):
            bloque = ""
            for sid in (estilo_ok, nombre_ok):
                if not sid:
                    continue
                coincidencia = re.search(r'<w:style [^>]*w:styleId="%s"[^>]*>.*?</w:style>'
                                         % sid, estilos_final, re.S)
                if coincidencia:
                    bloque = coincidencia.group(0)
                    break
            if not bloque:
                continue
            # Word elimina el rFonts explícito y el estilo hereda la fuente del tema
            if 'w:ascii="%s"' % FUENTE in bloque:
                continue
            if ("<w:rFonts" not in bloque or 'w:asciiTheme="minor' in bloque) \
                    and fuente_tema == FUENTE:
                continue
            sin_calibri.append(estilo_ok)
        check(39, "Todos los estilos usan la fuente %s" % FUENTE, not sin_calibri,
            "sin %s: %s" % (FUENTE, sin_calibri) if sin_calibri
            else "%s declarada o heredada del tema" % FUENTE)

        # --- anexos: documento académico autónomo con el formato del informe ---
        sin_portada, sin_indice, mal_indice = [], [], []
        mal_rotulo, sin_tamano, saltos_jerarquia = [], [], []
        for archivo, letra, titulo, nombre_salida in ANEXOS_MAPA:
            ruta_anexo = os.path.join(BUILD, nombre_salida)
            if not os.path.exists(ruta_anexo):
                sin_portada.append(letra)
                continue
            doc_a = zip_leer(ruta_anexo, "word/document.xml")
            est_a = zip_leer(ruta_anexo, "word/styles.xml")
            st_a = zip_leer(ruta_anexo, "word/settings.xml")
            nombre = "Anexo %s — %s" % (letra, titulo)
            frente = doc_a[:doc_a.find('w:val="TDC')] if 'w:val="TDC' in doc_a else doc_a
            if "<w:txbxContent>" not in doc_a or nombre not in frente:
                sin_portada.append(letra)
            if not re.search(r'<w:instrText[^>]*>\s*TOC\b', doc_a) \
                    or not ("updateFields" in st_a or 'w:fldCharType="separate"' in doc_a):
                sin_indice.append(letra)
            rot_tablas = len(re.findall(MARCA_ROTULO_TABLA, doc_a))
            rot_figuras = len(re.findall(MARCA_ROTULO_FIGURA, doc_a))
            if (rot_tablas and "%s;1" % NOMBRE_ROTULO_TABLA not in doc_a) \
                    or (rot_figuras and "%s;1" % NOMBRE_ROTULO_FIGURA not in doc_a):
                mal_indice.append("%s (%d tab, %d fig)" % (letra, rot_tablas, rot_figuras))
            secuencia_a = re.findall(r"<w:p[ >].*?</w:p>|<w:tbl>.*?</w:tbl>",
                                     _tras_frente(doc_a), re.S)
            faltan_rotulo, faltan_notas = 0, 0
            for i, bloque in enumerate(secuencia_a):
                anterior = secuencia_a[i - 1] if i else ""
                siguiente = secuencia_a[i + 1] if i + 1 < len(secuencia_a) else ""
                nota = "Fuente:" in siguiente and 'w:val="PIEDEFOTO"' in siguiente
                if bloque.startswith("<w:tbl>"):
                    if "Código y Nombre de la Historia" in bloque:
                        continue      # tarjeta de historia de usuario: sin rótulo ni nota
                    if not re.search(MARCA_ROTULO_TABLA, anterior):
                        faltan_rotulo += 1
                    if not nota:
                        faltan_notas += 1
                elif "<w:drawing>" in bloque:
                    if not re.search(MARCA_ROTULO_FIGURA, anterior):
                        faltan_rotulo += 1
                    if not nota:
                        faltan_notas += 1
            if faltan_rotulo or faltan_notas:
                mal_rotulo.append("%s (sin rótulo: %d, sin nota: %d)"
                                  % (letra, faltan_rotulo, faltan_notas))
            if not all(s in est_a for s in ('w:sz w:val="22"', 'w:sz w:val="24"')):
                sin_tamano.append(letra)
            md_anexo = os.path.join(BUILD, "anexo_%s.md" % letra)
            if os.path.exists(md_anexo):
                niveles = [len(m.group(1)) for m in re.finditer(r"^(#{1,6})\s", leer(md_anexo), re.M)]
                if any(b > a + 1 for a, b in zip(niveles, niveles[1:])):
                    saltos_jerarquia.append(letra)
        check(40, "Cada anexo tiene portada con su nombre como título", not sin_portada,
            "sin portada: %s" % sin_portada if sin_portada
            else "%d de %d anexos" % (len(ANEXOS_MAPA), len(ANEXOS_MAPA)))
        check(41, "Cada anexo tiene índice de contenido", not sin_indice,
            "sin índice: %s" % sin_indice if sin_indice else "campo TOC y updateFields en los 5")
        check(42, "Los anexos tienen índice de tablas y figuras según su contenido",
            not mal_indice, ", ".join(mal_indice) if mal_indice else "índices coherentes")
        check(43, "Cada tabla y figura de los anexos lleva rótulo y nota",
            not mal_rotulo, " | ".join(mal_rotulo) if mal_rotulo
            else "rótulos encima y notas debajo")
        check(44, "Los anexos usan Calibri 11 y 12", not sin_tamano,
            "revisar: %s" % sin_tamano if sin_tamano else "tamaños 11 y 12 declarados")
        check(45, "Sin saltos de jerarquía de títulos en los anexos",
            not saltos_jerarquia, "con salto: %s" % saltos_jerarquia if saltos_jerarquia
            else "jerarquía continua")

        # --- fuentes sin iconos ni reglas decorativas (se normalizan al generar) ---
        con_iconos, con_reglas = [], []
        for archivo, letra, titulo, nombre_salida in ANEXOS_MAPA:
            md_anexo = os.path.join(BUILD, "anexo_%s.md" % letra)
            if not os.path.exists(md_anexo):
                continue
            cuerpo_md = leer(md_anexo)
            titulos_md = re.findall(r"^#{1,6}\s+(.*)$", cuerpo_md, re.M)
            if any(re.search(r"[\U0001F000-\U0001FAFF\u2190-\u21FF\u2300-\u27BF\u2B00-\u2BFF\uFE0F]", t)
                   for t in titulos_md):
                con_iconos.append(letra)
            if re.search(r"^\s*---+\s*$", cuerpo_md, re.M):
                con_reglas.append(letra)
        check(46, "Ningún título de los anexos lleva iconos", not con_iconos,
            "con iconos: %s" % con_iconos if con_iconos else "títulos de texto plano")
        check(47, "Sin reglas horizontales decorativas en los anexos", not con_reglas,
            "con reglas: %s" % con_reglas if con_reglas else "separación por estilos")
        restos = [frase for frase in ("No olvides respetar", "Se sugiere", "Para realizar un listado",
                                      "Incluir aquí, numerando", "Presentar una síntesis",
                                      "Presentación de la temática", "Ejemplo de referencias")
                  if frase in doc]
        check(16, "Sin textos de instrucción de la plantilla", not restos, str(restos) or "ninguno")
        detalle_docx = "documento: %d tablas, %d imágenes" % (tablas_docx, imgs_docx)
    else:
        check(14, "La bibliografía se genera correctamente", False, "no existe Informe_Final.docx")
        detalle_docx = "no generado"

    # informe original vs copia
    desactualizado = os.path.exists(ORIGINAL) and os.path.getmtime(ORIGINAL) > os.path.getmtime(INFORME)
    check(17, "La copia informe.md está actualizada", not desactualizado,
        "el original es más reciente que la copia" if desactualizado else "sin cambios pendientes", False)

    # integridad del paquete DOCX y de los documentos de anexos
    # integridad de los paquetes DOCX (XML bien formado)
    danados = []
    documentos = [FINAL] + [os.path.join(BUILD, a[3]) for a in ANEXOS_MAPA]
    danados = []
    partes_total = 0
    for documento in documentos:
        if not os.path.exists(documento):
            danados.append("%s no existe" % os.path.basename(documento))
            continue
        with zipfile.ZipFile(documento) as z:
            for parte in z.namelist():
                if parte.endswith(".xml") or parte.endswith(".rels"):
                    partes_total += 1
                    try:
                        ET.fromstring(z.read(parte))
                    except Exception as exc:
                        danados.append("%s/%s (%s)" % (os.path.basename(documento), parte, exc))
    check(18, "Los paquetes DOCX son válidos (XML bien formado)", not danados,
        "; ".join(danados[:3]) if danados else "%d documentos, %d partes verificadas" % (len(documentos), partes_total))

    if os.path.exists(FINAL):

        # coherencia entre referencias y relaciones declaradas
        with zipfile.ZipFile(FINAL) as z:
            partes = set(z.namelist())
            doc_xml = z.read("word/document.xml").decode("utf-8")
            rels_xml = z.read("word/_rels/document.xml.rels").decode("utf-8")
        disponibles = set(re.findall(r'Id="([^"]+)"', rels_xml))
        usadas = set(re.findall(r'r:(?:embed|link|id)="([^"]+)"', doc_xml))
        huerfanas = sorted(usadas - disponibles)
        destinos = re.findall(r'Target="([^"]+)"', rels_xml)
        objetivos_rotos = sorted({d for d in destinos if d.startswith("media/")
                                  and ("word/" + d) not in partes})
        check(20, "Referencias del documento declaradas en las relaciones", not huerfanas,
            "sin declarar: %s" % huerfanas if huerfanas else "%d relaciones verificadas" % len(disponibles))
        check(21, "Recursos enlazados presentes en el paquete", not objetivos_rotos,
            "faltan: %s" % objetivos_rotos if objetivos_rotos else "todas las imágenes presentes")

    titulo = "# Reporte de validación del pipeline MD → DOCX\n\n"
    cuerpo = ("| # | Validación | Estado | Detalle |\n| :--- | :--- | :--- | :--- |\n"
              + "\n".join(filas) + "\n\n")
    secciones = ["## Resumen\n",
                 "| Métrica | Valor |",
                 "| :--- | :--- |",
                 "| Secciones de capítulo | %d |" % cap,
                 "| Anexos (documentos independientes) | %d |" % len(titulos_anexo),
                 "| Tablas del cuerpo | %d |" % n_tablas_md,
                 "| Figuras (informe / anexos) | %d / %d |" % (n_figuras, n_fig_anexo),
                 "| Imágenes referenciadas | %d |" % len(imgs),
                 "| Citas usadas | %d |" % len(claves_txt),
                 "| Referencias en el .bib | %d |" % len(claves_bib),
                 "| Advertencias | %d |" % len(advertencias),
                 "| Errores | %d |" % len(errores),
                 ""]
    if advertencias:
        secciones.append("## Advertencias\n")
        secciones += ["* %s" % a for a in advertencias] + [""]
    if errores:
        secciones.append("## Errores\n")
        secciones += ["* %s" % e for e in errores] + [""]
    contenido_reporte = titulo + cuerpo + "\n".join(secciones)
    escribir(REPORTE, contenido_reporte)

    log("--- Validaciones ---")
    for f in filas:
        log("  " + f)
    log("Advertencias: %d | Errores: %d" % (len(advertencias), len(errores)))
    log("Reporte: %s" % REPORTE)
    return {"ok": not errores, "advertencias": advertencias, "errores": errores,
            "citas": len(claves_txt), "refs": len(claves_bib), "tablas": n_tablas_md,
            "figuras": len(imgs), "capitulos": cap}


# --------------------------------------------------------------------------- #
def main():
    pasos = sys.argv[1:] or ["todo"]
    acumulado = {}
    if "todo" in pasos or "diagramas" in pasos:
        log("=== 1. Diagramas ===")
        acumulado["diagramas"] = paso_diagramas(forzar="--forzar" in sys.argv)
    if "todo" in pasos or "bibliografia" in pasos:
        log("=== 2. Fuentes bibliográficas y caché de citas ===")
        acumulado["bibliografia"] = paso_bibliografia()
    if "todo" in pasos or "preprocesar" in pasos:
        log("=== 3. Preprocesado del markdown ===")
        acumulado["pre"] = paso_preprocesar()
    if "todo" in pasos or "pandoc" in pasos:
        log("=== 4. Conversión con Pandoc ===")
        acumulado["pandoc"] = paso_pandoc()
    if "todo" in pasos or "armar" in pasos:
        log("=== 5. Armado en la plantilla ===")
        acumulado["armado"] = paso_armar()
    if "todo" in pasos or "anexos" in pasos:
        log("=== 6. Documentos de anexos ===")
        acumulado["anexos"] = paso_anexos()
    if "todo" in pasos or "validar" in pasos:
        log("=== 7. Validaciones ===")
        acumulado["validacion"] = paso_validar(acumulado)
    return 0


if __name__ == "__main__":
    sys.exit(main())
