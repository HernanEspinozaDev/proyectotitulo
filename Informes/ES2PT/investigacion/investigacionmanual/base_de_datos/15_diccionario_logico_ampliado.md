# Diccionario lógico ampliado del producto completo

**Estado:** propuesta de diseño, no DDL ejecutado. Extiende las 17 entidades de negocio y `outbox_evento` del [Anexo B actual](../../../anexos/B_diccionario_datos.md) según [RQF de ES1](../../../../ES1PT/anexo_requerimientos_funcionales.md), la decisión de unidad exclusiva y el nuevo alcance de producto completo. Una entidad candidata se incorpora al conteo oficial solo cuando su definición, cardinalidades, campos y restricción queden aprobados e integrados. No se inventan datos de campo ni resultados de proveedor.

## Convenciones

- **PK/FK/UK**: clave primaria/foránea/única propuesta. Todo FK tiene acción de borrado explícita; por defecto se evita cascada en hechos contractuales y financieros.
- **CLP**: importes cobrables en pesos enteros, objetivo `numeric(14,0)` tras migración; tasas intermedias en decimal exacto. Cada snapshot registra moneda y versión de regla.
- **Instante**: `timestamptz`; **intervalo**: `tstzrange` semiabierto `[)`. La zona IANA del espacio se guarda para interpretar calendario civil y horarios locales.
- **PII**: dato personal o seudónimo vinculable; el campo se clasifica por finalidad y acceso. UUID no es por sí mismo anónimo.
- **E**: extensión necesaria para RQF del producto; **C**: decisión comercial/externa pendiente; **O**: capacidad opcional posterior de ES2. Son prioridades de modelado, no evidencia de implementación.

## 1. Oferta, categorías, cotización y reserva

| Entidad/estado | Identidad y relaciones | Campos mínimos propuestos | Invariantes y trazabilidad |
| --- | --- | --- | --- |
| `categoria_espacio` **E** | `codigo` PK; 1:N con `espacio` | nombre, descripción, activa, orden, versión de definición | Código estable; desactivar no elimina reservas históricas. RQF-068/098 y cartera completa ES1. |
| `espacio` **núcleo ampliado** | `id` PK; `arrendador_id` FK usuario; `categoria_codigo` FK | título, descripción, dirección privada, `ubicacion` PostGIS, `zona_horaria`, superficie, aforo cuando aplique, reglas de uso, estado | Una publicación = una unidad física exclusiva. Precio vigente se obtiene de `regla_tarifa`; no almacenar una segunda verdad mutable sin período de transición. RQF-060–093/195–198/221–224. |
| `regla_tarifa` **E** | `id` PK; `espacio_id` FK; UK `(espacio_id, version)` | unidad (hora/día/semana/mes/año/bloque), precio base CLP, duración mínima/máxima, `vigencia`, zona y política de cancelación/version | Regla publicada inmutable por versión; una regla base aplicable por espacio e instante bajo alcance acordado; evitar solapes de vigencia entre reglas equivalentes. Precio base >5.000 CLP según RQF-073. Semana/mes/año requieren calendario civil explícito. |
| `politica_cancelacion` **E** | `id` PK; versión; opcional FK espacio/catálogo | texto mostrado, reglas de ventana/reembolso estructuradas, vigencia, estado | Cambios crean versión; reserva guarda snapshot aceptado. RQF-223/228–231. La fórmula se acuerda antes de automatizar devolución. |
| `cotizacion` **E** | `id` PK; `espacio_id` FK; usuario opcional; `regla_tarifa_id` FK | inicio, fin, creada_en, expira_en, base_arriendo_clp, tasa_comision, comisión neta, IVA comisión aplicable, garantía prevista, total, desglose y versión de política | Se puede persistir como fila con TTL o token firmado con ID registrado; definir una única estrategia antes del DDL. Una cotización no retiene inventario. Recalcular/invalidar al cambiar regla; no usarla después de expirar. RQF-104–107. |
| `regla_comision` **E** | `id` PK; versión/UK por vigencia y ámbito | porcentaje_neto inicial **0,03**, base de cálculo, activa_desde/hasta, aprobador, motivo | Cambio sin redespliegue (RNF-020); una tasa aplicable por ámbito y fecha; reserva guarda tasa e importe. El IVA y tarifa de proveedor no son parte de este porcentaje. |
| `reserva` **núcleo ampliado** | `id` PK; FK espacio, arrendatario, cotización y reglas/versiones | inicio/fin, estado, precio de arriendo, tasa y comisión neta snapshot, IVA de comisión si aplica, impuestos de arriendo si corresponden, garantía, total comprador, moneda, política/condiciones snapshot, creada_en, `version` | Snapshot no se sobrescribe; estado sí cambia por transición válida. Un espacio exclusivo; no doblar reserva. RQF-104–129/228–231. No calcular 7 % por fórmula fija de proveedor. |
| `ocupacion` **núcleo** | PK; FK espacio; FK compuesta a reserva cuando exista | `intervalo`, tipo, activo, `expira_en`, motivo | `EXCLUDE USING gist (espacio_id WITH =, intervalo WITH &&) WHERE (activo)`; bloqueo manual y reserva comparten calendario. RQF-083–085/111–112. |
| `reserva_transicion` **E** | PK; FK reserva; UK `(reserva_id, version_nueva)` | desde, hacia, versión anterior/nueva, actor/tipo, motivo, ocurrio_en, correlación | Misma transacción que `reserva.estado`; si auditoría actual cubre plenamente esto, se puede ampliar esa tabla en vez de duplicar. Completar `en_disputa`, `cerrada` y cancelación del arrendatario. |

