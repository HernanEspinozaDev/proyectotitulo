"""Simulación adoptada: caja mensual, devengo, desfase y liquidación separados."""
from pathlib import Path
from decimal import Decimal as D,ROUND_CEILING
import copy,json
from ejecutar_modelo_sapag import q,amortizacion,impuesto_perdidas,dump,writecsv,cargar_costos
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'06_escenario_adoptado'
def parametros():return json.loads((OUT/'parametros.json').read_text())
def reparto(annual):
    annual=q(annual);piece=q(annual/12)
    return [piece]*11+[annual-11*piece]
def costos(p):
    rows=copy.deepcopy(cargar_costos(p))
    for row in rows:
        if row['id']=='C05':row.update(anual_1_clp=D(p['costos']['dominio_anual_clp']),mensual_1_clp=D(p['costos']['dominio_anual_clp'])/12,fuente='NIC Chile tarifas públicas, consulta 2026-11-16; hipótesis de continuidad para 2027')
    return rows

def valor_presente(rate,flows,times):return sum(D(str(f))/(1+D(str(rate)))**D(str(t)) for f,t in zip(flows,times))
def metricas(flows,times,rate):
    flows=list(map(lambda x:D(str(x)),flows));times=list(map(lambda x:D(str(x)),times));rate=D(str(rate))
    signs=[1 if f>0 else -1 for f in flows if f];changes=sum(a!=b for a,b in zip(signs,signs[1:]));irr=None
    if len(set(signs))<2:state='No existe TIR: todos los flujos no nulos tienen el mismo signo'
    elif not flows or flows[0]>=0:state='Patrón financiado no convencional; no se interpreta como retorno de inversión'
    elif changes!=1:state='Varios cambios de signo; no se informa una TIR única'
    elif all(f<=0 for f in flows[1:-1]):state='Operación neta negativa; la única entrada es liquidación de CxC y no se informa una TIR útil de inversión'
    else:
        lo,hi=D('-.9999'),D(1)
        while valor_presente(hi,flows,times)>0:hi=hi*2+1
        assert valor_presente(lo,flows,times)>0 and valor_presente(hi,flows,times)<=0, 'No se acota raíz de TIR'
        for _ in range(90):
            mid=(lo+hi)/2
            if valor_presente(mid,flows,times)>0:lo=mid
            else:hi=mid
        irr=(lo+hi)/2;state='TIR única de inversión, con liquidación diferida incluida'
    def payback(discount):
        if flows[0]>=0:return None
        balance=flows[0]
        for i in range(1,len(flows)):
            value=flows[i]/(1+discount)**times[i]
            if balance<0<=balance+value:return times[i-1]-balance/value*(times[i]-times[i-1])
            balance+=value
        return None
    return dict(van_con_liquidacion_clp=q(valor_presente(rate,flows,times)),tir_anual=irr,tir_estado=state,cambios_signo=changes,
        recuperacion_simple_anios=payback(D(0)),recuperacion_descontada_anios=payback(rate),
        convencion='cierres anuales más liquidación de comisión a 4 + días/360; recuperación interpolada entre momentos, no fecha de pago contractual')

