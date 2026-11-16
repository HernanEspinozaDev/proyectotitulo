"""Recalcula metas de cobros sin modificar los insumos originales de Anita."""
from pathlib import Path
from decimal import Decimal as D, ROUND_CEILING
import argparse,csv,json
ROOT=Path(__file__).resolve().parents[1]

def calcular(sueldo=200000):
    with (ROOT/'01_extraccion/excel/03-base-mensual-valores.csv').open(encoding='utf-8-sig',newline='') as f:
        rows=list(csv.reader(f))
    valores={row[0]:D(row[1]) for row in rows if len(row)>1 and row[0] in ('Cloud GCP','FirmaVirtual/API','Marketing','Contabilidad','Dominio','Viajes coordinación')}
    aws=json.loads((ROOT/'02_contraste/parametros_aws.json').read_text())
    ingresos=json.loads((ROOT/'02_contraste/parametros_ingresos.json').read_text())
    tasa=D(ingresos['tarifa_indicada_usuario'])
    otros=sum(valores.values())-valores['Cloud GCP']+D(aws['clp_mensuales'])
    remuneraciones=D(sueldo)*3
    total=otros+remuneraciones
    def meta(costo,ticket):
        n=int((costo/(D(ticket)*tasa)).to_integral_value(rounding=ROUND_CEILING))
        return {'ticket_medio_clp':ticket,'comision_neta_por_pago_clp':str(D(ticket)*tasa),'pagos_mes':n,'gmv_redondeado_clp':n*ticket,'comision_neta_redondeada_clp':str(D(n)*D(ticket)*tasa)}
    metas=[meta(total,t) for t in (20000,50000,100000,200000)]
    base=meta(total,50000)
    # Verifica mínimo entero: el pago inmediatamente anterior no cubre el objetivo.
    for m in metas:
        unit=D(m['comision_neta_por_pago_clp'])
        assert unit*m['pagos_mes']>=total>unit*(m['pagos_mes']-1)
    return {'estado':'escenario de planificación parcial; no punto de equilibrio definitivo','fundadores':3,'meta_por_fundador_clp':sueldo,'meta_total_fundadores_clp':str(remuneraciones),'comision_neta':str(tasa),'costos_fuente_sin_fundadores_con_gcp_clp':str(sum(valores.values())),'gcp_retirado_clp':str(valores['Cloud GCP']),'aws_bruto_mensual_clp':aws['clp_mensuales'],'costos_parciales_sin_fundadores_aws_clp':str(otros),'costo_parcial_con_meta_fundadores_clp':str(total),'gmv_minimo_teorico_clp':str(total/tasa),'metas_por_ticket':metas,'solo_meta_fundadores_ticket_50000':meta(remuneraciones,50000),'solo_costos_parciales_ticket_50000':meta(otros,50000),'aws_y_meta_fundadores_ticket_50000':meta(D(aws['clp_mensuales'])+remuneraciones,50000),'espacios_equivalentes_a_dos_pagos_mes':int((D(base['pagos_mes'])/2).to_integral_value(rounding=ROUND_CEILING)),'brecha_sobre_16_pagos_mes':base['pagos_mes']-16,'faltante_mensual_con_16_pagos_clp':str(total-D(800000)*tasa),'componentes_fuente_clp':{k:str(v) for k,v in valores.items()},'exclusiones':['oficina y otros costos fijos sin validar','costos variables propios y crecimiento de infraestructura','costos legales, tributarios y de contratación','capital de trabajo, inversión y servicio de deuda','cancelaciones y devoluciones'],'pasarela':'a cargo del publicador; se supone íntegramente descontada de su liquidación, sin costo residual para espaciGo; pendiente validar tarifa e implementación','iva':'separado de comisión neta; excluido del ingreso para financiar remuneraciones','creditos_aws':'excluidos del umbral recurrente para evitar depender de beneficios temporales'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--sueldo-objetivo',type=int,default=200000);parser.add_argument('--guardar',action='store_true');a=parser.parse_args()
    if a.sueldo_objetivo<=0:parser.error('El sueldo objetivo debe ser mayor que cero.')
    result=calcular(a.sueldo_objetivo)
    if a.guardar:
        (ROOT/'02_contraste/umbrales_remuneraciones.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
