# INV-032 — Selección e inventario sugeridos para el borrador

Consulta: 24-09-2026. Autor: Codex. Completa documentalmente la comparación propuesta en ES1; no instala herramientas ni ejecuta benchmarks. Las puntuaciones de 2.1 son juicio ilustrativo SUP-04, no mediciones.

| Fuente primaria | Dato utilizable y límite |
| --- | --- |
| [Next.js, soporte](https://nextjs.org/support-policy) y [licencia del proyecto](https://github.com/vercel/next.js/blob/canary/license.md) | 16.x figura en soporte activo; licencia MIT. Selección objetivo, no versión instalada. |
| [Node.js, versiones](https://nodejs.org/en/about/previous-releases) | Política LTS y rama 24 para ejecución objetivo; fijar parche al instalar. |
| [Go, versión 1.26](https://go.dev/doc/go1.26) y [historial](https://go.dev/doc/devel/release) | Rama existente para el escenario; comprobar parche y soporte al construir. |
| [PostgreSQL, soporte](https://www.postgresql.org/support/versioning/) | Rama 17 soportada; mantener parche vigente. No inferir la versión de un servidor inexistente. |
| [Cloud SQL, extensiones](https://docs.cloud.google.com/sql/docs/postgres/extensions) | Tabla consultada lista PostGIS 3.5.2 con PostgreSQL 17 y btree_gist; disponibilidad particular por verificar. |
| [PostGIS, licencia](https://postgis.net/documentation/faq/gpl-license/) | GPLv2 para extensión; no confundir el uso mediante consultas con distribución de una modificación. |
| [Docker, acuerdo](https://www.docker.com/legal/docker-subscription-service-agreement/) y [página Personal](https://www.docker.com/products/personal/) | Hay diferencias de alcance entre información promocional y términos de uso consultados. No se afirma gratuidad contractual para tres integrantes coordinados. Proponer Engine en Linux y revisar licencias de las piezas elegidas; Desktop queda opcional y sin costo confirmado. |

Se propone Next.js/Go/PostgreSQL por continuidad y alcance, Cloud Run por menor operación manual y metodología incremental por incertidumbre de terceros. Las ventajas de velocidad de desarrollo o rendimiento no se han probado. La alternativa MySQL requiere cambiar RNF-038, independientemente de su puntuación. Hardware SUP-05 es una configuración objetivo, no un inventario levantado.
