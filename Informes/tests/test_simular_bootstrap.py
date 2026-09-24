"""Pruebas de caja, IVA y financiación; no ejecutan Word."""
import copy
import json
from pathlib import Path
import unittest

from Informes.herramientas.simular_bootstrap import escenarios, infraestructura, simular


class BootstrapTests(unittest.TestCase):
    def setUp(self):
        ruta = Path(__file__).parents[1] / "ES2PT/investigacion/supuestos_bootstrap.json"
        self.datos = json.loads(ruta.read_text(encoding="utf-8"))

    def test_presupuesto_infraestructura(self):
        p = infraestructura(self.datos, "piloto")
        self.assertAlmostEqual(p["partidas_usd"]["sql_cpu"], 2*730*.05782)
        self.assertAlmostEqual(p["caja_con_iva"], 283004.85585399996)

    def test_region_santiago_sin_provision_regional(self):
        self.assertTrue(self.datos["infraestructura"]["region_tarifas"].startswith("southamerica-west1"))
        self.assertEqual(self.datos["factor_prevision_regional"], 1.0)

    def test_sin_ventas_no_hay_sueldo_ni_devolucion_ficticia(self):
        r = simular(self.datos)
        a = r["anos"][0]
        self.assertEqual((a["ingresos"], a["sueldos"], a["idpc"]), (0,0,0))
        self.assertAlmostEqual(a["trabajo"], 43200000)
        self.assertGreater(a["remanente_iva"], 0)
        self.assertAlmostEqual(r["deficit_ano1"], 4815742.570978)

    def test_cobro_pasarela_no_es_solo_sobre_comision(self):
        d = copy.deepcopy(self.datos)
        d["reservas"][0] = 1
        f = simular(d)["meses"][0]
        self.assertEqual(f["ingreso_neto"], 12000)
        self.assertEqual(f["cobro_terceros"], 100000)
        self.assertAlmostEqual(f["pasarela_neta"], (100000+12000*1.19)*.0319)

    def test_ppm_no_duplica_idpc_y_fondo_no_es_ingreso(self):
        r = simular(self.datos)
        a = r["anos"][2]
        ajustes = sum(f["ajuste_idpc"] for f in r["meses"][24:])
        self.assertAlmostEqual(a["ppm"]+ajustes, a["idpc"])
        self.assertAlmostEqual(r["aporte_por_fundador"]*3, r["fondo_ano1_con_colchon"])
        self.assertGreater(r["deficit_maximo_36_meses"], r["fondo_ano1_con_colchon"])

    def test_reconciliacion_caja_y_oportunidad(self):
        r = simular(self.datos)
        self.assertAlmostEqual(sum(r["flujos_caja"]), r["meses"][-1]["saldo_sin_aportes"])
        for a, fc, fe in zip(r["anos"],r["flujos_caja"][1:],r["flujos_economicos"][1:]):
            self.assertAlmostEqual(fc-fe,a["costo_no_pagado"])
        self.assertLess(r["van_caja"], 0)
        self.assertLess(r["van_economico"], r["van_caja"])

    def test_calendario_invalido(self):
        self.datos["reservas"].pop()
        with self.assertRaises(ValueError):
            simular(self.datos)

    def test_ticket_bajo_no_se_vuelve_rentable_por_mas_reservas(self):
        r = escenarios(self.datos)
        bajo = r["ticket_30000"]
        base = r["base_sin_ventas_ano1"]
        alto = r["ticket_150000"]
        self.assertEqual(bajo["anos"][0]["reservas"], 0)
        self.assertEqual(bajo["anos"][2]["reservas"], base["anos"][2]["reservas"])
        self.assertLess(bajo["anos"][2]["ingresos"] - bajo["anos"][2]["variables"], 0)
        self.assertLess(bajo["van_caja"], base["van_caja"])
        self.assertGreater(alto["van_caja"], base["van_caja"])

    def test_un_segmento_reproduce_el_agregado_historico(self):
        original = simular(self.datos)
        d = copy.deepcopy(self.datos)
        cantidades = d.pop("reservas")
        d["segmentos"] = [dict(id="espacios_de_prueba", reservas=cantidades,
                               arriendo_final_base=d["arriendo_final_base"],
                               comision_neta=d["comision_neta"],
                               firmas_por_reserva=d["firmas_por_reserva"],
                               kyc_neto_por_reserva=d["kyc_neto_por_reserva"],
                               otros_variables_netos=d["otros_variables_netos"])]
        separado = simular(d)
        self.assertAlmostEqual(separado["van_caja"], original["van_caja"])
        self.assertAlmostEqual(separado["deficit_maximo_36_meses"],
                               original["deficit_maximo_36_meses"])
        self.assertEqual(separado["anos"][2]["reservas"], 1800)

    def test_dos_tipos_suman_ventas_y_preservan_detalle(self):
        d = copy.deepcopy(self.datos)
        cantidades = d.pop("reservas")
        comun = dict(comision_neta=.12, firmas_por_reserva=2,
                     kyc_neto_por_reserva=500, otros_variables_netos=500)
        d["segmentos"] = [
            dict(id="sala", reservas=[q/2 for q in cantidades],
                 arriendo_final_base=150000, **comun),
            dict(id="bodega", reservas=[q/2 for q in cantidades],
                 arriendo_final_base=50000, **comun),
        ]
        f = simular(d)["meses"][12]
        self.assertEqual(f["reservas"], 20)
        self.assertEqual(f["ingreso_neto"], 240000 * 1.04)
        self.assertEqual(f["cobro_terceros"], 2000000 * 1.04)
        self.assertEqual([s["id"] for s in f["detalle_segmentos"]], ["sala", "bodega"])

    def test_sensibilidad_segmentada_mueve_demanda_y_precios(self):
        d = copy.deepcopy(self.datos)
        cantidades = d.pop("reservas")
        d["segmentos"] = [dict(id="sala", reservas=cantidades,
                               arriendo_final_base=100000, comision_neta=.12,
                               firmas_por_reserva=2, kyc_neto_por_reserva=500,
                               otros_variables_netos=500)]
        resultados = escenarios(d)
        base = resultados["base_sin_ventas_ano1"]["anos"][2]
        self.assertEqual(resultados["demanda_mitad"]["anos"][2]["reservas"],
                         base["reservas"] / 2)
        self.assertEqual(resultados["ticket_mitad"]["anos"][2]["ingresos"],
                         base["ingresos"] / 2)

    def test_segmentos_sin_ticket_o_con_id_duplicado_fallan(self):
        d = copy.deepcopy(self.datos)
        cantidades = d.pop("reservas")
        s = dict(id="sala", reservas=cantidades, arriendo_final_base=None,
                 comision_neta=.12, firmas_por_reserva=2,
                 kyc_neto_por_reserva=500, otros_variables_netos=500)
        d["segmentos"] = [s]
        with self.assertRaisesRegex(ValueError, "arriendo_final_base"):
            simular(d)
        s["arriendo_final_base"] = 100000
        d["segmentos"].append(copy.deepcopy(s))
        with self.assertRaisesRegex(ValueError, "id único"):
            simular(d)


if __name__ == "__main__":
    unittest.main()
