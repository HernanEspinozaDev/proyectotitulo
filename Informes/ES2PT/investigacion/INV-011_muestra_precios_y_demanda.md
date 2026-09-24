# INV-011 — Precios públicos y validación de demanda por segmento

- Consulta: 23-09-2026. Estado: muestra documental de oferta; demanda, reservas y aceptación de comisión **sin verificar**.
- Base congelada: ES1 propone distintas clases de arriendo temporal, entre ellas microalmacenamiento, oficinas, espacios multipropósito, quinchos, estacionamientos y parcelas. No se modifica su informe. La decisión del equipo para ES2 es abarcar **todos los tipos de arriendo**, sin escoger una sola categoría como alcance comercial.
- Uso: 2.1 y Anexo A. Datos del cálculo: `supuestos_bootstrap.json`; salida regenerable: `../build/simulacion_bootstrap.json`.

## Pregunta y unidad de comparación

El modelo usa 100.000 CLP de **arriendo final por reserva**, 12 % de comisión neta y 0/720/1.800 reservas en los años 1–3. ¿Se puede tratar ese ticket y volumen como representativos de todos los espacios propuestos? **No con la evidencia disponible.** Una hora de oficina, una jornada de sala y un mes de bodega son unidades distintas; los avisos de oferta no miden transacciones ni ocupación.

La cartera se registrará como categorías extensibles y, dentro de cada una, por modalidad y duración. La reserva es la unidad transaccional; capacidad y ocupación se medirán en horas, días o meses disponibles según corresponda. Se investigarán en paralelo oficinas, salas/multipropósito, bodegas, estacionamientos, locales/stands, quinchos, parcelas/eventos y cualquier otro arriendo incorporado. Estas clases sirven para medir el mercado; no eliminan ninguna categoría del producto ni reemplazan los requisitos de ES1.

## Muestra dirigida de precios publicados

