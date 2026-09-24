# Diccionario de datos de ES2

Este Anexo B describe el **modelo lógico inicial propuesto**, derivado del núcleo transaccional de ES1. No es un esquema implementado ni cubre aún todo el catálogo de 236 RF. Los tipos orientan la posterior adaptación a PostgreSQL/PostGIS, exigida por RNF-038.

## Convenciones y alcance

- PK: clave primaria; FK: clave foránea. “No” en nulo implica obligatoriedad; “Sí” exige aplicar la condición indicada.
- Los UUID son identificadores internos propuestos. Fechas con zona se conservarán como instantes y se mostrarán en la zona del servicio, por confirmar.
- Los montos usan decimal exacto; moneda y reglas de redondeo deben validarse antes del DDL.
- Los campos sin valor inicial indicado no reciben un valor predeterminado implícito.
- Los estados nuevos se identifican como propuesta. El contrato de estados definitivo deberá mapear los nombres de ES1.
- Los roles de negocio coexisten. Una preferencia de uso no otorga privilegios administrativos.
- Relaciones y tipos constituyen decisiones de diseño ES2; sus cambios quedan registrados en el análisis de esta entrega.

## Entidades del núcleo

### usuario

Identidad de cuenta; perfil detallado y sesiones se ampliarán en otra iteración. Referencias de la base: RQF-001–018; RNF-013.

| Atributo | Tipo propuesto | Nulo | Claves, valores y reglas | Significado |
| --- | --- | --- | --- | --- |
| id | uuid | No | PK; generado al crear | Identificador interno |
| correo | text | No | Único sin distinguir mayúsculas; validar formato | Acceso y notificaciones |
| nombre | text | No | Sin valor por defecto | Identificación visible |
| hash_clave | text | No | Nunca contraseña plana; RNF-013 | Credencial derivada |
| estado | text | No | Inicial: correo pendiente; catálogo por validar | Situación de cuenta |
| creado_en | timestamptz | No | Instante de registro | Trazabilidad |

### rol_usuario

Permite coexistencia de Arrendador y Arrendatario, sin imponer roles excluyentes. Referencias de la base: RQF-213; anexo A.

| Atributo | Tipo propuesto | Nulo | Claves, valores y reglas | Significado |
| --- | --- | --- | --- | --- |
| usuario_id | uuid | No | FK usuario.id; parte de PK | Cuenta |
| rol | text | No | Parte de PK; catálogo de roles; privilegios administrativos restringidos | Rol autorizado |

### verificacion

Solicitud KYC/KYB y decisión automática o manual. Referencias de la base: RQF-038–060, 219–220; CU-11–14.

| Atributo | Tipo propuesto | Nulo | Claves, valores y reglas | Significado |
| --- | --- | --- | --- | --- |
| id | uuid | No | PK | Solicitud |
| usuario_id | uuid | No | FK usuario.id | Titular |
| tipo | text | No | KYC o KYB | Vía de verificación |
| estado | text | No | Pendiente, aprobada o rechazada; mapear estados ES1 | Estado de la solicitud |
| proveedor_ref | text | Sí | Identificador externo sin secretos | Correlación |
| revisor_id | uuid | Sí | FK usuario.id; requerir rol administrador si revisión manual | Decisor |
| motivo | text | Sí | Obligatorio en rechazo | Fundamento |
| resuelto_en | timestamptz | Sí | Obligatorio si finalizada | Fecha de decisión |

### espacio

Oferta del arrendador; unidad de publicación de la línea base. Referencias de la base: RQF-068–093, 221–224; CU-15–18.

| Atributo | Tipo propuesto | Nulo | Claves, valores y reglas | Significado |
| --- | --- | --- | --- | --- |
| id | uuid | No | PK | Publicación |
| arrendador_id | uuid | No | FK usuario.id; comprobar rol | Titular |
| titulo | text | No | Límites según catálogo RF | Título público |
| ubicacion | geography(Point,4326) | No | Índice espacial propuesto | Localización |
| tipo | text | No | Catálogo por definir | Tipo de inmueble |
| superficie_m2 | numeric(12,2) | No | Mayor que cero | Superficie |
| precio_base | numeric(14,2) | No | Regla de importe según RF; no float | Tarifa |
| unidad_tarifa | text | No | Hora, día o mes; reglas de cálculo por cerrar | Unidad |
| politica_cancelacion | text | No | Referencia/versionado por diseñar | Condiciones publicadas |
| estado | text | No | Borrador, Activa u Oculta; mapa a ES1 | Visibilidad |

### reserva

Solicitud transaccional con instantánea del precio aceptado. Referencias de la base: RQF-104–129, 140–152, 177, 227–231.

| Atributo | Tipo propuesto | Nulo | Claves, valores y reglas | Significado |
| --- | --- | --- | --- | --- |
| id | uuid | No | PK | Reserva |
| espacio_id | uuid | No | FK espacio.id | Espacio |
| arrendatario_id | uuid | No | FK usuario.id; identidad aprobada antes de reservar | Solicitante |
| inicio | timestamptz | No | Menor que fin; futuro al crear | Inicio |
| fin | timestamptz | No | Mayor que inicio | Término |
| estado | text | No | Inicial: Pendiente de Pago; transición validada | Situación del negocio |
| estadia | numeric(14,2) | No | Mayor o igual que cero | Precio acordado |
| comision | numeric(14,2) | No | Mayor o igual que cero | Comisión acordada |
| garantia_monto | numeric(14,2) | No | Mayor o igual que cero; no confundir con cobro efectivo | Garantía requerida |
| moneda | char(3) | No | Inicial CLP; sin conversión implícita | Moneda |
| politica_snapshot | text | No | Conservar condiciones aceptadas | Cancelación acordada |
| creada_en | timestamptz | No | Base del plazo de pago | Registro |
| version | integer | No | Inicial 1; control de actualización concurrente propuesto | Versión lógica |

