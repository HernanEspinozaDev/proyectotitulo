# INV-026 — Mercado Pago: reparto 1:1, tarifa, cuenta de empresa, entorno de pruebas y giros

**Decisión posterior del equipo (23-09-2026):** la propuesta de inicio de actividades es **631200 principal y 731001 complementaria**. La evaluación de 682000 de este registro queda como **consulta al contador/SII** por la comisión transaccional, no como tercer giro propuesto ni tercera patente. La patente municipal se calcula para la SpA en su domicilio con independencia del número de giros; ver [INV-029](INV-029_domicilio_patente_y_dom.md).

- Estado: investigación documental sobre documentación oficial de Mercado Pago (sitio Chile) y del SII, consultada el 24-09-2026. No existe cuenta de empresa constituida, ni aplicación creada, ni cuenta de prueba, ni cobro ejecutado. Nada de lo que sigue acredita habilitación comercial.
- Base: [INV-012](INV-012_pagos_firma_identidad.md), [INV-013](INV-013_monetizacion_pagos_y_promocion.md), [INV-014](INV-014_giro_publicidad.md), [INV-018](INV-018_comparacion_split.md) y el [Anexo A](../anexos/A_evaluacion_economica.md). Este registro **confirma y precisa** a INV-018; no lo reemplaza ni cambia el modelo económico.
- Alcance: arriendos de todas las categorías; el ingreso propio de EspaciGo es su comisión y sus servicios propios, nunca el arriendo de un tercero.
- Uso: responde al punto 1 de `pendientes.md` (terceros: pagos) y alimenta la decisión del equipo antes de tocar el cuerpo o el Anexo A.

## 1. Qué queda confirmado por la documentación oficial de Mercado Pago

