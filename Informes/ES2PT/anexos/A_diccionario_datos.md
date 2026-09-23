# Diccionario de datos de ES2

Este Anexo A describe el **modelo lógico inicial propuesto**, derivado del núcleo transaccional de ES1. No es un esquema implementado ni cubre aún todo el catálogo de 236 RF. Los tipos orientan la posterior adaptación a PostgreSQL/PostGIS, exigida por RNF-038 [@es1anexoc].

## Convenciones y alcance

- PK: clave primaria; FK: clave foránea. “No” en nulo implica obligatoriedad; “Sí” exige aplicar la condición indicada.
- Los UUID son identificadores internos propuestos. Fechas con zona se conservarán como instantes y se mostrarán en la zona del servicio, por confirmar.
- Los montos usan decimal exacto; moneda y reglas de redondeo deben validarse antes del DDL.
- Los campos sin valor inicial indicado no reciben un valor predeterminado implícito.
- Los estados nuevos se identifican como propuesta. El contrato de estados definitivo deberá mapear los nombres de ES1.
- Los roles de negocio coexisten. Una preferencia de uso no otorga privilegios administrativos.
- Relaciones y tipos constituyen decisiones de diseño ES2; sus cambios se registran en INV-004.

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
| proveedor | text | No | Producto por confirmar en INV-003 | Proveedor |
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
| espacio_id | uuid | Sí | FK espacio.id; uno de los cuatro propietarios | Galería |
| verificacion_id | uuid | Sí | FK verificacion.id; uno de los cuatro propietarios | Antecedente de identidad |
| contrato_id | uuid | Sí | FK contrato.id; uno de los cuatro propietarios | Contrato generado/firmado |
| reserva_id | uuid | Sí | FK reserva.id; uno de los cuatro propietarios | Evidencia o comprobante |
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
| accion | text | No | Catálogo de eventos por definir | Hecho |
| fecha | timestamptz | No | Instante del servidor | Momento |
| correlacion | text | No | Identificador de solicitud/evento | Rastreo |
| resumen | text | No | Sin contraseñas, tokens ni datos de tarjeta | Detalle minimizado |

## Reglas entre entidades

1. El espacio de una ocupación de reserva debe coincidir con el de la reserva. Proponer FK compuesta o control transaccional equivalente; una FK simple a reserva no basta.
2. Cada intervalo activo de ocupación debe excluir superposición para el mismo espacio. Usar un único calendario para bloqueos manuales y reservas. El vencimiento cambia explícitamente el estado activo; no se presupone un índice cuyo predicado dependa de la hora actual.
3. Una reserva pagada no equivale a contrato firmado. Habilitar ingreso solo al confirmar las firmas requeridas.
4. El usuario que firma debe ser parte de la reserva. La combinación contrato/usuario no demuestra por sí sola que estén todos los firmantes requeridos.
5. No liquidar con disputas abiertas. Importe, comisión, deducción y garantía deberán conciliarse con las operaciones confirmadas.
6. Documento debe tener exactamente un propietario entre espacio, verificación, contrato y reserva; la categoría y los permisos deben ser compatibles con ese propietario.
7. Las claves y referencias externas tienen ámbito definido por proveedor. Los eventos sin firma válida no ingresan al procesamiento de negocio; registrar su rechazo sin almacenar secretos.
8. No usar borrado en cascada sobre hechos financieros o evidencia. Conciliar privacidad, anonimización y retención mediante una política fundada; la FK a usuario no resuelve por sí sola esa política.
9. Toda tarea que llama a un proveedor debe registrar su intención y resultado y tratar respuestas inciertas. Un rollback local no revierte automáticamente un efecto externo.

## Ampliaciones todavía necesarias

[[PENDIENTE: completar perfil y cuenta bancaria, sesiones/tokens, tarifas y catálogos, mensajería, reseñas, detalle tributario, vínculo explícito entre cada evidencia y su evento/reclamo, notificaciones y reglas de privacidad. Revisar el tratamiento de autores automáticos de documentos. No afirmar cobertura total de los RF.]]

[[PENDIENTE: acordar los catálogos de estados, validar cardinalidades con el equipo, producir DDL y ejecutar pruebas de integridad, concurrencia y migración.]]
