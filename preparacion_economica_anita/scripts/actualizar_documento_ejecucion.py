"""Integra en la preparación Word el primer corte financiero parcial de Sapag."""
from pathlib import Path
from decimal import Decimal as D
import json
ROOT=Path(__file__).resolve().parents[1]
MODEL=ROOT/'04_modelo_sapag'
def load(p):return json.loads(p.read_text())
def money(v,decimals=2):
    return f'{D(str(v)):,.{decimals}f}'.replace(',','X').replace('.',',').replace('X','.')
def n(v):return money(v,0)
def mdtable(headers,rows):return '| '+' | '.join(headers)+' |\n|'+'|'.join('---' for _ in headers)+'|\n'+''.join('| '+' | '.join(map(str,r))+' |\n' for r in rows)

def flow_table(model,params,costs,caption):
    annual=model['anual'];loan=params['deuda_simulada'];fin=model['financiado']
    admin=[];op=[]
    for a in annual:
        year=a['periodo'];ad=sum(D(c['anual_1_clp'])*(1+D(params['costos']['reajuste_anual_presupuestos_clp']))**(year-1) for c in costs if c['id'] in ('C03','C04','C08'))
        admin.append(ad);op.append(D(a['opex_identificado_clp'])-ad+D(a['pago_fundadores_modelado_clp']))
    def series(key,initial=0):return [initial]+[D(a[key]) for a in annual]
    rows=[
      ('(+) Ingresos por comisiones',series('comision_neta_clp')),
      ('(-) Costos variables propios de pasarela',[0]*5),
      ('(-) Costos fijos operativos (OPEX)',[0]+op),
      ('(-) Gastos de administración y marketing',[0]+admin),
      ('(-) Depreciación de activos',[0]*5),
      ('(=) Resultado operativo (EBIT)',series('ebit_clp')),
      ('(-) Gastos financieros (intereses)',series('interes_clp')),
      ('(=) Utilidad antes de impuestos (EBT)',series('ebt_clp')),
      ('(-) Impuesto académico (27 %)',series('impuesto_clp')),
      ('(=) Utilidad neta',[0]+[D(a['ebt_clp'])-D(a['impuesto_clp']) for a in annual]),
      ('(+) Ajuste por depreciación',[0]*5),
      ('(+) Préstamo simulado recibido',[D(loan['principal_clp']) if fin else 0,0,0,0,0]),
      ('(-) Inversión y preparación identificadas',[-D(params['lanzamiento']['presupuesto_clp'])-D(params['equipos']['compra_inicial_clp']),0,0,0,0]),
      ('(-) Capital de trabajo del ciclo',['n.d.']*5),
      ('(-) Amortización de deuda',series('amortizacion_deuda_clp')),
      ('(=) Flujo neto parcial identificado',model['flujo_anual'])]
    vals=[[title]+[v if v=='n.d.' else money(v,0) for v in values] for title,values in rows]
    result=f'**Tabla {caption}**\n*Flujo '+('financiado' if fin else 'puro')+' parcial del escenario de referencia*\n\n'
    result+=mdtable(['Partida / período','Año 0','Año 1','Año 2','Año 3','Año 4'],vals)
    result+='\n*Nota.* Elaboración con los supuestos del primer corte. CLP redondeados para presentación; la memoria conserva centavos de presupuesto. Se conserva la secuencia del flujo de Anita. El subtotal excluye partidas sin valoración, capital de trabajo del ciclo y valor de cierre. «n.d.» significa no determinado, no cero. La depreciación y el costo residual propio de pasarela no se reconocen en este escenario parcial hasta resolver aportes y condiciones; no se afirma que sean cero en la operación real. Los equipos existentes no generan compra inicial. El lanzamiento presupuestado se asigna al momento cero, con clasificación contable por conciliar.\n'
    return result

