"""Conversión por documento y adaptación institucional con perfiles explícitos."""
import hashlib
import json
import re
import shutil
import subprocess
import zipfile
from pathlib import Path

from . import bibliografia, motor_word as motor
from .configuracion import ErrorInforme, RAIZ, leer_json
from .ensamblado import leer, reunir, resolver_imagen
from .validacion import claves, comprobar_fuentes, guardar_reporte, huella, inspeccionar_docx, validar


def perfil(cfg, permitir_borrador=False):
    """Verifica estructura y firma; solo la muestra aislada admite un perfil sin aprobar."""
    if not cfg.datos["plantilla"]:
        raise ErrorInforme("Plantilla institucional pendiente: incorpora y configura el DOCX. Puedes seguir redactando y ensamblando Markdown.")
    if not cfg.datos["perfil"]:
        raise ErrorInforme("Perfil institucional pendiente: adapta el perfil al DOCX incorporado. Puedes seguir redactando y ensamblando Markdown.")
    ruta = (cfg.recurso if cfg.datos.get("compatibilidad_es1") else cfg.entrada)(cfg.datos["perfil"])
    p = leer_json(ruta)
    plantilla = cfg.entrada(cfg.datos["plantilla"])
    if not plantilla.is_file():
        raise ErrorInforme(f"No existe la plantilla: {plantilla}")
    if p.get("adaptador") != "inacap_es1" or (not p.get("aprobado") and not permitir_borrador):
        raise ErrorInforme("Perfil pendiente de adaptación y revisión. El adaptador disponible es inacap_es1.")
    if p.get("insercion") != "reemplazar_desde_indice_tdc":
        raise ErrorInforme("Regla de inserción no soportada por este adaptador.")
    if p.get("sha256_plantilla") != hashlib.sha256(plantilla.read_bytes()).hexdigest():
        raise ErrorInforme("La plantilla no coincide con la revisada en el perfil. Inspecciona portada, estilos e índice antes de adaptar el perfil.")
    try:
        with zipfile.ZipFile(plantilla) as z:
            estilos = z.read("word/styles.xml").decode("utf-8")
            doc = z.read("word/document.xml").decode("utf-8")
            for parte in ("word/numbering.xml", "word/settings.xml", "word/_rels/document.xml.rels"):
                z.read(parte)
            faltan = [s for s in p["estilos_requeridos"] if f'w:styleId="{s}"' not in estilos]
            if faltan or 'w:val="TDC' not in doc:
                raise ErrorInforme(f"Plantilla incompatible con el perfil: estilos faltantes {faltan} o índice TDC ausente.")
    except (zipfile.BadZipFile, KeyError) as exc:
        raise ErrorInforme(f"Plantilla o perfil incompleto: {exc}") from exc
    return plantilla, p


def ejecutar_pandoc(argumentos, cwd):
    res = subprocess.run(["pandoc", *argumentos], cwd=cwd, capture_output=True,
                         text=True, encoding="utf-8", errors="replace")
    if res.returncode:
        raise ErrorInforme(f"Pandoc falló: {res.stderr[:1200]}")
    if res.stderr.strip():
        print(res.stderr.strip())


def preparar_imagenes(cfg, texto, origen):
    def reemplazar(m):
        original = resolver_imagen(cfg, origen, m.group(2))
        generado = cfg.salida("imagenes") / original.name
        if original.parent.name == "imagenes" and generado.is_file():
            destino = generado
        elif original.is_file():
            destino = cfg.salida("assets") / (hashlib.sha256(str(original).encode()).hexdigest()[:12] + original.suffix)
            destino.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(original, destino)
        else:
            raise ErrorInforme(f"No se generó o no existe la imagen: {m.group(2)}")
        return f"![{m.group(1)}]({destino.as_posix()})"
    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", reemplazar, texto)


