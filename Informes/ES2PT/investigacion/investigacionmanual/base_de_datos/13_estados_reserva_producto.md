# Máquina de estados de reserva para el producto completo

**Estado:** antecedente de análisis integrado en el [Anexo B v2](../../../anexos/B_diccionario_datos.md); no implementado. Usa los hitos de [RQF-113–177 y 228–231 de ES1](../../../../ES1PT/anexo_requerimientos_funcionales.md). La [fuente PlantUML](diagramas/07_estados_reserva_producto.puml) resume el camino principal; la fuente vigente de la figura del informe es [reserva_estados.puml](../../../diagramas/reserva_estados.puml). `pago.estado` y `disputa.estado` son entidades separadas; `reserva_transicion` registra actor, motivo, instante, versión y correlación de cada cambio.

## Estados y reglas

| Estado de reserva | Causa de entrada | Efecto sobre ocupación/liquidación |
| --- | --- | --- |
| `pendiente_de_pago` | Reserva/ocupación/outbox en un mismo commit | Intervalo retenido hasta `expira_en`; no hay pago confirmado. |
| `pagada` | Resultado de pago verificado o conciliado | Ocupación permanece; notificar al anfitrión. No implica firma ni aprobación. |
| `aprobada_host` | Decisión autorizada del arrendador | Puede generarse contrato; aún no habilita check-in. |
| `firma_parcial` | Primera firma válida | Esperar firmas exigidas; documentar rechazo o vencimiento. |
| `lista_para_checkin` | Todas las firmas y documento final confirmado | Habilitar operación solo en ventana autorizada. |
| `en_curso` | Check-in válido por participante autorizado | Registrar instante, ubicación y evidencia fotográfica. |
| `finalizada` | Check-out válido | Inicia período de recepción/reclamo y regla de liquidación. |
| `en_disputa` | Reclamo válido durante ventana de 24 h posterior al término | Bloquear liquidación; `disputa` separada guarda descargos/fallo. |
| `cerrada` | Liquidación conciliada tras plazo de gracia o resolución | No crear un segundo payout; evidencia tributaria según emisor aprobado. |
| `cancelada_*` | Pago rechazado/vencido, rechazo o falta de respuesta del anfitrión, falta de firma, cancelación de arrendatario conforme a política | Liberar ocupación transaccionalmente cuando la cancelación sea firme; conciliar reembolso/garantía. Causas se almacenan explícitamente. |

El **DDL preliminar anterior** omitía `en_disputa`, `cerrada` y la cancelación del arrendatario. El diccionario v2 ya define esos estados; las migraciones futuras deberán materializarlos y mantener reserva/disputa consistentes mediante un caso de uso transaccional. El `CHECK` por sí solo no valida el salto desde una fila anterior.

## Transiciones y actores

| Desde → hacia | Actor o fuente | Guarda y efecto esencial |
| --- | --- | --- |
| creación → `pendiente_de_pago` | Arrendatario autenticado / API | Cotización vigente, intervalo futuro, usuario autorizado, exclusión GiST sin conflicto. |
| `pendiente_de_pago` → `pagada` | Evento firmado o consulta de conciliación; adaptador simulado solo en pruebas locales | Proveedor confirma una operación idempotente; registrar `pago`, transición y outbox juntos. |
| `pendiente_de_pago` → `cancelada_por_pago` | Resultado rechazado o worker tras 15 min | Ante resultado financiero ambiguo, conciliar antes de liberar; RQF-119/120. |
| `pagada` → `aprobada_host` | Arrendador dueño del espacio | Decisión registrada antes de plazo; RQF-124/125. |
| `pagada` → `rechazada_arrendador` o `cancelada_por_vencimiento` | Arrendador o worker al cumplir 24 h | Reembolso/compensación idempotente y liberación coherente; RQF-126–129. |
| `aprobada_host` → `firma_parcial` → `lista_para_checkin` | Proveedor de firma verificado y caso de uso | Contrato/versiones y firmas de ambas partes; RQF-130–139. Si llegan juntas, salto directo aprobado explícitamente. |
| `aprobada_host`/`firma_parcial` → `cancelada_por_firma` | Worker al inicio sin firmas completas, o rechazo formal | Reembolso y liberación tras conciliación; RQF-140/141/202. |
| `lista_para_checkin` → `en_curso` | Arrendatario autorizado | Ventana de check-in, contrato final y foto obligatoria; RQF-143–149/203. |
| `en_curso` → `finalizada` | Arrendatario autorizado | Check-out y foto obligatoria; RQF-150–152/204. |
| `finalizada` → `en_disputa` | Parte habilitada dentro de ventana de reclamo | Reclamo/evidencia en `disputa`, bloqueo de payout; RQF-159–165. |
| `en_disputa` → `finalizada` | Administrador | Fallo motivado/conciliación de garantía; mantener historia de disputa y habilitar liquidación según resultado; RQF-166–171. |
| `finalizada` → `cerrada` | Proceso de liquidación confirmado | Tras 24 h sin reclamo, o disputa resuelta; registrar payout/documento según integración real; RQF-172–177/208. |
| Estado cancelable → `cancelada_arrendatario` | Arrendatario autorizado | Aplicar política snapshot, monto de devolución y proveedor; RQF-228–231. Estados cancelables exactos por política. |

El worker **no** avanza `confirmada/pagada → en_curso → finalizada` por reloj. El reloj habilita ventanas y dispara vencimientos; el uso requiere actos con evidencia. Tampoco existe una cola de espera FIFO en `ocupacion`. La confirmación de pago se puede recuperar por conciliación si falta webhook; no convertir el webhook en autoridad exclusiva de hecho externo.

## Restricciones adicionales sugeridas

- Índice único parcial: como máximo **una disputa abierta** por reserva, si ese es el contrato de negocio; varias disputas históricas pueden conservarse si los requisitos lo permiten.
- `reserva.version` aumenta en cada transición; `UPDATE ... WHERE id = ? AND version = ? AND estado = ?` verifica concurrencia optimista.
- `reserva_transicion` guarda `desde`, `hacia`, actor/tipo de actor, motivo, `ocurrio_en`, `correlacion`; la fila se inserta en el mismo commit del cambio. Si se decide usar `evento_auditoria`, dotarlo de estos campos/índices y evitar doble fuente de historia.
- `ocupacion.activo` cambia en el mismo commit que cancelación firme; una reserva cerrada conserva historial de intervalo. No usar predicados volátiles de `now()` dentro de un índice de exclusión.
- El saldo de garantía y la capacidad de retención/liberación del proveedor siguen sin verificar; representar `por_conciliar` y no atribuir fondos disponibles por un cambio de estado local.
