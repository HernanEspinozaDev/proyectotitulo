"""Indicadores anuales con clasificación explícita de signos y recuperación."""
from decimal import Decimal as D

def dec(x):return D(str(x))
def van(rate,flows):return sum(dec(f)/(1+dec(rate))**t for t,f in enumerate(flows))
def recuperacion(flows,rate=0):
    flows=list(map(dec,flows));rate=dec(rate)
    if not flows or flows[0]>=0:return None
    saldo=flows[0]
    for year,flow in enumerate(flows[1:],1):
        valor=flow/(1+rate)**year
        if saldo<0 and saldo+valor>=0:return dec(year-1)-saldo/valor
        saldo+=valor
    return None

def indicadores(flows,rate):
    flows=list(map(dec,flows));signs=[1 if f>0 else -1 for f in flows if f]
    changes=sum(a!=b for a,b in zip(signs,signs[1:]));tir=None
    if len(set(signs))<2:state='No existe TIR: la serie no combina entradas y salidas'
    elif signs[0]>0:state='Patrón de financiación; no se interpreta como rentabilidad de inversión'
    elif changes!=1:state='Múltiples cambios de signo; no se atribuye una TIR única sin analizar raíces'
    else:
        lo,hi=D('-.9999'),D(1)
        while van(hi,flows)>0:
            hi=hi*2+1
            if hi>D('1000000000'):raise ValueError('No se acota una raíz de TIR')
        for _ in range(100):
            mid=(lo+hi)/2
            if van(mid,flows)>0:lo=mid
            else:hi=mid
        tir=(lo+hi)/2;state='TIR única del flujo de inversión con un cambio de signo'
    return dict(van_clp=van(rate,flows),tasa_descuento=dec(rate),tir_anual=tir,tir_estado=state,
        cambios_signo=changes,recuperacion_simple_anios=recuperacion(flows),
        recuperacion_descontada_anios=recuperacion(flows,rate),
        convencion_recuperacion='interpolación lineal auxiliar entre cierres anuales; no fecha contractual ni cronograma mensual observado')
