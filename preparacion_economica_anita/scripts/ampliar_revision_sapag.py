"""Segundo corte Sapag: sensibilidades deterministas y coherencia cuerpo/anexo.

No estima demanda ni tarifas ni reemplaza partidas desconocidas por ceros.
Las metas presupuestadas son alternativas de evaluación, no nuevas decisiones.
"""
from pathlib import Path
from decimal import Decimal as D, ROUND_CEILING
import copy, json, re
from ejecutar_modelo_sapag import cargar_costos, construir_proyeccion, npv, q, dump, writecsv
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'04_modelo_sapag'

def load(name): return json.loads((OUT/name).read_text())
def money(v,decimals=0):
    return f'{D(str(v)):,.{decimals}f}'.replace(',','X').replace('.',',').replace('X','.')
def table(headers,rows):
    return '| '+' | '.join(headers)+' |\n|'+'|'.join('---' for _ in headers)+'|\n'+''.join('| '+' | '.join(map(str,r))+' |\n' for r in rows)
def ceil(v): return int(v.to_integral_value(rounding=ROUND_CEILING))
def van(params,costs,pay,mode):
    return npv(params['tasa_descuento_nominal'],construir_proyeccion(params,costs,pagos_mes=pay,modo=mode)['flujo_anual'])

def raiz_pagos(params,costs,mode):
    # Las metas fijas evitan la discontinuidad del pago condicionado de fundadores.
    lo,hi=D(0),D(16)
    while van(params,costs,hi,mode)<0:
        hi*=2
        if hi>D('100000000'): raise ValueError('No se acota un cruce bajo las partidas identificadas')
    for _ in range(65):
        mid=(lo+hi)/2
        if van(params,costs,mid,mode)<0:lo=mid
        else:hi=mid
    entero=ceil(hi)
    prev=van(params,costs,D(entero-1),mode);current=van(params,costs,D(entero),mode)
    assert prev<0<=current
    return dict(modo=mode,pagos_mes_teoricos=(lo+hi)/2,pagos_mes_enteros=entero,
                van_pago_anterior_clp=q(prev),van_pago_minimo_clp=q(current),
                interpretacion='quiebre parcial de VAN anual; sin costos de escalamiento, capital del ciclo, oportunidad ni cierre')

def construir_revision():
    params=load('parametros_ejecucion.json');costs=cargar_costos(params)
    base=construir_proyeccion(params,costs);basevan=npv(params['tasa_descuento_nominal'],base['flujo_anual'])
    pay=D(params['demanda']['espacios_promedio'])*D(params['demanda']['pagos_espacio_mes']);ticket=D(params['demanda']['ticket_clp'])
    rows=[]
    for variable in ['pagos','ticket','costos','cambio']:
        for factor in [D('.8'),D('1.2')]:
            altered=copy.deepcopy(costs)
            if variable=='cambio':
                for c in altered:
                    if c['moneda_modelada']=='aws':
                        c['anual_1_clp']*=factor;c['mensual_1_clp']*=factor
            model=construir_proyeccion(params,altered,pagos_mes=pay*factor if variable=='pagos' else pay,
                ticket=ticket*factor if variable=='ticket' else ticket,
                escala_costos=factor if variable=='costos' else D(1))
            result=npv(params['tasa_descuento_nominal'],model['flujo_anual'])
            rows.append(dict(variable=variable,variacion_pct=(factor-1)*100,van_parcial_clp=q(result),diferencia_base_clp=q(result-basevan)))
    for rate in [D('.10'),D('.12'),D('.25')]:
        result=npv(rate,base['flujo_anual'])
        rows.append(dict(variable='descuento',variacion_pct=rate*100,van_parcial_clp=q(result),diferencia_base_clp=q(result-basevan)))
    roots=[raiz_pagos(params,costs,mode) for mode in ['meta_200000','objetivo_millon']]
    threshold=[]
    candidate=construir_proyeccion(params,costs,pagos_mes=743)
    for a in base['anual']:
        op=D(a['opex_identificado_clp'])/12
        threshold.append(dict(anio=a['anio_calendario'],opex_mes_parcial_clp=op,
            pagos_meta_200000=ceil((op+D('600000'))/(ticket*D('.03'))),
            pagos_objetivo_millon=ceil((op+D('3000000'))/(ticket*D('.03'))),
            pago_condicionado_743_mes_clp=candidate['anual'][a['periodo']-1]['pago_fundadores_modelado_clp']/12))
    rate=D(params['tasa_descuento_nominal']);monthly_rate=(1+rate)**(D(1)/12)-1
    monthlyvan=D(base['flujo_anual'][0])+sum(D(x['flujo_parcial_clp'])/(1+rate)**(D(x['periodo'])/12) for x in base['mensual'])
    timing=dict(tasa_anual=rate,tasa_mensual_equivalente=monthly_rate,
        van_convencion_cierre_anual_clp=q(basevan),van_convencion_fin_mes_clp=q(monthlyvan),
        diferencia_clp=q(monthlyvan-basevan),
        alcance='contraste temporal del subtotal prorrateado; no calendario real ni capital de trabajo validado')
    result=dict(alcance='segundo corte parcial, determinista y sin probabilidades asignadas',
        tasa_base=rate,caso_base_pagos_mes=pay,ticket_clp=ticket,
        sensibilidades=rows,quiebres_van=roots,umbrales_anuales=threshold,temporalidad=timing,
        exclusiones=params['exclusiones_no_valoradas'])
    dump(OUT/'revision_coherencia_y_sensibilidad.json',result)
    writecsv(OUT/'sensibilidad_univariable.csv',rows)
    writecsv(OUT/'umbrales_anuales.csv',threshold)
    return result