### ocupacion

Calendario único para reservas y bloqueos manuales; propuesta de control de concurrencia. Referencias de la base: RQF-083–085, 111–112, 120, 200, 225–226.

| Atributo | Tipo propuesto | Nulo | Claves, valores y reglas | Significado |
| --- | --- | --- | --- | --- |
| id | uuid | No | PK | Intervalo |
| espacio_id | uuid | No | FK espacio.id | Espacio afectado |
| reserva_id | uuid | Sí | FK reserva.id; único cuando exista | Reserva causante |
| intervalo | tstzrange | No | Límites [inicio, fin); fin mayor que inicio | Período ocupado |
| tipo | text | No | Reserva o bloqueo manual | Origen |
| activo | boolean | No | Inicial true; requiere actualización transaccional | Participa en exclusión |
| expira_en | timestamptz | Sí | Retención temporal pendiente de pago | Vencimiento |
| motivo | text | Sí | Obligatorio para bloqueo manual | Justificación |

### pago

Intentos y resultados de cobro/reembolso, separados del estado de la reserva. Referencias de la base: RQF-114–119, 128, 230; RNF-012/028.

| Atributo | Tipo propuesto | Nulo | Claves, valores y reglas | Significado |
| --- | --- | --- | --- | --- |
| id | uuid | No | PK | Operación de pago |
| reserva_id | uuid | No | FK reserva.id | Reserva |
| proveedor | text | No | Producto por confirmar con el proveedor | Proveedor |
| tipo | text | No | Cobro o reembolso | Operación |
| clave_idempotencia | text | No | Única por proveedor y tipo | Evitar doble efecto |
| referencia_externa | text | Sí | Única por proveedor cuando exista | Operación remota |
| monto | numeric(14,2) | No | Mayor o igual que cero; moneda desde reserva | Importe |
| estado | text | No | Pendiente, confirmado, rechazado o por conciliar; propuesta | Resultado |
| creado_en | timestamptz | No | Registrar instante | Inicio |

### garantia

Autorización financiera diferenciada del pago de estadía. Referencias de la base: RQF-118, 174–175; CU-25/41/42.

| Atributo | Tipo propuesto | Nulo | Claves, valores y reglas | Significado |
| --- | --- | --- | --- | --- |
| id | uuid | No | PK | Intento de garantía |
| reserva_id | uuid | No | FK reserva.id | Reserva |
| referencia_externa | text | Sí | Proveedor y ámbito de unicidad por definir | Autorización |
| monto_autorizado | numeric(14,2) | No | Mayor o igual que cero | Cupo autorizado |
| monto_capturado | numeric(14,2) | No | Inicial 0; no superar autorizado | Compensación aplicada |
| estado | text | No | Pendiente, autorizada, capturada, liberada o vencida; propuesta | Situación |
| vence_en | timestamptz | Sí | Debe provenir del servicio real | Caducidad |

### evento_proveedor

Bandeja de eventos autenticados, con deduplicación y seguimiento. Referencias de la base: RNF-012/024/028; RQF-116, 136–139.

| Atributo | Tipo propuesto | Nulo | Claves, valores y reglas | Significado |
| --- | --- | --- | --- | --- |
| id | uuid | No | PK | Evento recibido |
| proveedor | text | No | Catálogo de adaptadores | Origen |
| evento_externo | text | No | Único junto con proveedor | Deduplicación |
| reserva_id | uuid | Sí | FK reserva.id; puede requerir conciliación | Correlación |
| hash_contenido | text | No | Digest; no reemplaza validación de firma | Integridad de evidencia |
| recibido_en | timestamptz | No | Instante de recepción | Fecha |
| estado | text | No | Recibido, procesado o error; propuesta | Procesamiento |
| intentos | integer | No | Inicial 0; no negativo | Control de reintentos |

### contrato

Versiones del contrato generado para la reserva. Referencias de la base: RQF-130–142; CU-29–32.

| Atributo | Tipo propuesto | Nulo | Claves, valores y reglas | Significado |
| --- | --- | --- | --- | --- |
| id | uuid | No | PK | Contrato |
| reserva_id | uuid | No | FK reserva.id | Reserva |
| version | integer | No | Única junto con reserva_id; mayor que cero | Versión |
| proveedor_ref | text | Sí | Correlación; sin credenciales ni enlace secreto | Servicio de firma |
| estado | text | No | Generado, Firma_Parcial o firmado; mapear ES1 | Estado |
| generado_en | timestamptz | No | Registrar generación | Fecha |

### firma_contrato

Participación y confirmación de cada firmante. Referencias de la base: RQF-134–139; CU-30.

| Atributo | Tipo propuesto | Nulo | Claves, valores y reglas | Significado |
| --- | --- | --- | --- | --- |
| contrato_id | uuid | No | FK contrato.id; parte de PK | Contrato |
| usuario_id | uuid | No | FK usuario.id; parte de PK; parte habilitada de la reserva | Firmante |
| estado | text | No | Pendiente, firmada o rechazada; propuesta | Respuesta |
| firmado_en | timestamptz | Sí | Solo tras confirmación verificada | Fecha |
| referencia_externa | text | Sí | Correlación con evento del proveedor | Evidencia |

### operacion_arriendo

Eventos de ingreso, salida y recepción del espacio. Referencias de la base: RQF-143–152, 203–206; CU-33/34/48.

