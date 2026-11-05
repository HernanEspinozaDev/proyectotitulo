# ANEXO A: ESPECIFICACIÓN DETALLADA DE REQUERIMIENTOS (IEEE 830)

## Catálogo consolidado de requerimientos funcionales (RQF)

El catálogo especifica el diseño objetivo y conserva identificadores de las iteraciones previas. La condición de implementación se registra por versión y entorno en los capítulos XII y XI. Los cambios históricos se conservan en el registro de contexto de la memoria.

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
| RQF-061 | El sistema debe comprobar la titularidad vigente para administrar una publicación. |
| RQF-062 | El sistema debe permitir ingresar un título para la publicación. |
| RQF-063 | El sistema debe validar que el título no exceda los 70 caracteres. |
| RQF-064 | El sistema debe permitir ingresar la descripción de la publicación. |
| RQF-065 | El sistema debe validar que la descripción contenga al menos 100 caracteres. |
| RQF-066 | El sistema debe permitir ingresar la superficie total del espacio en metros cuadrados. |
| RQF-067 | El sistema debe validar que la superficie ingresada sea un número mayor a cero. |
| RQF-068 | El sistema debe permitir seleccionar el tipo de espacio entre las categorías habilitadas para el corte. |
| RQF-069 | El sistema debe permitir establecer la capacidad máxima de personas. |
| RQF-070 | El sistema debe permitir agregar reglas de uso a la publicación. |
| RQF-071 | El sistema debe permitir configurar la modalidad tarifaria (por hora, día o mes). |
| RQF-072 | El sistema debe permitir ingresar el precio base del arriendo. |
| RQF-073 | El sistema debe validar que el precio base ingresado sea mayor a \$5.000 CLP. |
| RQF-074 | El sistema debe permitir cargar fotografías a la galería de la publicación. |
| RQF-075 | El sistema debe limitar la galería a 30 posiciones por espacio, incluidas las cargas reservadas. |
| RQF-076 | El sistema debe rechazar una imagen que exceda el límite de entrada del procesador multimedia del corte. |
| RQF-077 | El sistema debe permitir seleccionar una fotografía como portada. |
| RQF-078 | El sistema debe permitir eliminar una fotografía de la galería. |
| RQF-079 | El sistema debe permitir ingresar la dirección física completa del espacio. |
| RQF-080 | El sistema debe registrar la ubicación geográfica a partir de la dirección ingresada. |
| RQF-081 | El sistema debe asignar el estado "Borrador" automáticamente durante la creación. |
| RQF-082 | El sistema debe publicar el espacio cuando el titular vigente solicita la publicación y el anuncio satisface sus reglas. |
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
| RQF-098 | El sistema debe permitir buscar a través de filtros por categoría de espacio. |
| RQF-099 | El sistema debe permitir buscar a través de filtros de superficie mínima. |
| RQF-100 | El sistema debe permitir buscar a través de filtros de rango de fechas. |
| RQF-101 | El sistema debe excluir de los resultados las publicaciones sin disponibilidad en las fechas consultadas. |
| RQF-102 | El sistema debe permitir limpiar todos los filtros de búsqueda aplicados. |
| RQF-103 | El sistema debe permitir consultar los detalles completos de una publicación. |
| RQF-104 | El sistema debe calcular el costo total multiplicando el precio base por el tiempo seleccionado. |
| RQF-105 | El sistema debe calcular el monto de la comisión de servicio sobre el costo total. |
| RQF-106 | El sistema debe determinar el monto de la garantía cuando la oferta la exige y la modalidad está habilitada. |
| RQF-107 | El sistema debe mostrar por separado los importes de firma, renta, comisión y garantía que corresponden a la emisión. |
| RQF-108 | El sistema debe permitir seleccionar las fechas/horas de reserva en la publicación. |
| RQF-109 | El sistema debe validar que la fecha de inicio seleccionada sea posterior a la fecha actual. |
| RQF-110 | El sistema debe validar que la fecha de fin sea posterior a la fecha de inicio. |
| RQF-111 | El sistema debe validar la disponibilidad del espacio para el intervalo solicitado. |
| RQF-112 | El sistema debe rechazar la reserva si existe superposición temporal con otra reserva o bloqueo. |
| RQF-113 | El sistema debe activar un bloqueo cuando ambas identidades están verificadas y ambas partes acuerdan el horario y el precio. |
| RQF-114 | El sistema debe permitir al usuario seleccionar un método de pago mediante la pasarela integrada. |
| RQF-115 | El sistema debe iniciar el flujo de cobro comunicándose con la pasarela de pagos. |
| RQF-116 | El sistema debe confirmar la reserva cuando se satisfacen las condiciones de la emisión y se acreditan todos los cobros exigibles. |
| RQF-117 | El sistema debe registrar la renta como obligación independiente de los aportes de firma y de la garantía. |
| RQF-118 | El sistema debe habilitar el cobro separado de la garantía, cuando corresponde, después de acreditar la renta. |
| RQF-119 | El sistema debe registrar el rechazo del intento de pago y conservar el vencimiento original del bloqueo. |
| RQF-120 | El sistema debe mostrar el vencimiento de la etapa antes de iniciar el cobro. |
| RQF-121 | El sistema debe notificar al arrendatario cuando el pago sea procesado. |
| RQF-122 | El sistema debe notificar al arrendador sobre la recepción de una nueva solicitud de arriendo antes del acuerdo y del cobro. |
| RQF-123 | El sistema debe permitir al arrendador consultar las solicitudes de reserva entrantes. |
| RQF-124 | El sistema debe permitir al titular aceptar las condiciones de horario y precio propuestas en una solicitud de reserva. |
| RQF-125 | El sistema debe registrar el acuerdo del titular sobre el horario y el precio antes de iniciar el bloqueo. |
| RQF-126 | El sistema debe permitir al arrendador rechazar una solicitud de reserva. |
| RQF-127 | El sistema debe exigir al arrendador seleccionar un motivo al rechazar una solicitud. |
| RQF-128 | El sistema debe enviar a conciliación el pago acreditado después de vencer el bloqueo sin reactivar la reserva. |
| RQF-129 | El sistema debe mantener el vencimiento original ante reintentos y eventos duplicados. |
| RQF-130 | El sistema debe emitir un documento contractual inmutable cuando ambas identidades están verificadas. |
| RQF-131 | El sistema debe consultar los datos legales de las partes involucradas y del espacio arrendado. |
| RQF-132 | El sistema debe generar una nueva emisión al modificar las condiciones del contrato. |
| RQF-133 | El sistema debe solicitar la firma externa de la emisión cuando ambas partes eligen SimpleFirma y se acreditan los aportes exigibles. |
| RQF-134 | El sistema debe enviar el enlace de firma correspondiente al arrendatario. |
| RQF-135 | El sistema debe enviar el enlace de firma correspondiente al arrendador. |
| RQF-136 | El sistema debe cambiar el estado a "Firma_Parcial" tras recibir la confirmación de la primera firma. |
| RQF-137 | El sistema debe conservar el documento firmado en el historial de la emisión cuando se utiliza SimpleFirma. |
| RQF-138 | El sistema debe habilitar el cobro de la renta de la modalidad SimpleFirma al acreditar ambas firmas. |
| RQF-139 | El sistema debe notificar a las partes cuando el contrato esté completamente firmado. |
| RQF-140 | El sistema debe liberar el bloqueo cuando vence la etapa contractual o de pago aplicable. |
| RQF-141 | El sistema debe vincular cada devolución al pago y al pagador originales. |
| RQF-142 | El sistema debe permitir a cada parte autorizada descargar el documento disponible de su emisión, con su modalidad de firma. |
| RQF-143 | El sistema debe habilitar la opción de "Check-in" únicamente el día de inicio de la reserva. |
| RQF-144 | El sistema debe bloquear el Check-in fuera de la fecha de inicio de la reserva. |
| RQF-145 | El sistema debe permitir al arrendatario cargar fotografías en el formulario de Check-in. |
| RQF-146 | El sistema debe permitir al arrendatario ingresar comentarios de texto en el formulario de Check-in. |
| RQF-147 | El sistema debe registrar la fecha y ubicación al procesar el Check-in. |
| RQF-148 | El sistema debe cambiar el estado de la reserva a "En_Curso" tras procesar el Check-in. |
| RQF-149 | El sistema debe notificar al arrendador cuando el arrendatario procese el Check-in. |
| RQF-150 | El sistema debe permitir al arrendatario registrar el Check-out de la reserva. |
| RQF-151 | El sistema debe permitir cargar fotografías en el formulario de Check-out. |
| RQF-152 | El sistema debe registrar la entrega antes de la confirmación de desocupación del titular. |
| RQF-153 | El sistema debe permitir al arrendatario registrar una calificación numérica del espacio. |
| RQF-154 | El sistema debe permitir al arrendatario registrar una reseña de texto del espacio. |
| RQF-155 | El sistema debe mostrar las reseñas y calificaciones en la vista de detalle de la publicación. |
| RQF-156 | El sistema debe permitir al arrendatario enviar mensajes en el chat de la reserva. |
| RQF-157 | El sistema debe permitir al arrendador enviar mensajes en el chat de la reserva. |
| RQF-158 | El sistema debe permitir a las partes consultar el historial de mensajes de la reserva. |
| RQF-159 | El sistema debe habilitar el registro de reclamos durante el plazo aplicable a la modalidad informada. |
| RQF-160 | El sistema debe permitir al arrendador registrar un reclamo adjuntando texto descriptivo. |
| RQF-161 | El sistema debe exigir al arrendador cargar fotografías de evidencia en el reclamo. |
| RQF-162 | El sistema debe enviar a revisión el efecto de un reclamo sobre una garantía habilitada. |
| RQF-163 | El sistema debe cambiar el estado de la reserva a "En_Disputa" tras el registro de un reclamo. |
| RQF-164 | El sistema debe notificar al arrendatario sobre la apertura de una disputa. |
| RQF-165 | El sistema debe permitir al arrendatario ingresar texto y fotografías de defensa. |
| RQF-166 | El sistema debe permitir al administrador consultar el listado de disputas abiertas. |
| RQF-167 | El sistema debe permitir al administrador consultar la evidencia fotográfica vinculada a la disputa. |
| RQF-168 | El sistema debe permitir al administrador registrar un fallo a favor del arrendatario. |
| RQF-169 | El sistema debe permitir al administrador registrar un fallo a favor del arrendador. |
| RQF-170 | El sistema debe registrar el monto de ajuste cuando el reclamo afecta una garantía habilitada. |
| RQF-171 | El sistema debe cambiar el estado de la disputa a "Resuelta" tras el fallo del administrador. |
| RQF-172 | El sistema debe conciliar los movimientos de la reserva según la modalidad y el estado de sus obligaciones. |
| RQF-173 | El sistema debe asociar la acreditación de renta y comisión con el movimiento informado por la pasarela. |
| RQF-174 | El sistema debe registrar el ajuste de una garantía habilitada cuando corresponde compensación. |
| RQF-175 | El sistema debe vincular la devolución total o parcial de garantía al pago original. |
| RQF-176 | El sistema debe identificar la obligación documental de la comisión cuando se habilita la integración tributaria. |
| RQF-177 | El sistema debe registrar el resultado de la conciliación financiera sin prolongar el bloqueo de ocupación. |
| RQF-178 | El sistema debe permitir al administrador bloquear el acceso a una cuenta de usuario. |
| RQF-179 | El sistema debe permitir al administrador desbloquear una cuenta de usuario. |
| RQF-180 | El sistema debe permitir al administrador consultar el motivo de bloqueo de una cuenta. |
| RQF-181 | El sistema debe permitir al administrador ocultar una reseña reportada. |
| RQF-182 | El sistema debe exigir al administrador registrar un motivo al ocultar una reseña. |
| RQF-183 | El sistema debe permitir al administrador generar reportes de gestión de la plataforma. |
| RQF-184 | El sistema debe permitir al operador autorizado consultar eventos de auditoría mediante los filtros admitidos por el contrato. |
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
| RQF-205 | El sistema debe permitir al titular confirmar la desocupación después de la entrega del arrendatario. |
| RQF-206 | El sistema debe registrar la fecha y la ubicación al confirmar la recepción del espacio. |
| RQF-207 | El sistema debe permitir reportar una reseña publicada. |
| RQF-208 | El sistema debe tramitar la devolución aplicable de una garantía habilitada y vincularla a su pago original. |
| RQF-209 | El sistema debe permitir al administrador consultar la confirmación de recepción vinculada a la disputa. |
| RQF-210 | El sistema debe notificar el resultado de la disputa a las partes. |
| RQF-211 | El sistema debe permitir el acceso al documento tributario cuando la integración correspondiente está habilitada. |
| RQF-212 | El sistema debe permitir al administrador buscar una cuenta de usuario. |

