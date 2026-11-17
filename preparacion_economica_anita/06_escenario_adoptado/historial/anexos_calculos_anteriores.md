## H.27. Memoria actualizada de las metas de remuneración

Este apartado respalda las Tablas 20 y 21 y se actualiza con la conciliación de útiles de oficina. Los cálculos anteriores sin esa partida son un corte histórico. Se conserva su procedencia en la historia del repositorio.

El presupuesto mensual sin fundadores es CLP 514.083,02: la base parcial de CLP 491.583,02 más CLP 10.000 de útiles y CLP 12.500 de dirección tributaria. Los útiles proceden de Conciliacion costos!H9 y la periodicidad anual de la dirección es ratificada por el propietario. Con la meta conjunta inicial de CLP 600.000, se requieren CLP 1.114.083,02 de comisión neta. A ticket de CLP 50.000 y comisión neta de CLP 1.500 por cobro, el mínimo entero es 743 pagos: 742 producen CLP 1.113.000 y no alcanzan; 743 producen CLP 1.114.500. Para CLP 1.000.000 por fundador, el mínimo es 2.343 pagos.

El cálculo redondea hacia arriba (costo parcial + tres asignaciones objetivo) dividido por (ticket multiplicado por 0,03). Los costos variables propios que se determinen reducen la contribución por cobro. El script calcular_tickets_remuneraciones.py lee los componentes y genera umbrales_remuneraciones.json y umbral_sueldo_objetivo.json. La comparación con fuente y las proyecciones se documentan en H.31–H.35.

## H.28. Supuesto fiscal académico y calendario de evaluación

La empresa aún no se constituye. La preparación mantiene Pro Pyme General como régimen proyectado, sin afirmar inscripción vigente ante el SII. La actividad se modela como intermediación: los publicadores arriendan sus espacios y la plataforma cobra su comisión. Para el cálculo académico se conserva el impuesto fijo del 27 % utilizado por Anita, según la instrucción docente comunicada por el propietario. Esta elección metodológica no se presenta como tasa legal del régimen proyectado.

**Tabla H.28.1**
*Tasa de impuesto adoptada para el ejercicio académico*

| Período | Año comercial | Año tributario | Tasa académica |
|---|---|---|---|
| 1 | 2027 | 2028 | 27 % |
| 2 | 2028 | 2029 | 27 % |
| 3 | 2029 | 2030 | 27 % |
| 4 | 2030 | 2031 | 27 % |

*Nota.* Elaboración a partir del modelo de Anita y del criterio docente comunicado por el propietario el 16 de noviembre de 2026. Se utiliza 27 % fijo como supuesto de evaluación académica. El Año 0 de preparación corresponde a 2026. La tabla no constituye una determinación de la tasa legal aplicable al régimen proyectado.

El flujo conserva las columnas, partidas y secuencia de Anita. El impuesto se calcula sobre la base de resultados y ajustes del ejercicio, considerando las pérdidas que correspondan al modelo. Los fondos de terceros y el IVA se separan del ingreso propio. El trabajo valorizado, la depreciación y los desembolsos se concilian para evitar doble conteo. La serie definitiva y sus indicadores requieren cerrar los demás parámetros pendientes.

La tasa de descuento del ejercicio es 12 % nominal anual, según confirmación de Anita comunicada por el propietario. Se distingue del impuesto fijo del 27 % y de la comisión del 3 % más IVA. El interés del préstamo simulado también es 12 %, pero no se confunde con la rentabilidad mínima de evaluación. El 10 % y el 25 % dejan de utilizarse como tasas principales. El Anexo H.29 fundamenta la elección metodológica y el alcance del criterio.

Fuentes del supuesto académico: informe de Anita, sección 5.3; hoja FlujoNeto, A29:F45; instrucción del propietario del 16 de noviembre de 2026. Los parámetros se conservan en 02_contraste/parametros_tributarios.json. El contraste legal anterior permanece identificado como antecedente no aplicado al cálculo académico, para no confundirlo con el criterio adoptado.


## H.29. Fundamentación de la tasa de descuento adoptada

El ejercicio adopta 12 % nominal anual como tasa de descuento, según confirmación de Anita y ratificación del propietario del 16 de noviembre de 2026. Esta decisión sustituye el criterio previo del 25 % y fija una sola tasa base para los indicadores y escenarios de la preparación actualizada. El 10 % mencionado en el informe original se conserva únicamente en la extracción histórica, sin utilizarlo como criterio principal.

La elección se fundamenta metodológicamente en mantener la tasa de referencia del estudio económico aportado y comparar los escenarios bajo una rentabilidad mínima común. La tasa se aplica con periodicidad anual y en términos nominales, coherentes con flujos que incorporan los reajustes de precios y costos definidos por el modelo. El valor del VAN es la suma de cada flujo anual dividido por (1 + 0,12) elevado al número de período; el flujo del Año 0 no se descuenta.

