"""Comprobaciones numéricas aisladas; no utilizan Word ni archivos de ES1."""
import copy
import json
from pathlib import Path
import unittest

from Informes.herramientas.evaluacion_economica import evaluar, escenarios, tir, van


class EvaluacionEconomicaTests(unittest.TestCase):
    def setUp(self):
        ruta = Path(__file__).parents[1] / "ES2PT/investigacion/supuestos_economicos.json"
        self.datos = json.loads(ruta.read_text(encoding="utf-8"))

    def test_caso_con_solucion_conocida(self):
        self.assertAlmostEqual(van(.1, [-100, 110]), 0)
        self.assertAlmostEqual(tir([-100, 110]), .1)
        self.assertAlmostEqual(tir([-100, 90]), -.1)
        self.assertIsNone(tir([-100, 230, -132]))

    def test_flujo_e_impuesto_del_ejemplo(self):
        resultado = evaluar(self.datos)
        self.assertAlmostEqual(resultado["inversion_total"], 18000000)
        self.assertAlmostEqual(resultado["anos"][0]["impuesto"], 2592000)
        self.assertAlmostEqual(resultado["flujos"][1], 6912000)
        self.assertAlmostEqual(resultado["flujos"][3], 10175692.8)
        self.assertAlmostEqual(van(resultado["tir"], resultado["flujos"]), 0, places=6)

    def test_perdidas_no_generan_devolucion_y_precio_no_cambia(self):
        casos = escenarios(self.datos)
        self.assertEqual(casos["base"]["precio_base"], casos["demanda_menos_20"]["precio_base"])
        d = copy.deepcopy(self.datos)
        d["unidades_anuales"] = [0, 0, 0]
        self.assertTrue(all(f["impuesto"] == 0 for f in evaluar(d)["anos"]))

    def test_recuperacion_no_se_duplica(self):
        casos = escenarios(self.datos)
        base, sin = casos["base"], casos["sin_recuperacion_ct_ni_continuidad"]
        self.assertAlmostEqual(base["flujos"][-1] - sin["flujos"][-1], 2595840)
        self.assertAlmostEqual(base["anos"][0]["incremento_capital_trabajo"], 96000)

    def test_entrada_invalida(self):
        self.datos["margen_sobre_ventas"] = 1
        with self.assertRaises(ValueError):
            evaluar(self.datos)


if __name__ == "__main__":
    unittest.main()
