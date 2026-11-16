# Propuesta para cerrar las entradas de la evaluación económica

Fecha de consulta: 16 de noviembre de 2026. Esta propuesta distingue decisiones vigentes, presupuestos por adoptar y evidencia pendiente. No sustituye el escenario activo ni presenta datos estimados como observados. La tesis principal permanece sin modificaciones.

## 1. Demanda y validación comercial

Se propone mantener 8 espacios activos promedio, 2 pagos mensuales por espacio y ticket ponderado de CLP 50.000 como referencia agregada de lanzamiento. Produce 16 pagos, CLP 800.000 transados y CLP 24.000 de comisión neta al mes. No se asignan ventas obligatorias a las nueve categorías ni se aumenta la demanda para obtener VAN positivo. Los escenarios conservador y optimista de Anita se mantienen como sensibilidad, no como probabilidades.

Se recomienda completar un piloto de validación con objetivos exploratorios de 10 entrevistas a publicadores y 20 a personas que arriendan, con diversidad de categorías y modalidades. Esas cuotas propuestas no constituyen una muestra estadísticamente representativa. Antes del lanzamiento se documentan las ocho fichas de oferta previstas: categoría, modalidad, precio, disponibilidad, número de espacios por publicador y voluntad de publicar. Una entrevista o una carta de intención no equivale a una reserva pagada.

Durante los primeros tres meses desde enero de 2027 se registran consultas, espacios realmente activos, pagos completados, devoluciones, GMV, ticket ponderado y recurrencia por persona. La demanda observada sustituye los supuestos solo cuando existe evidencia. Las nueve filas de plantilla_validacion_oferta.csv sirven para clasificar el catálogo; no son nueve espacios ni ventas obtenidas.

