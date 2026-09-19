# Actores del Sistema y Requerimientos Funcionales por Módulo
## Sistema: EspaciGo — Marketplace SaaS B2B2C de Espacios Comerciales

> **Convención de ID:** `RQF-###` (Requerimiento Funcional).  
> Se usa `RQF` para distinguirlos inequívocamente de los Requerimientos No Funcionales (`RNQF`).

---

## 1. 🎭 Identificación de Actores

### 1.1 Actores Primarios (humanos que interactúan directamente con el sistema)

| Actor | Alias UML | Descripción | Estado requerido |
|---|---|---|---|
| **Visitante** | `Visitante` | Usuario anónimo, sin cuenta registrada. Puede navegar y explorar publicaciones públicas, pero no puede interactuar transaccionalmente. | Sin cuenta |
| **Usuario Registrado** | `Usuario` | Posee cuenta con correo verificado pero aún sin validación de identidad (KYC/KYB). Puede iniciar sesión, gestionar su perfil y visualizar publicaciones. | Correo verificado |
| **Arrendador** | `Arrendador` | Usuario con identidad verificada (KYC o KYB) que publica y gestiona espacios comerciales. Aprueba o rechaza reservas. | KYC/KYB aprobado |
| **Arrendatario** | `Arrendatario` | Usuario con identidad verificada (KYC o KYB) que busca, reserva y paga por espacios comerciales. | KYC/KYB aprobado |
| **Administrador** | `Administrador` | Operador interno de EspaciGo. Revisa validaciones fallidas, arbitra disputas y consulta auditorías. Acceso especial al panel de administración. | Rol especial de plataforma |

> **Nota:** Un mismo usuario puede actuar como **Arrendador** y **Arrendatario** simultáneamente; los roles no son excluyentes.  
> **Jerarquía de herencia (UML):**  
> `Visitante` → `Usuario Registrado` → `Arrendador / Arrendatario`

---

### 1.2 Actores Secundarios (sistemas externos que interactúan con EspaciGo)

| Actor Externo | Tipo | Rol en el sistema |
|---|---|---|
| **Registro Civil** | Sistema externo (API) | Valida la vigencia de la cédula de identidad en el proceso KYC |
| **SII** (Servicio de Impuestos Internos) | Sistema externo (API) | Valida el inicio de actividades y giro comercial en el proceso KYB |
| **Mercado Pago** | Sistema externo (Pasarela de pagos) | Procesa pagos con tarjeta, gestiona el Escrow, ejecuta reembolsos, pre-autorizaciones de garantía y transferencias de Payout |
| **FirmaVirtual** | Sistema externo (API) | Recibe el contrato PDF generado y distribuye los enlaces de firma electrónica a las partes |
| **BigQuery / Data Warehouse** | Sistema externo (Repositorio) | Almacena de forma inmutable los registros de auditoría de todas las acciones transaccionales |

---

## 2. 📦 Módulos del Sistema y Requerimientos Funcionales

> Los RF están renumerados con la notación `RQF-###`.  
> La numeración es correlativa dentro de cada módulo para facilitar la referencia en fichas de casos de uso.

---

### 📌 Módulo M01 — Autenticación y Gestión de Cuenta

**Actores involucrados:** Visitante, Usuario Registrado, Administrador

