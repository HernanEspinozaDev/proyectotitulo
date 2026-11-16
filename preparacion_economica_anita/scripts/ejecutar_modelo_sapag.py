"""Prepara proyecciones parciales y conciliaciones desde fuentes intactas de Anita.

Los JSON y CSV son memorias intermedias del informe Word, no un libro de Excel
reconstruido ni una liquidación fiscal. Los costos sin valoración quedan fuera del
subtotal y se conservan como pendientes explícitos.
"""
from pathlib import Path
from decimal import Decimal as D, ROUND_HALF_UP
import csv,json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'04_modelo_sapag'
CENT=D('.01')
PESO=D('1')

def dec(x): return D(str(x))
def q(x): return dec(x).quantize(CENT, rounding=ROUND_HALF_UP)
def peso(x): return dec(x).quantize(PESO,rounding=ROUND_HALF_UP)
def dump(path,obj):
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2,default=lambda v:format(v,'f') if isinstance(v,D) else str(v))+'\n')
def writecsv(path,rows,headers=None):
    if not rows:return
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=headers or list(rows[0]),lineterminator='\n');w.writeheader()
        for row in rows:w.writerow({k:format(v,'f') if isinstance(v,D) else v for k,v in row.items()})
def readcsv(name):
    with (ROOT/'01_extraccion/excel'/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.reader(f))
def cargar_costos(params=None):
    params=params or json.loads((OUT/'parametros_ejecucion.json').read_text())
    base=readcsv('03-base-mensual-valores.csv')
    byname={row[0]:row for row in base if row}
    con=readcsv('05-conciliacion-costos-valores.csv')
    utiles=next(row for row in con if row and row[0]=='Útiles de oficina')
    aws=json.loads((ROOT/'02_contraste/parametros_aws.json').read_text())
    specs=[('C01','AWS','aws','infraestructura',dec(aws['clp_anuales_brutos']),'parametros_aws.json; USD 26,41 × 972 × 12'),('C02','Firma y API','clp','suscripción presupuestada',dec(byname['FirmaVirtual/API'][1])*12,'Base mensual!B21'),('C03','Marketing','clp','presupuesto de captación',dec(params['costos']['marketing_presupuesto_base_mensual_clp'])*12,'Base mensual!B22; presupuesto operativo ratificado'),('C04','Contabilidad','clp','servicio presupuestado',dec(byname['Contabilidad'][1])*12,'Base mensual!B23'),('C05','Dominio','clp','renovación anual prorrateada',dec(byname['Dominio'][1])*12,'Base mensual!B24'),('C06','Coordinación','clp','viajes presupuestados',dec(byname['Viajes coordinación'][1])*12,'Base mensual!B25'),('C07','Útiles de oficina','clp','presupuesto auxiliar',dec(utiles[7]),'Conciliacion costos!H9; importe anual 120000')]
    specs.append(('C08','Dirección tributaria','clp','servicio presupuestado',dec(params['costos']['oficina_virtual_anual_clp']),'periodicidad anual ratificada por propietario; importe de la conciliación de Anita'))
    return [dict(id=a,concepto=b,moneda_modelada=c,tipo=d,anual_1_clp=e,mensual_1_clp=e/12,fuente=f,estado='presupuesto provisional identificado; no contrato o factura verificados') for a,b,c,d,e,f in specs]

def amortizacion(principal,tasa,anios):
    principal,tasa=dec(principal),dec(tasa)
    cuota=peso(principal*tasa/(1-(1+tasa)**(-anios))) if tasa else peso(principal/anios)
    saldo=principal;rows=[]
    for year in range(1,anios+1):
        interes=peso(saldo*tasa)
        pago=cuota if year<anios else saldo+interes
        capital=pago-interes
        rows.append(dict(anio=year,saldo_inicial_clp=saldo,interes_clp=interes,amortizacion_clp=capital,cuota_clp=pago,saldo_final_clp=saldo-capital,ajuste_ultima_cuota_clp=pago-cuota))
        saldo-=capital
    return rows

def impuesto_perdidas(ebt,perdida_inicial,tasa):
    ebt,loss,tasa=dec(ebt),dec(perdida_inicial),dec(tasa)
    usada=min(max(ebt,D(0)),loss)
    base=max(ebt-usada,D(0))
    return dict(ebt_clp=ebt,perdidas_iniciales_clp=loss,perdidas_utilizadas_clp=usada,base_academica_clp=base,impuesto_clp=q(base*tasa),perdidas_finales_clp=loss-usada+max(-ebt,D(0)))

