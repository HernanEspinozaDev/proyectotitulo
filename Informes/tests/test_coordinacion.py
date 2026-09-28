import json
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from Informes.herramientas.coordinacion import Coordinador, ErrorCoordinacion, cargar_tareas


class CoordinacionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.entrega = Path(self.temp.name) / "ES2PT"
        carpeta = self.entrega / "coordinacion"
        carpeta.mkdir(parents=True)
        self.tareas = [
            {"id": "A", "titulo": "Investigar A", "objetivo": "Fuentes A",
             "archivos": ["investigacion/a.md"], "depende": []},
            {"id": "B", "titulo": "Investigar B", "objetivo": "Fuentes B",
             "archivos": ["investigacion/b.md"], "depende": []},
            {"id": "C", "titulo": "Integrar", "objetivo": "Unir resultados",
             "archivos": ["secciones/c.md"], "depende": ["A", "B"]},
        ]
        self.archivo = carpeta / "tareas.json"
        self.guardar()
        self.reloj = [1000.0]
        self.coord = Coordinador(self.entrega, reloj=lambda: self.reloj[0])

    def guardar(self):
        self.archivo.write_text(json.dumps({"version": 1, "entrega": "ES2PT", "tareas": self.tareas}), encoding="utf-8")

    def entregar(self, ruta):
        archivo = self.entrega / ruta
        archivo.parent.mkdir(parents=True, exist_ok=True)
        archivo.write_text("Investigación con fuente y pendiente explícito.", encoding="utf-8")

    def test_asigna_trabajo_distinto_y_desbloquea_dependencias(self):
        uno = self.coord.tomar("agente-1")
        dos = self.coord.tomar("agente-2")
        self.assertEqual([uno["tarea"]["id"], dos["tarea"]["id"]], ["A", "B"])
        with self.assertRaises(ErrorCoordinacion):
            self.coord.tomar("agente-3", "C")
        self.entregar("investigacion/a.md")
        self.entregar("investigacion/b.md")
        self.coord.actualizar("A", "agente-1", uno["reserva"], "finalizar", "A documentada")
        self.coord.actualizar("B", "agente-2", dos["reserva"], "finalizar", "B documentada")
        self.assertEqual(self.coord.tomar("agente-3")["tarea"]["id"], "C")

    def test_traspaso_y_reserva_anterior_no_puede_cerrar(self):
        inicial = self.coord.tomar("primero", "A")
        self.coord.actualizar("A", "primero", inicial["reserva"], "avance", "Fuentes leídas; falta tabla")
        self.coord.actualizar("A", "primero", inicial["reserva"], "liberar", "Continuar tabla en a.md")
        nuevo = self.coord.tomar("segundo", "A")
        self.assertEqual(nuevo["avance_previo"], "Continuar tabla en a.md")
        self.assertEqual(nuevo["eventos_previos"][0]["accion"], "liberar")
        with self.assertRaises(ErrorCoordinacion):
            self.coord.actualizar("A", "primero", inicial["reserva"], "finalizar", "Hecho")
        self.assertEqual(self.coord.tablero()[0]["ultimo_agente"], "segundo")
        self.assertEqual([e["accion"] for e in self.coord.historial("A")[:3]],
                         ["tomada", "liberar", "avance"])

    def test_caducidad_permite_retomar(self):
        viejo = self.coord.tomar("primero", "A", minutos=5)
        self.reloj[0] += 301
        nuevo = self.coord.tomar("segundo", "A")
        self.assertNotEqual(viejo["reserva"], nuevo["reserva"])
        with self.assertRaises(ErrorCoordinacion):
            self.coord.actualizar("A", "primero", viejo["reserva"], "avance", "Tarde")
        self.assertIn("caducada", [e["accion"] for e in self.coord.historial("A")])

    def test_finalizar_exige_entregable(self):
        reserva = self.coord.tomar("uno", "A")
        with self.assertRaises(ErrorCoordinacion):
            self.coord.actualizar("A", "uno", reserva["reserva"], "finalizar", "Sin archivo")
        self.entregar("investigacion/a.md")
        self.coord.actualizar("A", "uno", reserva["reserva"], "finalizar", "Investigación registrada")
        self.assertEqual(self.coord.tablero()[0]["estado"], "terminada")
        self.assertTrue((self.entrega / "coordinacion/bitacora.md").is_file())

    def test_toma_concurrente_de_unica_tarea(self):
        self.tareas = self.tareas[:1]
        self.guardar()
        coord_a = Coordinador(self.entrega)
        coord_b = Coordinador(self.entrega)

        def intentar(par):
            try:
                return par[0].tomar(par[1], "A")["agente"]
            except ErrorCoordinacion:
                return None

        with ThreadPoolExecutor(max_workers=2) as grupo:
            resultados = list(grupo.map(intentar, [(coord_a, "uno"), (coord_b, "dos")]))
        self.assertEqual(len([r for r in resultados if r]), 1)

    def test_recurso_compartido_impide_escritura_simultanea(self):
        self.tareas[0]["recursos"] = ["bibliografia"]
        self.tareas[1]["recursos"] = ["bibliografia"]
        self.guardar()
        coord = Coordinador(self.entrega)
        coord.tomar("uno", "A")
        with self.assertRaises(ErrorCoordinacion):
            coord.tomar("dos", "B")
        self.assertIn("Comparte archivos/recursos", coord.tablero()[1]["impedimento"])

    def test_tarea_deshabilitada_y_tablero_vacio(self):
        self.tareas[0]["habilitada"] = False
        self.tareas[0]["motivo_espera"] = "Fase posterior"
        self.guardar()
        coord = Coordinador(self.entrega)
        with self.assertRaises(ErrorCoordinacion):
            coord.tomar("uno", "A")
        self.assertEqual(coord.tablero()[0]["impedimento"], "Fase posterior")
        self.tareas = []
        self.guardar()
        self.assertEqual(Coordinador(self.entrega).tablero(), [])

    def test_rechaza_ruta_insegura_y_ciclo(self):
        self.tareas[0]["archivos"] = ["../ES1PT/informe.md"]
        self.guardar()
        with self.assertRaises(ErrorCoordinacion):
            cargar_tareas(self.archivo)
        self.tareas[0]["archivos"] = ["investigacion/a.md"]
        self.tareas[0]["depende"] = ["C"]
        self.guardar()
        with self.assertRaises(ErrorCoordinacion):
            cargar_tareas(self.archivo)


if __name__ == "__main__":
    unittest.main()