| Atributo | Tipo propuesto | Nulo | Claves, valores y reglas | Significado |
| --- | --- | --- | --- | --- |
| id | uuid | No | PK | Evento de uso |
| reserva_id | uuid | No | FK reserva.id; único junto con tipo | Reserva |
| actor_id | uuid | No | FK usuario.id; validar participación | Autor |
| tipo | text | No | Check-in, check-out o recepción | Acción |
| fecha | timestamptz | No | Validar orden temporal y fecha de inicio | Instante |
| ubicacion | geography(Point,4326) | Sí | Obligatoria donde lo exige el RF | Localización |
| observaciones | text | Sí | Aplicar límite de negocio por definir | Descripción |

### disputa

Reclamo y resolución administrativa; detalle documental en documento. Referencias de la base: RQF-159–171, 209–210; CU-39–41.

| Atributo | Tipo propuesto | Nulo | Claves, valores y reglas | Significado |
| --- | --- | --- | --- | --- |
| id | uuid | No | PK | Disputa |
| reserva_id | uuid | No | FK reserva.id | Reserva |
| reclamante_id | uuid | No | FK usuario.id; arrendador de la reserva | Reclamante |
| descripcion | text | No | Obligatoria | Motivo |
| estado | text | No | Abierta o Resuelta; estados intermedios por definir | Situación |
| abierta_en | timestamptz | No | Validar ventana de 24 h | Fecha |
| resolutor_id | uuid | Sí | FK usuario.id; rol administrador | Responsable del fallo |
| fallo | text | Sí | Obligatorio al resolver; conservar motivo | Decisión |
| deduccion | numeric(14,2) | Sí | Entre 0 y garantía; obligatoria si corresponde | Compensación |

### liquidacion

Cierre financiero sujeto a ausencia de disputa pendiente. Referencias de la base: RQF-172–177, 208, 211; CU-42.

| Atributo | Tipo propuesto | Nulo | Claves, valores y reglas | Significado |
| --- | --- | --- | --- | --- |
| id | uuid | No | PK | Liquidación |
| reserva_id | uuid | No | FK reserva.id; único | Reserva |
| clave_idempotencia | text | No | Única; alcance del proveedor por verificar | Evitar doble pago |
| neto_arrendador | numeric(14,2) | No | Derivado de importes y decisión; no negativo | Transferencia |
| estado | text | No | Pendiente, confirmada o por conciliar; propuesta | Resultado |
| referencia_externa | text | Sí | Operación remota | Correlación |
| confirmada_en | timestamptz | Sí | Solo tras evidencia de éxito | Fecha |

### documento

Metadatos y vínculo a archivo restringido; nunca contenido binario en el informe. Referencias de la base: RQF-074–076, 137, 145, 151, 161, 165, 211; RNF-014/041–043.

| Atributo | Tipo propuesto | Nulo | Claves, valores y reglas | Significado |
| --- | --- | --- | --- | --- |
| id | uuid | No | PK | Archivo |
| espacio_id | uuid | Sí | FK espacio.id; uno de los seis propietarios | Galería |
| verificacion_id | uuid | Sí | FK verificacion.id; uno de los seis propietarios | Antecedente de identidad |
| contrato_id | uuid | Sí | FK contrato.id; uno de los seis propietarios | Contrato generado/firmado |
| reserva_id | uuid | Sí | FK reserva.id; uno de los seis propietarios | Evidencia o comprobante |
| disputa_id | uuid | Sí | FK disputa.id; uno de los seis propietarios | Reclamo o descargo concreto |
| operacion_arriendo_id | uuid | Sí | FK operacion_arriendo.id; uno de los seis propietarios | Evidencia de ingreso, salida o recepción |
| categoria | text | No | Galería, identidad, contrato, check-in, check-out, reclamo, descargo o boleta | Propósito |
| clave_objeto | text | No | Única; referencia interna sin URL pública | Almacenamiento |
| hash_sha256 | char(64) | No | Validar formato; digest no garantiza inmutabilidad | Integridad |
| bytes | bigint | No | Positivo; límites por categoría | Tamaño |
| autor_id | uuid | No | FK usuario.id; cuenta de servicio por definir si automático | Origen |
| creado_en | timestamptz | No | Fecha del archivo | Trazabilidad |

### evento_auditoria

Registro lógico de acciones; garantía física de inmutabilidad todavía pendiente. Referencias de la base: RQF-184–185; RNF-017/043.

| Atributo | Tipo propuesto | Nulo | Claves, valores y reglas | Significado |
| --- | --- | --- | --- | --- |
| id | uuid | No | PK | Evento |
| actor_id | uuid | Sí | FK usuario.id; nullable para eventos del sistema | Autor |
| reserva_id | uuid | Sí | FK reserva.id; opcional para otras acciones | Contexto |
| solicitud_titular_id | uuid | Sí | FK solicitud_titular.id; vincula la tramitación de derechos | Cumplimiento |
| accion | text | No | Catálogo de eventos por definir | Hecho |
| fecha | timestamptz | No | Instante del servidor | Momento |
| correlacion | text | No | Identificador de solicitud/evento | Rastreo |
| resumen | text | No | Sin contraseñas, tokens ni datos de tarjeta | Detalle minimizado |

### solicitud_titular

Registro de solicitudes de derechos sobre datos personales y de su respuesta. Corresponde a la fila de solicitudes de derechos de la matriz de tratamiento y permite conciliar la supresión con la conservación obligatoria sin borrar hechos financieros. El registro conserva la solicitud y su decisión, nunca el dato suprimido. Referencias de la base: RQF-034–037; RNF-018/026/029; Ley 21.719.