| ID | Descripción del Requerimiento Funcional |
|---|---|
| **RQF-001** | El sistema debe permitir registrar una cuenta de usuario. |
| **RQF-002** | El sistema debe validar que el campo "Correo Electrónico" contenga un formato válido (presencia de "@" y dominio). |
| **RQF-003** | El sistema debe validar que el campo "Contraseña" posea un mínimo de 8 caracteres. |
| **RQF-004** | El sistema debe validar que el campo "Contraseña" posea al menos una letra mayúscula. |
| **RQF-005** | El sistema debe validar que el campo "Contraseña" posea al menos un número. |
| **RQF-006** | El sistema debe validar que el campo "Contraseña" posea al menos un carácter especial. |
| **RQF-007** | El sistema debe rechazar el registro si el correo electrónico ya existe en la base de datos. |
| **RQF-008** | El sistema debe encriptar la contraseña del usuario antes de almacenarla en la base de datos. |
| **RQF-009** | El sistema debe enviar un correo electrónico con un token de verificación tras un registro exitoso. |
| **RQF-010** | El sistema debe cambiar el estado del usuario a "Verificado" al consumir el token del correo electrónico. |
| **RQF-011** | El sistema debe bloquear el inicio de sesión para cuentas en estado "No Verificado". |
| **RQF-012** | El sistema debe permitir iniciar sesión. |
| **RQF-013** | El sistema debe validar que la contraseña ingresada en el inicio de sesión coincida con el hash almacenado. |
| **RQF-014** | El sistema debe rechazar el inicio de sesión si las credenciales son incorrectas. |
| **RQF-015** | El sistema debe incrementar un contador de intentos fallidos al rechazar un inicio de sesión. |
| **RQF-016** | El sistema debe bloquear la cuenta de usuario al alcanzar 5 intentos fallidos consecutivos. |
| **RQF-017** | El sistema debe enviar un correo de alerta de seguridad al bloquear una cuenta. |
| **RQF-018** | El sistema debe liberar automáticamente una cuenta bloqueada tras 30 minutos. |
| **RQF-019** | El sistema debe generar una credencial temporal de sesión tras un inicio de sesión exitoso. |
| **RQF-020** | El sistema debe registrar la dirección IP del usuario durante el inicio de sesión. |
| **RQF-021** | El sistema debe permitir recuperar la contraseña. |
| **RQF-022** | El sistema debe enviar un enlace único de recuperación al correo electrónico ingresado. |
| **RQF-023** | El sistema debe expirar el enlace de recuperación de contraseña tras 15 minutos de su emisión. |
| **RQF-024** | El sistema debe permitir actualizar la contraseña desde el enlace de recuperación. |
| **RQF-025** | El sistema debe permitir cerrar la sesión activa invalidando la credencial temporal. |

---

### 📌 Módulo M02 — Gestión de Perfil de Usuario

**Actores involucrados:** Usuario Registrado, Arrendador, Arrendatario

| ID | Descripción del Requerimiento Funcional |
|---|---|
| **RQF-026** | El sistema debe permitir consultar los datos del perfil de usuario. |
| **RQF-027** | El sistema debe permitir modificar el nombre de perfil del usuario. |
| **RQF-028** | El sistema debe validar que el nombre de perfil contenga únicamente caracteres alfabéticos. |
| **RQF-029** | El sistema debe permitir modificar el número telefónico del usuario. |
| **RQF-030** | El sistema debe validar que el número telefónico contenga exactamente 9 dígitos. |
| **RQF-031** | El sistema debe permitir cargar una fotografía de perfil. |
| **RQF-032** | El sistema debe validar que la fotografía de perfil no supere los 2MB de tamaño. |
| **RQF-033** | El sistema debe comprimir la fotografía de perfil antes de almacenarla. |
| **RQF-034** | El sistema debe permitir eliminar la fotografía de perfil. |
| **RQF-035** | El sistema debe permitir registrar una cuenta bancaria asociada al perfil. |
| **RQF-036** | El sistema debe validar que el RUT de la cuenta bancaria coincida con el RUT verificado del usuario. |
| **RQF-037** | El sistema debe permitir solicitar la eliminación permanente de la cuenta de usuario. |
| **RQF-038** | El sistema debe consultar la existencia de reservas activas al solicitar la eliminación de la cuenta. |
| **RQF-039** | El sistema debe consultar la existencia de pagos pendientes al solicitar la eliminación de la cuenta. |
| **RQF-040** | El sistema debe consultar la existencia de disputas abiertas al solicitar la eliminación de la cuenta. |
| **RQF-041** | El sistema debe bloquear la eliminación de la cuenta si existe al menos un proceso (reserva, pago, disputa) activo. |
| **RQF-042** | El sistema debe anonimizar los datos transaccionales del usuario tras aprobar su eliminación. |
| **RQF-043** | El sistema debe eliminar los datos personales (nombre, teléfono, RUT) de la base de datos de manera irreversible. |

---

### 📌 Módulo M03 — Verificación de Identidad (KYC / KYB)

**Actores involucrados:** Usuario Registrado, Administrador, Registro Civil (externo), SII (externo)

