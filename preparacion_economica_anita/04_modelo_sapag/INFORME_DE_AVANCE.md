# Primer corte de ejecución del plan Sapag

## Correcciones aplicadas

Se registra la respuesta del propietario: equipos existentes, sin compra inicial, y CLP 1.200.000 de lanzamiento como presupuesto provisional. Se construyen 48 meses de referencia comercial y caja y se conserva el reparto de comisión, IVA y fondos de terceros. No se inventa distribución entre las nueve categorías.

Se consolida el presupuesto identificado en CLP 514.083,02 mensuales, incorporando CLP 10.000 de útiles de oficina y CLP 12.500 de dirección tributaria. La periodicidad anual de esta última se ratifica por el propietario. El marketing operativo queda separado del presupuesto de lanzamiento. Los importes permanecen provisionales. Los umbrales por ticket de CLP 50.000 pasan de 728 a 743 pagos para CLP 200.000 por fundador y de 2.328 a 2.343 para CLP 1.000.000.

La deuda simulada se cierra en saldo cero mediante ajuste de CLP 1 en la última cuota. Se demuestra que la compensación de la pérdida histórica, bajo el criterio explicado por Anita y pérdidas iniciales cero, cambia el impuesto del Año 2 de CLP 332.805 a CLP 74.577. Los originales permanecen intactos.

## Proyección calculada y límites

La referencia conserva 16 pagos mensuales, ticket de CLP 50.000, comisión neta de CLP 24.000 por mes y sin crecimiento de volumen o ticket. Se aplica 4 % anual a presupuestos CLP del insumo y costo AWS bruto constante. Los créditos no se aplican sin validar su disponibilidad en los años de operación. La caja condicionada a excedente no activa pagos a fundadores en esta referencia.

Los flujos puro y financiado de partidas identificadas se presentan completos en el cuerpo conservando la estructura de Anita. No se describen como flujos definitivos: capital del ciclo, costos sin valoración, costo de oportunidad, reinversiones y valor de cierre siguen abiertos. El flujo puro parcial arroja VAN de CLP -20.055.029,94 al 12 %. No tiene TIR por presentar solo salidas. El financiado inicia con una entrada de préstamo y luego salidas, por lo que no se interpreta una tasa de financiación como rendimiento de inversión.

La necesidad acumulada de financiación parcial es CLP 26.168.498,16, incluyendo el lanzamiento presupuestado. No se convierte en capital de trabajo adicional ni se suma de nuevo a la inversión inicial. La referencia actual no cubre sus costos identificados; esto no acredita una previsión de demanda ni una conclusión definitiva sobre un producto con otro volumen o estructura de costos.

## Entregables y reproducción

- parametros_ejecucion.json registra decisiones y exclusiones.
- matriz_categorias.json y CSV conserva el catálogo y los campos por completar.
- costos_conciliados.json registra las ocho partidas y su procedencia.
- proyeccion_mensual_2027_2030.csv y resumen_anual_2027_2030.csv contienen las memorias intermedias.
- resultados_proyeccion.json contiene seis perfiles: pago condicionado, meta inicial presupuestada y objetivo de un millón; cada uno puro y financiado.
- deuda_corregida y conciliacion_perdidas_historicas contienen las comprobaciones auxiliares.

Ejecutar scripts/ejecutar_modelo_sapag.py, recalcular los umbrales con scripts/calcular_tickets_remuneraciones.py y ejecutar scripts/verificar_modelo_sapag.py. scripts/actualizar_documento_ejecucion.py integra el corte en el borrador y anexos, y scripts/build_preview.py construye Word con DocSkill. La exportación y revisión visual del PDF se realiza con el flujo documental existente.

## Qué sigue abierto

Mezcla por categoría, adquisición y baja de oferta, ticket por modalidad, costos residuales y servicios pendientes, forma de remuneración, ciclo de liquidación e IVA de compras, valor de uso alternativo del trabajo y equipos, reposiciones y cierre. SP04–SP12 tienen avances calculados y no se marcan completos mientras dependan de esos datos. La tesis principal conserva sus reservas de integración.

## Segundo corte de coherencia y sensibilidad

Se corrige la persistencia de 2.335 pagos en el generador: la cifra activa de la meta de un millón es 2.343 en el Año 1. Se explicitan los antecedentes frente al escenario vigente, la fecha de descuento y el prorrateo de costos. El generador conserva los parámetros de reajuste e inversión, sin asumir un porcentaje distinto del modelo.

Se agregan once pruebas univariables, umbrales por año, dos cruces de VAN parcial y contraste temporal mensual/anual. H.36 y la sección 14.5 documentan métodos y límites. SP12 avanza, sin declararse completo mientras falten costos, demanda validada y rezagos.