| Atributo | Tipo propuesto | Nulo | Claves, valores y reglas | Significado |
| --- | --- | --- | --- | --- |
| id | uuid | No | PK | Solicitud |
| usuario_id | uuid | No | FK usuario.id; titular identificado | Solicitante |
| tipo | text | No | Acceso, rectificación, supresión, oposición o portabilidad | Derecho ejercido |
| canal | text | No | Catálogo por definir (formulario o correo) | Vía de ingreso |
| identidad_verificada | boolean | No | Inicial false; obligatoria antes de resolver | Control antifraude |
| solicitada_en | timestamptz | No | Instante de recepción; base del plazo de respuesta | Plazo |
| estado | text | No | Recibida, en revisión, resuelta o rechazada; propuesta | Situación |
| responsable_id | uuid | Sí | FK usuario.id; rol administrador o encargado de privacidad | Tramitación |
| resultado | text | Sí | Entregado, rectificado, anonimizado, bloqueado o denegado por conservación | Decisión aplicada |
| motivo | text | Sí | Obligatorio al cerrar; fundamenta el rechazo o la conservación | Fundamento |
| resuelta_en | timestamptz | Sí | Obligatorio al cerrar | Fecha de cierre |

## Matriz de tratamiento de datos (Ley 21.719 y Ley 19.628)

Conforme a las leyes 21.719 y 19.628, esta matriz establece la **política de tratamiento y retención** aprobada para EspaciGo. Las obligaciones legales (como las tributarias) prevalecen sobre el borrado automático de RNF-026.

| Flujo o categoría | Base Legal y Finalidad | Acción al cierre o solicitud de Supresión (Derecho al Olvido) |
| --- | --- | --- |
| **Cuenta, perfil de usuario** | *Consentimiento*. Identificar al usuario, enviar notificaciones. | Supresión en ≤ 72 horas. Eliminación física de PII. |
| **Verificación externa de identidad** | *Ejecución de contrato*. Validar identidad para reducir fraude. | Supresión en ≤ 72 horas o al expirar la obligación legal vinculada. |
| **Cuenta bancaria / Medio de pago** | *Ejecución de contrato*. Liquidar o cobrar operaciones. | Supresión del medio de pago en 72 horas; registros de transacciones previas se conservan. |
| **Reservas, comisiones y pagos** | *Obligación legal (Tributaria)*. Registro contable. | **Conservación por 5 años**. Los registros se anonimizan (se borra el vínculo con PII del usuario) pero la transacción permanece inmutable. |
| **Contratos y firmas** | *Obligación legal (Civil/Comercial)*. Acreditar acuerdo y resolución de disputas. | **Conservación por 5 años** (RNF-042). |
| **Auditoría y registros técnicos** | *Interés legítimo*. Seguridad de la plataforma e incidentes. | Conservación minimizada por 5 años (RNF-043); no incluye datos personales directos (solo UUID). |
| **Solicitudes de derechos (ARCO)** | *Obligación legal (Ley 21.719)*. Trazabilidad de cumplimiento. | Conservación del registro de la solicitud y su respuesta, sin el dato original. |

La implementación debe comprobar que las vistas y exportaciones solo incluyan datos autorizados y que una solicitud no destruya evidencia financiera sujeta a conservación tributaria de 5 años, utilizando anonimización para conciliar la supresión de la identidad con la inmutabilidad transaccional. La solicitud y su respuesta se registran en `solicitud_titular`, que guarda la decisión y su fundamento sin conservar el dato suprimido.

## Reglas entre entidades

1. El espacio de una ocupación de reserva debe coincidir con el de la reserva. Proponer FK compuesta o control transaccional equivalente; una FK simple a reserva no basta.
2. Cada intervalo activo de ocupación debe excluir superposición para el mismo espacio. Usar un único calendario para bloqueos manuales y reservas. El vencimiento cambia explícitamente el estado activo; no se presupone un índice cuyo predicado dependa de la hora actual.
3. Una reserva pagada no equivale a contrato firmado. Habilitar ingreso solo al confirmar las firmas requeridas.
4. El usuario que firma debe ser parte de la reserva. La combinación contrato/usuario no demuestra por sí sola que estén todos los firmantes requeridos.
5. No liquidar con disputas abiertas. Importe, comisión, deducción y garantía deberán conciliarse con las operaciones confirmadas.
6. Documento debe tener exactamente un propietario entre espacio, verificación, contrato, reserva, disputa y operación de arriendo; la categoría y los permisos deben ser compatibles con ese propietario. Los dos últimos vínculos resuelven la asociación que faltaba entre una evidencia y su reclamo o su evento de uso.
7. Las claves y referencias externas tienen ámbito definido por proveedor. Los eventos sin firma válida no ingresan al procesamiento de negocio; registrar su rechazo sin almacenar secretos.
8. No usar borrado en cascada sobre hechos financieros o evidencia. Conciliar privacidad, anonimización y retención por categoría mediante la matriz anterior; la FK a usuario no resuelve por sí sola esa política.
9. Toda tarea que llama a un proveedor debe registrar su intención y resultado y tratar respuestas inciertas. Un rollback local no revierte automáticamente un efecto externo.
10. Una solicitud de titular se resuelve con decisión fundada y no borra hechos financieros ni documentos sujetos a conservación: la identidad se anonimiza y el registro de la solicitud y su respuesta se conserva según la matriz de tratamiento. El registro no almacena el dato suprimido.
11. El DDL propuesto no reemplaza la validación de negocio: las transiciones de estado, los permisos, la minimización y la política de conservación se aplican en la aplicación y en los procesos programados, no en las restricciones declaradas.

## Catálogo de estados y transiciones

