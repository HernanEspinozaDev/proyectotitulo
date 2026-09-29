# Diseño físico propuesto para PostgreSQL 18

## Contrato de tipos y restricciones

| Decisión | Propuesta | Justificación y prueba |
| --- | --- | --- |
| Claves | Mantener `uuid` v4 con `gen_random_uuid()` en la primera migración; evaluar v7 solo con medición. | No hay evidencia de que el índice PK sea cuello de botella. UUIDv7 existe en PostgreSQL 18, pero cambia semántica observable ([PostgreSQL, UUID](https://www.postgresql.org/docs/18/functions-uuid.html)). |
| Dinero | Objetivo CLP en pesos enteros `numeric(14,0)` para importes cobrables, tras migrar el `numeric(14,2)` textual actual; tasas/cálculos intermedios en `numeric` de escala suficiente, moneda y regla de redondeo versionadas. | Nunca `float`; probar límites, moneda y suma de desglose. El dominio `monto` actual no impone misma moneda entre pago y reserva. La comisión decidida es 3 % neto más IVA de la comisión cuando corresponda. |
| Tiempo | `timestamptz` para hechos, `tstzrange` `[)` para calendario; zona IANA de negocio si tarifa depende de hora local. | Intervalos adyacentes son válidos; rechazar rango vacío y extremos infinitos si el negocio exige duración finita ([PostgreSQL, rangos](https://www.postgresql.org/docs/18/rangetypes.html)). |
| Geografía | `geography(Point,4326)` más GiST existente, filtros `ST_DWithin` y área aproximada solo cuando aplique. | Coordenadas WGS84 y distancia en metros; no publicar coordenada exacta si la privacidad de la oferta exige zona gruesa ([PostGIS, ST_DWithin](https://postgis.net/docs/ST_DWithin.html)). |
| Categoría/estado | FK a categoría para `espacio`; `CHECK` para conjuntos de estados estables; tablas de referencia si cambian por producto. | Evita texto libre y despliegues de esquema para categorías; los `CHECK` no garantizan transiciones entre filas/estados. |
| Documento | Clave de objeto privada, hash, bytes, tipo validado, propietario único; binario fuera de DB. | Mantener FK y evitar URLs firmadas persistidas. |
| JSONB | Solo payload outbox versionado y metadatos flexibles validados. | No usarlo como sustituto de columnas financieras o campos filtrables obligatorios. |

El DDL actual tiene `CHECK (NOT isempty(intervalo))`; este predicado por sí solo no exige que ambos extremos sean finitos. Si las reservas deben tener inicio y fin determinados, añadir validación `NOT lower_inf(intervalo) AND NOT upper_inf(intervalo)` y límite de duración por categoría. La FK compuesta `ocupacion(reserva_id, espacio_id) → reserva(id, espacio_id)` ya expresa coherencia de espacio; revisar el índice único de soporte sobre `(id, espacio_id)` y el costo adicional. El `EXCLUDE USING gist (espacio_id WITH =, intervalo WITH &&) WHERE (activo)` es una fortaleza del diseño; no sustituirlo por un `SELECT` de disponibilidad seguido de `INSERT`, que permite carrera. Las restricciones y FK se documentan en la [referencia oficial de PostgreSQL](https://www.postgresql.org/docs/18/ddl-constraints.html).

## Índices como hipótesis de carga

Conservar PK, unicidades, GiST espacial y GiST generado por exclusión. Candidatos **por medir**:

- `reserva(espacio_id, inicio)` para agenda del anfitrión; `reserva(arrendatario_id, creada_en DESC)` para historial personal.
- `ocupacion(espacio_id, activo)` solo si el GiST de exclusión no satisface la consulta real; estudiar `WHERE activo` y rango. No duplicar índices por intuición.
- `pago(reserva_id, creado_en DESC)`, `contrato(reserva_id, version DESC)`, `disputa(reserva_id, estado)` si los flujos efectivamente consultan por esas columnas.
- `evento_proveedor(estado, recibido_en)` para conciliación y `outbox_evento(disponible_en, creado_en) WHERE publicado_en IS NULL`, que ya existe; revisar selectividad y crecimiento.
- FK referenciantes de alta frecuencia, incluida `documento` por propietario, tras medir lecturas y cascadas. PostgreSQL crea índice para PK/UNIQUE, pero **no automáticamente** para el lado referenciante de una FK ([PostgreSQL, restricciones](https://www.postgresql.org/docs/18/ddl-constraints.html)).

Cada índice candidato debe registrar consulta, cardinalidad, porcentaje de filas devueltas, plan antes/después, costo de escritura y responsable. Usar `EXPLAIN (ANALYZE, BUFFERS)` sobre datos sintéticos representativos; `ANALYZE` actualiza estadísticas del planificador. El `EXPLAIN ANALYZE` **ejecuta** la sentencia, por lo que escrituras se ensayan en transacción con rollback o entorno desechable ([PostgreSQL, EXPLAIN](https://www.postgresql.org/docs/18/sql-explain.html); [ANALYZE](https://www.postgresql.org/docs/18/sql-analyze.html)).

## Partición, vistas y extensiones

La primera versión **no particiona** `ocupacion` ni `reserva`: no hay volumen medido que lo justifique y particionar ocupación por fecha puede invalidar la exclusión de solapamientos entre particiones. PostgreSQL exige que PK/UNIQUE de una tabla particionada incluyan clave de partición; las exclusiones también la incluyen comparada por igualdad. Solo estudiar particiones en tablas de eventos/auditoría con crecimiento/retención medidos y una estrategia de unicidad compatible ([PostgreSQL, particionamiento](https://www.postgresql.org/docs/18/ddl-partitioning.html)). Vistas normales para lectura pueden incorporarse con permiso mínimo; materializadas requieren política de refresco y tolerancia a retraso documentadas. Extensiones iniciales: `postgis`, `btree_gist`; otras necesitan razón de negocio y soporte en Cloud SQL.

## Migraciones como fuente de verdad ejecutable

1. Guardar archivos SQL numerados en `db/migrations/` del futuro backend Go, con checksum, autor, fecha y razón. El estado de la versión se registra en tabla de migraciones. Aplicar una vez por ambiente y bloquear ejecución paralela.
2. Para cambio compatible: **expandir** (columna/tabla nueva y lectura dual si procede), desplegar aplicación compatible, rellenar datos con lotes pequeños y verificación, **contraer** solo tras observar ausencia de lectores antiguos. No asumir que un `down` revierte pérdida de datos.
3. Probar desde base vacía y desde copia sintética de la versión previa. Validar extensiones, collation, zona, roles y `search_path`; fijar nombre de esquema en SQL sensible y prohibir objetos temporales en `public` para usuarios de aplicación.
4. Planificar DDL de alto impacto en ventana y medir locks. Los índices grandes se crean con estrategia compatible con la herramienta de migración; `CREATE INDEX CONCURRENTLY` no corre dentro de una transacción común y tiene manejo de fallos propio.
5. Registrar versión de PostgreSQL/PostGIS y checksum de migraciones junto a revisión API. El texto SQL del Anexo B deja de ser la fuente operativa cuando existan migraciones verificadas; se sincroniza como resumen académico.

## Consultas parametrizadas

Conservar la decisión del backend oficial: `pgx/pgxpool` + `sqlc` para consultas estáticas y SQL parametrizado con allowlist de filtros/orden en búsqueda dinámica. El pool se comparte por proceso; cada caso de uso recibe explícitamente la transacción. Se establecen `statement_timeout`, tiempo máximo de adquisición del pool y tiempo de transacción según perfil medido, sin mantener un `BEGIN` abierto durante llamadas a proveedor externo.
