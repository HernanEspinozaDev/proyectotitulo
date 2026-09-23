"""Validaciones de fuentes y OOXML, con resultados utilizables desde CLI y tests."""
import hashlib
import json
import posixpath
import re
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter

from . import bibliografia
from .configuracion import ErrorInforme, RAIZ
from .ensamblado import documentos, imagenes, leer, resolver_imagen, reunir, sin_codigo

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
B = "{http://schemas.openxmlformats.org/officeDocument/2006/bibliography}"
CITAS = r"\[[^\[\]]*@[^\[\]]*\]"


def claves(texto):
    return re.findall(r"@([\w:.-]+)", " ".join(re.findall(CITAS, sin_codigo(texto))))


def comprobar_fuentes(cfg, final=False):
    errores, avisos = [], []
    try:
        docs = documentos(cfg)
        entradas = bibliografia.leer_bib(str(cfg.entrada(cfg.datos["bibliografia"])))
    except (ErrorInforme, OSError, ValueError) as exc:
        return [str(exc)], []
    ids = [e["clave"] for e in entradas]
    errores += [f"Clave bibliográfica no soportada (contiene __): {k}" for k in ids if "__" in k]
    errores += [f"Clave bibliográfica duplicada: {k}" for k, n in Counter(ids).items() if n > 1]
    usadas = set()
    # Las etiquetas se resuelven por documento: secciones juntas; anexos independientes.
    grupos = [("informe", reunir(cfg))] + [(a["archivo"], leer(cfg.entrada(a["archivo"]))) for a in cfg.anexos]
    for nombre, texto in grupos:
        texto = sin_codigo(texto)
        usadas.update(claves(texto))
        etiquetas = re.findall(r"<!--#(tab|fig):([\w-]+)-->", texto)
        errores += [f"{nombre}: identificador duplicado {t}:{k}" for (t, k), n in Counter(etiquetas).items() if n > 1]
        for tipo, clave in re.findall(r"\{\{(Tabla|Figura):([\w-]+)\}\}", texto, re.I):
            if ("tab" if tipo.lower() == "tabla" else "fig", clave) not in etiquetas:
                errores.append(f"{nombre}: referencia sin destino {tipo}:{clave}")
        # El formato nativo heredado soporta citas parentéticas por claves, no localizadores.
        for cita in re.findall(CITAS, texto):
            if not re.fullmatch(r"\[\s*@[\w:.-]+(?:\s*;\s*@[\w:.-]+)*\s*\]", cita):
                errores.append(f"{nombre}: cita no soportada sin pérdida de información: {cita}")
        resto = re.sub(CITAS, "", texto)
        if re.search(r"(?<![\w/])@[\w:.-]+", resto):
            errores.append(f"{nombre}: usa citas parentéticas [@clave]; las citas narrativas no están implementadas.")
        if "[[PENDIENTE" in texto:
            (errores if final else avisos).append(f"{nombre}: contiene pendientes de redacción.")
    errores += [f"Cita sin fuente: {k}" for k in sorted(usadas - set(ids))]
    seleccionadas = [e for e in entradas if e["clave"] in usadas]
    _, auditoria = bibliografia.auditar(seleccionadas, sorted(usadas))
    for campo in ("incompletas", "pendientes"):
        if auditoria[campo]:
            (errores if final else avisos).append(f"Bibliografía citada: {auditoria[campo]} fuentes {campo}.")
    from .diagramas import nombres_generados
    try:
        generadas = {n + ".png" for n in nombres_generados(cfg)}
    except ErrorInforme as exc:
        errores.append(str(exc))
        generadas = set()
    for origen, texto in docs:
        for m in imagenes(sin_codigo(texto)):
            try:
                ruta = resolver_imagen(cfg, origen, m.group(1))
                if not ruta.is_file() and not (ruta.parent.name == "imagenes" and ruta.name in generadas):
                    errores.append(f"Imagen inexistente en {origen.name}: {m.group(1)}")
            except ErrorInforme as exc:
                errores.append(str(exc))
    if final:
        for campo in ("titulo", "proyecto", "asignatura", "seccion", "academico", "integrantes", "fecha"):
            valor = cfg.datos["metadatos"].get(campo, "")
            if not valor.strip() or "PENDIENTE" in valor.upper():
                errores.append(f"Metadato de entrega pendiente: {campo}")
        pendientes = cfg.raiz / "pendientes.md"
        if pendientes.exists() and re.search(r"^\s*- \[ \]", leer(pendientes), re.M):
            errores.append("pendientes.md contiene tareas sin cerrar.")
    return errores, avisos


def huella(cfg):
    rutas = {cfg.archivo, cfg.entrada(cfg.datos["bibliografia"]), RAIZ / "recursos/apa.csl"}
    rutas.update(p for p, _ in documentos(cfg))
    for campo in ("plantilla", "perfil"):
        if cfg.datos[campo]:
            rutas.add((cfg.recurso if cfg.datos.get("compatibilidad_es1") and campo == "perfil" else cfg.entrada)(cfg.datos[campo]))
    for carpeta in ("imagenes", "diagramas", "docx/imagenes", "docx/diagramas"):
        if (cfg.raiz / carpeta).is_dir():
            rutas.update(p for p in (cfg.raiz / carpeta).rglob("*") if p.is_file())
    rutas.update((RAIZ / "herramientas").glob("*.py"))
    h = hashlib.sha256()
    for p in sorted(rutas):
        h.update(str(p.relative_to(RAIZ)).encode())
        h.update(p.read_bytes())
    return h.hexdigest()