Los literales de ES1 se conservan tal como aparecen en su anexo B. Los estados marcados como propuestos todavía no tienen literal en la base y deben acordarse antes de implementar; el DDL solo delimita los valores admitidos, no la legalidad de cada transición.

*Tabla. Estados por entidad.* <!--#tab:es2-datos-estados-->

| Entidad | Literales verificados en ES1 | Estados propuestos de ES2 | Referencia |
| --- | --- | --- | --- |
| usuario | — | Correo pendiente, activo, bloqueado, baja solicitada y anonimizado | RQF-001–018; CU-09/43 |
| verificacion | Pendiente, aprobada y rechazada | — | RQF-060, 219–220; CU-11–14 |
| espacio | Borrador, Activa y Oculta | — | RQF-082, 089; CU-18 |
| reserva | Pendiente de Pago, Pagada, Aprobada_Host, Firma_Parcial, Lista_Para_Checkin, En_Curso, Finalizada y Cancelada_Por_Pago | Rechazada por el arrendador, cancelada por vencimiento, cancelada por falta de firma y cancelación solicitada por el arrendatario, sin literal en la base | RQF-113–152; CU-51 |
| pago | — | Pendiente, confirmado, rechazado y por conciliar | RNF-012/028 |
| garantia | — | Pendiente, autorizada, capturada, liberada y vencida | RQF-118, 174–175 |
| contrato | Firma_Parcial (compartido con la reserva en la base) | Generado y anulado | RQF-130–139 |
| firma_contrato | — | Pendiente, firmada y rechazada | RQF-134–139 |
| operacion_arriendo | — | Check-in, check-out y recepción | RQF-143–152, 203–205 |
| disputa | — | Abierta, en descargos y resuelta | RQF-159–171 |
| liquidacion | — | Pendiente, confirmada y por conciliar | RQF-172–177 |
| evento_proveedor | — | Recibido, procesado, error y rechazado | RNF-012/024/028 |
| solicitud_titular | — | Recibida, en revisión, resuelta y rechazada | Ley 21.719; RNF-018/029 |

*Tabla. Transiciones previstas de la reserva.* <!--#tab:es2-datos-transiciones-->

| Desde | Hacia | Disparador o condición | Referencia |
| --- | --- | --- | --- |
| Pendiente de Pago | Pagada | Confirmación del proveedor de pago | RQF-116 |
| Pendiente de Pago | Cancelada_Por_Pago | Rechazo del cobro o 15 minutos sin pago (T1) | RQF-119/120 |
| Pagada | Aprobada_Host | Aprobación del arrendador | RQF-124/125 |
| Pagada | Rechazada por el arrendador | Rechazo fundado con reembolso total | RQF-126–128 |
| Pagada | Cancelada por vencimiento | 24 horas sin respuesta del arrendador (T2) | RQF-129 |
| Aprobada_Host | Firma_Parcial | Primera firma confirmada | RQF-136 |
| Firma_Parcial | Lista_Para_Checkin | Todas las firmas confirmadas y contrato almacenado | RQF-137/138 |
| Firma_Parcial | Cancelada por falta de firma | Fecha de inicio alcanzada sin firmas completas (T3) | RQF-140/141 |
| Lista_Para_Checkin | En_Curso | Check-in registrado | RQF-148 |
| En_Curso | Finalizada | Check-out registrado | RQF-152 |
| Cualquier estado previo a En_Curso | Cancelación solicitada por el arrendatario | Cancelación de una reserva vigente | CU-51 |

Las transiciones anteriores se validan en la aplicación: una restricción de dominio no impide un salto de estado. Tampoco se declara que el proveedor financiero permita revertir un cobro confirmado; ese efecto se trata por conciliación.

## Permisos y accesos por rol

*Tabla. Permisos propuestos por rol.* <!--#tab:es2-datos-permisos-->

| Rol | Alcance | Operaciones permitidas | Restricciones propuestas |
| --- | --- | --- | --- |
| Visitante sin sesión | Catálogo público | Buscar, consultar detalle y leer reseñas | Sin chat, reservas ni datos de terceros |
| Usuario Registrado | Cuenta propia | Perfil, cuenta bancaria, contraseña y baja de cuenta | Solo sus propios registros |
| Arrendatario | Reservas propias | Reservar, pagar, firmar, chatear, reseñar, registrar check-in y check-out, cancelar y reclamar | Sin acceso a la resolución de disputas ni a publicaciones ajenas |
| Arrendador | Espacios y solicitudes propias | Publicar, galería, calendario, resolver solicitudes, firmar, confirmar recepción, reportar reseña y reclamar | Sin acceso a los datos de pago completos del arrendatario |
| Administrador | Plataforma | Revisión manual, bloqueo de cuentas, moderación, resolución de disputas, reportes y auditoría | Sin rol comercial; cada acción exige motivo registrado |
| Cuenta de servicio (propuesta) | Procesos automáticos | Generar contrato, registrar eventos, ejecutar temporizadores y anonimización | Sin credenciales interactivas; su diseño sigue pendiente |

Los permisos se aplican en la API y en las vistas de consulta; el DDL propuesto no define roles de base de datos ni políticas de fila. La consulta de auditoría de CU-46 queda restringida al Administrador, y la minimización de RNF-018/029 debe comprobarse en cada exportación. Si el equipo adopta seguridad a nivel de fila, su alcance se decidirá antes de implementar.

## DDL propuesto

El siguiente texto es una **propuesta no ejecutada** para PostgreSQL 16 o superior con PostGIS y `btree_gist`, según RNF-038. No crea datos, no reemplaza la validación del equipo y no se ha aplicado en ningún servidor. Su revisión fue textual y de coherencia: 17 tablas corresponden a las 17 entidades del diccionario, toda clave foránea apunta a una tabla declarada y los paréntesis y terminadores están equilibrados.

