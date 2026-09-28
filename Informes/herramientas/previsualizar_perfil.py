"""Genera una muestra aislada para revisar un perfil Word todavía no aprobado.

La generación oficial sigue exigiendo ``aprobado: true``. Esta muestra no es
una entrega académica y nunca se escribe en el directorio principal de build/.
"""

from dataclasses import replace
from pathlib import Path
import argparse
import json
import shutil
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from herramientas.configuracion import ErrorInforme, cargar
from herramientas.ensamblado import leer, sin_cabecera
from herramientas.word import generar_documento, perfil


def previsualizar(nombre):
    original = cargar(nombre)
    if original.datos["id"] != "ES2PT":
        raise ErrorInforme("Esta muestra usa secciones de ES2PT y solo admite ES2PT.")
    plantilla, datos_perfil = perfil(original, permitir_borrador=True)
    cfg = replace(original, build=original.salida("qa_perfil"))
    cfg.build.mkdir(parents=True, exist_ok=True)
    manifiesto = cfg.salida("generacion.json")
    manifiesto.write_text(json.dumps({"completa": False, "tipo": "muestra_tecnica_no_entrega"}, indent=2), encoding="utf-8")

    intro = sin_cabecera(leer(cfg.entrada("secciones/01_introduccion.md"))).split("[[PENDIENTE:", 1)[0].strip()
    arquitectura = sin_cabecera(leer(cfg.entrada("secciones/03_00_arquitectura.md"))).split("[[PENDIENTE:", 1)[0].strip()
    bpmn = sin_cabecera(leer(cfg.entrada("secciones/03_01_bpmn.md"))).split("### Reserva, pago y contratación", 1)[0].strip()
    texto = (
        "# Muestra técnica de formato ES2\n\n"
        "**Documento parcial para revisión visual. No constituye una entrega académica.**\n\n"
        f"{intro}\n\n{arquitectura}\n\n{bpmn}\n\n"
        "# Referencias bibliográficas\n\n::: {#refs}\n:::\n"
    )
    imagen = "figura-bpmn01_identidad.png"
    origen_imagen = original.salida("imagenes") / imagen
    if not origen_imagen.is_file():
        raise ErrorInforme(f"Falta imagen de revisión: {origen_imagen}. Ejecuta diagramas ES2PT primero.")
    carpeta_imagenes = cfg.salida("imagenes")
    carpeta_imagenes.mkdir(parents=True, exist_ok=True)
    shutil.copy2(origen_imagen, carpeta_imagenes / imagen)
    principal = "Muestra_ES2.docx"
    metricas_principal = generar_documento(cfg, plantilla, datos_perfil, texto, principal)

    # Se elige el catálogo de casos de prueba por su archivo, no por su letra:
    # la letra depende del orden de anexos declarado en informe.json.
    anexo = next((a for a in cfg.anexos if "casos_de_prueba" in a["archivo"]), None)
    if not anexo:
        raise ErrorInforme("La muestra requiere el catálogo de casos de prueba declarado en ES2.")
    parte = sin_cabecera(leer(cfg.entrada(anexo["archivo"]))).split("## PT-02", 1)[0].strip()
    parte = parte.replace("# Catálogo de casos de prueba de ES2", "# Muestra parcial del catálogo de pruebas", 1)
    parte = "**Muestra de formato; solo incluye PT-01. No constituye el anexo completo.**\n\n" + parte
    anexo_muestra = {**anexo, "titulo": "Muestra parcial de casos de prueba",
                     "salida": f"Anexo_{anexo['letra']}_Muestra.docx"}
    metricas_anexo = generar_documento(cfg, plantilla, datos_perfil, parte, anexo_muestra["salida"], anexo_muestra)
    manifiesto.write_text(json.dumps({"completa": True, "tipo": "muestra_tecnica_no_entrega",
        "documentos": {principal: metricas_principal, anexo_muestra["salida"]: metricas_anexo}}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Muestra técnica: {cfg.salida(principal)} — {metricas_principal}")
    print(f"Anexo parcial: {cfg.salida(anexo_muestra['salida'])} — {metricas_anexo}")
    print("Perfil oficial sin modificar; estos DOCX no son una entrega.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entrega", help="Configuración ES2PT")
    args = parser.parse_args()
    try:
        previsualizar(args.entrega)
        return 0
    except (ErrorInforme, OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