| ID | Descripción del Requerimiento Funcional |
|---|---|
| **RQF-044** | El sistema debe permitir solicitar la validación de identidad KYC (Persona Natural). |
| **RQF-045** | El sistema debe permitir cargar una fotografía del anverso de la Cédula de Identidad. |
| **RQF-046** | El sistema debe permitir cargar una fotografía del reverso de la Cédula de Identidad. |
| **RQF-047** | El sistema debe validar que las imágenes de la cédula posean un formato de archivo compatible. |
| **RQF-048** | El sistema debe extraer el RUT desde la fotografía del anverso mediante OCR. |
| **RQF-049** | El sistema debe extraer el número de serie desde la fotografía mediante OCR. |
| **RQF-050** | El sistema debe validar la vigencia de la cédula consultando la API del Registro Civil. |
| **RQF-051** | El sistema debe cambiar el estado del perfil a "Verificado_KYC" si la consulta al Registro Civil es exitosa. |
| **RQF-052** | El sistema debe rechazar la solicitud KYC si el documento se encuentra vencido. |
| **RQF-053** | El sistema debe enviar una notificación push al usuario al finalizar la validación KYC. |
| **RQF-054** | El sistema debe permitir solicitar la validación de identidad KYB (Empresa). |
| **RQF-055** | El sistema debe permitir ingresar el RUT de la empresa. |
| **RQF-056** | El sistema debe validar el dígito verificador del RUT ingresado. |
| **RQF-057** | El sistema debe consultar el giro comercial de la empresa mediante la API del SII. |
| **RQF-058** | El sistema debe rechazar la validación KYB si la empresa no posee inicio de actividades vigente. |
| **RQF-059** | El sistema debe cambiar el estado del perfil a "Verificado_KYB" tras una consulta exitosa al SII. |
| **RQF-060** | El sistema debe listar las validaciones KYC/KYB fallidas en un panel de administración. |
| **RQF-061** | El sistema debe permitir a un administrador aprobar manualmente una validación de identidad. |
| **RQF-062** | El sistema debe permitir a un administrador rechazar manualmente una validación de identidad. |
| **RQF-063** | El sistema debe requerir que el administrador ingrese un motivo en texto al rechazar una validación. |

---

### 📌 Módulo M04 — Gestión de Publicaciones

**Actores involucrados:** Arrendador, Visitante, Usuario Registrado

| ID | Descripción del Requerimiento Funcional |
|---|---|
| **RQF-064** | El sistema debe permitir acceder al panel de creación de publicaciones. |
| **RQF-065** | El sistema debe bloquear el acceso al panel de creación de publicaciones a usuarios no verificados. |
| **RQF-066** | El sistema debe permitir ingresar un título para la publicación. |
| **RQF-067** | El sistema debe validar que el título de la publicación no exceda los 70 caracteres. |
| **RQF-068** | El sistema debe permitir ingresar la descripción de la publicación. |
| **RQF-069** | El sistema debe validar que la descripción de la publicación contenga al menos 100 caracteres. |
| **RQF-070** | El sistema debe permitir ingresar la superficie total del inmueble en metros cuadrados. |
| **RQF-071** | El sistema debe validar que la superficie ingresada sea un número entero mayor a cero. |
| **RQF-072** | El sistema debe permitir seleccionar el tipo de inmueble desde una lista desplegable predefinida. |
| **RQF-073** | El sistema debe permitir establecer la capacidad máxima de personas del inmueble. |
| **RQF-074** | El sistema debe permitir agregar reglas de uso (ej. no ruido, no mascotas) a la publicación. |
| **RQF-075** | El sistema debe permitir ingresar el precio base de arriendo por día. |
| **RQF-076** | El sistema debe validar que el precio base ingresado sea mayor a $5.000 CLP. |
| **RQF-077** | El sistema debe permitir cargar una fotografía a la galería de la publicación. |
| **RQF-078** | El sistema debe validar que la cantidad de fotografías por publicación no exceda las 10 unidades. |
| **RQF-079** | El sistema debe rechazar la carga de fotografías que superen los 5MB de tamaño. |
| **RQF-080** | El sistema debe permitir seleccionar una fotografía como portada principal de la publicación. |
| **RQF-081** | El sistema debe permitir eliminar una fotografía de la galería de la publicación. |
| **RQF-082** | El sistema debe permitir ingresar la dirección física completa del inmueble. |
| **RQF-083** | El sistema debe transformar la dirección física en coordenadas de latitud y longitud. |
| **RQF-084** | El sistema debe guardar el estado de la publicación como "Borrador" de manera automática durante su creación. |
| **RQF-085** | El sistema debe cambiar el estado de la publicación a "Activa" tras finalizar y confirmar el formulario de creación. |
| **RQF-086** | El sistema debe generar un calendario de disponibilidad asociado a la publicación activa. |
| **RQF-087** | El sistema debe permitir al arrendador bloquear fechas específicas en el calendario de su publicación. |
| **RQF-088** | El sistema debe permitir al arrendador desbloquear fechas previamente bloqueadas manualmente. |
| **RQF-089** | El sistema debe permitir modificar el título de una publicación existente. |
| **RQF-090** | El sistema debe permitir modificar el precio base de una publicación existente. |
| **RQF-091** | El sistema debe permitir cambiar el estado de una publicación activa a "Oculta". |
| **RQF-092** | El sistema debe impedir la visualización pública de una publicación en estado "Oculta". |
| **RQF-093** | El sistema debe permitir cambiar el estado de una publicación "Oculta" a "Activa". |
| **RQF-094** | El sistema debe permitir eliminar permanentemente una publicación. |
| **RQF-095** | El sistema debe rechazar la eliminación de una publicación si posee reservas futuras pendientes. |
| **RQF-096** | El sistema debe permitir consultar la lista de todas las publicaciones del usuario (Mis Inmuebles). |

