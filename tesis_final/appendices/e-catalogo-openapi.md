# ANEXO E: CATÁLOGO DE CONTRATOS DE INTERFAZ OPENAPI 3.0

Este anexo formaliza seis procedimientos operativos estandarizados (*runbooks*) para guiar la respuesta técnica ante contingencias críticas en la infraestructura de **espaciGo**.

---

## RB-01: Caída de Conectividad o Falla Crítica en Cloud SQL (PostgreSQL)
- **Identificador**: `RB-01-DB-FAILOVER`
- **Severidad**: P1 (Crítica)
- **RTO / RPO Objetivo**: RTO ≤ 30 min (conmutación y failover) / RPO ≤ 5 min (PITR con WAL)
- **Procedimiento**: Comprobar estado de la instancia primaria en GCP Console (`gcloud sql instances describe espacigo-db-prod`). Si el failover automático no se activa, forzar conmutación manual (`gcloud sql instances failover espacigo-db-prod`). Reiniciar instancias de Cloud Run para refrescar el pool `pgxpool` hacia la nueva IP primaria. Verificar endpoint `/health/ready` y consistencia de transacciones en curso.

---

## RB-02: Falla o Indisponibilidad de la Pasarela de Pagos (Mercado Pago)
- **Identificador**: `RB-02-PAYMENT-GATEWAY`
- **Severidad**: P2 (Alta)
- **RTO Objetivo**: RTO < 20 min (modo contingencia)
- **Procedimiento**: Abrir circuit breaker mediante configuración dinámica en Cloud Run. El frontend despliega banner informativo informando de intermitencia externa. Ampliar automáticamente el TTL de reservas pendientes de 15 a 45 minutos. Tras la recuperación del proveedor, ejecutar comando batch de conciliación de webhooks pendientes.

---

## RB-03: Compromiso de Seguridad, Fuga de Credenciales o Brecha de Datos Personales
- **Identificador**: `RB-03-SECURITY-BREACH`
- **Severidad**: P1 (Crítica — Regulatoria)
- **Marco Normativo**: Art. 14 sexies de la Ley N° 21.719 sobre Protección de Datos Personales.
- **Procedimiento**: Aislar inmediatamente los servicios afectados revocando credenciales y secretos en Secret Manager. Forzar la invalidación global de sesiones activas en la tabla `public.sesion`. Evaluar volumen, tipología de datos comprometidos y aplicar medidas de contención técnicas. Conforme al Art. 14 sexies de la Ley N° 21.719, reportar la vulneración a la Agencia de Protección de Datos Personales y a los titulares afectados sin dilación indebida (sin dilaciones indebidas y a la mayor brevedad posible) una vez confirmada la brecha, detallando la naturaleza del evento, posibles consecuencias y acciones correctivas implementadas.

---

## RB-04: Despliegue Fallido o Regresión Crítica en Producción (Rollback)
- **Identificador**: `RB-04-ROLLBACK-DEPLOY`
- **Severidad**: P2 (Alta)
- **Procedimiento**: Desviar el 100% del tráfico hacia la revisión anterior de Cloud Run de forma atómica (`gcloud run services update-traffic --to-revisions=PREVIOUS=100`). Si el fallo involucra migraciones DDL, evaluar script de compensación versionado con `cmd/dbmigrate`. Ejecutar pruebas de humo inmediatas.

---

## RB-05: Corrupción o Inconsistencia en Índices Geoespaciales PostGIS
- **Identificador**: `RB-05-POSTGIS-REINDEX`
- **Severidad**: P3 (Media)
- **Procedimiento**: Identificar publicaciones afectadas mediante consulta de validación de geometrías (`ST_IsValid`). Reconstruir el índice GiST en línea sin bloquear lecturas concurrentes (`REINDEX INDEX CONCURRENTLY idx_publicacion_ubicacion_gist`). Verificar latencia de búsqueda en catálogo.

---

## RB-06: Falla o Degradación en Resolución de Nombres DNS
- **Identificador**: `RB-06-DNS-FAILOVER`
- **Severidad**: P1 (Crítica)
- **Procedimiento**: Verificar estado de delegación NS y registros DNSSEC. Si el proveedor primario presenta caída global, conmutar registros hacia proveedor secundario administrado con TTL de 300 segundos. Purgar cachés de borde y validar propagación global con sondas externas.
