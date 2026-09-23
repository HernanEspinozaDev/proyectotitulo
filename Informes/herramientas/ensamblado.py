"""Ensamblado reproducible de secciones; Markdown es la fuente editable."""
import json
import re
from pathlib import Path
from urllib.parse import unquote

from .configuracion import ErrorInforme, dentro


def leer(ruta):
    try:
        return Path(ruta).read_text(encoding="utf-8-sig")
    except OSError as exc:
        raise ErrorInforme(f"No se pudo leer {ruta}: {exc}") from exc


def sin_cabecera(texto):
    return re.sub(r"\A---\r?\n.*?\r?\n---(?:\r?\n|$)", "", texto, count=1, flags=re.S)


def sin_codigo(texto):
    """Excluye ejemplos de código de las comprobaciones de citas y etiquetas."""
    return re.sub(r"^(`{3,}|~{3,}).*?^\1\s*$", "", texto, flags=re.M | re.S)


def documentos(cfg):
    return [(cfg.entrada(s), leer(cfg.entrada(s))) for s in cfg.datos["secciones"]] + [
        (cfg.entrada(a["archivo"]), leer(cfg.entrada(a["archivo"]))) for a in cfg.anexos]


def imagenes(texto):
    return re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", texto)


def resolver_imagen(cfg, origen, ruta):
    ruta = unquote(ruta.strip().strip("<>"))
    if re.match(r"^[a-zA-Z]+://", ruta) or ruta.startswith("data:"):
        raise ErrorInforme(f"Guarda la imagen localmente para una entrega reproducible: {ruta}")
    # Convención: todas las rutas de recursos son relativas a la raíz de la entrega.
    # El perfil histórico usa la carpeta docx como raíz de imágenes.
    base = cfg.raiz / "docx" if cfg.datos.get("compatibilidad_es1") else cfg.raiz
    destino = (base / ruta).resolve()
    if not dentro(destino, cfg.raiz):
        raise ErrorInforme(f"Imagen fuera de la entrega en {origen.name}: {ruta}")
    return destino


def reunir(cfg):
    meta = {"lang": "es-CL", **cfg.datos["metadatos"]}
    cabecera = "---\n" + "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items()) + "\n---\n\n"
    partes = [sin_cabecera(leer(cfg.entrada(s))).strip() for s in cfg.datos["secciones"]]
    texto = cabecera + "\n\n".join(partes) + "\n"
    if cfg.datos.get("agregar_referencias", True):
        if not re.search(r"\{#refs\}", texto):
            texto += "\n# Referencias\n\n::: {#refs}\n:::\n"
    if cfg.anexos and cfg.datos.get("agregar_indice_anexos", True):
        texto += "\n# Anexos\n\n"
        for a in cfg.anexos:
            texto += f"## Anexo {a['letra']} — {a['titulo']}\n\nDocumento independiente: `{a['salida']}`.\n\n"
    return texto


def ensamblar(cfg):
    cfg.build.mkdir(parents=True, exist_ok=True)
    salida = cfg.salida("informe_ensamblado.md")
    salida.write_text(reunir(cfg), encoding="utf-8")
    return salida