La cotización de primera etapa aplica **una regla base a todo el intervalo**; si cruza reglas incompatibles, se rechaza con explicación. El prorrateo por múltiples tramos es una extensión que exige algoritmo, desglose y pruebas propias. Todos los tipos de arriendo caben en el catálogo; sus reglas exactas de duración/capacidad se validan por categoría antes de activarlas.

## 2. Identidad, acceso y verificación

| Entidad/estado | Identidad y relaciones | Campos mínimos propuestos | Invariantes y trazabilidad |
| --- | --- | --- | --- |
| `usuario`/`rol_usuario` **núcleo ampliado** | PK UUID; roles compuestos por cuenta | correo único normalizado, hash_clave, estado, creado_en; roles | No contraseña plana; bloqueo y recuperación auditados. RQF-001–023. |
| `perfil_usuario` **E** | `usuario_id` PK/FK 1:1 | nombre visible, teléfono, documento legal mínimo según rol, foto como FK `documento` | Separar identidad de credencial; acceso propio y minimización. RQF-024–031. |
| `sesion` **E** | PK; FK usuario | hash de token/ID, emitida_en, expira_en, revocada_en, huella técnica mínima | Token real no se guarda en claro; cierre revoca sesión. RQF-018/023. |
| `token_accion` **E** | PK; FK usuario | propósito (correo/recuperación), hash, expira_en, consumido_en, intentos | Uso único, vencimiento y límite; no confundir con sesión. RQF-008/019–022/188. |
| `aceptacion_terminos` **E** | PK; FK usuario; FK versión documento | aceptada_en, versión exacta, canal/evidencia mínima | Historial de aceptación, no sobrescribir; RQF-186/187. |
| `cuenta_cobro` **E/C** | PK; FK arrendador; referencia de proveedor | titular verificado, banco/tipo/número mínimo protegido o token externo, estado y validación | Acceso restringido; no persistir credenciales secretas; RQF-032/033/189–191. El medio exacto depende de proveedor/tributación. |
| `verificacion`/`documento` **núcleo ampliado** | FK usuario, revisor y archivos | tipo KYC/KYB, estado, intento, resultado/proveedor_ref, motivo, fechas | Documento privado y minimizado; decisión manual con actor/motivo; RQF-038–059/192–194. |
| `vinculo_proveedor_vendedor` **E/C** | PK; FK arrendador; UK por proveedor/identificador externo | estado OAuth, identificador externo, secreto_ref a Secret Manager, creado_en, expira_en, renovado_en | No guardar token secreto en PostgreSQL; vigencia y revocación auditadas. Solo activar tras integración confirmada. |

## 3. Pago, proveedor, contrato y cierre

| Entidad/estado | Identidad y relaciones | Campos mínimos propuestos | Invariantes y trazabilidad |
| --- | --- | --- | --- |
| `pago`/`evento_proveedor` **núcleo ampliado** | FK reserva; UK de clave idempotente y evento externo por proveedor | tipo/intento/estado, importe/moneda, referencia externa, hora, verificación y conciliación | Webhook repetido no duplica efectos; respuesta ambigua queda `por_conciliar`. RQF-114–120/128/141/230. |
| `movimiento_financiero` **E/C** | PK; FK reserva y pago origen; UK externa según proveedor | tipo, dirección, importe CLP firmado o columnas débito/crédito (elegir una convención), moneda, beneficiario económico, instante, referencia externa | Insert-only para hechos confirmados; ajuste/reembolso nuevo registro. No llamarlo libro mayor balanceado sin cuentas y asientos dobles. Registrar tarifa MP observada, comisión EspaciGo e IVA por separado. |
| `garantia`/`liquidacion` **núcleo ampliado** | FK reserva | autorizado/capturado/liberado, neto arrendador observado, estado, instante/causa | No presumir escrow/preautorización/liberación real sin proveedor; disputa abierta bloquea liquidación. RQF-117/118/162/172–175/208. |
| `documento_tributario` **E/C** | PK; FK reserva o movimiento de comisión | emisor, receptor, tipo, folio/ref externa, base/IVA/total, estado, objeto PDF en `documento` | El emisor y documento de comisión/arriendo se validan con contador/SII; no duplicar voucher como venta. RQF-176/211. |
| `contrato`/`firma_contrato` **núcleo ampliado** | FK reserva y participantes | versión de plantilla, hash final, estado/firma/ref proveedor, fechas | Solo documento final firmado habilita check-in. Firmantes pertenecen a la reserva. RQF-130–142/202. |
| `operacion_arriendo` **núcleo ampliado** | FK reserva y actor | check-in/out/recepción, instante, ubicación permitida, comentario, evidencias FK | El worker no crea uso por hora; fotos obligatorias según RF. RQF-143–152/203–206. |
| `disputa` **núcleo ampliado** | FK reserva, reclamante, resolutor | estado, motivo, fallo, importe de garantía, fechas, evidencias/descargos | Una disputa abierta bloquea liquidación; decisión administrativa trazable. RQF-159–171/209–210. |