def configurar_motor(cfg, plantilla, p, carpeta):
    # El CLI procesa documentos secuencialmente. Cada documento restablece todo el estado.
    motor.PERFIL = p
    motor.MAPA_ESTILOS = p["mapa_estilos"]
    motor.NIVEL_TITULO = p["niveles_titulo"]
    motor.FUENTE, motor.SZ_CUERPO, motor.SZ_TITULO = p["fuente"], p["tamano_cuerpo"], p["tamano_titulo"]
    motor.TOC_INSTRUCCION = p["toc"]
    motor.BASE = str(cfg.build)
    motor.BUILD = str(carpeta)
    motor.PLANTILLA = str(plantilla)
    motor.CSL = str(RAIZ / "recursos/apa.csl")
    motor.IDIOMA = "es-CL"
    motor.BIB = str(cfg.entrada(cfg.datos["bibliografia"]))
    motor.CACHE_CITAS = {}
    for variable, archivo in {"INFORME":"fuente.md", "ENSAMBLADO":"preprocesado.md",
        "ENSAMBLADO_CITAS":"campos.md", "BODY":"body.docx", "BODY_CITAS":"body_campos.docx",
        "SOURCES":"sources.xml", "AUDITORIA_CITAS":"auditoria_citas.md"}.items():
        setattr(motor, variable, str(carpeta / archivo))


def titulo_portada_anexo(p, proyecto, anexo):
    """Conserva títulos institucionales multipartes cuando el perfil lo exige."""
    if not anexo or p.get("conservar_titulo_plantilla_en_anexos", False):
        return None
    return "PROYECTO DE TÍTULO: " + proyecto