---

### 📌 Módulo M05 — Búsqueda y Exploración de Espacios

**Actores involucrados:** Visitante, Usuario Registrado, Arrendatario

| ID | Descripción del Requerimiento Funcional |
|---|---|
| **RQF-097** | El sistema debe renderizar un mapa interactivo en la vista de búsqueda de espacios. |
| **RQF-098** | El sistema debe desplegar pines en el mapa utilizando las coordenadas de las publicaciones activas. |
| **RQF-099** | El sistema debe mostrar una cuadrícula de tarjetas con el resumen de las publicaciones disponibles. |
| **RQF-100** | El sistema debe permitir buscar publicaciones ingresando un texto libre en una barra de búsqueda. |
| **RQF-101** | El sistema debe permitir filtrar los resultados de búsqueda definiendo un precio mínimo. |
| **RQF-102** | El sistema debe permitir filtrar los resultados de búsqueda definiendo un precio máximo. |
| **RQF-103** | El sistema debe permitir filtrar los resultados de búsqueda seleccionando el tipo de inmueble. |
| **RQF-104** | El sistema debe permitir filtrar los resultados de búsqueda ingresando una cantidad mínima de metros cuadrados. |
| **RQF-105** | El sistema debe permitir filtrar los resultados de búsqueda seleccionando una fecha de inicio y una de fin. |
| **RQF-106** | El sistema debe excluir de los resultados aquellas publicaciones que posean fechas bloqueadas o reservadas dentro del rango consultado. |
| **RQF-107** | El sistema debe permitir limpiar todos los filtros de búsqueda aplicados simultáneamente. |
| **RQF-108** | El sistema debe permitir consultar los detalles completos de una publicación al hacer clic en su tarjeta. |
| **RQF-109** | El sistema debe calcular el costo total de la estadía multiplicando el precio base por la cantidad de días seleccionados. |
| **RQF-110** | El sistema debe calcular el monto de la comisión de servicio (Fee) sobre el costo total de la estadía. |
| **RQF-111** | El sistema debe calcular el monto de la garantía exigida (porcentaje definido por el arrendador) sobre el costo total. |
| **RQF-112** | El sistema debe mostrar el desglose de cobro (Estadía + Comisión + Garantía) en el panel de cotización. |

---

### 📌 Módulo M06 — Reservas y Pagos (Escrow)

**Actores involucrados:** Arrendatario, Arrendador, Mercado Pago (externo)

