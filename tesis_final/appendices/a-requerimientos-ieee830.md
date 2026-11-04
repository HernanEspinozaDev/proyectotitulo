# ANEXO A: ESPECIFICACIÓN DETALLADA DE REQUERIMIENTOS (IEEE 830)

## Catálogo Consolidado de Requerimientos Funcionales (RQF)

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
| RQF-095 | El sistema debe mostrar un mapa interactivo con las ubicaciones de los espacios. |
| RQF-096 | El sistema debe mostrar una cuadrícula de tarjetas con el resumen de las publicaciones. |
| RQF-097 | El sistema debe permitir buscar a través de filtros de rango de precio. |
| RQF-098 | El sistema debe permitir buscar a través de filtros de tipo de inmueble. |
| RQF-099 | El sistema debe permitir buscar a través de filtros de superficie mínima. |
| RQF-100 | El sistema debe permitir buscar a través de filtros de rango de fechas. |
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
| RQF-118 | El sistema debe ejecutar una pre-autorización por el monto de la garantía. |
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
| RQF-144 | El sistema debe bloquear el Check-in fuera de la fecha de inicio de la reserva. |
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
| RQF-159 | El sistema debe habilitar el registro de reclamos durante las 24 horas posteriores al término de la reserva. |
| RQF-160 | El sistema debe permitir al arrendador registrar un reclamo adjuntando texto descriptivo. |
| RQF-161 | El sistema debe exigir al arrendador cargar fotografías de evidencia en el reclamo. |
| RQF-162 | El sistema debe bloquear la liberación de fondos de una reserva al detectar un reclamo registrado. |
| RQF-163 | El sistema debe cambiar el estado de la reserva a "En_Disputa" tras el registro de un reclamo. |
| RQF-164 | El sistema debe notificar al arrendatario sobre la apertura de una disputa. |
| RQF-165 | El sistema debe permitir al arrendatario ingresar texto y fotografías de defensa. |
| RQF-166 | El sistema debe permitir al administrador consultar el listado de disputas abiertas. |
| RQF-167 | El sistema debe permitir al administrador consultar la evidencia fotográfica vinculada a la disputa. |
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
| RQF-183 | El sistema debe permitir al administrador generar reportes de gestión de la plataforma. |
| RQF-184 | El sistema debe permitir al administrador consultar el historial de auditoría de un usuario filtrando por RUT. |
| RQF-185 | El sistema debe permitir al administrador exportar los registros de auditoría consultados. |

---

## Requerimientos funcionales complementarios (revisión de completitud)

> Estos **27 requerimientos (RQF-186 a RQF-212)** se incorporaron en la revisión de completitud del catálogo para cerrar brechas detectadas entre los RF originales (RQF-001 a RQF-185), el contexto narrativo, las Historias de Usuario aprobadas y los casos de uso.
>
> **Regla de trazabilidad aplicada:** se agregan con IDs nuevos **al final** del catálogo. Ningún requerimiento anterior fue renumerado, reescrito ni eliminado, por lo que todas las referencias existentes (informe, módulos, casos de uso, HU) siguen siendo válidas.

