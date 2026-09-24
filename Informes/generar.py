#!/usr/bin/env python
"""Entrada única del sistema de informes; ejecutar desde cualquier carpeta."""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

from herramientas.configuracion import ErrorInforme, RAIZ, cargar
from herramientas.ensamblado import ensamblar
from herramientas.validacion import comprobar_fuentes, guardar_reporte, validar


def nuevo(nombre, inicializar=False):
    if not re.fullmatch(r"ES[2-9][0-9]*PT|ES1[0-9]+PT", nombre):
        raise ErrorInforme("Usa un nombre de entrega ES2PT, ES3PT, ...; ES1 está cerrado.")
    destino = RAIZ / nombre
    if destino.exists() and not inicializar:
        raise ErrorInforme(f"{nombre} ya existe. No se ha sobrescrito ningún archivo.")
    destino.mkdir(parents=True, exist_ok=True)
    plantilla = RAIZ / "plantillas/nueva_entrega"
    for origen in plantilla.rglob("*"):
        salida = destino / origen.relative_to(plantilla)
        if origen.is_dir():
            salida.mkdir(parents=True, exist_ok=True)
        elif not salida.exists():
            contenido = origen.read_text(encoding="utf-8").replace("__ENTREGA__", nombre)
            # Exclusivo: también protege frente a creaciones concurrentes.
            with salida.open("x", encoding="utf-8", newline="\n") as f:
                f.write(contenido)
    return destino


def diagnostico(cfg):
    from herramientas.word import perfil
    errores, avisos = comprobar_fuentes(cfg)
    print(f"Entrega: {cfg.datos['id']}\nFuentes: {cfg.raiz}\nSalida: {cfg.build}")
    for programa in ("pandoc", "java"):
        print(f"{programa}: {shutil.which(programa) or 'NO DISPONIBLE'}")
    print("inkscape: " + (os.environ.get("INKSCAPE_BIN") or shutil.which("inkscape") or "NO DISPONIBLE"))
    print("PLANTUML_JAR: " + (os.environ.get("PLANTUML_JAR") or "no configurado; también admite --plantuml"))
    try:
        plantilla, _ = perfil(cfg)
        print(f"Plantilla revisada: {plantilla}")
    except ErrorInforme as exc:
        errores.append(str(exc))
    if not shutil.which("pandoc"):
        errores.append("Pandoc no disponible para generar Word.")
    guardar_reporte(cfg, errores, avisos)
    mostrar(errores, avisos)
    return 1 if errores else 0


def mostrar(errores, avisos):
    for e in errores:
        print("ERROR: " + e)
    for a in avisos:
        print("AVISO: " + a)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("accion", choices=["nuevo", "diagnostico", "diagramas", "ensamblar", "generar", "validar", "actualizar-word"])
    parser.add_argument("entrega", help="ES2PT o ruta a informe.json; compatibilidad: recursos/compatibilidad_es1.json")
    parser.add_argument("--plantuml", help="Ruta al JAR local de PlantUML")
    parser.add_argument("--final", action="store_true", help="Bloquear pendientes de redacción, bibliografía y metadatos")
    parser.add_argument("--inicializar-existente", action="store_true", help="Solo para nuevo: añadir archivos ausentes sin sobrescribir")
    parser.add_argument("--estilo-apa", help="Ruta explícita al APASeventhEdition.xsl instalado en Word")
    args = parser.parse_args(argv)
    try:
        if args.accion == "nuevo":
            print(nuevo(args.entrega, args.inicializar_existente))
            return 0
        cfg = cargar(args.entrega)
        if args.accion == "diagnostico":
            return diagnostico(cfg)
        if args.accion == "diagramas":
            from herramientas.diagramas import renderizar
            for imagen in renderizar(cfg, args.plantuml):
                print(imagen)
            return 0
        if args.accion == "ensamblar":
            errores, avisos = comprobar_fuentes(cfg, args.final)
            mostrar(errores, avisos)
            if errores:
                guardar_reporte(cfg, errores, avisos)
                return 1
            print(ensamblar(cfg))
        elif args.accion == "generar":
            from herramientas.word import generar
            generar(cfg, args.plantuml, args.final)
            print(f"Generación completada: {cfg.build}")
        elif args.accion == "validar":
            errores, avisos = validar(cfg, args.final)
            mostrar(errores, avisos)
            print(cfg.salida("reporte_validacion.md"))
            return 1 if errores else 0
        else:
            if os.name != "nt":
                raise ErrorInforme("actualizar-word requiere Windows y Microsoft Word instalado.")
            errores, avisos = validar(cfg, args.final)
            mostrar(errores, avisos)
            if errores:
                return 1
            cmd = ["powershell.exe", "-NoProfile", "-File", str(RAIZ / "herramientas/actualizar_campos.ps1"),
                   "-Carpeta", str(cfg.build), "-SoloIndices"]
            if args.estilo_apa:
                cmd += ["-EstiloApa", str(Path(args.estilo_apa).resolve())]
            res = subprocess.run(cmd)
            if res.returncode:
                return res.returncode
            errores, avisos = validar(cfg, args.final)
            mostrar(errores, avisos)
            return 1 if errores else 0
        return 0
    except (ErrorInforme, OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    sys.exit(main())