El INE informa actividad de alojamiento turístico y estacionalidad, útil para contextualizar solo el segmento de alojamiento de Inmuebles. No mide la captación de espaciGo ni valida oficina, bodega, stand u otras categorías. Su boletín de septiembre de 2026 no justifica por sí solo los 16 pagos del caso base. Fuente oficial: [INE EMAT septiembre 2026](https://www.ine.gob.cl/sala-de-prensa/prensa/general/noticia/2026/11/02/pernoctaciones-en-establecimientos-de-alojamiento-tur%C3%ADstico-disminuyeron-1-9-interanualmente-en-septiembre-de-2026).

El presupuesto de marketing de CLP 350.000 al mes se conserva por decisión previa. Dividido por los 16 pagos de referencia equivale a CLP 21.875 por pago, frente a CLP 1.500 de comisión neta unitaria. Es una comparación del presupuesto, no CAC medido ni un costo por cliente único. Se revisan conversión y recurrencia; no se presupone que la publicidad genere automáticamente el volumen rentable.

## 2. Costos y calendario propuesto

Se propone distinguir tarifa pública, presupuesto y costo contratado. Solo este último requiere evidencia contractual. No hace falta llamar definitivo a un presupuesto para utilizarlo en una simulación académica.

NIC Chile publica CLP 9.990 por un año de inscripción o renovación .cl, exento de IVA, consultado en la fecha de corte. Se propone ese valor para registro directo, sustituyendo CLP 10.950 del insumo; si interviene un revendedor o servicio adicional se concilia su cobro. No se garantiza que la tarifa permanezca igual en 2027. Fuente: [NIC Chile tarifas](https://www.nic.cl/dominios/tarifas.html).

Con el único ajuste del dominio, el subtotal identificado propuesto es CLP 514.003,02 mensuales prorrateados y CLP 6.168.036,24 anuales, sin asignaciones. Los demás importes mantienen su condición presupuestaria. El script calcular_propuesta.py calcula la comparación sin sobrescribir el escenario vigente.

Se propone pagar dominio y dirección tributaria una vez al año en enero, y distribuir los demás presupuestos mensualmente. El mes de enero registra CLP 660.660,52 de egresos identificados; los demás meses, CLP 500.670,52. Es un calendario de simulación, no fechas de facturas confirmadas. La dirección se mantiene en CLP 150.000 por año. Los CLP 120.000 anuales de útiles se reparten en CLP 10.000 por mes como convención presupuestaria.

Para la comisión propia se propone una liberación de siete días como hipótesis académica, con treinta días como estrés. No se atribuye ese plazo a Mercado Pago. Bajo mes financiero de treinta días, cobros uniformes y comisión mensual de CLP 24.000, siete días inmovilizan CLP 5.600 de comisión neta. El calendario conserva ese saldo por cobrar; no lo trata como caja disponible. La tarifa y liquidación efectivas se sustituyen al contar con condiciones de integración.

La documentación oficial de Split 1:1 respalda separar el saldo del vendedor y la comisión del marketplace, y señala requisitos específicos para configurar liberación de comisiones. No confirma las fechas o tarifas particulares de espaciGo. Referencias: [integración](https://www.mercadopago.com/developers/es/docs/split-payments/split-1-1/integration-configuration/integrate-marketplace) y [requisitos](https://www.mercadopago.com/developers/es/docs/split-payments/split-1-1/prerequisites). Se mantiene el descuento de comisión e IVA al publicador, junto al cargo de pasarela. No se contratan ni activan proveedores.

El escenario auxiliar requiere CLP 2.862.001,56 para cubrir lanzamiento y egresos identificados del primer trimestre sin depender de ventas, o CLP 2.795.601,56 si se materializan los 16 pagos mensuales y el plazo supuesto. Estos son importes de liquidez, no gastos nuevos que se suman otra vez al flujo. Excluyen partidas aún sin valorar y no garantizan continuidad después de tres meses. El IVA de comisión y los fondos de publicadores siguen separados; este ejercicio no calcula crédito fiscal de compras ni calendario tributario efectivo.

### Desglose propuesto del lanzamiento

| Asignación presupuestaria | CLP |
|---|---:|
| Formalización, trámites y asesoría | 300.000 |
| Preparación de contenidos y materiales | 300.000 |
| Campaña de lanzamiento previa a operar | 400.000 |
| Margen de contingencia preoperativa | 200.000 |
| Total | 1.200.000 |

Son asignaciones propuestas dentro del total ratificado, no cotizaciones, tasas legales ni gastos ejecutados. La campaña previa al lanzamiento se distingue de los CLP 350.000 mensuales operativos de 2027, mediante fechas y comprobantes. El margen no utilizado no se declara desembolsado por el solo hecho de reservarlo.

### Coherencia del presupuesto tecnológico

El documento interno 05-cost-analysis.md adopta USD 26,41 mensuales para una alternativa Single-AZ de piloto. El README de espacigo-aws también describe Multi-AZ y balanceador. Por tanto, no se aplica el costo del perfil pequeño a todo el diseño objetivo. Se propone mantener la cifra solo en la referencia piloto y evaluar el despliegue objetivo con presupuesto separado, antes de actualizar costos y umbrales comerciales.

Las cifras de escalamiento del documento interno no son cotizaciones nuevas ni pruebas de capacidad. No se verifican tarifas live ni se accede a un proyecto AWS. Los créditos no reducen el gasto de 2027 sin confirmar vigencia, saldo y elegibilidad. Esta revisión no cambia la arquitectura ni despliega recursos.

## 3. Desarrollo ejecutado y pendiente

El informe de Anita, apartado 2.2, sí contiene la base del importe: 16 semanas × 20 horas por semana × 3 integrantes = 960 horas; a CLP 6.500 por hora, totaliza CLP 6.240.000. La tarifa es una referencia del insumo, no un salario de mercado verificado ni un desembolso pactado. Esta evidencia permite cerrar la procedencia de la valorización, sin demostrar ejecución.

Se recomienda mantener las 960 horas como presupuesto global preoperativo y separar horas realmente ejecutadas y esfuerzo restante. No se propone adjudicar arbitrariamente un 50 % o un 80 % realizado. La cantidad de commits, funcionalidades o semanas transcurridas tampoco equivale a horas trabajadas.

Para planificar el tramo desde el 16 de noviembre hasta el 27 de diciembre de 2026 se propone una capacidad máxima de seis semanas × veinte horas × tres integrantes = 360 horas, valorizadas en CLP 2.340.000. Es capacidad propuesta disponible, no una estimación del trabajo que falta ni un porcentaje de avance probado. Si una revisión de tareas estima 360 horas pendientes, entonces ese saldo se usa para la evaluación incremental; las 600 horas restantes del presupuesto original no se declaran realizadas sin registros.

El registro_horas_y_pendientes.csv permite anotar por tarea: integrante, trabajo ejecutado reconstruido con evidencia, trabajo restante estimado y rango de incertidumbre. Se conserva el importe global en la evaluación de recuperación de la valorización; el flujo de caja no lo transforma en un pago obligatorio. No se modifica el Gantt de Erick ni se redacta su sección.

## 4. Reposición y cierre del horizonte

Se propone como caso de referencia no presupuestar compra de equipos personales ni venta de ellos por parte de la empresa. El valor económico del uso alternativo sigue separado. Esta delimitación coincide con la respuesta del propietario sobre uso personal y compartido; no prueba que jamás se requiera reemplazo.

Como escenario de estrés se propone comprar un notebook por CLP 900.000 en 2029. Es un presupuesto, no una cotización: el insumo de Anita usa CLP 800.000 por unidad; aplicar el supuesto del 4 % durante tres años produce CLP 899.891,20, redondeado presupuestariamente a CLP 900.000. La prueba requiere que la futura empresa asuma esa compra; no se presume que deba pagar la reposición de bienes personales.

A tasa del 12 %, una salida aislada de CLP 900.000 en el Año 3 reduce el VAN en CLP 640.602,22, sin atribuir un escudo fiscal no demostrado. Una reserva de CLP 25.000 por treinta y seis meses acumula CLP 900.000, pero es una separación interna de liquidez: no se resta como gasto mensual además de la compra. Si los fundadores continúan sin remuneración, la condición no elimina la necesidad de recursos para financiar esa reserva.

Para el cierre de 2030 se propone un caso prudente con cobro neto por venta de activos/software igual a cero y sin perpetuidad. Es una convención explícita para no depender de una venta futura, no una tasación de la empresa ni afirmación de que sus activos carezcan de valor. Se compara un caso con valor comercial únicamente cuando existe evidencia. Las cuentas por cobrar recuperables y cualquier capital del ciclo realmente aportado se liquidan por separado; no se recuperan pérdidas operativas acumuladas como si fueran un activo.

## 5. Decisiones recomendadas y orden de aplicación

1. Adoptar un caso académico de referencia con demanda hipotética delimitada y un plan de validación real, preservando las nueve categorías.
2. Usar la tarifa pública de NIC directo y el calendario anual/mensual propuesto, con siete días de comisión por cobrar y estrés de treinta, hasta sustituirlos por condiciones efectivas.
3. Mantener CLP 6.240.000 como valorización global trazable y calcular el saldo incremental por tareas y horas, sin inventar porcentaje ejecutado.
4. Comparar caso sin compra de equipos propios con estrés de CLP 900.000 en 2029; no duplicar la reserva interna y la adquisición.
5. Cerrar el caso prudente sin ingreso esperado por venta ni perpetuidad. Emitir una conclusión del escenario, distinta de una validación comercial real.

Después de adoptar las hipótesis se recalculan los cuatro años, cuentas por cobrar, flujo puro/financiado y asignaciones condicionadas, VAN, TIR y recuperación, manteniendo descuento 12 % e impuesto académico 27 %. Solo entonces se reemplaza la versión económica de referencia. La propuesta no declara cerrado por anticipado el costo de capital de mercado, demanda empírica o contratación de proveedores.

## Insumos y trazabilidad

- Valorización: 01_extraccion/informe/informe_completo.md, sección 2.2.
- Precio de referencia del notebook: 01_extraccion/excel/13-maquinaria-valores.csv.
- Presupuestos conciliados: 04_modelo_sapag/costos_conciliados.json.
- Propiedad y lanzamiento: 04_modelo_sapag/parametros_ejecucion.json y aclaraciones del propietario.
- Alcance tecnológico: espacigo-aws/README.md y docs/architecture/aws-proposal/05-cost-analysis.md. Solo contraste documental local.
- Calculo: calcular_propuesta.py; resultados en parametros_propuestos.json y calendario_2027_propuesto.csv.

## Ubicación de la actualización posterior

| Entrada | Cuerpo | Memoria o anexo |
|---|---|---|
| Demanda, ticket y validación | 14.1 | H.31 y matriz de oferta |
| Costos, fechas de pago y cuentas por cobrar | 14.2.2, 14.3 y 14.7 | H.32 y H.37 |
| Horas ejecutadas/restantes y valoración | 14.2.1 | H.40 |
| Reposición y cierre | 14.3 y 14.8 | H.39 |
| Indicadores recalculados del escenario elegido | 14.4–14.6 | H.36 y H.38 |

La actualización conserva las tablas de flujos completos en el cuerpo y las memorias en el anexo. Los insumos originales se mantienen como antecedentes. Los registros de campo o tareas no completados siguen vacíos, sin convertirse en ceros observados.