| ID | Descripción del Requerimiento Funcional |
| :--- | :--- |
| RQF-186 | El sistema debe exigir la aceptación de los términos y condiciones durante el registro de la cuenta. |
| RQF-187 | El sistema debe registrar la fecha y la versión de los términos y condiciones aceptados. |
| RQF-188 | El sistema debe permitir reenviar el correo de verificación de la cuenta. |
| RQF-189 | El sistema debe permitir consultar la cuenta bancaria registrada en el perfil. |
| RQF-190 | El sistema debe permitir modificar la cuenta bancaria asociada al perfil. |
| RQF-191 | El sistema debe permitir eliminar la cuenta bancaria asociada al perfil. |
| RQF-192 | El sistema debe permitir capturar una fotografía tipo selfie durante la validación KYC. |
| RQF-193 | El sistema debe permitir consultar el estado de la validación de identidad. |
| RQF-194 | El sistema debe notificar al usuario el resultado de su validación KYB. |
| RQF-195 | El sistema debe permitir modificar la descripción de una publicación existente. |
| RQF-196 | El sistema debe permitir modificar las reglas de uso de una publicación existente. |
| RQF-197 | El sistema debe permitir modificar la capacidad máxima de una publicación existente. |
| RQF-198 | El sistema debe permitir modificar la modalidad tarifaria de una publicación existente. |
| RQF-199 | El sistema debe permitir consultar el historial de reservas asociadas al usuario. |
| RQF-200 | El sistema debe liberar las fechas bloqueadas al cancelar una reserva. |
| RQF-201 | El sistema debe notificar al arrendatario cuando el pago sea rechazado. |
| RQF-202 | El sistema debe registrar el rechazo de firma notificado por el proveedor de firma electrónica. |
| RQF-203 | El sistema debe exigir la carga de al menos una fotografía para procesar el Check-in. |
| RQF-204 | El sistema debe exigir la carga de al menos una fotografía para registrar el Check-out. |
| RQF-205 | El sistema debe permitir al arrendador confirmar la recepción del espacio tras el Check-out. |
| RQF-206 | El sistema debe registrar la fecha y la ubicación al confirmar la recepción del espacio. |
| RQF-207 | El sistema debe permitir reportar una reseña publicada. |
| RQF-208 | El sistema debe liberar la totalidad de la garantía al arrendatario cuando la reserva finalice sin reclamos. |
| RQF-209 | El sistema debe permitir al administrador consultar la confirmación de recepción vinculada a la disputa. |
| RQF-210 | El sistema debe notificar el resultado de la disputa a las partes. |
| RQF-211 | El sistema debe enviar la boleta electrónica al correo del arrendador. |
| RQF-212 | El sistema debe permitir al administrador buscar una cuenta de usuario. |

### Brechas cerradas y módulo al que se incorpora cada RF

| Brecha detectada | RF agregados | Módulo |
| :--- | :--- | :--- |
| No existía requerimiento de aceptación de términos y condiciones (ejemplo explícito señalado en la retroalimentación). | RQF-186, RQF-187 | M01 |
| El flujo alternativo "reenviar token de verificación" (CU-02) no tenía RF que lo respaldara. | RQF-188 | M01 |
| La entidad "cuenta bancaria" solo tenía la operación de registro (RQF-032, RQF-033): faltaban consultar, modificar y eliminar. | RQF-189, RQF-190, RQF-191 | M02 |
| La HU04 contempla la captura de selfie de validación facial, sin RF asociado. | RQF-192 | M03 |
| El paso "consultar el estado de la validación" (CU-14) no tenía RF. | RQF-193 | M03 |
| Asimetría: el resultado de la validación se notificaba solo para KYC (RQF-047), no para KYB. | RQF-194 | M03 |
| La HU06 permite editar descripción, reglas de uso, capacidad y tarifas, pero el catálogo solo permitía editar título (RQF-086) y precio base (RQF-087). | RQF-195, RQF-196, RQF-197, RQF-198 | M04 |
| No existía RF para consultar las reservas del usuario, pese a ser precondición de CU-24, CU-26, CU-33, CU-34 y CU-42. | RQF-199 | M06 |
| Las cancelaciones automáticas (CU-27, CU-28) liberaban las fechas sin RF que lo declarara. | RQF-200 | M06 |
| El rechazo del pago cambiaba de estado (RQF-119) sin notificar al arrendatario. | RQF-201 | M06 |
| El escenario "una parte no firma" (CU-30) no tenía RF que registrara el rechazo notificado por el proveedor. | RQF-202 | M07 |
| La obligatoriedad de evidencia fotográfica en Check-in y Check-out había quedado fuera del catálogo. | RQF-203, RQF-204 | M08 |
| **El arrendador no tenía ninguna acción al término de la reserva** (brecha reportada en la revisión). | RQF-205, RQF-206 | M08 |
| RQF-181 presupone reseñas reportadas, pero no existía RF que permitiera reportar una reseña. | RQF-207 | M09 |
| **No existía RF de liberación de la garantía en el flujo sin reclamos** (solo RQF-175 "saldo restante tras deducciones"). | RQF-208 | M10 |
| El administrador no tenía RF para consultar la evidencia de recepción del arrendador al arbitrar (simetría con RQF-167). | RQF-209 | M10 |
| Solo existía la notificación de apertura de disputa (RQF-164), no la del resultado. | RQF-210 | M10 |
| La boleta electrónica solo se generaba (RQF-176); no se enviaba al arrendador. | RQF-211 | M10 |
| Bloquear/desbloquear una cuenta (RQF-178 a RQF-180) requiere localizarla previamente. | RQF-212 | M11 |

