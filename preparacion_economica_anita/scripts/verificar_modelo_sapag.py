"""Verificaciones financieras independientes del primer corte de ejecución."""
from pathlib import Path
from decimal import Decimal as D
import json,sys,copy
import math
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from ejecutar_modelo_sapag import amortizacion,impuesto_perdidas,cargar_costos,construir_proyeccion
from calcular_tickets_remuneraciones import calcular

def main():
    model=json.loads((ROOT/'04_modelo_sapag/resultados_proyeccion.json').read_text())
    costos=cargar_costos()
    # Fuente identificada: 5.860.950 CLP no cloud + 26,41 USD × 972 × 12.
    annual=sum(x['anual_1_clp'] for x in costos)
    assert annual==D('5860950')+D('26.41')*D('972')*12==D('6168996.24')
    assert len({x['id'] for x in costos})==8
    loan=amortizacion(3720000,'.12',3)
    assert sum(x['amortizacion_clp'] for x in loan)==D('3720000')
    assert loan[-1]['saldo_final_clp']==0 and loan[-1]['ajuste_ultima_cuota_clp']==1
    assert all(x['saldo_inicial_clp']-x['amortizacion_clp']==x['saldo_final_clp'] and x['interes_clp']+x['amortizacion_clp']==x['cuota_clp'] for x in loan)
    tax=impuesto_perdidas(1232610,956400,'.27')
    assert tax['base_academica_clp']==D(276210) and tax['impuesto_clp']==D('74576.70')
    loss=impuesto_perdidas(-500,100,'.27');assert loss['impuesto_clp']==0 and loss['perdidas_finales_clp']==600
    for key,m in model.items():
        assert len(m['mensual'])==48 and len(m['anual'])==4
        monthly=m['mensual']
        balance=D(m['flujo_anual'][0])
        for row in monthly:
            balance+=D(row['flujo_parcial_clp'])
            assert balance==D(row['caja_acumulada_sin_aportes_adicionales_clp'])
        assert balance==sum(D(v) for v in m['flujo_anual'])
        assert len({x['fecha'] for x in monthly})==48
        for i,a in enumerate(m['anual']):
            subset=monthly[i*12:(i+1)*12]
            assert sum(D(x['comision_neta_clp']) for x in subset)==D(a['comision_neta_clp'])==D('288000')
            assert sum(D(x['flujo_parcial_clp']) for x in subset)==D(a['flujo_parcial_clp'])
        for x in monthly:
            assert D(x['comision_neta_clp'])==D(x['gmv_clp'])*D('.03')
            assert D(x['saldo_publicadores_antes_pasarela_clp'])+D(x['comision_neta_clp'])+D(x['iva_comision_restringido_clp'])==D(x['gmv_clp'])
            assert x['tarifa_pasarela'] is None and x['abono_final_publicadores_clp'] is None
            assert x['costos_pendientes_adicionales'] is None
        independent=math.fsum(float(x)*math.pow(1.12,-i) for i,x in enumerate(m['flujo_anual']))
        assert abs(independent-float(m['van_parcial_12_clp']))<.01
    pure=model['condicionada_puro'];fin=model['condicionada_financiado']
    assert D(pure['flujo_anual'][0])==D('-1200000')
    assert D(fin['flujo_anual'][0])==D('2520000')
    assert all(D(a['pago_fundadores_modelado_clp'])==0 for a in pure['anual'])
    assert abs(D(pure['van_parcial_12_clp'])-D(fin['van_parcial_12_clp']))<1
    assert pure['capital_trabajo_ciclo_clp'] is None and pure['valor_cierre_clp'] is None
    assert next(x for x in calcular(200000)['metas_por_ticket'] if x['ticket_medio_clp']==50000)['pagos_mes']==743
    assert next(x for x in calcular(1000000)['metas_por_ticket'] if x['ticket_medio_clp']==50000)['pagos_mes']==2343
    params=json.loads((ROOT/'04_modelo_sapag/parametros_ejecucion.json').read_text())
    higher=copy.deepcopy(params)
    higher['costos']['marketing_presupuesto_base_mensual_clp']='450000'
    changed=construir_proyeccion(higher,cargar_costos(higher))
    assert changed['anual'][0]['opex_identificado_clp']-D(pure['anual'][0]['opex_identificado_clp'])==D('1200000')
    assert changed['van_parcial_12_clp']<D(pure['van_parcial_12_clp'])
    below=construir_proyeccion(params,costos,pagos_mes=742)
    above=construir_proyeccion(params,costos,pagos_mes=743)
    assert below['anual'][0]['pago_fundadores_modelado_clp']==0
    assert above['anual'][0]['pago_fundadores_modelado_clp']==D('7200000')
    print('Fuentes, 48 meses por perfil, agregación anual, caja, fondos de terceros, deuda a cero, pérdidas, VAN independiente, cambio de presupuesto y umbral de pago verificados.')

if __name__=='__main__':main()