| ID | Descripción del Requerimiento Funcional |
|---|---|
| **RQF-113** | El sistema debe permitir seleccionar las fechas de reserva dentro del detalle de la publicación. |
| **RQF-114** | El sistema debe validar que la fecha de inicio seleccionada sea mayor a la fecha actual. |
| **RQF-115** | El sistema debe validar que la fecha de fin sea mayor a la fecha de inicio. |
| **RQF-116** | El sistema debe consultar en la base de datos la disponibilidad en tiempo real de las fechas seleccionadas al presionar "Reservar". |
| **RQF-117** | El sistema debe rechazar el intento de reserva si la consulta en tiempo real detecta colisión de fechas. |
| **RQF-118** | El sistema debe registrar un intento de reserva en estado "Pendiente de Pago" tras validar la disponibilidad. |
| **RQF-119** | El sistema debe redirigir al usuario hacia la interfaz de la pasarela de pagos integrada. |
| **RQF-120** | El sistema debe permitir ingresar el número de una Tarjeta de Crédito. |
| **RQF-121** | El sistema debe permitir ingresar el código de seguridad (CVV) de la Tarjeta de Crédito. |
| **RQF-122** | El sistema debe permitir ingresar el número de una Tarjeta de Débito. |
| **RQF-123** | El sistema debe enviar el token de la tarjeta y los montos a la API de la pasarela de pagos. |
| **RQF-124** | El sistema debe cambiar el estado de la reserva a "Pagada_Escrow" al recibir confirmación exitosa de la pasarela. |
| **RQF-125** | El sistema debe retener temporalmente los fondos recaudados en la cuenta recaudadora principal (Escrow). |
| **RQF-126** | El sistema debe ejecutar una solicitud de pre-autorización (bloqueo de cupo) en la tarjeta de crédito por el monto exacto de la garantía. |
| **RQF-127** | El sistema debe cambiar el estado de la reserva a "Cancelada_Por_Pago" si la pasarela rechaza la transacción por fondos insuficientes. |
| **RQF-128** | El sistema debe ejecutar un proceso en segundo plano que cancele las reservas en estado "Pendiente de Pago" tras 15 minutos de inactividad. |
| **RQF-129** | El sistema debe notificar al arrendatario mediante correo electrónico cuando el pago sea exitoso. |
| **RQF-130** | El sistema debe notificar al arrendador mediante correo electrónico sobre la recepción de una nueva solicitud pagada. |
| **RQF-131** | El sistema debe mostrar las solicitudes de reserva entrantes en el panel del arrendador. |
| **RQF-132** | El sistema debe permitir al arrendador aprobar una solicitud de reserva entrante. |
| **RQF-133** | El sistema debe cambiar el estado de la reserva a "Aprobada_Host" tras la aprobación. |
| **RQF-134** | El sistema debe permitir al arrendador rechazar una solicitud de reserva entrante. |
| **RQF-135** | El sistema debe exigir al arrendador seleccionar un motivo de rechazo desde una lista predefinida. |
| **RQF-136** | El sistema debe ejecutar automáticamente el reembolso total a la tarjeta del arrendatario tras el rechazo. |
| **RQF-137** | El sistema debe cancelar automáticamente las solicitudes de reserva no respondidas por el arrendador en 24 horas. |

---

### 📌 Módulo M07 — Generación y Firma de Contratos

**Actores involucrados:** Arrendador, Arrendatario, FirmaVirtual (externo)

