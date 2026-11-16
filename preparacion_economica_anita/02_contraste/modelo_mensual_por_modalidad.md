# Modelo mensual de ingresos por modalidades

Se conserva como escenario provisional la referencia de ocho espacios activos, dieciséis cobros al mes y ticket medio comisionable de CLP 50.000. Esos valores equivalen a CLP 800.000 transados por mes y CLP 24.000 de comisión neta.

## Cálculo del promedio mensual

Para cada modalidad se multiplica el número de cobros mensuales por su ticket medio comisionable. La suma constituye el GMV del mes. El ticket global es GMV dividido por número de cobros. La comisión del mes es GMV multiplicado por 3 %. La comisión se aplica en cada pago procesado: sobre cada cuota mensual o sobre el pago anual completo cuando el contrato se paga una sola vez. Los contratos y los cobros se cuentan por separado.

| Modalidad | Datos para construir el ticket | Dato de frecuencia |
|---|---|---|
| Hora | Horas promedio por reserva × precio por hora. | Reservas cobradas por mes. |
| Día | Días promedio por reserva × precio por día. | Reservas cobradas por mes. |
| Mes | Importe del período que se cobra. | Pagos efectivamente procesados en el mes. |

Un mismo espacio puede admitir varias modalidades. El inventario se cuenta por espacios únicos y las transacciones se clasifican una sola vez, evitando duplicar renta o ingresos.

## Ejemplo que mantiene la referencia original

El ejemplo siguiente es ilustrativo. Su distribución y precios requieren ratificación.

| Modalidad | Cobros en el mes | Ticket medio comisionable CLP | Total mensual CLP |
|---|---|---|---|
| Hora | 10 | 20.000 | 200.000 |
| Día | 4 | 50.000 | 200.000 |
| Mes | 2 | 200.000 | 400.000 |
| Total | 16 | 50.000 ponderado | 800.000 |

El promedio ponderado resulta de 800.000 dividido por 16. La comisión de espaciGo es CLP 24.000, el IVA sobre la comisión es CLP 4.560 y el cobro total de comisión es CLP 28.560. Los datos por modalidad permiten modificar el mix sin cambiar la tasa del 3 %.

## Relación con los costos

El presupuesto AWS preparado utiliza CLP 25.670,52 mensuales antes de créditos. Para cubrir exclusivamente esa partida con una comisión neta del 3 %, el total transado debe alcanzar CLP 855.684 mensuales. El cálculo excluye personal, comercialización y los demás costos operativos. La cobertura por créditos tiene su propio calendario.

La referencia de ocho espacios puede caracterizar una etapa inicial de validación. La sostenibilidad del servicio depende del GMV mensual y del conjunto de costos. El resultado del escenario debe determinar la necesidad de caja, sin ajustar la demanda solamente para conseguir rentabilidad.

## Reparto confirmado por pago

Quien publica asume la comisión de espaciGo más su IVA y el cargo de Mercado Pago mediante deducción del importe del arriendo. Para un pago de CLP 100.000, espaciGo percibe CLP 3.000 de comisión neta y se separan CLP 570 de IVA. El publicador recibe CLP 96.430 menos el cargo efectivo de Mercado Pago. La tarifa de la pasarela permanece pendiente; no se presume un porcentaje.

En el escenario provisional de CLP 800.000 mensuales, el saldo agregado de los publicadores es CLP 771.440 menos los cargos de Mercado Pago. Los CLP 24.000 de comisión neta pertenecen a espaciGo y los CLP 4.560 de IVA se registran por separado. La deducción de la pasarela al publicador se concilia con su liquidación para evitar duplicarla como gasto financiado por espaciGo.