def npv(rate,flows):return sum(dec(x)/(1+dec(rate))**i for i,x in enumerate(flows))

def construir_proyeccion(params,costos,pagos_mes=None,ticket=None,financiado=False,modo='condicionada',escala_costos=D(1)):
    d=params['demanda'];pay=dec(pagos_mes if pagos_mes is not None else dec(d['espacios_promedio'])*dec(d['pagos_espacio_mes']))
    ticket=dec(ticket if ticket is not None else d['ticket_clp'])
    ingresos=json.loads((ROOT/'02_contraste/parametros_ingresos.json').read_text());com=dec(ingresos['tarifa_indicada_usuario']);iva=dec(ingresos['iva_referencia']);tax=dec(params['tasa_impuesto_academica']);growth=dec(params['costos']['reajuste_anual_presupuestos_clp'])
    loan=params['deuda_simulada'];deuda=amortizacion(loan['principal_clp'],loan['interes_anual'],loan['anios']) if financiado else []
    initial=-dec(params['lanzamiento']['presupuesto_clp'])-dec(params['equipos']['compra_inicial_clp'])+(dec(loan['principal_clp']) if financiado else D(0))
    cash=initial;loss=D(0);annual=[];monthly=[];years=params['anios_operacion'];meta=dec(params['fundadores']['cantidad'])*dec(params['fundadores']['meta_mensual_persona_clp']);objetivo=dec(params['fundadores']['cantidad'])*dec(params['fundadores']['objetivo_alternativo_persona_clp'])
    for year in range(1,years+1):
        pagos=pay*(1+dec(d['crecimiento_anual_cobros']))**(year-1);price=ticket*(1+dec(d['crecimiento_anual_ticket']))**(year-1)
        gmv=pagos*price;revenue=gmv*com;vat=revenue*iva
        op=q(sum(c['anual_1_clp']/12*((1+growth)**(year-1) if c['moneda_modelada']=='clp' else 1) for c in costos)*escala_costos)
        interests=deuda[year-1]['interes_clp'] if financiado and year<=len(deuda) else D(0)
        principal=deuda[year-1]['amortizacion_clp'] if financiado and year<=len(deuda) else D(0)
        cuota=interests+principal
        candidato=meta if modo!='objetivo_millon' else objetivo
        available=revenue-op
        taxreserve=max(available-candidato-interests/12,D(0))*tax
        wage=candidato if modo in ('meta_200000','objetivo_millon') or available-cuota/12-taxreserve>=candidato else D(0)
        ebit=12*(revenue-op-wage)
        t=impuesto_perdidas(ebit-interests,loss,tax);loss=t['perdidas_finales_clp']
        period_rows=[]
        for month in range(1,13):
            interest_cash=interests if month==12 else D(0);debt_cash=principal if month==12 else D(0);tax_cash=t['impuesto_clp'] if month==12 else D(0)
            fnc=revenue-op-wage-interest_cash-debt_cash-tax_cash
            cash+=fnc
            row=dict(periodo=(year-1)*12+month,fecha=f"{params['anio_1']+year-1}-{month:02d}-01",anio_operacion=year,espacios_referencia=d['espacios_promedio'],pagos_mes=pagos,ticket_clp=price,gmv_clp=gmv,comision_neta_clp=revenue,iva_comision_restringido_clp=vat,cargo_comision_total_clp=revenue+vat,saldo_publicadores_antes_pasarela_clp=gmv-revenue-vat,tarifa_pasarela=None,abono_final_publicadores_clp=None,opex_identificado_clp=op,meta_fundadores_clp=candidato,pago_fundadores_modelado_clp=wage,interes_pagado_clp=interest_cash,principal_pagado_clp=debt_cash,impuesto_academico_pagado_clp=tax_cash,flujo_parcial_clp=fnc,caja_acumulada_sin_aportes_adicionales_clp=cash,costos_pendientes_adicionales=None)
            monthly.append(row);period_rows.append(row)
        yearrow=dict(periodo=year,anio_calendario=params['anio_1']+year-1,gmv_clp=12*gmv,comision_neta_clp=12*revenue,iva_comision_clp=12*vat,opex_identificado_clp=12*op,meta_fundadores_clp=12*candidato,pago_fundadores_modelado_clp=12*wage,ebit_clp=ebit,interes_clp=interests,amortizacion_deuda_clp=principal,**t,flujo_parcial_clp=sum(x['flujo_parcial_clp'] for x in period_rows),caja_final_parcial_clp=cash)
        annual.append(yearrow)
    flows=[initial]+[a['flujo_parcial_clp'] for a in annual]
    cumulative=initial;acc=[]
    for i,f in enumerate(flows):cumulative+=f if i else 0;acc.append(cumulative)
    signs=[1 if x>0 else -1 for x in flows if x]
    irrstate='No existe TIR con entradas y salidas de signos opuestos' if len(set(signs))<2 else ('No se interpreta como rentabilidad de inversión: entrada inicial y salidas posteriores' if signs[0]>0 else 'Requiere cálculo e interpretación de TIR del flujo de inversión')
    return dict(alcance='subtotal de caja de partidas identificadas; no flujo financiero definitivo',modo=modo,financiado=financiado,flujo_anual=flows,anual=annual,mensual=monthly,van_parcial_12_clp=q(npv(params['tasa_descuento_nominal'],flows)),tir_estado=irrstate,recuperacion_simple='No se identifica recuperación de inversión en la serie parcial' if flows[0]<0 and not any(x>=0 for x in acc[1:]) else 'No interpretable como recuperación de inversión convencional',necesidad_financiacion_acumulada_parcial_clp=max(D(0),-min([initial]+[x['caja_acumulada_sin_aportes_adicionales_clp'] for x in monthly])),capital_trabajo_ciclo_clp=None,valor_cierre_clp=None,partidas_sin_valorar=params['exclusiones_no_valoradas'])