**Catálogo total resultante: 212 requerimientos funcionales (RQF-001 a RQF-212).**

---

## Requerimientos funcionales complementarios — Segunda revisión (Historias de Usuario)

> Estos **24 requerimientos (RQF-213 a RQF-236)** se incorporaron al revisar íntegramente las 30 Historias de Usuario. Su objetivo es que **ninguna HU quede con criterios de aceptación sin respaldo funcional**, y al mismo tiempo se corrigieron en las HU todas las contradicciones numéricas y de alcance detectadas.
>
> Se mantiene la regla de trazabilidad: **IDs nuevos al final**, sin renumerar ni modificar los requerimientos anteriores.

| ID | Descripción del Requerimiento Funcional |
| :--- | :--- |
| RQF-213 | El sistema debe registrar la preferencia de uso del usuario durante el registro de la cuenta. |
| RQF-214 | El sistema debe permitir al usuario autenticado cambiar su contraseña. |
| RQF-215 | El sistema debe validar la contraseña actual al solicitar un cambio de contraseña. |
| RQF-216 | El sistema debe rechazar una contraseña nueva igual a la contraseña actual. |
| RQF-217 | El sistema debe rechazar una contraseña nueva utilizada en los últimos 3 meses. |
| RQF-218 | El sistema debe notificar al usuario el cambio de contraseña realizado. |
| RQF-219 | El sistema debe validar que las imágenes de la cédula no superen los 10MB. |
| RQF-220 | El sistema debe cambiar el estado del perfil a "Pendiente de Verificación" al recibir los documentos de identidad. |
| RQF-221 | El sistema debe validar que el precio base modificado sea mayor a \$5.000 CLP. |
| RQF-222 | El sistema debe validar que la regla de uso personalizada no exceda los 250 caracteres. |
| RQF-223 | El sistema debe permitir configurar la política de cancelación de la publicación. |
| RQF-224 | El sistema debe mostrar las reglas de uso y la política de cancelación en el detalle de la publicación. |
| RQF-225 | El sistema debe exigir un motivo al registrar un bloqueo manual de fechas. |
| RQF-226 | El sistema debe validar que la fecha de término del bloqueo manual sea posterior a la fecha de inicio. |
| RQF-227 | El sistema debe rechazar la reserva si el usuario no cuenta con su identidad verificada. |
| RQF-228 | El sistema debe permitir al arrendatario cancelar una reserva conforme a la política de cancelación. |
| RQF-229 | El sistema debe calcular el monto a reembolsar según la política de cancelación aplicada. |
| RQF-230 | El sistema debe ejecutar el reembolso al arrendatario tras la cancelación de la reserva. |
| RQF-231 | El sistema debe notificar a las partes la cancelación de la reserva. |
| RQF-232 | El sistema debe permitir al arrendador registrar una calificación numérica del arrendatario. |
| RQF-233 | El sistema debe permitir al arrendador registrar una reseña de texto del arrendatario. |
| RQF-234 | El sistema debe rechazar el registro de una segunda reseña para la misma reserva. |
| RQF-235 | El sistema debe calcular el promedio de calificaciones del espacio. |
| RQF-236 | El sistema debe permitir al administrador consultar el listado de espacios publicados. |

### Brechas cerradas en la revisión de las HU