## Requerimientos funcionales complementarios — Historias de usuario

> Estos **24 requerimientos (RQF-213 a RQF-236)** se incorporaron al revisar el catálogo de 35 historias de usuario. Su objetivo es que **ninguna HU quede con criterios de aceptación sin respaldo funcional**, y al mismo tiempo se corrigieron en las HU todas las contradicciones numéricas y de alcance detectadas.
>
> Se mantiene la regla de trazabilidad: **IDs nuevos al final**, sin renumerar ni modificar los requerimientos anteriores.

| ID | Descripción del Requerimiento Funcional |
| :--- | :--- |
| RQF-213 | El sistema debe permitir registrar una cuenta sin exigir una preferencia inicial de arriendo u oferta. |
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
| RQF-227 | El sistema debe impedir la emisión contractual sin identidad verificada de ambas partes. |
| RQF-228 | El sistema debe permitir al arrendatario cancelar una reserva conforme a la política de cancelación. |
| RQF-229 | El sistema debe calcular el monto a reembolsar según la política de cancelación aplicada. |
| RQF-230 | El sistema debe ejecutar el reembolso al arrendatario tras la cancelación de la reserva. |
| RQF-231 | El sistema debe notificar a las partes la cancelación de la reserva. |
| RQF-232 | El sistema debe permitir al arrendador registrar una calificación numérica del arrendatario. |
| RQF-233 | El sistema debe permitir al arrendador registrar una reseña de texto del arrendatario. |
| RQF-234 | El sistema debe rechazar el registro de una segunda reseña del mismo participante para la misma reserva. |
| RQF-235 | El sistema debe calcular el promedio de calificaciones del espacio. |
| RQF-236 | El sistema debe permitir al administrador consultar el listado de espacios publicados. |

