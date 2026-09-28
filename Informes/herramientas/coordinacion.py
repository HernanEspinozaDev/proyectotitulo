"""Coordinación local de tareas documentales entre procesos/agentes.

SQLite es la fuente de verdad del estado vivo; tareas.json define el trabajo y
bitacora.md es una vista legible. No se importan módulos ni se escriben archivos de ES1.
"""

from __future__ import annotations

import json
import os
import re
import sqlite3
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath


class ErrorCoordinacion(Exception):
    """Solicitud o estado de coordinación inválido."""


def fecha_utc(instante: float) -> str:
    return datetime.fromtimestamp(instante, timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def ruta_relativa(valor: str) -> str:
    if not isinstance(valor, str) or not valor or "\\" in valor or ":" in valor:
        raise ErrorCoordinacion(f"Ruta de tarea inválida: {valor!r}")
    ruta = PurePosixPath(valor)
    if ruta.is_absolute() or any(parte in (".", "..") for parte in ruta.parts):
        raise ErrorCoordinacion(f"Ruta de tarea fuera de la entrega: {valor!r}")
    if ruta.parts[0] == "build":
        raise ErrorCoordinacion("Una tarea no puede entregar fuentes en build/.")
    return ruta.as_posix()


def cargar_tareas(archivo: Path, entrega: str | None = None) -> list[dict]:
    if not archivo.is_file():
        raise ErrorCoordinacion(f"Falta el tablero: {archivo}")
    datos = json.loads(archivo.read_text(encoding="utf-8"))
    if datos.get("version") != 1 or not isinstance(datos.get("tareas"), list):
        raise ErrorCoordinacion("tareas.json requiere version=1 y una lista tareas.")
    if entrega is not None and datos.get("entrega") != entrega:
        raise ErrorCoordinacion(f"El tablero no corresponde a {entrega}.")
    tareas = datos["tareas"]
    ids = set()
    for tarea in tareas:
        ident = tarea.get("id")
        if not isinstance(ident, str) or not re.fullmatch(r"[A-Z0-9_-]+", ident):
            raise ErrorCoordinacion(f"Identificador inválido: {ident!r}")
        if ident in ids:
            raise ErrorCoordinacion(f"Identificador duplicado: {ident}")
        ids.add(ident)
        if not tarea.get("titulo") or not tarea.get("objetivo"):
            raise ErrorCoordinacion(f"Faltan título u objetivo de {ident}")
        if not isinstance(tarea.get("archivos"), list) or not tarea["archivos"]:
            raise ErrorCoordinacion(f"{ident} necesita archivos de entrega.")
        tarea["archivos"] = [ruta_relativa(p) for p in tarea["archivos"]]
        tarea["recursos"] = list(tarea.get("recursos", []))
        tarea["depende"] = list(tarea.get("depende", []))
        tarea["lecturas"] = list(tarea.get("lecturas", []))
        if not isinstance(tarea.get("habilitada", True), bool):
            raise ErrorCoordinacion(f"habilitada debe ser booleana en {ident}")
        if not all(isinstance(d, str) for d in tarea["depende"]):
            raise ErrorCoordinacion(f"Dependencias inválidas en {ident}")
        for recurso in tarea["recursos"]:
            if not isinstance(recurso, str) or not recurso:
                raise ErrorCoordinacion(f"Recurso inválido en {ident}")
    for tarea in tareas:
        desconocidas = set(tarea["depende"]) - ids
        if desconocidas:
            raise ErrorCoordinacion(f"Dependencia desconocida de {tarea['id']}: {desconocidas}")
    grafo = {t["id"]: t["depende"] for t in tareas}
    visitados, pila = set(), set()

    def visitar(ident):
        if ident in pila:
            raise ErrorCoordinacion(f"Ciclo de dependencias en {ident}")
        if ident in visitados:
            return
        pila.add(ident)
        for previo in grafo[ident]:
            visitar(previo)
        pila.remove(ident)
        visitados.add(ident)

    for ident in grafo:
        visitar(ident)
    return tareas


class Coordinador:
    def __init__(self, entrega: Path, db: Path | None = None, reloj=None):
        self.entrega = Path(entrega).resolve()
        self.carpeta = self.entrega / "coordinacion"
        self.tareas = cargar_tareas(self.carpeta / "tareas.json", self.entrega.name)
        self.por_id = {t["id"]: t for t in self.tareas}
        self.db = Path(db).resolve() if db else self.carpeta / "estado.sqlite3"
        self.reloj = reloj or time.time

    def _conexion(self):
        self.db.parent.mkdir(parents=True, exist_ok=True)
        con = sqlite3.connect(self.db, timeout=15, isolation_level=None)
        con.row_factory = sqlite3.Row
        con.execute("PRAGMA busy_timeout=15000")
        con.execute("PRAGMA journal_mode=WAL")
        con.execute("""CREATE TABLE IF NOT EXISTS estados (
            id TEXT PRIMARY KEY, estado TEXT NOT NULL, agente TEXT, ultimo_agente TEXT,
            reserva TEXT, vence REAL, resumen TEXT NOT NULL DEFAULT '', actualizado REAL NOT NULL
        )""")
        con.execute("""CREATE TABLE IF NOT EXISTS eventos (
            numero INTEGER PRIMARY KEY AUTOINCREMENT, tarea TEXT NOT NULL, instante REAL NOT NULL,
            agente TEXT NOT NULL, accion TEXT NOT NULL, nota TEXT NOT NULL
        )""")
        return con

    def _sincronizar(self, con, ahora):
        declaradas = set(self.por_id)
        huerfanas = [fila["id"] for fila in con.execute(
            "SELECT id FROM estados WHERE estado='en_curso'") if fila["id"] not in declaradas]
        if huerfanas:
            raise ErrorCoordinacion("Hay reservas activas retiradas de tareas.json: " + ", ".join(huerfanas))
        nuevos = 0
        for tarea in self.tareas:
            antes = con.total_changes
            con.execute("INSERT OR IGNORE INTO estados(id, estado, actualizado) VALUES(?, 'pendiente', ?)",
                        (tarea["id"], ahora))
            nuevos += con.total_changes - antes
        return nuevos

    def _caducar(self, con, ahora):
        vencidas = con.execute(
            "SELECT id, agente FROM estados WHERE estado='en_curso' AND vence<=?", (ahora,)
        ).fetchall()
        for fila in vencidas:
            con.execute("""UPDATE estados SET estado='pendiente', agente=NULL, reserva=NULL,
                        vence=NULL, actualizado=? WHERE id=?""", (ahora, fila["id"]))
            self._evento(con, fila["id"], fila["agente"] or "sistema", "caducada",
                         "Reserva vencida; el avance anterior sigue en la bitácora.", ahora)
        return len(vencidas)

    @staticmethod
    def _evento(con, tarea, agente, accion, nota, ahora):
        con.execute("INSERT INTO eventos(tarea, instante, agente, accion, nota) VALUES(?,?,?,?,?)",
                    (tarea, ahora, agente, accion, nota))

    @staticmethod
    def _recursos(tarea):
        return set(tarea["archivos"]) | set(tarea["recursos"])

    def _estado(self, con, ident):
        return con.execute("SELECT * FROM estados WHERE id=?", (ident,)).fetchone()

    def _impedimento(self, con, tarea):
        fila = self._estado(con, tarea["id"])
        if fila["estado"] != "pendiente":
            return fila["estado"]
        if not tarea.get("habilitada", True):
            return tarea.get("motivo_espera", "Deshabilitada en tareas.json")
        previas = [ident for ident in tarea["depende"]
                   if self._estado(con, ident)["estado"] != "terminada"]
        if previas:
            return "Depende de: " + ", ".join(previas)
        propios = self._recursos(tarea)
        for otra in self.tareas:
            if otra["id"] != tarea["id"] and self._estado(con, otra["id"])["estado"] == "en_curso":
                if propios & self._recursos(otra):
                    return f"Comparte archivos/recursos con {otra['id']}"
        return None

    @staticmethod
    def _limpiar(nota):
        return str(nota or "").replace("\r", " ").replace("\n", " ").replace("|", "\\|").strip()

    def _bitacora(self, con):
        lineas = [f"# Bitácora de coordinación de {self.entrega.name}", "",
                  "Vista generada de `estado.sqlite3`; consultar el tablero para el estado actual. No editar a mano.",
                  "", "| Tarea | Estado | Agente actual | Último agente | Vence (UTC) | Disponibilidad | Último avance |",
                  "| --- | --- | --- | --- | --- | --- | --- |"]
        for tarea in self.tareas:
            fila = self._estado(con, tarea["id"])
            vence = fecha_utc(fila["vence"]) if fila["vence"] else "—"
            impedimento = self._impedimento(con, tarea)
            lineas.append(f"| {tarea['id']} — {self._limpiar(tarea['titulo'])} | {fila['estado']} | "
                          f"{self._limpiar(fila['agente']) or '—'} | "
                          f"{self._limpiar(fila['ultimo_agente']) or '—'} | {vence} | "
                          f"{self._limpiar(impedimento) if impedimento else 'disponible'} | "
                          f"{self._limpiar(fila['resumen']) or '—'} |")
        lineas.extend(["", "## Eventos", ""])
        for fila in con.execute("SELECT * FROM eventos ORDER BY numero DESC"):
            lineas.append(f"- {fecha_utc(fila['instante'])} · **{fila['tarea']}** · "
                          f"{self._limpiar(fila['agente'])} · {fila['accion']}: {self._limpiar(fila['nota'])}")
        temporal = self.carpeta / f".bitacora.{uuid.uuid4().hex}.tmp"
        temporal.write_text("\n".join(lineas) + "\n", encoding="utf-8")
        os.replace(temporal, self.carpeta / "bitacora.md")

    def _operar(self, accion, mutacion=False):
        con = self._conexion()
        try:
            con.execute("BEGIN IMMEDIATE")
            ahora = self.reloj()
            nuevos = self._sincronizar(con, ahora)
            caducadas = self._caducar(con, ahora)
            resultado = accion(con, ahora)
            if mutacion or nuevos or caducadas:
                self._bitacora(con)
            con.commit()
            return resultado
        except Exception:
            con.rollback()
            raise
        finally:
            con.close()

    def tablero(self):
        def leer(con, _):
            filas = []
            for tarea in self.tareas:
                estado = self._estado(con, tarea["id"])
                filas.append({
                    "id": tarea["id"], "titulo": tarea["titulo"], "estado": estado["estado"],
                    "agente": estado["agente"], "ultimo_agente": estado["ultimo_agente"],
                    "vence": fecha_utc(estado["vence"]) if estado["vence"] else None,
                    "resumen": estado["resumen"], "impedimento": self._impedimento(con, tarea),
                    "depende": tarea["depende"], "archivos": tarea["archivos"]
                })
            return filas
        return self._operar(leer, mutacion=True)

    def tomar(self, agente, ident=None, minutos=90):
        if not isinstance(agente, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}", agente) or not 5 <= minutos <= 240:
            raise ErrorCoordinacion("Indicar un agente único y una reserva entre 5 y 240 minutos.")

        def reservar(con, ahora):
            candidatas = [self.por_id[ident]] if ident in self.por_id else self.tareas if ident is None else []
            if not candidatas:
                raise ErrorCoordinacion(f"Tarea desconocida: {ident}")
            elegida = next((t for t in candidatas if self._impedimento(con, t) is None), None)
            if elegida is None:
                razones = "; ".join(f"{t['id']}: {self._impedimento(con, t)}" for t in candidatas)
                raise ErrorCoordinacion("Ninguna tarea disponible. " + razones)
            previos = [dict(f) for f in con.execute(
                "SELECT instante, agente, accion, nota FROM eventos WHERE tarea=? ORDER BY numero DESC LIMIT 3",
                (elegida["id"],)).fetchall()]
            for evento in previos:
                evento["fecha"] = fecha_utc(evento.pop("instante"))
            reserva = uuid.uuid4().hex
            con.execute("""UPDATE estados SET estado='en_curso', agente=?, ultimo_agente=?,
                        reserva=?, vence=?, actualizado=? WHERE id=?""",
                        (agente, agente, reserva, ahora + minutos * 60, ahora, elegida["id"]))
            self._evento(con, elegida["id"], agente, "tomada", "Reserva exclusiva iniciada.", ahora)
            return {"tarea": elegida, "agente": agente, "reserva": reserva,
                    "vence": fecha_utc(ahora + minutos * 60),
                    "avance_previo": self._estado(con, elegida["id"])["resumen"],
                    "eventos_previos": previos}
        return self._operar(reservar, mutacion=True)

    def _comprobar_reserva(self, con, ident, agente, reserva):
        if ident not in self.por_id:
            raise ErrorCoordinacion(f"Tarea desconocida: {ident}")
        fila = self._estado(con, ident)
        if fila["estado"] != "en_curso" or fila["agente"] != agente or fila["reserva"] != reserva:
            raise ErrorCoordinacion("La tarea no pertenece a esta reserva; consultar tablero y tomar de nuevo.")

    def actualizar(self, ident, agente, reserva, accion, nota="", minutos=90):
        if accion not in {"avance", "renovar", "liberar", "bloquear", "finalizar"}:
            raise ErrorCoordinacion(f"Acción desconocida: {accion}")
        if not 5 <= minutos <= 240:
            raise ErrorCoordinacion("La reserva debe durar entre 5 y 240 minutos.")
        if accion != "renovar" and not nota.strip():
            raise ErrorCoordinacion("Registrar una nota concreta para el traspaso.")

        def cambiar(con, ahora):
            self._comprobar_reserva(con, ident, agente, reserva)
            if accion == "finalizar":
                faltantes = []
                for ruta in self.por_id[ident]["archivos"]:
                    destino = (self.entrega / ruta).resolve()
                    if not destino.is_relative_to(self.entrega):
                        raise ErrorCoordinacion(f"Entregable fuera de la entrega: {ruta}")
                    if not destino.is_file():
                        faltantes.append(ruta)
                if faltantes:
                    raise ErrorCoordinacion("Faltan entregables: " + ", ".join(faltantes))
            estado = {"avance": "en_curso", "renovar": "en_curso", "liberar": "pendiente",
                      "bloquear": "bloqueada", "finalizar": "terminada"}[accion]
            continua = accion in {"avance", "renovar"}
            con.execute("""UPDATE estados SET estado=?, agente=?, reserva=?, vence=?,
                        resumen=?, actualizado=? WHERE id=?""",
                        (estado, agente if continua else None, reserva if continua else None,
                         ahora + minutos * 60 if continua else None,
                         nota if nota else self._estado(con, ident)["resumen"], ahora, ident))
            if accion != "renovar":
                self._evento(con, ident, agente, accion, nota, ahora)
            return {"tarea": ident, "estado": estado,
                    "vence": fecha_utc(ahora + minutos * 60) if continua else None}
        return self._operar(cambiar, mutacion=True)

    def desbloquear(self, ident, agente, nota):
        if not isinstance(agente, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}", agente) or not nota.strip():
            raise ErrorCoordinacion("Indicar agente y motivo de desbloqueo.")

        def cambiar(con, ahora):
            if ident not in self.por_id or self._estado(con, ident)["estado"] != "bloqueada":
                raise ErrorCoordinacion("La tarea no está bloqueada.")
            con.execute("""UPDATE estados SET estado='pendiente', resumen=?, actualizado=? WHERE id=?""",
                        (nota, ahora, ident))
            self._evento(con, ident, agente, "desbloqueada", nota, ahora)
            return {"tarea": ident, "estado": "pendiente"}
        return self._operar(cambiar, mutacion=True)

    def historial(self, ident=None, limite=50):
        if ident is not None and ident not in self.por_id:
            raise ErrorCoordinacion(f"Tarea desconocida: {ident}")
        if not 1 <= limite <= 500:
            raise ErrorCoordinacion("El límite debe estar entre 1 y 500.")

        def leer(con, _):
            if ident:
                filas = con.execute("SELECT * FROM eventos WHERE tarea=? ORDER BY numero DESC LIMIT ?",
                                    (ident, limite)).fetchall()
            else:
                filas = con.execute("SELECT * FROM eventos ORDER BY numero DESC LIMIT ?", (limite,)).fetchall()
            return [{"numero": f["numero"], "tarea": f["tarea"], "fecha": fecha_utc(f["instante"]),
                     "agente": f["agente"], "accion": f["accion"], "nota": f["nota"]} for f in filas]
        return self._operar(leer)

    def exportar(self):
        def escribir(con, _):
            self._bitacora(con)
            return self.carpeta / "bitacora.md"
        return self._operar(escribir)