| HU que lo exigía | Brecha detectada | RF agregados | Módulo |
| :--- | :--- | :--- | :--- |
| HU01 | La HU pedía seleccionar el perfil principal (Arrendador/Arrendatario) y no existía RF. Se redefine como **preferencia de uso no excluyente**. | RQF-213 | M01 |
| HU03 | La HU describía el **cambio de contraseña con sesión iniciada**, que no existía en el catálogo (solo la recuperación), junto con sus validaciones (contraseña actual, no repetir la anterior, no reutilizar en 3 meses) y la notificación del cambio. | RQF-214 a RQF-218 | M01 |
| HU04 | La HU definía un **límite de 10 MB** por documento y un estado **"Pendiente de Verificación"** inexistentes en el catálogo. | RQF-219, RQF-220 | M03 |
| HU06 | La HU validaba la tarifa al **modificar** la publicación; el catálogo solo validaba el precio al crearla (RQF-073). | RQF-221 | M04 |
| HU07 | La HU definía un **máximo de 250 caracteres** para reglas personalizadas y la existencia de una **política de cancelación** configurable y visible en el detalle. | RQF-222, RQF-223, RQF-224 | M04 |
| HU21 | La HU exigía **motivo obligatorio** y validación de fechas en el bloqueo manual del calendario. | RQF-225, RQF-226 | M04 |
| HU17 | La HU exigía validar la **identidad verificada antes de pagar**; el caso de uso lo declaraba como precondición sin RF que lo respaldara. | RQF-227 | M06 |
| HU19 | La HU describía la **cancelación de la reserva por el arrendatario** con cálculo de devolución, ejecución del reembolso y notificación a las partes. El catálogo solo contemplaba el rechazo del arrendador, la expiración por falta de pago y la falta de firma. | RQF-228 a RQF-231 | M06 |
| HU25 | La HU pedía **calificación y reseña recíproca** (arrendador hacia arrendatario), el bloqueo de una segunda reseña por reserva y el recálculo del promedio de calificaciones. | RQF-232 a RQF-235 | M09 |
| HU26 | La HU requería que el administrador pudiera **consultar el listado de espacios publicados** para su supervisión. | RQF-236 | M11 |

**Catálogo total resultante: 236 requerimientos funcionales (RQF-001 a RQF-236).**

---

## Requerimientos No Funcionales (RNF) — Sistema EspaciGo

> **Versión corregida (19-09-2026).** Catálogo de **43 requerimientos no funcionales (RNF-001 a RNF-043)**, clasificados según categorías y subcategorías del estándar **ISO/IEC 25010** y del modelo de Sommerville.

**Convenciones aplicadas**

1. **Redacción estándar:** todos los RNF se redactan como **"El sistema debe [condición de calidad]"**, evitando verbos de acción funcional (los verbos de función pertenecen al catálogo de RF). Excepción controlada: los RNF de *Implementación / Gestión de configuración*, redactados como *"El código fuente debe almacenarse..."*, siguiendo el formato de referencia entregado en la retroalimentación.
2. **Categoría y subcategoría:** cada RNF declara su categoría principal (en negrita en la sección de resumen) y su subcategoría específica.
3. **Mínimo 3 ejemplos por categoría:** todas las categorías declaradas tienen al menos 3 requerimientos (ver sección de resumen).
4. **Separación RF/RNF:** los RNF describen *condiciones de calidad, restricciones o cumplimiento*. Las acciones del sistema (registrar, generar, ejecutar, notificar, etc.) están exclusivamente en el catálogo de RF. Se corrigieron los RNF que contenían acciones funcionales (RNF-002, RNF-003, RNF-004 y RNF-027) y se separaron los que mezclaban dos condiciones distintas (RNF-012 y RNF-018).
5. **Sin duplicación de RF:** ningún RNF reemplaza a un requerimiento funcional; cuando un RNF se apoya en una función, esta existe además como RF (por ejemplo: boleta electrónica → RQF-176 y RQF-211).

---

## 1. Catálogo de Requerimientos No Funcionales

