"""Presupuesto mensual de caja y costo de oportunidad; no genera Word ni trámites."""
import argparse
import copy
import json
import math
from pathlib import Path

try:
    from .evaluacion_economica import tir, van
except ImportError:
    from evaluacion_economica import tir, van


def infraestructura(d, perfil):
    partidas = {p["id"]: p[perfil] * p["tarifa_usd"] for p in d["infraestructura"]["partidas"]}
    usd = sum(partidas.values())
    neto = usd * d["usd_clp"] * d["factor_prevision_regional"]
    return dict(partidas_usd=partidas, usd_referencia=usd, neto_clp=neto,
                caja_con_iva=neto * (1 + d["iva"]))


def suma_partidas(partidas, factor, tasa):
    neto = sum(p["neto"] for p in partidas) * factor
    iva = sum(p["neto"] for p in partidas if p["iva"]) * factor * tasa
    return neto, iva


def _segmentos(d):
    """Devuelve segmentos económicos; conserva el ejemplo agregado anterior."""
    if "segmentos" not in d:
        if len(d["reservas"]) != 36 or any(
                not isinstance(q, (int, float)) or not math.isfinite(q) or q < 0
                for q in d["reservas"]):
            raise ValueError("Se requieren 36 cantidades mensuales no negativas")
        return [dict(id="agregado_provisional", reservas=d["reservas"],
                     arriendo_final_base=d["arriendo_final_base"],
                     comision_neta=d["comision_neta"],
                     firmas_por_reserva=d["firmas_por_reserva"],
                     kyc_neto_por_reserva=d["kyc_neto_por_reserva"],
                     otros_variables_netos=d["otros_variables_netos"])]
    segmentos = d["segmentos"]
    if not isinstance(segmentos, list) or not segmentos or "reservas" in d:
        raise ValueError("La modalidad segmentada exige una lista no vacía y sin reservas agregadas")
    ids = set()
    for s in segmentos:
        clave = s.get("id")
        if not isinstance(clave, str) or not clave or clave in ids:
            raise ValueError("Cada segmento necesita un id único")
        ids.add(clave)
        cantidades = s.get("reservas")
        if not isinstance(cantidades, list) or len(cantidades) != 36 or any(
                not isinstance(q, (int, float)) or not math.isfinite(q) or q < 0
                for q in cantidades):
            raise ValueError(f"{clave}: se requieren 36 cantidades mensuales no negativas")
        for campo in ("arriendo_final_base", "comision_neta", "firmas_por_reserva",
                      "kyc_neto_por_reserva", "otros_variables_netos"):
            valor = s.get(campo)
            if not isinstance(valor, (int, float)) or not math.isfinite(valor) or valor < 0:
                raise ValueError(f"{clave}: {campo} debe ser un número no negativo")
        if s["arriendo_final_base"] == 0 or not 0 < s["comision_neta"] < 1:
            raise ValueError(f"{clave}: arriendo y comisión deben ser positivos")
    return segmentos


