# Comisión del 3 % y reparto de los tres socios: contrato de datos

**Decisión del usuario, 29-09-2026:** la comisión de servicio de EspaciGo para el escenario vigente es **3 % neto del arriendo**, más IVA de la comisión cuando corresponda; el reparto de los tres fundadores ocurre **dentro de la empresa**, fuera de Mercado Pago Split 1:1. La tasa del 12 % de comisión es un escenario anterior incorporado el 24-09-2026 por Hernán. El aporte de Shiva modela **25 % de comisión** en un estudio hipotético; usa **12 % como tasa de descuento** para el VAN. El Anexo A y ambas configuraciones del simulador ya se recalcularon al 3 %; ningún escenario acredita venta o tarifa contractual.

**Aclaración comercial posterior, congelada por ahora:** el usuario asocia una cifra de **3,19 %** al Split 1:1 y plantea que el comprador asuma además el costo operativo de Checkout API, con una merma aproximada de 7 % para el propietario. Es una **hipótesis para investigar en el anexo de Mercado Pago**, no una tasa contractual ni una liquidación demostrada. Aritméticamente, **3 % más IVA de 19 % sobre esa comisión = 3,57 % del arriendo**, no 3,19 %. La documentación oficial del Split indica que la tarifa de Mercado Pago se descuenta primero al **vendedor/arrendador** y luego la comisión del marketplace del saldo; trasladar económicamente un cargo al comprador requeriría definir precio final y verificar contrato/checkout ([Mercado Pago, integración 1:1](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/integration-configuration/integrate-marketplace)). El **arrendatario paga**; quien recibe el neto del arriendo es el **arrendador**. No afirmar un 7 % exacto hasta conocer tasas, bases imponibles y comprobante de liquidación. Esta incertidumbre no bloquea el diseño de la base: se guardan importes reales y su fuente por componente.

## Flujo de una reserva, ejemplo didáctico

El Anexo A vigente usa **precio final publicado de arriendo de 100.000 CLP pagado por el comprador**. La comisión y la tarifa de proveedor se descuentan del saldo del arrendador en el ejemplo, conforme al orden público de Split 1:1. Las condiciones de la cuenta, el contrato y el documento tributario aún deben confirmar el flujo exacto.

| Concepto | Ejemplo con arriendo de 100.000 CLP | Naturaleza |
| --- | ---: | --- |
| Arriendo del vendedor | 100.000 | Fondo de tercero, no ingreso de EspaciGo |
| Comisión neta EspaciGo: `100.000 × 0,03` | 3.000 | Ingreso propio antes de costos/impuestos sobre renta |
| IVA ilustrativo sobre comisión: `3.000 × 0,19` | 570 | Impuesto recargado, no utilidad de socios; aplicabilidad/documento por validar con contador/SII |
| Tarifa pública referencial de Mercado Pago: `100.000 × 0,0319` | 3.190 | Descuento neto al vendedor; no tarifa contractual Split |
| IVA referencial de esa tarifa | 606,10 | Tratamiento/documento del vendedor por confirmar |
| Total ilustrativo a cobrar al comprador | 100.000 | Precio final publicado; excluye garantía |
| Neto aritmético del vendedor | 92.633,90 | 100.000 − 3.190 − 606,10 − 3.000 − 570; requiere reporte real |