| ID | Nombre del requerimiento | Categoría / Subcategoría | Descripción |
| :--- | :--- | :--- | :--- |
| RNF-001 | Tiempo de respuesta del motor de búsqueda | Rendimiento / Comportamiento temporal | El sistema debe retornar los resultados de búsqueda en un tiempo máximo de 2 segundos bajo una carga concurrente de 200 usuarios, medido desde que el usuario confirma los parámetros. |
| RNF-002 | Tiempo de procesamiento del flujo de pago Escrow | Rendimiento / Comportamiento temporal | El sistema debe garantizar que el ciclo de pago retenido (Escrow) se complete en un tiempo máximo de 8 segundos, excluyendo el tiempo de respuesta de la pasarela externa. |
| RNF-003 | Tiempo de generación del contrato PDF | Rendimiento / Comportamiento temporal | El sistema debe garantizar que el contrato en formato PDF esté disponible en un tiempo máximo de 10 segundos desde su solicitud, con un tamaño resultante inferior a 2 MB. |
| RNF-004 | Optimización de recursos multimedia | Rendimiento / Eficiencia de recursos | El sistema debe mantener las imágenes de galería optimizadas en peso antes de su almacenamiento, reduciendo los tiempos de carga de la interfaz. |
| RNF-005 | Acceso a la funcionalidad de reserva en pocos pasos | Usabilidad / Operabilidad | El sistema debe permitir al usuario completar el proceso de reserva en un máximo de 7 interacciones (clics) y sin superar los 3 niveles de profundidad de navegación. |
| RNF-006 | Retroalimentación visual ante errores de validación | Usabilidad / Reconocimiento de errores | El sistema debe mostrar mensajes de error descriptivos (máximo 120 caracteres) en un tiempo inferior a 500 milisegundos tras una validación fallida en formularios, sin recargar la página. |
| RNF-007 | Adaptabilidad visual a dispositivos móviles | Usabilidad / Adaptabilidad visual | El sistema debe presentar sus interfaces sin superposición de elementos en resoluciones desde 375px hasta 1920px de ancho, manteniendo botones con un área mínima de 44x44 píxeles. |
| RNF-008 | Accesibilidad de los flujos principales | Usabilidad / Accesibilidad | El sistema debe permitir operar los flujos de registro, búsqueda y reserva exclusivamente mediante teclado, cumpliendo el estándar de accesibilidad WCAG 2.1 nivel AA. |
| RNF-009 | Disponibilidad continua de la plataforma | Fiabilidad / Disponibilidad | El sistema debe garantizar una disponibilidad mínima del 99,9% mensual para las funciones críticas de autenticación, búsqueda y reservas. |
| RNF-010 | Respaldo y recuperación de la base de datos | Fiabilidad / Recuperabilidad | El sistema debe ejecutar respaldos automáticos de la base de datos que permitan una recuperación con un RPO máximo de 4 horas y un RTO máximo de 6 horas. |
| RNF-011 | Consistencia transaccional en flujos de pago | Fiabilidad / Tolerancia a fallos | El sistema debe garantizar la atomicidad transaccional ejecutando un rollback automático (revirtiendo el estado de la base de datos) ante cualquier fallo en el flujo de pagos. |
| RNF-012 | Idempotencia de los intentos de pago | Fiabilidad / Integridad | El sistema debe garantizar la idempotencia de cada intento de pago mediante una clave única de operación, evitando cargos duplicados ante reintentos del usuario o de la pasarela. |
| RNF-013 | Almacenamiento de contraseñas con hash irreversible | Seguridad / Confidencialidad | El sistema debe almacenar las contraseñas exclusivamente en formato de hash irreversible utilizando bcrypt con un factor de costo mínimo de 12 rounds, prohibiendo su almacenamiento en texto plano. |
| RNF-014 | Cifrado de datos en reposo | Seguridad / Confidencialidad | El sistema debe aplicar cifrado en reposo mediante el algoritmo AES-256 a los datos bancarios y a los documentos PDF finales almacenados. |
| RNF-015 | Protección de comunicaciones y credenciales | Seguridad / Confidencialidad | El sistema debe transmitir credenciales y datos sensibles exclusivamente mediante HTTPS con protocolo TLS 1.2 o superior, impidiendo que los tokens viajen por URL. |
| RNF-016 | Invalidación automática de sesión por inactividad | Seguridad / Autenticidad | El sistema debe invalidar automáticamente el token de sesión tras 30 minutos de inactividad del usuario, con un límite de caducidad absoluta de 8 horas. |
| RNF-017 | Inmutabilidad de los registros de auditoría | Seguridad / Integridad | El sistema debe preservar los logs de auditoría transaccional en un repositorio inmutable, bloqueando a nivel de infraestructura cualquier intento de modificación o eliminación de los registros. |
| RNF-018 | Eliminación irreversible de datos personales | Seguridad / Privacidad | El sistema debe garantizar la eliminación irreversible de los datos personales identificables (PII) tras aprobarse la baja de una cuenta de usuario. |
| RNF-019 | Escalabilidad horizontal del servicio | Flexibilidad / Escalabilidad | El sistema debe soportar un escalamiento horizontal automático para absorber incrementos del 200% de carga, desplegando nuevas instancias en un tiempo máximo de 10 minutos. |
| RNF-020 | Modificación de parámetros sin redespliegue | Flexibilidad / Modificabilidad | El sistema debe permitir la modificación de parámetros de negocio (como el porcentaje de comisión) aplicando los cambios en máximo 60 segundos sin requerir reinicio del servidor. |
| RNF-021 | Cobertura mínima de pruebas automatizadas | Mantenibilidad / Testeabilidad | El sistema debe mantener una cobertura de pruebas unitarias mínima del 80% sobre la capa de negocio, forzando el fallo del proceso de integración (CI/CD) si desciende de este umbral. |
| RNF-022 | Compatibilidad con navegadores actuales | Compatibilidad / Interoperabilidad | El sistema debe ejecutarse correctamente en las dos últimas versiones estables de Chrome, Firefox, Edge y Safari. |
| RNF-023 | Tolerancia a degradación de servicios API externos | Compatibilidad / Interoperabilidad | El sistema debe abortar las llamadas a APIs externas tras un timeout de 5 segundos, reintentando automáticamente un máximo de 2 veces con intervalos de 2 segundos antes de reportar la caída del servicio. |
| RNF-024 | Recepción y recuperación de webhooks | Compatibilidad / Interoperabilidad | El sistema debe validar la firma de los webhooks entrantes y reintentar su procesamiento hasta 5 veces con un backoff exponencial ante fallos de conexión externa. |
| RNF-025 | Cumplimiento PCI-DSS en datos de tarjetas de pago | Requerimientos Externos / Estándares | El sistema debe procesar los pagos exclusivamente mediante tokenización, sin almacenar en la base de datos los datos PAN o CVV, para dar estricto cumplimiento al estándar PCI-DSS. |
| RNF-026 | Protección de datos personales conforme a la Ley 21.719 | Requerimientos Externos / Legislativos | El sistema debe procesar las solicitudes de eliminación o rectificación de datos personales en un plazo administrativo máximo de 72 horas, en cumplimiento de la Ley 21.719. |
| RNF-027 | Boleta electrónica conforme a la normativa del SII | Requerimientos Externos / Legislativos | El sistema debe cumplir la normativa de boleta electrónica del SII, garantizando que toda boleta emitida por la plataforma quede timbrada y disponible en formato XML y PDF dentro de un plazo máximo de 24 horas. |
| RNF-028 | Conciliación de pagos sin confirmación | Fiabilidad / Integridad | El sistema debe conciliar automáticamente cada 5 minutos los eventos de pago que no registren confirmación, dejando evidencia del resultado de la conciliación para su revisión. |
| RNF-029 | Anonimización de la información transaccional | Seguridad / Privacidad | El sistema debe garantizar la anonimización de la información transaccional histórica tras aprobarse la baja de una cuenta, preservando las obligaciones de auditoría. |
| RNF-030 | Capacidad de usuarios y escrituras concurrentes | Rendimiento / Capacidad | El sistema debe soportar al menos 500 usuarios concurrentes y 100 operaciones de escritura por segundo sobre la base de datos transaccional, sin degradar los tiempos de respuesta definidos. |
| RNF-031 | Adaptabilidad funcional del catálogo | Flexibilidad / Adaptabilidad | El sistema debe permitir incorporar nuevos tipos de inmueble y nuevos métodos de pago sin modificar los módulos existentes. |
| RNF-032 | Documentación del contrato de la API | Mantenibilidad / Analizabilidad | El sistema debe mantener documentado el contrato de su API REST (especificación OpenAPI) y actualizado con cada versión desplegada. |
| RNF-033 | Modularidad del código por dominio | Mantenibilidad / Modularidad | El sistema debe organizarse en módulos desacoplados por dominio funcional, con interfaces documentadas entre ellos. |
| RNF-034 | Despliegue agnóstico del proveedor de nube | Portabilidad / Adaptabilidad | El sistema debe desplegarse sobre contenedores compatibles con cualquier proveedor de nube que soporte Docker, sin dependencias propietarias del entorno. |
| RNF-035 | Reproducción del entorno local | Portabilidad / Instalabilidad | El sistema debe poder reproducirse íntegramente en un entorno local mediante contenedores, incluyendo la base de datos y los servicios de apoyo. |
| RNF-036 | Reemplazabilidad del proveedor de nube | Portabilidad / Reemplazabilidad | El sistema debe poder desplegarse en al menos dos proveedores de nube compatibles con contenedores, sin modificar el código fuente. |
| RNF-037 | Implementación en contenedores | Implementación / Empaquetado | El sistema debe estar implementado en contenedores Docker, garantizando la consistencia entre los entornos de desarrollo, pruebas y producción. |
| RNF-038 | Motor de base de datos relacional | Implementación / Base de datos | El sistema debe utilizar un motor de base de datos relacional (PostgreSQL) con soporte de transacciones ACID y extensiones geoespaciales. |
| RNF-039 | Control de versiones del código fuente | Implementación / Gestión de configuración | El código fuente debe almacenarse en un repositorio Git corporativo (GitHub o equivalente), con control de versiones y revisión de cambios. |
| RNF-040 | Integración y despliegue continuos | Implementación / Despliegue | El sistema debe contar con un pipeline de integración y despliegue continuos (CI/CD) que ejecute las pruebas automatizadas antes de cada despliegue. |
| RNF-041 | Capacidad de almacenamiento por publicación | Almacenamiento / Capacidad | El sistema debe limitar el almacenamiento de archivos por publicación a 50 MB, considerando un máximo de 10 imágenes de 5 MB. |
| RNF-042 | Retención de contratos y evidencias | Almacenamiento / Retención | El sistema debe conservar los contratos firmados y la evidencia fotográfica de las reservas por un plazo mínimo de 5 años. |
| RNF-043 | Retención de los registros de auditoría | Almacenamiento / Retención | El sistema debe conservar los registros de auditoría por un plazo mínimo de 5 años, conforme a los requisitos de trazabilidad del proyecto. |

