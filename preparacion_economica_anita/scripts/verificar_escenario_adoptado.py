"""Auditoría independiente de caja, calendario, liquidación y documentos."""
from pathlib import Path
from decimal import Decimal as D
import json,math,re,subprocess,zipfile
from lxml import etree as E
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'06_escenario_adoptado'
def load(name):return json.loads((OUT/name).read_text())
def number(x):return D(x.strip().replace('.','').replace(',','.'))
def main():
 p=load('parametros.json');models=load('resultados.json');cs=load('costos.json');roots=load('umbrales_van.json')
 assert sum(D(c['anual_1_clp']) for c in cs)==D('6168036.24')
 assert len({c['id'] for c in cs})==8
 assert next(D(c['anual_1_clp']) for c in cs if c['id']=='C05')==D(9990)
 assert sum(p['lanzamiento']['desglose_presupuesto_clp'].values())==1200000
 pure=models['condicionada_puro'];fin=models['condicionada_financiado']
 assert [D(r['opex_pagado_clp']) for r in pure['mensual'][:3]]==[D('660660.52'),D('500670.52'),D('500670.52')]
 assert [D(r['comision_neta_cobrada_clp']) for r in pure['mensual'][:3]]==[D(18400),D(24000),D(24000)]
 assert D(pure['mensual'][-1]['cxc_final_clp'])==D(5600)
 assert D(pure['flujo_anual_operacion_clp'][0])==D(-1200000)
 assert D(fin['flujo_anual_operacion_clp'][0])==D(2520000)
 for key,m in models.items():
  assert len(m['mensual'])==48 and len(m['anual'])==4 and len(m['aportes'])==49
  starting=D(m['flujo_anual_operacion_clp'][0]);balance=starting;cx=D(0)
  for r in m['mensual']:
   assert D(r['comision_neta_cobrada_clp'])==D(r['comision_neta_devengada_clp'])+cx-D(r['cxc_final_clp'])
   assert D(r['cxc_final_clp'])==D(r['comision_neta_devengada_clp'])*D(m['lag_dias'])/30
   assert D(r['gmv_clp'])==D(r['comision_neta_devengada_clp'])+D(r['iva_comision_restringido_clp'])+D(r['saldo_publicadores_antes_pasarela_clp'])
   assert r['tarifa_pasarela'] is None and r['abono_final_publicadores_clp'] is None
   cash=D(r['comision_neta_cobrada_clp'])-sum(D(r[k]) for k in ['opex_pagado_clp','pago_fundadores_clp','interes_pagado_clp','principal_pagado_clp','compra_reposicion_clp','impuesto_pagado_clp'])
   balance+=cash;assert cash==D(r['flujo_caja_clp']) and balance==D(r['caja_sin_aportes_clp'])
   cx=D(r['cxc_final_clp'])
   if m['modo']=='condicionada':
    target=D(r['meta_fundadores_clp']);actual=D(r['pago_fundadores_clp'])
    assert actual in (D(0),target)
    assert actual==0 or D(r['capacidad_mensual_para_meta_clp'])>=target
  for i,y in enumerate(m['anual']):
   rows=m['mensual'][12*i:12*(i+1)]
   for annual,monthly in [('opex_devengado_clp','opex_devengado_clp'),('opex_pagado_clp','opex_pagado_clp'),('pago_fundadores_clp','pago_fundadores_clp'),('flujo_caja_clp','flujo_caja_clp')]:assert D(y[annual])==sum(D(r[monthly]) for r in rows)
   assert D(y['opex_devengado_clp'])==D(y['opex_pagado_clp'])
   expected=D(y['ebt_clp'])-D(y['impuesto_clp'])-D(y['amortizacion_deuda_clp'])-D(y['compra_reposicion_clp'])-D(y['variacion_cxc_clp'])
   assert expected==D(y['flujo_caja_clp'])
  funds=D(0);cash=D(0);minimum=D(0);required=D(0)
  for r in m['aportes']:
   cash+=D(r['flujo_caja_clp']);minimum=min(minimum,cash);required=max(required,D(r['reserva_objetivo_clp'])-cash);funds+=D(r['aporte_minimo_clp'])
   assert cash+funds==D(r['caja_con_aportes_clp'])>=D(r['reserva_objetivo_clp'])
   assert D(r['aporte_minimo_clp'])==0 or D(r['caja_con_aportes_clp'])==D(r['reserva_objetivo_clp'])
  assert funds==required==D(m['aporte_minimo_acumulado_clp'])
  assert D(m['liquidacion']['cobro_cxc_clp'])==cx
  assert D(m['liquidacion']['caja_final_con_aportes_clp'])==cash+funds+cx
  assert D(m['liquidacion']['venta_activos_clp'])==D(m['liquidacion']['venta_software_clp'])==0
  flows=[float(x) for x in m['flujos_indicadores_clp']];times=[float(x) for x in m['momentos_indicadores_anios']]
  independent=math.fsum(f/1.12**t for f,t in zip(flows,times))
  assert abs(independent-float(m['indicadores']['van_con_liquidacion_clp']))<.01
  monthly=float(m['flujo_anual_operacion_clp'][0])+math.fsum(float(r['flujo_caja_clp'])/1.12**(r['periodo']/12) for r in m['mensual'])+float(cx)/1.12**(4+float(m['lag_dias'])/360)
  assert abs(monthly-float(m['van_mensual_control_clp']))<.01
  assert D(m['liquidacion']['momento_anios'])==D(4)+D(m['lag_dias'])/360
 assert all(D(r['pago_fundadores_clp'])==0 for r in pure['mensual'])
 assert pure['indicadores']['tir_anual'] is None and pure['indicadores']['recuperacion_simple_anios'] is None
 assert models['estres_cobro30']['mensual'][0]['comision_neta_cobrada_clp']=='0.00'
 assert D(models['estres_cobro30']['liquidacion']['cobro_cxc_clp'])==24000
 repl=models['estres_reposicion'];assert sum(D(r['compra_reposicion_clp']) for r in repl['mensual'])==900000
 assert sum(D(r['reserva_reposicion_regla_pago_clp']) for r in repl['mensual'])==900000
 assert D(repl['aportes'][1]['reserva_objetivo_clp'])==25000 and D(repl['aportes'][35]['reserva_objetivo_clp'])==875000
 assert D(repl['aportes'][36]['reserva_objetivo_clp'])==0
 assert D(repl['flujo_anual_operacion_clp'][3])-D(pure['flujo_anual_operacion_clp'][3])==D(-900000)
 # Independiente: flujos anuales de demanda uniforme con asignaciones fijas.
 def independent(count,wage,valuation=0):
  loss=0.;flows=[-1200000.-valuation];times=[0,1,2,3,4,4+7/360]
  stock=count*1500*7/30
  for i,y in enumerate(pure['anual']):
   ebt=count*1500*12-float(y['opex_devengado_clp'])-wage*12
   used=min(max(ebt,0),loss);tax=round(max(ebt-used,0)*.27,2);loss+=max(-ebt,0)-used
   flows.append(ebt-tax-(stock if i==0 else 0))
  flows.append(stock)
  return math.fsum(f/1.12**t for f,t in zip(flows,times))
 for root in roots:
  count=root['pagos_mes'];wage={'sin_asignaciones':0,'meta_200000':600000,'objetivo_millon':3000000}[root['modo']];valuation=6240000 if root['recupera_valorizacion'] else 0
  assert independent(count-1,wage,valuation)<0<=independent(count,wage,valuation)
  assert abs(independent(count,wage,valuation)-float(root['van_minimo_clp']))<.01
  flows=[float(f) for f in root['flujos_clp']];times=[float(t) for t in root['momentos_anios']];irr=float(root['indicadores']['tir_anual'])
  assert abs(math.fsum(f/(1+irr)**t for f,t in zip(flows,times)))<.01
  for field,rate in [('recuperacion_simple_anios',0),('recuperacion_descontada_anios',.12)]:
   when=float(root['indicadores'][field]);idx=next(i for i,t in enumerate(times) if t>=when)
   balance=math.fsum(f/(1+rate)**t for f,t in zip(flows[:idx],times[:idx]));fraction=(when-times[idx-1])/(times[idx]-times[idx-1])
   assert abs(balance+fraction*flows[idx]/(1+rate)**times[idx])<.01
 # Sensibilidades contrastadas con expresión independiente de la referencia sin impuesto.
 sens=load('sensibilidad.json');assert len(sens)==11
 amounts=[float(c['anual_1_clp']) for c in cs];currency=[c['moneda_modelada'] for c in cs]
 for row in sens:
  var=row['variable'];factor=1+float(row['variacion_pct'])/100
  if var=='descuento':
   r=float(row['variacion_pct'])/100
   expected=math.fsum(float(f)/(1+r)**float(t) for f,t in zip(pure['flujos_indicadores_clp'],pure['momentos_indicadores_anios']))
  else:
   fees=24000*(factor if var in ('pagos','ticket') else 1);stock=round(fees*7/30,2)
   flows=[-1200000.]
   for year in range(4):
    annual=math.fsum(round(v*(1.04**year if c=='clp' else 1)*(factor if var=='costos' or (var=='cambio' and c=='aws') else 1),2) for v,c in zip(amounts,currency))
    flows.append(fees*12-annual-(stock if year==0 else 0))
   flows.append(stock);expected=math.fsum(f/1.12**t for f,t in zip(flows,[0,1,2,3,4,4+7/360]))
  assert abs(expected-float(row['van_con_liquidacion_clp']))<.10
 commercial=load('escenarios_comerciales_anita.json')
 assert [(float(x['pagos_mes']),x['ticket_clp']) for x in commercial]==[(4,35000),(16,50000),(45,65000)]
 assert commercial[1]['van_con_liquidacion_clp']==pure['indicadores']['van_con_liquidacion_clp']
 for x in commercial:
  revenue=float(x['pagos_mes'])*x['ticket_clp']*.03;stock=revenue*7/30
  flows=[-1200000.]+[revenue*12-float(a['opex_devengado_clp'])-(stock if i==0 else 0) for i,a in enumerate(pure['anual'])]+[stock]
  expected=math.fsum(f/1.12**t for f,t in zip(flows,[0,1,2,3,4,4+7/360]))
  assert abs(expected-float(x['van_con_liquidacion_clp']))<.01
 # La deuda inicial no habilita asignaciones con ingresos insuficientes.
 assert all(D(r['pago_fundadores_clp'])==0 for r in fin['mensual'])
 from escenario_adoptado import proyectar
 control=proyectar(p,pagos=793)
 assert control['mensual'][0]['pago_fundadores_clp']==0
 assert any(r['pago_fundadores_clp']>0 for r in control['mensual'][1:])
 assert D(pure['aportes'][3]['aportes_acumulados_clp'])==D('2795601.56')
 # Contraste visible y preservación de fuente.
 body=(ROOT/'03_propuesta/capitulo_xiv_borrador.md').read_text();annex=(ROOT/'03_propuesta/anexo_h_tablas_fuente.md').read_text()
 original=subprocess.check_output(['git','show','755df58:preparacion_economica_anita/03_propuesta/anexo_h_tablas_fuente.md'],cwd=ROOT.parent).decode()
 assert original.split('## H.27.')[0]==annex.split('## H.27.')[0]
 labels=re.findall(r'^\*\*Tabla ([^*]+)\*\*$',body+'\n'+annex,re.M);assert len(labels)==len(set(labels))
 for n in range(14,27):assert str(n) in labels
 for n,key in [(18,'condicionada_puro'),(19,'condicionada_financiado'),(20,'estres_reposicion'),(21,'estres_cobro30')]:
  block=body.split(f'**Tabla {n}**')[1].split('*Nota.*')[0]
  rows={r.split('|')[1].strip():[number(x) for x in r.split('|')[2:-1]] for r in block.splitlines() if r.startswith('| (')}
  get=lambda start:next(v for k,v in rows.items() if k.startswith(start))
  for i in range(5):
   expected=get('(=) Utilidad neta')[i]+get('(+) Ajuste')[i]+get('(+) Préstamo')[i]+get('(-) Lanzamiento')[i]-get('(-) Variación')[i]-get('(-) Amortización')[i]
   assert abs(expected-get('(=) Flujo')[i])<=2
   assert abs(get('(=) Flujo')[i]-D(models[key]['flujo_anual_operacion_clp'][i]))<=D('.5')
 current=body[body.index('#### 14.3.3.'):]+annex[annex.index('## H.27.'):]
 for stale in ['514.083,02','20.055.029,94','2.335']:
  assert stale not in current,stale
 doc=ROOT/'03_propuesta/build/Preparacion_economica_espaciGo.docx'
 with zipfile.ZipFile(doc) as z:xml=E.fromstring(z.read('word/document.xml'))
 ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'};text=''.join(xml.xpath('//w:t/text()',namespaces=ns));nt=len(xml.xpath('//w:tbl',namespaces=ns))
 assert nt==len(labels)
 for label in labels:assert f'Tabla {label}' in text
 result=dict(estado='correcto',alcance='simulación adoptada, no prueba comercial o contractual',escenarios=len(models),meses_por_escenario=48,tablas_word=nt,
 verificaciones=['fuente H.1–H.26 íntegra','costos y anualidades conciliados','devengo/cobro/CxC y liquidación sin doble conteo','IVA y fondos ajenos separados','caja y déficit máximo por escenario','reserva de reposición sin gasto duplicado','VAN independiente anual y mensual','raíces adyacentes, TIR y recuperación con fechas','cuatro flujos completos visibles y referencias únicas','cifras antiguas retiradas de memorias activas'])
 (OUT/'auditoria.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