def generar_documento(cfg, plantilla, p, texto, nombre, anexo=None):
    carpeta = cfg.salida("intermedios") / (anexo["letra"] if anexo else "informe")
    carpeta.mkdir(parents=True, exist_ok=True)
    configurar_motor(cfg, plantilla, p, carpeta)
    motor.TRANSFORMACION = anexo["transformacion"] if anexo else "general"
    if anexo and (anexo["transformacion"] != "general" or cfg.datos.get("compatibilidad_es1")):
        texto, figuras, tablas = motor.preparar_anexo(texto, anexo["letra"])
        texto = f"# Anexo {anexo['letra']} — {anexo['titulo']}\n\n{texto}\n"
    elif anexo:
        from .ensamblado import sin_cabecera
        texto = sin_cabecera(texto).strip()
        if re.match(r"^#\s+", texto):
            texto = texto.split("\n", 1)[1] if "\n" in texto else ""
        texto = f"# Anexo {anexo['letra']} — {anexo['titulo']}\n\n{texto}\n"
    if anexo and claves(texto) and "{#refs}" not in texto:
        texto += "\n## Referencias\n\n::: {#refs}\n:::\n"
    texto = preparar_imagenes(cfg, texto, cfg.raiz)
    Path(motor.INFORME).write_text(texto, encoding="utf-8")
    entradas = bibliografia.leer_bib(motor.BIB)
    citadas = list(dict.fromkeys(claves(texto)))
    entradas = [e for e in entradas if e["clave"] in citadas]
    Path(motor.SOURCES).write_text(bibliografia.parte_sources(entradas), encoding="utf-8")
    motor.CACHE_CITAS = motor.probar_citas(citadas)
    if set(citadas) - motor.CACHE_CITAS.keys():
        raise ErrorInforme("No se pudo generar la caché APA 7 de todas las citas.")
    auditoria, _ = bibliografia.auditar(entradas, citadas, motor.CACHE_CITAS, len(claves(texto)))
    Path(motor.AUDITORIA_CITAS).write_text(auditoria, encoding="utf-8")
    resultado = motor.paso_preprocesar()
    if resultado.get("avisos"):
        raise ErrorInforme("; ".join(resultado["avisos"]))
    if anexo and anexo["transformacion"] == "general":
        # Numeración autónoma: Tabla A.1, Figura A.1, incluidas sus referencias.
        for path in (motor.ENSAMBLADO, motor.ENSAMBLADO_CITAS):
            contenido = leer(path)
            contenido = re.sub(r"\b(Tabla|Figura) (\d+)\b", rf"\1 {anexo['letra']}.\2", contenido)
            Path(path).write_text(contenido, encoding="utf-8")
    comunes = ["--reference-doc=" + str(plantilla), "--from=markdown+fenced_divs+pipe_tables+raw_attribute",
               "--wrap=none", "--metadata=lang:es-CL"]
    ejecutar_pandoc([motor.ENSAMBLADO, "-o", motor.BODY, "--citeproc", "--bibliography=" + motor.BIB,
                    "--csl=" + motor.CSL, *comunes], cfg.build)
    ejecutar_pandoc([motor.ENSAMBLADO_CITAS, "-o", motor.BODY_CITAS, *comunes], cfg.build)
    meta = dict(cfg.datos["metadatos"])
    if anexo:
        meta["proyecto"] = f"Anexo {anexo['letra']} — {anexo['titulo']}"
    # Escribir primero un temporal impide reemplazar una entrega válida con un ZIP incompleto.
    temporal = carpeta / "resultado.docx"
    r = motor._ensamblar(motor.BODY_CITAS, str(temporal), meta=meta, con_portada=True,
        numerar=not bool(anexo), etiqueta=nombre, es_anexo=bool(anexo),
        linea_titulo=titulo_portada_anexo(p, cfg.datos["metadatos"].get("proyecto", ""), anexo),
        ilustraciones=("**Tabla " in leer(motor.ENSAMBLADO), "**Figura " in leer(motor.ENSAMBLADO)))
    if not r.get("ok") or r.get("toc"):
        raise ErrorInforme(str(r))
    errores, metricas = inspeccionar_docx(temporal)
    if metricas.get("citas") != len(claves(texto)):
        errores.append("La cantidad de campos CITATION no coincide con las citas de la fuente.")
    if sorted(citadas) != metricas.get("fuentes"):
        errores.append("Las fuentes nativas de Word no coinciden con las citadas en este documento.")
    if citadas and metricas.get("bibliografias") != 1:
        errores.append("Falta el campo nativo BIBLIOGRAPHY.")
    if errores:
        raise ErrorInforme(f"{nombre}: " + "; ".join(errores))
    try:
        temporal.replace(cfg.salida(nombre))
    except PermissionError as exc:
        raise ErrorInforme(f"No se pudo reemplazar {nombre}; cierra ese documento en Word y vuelve a generar.") from exc
    return metricas


def generar(cfg, jar=None, final=False):
    errores, avisos = comprobar_fuentes(cfg, final)
    if errores:
        guardar_reporte(cfg, errores, avisos)
        raise ErrorInforme("\n".join(errores))
    plantilla, p = perfil(cfg)
    if not shutil.which("pandoc"):
        raise ErrorInforme("Instala Pandoc 3.x y agrégalo a PATH.")
    cfg.build.mkdir(parents=True, exist_ok=True)
    estado = {"completa": False, "huella": huella(cfg), "documentos": {}}
    manifiesto = cfg.salida("generacion.json")
    manifiesto.write_text(json.dumps(estado, indent=2), encoding="utf-8")
    from .diagramas import renderizar
    from .ensamblado import ensamblar
    renderizar(cfg, jar)
    ensamblar(cfg)
    estado["documentos"]["Informe_Final.docx"] = generar_documento(cfg, plantilla, p, reunir(cfg), "Informe_Final.docx")
    for anexo in cfg.anexos:
        estado["documentos"][anexo["salida"]] = generar_documento(cfg, plantilla, p, leer(cfg.entrada(anexo["archivo"])), anexo["salida"], anexo)
    estado["completa"] = True
    manifiesto.write_text(json.dumps(estado, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    errores, avisos = validar(cfg, final)
    if errores:
        raise ErrorInforme("\n".join(errores))
    return estado
