# 03. Pendientes con terceros: qué hay que pedir, a quién y con qué se cierra

Nada de esta lista se cierra con trabajo documental: exige una cotización, una credencial, un contrato, una respuesta escrita o una entrevista. Las preguntas concretas ya están preparadas en [`INV-027_gestion_terceros.md`](../INV-027_gestion_terceros.md) y [`INV-026_mercado_pago_split.md`](../INV-026_mercado_pago_split.md); aquí solo se ordena qué enviar y en qué secuencia.

**Estado: ninguna consulta se ha enviado.** Todas las filas están abiertas.

## Prioridad sugerida

1. **Pago y firma** — son los que cambian el modelo económico y la sección 2.2.
2. **Contador** — IVA, crédito fiscal, giro y documentos.
3. **Municipio y domicilio** — patente, DOM y aseo.
4. **Trabajo de campo** — demanda y precios por categoría.
5. **Accesos** — organismos, pasarela y firma.

## Filas

| # | Qué falta | A quién se le pide | Evidencia que lo cierra | Responsable | Estado |
| --- | --- | --- | --- | --- | --- |
| 1 | **Quién soporta la tarifa y el IVA del split**, el saldo real de cada parte, los reembolsos, la garantía y la liberación condicionada | Proveedor de pago, cuenta de empresa y entorno de pruebas | Liquidación detallada de un caso real y un reembolso con vendedor sin saldo | | Abierto |
| 2 | **Diez preguntas abiertas de Mercado Pago** (ver abajo) | Ejecutivo comercial, cuenta de empresa y contador | Respuesta escrita + acta del ensayo en cuentas de prueba con cobro, reparto, reembolso y contracargo | | Abierto |
| 3 | **Cotizar firma electrónica** por documento y tipo jurídico, y verificación de identidad por usuario nuevo y por revalidación | Proveedor de firma e identidad | Cotización o contrato formal, comparable con la tarifa pública de INV-012 | | Abierto |
| 4 | **IVA y crédito fiscal de Google Cloud** y tipo de cambio aplicado | Contador + comprobantes de facturación | Primera factura pagada y su registro contable (hoy USD/CLP 1.000 y 19 % son supuestos) | | Abierto |
| 5 | **Confirmar giro y régimen**: 631200 principal, 731001 complementaria, documentos, DTE y capital pagable; consultar si la comisión exige 682000 u otra actividad | Contador y SII | Respuesta particular según contrato y prestaciones | | Abierto |
| 6 | **Domicilio y patente**: contrato con Oficina Express, la única patente comercial, trámites DOM, aseo y honorarios legales y contables | Municipalidad de Santiago, Oficina Express y profesionales | Contrato o derecho de uso, zonificación, exigencias DOM, liquidación de patente y aseo y presupuestos | | Abierto |
| 7 | **Medir el campo**: oferta, demanda, precio final, duración, capacidad, ocupación y aceptación de la comisión en **cada** tipo de arriendo | Arrendadores y arrendatarios, con consentimiento | Fichas del protocolo de INV-016 por `categoría × modalidad × comuna`, con rechazos y fuente | | Abierto |
| 8 | **Decidir y cotizar el destaque pagado**: precio, zona, cupos, pausas y reembolsos, y si entra en ES2 | Equipo y clientes piloto | Prueba con tráfico y oferta aprobada, con aceptación y canibalización medidas | | Abierto |
| 9 | **Ejecutar una campaña de Meta Ads** y medir costo por publicación y por reserva pagada | Equipo, cuenta publicitaria y la provisión de 357.000 CLP ya supuesta | Panel de campaña y eventos verificados | | Abierto |
| 10 | **Habilitar accesos**: Registro Civil, SII y pasarelas | Organismos y proveedores | Credenciales y una primera consulta registrada, sin secretos en el repositorio | | Abierto |

## Las diez preguntas a Mercado Pago (fila 2)

Ya está confirmado con documentación oficial que el reparto 1:1 existe en Chile, que exige KYC 6 y OAuth por arrendador, y que la tarifa del proveedor se descuenta primero al vendedor. Lo que sigue abierto y **lo que más afecta al producto**:

1. ¿La condición «solo permite pagos con dinero en cuenta» restringe el **medio de pago del comprador**? Es la pregunta crítica.
2. ¿Cuál es la **tarifa contractual** de Split para esta cuenta? La página de costos ya no responde.
3. ¿La **cuenta de empresa** de la SpA cumple KYC 6?
4. ¿Qué **nivel de identificación** se exige a cada arrendador vinculado?
5. ¿Se puede ejecutar el **ensayo en cuentas de prueba** (cobro, reparto, conciliación, reembolso sin saldo, contracargo)?
6. ¿Cómo se documenta tributariamente la comisión del marketplace?
7. ¿Qué pasa con la garantía y la liberación condicionada: son parte del split o van **por separado**?
8. ¿Qué requisitos adicionales (Bricks, modelos de marketplace, países admitidos) aplican a nuestra integración?
9. ¿Cuánto tarda la habilitación de un arrendador nuevo?
10. ¿Qué soporte existe para disputas y contracargos?

## Qué NO hace falta volver a investigar

- Que el split exista en Chile, o que la tarifa se descuente primero al vendedor: ya está documentado.
- Los precios publicados de oficina, sala, bodega, estacionamiento y stand: ya están transcritos en INV-011. Falta el **precio final, la duración y la conversión** de cada categoría, no el aviso.
- Las licencias y las capacidades documentadas de las tecnologías: están verificadas con fuente primaria.

## Nota sobre el domicilio

La oferta pública de Oficina Express (50.000 CLP/año más 5.000 CLP por firma del contrato, IVA incluido) y el mínimo ilustrativo de **1 UTM anual** de patente son referencias, no derechos adquiridos. La zona y la aceptación municipal del domicilio para el giro todavía no están confirmadas, y el aseo y las actuaciones DOM dependen de liquidación.