---

## 2. Resumen por categoría (mínimo 3 RNF por categoría)

| Categoría | Subcategorías incluidas | Cantidad | RNF |
| :--- | :--- | :---: | :--- |
| **Rendimiento** | Comportamiento temporal, Eficiencia de recursos, Capacidad | 5 | 001, 002, 003, 004, 030 |
| **Usabilidad** | Operabilidad, Reconocimiento de errores, Adaptabilidad visual, Accesibilidad | 4 | 005, 006, 007, 008 |
| **Fiabilidad** | Disponibilidad, Recuperabilidad, Tolerancia a fallos, Integridad | 5 | 009, 010, 011, 012, 028 |
| **Seguridad** | Confidencialidad, Autenticidad, Integridad, Privacidad | 7 | 013, 014, 015, 016, 017, 018, 029 |
| **Flexibilidad** | Escalabilidad, Modificabilidad, Adaptabilidad | 3 | 019, 020, 031 |
| **Mantenibilidad** | Testeabilidad, Analizabilidad, Modularidad | 3 | 021, 032, 033 |
| **Compatibilidad** | Interoperabilidad | 3 | 022, 023, 024 |
| **Portabilidad** | Adaptabilidad, Instalabilidad, Reemplazabilidad | 3 | 034, 035, 036 |
| **Implementación** | Empaquetado, Base de datos, Gestión de configuración, Despliegue | 4 | 037, 038, 039, 040 |
| **Almacenamiento** | Capacidad, Retención | 3 | 041, 042, 043 |
| **Requerimientos Externos** | Estándares (PCI-DSS), Legislativos (Ley 21.719, SII) | 3 | 025, 026, 027 |
| **Total** | — | **43** | RNF-001 – RNF-043 |