def main():
    params=load(MODEL/'parametros_ejecucion.json');models=load(MODEL/'resultados_proyeccion.json');costinfo=load(MODEL/'costos_conciliados.json');costs=costinfo['partidas'];pure=models['condicionada_puro'];fin=models['condicionada_financiado']
    base=load(ROOT/'02_contraste/umbrales_remuneraciones.json');target=load(ROOT/'02_contraste/umbral_sueldo_objetivo.json')
    bodypath=ROOT/'03_propuesta/capitulo_xiv_borrador.md';annexpath=ROOT/'03_propuesta/anexo_h_tablas_fuente.md'
    body=bodypath.read_text();annex=annexpath.read_text()
    # Primera ejecución: numeración de las dos tablas que siguen a los nuevos flujos.
    if '#### 14.3.3. Proyección parcial' not in body:
      body=body.replace('**Tabla 18**','**Tabla 20**').replace('**Tabla 19**','**Tabla 21**')
      annex=annex.replace('Tablas 18 y 19','Tablas 20 y 21')
    body=body.replace('La relación con la inversión inicial y el estado de compra requiere conciliación.','El propietario confirma que los tres notebooks y el teléfono ya existen y no se compran al inicio. Por ello, el desembolso inicial por estos equipos es CLP 0. Su eventual aporte, uso alternativo y tratamiento de depreciación permanecen por conciliar. El presupuesto de preparación y lanzamiento de CLP 1.200.000 se conserva como provisional, pendiente de desglose.')
    method='El capital de trabajo se determina mediante el calendario de ingresos y egresos mensuales y el método propuesto del déficit acumulado máximo.'
    if 'La proyección disponible muestra déficit operativo persistente' not in body:
        body=body.replace(method,method+' La proyección disponible muestra déficit operativo persistente y lo presenta como necesidad de financiación de partidas identificadas. No se suma ese déficit nuevamente al Año 0 como capital de trabajo, porque duplicaría las pérdidas. El capital del ciclo de liquidación continúa no determinado.')
    start=body.index('### 14.6. Cobros necesarios para financiar remuneraciones')
    updated='''### 14.6. Cobros necesarios para financiar remuneraciones

Se mantienen CLP 200.000 por fundador como meta inicial y CLP 1.000.000 como objetivo adicional. La regla de escenario prevé pago conjunto completo o cero, sujeto al excedente propio después de obligaciones identificadas. En la proyección de referencia no se activa el pago porque la comisión mensual es inferior al costo operativo parcial. Esto no elimina el costo económico del trabajo ni define obligaciones laborales.

La conciliación incorpora una sola vez los útiles de oficina de CLP 120.000 anuales y la dirección tributaria de CLP 150.000 anuales, cuya periodicidad ratifica el propietario. El marketing operativo se mantiene separado del lanzamiento. Ambas partidas son presupuestarias y provisionales, sin acreditar contratación. Por ello, los umbrales previos de 728 y 2.328 pagos se actualizan a 743 y 2.343 al ticket de CLP 50.000.

**Tabla 20**
*Presupuesto mensual parcial conciliado para calcular las metas*

'''
    tablecost=[[c['concepto'],money(c['mensual_1_clp'])] for c in costs]+[['Subtotal sin fundadores',money(costinfo['total_mensual_1_clp'])],['Meta conjunta inicial de fundadores','600.000,00'],['Subtotal con meta inicial',money(base['costo_parcial_con_meta_fundadores_clp'])]]
    updated+=mdtable(['Componente','Importe mensual CLP'],tablecost)
    updated+='\n*Nota.* Se utilizan Base mensual!B21:B25, Conciliacion costos!H9, el escenario AWS adoptado y la dirección tributaria anual ratificada. Cada componente se cuenta una sola vez. Se retiran GCP y subtotales duplicados; los presupuestos de útiles y dirección se suman separadamente. Los conceptos sin importe o alcance completos permanecen pendientes fuera de este subtotal. H.32 detalla fuentes, inversión y exclusiones.\n\n'
    updated+='''El análisis conserva la lógica costo-volumen-utilidad de Sapag, con sus límites respecto de inversión e impuestos (Sapag Chain & Sapag Chain, 2008, pp. 129–130). La contribución unitaria es la comisión neta por cobro menos costos variables propios cuando se determinen. Se redondea hacia arriba el cociente entre costos y asignaciones objetivo y esa contribución. El IVA no financia remuneraciones.

**Tabla 21**
*Cobros requeridos por ticket para dos metas de remuneración*

'''
    updated+=mdtable(['Ticket medio CLP','Comisión neta por cobro CLP','Pagos para CLP 200.000 por persona','Pagos para CLP 1.000.000 por persona'],[[n(a['ticket_medio_clp']),n(a['comision_neta_por_pago_clp']),n(a['pagos_mes']),n(b['pagos_mes'])] for a,b in zip(base['metas_por_ticket'],target['metas_por_ticket'])])
    updated+='\n*Nota.* Tres fundadores, comisión neta de 3 % y costos parciales de CLP '+money(costinfo['total_mensual_1_clp'])+' mensuales. Los cálculos excluyen partidas pendientes y variación de infraestructura por volumen. Son cantidades de pagos, no de contratos o personas únicas, y no equivalen a VAN cero.\n\n'
    updated+='''A ticket de CLP 50.000, cubrir solo CLP 600.000 requiere 400 pagos. Con el costo parcial conciliado se requieren 743 pagos, CLP 37.150.000 transados y CLP 1.114.500 de comisión neta. El remanente sobre costos parciales y meta inicial es CLP 416,98, antes de partidas pendientes. Para CLP 1.000.000 por fundador se requieren 2.343 pagos y CLP 117.150.000 transados.

La referencia comercial de 16 pagos mensuales conserva CLP 24.000 de comisión neta. La brecha para cubrir costo parcial y meta inicial es de 727 pagos y CLP 1.090.083,02 mensuales. Con dos pagos por espacio, 743 pagos equivalen aproximadamente a 372 espacios activos. Son equivalencias bajo supuestos, no captación comprobada. Los anexos H.27 y H.31–H.35 respaldan los cálculos y su alcance.
'''
    body=body[:start]+updated
    # Insertar o reemplazar los flujos corregidos de partidas identificadas.
    marker='#### 14.3.3. Proyección parcial de las partidas identificadas'
    block='''#### 14.3.3. Proyección parcial de las partidas identificadas

El primer corte proyecta 48 meses entre 2027 y 2030. Conserva 16 pagos y CLP 50.000 por pago, sin crecimiento automático de volumen ni ticket. Los presupuestos CLP se reajustan al 4 % anual como supuesto de Anita; USD y tipo de cambio del presupuesto AWS se mantienen constantes. No se aplican créditos sin vigencia y elegibilidad verificadas para el período. La mezcla por categoría y el calendario de liquidación aún requieren definición; H.31 y H.33 contienen el detalle.

En el Año 1 se presupuestan CLP 288.000 de comisión neta y CLP 6.168.996,24 de costos identificados. El pago condicionado a fundadores resulta cero por falta de excedente. No se confunde ese desembolso con la valorización del trabajo. Las proyecciones siguientes son subtotales de caja y no certifican viabilidad, porque faltan partidas de inversión, costos, capital de trabajo y cierre.

'''+flow_table(pure,params,costs,18)+'\n\n#### 14.3.4. Escenario parcial con financiamiento simulado\n\nEl préstamo continúa como simulación de CLP 3.720.000, al 12 % anual, con tres cuotas al final de cada año. La última cuota se ajusta en CLP 1 para cerrar el saldo. La entrada del Año 0 es financiamiento y no ingreso del marketplace. Al superar el lanzamiento identificado, origina una entrada neta inicial; este patrón exige evitar interpretar una TIR de financiación como rentabilidad de inversión. H.34 documenta la amortización.\n\n'+flow_table(fin,params,costs,19)+'\n\n'
    insert=body.index('### 14.4.')
    if marker in body:
        a=body.index(marker);body=body[:a]+block+body[insert:]
    else:body=body[:insert]+block+body[insert:]
    a=body.index('El recálculo del vector original de Anita')
    b=body.index('### 14.5.',a)
    body=body[:a]+'El recálculo del vector original de Anita produce VAN de CLP −2.291.237,39 al 12 % y TIR de 0,85115 %. Estos indicadores pertenecen al flujo histórico. La serie definitiva AWS requiere completar las partidas pendientes. Para el subtotal puro identificado se obtiene un VAN parcial al 12 % de CLP '+money(pure['van_parcial_12_clp'])+', y para el financiado, CLP '+money(fin['van_parcial_12_clp'])+'. La serie pura solo presenta salidas y no tiene una TIR con signos opuestos. En la financiada, una entrada inicial seguida de salidas no se interpreta como rendimiento convencional de inversión. Estos resultados parciales no sustituyen el cierre del proyecto.\n\n'+body[b:]
    if 'El primer corte compara los tres escenarios de demanda' not in body:
        body=body.replace('La transcripción de las 26 hojas permite revisar esa trazabilidad.','La transcripción de las 26 hojas permite revisar esa trazabilidad. El primer corte compara los tres escenarios de demanda originales con comisión común del 3 %, sin atribuir probabilidades. Los VAN de partidas identificadas continúan negativos; el cierre de costos y los puntos de quiebre definitivos permanecen pendientes. H.33 registra los resultados parciales.')
    bodypath.write_text(body)
    # H.27 se actualiza como memoria activa, manteniendo H.1–H.26 intactos.
    a=annex.index('## H.27.');b=annex.index('## H.28.',a)
    annex=annex[:a]+'''## H.27. Memoria actualizada de las metas de remuneración

Este apartado respalda las Tablas 20 y 21 y se actualiza con la conciliación de útiles de oficina. Los cálculos anteriores sin esa partida son un corte histórico. Se conserva su procedencia en la historia del repositorio.

El presupuesto mensual sin fundadores es CLP 514.083,02: la base parcial de CLP 491.583,02 más CLP 10.000 de útiles y CLP 12.500 de dirección tributaria. Los útiles proceden de Conciliacion costos!H9 y la periodicidad anual de la dirección es ratificada por el propietario. Con la meta conjunta inicial de CLP 600.000, se requieren CLP 1.114.083,02 de comisión neta. A ticket de CLP 50.000 y comisión neta de CLP 1.500 por cobro, el mínimo entero es 743 pagos: 742 producen CLP 1.113.000 y no alcanzan; 743 producen CLP 1.114.500. Para CLP 1.000.000 por fundador, el mínimo es 2.343 pagos.

El cálculo redondea hacia arriba (costo parcial + tres asignaciones objetivo) dividido por (ticket multiplicado por 0,03). Los costos variables propios que se determinen reducen la contribución por cobro. El script calcular_tickets_remuneraciones.py lee los componentes y genera umbrales_remuneraciones.json y umbral_sueldo_objetivo.json. La comparación con fuente y las proyecciones se documentan en H.31–H.35.

'''+annex[b:]
    if '## H.31.' in annex:annex=annex[:annex.index('## H.31.')].rstrip()+'\n'
    annex+='''
## H.31. Proyección comercial agregada y categorías

La referencia conserva ocho espacios promedio, dos pagos mensuales por espacio y ticket de CLP 50.000. No se añade crecimiento de volumen o precio sin una decisión respaldada. El archivo proyeccion_mensual_2027_2030.csv registra los 48 meses con comisión, IVA y fondos de publicadores separados. La tabla siguiente no reparte los ocho espacios entre categorías, porque ese dato aún no está definido. Nueve categorías disponibles no implica nueve espacios activos ni demanda validada en todas ellas.

**Tabla H.31.1**
*Estado de asignación de la oferta por categoría*

'''
    annex+=mdtable(['ID','Categoría','Espacios y pagos','Ticket y mezcla'],[[str(x['id']),x['categoria'],'Pendiente de asignar','Pendiente de ratificar'] for x in load(MODEL/'matriz_categorias.json')])
    annex+='\n*Nota.* Catálogo de nueve categorías comunicado por el propietario. No se sustituyen datos faltantes por ceros observados. La referencia agregada puede calcularse sin atribuir ventas a una categoría. La mezcla de modalidades previa se conserva como ejemplo no ratificado.\n\n**Tabla H.31.2**\n*Proyección comercial agregada sin crecimiento automático*\n\n'
    annex+=mdtable(['Año','Pagos anuales','GMV CLP','Comisión neta CLP','IVA de comisión CLP'],[[str(a['anio_calendario']),'192',money(a['gmv_clp']),money(a['comision_neta_clp']),money(a['iva_comision_clp'])] for a in pure['anual']])
    annex+='\n*Nota.* Elaboración con los parámetros agregados ratificados como referencia provisional. El total transado no es ingreso propio de espaciGo. Por mes, el saldo de publicadores antes de Mercado Pago es CLP 771.440; el abono final no se determina sin la tarifa y liquidación efectivas.\n\n## H.32. Recursos y presupuesto conciliado\n\nLos tres notebooks y el teléfono ya existen, según confirmación del propietario. Su compra inicial se fija en cero. El aporte patrimonial, uso alternativo y depreciación se mantienen separados y no se atribuyen automáticamente a una empresa aún no constituida. El presupuesto de CLP 1.200.000 de lanzamiento se mantiene provisional en el Año 0, sin duplicarlo con marketing operativo.\n\n**Tabla H.32.1**\n*Componentes del presupuesto identificado del Año 1*\n\n'
    annex+=mdtable(['ID','Componente','Mensual CLP','Anual CLP'],[[c['id'],c['concepto'],money(c['mensual_1_clp']),money(c['anual_1_clp'])] for c in costs]+[['Total','Subtotal parcial',money(costinfo['total_mensual_1_clp']),money(costinfo['total_anual_1_clp'])]])
    annex+='\n*Nota.* Presupuestos de Base mensual!B21:B25 y Conciliacion costos!H9, con sustitución de GCP por el escenario AWS adoptado y dirección tributaria anual ratificada. Los útiles y la dirección se cuentan una sola vez. El importe anual de dirección se prorratea como referencia, sin afirmar facturación mensual efectiva. Se mantienen fuera los subtotales genéricos y los conceptos suspendidos de mantenimiento o respaldo sin alcance independiente. La tabla no equivale a costos contratados o facturados.\n\nConstitución, cargas de contratación, costos residuales propios, recursos de uso alternativo y reposiciones carecen de valoración completa. Se registran como pendientes y no como cero real. La depreciación no se reconoce en el subtotal hasta definir el eventual aporte de equipos. Los CLP 6.240.000 de desarrollo valorizado tampoco se suman como pago inicial: se debe distinguir trabajo pasado, compromiso irreversible y trabajo incremental futuro.\n\n## H.33. Caja de referencia y necesidad de financiación\n\nLos costos identificados se proyectan mensualmente, con reajuste del 4 % anual para presupuestos CLP y costo AWS constante bajo el USD y cambio adoptados. La proyección no aplica créditos y no garantiza capacidad cloud para otros volúmenes. El IVA de comisión se reserva separado; el crédito por compras y las fechas efectivas de remisión permanecen pendientes. El impuesto del ejercicio se liquida al cierre anual por convención de la simulación, no como calendario fiscal real.\n\nEl caso de pago condicionado a fundadores utiliza solo excedente propio después de costos identificados, reserva de servicio de deuda y provisión académica de impuesto. Nunca utiliza préstamos, IVA o fondos de publicadores para activar la distribución. En la referencia agregada, el pago es cero durante el horizonte. Los escenarios con CLP 200.000 y CLP 1.000.000 efectivamente presupuestados por persona se calculan por separado, sin afirmar que exista caja para pagarlos. En el ejercicio se tratan como egreso de personal; la modalidad jurídica y la deducibilidad real se mantienen pendientes.\n\n**Tabla H.33.1**\n*Resultados operativos parciales del escenario agregado*\n\n'
    annex+=mdtable(['Año','Comisión neta CLP','Costos identificados CLP','Pago condicionado CLP','Flujo operativo parcial CLP'],[[str(a['anio_calendario']),money(a['comision_neta_clp']),money(a['opex_identificado_clp']),money(a['pago_fundadores_modelado_clp']),money(a['flujo_parcial_clp'])] for a in pure['anual']])
    annex+='\n*Nota.* Caso sin deuda, antes de partidas excluidas. La compra de equipos es cero; el lanzamiento presupuestado de CLP 1.200.000 figura en el Año 0 del flujo del cuerpo. La necesidad acumulada de financiación parcial, incluyendo ese lanzamiento, alcanza CLP '+money(pure['necesidad_financiacion_acumulada_parcial_clp'])+'. Es financiación de déficit persistente, no capital de trabajo del ciclo determinado. No se suma nuevamente al Año 0 además de las pérdidas operativas.\n\n**Tabla H.33.2**\n*Comparación parcial de los escenarios de demanda del insumo*\n\n'
    annex+=mdtable(['Escenario','Pagos mensuales','Ticket CLP','Comisión Año 1 CLP','VAN parcial al 12 % CLP'],[[a['escenario'],n(a['pagos_mes']),n(a['ticket_clp']),money(a['comision_neta_anual_1_clp']),money(a['van_parcial_12_clp'])] for a in load(MODEL/'sensibilidad_demanda_parcial.json')])
    annex+='\n*Nota.* Sin probabilidades atribuidas y sin ajuste de demanda para producir rentabilidad. El costo cloud y otros consumos deben reestimarse al cambiar el volumen; la comparación es un primer cálculo parcial, no una evaluación cerrada de capacidad o viabilidad.\n\n## H.34. Corrección de la deuda simulada\n\nSe calcula el préstamo de CLP 3.720.000 al 12 % anual y tres años con cuotas anuales, como el insumo. La cuota de referencia redondeada es CLP 1.548.818. La última cuota incorpora CLP 1 adicional para extinguir la deuda y conciliar capital amortizado con capital recibido. La simulación no acredita contratación, CAE, seguros ni comisiones.\n\n**Tabla H.34.1**\n*Amortización conciliada hasta saldo cero*\n\n'
    debt=load(MODEL/'deuda_corregida.json')
    annex+=mdtable(['Año','Saldo inicial CLP','Interés CLP','Amortización CLP','Cuota CLP','Saldo final CLP'],[[str(x['anio'])]+[n(x[k]) for k in ['saldo_inicial_clp','interes_clp','amortizacion_clp','cuota_clp','saldo_final_clp']] for x in debt])
    annex+='\n*Nota.* El principal amortizado totaliza CLP 3.720.000 y el saldo final es cero. La entrada del préstamo no se incluye como ingreso por comisiones. El flujo financiado del cuerpo presenta el efecto de la deuda y sus pagos.\n\n## H.35. Conciliación demostrativa de pérdidas históricas\n\nEsta comprobación conserva el 27 % y aplica el criterio de compensar pérdidas que describe el informe de Anita. Supone pérdidas iniciales cero y utiliza solo el EBT del bloque histórico corregido. No determina una base fiscal real ni reemplaza la conciliación del escenario actualizado.\n\n**Tabla H.35.1**\n*Impuesto histórico frente a compensación de pérdidas del ejercicio*\n\n'
    losses=load(MODEL/'conciliacion_perdidas_historicas.json')['filas']
    annex+=mdtable(['Año','EBT CLP','Pérdida compensada CLP','Impuesto fuente CLP','Impuesto recalculado CLP','Diferencia CLP'],[[str(x['periodo']),n(x['ebt_clp']),n(x['perdidas_utilizadas_clp']),n(x['impuesto_fuente_clp']),n(x['impuesto_academico_redondeado_clp']),n(x['diferencia_redondeada_clp'])] for x in losses])
    annex+='\n*Nota.* En el Año 2, CLP 1.232.610 menos CLP 956.400 deja una base de CLP 276.210. Al 27 %, el impuesto es CLP 74.576,70, redondeado a CLP 74.577. La diferencia con CLP 332.805 del origen es CLP 258.228. La corrección concilia la explicación con la tabla bajo este supuesto, sin alterar la extracción original.\n'
    annexpath.write_text(annex)
    # Informe breve del avance, fuera del texto académico.
    report='''# Primer corte de ejecución del plan Sapag

## Correcciones aplicadas

Se registra la respuesta del propietario: equipos existentes, sin compra inicial, y CLP 1.200.000 de lanzamiento como presupuesto provisional. Se construyen 48 meses de referencia comercial y caja y se conserva el reparto de comisión, IVA y fondos de terceros. No se inventa distribución entre las nueve categorías.

Se consolida el presupuesto identificado en CLP 514.083,02 mensuales, incorporando CLP 10.000 de útiles de oficina y CLP 12.500 de dirección tributaria. La periodicidad anual de esta última se ratifica por el propietario. El marketing operativo queda separado del presupuesto de lanzamiento. Los importes permanecen provisionales. Los umbrales por ticket de CLP 50.000 pasan de 728 a 743 pagos para CLP 200.000 por fundador y de 2.328 a 2.343 para CLP 1.000.000.

La deuda simulada se cierra en saldo cero mediante ajuste de CLP 1 en la última cuota. Se demuestra que la compensación de la pérdida histórica, bajo el criterio explicado por Anita y pérdidas iniciales cero, cambia el impuesto del Año 2 de CLP 332.805 a CLP 74.577. Los originales permanecen intactos.

## Proyección calculada y límites

La referencia conserva 16 pagos mensuales, ticket de CLP 50.000, comisión neta de CLP 24.000 por mes y sin crecimiento de volumen o ticket. Se aplica 4 % anual a presupuestos CLP del insumo y costo AWS bruto constante. Los créditos no se aplican sin validar su disponibilidad en los años de operación. La caja condicionada a excedente no activa pagos a fundadores en esta referencia.

Los flujos puro y financiado de partidas identificadas se presentan completos en el cuerpo conservando la estructura de Anita. No se describen como flujos definitivos: capital del ciclo, costos sin valoración, costo de oportunidad, reinversiones y valor de cierre siguen abiertos. El flujo puro parcial arroja VAN de CLP '''+money(pure['van_parcial_12_clp'])+''' al 12 %. No tiene TIR por presentar solo salidas. El financiado inicia con una entrada de préstamo y luego salidas, por lo que no se interpreta una tasa de financiación como rendimiento de inversión.

La necesidad acumulada de financiación parcial es CLP '''+money(pure['necesidad_financiacion_acumulada_parcial_clp'])+''', incluyendo el lanzamiento presupuestado. No se convierte en capital de trabajo adicional ni se suma de nuevo a la inversión inicial. La referencia actual no cubre sus costos identificados; esto no acredita una previsión de demanda ni una conclusión definitiva sobre un producto con otro volumen o estructura de costos.

## Entregables y reproducción

- parametros_ejecucion.json registra decisiones y exclusiones.
- matriz_categorias.json y CSV conserva el catálogo y los campos por completar.
- costos_conciliados.json registra las ocho partidas y su procedencia.
- proyeccion_mensual_2027_2030.csv y resumen_anual_2027_2030.csv contienen las memorias intermedias.
- resultados_proyeccion.json contiene seis perfiles: pago condicionado, meta inicial presupuestada y objetivo de un millón; cada uno puro y financiado.
- deuda_corregida y conciliacion_perdidas_historicas contienen las comprobaciones auxiliares.

Ejecutar scripts/ejecutar_modelo_sapag.py, recalcular los umbrales con scripts/calcular_tickets_remuneraciones.py y ejecutar scripts/verificar_modelo_sapag.py. scripts/actualizar_documento_ejecucion.py integra el corte en el borrador y anexos, y scripts/build_preview.py construye Word con DocSkill. La exportación y revisión visual del PDF se realiza con el flujo documental existente.

## Qué sigue abierto

Mezcla por categoría, adquisición y baja de oferta, ticket por modalidad, costos residuales y servicios pendientes, forma de remuneración, ciclo de liquidación e IVA de compras, valor de uso alternativo del trabajo y equipos, reposiciones y cierre. SP04–SP12 tienen avances calculados y no se marcan completos mientras dependan de esos datos. La tesis principal conserva sus reservas de integración.
'''
    (MODEL/'INFORME_DE_AVANCE.md').write_text(report)
    # Actualizar notas activas de umbrales, sin editar antecedentes de extracción o auditorías fechadas.
    (ROOT/'02_contraste/tickets_para_remuneraciones.md').write_text('# Tickets actualizados para remuneraciones\n\nEl primer corte añade CLP 120.000 anuales de útiles identificados en Conciliacion costos!H9 y CLP 150.000 anuales de dirección tributaria ratificados como presupuesto provisional. El presupuesto parcial mensual sin fundadores es CLP 514.083,02. A ticket de CLP 50.000 se requieren 743 pagos para CLP 200.000 por fundador y 2.343 para CLP 1.000.000. Los cálculos anteriores sin esa partida quedan como antecedentes.\n\nLa memoria activa es H.27, las Tablas 20 y 21 del cuerpo y los parámetros de umbrales. El alcance sigue siendo parcial y el costo variable propio se añade cuando se determine. El soporte del flujo se encuentra en 04_modelo_sapag/INFORME_DE_AVANCE.md.\n')
    from ampliar_revision_sapag import main as ampliar
    ampliar()
    print('Actualizados cuerpo y H.27/H.31–H.35, dos flujos parciales y memorias de ejecución.')

if __name__=='__main__':main()
