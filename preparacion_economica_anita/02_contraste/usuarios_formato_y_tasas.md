# Usuarios activos, formato del flujo y significado de las tasas

Fecha de corte: 16 de noviembre de 2026.

**Referencia principal vigente:** Sapag Chain y Sapag Chain (2008), quinta edición; contraste documentado en sapag2008_matriz_brechas.md. Las referencias externas anteriores se conservan como historial.

**Criterio vigente:** descuento nominal anual del 12 % confirmado por Anita y ratificado por el propietario; impuesto académico fijo del 27 %. Las entradas posteriores documentan la evolución y quedan subordinadas a esta decisión final. El 10 % y el 25 % no son tasas base. Este análisis complementa el cálculo de remuneraciones sin modificar la tesis publicada ni los datos recibidos de Anita.

## Usuarios y cobros

Un publicador puede administrar uno o varios espacios. Cada espacio puede generar uno o varios pagos; una reserva puede generar cuotas mensuales. La persona que reserva también puede pagar varias veces en un mes. Por ello, pagos, reservas, contratos, espacios y usuarios únicos son magnitudes distintas. Los usuarios registrados que no operan no se estiman a partir de transacciones sin una tasa de activación respaldada.

El cálculo aproxima publicadores activos como pagos mensuales divididos por promedio de pagos por publicador, redondeado hacia arriba. Se suman todos los pagos de todos los espacios de cada publicador. Para usuarios que reservan se usa su propio promedio de pagos mensuales. Las estimaciones siguientes mantienen ticket medio ponderado de CLP 50.000 y las metas parciales de 728 y 2.328 pagos, respectivamente.

| Promedio de pagos por publicador y mes | Publicadores para 728 pagos | Publicadores para 2.328 pagos |
|---|---|---|
| 1 | 728 | 2.328 |
| 4 | 182 | 582 |
| 10 | 73 | 233 |
| 20 | 37 | 117 |

Los promedios son escenarios ilustrativos, no frecuencias observadas. Un promedio de cuatro pagos puede corresponder a un espacio con cuatro pagos, dos espacios con dos pagos cada uno o una mezcla heterogénea. Las cifras no suponen que todos los publicadores tengan el mismo comportamiento.

Si cada persona que reserva genera dos pagos por mes, se requieren aproximadamente 364 o 1.164 arrendatarios activos. Combinados con cuatro pagos por publicador, el ejemplo resulta en 182 publicadores y 364 arrendatarios para la meta inicial, o 582 y 1.164 para el objetivo adicional. Sumar ambos da 546 y 1.746 participaciones por rol; solo serían usuarios únicos si las personas de ambos grupos no se superponen. No se incluyen usuarios inactivos, cancelaciones ni altas necesarias para compensar deserción.

La mezcla por categoría y modalidad determina tanto frecuencia como ticket. No se conserva automáticamente el ticket de CLP 50.000 si aumenta el peso de arriendos mensuales. Se requiere una matriz de publicadores, espacios, pagos efectivos y ticket por segmento para validar los promedios. Los ejemplos son equivalencias aritméticas y no demanda comprobada.

## Formato del flujo exigido

Por instrucción del propietario, se conserva como formato rector el flujo que entrega Anita y que solicita la profesora: columnas Año 0 a Año 4 y secuencia de ingresos, costos variables, OPEX, administración/marketing, depreciación, EBIT, intereses, EBT, impuesto, utilidad neta, reincorporación de depreciación, préstamo recibido, inversiones, capital de trabajo, amortización y flujo neto de caja. No se sustituye por una tabla de tickets ni por una tabla mensual abreviada.

Las Tablas 18 y 19 son auxiliares del flujo. La versión actualizada debe conservar la estructura original y corregir sus valores y notas: comisión del 3 %, cloud AWS, remuneraciones previstas y pagadas, pasarela a cargo del publicador y financiamiento simulado. Debe separar el ingreso propio de los fondos de terceros y el trabajo valorizado del desembolso, sin alterar arbitrariamente la secuencia requerida. La fuente es FlujoNeto A29:F45 y la Figura 17 del informe recibido.

Se mantienen VAN, TIR y recuperación después del flujo completo. Los indicadores se recalculan cuando se cierre una serie única; no se trasladan los resultados históricos al escenario AWS. El flujo con préstamo y amortización exige distinguir la evaluación de los socios de la evaluación del proyecto antes de elegir la tasa de descuento.

## Qué significa cada porcentaje encontrado