```sql
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS btree_gist;

CREATE DOMAIN monto AS numeric(14,2) CHECK (VALUE >= 0);
CREATE DOMAIN monto_estricto AS numeric(14,2) CHECK (VALUE > 0);
CREATE DOMAIN hash_hex AS char(64) CHECK (VALUE ~ '^[0-9a-f]{64}$');

CREATE TABLE usuario (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    correo text NOT NULL,
    nombre text NOT NULL,
    hash_clave text NOT NULL,
    estado text NOT NULL DEFAULT 'correo_pendiente'
        CHECK (estado IN ('correo_pendiente','activo','bloqueado','baja_solicitada','anonimizado')),
    creado_en timestamptz NOT NULL DEFAULT now()
);
CREATE UNIQUE INDEX usuario_correo_unico ON usuario (lower(correo));

CREATE TABLE rol_usuario (
    usuario_id uuid NOT NULL REFERENCES usuario(id),
    rol text NOT NULL CHECK (rol IN ('arrendador','arrendatario','administrador')),
    PRIMARY KEY (usuario_id, rol)
);

CREATE TABLE verificacion (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    usuario_id uuid NOT NULL REFERENCES usuario(id),
    tipo text NOT NULL CHECK (tipo IN ('KYC','KYB')),
    estado text NOT NULL CHECK (estado IN ('pendiente','aprobada','rechazada')),
    proveedor_ref text,
    revisor_id uuid REFERENCES usuario(id),
    motivo text,
    creada_en timestamptz NOT NULL DEFAULT now(),
    resuelto_en timestamptz,
    CONSTRAINT verificacion_rechazo_fundado CHECK (estado <> 'rechazada' OR motivo IS NOT NULL),
    CONSTRAINT verificacion_cierre_coherente CHECK ((estado = 'pendiente') = (resuelto_en IS NULL))
);

CREATE TABLE espacio (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    arrendador_id uuid NOT NULL REFERENCES usuario(id),
    titulo text NOT NULL,
    ubicacion geography(Point,4326) NOT NULL,
    tipo text NOT NULL,
    superficie_m2 numeric(12,2) NOT NULL CHECK (superficie_m2 > 0),
    precio_base monto_estricto NOT NULL,
    unidad_tarifa text NOT NULL CHECK (unidad_tarifa IN ('hora','dia','mes')),
    politica_cancelacion text NOT NULL,
    estado text NOT NULL DEFAULT 'borrador' CHECK (estado IN ('borrador','activa','oculta')),
    creado_en timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX espacio_ubicacion_gix ON espacio USING gist (ubicacion);

CREATE TABLE reserva (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    espacio_id uuid NOT NULL REFERENCES espacio(id),
    arrendatario_id uuid NOT NULL REFERENCES usuario(id),
    inicio timestamptz NOT NULL,
    fin timestamptz NOT NULL,
    estado text NOT NULL DEFAULT 'pendiente_de_pago'
        CHECK (estado IN ('pendiente_de_pago','pagada','aprobada_host','rechazada_arrendador',
                          'cancelada_por_pago','cancelada_por_vencimiento','cancelada_por_firma',
                          'firma_parcial','lista_para_checkin','en_curso','finalizada')),
    estadia monto NOT NULL,
    comision monto NOT NULL,
    garantia_monto monto NOT NULL,
    moneda char(3) NOT NULL DEFAULT 'CLP',
    politica_snapshot text NOT NULL,
    creada_en timestamptz NOT NULL DEFAULT now(),
    version integer NOT NULL DEFAULT 1 CHECK (version > 0),
    CONSTRAINT reserva_intervalo_valido CHECK (fin > inicio),
    CONSTRAINT reserva_id_espacio_unico UNIQUE (id, espacio_id)
);

CREATE TABLE ocupacion (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    espacio_id uuid NOT NULL REFERENCES espacio(id),
    reserva_id uuid,
    intervalo tstzrange NOT NULL,
    tipo text NOT NULL CHECK (tipo IN ('reserva','bloqueo_manual')),
    activo boolean NOT NULL DEFAULT true,
    expira_en timestamptz,
    motivo text,
    CONSTRAINT ocupacion_reserva_espacio_coherente
        FOREIGN KEY (reserva_id, espacio_id) REFERENCES reserva (id, espacio_id),
    CONSTRAINT ocupacion_intervalo_no_vacio CHECK (NOT isempty(intervalo)),
    CONSTRAINT ocupacion_motivo_bloqueo CHECK (tipo <> 'bloqueo_manual' OR motivo IS NOT NULL),
    CONSTRAINT ocupacion_reserva_coherente CHECK ((tipo = 'reserva') = (reserva_id IS NOT NULL)),
    CONSTRAINT ocupacion_sin_solape EXCLUDE USING gist (espacio_id WITH =, intervalo WITH &&) WHERE (activo)
);
CREATE UNIQUE INDEX ocupacion_reserva_unica ON ocupacion (reserva_id) WHERE (reserva_id IS NOT NULL);

CREATE TABLE pago (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    reserva_id uuid NOT NULL REFERENCES reserva(id),
    proveedor text NOT NULL,
    tipo text NOT NULL CHECK (tipo IN ('cobro','reembolso')),
    clave_idempotencia text NOT NULL,
    referencia_externa text,
    monto monto NOT NULL,
    estado text NOT NULL CHECK (estado IN ('pendiente','confirmado','rechazado','por_conciliar')),
    creado_en timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT pago_idempotencia_unica UNIQUE (proveedor, tipo, clave_idempotencia),
    CONSTRAINT pago_referencia_unica UNIQUE (proveedor, referencia_externa)
);

CREATE TABLE garantia (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    reserva_id uuid NOT NULL REFERENCES reserva(id),
    referencia_externa text,
    monto_autorizado monto NOT NULL,
    monto_capturado monto NOT NULL DEFAULT 0,
    estado text NOT NULL CHECK (estado IN ('pendiente','autorizada','capturada','liberada','vencida')),
    vence_en timestamptz,
    CONSTRAINT garantia_captura_tope CHECK (monto_capturado <= monto_autorizado)
);

CREATE TABLE evento_proveedor (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    proveedor text NOT NULL,
    evento_externo text NOT NULL,
    reserva_id uuid REFERENCES reserva(id),
    hash_contenido hash_hex NOT NULL,
    recibido_en timestamptz NOT NULL DEFAULT now(),
    estado text NOT NULL DEFAULT 'recibido'
        CHECK (estado IN ('recibido','procesado','error','rechazado')),
    intentos integer NOT NULL DEFAULT 0 CHECK (intentos >= 0),
    CONSTRAINT evento_proveedor_unico UNIQUE (proveedor, evento_externo)
);

CREATE TABLE contrato (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    reserva_id uuid NOT NULL REFERENCES reserva(id),
    version integer NOT NULL CHECK (version > 0),
    proveedor_ref text,
    estado text NOT NULL CHECK (estado IN ('generado','firma_parcial','firmado','anulado')),
    generado_en timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT contrato_version_unica UNIQUE (reserva_id, version)
);

CREATE TABLE firma_contrato (
    contrato_id uuid NOT NULL REFERENCES contrato(id),
    usuario_id uuid NOT NULL REFERENCES usuario(id),
    estado text NOT NULL CHECK (estado IN ('pendiente','firmada','rechazada')),
    firmado_en timestamptz,
    referencia_externa text,
    PRIMARY KEY (contrato_id, usuario_id),
    CONSTRAINT firma_fecha_coherente CHECK ((estado = 'firmada') = (firmado_en IS NOT NULL))
);

CREATE TABLE operacion_arriendo (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    reserva_id uuid NOT NULL REFERENCES reserva(id),
    actor_id uuid NOT NULL REFERENCES usuario(id),
    tipo text NOT NULL CHECK (tipo IN ('check_in','check_out','recepcion')),
    fecha timestamptz NOT NULL DEFAULT now(),
    ubicacion geography(Point,4326),
    observaciones text,
    CONSTRAINT operacion_arriendo_unica UNIQUE (reserva_id, tipo)
);

CREATE TABLE disputa (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    reserva_id uuid NOT NULL REFERENCES reserva(id),
    reclamante_id uuid NOT NULL REFERENCES usuario(id),
    descripcion text NOT NULL,
    estado text NOT NULL DEFAULT 'abierta' CHECK (estado IN ('abierta','en_descargos','resuelta')),
    abierta_en timestamptz NOT NULL DEFAULT now(),
    resolutor_id uuid REFERENCES usuario(id),
    fallo text,
    deduccion monto,
    resuelta_en timestamptz,
    CONSTRAINT disputa_resolucion_fundada
        CHECK (estado <> 'resuelta' OR (fallo IS NOT NULL AND resolutor_id IS NOT NULL))
);

CREATE TABLE liquidacion (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    reserva_id uuid NOT NULL REFERENCES reserva(id) UNIQUE,
    clave_idempotencia text NOT NULL UNIQUE,
    neto_arrendador monto NOT NULL,
    estado text NOT NULL CHECK (estado IN ('pendiente','confirmada','por_conciliar')),
    referencia_externa text,
    confirmada_en timestamptz,
    CONSTRAINT liquidacion_confirmacion CHECK ((estado = 'confirmada') = (confirmada_en IS NOT NULL))
);

CREATE TABLE solicitud_titular (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    usuario_id uuid NOT NULL REFERENCES usuario(id),
    tipo text NOT NULL CHECK (tipo IN ('acceso','rectificacion','supresion','oposicion','portabilidad')),
    canal text NOT NULL,
    identidad_verificada boolean NOT NULL DEFAULT false,
    solicitada_en timestamptz NOT NULL DEFAULT now(),
    estado text NOT NULL DEFAULT 'recibida'
        CHECK (estado IN ('recibida','en_revision','resuelta','rechazada')),
    responsable_id uuid REFERENCES usuario(id),
    resultado text CHECK (resultado IN ('entregado','rectificado','anonimizado','bloqueado','denegado_conservacion')),
    motivo text,
    resuelta_en timestamptz,
    CONSTRAINT solicitud_cierre_fundado
        CHECK (estado IN ('recibida','en_revision') OR (motivo IS NOT NULL AND resuelta_en IS NOT NULL)),
    CONSTRAINT solicitud_supresion_resultado
        CHECK (tipo <> 'supresion' OR estado <> 'resuelta'
               OR resultado IN ('anonimizado','bloqueado','denegado_conservacion'))
);

CREATE TABLE documento (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    espacio_id uuid REFERENCES espacio(id),
    verificacion_id uuid REFERENCES verificacion(id),
    contrato_id uuid REFERENCES contrato(id),
    reserva_id uuid REFERENCES reserva(id),
    disputa_id uuid REFERENCES disputa(id),
    operacion_arriendo_id uuid REFERENCES operacion_arriendo(id),
    categoria text NOT NULL CHECK (categoria IN ('galeria','identidad','contrato','check_in','check_out','reclamo','descargo','boleta')),
    clave_objeto text NOT NULL UNIQUE,
    hash_sha256 hash_hex NOT NULL,
    bytes bigint NOT NULL CHECK (bytes > 0),
    autor_id uuid NOT NULL REFERENCES usuario(id),
    creado_en timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT documento_un_propietario CHECK (
        (espacio_id IS NOT NULL)::int + (verificacion_id IS NOT NULL)::int + (contrato_id IS NOT NULL)::int
      + (reserva_id IS NOT NULL)::int + (disputa_id IS NOT NULL)::int + (operacion_arriendo_id IS NOT NULL)::int = 1),
    CONSTRAINT documento_categoria_coherente CHECK (CASE categoria
        WHEN 'galeria' THEN espacio_id IS NOT NULL
        WHEN 'identidad' THEN verificacion_id IS NOT NULL
        WHEN 'contrato' THEN contrato_id IS NOT NULL
        WHEN 'reclamo' THEN disputa_id IS NOT NULL
        WHEN 'descargo' THEN disputa_id IS NOT NULL
        WHEN 'check_in' THEN operacion_arriendo_id IS NOT NULL
        WHEN 'check_out' THEN operacion_arriendo_id IS NOT NULL
        WHEN 'boleta' THEN reserva_id IS NOT NULL
        END)
);

CREATE TABLE evento_auditoria (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    actor_id uuid REFERENCES usuario(id),
    reserva_id uuid REFERENCES reserva(id),
    solicitud_titular_id uuid REFERENCES solicitud_titular(id),
    accion text NOT NULL,
    fecha timestamptz NOT NULL DEFAULT now(),
    correlacion text NOT NULL,
    resumen text NOT NULL
);
```