---

## 3. Trazabilidad con los requerimientos funcionales y los módulos

| RNF | Se relaciona con los RF | Módulos / casos de uso afectados |
| :--- | :--- | :--- |
| RNF-001, RNF-030 | RQF-094, RQF-101, RQF-111 | M05 (CU-19), M06 (CU-22) |
| RNF-002, RNF-011, RNF-012, RNF-028 | RQF-114 a RQF-120, RQF-172, RQF-173 | M06 (CU-24, CU-27), M10 (CU-42) |
| RNF-003 | RQF-132, RQF-133 | M07 (CU-29) |
| RNF-004, RNF-041 | RQF-074 a RQF-076 | M04 (CU-16) |
| RNF-005, RNF-006 | RQF-107, RQF-108, RQF-113 | M05 (CU-21), M06 (CU-22) |
| RNF-007, RNF-008, RNF-022 | Todos los flujos de interfaz | Transversal |
| RNF-009, RNF-010 | Funciones críticas (autenticación, búsqueda, reservas) | Transversal |
| RNF-013, RNF-015, RNF-016 | RQF-003 a RQF-006, RQF-011 a RQF-018, RQF-215 a RQF-217 | M01 (CU-01, CU-03, CU-50) |
| RNF-014 | RQF-032, RQF-137 | M02 (CU-08), M07 (CU-30) |
| RNF-017, RNF-043 | RQF-184, RQF-185 | M11 (CU-46) |
| RNF-018, RNF-029, RNF-026 | RQF-034 a RQF-037 | M02 (CU-09) |
| RNF-019, RNF-031 | RQF-068, RQF-114 | M04 (CU-15), M06 (CU-24) |
| RNF-020 | RQF-105, RQF-223 | M05 (CU-21), M04 (CU-18) |
| RNF-021, RNF-032, RNF-033, RNF-040 | — | Transversal (arquitectura y construcción) |
| RNF-023, RNF-024 | RQF-044, RQF-051, RQF-133, RQF-148 | M03 (CU-11, CU-12), M07 (CU-29) |
| RNF-025 | RQF-114, RQF-115 | M06 (CU-24) |
| RNF-027 | RQF-176, RQF-211 | M10 (CU-42) |
| RNF-034 a RNF-039 | — | Transversal (infraestructura y arquitectura TI) |
| RNF-042 | RQF-137, RQF-167, RQF-205 | M07 (CU-30), M08 (CU-33, CU-48), M10 (CU-41) |