| ID | Descripción del Requerimiento Funcional |
|---|---|
| **RQF-138** | El sistema debe iniciar el proceso de generación de contrato tras la aprobación de la reserva por el arrendador. |
| **RQF-139** | El sistema debe consultar los datos legales del arrendador (Nombre, RUT, Dirección) desde la base de datos. |
| **RQF-140** | El sistema debe consultar los datos legales del arrendatario (Nombre, RUT, Dirección) desde la base de datos. |
| **RQF-141** | El sistema debe consultar los detalles del inmueble (Dirección, Dimensiones) desde la base de datos. |
| **RQF-142** | El sistema debe reemplazar las variables etiquetadas en la plantilla HTML del contrato con los datos extraídos. |
| **RQF-143** | El sistema debe compilar el documento HTML y exportarlo en formato PDF. |
| **RQF-144** | El sistema debe enviar el archivo PDF generado hacia el proveedor de firma electrónica externa. |
| **RQF-145** | El sistema debe extraer los enlaces de firma únicos devueltos por la API de firma electrónica. |
| **RQF-146** | El sistema debe enviar el enlace de firma correspondiente al correo electrónico del arrendatario. |
| **RQF-147** | El sistema debe enviar el enlace de firma correspondiente al correo electrónico del arrendador. |
| **RQF-148** | El sistema debe recibir notificaciones asíncronas (Webhooks) desde el proveedor de firma cada vez que un participante firme. |
| **RQF-149** | El sistema debe cambiar el estado del contrato a "Firma_Parcial" tras recibir el primer Webhook de firma exitosa. |
| **RQF-150** | El sistema debe descargar el documento PDF firmado y certificado tras recibir el Webhook de finalización. |
| **RQF-151** | El sistema debe cifrar el documento PDF final antes de su almacenamiento. |
| **RQF-152** | El sistema debe almacenar el documento PDF cifrado en un repositorio de archivos seguro. |
| **RQF-153** | El sistema debe cambiar el estado de la reserva a "Lista_Para_Checkin" tras almacenar el contrato notariado. |
| **RQF-154** | El sistema debe notificar a ambas partes que el contrato ha sido firmado exitosamente. |
| **RQF-155** | El sistema debe ejecutar un trabajo programado diario (CronJob) para detectar reservas cuya fecha de inicio es igual a la fecha actual y no poseen el contrato firmado. |
| **RQF-156** | El sistema debe cancelar automáticamente las reservas detectadas sin contrato firmado. |
| **RQF-157** | El sistema debe reembolsar el pago retenido al arrendatario en caso de cancelación por falta de firmas. |
| **RQF-158** | El sistema debe permitir al arrendatario consultar el contrato PDF descargándolo mediante una URL firmada temporal. |

---

### 📌 Módulo M08 — Check-in y Check-out

**Actores involucrados:** Arrendatario, Arrendador

| ID | Descripción del Requerimiento Funcional |
|---|---|
| **RQF-159** | El sistema debe habilitar el botón de "Check-in" en el panel del arrendatario únicamente el día de inicio de la reserva. |
| **RQF-160** | El sistema debe requerir la carga de al menos una fotografía del inmueble para procesar el Check-in. |
| **RQF-161** | El sistema debe registrar la fecha, hora y ubicación GPS del dispositivo al momento de procesar el Check-in. |
| **RQF-162** | El sistema debe cambiar el estado de la reserva a "En_Curso" tras enviar el formulario de Check-in. |
| **RQF-163** | El sistema debe notificar al arrendador que el arrendatario ha ingresado al inmueble. |
| **RQF-164** | El sistema debe bloquear la posibilidad de realizar Check-in fuera de la fecha de inicio del arriendo. |
| **RQF-165** | El sistema debe validar que las fotografías de Check-in tengan una resolución mínima de 720p. |
| **RQF-166** | El sistema debe rechazar la carga de imágenes corruptas en el formulario de Check-in. |
| **RQF-167** | El sistema debe permitir al arrendatario adjuntar comentarios de texto junto a cada foto de Check-in. |

---

### 📌 Módulo M09 — Resolución de Disputas

**Actores involucrados:** Arrendador, Arrendatario, Administrador, Mercado Pago (externo)