**Qué declara este DDL.** Claves primarias y foráneas, la coherencia entre el espacio de una reserva y el de su ocupación mediante clave foránea compuesta, la exclusión de solapamiento por espacio con `EXCLUDE USING gist` sobre el rango semiabierto, la unicidad de idempotencia por proveedor, la deduplicación de eventos externos, los topes de monto y la coherencia entre categoría de documento y propietario.

**Qué no declara.** Las transiciones de estado entre tablas, los permisos por rol, la minimización de datos, la política de conservación y anonimización, la inmutabilidad del repositorio de auditoría de RNF-017 y la emisión de la boleta. Todo ello requiere lógica de aplicación o procesos programados, y no se acredita por existir el esquema.

## Pruebas previstas del modelo

Los ensayos siguientes comprueban el diccionario y su DDL. **Ninguno se ha ejecutado**: requieren base desplegada, producto y entorno autorizado. Se mantienen separados de los dieciséis casos del Anexo C; los que correspondan se incorporarán allí si el equipo lo decide.

*Tabla. Ensayos previstos del modelo de datos.* <!--#tab:es2-datos-ensayos-->

| Código | Ensayo | Qué comprueba | Caso del Anexo C relacionado |
| --- | --- | --- | --- |
| MD-01 | Unicidad de correo y de claves idempotentes | Rechazo de duplicados con distinta capitalización y de reintentos repetidos | — |
| MD-02 | Exclusión de solapamiento por espacio | Dos inserciones simultáneas con intervalos que se superponen | PT-01, PT-02 |
| MD-03 | Coherencia espacio–reserva de la ocupación | Ocupación cuyo espacio difiere del de su reserva | PT-01 |
| MD-04 | Documento con un único propietario | Registros con cero y con dos propietarios, y categoría incompatible | — |
| MD-05 | Topes de monto y garantía | Valores negativos y captura superior al monto autorizado | PT-08 |
| MD-06 | Deduplicación de eventos del proveedor | Reenvío del mismo evento externo y de una respuesta tardía | PT-04 |
| MD-07 | Concurrencia entre reserva y bloqueo manual | Reserva creada mientras se bloquea el mismo rango | PT-01, PT-02 |
| MD-08 | Vencimiento de la retención temporal | Expiración que libera la ocupación sin invocar la hora durante la búsqueda | PT-03 |
| MD-09 | Derechos de titulares y ciclo de datos | Supresión con conservación obligatoria y registro de la solicitud | PT-16 |
| MD-10 | Migración y reversión del esquema | Aplicar el DDL en una base vacía, migrar y revertir sin pérdida | — |
| MD-11 | Retención y anonimización | Anonimización que preserva el hecho financiero y su trazabilidad | PT-16 |
| MD-12 | Restauración del esquema | Restaurar un respaldo y verificar integridad referencial | PT-11 |

