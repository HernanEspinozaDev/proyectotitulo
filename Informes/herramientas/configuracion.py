"""Configuración explícita y rutas independientes del directorio de ejecución."""
import json
import re
from dataclasses import dataclass
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


class ErrorInforme(ValueError):
    """Error accionable de configuración, fuentes o generación."""


def leer_json(ruta):
    try:
        return json.loads(Path(ruta).read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as exc:
        raise ErrorInforme(f"No se pudo leer {ruta}: {exc}") from exc


def dentro(ruta, raiz):
    return ruta.resolve().is_relative_to(raiz.resolve())


@dataclass
class Informe:
    archivo: Path
    datos: dict
    raiz: Path
    build: Path

    def entrada(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorInforme("La ruta de entrada debe ser un texto no vacío.")
        ruta = (self.raiz / nombre).resolve()
        if not dentro(ruta, self.raiz):
            raise ErrorInforme(f"Entrada fuera de la entrega: {nombre}")
        if dentro(ruta, self.build):
            raise ErrorInforme(f"Una fuente editable no puede estar en build/: {nombre}")
        return ruta

    def salida(self, nombre):
        ruta = (self.build / nombre).resolve()
        if not dentro(ruta, self.build) or ruta == self.build:
            raise ErrorInforme(f"Salida fuera de build/: {nombre}")
        return ruta

    def recurso(self, nombre):
        ruta = (self.archivo.parent / nombre).resolve()
        if not dentro(ruta, RAIZ):
            raise ErrorInforme(f"Recurso fuera de Informes/: {nombre}")
        return ruta

    @property
    def anexos(self):
        return self.datos["anexos"]


def cargar(destino):
    ruta = Path(destino)
    if not ruta.is_absolute():
        ruta = RAIZ / ruta
    if ruta.suffix != ".json":
        ruta /= "informe.json"
    ruta = ruta.resolve()
    datos = leer_json(ruta)
    if not isinstance(datos, dict) or datos.get("version") != 1:
        raise ErrorInforme("Se requiere una configuración objeto con version: 1.")
    for campo in ("id", "metadatos", "secciones", "anexos", "bibliografia", "plantilla", "perfil"):
        if campo not in datos:
            raise ErrorInforme(f"Falta el campo de configuración: {campo}")
    if not re.fullmatch(r"ES[1-9][0-9]*PT", datos["id"]):
        raise ErrorInforme("El identificador debe tener el formato ES2PT, ES3PT, etc.")
    compat = datos.get("compatibilidad_es1", False)
    # Única excepción de lectura entre entregas: perfil de regresión mantenido en recursos/.
    esperado = (RAIZ / "recursos/compatibilidad_es1.json").resolve()
    if compat and ruta != esperado:
        raise ErrorInforme("compatibilidad_es1 solo se permite en recursos/compatibilidad_es1.json.")
    raiz = (RAIZ / "ES1PT").resolve() if compat else ruta.parent
    if raiz == (RAIZ / "ES1PT").resolve() and not compat:
        raise ErrorInforme("ES1 está cerrado. Utiliza el perfil aislado de compatibilidad.")
    build = (RAIZ / "build/compatibilidad_es1").resolve() if compat else (raiz / "build").resolve()
    if not dentro(build, RAIZ) or dentro(build, RAIZ / "ES1PT"):
        raise ErrorInforme("La salida debe estar en Informes/ y fuera de ES1PT.")
    cfg = Informe(ruta, datos, raiz, build)
    if not isinstance(datos["metadatos"], dict) or any(not isinstance(v, str) for v in datos["metadatos"].values()):
        raise ErrorInforme("metadatos debe ser un objeto con valores de texto.")
    for lista in ("secciones", "anexos"):
        if not isinstance(datos[lista], list):
            raise ErrorInforme(f"{lista} debe ser una lista ordenada.")
    if not datos["secciones"]:
        raise ErrorInforme("Declara al menos una sección de trabajo.")
    for seccion in datos["secciones"]:
        cfg.entrada(seccion)
    if len(set(datos["secciones"])) != len(datos["secciones"]):
        raise ErrorInforme("Una sección está incluida más de una vez.")
    letras, salidas, fuentes = set(), {"Informe_Final.docx"}, set(datos["secciones"])
    for anexo in cfg.anexos:
        if not isinstance(anexo, dict):
            raise ErrorInforme("Cada anexo debe ser un objeto.")
        for campo in ("letra", "titulo", "archivo", "salida", "transformacion"):
            if not isinstance(anexo.get(campo), str) or not anexo[campo].strip():
                raise ErrorInforme(f"Falta {campo} en un anexo.")
        letra, salida = anexo["letra"], anexo["salida"]
        if not re.fullmatch(r"[A-Z]", letra) or letra in letras:
            raise ErrorInforme(f"Letra de anexo inválida o duplicada: {letra}")
        if not re.fullmatch(r"Anexo_[A-Z]_[\w-]+\.docx", salida) or salida.lower() in {s.lower() for s in salidas}:
            raise ErrorInforme(f"Nombre de salida de anexo inválido o duplicado: {salida}")
        if anexo["archivo"] in fuentes:
            raise ErrorInforme(f"Fuente de anexo duplicada: {anexo['archivo']}")
        if anexo["transformacion"] not in {"general", "casos_uso", "historias_usuario"}:
            raise ErrorInforme(f"Transformación desconocida: {anexo['transformacion']}")
        cfg.entrada(anexo["archivo"])
        cfg.salida(salida)
        letras.add(letra)
        salidas.add(salida)
        fuentes.add(anexo["archivo"])
    cfg.entrada(datos["bibliografia"])
    for campo in ("plantilla", "perfil"):
        if datos[campo] is not None:
            (cfg.recurso if compat and campo == "perfil" else cfg.entrada)(datos[campo])
    return cfg