La fuente recibida no deriva el 12 % a partir de un modelo propio de costo de capital. La confirmación de la autora acredita el parámetro elegido y no una estimación empírica del riesgo. Sapag exige distinguir rentabilidad del proyecto, rentabilidad del inversionista y capacidad de pago, y relaciona el costo de capital con alternativas de riesgo comparable (Sapag Chain & Sapag Chain, 2008, pp. 5–6, 343–345, 353–356). El marco metodológico exige distinguir el flujo para los socios del flujo del proyecto y usar una tasa apropiada al destinatario del flujo. El estudio mantiene esa distinción al separar inversión, costo de oportunidad y financiamiento simulado. No se inventan primas de riesgo para obtener el porcentaje adoptado.

La coincidencia entre descuento del 12 % e interés del préstamo del 12 % no implica que sean el mismo concepto. El primero es la rentabilidad mínima de referencia para evaluar; el segundo corresponde al servicio de una deuda simulada. La incertidumbre comercial y tecnológica se examina con sensibilidad de demanda, precio, gastos y tasa. Un descuento menor no reduce el riesgo operativo ni aumenta por sí mismo las ventas: modifica el valor presente asignado a los flujos esperados.

El crecimiento en años posteriores se incorpora mediante cobros, comisiones y costos proyectados con sustento. El horizonte actual conserva los Años 0 a 4 del formato de Anita. Una eventual extensión al Año 5 requiere un escenario explícito, incluyendo capital de trabajo y demás partidas; no se añade un año o valor terminal únicamente para obtener un VAN positivo.

Sobre el vector original [−6.420.000, −1.278.818, 445.097, 2.104.062, 5.378.456], el VAN al 12 % es CLP −2.291.237,39 y la TIR es aproximadamente 0,85115 %. Son comprobaciones históricas y no resultados del flujo nuevo pendiente de cierre. Para un flujo convencional de inversión, el criterio compara VAN con cero y TIR con el 12 %; si no existe TIR interpretable o hay múltiples soluciones, se informa esa condición.

Fuentes: informe de Anita, sección 5.3; confirmación de la autora comunicada por el propietario el 16 de noviembre de 2026; Sapag Chain y Sapag Chain (2008, pp. 321–323, 335–336, 343–356). El libro respalda el método y la correspondencia entre flujos y tasas; no prescribe un 12 % para espaciGo. El ejemplo del libro que utiliza 12 % en la página 296 es un caso ilustrativo, no una tasa general obligatoria.

## H.30. Aplicación del método de Sapag al formato económico

### H.30.1. Fuente y alcance

La preparación utiliza como referencia principal Sapag Chain y Sapag Chain (2008), quinta edición. Las páginas citadas corresponden a la numeración impresa; en la copia local la página PDF equivale a la impresa más 18. El método se adapta a la intermediación digital y no impone partidas industriales que no correspondan al proyecto. La evaluación privada se concentra en los flujos de inversión, operación y financiamiento; no se presenta como evaluación social completa.

### H.30.2. Correspondencia del flujo

**Tabla H.30.1**
*Correspondencia entre la estructura de Sapag y el flujo de Anita*

| ID | Bloque metodológico | Aplicación al formato recibido | Respaldo impreso |
|---|---|---|---|
| 1 | Ingresos y egresos afectos | Comisiones y costos propios; separar IVA y arriendos de terceros. | pp. 293–294 |
| 2 | Gastos no desembolsables | Depreciación y amortización: efecto fiscal y ajuste de caja. | pp. 293–297 |
| 3 | Impuesto y resultado | 27 % académico; conciliar base y pérdidas. | pp. 293–297 |
| 4 | Ajustes de caja | Reincorporar gastos sin desembolso; evitar duplicidades. | pp. 294–297 |
| 5 | Inversión y capital de trabajo | Aportes iniciales, reinversión y capital de trabajo. | pp. 259–269, 295 |
| 6 | Cierre del horizonte | Valor de desecho y recuperación sin duplicaciones. | pp. 277–282, 295 |
| 7 | Flujo del inversionista | Préstamo, interés antes de impuesto y principal después. | pp. 297–298 |

*Nota.* Elaboración propia a partir de Sapag Chain y Sapag Chain (2008). La tabla relaciona conceptos y conserva la secuencia del flujo de Anita. Las cifras originales se mantienen como antecedentes; la equivalencia metodológica no certifica sus supuestos ni la viabilidad del escenario actualizado.

### H.30.3. Inversión y costos pertinentes

La memoria de recursos distingue desembolso incremental futuro, pago irreversible ya comprometido y costo de oportunidad con uso alternativo. No se elimina todo trabajo valorizado por no ser efectivo ni se agrega a caja como si fuera una compra pagada. La clasificación se realiza a la fecha de decisión y se vincula con cada recurso. Se concilian equipos aportados, compras, depreciación y reposición durante la operación (Sapag Chain & Sapag Chain, 2008, pp. 126, 259–262, 269).