| Afirmación | Evidencia primaria | Límite que conserva |
| --- | --- | --- |
| El **reparto 1:1 es el modelo documentado para un marketplace** y Chile figura entre los países con disponibilidad. | [Split de Pagos 1:1](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/overview): «proporcionar servicios de Proveedor de Servicios de Pago (PSP) a vendedores en modelos de marketplace», con listado de países que incluye Chile. | Disponibilidad de producto no equivale a contrato ni a habilitación de la cuenta de EspaciGo. |
| El chequeo es el **usual de Mercado Pago**: Checkout Pro, Checkout API o Checkout Bricks, y **no otros productos**. | [Crear configuración](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/integration-configuration/create-configuration): «la solución de Split de Pagos 1:1 sólo se puede integrar con Checkout Pro, Checkout API y Checkout Bricks, y no está disponible para otros productos». | La página de [requisitos previos](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/prerequisites) menciona **solo** Checkout Pro y Checkout API. Las dos páginas oficiales no coinciden en Bricks: hay que confirmarlo por escrito antes de elegir producto. |
| El **modelo 1:N** (varios receptores en un pago) **no está abierto**: requiere cartera asesorada. | Misma página de requisitos: «El modelo 1:N está disponible únicamente para vendedores de cartera asesorada que estén en contacto con el equipo comercial de Mercado Pago». Y: «si es necesario realizar configuraciones sobre la fecha de liberación de la comisión (marketplace fee o application fee), contacta a tu ejecutivo comercial de cartera asesorada». | Refuerza que el reparto automático contemporáneo al pago corresponde al 1:1 y que cualquier liberación diferida depende de un ejecutivo comercial. |
| Se exige **cuenta de vendedor con KYC 6**, aplicación, **OAuth con cada revendedor**, credenciales y cuentas de prueba. | Misma página de requisitos, tabla de requisitos: «Para integrar, necesitas una cuenta de vendedor en Mercado Pago con un nivel de identificación KYC 6»; «Los revendedores en el Marketplace deben pasar por el proceso de autorización OAuth»; «Cuentas de prueba: te permiten realizar testeos… Las puedes crear en Tus integraciones». | La documentación **no distingue persona natural de persona jurídica** ni describe una «cuenta de empresa» con ese nombre: hay que confirmar con el ejecutivo que la cuenta de empresa de la SpA cumple KYC 6 y puede activar el modelo marketplace. |
| La **comisión de Mercado Pago se descuenta primero de los fondos del vendedor** y la del marketplace del saldo restante. | [Integrar el checkout (marketplace)](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/integration-configuration/integrate-marketplace): «La comisión de Mercado Pago se descuenta de los fondos recibidos por el vendedor. Es decir, primero se descuenta la comisión de Mercado Pago, y la comisión del marketplace se descuenta del saldo restante». | Confirma la afirmación ya usada en el informe y en INV-018. No fija la tasa para Split ni dice quién asume la incidencia económica si el arrendador debe recibir el arriendo íntegro. |
| La comisión de EspaciGo se parametriza con **`marketplace_fee`** (Checkout Pro) o **`application_fee`** (Checkout API). | Misma guía de integración, pasos 3 y 4: `marketplace_fee` en `/checkout/preferences`; `application_fee` en `/v1/payments`. | El monto depende del acuerdo con el arrendador; el proveedor no lo define. |
| Para el reparto se usa **`public_key` del integrador y el `access_token` del vendedor** obtenido por OAuth. | Misma guía: «usa la `public_key` de tu cuenta de integrador en el frontend e inserta el `access_token` del vendedor (obtenido en el paso 1) en el backend». | Obliga a custodiar los tokens de cada arrendador y a separar credenciales por entorno. |
| Las credenciales del vendedor vinculado **válidas 6 meses**, con `refresh_token` y `user_id`/`collector_id`. | [Crear configuración](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/integration-configuration/create-configuration), respuesta de OAuth: «Estas credenciales tienen una validez de 6 meses. En caso de no renovarlas antes de ese período, perderán vigencia y será necesario repetir el proceso de vinculación». | Es una obligación operativa mensual: sin renovación, la venta del arrendador deja de operar. |
| En un **reembolso** se descuenta proporcionalmente a ambas cuentas y el marketplace **no puede completar el reembolso total si el vendedor no tiene saldo**. | Misma guía: «En caso de reembolso, el valor adeudado al cliente final será dividido y restado de la cuenta del vendedor y de la cuenta del Marketplace, de forma proporcional… el Marketplace no podrá realizar el reembolso total si el vendedor no tuviera dinero en la cuenta». | Riesgo de servicio y de caja ya registrado en INV-018; se mantiene. |
| El producto 1:1 **solo admite pagos con dinero en cuenta entre cuentas de Mercado Pago** y no transferencias de instituciones financieras externas. | Misma guía, al cierre: «la solución Split de Pagos 1:1 sólo permite realizar pagos con dinero en cuenta entre cuentas de Mercado Pago. No se permiten transferencias de instituciones financieras externas». | **Punto crítico y ambiguo.** Puede leerse (a) como medio de pago del comprador limitado al saldo de su cuenta, o (b) como forma de acreditación entre cuentas, sin habilitar retiro por transferencia a un banco externo. Las dos lecturas cambian el diseño del checkout; hay que confirmarlo por escrito con Mercado Pago. Hoy el informe no afirma ninguna de las dos (ver 2.2 del cuerpo). |
| El **reporte de ventas del split** entrega tarifa de Mercado Pago, tarifa del marketplace y monto recibido, y sirve para conciliación y para casos de liquidación/bloqueo/desbloqueo. | [Reporte de ventas con split de pagos](https://www.mercadopago.cl/developers/es/docs/reports/sales-report/introduction) y sus [campos](https://www.mercadopago.cl/developers/es/docs/reports/sales-report/report-fields): «tarifa del marketplace, tarifa de Mercado Pago y monto total de dinero recibido»; campos `MP fee amt. LC`, `Net Received Amt LC`, `Description split`, `External reference`. | Se genera y descarga **solo por API**; exige construir la conciliación antes de prometer liquidaciones. Incluye `Payment method type`, dato que ayudará a medir qué medios están realmente habilitados. |

## 2. El entorno de pruebas es el de Mercado Pago (cuentas de prueba)

Evidencia: [Cuentas de prueba](https://www.mercadopago.cl/developers/es/docs/your-integrations/test/accounts) y la tabla de requisitos de Split.

1. Las cuentas de prueba «tienen las mismas características que una cuenta real de Mercado Pago» y se crean automáticamente al crear la aplicación, o manualmente en **Tus integraciones → la aplicación → Cuentas de prueba**.
2. Hay tres tipos y el modelo marketplace usa los tres: **Vendedor** («cuenta requerida para configurar la aplicación y las credenciales. Esta es tu cuenta de usuario»), **Comprador** y **Integrador** («cuenta que se usa en integraciones del modelo marketplace»).
3. Solo se pueden generar **15 a la vez** y **no se pueden eliminar**.
4. El **país se fija al crear la cuenta y no se puede editar después**; comprador y vendedor deben ser del mismo país (Chile).
5. Se dispone de **tarjetas de prueba** y de un **saldo ficticio** editable para simular pagos y el saldo de la cuenta.
6. Al iniciar sesión con una cuenta de prueba **no hay acceso a «Credenciales de prueba» ni a «Calidad de integración»**; la documentación indica que esas secciones no son necesarias para esas cuentas y que pueden interferir en su uso.
7. **Checkout Bricks no soporta cuentas de prueba** para pruebas de integración. Si se eligiera Bricks, el camino de prueba sería distinto del de Pro/API (otra razón para resolver la discrepancia del punto 1).

**Qué no se puede probar así:** la habilitación comercial real de la cuenta de empresa, la tarifa efectiva de Split, los medios definitivamente habilitados por contrato, los plazos de acreditación y el tratamiento tributario. El entorno de prueba verifica **flujo**, no condiciones comerciales.

**Ensayo mínimo que ya venía definido en INV-018** y sigue siendo el criterio: vincular un arrendador de prueba por OAuth, fijar una comisión acordada, crear la reserva con identificador idempotente, cubrir pago aprobado y rechazado, repetición de la notificación y cambio de medio sin doble cobro; conciliar con el reporte de ventas (tarifa, comisión, neto, `External reference`); y probar cancelación antes del pago, reembolso total y parcial después del pago, vendedor sin saldo y contracargo. La garantía o depósito se prueba **aparte**: el split no es custodia.

## 3. Tarifa: qué soporta Mercado Pago y qué falta

- Mercado Pago **sí** soporta una tarifa por transacción y la descuenta automáticamente en el reparto (punto 1). Lo que no publica en la documentación de Split consultada es **la tasa aplicable a EspaciGo**.
- La tasa que usa el Anexo A (**3,19 % + IVA**, con **2,89 % + IVA** a diez días como alternativa) proviene de la página comercial de Checkout y debe seguir rotulada **supuesto referencial** (INV-018). Nada en la documentación de Split la confirma para este caso.
- La página de costos enlazada desde el sitio de desarrolladores **ya no responde** (`https://www.mercadopago.cl/costs-and-fees` devuelve «Esta página no existe», comprobado el 24-09-2026). El mismo día, `https://www.mercadopago.cl/herramientas-para-vender/check-out` redirigió a un rastreador publicitario y no entregó contenido. Conclusión operativa: **la tarifa vigente por producto, medio y plazo debe pedirse al ejecutivo o al soporte**, no deducirse de una página.
- **IVA de la tarifa.** La guía de Split describe a qué saldo se descuenta el cargo, pero no demuestra quién será el receptor del documento tributario ni quién podrá utilizar un eventual crédito fiscal en el caso concreto. El contador debe revisar factura, contrato y compensación al arrendador antes de atribuir ese IVA a cualquiera de las partes. Si EspaciGo decide compensar al arrendador para que reciba el arriendo íntegro, también debe definir cómo se registra y documenta esa compensación.
- **Efecto en el informe:** el Anexo A asigna hoy la incidencia económica de la tarifa a EspaciGo como hipótesis. La documentación confirma que el descuento ocurre en la cuenta del vendedor, de modo que la hipótesis sigue siendo una **decisión económica pendiente** (compensar, ajustar el precio informado o negociar), no un hecho que el proveedor resuelva por EspaciGo.

## 4. Giros: son más de uno y dependen de cada ingreso

La pregunta «¿cuántos giros?» se responde según las **actividades efectivamente desarrolladas** y los servicios cobrados. El modelo vigente prevé una comisión de intermediación y estudia cobrar destaques; operar el portal podría ser el canal de esa intermediación, sin constituir por ello un tercer ingreso. Los tres códigos siguientes son candidatos para revisar con un contador, no tres ingresos ya definidos.

| Actividad candidata | Dato verificable | IVA y comentario |
| --- | --- | --- |
| **682000 — Actividades inmobiliarias realizadas a cambio de una retribución o por contrata** | El [catálogo de actividades](https://www.sii.cl/catastro/codigos.htm) es la fuente de consulta. El SII precisa en su [pregunta frecuente sobre corretaje](https://www.sii.cl/preguntas_frecuentes/impuestos_mensuales/001_130_3147.htm) (ID 001.130.3147.007, actualizada el 24-06-2025) que, como norma general, el corretaje de propiedades es actividad de **primera categoría** y que quienes la ejercen «deberán declarar dicho impuesto y el IVA, siempre y cuando corresponda a personas jurídicas»; la excepción exenta del IVA (art. 12, letra E, N.º 8, de la LIVS) está descrita para **personas naturales** por actuación exclusivamente personal. | **Comisión por intermediación de arriendos.** EspaciGo es una SpA, no una persona natural: la lectura del texto del SII apunta a actividad **afecta a IVA**. El catálogo marca este código con estado de IVA dependiente («G»), por lo que la clasificación particular sigue requiriendo contador. |
| **631200 — Portales web** | El [catálogo de actividades](https://www.sii.cl/catastro/codigos.htm) lo registra con IVA «Sí». | **Actividad candidata por operar la plataforma.** El portal puede ser un canal sin precio propio; confirmar si corresponde inscribir este código además del de intermediación. No presupuestar ingreso de portal sin un servicio cobrado. |
| **731001 — Servicios de publicidad prestados por empresas** | El [catálogo](https://www.sii.cl/catastro/codigos.htm) lo marca con IVA «Sí». El SII responde en su [pregunta frecuente sobre propaganda](https://www.sii.cl/preguntas_frecuentes/declaracion_renta/001_140_3694.htm) (ID 001.140.3694.007, actualizada el 27-05-2025) que «los ingresos por concepto de publicidad, independiente del medio donde se realicen, se afectan con el Impuesto de Primera Categoría, mientras que estos servicios son gravados con el Impuesto al Valor Agregado». | **Destaques pagados**, y solo si el producto se vende. Con [INV-014](INV-014_giro_publicidad.md), sigue siendo candidato documental sólido, no giro aprobado. |

**Reglas de contexto que también importan:**

- **Regla general de servicios afectos a IVA.** Desde el 01-01-2023, por la entrada en vigencia de la Ley 21.420, «todas las prestaciones de servicios estarán afectas a IVA», con las exenciones que la ley mantiene (servicios personales con boletas de honorarios, transporte, educación, salud ambulatoria y sociedades de profesionales registradas), según la [noticia oficial del SII del 21-12-2022](https://www.sii.cl/noticias/2022/211222noti01aav.htm). Un servicio propio de EspaciGo parte, por tanto, desde la afectación, no desde la exención.
- **Sí se pueden registrar varias actividades, y agregar una afecta obligaciones.** El SII permite ampliar o agregar actividades en línea en su [portal del emprendedor](https://www.sii.cl/portales/emprendedor/verificacion_actividades.html); y al ampliar un giro afecto a IVA puede pedir **verificación de actividad** antes de seguir facturando (documentado en [INV-014](INV-014_giro_publicidad.md)).
- **La verificación de actividad depende del documento que se emitirá.** Ese mismo portal la exige «si iniciaste tu actividad comercial y necesitas emitir facturas electrónicas y/o otros documentos que dan derecho a crédito fiscal», y advierte que **no se requiere** «si solo emitirás boletas de ventas y servicios». Como los arrendadores serán, en su mayoría, personas que desarrollan actividad económica, la comisión de EspaciGo apunta a **factura electrónica** y, con ello, a verificación de actividad. Es un trámite previo, no un detalle posterior.
- **IVA Digital no aplica por domicilio.** El [portal IVA Digital del SII](https://www.sii.cl/destacados/iva_digital/index.html) delimita el régimen a plataformas **sin domicilio ni residencia en Chile** que prestan servicios gravados, y, desde el 25-10-2025, a plataformas o comercios de **intermediación digital extranjeros** que venden bienes remotos por hasta USD 500. EspaciGo, SpA constituida en Chile, no queda en ese régimen por su domicilio. La etiqueta «IVA digital» no debe usarse como régimen de la SpA.

## 5. Qué haría falta para habilitarlo (lista operativa, no ejecutada)

1. Constituir la SpA con un objeto social que permita intermediar arriendos, operar el portal y, si se decide, vender promoción; obtener RUT.
2. Abrir la **cuenta de empresa** de Mercado Pago a nombre de la SpA y confirmar que alcanza **KYC 6** y que puede activar el modelo marketplace.
3. Crear la aplicación en **Tus integraciones** como Pagos online, con Checkout Pro o Checkout API, **modelo de integración Marketplace**, y configurar la **Redirect URL** para OAuth.
4. Implementar **OAuth** con cada arrendador, almacenar `refresh_token` y `user_id` y programar la **renovación a los 6 meses**.
5. Definir el contrato de comisión y decidir **quién soporta la tarifa**; expresarlo en los términos y en el precio informado.
6. Crear las tres cuentas de prueba y ejecutar el ensayo mínimo de INV-018, incluidos reembolsos y contracargo.
7. Construir la conciliación con el reporte de ventas por API (`External reference` de la reserva).
8. Inscribir o verificar las actividades en el SII y habilitar la facturación electrónica de la comisión **antes** de cobrar.

## 6. Riesgos y límites que siguen abiertos

1. **Medio de pago.** Si la restricción de «dinero en cuenta» es del medio del comprador, hoy no se podría cobrar con tarjeta bajo 1:1 y habría que reabrir la comparación de pasarelas. Es la primera pregunta a resolver.
2. **Un arrendador por pago.** El 1:1 reparte entre un vendedor y un marketplace; una reserva con un solo arrendador encaja, pero un pago que deba dividirse entre varios (por ejemplo, espacios compartidos) no está cubierto sin cartera asesorada.
3. **Garantía o depósito.** El split no retiene ni libera fondos condicionados; la promesa de garantía de ES1 sigue sin mecanismo técnico verificado.
4. **Reembolsos y contracargos** dependen del saldo del arrendador; el marketplace no puede forzar el reembolso total.
5. **KYC por arrendador.** Cada arrendador debe vincular una cuenta de Mercado Pago propia; su nivel de identificación y su disposición a vincularse son una barrera de adopción no medida.
6. **Renovación de tokens** cada 6 meses: obligación operativa permanente.
7. **Tarifa y tributación** de la comisión sin cotización ni definición de documento por parte del contador.
8. **Discrepancia Bricks** entre dos páginas oficiales de requisitos.

## 7. Preguntas concretas para Mercado Pago (ejecutivo comercial o soporte)

1. ¿Cuál es la **tarifa de Split 1:1** para una SpA chilena, por medio de pago, cuotas y plazo de acreditación, y dónde se publica o se entrega por escrito?
2. La frase «sólo permite realizar pagos con **dinero en cuenta** entre cuentas de Mercado Pago»: ¿restringe el **medio del comprador** al saldo de su cuenta de Mercado Pago, o describe solo la forma de acreditación entre vendedor y marketplace? ¿Se admiten tarjetas de crédito o débito en Split 1:1?
3. ¿Una **cuenta de empresa** (persona jurídica) con KYC 6 habilita el modelo marketplace, o se requiere otra condición societaria?
4. ¿Cuál es el **nivel de identificación exigido a cada arrendador** que se vincula por OAuth, y qué pasa con su reserva si baja de nivel?
5. ¿Se puede integrar **Checkout Bricks** con Split 1:1? ¿Y cómo se prueba, si Bricks no admite cuentas de prueba?
6. ¿Cómo se documenta tributariamente la **tarifa de Mercado Pago** descontada al arrendador y la **comisión** acreditada a EspaciGo? ¿Qué documentos emite cada parte?
7. ¿Qué configuración de la **fecha de liberación** de la comisión existe y qué requiere del ejecutivo comercial?
8. ¿Hay límites de monto, cantidad de cuentas vinculadas o volumen para el modelo 1:1?
9. ¿Qué ocurre con la reserva si el **arrendador se desvincula** o su token vence a mitad del arriendo?
10. ¿Se puede probar **reembolso con vendedor sin saldo** en el entorno de pruebas antes de contratar?

## 8. Preguntas para el contador o el SII

1. ¿Cuál de estas glosas describe mejor la **comisión por intermediación**: 682000, otra actividad inmobiliaria por contrata, u otra distinta, considerando que EspaciGo no arrienda el bien ni es propietario?
2. ¿La comisión queda **afecta a IVA** siendo SpA, y con qué documento se emite al arrendador (factura electrónica, boleta según su calidad tributaria)?
3. ¿Se necesita también **631200** por operar el portal, o la comisión y el portal se cubren con una sola actividad?
4. Si se venden destaques, ¿se agrega **731001** y se emite documento separado del de la comisión?
5. ¿Qué implica la **verificación de actividad** al agregar un giro afecto y en qué orden debe hacerse respecto de la facturación?
6. ¿La **compensación al arrendador** por la tarifa del procesador es gasto, menor comisión u otro concepto, y cómo se documenta?
7. El **arriendo de cada categoría** (oficina, sala, bodega, estacionamiento, local, parcela con quincho, entre otras): ¿puede quedar afecto a IVA según amoblado, equipamiento y tipo de prestador, y dónde queda el límite?
8. ¿Corresponde que EspaciGo emita documento por el **total** procesado o solo por su comisión, y cómo se trata el dinero del tercero?

## 9. Efecto sobre el informe y decisión propuesta

- **El cuerpo y el Anexo A no cambian todavía.** Lo confirmado hoy no agrega ingresos, no modifica el VAN ni la TIR y no altera la tasa referencial. Lo que sí queda registrado es que en Split 1:1 **la tarifa se descuenta al arrendador**, de modo que la asignación de esa incidencia a EspaciGo es una **decisión económica pendiente**.
- **Si el equipo ratifica Mercado Pago Split 1:1**, corresponde entonces sí escribir en 2.2 y en el Anexo A: (a) el límite de producto (Checkout Pro o API, no otros), (b) la regla de quién soporta la tarifa y su compensación, (c) la regla de reembolso con saldo del vendedor y (d) el estado del medio de pago, con la respuesta escrita del proveedor.
- **Decisión propuesta:** mantener Split 1:1 como candidato principal, no prometer garantía retenida y ejecutar en paralelo (i) la consulta escrita al ejecutivo por las diez preguntas de la sección 7, (ii) la constitución de la SpA con verificación de actividad y (iii) el ensayo en las cuentas de prueba de Mercado Pago. La selección definitiva sigue dependiendo de contrato, prueba y revisión tributaria.

[[PENDIENTE: respuesta escrita de Mercado Pago sobre el medio de pago admitido en Split 1:1, la tarifa contractual por producto y medio, el nivel de identificación exigido a cada arrendador y la habilitación de una cuenta de empresa; confirmación del contador sobre la glosa de la comisión y sobre 631200 y 731001; decisión del equipo sobre quién soporta la tarifa y su documentación; ensayo en las cuentas de prueba, aún no ejecutado.]]
