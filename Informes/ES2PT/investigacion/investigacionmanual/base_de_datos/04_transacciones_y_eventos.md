# Transacciones, concurrencia y eventos durables

## Invariantes transaccionales

La integridad de una reserva depende de una unidad reservable, un intervalo válido, un precio/política versionados, el estado permitido y una ocupación activa sin solape. La disponibilidad mostrada por la búsqueda es informativa; solo la inserción transaccional con restricción de exclusión decide. Dos solicitudes simultáneas pueden leer “libre”, pero exactamente una podrá insertar un intervalo incompatible. La aplicación captura la violación de exclusión y devuelve conflicto de disponibilidad, sin reintentar ciegamente otra operación financiera. Ver [PostgreSQL, restricciones de exclusión](https://www.postgresql.org/docs/18/ddl-constraints.html) y [rangos](https://www.postgresql.org/docs/18/rangetypes.html).

### Reserva propuesta

1. Validar identidad, rol y permiso sobre el recurso, duración/capacidad y regla de tarifa vigente. Calcular cotización determinista con versión y expiración.
2. Iniciar transacción corta. Verificar que la cotización sigue vigente y que la retención previa expiró según la regla de negocio. Crear `reserva` pendiente con snapshot, `ocupacion` activa con `expira_en` y evento outbox con el mismo ID de agregado. Confirmar los tres juntos.
3. Si la exclusión falla, hacer rollback completo e informar intervalo no disponible. Si hay timeout del cliente tras commit, recuperar por clave idempotente de la solicitud para no crear otra reserva.
4. Solo después del commit, llamar al adaptador de pago simulado o sandbox según fase. Persistir cada intento y resultado por una nueva transacción. Un efecto externo confirmado no se revierte con rollback local.
5. Procesar webhook autenticado en `evento_proveedor` bajo unicidad `(proveedor, evento_externo)`. Respuestas ambiguas pasan a `por_conciliar`; una repetición no debe duplicar cobro, reserva, reembolso ni liquidación.
6. Expiración de retención: worker reclama reservas vencidas, consulta el estado financiero cuando sea incierto y desactiva `ocupacion` en la misma transacción que cambia `reserva`. La validación sincrónica al intentar reservar impide depender solo de la cadencia del worker.

La reserva no debe autoconfirmarse por recepción no autenticada del webhook. El estado de proveedor y el de negocio son máquinas distintas. El producto completo conserva aprobación del anfitrión, firma, cancelación, check-in/out, reclamación y liquidación del Anexo B. Se propone un catálogo de transición autorizado por rol/actor, versión anterior y condición; el `CHECK estado IN (...)` solo limita valores posibles, no saltos.

## Inbox de proveedor y outbox analítica

| Mecanismo | Inserción | Clave de deduplicación | Garantía alcanzable |
| --- | --- | --- | --- |
| `evento_proveedor` (inbox) | Tras verificar autenticidad y sintaxis del mensaje | `(proveedor, evento_externo)`; si falta ID confiable, definir hash/ventana como política específica | Evita procesar dos veces el mismo identificador localmente; no certifica estado remoto. |
| `outbox_evento` | En el mismo commit del cambio de negocio | `id` del evento y `version_esquema` | Evita perder intención de publicación tras commit; entrega a Pub/Sub puede repetirse. |
| Consumidor BigQuery | Asíncrono; fuera de ruta de reserva | `event_id` estable | Debe deduplicar/agregar por contrato; BigQuery es analítica, no fuente de verdad de negocio. |

El worker interno del monolito puede reclamar lotes con `SELECT ... FOR UPDATE SKIP LOCKED`, establecer `lease_hasta`, `lease_token` (UUID o contador monotónico), `intentos` y `disponible_en`, hacer commit y luego publicar fuera de la transacción. Al confirmar, `UPDATE ... WHERE id = ? AND lease_token = ? AND publicado_en IS NULL`: un worker retrasado no marca un reclamo nuevo como propio. Tras respuesta ambigua de Pub/Sub se reenvía el **mismo ID**, nunca se supone exactamente una vez. Con reintentos máximos se marca `requiere_revision` y se alerta; no borrar la fila fallida sin diagnóstico. El comportamiento de `SKIP LOCKED` sirve para consumidores de colas, según [PostgreSQL, SELECT](https://www.postgresql.org/docs/18/sql-select.html).

## Concurrencia entre procesos y fallos

- El aislamiento predeterminado `READ COMMITTED` más restricciones físicas resuelve el solapamiento; si una regla agregada exige serialización adicional, documentar exactamente qué filas se bloquean y ensayar posibles deadlocks. No asumir que subir a `SERIALIZABLE` elimina el deber de reintentar abortos.
- Ordenar adquisición de locks por ID estable y mantener transacciones cortas. Usar control optimista `reserva.version` al editar estados, con condición `WHERE version = esperado`; verificar filas afectadas.
- Al reiniciar Cloud Run, goroutines y timers desaparecen. Solo la base conserva intención, vencimiento y progreso. Un mínimo de instancia y CPU fuera de solicitudes habilitan el worker previsto en backend, pero no garantizan ejecución continua ni exactamente una vez.
- Pago, documento en Cloud Storage y base requieren reconciliación/compensación; no escribir una transacción que espere HTTPS externo. Registrar intención y referencia externa, consultar estado remoto antes de un segundo intento cuando el resultado es ambiguo.
- Simular caída en cada frontera: antes/después de commit, después de publicar/antes de marcar, entre webhook y actualización, durante caducidad. Criterios de aceptación: no doble reserva, no doble efecto económico, outbox recuperable y auditoría de motivo. El worker expira o concilia; no genera check-in/check-out por pasar el tiempo.

## Frontera analítica

Solo eventos de dominio seleccionados viajan por outbox→Pub/Sub→BigQuery. Impresiones/clics de volumen alto siguen el diseño oficial de telemetría validada hacia Pub/Sub; no deben crear una fila operacional por vista. Definir versión de esquema, finalidad, minimización, retención, llegada tardía y agregación. Un reporte premium requiere autorización/entitlement en API antes de exponer cifras a cada vendedor.
