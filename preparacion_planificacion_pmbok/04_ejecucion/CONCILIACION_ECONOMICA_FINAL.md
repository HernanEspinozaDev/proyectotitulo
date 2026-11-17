# Conciliación económica temporal P07

## Criterio vigente

La valoración global conserva 960 horas nominales a CLP 6.500 por hora, equivalentes a CLP 6.240.000. La capacidad nominal del bloque académico comprendido entre el 11 de agosto y el 30 de noviembre de 2026 es de 960 horas (320 por integrante; veinte horas semanales durante dieciséis semanas). El cronograma asigna 632 horas a ese bloque, 36 horas a la defensa y 40 horas a la transición preoperativa. El total asignado asciende a 708 horas y su valoración es CLP 4.602.000.

La reserva presupuestaria es de 252 horas, equivalente a CLP 1.638.000. La capacidad base libre es de 328 horas. La diferencia de 76 horas se explica porque la reserva se calcula contra las 708 horas asignadas e incluye 76 horas posteriores a la entrega (36 de defensa y 40 de transición). La transición se programa entre el 10 y el 31 de diciembre de 2026. La operación comienza el 1 de enero de 2027.

Las horas corresponden a una estimación de planificación del modelo vigente; no hay horas reales acreditadas. En consecuencia, la valorización es presupuestaria: no constituye remuneraciones, contratos ni egreso de caja. Las cifras de flujo e indicadores financieros permanecen sin cambios.

## Archivos conciliados

- `tesis_final/appendices/h-evaluacion-economica-detallada.md`: reemplazo de la ventana antigua en H.5.
- `preparacion_economica_anita/scripts/preparar_redaccion_tesis.py`: H.5 se genera desde la conciliación incluida en el modelo de cronograma; también actualiza la redacción temporal del capítulo XIV de preparación.
- `preparacion_economica_anita/scripts/actualizar_escenario_adoptado.py`: actualización de la síntesis temporal y del bloque H.40 generado.
- `preparacion_economica_anita/03_propuesta/`, `05_propuesta_cierre/`, `06_escenario_adoptado/` y `07_texto_para_tesis/`: sincronización de los textos económicos activos de preparación y las salidas del generador.
- `preparacion_planificacion_pmbok/04_ejecucion/calculo_cronograma.json`: incorporación del objeto `conciliacion_economica` con valores, fechas, tarifa y nota metodológica.
- `preparacion_planificacion_pmbok/03_plan/cronologia_rectora.json`: el dato de 360 horas queda identificado como antecedente sustituido y remite al cálculo vigente.

## Verificaciones

- Las sumas por etapa del cronograma concilian con 632 + 36 + 40 = 708 horas.
- Las capacidades y reservas concilian: 960 − 632 = 328 horas libres en el bloque base; 960 − 708 = 252 horas de reserva presupuestaria; 328 − 252 = 76 horas de diferencia.
- Los valores concilian: 708 × CLP 6.500 = CLP 4.602.000; 252 × CLP 6.500 = CLP 1.638.000.
- No quedan referencias activas a la ventana de seis semanas/360 horas en H.5 ni en los textos económicos vigentes de preparación. Las referencias conservadas en antecedentes históricos no son el modelo vigente.
- Los 27 rótulos de tablas del Capítulo XIV y Anexo H permanecen intactos. No se editaron tablas, flujos, indicadores ni los capítulos XIV de la tesis.
- Los dos generadores Python afectados compilan con `py_compile`. No se ejecutó una compilación completa de la tesis.

La conciliación también actualiza `06_escenario_adoptado/parametros.json`: reemplaza los campos activos de 360 h y CLP 2.340.000 por capacidad base 960 h y su valoración, detalla las asignaciones por etapa y fija la fecha 2027-01-01. En los parámetros de la propuesta histórica, la cifra anterior se identifica como antecedente sustituido. No se altera ningún parámetro de ingreso, gasto operativo, flujo o tasa.