La ruta del dinero se modela con **importes por parte**, no con el “≈7 %” como constante. El comprador es **arrendatario**; el receptor del neto de arriendo es **arrendador**. `monto_total_comprador`, `comision_marketplace_neta`, `iva_comision_marketplace`, `cargo_proveedor_neto`, `iva_cargo_proveedor`, `neto_arrendador`, `fuente_importe` y la regla versionada de quién soporta económicamente el cargo deben poder conciliarse con el reporte real del proveedor. Los pagos a socios de la SpA quedan fuera del esquema operacional de reservas.

## 4. Comunicación, reputación, privacidad y analítica

| Entidad/estado | Identidad y relaciones | Campos mínimos propuestos | Invariantes y trazabilidad |
| --- | --- | --- | --- |
| `mensaje_reserva` **E** | PK; FK reserva y autor | cuerpo minimizado, creado_en, editado_en/estado | Solo participantes leen/escriben; retención propia. RQF-156–158. |
| `resena` **E** | PK; FK reserva, espacio y autor; UK por reserva/autor/tipo | nota, texto, estado publicación, fecha | Solo tras uso elegible; moderación registrada. RQF-153–155/181–182. |
| `reporte_resena` **E** | PK; FK reseña y denunciante | motivo, estado, decisión, administrador, fechas | Motivo obligatorio para ocultar; RQF-181/182/207. |
| `notificacion`/`entrega_notificacion` **E** | PK; FK destinatario y evento/recurso | plantilla/version, canal, estado, creada_en, enviada_en, intentos, error saneado | Reintentos idempotentes; no copiar documento/PII al outbox. RQF de avisos de cuenta, pago, firma, uso, disputa y cancelación. |
| `evento_auditoria` **núcleo ampliado** | PK; actor/servicio y recurso | acción, resultado, motivo, instante, correlación, origen mínimo | No se sustituye por outbox/log; acceso administrador auditado y exportación autorizada. RQF-178–185/212; RNF-017. |
| `solicitud_titular` **núcleo ampliado** | PK; FK usuario/responsable | derecho, identidad verificada, estado, decisión fundada, fechas y evidencia mínima | Matriz de retención por finalidad aún requiere revisión; no borrar hechos financieros en cascada. |
| `outbox_evento` **técnica ampliada** | PK evento estable; agregado tipo/id | versión_esquema, payload minimizado, disponible_en, intentos, lease_token/hasta, estado, publicado_en | Mismo commit del hecho de dominio; entrega repetida posible, consumidor deduplica. |
| `campana`/`derecho_reporte`/`respuesta_nps` **O** | FK espacio/usuario cuando aplique | período, pago/estado, permiso de consulta, respuesta voluntaria minimizada | Extensiones comerciales/analíticas de ES2 solo tras decisión y política de tratamiento; BigQuery no decide hechos operativos. |

## Reglas transversales de cierre del diccionario

1. **No duplicar verdad:** estado actual en entidad, historia en transición/auditoría, snapshot en reserva, tarifa vigente en tabla versionada. Una vista puede unirlos, no reemplazar integridad.
2. **Restricciones físicas:** PK/UK/FK/CHECK/EXCLUDE para invariantes de fila/conjunto; permisos y transiciones en casos de uso y pruebas. Añadir índices referenciantes solo según consultas y planes medidos.
3. **Borrado y retención:** ninguna cascada en reservas, pagos, contratos, disputas y evidencia. Para PII, documentar seudonimización, supresión fundada y comportamiento tras restauración, con plazos por categoría validados.
4. **Reproducibilidad:** migraciones PG18/PostGIS numeradas, diccionario con versión y diagramas derivados. El texto del Anexo B se actualizará tras cerrar estas definiciones y no se declarará ejecutado sin evidencia.
5. **Trazabilidad:** cada tabla nueva tendrá RQF/RNF/CU, dueño del dato, finalidad y caso MD/PT. El conteo de entidades y atributos se recalculará al consolidar el diccionario físico.