| ID | Descripción del Requerimiento Funcional |
|---|---|
| **RQF-168** | El sistema debe ejecutar un temporizador de 24 horas a partir del fin de la estadía para el cobro o disputa. |
| **RQF-169** | El sistema debe permitir al arrendador registrar un reclamo de daños ingresando texto descriptivo. |
| **RQF-170** | El sistema debe exigir al arrendador cargar fotografías de evidencia para validar el reclamo. |
| **RQF-171** | El sistema debe bloquear la ejecución del Payout y la liberación de la garantía al detectar un reclamo registrado. |
| **RQF-172** | El sistema debe cambiar el estado de la reserva a "En_Disputa" tras el registro de un reclamo. |
| **RQF-173** | El sistema debe notificar al arrendatario sobre la apertura de una disputa en su contra. |
| **RQF-174** | El sistema debe permitir al arrendatario ingresar un texto de defensa asociado a la disputa. |
| **RQF-175** | El sistema debe permitir al arrendatario adjuntar imágenes adicionales a su texto de defensa. |
| **RQF-176** | El sistema debe listar todas las disputas en estado "En_Disputa" en el panel de administración. |
| **RQF-177** | El sistema debe permitir al administrador consultar las fotos del Check-in vinculadas a la reserva en disputa. |
| **RQF-178** | El sistema debe permitir al administrador consultar el contrato firmado vinculado a la reserva en disputa. |
| **RQF-179** | El sistema debe permitir al administrador registrar un fallo a favor del arrendatario (Rechazar reclamo). |
| **RQF-180** | El sistema debe permitir al administrador registrar un fallo a favor del arrendador (Aprobar reclamo). |
| **RQF-181** | El sistema debe exigir al administrador ingresar el monto exacto a deducir de la garantía al fallar a favor del arrendador. |
| **RQF-182** | El sistema debe cambiar el estado de la disputa a "Resuelta" tras el registro del fallo del administrador. |
| **RQF-183** | El sistema debe consumir la API de la pasarela para hacer efectivo el cobro parcial sobre la pre-autorización de la garantía. |
| **RQF-184** | El sistema debe consumir la API de la pasarela para liberar el saldo sobrante de la pre-autorización de la garantía. |

---

### 📌 Módulo M10 — Payout y Facturación

**Actores involucrados:** Arrendador, Arrendatario, Mercado Pago (externo)

| ID | Descripción del Requerimiento Funcional |
|---|---|
| **RQF-185** | El sistema debe ejecutar el proceso de Payout automáticamente si transcurren las 24 horas de gracia sin reclamos. |
| **RQF-186** | El sistema debe calcular el monto a transferir al arrendador (Monto total estadía - Comisión EspaciGo). |
| **RQF-187** | El sistema debe consumir la API de transferencia para enviar el dinero a la cuenta bancaria del arrendador. |
| **RQF-188** | El sistema debe consumir la API de la pasarela para liberar el 100% de la pre-autorización de la garantía. |
| **RQF-189** | El sistema debe notificar al arrendador sobre la transferencia exitosa de sus fondos. |
| **RQF-190** | El sistema debe generar la boleta electrónica correspondiente a la comisión cobrada por EspaciGo. |
| **RQF-191** | El sistema debe enviar la boleta electrónica en formato PDF al correo del arrendatario. |
| **RQF-192** | El sistema debe cambiar el estado de la reserva a "Cerrada" tras la ejecución exitosa del Payout. |

---

### 📌 Módulo M11 — Auditoría y Trazabilidad

**Actores involucrados:** Administrador, BigQuery / Data Warehouse (externo)

| ID | Descripción del Requerimiento Funcional |
|---|---|
| **RQF-193** | El sistema debe capturar cada acción transaccional (login, reserva, pago, firma, eliminación) generada en la plataforma. |
| **RQF-194** | El sistema debe empaquetar los datos transaccionales en una estructura de datos estandarizada. |
| **RQF-195** | El sistema debe enviar la estructura de datos a una cola de mensajes asíncrona para auditoría. |
| **RQF-196** | El sistema debe almacenar los registros transaccionales en un repositorio de datos de solo lectura. |
| **RQF-197** | El sistema debe denegar cualquier petición de modificación sobre los registros de auditoría. |
| **RQF-198** | El sistema debe denegar cualquier petición de eliminación sobre los registros de auditoría. |
| **RQF-199** | El sistema debe permitir al administrador consultar el historial inmutable de un usuario filtrando por su RUT. |
| **RQF-200** | El sistema debe exportar los resultados de la consulta de auditoría en un formato de hoja de cálculo estructurado para reportes legales. |

---

### 📌 Requerimientos funcionales complementarios