## Ampliaciones todavía necesarias

### Extensión propuesta de campañas patrocinadas

No forma parte de las 16 entidades iniciales ni de los requisitos validados de ES1. Si el equipo aprueba el producto de destaque pagado, modelar al menos `campaña_destacada` (`id`, `espacio_id`, `arrendador_id`, `categoria`, `zona`, `inicio`, `fin`, `estado`, `precio_neto`, `iva`, `pago_id`, `condiciones_version`) y `exposicion_campaña` agregada (`campaña_id`, `fecha`, `zona`, `impresiones_validas`, `clics`, `reservas_atribuidas`). Las claves, retención, consentimiento/fundamento, protección antifraude y consistencia con el calendario se revisarán antes de DDL. No guardar ubicación precisa ni perfil personal del visitante en una métrica que pueda agregarse.

[[PENDIENTE: completar perfil y cuenta bancaria, sesiones y tokens, tarifas y catálogos, mensajería, reseñas, detalle tributario y notificaciones; revisar el tratamiento de los autores automáticos de documentos. No afirmar cobertura total de los RF.]]

[[PENDIENTE: mapear los literales de estado de ES1 a los propuestos y acordarlos con el equipo, validar cardinalidades, aplicar el DDL en un entorno autorizado y ejecutar los ensayos MD-01 a MD-12 con evidencia fechada.]]
