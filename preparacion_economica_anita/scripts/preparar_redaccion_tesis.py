"""Publica la evaluación económica con voz académica y datos del escenario activo.

No modifica el modelo financiero ni las transcripciones documentales históricas.
"""
from pathlib import Path
import json
import re
from decimal import Decimal
from actualizar_escenario_adoptado import money, table, flow

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '07_texto_para_tesis'
DATA = ROOT / '06_escenario_adoptado'
PLAN = ROOT.parent / 'preparacion_planificacion_pmbok/04_ejecucion/calculo_cronograma.json'


def load(name):
    return json.loads((DATA / name).read_text())


def source_table(text, number):
    match = re.search(r'\*\*Tabla ' + re.escape(number) + r'\*\*\n.*?\n\n(\|.*?)(?=\n\n)', text, re.S)
    if not match:
        raise ValueError(number)
    return match.group(1) + '\n'


def cuadro(number, title, grid, note):
    return f'**Tabla {number}**\n\n*{title}*\n\n{grid}\n*Nota.* Elaboración propia. {note}\n\n'


def clp(value):
    return f'{value:,}'.replace(',', '.')


def texto_h5():
    plan = json.loads(PLAN.read_text())
    c = plan['conciliacion_economica']
    return (f"El cronograma académico vigente asigna {c['horas_base_asignadas']} horas entre el "
            f"{c['inicio_base']} y el {c['fin_base']}. La capacidad nominal de ese bloque es de "
            f"{c['capacidad_base_horas']} horas: {c['capacidad_por_integrante_horas']} por integrante, "
            f"a {c['horas_semana_persona']} horas semanales durante {c['semanas_base']} semanas. "
            f"El presupuesto de valoración, calculado sobre las {c['presupuesto_valorizado_horas']} horas "
            f"a CLP {clp(c['tarifa_clp_hora'])} por hora, asciende a CLP {clp(c['presupuesto_valorizado_clp'])}. "
            "No existen horas reales acreditadas; por ello, la valorización es presupuestaria y no representa "
            "remuneraciones, contratación ni egreso de caja.\n\n"
            f"Después del bloque académico se asignan {c['horas_defensa']} horas a la defensa y "
            f"{c['horas_transicion']} horas a la transición preoperativa, para un total de "
            f"{c['horas_asignadas_total']} horas asignadas. La reserva presupuestaria es de "
            f"{c['reserva_presupuestaria_horas']} horas, equivalentes a CLP {clp(c['reserva_presupuestaria_clp'])}, "
            f"y el valor de las horas asignadas es CLP {clp(c['valor_asignaciones_clp'])}. La capacidad nominal "
            f"base libre asciende a {c['capacidad_base_libre_horas']} horas; supera la reserva presupuestaria "
            f"en {c['diferencia_capacidad_reserva_horas']} horas porque esta última se calcula contra la "
            "asignación total e incluye actividades posteriores a la entrega. La transición se programa del "
            f"{c['inicio_transicion']} al {c['fin_transicion']} y el inicio de la operación se fija para el "
            f"{c['inicio_operacion']}. Estas capacidades y asignaciones son estimaciones de planificación, "
            "no registros de trabajo ejecutado ni pagos.")


