# INV-031 — Fuentes para cerrar decisiones del borrador

Consulta: 24-09-2026. Autor: Codex. Se contrasta la propuesta de integraciones de la entrega anterior; no se contactó a proveedores ni se obtuvieron accesos.

| Pregunta | Fuente primaria consultada | Hallazgo y decisión provisional |
| --- | --- | --- |
| ¿Split 1:1 está disponible en Chile? | [Mercado Pago, resumen](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/overview) | Chile está listado. Confirma el contraste previo; no acredita cuenta habilitada. |
| ¿Se pueden prometer tarjetas, liberación y custodia? | [Mercado Pago, integración](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/integration-configuration/integrate-marketplace) | Documenta Pro/API, descuento inicial de tarifa al vendedor, OAuth y restricción de dinero en cuenta. SUP-06 adopta lectura restrictiva. La página no acredita custodia ni garantía condicionada. |
| ¿Qué acceso exige? | [Mercado Pago, requisitos](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/prerequisites) | Publica KYC 6 y OAuth. Sigue faltando comprobar la habilitación particular del proyecto y de cada vendedor. |
| ¿Puede fijarse un precio API de firma? | [FirmaVirtual, API](https://firmavirtual.legal/servicios/api-firma-electronica) | Describe cobro por documento/contrato, planes y firmantes; acceso comercial mediante credenciales. No se obtuvo importe contractual. Mantener provisión y sensibilidad, no cotización inventada. |
| ¿Qué mecanismo puede proteger auditoría? | [Google Cloud, Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock) | Una política bloqueada impide reducir/quitar retención y borrar/reemplazar objetos antes del plazo; bloqueo irreversible. SUP-13 propone ensayarlo con eventos sintéticos mínimos; retención productiva y prueba siguen abiertas. |

Las fuentes amplían/precisan el diseño anterior. No sustituyen INV-026–029 ni convierten una tarifa pública de otro producto en precio contratado. La investigación permite redactar decisiones condicionadas sin esperar respuesta externa; la habilitación comercial sigue posterior.

## Búsquedas siguientes, con criterio de parada

1. Exportación del calculador y SKU de GCP Santiago para los recursos exactos del Anexo A: Cloud Run, Cloud SQL, Storage, red y respaldos. Capturar unidad, carga, región, fecha e impuestos separados. Sin SKU comparable, conservar provisión y rotularla.
2. Precios anunciados de ofertas por cada categoría/modalidad de INV-011: registrar precio final, duración, capacidad y fecha. Si no hay precio público, conservar «a cotizar» o un supuesto propio, nunca imputarlo al proveedor.
3. Tarifas particulares Split/firma/KYC y domicilio: una búsqueda pública termina al identificar que requieren cotización; pasar a V01–V03, sin repetir búsquedas como si fueran a producir un contrato.
4. SII/municipalidad: reutilizar fuentes primarias de INV-029 para normas generales. La web no determina por sí sola el régimen, el crédito fiscal o la aceptación del domicilio de EspaciGo.
