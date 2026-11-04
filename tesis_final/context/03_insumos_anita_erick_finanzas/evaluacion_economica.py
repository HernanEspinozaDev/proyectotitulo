"""Modelo académico sin deuda: CLP nominales, impuesto simplificado y flujos anuales.

No genera Word ni determina la renta líquida imponible legal. Las entradas conservan
las fuentes y supuestos en el JSON; la documentación explica sus limitaciones.
"""
import argparse
import copy
import json
import math
from pathlib import Path


def van(tasa, flujos):
    if tasa <= -1:
        raise ValueError("La tasa debe ser mayor que -100 %")
    return sum(flujo / (1 + tasa) ** periodo for periodo, flujo in enumerate(flujos))


def tir(flujos):
    """Bisección para inversión inicial negativa y una sola variación de signo."""
    signos = [1 if x > 0 else -1 for x in flujos if x]
    cambios = sum(a != b for a, b in zip(signos, signos[1:]))
    if not signos or signos[0] != -1 or cambios != 1:
        return None
    inferior, superior = -0.999, 1.0
    for _ in range(60):
        if van(superior, flujos) < 0:
            break
        superior = 2 * superior + 1
    else:
        return None
    if van(inferior, flujos) <= 0:
        return None
    for _ in range(160):
        medio = (inferior + superior) / 2
        if van(medio, flujos) > 0:
            inferior = medio
        else:
            superior = medio
    return (inferior + superior) / 2


def evaluar(datos):
    d = datos
    cantidades = d["unidades_anuales"]
    if not cantidades or any(not math.isfinite(q) or q < 0 for q in cantidades):
        raise ValueError("Se requiere al menos un año y cantidades no negativas")
    if not 0 <= d["margen_sobre_ventas"] < 1 or d["unidades_referencia"] <= 0:
        raise ValueError("Margen o unidades de referencia inválidos")
    if not 0 <= d["impuesto"] <= 1 or d["meses_capital_trabajo"] < 0:
        raise ValueError("Impuesto o capital de trabajo inválidos")
    for campo in ("ipc_costos", "reajuste_precio", "tasa_descuento_nominal"):
        if not math.isfinite(d[campo]) or d[campo] <= -1:
            raise ValueError(f"Tasa inválida: {campo}")
    grupos = ("costos_fijos_anuales", "costos_variables_unitarios", "inversion_inicial")
    for grupo in grupos:
        if any(not math.isfinite(x["clp"]) or x["clp"] < 0 for x in d[grupo]):
            raise ValueError(f"Monto inválido en {grupo}")
    n = len(cantidades)
    for campo in ("depreciacion_anual", "reinversion_anual"):
        if len(d[campo]) != n or any(not math.isfinite(x) or x < 0 for x in d[campo]):
            raise ValueError(f"Debe existir un monto no negativo por año: {campo}")
    fijo = sum(x["clp"] for x in d["costos_fijos_anuales"])
    variable = sum(x["clp"] for x in d["costos_variables_unitarios"])
    inversion = sum(x["clp"] for x in d["inversion_inicial"])
    precio = (fijo / d["unidades_referencia"] + variable) / (1 - d["margen_sobre_ventas"])
    filas = []
    for i, unidades in enumerate(cantidades):
        factor = (1 + d["ipc_costos"]) ** i
        p = precio * (1 + d["reajuste_precio"]) ** i
        cf, cv = fijo * factor, variable * factor
        ingreso, costo_variable = unidades * p, unidades * cv
        contribucion = ingreso - costo_variable
        ebitda = contribucion - cf
        depreciacion = d["depreciacion_anual"][i]
        ebit = ebitda - depreciacion
        impuesto = max(0, ebit) * d["impuesto"]
        filas.append(dict(ano=i + 1, unidades=unidades, precio=p, costo_variable_unitario=cv,
                          ingresos=ingreso, costos_variables=costo_variable, costos_fijos=cf,
                          contribucion=contribucion, ebitda=ebitda, depreciacion=depreciacion,
                          utilidad_antes_impuesto=ebit, impuesto=impuesto,
                          utilidad_neta=ebit - impuesto,
                          capital_trabajo=(cf + costo_variable) * d["meses_capital_trabajo"] / 12))
    ct0 = filas[0]["capital_trabajo"]
    flujos = [-inversion - ct0]
    for i, fila in enumerate(filas):
        ultimo = i == n - 1
        aumento_ct = 0 if ultimo else filas[i + 1]["capital_trabajo"] - fila["capital_trabajo"]
        recuperacion = fila["capital_trabajo"] if ultimo and d["recuperar_capital_trabajo"] else 0
        residual = d["valor_residual_neto"] if ultimo else 0
        fila.update(incremento_capital_trabajo=aumento_ct, recuperacion_capital_trabajo=recuperacion,
                    reinversion=d["reinversion_anual"][i], residual_neto=residual)
        flujo = (fila["utilidad_neta"] + fila["depreciacion"] - aumento_ct
                 - fila["reinversion"] + recuperacion + residual)
        fila["flujo_neto"] = flujo
        flujos.append(flujo)
    return dict(precio_base=precio, inversion_sin_ct=inversion, capital_trabajo_inicial=ct0,
                inversion_total=-flujos[0], anos=filas, flujos=flujos,
                van=van(d["tasa_descuento_nominal"], flujos), tir=tir(flujos),
                equilibrio_operativo_unidades=fijo / (precio - variable) if precio > variable else None)


def escenarios(datos):
    casos = {}
    for nombre, factor in (("base", 1), ("demanda_menos_20", .8), ("demanda_mas_20", 1.2)):
        d = copy.deepcopy(datos)
        d["unidades_anuales"] = [q * factor for q in d["unidades_anuales"]]
        casos[nombre] = evaluar(d)
    d = copy.deepcopy(datos)
    d["reajuste_precio"] = 0
    casos["sin_reajustar_comision"] = evaluar(d)
    d = copy.deepcopy(datos)
    d["recuperar_capital_trabajo"] = False
    casos["sin_recuperacion_ct_ni_continuidad"] = evaluar(d)
    d = copy.deepcopy(datos)
    d["costos_fijos_anuales"] = [dict(x, clp=x["clp"] * 1.1) for x in d["costos_fijos_anuales"]]
    # Conservar la comisión original al subir costos; no restaurar el margen automáticamente.
    fijo = sum(x["clp"] for x in d["costos_fijos_anuales"])
    variable = sum(x["clp"] for x in d["costos_variables_unitarios"])
    d["margen_sobre_ventas"] = 1 - (fijo / d["unidades_referencia"] + variable) / casos["base"]["precio_base"]
    casos["costos_fijos_mas_10"] = evaluar(d)
    return casos


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("supuestos", type=Path)
    parser.add_argument("--salida", type=Path)
    args = parser.parse_args()
    try:
        datos = json.loads(args.supuestos.read_text(encoding="utf-8-sig"))
        salida = json.dumps(escenarios(datos), ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    except (OSError, ValueError, KeyError, TypeError, OverflowError) as exc:
        parser.exit(1, f"Error de evaluación: {exc}\n")
    if args.salida:
        args.salida.parent.mkdir(parents=True, exist_ok=True)
        args.salida.write_text(salida, encoding="utf-8")
        print(args.salida)
    else:
        print(salida, end="")


if __name__ == "__main__":
    main()