### H.30.4. Calendario y capital de trabajo

El método propuesto de déficit acumulado máximo calcula cobros y pagos mensuales, antes de aportes de financiamiento, y determina la máxima necesidad de recursos acumulada. Su aplicación requiere identificar rezagos, estacionalidad y el ciclo de liquidación. La inversión y los gastos de preparación se registran por separado para no financiarlos dos veces. Los arriendos de terceros y el IVA no se convierten en caja libre del negocio. La falta persistente de ingresos para cubrir operación también debe explicarse como necesidad de financiamiento de pérdidas (Sapag Chain & Sapag Chain, 2008, pp. 134–135, 262, 267–269).

### H.30.5. Horizonte y valor de cierre

El caso base conserva cuatro años de operación y un Año 0 de preparación. La evaluación debe resolver el valor remanente de activos o de continuidad y justificar sus datos. Si se usa un método económico que incorpora el negocio funcionando, no se añade nuevamente la recuperación de capital de trabajo. El valor patrimonial de cierre se distingue del efectivo disponible. Se puede estudiar un quinto año mediante un escenario completo, sin prolongar ingresos aisladamente ni introducir una perpetuidad para cambiar el signo del VAN (Sapag Chain & Sapag Chain, 2008, pp. 277–282, 292, 295).

### H.30.6. Indicadores y sensibilidad

El VAN se calcula sobre una serie identificada, con Año 0 sin descuento, y la TIR se interpreta según los signos del flujo. Se distingue recuperación simple de descontada. El umbral operativo de la sección 14.6 no equivale al volumen que produce VAN igual a cero. La sensibilidad modifica variables desde una base única y revela los puntos de quiebre; las probabilidades y distribuciones no se inventan cuando solo se dispone de escenarios ilustrativos (Sapag Chain & Sapag Chain, 2008, pp. 129–130, 321–323, 329–330, 371, 398–400, 406).

### H.30.7. Condiciones de cierre de la preparación

El escenario actualizado requiere completar demanda mensual, costos, inversión pertinente, caja con IVA, tratamiento de pérdidas con impuesto académico, capital de trabajo, valor de cierre y deuda simulada. Los flujos puro y financiado se presentan completos en el cuerpo cuando se concilien; el anexo respalda los supuestos y cálculos. Las tareas abiertas no se identifican como resultados financieros obtenidos. El 12 % de descuento y el 27 % de impuesto continúan como decisiones del ejercicio, sin atribuir su prescripción al libro.

### H.30.8. Referencia metodológica

Sapag Chain, N., & Sapag Chain, R. (2008). Preparación y evaluación de proyectos (5.ª ed.). McGraw-Hill Interamericana.

## H.31. Proyección comercial agregada y categorías

La referencia conserva ocho espacios promedio, dos pagos mensuales por espacio y ticket de CLP 50.000. No se añade crecimiento de volumen o precio sin una decisión respaldada. El archivo proyeccion_mensual_2027_2030.csv registra los 48 meses con comisión, IVA y fondos de publicadores separados. La tabla siguiente no reparte los ocho espacios entre categorías, porque ese dato aún no está definido. Nueve categorías disponibles no implica nueve espacios activos ni demanda validada en todas ellas.

**Tabla H.31.1**
*Estado de asignación de la oferta por categoría*

| ID | Categoría | Espacios y pagos | Ticket y mezcla |
|---|---|---|---|
| 1 | Oficina | Pendiente de asignar | Pendiente de ratificar |
| 2 | Sala multipropósito | Pendiente de asignar | Pendiente de ratificar |
| 3 | Bodega | Pendiente de asignar | Pendiente de ratificar |
| 4 | Estacionamiento | Pendiente de asignar | Pendiente de ratificar |
| 5 | Local flexible | Pendiente de asignar | Pendiente de ratificar |
| 6 | Stand | Pendiente de asignar | Pendiente de ratificar |
| 7 | Quincho | Pendiente de asignar | Pendiente de ratificar |
| 8 | Parcela de eventos | Pendiente de asignar | Pendiente de ratificar |
| 9 | Inmuebles | Pendiente de asignar | Pendiente de ratificar |

*Nota.* Catálogo de nueve categorías comunicado por el propietario. No se sustituyen datos faltantes por ceros observados. La referencia agregada puede calcularse sin atribuir ventas a una categoría. La mezcla de modalidades previa se conserva como ejemplo no ratificado.

**Tabla H.31.2**
*Proyección comercial agregada sin crecimiento automático*

| Año | Pagos anuales | GMV CLP | Comisión neta CLP | IVA de comisión CLP |
|---|---|---|---|---|
| 2027 | 192 | 9.600.000,00 | 288.000,00 | 54.720,00 |
| 2028 | 192 | 9.600.000,00 | 288.000,00 | 54.720,00 |
| 2029 | 192 | 9.600.000,00 | 288.000,00 | 54.720,00 |
| 2030 | 192 | 9.600.000,00 | 288.000,00 | 54.720,00 |

