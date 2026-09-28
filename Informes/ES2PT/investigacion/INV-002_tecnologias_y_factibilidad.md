# INV-002 — Tecnologías y factibilidad

- Estado: investigación documental inicial y borrador; evaluación cuantitativa y económica abiertas.
- Fecha de consulta: 2026-09-23.
- Secciones: 2.1 y 2.2; impacto adicional en 3.3–3.7, 4.2 y 6.1–6.3.
- Base: informe ES1, Definición de arquitectura TI, Metodología de Trabajo y Plan de recursos; anexo C.

## Pregunta y método

¿Qué capacidades de las tecnologías propuestas en ES1 están sustentadas y qué falta medir para justificar su selección en EspaciGo? Se consultó documentación primaria de cada alternativa. Las comparaciones se limitan a las capacidades observadas; no se ejecutaron benchmarks, despliegues ni pruebas del producto. Los pesos del borrador son una propuesta de evaluación anterior a cualquier asignación de puntajes, pendiente de revisión del equipo.

## Registro de fuentes verificadas

Las claves siguientes están incorporadas a `referencias.bib`. Cuando la fecha editorial no se identifica con certeza se conserva la fecha de consulta sin inventar un año de publicación.

| Clave | Fuente primaria | Evidencia y límite |
| --- | --- | --- |
| es2nextcomponents | [Vercel: Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) | Composición entre servidor y cliente; no mide la latencia de EspaciGo |
| es2reactapp | [React: Creating a React App](https://react.dev/learn/creating-a-react-app) | Frameworks y decisiones requeridas al iniciar desde cero |
| es2goconcurrency | [The Go Authors: Effective Go](https://go.dev/doc/effective_go#concurrency) | Goroutines y canales; no compara rendimiento entre lenguajes |
| es2nodeeventloop | [Node.js: Don't Block the Event Loop](https://nodejs.org/learn/asynchronous-work/dont-block-the-event-loop) | Modelo de ejecución y riesgo de bloqueo; no demuestra inferioridad universal |
| es2pgtransactions | [PostgreSQL: Transactions](https://www.postgresql.org/docs/18/tutorial-transactions.html) | Atomicidad y rollback dentro de la transacción de base de datos |
| es2postgiswithin | [PostGIS: ST_DWithin](https://postgis.net/docs/ST_DWithin.html) | Consulta por distancia; unidades según geometry/geography |
| es2mysqlinnodb | [Oracle: Introduction to InnoDB](https://dev.mysql.com/doc/refman/8.4/en/innodb-introduction.html) | Transacciones e índices geoespaciales como alternativa a comparar |
| es2cloudrunoverview | [Google Cloud: What is Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) | Ejecución gestionada de aplicaciones/contenedores |
| es2computeinstances | [Google Cloud: Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances) | Configuración de máquinas, sistema operativo y almacenamiento |
| es2cloudrunpricing | [Google Cloud: Cloud Run pricing](https://cloud.google.com/run/pricing) | Facturación y costos separados de otros servicios; no es presupuesto de EspaciGo |
| es2cloudsqlpricing | [Google Cloud: Cloud SQL pricing](https://cloud.google.com/sql/pricing?hl=es-419) | Tarifas por vCPU, memoria, almacenamiento y respaldos; el costo depende de la región y la configuración |
| es2bigquerydml | [Google Cloud: GoogleSQL DML](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax) | Operaciones UPDATE/DELETE; elegir BigQuery por sí solo no garantiza inmutabilidad |
| es2dockeroverview | [Docker: What is Docker?](https://docs.docker.com/get-started/docker-overview/) | Imagen, contenedor y necesidad de persistencia separada |
| es2burgan2014 | [Burgan y Burgan: Choosing the right project approach](https://www.pmi.org/learning/library/choosing-right-project-approach-9346) | Comparación de enfoques predictivo, iterativo/incremental y adaptativo; ponencia de 2014, no nueva edición de PMBOK |

## Hallazgos y efecto en la base

| Hallazgo | Clasificación | Consecuencia para ES2 |
| --- | --- | --- |
| Next.js permite combinar renderizado de servidor e interacción de cliente | Confirma una capacidad | Mantener como candidato; medir comportamiento de búsqueda y reserva |
| Go y Node.js ofrecen modelos de concurrencia diferentes | Amplía la comparación | No repetir la superioridad de rendimiento de Go como si fuera un resultado medido |
| PostgreSQL y MySQL/InnoDB disponen de soporte transaccional; PostGIS documenta consultas por distancia | Amplía alternativas | Justificar selección por consultas, restricciones y esfuerzo real, no por negar capacidades de la alternativa |
| Cloud Run gestiona ejecución; Compute Engine permite elegir características de instancias | Confirma opciones de despliegue | Comparar carga operativa, capacidad y costo bajo igual escenario |
| Cloud SQL separa tarifas de cómputo, memoria, almacenamiento, alta disponibilidad y copias utilizadas | Confirma partidas de costo para una alternativa administrada de PostgreSQL | Elaborar una línea base de cotización; no inferir dimensionamiento suficiente para RNF-030 |
| BigQuery documenta modificación y eliminación mediante DML | Contradice la suficiencia de la selección para RNF-017 | Separar repositorio analítico de garantía de inmutabilidad; investigar controles y prueba de no alteración |
| La tarifa Cloud Run no incluye todos los servicios del sistema | Limita la conclusión económica | Desglosar BD, archivos, compilación, registro, red, logs y servicios externos |

Las consecuencias son inferencias de diseño para EspaciGo; las páginas consultadas no evalúan este proyecto. En particular, una operación atómica en PostgreSQL no acredita reversión automática de una operación realizada por un proveedor de pago externo.

## Cierre pendiente

- Revisar criterios/pesos; valorar alternativas con justificación por celda y sin convertir «no evaluado» en cero.
- Comparar consultas, carga y esfuerzo con versiones, entorno y datos controlados.
- Sustituir la línea base de costos de Cloud SQL por la configuración y región que apruebe el equipo; agregar cómputo, red, archivos, observabilidad, licencias, costos de integración y costo de oportunidad.
- Confirmar competencias, capacidad semanal, responsables y disponibilidad del equipo.
- Documentar decisión técnica y su impacto en requisitos; conservar las discrepancias de ES1 como antecedentes.

## Antecedente de cálculo pendiente de verificación regional

El cálculo anterior utilizó 1 vCPU, 4 GiB de RAM, 20 GiB SSD, 10 GiB de copias y 730 horas, con tarifas 0,0537 USD/vCPU-h, 0,0091 USD/GiB-h, 0,000232877 USD/GiB-h de SSD y 0,000109589 USD/GiB-h de copias. Su suma aritmética es USD 69,97/mes. **No se conserva evidencia suficiente de que esas tarifas correspondan a Santiago (`southamerica-west1`) y a esa configuración.** Se retira su condición de cotización regional verificada; no utilizarla para presupuestar ni puntuar alternativas.

La página de precios sigue siendo fuente primaria para identificar partidas, pero su selector regional requiere evidencia de selección. Para cerrar: registrar edición, recursos, disponibilidad, región, unidades, moneda, fecha y exportación de la cotización; sumar aplicación, red, logs, archivos, respaldos y operación [@es2cloudsqlpricing; @es2cloudrunpricing].

La evaluación comercial vigente se desarrolla en [INV-010](INV-010_infraestructura_y_formalizacion.md) y el Anexo A, con tarifas de referencia Iowa más una provisión regional hipotética. INV-009 es un ejemplo pedagógico anterior. La simulación no sustituye el TCO comparativo ni demuestra RNF-030 o RNF-009.
