# Catálogo Consolidado de Requerimientos Funcionales (RQF)

## Sistema EspaciGo

| ID | Descripción del Requerimiento Funcional |
| :--- | :--- |
| RQF-001 | El sistema debe permitir registrar una cuenta de usuario. |
| RQF-002 | El sistema debe validar que el correo electrónico ingresado posea un formato válido. |
| RQF-003 | El sistema debe validar que la contraseña posea un mínimo de 8 caracteres. |
| RQF-004 | El sistema debe validar que la contraseña posea al menos una letra mayúscula. |
| RQF-005 | El sistema debe validar que la contraseña posea al menos un número. |
| RQF-006 | El sistema debe validar que la contraseña posea al menos un carácter especial. |
| RQF-007 | El sistema debe rechazar el registro si el correo electrónico ya existe en la plataforma. |
| RQF-008 | El sistema debe enviar un correo electrónico con un token de verificación tras el registro. |
| RQF-009 | El sistema debe cambiar el estado de la cuenta a "Verificado" al confirmar el correo electrónico. |
| RQF-010 | El sistema debe bloquear el inicio de sesión para cuentas en estado "No Verificado". |
| RQF-011 | El sistema debe permitir iniciar sesión. |
| RQF-012 | El sistema debe validar las credenciales ingresadas durante el inicio de sesión. |
| RQF-013 | El sistema debe rechazar el inicio de sesión si las credenciales son incorrectas. |
| RQF-014 | El sistema debe incrementar un contador de intentos fallidos al rechazar un inicio de sesión. |
| RQF-015 | El sistema debe bloquear la cuenta de usuario al alcanzar 5 intentos fallidos consecutivos. |
| RQF-016 | El sistema debe enviar un correo de alerta de seguridad al bloquear una cuenta. |
| RQF-017 | El sistema debe liberar automáticamente una cuenta bloqueada tras 30 minutos. |
| RQF-018 | El sistema debe generar una sesión temporal tras un inicio de sesión exitoso. |
| RQF-019 | El sistema debe permitir solicitar la recuperación de contraseña. |
| RQF-020 | El sistema debe enviar un enlace único de recuperación al correo electrónico. |
| RQF-021 | El sistema debe expirar el enlace de recuperación tras 15 minutos de su emisión. |
| RQF-022 | El sistema debe permitir actualizar la contraseña utilizando el enlace de recuperación. |
| RQF-023 | El sistema debe permitir cerrar la sesión activa. |
| RQF-024 | El sistema debe permitir consultar los datos del perfil de usuario. |
| RQF-025 | El sistema debe permitir modificar el nombre de perfil del usuario. |
| RQF-026 | El sistema debe validar que el nombre de perfil contenga únicamente caracteres alfabéticos y espacios. |
| RQF-027 | El sistema debe permitir modificar el número telefónico del usuario. |
| RQF-028 | El sistema debe validar que el número telefónico contenga exactamente 9 dígitos. |
| RQF-029 | El sistema debe permitir cargar una fotografía de perfil. |
| RQF-030 | El sistema debe validar que la fotografía de perfil no supere los 2MB de tamaño. |
| RQF-031 | El sistema debe permitir eliminar la fotografía de perfil. |
| RQF-032 | El sistema debe permitir registrar una cuenta bancaria asociada al perfil. |
| RQF-033 | El sistema debe validar que el RUT de la cuenta bancaria coincida con el RUT del usuario. |
| RQF-034 | El sistema debe permitir solicitar la eliminación de la cuenta de usuario. |
| RQF-035 | El sistema debe rechazar la eliminación de la cuenta si existen reservas activas. |
| RQF-036 | El sistema debe rechazar la eliminación de la cuenta si existen pagos pendientes. |
| RQF-037 | El sistema debe rechazar la eliminación de la cuenta si existen disputas abiertas. |
| RQF-038 | El sistema debe permitir solicitar la validación de identidad KYC (Persona Natural). |
| RQF-039 | El sistema debe permitir cargar una fotografía del anverso de la Cédula de Identidad. |
| RQF-040 | El sistema debe permitir cargar una fotografía del reverso de la Cédula de Identidad. |
| RQF-041 | El sistema debe validar que las imágenes de la cédula posean un formato compatible. |
| RQF-042 | El sistema debe extraer el RUT desde la fotografía del anverso. |
| RQF-043 | El sistema debe extraer el número de serie desde la fotografía. |
| RQF-044 | El sistema debe validar la vigencia de la cédula ante el organismo correspondiente. |
| RQF-045 | El sistema debe cambiar el estado del perfil a "Verificado _KYC" tras una validación exitosa. |
| RQF-046 | El sistema debe rechazar la solicitud KYC si el documento se encuentra vencido. |
| RQF-047 | El sistema debe notificar al usuario el resultado de su validación KYC. |
| RQF-048 | El sistema debe permitir solicitar la validación de identidad KYB (Empresa). |
| RQF-049 | El sistema debe permitir ingresar el RUT de la empresa. |
| RQF-050 | El sistema debe validar el dígito verificador del RUT ingresado. |
| RQF-051 | El sistema debe consultar el inicio de actividades de la empresa. |
| RQF-052 | El sistema debe rechazar la validación KYB si la empresa no posee inicio de actividades. |
| RQF-053 | El sistema debe cambiar el estado del perfil a "Verificado_KYB" tras una validación exitosa. |
| RQF-054 | El sistema debe permitir al administrador consultar el listado de validaciones fallidas. |
| RQF-055 | El sistema debe permitir al administrador aprobar manualmente una validación de identidad. |
| RQF-056 | El sistema debe permitir al administrador rechazar manualmente una validación de identidad. |
| RQF-057 | El sistema debe exigir al administrador ingresar un motivo al rechazar una validación. |
| RQF-058 | El sistema debe permitir al usuario modificar los antecedentes rechazados de una validación. |
| RQF-059 | El sistema debe permitir al usuario solicitar un nuevo intento de validación. |
| RQF-060 | El sistema debe permitir acceder al panel de creación de publicaciones. |
| RQF-061 | El sistema debe bloquear el panel de creación de publicaciones a usuarios no verificados. |
| RQF-062 | El sistema debe permitir ingresar un título para la publicación. |
| RQF-063 | El sistema debe validar que el título no exceda los 70 caracteres. |
| RQF-064 | El sistema debe permitir ingresar la descripción de la publicación. |
| RQF-065 | El sistema debe validar que la descripción contenga al menos 100 caracteres. |
| RQF-066 | El sistema debe permitir ingresar la superficie total del inmueble en metros cuadrados. |
| RQF-067 | El sistema debe validar que la superficie ingresada sea un número mayor a cero. |
| RQF-068 | El sistema debe permitir seleccionar el tipo de inmueble. |
| RQF-069 | El sistema debe permitir establecer la capacidad máxima de personas. |
| RQF-070 | El sistema debe permitir agregar reglas de uso a la publicación. |
| RQF-071 | El sistema debe permitir configurar la modalidad tarifaria (por hora, día o mes). |
| RQF-072 | El sistema debe permitir ingresar el precio base del arriendo. |
| RQF-073 | El sistema debe validar que el precio base ingresado sea mayor a \$5.000 CLP. |
| RQF-074 | El sistema debe permitir cargar fotografías a la galería de la publicación. |
| RQF-075 | El sistema debe validar que la galería no exceda las 10 fotografías. |
| RQF-076 | El sistema debe rechazar la carga de fotografías que superen los 5MB. |
| RQF-077 | El sistema debe permitir seleccionar una fotografía como portada. |
| RQF-078 | El sistema debe permitir eliminar una fotografía de la galería. |
| RQF-079 | El sistema debe permitir ingresar la dirección física completa del inmueble. |
| RQF-080 | El sistema debe registrar la ubicación geográfica a partir de la dirección ingresada. |
| RQF-081 | El sistema debe asignar el estado "Borrador" automáticamente durante la creación. |
| RQF-082 | El sistema debe cambiar el estado a "Activa" al confirmar la creación. |
| RQF-083 | El sistema debe generar un calendario de disponibilidad para la publicación. |
| RQF-084 | El sistema debe permitir al arrendador bloquear fechas en el calendario. |
| RQF-085 | El sistema debe permitir al arrendador desbloquear fechas manualmente. |
| RQF-086 | El sistema debe permitir modificar el título de una publicación existente. |
| RQF-087 | El sistema debe permitir modificar el precio base de una publicación existente. |
| RQF-088 | El sistema debe permitir cambiar el estado de una publicación activa a "Oculta". |
| RQF-089 | El sistema debe ocultar en los resultados públicos las publicaciones en estado "Oculta". |
| RQF-090 | El sistema debe permitir cambiar el estado de una publicación "Oculta" a "Activa". |
| RQF-091 | El sistema debe permitir eliminar permanentemente una publicación. |
| RQF-092 | El sistema debe rechazar la eliminación de una publicación si posee reservas futuras pendientes. |
| RQF-093 | El sistema debe permitir al usuario consultar su listado de publicaciones. |
| RQF-094 | El sistema debe permitir buscar publicaciones ingresando texto en una barra de búsqueda. |
| RQF-095 | El sistema debe renderizar un mapa interactivo con las ubicaciones de los espacios. |
| RQF-096 | El sistema debe mostrar una cuadrícula de tarjetas con el resumen de las publicaciones. |
| RQF-097 | El sistema debe permitir filtrar los resultados de búsqueda por precio mínimo y máximo. |
| RQF-098 | El sistema debe permitir filtrar los resultados seleccionando el tipo de inmueble. |
| RQF-099 | El sistema debe permitir filtrar los resultados por cantidad mínima de metros cuadrados. |
| RQF-100 | El sistema debe permitir filtrar los resultados seleccionando un rango de fechas. |
| RQF-101 | El sistema debe excluir de los resultados las publicaciones sin disponibilidad en las fechas consultadas. |
| RQF-102 | El sistema debe permitir limpiar todos los filtros de búsqueda aplicados. |
| RQF-103 | El sistema debe permitir consultar los detalles completos de una publicación. |
| RQF-104 | El sistema debe calcular el costo total multiplicando el precio base por el tiempo seleccionado. |
| RQF-105 | El sistema debe calcular el monto de la comisión de servicio sobre el costo total. |
| RQF-106 | El sistema debe calcular el monto de la garantía exigida sobre el costo total. |
| RQF-107 | El sistema debe mostrar el desglose de cobro (Estadía + Comisión + Garantía). |
| RQF-108 | El sistema debe permitir seleccionar las fechas/horas de reserva en la publicación. |
| RQF-109 | El sistema debe validar que la fecha de inicio seleccionada sea posterior a la fecha actual. |
| RQF-110 | El sistema debe validar que la fecha de fin sea posterior a la fecha de inicio. |
| RQF-111 | El sistema debe validar la disponibilidad del espacio para el intervalo solicitado. |
| RQF-112 | El sistema debe rechazar la reserva si existe superposición temporal con otra reserva o bloqueo. |
| RQF-113 | El sistema debe registrar la reserva en estado "Pendiente de Pago" al confirmar disponibilidad. |
| RQF-114 | El sistema debe permitir al usuario seleccionar un método de pago mediante la pasarela integrada. |
| RQF-115 | El sistema debe iniciar el flujo de cobro comunicándose con la pasarela de pagos. |
| RQF-116 | El sistema debe cambiar el estado de la reserva a "Pagada" al recibir confirmación exitosa. |
| RQF-117 | El sistema debe mantener retenidos los fondos de la reserva hasta que se cumplan las condiciones de liberación. |
| RQF-118 | El sistema debe realizar una pre-autorización por el monto de la garantía. |
| RQF-119 | El sistema debe cambiar el estado a "Cancelada_Por_Pago" si la pasarela rechaza la transacción. |
| RQF-120 | El sistema debe cancelar automáticamente las reservas "Pendientes de Pago" tras 15 minutos sin completarse. |
| RQF-121 | El sistema debe notificar al arrendatario cuando el pago sea procesado. |
| RQF-122 | El sistema debe notificar al arrendador sobre la recepción de una nueva solicitud pagada. |
| RQF-123 | El sistema debe permitir al arrendador consultar las solicitudes de reserva entrantes. |
| RQF-124 | El sistema debe permitir al arrendador aprobar una solicitud de reserva. |
| RQF-125 | El sistema debe cambiar el estado de la reserva a "Aprobada_Host" tras la aprobación. |
| RQF-126 | El sistema debe permitir al arrendador rechazar una solicitud de reserva. |
| RQF-127 | El sistema debe exigir al arrendador seleccionar un motivo al rechazar una solicitud. |
| RQF-128 | El sistema debe ejecutar el reembolso total al arrendatario tras el rechazo del arrendador. |
| RQF-129 | El sistema debe cancelar las solicitudes no respondidas por el arrendador en un plazo de 24 horas. |
| RQF-130 | El sistema debe iniciar la generación del contrato tras la aprobación de la reserva. |
| RQF-131 | El sistema debe consultar los datos legales de las partes involucradas y del inmueble. |
| RQF-132 | El sistema debe generar un documento de contrato incorporando los datos extraídos. |
| RQF-133 | El sistema debe enviar el documento al proveedor de firma electrónica externa. |
| RQF-134 | El sistema debe enviar el enlace de firma correspondiente al arrendatario. |
| RQF-135 | El sistema debe enviar el enlace de firma correspondiente al arrendador. |
| RQF-136 | El sistema debe cambiar el estado a "Firma_Parcial" tras recibir la confirmación de la primera firma. |
| RQF-137 | El sistema debe almacenar el contrato final asociado a la reserva tras la confirmación de todas las firmas. |
| RQF-138 | El sistema debe cambiar el estado a "Lista_Para_Checkin" tras el almacenamiento del contrato. |
| RQF-139 | El sistema debe notificar a las partes cuando el contrato esté completamente firmado. |
| RQF-140 | El sistema debe cancelar las reservas que alcancen su fecha de inicio sin poseer el contrato firmado. |
| RQF-141 | El sistema debe reembolsar el pago al arrendatario en caso de cancelación por falta de firmas. |
| RQF-142 | El sistema debe permitir a las partes descargar el contrato firmado. |
| RQF-143 | El sistema debe habilitar la opción de "Check-in" únicamente el día de inicio de la reserva. |
| RQF-144 | El sistema debe bloquear la posibilidad de realizar Check-in fuera de la fecha de inicio. |
| RQF-145 | El sistema debe permitir al arrendatario cargar fotografías en el formulario de Check-in. |
| RQF-146 | El sistema debe permitir al arrendatario ingresar comentarios de texto en el formulario de Check-in. |
| RQF-147 | El sistema debe registrar la fecha y ubicación al procesar el Check-in. |
| RQF-148 | El sistema debe cambiar el estado de la reserva a "En_Curso" tras procesar el Check-in. |
| RQF-149 | El sistema debe notificar al arrendador cuando el arrendatario procese el Check-in. |
| RQF-150 | El sistema debe permitir al arrendatario registrar el Check-out de la reserva. |
| RQF-151 | El sistema debe permitir cargar fotografías en el formulario de Check-out. |
| RQF-152 | El sistema debe cambiar el estado de la reserva a "Finalizada" al registrar el Check-out. |
| RQF-153 | El sistema debe permitir al arrendatario registrar una calificación numérica del espacio. |
| RQF-154 | El sistema debe permitir al arrendatario registrar una reseña de texto del espacio. |
| RQF-155 | El sistema debe mostrar las reseñas y calificaciones en la vista de detalle de la publicación. |
| RQF-156 | El sistema debe permitir al arrendatario enviar mensajes en el chat de la reserva. |
| RQF-157 | El sistema debe permitir al arrendador enviar mensajes en el chat de la reserva. |
| RQF-158 | El sistema debe permitir a las partes consultar el historial de mensajes de la reserva. |
| RQF-159 | El sistema debe habilitar el período de 24 horas posteriores al término de la reserva para registrar reclamos. |
| RQF-160 | El sistema debe permitir al arrendador registrar un reclamo adjuntando texto descriptivo. |
| RQF-161 | El sistema debe exigir al arrendador cargar fotografías de evidencia en el reclamo. |
| RQF-162 | El sistema debe bloquear la liberación de fondos de una reserva al detectar un reclamo registrado. |
| RQF-163 | El sistema debe cambiar el estado de la reserva a "En_Disputa" tras el registro de un reclamo. |
| RQF-164 | El sistema debe notificar al arrendatario sobre la apertura de una disputa. |
| RQF-165 | El sistema debe permitir al arrendatario ingresar texto y fotografías de defensa. |
| RQF-166 | El sistema debe permitir al administrador consultar el listado de disputas abiertas. |
| RQF-167 | El sistema debe permitir al administrador consultar las fotos de Check-in y Check-out vinculadas a la disputa. |
| RQF-168 | El sistema debe permitir al administrador registrar un fallo a favor del arrendatario. |
| RQF-169 | El sistema debe permitir al administrador registrar un fallo a favor del arrendador. |
| RQF-170 | El sistema debe exigir al administrador ingresar el monto a deducir de la garantía al fallar a favor del arrendador. |
| RQF-171 | El sistema debe cambiar el estado de la disputa a "Resuelta" tras el fallo del administrador. |
| RQF-172 | El sistema debe iniciar la liquidación (Payout) si transcurren las 24 horas de gracia sin reclamos. |
| RQF-173 | El sistema debe transferir el monto de la estadía (menos comisiones) a la cuenta bancaria del arrendador. |
| RQF-174 | El sistema debe ejecutar el cobro de la pre-autorización de garantía cuando el fallo exija compensación. |
| RQF-175 | El sistema debe liberar el saldo de garantía restante al arrendatario tras aplicar posibles deducciones. |
| RQF-176 | El sistema debe generar la boleta electrónica por la comisión cobrada. |
| RQF-177 | El sistema debe cambiar el estado de la reserva a "Cerrada" tras la ejecución exitosa de la liquidación. |
| RQF-178 | El sistema debe permitir al administrador bloquear el acceso a una cuenta de usuario. |
| RQF-179 | El sistema debe permitir al administrador desbloquear una cuenta de usuario. |
| RQF-180 | El sistema debe permitir al administrador consultar el motivo de bloqueo de una cuenta. |
| RQF-181 | El sistema debe permitir al administrador ocultar una reseña reportada. |
| RQF-182 | El sistema debe exigir al administrador registrar un motivo al ocultar una reseña. |
| RQF-183 | El sistema debe permitir al administrador generar reportes de reservas, pagos y disputas. |
| RQF-184 | El sistema debe permitir al administrador consultar el historial de auditoría de un usuario filtrando por RUT. |
| RQF-185 | El sistema debe permitir al administrador exportar los registros de auditoría consultados. |