"""Contrastes independientes del tercer corte de liquidez e indicadores."""
from pathlib import Path
from decimal import Decimal as D
import json,math
from indicadores_sapag import indicadores
ROOT=Path(__file__).resolve().parents[1]
def main():
 r=json.loads((ROOT/'04_modelo_sapag/liquidez_indicadores_y_cierre.json').read_text());m=json.loads((ROOT/'04_modelo_sapag/resultados_proyeccion.json').read_text())
 totals={}
 for key,rows in r['financiacion_mensual'].items():
  assert len(rows)==49
  unfinanced=0.;provided=0.
  for row in rows:
   unfinanced+=float(row['flujo_parcial_clp']);provided+=float(row['aporte_minimo_adicional_clp'])
   assert abs(unfinanced+provided-float(row['caja_con_aportes_clp']))<1e-6
   assert float(row['caja_con_aportes_clp'])>=0 and float(row['aporte_minimo_adicional_clp'])>=0
   assert float(row['aporte_minimo_adicional_clp'])==0 or float(row['caja_con_aportes_clp'])==0
  assert abs(provided-max(0,-min(math.fsum(float(x['flujo_parcial_clp']) for x in rows[:i+1]) for i in range(49))))<1e-6
  totals[key]=provided
  assert abs(provided-float(m[key]['necesidad_financiacion_acumulada_parcial_clp']))<1e-6
 interests=math.fsum(float(a['interes_clp']) for a in m['condicionada_financiado']['anual'])
 assert abs(totals['condicionada_financiado']-totals['condicionada_puro']-interests)<1e-6
 assert totals['condicionada_puro']==26168498.16
 assert abs(sum(float(x['aporte_minimo_puro_clp']) for x in r['financiacion_anual'])-totals['condicionada_puro'])<1e-6
 for x in r['cobertura_deuda']:
  if x['servicio_deuda_clp']!='0':
   expected=float(x['caja_propia_antes_deuda_clp'])/float(x['servicio_deuda_clp'])
   assert abs(expected-float(x['cobertura_caja_sobre_cuota']))<1e-12
   assert expected<0
  else:assert x['cobertura_caja_sobre_cuota'] is None
 for i,x in enumerate(r['indicadores']):
  flows=[float(v) for v in x['flujo_anual']]
  independent=math.fsum(f/1.12**t for t,f in enumerate(flows))
  assert abs(independent-float(x['van_clp']))<.0001
  if x['tir_anual'] is not None:
   irr=float(x['tir_anual']);assert abs(math.fsum(f/(1+irr)**t for t,f in enumerate(flows)))<1e-6
   for field,rate in [('recuperacion_simple_anios',0),('recuperacion_descontada_anios',.12)]:
    when=float(x[field]);year=math.floor(when);fraction=when-year
    balance=math.fsum(f/(1+rate)**t for t,f in enumerate(flows[:year+1]))
    recovered=balance+fraction*flows[year+1]/(1+rate)**(year+1)
    assert abs(recovered)<1e-6
  else:assert x['recuperacion_simple_anios'] is None and x['recuperacion_descontada_anios'] is None
 assert r['indicadores'][2]['pagos_mes']==391
 assert all(D(v)==D(w) for v,w in zip(r['indicadores'][2]['flujo_anual'],r['indicadores'][3]['flujo_anual']))
 assert indicadores([-100,110],'.12')['tir_anual'].quantize(D('.0001'))==D('.1000')
 # Un patrón de financiación y uno con varios cambios no se etiquetan TIR de inversión única.
 assert indicadores([100,-110],'.12')['tir_anual'] is None
 assert indicadores([-100,230,-132],'.12')['tir_anual'] is None
 for x in r['sensibilidad_cuentas_cobrar']:
  tied=24000*x['dias_supuesto']/30
  assert abs(tied-float(x['comision_por_cobrar_clp']))<1e-6
  assert abs(-tied+tied/1.12**4-float(x['efecto_van_clp']))<1e-6
 pureflows=[float(v) for v in m['condicionada_puro']['flujo_anual']]
 pureflows[-1]+=float(r['cobro_terminal_neto_para_van_cero_clp'])
 assert abs(math.fsum(f/1.12**t for t,f in enumerate(pureflows)))<1e-6
 assert r['capital_trabajo_completo_clp'] is None and r['valor_terminal_estimado_clp'] is None
 pre=json.loads((ROOT/'04_modelo_sapag/ratificacion_preoperacion.json').read_text())
 params=json.loads((ROOT/'04_modelo_sapag/parametros_ejecucion.json').read_text())
 assert params['lanzamiento']['incluye_constitucion_tramites'] is True
 assert params['equipos']['uso']=='personales y compartidos' and not params['equipos']['transferencia_dominio_prevista']
 assert pre['altera_caja_activa'] is False and pre['deduccion_tributaria_por_valorizacion_aplicada'] is False
 assert D(pre['valor_preoperativo_agregado_clp'])==D('7440000')
 for row,wage in zip(pre['quiebres'],[0,600000,3000000]):
  def independently(count):
   flows=[-7440000.]
   for a in m['condicionada_puro']['anual']:
    pretax=count*1500*12-float(a['opex_identificado_clp'])-12*wage
    assert pretax>0
    flows.append(pretax-round(pretax*.27,2))
   return math.fsum(f/1.12**t for t,f in enumerate(flows))
  count=row['pagos_mes_minimos']
  assert independently(count-1)<0<=independently(count)
  assert abs(independently(count)-float(row['van_minimo_clp']))<.01
 assert D(pre['van_base_con_recuperacion_valorizacion_clp'])==D(m['condicionada_puro']['van_parcial_12_clp'])-D('6240000')
 audit={'estado':'correcto','alcance':'tercer corte parcial; no confirma datos comerciales o contractuales','calendarios':2,'momentos_por_calendario':49,'indicadores_contrastados':len(r['indicadores']),'aportes_adicionales_sin_deuda_clp':totals['condicionada_puro'],'aportes_adicionales_con_deuda_clp':totals['condicionada_financiado'],'incremento_por_intereses_clp':interests,'pruebas':['identidad de caja y aportes mínimos','déficit máximo sin aportes','cobertura negativa de deuda','VAN y raíces de TIR','recuperación nominal y descontada','ausencia de TIR convencional para financiación y múltiples signos','sensibilidad de cuentas por cobrar','umbral terminal sin incorporarlo como valor esperado']}
 (ROOT/'04_modelo_sapag/auditoria_tercer_corte.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n');print(json.dumps(audit,ensure_ascii=False))
if __name__=='__main__':main()