def proyectar(p,cs=None,pagos=None,ticket=None,financiado=False,modo='condicionada',lag=None,reposicion=False,escala=D(1),valorizar=False,indicadores=True):
    cs=cs if cs is not None else costos(p)
    pay=D(str(pagos)) if pagos is not None else D(p['demanda']['espacios_promedio'])*D(p['demanda']['pagos_espacio_mes'])
    price=D(str(ticket)) if ticket is not None else D(p['demanda']['ticket_clp'])
    lag=D(str(lag if lag is not None else p['calendario']['dias_cobro_comision']));assert 0<=lag<=30
    ing=json.loads((ROOT/'02_contraste/parametros_ingresos.json').read_text());fee=D(ing['tarifa_indicada_usuario']);iva=D(ing['iva_referencia']);rate=D(p['tasa_descuento_nominal']);taxrate=D(p['tasa_impuesto_academica']);growth=D(p['costos']['reajuste_anual_presupuestos_clp'])
    loan=p['deuda_simulada'];debt=amortizacion(loan['principal_clp'],loan['interes_anual'],loan['anios']) if financiado else []
    initial=-D(p['lanzamiento']['presupuesto_clp'])-D(p['equipos']['compra_inicial_clp'])+(D(loan['principal_clp']) if financiado else 0)
    valuation=D(p['desarrollo_valorizado']['valor_total_preoperativo_clp']) if valorizar else D(0)
    cash=initial;cx=D(0);loss=D(0);months=[];years=[]
    for y in range(1,p['anios_operacion']+1):
        amounts={c['id']:q(D(c['anual_1_clp'])*((1+growth)**(y-1) if c['moneda_modelada']=='clp' else 1)*D(escala)) for c in cs}
        accrual={k:reparto(v) for k,v in amounts.items()}
        yearly_pay=pay*(1+D(p['demanda']['crecimiento_anual_cobros']))**(y-1);yearly_price=price*(1+D(p['demanda']['crecimiento_anual_ticket']))**(y-1)
        gmv=q(yearly_pay*yearly_price);revenue=q(gmv*fee);vat=q(revenue*iva)
        interest=debt[y-1]['interes_clp'] if y<=len(debt) else D(0);principal=debt[y-1]['amortizacion_clp'] if y<=len(debt) else D(0)
        target=D(p['fundadores']['cantidad'])*D(p['fundadores']['objetivo_alternativo_persona_clp'] if modo=='objetivo_millon' else p['fundadores']['meta_mensual_persona_clp'])
        period=[];cx_start=cx
        for m in range(1,13):
            accrued=sum(v[m-1] for v in accrual.values())
            paid=sum((amounts[k] if m==p['calendario']['mes_pago_anual'] else D(0)) if k in p['calendario']['meses_facturacion_anual'] else v[m-1] for k,v in accrual.items())
            previous_cx=cx;cx=q(revenue*lag/30);received=revenue+previous_cx-cx
            replacement=q(p['reposicion']['estres_compra_clp']) if reposicion and y==p['reposicion']['anio_estres'] and m==p['reposicion']['mes_estres'] else D(0)
            reserved=D(p['reposicion']['reserva_interna_mes_clp']) if reposicion and (y-1)*12+m<=p['reposicion']['meses_reserva'] else D(0)
            provision_with=q(max(revenue-accrued-target-interest/12,D(0))*taxrate)
            capacity=received-paid-(interest+principal)/12-provision_with-reserved
            if modo=='sin_asignaciones':wage=D(0)
            elif modo in ('meta_200000','objetivo_millon'):wage=target
            else:wage=target if capacity>=target else D(0)
            provision=q(max(revenue-accrued-wage-interest/12,D(0))*taxrate)
            row=dict(periodo=(y-1)*12+m,fecha=f'{p["anio_1"]+y-1}-{m:02}',anio_operacion=y,gmv_clp=gmv,pagos_mes=yearly_pay,ticket_clp=yearly_price,
                comision_neta_devengada_clp=revenue,comision_neta_cobrada_clp=received,iva_comision_restringido_clp=vat,
                saldo_publicadores_antes_pasarela_clp=gmv-revenue-vat,tarifa_pasarela=None,abono_final_publicadores_clp=None,
                cxc_inicial_clp=previous_cx,cxc_final_clp=cx,variacion_cxc_clp=cx-previous_cx,
                opex_devengado_clp=accrued,opex_pagado_clp=paid,meta_fundadores_clp=target,pago_fundadores_clp=wage,
                provision_impuesto_regla_pago_clp=provision,reserva_deuda_regla_pago_clp=(interest+principal)/12,
                reserva_reposicion_regla_pago_clp=reserved,capacidad_mensual_para_meta_clp=capacity,
                interes_pagado_clp=interest if m==12 else D(0),principal_pagado_clp=principal if m==12 else D(0),
                compra_reposicion_clp=replacement,impuesto_pagado_clp=D(0))
            period.append(row)
        ebit=sum(r['comision_neta_devengada_clp']-r['opex_devengado_clp']-r['pago_fundadores_clp'] for r in period)
        taxes=impuesto_perdidas(ebit-interest,loss,taxrate);loss=taxes['perdidas_finales_clp'];period[-1]['impuesto_pagado_clp']=taxes['impuesto_clp']
        for row in period:
            row['flujo_caja_clp']=row['comision_neta_cobrada_clp']-row['opex_pagado_clp']-row['pago_fundadores_clp']-row['interes_pagado_clp']-row['principal_pagado_clp']-row['compra_reposicion_clp']-row['impuesto_pagado_clp']
            cash+=row['flujo_caja_clp'];row['caja_sin_aportes_clp']=cash;months.append(row)
        years.append(dict(periodo=y,anio=p['anio_1']+y-1,gmv_clp=12*gmv,comision_neta_devengada_clp=12*revenue,
            comision_neta_cobrada_clp=sum(r['comision_neta_cobrada_clp'] for r in period),iva_comision_restringido_clp=12*vat,
            opex_devengado_clp=sum(amounts.values()),opex_pagado_clp=sum(r['opex_pagado_clp'] for r in period),
            administracion_marketing_clp=sum(v for k,v in amounts.items() if k in ('C03','C04','C08')),
            pago_fundadores_clp=sum(r['pago_fundadores_clp'] for r in period),ebit_clp=ebit,interes_clp=interest,amortizacion_deuda_clp=principal,
            variacion_cxc_clp=cx-cx_start,cxc_final_clp=cx,compra_reposicion_clp=sum(r['compra_reposicion_clp'] for r in period),**taxes,
            flujo_caja_clp=sum(r['flujo_caja_clp'] for r in period),caja_final_sin_aportes_clp=cash))
    annual=[initial-valuation]+[y['flujo_caja_clp'] for y in years]
    settlement=cx;when=D(p['anios_operacion'])+lag/360
    flows=annual+[settlement] if settlement else annual
    times=list(map(D,range(len(annual))))+([when] if settlement else [])
    metrics=metricas(flows,times,rate) if indicadores else dict(van_con_liquidacion_clp=q(valor_presente(rate,flows,times)))
    monthly_pv=initial-valuation+sum(r['flujo_caja_clp']/(1+rate)**(D(r['periodo'])/12) for r in months)+settlement/(1+rate)**when
    aporte=max(-initial,D(0));saldo=initial+aporte;contrib=aporte
    funds=[dict(periodo=0,fecha='2026-12',flujo_caja_clp=initial,reserva_objetivo_clp=D(0),aporte_minimo_clp=aporte,caja_con_aportes_clp=saldo,aportes_acumulados_clp=contrib)]
    reserve_debt=D(0);reserve_repl=D(0)
    for row in months:
        reserve_debt+=row['reserva_deuda_regla_pago_clp']-row['interes_pagado_clp']-row['principal_pagado_clp']
        reserve_repl+=row['reserva_reposicion_regla_pago_clp']-row['compra_reposicion_clp']
        # La última cuota consume la reserva anual; evita residuos por división /12.
        if row['periodo']%12==0:reserve_debt=D(0)
        if reposicion and row['periodo']==p['reposicion']['meses_reserva']:reserve_repl=D(0)
        floor=q(max(reserve_debt,D(0))+max(reserve_repl,D(0)))
        add=max(floor-(saldo+row['flujo_caja_clp']),D(0));contrib+=add;saldo+=row['flujo_caja_clp']+add
        funds.append(dict(periodo=row['periodo'],fecha=row['fecha'],flujo_caja_clp=row['flujo_caja_clp'],reserva_objetivo_clp=floor,aporte_minimo_clp=add,caja_con_aportes_clp=saldo,aportes_acumulados_clp=contrib))
    return dict(alcance='simulación adoptada sobre partidas identificadas, sin confirmar demanda o contratos',modo=modo,financiado=financiado,lag_dias=lag,reposicion=reposicion,valoracion_no_desembolsable_clp=valuation,
        flujo_anual_operacion_clp=annual,anual=years,mensual=months,flujos_indicadores_clp=flows,momentos_indicadores_anios=times,indicadores=metrics,
        van_operacion_sin_liquidacion_clp=q(valor_presente(rate,annual,range(len(annual)))),van_mensual_control_clp=q(monthly_pv),
        liquidacion=dict(fecha_referencia='2031-01',dias_despues_horizonte=lag,momento_anios=when,cobro_cxc_clp=settlement,venta_activos_clp=D(0),venta_software_clp=D(0),caja_final_con_aportes_clp=saldo+settlement),
        aportes=funds,aporte_minimo_acumulado_clp=contrib,
        capital_ciclo_comision_clp=cx,capital_ciclo_completo_clp=None,
        advertencia='CxC ya incluida mediante menores cobros; no se agrega de nuevo al Año 0. La recuperación posterior no es venta ni ingreso por operación de un quinto año.')

