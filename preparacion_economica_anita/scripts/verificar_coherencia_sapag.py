"""Auditoría terminal independiente de memorias, Markdown y Word económico."""
from pathlib import Path
from decimal import Decimal as D
import hashlib,json,math,re,subprocess,zipfile
from lxml import etree
ROOT=Path(__file__).resolve().parents[1]

def load(name):return json.loads((ROOT/'04_modelo_sapag'/name).read_text())
def fmt(v):return f'{D(str(v)):,.0f}'.replace(',','.')
def parse(v):return D(v.replace('.','').replace(',','.'))
def main():
    rev=load('revision_coherencia_y_sensibilidad.json');models=load('resultados_proyeccion.json');params=load('parametros_ejecucion.json')
    body=(ROOT/'03_propuesta/capitulo_xiv_borrador.md').read_text();annex=(ROOT/'03_propuesta/anexo_h_tablas_fuente.md').read_text()
    # Comprobaciones independientes con flujos convencionales y supuestos académicos.
    def independent_van(pay,wage):
        loss=0.;flows=[-1200000.]
        for year,a in enumerate(models['condicionada_puro']['anual']):
            earnings=pay*50000*.03*12-float(a['opex_identificado_clp'])-wage*3*12
            used=min(max(earnings,0),loss);tax=round(max(earnings-used,0)*.27,2)
            loss=loss-used+max(-earnings,0)
            flows.append(earnings-tax)
        return math.fsum(f/(1.12**i) for i,f in enumerate(flows))
    for root,wage in zip(rev['quiebres_van'],[200000,1000000]):
        count=root['pagos_mes_enteros']
        assert independent_van(count-1,wage)<0<=independent_van(count,wage)
        assert abs(independent_van(count,wage)-float(root['van_pago_minimo_clp']))<.01
        assert str(count) in body.replace('.','')
    for item in rev['umbrales_anuales']:
        year=item['anio']-2027;a=models['condicionada_puro']['anual'][year]
        for key,wage in [('pagos_meta_200000',200000),('pagos_objetivo_millon',1000000)]:
            needed=float(a['opex_identificado_clp'])/12+3*wage
            n=item[key];assert (n-1)*1500<needed<=n*1500
    # 743 no se traslada como activación de pago permanente en los años reajustados.
    assert [float(x['pago_condicionado_743_mes_clp']) for x in rev['umbrales_anuales']]==[600000,0,0,0]
    flows=[float(x) for x in models['condicionada_puro']['flujo_anual']]
    basevan=math.fsum(f/1.12**i for i,f in enumerate(flows))
    assert len(rev['sensibilidades'])==11
    for row in rev['sensibilidades']:
        factor=float(row['variacion_pct'])/100
        var=row['variable']
        if var=='descuento':expected=math.fsum(f/(1+factor)**i for i,f in enumerate(flows))
        elif var in ('pagos','ticket'):expected=basevan+factor*math.fsum(288000/1.12**i for i in range(1,5))
        else:
            recalculated=[-1200000.]
            for year in range(4):
                clp=5860950/12*1.04**year
                cloud=25670.52*(1+factor if var=='cambio' else 1)
                opex=round((clp+cloud)*(1+factor if var=='costos' else 1),2)
                recalculated.append(288000-12*opex)
            expected=math.fsum(f/1.12**i for i,f in enumerate(recalculated))
        assert abs(expected-float(row['van_parcial_clp']))<.10,(row,expected)
    monthly=flows[0]+math.fsum(float(x['flujo_parcial_clp'])/1.12**(x['periodo']/12) for x in models['condicionada_puro']['mensual'])
    assert abs(monthly-float(rev['temporalidad']['van_convencion_fin_mes_clp']))<.01
    assert abs((1+float(rev['temporalidad']['tasa_mensual_equivalente']))**12-1.12)<1e-12
    # Aritmética de las tablas tal como se muestran, tolerancia de redondeo a CLP.
    for number in [18,19]:
        block=body.split(f'**Tabla {number}**')[1].split('*Nota.*')[0]
        rows={r.split('|')[1].strip():[parse(v.strip()) for v in r.split('|')[2:-1]] for r in block.splitlines() if r.startswith('| (') and 'n.d.' not in r}
        get=lambda prefix:next(values for key,values in rows.items() if key.startswith(prefix))
        for i in range(5):
            ebit=get('(+) Ingresos')[i]-get('(-) Costos variables')[i]-get('(-) Costos fijos')[i]-get('(-) Gastos de administración')[i]-get('(-) Depreciación')[i]
            assert abs(ebit-get('(=) Resultado operativo')[i])<=1
            net=get('(=) Utilidad neta')[i]+get('(+) Ajuste')[i]+get('(+) Préstamo')[i]+get('(-) Inversión')[i]-get('(-) Amortización')[i]
            assert abs(net-get('(=) Flujo neto')[i])<=1
        assert 'n.d.' in block
    # Referencias exactas de tablas H y rótulos únicos.
    labels=re.findall(r'^\*\*Tabla ([^*]+)\*\*$',body+'\n'+annex,re.M)
    assert len(labels)==len(set(labels))
    for number in range(14,22): assert str(number) in labels
    for number in ['H.36.1','H.36.2','H.36.3']:assert number in labels
    assert '2.335' not in body+annex[annex.index('## H.27.'):]
    assert body.count('El cálculo rector descuenta')==1
    # Las metas y costos publicados coinciden con las memorias activas.
    base=json.loads((ROOT/'02_contraste/umbrales_remuneraciones.json').read_text())
    target=json.loads((ROOT/'02_contraste/umbral_sueldo_objetivo.json').read_text())
    block=body.split('**Tabla 21**')[1].split('*Nota.*')[0]
    numeric=[[parse(v.strip()) for v in line.split('|')[1:-1]] for line in block.splitlines() if re.match(r'^\| [0-9]',line)]
    expected=[[D(x['ticket_medio_clp']),D(x['comision_neta_por_pago_clp']),D(x['pagos_mes']),D(y['pagos_mes'])] for x,y in zip(base['metas_por_ticket'],target['metas_por_ticket'])]
    assert numeric==expected
    costblock=body.split('**Tabla 20**')[1].split('*Nota.*')[0]
    costrows=[line.split('|')[1:-1] for line in costblock.splitlines() if line.startswith('| ')][1:]
    assert sum(parse(row[1].strip()) for row in costrows[:8])==D(base['costos_parciales_sin_fundadores_aws_clp'])
    # Las transcripciones originales del anexo se conservan byte por byte.
    previous=subprocess.check_output(['git','show','ee473e9:preparacion_economica_anita/03_propuesta/anexo_h_tablas_fuente.md'],cwd=ROOT.parent).decode()
    assert previous.split('## H.27.')[0]==annex.split('## H.27.')[0]
    doc=ROOT/'03_propuesta/build/Preparacion_economica_espaciGo.docx'
    with zipfile.ZipFile(doc) as z:
        xml=etree.fromstring(z.read('word/document.xml'))
    ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    text=''.join(xml.xpath('//w:t/text()',namespaces=ns))
    for label in labels:assert f'Tabla {label}' in text
    assert '2.335' not in text[text.index('H.27. Memoria'):]
    assert len(xml.xpath('//w:tbl',namespaces=ns))==len(labels)
    result={'alcance':'segundo corte parcial; no cierre de factibilidad','comprobaciones':'sensibilidad independiente, cruces adyacentes, umbrales anuales, fechas, aritmética de tablas, rótulos, Word y fuentes conservadas','tablas_word':len(labels),'transcripcion_original_intacta':True,'estado':'correcto'}
    (ROOT/'04_modelo_sapag/auditoria_segundo_corte.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
