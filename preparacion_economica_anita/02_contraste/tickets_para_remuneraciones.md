# Cálculo de tickets y remuneraciones

## Criterio de cálculo

El escenario provisional adopta CLP 200.000 mensuales por fundador, equivalentes a CLP 600.000 para tres integrantes. Esta indicación sustituye el criterio anterior de ausencia de pagos iniciales sin monto objetivo. La regla de trabajo propone distribuir el monto completo cuando la caja disponible, después de las obligaciones operativas, alcanza CLP 600.000. Si no se alcanza la meta, no se distribuye en ese período. La remuneración prevista y la efectivamente pagada se registran separadas. La regla financiera no determina por sí sola la existencia o ausencia de obligaciones laborales.

El objetivo adicional solicitado es CLP 1.000.000 mensuales por integrante. Se modela como asignación de referencia antes de definir cargas, retenciones o equivalencia líquida. El costo de contratación completo requiere una definición posterior.

**Tabla 18**
*Costos mensuales parciales utilizados en el cálculo de cobros*

| Componente | Importe mensual CLP |
|---|---|
| FirmaVirtual/API | 50.000 |
| Marketing | 350.000 |
| Contabilidad | 50.000 |
| Dominio | 912,50 |
| Viajes de coordinación | 15.000 |
| AWS, escenario bruto adoptado | 25.670,52 |
| Total parcial sin fundadores | 491.583,02 |
| Meta inicial para tres fundadores | 600.000 |
| Total parcial con meta inicial | 1.091.583,02 |

*Nota.* Elaboración a partir de Base mensual, A20:B25, y del escenario AWS documentado. Se retiran CLP 150.000 de GCP y se incorporan CLP 25.670,52 de AWS. Los créditos temporales no reducen el umbral recurrente. La transcripción original permanece en H.3 y la comparación de remuneraciones de Anita en H.24. Las partidas conservan su condición de supuestos de planificación.

La comisión neta por pago es ticket medio multiplicado por 0,03. El número mínimo de cobros se obtiene redondeando hacia arriba el cociente entre costos parciales más remuneraciones objetivo y comisión neta por pago. El IVA de la comisión se separa del ingreso operativo. El costo de Mercado Pago se supone íntegramente descontado al publicador; cualquier costo residual para espaciGo debe agregarse al modelo cuando se determine.

**Tabla 19**
*Pagos mensuales requeridos según ticket y remuneración objetivo*

| Ticket medio CLP | Comisión neta por pago CLP | Pagos para CLP 200.000 por persona y costos parciales | Pagos para CLP 1.000.000 por persona y costos parciales |
|---|---|---|---|
| 20.000 | 600 | 1.820 | 5.820 |
| 50.000 | 1.500 | 728 | 2.328 |
| 100.000 | 3.000 | 364 | 1.164 |
| 200.000 | 6.000 | 182 | 582 |

*Nota.* Elaboración propia mediante calcular_tickets_remuneraciones.py. Se consideran tres fundadores, comisión neta del 3 % y costos parciales de CLP 491.583,02 por mes. Son cantidades de pagos procesados y no necesariamente reservas ni contratos únicos. El ticket representa un promedio ponderado por cobros de las distintas modalidades y categorías. Los umbrales no constituyen una previsión de ventas ni un punto de equilibrio definitivo.

Con ticket medio de CLP 50.000, cubrir únicamente la meta inicial de CLP 600.000 exige 400 pagos y CLP 20.000.000 transados al mes. Al incorporar los costos parciales, se requieren 728 pagos y CLP 36.400.000 transados, que producen CLP 1.092.000 de comisión neta. Después de CLP 491.583,02 de costos parciales y CLP 600.000 para fundadores, el remanente es CLP 416,98 antes de partidas excluidas. Por ello, ese umbral no ofrece todavía un margen de seguridad.

El objetivo de CLP 1.000.000 por fundador exige, con el mismo ticket, 2.328 pagos mensuales y CLP 116.400.000 transados. La comisión neta asciende a CLP 3.492.000 frente a CLP 3.491.583,02 de costos parciales y asignaciones objetivo. El volumen debe contrastarse con demanda, capacidad e infraestructura; el presupuesto AWS de referencia no acredita capacidad para ese nivel de actividad.

La referencia inicial de 16 pagos mensuales genera CLP 24.000 de comisión neta. La brecha respecto de la meta inicial con costos parciales es de 712 pagos y CLP 1.067.583,02 mensuales. Si se conserva la hipótesis de dos pagos por espacio y mes, 728 pagos equivalen a 364 espacios activos. Es una equivalencia aritmética y no una demanda demostrada.

El umbral excluye costos todavía no conciliados de oficina, mantenimiento, obligaciones legales y tributarias, cargas de contratación, inversión, deuda y capital de trabajo. También requiere ajustar cancelaciones, devoluciones, costos variables propios y escalamiento de infraestructura. Se mantiene la fórmula de Anita y se actualizan tarifa, remuneración y componente cloud; los resultados históricos calculados al 14 % permanecen identificados como antecedentes en H.24.

## Reproducción

Ejecutar `python3 preparacion_economica_anita/scripts/calcular_tickets_remuneraciones.py --sueldo-objetivo 200000` y repetir con `--sueldo-objetivo 1000000`. La opción `--guardar` actualiza umbrales_remuneraciones.json y se utiliza únicamente para la meta provisional elegida.