def main():
    data=construir_revision()
    bodypath=ROOT/'03_propuesta/capitulo_xiv_borrador.md';annexpath=ROOT/'03_propuesta/anexo_h_tablas_fuente.md'
    body=bodypath.read_text();annex=annexpath.read_text()
    # Los antecedentes se conservan identificados. Se corrige el estado del corte activo.
    body=body.replace('El flujo puro complementario requiere un recálculo completo en el cuerpo, con impuesto y financiamiento consistentes; no se obtiene únicamente borrando el interés.',
        'Las Tablas 18 y 19 presentan el recálculo parcial vigente, separado de este antecedente. La evaluación definitiva aún requiere cerrar las partidas no determinadas; el flujo puro no se obtiene únicamente borrando el interés.')
    body=body.replace('La sustitución AWS debe propagarse por costos, resultados, capital de trabajo y caja después de conciliar las decisiones comerciales y financieras.',
        'La Tabla 17 conserva el modelo de origen con GCP y comisión del 14 %, exclusivamente como antecedente comparativo. Las Tablas 18 a 21 y los anexos H.31 a H.36 contienen el corte vigente con AWS y comisión del 3 %. El capital de trabajo y el cierre permanecen sin determinar.')
    body=body.replace('La sensibilidad evalúa el efecto de cobros, ticket, costos, tipo de cambio, rezagos y tasa sobre el VAN y determina puntos de quiebre desde un caso base único.',
        'La sensibilidad calcula el efecto individual de cobros, ticket, costos, tipo de cambio y tasa sobre el VAN desde un caso base único. Los rezagos efectivos de liquidación quedan pendientes hasta conocer sus condiciones.')
    original='La evaluación compara volumen de reservas, ticket, comisión, remuneración, pasarela e infraestructura.'
    a=body.index(original if original in body else 'El segundo corte aplica variaciones individuales')
    b=body.index('### 14.6.',a)
    roots=data['quiebres_van']
    body=body[:a]+'''El segundo corte aplica variaciones individuales de menos y más 20 % en cobros, ticket y costos identificados. La variación cambiaria afecta únicamente al componente AWS expresado en USD. También compara descuentos del 10 %, 12 % y 25 % sin reemplazar la tasa base del 12 %. Estos rangos son pruebas deterministas seleccionadas para observar sensibilidad; no son intervalos de confianza ni probabilidades de ocurrencia. H.36.1 presenta los resultados y sus límites.

Como la referencia solo contiene salidas netas, un descuento mayor vuelve el VAN menos negativo al reducir el valor presente de esas salidas. Ello no significa que un 25 % reduzca el riesgo o mejore la operación. El ticket nominal permanece constante por decisión del caso de referencia, mientras los presupuestos CLP aumentan 4 % anual; se explicita esta asimetría sin presentarla como una estimación validada de inflación o demanda.

El quiebre del VAN parcial se calcula por separado con asignaciones fijas presupuestadas, evitando la discontinuidad del pago condicionado. Con ticket constante de CLP 50.000, el primer entero mensual que produce VAN parcial no negativo es '''+money(roots[0]['pagos_mes_enteros'])+''' para CLP 200.000 por fundador y '''+money(roots[1]['pagos_mes_enteros'])+''' para CLP 1.000.000. Es un cálculo sobre costos identificados constantes respecto del volumen y no acredita capacidad técnica, captación o rentabilidad definitiva. H.36.3 muestra el contraste con el entero inmediatamente anterior.

Los cobros mensuales representan pagos procesados; no equivalen a personas únicas ni a contratos. La cantidad de publicadores depende de los espacios por publicador y de la recurrencia. No existe una cifra única de usuarios deducible de estos umbrales sin definir esa mezcla.

'''+body[b:]
    body=body.replace('Los anexos H.27 y H.31–H.35 respaldan los cálculos y su alcance.',
        'Los anexos H.27 y H.31–H.36 respaldan los cálculos y su alcance. Los 743 y 2.343 pagos son umbrales operativos parciales del Año 1; no incluyen el lanzamiento, la deuda ni la recuperación exigida por el VAN. El reajuste de costos eleva las cantidades de los años siguientes, como muestra H.36.2. Con 743 pagos constantes, la regla condicionada solo permite la meta inicial en el primer año bajo las partidas identificadas.')
    # Convención docente de VAN anual explícita frente al cronograma mensual prorrateado.
    key='El formato del flujo de Anita se conserva como estructura rectora, con indicadores posteriores a la tabla completa.'
    timing=data['temporalidad']
    note=' El cálculo rector descuenta cada subtotal anual al cierre del año. El contraste de H.36.4 descuenta los importes mensuales prorrateados al final de cada mes con la tasa mensual equivalente a 12 % anual. Se mantienen ambas convenciones identificadas y no se comparan sus VAN como si emplearan las mismas fechas.'
    body=body.replace(note,'')
    body=body.replace(key,key+' El cálculo rector descuenta cada subtotal anual al cierre del año. El contraste de H.36.4 descuenta los importes mensuales prorrateados al final de cada mes con la tasa mensual equivalente a 12 % anual. Se mantienen ambas convenciones identificadas y no se comparan sus VAN como si emplearan las mismas fechas.')
    if '## H.36.' in annex:annex=annex[:annex.index('## H.36.')].rstrip()+'\n'
    annex+='''
## H.36. Coherencia y sensibilidad del segundo corte

La comprobación conserva la comisión neta del 3 %, la tasa de descuento base del 12 %, el impuesto académico del 27 % y los cuatro años 2027 a 2030. Cada sensibilidad cambia un solo parámetro y mantiene los demás. Los cambios de menos y más 20 % son rangos exploratorios definidos en esta revisión; no provienen de distribuciones observadas ni expresan certeza estadística. El caso base mantiene 16 cobros de CLP 50.000 al mes y pago condicionado cero.

**Tabla H.36.1**
*Sensibilidad individual del VAN parcial del caso base*

'''
    names={'pagos':'Cobros mensuales','ticket':'Ticket medio','costos':'Costos identificados','cambio':'CLP por USD','descuento':'Tasa de descuento'}
    rows=[]
    for x in data['sensibilidades']:
        label=money(x['variacion_pct'])+' %'+(' anual' if x['variable']=='descuento' else ' de variación')
        rows.append([names[x['variable']],label,money(x['van_parcial_clp']),money(x['diferencia_base_clp'])])
    annex+=table(['Variable','Prueba','VAN parcial CLP','Cambio del VAN CLP'],rows)
    annex+='''
*Nota.* Elaboración mediante el modelo reproducible. Valores redondeados a pesos para presentación. La variación cambiaria afecta solo a AWS; la de costos afecta a las ocho partidas identificadas. No se modifican el lanzamiento ni la comisión. Se mantienen las exclusiones del corte base. Un VAN menos negativo al elevar la tasa sobre flujos de salida no acredita menor riesgo. No se estiman costos cloud de escalamiento ni efectos de demanda cruzados.

**Tabla H.36.2**
*Umbrales operativos parciales por año sin deuda*

'''
    annex+=table(['Año','Costo mensual CLP','Pagos para $200.000 por persona','Pagos para $1.000.000 por persona'],[[x['anio'],money(x['opex_mes_parcial_clp']),money(x['pagos_meta_200000']),money(x['pagos_objetivo_millon'])] for x in data['umbrales_anuales']])
    annex+='''
*Nota.* Ticket de CLP 50.000, comisión de CLP 1.500 por pago y tres personas. El costo mensual es un prorrateo presupuestario, no una fecha contractual de pago. Los útiles, la dirección tributaria y el dominio no acreditan facturación mensual. La meta se mantiene nominal constante y los costos CLP se reajustan 4 %. La regla de pago condicionado a 743 cobros activa CLP 600.000 al mes solo en el Año 1 y cero en los demás. Los umbrales cubren costos y asignaciones del año; no incorporan recuperación del lanzamiento, deuda, costos omitidos ni VAN cero.

**Tabla H.36.3**
*Quiebre del VAN anual parcial con asignaciones presupuestadas constantes*

'''
    annex+=table(['Meta por persona CLP','Pagos mensuales mínimos','VAN con un pago menos CLP','VAN con el mínimo CLP'],[[money(200000 if x['modo']=='meta_200000' else 1000000),money(x['pagos_mes_enteros']),money(x['van_pago_anterior_clp']),money(x['van_pago_minimo_clp'])] for x in roots])
    annex+='''
*Nota.* Búsqueda numérica del volumen mensual uniforme a ticket de CLP 50.000. Se presupuestan las asignaciones completas como gasto académico, con independencia de que el escenario disponga de caja; no se cambia la decisión de pago condicionado. El flujo es puro, el Año 0 incluye CLP 1.200.000 de lanzamiento, el impuesto académico considera compensación de pérdidas y el VAN se descuenta al 12 % al cierre de cada año. El cálculo redondea hacia arriba el cruce y verifica los dos enteros adyacentes. El costo identificado no aumenta por volumen en esta prueba; antes de una decisión comercial se deben valorar escalamiento, recursos de oportunidad, cargas de contratación, capital del ciclo y cierre. El resultado no es una meta de captación validada.

### H.36.4. Convenciones de fechas y límites de cierre

'''
    annex+='La tasa mensual equivalente es (1 + 0,12) elevado a 1/12 menos 1, equivalente a '+money(D(timing['tasa_mensual_equivalente'])*100,6)+' %. El VAN anual rector del subtotal puro es CLP '+money(timing['van_convencion_cierre_anual_clp'],2)+'. Si los importes prorrateados se ubican al final de cada mes, el VAN es CLP '+money(timing['van_convencion_fin_mes_clp'],2)+', diferencia de CLP '+money(timing['diferencia_clp'],2)+'. Se informa el contraste porque adelantar egresos modifica su valor presente. No se reemplaza el formato anual docente ni se afirma que el prorrateo sea un calendario efectivo de caja.\n\n'
    annex+='''Los flujos vigentes se vinculan con las Tablas 18 a 21, H.27 y H.31 a H.36. Las Tablas 15 a 17 y H.1 a H.26 preservan los antecedentes recibidos; sus valores GCP, tasas o inversiones anteriores no constituyen decisiones activas. La reconstrucción conserva su contenido para la comparación solicitada.

El caso base no presenta recuperación simple ni descontada dentro de los cuatro años: sus flujos propios son negativos. El valor de cierre y el capital del ciclo siguen sin cuantificarse. El cierre no adopta cero como valor económico definitivo ni convierte automáticamente el déficit persistente en capital de trabajo recuperable. La conclusión se limita al subtotal modelado; la evaluación integral continúa abierta conforme a los criterios de Sapag.
'''
    bodypath.write_text(body);annexpath.write_text(annex)
    # La nota activa también se genera desde la memoria de umbrales, no desde cifras antiguas.
    initial=json.loads((ROOT/'02_contraste/umbrales_remuneraciones.json').read_text())
    target=json.loads((ROOT/'02_contraste/umbral_sueldo_objetivo.json').read_text())
    def at50(data):return next(x['pagos_mes'] for x in data['metas_por_ticket'] if x['ticket_medio_clp']==50000)
    (ROOT/'02_contraste/tickets_para_remuneraciones.md').write_text('# Tickets actualizados para remuneraciones\n\nEl subtotal del primer año es CLP '+money(initial['costos_parciales_sin_fundadores_aws_clp'],2)+' mensuales sin fundadores. A ticket de CLP 50.000, los umbrales operativos parciales son '+money(at50(initial))+' pagos para CLP 200.000 por persona y '+money(at50(target))+' para CLP 1.000.000.\n\nSe mantienen tres personas, comisión del 3 %, marketing separado del lanzamiento, útiles y dirección tributaria anual. H.36 diferencia estos umbrales del Año 1, los de años siguientes y los quiebres de VAN. No equivalen a usuarios únicos ni incluyen costos pendientes o escalamiento por volumen.\n')
    report=OUT/'INFORME_DE_AVANCE.md'
    text=report.read_text().split('## Segundo corte de coherencia')[0].rstrip()
    text+='\n\n## Segundo corte de coherencia y sensibilidad\n\nSe corrige la persistencia de 2.335 pagos en el generador: la cifra activa de la meta de un millón es 2.343 en el Año 1. Se explicitan los antecedentes frente al escenario vigente, la fecha de descuento y el prorrateo de costos. El generador conserva los parámetros de reajuste e inversión, sin asumir un porcentaje distinto del modelo.\n\nSe agregan once pruebas univariables, umbrales por año, dos cruces de VAN parcial y contraste temporal mensual/anual. H.36 y la sección 14.5 documentan métodos y límites. SP12 avanza, sin declararse completo mientras falten costos, demanda validada y rezagos.\n'
    report.write_text(text)
    print('Segundo corte: sensibilidad, quiebres de VAN, umbrales anuales y coherencia integrados en H.36.')

if __name__=='__main__': main()
