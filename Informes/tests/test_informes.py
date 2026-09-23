import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import generar
from herramientas.configuracion import ErrorInforme, RAIZ, cargar
from herramientas.ensamblado import reunir
from herramientas.validacion import comprobar_fuentes, huella, inspeccionar_docx, validar
from herramientas.word import perfil, titulo_portada_anexo


class InformesTest(unittest.TestCase):
    def setUp(self):
        (RAIZ / "build/tests").mkdir(parents=True, exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(dir=RAIZ / "build/tests")
        self.addCleanup(self.tmp.cleanup)
        self.raiz = Path(self.tmp.name)
        self.datos = {"version": 1, "id": "ES99PT", "metadatos": {"proyecto": "EspaciGo"},
                      "secciones": ["uno.md", "dos.md"], "anexos": [],
                      "bibliografia": "referencias.bib", "plantilla": None, "perfil": None}
        (self.raiz / "uno.md").write_text("# Uno\n\nPrimer contenido.\n", encoding="utf-8")
        (self.raiz / "dos.md").write_text("# Dos\n\nSegundo contenido.\n", encoding="utf-8")
        (self.raiz / "referencias.bib").write_text("", encoding="utf-8")

    def cfg(self):
        path = self.raiz / "informe.json"
        path.write_text(json.dumps(self.datos), encoding="utf-8")
        return cargar(path)

    def texto(self, text):
        (self.raiz / "uno.md").write_text(text, encoding="utf-8")

    def test_orden_explicito(self):
        self.datos["secciones"].reverse()
        text = reunir(self.cfg())
        self.assertLess(text.index("# Dos"), text.index("# Uno"))

    def test_rutas_independientes_de_cwd(self):
        cfg = self.cfg()
        self.assertEqual(cfg.entrada("uno.md"), self.raiz / "uno.md")
        with self.assertRaises(ErrorInforme):
            cfg.entrada("../fuera.md")
        with self.assertRaises(ErrorInforme):
            cfg.salida("../fuera.docx")

    def test_no_fuentes_en_build(self):
        self.datos["secciones"] = ["build/fuente.md"]
        with self.assertRaises(ErrorInforme):
            self.cfg()

    def test_seccion_inexistente(self):
        self.datos["secciones"] = ["ausente.md"]
        self.assertTrue(any("ausente.md" in e for e in comprobar_fuentes(self.cfg())[0]))

    def test_referencia_sin_destino(self):
        self.texto("# Uno\n\nVer {{Tabla:ausente}}.")
        self.assertTrue(any("sin destino" in e for e in comprobar_fuentes(self.cfg())[0]))

    def test_etiqueta_duplicada_entre_secciones(self):
        self.texto("# Uno\n\n*Tabla. Uno* <!--#tab:repetida-->")
        (self.raiz / "dos.md").write_text("# Dos\n\n*Tabla. Dos* <!--#tab:repetida-->", encoding="utf-8")
        self.assertTrue(any("duplicado" in e for e in comprobar_fuentes(self.cfg())[0]))

    def test_cita_sin_fuente(self):
        self.texto("# Uno\n\nAfirmación [@ausente].")
        self.assertIn("Cita sin fuente: ausente", comprobar_fuentes(self.cfg())[0])

    def test_intervalo_semiabierto_no_absorbe_cita_siguiente(self):
        self.texto("# Uno\n\nIntervalo [inicio, fin) según [@fuente].")
        (self.raiz / "referencias.bib").write_text(
            "@misc{fuente, author={{Autor}}, title={Documento}, year={2026}}\n",
            encoding="utf-8")
        self.assertEqual(comprobar_fuentes(self.cfg())[0], [])

    def test_localizador_no_se_pierde_silenciosamente(self):
        self.texto("# Uno\n\nAfirmación [@fuente, p. 3].")
        self.assertTrue(any("pérdida" in e for e in comprobar_fuentes(self.cfg())[0]))

    def test_codigo_no_cuenta_como_cita(self):
        self.texto("# Uno\n\n```text\n[@ejemplo]\n```\n")
        self.assertEqual(comprobar_fuentes(self.cfg())[0], [])

    def test_pendiente_borrador_y_final(self):
        self.texto("# Uno\n\n[[PENDIENTE: evidencia]]")
        errores, avisos = comprobar_fuentes(self.cfg())
        self.assertFalse(errores)
        self.assertTrue(avisos)
        self.assertTrue(comprobar_fuentes(self.cfg(), final=True)[0])

    def test_imagen_inexistente(self):
        self.texto("# Uno\n\n![Imagen](imagenes/falta.png)")
        self.assertTrue(any("Imagen inexistente" in e for e in comprobar_fuentes(self.cfg())[0]))

    def test_anexos_duplicados(self):
        anexo = {"letra": "A", "titulo": "Prueba", "archivo": "anexo.md", "salida": "Anexo_A_Prueba.docx", "transformacion": "general"}
        self.datos["anexos"] = [anexo, dict(anexo)]
        with self.assertRaises(ErrorInforme):
            self.cfg()

    def test_transformacion_explicita(self):
        self.datos["anexos"] = [{"letra": "F", "titulo": "Prueba", "archivo": "anexo.md", "salida": "Anexo_F_Prueba.docx", "transformacion": "inventada"}]
        with self.assertRaises(ErrorInforme):
            self.cfg()

    def test_mas_de_cinco_anexos(self):
        for letra in "ABCDEF":
            (self.raiz / f"{letra}.md").write_text(f"# Anexo {letra}\nTexto", encoding="utf-8")
            self.datos["anexos"].append({"letra": letra, "titulo": "Prueba", "archivo": f"{letra}.md", "salida": f"Anexo_{letra}_Prueba.docx", "transformacion": "general"})
        cfg = self.cfg()
        self.assertEqual(len(cfg.anexos), 6)
        self.assertFalse(comprobar_fuentes(cfg)[0])

    def test_sin_plantilla_permite_ensamblado(self):
        cfg = self.cfg()
        self.assertIn("Primer contenido", reunir(cfg))
        with self.assertRaisesRegex(ErrorInforme, "pendiente"):
            perfil(cfg)

    def test_titulo_anexo_conserva_portada_multipartes_es2(self):
        anexo = {"letra": "A"}
        self.assertIsNone(titulo_portada_anexo(
            {"conservar_titulo_plantilla_en_anexos": True}, "EspaciGo", anexo))
        self.assertEqual(titulo_portada_anexo({}, "EspaciGo", anexo),
                         "PROYECTO DE TÍTULO: EspaciGo")

    def test_validar_sin_generacion_falla(self):
        self.assertTrue(validar(self.cfg())[0])

    def test_huella_detecta_cambio(self):
        cfg = self.cfg()
        antes = huella(cfg)
        self.texto("Contenido actualizado")
        self.assertNotEqual(antes, huella(cfg))

    def test_docx_corrupto(self):
        path = self.raiz / "roto.docx"
        path.write_bytes(b"no es un zip")
        self.assertTrue(inspeccionar_docx(path)[0])

    def test_es3_se_crea_sin_scripts_y_no_sobrescribe(self):
        shutil.copytree(RAIZ / "plantillas", self.raiz / "plantillas")
        with patch.object(generar, "RAIZ", self.raiz):
            creado = generar.nuevo("ES3PT")
            self.assertTrue((creado / "informe.json").is_file())
            self.assertFalse(list(creado.rglob("*.py")))
            with self.assertRaises(ErrorInforme):
                generar.nuevo("ES3PT")
            borrador = creado / "secciones/00_borrador.md"
            borrador.write_text("Trabajo del equipo", encoding="utf-8")
            generar.nuevo("ES3PT", inicializar=True)
            self.assertEqual(borrador.read_text(encoding="utf-8"), "Trabajo del equipo")


if __name__ == "__main__":
    unittest.main()