---

## 4. Cambios aplicados respecto de la versión anterior (27 RNF)

| RNF | Cambio aplicado | Motivo |
| :--- | :--- | :--- |
| RNF-002 | Se reescribió para eliminar el verbo funcional "completar el ciclo": ahora expresa la condición de tiempo (*"debe garantizar que el ciclo de pago se complete en..."*). | Evitar contenido funcional en un RNF. |
| RNF-003 | Se reescribió para eliminar los verbos "compilar y exportar". | Ídem anterior. |
| RNF-004 | Se reescribió para eliminar el verbo funcional "comprimir". | Ídem anterior. |
| RNF-012 | Se dividió en **RNF-012** (idempotencia) y **RNF-028** (conciliación), porque un requerimiento no debe contener dos condiciones distintas. | Regla de atomicidad también aplicada a los RNF. |
| RNF-018 | Se dividió en **RNF-018** (eliminación irreversible) y **RNF-029** (anonimización de la información transaccional). | Ídem anterior. |
| RNF-027 | Se reescribió para eliminar las acciones funcionales "generar la boleta" y "entregarla" (ya cubiertas por RQF-176 y RQF-211); ahora expresa el cumplimiento normativo. | Separación RF/RNF. |
| RNF-007 | Se ajustó el nombre y la redacción ("presentar sus interfaces" en lugar de "renderizar"). | Evitar lenguaje técnico de implementación. |
| RNF-017 | Se ajustó "almacenar log" por **"preservar los logs"**, manteniendo el foco en la integridad y no en una acción funcional. | Evitar duplicidad con el catálogo de RF. |
| Nuevos | Se agregaron **RNF-030 a RNF-043** (14 requerimientos) para completar las categorías exigidas por la retroalimentación: **Implementación** (contenedores Docker, motor de base de datos relacional, repositorio de código, CI/CD), **Almacenamiento** (capacidad y retención), **Portabilidad** (despliegue agnóstico, entorno local, reemplazabilidad) y completar **Flexibilidad**, **Mantenibilidad** y **Rendimiento**. | Cada categoría debe tener al menos 3 ejemplos. |
