"""Genera cuerpo y memorias vigentes desde la simulación adoptada."""
from pathlib import Path
from decimal import Decimal as D
import json,re
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'06_escenario_adoptado'
def load(name):return json.loads((OUT/name).read_text())
def money(x,decimals=0):return f'{D(str(x)):,.{decimals}f}'.replace(',','X').replace('.',',').replace('X','.')
def table(headers,rows):return '| '+' | '.join(headers)+' |\n|'+'|'.join('---' for _ in headers)+'|\n'+''.join('| '+' | '.join(map(str,row))+' |\n' for row in rows)
def cuadro(number,title,headers,rows,note):return f'**Tabla {number}**\n*{title}*\n\n'+table(headers,rows)+'\n*Nota.* '+note+'\n\n'
def flow(m,p,number,title):
 a=m['anual'];zero=[0]*5
 def series(key):return [0]+[D(x[key]) for x in a]
 admin=[D(x['administracion_marketing_clp']) for x in a]
 operative=[D(x['opex_devengado_clp'])-ad+D(x['pago_fundadores_clp']) for x,ad in zip(a,admin)]
 rows=[('(+) Ingresos por comisiones',series('comision_neta_devengada_clp')),
 ('(-) Costos variables propios de pasarela',zero),('(-) Costos fijos operativos (OPEX)',[0]+operative),
 ('(-) Administración y marketing',[0]+admin),('(-) Depreciación',zero),('(=) Resultado operativo (EBIT)',series('ebit_clp')),
 ('(-) Intereses',series('interes_clp')),('(=) Resultado antes de impuestos',series('ebt_clp')),('(-) Impuesto académico 27 %',series('impuesto_clp')),
 ('(=) Utilidad neta',[0]+[D(x['ebt_clp'])-D(x['impuesto_clp']) for x in a]),('(+) Ajuste por depreciación',zero),
 ('(+) Préstamo simulado',[D(p['deuda_simulada']['principal_clp']) if m['financiado'] else 0,0,0,0,0]),
 ('(-) Lanzamiento y compras',[-D(p['lanzamiento']['presupuesto_clp'])]+[-D(x['compra_reposicion_clp']) for x in a]),
 ('(-) Variación comisión por cobrar',series('variacion_cxc_clp')),('(-) Amortización de deuda',series('amortizacion_deuda_clp')),
 ('(=) Flujo de caja simulado',m['flujo_anual_operacion_clp'])]
 return cuadro(number,title,['Partida / período','Año 0','Año 1','Año 2','Año 3','Año 4'],[[label]+[money(v) for v in values] for label,values in rows],
 'CLP redondeados a pesos; la memoria conserva centavos y la secuencia de Anita. Se resta la variación de comisión por cobrar; su liquidación posterior figura en la Tabla 22. Pasarela propia y depreciación no se reconocen sin respaldo, sin afirmar costo real cero. IVA y fondos ajenos no son caja libre. H.33 concilia fechas; la reposición se registra una vez y sin escudo fiscal atribuido.')

