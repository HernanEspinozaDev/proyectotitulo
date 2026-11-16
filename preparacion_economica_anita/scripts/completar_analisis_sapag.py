"""Completa cálculos disponibles de liquidez, cobertura, indicadores y cierre.

Mantiene las exclusiones sin cuantificar. No transforma estos cálculos en prueba
comercial, oferta de financiación ni tasación de valor de desecho.
"""
from pathlib import Path
from decimal import Decimal as D
import json
from ejecutar_modelo_sapag import construir_proyeccion,cargar_costos,dump,writecsv,q,npv
from indicadores_sapag import indicadores
from ampliar_revision_sapag import money,table
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'04_modelo_sapag'
def load(name):return json.loads((OUT/name).read_text())

def calendario_aportes(model):
    # Aporte inicial y posteriores solo cuando el saldo propio cae bajo cero.
    saldo=D(model['flujo_anual'][0]);initial=max(-saldo,D(0));saldo+=initial;total=initial
    rows=[dict(periodo=0,fecha='2026-12',flujo_parcial_clp=D(model['flujo_anual'][0]),aporte_minimo_adicional_clp=initial,caja_con_aportes_clp=saldo,aportes_acumulados_clp=total)]
    for row in model['mensual']:
        flow=D(row['flujo_parcial_clp']);aporte=max(-(saldo+flow),D(0));saldo+=flow+aporte;total+=aporte
        rows.append(dict(periodo=row['periodo'],fecha=row['fecha'][:7],flujo_parcial_clp=flow,aporte_minimo_adicional_clp=aporte,caja_con_aportes_clp=saldo,aportes_acumulados_clp=total))
    assert total==D(model['necesidad_financiacion_acumulada_parcial_clp'])
    return rows

