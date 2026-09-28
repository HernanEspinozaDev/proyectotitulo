"""CLI de coordinación de investigación; ejecutar desde la raíz del repositorio."""

import argparse
import json
import os
import re
import sqlite3
import sys
from pathlib import Path

from herramientas.coordinacion import Coordinador, ErrorCoordinacion


RAIZ = Path(__file__).resolve().parent

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Coordina tareas documentales entre agentes en un mismo estado SQLite")
    parser.add_argument("--entrega", default="ES2PT", help="Carpeta de entrega dentro de Informes/")
    parser.add_argument("--db", default=os.environ.get("INFORMES_COORD_DB"), help="Base SQLite compartida opcional")
    sub = parser.add_subparsers(dest="orden", required=True)
    sub.add_parser("contexto", help="Orden de lectura y tareas actuales")
    tablero = sub.add_parser("tablero", help="Ver tareas, agentes y bloqueos")
    tablero.add_argument("--json", action="store_true")
    tomar = sub.add_parser("tomar", help="Reservar la siguiente tarea disponible")
    tomar.add_argument("--agente", required=True)
    tomar.add_argument("--tarea")
    tomar.add_argument("--minutos", type=int, default=90)
    for nombre in ("avance", "renovar", "liberar", "bloquear", "finalizar"):
        cmd = sub.add_parser(nombre)
        cmd.add_argument("--tarea", required=True)
        cmd.add_argument("--agente", required=True)
        cmd.add_argument("--reserva", required=True)
        cmd.add_argument("--nota", default="")
        cmd.add_argument("--minutos", type=int, default=90)
    liberar = sub.add_parser("desbloquear", help="Reabrir una tarea bloqueada con nueva evidencia")
    liberar.add_argument("--tarea", required=True)
    liberar.add_argument("--agente", required=True)
    liberar.add_argument("--nota", required=True)
    historial = sub.add_parser("historial", help="Ver el registro de avances")
    historial.add_argument("--tarea")
    historial.add_argument("--limite", type=int, default=50)
    sub.add_parser("exportar", help="Actualizar bitacora.md desde SQLite")
    args = parser.parse_args(argv)
    if not re.fullmatch(r"ES[2-9][0-9]*PT|ES1[0-9]+PT", args.entrega):
        parser.error("--entrega debe ser ES2PT, ES3PT, etc.; ES1 está cerrada.")
    try:
        coordinador = Coordinador(RAIZ / args.entrega, Path(args.db) if args.db else None)
        if args.orden == "contexto":
            resumen = RAIZ / args.entrega / "coordinacion/RESUMEN.md"
            if resumen.is_file():
                print(resumen.read_text(encoding="utf-8"))
            lectura = ["AGENTS.md", "Informes/contexto/README.md", "Informes/contexto/decisiones.md",
                       f"Informes/{args.entrega}/coordinacion/RESUMEN.md",
                       f"Informes/{args.entrega}/contexto.md", f"Informes/{args.entrega}/pendientes.md",
                       f"Informes/{args.entrega}/informe.json", f"Informes/{args.entrega}/plan_de_trabajo.md"]
            lectura += [f"Informes/{args.entrega}/investigacion/{p.name}"
                        for p in sorted((RAIZ / args.entrega / "investigacion").glob("matriz_trazabilidad*.md"))]
            print("Leer en este orden:")
            for ruta in lectura:
                if (RAIZ.parent / ruta).is_file():
                    print("-", ruta)
            print("Después: rúbrica, investigación ES1/ES2 y archivos indicados por la tarea reservada.")
            print("No editar ES1 ni build/. Seguir las prioridades de la entrega para Word.")
            print("Tablero:")
            for fila in coordinador.tablero():
                print(f"{fila['id']}: {fila['estado']} · {fila['agente'] or 'sin agente'} · "
                      f"{fila['impedimento'] or 'disponible'} · {fila['resumen'] or 'sin avance registrado'}")
        elif args.orden == "tablero":
            filas = coordinador.tablero()
            if args.json:
                print(json.dumps(filas, ensure_ascii=False, indent=2))
            else:
                for fila in filas:
                    print(f"{fila['id']} | {fila['estado']} | actual: {fila['agente'] or '—'} | "
                          f"último: {fila['ultimo_agente'] or '—'} | "
                          f"{fila['vence'] or '—'} | {fila['impedimento'] or 'disponible'}")
                    if fila["resumen"]:
                        print("  Último avance:", fila["resumen"])
        elif args.orden == "tomar":
            print(json.dumps(coordinador.tomar(args.agente, args.tarea, args.minutos), ensure_ascii=False, indent=2))
        elif args.orden in ("avance", "renovar", "liberar", "bloquear", "finalizar"):
            print(json.dumps(coordinador.actualizar(args.tarea, args.agente, args.reserva, args.orden,
                                                     args.nota, args.minutos), ensure_ascii=False, indent=2))
        elif args.orden == "desbloquear":
            print(json.dumps(coordinador.desbloquear(args.tarea, args.agente, args.nota), ensure_ascii=False))
        elif args.orden == "historial":
            print(json.dumps(coordinador.historial(args.tarea, args.limite), ensure_ascii=False, indent=2))
        else:
            print(coordinador.exportar())
        return 0
    except (ErrorCoordinacion, sqlite3.Error, OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
