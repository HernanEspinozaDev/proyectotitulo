# Hallazgos de conciliación económica

| Hallazgo | Fuente | Corrección propuesta |
|---|---|---|
| Dos bases de ingreso | Informe y FlujoNeto parten de CLP 35.000.000 anuales. Modelo reconstruido!C8 parte de CLP 1.344.000. | Elegir un escenario rector y conservar la alternativa identificada. |
| Comisión del 10 % frente a 14 % | Informe 5.1 y Supuestos modelo!B7. | Fijar el parámetro de evaluación sin atribuir una tarifa contratada. |
| Remuneración anual de 14,4 frente a 7,2 millones | Supuestos modelo!B11 frente a Conciliacion costos!B16 y Perspectivas fundadores!C7. | Adoptar una política y contabilizar el trabajo una sola vez. |
| Resultados pendientes del modelo reconstruido | Modelo reconstruido!C9:F38. | Completar pasarela, oficina, respaldo, mantención y demás parámetros requeridos. |
| Error de signo en el flujo duplicado | FlujoNeto!C15 muestra EBT positivo de 956.400. La copia C37 contiene −956.400. | Mantener una tabla coherente con EBIT e intereses. |
| Año 0 distinto entre las dos tablas | FlujoNeto!B17 contiene −1.350.000 y B39 contiene cero. | Conciliar gastos preoperativos e inversión y evitar doble conteo. |
| OPEX sin conciliación | FlujoNeto!C10 usa 18.000.000; Costos y gastos generales!C26 totaliza 16.991.388. | Reconstruir componentes y tratamiento de depreciación y salarios. |
| Pasarela ligada a otro volumen | Costo anual de 10.800.000 frente a 192 reservas del escenario reconstruido. | Recalcular desde GMV y tarifa aplicable. |
| Trabajo valorizado dentro del desembolso | Desarrollo de 6.240.000 en la inversión y el flujo. | Separar costo de oportunidad y flujo de caja. |
| Saldo de amortización distinto entre imagen y tabla | La imagen 11 del informe presenta saldo final negativo; cuadro amortizacion!B17 conserva 1 CLP. | Reconstruir intereses, cuota, capital y redondeo hasta saldo cero. |
| Crédito e impuestos sin respaldo específico | Tasa 12 %, deuda 3.720.000 y tasa tributaria 27 % en el informe. | Modelar parámetros y confirmar oferta, régimen y método antes de cerrar. |
| Imagen 2 mal rotulada | Imagen Google Play frente a título de conversión cloud. | Retirar del costo web o tratar como escenario móvil separado. |
| Respaldo potencialmente duplicado | Servicio respaldo y Revision respaldo. | Actualizar protección de RDS/S3 y evitar otra partida sin alcance propio. |
| Alcance solo comercial | Informe y escenarios A/B. | Mantener nueve categorías y delimitar un mix inicial de evaluación. |

## Recálculo del flujo original

Para el vector [−6.420.000, −1.278.818, 445.097, 2.104.062, 5.378.456], se obtiene VAN de −1.960.342,32 al 10 %, VAN de −2.291.237,39 al 12 % y TIR de 0,85115 %. Las cifras coinciden con el redondeo del informe y dependen de ese flujo. El acumulado nominal final es 228.797.

Al retirar únicamente los 6.240.000 de desarrollo valorizado del desembolso inicial, manteniendo los demás flujos, el acumulado sigue negativo al terminar el Año 2 (−1.013.721) y pasa a positivo en el Año 3 (1.090.341). Se debe rectificar la afirmación del informe que sitúa esa recuperación en el Año 2.

## Criterio de evidencia

Se conservan los datos de Anita con identificación de fuente. Los supuestos pueden adoptarse como parámetros del escenario de planificación. El recálculo acredita consistencia aritmética bajo esos parámetros. La confirmación de una tarifa, contratación, consumo o régimen tributario requiere su respaldo específico.