- Comisión vigente: 3 % más IVA por pago, según decisión del propietario. El IVA no forma parte del ingreso neto.
- Tasa de descuento del informe de Anita, sección 5.3: 10 % y 12 % anuales, expresamente referenciales. No se encuentra una derivación del costo de capital que permita calificarlas como tasas verificadas o seguras.
- Interés del préstamo: 12 % anual en una simulación. No equivale automáticamente a la tasa de descuento.
- TIR histórica: aproximadamente 0,85 % sobre el vector original. Es un resultado del flujo y no un porcentaje elegido de antemano.
- 25 % en Auditoria y decisiones, fila 5: comisión mencionada en una conversación con un proveedor para la primera reserva; la propia hoja descarta fijarla como tarifa final.
- 25 % en el antecedente INV-009: margen operativo objetivo de un ejercicio pedagógico anterior, identificado como superado. No acredita rentabilidad del escenario actual.
- 25 % en TasaInteresCredito: cofinanciamiento supuesto de una alternativa de fondos concursables, no una tasa de descuento ni un margen de seguridad.
- Impuesto del 27 % en el informe: supuesto de origen. El régimen y el año fiscal deben verificarse antes de cerrar el flujo; no se sustituye por 25 % sin fundamento.

No existe un porcentaje que garantice rentabilidad. La tasa del VAN debe justificarse por el tipo de flujo, riesgo, moneda, horizonte y estructura de financiamiento; se propone conservar 10 % y 12 % como comparación histórica y someter el escenario nuevo a sensibilidad, sin declararlos costo de capital validado.

## Comparación previa de reserva y margen operativo

Si se desea evaluar 25 % adicional de cobertura sobre costos, se utiliza ingreso objetivo = costo × 1,25. Si se desea un margen del 25 % sobre ingresos, se utiliza ingreso objetivo = costo / 0,75. Son objetivos diferentes y ninguno se incorpora como decisión ratificada.

Con ticket de CLP 50.000, comisión neta de CLP 1.500 y los costos parciales actuales, la cobertura adicional del 25 % demanda 910 pagos para la meta de CLP 200.000 por fundador y 2.910 para CLP 1.000.000. Un margen del 25 % sobre ingresos demanda 971 y 3.104 pagos respectivamente. Todos excluyen los costos aún pendientes y dependen de demanda y capacidad por acreditar.

## Fuentes

- Extracción íntegra del informe de Anita: 01_extraccion/informe/informe_completo.md, secciones 5.1 a 5.3 y Figura 17.
- Libro recibido: FlujoNeto A29:F45; Auditoria y decisiones, fila 5; Perspectivas fundadores; TasaInteresCredito.
- Antecedente pedagógico local: tesis_final/context/03_insumos_anita_erick_finanzas/INV-009_evaluacion_economica.md.
- NYU Stern, Aswath Damodaran, Approaches to Valuation: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/approach.html. Distingue tasa correspondiente a flujos de socios y a flujos de empresa.
- SII, tasas de Primera Categoría: https://www.sii.cl/preguntas_frecuentes/declaracion_renta/001_140_4708.htm. Requiere diferenciar ejercicio y régimen.


## Aclaración del criterio docente del 25 %

El propietario aclara que el 25 % corresponde al criterio de riesgo indicado por su profesor de Planificación de Proyectos. Se adopta para la evaluación académica como tasa de descuento anual total del 25 %, sustituyendo el uso principal de las tasas referenciales de 10 % y 12 %. La fuente de la exigencia es la indicación docente comunicada por el propietario; no se atribuye a una norma financiera general ni a la rúbrica documental sin evidencia escrita.

Esta tasa no representa una probabilidad de fracaso del 25 %, no se resta como gasto del flujo y no incrementa automáticamente costos o tickets en 25 %. Las comparaciones anteriores sobre cobertura y margen son conceptos distintos y no se aplican como consecuencia de esta aclaración. VAN utiliza 0,25 como tasa anual; TIR se calcula a partir del flujo y luego se compara con esa exigencia. La TIR no se fija en 25 % por decisión.

Como comprobación exclusivamente histórica, el vector original de Anita, [−6.420.000, −1.278.818, 445.097, 2.104.062, 5.378.456], produce VAN al 25 % de CLP -3.877.897,00. Su TIR conserva aproximadamente 0,85 %. Este resultado no se atribuye al flujo nuevo de AWS y comisión del 3 %, que requiere cierre propio.

El flujo original sí contiene la fila de impuesto a la renta del 27 %. Ese porcentaje corresponde a un supuesto del modelo recibido y no se extiende automáticamente a toda empresa chilena. Según la tabla del SII, Pro Pyme General presenta una tasa de 12,5 % para el año comercial 2026 y también para 2027, bajo las condiciones del régimen. La ley 21.850, artículo sexto transitorio, establece para el régimen general una secuencia de 27 % en 2026, 25,5 % en 2027, 24 % en 2028 y 23 % desde 2029, preservando las disposiciones señaladas para Pro Pyme. El cierre del flujo requiere régimen y año comercial por columna, así como la base imponible y pérdidas que efectivamente correspondan.