*Nota.* Elaboración con los parámetros agregados ratificados como referencia provisional. El total transado no es ingreso propio de espaciGo. Por mes, el saldo de publicadores antes de Mercado Pago es CLP 771.440; el abono final no se determina sin la tarifa y liquidación efectivas.

## H.32. Recursos y presupuesto conciliado

Los tres notebooks y el teléfono son personales y compartidos, según el propietario. Su compra inicial se fija en cero y no se presume transferencia de dominio a la empresa proyectada. Se mantienen separados el uso alternativo y eventuales costos incrementales; no se asigna a la empresa una depreciación o venta de bienes personales sin respaldo. El presupuesto de CLP 1.200.000 de lanzamiento se mantiene provisional en el Año 0, sin duplicarlo con marketing operativo.

**Tabla H.32.1**
*Componentes del presupuesto identificado del Año 1*

| ID | Componente | Mensual CLP | Anual CLP |
|---|---|---|---|
| C01 | AWS | 25.670,52 | 308.046,24 |
| C02 | Firma y API | 50.000,00 | 600.000,00 |
| C03 | Marketing | 350.000,00 | 4.200.000,00 |
| C04 | Contabilidad | 50.000,00 | 600.000,00 |
| C05 | Dominio | 912,50 | 10.950,00 |
| C06 | Coordinación | 15.000,00 | 180.000,00 |
| C07 | Útiles de oficina | 10.000,00 | 120.000,00 |
| C08 | Dirección tributaria | 12.500,00 | 150.000,00 |
| Total | Subtotal parcial | 514.083,02 | 6.168.996,24 |

*Nota.* Presupuestos de Base mensual!B21:B25 y Conciliacion costos!H9, con sustitución de GCP por el escenario AWS adoptado y dirección tributaria anual ratificada. Los útiles y la dirección se cuentan una sola vez. El importe anual de dirección se prorratea como referencia, sin afirmar facturación mensual efectiva. Se mantienen fuera los subtotales genéricos y los conceptos suspendidos de mantenimiento o respaldo sin alcance independiente. La tabla no equivale a costos contratados o facturados.

La constitución y los trámites se incluyen en los CLP 1.200.000 de lanzamiento y no se suman otra vez. Las cargas de contratación, costos residuales propios, recursos de uso alternativo y reposiciones carecen de valoración completa. Se registran como pendientes y no como cero real. La depreciación no se reconoce en el subtotal hasta definir el eventual aporte de equipos. Los CLP 6.240.000 de desarrollo valorizado tampoco se suman como pago inicial: se debe distinguir trabajo pasado, compromiso irreversible y trabajo incremental futuro.

## H.33. Caja de referencia y necesidad de financiación

Los costos identificados se proyectan mensualmente, con reajuste del 4 % anual para presupuestos CLP y costo AWS constante bajo el USD y cambio adoptados. La proyección no aplica créditos y no garantiza capacidad cloud para otros volúmenes. El IVA de comisión se reserva separado; el crédito por compras y las fechas efectivas de remisión permanecen pendientes. El impuesto del ejercicio se liquida al cierre anual por convención de la simulación, no como calendario fiscal real.

El caso de pago condicionado a fundadores utiliza solo excedente propio después de costos identificados, reserva de servicio de deuda y provisión académica de impuesto. Nunca utiliza préstamos, IVA o fondos de publicadores para activar la distribución. En la referencia agregada, el pago es cero durante el horizonte. Los escenarios con CLP 200.000 y CLP 1.000.000 efectivamente presupuestados por persona se calculan por separado, sin afirmar que exista caja para pagarlos. En el ejercicio se tratan como egreso de personal; la modalidad jurídica y la deducibilidad real se mantienen pendientes.

**Tabla H.33.1**
*Resultados operativos parciales del escenario agregado*

| Año | Comisión neta CLP | Costos identificados CLP | Pago condicionado CLP | Flujo operativo parcial CLP |
|---|---|---|---|---|
| 2027 | 288.000,00 | 6.168.996,24 | 0,00 | -5.880.996,24 |
| 2028 | 288.000,00 | 6.403.434,24 | 0,00 | -6.115.434,24 |
| 2029 | 288.000,00 | 6.647.249,76 | 0,00 | -6.359.249,76 |
| 2030 | 288.000,00 | 6.900.817,92 | 0,00 | -6.612.817,92 |

*Nota.* Caso sin deuda, antes de partidas excluidas. La compra de equipos es cero; el lanzamiento presupuestado de CLP 1.200.000 figura en el Año 0 del flujo del cuerpo. La necesidad acumulada de financiación parcial, incluyendo ese lanzamiento, alcanza CLP 26.168.498,16. Es financiación de déficit persistente, no capital de trabajo del ciclo determinado. No se suma nuevamente al Año 0 además de las pérdidas operativas.