## Requerimientos No Funcionales (RNF) — Sistema EspaciGo

> **Versión corregida (19-09-2026).** Catálogo de **43 requerimientos no funcionales (RNF-001 a RNF-043)**, clasificados según categorías y subcategorías del estándar **ISO/IEC 25010** y del modelo de Sommerville.

**Convenciones aplicadas**

1. **Redacción estándar:** todos los RNF se redactan como **"El sistema debe [condición de calidad]"**, evitando verbos de acción funcional (los verbos de función pertenecen al catálogo de RF). Excepción controlada: los RNF de *Implementación / Gestión de configuración*, redactados como *"El código fuente debe almacenarse..."*, siguiendo el estándar de especificación adoptado en el proyecto.
2. **Categoría y subcategoría:** cada RNF declara su categoría principal (en negrita en la sección de resumen) y su subcategoría específica.
3. **Mínimo 3 ejemplos por categoría:** todas las categorías declaradas tienen al menos 3 requerimientos (ver sección de resumen).
4. **Separación RF/RNF:** los RNF describen *condiciones de calidad, restricciones o cumplimiento*. Las acciones del sistema (registrar, generar, ejecutar, notificar, etc.) están exclusivamente en el catálogo de RF. Se corrigieron los RNF que contenían acciones funcionales (RNF-002, RNF-003, RNF-004 y RNF-027) y se separaron los que mezclaban dos condiciones distintas (RNF-012 y RNF-018).
5. **Sin duplicación de RF:** ningún RNF reemplaza a un requerimiento funcional; cuando un RNF se apoya en una función, esta existe además como RF (por ejemplo: boleta electrónica → RQF-176 y RQF-211).