Fuentes tributarias consultadas el 16 de noviembre de 2026: tabla SII https://www.sii.cl/preguntas_frecuentes/declaracion_renta/001_140_4708.htm y ley 21.850, artículo sexto transitorio, BCN https://www.bcn.cl/leychile/Navegar?idNorma=1229250&idParte=10613949&idVersion=2026-11-01.

## Selección del escenario tributario y calendario

El propietario confirma que la empresa aún no se constituye y elige modelar Pro Pyme General, con Año 1 de operación en 2027. Se registra como régimen proyectado, sin afirmar acogimiento formal. El ingreso propio modelado es la comisión de intermediación; los arriendos corresponden a los publicadores. El Anexo H.28 vincula este supuesto con las tasas proyectadas de 12,5 % en 2027, 15 % en 2028 y 23 % desde 2029, según normativa consultada. El calendario estructurado y las fuentes se conservan en parametros_tributarios.json. El estado tributario efectivo y la conciliación de la base siguen sujetos a formalización y cierre.

## Criterio vigente del impuesto académico

La última instrucción del propietario conserva 27 % fijo como impuesto del ejercicio, tal como lo presenta Anita y por el criterio de revisión de la profesora. Sustituye el uso de tasas legales por año en el cálculo académico. Se mantiene el régimen Pro Pyme General como proyección organizativa, con empresa aún no constituida, sin atribuir a ese régimen la tasa legal del 27 %. Las tasas legales consultadas antes quedan solo como antecedente de contraste. Se mantienen Año 1 en 2027 y descuento académico del 25 %; las tasas de descuento originales de Anita son 10 % y 12 % referenciales. El formato del flujo permanece intacto.

## Diferencia entre descuento referencial y exigencia académica

La revisión del informe completo encuentra que la sección 5.3 denomina referencial al COK del 10 % al 12 % anual. No presenta una derivación cuantitativa de esas tasas mediante costo de oportunidad, prima de riesgo, comparables o un modelo de costo de capital. La explicación de la simulación de préstamo al 12 % justifica otra variable y no basta por sí sola para justificar el descuento de los flujos. En las hojas extraídas tampoco se identifica una derivación adicional del COK. Se trata de ausencia de respaldo en los insumos revisados, no de prueba de que la tasa sea necesariamente incorrecta.

El 25 % comunicado por el profesor constituye una exigencia metodológica para el ejercicio. Puede sustentarse como criterio docente adoptado y acompañarse de sensibilidad al 10 % y 12 %, sin presentarse como estimación de mercado validada. Una justificación económica propia requeriría identificar tipo de flujo, moneda, tasa nominal o real, costo de oportunidad y evidencia del riesgo. No se inventa una suma de primas para obtener exactamente 25 %.

Por ejemplo, CLP 100.000 recibidos dentro de cuatro años tienen valor presente de CLP 68.301,35 al 10 %, frente a CLP 40.960 al 25 %. Los cobros proyectados permanecen iguales; cambia su valor para la evaluación actual. La TIR del mismo flujo no depende de la tasa elegida para el VAN. En el vector histórico de Anita, el VAN cambia de CLP −1.960.342,32 al 10 % a CLP −3.877.897 al 25 %, mientras la TIR permanece en aproximadamente 0,85 %.

La base metodológica es el descuento de flujos con una tasa acorde a su riesgo y al destinatario del flujo: NYU Stern, Aswath Damodaran, https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/approach.html. Esta fuente respalda el método; no prescribe 25 % para espaciGo.

## Ratificación final del 12 %

El propietario confirma con Anita que la tasa utilizada es 12 % y solicita adoptarla y justificarla. Se sustituye el uso principal del 25 % y se retira el 10 % como alternativa base. La justificación metodológica y sus límites se documentan en justificacion_descuento12.md y H.29; la elección no se presenta como cálculo empírico de CAPM o WACC ni como equivalencia automática con el interés del préstamo. El mayor crecimiento esperado se refleja en el flujo y el menor descuento solo cambia su valoración presente.

## Umbrales vigentes tras la conciliación de costos

El corte de ejecución incorpora útiles y dirección tributaria anual ratificada. A ticket de CLP 50.000, las metas vigentes son 743 y 2.343 pagos mensuales para las dos asignaciones por fundador. Las comparaciones previas de usuarios a partir de 728 y 2.328 pagos se conservan como antecedente del presupuesto anterior y no se presentan como cantidades actuales. La fórmula de usuarios sigue siendo pagos divididos por frecuencia por persona, redondeando hacia arriba.