**Tabla H.33.2**
*Comparación parcial de los escenarios de demanda del insumo*

| Escenario | Pagos mensuales | Ticket CLP | Comisión Año 1 CLP | VAN parcial al 12 % CLP |
|---|---|---|---|---|
| conservador | 4 | 35.000 | 50.400,00 | -20.776.704,15 |
| base | 16 | 50.000 | 288.000,00 | -20.055.029,94 |
| optimista | 45 | 65.000 | 1.053.000,00 | -17.731.457,69 |

*Nota.* Sin probabilidades atribuidas y sin ajuste de demanda para producir rentabilidad. El costo cloud y otros consumos deben reestimarse al cambiar el volumen; la comparación es un primer cálculo parcial, no una evaluación cerrada de capacidad o viabilidad.

## H.34. Corrección de la deuda simulada

Se calcula el préstamo de CLP 3.720.000 al 12 % anual y tres años con cuotas anuales, como el insumo. La cuota de referencia redondeada es CLP 1.548.818. La última cuota incorpora CLP 1 adicional para extinguir la deuda y conciliar capital amortizado con capital recibido. La simulación no acredita contratación, CAE, seguros ni comisiones.

**Tabla H.34.1**
*Amortización conciliada hasta saldo cero*

| Año | Saldo inicial CLP | Interés CLP | Amortización CLP | Cuota CLP | Saldo final CLP |
|---|---|---|---|---|---|
| 1 | 3.720.000 | 446.400 | 1.102.418 | 1.548.818 | 2.617.582 |
| 2 | 2.617.582 | 314.110 | 1.234.708 | 1.548.818 | 1.382.874 |
| 3 | 1.382.874 | 165.945 | 1.382.874 | 1.548.819 | 0 |

*Nota.* El principal amortizado totaliza CLP 3.720.000 y el saldo final es cero. La entrada del préstamo no se incluye como ingreso por comisiones. El flujo financiado del cuerpo presenta el efecto de la deuda y sus pagos.

## H.35. Conciliación demostrativa de pérdidas históricas

Esta comprobación conserva el 27 % y aplica el criterio de compensar pérdidas que describe el informe de Anita. Supone pérdidas iniciales cero y utiliza solo el EBT del bloque histórico corregido. No determina una base fiscal real ni reemplaza la conciliación del escenario actualizado.

**Tabla H.35.1**
*Impuesto histórico frente a compensación de pérdidas del ejercicio*

| Año | EBT CLP | Pérdida compensada CLP | Impuesto fuente CLP | Impuesto recalculado CLP | Diferencia CLP |
|---|---|---|---|---|---|
| 1 | -956.400 | 0 | 0 | 0 | 0 |
| 2 | 1.232.610 | 956.400 | 332.805 | 74.577 | 258.228 |
| 3 | 3.708.132 | 0 | 1.001.196 | 1.001.196 | 0 |
| 4 | 7.367.748 | 0 | 1.989.292 | 1.989.292 | 0 |

*Nota.* En el Año 2, CLP 1.232.610 menos CLP 956.400 deja una base de CLP 276.210. Al 27 %, el impuesto es CLP 74.576,70, redondeado a CLP 74.577. La diferencia con CLP 332.805 del origen es CLP 258.228. La corrección concilia la explicación con la tabla bajo este supuesto, sin alterar la extracción original.

## H.36. Coherencia y sensibilidad del segundo corte

La comprobación conserva la comisión neta del 3 %, la tasa de descuento base del 12 %, el impuesto académico del 27 % y los cuatro años 2027 a 2030. Cada sensibilidad cambia un solo parámetro y mantiene los demás. Los cambios de menos y más 20 % son rangos exploratorios definidos en esta revisión; no provienen de distribuciones observadas ni expresan certeza estadística. El caso base mantiene 16 cobros de CLP 50.000 al mes y pago condicionado cero.

**Tabla H.36.1**
*Sensibilidad individual del VAN parcial del caso base*

| Variable | Prueba | VAN parcial CLP | Cambio del VAN CLP |
|---|---|---|---|
| Cobros mensuales | -20 % de variación | -20.229.981 | -174.951 |
| Cobros mensuales | 20 % de variación | -19.880.079 | 174.951 |
| Ticket medio | -20 % de variación | -20.229.981 | -174.951 |
| Ticket medio | 20 % de variación | -19.880.079 | 174.951 |
| Costos identificados | -20 % de variación | -16.109.073 | 3.945.957 |
| Costos identificados | 20 % de variación | -24.000.987 | -3.945.957 |
| CLP por USD | -20 % de variación | -19.867.901 | 187.129 |
| CLP por USD | 20 % de variación | -20.242.159 | -187.129 |
| Tasa de descuento | 10 % anual | -20.894.880 | -839.850 |
| Tasa de descuento | 12 % anual | -20.055.030 | 0 |
| Tasa de descuento | 25 % anual | -15.783.221 | 4.271.809 |

