"""Aplica las aclaraciones del propietario sin confundir valoración y efectivo."""
from pathlib import Path
from decimal import Decimal as D
import json
from ejecutar_modelo_sapag import construir_proyeccion,cargar_costos,npv,dump,q
from ampliar_revision_sapag import table,money
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'04_modelo_sapag'

def main():
 params=json.loads((OUT/'parametros_ejecucion.json').read_text());valuation=D(params['desarrollo_valorizado']['valor_total_preoperativo_clp']);costs=cargar_costos(params)
 def evaluate(count,mode):
  model=construir_proyeccion(params,costs,pagos_mes=count,modo=mode)
  flows=list(model['flujo_anual']);flows[0]-=valuation
  return npv(params['tasa_descuento_nominal'],flows),model
 cases=[]
 for mode in ['condicionada','meta_200000','objetivo_millon']:
  lo,hi=0,(742 if mode=='condicionada' else 4096)
  assert evaluate(hi,mode)[0]>0
  while lo<hi:
   mid=(lo+hi)//2
   if evaluate(mid,mode)[0]>=0:hi=mid
   else:lo=mid+1
  positive,model=evaluate(lo,mode);previous,_=evaluate(lo-1,mode)
  if mode=='condicionada':assert all(a['pago_fundadores_modelado_clp']==0 for a in model['anual'])
  cases.append(dict(modo=mode,pagos_mes_minimos=lo,van_pago_anterior_clp=q(previous),van_minimo_clp=q(positive)))
 base=evaluate(16,'condicionada')[0]
 result=dict(alcance='prueba de recuperación de valorización total preoperativa; no flujo de desembolso ni estimación validada de costo de oportunidad incremental',desarrollo_valorizado_clp=valuation,
  lanzamiento_con_constitucion_clp=D(params['lanzamiento']['presupuesto_clp']),equipos='personales y compartidos, sin nueva compra ni transferencia de dominio presumida',
  valor_preoperativo_agregado_clp=valuation+D(params['lanzamiento']['presupuesto_clp']),van_base_con_recuperacion_valorizacion_clp=q(base),quiebres=cases,
  altera_caja_activa=False,desarrollo_efectivamente_pagado_clp=None,reparto_trabajo_pasado_futuro=None,deduccion_tributaria_por_valorizacion_aplicada=False)
 dump(OUT/'ratificacion_preoperacion.json',result)
 bp=ROOT/'03_propuesta/capitulo_xiv_borrador.md';ap=ROOT/'03_propuesta/anexo_h_tablas_fuente.md';body=bp.read_text();annex=ap.read_text()
 body=body.replace('Su eventual aporte, uso alternativo y tratamiento de depreciación permanecen por conciliar.', 'Los equipos siguen siendo personales y compartidos: no se presume transferencia de dominio ni se imputa una venta final a la empresa. Su uso alternativo y posibles costos incrementales permanecen separados.')
 body=body.replace('El presupuesto de preparación y lanzamiento de CLP 1.200.000 se conserva como provisional, pendiente de desglose.', 'El presupuesto de preparación y lanzamiento de CLP 1.200.000 incluye constitución y trámites, según ratificación del propietario. Se mantiene provisional y pendiente de desglose, sin añadir otra partida legal por los mismos conceptos.')
 annex=annex.replace('Los equipos existentes no generan compra inicial.', 'Los equipos personales y compartidos no generan compra inicial.')
 annex=annex.replace('Los tres notebooks y el teléfono ya existen, según confirmación del propietario. Su compra inicial se fija en cero. El aporte patrimonial, uso alternativo y depreciación se mantienen separados y no se atribuyen automáticamente a una empresa aún no constituida.', 'Los tres notebooks y el teléfono son personales y compartidos, según el propietario. Su compra inicial se fija en cero y no se presume transferencia de dominio a la empresa proyectada. Se mantienen separados el uso alternativo y eventuales costos incrementales; no se asigna a la empresa una depreciación o venta de bienes personales sin respaldo.')
 annex=annex.replace('Constitución, cargas de contratación, costos residuales propios, recursos de uso alternativo y reposiciones carecen de valoración completa.', 'La constitución y los trámites se incluyen en los CLP 1.200.000 de lanzamiento y no se suman otra vez. Las cargas de contratación, costos residuales propios, recursos de uso alternativo y reposiciones carecen de valoración completa.')
 annex=annex.replace('El desglose de CLP 1.200.000 de lanzamiento debe aclarar si incluye trámites de constitución para evitar duplicarlos.', 'Los CLP 1.200.000 de lanzamiento incluyen constitución y trámites por decisión del propietario; el desglose y la ejecución efectiva se documentan sin duplicar la partida.')
 reference='El lanzamiento objetivo es enero de 2027; H.40 evalúa por separado la recuperación del desarrollo valorizado.'
 if reference not in body:body=body.replace('Se clasifica cada recurso según',reference+' Se clasifica cada recurso según')
 if '## H.40.' in annex:annex=annex.split('## H.40.')[0].rstrip()+'\n'
 annex+='''
## H.40. Ratificación de decisiones preoperativas

El propietario ratifica que el lanzamiento se prevé en enero de 2027, los CLP 1.200.000 de preparación y lanzamiento incluyen constitución y trámites, y los equipos permanecen personales y compartidos. La inclusión de trámites evita duplicar el desembolso. El uso compartido no acredita transferencia patrimonial ni ingreso de venta final de equipos a la empresa.

La aclaración interpreta los CLP 6.240.000 como valorización del esfuerzo total para desarrollar el producto funcional antes del lanzamiento. No determina cuánto está ejecutado, cuánto falta ni un pago contratado. Se distingue la valoración global de origen del costo incremental pertinente a la fecha de decisión. El caso de caja conserva cero desembolso de desarrollo adicional confirmado; ello no declara cero su costo económico (Sapag Chain & Sapag Chain, 2008, pp. 126, 259–262).

Para observar qué volumen permitiría recuperar también esa valoración, se añade CLP 6.240.000 una sola vez al momento cero de una prueba separada, junto con el lanzamiento de CLP 1.200.000. El total de referencia pasa a CLP 7.440.000, sin sumar los equipos personales. No se incluye depreciación, amortización contable ni escudo tributario por esa valoración sin evidencia de su procedencia. No es una nueva salida de efectivo ni una valoración legal del software.

**Tabla H.40.1**
*Quiebre parcial al exigir recuperar la valoración global de desarrollo*

'''
 labels=['Sin asignaciones','Meta CLP 200.000 por persona','Meta CLP 1.000.000 por persona']
 annex+=table(['Escenario','Pagos mensuales mínimos','VAN con un pago menos CLP','VAN con el mínimo CLP'],[[label,money(x['pagos_mes_minimos']),money(x['van_pago_anterior_clp'],2),money(x['van_minimo_clp'],2)] for label,x in zip(labels,cases)])
 annex+='\n*Nota.* Ticket constante de CLP 50.000, comisión neta del 3 %, cuatro años y descuento del 12 %. Los gastos de lanzamiento ya incluyen trámites. El caso de 16 pagos, al exigir recuperar además la valoración global, produce VAN de CLP '+money(base,2)+'. Esta prueba mantiene los costos identificados independientes del volumen y no sustituye la caja de las Tablas 18 y 19 ni estima el costo de oportunidad incremental real. Las partidas aún no valoradas continúan excluidas.\n'
 bp.write_text(body);ap.write_text(annex)
 report=OUT/'INFORME_DE_AVANCE.md';text=report.read_text().split('## Aclaraciones preoperativas')[0].rstrip()
 text+='\n\n## Aclaraciones preoperativas incorporadas\n\nLanzamiento objetivo enero de 2027; constitución y trámites dentro del presupuesto de CLP 1.200.000; equipos personales compartidos sin compra ni transferencia presumida. El desarrollo de CLP 6.240.000 se interpreta como valorización global preoperativa, sin atribuir reparto pasado/futuro ni pago efectivo. H.40 calcula una prueba separada de recuperación de esa valoración. No se altera la necesidad de efectivo ni se declara una deducción fiscal por el solo valorizar trabajo.\n'
 report.write_text(text)
 print('Ratificadas decisiones de preoperación y prueba separada de recuperación del desarrollo valorizado.')

if __name__=='__main__':main()
