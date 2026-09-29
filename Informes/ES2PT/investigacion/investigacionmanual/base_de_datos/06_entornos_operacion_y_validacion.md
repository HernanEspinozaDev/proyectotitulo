# Entornos, operación y validación

## De Docker local a Cloud SQL

La conversación adjunta plantea PostgreSQL 18 local en Docker y destino Cloud SQL. Proponer una imagen **fijada por digest** de PostgreSQL 18 con PostGIS compatible (o imagen propia reproducible), servicio con `healthcheck`, volumen de datos explícito, red local no expuesta públicamente, usuario/DB de desarrollo y datos semilla **sintéticos**. Docker Compose contiene API Go y DB; se documentan comandos de arranque, migración, reseteo del volumen y backup local. Una imagen que solo dice `postgres:18` no incluye necesariamente PostGIS; la disponibilidad de `btree_gist`/PostGIS se comprueba al ejecutar migraciones. Los scripts de inicialización de la imagen se aplican al crear un volumen nuevo, no deben ser mecanismo de migración incremental ([Docker Official Image, postgres](https://hub.docker.com/_/postgres)). La conversación menciona Windows/Node como ejemplo genérico; el proyecto usa Go y el equipo trabaja en Linux, por lo que el diagrama local no debe atribuir Windows o Node a EspaciGo.

Cloud SQL usa la misma **versión mayor objetivo** y extensiones compatibles; fijar minor exacta no garantiza paridad permanente porque Cloud SQL gestiona mantenimiento. Registrar al desplegar `SHOW server_version`, extensiones y `postgis_full_version()` y ensayar el mismo conjunto de migraciones. La configuración propuesta separa dev/staging/producción, región Santiago, acceso privado cuando se confirme red/costo, SSL/conector autenticado, permisos mínimos, respaldos y PITR conforme a objetivos. Cloud SQL documenta [versiones](https://docs.cloud.google.com/sql/docs/postgres/db-versions), [extensiones](https://docs.cloud.google.com/sql/docs/postgres/extensions), [conexión desde Cloud Run](https://docs.cloud.google.com/sql/docs/postgres/connect-run) y [conectividad privada](https://docs.cloud.google.com/sql/docs/postgres/private-ip). La edición de Cloud SQL, HA y consumo deben reflejarse en Anexo A antes de escoger configuración; el presupuesto actual es escenario, no cotización contratada.

## Conexiones y capacidad

Definir presupuesto de conexiones: `instancias_max_API × max_conns_pool_API + conexiones_workers + migración + operaciones + margen < límite_cloud_sql`. Si los workers viven dentro de cada instancia API, evitar contar un pool adicional si comparten el mismo `pgxpool`; reservar conexiones para consultas largas y administración. Ajustar `MaxConns`, `MinConns`, vida útil, timeout de adquisición y máximo de Cloud Run tras PT-09/PT-10. Google documenta un límite de 100 conexiones Cloud SQL **por instancia de Cloud Run**, además del límite total de la instancia de base; no es objetivo de diseño ocuparlas todas ([Google Cloud, conectar Cloud Run](https://docs.cloud.google.com/sql/docs/postgres/connect-run)). Medir conexiones activas, espera de pool, CPU, memoria, I/O, espacio, locks, deadlocks, latencia p50/p95/p99 y edad de outbox.

## Recuperación, cambios y continuidad

RNF-010 plantea RPO ≤4 h y RTO ≤6 h. La configuración de backups/PITR debe elegirse para satisfacer esos objetivos **y probarse**; una opción activada no acredita el tiempo real. Restaurar a **instancia aislada** con versión/migración controlada, comprobar integridad y conteos, reconectar API de ensayo, medir desde inicio del incidente simulado hasta servicio funcional, documentar pérdida observada, costo y responsable. Incluir objetos GCS, secretos/configuración, outbox e inbox en el plan de continuidad. Cloud SQL ofrece procedimientos de [respaldo y restauración](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore). Mantener runbook de failover, pérdida de conexión, agotamiento de pool/disco y migración fallida; registrar decisión de rollback lógico o restauración, pues `down` de SQL no siempre recupera datos.

## Plan de verificación propuesto

| Fase | Evidencia exigible | Referencia ES2 |
| --- | --- | --- |
| Esquema vacío y migración | DDL aplicable en PostgreSQL 18/PostGIS local y Cloud SQL de ensayo; versión, checksum, extensiones y collation registrados | MD-10; Anexo B |
| Integridad | FK, dominio, snapshot, propiedad documental y estados inválidos rechazados; datos sintéticos | MD-01–MD-13 según caso |
| Concurrencia | Dos reservas solapadas: una confirma y la otra recibe conflicto; adyacentes aceptadas; bloqueo manual respeta exclusión | MD-02/PT-01/PT-02 |
| Fallos de integración | Webhook duplicado/falso/tardío, outbox duplicado, lease vencido, proveedor ambiguo, expiración con reinicio | PT-03/PT-04 |
| Seguridad/privacidad | Matriz aprobada, aislamiento entre identidades, exportación/supresión/restauración sin PII resucitada | PT-16 |
| Rendimiento | Perfil por categoría, planes antes/después de índice, 200/500 usuarios y 100 escrituras/s solo bajo carga definida | PT-09/PT-10 |
| Recuperación | Restauración en instancia aislada, RPO/RTO **medidos**, comparados contra 4 h/6 h | PT-11 |

No se ejecutan esas pruebas en esta investigación. En la sección 3.4 el último marcador dice MD-01–MD-12, pero el párrafo y Anexo B ya hablan de MD-01–MD-13; corregirlo al integrar. El informe también debe distinguir pruebas de integridad del modelo (MD) de casos de producto (PT) y guardar fecha, versión de esquema, datos, esperado, observado y responsable por ensayo.

## Plan de trabajo por incremento

1. **Local reproducible:** imagen PG18/PostGIS, Compose, migración núcleo, fixtures sintéticos y consultas Go.
2. **Invariantes:** categorías, unidad reservable, tarifas/snapshot, reserva/ocupación y concurrencia; completar diccionario antes de nuevas tablas.
3. **Integración:** inbox/outbox, pago simulado y sandbox, workers idempotentes, reconciliación.
4. **Nube de ensayo:** Terraform Cloud SQL/secretos/red/backups, misma migración y smoke con identidad de servicio.
5. **Operación:** carga, índices basados en planes, restauración, retención aprobada, evidencia para MD/PT y actualización académica del Anexo B.
