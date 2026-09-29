# Estado del diseño de base de datos y próximos pasos

**Corte:** 29-09-2026. **Decisión vigente:** el [Anexo B v2](../../../anexos/B_diccionario_datos.md) define las 43 tablas del producto completo y la [propuesta backend v1.2](../../../investigacion/propuesta_backend_final.md) usa el mismo alcance, módulos, estados y límites de almacenamiento. La [matriz de correspondencia](17_contrato_datos_backend.md) permite revisar esa sincronización. Los documentos 01–16 conservan análisis y alternativas; cualquier mención suya al Anexo B de 17+1 entidades describe un estado anterior.

## Qué está definido

- PostgreSQL 18/PostGIS y `btree_gist` como objetivo para el monolito Go, con `pgx/pgxpool`, `sqlc` y migraciones SQL versionadas.
- Todas las categorías representadas por catálogo y cada `espacio` como unidad exclusiva; tarifas, cancelación y comisión versionadas; cotización y reserva con snapshots.
- Calendario único `ocupacion` con intervalo `[)`, FK coherente y exclusión GiST sobre ocupaciones activas; reserva/transición/outbox en commit local.
- Pago, webhook, movimiento financiero, garantía y liquidación separados; contrato, firmas, uso, disputa, comunicación, promoción y NPS con tablas definidas.
- Objetos binarios privados en GCS; PostgreSQL guarda metadatos y propietario; eventos de dominio por Outbox→Pub/Sub→BigQuery, telemetría masiva fuera de tablas operativas.
- Ley 21.719 **desde el primer incremento** como criterio de minimización, acceso, derechos, protección y retención por finalidad; PT-16 como ensayo futuro. La fecha de vigencia no aplaza este trabajo.
- Comisión neta inicial 3 % en regla versionada; el costo real de Split, IVA/documentos y neto del arrendador se registran por concepto y se verificarán con Mercado Pago/contador. No se fija una pérdida de 7 % como constante.

## Qué falta para pasar de diseño a implementación comprobada

1. Convertir el Anexo B en migraciones SQL numeradas, con PK/FK/UK/CHECK/EXCLUDE, roles DB, índices basados en consultas y carga de categorías. El DDL preliminar de 17+1 no es migración vigente.
2. Aplicar desde cero en PostgreSQL 18 local con PostGIS y comprobar las mismas migraciones en Cloud SQL de ensayo. Registrar versiones y errores; no declarar compatibilidad por lectura documental.
3. Ejecutar MD-01–MD-13 y PT aplicables, especialmente concurrencia de ocupación, expiración frente a webhook tardío, idempotencia, permisos, PT-16 y restauración. Ninguno se ha ejecutado.
4. Verificar con el responsable jurídico/privacidad la base y plazo por finalidad, y con contador/proveedor el documento tributario, IVA y las capacidades de pago. Las decisiones de diseño de minimización y control de acceso ya rigen mientras se obtiene esa evidencia.
5. Actualizar las figuras del capítulo III para que ilustren también las ampliaciones del modelo. Las figuras presentes muestran vistas legibles del núcleo; el Anexo B es la lista completa.
6. Regenerar Word y revisar APA/figuras solo al cerrar contenido, conforme al proceso de ES2. La salida del 24-09-2026 está desactualizada respecto de este diccionario.

El siguiente entregable técnico es la **primera migración PG18** y sus consultas/transacciones Go; el siguiente entregable académico es la revisión de figuras y trazabilidad con el diccionario ya integrado. No se añade un nuevo motor, servicio de workers ni herramienta de CDC.