*Nota.* Elaboración mediante el modelo reproducible. Valores redondeados a pesos para presentación. La variación cambiaria afecta solo a AWS; la de costos afecta a las ocho partidas identificadas. No se modifican el lanzamiento ni la comisión. Se mantienen las exclusiones del corte base. Un VAN menos negativo al elevar la tasa sobre flujos de salida no acredita menor riesgo. No se estiman costos cloud de escalamiento ni efectos de demanda cruzados.

**Tabla H.36.2**
*Umbrales operativos parciales por año sin deuda*

| Año | Costo mensual CLP | Pagos para $200.000 por persona | Pagos para $1.000.000 por persona |
|---|---|---|---|
| 2027 | 514.083 | 743 | 2.343 |
| 2028 | 533.620 | 756 | 2.356 |
| 2029 | 553.937 | 770 | 2.370 |
| 2030 | 575.068 | 784 | 2.384 |

*Nota.* Ticket de CLP 50.000, comisión de CLP 1.500 por pago y tres personas. El costo mensual es un prorrateo presupuestario, no una fecha contractual de pago. Los útiles, la dirección tributaria y el dominio no acreditan facturación mensual. La meta se mantiene nominal constante y los costos CLP se reajustan 4 %. La regla de pago condicionado a 743 cobros activa CLP 600.000 al mes solo en el Año 1 y cero en los demás. Los umbrales cubren costos y asignaciones del año; no incorporan recuperación del lanzamiento, deuda, costos omitidos ni VAN cero.

**Tabla H.36.3**
*Quiebre del VAN anual parcial con asignaciones presupuestadas constantes*

| Meta por persona CLP | Pagos mensuales mínimos | VAN con un pago menos CLP | VAN con el mínimo CLP |
|---|---|---|---|
| 200.000 | 791 | -37.544 | 2.367 |
| 1.000.000 | 2.391 | -37.544 | 2.367 |

*Nota.* Búsqueda numérica del volumen mensual uniforme a ticket de CLP 50.000. Se presupuestan las asignaciones completas como gasto académico, con independencia de que el escenario disponga de caja; no se cambia la decisión de pago condicionado. El flujo es puro, el Año 0 incluye CLP 1.200.000 de lanzamiento, el impuesto académico considera compensación de pérdidas y el VAN se descuenta al 12 % al cierre de cada año. El cálculo redondea hacia arriba el cruce y verifica los dos enteros adyacentes. El costo identificado no aumenta por volumen en esta prueba; antes de una decisión comercial se deben valorar escalamiento, recursos de oportunidad, cargas de contratación, capital del ciclo y cierre. El resultado no es una meta de captación validada.

### H.36.4. Convenciones de fechas y límites de cierre

La tasa mensual equivalente es (1 + 0,12) elevado a 1/12 menos 1, equivalente a 0,948879 %. El VAN anual rector del subtotal puro es CLP -20.055.029,94. Si los importes prorrateados se ubican al final de cada mes, el VAN es CLP -21.070.841,39, diferencia de CLP -1.015.811,45. Se informa el contraste porque adelantar egresos modifica su valor presente. No se reemplaza el formato anual docente ni se afirma que el prorrateo sea un calendario efectivo de caja.

Los flujos vigentes se vinculan con las Tablas 18 a 21, H.27 y H.31 a H.36. Las Tablas 15 a 17 y H.1 a H.26 preservan los antecedentes recibidos; sus valores GCP, tasas o inversiones anteriores no constituyen decisiones activas. La reconstrucción conserva su contenido para la comparación solicitada.

El caso base no presenta recuperación simple ni descontada dentro de los cuatro años: sus flujos propios son negativos. El valor de cierre y el capital del ciclo siguen sin cuantificarse. El cierre no adopta cero como valor económico definitivo ni convierte automáticamente el déficit persistente en capital de trabajo recuperable. La conclusión se limita al subtotal modelado; la evaluación integral continúa abierta conforme a los criterios de Sapag.

## H.37. Liquidez y memoria del déficit acumulado

### H.37.1. Aportes mínimos y déficit persistente

Se recorre el saldo mensual con lanzamiento, operación y deuda, cuando corresponde. Si el saldo antes de aporte es negativo, el aporte mínimo es su valor absoluto; si es positivo, el aporte es cero. La caja de cierre después del aporte se mantiene no negativa. La suma de aportes coincide con el déficit acumulado máximo antes de aportes. Se conservan los 49 momentos en aportes_minimos_condicionada_puro.csv y aportes_minimos_condicionada_financiado.csv. El cálculo distingue necesidad de financiación de pérdidas de capital de trabajo del ciclo (Sapag Chain & Sapag Chain, 2008, pp. 267–269).

**Tabla H.37.1**
*Conciliación de la financiación adicional acumulada*