La tasa general de IVA publicada por el SII es 19 %, pero la afectación y el emisor del documento de **cada componente** requieren revisión particular ([SII, tasa IVA](https://www.sii.cl/preguntas_frecuentes/impuestos_mensuales/001_130_0572.htm)). El arriendo puede tener tratamiento distinto al servicio de la plataforma. La garantía se modela por separado; no es ingreso propio. La tarifa de Mercado Pago y su incidencia económica no se deducen del 3 %. En Split 1:1 el proveedor documenta el reparto entre **vendedor y marketplace** y descuento inicial de su cargo al vendedor ([Mercado Pago, integración 1:1](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/integration-configuration/integrate-marketplace)).

## Reparto igualitario dentro de la SpA

El informe plantea tres fundadores con 1.000 de 3.000 acciones cada uno. Como hipótesis de propiedad igualitaria, la participación es `1/3` para cada socio. Esta proporción **no autoriza automáticamente** pagar cada mes un tercio de cada comisión: primero se separan fondos de terceros, IVA, comisiones del proveedor, reembolsos, operación, obligaciones tributarias y reservas que establezcan estatutos/decisiones societarias. Los socios reciben la distribución que se acuerde sobre el **monto distribuible** de la empresa, con su documentación tributaria. El SII distingue distribuciones/retiros de las operaciones de venta y su tratamiento depende del régimen de la sociedad ([SII, regímenes tributarios 2026](https://www.sii.cl/destacados/renta/2026/intermediarios/regimenes_tributarios/)); el Código de Comercio regula la SpA y sus reglas estatutarias ([BCN, Código de Comercio](https://www.bcn.cl/leychile/navegar?idNorma=1974&idParte=8725218)).

**Ejemplo solicitado:** si el resultado contable y la decisión societaria dejan **12.000.000 CLP distribuibles**, cada socio con un tercio recibiría **4.000.000 CLP**, antes de los impuestos personales que correspondan. Si los 12.000.000 CLP son solo **comisiones netas facturadas** en el mes, `12.000.000 / 3 = 4.000.000` es una **atribución teórica bruta** por socio, no un pago disponible: faltan costos, impuestos y ajustes. Si los 12 millones fueran el total cobrado a compradores, incluirían arriendos de terceros e IVA; no pueden repartirse entre fundadores.

En una reserva de 100.000 CLP, los 3.000 CLP netos de comisión equivalen aritméticamente a **1.000 CLP atribuidos a cada fundador antes de costos**. El sistema de reservas no ordena tres transferencias de 1.000 CLP. El monto efectivamente pagable a cada socio surge del cierre y acuerdo societario.

## Sensibilidad inmediata del 3 %

El Anexo A usa como **comparador público de Checkout**, no tarifa contractual de Split, un cargo del procesador de **3,19 % neto + IVA** sobre el cobro al comprador: 3.190 + 606,10 CLP con ticket de 100.000 CLP. El vendedor recibe 92.633,90 CLP en esta aritmética, **7,3661 % menos** que el precio publicado; no se fija un descuento constante en la base. La plataforma recibe 3.000 CLP netos y presupone 3.000 CLP de firma, KYC y otros costos variables: contribución unitaria cero antes de infraestructura y trabajo fundador. Una compensación al vendedor por la tarifa del proveedor sería un **costo nuevo**, no incluido. El VAN de caja simulado al 3 % y con API mínima es −15.140.998 CLP; la TIR no está definida. No concluir viabilidad definitiva sin tarifa contractual, demanda y costos por categoría.

## Consecuencia para PostgreSQL

- `regla_comision` o configuración comercial versionada: `porcentaje_neto = 0,03`, base de cálculo, vigencia, moneda y actor que aprobó el cambio. RNF-020 de ES1 pide cambiar el parámetro sin redespliegue; la API lee la versión vigente y deja evidencia del cambio.
- `reserva` conserva `precio_arriendo_clp`, `comision_id`, `comision_neta_clp`, `iva_comision_clp`, `total_comprador_clp`, moneda y `calculo_version` junto con condiciones aceptadas. No reconstruir una reserva antigua usando la tasa del mes siguiente.
- `pago`/`movimiento_financiero` distinguen fondos del arrendador, comisión EspaciGo, IVA, cargo proveedor, reembolso y neto conciliado. Son hechos de negocio por reserva; un reembolso o contracargo agrega movimiento compensatorio.
- `cotizacion` y `reserva` guardan precio comprador, comisión e IVA por separado; `movimiento_financiero` registra fuente del importe y `liquidacion` conserva tarifa/IVA del proveedor y neto arrendador **observados**. La incidencia inicial al vendedor está documentada en la regla comercial y este escenario; si se cambia, se versiona la regla y la API. No inferir el neto con un porcentaje fijo en DDL.
- **No** crear tres destinatarios de pago en Split 1:1 ni tres `pago` por reserva. La distribución de utilidades de la SpA pertenece al sistema contable/administrativo y no debe contaminar el estado de la reserva. Si se registra en EspaciGo en el futuro, usar un módulo y tablas separados (`periodo_distribucion`, `acuerdo_distribucion`, `pago_socio`) con importes aprobados, soporte contable y permisos restrictivos; no es parte del DDL nuclear.
- La tarifa mínima de RQF-073 (>5.000 CLP de precio base) se conserva por trazabilidad; con 3 % puede no cubrir costos de una reserva corta. El resultado exige reestimar por categoría una duración mínima, cargo mínimo o política comercial, sin modificar silenciosamente ese RQF.

## Pendientes para el informe económico y legal

`[[PENDIENTE: precisar con documentos el IVA y emisor de comisión/arriendo/tarifa, la tarifa contractual de Split, las condiciones de compensación o cargo al comprador si se proponen, el régimen tributario y el mecanismo societario de reparto con contador/estatutos.]]`