---

## 1. Catálogo de Requerimientos No Funcionales

| ID | Nombre del requerimiento | Categoría / Subcategoría | Descripción |
| :--- | :--- | :--- | :--- |
| RNF-001 | Tiempo de respuesta del motor de búsqueda | Rendimiento / Comportamiento temporal | El sistema debe retornar los resultados de búsqueda en un tiempo máximo de 2 segundos bajo una carga concurrente de 200 usuarios, medido desde que el usuario confirma los parámetros. |
| RNF-002 | Tiempo de procesamiento interno de renta | Rendimiento / Comportamiento temporal | El sistema debe procesar la acreditación interna de la renta en un máximo de 8 segundos, excluido el tiempo de respuesta del proveedor. |
| RNF-003 | Tiempo de generación del contrato PDF | Rendimiento / Comportamiento temporal | El sistema debe garantizar que el contrato en formato PDF esté disponible en un tiempo máximo de 10 segundos desde su solicitud, con un tamaño resultante inferior a 2 MB. |
| RNF-004 | Optimización de recursos multimedia | Rendimiento / Eficiencia de recursos | El sistema debe mantener las imágenes de galería optimizadas en peso antes de su almacenamiento, reduciendo los tiempos de carga de la interfaz. |
| RNF-005 | Acceso a la funcionalidad de reserva en pocos pasos | Usabilidad / Operabilidad | El sistema debe permitir al usuario completar el proceso de reserva en un máximo de 7 interacciones (clics) y sin superar los 3 niveles de profundidad de navegación. |
| RNF-006 | Retroalimentación visual ante errores de validación | Usabilidad / Reconocimiento de errores | El sistema debe mostrar mensajes de error descriptivos (máximo 120 caracteres) en un tiempo inferior a 500 milisegundos tras una validación fallida en formularios, sin recargar la página. |
| RNF-007 | Adaptabilidad visual a dispositivos móviles | Usabilidad / Adaptabilidad visual | El sistema debe presentar sus interfaces sin superposición de elementos en resoluciones desde 375px hasta 1920px de ancho, manteniendo botones con un área mínima de 44x44 píxeles. |
| RNF-008 | Accesibilidad de los flujos principales | Usabilidad / Accesibilidad | El sistema debe permitir operar los flujos de registro, búsqueda y reserva exclusivamente mediante teclado, cumpliendo el estándar de accesibilidad WCAG 2.1 nivel AA. |
| RNF-009 | Disponibilidad continua de la plataforma | Fiabilidad / Disponibilidad | El sistema debe garantizar una disponibilidad mínima del 99,9% mensual para las funciones críticas de autenticación, búsqueda y reservas. |
| RNF-010 | Respaldo y recuperación de la base de datos | Fiabilidad / Recuperabilidad | El sistema debe permitir la recuperación de la base de datos con un RPO máximo de 15 minutos y un RTO máximo de 1 hora, verificados mediante un ensayo de recuperación en el entorno objetivo. |
| RNF-011 | Consistencia transaccional en flujos de pago | Fiabilidad / Tolerancia a fallos | El sistema debe mantener un estado interno consistente cuando falla una operación de pago, mediante transiciones atómicas y conciliación de eventos externos. |
| RNF-012 | Idempotencia de los intentos de pago | Fiabilidad / Integridad | El sistema debe garantizar la idempotencia de cada intento de pago mediante una clave única de operación, evitando cargos duplicados ante reintentos del usuario o de la pasarela. |
| RNF-013 | Almacenamiento de contraseñas con hash irreversible | Seguridad / Confidencialidad | El sistema debe almacenar las contraseñas exclusivamente en formato de hash irreversible utilizando bcrypt con un factor de costo mínimo de 12 rounds, prohibiendo su almacenamiento en texto plano. |
| RNF-014 | Cifrado de datos en reposo | Seguridad / Confidencialidad | El sistema debe aplicar cifrado en reposo mediante el algoritmo AES-256 a los datos bancarios y a los documentos PDF finales almacenados. |
| RNF-015 | Protección de comunicaciones y credenciales | Seguridad / Confidencialidad | El sistema debe transmitir credenciales y datos sensibles exclusivamente mediante HTTPS con protocolo TLS 1.2 o superior, impidiendo que los tokens viajen por URL. |
| RNF-016 | Invalidación automática de sesión por inactividad | Seguridad / Autenticidad | El sistema debe invalidar automáticamente el token de sesión tras 30 minutos de inactividad del usuario, con un límite de caducidad absoluta de 8 horas. |
| RNF-017 | Inmutabilidad de los registros de auditoría | Seguridad / Integridad | El sistema debe preservar los logs de auditoría transaccional en un repositorio inmutable, bloqueando a nivel de infraestructura cualquier intento de modificación o eliminación de los registros. |
| RNF-018 | Eliminación irreversible de datos personales | Seguridad / Privacidad | El sistema debe aplicar la acción autorizada de supresión o restricción según la finalidad y las obligaciones de conservación identificadas. |
| RNF-019 | Escalabilidad horizontal del servicio | Flexibilidad / Escalabilidad | El sistema debe soportar un escalamiento horizontal automático para absorber incrementos del 200% de carga, desplegando nuevas instancias en un tiempo máximo de 10 minutos. |
| RNF-020 | Modificación de parámetros sin redespliegue | Flexibilidad / Modificabilidad | El sistema debe permitir la modificación de parámetros de negocio (como el porcentaje de comisión) aplicando los cambios en máximo 60 segundos sin requerir reinicio del servidor. |
| RNF-021 | Cobertura mínima de pruebas automatizadas | Mantenibilidad / Testeabilidad | El sistema debe mantener una cobertura de pruebas unitarias mínima del 80% sobre la capa de negocio, forzando el fallo del proceso de integración (CI/CD) si desciende de este umbral. |
| RNF-022 | Compatibilidad con navegadores actuales | Compatibilidad / Interoperabilidad | El sistema debe ejecutarse correctamente en las dos últimas versiones estables de Chrome, Firefox, Edge y Safari. |
| RNF-023 | Tolerancia a degradación de servicios API externos | Compatibilidad / Interoperabilidad | El sistema debe abortar las llamadas a APIs externas tras un timeout de 5 segundos, reintentando automáticamente un máximo de 2 veces con intervalos de 2 segundos antes de reportar la caída del servicio. |
| RNF-024 | Recepción y recuperación de webhooks | Compatibilidad / Interoperabilidad | El sistema debe validar la firma de los webhooks entrantes y reintentar su procesamiento hasta 5 veces con un backoff exponencial ante fallos de conexión externa. |
| RNF-025 | Cumplimiento PCI-DSS en datos de tarjetas de pago | Requerimientos Externos / Estándares | El sistema debe delegar la captura de datos de tarjeta al proveedor y excluir PAN y CVV de la persistencia de espaciGo. |
| RNF-026 | Protección de datos personales conforme a la Ley 21.719 | Requerimientos Externos / Legislativos | El sistema debe registrar las solicitudes de derechos sobre datos personales y tratarlas según el procedimiento y los plazos aplicables al entorno. |
| RNF-027 | Boleta electrónica conforme a la normativa del SII | Requerimientos Externos / Legislativos | Cuando se habilita la integración tributaria, el sistema debe verificar el formato y el estado del documento asociado a la comisión según los requisitos aplicables. |
| RNF-028 | Conciliación de pagos sin confirmación | Fiabilidad / Integridad | El sistema debe conciliar automáticamente cada 5 minutos los eventos de pago que no registren confirmación, dejando evidencia del resultado de la conciliación para su revisión. |
| RNF-029 | Anonimización de la información transaccional | Seguridad / Privacidad | El sistema debe aplicar las medidas de minimización, supresión o anonimización que correspondan al dato y su finalidad. |
| RNF-030 | Capacidad de usuarios y escrituras concurrentes | Rendimiento / Capacidad | El sistema debe soportar al menos 500 usuarios concurrentes y 100 operaciones de escritura por segundo sobre la base de datos transaccional, sin degradar los tiempos de respuesta definidos. |
| RNF-031 | Adaptabilidad funcional del catálogo | Flexibilidad / Adaptabilidad | El sistema debe permitir incorporar nuevas categorías de espacio y nuevos métodos de pago sin modificar los módulos existentes. |
| RNF-032 | Documentación del contrato de la API | Mantenibilidad / Analizabilidad | El sistema debe mantener documentado el contrato de su API REST (especificación OpenAPI) y actualizado con cada versión desplegada. |
| RNF-033 | Modularidad del código por dominio | Mantenibilidad / Modularidad | El sistema debe organizarse en módulos desacoplados por dominio funcional, con interfaces documentadas entre ellos. |
| RNF-034 | Despliegue agnóstico del proveedor de nube | Portabilidad / Adaptabilidad | El sistema debe desplegarse sobre contenedores compatibles con cualquier proveedor de nube que soporte Docker, sin dependencias propietarias del entorno. |
| RNF-035 | Reproducción del entorno local | Portabilidad / Instalabilidad | El sistema debe poder reproducirse íntegramente en un entorno local mediante contenedores, incluyendo la base de datos y los servicios de apoyo. |
| RNF-036 | Reemplazabilidad del proveedor de nube | Portabilidad / Reemplazabilidad | El sistema debe poder desplegarse en al menos dos proveedores de nube compatibles con contenedores, sin modificar el código fuente. |
| RNF-037 | Implementación en contenedores | Implementación / Empaquetado | El sistema debe estar implementado en contenedores Docker, garantizando la consistencia entre los entornos de desarrollo, pruebas y producción. |
| RNF-038 | Motor de base de datos relacional | Implementación / Base de datos | El sistema debe utilizar un motor de base de datos relacional (PostgreSQL) con soporte de transacciones ACID y extensiones geoespaciales. |
| RNF-039 | Control de versiones del código fuente | Implementación / Gestión de configuración | El código fuente debe almacenarse en un repositorio Git corporativo (GitHub o equivalente), con control de versiones y revisión de cambios. |
| RNF-040 | Integración y despliegue continuos | Implementación / Despliegue | El sistema debe contar con un pipeline de integración y despliegue continuos (CI/CD) que ejecute las pruebas automatizadas antes de cada despliegue. |
| RNF-041 | Capacidad de almacenamiento por publicación | Almacenamiento / Capacidad | El sistema debe controlar la capacidad de la galería según RQF-075 y el límite de entrada del procesador multimedia del corte. |
| RNF-042 | Retención de contratos y evidencias | Almacenamiento / Retención | El sistema debe conservar emisiones y evidencias operativas según las reglas de retención por finalidad, modalidad y estado. |
| RNF-043 | Retención de los registros de auditoría | Almacenamiento / Retención | El sistema debe aplicar la política de retención definida para cada clase de registro de auditoría. |

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