| Escenario | Aporte adicional Año 0 CLP | Aportes adicionales totales CLP | Caja final tras aportes CLP |
|---|---|---|---|
| Sin deuda | 1.200.000 | 26.168.498 | 0 |
| Con deuda simulada | 0 | 27.094.953 | 0 |

*Nota.* El aporte inicial de cero en la alternativa financiada se explica por el préstamo que excede el lanzamiento identificado. No significa ausencia de inversión o de aportes posteriores. Los aportes son una necesidad calculada, no un compromiso confirmado de los socios. El excedente prestado no es utilidad ni habilita remuneraciones por sí solo.

### H.37.2. Cobertura de las cuotas de deuda

**Tabla H.37.2**
*Caja propia frente al servicio de la deuda simulada*

| Año | Caja antes de cuota CLP | Intereses y principal CLP | Cobertura veces |
|---|---|---|---|
| 2027 | -5.880.996 | 1.548.818 | -3,797 |
| 2028 | -6.115.434 | 1.548.818 | -3,948 |
| 2029 | -6.359.250 | 1.548.819 | -4,106 |
| 2030 | -6.612.818 | 0 | No aplica |

*Nota.* La caja propia antes de cuota resta OPEX, asignaciones pagadas e impuesto académico de las comisiones netas. No incluye préstamo, aportes nuevos, IVA ni arriendos de terceros. La razón es un diagnóstico auxiliar; no se afirma que una entidad financiera apruebe el préstamo. La falta de cuota en 2030 no elimina el déficit operativo.

### H.37.3. Sensibilidad aislada de la comisión por cobrar

**Tabla H.37.3**
*Efecto auxiliar de inmovilizar comisión neta por distintos plazos*

| Días ilustrativos | Comisión por cobrar CLP | Efecto en VAN CLP |
|---|---|---|
| 0 | 0 | 0,00 |
| 7 | 5.600 | -2.041,10 |
| 30 | 24.000 | -8.747,57 |

*Nota.* Se utiliza la comisión neta de CLP 24.000 mensuales y un mes de 30 días, con cobros uniformes. Los plazos 0, 7 y 30 días son pruebas, no condiciones de Mercado Pago. El stock auxiliar se aporta en el Año 0 y se recupera íntegro en el Año 4 para aislar su efecto: variación del VAN = menos stock más stock descontado al cierre. No se aplica este ajuste al caso activo ni se identifica como capital completo del ciclo. Faltan pagos anticipados, plazos de proveedores, IVA de compras y devoluciones. El IVA recaudado y los fondos de publicadores se excluyen de caja libre.

## H.38. Indicadores y recuperación de los escenarios delimitados

Se calcula VAN con momento cero sin descuento y cierres anuales al 12 %. La TIR solo se informa como rentabilidad cuando existe un flujo de inversión con un cambio de signo. Una serie de egresos no tiene TIR; una entrada inicial seguida de pagos corresponde a otro patrón y no se presenta como rentabilidad de los socios. La recuperación simple acumula importes nominales y la descontada acumula importes descontados (Sapag Chain & Sapag Chain, 2008, pp. 321–323, 329–330).

**Tabla H.38.1**
*VAN y TIR de la referencia y los quiebres parciales*

| Escenario | Pagos al mes | VAN parcial CLP | TIR anual |
|---|---|---|---|
| Base sin deuda | 16 | -20.055.029,94 | No existe |
| Base con deuda | 16 | -20.055.030,16 | No interpretable como inversión |
| Quiebre sin asignaciones | 391 | 2.367,04 | 12,1225 % |
| Meta CLP 200.000 por persona | 791 | 2.367,04 | 12,1225 % |
| Meta CLP 1.000.000 por persona | 2.391 | 2.367,04 | 12,1225 % |

*Nota.* El quiebre sin asignaciones es el primer entero con VAN no negativo antes de activarse la meta conjunta: se comprueba que con 390 pagos el VAN es negativo y con 391 no lo es. Los otros dos quiebres presuponen asignaciones completas como egreso académico; no reemplazan la decisión de pago condicionado del caso base. Sus flujos se conservan en liquidez_indicadores_y_cierre.json. El costo identificado no se reestima por volumen en estas pruebas, por lo que los resultados excluyen escalamiento, capital completo del ciclo, oportunidad y cierre. El VAN positivo de unos pocos miles de pesos no constituye margen para absorber partidas desconocidas. No se asume costo económico cero del trabajo por carecer de pago.

**Tabla H.38.2**
*Recuperación simple y descontada de las series anuales*

| Escenario | Simple en años | Descontada en años |
|---|---|---|
| Base sin deuda | No se recupera | No se recupera |
| Base con deuda | No aplica al patrón | No aplica al patrón |
| Quiebre sin asignaciones | 2,359 | 3,963 |
| Meta CLP 200.000 por persona | 2,359 | 3,963 |
| Meta CLP 1.000.000 por persona | 2,359 | 3,963 |