| ID | Descripción del Requerimiento Funcional |
|---|---|
| **RQF-201** | El sistema debe permitir al arrendatario registrar una reseña y una calificación numérica sobre un espacio después de completar una reserva. |
| **RQF-202** | El sistema debe mostrar las reseñas y calificaciones publicadas de un espacio en su vista de detalle. |
| **RQF-203** | El sistema debe permitir al administrador ocultar una reseña reportada cuando incumpla las reglas de publicación, registrando el motivo de la acción. |
| **RQF-204** | El sistema debe permitir al arrendador configurar una tarifa por hora, día o mes para cada publicación activa. |
| **RQF-205** | El sistema debe calcular el precio de una reserva según la modalidad tarifaria seleccionada y la unidad de tiempo solicitada. |
| **RQF-206** | El sistema debe permitir seleccionar la hora de inicio y término cuando la modalidad de reserva sea por hora. |
| **RQF-207** | El sistema debe impedir la creación de reservas cuyos intervalos de tiempo se superpongan con reservas confirmadas o bloqueos existentes. |
| **RQF-208** | El sistema debe permitir al arrendatario registrar el check-out indicando la fecha, hora, observaciones y fotografías del estado final del espacio. |
| **RQF-209** | El sistema debe cambiar el estado de la reserva a "Finalizada" cuando el check-out sea registrado correctamente. |
| **RQF-210** | El sistema debe permitir al arrendatario y al arrendador enviar y consultar mensajes asociados a una reserva mediante un chat interno. |
| **RQF-211** | El sistema debe conservar el historial de mensajes del chat asociado a la reserva mientras exista una disputa abierta o durante el periodo de auditoría definido. |
| **RQF-212** | El sistema debe notificar al arrendatario y al arrendador los cambios de estado de una reserva mediante los canales configurados. |
| **RQF-213** | El sistema debe notificar al arrendatario cuando el pago sea rechazado, quede pendiente o requiera una nueva acción. |
| **RQF-214** | El sistema debe notificar a los participantes cuando el contrato esté pendiente de firma, haya sido firmado parcialmente o esté completamente firmado. |
| **RQF-215** | El sistema debe permitir al arrendatario solicitar un reembolso cuando una reserva sea cancelada conforme a las políticas configuradas. |
| **RQF-216** | El sistema debe registrar y mostrar el resultado de cada intento de reembolso, incluyendo estado, fecha, monto y código de operación de la pasarela. |
| **RQF-217** | El sistema debe permitir al usuario corregir los antecedentes rechazados en una validación KYC o KYB y solicitar un nuevo intento de validación. |
| **RQF-218** | El sistema debe permitir al administrador consultar y cambiar el estado de los reclamos, registrando resolución, fecha, responsable y observaciones. |
| **RQF-219** | El sistema debe permitir al administrador bloquear, desbloquear y consultar el motivo de bloqueo de una cuenta de usuario. |
| **RQF-220** | El sistema debe permitir al administrador generar reportes de reservas, pagos, reembolsos y disputas filtrados por periodo y estado. |

---

## 3. 🗺️ Resumen: Actores por Módulo

| Módulo | Actores Primarios | Actores Externos |
|---|---|---|
| M01 — Autenticación y Gestión de Cuenta | Visitante, Usuario Registrado, Administrador | — |
| M02 — Gestión de Perfil | Usuario Registrado, Arrendador, Arrendatario | — |
| M03 — Verificación de Identidad (KYC/KYB) | Usuario Registrado, Administrador | Registro Civil, SII |
| M04 — Gestión de Publicaciones | Arrendador | — |
| M05 — Búsqueda y Exploración | Visitante, Usuario Registrado, Arrendatario | — |
| M06 — Reservas y Pagos (Escrow) | Arrendatario, Arrendador | Mercado Pago |
| M07 — Generación y Firma de Contratos | Arrendador, Arrendatario | FirmaVirtual |
| M08 — Check-in y Check-out | Arrendatario, Arrendador | — |
| M09 — Resolución de Disputas | Arrendador, Arrendatario, Administrador | Mercado Pago |
| M10 — Payout y Facturación | Arrendador, Arrendatario | Mercado Pago |
| M11 — Auditoría y Trazabilidad | Administrador | BigQuery |

---

## 4. 📊 Estadísticas del Catálogo

| Métrica | Valor |
|---|---|
| Total de Requerimientos Funcionales | **220** |
| Total de Módulos | **11** |
| Actores Primarios | **5** (Visitante, Usuario Registrado, Arrendador, Arrendatario, Administrador) |
| Actores Externos (Sistemas) | **5** (Registro Civil, SII, Mercado Pago, FirmaVirtual, BigQuery) |
| Módulo con más RQF | M06 — Reservas y Pagos (25 RQF) |
| Módulo con menos RQF | M08 — Check-in / Check-out (9 RQF) |