def main():
    params=json.loads((OUT/'parametros_ejecucion.json').read_text());costos=cargar_costos();dump(OUT/'costos_conciliados.json',dict(partidas=costos,total_anual_1_clp=sum(x['anual_1_clp'] for x in costos),total_mensual_1_clp=sum(x['mensual_1_clp'] for x in costos),estado_total='parcial; partidas sin valoración fuera del subtotal'))
    writecsv(OUT/'costos_identificados.csv',costos)
    pendiente=[dict(id='P02',concepto='Costos legales y de constitución',importe=None,motivo='sin desglose, no duplicar contabilidad'),dict(id='P03',concepto='Cargas de contratación',importe=None,motivo='sin modalidad ni base definidas'),dict(id='P04',concepto='Costo residual de pasarela',importe=None,motivo='regla comercial a cargo del publicador, tarifa e implementación pendientes'),dict(id='P05',concepto='Capital de trabajo del ciclo',importe=None,motivo='desfase de liquidación y pagos pendientes'),dict(id='P06',concepto='Reposición y cierre',importe=None,motivo='equipos existentes, aportes y continuidad sin valoración')]
    dump(OUT/'partidas_pendientes.json',pendiente)
    categories=['Oficina','Sala multipropósito','Bodega','Estacionamiento','Local flexible','Stand','Quincho','Parcela de eventos','Inmuebles']
    cat=[dict(id=i,categoria=c,publicadores_activos=None,espacios_promedio=None,pagos_por_espacio_mes=None,ticket_clp=None,peso_modalidad_hora=None,peso_modalidad_dia=None,peso_modalidad_mes=None,estado='categoría vigente; mezcla y volúmenes por ratificar') for i,c in enumerate(categories,1)]
    dump(OUT/'matriz_categorias.json',cat);writecsv(OUT/'matriz_categorias.csv',cat)
    resources=[dict(recurso='Tres notebooks y un teléfono',valor_fuente_clp=dec(params['equipos']['valor_fuente_clp']),desembolso_inicial_clp=D(0),estado='existentes, sin compra inicial confirmado por propietario',aporte_oportunidad_pendiente=True),dict(recurso='Preparación y lanzamiento',valor_fuente_clp=dec(params['lanzamiento']['presupuesto_clp']),desembolso_inicial_clp=dec(params['lanzamiento']['presupuesto_clp']),estado='presupuesto provisional ratificado; desglose y tratamiento pendientes',aporte_oportunidad_pendiente=False),dict(recurso='Desarrollo valorizado',valor_fuente_clp=D(6240000),desembolso_inicial_clp=None,estado='no sumar como pago por el solo hecho de estar valorizado; separar pasado y trabajo incremental futuro',aporte_oportunidad_pendiente=True)]
    dump(OUT/'inversion_clasificada.json',resources)
    deuda=amortizacion(**dict(principal=params['deuda_simulada']['principal_clp'],tasa=params['deuda_simulada']['interes_anual'],anios=params['deuda_simulada']['anios']));dump(OUT/'deuda_corregida.json',deuda);writecsv(OUT/'deuda_corregida.csv',deuda)
    loss=D(0);hist=[]
    for year,(ebt,original) in enumerate(zip([-956400,1232610,3708132,7367748],[0,332805,1001196,1989292]),1):
        t=impuesto_perdidas(ebt,loss,params['tasa_impuesto_academica']);loss=t['perdidas_finales_clp'];hist.append(dict(periodo=year,**t,impuesto_academico_redondeado_clp=peso(t['impuesto_clp']),impuesto_fuente_clp=original,diferencia_redondeada_clp=dec(original)-peso(t['impuesto_clp'])))
    dump(OUT/'conciliacion_perdidas_historicas.json',dict(alcance='demostración bajo compensación de pérdidas que describe Anita, con pérdidas iniciales cero; no nueva liquidación legal',filas=hist));writecsv(OUT/'conciliacion_perdidas_historicas.csv',hist)
    outputs={}
    for modo in ['condicionada','meta_200000','objetivo_millon']:
        for fin in [False,True]:
            key=modo+('_financiado' if fin else '_puro');m=construir_proyeccion(params,costos,financiado=fin,modo=modo);outputs[key]=m
    dump(OUT/'resultados_proyeccion.json',outputs)
    model=outputs['condicionada_puro'];writecsv(OUT/'proyeccion_mensual_2027_2030.csv',model['mensual']);writecsv(OUT/'resumen_anual_2027_2030.csv',model['anual'])
    sensitivity=[]
    inputs=json.loads((ROOT/'02_contraste/parametros_ingresos.json').read_text())
    for c in inputs['escenarios']:
        pay=dec(c['espacios'])*dec(c['reservas_espacio_mes']);m=construir_proyeccion(params,costos,pagos_mes=pay,ticket=c['ticket_comisionable_clp']);sensitivity.append(dict(escenario=c['escenario'],pagos_mes=pay,ticket_clp=c['ticket_comisionable_clp'],comision_neta_anual_1_clp=m['anual'][0]['comision_neta_clp'],pago_fundadores_anual_1_clp=m['anual'][0]['pago_fundadores_modelado_clp'],van_parcial_12_clp=m['van_parcial_12_clp']))
    dump(OUT/'sensibilidad_demanda_parcial.json',sensitivity)
    summary={'alcance':'primer corte de ejecución con datos identificados y exclusiones explícitas','pagos_mes':model['mensual'][0]['pagos_mes'],'gmv_mes_clp':model['mensual'][0]['gmv_clp'],'comision_neta_mes_clp':model['mensual'][0]['comision_neta_clp'],'iva_comision_mes_restringido_clp':model['mensual'][0]['iva_comision_restringido_clp'],'opex_parcial_mes_clp':sum(x['mensual_1_clp'] for x in costos),'meta_fundadores_mes_clp':dec(params['fundadores']['cantidad'])*dec(params['fundadores']['meta_mensual_persona_clp']),'utiles_anuales_incorporados_clp':D(120000),'inversion_equipos_desembolso_clp':dec(params['equipos']['compra_inicial_clp']),'lanzamiento_presupuestado_clp':dec(params['lanzamiento']['presupuesto_clp']),'fundadores_pagados_anual_base_clp':model['anual'][0]['pago_fundadores_modelado_clp'],'van_parcial_puro_12_clp':model['van_parcial_12_clp'],'necesidad_financiacion_acumulada_parcial_clp':model['necesidad_financiacion_acumulada_parcial_clp'],'capital_trabajo_ciclo_clp':None,'advertencia':'el déficit persistente se presenta como necesidad de financiación, no se carga de nuevo al Año 0 como capital de trabajo además de las pérdidas operativas'}
    dump(OUT/'resumen_ejecucion.json',summary)
    from calcular_tickets_remuneraciones import calcular
    dump(ROOT/'02_contraste/umbrales_remuneraciones.json',calcular(params['fundadores']['meta_mensual_persona_clp']))
    dump(ROOT/'02_contraste/umbral_sueldo_objetivo.json',calcular(params['fundadores']['objetivo_alternativo_persona_clp']))
    print(json.dumps(summary,ensure_ascii=False,indent=2,default=str))

if __name__=='__main__':main()