*Nota.* Se interpola linealmente entre cierres anuales para expresar fracciones de año. Esa interpolación no identifica una fecha contractual ni sustituye la convención anual del VAN. No se trasladan estas recuperaciones al caso comercial de 16 pagos ni se confunde recuperación nominal con cumplimiento de la tasa de descuento.

## H.39. Horizonte y condiciones para cerrar la evaluación integral

### H.39.1. Método de cierre y límite del cálculo

El caso de referencia conserva cuatro años de operación. El procedimiento requiere inventariar activos y derechos efectivamente atribuibles al proyecto, su uso alternativo, vida remanente y posibles desembolsos de reposición. Después se estima un valor comercial neto de realización con respaldo o, si existe una proyección sostenible posterior, se evalúa un valor de continuidad que no duplique recuperaciones ya incluidas. El libro distingue métodos contable, comercial y económico; el valor contable no acredita por sí solo dinero de venta (Sapag Chain & Sapag Chain, 2008, pp. 277–282, 292–295).

Para que un único cobro terminal neto adicional en el Año 4 neutralice el VAN del subtotal base, se requiere CLP 31.556.977,88. Se obtiene multiplicando el valor absoluto del VAN por (1 + 0,12) elevado a cuatro. Este umbral algebraico no tasa equipos, software o empresa; no demuestra la existencia de comprador ni de flujos posteriores. No se incorpora a las Tablas 18 y 19 como ingreso esperado.

### H.39.2. Datos y decisiones que no se sustituyen por supuestos confirmados

El cierre comercial requiere ratificar distribución de espacios, pagos, ticket y estacionalidad entre las nueve categorías. La referencia agregada no inventa ventas por categoría. Los CLP 1.200.000 de lanzamiento incluyen constitución y trámites por decisión del propietario; el desglose y la ejecución efectiva se documentan sin duplicar la partida.

El desarrollo valorizado se separa en trabajo pasado, compromisos irreversibles y trabajo incremental futuro. Los equipos existentes no generan nueva compra; se precisa su propiedad, aporte y uso alternativo antes de asignar depreciación o valor de cierre. Ausencia de pago no equivale a costo de oportunidad cero.

Antes de integrar se precisan costos y condiciones de proveedores, pasarela, devoluciones, retenciones, liquidaciones y formalización de asignaciones. Se conserva el impuesto académico del 27 % sin afirmar liquidación fiscal real. Con esas entradas se recalculan flujos, capital del ciclo, indicadores y conclusión. La preparación mantiene las reservas de la tesis principal y las secciones de planificación de Erick.

## H.40. Ratificación de decisiones preoperativas

El propietario ratifica que el lanzamiento se prevé en enero de 2027, los CLP 1.200.000 de preparación y lanzamiento incluyen constitución y trámites, y los equipos permanecen personales y compartidos. La inclusión de trámites evita duplicar el desembolso. El uso compartido no acredita transferencia patrimonial ni ingreso de venta final de equipos a la empresa.

La aclaración interpreta los CLP 6.240.000 como valorización del esfuerzo total para desarrollar el producto funcional antes del lanzamiento. No determina cuánto está ejecutado, cuánto falta ni un pago contratado. Se distingue la valoración global de origen del costo incremental pertinente a la fecha de decisión. El caso de caja conserva cero desembolso de desarrollo adicional confirmado; ello no declara cero su costo económico (Sapag Chain & Sapag Chain, 2008, pp. 126, 259–262).

Para observar qué volumen permitiría recuperar también esa valoración, se añade CLP 6.240.000 una sola vez al momento cero de una prueba separada, junto con el lanzamiento de CLP 1.200.000. El total de referencia pasa a CLP 7.440.000, sin sumar los equipos personales. No se incluye depreciación, amortización contable ni escudo tributario por esa valoración sin evidencia de su procedencia. No es una nueva salida de efectivo ni una valoración legal del software.

**Tabla H.40.1**
*Quiebre parcial al exigir recuperar la valoración global de desarrollo*

| Escenario | Pagos mensuales mínimos | VAN con un pago menos CLP | VAN con el mínimo CLP |
|---|---|---|---|
| Sin asignaciones | 548 | -11.552,77 | 28.358,00 |
| Meta CLP 200.000 por persona | 948 | -11.552,77 | 28.358,00 |
| Meta CLP 1.000.000 por persona | 2.548 | -11.552,77 | 28.358,00 |

*Nota.* Ticket constante de CLP 50.000, comisión neta del 3 %, cuatro años y descuento del 12 %. Los gastos de lanzamiento ya incluyen trámites. El caso de 16 pagos, al exigir recuperar además la valoración global, produce VAN de CLP -26.295.029,94. Esta prueba mantiene los costos identificados independientes del volumen y no sustituye la caja de las Tablas 18 y 19 ni estima el costo de oportunidad incremental real. Las partidas aún no valoradas continúan excluidas.
