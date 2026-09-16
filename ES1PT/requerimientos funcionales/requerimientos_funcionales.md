# Listado Exhaustivo de Requerimientos Funcionales
*Basado estrictamente en el estándar IEEE 830. Lista plana, atómica y lineal.*

| ID | Descripción del Requerimiento Funcional |
|---|---|
| **RF-001** | El sistema debe permitir registrar una cuenta de usuario. |
| **RF-002** | El sistema debe validar que el campo "Correo Electrónico" contenga un formato válido (presencia de "@" y dominio). |
| **RF-003** | El sistema debe validar que el campo "Contraseña" posea un mínimo de 8 caracteres. |
| **RF-004** | El sistema debe validar que el campo "Contraseña" posea al menos una letra mayúscula. |
| **RF-005** | El sistema debe validar que el campo "Contraseña" posea al menos un número. |
| **RF-006** | El sistema debe validar que el campo "Contraseña" posea al menos un carácter especial. |
| **RF-007** | El sistema debe rechazar el registro si el correo electrónico ya existe en la base de datos. |
| **RF-008** | El sistema debe encriptar la contraseña del usuario antes de almacenarla en la base de datos. |
| **RF-009** | El sistema debe enviar un correo electrónico con un token de verificación tras un registro exitoso. |
| **RF-010** | El sistema debe cambiar el estado del usuario a "Verificado" al consumir el token del correo electrónico. |
| **RF-011** | El sistema debe bloquear el inicio de sesión para cuentas en estado "No Verificado". |
| **RF-012** | El sistema debe permitir iniciar sesión. |
| **RF-013** | El sistema debe validar que la contraseña ingresada en el inicio de sesión coincida con el hash almacenado. |
| **RF-014** | El sistema debe rechazar el inicio de sesión si las credenciales son incorrectas. |
| **RF-015** | El sistema debe incrementar un contador de intentos fallidos al rechazar un inicio de sesión. |
| **RF-016** | El sistema debe bloquear la cuenta de usuario al alcanzar 5 intentos fallidos consecutivos. |
| **RF-017** | El sistema debe enviar un correo de alerta de seguridad al bloquear una cuenta. |
| **RF-018** | El sistema debe liberar automáticamente una cuenta bloqueada tras 30 minutos. |
| **RF-019** | El sistema debe generar una credencial temporal de sesión tras un inicio de sesión exitoso. |
| **RF-020** | El sistema debe registrar la dirección IP del usuario durante el inicio de sesión. |
| **RF-021** | El sistema debe permitir recuperar la contraseña. |
| **RF-022** | El sistema debe enviar un enlace único de recuperación al correo electrónico ingresado. |
| **RF-023** | El sistema debe expirar el enlace de recuperación de contraseña tras 15 minutos de su emisión. |
| **RF-024** | El sistema debe permitir actualizar la contraseña desde el enlace de recuperación. |
| **RF-025** | El sistema debe permitir cerrar la sesión activa invalidando la credencial temporal. |
| **RF-026** | El sistema debe permitir consultar los datos del perfil de usuario. |
| **RF-027** | El sistema debe permitir modificar el nombre de perfil del usuario. |
| **RF-028** | El sistema debe validar que el nombre de perfil contenga únicamente caracteres alfabéticos. |
| **RF-029** | El sistema debe permitir modificar el número telefónico del usuario. |
| **RF-030** | El sistema debe validar que el número telefónico contenga exactamente 9 dígitos. |
| **RF-031** | El sistema debe permitir cargar una fotografía de perfil. |
| **RF-032** | El sistema debe validar que la fotografía de perfil no supere los 2MB de tamaño. |
| **RF-033** | El sistema debe comprimir la fotografía de perfil antes de almacenarla. |
| **RF-034** | El sistema debe permitir eliminar la fotografía de perfil. |
| **RF-035** | El sistema debe permitir solicitar la validación de identidad KYC (Persona Natural). |
| **RF-036** | El sistema debe permitir cargar una fotografía del anverso de la Cédula de Identidad. |
| **RF-037** | El sistema debe permitir cargar una fotografía del reverso de la Cédula de Identidad. |
| **RF-038** | El sistema debe validar que las imágenes de la cédula posean un formato de archivo compatible. |
| **RF-039** | El sistema debe extraer el RUT desde la fotografía del anverso mediante OCR. |
| **RF-040** | El sistema debe extraer el número de serie desde la fotografía mediante OCR. |
| **RF-041** | El sistema debe validar la vigencia de la cédula consultando la API del Registro Civil. |
| **RF-042** | El sistema debe cambiar el estado del perfil a "Verificado_KYC" si la consulta al Registro Civil es exitosa. |
| **RF-043** | El sistema debe rechazar la solicitud KYC si el documento se encuentra vencido. |
| **RF-044** | El sistema debe enviar una notificación push al usuario al finalizar la validación KYC. |
| **RF-045** | El sistema debe permitir solicitar la validación de identidad KYB (Empresa). |
| **RF-046** | El sistema debe permitir ingresar el RUT de la empresa. |
| **RF-047** | El sistema debe validar el dígito verificador del RUT ingresado. |
| **RF-048** | El sistema debe consultar el giro comercial de la empresa mediante la API del SII. |
| **RF-049** | El sistema debe rechazar la validación KYB si la empresa no posee inicio de actividades vigente. |
| **RF-050** | El sistema debe cambiar el estado del perfil a "Verificado_KYB" tras una consulta exitosa al SII. |
| **RF-051** | El sistema debe listar las validaciones KYC/KYB fallidas en un panel de administración. |
| **RF-052** | El sistema debe permitir a un administrador aprobar manualmente una validación de identidad. |
| **RF-053** | El sistema debe permitir a un administrador rechazar manualmente una validación de identidad. |
| **RF-054** | El sistema debe requerir que el administrador ingrese un motivo en texto al rechazar una validación. |
| **RF-055** | El sistema debe permitir registrar una cuenta bancaria asociada al perfil. |
| **RF-056** | El sistema debe validar que el RUT de la cuenta bancaria coincida con el RUT verificado del usuario. |
| **RF-057** | El sistema debe permitir solicitar la eliminación permanente de la cuenta de usuario. |
| **RF-058** | El sistema debe consultar la existencia de reservas activas al solicitar la eliminación de la cuenta. |
| **RF-059** | El sistema debe consultar la existencia de pagos pendientes al solicitar la eliminación de la cuenta. |
| **RF-060** | El sistema debe consultar la existencia de disputas abiertas al solicitar la eliminación de la cuenta. |
| **RF-061** | El sistema debe bloquear la eliminación de la cuenta si existe al menos un proceso (reserva, pago, disputa) activo. |
| **RF-062** | El sistema debe anonimizar los datos transaccionales del usuario tras aprobar su eliminación. |
| **RF-063** | El sistema debe eliminar los datos personales (nombre, teléfono, RUT) de la base de datos de manera irreversible. |
| **RF-064** | El sistema debe permitir acceder al panel de creación de publicaciones. |
| **RF-065** | El sistema debe bloquear el acceso al panel de creación de publicaciones a usuarios no verificados. |
| **RF-066** | El sistema debe permitir ingresar un título para la publicación. |
| **RF-067** | El sistema debe validar que el título de la publicación no exceda los 70 caracteres. |
| **RF-068** | El sistema debe permitir ingresar la descripción de la publicación. |
| **RF-069** | El sistema debe validar que la descripción de la publicación contenga al menos 100 caracteres. |
| **RF-070** | El sistema debe permitir ingresar la superficie total del inmueble en metros cuadrados. |
| **RF-071** | El sistema debe validar que la superficie ingresada sea un número entero mayor a cero. |
| **RF-072** | El sistema debe permitir seleccionar el tipo de inmueble desde una lista desplegable predefinida. |
| **RF-073** | El sistema debe permitir establecer la capacidad máxima de personas del inmueble. |
| **RF-074** | El sistema debe permitir agregar reglas de uso (ej. no ruido, no mascotas) a la publicación. |
| **RF-075** | El sistema debe permitir ingresar el precio base de arriendo por día. |
| **RF-076** | El sistema debe validar que el precio base ingresado sea mayor a $5.000 CLP. |
| **RF-077** | El sistema debe permitir cargar una fotografía a la galería de la publicación. |
| **RF-078** | El sistema debe validar que la cantidad de fotografías por publicación no exceda las 10 unidades. |
| **RF-079** | El sistema debe rechazar la carga de fotografías que superen los 5MB de tamaño. |
| **RF-080** | El sistema debe permitir seleccionar una fotografía como portada principal de la publicación. |
| **RF-081** | El sistema debe permitir eliminar una fotografía de la galería de la publicación. |
| **RF-082** | El sistema debe permitir ingresar la dirección física completa del inmueble. |
| **RF-083** | El sistema debe transformar la dirección física en coordenadas de latitud y longitud. |
| **RF-084** | El sistema debe guardar el estado de la publicación como "Borrador" de manera automática durante su creación. |
| **RF-085** | El sistema debe cambiar el estado de la publicación a "Activa" tras finalizar y confirmar el formulario de creación. |
| **RF-086** | El sistema debe generar un calendario de disponibilidad asociado a la publicación activa. |
| **RF-087** | El sistema debe permitir al arrendador bloquear fechas específicas en el calendario de su publicación. |
| **RF-088** | El sistema debe permitir al arrendador desbloquear fechas previamente bloqueadas manualmente. |
| **RF-089** | El sistema debe permitir modificar el título de una publicación existente. |
| **RF-090** | El sistema debe permitir modificar el precio base de una publicación existente. |
| **RF-091** | El sistema debe permitir cambiar el estado de una publicación activa a "Oculta". |
| **RF-092** | El sistema debe impedir la visualización pública de una publicación en estado "Oculta". |
| **RF-093** | El sistema debe permitir cambiar el estado de una publicación "Oculta" a "Activa". |
| **RF-094** | El sistema debe permitir eliminar permanentemente una publicación. |
| **RF-095** | El sistema debe rechazar la eliminación de una publicación si posee reservas futuras pendientes. |
| **RF-096** | El sistema debe permitir consultar la lista de todas las publicaciones del usuario (Mis Inmuebles). |
| **RF-097** | El sistema debe renderizar un mapa interactivo en la vista de búsqueda de espacios. |
| **RF-098** | El sistema debe desplegar pines en el mapa utilizando las coordenadas de las publicaciones activas. |
| **RF-099** | El sistema debe mostrar una cuadrícula de tarjetas con el resumen de las publicaciones disponibles. |
| **RF-100** | El sistema debe permitir buscar publicaciones ingresando un texto libre en una barra de búsqueda. |
| **RF-101** | El sistema debe permitir filtrar los resultados de búsqueda definiendo un precio mínimo. |
| **RF-102** | El sistema debe permitir filtrar los resultados de búsqueda definiendo un precio máximo. |
| **RF-103** | El sistema debe permitir filtrar los resultados de búsqueda seleccionando el tipo de inmueble. |
| **RF-104** | El sistema debe permitir filtrar los resultados de búsqueda ingresando una cantidad mínima de metros cuadrados. |
| **RF-105** | El sistema debe permitir filtrar los resultados de búsqueda seleccionando una fecha de inicio y una de fin. |
| **RF-106** | El sistema debe excluir de los resultados aquellas publicaciones que posean fechas bloqueadas o reservadas dentro del rango consultado. |
| **RF-107** | El sistema debe permitir limpiar todos los filtros de búsqueda aplicados simultáneamente. |
| **RF-108** | El sistema debe permitir consultar los detalles completos de una publicación al hacer clic en su tarjeta. |
| **RF-109** | El sistema debe calcular el costo total de la estadía multiplicando el precio base por la cantidad de días seleccionados. |
| **RF-110** | El sistema debe calcular el monto de la comisión de servicio (Fee) sobre el costo total de la estadía. |
| **RF-111** | El sistema debe calcular el monto de la garantía exigida (porcentaje definido por el arrendador) sobre el costo total. |
| **RF-112** | El sistema debe mostrar el desglose de cobro (Estadía + Comisión + Garantía) en el panel de cotización. |
| **RF-113** | El sistema debe permitir seleccionar las fechas de reserva dentro del detalle de la publicación. |
| **RF-114** | El sistema debe validar que la fecha de inicio seleccionada sea mayor a la fecha actual. |
| **RF-115** | El sistema debe validar que la fecha de fin sea mayor a la fecha de inicio. |
| **RF-116** | El sistema debe consultar en la base de datos la disponibilidad en tiempo real de las fechas seleccionadas al presionar "Reservar". |
| **RF-117** | El sistema debe rechazar el intento de reserva si la consulta en tiempo real detecta colisión de fechas. |
| **RF-118** | El sistema debe registrar un intento de reserva en estado "Pendiente de Pago" tras validar la disponibilidad. |
| **RF-119** | El sistema debe redirigir al usuario hacia la interfaz de la pasarela de pagos integrada. |
| **RF-120** | El sistema debe permitir ingresar el número de una Tarjeta de Crédito. |
| **RF-121** | El sistema debe permitir ingresar el código de seguridad (CVV) de la Tarjeta de Crédito. |
| **RF-122** | El sistema debe permitir ingresar el número de una Tarjeta de Débito. |
| **RF-123** | El sistema debe enviar el token de la tarjeta y los montos a la API de la pasarela de pagos. |
| **RF-124** | El sistema debe cambiar el estado de la reserva a "Pagada_Escrow" al recibir confirmación exitosa de la pasarela. |
| **RF-125** | El sistema debe retener temporalmente los fondos recaudados en la cuenta recaudadora principal (Escrow). |
| **RF-126** | El sistema debe ejecutar una solicitud de pre-autorización (bloqueo de cupo) en la tarjeta de crédito por el monto exacto de la garantía. |
| **RF-127** | El sistema debe cambiar el estado de la reserva a "Cancelada_Por_Pago" si la pasarela rechaza la transacción por fondos insuficientes. |
| **RF-128** | El sistema debe ejecutar un proceso en segundo plano que cancele las reservas en estado "Pendiente de Pago" tras 15 minutos de inactividad. |
| **RF-129** | El sistema debe notificar al arrendatario mediante correo electrónico cuando el pago sea exitoso. |
| **RF-130** | El sistema debe notificar al arrendador mediante correo electrónico sobre la recepción de una nueva solicitud pagada. |
| **RF-131** | El sistema debe mostrar las solicitudes de reserva entrantes en el panel del arrendador. |
| **RF-132** | El sistema debe permitir al arrendador aprobar una solicitud de reserva entrante. |
| **RF-133** | El sistema debe cambiar el estado de la reserva a "Aprobada_Host" tras la aprobación. |
| **RF-134** | El sistema debe permitir al arrendador rechazar una solicitud de reserva entrante. |
| **RF-135** | El sistema debe exigir al arrendador seleccionar un motivo de rechazo desde una lista predefinida. |
| **RF-136** | El sistema debe ejecutar automáticamente el reembolso total a la tarjeta del arrendatario tras el rechazo. |
| **RF-137** | El sistema debe cancelar automáticamente las solicitudes de reserva no respondidas por el arrendador en 24 horas. |
| **RF-138** | El sistema debe iniciar el proceso de generación de contrato tras la aprobación de la reserva por el arrendador. |
| **RF-139** | El sistema debe consultar los datos legales del arrendador (Nombre, RUT, Dirección) desde la base de datos. |
| **RF-140** | El sistema debe consultar los datos legales del arrendatario (Nombre, RUT, Dirección) desde la base de datos. |
| **RF-141** | El sistema debe consultar los detalles del inmueble (Dirección, Dimensiones) desde la base de datos. |
| **RF-142** | El sistema debe reemplazar las variables etiquetadas en la plantilla HTML del contrato con los datos extraídos. |
| **RF-143** | El sistema debe compilar el documento HTML y exportarlo en formato PDF. |
| **RF-144** | El sistema debe enviar el archivo PDF generado hacia el proveedor de firma electrónica externa. |
| **RF-145** | El sistema debe extraer los enlaces de firma únicos devueltos por la API de firma electrónica. |
| **RF-146** | El sistema debe enviar el enlace de firma correspondiente al correo electrónico del arrendatario. |
| **RF-147** | El sistema debe enviar el enlace de firma correspondiente al correo electrónico del arrendador. |
| **RF-148** | El sistema debe recibir notificaciones asíncronas (Webhooks) desde el proveedor de firma cada vez que un participante firme. |
| **RF-149** | El sistema debe cambiar el estado del contrato a "Firma_Parcial" tras recibir el primer Webhook de firma exitosa. |
| **RF-150** | El sistema debe descargar el documento PDF firmado y certificado tras recibir el Webhook de finalización. |
| **RF-151** | El sistema debe cifrar el documento PDF final antes de su almacenamiento. |
| **RF-152** | El sistema debe almacenar el documento PDF cifrado en un repositorio de archivos seguro. |
| **RF-153** | El sistema debe cambiar el estado de la reserva a "Lista_Para_Checkin" tras almacenar el contrato notariado. |
| **RF-154** | El sistema debe notificar a ambas partes que el contrato ha sido firmado exitosamente. |
| **RF-155** | El sistema debe ejecutar un trabajo programado diario (CronJob) para detectar reservas cuya fecha de inicio es igual a la fecha actual y no poseen el contrato firmado. |
| **RF-156** | El sistema debe cancelar automáticamente las reservas detectadas sin contrato firmado. |
| **RF-157** | El sistema debe reembolsar el pago retenido al arrendatario en caso de cancelación por falta de firmas. |
| **RF-158** | El sistema debe permitir al arrendatario consultar el contrato PDF descargándolo mediante una URL firmada temporal. |
| **RF-159** | El sistema debe habilitar el botón de "Check-in" en el panel del arrendatario únicamente el día de inicio de la reserva. |
| **RF-160** | El sistema debe requerir la carga de al menos una fotografía del inmueble para procesar el Check-in. |
| **RF-161** | El sistema debe registrar la fecha, hora y ubicación GPS del dispositivo al momento de procesar el Check-in. |
| **RF-162** | El sistema debe cambiar el estado de la reserva a "En_Curso" tras enviar el formulario de Check-in. |
| **RF-163** | El sistema debe notificar al arrendador que el arrendatario ha ingresado al inmueble. |
| **RF-164** | El sistema debe bloquear la posibilidad de realizar Check-in fuera de la fecha de inicio del arriendo. |
| **RF-165** | El sistema debe validar que las fotografías de Check-in tengan una resolución mínima de 720p. |
| **RF-166** | El sistema debe rechazar la carga de imágenes corruptas en el formulario de Check-in. |
| **RF-167** | El sistema debe permitir al arrendatario adjuntar comentarios de texto junto a cada foto de Check-in. |
| **RF-168** | El sistema debe ejecutar un temporizador de 24 horas a partir del fin de la estadía para el cobro o disputa. |
| **RF-169** | El sistema debe permitir al arrendador registrar un reclamo de daños ingresando texto descriptivo. |
| **RF-170** | El sistema debe exigir al arrendador cargar fotografías de evidencia para validar el reclamo. |
| **RF-171** | El sistema debe bloquear la ejecución del Payout y la liberación de la garantía al detectar un reclamo registrado. |
| **RF-172** | El sistema debe cambiar el estado de la reserva a "En_Disputa" tras el registro de un reclamo. |
| **RF-173** | El sistema debe notificar al arrendatario sobre la apertura de una disputa en su contra. |
| **RF-174** | El sistema debe permitir al arrendatario ingresar un texto de defensa asociado a la disputa. |
| **RF-175** | El sistema debe permitir al arrendatario adjuntar imágenes adicionales a su texto de defensa. |
| **RF-176** | El sistema debe listar todas las disputas en estado "En_Disputa" en el panel de administración. |
| **RF-177** | El sistema debe permitir al administrador consultar las fotos del Check-in vinculadas a la reserva en disputa. |
| **RF-178** | El sistema debe permitir al administrador consultar el contrato firmado vinculado a la reserva en disputa. |
| **RF-179** | El sistema debe permitir al administrador registrar un fallo a favor del arrendatario (Rechazar reclamo). |
| **RF-180** | El sistema debe permitir al administrador registrar un fallo a favor del arrendador (Aprobar reclamo). |
| **RF-181** | El sistema debe exigir al administrador ingresar el monto exacto a deducir de la garantía al fallar a favor del arrendador. |
| **RF-182** | El sistema debe cambiar el estado de la disputa a "Resuelta" tras el registro del fallo del administrador. |
| **RF-183** | El sistema debe consumir la API de la pasarela para hacer efectivo el cobro parcial sobre la pre-autorización de la garantía. |
| **RF-184** | El sistema debe consumir la API de la pasarela para liberar el saldo sobrante de la pre-autorización de la garantía. |
| **RF-185** | El sistema debe ejecutar el proceso de Payout automáticamente si transcurren las 24 horas de gracia sin reclamos. |
| **RF-186** | El sistema debe calcular el monto a transferir al arrendador (Monto total estadía - Comisión EspaciGo). |
| **RF-187** | El sistema debe consumir la API de transferencia para enviar el dinero a la cuenta bancaria del arrendador. |
| **RF-188** | El sistema debe consumir la API de la pasarela para liberar el 100% de la pre-autorización de la garantía. |
| **RF-189** | El sistema debe notificar al arrendador sobre la transferencia exitosa de sus fondos. |
| **RF-190** | El sistema debe generar la boleta electrónica correspondiente a la comisión cobrada por EspaciGo. |
| **RF-191** | El sistema debe enviar la boleta electrónica en formato PDF al correo del arrendatario. |
| **RF-192** | El sistema debe cambiar el estado de la reserva a "Cerrada" tras la ejecución exitosa del Payout. |
| **RF-193** | El sistema debe capturar cada acción transaccional (login, reserva, pago, firma, eliminación) generada en la plataforma. |
| **RF-194** | El sistema debe empaquetar los datos transaccionales en una estructura de datos estandarizada. |
| **RF-195** | El sistema debe enviar la estructura de datos a una cola de mensajes asíncrona para auditoría. |
| **RF-196** | El sistema debe almacenar los registros transaccionales en un repositorio de datos de solo lectura. |
| **RF-197** | El sistema debe denegar cualquier petición de modificación sobre los registros de auditoría. |
| **RF-198** | El sistema debe denegar cualquier petición de eliminación sobre los registros de auditoría. |
| **RF-199** | El sistema debe permitir al administrador consultar el historial inmutable de un usuario filtrando por su RUT. |
| **RF-200** | El sistema debe exportar los resultados de la consulta de auditoría en un formato de hoja de cálculo estructurado para reportes legales. |