def simular(d):
    segmentos = _segmentos(d)
    if d["fundadores"] <= 0 or d["usd_clp"] <= 0 or (
            "segmentos" not in d and not 0 < d["comision_neta"] < 1):
        raise ValueError("Fundadores, dólar o comisión inválidos")
    perfiles = []
    for ano in d["infraestructura"]["perfil_por_ano"]:
        if len(ano) % 2:
            raise ValueError("Perfil anual incompleto")
        bloque = []
        for i in range(0, len(ano), 2):
            bloque += [ano[i]] * ano[i + 1]
        if len(bloque) != 12:
            raise ValueError("Cada año debe tener 12 meses de infraestructura")
        perfiles += bloque
    iva = d["iva"]
    inicial, credito_iva = suma_partidas(d["inicio"], 1, iva)
    caja_inicial = inicial + credito_iva
    saldo, deficit = -caja_inicial, caja_inicial
    meses, anos = [], []
    for y in range(3):
        factor = (1 + d["ipc_clp"]) ** y
        filas = []
        for m in range(12):
            indice = y * 12 + m
            detalle = []
            for s in segmentos:
                q_s = s["reservas"][indice]
                ticket_s = s["arriendo_final_base"] * factor
                precio_s = ticket_s * s["comision_neta"]
                ingreso_s = q_s * precio_s
                cobro_s = q_s * (ticket_s + precio_s * (1 + iva))
                pasarela_s = cobro_s * d["pasarela_sobre_cobro"]
                otros_s = q_s * factor * (s["firmas_por_reserva"] * d["firma_neta_unitaria"]
                                         + s["kyc_neto_por_reserva"] + s["otros_variables_netos"])
                detalle.append(dict(id=s["id"], reservas=q_s, arriendo_final_unitario=ticket_s,
                                    ingreso_neto=ingreso_s, cobro_terceros=q_s * ticket_s,
                                    pasarela_neta=pasarela_s, otros_variables=otros_s,
                                    contribucion=ingreso_s - pasarela_s - otros_s))
            q = sum(s["reservas"] for s in detalle)
            ingreso = sum(s["ingreso_neto"] for s in detalle)
            pasarela = sum(s["pasarela_neta"] for s in detalle)
            otros = sum(s["otros_variables"] for s in detalle)
            cv = pasarela + otros
            seleccion = [p for p in d["mensual"] if indice + 1 >= p["desde"]]
            seleccion += [p for p in d["anual"] if p["mes"] == m + 1]
            fijo, iva_fijo = suma_partidas(seleccion, factor, iva)
            infra = infraestructura(d, perfiles[indice])["neto_clp"]
            sueldo = d["sueldos_totales_mensuales"][y] * factor
            costos = fijo + infra + cv + sueldo
            iva_compra = iva_fijo + (infra + cv) * iva
            iva_debito = ingreso * iva
            disponible = credito_iva + iva_compra
            pago_iva = max(0, iva_debito - disponible)
            credito_iva = max(0, disponible - iva_debito)
            ppm = ingreso * d["ppm_provision"]
            caja = ingreso + iva_debito - costos - iva_compra - pago_iva - ppm
            horas = d["fundadores"] * d["horas_semanales_por_fundador"][y] * d["semanas_por_ano"] / 12
            oportunidad = horas * d["valor_hora_base"] * factor
            filas.append(dict(mes=indice + 1, perfil=perfiles[indice], reservas=q,
                              detalle_segmentos=detalle, ingreso_neto=ingreso,
                              cobro_terceros=sum(s["cobro_terceros"] for s in detalle),
                              pasarela_neta=pasarela, otros_variables=otros, costo_variable=cv,
                              fijo_neto=fijo + infra, sueldo_pagado=sueldo, costo_neto=costos,
                              iva_credito_mes=iva_compra, iva_debito=iva_debito, iva_pagado=pago_iva,
                              remanente_iva=credito_iva, ppm=ppm, ajuste_idpc=0,
                              flujo_caja=caja, trabajo_valorizado=oportunidad,
                              costo_no_pagado=max(0, oportunidad - sueldo)))
        resultado = sum(f["ingreso_neto"] - f["costo_neto"] for f in filas) - (inicial if y == 0 else 0)
        impuesto = max(0, resultado) * d["idpc_academico"]
        anticipos = sum(f["ppm"] for f in filas)
        ajuste = max(0, impuesto - anticipos)
        filas[-1]["ajuste_idpc"] = ajuste
        filas[-1]["flujo_caja"] -= ajuste
        for f in filas:
            saldo += f["flujo_caja"]
            deficit = max(deficit, -saldo)
            f["saldo_sin_aportes"] = saldo
            meses.append(f)
        sumar = lambda campo: sum(f[campo] for f in filas)
        anos.append(dict(ano=y + 1, reservas=sumar("reservas"), ingresos=sumar("ingreso_neto"),
                         variables=sumar("costo_variable"), fijos=sumar("fijo_neto"),
                         sueldos=sumar("sueldo_pagado"), resultado_tributario_modelado=resultado,
                         idpc=impuesto, ppm=anticipos, ppm_sin_recuperar=max(0, anticipos-impuesto),
                         iva_pagado=sumar("iva_pagado"), remanente_iva=credito_iva,
                         caja_operativa=sumar("flujo_caja"), trabajo=sumar("trabajo_valorizado"),
                         costo_no_pagado=sumar("costo_no_pagado")))
    flujos = [-caja_inicial] + [a["caja_operativa"] for a in anos]
    economicos = [-caja_inicial] + [a["caja_operativa"] - a["costo_no_pagado"] for a in anos]
    deficit_ano1 = max(caja_inicial, -min(f["saldo_sin_aportes"] for f in meses[:12]))
    fondo = deficit_ano1 * (1 + d["colchon_caja"])
    return dict(infraestructura={p: infraestructura(d, p) for p in ("ensayo", "piloto", "ha")},
                gasto_inicial_neto=inicial, caja_inicial=caja_inicial, meses=meses, anos=anos,
                flujos_caja=flujos, van_caja=van(d["descuento_nominal"], flujos), tir_caja=tir(flujos),
                flujos_economicos=economicos, van_economico=van(d["descuento_nominal"], economicos),
                tir_economica=tir(economicos), deficit_maximo_36_meses=deficit,
                deficit_ano1=deficit_ano1, fondo_ano1_con_colchon=fondo,
                aporte_por_fundador=fondo/d["fundadores"],
                complemento_sobre_capital=max(0, fondo-d["capital_social_propuesto"]))