def umbral(p,mode,valorizar=False):
    lo,hi=0,4096
    def evaluate(n):
        m=proyectar(p,pagos=n,modo=mode,valorizar=valorizar,indicadores=False)
        return valor_presente(p['tasa_descuento_nominal'],m['flujos_indicadores_clp'],m['momentos_indicadores_anios'])
    while evaluate(hi)<0:hi*=2
    while lo<hi:
        mid=(lo+hi)//2
        if evaluate(mid)>=0:hi=mid
        else:lo=mid+1
    return dict(modo=mode,recupera_valorizacion=valorizar,pagos_mes=lo,van_anterior_clp=q(evaluate(lo-1)),van_minimo_clp=q(evaluate(lo)))

def main():
    p=parametros();cs=costos(p);dump(OUT/'costos.json',cs);writecsv(OUT/'costos.csv',cs)
    outputs={}
    for mode in ['condicionada','meta_200000','objetivo_millon']:
        for fin in [False,True]:outputs[mode+('_financiado' if fin else '_puro')]=proyectar(p,cs,financiado=fin,modo=mode)
    outputs['estres_reposicion']=proyectar(p,cs,reposicion=True)
    outputs['estres_cobro30']=proyectar(p,cs,lag=30)
    dump(OUT/'resultados.json',outputs)
    for key,m in outputs.items():
        writecsv(OUT/f'mensual_{key}.csv',m['mensual']);writecsv(OUT/f'anual_{key}.csv',m['anual']);writecsv(OUT/f'aportes_{key}.csv',m['aportes'])
    roots=[umbral(p,mode,v) for v in [False,True] for mode in ['sin_asignaciones','meta_200000','objetivo_millon']]
    for root in roots:
        m=proyectar(p,cs,pagos=root['pagos_mes'],modo=root['modo'],valorizar=root['recupera_valorizacion'])
        root['indicadores']=m['indicadores'];root['flujos_clp']=m['flujos_indicadores_clp'];root['momentos_anios']=m['momentos_indicadores_anios']
    dump(OUT/'umbrales_van.json',roots)
    base=outputs['condicionada_puro'];payroll=[]
    for ticket in [20000,50000,100000,200000]:
        avg=sum(c['anual_1_clp'] for c in cs)/12;unit=D(ticket)*D('.03')
        payroll.append(dict(ticket_clp=ticket,comision_unitaria_clp=unit,pagos_promedio_meta_200000=int(((avg+600000)/unit).to_integral_value(rounding=ROUND_CEILING)),pagos_promedio_meta_millon=int(((avg+3000000)/unit).to_integral_value(rounding=ROUND_CEILING))))
    dump(OUT/'umbrales_operativos_promedio.json',payroll)
    # Sensibilidades univariables, desde la misma referencia y con liquidación.
    sensitivity=[];basevan=base['indicadores']['van_con_liquidacion_clp']
    for variable in ['pagos','ticket','costos','cambio']:
        for factor in [D('.8'),D('1.2')]:
            changed=copy.deepcopy(cs)
            if variable=='cambio':
                for c in changed:
                    if c['moneda_modelada']=='aws':c['anual_1_clp']*=factor
            m=proyectar(p,changed,pagos=D(16)*factor if variable=='pagos' else None,ticket=D(50000)*factor if variable=='ticket' else None,escala=factor if variable=='costos' else D(1),indicadores=False)
            value=m['indicadores']['van_con_liquidacion_clp'];sensitivity.append(dict(variable=variable,variacion_pct=(factor-1)*100,van_con_liquidacion_clp=value,diferencia_base_clp=value-basevan))
    for rate in [D('.10'),D('.12'),D('.25')]:
        value=q(valor_presente(rate,base['flujos_indicadores_clp'],base['momentos_indicadores_anios']));sensitivity.append(dict(variable='descuento',variacion_pct=rate*100,van_con_liquidacion_clp=value,diferencia_base_clp=value-basevan))
    dump(OUT/'sensibilidad.json',sensitivity)
    coverage=[]
    for row in outputs['condicionada_financiado']['anual']:
        service=row['interes_clp']+row['amortizacion_deuda_clp'];capacity=row['comision_neta_cobrada_clp']-row['opex_pagado_clp']-row['pago_fundadores_clp']-row['impuesto_clp']
        coverage.append(dict(anio=row['anio'],caja_antes_cuota_clp=capacity,cuota_clp=service,cobertura=capacity/service if service else None))
    dump(OUT/'cobertura_deuda.json',coverage)
    inputs=json.loads((ROOT/'02_contraste/parametros_ingresos.json').read_text())
    commercial=[]
    for c in inputs['escenarios']:
        count=D(c['espacios'])*D(c['reservas_espacio_mes'])
        m=proyectar(p,cs,pagos=count,ticket=c['ticket_comisionable_clp'],indicadores=False)
        commercial.append(dict(escenario=c['escenario'],pagos_mes=count,ticket_clp=c['ticket_comisionable_clp'],comision_anual_1_clp=m['anual'][0]['comision_neta_devengada_clp'],van_con_liquidacion_clp=m['indicadores']['van_con_liquidacion_clp']))
    dump(OUT/'escenarios_comerciales_anita.json',commercial)

    summary=dict(subtotal_mensual_prorrateado_clp=sum(c['anual_1_clp'] for c in cs)/12,subtotal_anual_1_clp=sum(c['anual_1_clp'] for c in cs),
        cxc_supuesto_base_clp=base['capital_ciclo_comision_clp'],van_base_con_liquidacion_clp=basevan,aportes_minimos_base_clp=base['aporte_minimo_acumulado_clp'],
        enero_opex_clp=base['mensual'][0]['opex_pagado_clp'],enero_comision_cobrada_clp=base['mensual'][0]['comision_neta_cobrada_clp'],
        reposicion_efecto_van_clp=outputs['estres_reposicion']['indicadores']['van_con_liquidacion_clp']-basevan,
        dias30_efecto_van_clp=outputs['estres_cobro30']['indicadores']['van_con_liquidacion_clp']-basevan,
        raiz_sin_asignaciones=roots[0]['pagos_mes'],raiz_meta_200000=roots[1]['pagos_mes'],raiz_meta_millon=roots[2]['pagos_mes'])
    dump(OUT/'resumen.json',summary);print(json.dumps(summary,ensure_ascii=False,indent=2,default=str))
if __name__=='__main__':main()
