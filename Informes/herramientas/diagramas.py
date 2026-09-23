"""Render de PlantUML y SVG editables en build/, nunca sobre las fuentes."""
import os
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

from .configuracion import ErrorInforme
from .ensamblado import leer


def fuentes(cfg):
    entradas = {}
    carpeta = cfg.entrada("docx/diagramas" if cfg.datos.get("compatibilidad_es1") else "diagramas")
    for ruta in sorted(carpeta.glob("*.puml")):
        entradas["figura-" + ruta.stem] = leer(ruta)
    # Interpretación histórica explícita; no inferir M01/actores en anexos genéricos.
    for a in cfg.anexos:
        if a["transformacion"] != "casos_uso":
            continue
        from .motor_word import _bloques_puml
        lineas = leer(cfg.entrada(a["archivo"])).splitlines()
        for inicio, fin, clave in _bloques_puml(lineas):
            nombre = "figura-" + clave
            cuerpo = "\n".join(lineas[inicio + 1:fin])
            if nombre in entradas:
                raise ErrorInforme(f"Identificador PlantUML duplicado: {nombre}")
            entradas[nombre] = cuerpo
    return entradas


def renderizar(cfg, jar=None):
    nombres_generados(cfg)
    resultados = renderizar_svg(cfg)
    entradas = fuentes(cfg)
    if not entradas:
        return resultados
    jar_path = Path(jar or os.environ.get("PLANTUML_JAR", ""))
    if not jar_path.is_file():
        raise ErrorInforme("Indica --plantuml C:/ruta/plantuml.jar o configura PLANTUML_JAR.")
    java = shutil.which("java")
    if not java:
        raise ErrorInforme("Java no está disponible en PATH.")
    puml, imagenes = cfg.salida("puml"), cfg.salida("imagenes")
    puml.mkdir(parents=True, exist_ok=True)
    imagenes.mkdir(parents=True, exist_ok=True)
    for nombre, cuerpo in entradas.items():
        ruta = puml / (nombre + ".puml")
        if "@startuml" not in cuerpo:
            cuerpo = "@startuml\n" + cuerpo + "\n@enduml\n"
        destino = imagenes / (nombre + ".png")
        # Reutilizar solo una imagen cuya fuente y JAR no hayan cambiado.
        misma_fuente = ruta.is_file() and leer(ruta) == cuerpo
        if misma_fuente and destino.is_file() and destino.stat().st_mtime >= max(ruta.stat().st_mtime, jar_path.stat().st_mtime):
            resultados.append(destino)
            continue
        ruta.write_text(cuerpo, encoding="utf-8")
        res = subprocess.run([java, "-Djava.awt.headless=true", "-jar", str(jar_path.resolve()),
                              "-charset", "UTF-8", "-tpng", "-o", str(imagenes), str(ruta)],
                             capture_output=True, text=True, encoding="utf-8", errors="replace")
        if res.returncode or not destino.is_file():
            raise ErrorInforme(f"PlantUML falló para {nombre}: {res.stderr[:500]}")
        resultados.append(destino)
    return resultados


def fuentes_svg(cfg):
    """SVG editables para notaciones que no representa PlantUML, como BPMN."""
    carpeta = cfg.entrada("diagramas")
    entradas = {}
    for ruta in sorted(carpeta.glob("*.svg")):
        try:
            raiz = ET.parse(ruta).getroot()
        except (OSError, ET.ParseError) as exc:
            raise ErrorInforme(f"SVG inválido {ruta.name}: {exc}") from exc
        if raiz.tag != "{http://www.w3.org/2000/svg}svg":
            raise ErrorInforme(f"SVG sin elemento raíz válido: {ruta.name}")
        entradas["figura-" + ruta.stem] = ruta
    return entradas


def nombres_generados(cfg):
    puml, svg = fuentes(cfg), fuentes_svg(cfg)
    repetidos = set(puml) & set(svg)
    if repetidos:
        raise ErrorInforme("Nombre de diagrama duplicado entre PlantUML y SVG: " + ", ".join(sorted(repetidos)))
    return set(puml) | set(svg)


def renderizar_svg(cfg):
    entradas = fuentes_svg(cfg)
    if not entradas:
        return []
    inkscape = os.environ.get("INKSCAPE_BIN") or shutil.which("inkscape")
    if not inkscape or not Path(inkscape).is_file():
        raise ErrorInforme("Los diagramas SVG requieren Inkscape en PATH o INKSCAPE_BIN.")
    imagenes = cfg.salida("imagenes")
    imagenes.mkdir(parents=True, exist_ok=True)
    resultados = []
    for nombre, origen in entradas.items():
        destino = imagenes / (nombre + ".png")
        res = subprocess.run([str(inkscape), str(origen), "--export-type=png",
                              "--export-width=1800", "--export-background=white",
                              "--export-filename=" + str(destino)], capture_output=True,
                             text=True, encoding="utf-8", errors="replace")
        if res.returncode or not destino.is_file():
            raise ErrorInforme(f"Inkscape falló para {nombre}: {res.stderr[:500]}")
        resultados.append(destino)
    return resultados