def escenarios(d):
    salida = {"base_sin_ventas_ano1": simular(d)}
    cambios = [
        ("usd_1100", {"usd_clp": 1100}),
        ("sueldos_ano3", {"sueldos_totales_mensuales": [0,0,1800000]}),
        ("idpc_12_5_estatico", {"idpc_academico": .125}),
        ("piloto_12_meses_ano1", {"infraestructura": {**d["infraestructura"], "perfil_por_ano": [["piloto",12]]*3}}),
    ]
    if "segmentos" in d:
        mitad = copy.deepcopy(d["segmentos"])
        for s in mitad:
            s["reservas"] = [q * .5 for q in s["reservas"]]
        cambios.append(("demanda_mitad", {"segmentos": mitad}))
        for nombre, multiplicador in (("ticket_mitad", .5), ("ticket_1_5", 1.5)):
            mezcla = copy.deepcopy(d["segmentos"])
            for s in mezcla:
                s["arriendo_final_base"] *= multiplicador
            cambios.append((nombre, {"segmentos": mezcla}))
    else:
        cambios.extend([
            ("piloto_ventas_mes7", {"reservas": [0]*6 + [5,10,15,20,25,30] + d["reservas"][12:]}),
            ("demanda_mitad", {"reservas": [q*.5 for q in d["reservas"]]}),
            ("ticket_30000", {"arriendo_final_base": 30000}),
            ("ticket_50000", {"arriendo_final_base": 50000}),
            ("ticket_150000", {"arriendo_final_base": 150000}),
        ])
    cambios.append(("firma_2500", {"firma_neta_unitaria": 2500}))
    for nombre, cambio in cambios:
        copia = copy.deepcopy(d)
        copia.update(cambio)
        salida[nombre] = simular(copia)
    return salida


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("entrada", type=Path)
    p.add_argument("--salida", type=Path, required=True)
    args = p.parse_args()
    d = json.loads(args.entrada.read_text(encoding="utf-8-sig"))
    r = escenarios(d)
    args.salida.parent.mkdir(parents=True, exist_ok=True)
    args.salida.write_text(json.dumps(r, ensure_ascii=False, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(args.salida)


if __name__ == "__main__":
    main()
