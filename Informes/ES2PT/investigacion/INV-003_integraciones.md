# INV-003 — Acceso y pruebas de integraciones

- Estado: investigación documental inicial; acceso y pruebas sin acreditar.
- Fecha de consulta: 2026-09-23.
- Base: informe ES1, arquitectura TI y anexos A–D.
- Secciones: 2.2, 3.1–3.7, 4.2 y 5.1.

## Pregunta y criterio de evidencia

¿Qué capacidades de los proveedores propuestos en ES1 están documentadas y cuáles puede utilizar efectivamente EspaciGo? Se separan cuatro niveles: página pública consultada, condiciones contractuales y de acceso, credenciales habilitadas, y prueba reproducible. Solo el primero tiene evidencia parcial. No se han contactado proveedores ni ejecutado integraciones.

| Integración | Hallazgo documental | Límite para EspaciGo | Evidencia siguiente |
| --- | --- | --- | --- |
| Mercado Pago | La [documentación oficial de Split Payments 1:1](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/prerequisites) menciona integración de vendedores con OAuth y reparto de pagos. La página completa devolvió 403 en esta consulta; el hallazgo proviene del extracto indexado. | Dividir un pago no acredita custodia, retención, liberación, garantía ni reembolso según ES1. Tampoco prueba habilitación comercial para el equipo. | Obtener documentación completa del producto aplicable en Chile, condiciones y entorno de prueba; probar cobro, eventos, devolución y conciliación con datos de ensayo. |
| FirmaVirtual | La [página oficial de API](https://firmavirtual.legal/servicios/api-firma-electronica) describe integración y entorno de pruebas. | No confirma credenciales del equipo, modalidad de firma jurídicamente adecuada ni contrato implementado. | Documentación técnica y condiciones de acceso; prueba de firma de ambas partes, rechazo, vencimiento y consulta de resultado. |
| SII | La [consulta de situación tributaria de terceros](https://www.sii.cl/como_se_hace_para/situacion_trib_terceros.html) es un servicio web público. | La página no constituye una API autorizada para EspaciGo ni cubre por sí sola KYB y emisión tributaria. | Identificar separadamente consulta KYB y emisión de documento; condiciones de automatización, autorización y pruebas. |
| Registro Civil | La [Resolución Exenta SII N.º 195 de 2025](https://www.sii.cl/normativa_legislacion/resoluciones/2025/reso195.pdf) acredita un convenio de interoperabilidad entre organismos públicos. | Es un ejemplo institucional, sin demostrar una API pública o un convenio disponible para EspaciGo. | Determinar canal oficial y requisitos de acceso al servicio concreto; si no procede, diseñar verificación alternativa documentada. |

Las claves `es2mpsplit`, `es2firmavirtualapi`, `es2siiconsulta` y `es2sii195` se registran en `referencias.bib`. La inferencia principal es que **ninguna capacidad de integración está demostrada en el proyecto** por estas páginas. Un error de red o timeout tampoco equivale a rechazo de una transacción; el diseño debe conservar correlación y conciliar antes de resolver reservas o fondos.

## Primer experimento propuesto

Preparar un adaptador de pagos con idempotencia, evento firmado, persistencia del estado y una prueba de respuesta tardía en entorno de ensayo. Registrar producto, versión de API, acceso autorizado, payload sin secretos, identificador de operación, respuesta, evento posterior y conciliación. Ejecutarlo solo después de elegir un producto que cubra el flujo aprobado. Los simuladores, si se usan, se etiquetarán como tales y no probarán la capacidad del proveedor.

[[PENDIENTE: confirmar productos, condiciones de acceso y capacidades con documentación completa; obtener autorización y ejecutar pruebas reproducibles.]]