| Segmento y proveedor | Producto/duración publicados | Precio anunciado | Importe final comparable del ejemplo | Límite |
| --- | --- | ---: | ---: | --- |
| Oficina privada, [Lofwork Santiago Centro](https://www.lofwork.cl/salas-y-oficinas-en-santiago/) | 1 hora, hasta 3 personas | 6.000 CLP + IVA/h | 7.140 CLP por 1 h | Precio «desde»; agenda y total final en TUU |
| Sala, [Lofwork Santiago Centro](https://www.lofwork.cl/salas-y-oficinas-en-santiago/) | 1 hora, hasta 10 personas | 18.000 CLP + IVA/h | 21.420 CLP por 1 h | Capacidad y condiciones distintas de oficina |
| Sala, [Cowork del Centro](https://coworkdelcentro.cl/) | 2 h seguidas, mínimo publicado | 17.750 CLP + IVA/h | 42.245 CLP por 2 h | Tarifa depende de duración |
| Sala, [Cowork del Centro](https://coworkdelcentro.cl/) | 5 h seguidas | 10.500 CLP + IVA/h | 62.475 CLP por 5 h | No equivale a cinco reservas individuales |
| Sala, [Cowork del Centro](https://coworkdelcentro.cl/) | 10 h seguidas | 7.750 CLP + IVA/h | 92.225 CLP por 10 h | Una jornada, no una hora promedio |
| Minibodega, [BLT](https://www.bltminibodegas.cl/bodegas?bussines=true) | 2–4 m², mes | Desde 55.000 CLP/mes; promoción 29.000 los dos primeros meses | Sin conversión: IVA/condiciones no aclarados en el aviso | Sucursal Macul consultada, no Santiago Centro; verificar vigencia y tamaño específico |
| Minibodega, [BLT](https://www.bltminibodegas.cl/bodegas?bussines=true) | 5,7–8 m², mes | Desde 105.000 CLP/mes; promoción 55.500 los dos primeros meses | Sin conversión: IVA/condiciones no aclarados en el aviso | Precio inicial/promocional distinto de renovación |
| Estacionamiento, [Saba Santa Rosa](https://www.saba-chile.cl/es/parking-santiago/parking-saba-santa-rosa) | 1 hora | 2.940 CLP/h en promoción | 2.940 CLP anunciados | Tarifa del operador directo; no demuestra precio, disponibilidad ni comisión de EspaciGo |
| Stand comercial, [Busho Galería La Bota Italia](https://busho.cl/stand-7-en-galeria-la-bota-italia-tu-espacio-emprendedor-en-barrio-italia-560) | Bloque mínimo de 4 días | 83.000 CLP/4 días; ficha expresa 20.750 CLP/día | 83.000 CLP para el bloque publicado | El día no se vende por separado; impuestos y total de checkout por confirmar |
| Espacio de trabajo flexible, [Espacio Temporal](https://www.espaciotemporal.cl/) | Mes; contrato desde 3 meses | Desde 175.000 CLP/mes en sede Salvador | Sin conversión: mínimo contractual y tratamiento tributario por confirmar | No equivale a una reserva por hora ni prueba precio EspaciGo |
| Parcela para eventos con quincho, [Palmas de Malloco](https://www.palmasdemalloco.cl/precios-arriendo-parcela-eventos/) | Jornada según evento | Cotizador según asistentes, temporada, horario y adicionales | Pendiente de cotización concreta | Quincho integrado, no precio de quincho independiente; garantía reembolsable de 150.000 CLP no es ingreso |

Los importes finales de salas son **cálculos** `precio publicado × horas × 1,19`, no nuevos precios anunciados. En BLT no se suma IVA por no constar su tratamiento en la ficha consultada. Lofwork indica revisión propia el 11-08-2026; las otras páginas no muestran fecha editorial clara. Los valores pueden cambiar y no se comprueba disponibilidad al reservar. La muestra es dirigida, pequeña y heterogénea; **no se promedia** ni prueba disposición a pagar. El ejemplo de parcela incluye quincho, pero falta una tarifa de quincho separado. La oficina física Lofwork es un producto distinto de la **oficina virtual** presupuestada para la SpA. Las garantías y fondos del arrendador no se sumarán a los ingresos de EspaciGo.

## Efecto del ticket en la simulación

Se mantienen exactamente las cantidades hipotéticas, 12 % de comisión, cargos de terceros, IPC y costos del caso base; solo cambia el arriendo final inicial. Por tanto, estas filas **no** son proyecciones de cada segmento ni incorporan su distinta duración, ocupación o tratamiento tributario.

| Arriendo final inicial por reserva | VAN de caja a tres años | Contribución total del año 3, antes de fijos | Lectura |
| ---: | ---: | ---: | --- |
| 30.000 CLP | -15.151.774 CLP | -961.096 CLP | El costo variable excede la comisión; vender más reservas idénticas agrava la pérdida variable |
| 50.000 CLP | -11.221.363 CLP | 2.291.933 CLP | Contribución positiva, insuficiente para cubrir fijos |
| 100.000 CLP, base | -2.448.407 CLP | 10.424.507 CLP | Sigue sin recuperar el proyecto en 36 meses |
| 150.000 CLP | 3.929.083 CLP | 18.557.080 CLP | VAN positivo **condicionado** a ese ticket y volumen no demostrados |

Con un arriendo inicial de 30.000 CLP, la comisión neta es 3.600; la pasarela estimada cobra sobre `30.000 + 3.600 × 1,19`, unos 1.094 netos, y los demás variables suman 3.000. Queda una contribución de unos **-494 CLP por reserva**, antes de fijos. Bajo estos mismos parámetros y sin descuentos por volumen, la contribución se hace positiva recién sobre **35.909 CLP de arriendo final inicial**. Esta frontera de costo variable **no** es punto de equilibrio empresarial ni justifica imponer precio mínimo al mercado.

Para comparar el efecto del tamaño de transacción en el **mismo flujo hipotético**, la contribución por reserva inicial es `arriendo_final × [0,12 − 0,0319 × (1 + 0,12 × 1,19)] − 3.000`. Los 3.000 CLP reúnen dos firmas, KYC y otros cargos presupuestados; se mantienen para todas las filas solo como prueba de tensión, aunque el flujo legal y operativo real podría diferir por categoría. No se incorporan costos fijos ni se deduce el IVA del arriendo del operador.

| Arriendo final supuesto para una reserva | Contribución variable calculada | Lectura condicionada |
| ---: | ---: | --- |
| 2.940 CLP | -2.754 CLP | Ejemplo del tamaño de una hora de estacionamiento anunciada |
| 7.140 CLP | -2.403 CLP | Ejemplo de una hora de oficina con IVA calculado |
| 21.420 CLP | -1.210 CLP | Ejemplo de una hora de sala con IVA calculado |
| 42.245 CLP | +529 CLP | Ejemplo de bloque de dos horas de sala con IVA calculado |
| 83.000 CLP | +3.934 CLP | Ejemplo del bloque mínimo publicado de stand; total tributario por confirmar |

Estas cifras **no** convierten anuncios de terceros en tarifas EspaciGo ni prueban que el mismo conjunto de cargos corresponda a cada producto. Indican que antes de presupuestar reservas cortas hay que cotizar si firma e identidad se cobran por reserva, por usuario o por contrato, y si la pasarela admite el reparto planteado. No se modifica por esta sensibilidad ningún requisito funcional ya validado.

## Demanda y capacidad aún sin evidencia

La vacancia de oficinas citada en ES1 es una medida del **stock de oferta**; no permite deducir que EspaciGo obtendrá 720 o 1.800 reservas. El año 2 supone 60 reservas mensuales en promedio y el año 3, 150. Como prueba aritmética, con 30 espacios activos el segundo objetivo exigiría 5 reservas por espacio al mes; una sala por horas puede tener esos turnos, pero una minibodega cedida por el mes completo no. No hay inventario comprometido, calendario publicado ni compradores identificados que acrediten esa capacidad.

Para sustituir los supuestos, levantar **muestras separadas por tipo, modalidad y comuna**. Registrar anuncios comparables con fecha, enlace, superficie/capacidad, duración mínima, precio total, impuestos, garantía, cancelación y disponibilidad; separar precio normal de promoción. Entrevistar por separado a dueños y arrendatarios de cada categoría con una **muestra exploratoria propuesta**, no estadísticamente representativa, y conservar consentimiento y respuestas agregadas sin datos personales en el informe. Preguntar al arrendador cuántos turnos podría ofrecer, restricciones de subarriendo y comisión aceptable; al comprador, duración real, precio total tolerable, condiciones de garantía y si completaría una reserva. Contrastar intención declarada con pruebas de reserva efectivamente pagada cuando exista producto.

Definir por categoría `reservas posibles = turnos comercializables × ocupación observada × conversión a pago`, evitando contar la conversión dos veces si la ocupación ya representa reservas pagadas. Registrar cancelaciones/reembolsos, compradores recurrentes, costo de firma y KYC aplicable a cada operación; **no** usar visitas web o respuestas favorables como ventas. Una reserva mensual inmoviliza el espacio durante ese mes; las horas disponibles de una sala pueden generar varias reservas. Si no hay evidencia antes de ES2, mantener 0/720/1.800 y 100.000 CLP etiquetados como supuestos y presentar las sensibilidades, sin seleccionar el escenario favorable como conclusión.

El motor `simular_bootstrap.py` admite una lista `segmentos` que reemplaza la lista agregada `reservas` del JSON. Cada entrada necesita `id`, 36 cantidades mensuales, `arriendo_final_base`, `comision_neta`, `firmas_por_reserva`, `kyc_neto_por_reserva` y `otros_variables_netos`. Puede haber varias entradas de una misma categoría con duraciones distintas. El resultado mensual conserva `detalle_segmentos`; así se suman flujos de caja sin promediar precios de horas, días y meses. **No se ha llenado esa lista con ventas inventadas:** el archivo vigente sigue siendo un escenario agregado provisional hasta contar con precios finales, oferta y demanda medidos por tipo.

[[PENDIENTE: levantar inventario y muestra comparable para todas las categorías propuestas, incluido quincho independiente; obtener entrevistas con consentimiento, precios finales y condiciones; medir conversión y ocupación por modalidad; validar aceptación de comisión, firma y garantía; cargar 36 meses por tipo y recalcular costos, flujos y sensibilidad.]]
