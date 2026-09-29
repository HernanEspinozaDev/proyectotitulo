# Contrato entre el backend oficial y el diccionario de datos ES2

**Decisión del usuario, 29-09-2026:** la arquitectura planifica el producto completo; PostgreSQL/PostGIS y el monolito Go se diseñan juntos. La Ley 21.719 condiciona **el primer incremento**. El [Anexo B](../../../anexos/B_diccionario_datos.md) es el diccionario oficial de diseño y la [propuesta backend v1.2](../../../investigacion/propuesta_backend_final.md) fija módulos, transacciones, workers y almacenamiento. Ninguno acredita código ejecutado.

## Inventario coherente: 43 tablas de diseño

| Dueño lógico en Go | Tablas PostgreSQL | Número | Contrato de escritura |
| --- | --- | ---: | --- |
| `identity` | `usuario`, `rol_usuario`, `perfil_usuario`, `sesion`, `token_accion`, `version_terminos`, `aceptacion_terminos`, `verificacion`, `cuenta_cobro`, `vinculo_proveedor_vendedor` | 10 | Credenciales/tokens protegidos; rol por recurso; proveedor referenciado sin secreto en BD. |
| `catalog`, `search`, `booking` | `categoria_espacio`, `espacio`, `politica_cancelacion`, `tramo_cancelacion`, `regla_tarifa`, `regla_comision`, `cotizacion`, `reserva`, `ocupacion`, `reserva_transicion` | 10 | Catálogo para todas las categorías; snapshots; ocupación exclusiva y transición atómica. |
| `payments` | `pago`, `evento_proveedor`, `movimiento_financiero`, `garantia`, `liquidacion`, `documento_tributario` | 6 | Idempotencia, inbox, hechos inmutables y conciliación por componente; proveedor solo sandbox durante desarrollo. |
| `contracts`, `operations`, `disputes`, `storage` | `contrato`, `firma_contrato`, `operacion_arriendo`, `disputa`, `documento` | 5 | Actos/firmas autorizados, objeto privado con propietario FK, liquidación bloqueada por disputa. |
| `communications` | `mensaje_reserva`, `resena`, `reporte_resena`, `notificacion`, `entrega_notificacion` | 5 | Participantes y moderación; intentos de entrega durables. |
| `audit`, `platform`, `analytics` | `evento_auditoria`, `solicitud_titular`, `outbox_evento` | 3 | Derechos, trazabilidad y evento de dominio en mismo commit; BigQuery solo lectura analítica. |
| `promotions`, `analytics` | `campana`, `orden_promocion`, `derecho_reporte`, `respuesta_nps` | 4 | Derecho de métricas verificado en PostgreSQL; NPS voluntario; activación comercial posterior. |
| **Total** | | **43** | |

## Contratos que conectan módulos

1. **Publicación y disponibilidad.** `catalog` escribe `espacio` con FK de categoría y reglas versionadas. `search` consulta PostGIS/calendario sin retener espacio. `booking` inserta `reserva`, `ocupacion` y `outbox_evento` en un solo commit. La restricción GiST decide conflictos simultáneos, incluidos bloqueos manuales.
2. **Pago.** `payments` recibe una intención durable con clave idempotente, llama al adaptador fuera de la transacción local y procesa `evento_proveedor` autenticado. Una respuesta incierta queda por conciliar; cobro, comisión, IVA aplicable, tarifa externa y neto se desglosan. `booking` avanza solo con resultado confirmado. El plazo vencido se valida sincrónicamente y el worker del mismo monolito ejecuta limpieza recuperable.
3. **Contrato y uso.** `contracts` guarda versiones y firmas por participante; `operations` exige contrato/firma final para check-in. `disputes` bloquea `liquidacion` mientras un reclamo está abierto. El reloj habilita ventanas o vence esperas; no crea check-in/out por sí solo.
4. **Archivos.** `storage` guarda bytes en Cloud Storage privado y una fila `documento` con dueño FK y generación/hash. El perfil, publicación, verificación, contrato, operación, disputa, términos y documento tributario usan la misma política de acceso por propietario. No se guardan URL firmadas.
5. **Privacidad.** Cada caso de uso conoce finalidad y campos permitidos. `identity` y `audit` tramitan `solicitud_titular`; el resultado debe abarcar PostgreSQL, objetos GCS, analítica, copias y encargados. No se aplica `ON DELETE CASCADE` a hechos. La matriz del Anexo B se convierte en configuración/procedimiento ejecutable cuando se validen plazos y bases jurídicas, pero minimización, permisos y trazabilidad se implementan desde la primera migración/API.
6. **Analítica.** Los hechos de dominio salen por outbox a Pub/Sub y BigQuery con entrega repetible; las interacciones de alto volumen se publican directamente a Pub/Sub. `derecho_reporte` y titularidad se verifican en PostgreSQL antes de servir métricas. `evento_auditoria` no se sustituye por outbox ni por log técnico.

## Orden de migración y criterios de cierre

| Incremento | Migración/servicio previsto | Evidencia necesaria |
| --- | --- | --- |
| 1. Fundamento seguro | Catálogos, usuario/rol/perfil/sesión, documento privado, solicitudes de derechos, roles DB mínimos, auditoría y clasificación | SQL versionado PG18/PostGIS aplicado; controles de acceso y PT-16 con datos sintéticos. |
| 2. Oferta y reserva | Tarifas/políticas/comisión versionadas, cotización, reserva, ocupación y transición | Exclusión GiST y FK compuesta en pruebas concurrentes; todas las categorías cargables. |
| 3. Pago y formalización | Pago, inbox, movimientos, garantía/liquidación, contrato/firma y DTE | Sandbox/conciliación e idempotencia; documento tributario según contador y proveedor. |
| 4. Operación y comunicación | Check-in/out, disputa, chat, reseñas, notificaciones y objetos | Permisos por participante, historial, reclamación y restauración. |
| 5. Promoción y analítica | Campaña/orden/derecho, NPS, outbox→Pub/Sub→BigQuery | Aislamiento entre vendedores y retención/costo medidos antes de exposición. |

El orden de entrega es incremental, pero **las 43 tablas y sus relaciones quedan definidas como diseño del producto**. Solo se afirma implementación al aplicar migraciones y conservar evidencia fechada. Las únicas decisiones externas que no se fijan por inferencia son tarifa/capacidad efectiva de Mercado Pago, tratamiento tributario por componente, y base jurídica/plazo específico por finalidad. No suspenden el trabajo de protección de datos ni la definición de claves y restricciones.