def main():
 p=load('parametros.json');models=load('resultados.json');cs=load('costos.json');s=load('resumen.json');roots=load('umbrales_van.json');oper=load('umbrales_operativos_promedio.json')
 base=models['condicionada_puro'];fin=models['condicionada_financiado'];chosen=[('Base sin deuda',base),('Base financiado',fin),('Reposición 2029',models['estres_reposicion']),('Cobro a 30 días',models['estres_cobro30'])]
 archive=(OUT/'historial/cuerpo_antes_adopcion.md').read_text();oldann=(OUT/'historial/anexos_calculos_anteriores.md').read_text()
 bp=ROOT/'03_propuesta/capitulo_xiv_borrador.md';ap=ROOT/'03_propuesta/anexo_h_tablas_fuente.md'
 body=archive[:archive.index('#### 14.3.3.')]
 body=body.replace('Se mantiene provisional y pendiente de desglose, sin añadir otra partida legal por los mismos conceptos.', 'El desglose presupuestario adoptado distingue CLP 300.000 de formalización y asesoría, CLP 300.000 de contenidos, CLP 400.000 de campaña previa y CLP 200.000 de contingencia. No representa gasto ejecutado; el caso máximo programa el uso de CLP 1.200.000 en el Año 0, sin duplicarlo como otro egreso legal.')
 body=body.replace('El escenario AWS preparado adopta USD 26,41 mensuales', 'El escenario de piloto Single-AZ preparado adopta USD 26,41 mensuales')
 body=body.replace('El importe histórico equivalente a un mes de OPEX queda como antecedente hasta verificar el ciclo de cobros y pagos.', 'El importe histórico equivalente a un mes de OPEX queda como antecedente. La simulación adoptada utiliza siete días para la comisión propia y treinta días como estrés, sin atribuir esos plazos al contrato de la pasarela.')
 body=body.replace('Este borrador organiza los insumos económicos de Anita en la estructura de la memoria. Las tablas editables permiten contrastar los modelos antes de elegir la versión definitiva. El escenario AWS sustituye el componente tecnológico en su alcance de planificación. El plan identifica las conciliaciones necesarias para cerrar los resultados dependientes.', 'La preparación organiza los insumos económicos de Anita y aplica la simulación académica adoptada. Los antecedentes se conservan para contrastar su origen con las decisiones vigentes de ingreso, costos, calendario y cierre. La evaluación distingue hipótesis parametrizadas de evidencia comercial o contractual pendiente.')
 body=body.replace('Esos parámetros producen 192 reservas', 'Para la simulación esos parámetros se interpretan como 192 pagos procesados')
 body=body.replace('El capital del ciclo de liquidación continúa no determinado.', 'El capital completo del ciclo requiere condiciones reales; la comisión por cobrar se cuantifica en la simulación adoptada.')
 body=body.replace('Las Tablas 18 y 19 presentan el recálculo parcial vigente, separado de este antecedente. La evaluación definitiva aún requiere cerrar las partidas no determinadas;', 'Las Tablas 18 y 19 presentan la referencia académica adoptada, separada de este antecedente. La evaluación operativa real requiere respaldar las condiciones no verificadas;')
 body=body.replace('El capital de trabajo y el cierre permanecen sin determinar.', 'La simulación posterior cuantifica la comisión por cobrar y define el cierre prudente, sin acreditar condiciones reales de operación.')
 body=body.replace('La elección y su cuantía permanecen pendientes de respaldo.', 'El escenario adopta cero ingreso por venta como convención prudente y separa el cobro posterior de comisiones; no se atribuye una tasación comercial.')
 body+='''#### 14.3.3. Referencia adoptada sin deuda

La simulación conserva 16 pagos mensuales de CLP 50.000, comisión neta del 3 %, cuatro años de operación desde enero de 2027 y uso compartido de equipos personales sin compra inicial. NIC Chile publica CLP 9.990 por un año de dominio .cl, consultado el 16 de noviembre de 2026; ese importe se adopta para 2027 como supuesto y se reajusta después al 4 % junto a los presupuestos CLP. El costo cloud permanece en USD y cambio constantes del perfil piloto presupuestado, sin créditos no acreditados para la operación.

El dominio y la dirección tributaria se pagan en enero. Los demás presupuestos se distribuyen mensualmente. Se adopta un desfase de siete días para cobrar la comisión propia, con mes financiero de treinta días. Esta hipótesis determina cuentas por cobrar y caja, pero no acredita condiciones comerciales de Mercado Pago. H.31–H.33 contienen la memoria.

'''
 body+='En el Año 1, el subtotal identificado es CLP '+money(s['subtotal_anual_1_clp'],2)+'. Enero paga CLP '+money(s['enero_opex_clp'],2)+' y cobra CLP '+money(s['enero_comision_cobrada_clp'],2)+' de comisión neta. La diferencia por cobrar es CLP '+money(s['cxc_supuesto_base_clp'],2)+'. Los pagos condicionados a fundadores siguen en cero en la referencia.\n\n'
 body+=flow(base,p,18,'Flujo puro de la referencia académica adoptada')
 body+='''#### 14.3.4. Alternativa con deuda simulada

El préstamo de CLP 3.720.000 permanece como alternativa de comparación, no como financiamiento contratado. Se conservan tres cuotas anuales al 12 %, con última cuota ajustada para extinguir la deuda. El dinero prestado no constituye ingreso por intermediación ni activa remuneraciones. H.34 conserva la amortización y H.37 la capacidad de pago.

'''+flow(fin,p,19,'Flujo de la alternativa financiada')
 body+='''#### 14.3.5. Escenario de reposición

El caso de estrés programa una compra de notebook por CLP 900.000 en diciembre de 2029. El presupuesto deriva del importe unitario de CLP 800.000 del insumo, reajustado como referencia; no acredita una cotización futura. La reserva interna de CLP 25.000 mensuales durante 36 meses solo restringe la disponibilidad para asignaciones: no se vuelve a restar como gasto además de la compra. La prueba no reconoce escudo fiscal por depreciación sin respaldo. H.39 documenta sus límites.

'''+flow(models['estres_reposicion'],p,20,'Flujo con compra de reposición en el Año 3')
 body+='''#### 14.3.6. Escenario de cobro a treinta días

El estrés amplía a treinta días el plazo supuesto para cobrar comisión. Se conserva la demanda y los costos, para aislar el efecto del rezago. El primer mes no cobra comisión propia y el saldo por cobrar al corte aumenta. Los fondos del publicador siguen separados de los ingresos de la plataforma.

'''+flow(models['estres_cobro30'],p,21,'Flujo con plazo supuesto de cobro de treinta días')
 body+='''#### 14.3.7. Liquidación de operaciones del horizonte

La venta de activos y software se fija en cero como caso prudente y no se incorpora perpetuidad. Esa convención no tasa la empresa. La comisión generada dentro de los cuatro años se cobra después del corte conforme al plazo supuesto, separada de nuevos servicios de un quinto año. Este cobro no se anticipa al Año 0 ni se suma como venta. La Tabla 22 completa el flujo de cada alternativa fuera de las columnas anuales rectoras.

'''
 body+=cuadro(22,'Cobro de comisión posterior al horizonte de operación',['Escenario','Días tras el corte','Cobro de CxC CLP','Venta de activos CLP'],[[name,money(m['liquidacion']['dias_despues_horizonte']),money(m['liquidacion']['cobro_cxc_clp']),0] for name,m in chosen],
 'El plazo es una hipótesis. La liquidación pertenece a operaciones hasta diciembre de 2030 y se sitúa en 4 + días/360 años. La venta se mantiene en cero por convención prudente. No se presenta la recuperación de pérdidas operativas como activo. H.33 y H.38 concilian los flujos y el descuento.')
 body+='''### 14.4. Indicadores de rentabilidad financiera

El descuento nominal anual se mantiene en 12 %, confirmado por Anita y adoptado como referencia del ejercicio. Sapag vincula el costo de capital con alternativas de riesgo comparable; el libro no prescribe ese porcentaje para espaciGo ni acredita una estimación de CAPM o WACC (Sapag Chain & Sapag Chain, 2008, pp. 343–345, 353–356). El impuesto académico se conserva en 27 %, separado de la tributación efectiva de una empresa aún no constituida.

El VAN rector descuenta cierres anuales y añade el cobro de la Tabla 22 en su momento diferido. La memoria también informa el control con importes mensuales a tasa equivalente, evitando mezclar fechas de valoración. La TIR se calcula únicamente cuando el patrón y el intervalo permiten una interpretación útil de inversión. La referencia presenta operación neta negativa y solo una pequeña recuperación final de cuentas por cobrar; no se publica una tasa numérica extrema como prueba de rendimiento. La alternativa financiada tampoco se interpreta como flujo convencional de inversión.

'''
 metrows=[[name,money(m['indicadores']['van_con_liquidacion_clp'],2),'No se informa TIR útil'] for name,m in chosen]
 for root,label in zip(roots[:3],['Quiebre sin asignaciones','Quiebre meta $200.000','Quiebre meta $1.000.000']):
  metrows.append([label,money(root['indicadores']['van_con_liquidacion_clp'],2),money(D(root['indicadores']['tir_anual'])*100,4)+' %'])
 body+=cuadro(23,'VAN y TIR de las simulaciones delimitadas',['Escenario','VAN con liquidación CLP','TIR anual'],metrows,
 'Las tres últimas filas son volúmenes analíticos de quiebre, no previsiones de ventas. Se conserva 12 % de descuento y se incluyen las fechas de liquidación. H.38 presenta sus pagos mensuales y recuperaciones. Los costos propios no valorados y el escalamiento siguen fuera; ningún resultado confirma viabilidad comercial.')
 body+='''### 14.5. Sensibilidad y escenarios

Se modifica individualmente volumen de pagos, ticket, costos y cambio en menos y más 20 %. La variación cambiaria afecta solo a AWS. Se compara descuento del 10 %, 12 % y 25 % manteniendo la base del 12 %. Los rangos son pruebas deterministas, sin probabilidades atribuidas. La reposición y el cobro a treinta días se comparan por separado, sin cambiar la demanda para fabricar rentabilidad (Sapag Chain & Sapag Chain, 2008, pp. 371, 375, 398–400, 406).

'''
 body+='Con ticket de CLP 50.000, el primer entero mensual con VAN rector no negativo es '+money(roots[0]['pagos_mes'])+' sin asignaciones, '+money(roots[1]['pagos_mes'])+' con CLP 200.000 por fundador presupuestados y '+money(roots[2]['pagos_mes'])+' con CLP 1.000.000 por persona. Se verifica el entero inmediatamente anterior. Son metas bajo costos identificados independientes del volumen y no acreditan capacidad técnica ni captación. H.36 conserva las pruebas y la comparación de los escenarios comerciales de origen de Anita, sin probabilidades atribuidas.\n\n'
 body+='''### 14.6. Cobros para financiar asignaciones a fundadores

La regla adoptada compara la recaudación propia del mes con los pagos programados, una provisión académica de impuesto y reservas de deuda y reposición cuando corresponden. Solo permite el monto conjunto completo de CLP 600.000 o cero en el caso condicionado. La provisión de impuesto y las reservas no vuelven a descontarse como gastos: los flujos registran impuesto, cuota y compra en sus fechas programadas. La regla excluye préstamo, aportes, IVA y fondos ajenos como fuentes para habilitar el pago. Las metas presupuestadas completas se evalúan aparte, sin asegurar que exista caja para pagarlas.

'''
 body+=cuadro(24,'Presupuesto mensual prorrateado del Año 1',['Componente','CLP por mes'],[[c['concepto'],money(c['mensual_1_clp'],2)] for c in cs]+[['Subtotal identificado',money(s['subtotal_mensual_prorrateado_clp'],2)]],
 'El prorrateo sirve al análisis costo-volumen; el pago real simulado usa enero para dominio y dirección tributaria. Los importes son presupuestos, salvo la tarifa pública consultada que se proyecta como supuesto de continuidad. H.32 conserva la procedencia. No se acredita contratación de proveedores.')
 body+=cuadro(25,'Umbrales operativos por ticket con costos promedio',['Ticket medio CLP','Comisión neta unitaria CLP','Pagos para $200.000 por persona','Pagos para $1.000.000 por persona'],[[money(x['ticket_clp']),money(x['comision_unitaria_clp']),money(x['pagos_promedio_meta_200000']),money(x['pagos_promedio_meta_millon'])] for x in oper],
 'Se redondea hacia arriba (costo medio identificado + asignaciones) / comisión unitaria neta. Es un umbral promedio de costos, no VAN cero ni garantía de activar el pago en todos los meses. Enero concentra anualidades y el primer mes cobra parcialmente su comisión. H.27 y H.33 distinguen presupuesto, devengo y caja.')
 body+='''### 14.7. Necesidad de aportes y capacidad de pago

El déficit acumulado máximo se obtiene recorriendo el saldo antes de aportes. El aporte mínimo cubre el faltante para sostener caja no negativa y las reservas de deuda o reposición programadas, sin registrarlas como gasto adicional. No se carga nuevamente como inversión inicial el déficit que ya aparece en los flujos operativos. La alternativa financiada usa primero el excedente del préstamo; sus aportes adicionales no duplican esa entrada. La capacidad propia de atender las cuotas es negativa en la referencia, según H.37 (Sapag Chain & Sapag Chain, 2008, pp. 5–6, 267–269, 297–298).

'''
 rows=[]
 for y in range(5):
  values=[]
  for m in [base,fin]:values.append(sum(D(r['aporte_minimo_clp']) for r in m['aportes'] if (r['periodo']-1)//12+1==y))
  rows.append([2026+y]+[money(v) for v in values])
 rows.append(['Total',money(base['aporte_minimo_acumulado_clp']),money(fin['aporte_minimo_acumulado_clp'])])
 body+=cuadro(26,'Aportes mínimos adicionales por año',['Año','Referencia sin deuda CLP','Alternativa financiada CLP'],rows,
 'Necesidades de liquidez sobre las partidas identificadas; no disponibilidad confirmada de los socios. La liquidación posterior deja la comisión recuperada como caja al corte ampliado y no elimina los déficits previos. Los equipos compartidos y el trabajo valorizado no se incorporan como efectivo.')
 body+='''### 14.8. Conclusión y condiciones de validación

La simulación adoptada completa el calendario y los cálculos del escenario académico, con límites explícitos. La referencia de 16 pagos mensuales no cubre los costos identificados, no activa asignaciones y necesita aportes. El resultado no se altera mediante crecimiento comercial o venta de activos sin respaldo. La muestra de entrevistas y las fichas de oferta son objetivos de validación, no resultados obtenidos.

El inicio de la operación se fija para el 1 de enero de 2027. Los equipos son personales y compartidos; la constitución se incluye en el presupuesto de CLP 1.200.000. El presupuesto de valoración conserva 960 horas a CLP 6.500 por hora. El plan vigente asigna 632 horas al bloque académico del 11 de agosto al 30 de noviembre, 36 horas a la defensa y 40 horas a la transición preoperativa, para 708 horas asignadas y una reserva presupuestaria de 252 horas. No existen horas reales acreditadas; la valorización no representa remuneraciones ni egreso de caja. H.39–H.40 documentan decisiones, límites y trazabilidad.

La validación real requiere demanda, costos, escalamiento y condiciones de proveedores respaldados. El cierre sin venta es una convención, no una tasación. La preparación se mantiene separada de la tesis principal y conserva la planificación de Erick.
'''
 bp.write_text(body)
 # El prefijo de 26 hojas transcritas se conserva exactamente.
 source=ap.read_text().split('## H.27.')[0]
 annex=source+'## H.27. Umbrales y regla de asignaciones adoptados\n\n'
 annex+='Este apartado respalda las Tablas 24 y 25. El presupuesto medio identificado es CLP '+money(s['subtotal_mensual_prorrateado_clp'],2)+'. A ticket de CLP 50.000, los umbrales promedio siguen siendo 743 y 2.343 pagos para las dos metas por persona. La caja del mes puede no permitirlas, aunque el promedio las cubra: enero paga anualidades y el lanzamiento tiene comisión por cobrar.\n\n'
 annex+='La regla verifica recaudación del mes menos OPEX pagado, reserva de cuota y provisión académica de impuesto después de la meta; en estrés también reserva CLP 25.000 durante 36 meses para reposición. Si alcanza, paga la meta completa; en otro caso paga cero. Las reservas no se suman a los egresos de caja ya registrados por sus conceptos. La provisión no utiliza pérdidas fiscales para aumentar disponibilidad; el impuesto anual sí concilia las pérdidas del ejercicio académico. No se presupone relación laboral formal ni costo económico cero del trabajo.\n\n'
 def section(text,heading,nextheading):return text[text.index(heading):text.index(nextheading)]
 tax=section(oldann,'## H.28.','## H.29.').replace('La serie definitiva y sus indicadores requieren cerrar los demás parámetros pendientes.','La simulación adoptada completa las fechas y partidas definidas; las condiciones reales no respaldadas permanecen identificadas.')
 rate=section(oldann,'## H.29.','## H.30.').replace('Son comprobaciones históricas y no resultados del flujo nuevo pendiente de cierre.','Son comprobaciones históricas y no resultados de la simulación adoptada.')
 rate=rate.replace('se conserva únicamente en la extracción histórica, sin utilizarlo como criterio principal.', 'se conserva como antecedente y prueba de sensibilidad, sin utilizarlo como criterio principal.')
 rate=rate.replace('el flujo del Año 0 no se descuenta.','el flujo del Año 0 no se descuenta. El escenario adoptado añade el cobro posterior de comisión en su momento 4 + días/360. H.38 distingue el VAN sin liquidación, el VAN con liquidación y el control mensual.')
 annex+=tax+rate
 annex+='''## H.30. Aplicación metodológica y alcance

La preparación utiliza Sapag Chain y Sapag Chain (2008), quinta edición. La referencia diferencia rentabilidad del proyecto, de los socios y capacidad de servicio de deuda; clasifica inversión, costos pertinentes, capital del ciclo y valor final (pp. 5–6, 126, 259–269, 277–282, 291–298). Los indicadores se calculan por flujos y fechas coherentes, distinguiendo recuperación nominal y descontada (pp. 321–323, 329–330).

Las hipótesis elegidas permiten terminar la simulación académica sin denominarlas demanda observada, facturas, contratos o tasas de mercado estimadas. Las salidas de partidas desconocidas quedan fuera de su alcance. Los originales H.1–H.26 conservan diferencias históricas de GCP, porcentajes y recursos para el contraste solicitado; los cálculos vigentes de H.27–H.40 utilizan el nuevo escenario. Los cortes calculados anteriores se conservan en el historial de preparación y en Git, separados de los resultados activos.

Referencia: Sapag Chain, N., & Sapag Chain, R. (2008). Preparación y evaluación de proyectos (5.ª ed.). McGraw-Hill Interamericana. En la copia aportada, la página PDF equivale a la impresa más 18.

## H.31. Referencia comercial y plan de validación

Se conservan ocho espacios activos promedio, dos pagos por espacio y mes y ticket de CLP 50.000. Las nueve categorías son catálogo disponible; no se reparten los ocho espacios ni se atribuyen ventas a todas ellas sin evidencia. El crecimiento de cobros y precio se mantiene en cero como referencia, y no como certeza comercial.

'''
 categories=['Oficina','Sala multipropósito','Bodega','Estacionamiento','Local flexible','Stand','Quincho','Parcela de eventos','Inmuebles']
 annex+=cuadro('H.31.1','Categorías y evidencia por recopilar',['ID','Categoría','Estado de oferta y pagos'],[[i,c,'Por validar con fichas y pagos observados'] for i,c in enumerate(categories,1)],'Catálogo indicado por el propietario. Los registros vacíos no se sustituyen por ceros observados.')
 annex+=cuadro('H.31.2','Objetivos exploratorios de validación',['Registro','Objetivo','Evidencia disponible'],[['Fichas de oferta',8,'Sin fichas de campo en esta preparación'],['Entrevistas a publicadores',10,'Objetivo, no entrevistas realizadas'],['Entrevistas a arrendatarios',20,'Objetivo, sin representatividad estadística atribuida']],
 'El piloto observa enero-marzo de 2027. Se registra categoría, modalidad, disponibilidad, precio, pagos completos, devoluciones, GMV y recurrencia. Una intención no equivale a un pago. Los datos generales del INE sobre alojamiento solo contextualizan ese segmento, no la captación ni todas las categorías.')
 annex+='## H.32. Costos y lanzamiento adoptados\n\n'
 annex+=cuadro('H.32.1','Componentes del Año 1',['ID','Componente','Promedio mensual CLP','Presupuesto anual CLP'],[[c['id'],c['concepto'],money(c['mensual_1_clp'],2),money(c['anual_1_clp'],2)] for c in cs]+[['Total','Subtotal identificado',money(s['subtotal_mensual_prorrateado_clp'],2),money(s['subtotal_anual_1_clp'],2)]],
 'Presupuestos originales conciliados sin duplicar subtotales, más dirección tributaria ratificada. El dominio usa la tarifa pública NIC directo. Los servicios siguen sin contratación acreditada. Útiles y dirección se contabilizan una vez.')
 annex+='NIC Chile publica CLP 9.990 por año .cl, exento de IVA, consultado el 16 de noviembre de 2026: https://www.nic.cl/dominios/tarifas.html. Se asume continuidad para 2027 y reajuste presupuestario posterior del 4 %; no se garantiza la tarifa futura. El presupuesto cloud conserva USD 26,41 del perfil piloto Single-AZ de la propuesta interna, convertido a 972 CLP/USD. La descripción Multi-AZ con balanceador del README requiere presupuesto separado; el importe piloto no acredita ese alcance o capacidad de carga. No se verifica facturación AWS ni se aplican créditos sin evidencia de vigencia.\n\n'
 labels=['Formalización y asesoría','Contenidos y materiales','Campaña previa','Contingencia preoperativa']
 annex+=cuadro('H.32.2','Desglose presupuestario de lanzamiento',['Componente','CLP'],[[label,money(v)] for label,v in zip(labels,p['lanzamiento']['desglose_presupuesto_clp'].values())]+[['Total','1.200.000']],
 'Asignaciones del presupuesto, no cotizaciones o gastos realizados. La campaña previa corresponde al Año 0 y se distingue del marketing operativo de 2027. El caso máximo utiliza todo el presupuesto en el Año 0; un margen no ejecutado se ajusta cuando existe evidencia. No se suma otra constitución por separado.')
 annex+='''## H.33. Devengo, pagos y comisión por cobrar

El dominio y la dirección tributaria se pagan en enero de cada año; los demás componentes se distribuyen mensualmente, conciliando centavos en el último mes. El gasto devengado permite calcular resultado e impuesto; el calendario pagado determina caja. Los importes CLP aumentan 4 % al año y AWS permanece constante en los USD y cambio adoptados.

Para la comisión se adopta siete días y mes de treinta días. Saldo por cobrar = comisión mensual devengada × días/30. Cobro del mes = comisión devengada + saldo inicial por cobrar − saldo final por cobrar. No se agregan otra vez esos saldos al Año 0 como capital de trabajo. Se mide un componente del ciclo; IVA de compras, retenciones y condiciones reales sin respaldo no se convierten en cifras confirmadas.

'''
 annex+=cuadro('H.33.1','Calendario de los primeros tres meses',['Mes','Comisión cobrada CLP','OPEX pagado CLP','CxC final CLP','Flujo neto CLP'],[[r['fecha'],money(r['comision_neta_cobrada_clp'],2),money(r['opex_pagado_clp'],2),money(r['cxc_final_clp'],2),money(r['flujo_caja_clp'],2)] for r in base['mensual'][:3]],
 'Referencia sin deuda ni asignaciones pagadas. El IVA de la comisión y los fondos de publicadores se mantienen fuera de caja libre. El abono final al publicador no se determina sin tarifa de pasarela. Las fechas son convenciones de simulación, no facturas o plazos contratados.')
 annex+='La última comisión por cobrar se cobra siete días después del corte de diciembre de 2030. En estrés se utilizan treinta días. La Tabla 22 muestra ambos saldos. Este cobro liquida operaciones del horizonte y no supone un quinto año de nuevos arriendos. Para el descuento, la fecha financiera es 4 + días/360. La documentación de Split 1:1 no confirma el plazo particular de espaciGo; se mantiene como hipótesis adoptada.\n\n'
 annex+='## H.34. Servicio de la deuda simulada\n\n'
 debt=json.loads((ROOT/'04_modelo_sapag/deuda_corregida.json').read_text())
 annex+=cuadro('H.34.1','Amortización hasta saldo cero',['Año','Saldo inicial CLP','Interés CLP','Capital CLP','Cuota CLP','Saldo final CLP'],[[x['anio']]+[money(x[k]) for k in ['saldo_inicial_clp','interes_clp','amortizacion_clp','cuota_clp','saldo_final_clp']] for x in debt],
 'Principal CLP 3.720.000, interés 12 % y tres cuotas anuales. La última suma CLP 1 por redondeo. No se acredita contratación, seguros o comisiones financieras. El capital amortizado coincide con el recibido.')
 annex+=section(oldann,'## H.35.','## H.36.')
 annex+='## H.36. Sensibilidad y quiebres de VAN\n\n'
 sens=load('sensibilidad.json');names={'pagos':'Cobros','ticket':'Ticket','costos':'Costos','cambio':'CLP/USD','descuento':'Descuento'}
 annex+=cuadro('H.36.1','Sensibilidad desde la misma referencia',['Variable','Prueba','VAN con liquidación CLP','Cambio CLP'],[[names[x['variable']],money(x['variacion_pct'])+' %'+(' anual' if x['variable']=='descuento' else ''),money(x['van_con_liquidacion_clp']),money(x['diferencia_base_clp'])] for x in sens],
 'Pruebas deterministas sin probabilidades. Se altera una variable cada vez y se conserva la comisión del 3 %. El cambio afecta solo AWS; los rangos no acreditan capacidad de escalamiento. Cambiar descuento no modifica el riesgo ni las ventas.')
 annex+=cuadro('H.36.2','Primer entero de pagos mensuales con VAN no negativo',['Meta por persona','Pagos al mes','VAN con un pago menos CLP','VAN con el mínimo CLP'],[[label,money(x['pagos_mes']),money(x['van_anterior_clp'],2),money(x['van_minimo_clp'],2)] for label,x in zip(['Sin asignaciones','$200.000','$1.000.000'],roots[:3])],
 'Ticket CLP 50.000. Incluye liquidación diferida y descuento 12 %. La búsqueda usa escenarios de asignaciones fijas para evitar saltos de la regla condicionada. Los mínimos son analíticos y no demanda proyectada. Se mantienen fuera costos residuales y escalamiento.')
 annex+=cuadro('H.36.3','Escenarios comerciales de Anita con comisión común del 3 %',['Escenario','Pagos al mes','Ticket CLP','VAN con liquidación CLP'],[[x['escenario'],money(x['pagos_mes']),money(x['ticket_clp']),money(x['van_con_liquidacion_clp'])] for x in load('escenarios_comerciales_anita.json')],
 'Se conservan los volúmenes y tickets del insumo y se aplican el mismo calendario y la comisión del 3 %. No son probabilidades ni ventas observadas. Se mantiene el costo piloto sin validar capacidad de escalamiento. La fila base coincide con la referencia adoptada.')
 annex+='## H.37. Aportes mínimos y cobertura de cuotas\n\n'
 annex+='Se recorren los 49 momentos de caja, incluido Año 0. Aporte mínimo = máximo entre cero y reserva objetivo menos caja antes del aporte. Se acumula la reserva de cuota durante cada año y la de reposición hasta la compra; al pagar se libera el monto reservado. La suma se concilia con el déficit máximo respecto de ese piso de liquidez, sin restar las reservas de nuevo como gasto. En la referencia sin reservas, el piso es cero. Después se cobra la cuenta pendiente, dejando caja al corte ampliado; ese retorno no borra los déficits que antes requieren financiamiento.\n\n'
 annex+=cuadro('H.37.1','Aportes y caja después de la liquidación',['Escenario','Aporte mínimo acumulado CLP','CxC liquidada CLP','Caja final con aportes CLP'],[[name,money(m['aporte_minimo_acumulado_clp'],2),money(m['liquidacion']['cobro_cxc_clp'],2),money(m['liquidacion']['caja_final_con_aportes_clp'],2)] for name,m in chosen],
 'Aportes no confirmados. La alternativa financiada incluye su préstamo antes de calcular necesidades adicionales. La liquidación de comisión recupera un activo del ciclo; no es beneficio operativo adicional ni una venta de equipos.')
 annex+=cuadro('H.37.2','Cobertura propia antes de cuotas',['Año','Caja antes de cuota CLP','Cuota CLP','Cobertura veces'],[[x['anio'],money(x['caja_antes_cuota_clp']),money(x['cuota_clp']),money(x['cobertura'],3) if x['cobertura'] is not None else 'No aplica'] for x in load('cobertura_deuda.json')],
 'Caja propia cobrada menos OPEX, asignaciones e impuesto, dividida por intereses más capital cuando hay cuota. Un resultado negativo no acredita capacidad propia de pago, aunque existan aportes o un préstamo inicial.')
 annex+='## H.38. Indicadores y fechas\n\n'
 annex+='El VAN rector considera los cierres anuales del formato docente y la comisión liquidada en su fecha diferida. No se adelanta esa recuperación al último cierre anual. Se informa además un control que descuenta cada importe mensual con (1 + 0,12) elevado a período/12, y la liquidación con su momento en años. La diferencia responde a fechas de egresos e ingresos, no a dos tasas base.\n\n'
 annex+=cuadro('H.38.1','Convenciones de valoración del caso de referencia',['Cálculo','VAN CLP'],[['Operación hasta diciembre de 2030',money(base['van_operacion_sin_liquidacion_clp'],2)],['Cierres anuales más liquidación',money(base['indicadores']['van_con_liquidacion_clp'],2)],['Control mensual más liquidación',money(base['van_mensual_control_clp'],2)]],
 'Los tres importes corresponden a convenciones identificadas de la misma referencia. Las raíces de H.36 utilizan cierres anuales más liquidación, al igual que la Tabla 23. No se comparan como si tuvieran las mismas fechas.')
 annex+='En la referencia, los flujos operativos son negativos. Añadir el cobro final del pequeño saldo por cobrar genera una entrada positiva tardía, pero no se publica una raíz negativa extrema como indicador útil de inversión. El VAN y la ausencia de recuperación dentro del horizonte ampliado describen su resultado. El patrón de la alternativa financiada tampoco es una inversión convencional.\n\n'
 annex+=cuadro('H.38.2','Recuperación de los volúmenes de quiebre',['Escenario','Pagos al mes','Recuperación simple años','Recuperación descontada años'],[[label,money(x['pagos_mes']),money(x['indicadores']['recuperacion_simple_anios'],3),money(x['indicadores']['recuperacion_descontada_anios'],3)] for label,x in zip(['Sin asignaciones','Meta $200.000','Meta $1.000.000'],roots[:3])],
 'Interpolación auxiliar entre momentos anuales y, si corresponde, liquidación. No es fecha contractual. La referencia y los dos estreses no recuperan la inversión; las metas de quiebre no acreditan oferta, adquisición de usuarios o costos completos de operación.')
 annex+='''## H.39. Reposición y cierre prudente

Los equipos existentes permanecen personales y compartidos. La referencia no compra ni vende esos bienes como si fueran propiedad de la empresa. El estrés sí programa una nueva compra de CLP 900.000 en 2029, sin deducción o depreciación fiscal atribuida. El importe deriva del notebook de CLP 800.000 del insumo, reajustado con el supuesto del 4 % durante tres años y redondeado presupuestariamente; no es cotización futura.

La reserva objetivo de CLP 25.000 durante 36 meses mantiene un piso de liquidez para la compra y restringe asignaciones. Si la operación no la financia, el calendario de aportes cubre ese piso. No es gasto adicional y se libera al pagar la adquisición. La salida de caja se registra una vez al adquirir. El caso prudente establece cero cobro por venta de activos y software y no incorpora perpetuidad. No se afirma que la empresa o sus activos valgan cero. Sapag diferencia valoración de desecho de caja disponible (2008, pp. 277–282, 292–295).

El capital modelado de comisión por cobrar ya está en el flujo por variación de saldos y se recupera en su fecha diferida. No se recuperan pérdidas persistentes como si fueran un activo. El resto del ciclo —IVA de compras, retenciones, devoluciones y proveedores— exige evidencia para una evaluación operativa real; no se confirma por adoptar esta simulación.

## H.40. Desarrollo, decisiones y trazabilidad

El cronograma académico vigente asigna 632 horas entre el 11 de agosto y el 30 de noviembre de 2026. La capacidad nominal del bloque es de 960 horas, equivalente a 320 por integrante y veinte horas semanales durante dieciséis semanas. A CLP 6.500 por hora, el presupuesto valorizado asciende a CLP 6.240.000. No existen horas reales acreditadas; el importe no representa remuneraciones ni egreso de caja.

Después del bloque académico se asignan 36 horas a la defensa y 40 horas a la transición preoperativa, para un total de 708 horas. La reserva presupuestaria es de 252 horas, equivalente a CLP 1.638.000, mientras que el valor de las horas asignadas asciende a CLP 4.602.000. La capacidad nominal base libre es de 328 horas, 76 horas superior a la reserva, porque esta última también descuenta las actividades posteriores a la entrega. La transición se programa del 10 al 31 de diciembre y la operación comienza el 1 de enero de 2027. El registro no acredita ejecución ni pago.

'''
 annex+=cuadro('H.40.1','Quiebre al exigir recuperar también la valorización global',['Meta por persona','Pagos al mes','VAN con un pago menos CLP','VAN con el mínimo CLP'],[[label,money(x['pagos_mes']),money(x['van_anterior_clp'],2),money(x['van_minimo_clp'],2)] for label,x in zip(['Sin asignaciones','$200.000','$1.000.000'],roots[3:])],
 'La prueba añade CLP 6.240.000 una vez al momento cero, sin deducción fiscal ni incorporación a aportes de efectivo. No estima el costo de oportunidad incremental a la fecha de decisión. Los flujos de caja de las Tablas 18–21 permanecen separados de esa valorización.')
 ap.write_text(annex.rstrip()+"\n")
 print('Actualizados cuerpo y H.27–H.40 desde la simulación adoptada; H.1–H.26 conservados.')
if __name__=='__main__':main()
