# INV-012 — Costos y liquidación de pagos, firma e identidad

- Consulta: 23-09-2026. Estado: contraste documental; sin contrato, credenciales, cotización API ni transacciones de EspaciGo.
- Base: modelo de comisión y flujos de ES1; secciones ES2 2.2, 3.5 y Anexo A. No cambia requisitos validados.
- Método: páginas oficiales de proveedores. Mercado Pago bloqueó la apertura directa (HTTP 403); el detalle siguiente proviene del contenido indexado de sus páginas oficiales, pendiente de contraste contractual y en sandbox.

## Pagos divididos: quién soporta la tarifa

La [documentación de Split de Pagos 1:1](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/overview) identifica Chile como mercado disponible. Sus [prerrequisitos](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/prerequisites) incluyen vendedor con nivel KYC 6 y autorización OAuth; 1:N requiere cartera asesorada. La [guía de integración](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/integration-configuration/integrate-marketplace) describe `marketplace_fee`/`application_fee`, indica que la tarifa de Mercado Pago se descuenta primero del vendedor y después la comisión del marketplace, y advierte límites de reembolso cuando el vendedor no tiene saldo. Es un reparto 1:1; la documentación consultada **no demuestra custodia, garantía retenida ni liberación condicionada**. La [página pública de Checkout](https://www.mercadopago.cl/herramientas-para-vender/check-out) muestra 3,19 % + IVA para disponibilidad inmediata, pero esa tarifa no es una oferta individual de Split.

El presupuesto vigente supone que **EspaciGo absorbe económicamente** 3,19 % neto del cobro completo. Eso no describe la liquidación predeterminada que publica Split: para dejar al arrendador indemne haría falta acordar otro precio, compensarlo o contratar una condición diferente. Por ello, el costo de pasarela en `supuestos_bootstrap.json` es una **hipótesis de incidencia económica**, no un débito verificado de la cuenta de EspaciGo ni un crédito fiscal demostrado. Tampoco se sabe si el proveedor acepta cobrar arriendo más servicio gravado como se dibuja en el modelo.

Ejemplo de conciliación **solo aritmético**, antes de confirmar tasa/producto/impuestos: con arriendo anunciado de 100.000 CLP, comisión neta de EspaciGo de 12.000 e IVA supuesto de 2.280, el comprador pagaría 114.280. Si se aplica como referencia la tasa Checkout de 3,19 % más IVA a ese total, la tarifa sería 3.646 netos y 4.338 de salida bruta aproximada. Un reparto que entregue 14.280 a la plataforma dejaría unos 95.662 al vendedor, no 100.000. Estos importes no son una liquidación de prueba y omiten redondeo, impuestos propios del arrendador, contracargos y reglas exactas de Split. El ingreso propio no incluye los 100.000 de arriendo.

| Alternativa comercial por verificar | Ingreso y riesgo que se deben presupuestar |
| --- | --- |
| Vendedor soporta la tarifa de pagos, como indica la guía de Split | Definir si acepta recibir menos que el arriendo anunciado y cómo se exhibe precio/comisión al cliente. No tratar la tarifa como gasto pagado por EspaciGo. |
| EspaciGo compensa al vendedor | Obtener mecanismo contractual y tributario de compensación; calcular costo bruto, IVA, documentos y caja sin presumir crédito fiscal. |
| Precio final incorpora todos los cargos | Medir conversión y aceptación por tipo de arriendo; fijar claramente qué parte es del vendedor y cuál de EspaciGo. |

Para devoluciones, el proveedor describe descuentos proporcionales a ambas cuentas y un límite si al vendedor le falta saldo. Separar reserva cancelada, devolución parcial, contracargo y garantía; determinar quién adelanta caja y qué saldo mínimo se necesitaría. La garantía del arrendador no financiará a EspaciGo.

## Firma y verificación de identidad

La [tarifa pública de FirmaVirtual](https://firmavirtual.legal/servicios/precios) muestra FES sin notaría por **4.490 CLP por documento de dos a diez firmantes** y 3.450 por documento de un firmante. En la misma página, una respuesta resumida dice 3.450 «por parte», de modo que se debe confirmar la unidad comercial. La [API](https://firmavirtual.legal/servicios/api-firma-electronica) ofrece cobro por documento/contrato o volumen, pero **no publica aquí una tarifa numérica de API**. Los 2.000 CLP netos por reserva del presupuesto (dos firmantes a 1.000) son provisión, no esa tarifa. La sensibilidad ya calculada con 2.500 netos por firmante equivale a 5.000 por dos y lleva el VAN de caja de -2,45 a **-8,47 millones CLP**, sin probar que sea el precio API. Hay que determinar si se firma cada reserva o un contrato marco y qué modalidad jurídica procede por tipo de espacio.

Como **comparador internacional**, [Didit publica para Chile](https://didit.me/es/solutions/countries/chile/) un paquete KYC desde USD 0,33 y una consulta `chl_rut` adicional de USD 0,20, con nivel gratuito anunciado. Es información comercial del proveedor, no acceso probado, acuerdo de tratamiento de datos, acreditación de cumplimiento chileno ni precio final en CLP. A USD/CLP 1.000 supuesto, ambas partidas sumarían 530 CLP antes de impuestos y costos de cobro; los 500 CLP del presupuesto son cercanos solo aritméticamente. Si la verificación ocurre al alta del usuario y no en cada reserva, el costo dependerá de usuarios nuevos y revalidaciones, no de reservas. No se descontará automáticamente el nivel gratuito ni se adoptarán afirmaciones legales del proveedor como dictamen.

## Evidencia necesaria para reemplazar las hipótesis

1. Cotización escrita para Split 1:1 en Chile: tasa, IVA, responsable de la tarifa, base de cálculo, plazos, medios de pago, límites, reversos, contracargos, conciliación y facturación.
2. Prueba controlada de cobro, reparto y reembolso con vendedor de prueba, registrando monto inicial, comisión, tarifa, IVA y saldo de cada cuenta. Comprobar que el flujo aprobado de garantía/liberación es realmente posible; de lo contrario, documentar alternativa para decisión del equipo.
3. Oferta API de firma para uno y dos firmantes, FES/FEA/notaría según contrato, mínimo mensual, documentos rechazados y costo por renovación; revisión jurídica de cuándo se requiere firma.
4. Oferta y evaluación de identidad/KYB: número de usuarios nuevos, verificaciones repetidas, consultas nacionales, moneda, impuestos, ubicación de datos, conservación, eliminación y responsabilidades bajo Ley 21.719.

[[PENDIENTE: cotizaciones, acuerdo de incidencia de tarifas y tratamiento tributario, prueba Split de liquidación/reembolso, firma jurídicamente adecuada y precio API, evaluación de identidad y protección de datos.]]