def inspeccionar_docx(ruta):
    errores = []
    try:
        with zipfile.ZipFile(ruta) as z:
            nombres = z.namelist()
            if len(nombres) != len(set(nombres)):
                errores.append("Partes ZIP duplicadas")
            for n in nombres:
                if n.endswith((".xml", ".rels")):
                    ET.fromstring(z.read(n))
                if n.endswith(".rels"):
                    base = posixpath.dirname(posixpath.dirname(n))
                    for r in ET.fromstring(z.read(n)):
                        if r.get("TargetMode") == "External":
                            continue
                        objetivo = r.get("Target", "").replace("\\", "/").split("#")[0]
                        destino = objetivo.lstrip("/") if objetivo.startswith("/") else posixpath.normpath(posixpath.join(base, objetivo))
                        if destino not in nombres:
                            errores.append(f"Recurso OOXML ausente: {destino}")
            doc = ET.fromstring(z.read("word/document.xml"))
            texto = " ".join(t.text or "" for t in doc.iter(W + "t"))
            for marca in ("CITA__", "BIBLIOGRAFIA__WORD", "FUENTE__PEND__", "{{Tabla:", "{{Figura:"):
                if marca in texto:
                    errores.append(f"Marcador sin resolver: {marca}")
            instrucciones = [t.text or "" for t in doc.iter(W + "instrText")]
            titulos = []
            for parrafo in doc.iter(W + "p"):
                estilo = parrafo.find("./" + W + "pPr/" + W + "pStyle")
                sid = estilo.get(W + "val", "") if estilo is not None else ""
                if sid in {"Ttulo1", "Subtitulo1", "Subtitulo2", "Prrafodelista"}:
                    valor = "".join(t.text or "" for t in parrafo.iter(W + "t"))
                    titulos.append([sid, valor])
            fuentes = []
            for n in nombres:
                if n.startswith("customXml/") and n.endswith(".xml"):
                    fuentes += [t.text for t in ET.fromstring(z.read(n)).iter(B + "Tag")]
            metricas = {"parrafos": len(list(doc.iter(W + "p"))), "tablas": len(list(doc.iter(W + "tbl"))),
                        "imagenes": len([n for n in nombres if n.startswith("word/media/")]),
                        "citas": sum("CITATION " in i for i in instrucciones),
                        "bibliografias": sum("BIBLIOGRAPHY " in i for i in instrucciones),
                        "indices": sum("TOC " in i for i in instrucciones), "fuentes": sorted(fuentes),
                        "titulos": titulos,
                        "capitulos": sum(s == "Ttulo1" and not t.startswith("Anexo ") for s, t in titulos)}
            # Relaciones usadas por el cuerpo deben estar declaradas.
            rels = ET.fromstring(z.read("word/_rels/document.xml.rels"))
            declaradas = {r.get("Id") for r in rels}
            rn = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
            for elemento in doc.iter():
                for attr in (rn + "id", rn + "embed", rn + "link"):
                    if attr in elemento.attrib and elemento.attrib[attr] not in declaradas:
                        errores.append(f"Relación sin declarar: {elemento.attrib[attr]}")
            tipos = [t.get(W + "fldCharType") for t in doc.iter(W + "fldChar")]
            if tipos.count("begin") != tipos.count("end"):
                errores.append("Campos Word sin cierre equilibrado")
            return errores, metricas
    except (OSError, zipfile.BadZipFile, ET.ParseError, KeyError) as exc:
        return [f"DOCX inválido {ruta.name}: {exc}"], {}


def validar(cfg, final=False):
    errores, avisos = comprobar_fuentes(cfg, final)
    metricas = {}
    manifiesto = cfg.salida("generacion.json")
    if not manifiesto.exists():
        errores.append("No hay una generación Word verificada; ejecuta generar.")
    else:
        estado = json.loads(leer(manifiesto))
        if not estado.get("completa"):
            errores.append("La última generación quedó incompleta.")
        try:
            if estado.get("huella") != huella(cfg):
                errores.append("Los documentos están desactualizados respecto de las fuentes o del motor.")
        except OSError as exc:
            errores.append(str(exc))
    for nombre in ["Informe_Final.docx"] + [a["salida"] for a in cfg.anexos]:
        fallos, datos = inspeccionar_docx(cfg.salida(nombre))
        errores += [f"{nombre}: {e}" for e in fallos]
        metricas[nombre] = datos
    guardar_reporte(cfg, errores, avisos, metricas)
    return errores, avisos


def guardar_reporte(cfg, errores, avisos, metricas=None):
    cfg.build.mkdir(parents=True, exist_ok=True)
    resultado = {"errores": errores, "advertencias": avisos, "documentos": metricas or {}}
    cfg.salida("validacion.json").write_text(json.dumps(resultado, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lineas = ["# Validación del informe", "", f"Errores: {len(errores)} | Advertencias: {len(avisos)}", "",
              "## Errores", ""] + [f"- {e}" for e in errores or ["Ninguno."]]
    lineas += ["", "## Advertencias", ""] + [f"- {a}" for a in avisos or ["Ninguna."]]
    cfg.salida("reporte_validacion.md").write_text("\n".join(lineas) + "\n", encoding="utf-8")