def construir():
    params=load('parametros_ejecucion.json');models=load('resultados_proyeccion.json');rev=load('revision_coherencia_y_sensibilidad.json')
    funding={};annual=[]
    for key in ['condicionada_puro','condicionada_financiado']:
        rows=calendario_aportes(models[key]);funding[key]=rows;writecsv(OUT/f'aportes_minimos_{key}.csv',rows)
    for year in range(5):
        def subtotal(key):return sum(r['aporte_minimo_adicional_clp'] for r in funding[key] if (r['periodo']-1)//12+1==year)
        annual.append(dict(anio=2026+year,aporte_minimo_puro_clp=subtotal('condicionada_puro'),aporte_minimo_financiado_clp=subtotal('condicionada_financiado')))
    coverage=[]
    for a in models['condicionada_financiado']['anual']:
        available=D(a['comision_neta_clp'])-D(a['opex_identificado_clp'])-D(a['pago_fundadores_modelado_clp'])-D(a['impuesto_clp'])
        service=D(a['interes_clp'])+D(a['amortizacion_deuda_clp'])
        coverage.append(dict(anio=a['anio_calendario'],caja_propia_antes_deuda_clp=available,servicio_deuda_clp=service,cobertura_caja_sobre_cuota=available/service if service else None,
            estado='sin generación propia para atender la cuota' if service and available<service else ('sin cuota de deuda' if not service else 'cuota cubierta bajo partidas identificadas')))
    rates=D(params['tasa_descuento_nominal']);cycles=[]
    netfee=D(models['condicionada_puro']['mensual'][0]['comision_neta_clp'])
    for days in [0,7,30]:
        tied=netfee*D(days)/30
        cycles.append(dict(dias_supuesto=days,comision_por_cobrar_clp=tied,inversion_inicial_auxiliar_clp=-tied,recuperacion_auxiliar_anio4_clp=tied,efecto_van_clp=-tied+tied/(1+rates)**4,
            alcance='solo cuentas por cobrar de comisión neta con mes de 30 días y cobros uniformes; no capital de trabajo completo ni plazo del proveedor confirmado'))
    metrics=[]
    for label,key in [('Base sin deuda','condicionada_puro'),('Base con deuda','condicionada_financiado')]:
        m=models[key];metrics.append(dict(escenario=label,pagos_mes=D(16),modo=m['modo'],financiado=m['financiado'],flujo_anual=m['flujo_anual'],**indicadores(m['flujo_anual'],rates)))
    # Primer cruce dentro del tramo sin asignaciones: no se bisecciona la regla
    # condicionada completa, que presenta saltos cuando se activa el pago.
    costs=cargar_costos(params);lo=0;hi=rev['umbrales_anuales'][0]['pagos_meta_200000']-1
    assert construir_proyeccion(params,costs,pagos_mes=hi)['van_parcial_12_clp']>=0
    while lo<hi:
        mid=(lo+hi)//2
        if construir_proyeccion(params,costs,pagos_mes=mid)['van_parcial_12_clp']>=0:hi=mid
        else:lo=mid+1
    no_wage=construir_proyeccion(params,costs,pagos_mes=lo)
    assert all(a['pago_fundadores_modelado_clp']==0 for a in no_wage['anual'])
    assert construir_proyeccion(params,costs,pagos_mes=lo-1)['van_parcial_12_clp']<0
    metrics.append(dict(escenario='Quiebre sin asignaciones',pagos_mes=lo,modo='condicionada',financiado=False,flujo_anual=no_wage['flujo_anual'],**indicadores(no_wage['flujo_anual'],rates)))
    for root in rev['quiebres_van']:
        count=root['pagos_mes_enteros'];mode=root['modo'];m=construir_proyeccion(params,cargar_costos(params),pagos_mes=count,modo=mode)
        metrics.append(dict(escenario='Meta CLP '+money(200000 if mode=='meta_200000' else 1000000)+' por persona',pagos_mes=count,modo=mode,financiado=False,flujo_anual=m['flujo_anual'],**indicadores(m['flujo_anual'],rates)))
    # Cobro terminal NETO adicional requerido para neutralizar el VAN del subtotal.
    terminal=-npv(rates,models['condicionada_puro']['flujo_anual'])*(1+rates)**params['anios_operacion']
    result=dict(alcance='cálculos disponibles de la evaluación parcial; no cierre comercial ni valoración legal',financiacion_mensual=funding,financiacion_anual=annual,cobertura_deuda=coverage,
        sensibilidad_cuentas_cobrar=cycles,indicadores=metrics,cobro_terminal_neto_para_van_cero_clp=terminal,
        valor_terminal_estimado_clp=None,capital_trabajo_completo_clp=None,
        advertencia_terminal='umbral algebraico, no tasación ni venta esperada; no se agrega al flujo activo')
    dump(OUT/'liquidez_indicadores_y_cierre.json',result)
    writecsv(OUT/'aportes_minimos_anuales.csv',annual);writecsv(OUT/'cobertura_deuda.csv',coverage)
    writecsv(OUT/'sensibilidad_cuentas_por_cobrar.csv',cycles)
    return result

def main():
    r=construir();bodypath=ROOT/'03_propuesta/capitulo_xiv_borrador.md';annexpath=ROOT/'03_propuesta/anexo_h_tablas_fuente.md'
    body=bodypath.read_text().split('### 14.7. Capacidad de pago')[0].rstrip()+'\n\n'
    annex=annexpath.read_text().split('## H.37.')[0].rstrip()+'\n\n'
    body+='''### 14.7. Capacidad de pago y necesidades de financiación

La capacidad de atender obligaciones se evalúa separada de la rentabilidad del proyecto y de los socios, de acuerdo con la distinción metodológica de Sapag Chain y Sapag Chain (2008, pp. 5–6, 297–298). El préstamo simulado aporta liquidez al inicio, pero no convierte las comisiones insuficientes en generación operativa. La caja disponible antes de pagar cuotas es negativa en los tres años con servicio de deuda. El indicador auxiliar de cobertura divide esa caja por intereses más principal; un resultado inferior a uno evidencia insuficiencia de generación propia bajo las partidas identificadas. H.37.2 contiene el cálculo.

El calendario de financiación aplica aportes adicionales solo cuando el saldo de caja pasa a ser negativo. El aporte inicial del caso puro cubre el lanzamiento. En el caso financiado se utiliza primero el excedente inicial del préstamo. Se calcula el aporte mínimo necesario para sostener caja no negativa; no se afirma que los socios dispongan de esos recursos ni que el financiamiento esté contratado.

**Tabla 22**
*Necesidades adicionales de financiación del subtotal por año*

'''
    body+=table(['Año','Aporte mínimo sin deuda CLP','Aporte mínimo con deuda CLP'],[[x['anio'],money(x['aporte_minimo_puro_clp']),money(x['aporte_minimo_financiado_clp'])] for x in r['financiacion_anual']]+[['Total',money(sum(x['aporte_minimo_puro_clp'] for x in r['financiacion_anual'])),money(sum(x['aporte_minimo_financiado_clp'] for x in r['financiacion_anual']))]])
    body+='''
*Nota.* Elaboración con el calendario prorrateado del caso base y cuota anual del insumo. El caso financiado ya incorpora el préstamo de CLP 3.720.000: los aportes adicionales no vuelven a sumar esa entrada. El resultado refleja el déficit persistente de las partidas identificadas, sin asignarlo nuevamente al Año 0 como capital de trabajo recuperable. El capital propio requerido no equivale al trabajo valorizado ni a fondos de publicadores. H.37.1 contiene los 49 momentos de cada escenario, incluido el momento cero.

### 14.8. Conclusión de la evaluación delimitada y condiciones de cierre

La referencia de 16 pagos mensuales no cubre los costos identificados, no activa remuneraciones ni recupera el lanzamiento en cuatro años. El flujo puro carece de TIR por presentar solo egresos netos. La entrada inicial del caso financiado no se interpreta como inversión convencional de los socios; los resultados históricos de Anita no se trasladan al corte vigente.

El primer quiebre parcial sin asignaciones se obtiene con 391 pagos mensuales de CLP 50.000; la regla condicionada no activa remuneraciones durante el horizonte. Los quiebres de 791 y 2.391 pagos presupuestan las metas completas de CLP 200.000 y CLP 1.000.000 por persona. H.38 presenta su TIR y recuperación simple y descontada. El margen de VAN es reducido antes de costos excluidos y no acredita demanda, capacidad técnica ni viabilidad integral.

El horizonte conserva cuatro años por la estructura docente. No se presume una perpetuidad ni una venta de activos sin valoración. H.39 documenta el procedimiento de cierre y las entradas pendientes: mezcla comercial, recursos aportados, costos completos, liquidaciones, reposiciones y valor final. El déficit persistente no se recupera como si fuera un activo. El análisis calculable queda ejecutado; la conclusión integral y la integración a la tesis requieren completar esos antecedentes, conservando la autoría económica de Anita.
'''
    annex+='''## H.37. Liquidez y memoria del déficit acumulado

### H.37.1. Aportes mínimos y déficit persistente

Se recorre el saldo mensual con lanzamiento, operación y deuda, cuando corresponde. Si el saldo antes de aporte es negativo, el aporte mínimo es su valor absoluto; si es positivo, el aporte es cero. La caja de cierre después del aporte se mantiene no negativa. La suma de aportes coincide con el déficit acumulado máximo antes de aportes. Se conservan los 49 momentos en aportes_minimos_condicionada_puro.csv y aportes_minimos_condicionada_financiado.csv. El cálculo distingue necesidad de financiación de pérdidas de capital de trabajo del ciclo (Sapag Chain & Sapag Chain, 2008, pp. 267–269).

**Tabla H.37.1**
*Conciliación de la financiación adicional acumulada*

'''
    rows=[]
    for key,label in [('condicionada_puro','Sin deuda'),('condicionada_financiado','Con deuda simulada')]:
        items=r['financiacion_mensual'][key]
        rows.append([label,money(items[0]['aporte_minimo_adicional_clp']),money(items[-1]['aportes_acumulados_clp']),money(items[-1]['caja_con_aportes_clp'])])
    annex+=table(['Escenario','Aporte adicional Año 0 CLP','Aportes adicionales totales CLP','Caja final tras aportes CLP'],rows)
    annex+='''
*Nota.* El aporte inicial de cero en la alternativa financiada se explica por el préstamo que excede el lanzamiento identificado. No significa ausencia de inversión o de aportes posteriores. Los aportes son una necesidad calculada, no un compromiso confirmado de los socios. El excedente prestado no es utilidad ni habilita remuneraciones por sí solo.

### H.37.2. Cobertura de las cuotas de deuda

**Tabla H.37.2**
*Caja propia frente al servicio de la deuda simulada*

'''
    annex+=table(['Año','Caja antes de cuota CLP','Intereses y principal CLP','Cobertura veces'],[[x['anio'],money(x['caja_propia_antes_deuda_clp']),money(x['servicio_deuda_clp']),money(x['cobertura_caja_sobre_cuota'],3) if x['cobertura_caja_sobre_cuota'] is not None else 'No aplica'] for x in r['cobertura_deuda']])
    annex+='''
*Nota.* La caja propia antes de cuota resta OPEX, asignaciones pagadas e impuesto académico de las comisiones netas. No incluye préstamo, aportes nuevos, IVA ni arriendos de terceros. La razón es un diagnóstico auxiliar; no se afirma que una entidad financiera apruebe el préstamo. La falta de cuota en 2030 no elimina el déficit operativo.

### H.37.3. Sensibilidad aislada de la comisión por cobrar

**Tabla H.37.3**
*Efecto auxiliar de inmovilizar comisión neta por distintos plazos*

'''
    annex+=table(['Días ilustrativos','Comisión por cobrar CLP','Efecto en VAN CLP'],[[x['dias_supuesto'],money(x['comision_por_cobrar_clp']),money(x['efecto_van_clp'],2)] for x in r['sensibilidad_cuentas_cobrar']])
    annex+='''
*Nota.* Se utiliza la comisión neta de CLP 24.000 mensuales y un mes de 30 días, con cobros uniformes. Los plazos 0, 7 y 30 días son pruebas, no condiciones de Mercado Pago. El stock auxiliar se aporta en el Año 0 y se recupera íntegro en el Año 4 para aislar su efecto: variación del VAN = menos stock más stock descontado al cierre. No se aplica este ajuste al caso activo ni se identifica como capital completo del ciclo. Faltan pagos anticipados, plazos de proveedores, IVA de compras y devoluciones. El IVA recaudado y los fondos de publicadores se excluyen de caja libre.

## H.38. Indicadores y recuperación de los escenarios delimitados

Se calcula VAN con momento cero sin descuento y cierres anuales al 12 %. La TIR solo se informa como rentabilidad cuando existe un flujo de inversión con un cambio de signo. Una serie de egresos no tiene TIR; una entrada inicial seguida de pagos corresponde a otro patrón y no se presenta como rentabilidad de los socios. La recuperación simple acumula importes nominales y la descontada acumula importes descontados (Sapag Chain & Sapag Chain, 2008, pp. 321–323, 329–330).

**Tabla H.38.1**
*VAN y TIR de la referencia y los quiebres parciales*

'''
    annex+=table(['Escenario','Pagos al mes','VAN parcial CLP','TIR anual'],[[x['escenario'],money(x['pagos_mes']),money(x['van_clp'],2),money(D(x['tir_anual'])*100,4)+' %' if x['tir_anual'] is not None else ('No existe' if not x['financiado'] else 'No interpretable como inversión')] for x in r['indicadores']])
    annex+='''
*Nota.* El quiebre sin asignaciones es el primer entero con VAN no negativo antes de activarse la meta conjunta: se comprueba que con 390 pagos el VAN es negativo y con 391 no lo es. Los otros dos quiebres presuponen asignaciones completas como egreso académico; no reemplazan la decisión de pago condicionado del caso base. Sus flujos se conservan en liquidez_indicadores_y_cierre.json. El costo identificado no se reestima por volumen en estas pruebas, por lo que los resultados excluyen escalamiento, capital completo del ciclo, oportunidad y cierre. El VAN positivo de unos pocos miles de pesos no constituye margen para absorber partidas desconocidas. No se asume costo económico cero del trabajo por carecer de pago.

**Tabla H.38.2**
*Recuperación simple y descontada de las series anuales*

'''
    annex+=table(['Escenario','Simple en años','Descontada en años'],[[x['escenario'],money(x['recuperacion_simple_anios'],3) if x['recuperacion_simple_anios'] is not None else ('No se recupera' if not x['financiado'] else 'No aplica al patrón'),money(x['recuperacion_descontada_anios'],3) if x['recuperacion_descontada_anios'] is not None else ('No se recupera' if not x['financiado'] else 'No aplica al patrón')] for x in r['indicadores']])
    annex+='''
*Nota.* Se interpola linealmente entre cierres anuales para expresar fracciones de año. Esa interpolación no identifica una fecha contractual ni sustituye la convención anual del VAN. No se trasladan estas recuperaciones al caso comercial de 16 pagos ni se confunde recuperación nominal con cumplimiento de la tasa de descuento.

## H.39. Horizonte y condiciones para cerrar la evaluación integral

### H.39.1. Método de cierre y límite del cálculo

El caso de referencia conserva cuatro años de operación. El procedimiento requiere inventariar activos y derechos efectivamente atribuibles al proyecto, su uso alternativo, vida remanente y posibles desembolsos de reposición. Después se estima un valor comercial neto de realización con respaldo o, si existe una proyección sostenible posterior, se evalúa un valor de continuidad que no duplique recuperaciones ya incluidas. El libro distingue métodos contable, comercial y económico; el valor contable no acredita por sí solo dinero de venta (Sapag Chain & Sapag Chain, 2008, pp. 277–282, 292–295).

'''
    annex+='Para que un único cobro terminal neto adicional en el Año 4 neutralice el VAN del subtotal base, se requiere CLP '+money(r['cobro_terminal_neto_para_van_cero_clp'],2)+'. Se obtiene multiplicando el valor absoluto del VAN por (1 + 0,12) elevado a cuatro. Este umbral algebraico no tasa equipos, software o empresa; no demuestra la existencia de comprador ni de flujos posteriores. No se incorpora a las Tablas 18 y 19 como ingreso esperado.\n\n'
    annex+='''### H.39.2. Datos y decisiones que no se sustituyen por supuestos confirmados

El cierre comercial requiere ratificar distribución de espacios, pagos, ticket y estacionalidad entre las nueve categorías. La referencia agregada no inventa ventas por categoría. El desglose de CLP 1.200.000 de lanzamiento debe aclarar si incluye trámites de constitución para evitar duplicarlos.

El desarrollo valorizado se separa en trabajo pasado, compromisos irreversibles y trabajo incremental futuro. Los equipos existentes no generan nueva compra; se precisa su propiedad, aporte y uso alternativo antes de asignar depreciación o valor de cierre. Ausencia de pago no equivale a costo de oportunidad cero.

Antes de integrar se precisan costos y condiciones de proveedores, pasarela, devoluciones, retenciones, liquidaciones y formalización de asignaciones. Se conserva el impuesto académico del 27 % sin afirmar liquidación fiscal real. Con esas entradas se recalculan flujos, capital del ciclo, indicadores y conclusión. La preparación mantiene las reservas de la tesis principal y las secciones de planificación de Erick.
'''
    bodypath.write_text(body);annexpath.write_text(annex)
    report=OUT/'INFORME_DE_AVANCE.md'
    text=report.read_text().split('## Tercer corte de liquidez')[0].rstrip()
    pure=r['financiacion_mensual']['condicionada_puro'][-1]['aportes_acumulados_clp']
    financed=r['financiacion_mensual']['condicionada_financiado'][-1]['aportes_acumulados_clp']
    metric=r['indicadores'][2]
    text+='\n\n## Tercer corte de liquidez e indicadores\n\nSe completan dos calendarios de 49 momentos, aportes mínimos y cobertura de deuda. La referencia requiere CLP '+money(pure,2)+' de aportes sin deuda y CLP '+money(financed,2)+' adicionales al préstamo con deuda. La diferencia corresponde a intereses, no a una eliminación del déficit.\n\n'
    text+='Se evalúan cinco series. El primer quiebre parcial sin asignaciones es '+money(metric['pagos_mes'])+' pagos mensuales de CLP 50.000. Sus indicadores y los de las metas presupuestadas se presentan en H.38. Se calculan TIR y recuperación solo donde corresponde al patrón de flujos. Los costos omitidos, escalamiento y demanda no se dan por confirmados.\n\n'
    text+='H.39 documenta el cierre; el cobro terminal neto de CLP '+money(r['cobro_terminal_neto_para_van_cero_clp'],2)+' solo es un umbral algebraico y no se incorpora como valor esperado. La cadena reproducible es scripts/reconstruir_preparacion_sapag.py; el material continúa separado de la tesis principal hasta conciliar las entradas.\n'
    report.write_text(text)
    from ratificar_preoperacion_sapag import main as ratificar
    ratificar()
    print('Liquidez, cobertura, cuentas por cobrar, indicadores y procedimiento de cierre integrados en 14.7–14.8 y H.37–H.39.')

if __name__=='__main__':main()
