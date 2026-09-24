"""Pruebas de integración pequeñas; requieren Pandoc, sin Java ni Word."""
import contextlib
import io
import json
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from herramientas.configuracion import ErrorInforme, RAIZ, cargar
from herramientas.word import generar, perfil
from herramientas.validacion import validar


@unittest.skipUnless(shutil.which("pandoc"), "Requiere Pandoc 3.x")
class WordTest(unittest.TestCase):
    def setUp(self):
        (RAIZ / "build/tests").mkdir(parents=True, exist_ok=True)
        tmp = tempfile.TemporaryDirectory(dir=RAIZ / "build/tests")
        self.addCleanup(tmp.cleanup)
        self.raiz = Path(tmp.name)
        shutil.copyfile(RAIZ / "ES1PT/docx/plantilla.docx", self.raiz / "plantilla.docx")
        shutil.copyfile(RAIZ / "recursos/perfiles/inacap_es1.json", self.raiz / "perfil.json")
        shutil.copyfile(RAIZ / "ES1PT/docx/referencias.bib", self.raiz / "referencias.bib")
        self.datos = {"version": 1, "id": "ES99PT", "metadatos": {"proyecto": "Prueba & ejemplo", "titulo": "Prueba"},
            "secciones": ["uno.md", "dos.md"], "anexos": [], "bibliografia": "referencias.bib",
            "plantilla": "plantilla.docx", "perfil": "perfil.json"}
        (self.raiz / "uno.md").write_text("# Primero\n\nTexto de prueba.\n", encoding="utf-8")
        (self.raiz / "dos.md").write_text("# Segundo\n\nMás texto.\n", encoding="utf-8")

    def ejecutar(self):
        path = self.raiz / "informe.json"
        path.write_text(json.dumps(self.datos), encoding="utf-8")
        cfg = cargar(path)
        with contextlib.redirect_stdout(io.StringIO()):
            estado = generar(cfg)
        self.assertEqual(validar(cfg)[0], [])
        return cfg, estado

    def test_sin_citas_ni_anexos_y_capitulos_variables(self):
        cfg, estado = self.ejecutar()
        metricas = estado["documentos"]["Informe_Final.docx"]
        self.assertEqual(metricas["citas"], 0)
        self.assertEqual(metricas["fuentes"], [])
        self.assertEqual(metricas["capitulos"], 3)  # dos secciones y Referencias
        self.assertEqual(len(estado["documentos"]), 1)
        with zipfile.ZipFile(cfg.salida("Informe_Final.docx")) as z:
            xml = z.read("word/document.xml").decode()
            self.assertIn("Prueba &amp; ejemplo", xml)
            self.assertNotIn("BIBLIOGRAFIA__WORD", xml)

    def test_citas_por_documento_y_anexo_generico(self):
        (self.raiz / "uno.md").write_text("# Primero\n\nArgumento [@sommerville; @iso25010].\n\n"
            "*Tabla. Comparación* <!--#tab:comparacion-->\n\n| A | B |\n| --- | --- |\n| 1 | 2 |\n\n"
            "Ver {{Tabla:comparacion}}.\n\n```text\n[@ejemplo_literal]\n```\n", encoding="utf-8")
        (self.raiz / "anexo.md").write_text("# Evidencias\n\nReferencia [@wcag21].\n\n"
            "*Tabla. Detalle* <!--#tab:detalle-->\n\n| A | B |\n| --- | --- |\n| 1 | 2 |\n\n"
            "Ver {{Tabla:detalle}}.\n", encoding="utf-8")
        self.datos["anexos"] = [{"letra": "F", "titulo": "Evidencias", "archivo": "anexo.md",
                                 "salida": "Anexo_F_Evidencias.docx", "transformacion": "general"}]
        cfg, estado = self.ejecutar()
        self.assertEqual(estado["documentos"]["Informe_Final.docx"]["fuentes"], ["iso25010", "sommerville"])
        self.assertEqual(estado["documentos"]["Anexo_F_Evidencias.docx"]["fuentes"], ["wcag21"])
        with zipfile.ZipFile(cfg.salida("Anexo_F_Evidencias.docx")) as z:
            self.assertIn("Tabla F.1", z.read("word/document.xml").decode())
        with zipfile.ZipFile(cfg.salida("Informe_Final.docx")) as z:
            self.assertIn("ejemplo_literal", z.read("word/document.xml").decode())

    def test_muestra_no_habilita_perfil_oficial_ni_omite_firma(self):
        perfil_ruta = self.raiz / "perfil.json"
        datos = json.loads(perfil_ruta.read_text(encoding="utf-8"))
        datos["aprobado"] = False
        perfil_ruta.write_text(json.dumps(datos), encoding="utf-8")
        ruta = self.raiz / "informe.json"
        ruta.write_text(json.dumps(self.datos), encoding="utf-8")
        cfg = cargar(ruta)
        with self.assertRaisesRegex(ErrorInforme, "pendiente de adaptación"):
            perfil(cfg)
        self.assertEqual(perfil(cfg, permitir_borrador=True)[0], self.raiz / "plantilla.docx")
        datos["sha256_plantilla"] = "0" * 64
        perfil_ruta.write_text(json.dumps(datos), encoding="utf-8")
        with self.assertRaisesRegex(ErrorInforme, "no coincide"):
            perfil(cfg, permitir_borrador=True)


if __name__ == "__main__":
    unittest.main()
