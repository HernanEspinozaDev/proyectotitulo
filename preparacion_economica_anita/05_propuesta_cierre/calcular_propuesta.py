"""Propuestas para cerrar entradas: no sobrescribe el escenario activo."""
from pathlib import Path
from decimal import Decimal as D,ROUND_HALF_UP
import csv,json
ROOT=Path(__file__).resolve().parents[1];OUT=Path(__file__).resolve().parent

def main():
 q=lambda x:x.quantize(D('.01'),rounding=ROUND_HALF_UP)
 # Hipótesis propuestas: NIC directo; anualidades en enero; comisión a siete días.
 costs=json.loads((ROOT/'04_modelo_sapag/costos_conciliados.json').read_text())['partidas']
 current=sum(D(c['mensual_1_clp']) for c in costs)
 proposed=current-D('10950')/12+D('9990')/12
 monthly=proposed-D('9990')/12-D('150000')/12
 netfee=D('24000');lag=D(7);receivable=netfee*lag/30
 rows=[];cum=-D('1200000')
 for m in range(1,13):
  opex=monthly+(D('159990') if m==1 else D(0))
  received=netfee-receivable if m==1 else netfee
  flow=received-opex;cum+=flow
  rows.append(dict(mes=f'2027-{m:02}',egresos_identificados_propuestos_clp=q(opex),comision_neta_devengada_clp=netfee,comision_neta_cobrada_supuesto_clp=q(received),cuenta_por_cobrar_clp=receivable,flujo_parcial_supuesto_clp=q(flow),caja_sin_aportes_clp=q(cum)))
 results=dict(estado='propuesta no adoptada; no modifica parámetros vigentes',
  dominio_tarifa_publicada_clp=9990,dominio_presupuesto_previo_clp=10950,
  subtotal_mensual_prorrateado_propuesto_clp=q(proposed),presupuesto_anual_identificado_propuesto_clp=q(proposed*12),
  lag_dias_propuesto=7,lag_estres_dias=30,comision_por_cobrar_supuesto_clp=receivable,
  caja_bruta_para_lanzamiento_y_primer_trimestre_sin_ventas_clp=q(D('1200000')+sum(r['egresos_identificados_propuestos_clp'] for r in rows[:3])),
  necesidad_parcial_acumulada_primer_trimestre_con_referencia_16_pagos_clp=-rows[2]['caja_sin_aportes_clp'],
  horas_totales_valorizacion_fuente=960,tarifa_hora_fuente_clp=6500,valor_desarrollo_fuente_clp=960*6500,
  capacidad_seis_semanas_horas=6*20*3,valor_capacidad_seis_semanas_clp=6*20*3*6500,
  advertencia_capacidad='capacidad propuesta, no backlog estimado ni evidencia de horas ya realizadas',
  reposicion_estres_referencia_clp=900000,precio_fuente_notebook_clp=800000,referencia_reajustada_tres_anios_clp=q(D('800000')*D('1.04')**3),
  reserva_interna_mensual_para_reposicion_clp=D('900000')/36,
  efecto_van_aislado_compra_900000_anio3_clp=q(-D('900000')/D('1.12')**3),
  valor_venta_terminal_caso_prudente_clp=0,
  advertencia_cierre='cero cobro por venta en caso prudente, no tasación de activos o empresa; sin perpetuidad y sin recuperar pérdidas como activo',
  gasto_marketing_por_pago_referencia_clp=D('350000')/16,
  advertencia_marketing='cociente de presupuesto por pagos de referencia; no CAC medido ni costo por cliente único',
  lanzamiento_desglose_propuesto_clp={'formalizacion_y_asesoria':300000,'preparacion_contenidos_y_materiales':300000,'campana_lanzamiento':400000,'contingencia_preoperativa':200000})
 assert sum(results['lanzamiento_desglose_propuesto_clp'].values())==1200000
 assert sum(r['egresos_identificados_propuestos_clp'] for r in rows)==q(proposed*12)
 assert sum(r['comision_neta_cobrada_supuesto_clp'] for r in rows)+receivable==netfee*12
 assert results['valor_desarrollo_fuente_clp']==6240000
 assert results['reserva_interna_mensual_para_reposicion_clp']*36==900000
 (OUT/'parametros_propuestos.json').write_text(json.dumps(results,ensure_ascii=False,indent=2,default=lambda v:format(v,'f'))+'\n')
 with (OUT/'calendario_2027_propuesto.csv').open('w',newline='',encoding='utf-8') as f:
  writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
 print(json.dumps(results,ensure_ascii=False,indent=2,default=str))
if __name__=='__main__':main()
