"""Pruebas de integración de fuentes SVG en el flujo común de informes."""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from herramientas.configuracion import ErrorInforme, RAIZ, cargar
from herramientas.diagramas import nombres_generados, renderizar
from herramientas.validacion import comprobar_fuentes


class DiagramasSVGTest(unittest.TestCase):
    def setUp(self):
        pruebas = RAIZ / "build/tests"
        pruebas.mkdir(parents=True, exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(dir=pruebas)
        self.addCleanup(self.tmp.cleanup)
        self.raiz = Path(self.tmp.name)
        (self.raiz / "diagramas").mkdir()
        (self.raiz / "seccion.md").write_text(
            "# Informe\n\n![Proceso](imagenes/figura-proceso.png)\n", encoding="utf-8")
        (self.raiz / "referencias.bib").write_text("", encoding="utf-8")
        (self.raiz / "informe.json").write_text(json.dumps({
            "version": 1, "id": "ES99PT", "metadatos": {"proyecto": "Prueba"},
            "secciones": ["seccion.md"], "anexos": [], "bibliografia": "referencias.bib",
            "plantilla": None, "perfil": None,
        }), encoding="utf-8")
        self.cfg = cargar(self.raiz / "informe.json")
        self.svg = self.raiz / "diagramas/proceso.svg"

    def test_svg_referenciado_se_acepta_y_solo_renderiza_en_build(self):
        original = '<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10"/>'
        self.svg.write_text(original, encoding="utf-8")
        self.assertEqual(comprobar_fuentes(self.cfg)[0], [])

        def exportar(argumentos, **_):
            destino = Path(next(a.split("=", 1)[1] for a in argumentos if a.startswith("--export-filename=")))
            destino.write_bytes(b"PNG de prueba")
            return type("Resultado", (), {"returncode": 0, "stderr": ""})()

        with patch.dict(os.environ, {"INKSCAPE_BIN": sys.executable}):
            with patch("herramientas.diagramas.subprocess.run", side_effect=exportar):
                salidas = renderizar(self.cfg)
        self.assertEqual(salidas, [self.raiz / "build/imagenes/figura-proceso.png"])
        self.assertEqual(self.svg.read_text(encoding="utf-8"), original)

    def test_svg_malformado_es_error(self):
        self.svg.write_text("<svg", encoding="utf-8")
        with self.assertRaisesRegex(ErrorInforme, "SVG inválido"):
            nombres_generados(self.cfg)

    def test_nombre_duplicado_entre_svg_y_plantuml_es_error(self):
        self.svg.write_text('<svg xmlns="http://www.w3.org/2000/svg"/>', encoding="utf-8")
        (self.raiz / "diagramas/proceso.puml").write_text("@startuml\n@enduml\n", encoding="utf-8")
        with self.assertRaisesRegex(ErrorInforme, "duplicado"):
            nombres_generados(self.cfg)


if __name__ == "__main__":
    unittest.main()
