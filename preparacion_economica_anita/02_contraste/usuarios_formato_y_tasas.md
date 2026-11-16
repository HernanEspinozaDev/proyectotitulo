# Usuarios activos, formato del flujo y significado de las tasas

Fecha de corte: 16 de noviembre de 2026. Este análisis complementa el cálculo de remuneraciones sin modificar la tesis publicada ni los datos recibidos de Anita.

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

## Reserva y margen operativo

Si se desea evaluar 25 % adicional de cobertura sobre costos, se utiliza ingreso objetivo = costo × 1,25. Si se desea un margen del 25 % sobre ingresos, se utiliza ingreso objetivo = costo / 0,75. Son objetivos diferentes y ninguno se incorpora como decisión ratificada.

Con ticket de CLP 50.000, comisión neta de CLP 1.500 y los costos parciales actuales, la cobertura adicional del 25 % demanda 910 pagos para la meta de CLP 200.000 por fundador y 2.910 para CLP 1.000.000. Un margen del 25 % sobre ingresos demanda 971 y 3.104 pagos respectivamente. Todos excluyen los costos aún pendientes y dependen de demanda y capacidad por acreditar.

## Fuentes

- Extracción íntegra del informe de Anita: 01_extraccion/informe/informe_completo.md, secciones 5.1 a 5.3 y Figura 17.
- Libro recibido: FlujoNeto A29:F45; Auditoria y decisiones, fila 5; Perspectivas fundadores; TasaInteresCredito.
- Antecedente pedagógico local: tesis_final/context/03_insumos_anita_erick_finanzas/INV-009_evaluacion_economica.md.
- NYU Stern, Aswath Damodaran, Approaches to Valuation: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/approach.html. Distingue tasa correspondiente a flujos de socios y a flujos de empresa.
- SII, tasas de Primera Categoría: https://www.sii.cl/preguntas_frecuentes/declaracion_renta/001_140_4708.htm. Requiere diferenciar ejercicio y régimen.