def main():
    OUT.mkdir(exist_ok=True)
    p = load('parametros.json')
    models = load('resultados.json')
    base = models['condicionada_puro']
    oldbody = (ROOT / '03_propuesta/capitulo_xiv_borrador.md').read_text()
    oldannex = (ROOT / '03_propuesta/anexo_h_tablas_fuente.md').read_text()
    body = '''# Capítulo XIV Evaluación económica de espaciGo

## 14. Factibilidad económica

La evaluación económica de espaciGo determina los ingresos, costos y necesidades de financiamiento de la plataforma para el período 2027–2030, con inversión preoperativa en 2026. El análisis comprende el flujo del proyecto sin deuda, una alternativa financiada y escenarios de sensibilidad. La referencia comercial considera dieciséis pagos mensuales y permite calcular el volumen de operaciones necesario para cubrir costos y financiar las asignaciones del equipo fundador.

El estudio aplica la metodología de Sapag Chain y Sapag Chain (2008), que distingue la rentabilidad del proyecto, la rentabilidad de los recursos propios y la capacidad de pago de la deuda. La inversión, el capital de trabajo, los costos pertinentes y el cierre del horizonte se relacionan con los flujos y las fechas de cada alternativa (pp. 5–6, 259–269, 277–282, 291–298). El Anexo H desarrolla los parámetros y las memorias de cálculo que respaldan este capítulo.

### 14.1. Estudio de mercado y modelo de ingresos

espaciGo actúa como intermediario entre quien publica un espacio y quien lo arrienda. La plataforma admite personas y organizaciones y comprende nueve categorías: oficina, sala multipropósito, bodega, estacionamiento, local flexible, stand, quincho, parcela de eventos e inmuebles. Esta última categoría distingue casa, departamento, habitación y cabaña. El alcance incluye espacios de uso personal, profesional, industrial, comercial y habitacional, con modalidades de contratación por hora, día o períodos de mayor duración.

El escenario base establece un inventario de ocho espacios activos, dos pagos mensuales por espacio y un ticket promedio ponderado de CLP 50.000. La proyección equivale a dieciséis pagos y CLP 800.000 transados al mes, o 192 pagos y CLP 9.600.000 al año. El número de pagos constituye la unidad del modelo de ingresos; un mismo espacio puede originar varias operaciones y un contrato puede comprender pagos sucesivos. Por ello, el volumen de transacciones no equivale al número de usuarios únicos.

La plataforma cobra una comisión neta del 3 % más IVA sobre cada pago procesado. La comisión y el cargo de Mercado Pago se descuentan del importe que recibe quien publica el espacio, denominado arrendador. La persona que contrata su uso corresponde al arrendatario. En un contrato con cuotas mensuales, la comisión se calcula sobre cada cuota; si el contrato se paga íntegramente una vez, se calcula sobre ese único pago.

El ingreso propio de espaciGo corresponde a la comisión neta. El valor bruto de los arriendos y el IVA de la comisión se registran por separado. Con el volumen base, el ingreso neto es CLP 24.000 mensuales y CLP 288.000 anuales. Por ejemplo, un pago de CLP 100.000 genera CLP 3.000 de comisión neta y CLP 570 de IVA; el arrendador recibe CLP 96.430 menos el cargo de la pasarela que corresponda a la operación.

La Tabla 14.1 presenta la distribución de pagos utilizada en la planificación mensual. El promedio ponderado se obtiene dividiendo el total transado por el número de pagos. Esta agregación permite evaluar modalidades de distinta duración mediante una misma unidad financiera, sin asignar un precio uniforme a todas las categorías.

'''
    body += cuadro('14.1', 'Distribución mensual de pagos por modalidad', source_table(oldbody, '14'),
                   'Los ocho espacios corresponden a inventario único. El ticket ponderado es CLP 800.000 / 16 pagos. La comisión se aplica a cada pago procesado, incluida cada cuota mensual o el pago anual íntegro cuando se realiza en una sola operación.')
    body += '''El escenario mantiene constantes el número de pagos y el ticket durante el horizonte. La sensibilidad analiza por separado sus variaciones y evita atribuir crecimiento automático al transcurso del tiempo. La estimación de mercado se interpreta como proyección de actividad, de acuerdo con la distinción entre antecedentes de mercado y ventas esperadas que establece Sapag Chain y Sapag Chain (2008, pp. 64, 68, 81, 89–90).

### 14.2. Inversión y costos del proyecto

#### 14.2.1. Recursos e inversión preoperativa

El equipo de espaciGo aporta el trabajo de desarrollo y utiliza tres notebooks y un teléfono de propiedad personal y uso compartido. La evaluación no contempla su compra inicial ni su transferencia al patrimonio de la empresa. En consecuencia, el flujo registra CLP 0 de desembolso inicial por estos equipos y no incorpora su venta al cierre.

El presupuesto de valoración del desarrollo asciende a CLP 6.240.000 y corresponde a 960 horas nominales a CLP 6.500 por hora. De esa capacidad, el plan vigente asigna 632 horas al bloque académico hasta el 30 de noviembre, 36 horas a la defensa y 40 horas a la transición preoperativa. No hay horas reales acreditadas; la valoración no constituye remuneración ni egreso de caja. El presupuesto de preparación y lanzamiento asciende a CLP 1.200.000 e incluye formalización, asesoría, contenidos, campaña de lanzamiento y contingencia. La Tabla 14.2 distingue el tratamiento de cada recurso.

'''
    body += cuadro('14.2', 'Recursos preoperativos y tratamiento en la evaluación', table(
        ['Recurso', 'Valor de referencia CLP', 'Tratamiento'], [
            ['Desarrollo del software', '6.240.000', 'Trabajo valorizado del equipo; recuperación económica evaluada por separado'],
            ['Preparación y lanzamiento', '1.200.000', 'Desembolso presupuestado en el Año 0'],
            ['Equipos personales compartidos', '2.700.000', 'Sin compra inicial ni venta por parte de la empresa'],
            ['Desembolso inicial del escenario base', '1.200.000', 'Egreso del flujo de caja en 2026'],
        ]), 'Los valores de referencia de trabajo y equipos no se suman al desembolso inicial. El Anexo H.4 detalla el lanzamiento y el Anexo H.5 desarrolla la valorización del trabajo.')
    body += '''El capital de trabajo se examina mediante el calendario mensual de cobros y pagos y el déficit acumulado máximo. Los déficits operativos forman parte de los flujos de cada período y no se agregan nuevamente como una salida inicial, lo que evita duplicar la necesidad de recursos. La comisión por cobrar se incorpora mediante su variación mensual y su recuperación al finalizar el horizonte (Sapag Chain & Sapag Chain, 2008, pp. 262, 267–269).

#### 14.2.2. Presupuesto de operación

El presupuesto operativo del primer año asciende a CLP 6.168.036,24, equivalente a CLP 514.003,02 mensuales en promedio. Comprende infraestructura AWS, firma y API, marketing, contabilidad, dominio, coordinación, útiles de oficina y dirección tributaria. El marketing operativo de CLP 350.000 mensuales se distingue de la campaña preoperativa incluida en el lanzamiento.

La infraestructura del piloto se presupuesta en USD 26,41 mensuales, convertidos a 972 CLP/USD, para un total de CLP 25.670,52 mensuales. Esta evaluación corresponde al perfil piloto Single-AZ; el escalamiento y la alta disponibilidad constituyen un alcance tecnológico diferente. Los créditos promocionales no se descuentan del costo recurrente del proyecto.

'''
    body += cuadro('14.3', 'Presupuesto operativo mensual promedio del primer año', source_table(oldbody, '24').replace('Subtotal identificado', 'Total operativo'),
                   'El prorrateo permite comparar costos con ingresos mensuales. El dominio y la dirección tributaria se pagan en enero; los demás componentes se distribuyen mensualmente. El Anexo H.3 presenta los valores anuales y el Anexo H.6 concilia el calendario de caja.')
    body += '''El dominio se presupuesta en CLP 9.990 anuales, utilizando como referencia la tarifa publicada por NIC Chile (2026). Los presupuestos expresados en pesos se reajustan un 4 % anual desde el segundo año. El costo AWS en dólares y el tipo de cambio permanecen constantes para aislar la sensibilidad cambiaria del resto de las partidas.

### 14.3. Flujos de caja proyectados

El Año 0 corresponde a 2026 y el período operativo comprende 2027–2030. Los flujos conservan la estructura de ingresos, costos, depreciación, resultado, impuesto, financiamiento e inversión del formato de evaluación del proyecto. Los valores se presentan redondeados a pesos; las memorias mantienen centavos para conciliar los cálculos.

La evaluación utiliza una tasa de impuesto del 27 % como criterio del ejercicio financiero. El impuesto se aplica al resultado positivo después de compensar las pérdidas acumuladas del modelo. Este parámetro de evaluación se distingue del régimen Pro Pyme General contemplado para la organización y de la determinación tributaria efectiva al constituirse. El Anexo H.8 presenta su aplicación por período.

El ingreso se devenga al procesar cada pago. El calendario financiero establece siete días para el cobro de la comisión propia, con mes de treinta días, y evalúa treinta días como escenario de tensión. Los plazos son parámetros del calendario proyectado. En enero de 2027 se cobran CLP 18.400 de comisión neta y quedan CLP 5.600 por cobrar. El calendario de ese mes concentra CLP 660.660,52 de pagos operativos.

#### 14.3.1. Flujo del proyecto sin deuda

El flujo sin deuda permite evaluar la actividad de espaciGo independientemente de su financiamiento. En el escenario base, la recaudación no alcanza el monto requerido para activar las asignaciones del equipo fundador. La Tabla 14.4 presenta la operación, la inversión de lanzamiento y la variación de comisión por cobrar.

'''
    def flow_ready(key, number, title):
        raw = flow(models[key], p, 0, title)
        grid = source_table(raw, '0').replace('Impuesto académico 27 %', 'Impuesto a la renta (27 %)').replace('Préstamo simulado', 'Financiamiento recibido').replace('Flujo de caja simulado', 'Flujo de caja proyectado')
        return cuadro(number, title, grid,
                      'Importes en CLP, redondeados a pesos. El costo de pasarela se descuenta al arrendador y los equipos compartidos no generan depreciación fiscal en este flujo. El IVA y los fondos de los arrendadores se registran separados del ingreso propio. La liquidación final de cuentas por cobrar se presenta en la Tabla 14.8.')
    body += flow_ready('condicionada_puro', '14.4', 'Flujo de caja del proyecto sin deuda')
    body += '''#### 14.3.2. Flujo de la alternativa financiada

La alternativa financiada evalúa un préstamo de CLP 3.720.000 al 12 % anual, amortizado mediante tres cuotas al cierre de cada año. La última cuota incorpora el ajuste de redondeo necesario para extinguir el saldo. El préstamo constituye una entrada de financiamiento y no ingreso por intermediación. La regla de asignaciones excluye los recursos prestados al medir la disponibilidad operativa. El Anexo H.7 presenta el cuadro de amortización.

'''
    body += flow_ready('condicionada_financiado', '14.5', 'Flujo de caja de la alternativa financiada')
    body += '''#### 14.3.3. Flujo con reposición de equipamiento

El escenario de reposición incorpora una compra de notebook de CLP 900.000 en diciembre de 2029. El presupuesto toma como referencia CLP 800.000 y aplica el reajuste anual del 4 % durante tres años, con redondeo presupuestario. La reserva interna de CLP 25.000 mensuales durante 36 meses mantiene liquidez para la adquisición. Su acumulación no constituye un gasto adicional: el flujo registra la compra una sola vez. El análisis conserva la reposición sin deducción fiscal por depreciación, según el tratamiento definido en el Anexo H.14.

'''
    body += flow_ready('estres_reposicion', '14.6', 'Flujo de caja con reposición en el tercer año')
    body += '''#### 14.3.4. Flujo con cobro de comisión a treinta días

La evaluación de liquidez amplía el plazo de cobro de siete a treinta días y mantiene constantes los ingresos devengados y los costos. De esta manera, el efecto corresponde exclusivamente al rezago de caja. En el primer mes no se cobra comisión propia y el saldo por cobrar al finalizar el período asciende a CLP 24.000.

'''
    body += flow_ready('estres_cobro30', '14.7', 'Flujo de caja con plazo de cobro de treinta días')
    body += '''#### 14.3.5. Liquidación al cierre del horizonte

El cierre no incorpora ingreso por venta de activos o software ni valor de continuidad. La comisión devengada hasta diciembre de 2030 se recupera después del corte, en la fecha correspondiente a cada calendario. La recuperación liquida operaciones del horizonte y no representa actividad adicional de un quinto año. El criterio de cierre se refiere al flujo disponible y no a una tasación de la empresa (Sapag Chain & Sapag Chain, 2008, pp. 277–282, 292–295).

'''
    body += cuadro('14.8', 'Liquidación de comisión al cierre del horizonte', source_table(oldbody, '22'),
                   'La recuperación se descuenta en el momento financiero 4 + días/360. Se liquida la comisión generada hasta diciembre de 2030. Las pérdidas operativas no se registran como activos recuperables.')
    body += '''### 14.4. Indicadores de rentabilidad

La evaluación adopta una tasa de descuento nominal anual del 12 % como rentabilidad mínima de referencia común a los escenarios. La tasa permite comparar los flujos bajo un mismo criterio y se somete a sensibilidad al 10 % y al 25 %. La correspondencia entre flujo, destinatario y tasa se desarrolla en el Anexo H.9, siguiendo la metodología de Sapag Chain y Sapag Chain (2008, pp. 321–323, 335–336, 343–356).

El valor actual neto (VAN) descuenta los flujos al cierre de cada año y agrega la liquidación de comisión en su fecha específica. El Anexo H.13 incorpora un control mensual con tasa equivalente para examinar el efecto de las fechas de cobro y pago. Los resultados principales utilizan la convención anual de manera uniforme.

La tasa interna de retorno (TIR) se interpreta de acuerdo con el patrón del flujo. El escenario base presenta egresos netos operativos y una recuperación final reducida; por tanto, no proporciona una TIR útil como medida de rendimiento de la inversión. La alternativa financiada presenta un patrón no convencional. Para los volúmenes de quiebre, la Tabla 14.9 informa las TIR que permiten una interpretación financiera.

'''
    body += cuadro('14.9', 'VAN y TIR de los escenarios de evaluación', source_table(oldbody, '23'),
                   'Se utiliza descuento del 12 % e incluye la liquidación final en su fecha. Las tres últimas filas corresponden a volúmenes calculados para alcanzar VAN no negativo, con asignaciones presupuestadas completas. El Anexo H.11 presenta los pagos mensuales y el Anexo H.13 desarrolla la recuperación.')
    body += '''### 14.5. Sensibilidad y volumen de equilibrio

La sensibilidad modifica una variable por vez: pagos, ticket, costos y tipo de cambio, con variaciones del −20 % y +20 %. La modificación cambiaria afecta al componente AWS. También se comparan tasas de descuento del 10 %, 12 % y 25 %, manteniendo el 12 % como referencia principal. La reposición y el plazo de cobro se examinan separadamente para identificar sus efectos sobre la liquidez y el VAN (Sapag Chain & Sapag Chain, 2008, pp. 371, 375, 398–400, 406).

Con ticket de CLP 50.000, el primer número entero de pagos mensuales con VAN no negativo es 392 sin asignaciones, 793 con CLP 200.000 mensuales por fundador y 2.397 con CLP 1.000.000 por integrante. El cálculo verifica que el número inmediatamente anterior mantiene VAN negativo. Estos umbrales se obtienen bajo el presupuesto del piloto y constituyen objetivos analíticos de volumen; su aplicación a una operación de mayor escala requiere considerar el costo de ese alcance. Los Anexos H.10 y H.11 presentan las pruebas y los escenarios comerciales.

### 14.6. Asignaciones al equipo fundador

La política inicial establece CLP 200.000 mensuales por cada uno de los tres integrantes, para un monto conjunto de CLP 600.000. El pago se activa únicamente cuando la recaudación propia del mes cubre costos programados, provisión de impuesto y reservas de deuda y reposición. Se paga el monto conjunto completo o se mantiene en cero. Los préstamos, aportes, IVA y fondos de los arrendadores se excluyen de la disponibilidad para activar asignaciones.

El estudio evalúa además una meta de CLP 1.000.000 mensuales por integrante. La Tabla 14.10 calcula el volumen operativo requerido para ambas metas mediante el costo mensual promedio y la comisión neta unitaria. Este cálculo difiere del volumen de VAN no negativo, que también considera inversión, reajustes y fechas del horizonte completo.

'''
    body += cuadro('14.10', 'Pagos mensuales requeridos para financiar las asignaciones', source_table(oldbody, '25'),
                   'El cálculo redondea hacia arriba la razón entre costo mensual promedio más asignaciones y comisión neta por pago. El costo promedio es CLP 514.003,02. La regla de pago mensual utiliza el calendario efectivo de la proyección; enero concentra las anualidades. El Anexo H.1 diferencia ambos criterios.')
    body += '''### 14.7. Financiamiento y capacidad de pago

La necesidad de aportes se calcula recorriendo el saldo mensual antes de financiamiento adicional. El aporte mínimo mantiene caja no negativa y cubre las reservas de deuda o reposición programadas. La reserva constituye un piso de liquidez y se libera al pagar la cuota o realizar la compra; el gasto no se descuenta dos veces. La alternativa financiada utiliza primero la disponibilidad que genera el préstamo y calcula después los aportes adicionales.

'''
    body += cuadro('14.11', 'Necesidad de aportes adicionales durante el horizonte', source_table(oldbody, '26'),
                   'Los importes expresan la necesidad de financiamiento de cada alternativa. El préstamo ya se incorpora antes de calcular los aportes adicionales. La liquidación final de comisión no elimina los déficits de períodos anteriores. El Anexo H.12 presenta el total acumulado y la cobertura de deuda.')
    body += '''La referencia sin deuda requiere CLP 26.170.021,53 de aportes acumulados. La alternativa financiada requiere CLP 27.096.476,53 adicionales al préstamo durante el horizonte. La caja operativa previa al servicio de deuda es negativa en los tres años con cuotas; por ello, el escenario base no genera capacidad propia para financiarlas. La disponibilidad de financiamiento externo se distingue de la rentabilidad de la actividad (Sapag Chain & Sapag Chain, 2008, pp. 5–6, 297–298).

### 14.8. Conclusión de la evaluación económica

La proyección base de dieciséis pagos mensuales genera CLP 288.000 de ingreso neto anual frente a CLP 6.168.036,24 de costo operativo en el primer año. El VAN sin deuda es −CLP 20.053.400,45 al 12 %, las asignaciones iniciales no se activan y la operación requiere aportes durante todo el horizonte. La alternativa con préstamo modifica el calendario de financiamiento, pero no corrige el déficit de la actividad.

El proyecto prioriza aumentar el volumen de pagos, revisar el gasto de captación y controlar la caja antes de habilitar asignaciones. Los umbrales permiten medir la distancia respecto de esas metas. La evaluación de desarrollo, reposición y cierre complementa el análisis financiero. El presupuesto del piloto se actualiza con los registros de actividad y el alcance tecnológico implementado.

'''
    (OUT / 'capitulo_xiv_evaluacion_economica.md').write_text(body.rstrip() + '\n')

    annex = '''# Anexo H Evaluación económica detallada

El anexo desarrolla los parámetros, presupuestos y cálculos de la evaluación económica de espaciGo. Las tablas complementan el Capítulo XIV y utilizan la misma comisión, calendario, tasa de descuento y criterio de impuesto. Los valores monetarios se expresan en pesos chilenos, salvo indicación de dólares estadounidenses.

## H.1. Parámetros y política de asignaciones

'''
    annex += cuadro('H.1.1', 'Parámetros generales de evaluación', table(['Parámetro', 'Criterio del proyecto'], [
        ['Año preoperativo y horizonte', '2026; operación 2027–2030'],
        ['Inventario y frecuencia mensual', '8 espacios; 2 pagos por espacio'],
        ['Pagos mensuales y ticket promedio', '16; CLP 50.000'],
        ['Comisión y responsable de costos', '3 % más IVA; descuento al arrendador, junto con la pasarela'],
        ['Descuento nominal anual', '12 %'], ['Impuesto de evaluación', '27 %'],
        ['Reajuste anual de presupuestos CLP', '4 % desde el segundo año'],
        ['Cobro de comisión', '7 días; escenario de tensión de 30 días'],
        ['Tipo de cambio de evaluación', '972 CLP/USD'],
        ['Asignación inicial por integrante', 'CLP 200.000 mensuales, con activación conjunta condicionada'],
        ['Meta adicional por integrante', 'CLP 1.000.000 mensuales'],
    ]), 'Los parámetros definen la proyección económica y se aplican de forma uniforme al cuerpo y al anexo.')
    annex += '''La regla inicial compara la recaudación mensual propia con los pagos programados, la provisión de impuesto y las reservas de deuda y reposición. La asignación conjunta de CLP 600.000 se activa cuando el excedente cubre la totalidad; en otro caso, el pago es cero. La provisión y las reservas controlan disponibilidad, mientras que el flujo reconoce el impuesto, la cuota y la compra en sus respectivas fechas.

El umbral operativo promedio divide costo mensual más asignaciones por la comisión neta unitaria. La activación mensual utiliza cobros y pagos del mes; el quiebre de VAN considera todos los períodos y su descuento. Estas tres mediciones responden a objetivos distintos y no se intercambian.

## H.2. Categorías y proyección de operaciones

'''
    categories = [
        ['Oficina', 'Puestos y condiciones de trabajo'], ['Sala multipropósito', 'Configuración y equipamiento para actividades grupales'],
        ['Bodega', 'Almacenamiento, capacidad y acceso'], ['Estacionamiento', 'Dimensiones y acceso de vehículos'],
        ['Local flexible', 'Recinto comercial y atención temporal'], ['Stand', 'Puesto en ferias, exhibiciones o promociones'],
        ['Quincho', 'Equipamiento para cocinar y reunirse'], ['Parcela de eventos', 'Predio e instalaciones para encuentros'],
        ['Inmuebles', 'Casa, departamento, habitación o cabaña; modalidades de alojamiento y arriendo habitacional'],
    ]
    annex += cuadro('H.2.1', 'Categorías de espacios de espaciGo', table(['Categoría', 'Objeto de la publicación'], categories),
                    'El catálogo comprende nueve categorías. El inventario base suma ocho espacios únicos y no exige disponer de un espacio en cada categoría.')
    annex += cuadro('H.2.2', 'Operaciones e ingresos del escenario base', table(['Concepto', 'Mes', 'Año'], [
        ['Pagos procesados', '16', '192'], ['Monto transado CLP', '800.000', '9.600.000'],
        ['Comisión neta CLP', '24.000', '288.000'], ['IVA de la comisión CLP', '4.560', '54.720'],
        ['Comisión más IVA CLP', '28.560', '342.720'],
    ]), 'La comisión neta es monto transado × 3 %; el IVA se calcula sobre esa comisión. La proyección anual mantiene una distribución mensual constante.')
    annex += '''El ticket promedio ponderado relaciona el valor transado con el número de pagos y reúne las modalidades por hora, día y mes de la Tabla 14.1. Un publicador puede administrar varios espacios y un arrendatario puede efectuar pagos recurrentes. El modelo no transforma transacciones en usuarios únicos mediante una equivalencia uno a uno.

## H.3. Presupuesto de operación

'''
    annex += cuadro('H.3.1', 'Componentes mensuales y anuales del primer año', source_table(oldannex, 'H.32.1').replace('Subtotal identificado', 'Total operativo'),
                    'Las partidas se contabilizan una vez. El costo mensual se expresa como promedio; el calendario paga dominio y dirección tributaria en enero. AWS corresponde al presupuesto del piloto Single-AZ.')
    annex += '''El dominio utiliza como referencia la tarifa anual de CLP 9.990 publicada por NIC Chile (2026). El costo de infraestructura asciende a USD 26,41 × 972 CLP/USD = CLP 25.670,52 mensuales. La evaluación mantiene ese componente constante y reajusta las partidas CLP un 4 % anual. El presupuesto no descuenta créditos promocionales del costo recurrente. La ampliación a alta disponibilidad o mayor escala requiere un presupuesto correspondiente a ese perfil.

## H.4. Presupuesto de preparación y lanzamiento

'''
    annex += cuadro('H.4.1', 'Distribución del presupuesto preoperativo', source_table(oldannex, 'H.32.2'),
                    'El presupuesto se registra en el Año 0. La formalización incluye constitución y trámites. La campaña previa se diferencia de los CLP 350.000 mensuales de marketing operativo. La contingencia forma parte del límite de CLP 1.200.000, sin sumar otro egreso por igual concepto.')
    annex += '''## H.5. Valorización del desarrollo y recursos compartidos

'''+texto_h5()+'''

Los tres notebooks y el teléfono, valorados conjuntamente en CLP 2.700.000, mantienen su carácter personal y compartido. La evaluación no registra compra inicial, aporte patrimonial, depreciación fiscal ni venta de estos bienes por parte de la empresa. La Tabla H.11.2 presenta por separado el volumen necesario para recuperar también la valorización global del desarrollo. Esta distinción evita confundir costo de oportunidad, costo hundido y desembolso de caja (Sapag Chain & Sapag Chain, 2008, pp. 126, 259–262).

## H.6. Calendario de cobros y pagos

Los pagos de dominio y dirección tributaria se concentran en enero de cada año. Los demás costos se distribuyen mensualmente y el último mes concilia los centavos del total anual. El resultado utiliza ingreso y costo devengados, mientras que el flujo refleja las fechas de cobro y pago.

La cuenta por cobrar se calcula como comisión mensual devengada × días de cobro / 30. El cobro del mes corresponde a comisión devengada + saldo inicial por cobrar − saldo final por cobrar. Este tratamiento incorpora el financiamiento de la comisión mediante su variación y evita repetirlo como otra inversión inicial.

'''
    annex += cuadro('H.6.1', 'Calendario de caja del primer trimestre de 2027', source_table(oldannex, 'H.33.1'),
                    'Corresponde al escenario sin deuda y sin asignaciones activadas. Los fondos de arrendadores y el IVA se registran fuera de la caja propia disponible. Los valores mantienen centavos para la conciliación.')
    annex += '''El saldo de CLP 5.600 se recupera siete días después del cierre de diciembre de 2030. El escenario de treinta días acumula CLP 24.000, recuperados a ese plazo. La Tabla 14.8 presenta la liquidación. Su momento financiero es 4 + días/360, sin agregar nuevas operaciones después del horizonte. Los siete y treinta días definen el calendario de evaluación y no se presentan como condiciones contractuales de la pasarela.

## H.7. Alternativa de financiamiento y amortización

'''
    annex += cuadro('H.7.1', 'Amortización de la alternativa de financiamiento', source_table(oldannex, 'H.34.1'),
                    'El principal es CLP 3.720.000, con interés anual del 12 % y tres cuotas. La última cuota ajusta CLP 1 por redondeo. El capital amortizado coincide con el recibido y el saldo final es cero. El cuadro evalúa la alternativa de préstamo del proyecto.')
    annex += '''La cuota comprende interés y abono de capital. El resultado del período descuenta el interés; el flujo de caja descuenta además el capital amortizado. El préstamo se incorpora una vez como entrada inicial. La reserva de servicio de deuda se acumula durante el año y se libera al pagar la cuota; no constituye otro costo financiero.

## H.8. Impuesto y compensación de pérdidas

La evaluación utiliza un impuesto del 27 % durante los cuatro años de operación. La base de cada período corresponde al resultado antes de impuestos positivo después de compensar las pérdidas acumuladas. Un resultado negativo incrementa la pérdida por compensar y no genera una entrada de caja por impuesto. El calendario registra el pago al cierre anual para mantener la correspondencia con el formato de evaluación.

'''
    annex += cuadro('H.8.1', 'Aplicación del impuesto en el escenario sin deuda', table(
        ['Año', 'Resultado antes de impuesto CLP', 'Pérdida por compensar acumulada CLP', 'Impuesto CLP'],
        [[row['anio'], money(row['ebt_clp']), money(sum(min(Decimal(x['ebt_clp']), 0) for x in base['anual'][:i+1]) * -1), money(row['impuesto_clp'])] for i, row in enumerate(base['anual'])]),
        'La operación base mantiene pérdidas, por lo que no genera impuesto. El 27 % es el criterio financiero de evaluación; se distingue de la determinación tributaria efectiva y del régimen Pro Pyme General contemplado para la empresa.')
    annex += '''## H.9. Tasa de descuento y criterio de evaluación

espaciGo adopta el 12 % nominal anual como rentabilidad mínima de referencia para comparar las alternativas del estudio. La elección mantiene un criterio uniforme de evaluación y se examina mediante sensibilidad al 10 % y al 25 %. El porcentaje es una decisión metodológica del proyecto y no una tasa prescrita por Sapag ni un costo de capital derivado de CAPM o WACC.

El VAN descuenta cada flujo anual mediante (1 + 0,12) elevado al número de período, incorpora el Año 0 sin descuento y suma la recuperación final de comisión en su fecha. Un VAN no negativo indica que el flujo alcanza la referencia adoptada. La TIR se compara con el descuento cuando el patrón del flujo permite una interpretación de inversión. La recuperación simple y descontada complementa estos indicadores (Sapag Chain & Sapag Chain, 2008, pp. 321–323, 329–330, 335–336, 343–356).

La tasa de descuento, el interés del préstamo y el impuesto tienen funciones diferentes. El descuento valora los flujos en el tiempo; el interés determina el servicio de la deuda; el impuesto grava la base de resultados del ejercicio. Una mayor tasa de descuento no modifica las ventas ni elimina el riesgo operativo. El análisis de sensibilidad permite observar el efecto de cada variable sin cambiar el escenario base.

## H.10. Sensibilidad y escenarios comerciales

'''
    annex += cuadro('H.10.1', 'Sensibilidad del VAN respecto del escenario base', source_table(oldannex, 'H.36.1'),
                    'Se modifica una variable por vez. El cambio de tipo de cambio afecta a AWS; la comisión se mantiene en 3 %. Las pruebas son deterministas y no asignan probabilidades a los escenarios.')
    annex += cuadro('H.10.2', 'Escenarios de volumen y ticket de espaciGo', source_table(oldannex, 'H.36.3'),
                    'Los escenarios conservador, base y optimista utilizan la misma comisión y el mismo calendario de costos. Los volúmenes representan proyecciones alternativas. La fila base coincide con el flujo de la Tabla 14.4.')
    annex += '''Los tres escenarios mantienen VAN negativo con el presupuesto operativo definido. La sensibilidad identifica la importancia del gasto recurrente frente al ingreso por comisión y permite evaluar cambios de volumen y ticket sin atribuirles probabilidades de ocurrencia. La reposición y el plazo de cobro se presentan en las Tablas 14.6 y 14.7.

## H.11. Volúmenes de quiebre del VAN

'''
    annex += cuadro('H.11.1', 'Número mínimo de pagos mensuales para VAN no negativo', source_table(oldannex, 'H.36.2'),
                    'El ticket es CLP 50.000, el descuento 12 % y se incluye liquidación diferida. Las metas utilizan asignaciones completas presupuestadas. Se verifica el entero anterior para establecer el mínimo. El cálculo mantiene los costos del perfil piloto.')
    annex += cuadro('H.11.2', 'Volumen requerido al recuperar también el desarrollo valorizado', source_table(oldannex, 'H.40.1'),
                    'El análisis agrega CLP 6.240.000 de valorización una vez en el momento cero, sin deducción fiscal ni incorporación a los aportes de efectivo. Los flujos principales se mantienen separados de este criterio de recuperación económica.')
    annex += '''El número de pagos es una meta de actividad financiera y no una cantidad de usuarios únicos. La equivalencia depende de la recurrencia de arrendatarios y del número de espacios administrados por cada publicador. La ampliación de actividad se evalúa junto con los costos de captación, soporte e infraestructura correspondientes al volumen que se implemente.

## H.12. Aportes y cobertura de deuda

El cálculo recorre 49 momentos de caja, incluido el Año 0. En cada mes, el aporte mínimo corresponde al máximo entre cero y la reserva objetivo menos la caja anterior al aporte. La reserva de cuota se acumula durante el año y la de reposición hasta la compra. Su liberación permite pagar la obligación sin registrar un gasto duplicado. En el caso sin reservas, el piso de caja es cero.

'''
    annex += cuadro('H.12.1', 'Aportes acumulados y caja posterior a la liquidación', source_table(oldannex, 'H.37.1'),
                    'Los aportes expresan necesidades de financiamiento. La alternativa financiada incorpora primero el préstamo y luego calcula los recursos adicionales. La recuperación final de comisión liquida una cuenta por cobrar y no representa un beneficio operativo adicional.')
    annex += cuadro('H.12.2', 'Cobertura del servicio de deuda con caja operativa propia', source_table(oldannex, 'H.37.2'),
                    'La cobertura divide caja propia antes de cuotas por interés más amortización. Un resultado negativo expresa insuficiencia operativa para atender el servicio de deuda. En 2030 no existe cuota.')
    annex += '''## H.13. Convenciones de fechas y recuperación

El VAN principal utiliza cierres anuales y liquidación de comisión en su fecha financiera. El control mensual descuenta los importes mediante (1 + 0,12) elevado a período/12, y mantiene la fecha de liquidación. La diferencia entre ambas convenciones responde a la oportunidad de los cobros y pagos, no a tasas principales distintas.

'''
    annex += cuadro('H.13.1', 'VAN según fecha de valoración del escenario base', source_table(oldannex, 'H.38.1'),
                    'La primera fila excluye la recuperación posterior; las otras dos la incluyen en su fecha. Los resultados principales del capítulo y los volúmenes de quiebre utilizan cierres anuales más liquidación.')
    annex += '''El escenario base presenta flujos operativos negativos y una recuperación final reducida. Una raíz numérica extrema no representa una medida útil del rendimiento de la inversión. Por ello, la Tabla 14.9 informa la ausencia de TIR útil para la referencia y los escenarios de tensión. El patrón financiado también se distingue de un flujo convencional de inversión.

'''
    annex += cuadro('H.13.2', 'Recuperación en los volúmenes de quiebre', source_table(oldannex, 'H.38.2'),
                    'La recuperación se interpola entre momentos anuales y liquidación final cuando corresponde. Los años se miden desde el momento inicial; la interpolación constituye una medida financiera y no una fecha contractual de cobro. El escenario base no recupera la inversión dentro del horizonte ampliado.')
    annex += '''## H.14. Reposición y cierre del horizonte

La reposición considera un notebook de CLP 900.000 en diciembre de 2029. El cálculo utiliza CLP 800.000 × (1,04)³ = CLP 899.891,20 y redondea a CLP 900.000 para el presupuesto. Una reserva de CLP 25.000 mensuales durante 36 meses acumula el importe de compra. La reserva mantiene un piso de liquidez y restringe la disponibilidad para asignaciones, mientras que la compra constituye el único egreso por adquisición. La prueba no incorpora deducción fiscal por depreciación del equipo de reposición.

El cierre establece ingreso por venta de activos y software igual a cero, sin perpetuidad. El criterio evita depender de una venta futura y no constituye una tasación de los bienes o de la empresa. Los equipos personales compartidos no se venden como patrimonio de espaciGo. La cuenta por cobrar se recupera por separado conforme a la Tabla 14.8. Las pérdidas acumuladas no se recuperan como capital de trabajo (Sapag Chain & Sapag Chain, 2008, pp. 277–282, 292–295).

El alcance de la evaluación comprende el presupuesto del piloto, las asignaciones modeladas y las condiciones financieras descritas. La contratación de proveedores, el tratamiento tributario efectivo, las devoluciones, las cargas asociadas a la modalidad de remuneración y el costo del escalamiento pertenecen al control económico de la operación. El modelo se actualiza con esos registros conservando la separación entre ingreso propio, fondos de terceros, financiamiento y trabajo valorizado.

## Referencias

NIC Chile. (2026). *Tarifas de dominios .cl*. https://www.nic.cl/dominios/tarifas.html

Sapag Chain, N., & Sapag Chain, R. (2008). *Preparación y evaluación de proyectos* (5.ª ed.). McGraw-Hill Interamericana.
'''
    (OUT / 'anexo_h_evaluacion_economica.md').write_text(annex.rstrip() + '\n')
    manifest = {'version': 1, 'id': 'evaluacion_economica_espacigo', 'metadata': {
        'title': 'Evaluación económica de espaciGo',
        'subtitle': 'Capítulo XIV y Anexo H',
        'authors': ['Espinoza Castillo, Hernán', 'Marchant Pacheco, Anita', 'Silva Quezada, Erick'],
        'lang': 'es-CL', 'date': '16 de noviembre de 2026'},
        'sections': ['capitulo_xiv_evaluacion_economica.md', 'anexo_h_evaluacion_economica.md'],
        'appendices': [], 'template': 'templates/reference.docx', 'style_profile': 'templates/style-profile.json',
        'output': 'Evaluacion_economica_espaciGo.docx', 'toc': {'enabled': False}}
    (OUT / 'document.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print('Redacción académica generada; el modelo financiero y los antecedentes históricos no cambian.')


if __name__ == '__main__':
    main()
