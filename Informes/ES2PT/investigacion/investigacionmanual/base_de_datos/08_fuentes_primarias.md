# Fuentes primarias para profundizar la sección de datos

**Consulta:** 29-09-2026. En el informe usar el formato bibliográfico institucional y claves de `recursos/`; los enlaces de esta lista son materiales de trabajo. Cada hecho externo se debe atribuir directamente al proveedor/estándar. La inferencia específica para EspaciGo debe nombrarse como propuesta y someterse a prueba.

| Fuente primaria | Sustenta | No sustenta |
| --- | --- | --- |
| [PostgreSQL 18: restricciones](https://www.postgresql.org/docs/18/ddl-constraints.html) | PK, FK, `CHECK`, unicidad, exclusión y creación/no creación de índices asociados. | Que el DDL de EspaciGo se haya ejecutado. |
| [PostgreSQL 18: tipos de rango](https://www.postgresql.org/docs/18/rangetypes.html) | `tstzrange`, límites semiabiertos y operadores de solapamiento. | Duración aceptada de cada categoría. |
| [PostgreSQL 18: particionamiento](https://www.postgresql.org/docs/18/ddl-partitioning.html) | Restricciones de PK/UNIQUE/EXCLUDE con clave de partición. | Necesidad de particionar este piloto. |
| [PostgreSQL 18: funciones UUID](https://www.postgresql.org/docs/18/functions-uuid.html) | `gen_random_uuid`/`uuidv7()`. | Mejor rendimiento de UUIDv7 en EspaciGo sin medición. |
| [PostgreSQL 18: SELECT](https://www.postgresql.org/docs/18/sql-select.html) y [control de concurrencia](https://www.postgresql.org/docs/18/mvcc.html) | `FOR UPDATE SKIP LOCKED`, transacciones y aislamiento. | Exactamente una entrega de Pub/Sub. |
| [PostgreSQL 18: EXPLAIN](https://www.postgresql.org/docs/18/sql-explain.html), [ANALYZE](https://www.postgresql.org/docs/18/sql-analyze.html), [uso de índices](https://www.postgresql.org/docs/18/indexes-examine.html) | Planes, estadísticas e índices guiados por carga. | Cumplimiento de 2 s/100 escrituras/s sin pruebas. |
| [PostGIS: ST_DWithin](https://postgis.net/docs/ST_DWithin.html) | Filtro geográfico e índice espacial aprovechable según consulta. | Precisión o privacidad acordada para EspaciGo. |
| [Cloud SQL: versiones](https://docs.cloud.google.com/sql/docs/postgres/db-versions) y [extensiones](https://docs.cloud.google.com/sql/docs/postgres/extensions) | Soporte documentado para PostgreSQL 18/PostGIS. | Compatibilidad de la imagen local concreta ni costo contratado. |
| [Cloud SQL: conectar Cloud Run](https://docs.cloud.google.com/sql/docs/postgres/connect-run), [gestión de conexiones](https://docs.cloud.google.com/sql/docs/postgres/manage-connections) y [red privada](https://docs.cloud.google.com/sql/docs/postgres/private-ip) | Conectividad, pools/límites y opciones privadas. | Que la red, IAM o pool estén configurados. |
| [Cloud SQL: restaurar](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore) | Procedimiento y límites de recuperación administrada. | RPO 4 h/RTO 6 h logrados sin ensayo. |
| [Cloud SQL: ediciones](https://docs.cloud.google.com/sql/docs/postgres/choose-edition), [HA](https://docs.cloud.google.com/sql/docs/postgres/high-availability) y [PITR](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr) | PostgreSQL 18 en Enterprise/Enterprise Plus, disponibilidad y recuperación administrada. | Que Plus sea necesario o que backups garanticen RTO del proyecto. |
| [Mercado Pago: Split 1:1](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/integration-configuration/integrate-marketplace) | Reparto vendedor–marketplace y orden de descuento de la tarifa de proveedor. | Reparto nativo entre tres socios o tarifa contractual de EspaciGo. |
| [SII: IVA general](https://www.sii.cl/preguntas_frecuentes/impuestos_mensuales/001_130_0572.htm) y [conservación contable](https://www.sii.cl/preguntas_frecuentes/declaracion_renta/001_140_4628.htm) | Tasa general del IVA y respuesta referencial sobre conservación de libros/documentos. | IVA/retención universal para cada arriendo o titular. |
| [BCN: reglamento del redondeo en efectivo](https://www.bcn.cl/leychile/navegar?idNorma=1111243) y [Código de Comercio, SpA](https://www.bcn.cl/leychile/navegar?idNorma=1974&idParte=8725218) | Alcance del redondeo legal y marco societario. | Redondeo a decena para pago digital o dividendos automáticos mensuales. |
| [Docker Official Image: postgres](https://hub.docker.com/_/postgres) | Variables de inicialización, volúmenes y arranque local. | Inclusión de PostGIS en la imagen base. |
| [PlantUML: clases](https://plantuml.com/class-diagram), [secuencia](https://plantuml.com/sequence-diagram) y [despliegue](https://plantuml.com/deployment-diagram) | Sintaxis de las fuentes UML propuestas. | Integridad física de la base. |
| [OMG: UML 2.5.1](https://www.omg.org/spec/UML/2.5.1/) | Semántica general de diagramas UML. | Que un diagrama de clases sea por sí solo un modelo relacional completo. |
| [BCN: Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) | Texto legal y fecha de vigencia a verificar en fuente oficial. | Base jurídica/plazo particular de EspaciGo ni cumplimiento. |

## Evidencia interna que no se cita como fuente autor–año

- [Sección 3.4](../../../secciones/03_04_datos.md) y [Anexo B](../../../anexos/B_diccionario_datos.md): estado textual actual del informe.
- [Backend oficial](../../propuesta_backend_final.md): decisiones de Go, Cloud SQL, outbox y alcance de demo.
- [Anexo C](../../../anexos/C_casos_de_prueba.md): PT-01–PT-16 previstos.
- [INV-004](../../INV-004_modelado_y_datos.md): historia de un modelo anterior; no usar su recuento como estado actual.
- Conversación adjunta del usuario: motivación de vistas UML y PG18; no es fuente técnica primaria.
