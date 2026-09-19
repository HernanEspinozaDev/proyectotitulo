# Listado de Historias de Usuario (HU)

## HU01 - Registro de nuevo usuario

**Como** visitante de la plataforma,
**Quiero** registrarme ingresando mis datos personales y seleccionando mi perfil principal (Propietario o Arrendatario),
**Para que** pueda acceder a las funcionalidades del sistema según el rol que necesite desempeñar en EspaciGo.

### Criterios de Aceptación
- Tener un formulario de registro que solicite: Nombre completo, correo electrónico, contraseña, teléfono de contacto y la selección explícita del rol ("Quiero ofrecer espacios" o "Quiero arrendar espacios").
- Validar que el correo electrónico ingresado tenga un formato válido y no se encuentre registrado previamente en el sistema; si ya existe, mostrar el mensaje *"El correo electrónico ya está registrado, por favor inicie sesión o recupere su contraseña"*.
- La contraseña ingresada debe cumplir obligatoriamente con las políticas de seguridad: tener 8 o más caracteres, incluir al menos una letra mayúscula, una minúscula, un número y un carácter especial, sin contener espacios en blanco.
- Si el formato de la contraseña no cumple con los requisitos, mostrar un mensaje de error detallado indicando los elementos faltantes.
- Si todos los datos son correctos al enviar el formulario, registrar la cuenta con estado activo y enviar un correo electrónico de bienvenida con un enlace de confirmación.
- Al completarse el registro exitosamente, redirigir automáticamente al usuario al panel principal o a la vista de perfil para completar su verificación.

> **Nota:** Incluye la interfaz asociada a la pantalla de registro y selección de perfiles.

---

## HU02 - Inicio de sesión en la plataforma

**Como** usuario registrado (propietario, arrendatario o administrador),
**Quiero** ingresar mis credenciales (correo y contraseña) en la plataforma,
**Para que** pueda autenticar mi identidad y acceder a mi panel de control personalizado.

### Criterios de Aceptación
- Tener un formulario de login con campos obligatorios para "Correo electrónico" y "Contraseña", además de un botón de "Iniciar Sesión" y un enlace de "¿Olvidó su contraseña?".
- Si se ingresan credenciales incorrectas o un correo no registrado, mostrar un mensaje genérico de seguridad *"Correo electrónico o contraseña incorrectos"* para evitar la enumeración de usuarios.
- Tras 3 intentos fallidos consecutivos de inicio de sesión, bloquear temporalmente el acceso desde esa dirección IP / cuenta durante 5 minutos, mostrando el mensaje *"Demasiados intentos fallidos. Su cuenta ha sido bloqueada temporalmente por seguridad. Intente nuevamente en 5 minutos"*.
- Si las credenciales son correctas, validar el rol del usuario y redirigirlo de forma inmediata a su respectivo dashboard (Vista de Propietario, Vista de Arrendatario o Panel de Administrador).

> **Nota:** Incluye la interfaz asociada a la pantalla de inicio de sesión y alertas de bloqueo.

---

## HU03 - Modificar contraseña

**Como** usuario registrado (propietario, arrendatario o administrador),
**Quiero** cambiar mi contraseña,
**Para que** al acceder tener una contraseña propia que yo elija y/o tener una contraseña con mayor seguridad o facilidad al recordar u otro fin que yo estime conveniente.

### Criterios de Aceptación
- Tener un formulario inicial donde haya que ingresar el correo electrónico del usuario que desea modificar la contraseña.
- Si el correo ingresado no es válido o no existe en el sistema, mostrar el mensaje *"El correo no es válido, por favor intente nuevamente"* y no dejar avanzar hasta ingresar un correo válido.
- Si se ingresa un correo válido, enviar un enlace/botón de verificación de identidad de 10 minutos al correo personal del usuario ingresado, conteniendo un botón "Cambiar contraseña" que redireccione al siguiente formulario.
- Tener un formulario protegido donde ingresar: Contraseña actual, Contraseña nueva y Repetición de la contraseña nueva.
- Si el enlace del correo no es verificado en el tiempo asignado (10 minutos), la verificación se invalida automáticamente y se debe realizar el proceso nuevamente.
- La contraseña nueva debe tener obligatoriamente 8 o más caracteres, letras mayúsculas y minúsculas, contener un carácter especial, tener al menos un número y no contener espacios en blanco.
- Si la contraseña nueva es igual que la actual, mostrar un mensaje de error *"La contraseña nueva no puede ser igual a la actual"*.
- En caso de ingresar una contraseña nueva que ya haya sido utilizada en los últimos 3 meses, mostrar el mensaje *"La contraseña nueva ha sido registrada hace n° mes/es, ingrese una fuera de ese rango"*.
- Si cumple con todas las validaciones, modificar correctamente la contraseña en la base de datos y enviar un correo electrónico de notificación que contenga:
  - Un mensaje que diga *"La contraseña ha sido modificada correctamente"*.
  - Un enlace que diga *"¿No fue usted?"* que redireccione al mismo formulario donde ingresar el correo y luego las contraseñas para bloquear o revertir la acción.

> **Nota:** Incluye la interfaz asociada al flujo completo de recuperación y cambio de contraseña.

---

## HU04 - Verificación de identidad (KYC)

**Como** usuario de la plataforma (especialmente anfitriones y arrendatarios),
**Quiero** subir y verificar mis documentos de identidad oficial,
**Para que** se valide mi perfil y pueda realizar transacciones seguras dentro del marketplace.

### Criterios de Aceptación
- Tener una sección en el perfil de usuario dedicada al estado de verificación de identidad con el distintivo "Cuenta no verificada" o "Verificada".
- Permitir la carga de una fotografía frontal y dorsal del documento de identidad (Cédula de Identidad o Pasaporte) en formatos válidos (JPG, PNG o PDF) con un peso máximo de 10 MB.
- Permitir opcionalmente la captura de una selfie de validación facial en tiempo real para contrastarla con el documento cargado mediante la API de KYC del ecosistema.
- Si el archivo supera el peso o formato permitido, mostrar el mensaje *"El documento no cumple con los formatos permitidos o excede los 10MB"*.
- Al enviar los documentos exitosamente, cambiar el estado del usuario a "Pendiente de Verificación" y mostrar un mensaje *"Sus documentos han sido enviados con éxito y están siendo evaluados por nuestro sistema de seguridad"*.
- Una vez que el servicio de validación procese los datos, actualizar automáticamente el estado del perfil a "Verificado" (habilitando todas las funciones de reserva y arriendo) o a "Rechazado" (notificando el motivo específico al usuario).

> **Nota:** Incluye la interfaz asociada al panel de subida de documentos y estado de validación KYC.

---

## HU05 - Publicar un espacio físico

**Como** propietario,
**Quiero** registrar y publicar los detalles de mi espacio físico (como quinchos, bodegas, estacionamientos o parcelas) en la plataforma,
**Para que** los usuarios interesados puedan visualizarlo, conocer sus características y solicitar su arriendo de forma digital.

### Criterios de Aceptación
- Tener un formulario de registro de espacio estructurado en secciones: Información General, Ubicación, Tarifas y Multimedia.
- El título del espacio debe tener una longitud mínima de 10 caracteres y máxima de 100 caracteres; si no cumple, mostrar el mensaje *"El título debe tener entre 10 y 100 caracteres"*.
- Validar que la categoría seleccionada pertenezca a las opciones permitidas del sistema (Quincho, Bodega, Estacionamiento, Parcela, Salón o Centro de Eventos).
- En la sección de ubicación, el sistema debe integrar un mapa interactivo para fijar las coordenadas exactas y exigir que se ingrese la dirección completa (Calle, Número, Comuna).
- En la sección de tarifas, el precio por hora o por día ingresado debe ser mayor a 0; de lo contrario, mostrar el mensaje *"La tarifa debe ser un valor numérico mayor a cero"*.
- Permitir cargar entre un mínimo de 3 y un máximo de 10 imágenes en formato JPG o PNG, donde cada archivo no supere los 5 MB.
- Si se intenta subir un archivo con formato no válido o peso excedido, mostrar el mensaje *"El archivo [nombre_archivo] no es válido o supera el tamaño máximo permitido de 5MB"*.
- Si faltan campos obligatorios al intentar guardar, resaltar los campos en rojo y mostrar el mensaje superior *"Por favor, complete todos los campos obligatorios marcados en rojo para continuar"*.
- Si el espacio se registra exitosamente, guardar el registro con estado "Activo", mostrar una pantalla de éxito con el mensaje *"Su espacio ha sido publicado con éxito"* y un botón para "Ver mi publicación".

> **Nota:** Incluye la interfaz asociada al panel de control del propietario y el formulario paso a paso de publicación de anuncios.

---

## HU06 - Editar y actualizar información de un espacio

**Como** propietario,
**Quiero** modificar los datos, descripciones, fotografías o tarifas de un anuncio previamente publicado,
**Para que** la información mostrada a los arrendatarios esté siempre actualizada y refleje las condiciones reales del inmueble.

### Criterios de Aceptación
- Tener un listado en el panel del propietario con los espacios publicados y un botón de "Editar" en cada tarjeta.
- Al hacer clic en "Editar", cargar un formulario precargado con los datos actuales del espacio registrado.
- Permitir modificar cualquier campo editable (descripción, reglas de uso, capacidad máxima, tarifas o agregar/eliminar fotografías).
- Si se intenta modificar la tarifa dejándola en valor cero o negativo, mostrar el mensaje *"La tarifa actualizada debe ser mayor a cero"* y bloquear la actualización.
- Al guardar los cambios, mostrar una ventana de confirmación *"¿Está seguro de actualizar la información de este espacio?"* con opciones de Confirmar y Cancelar.
- Si se confirma, actualizar los registros en la base de datos de manera inmediata, mostrar un mensaje de éxito *"Anuncio actualizado correctamente"* y redirigir al listado de espacios del anfitrión.

> **Nota:** Incluye la interfaz asociada al panel de edición de anuncios del propietario.

---

## HU07 - Establecer reglas de uso y restricciones del espacio

**Como** propietario del espacio,
**Quiero** definir reglas específicas de uso, políticas de cancelación y restricciones (ej. prohibido fumar, acceso de mascotas, límite de ruido) para mi inmueble,
**Para que** los arrendatarios conozcan las condiciones antes de reservar y se proteja la integridad de mi propiedad.

### Criterios de Aceptación
- Tener una sección específica dentro del formulario de publicación o edición llamada "Normas y Restricciones" con casillas de verificación (Checkboxes) predefinidas y un campo de texto libre para reglas personalizadas.
- Permitir seleccionar políticas de cancelación (Flexible, Moderada o Estricta) mediante un selector desplegable con su respectiva descripción de plazos.
- Si el usuario escribe una regla personalizada que exceda los 250 caracteres, mostrar un mensaje de advertencia *"La regla personalizada no puede superar los 250 caracteres"*.
- Guardar las reglas asociadas directamente al identificador único del espacio en la base de datos.
- Visualizar claramente estas reglas y la política de cancelación seleccionada en la vista de detalle del espacio para que el arrendatario deba aceptarlas obligatoriamente antes de proceder con la reserva.

> **Nota:** Incluye la interfaz asociada a la configuración de normativas en el panel del anfitrión.

---

## HU08 - Desactivar o eliminar temporalmente un espacio

**Como** propietario del espacio,
**Quiero** cambiar el estado de mi anuncio a "Inactivo" o "Pausado",
**Para que** el espacio deje de aparecer en los resultados de búsqueda del marketplace cuando no esté disponible para arriendo.

### Criterios de Aceptación
- Tener un interruptor (Switch) o botón de estado ("Activo" / "Pausado") en cada tarjeta de espacio dentro del panel de control del propietario.
- Si el espacio posee reservas vigentes o futuras confirmadas al momento de intentar pausarlo, mostrar una ventana de advertencia: *"No puede desactivar este espacio porque tiene reservas activas pendientes. Debe atenderlas o cancelarlas primero"*.
- Si no existen reservas pendientes, al hacer clic en desactivar, solicitar una confirmación mediante un modal *"¿Desea pausar la visibilidad de este espacio en el marketplace?"*.
- Al confirmar la acción, cambiar el estado del anuncio a "Inactivo" en tiempo real, ocultándolo instantáneamente de los resultados de búsqueda general.
- Permitir reactivar el espacio en cualquier momento volviendo a accionar el interruptor a "Activo", lo cual validará nuevamente que cumpla con los requisitos mínimos de publicación.

> **Nota:** Incluye la interfaz asociada al panel de control de anuncios y modales de confirmación de estado.

---

## HU09 - Gestionar adicionales o equipamiento extra del espacio

**Como** propietario del espacio,
**Quiero** agregar opcionalmente equipamiento o servicios adicionales asociados a mi espacio (ej. proyector, parlantes, servicio de limpieza final, sillas extra) con su respectiva tarifa,
**Para que** los arrendatarios puedan seleccionarlos de forma opcional al momento de hacer su reserva.

### Criterios de Aceptación
- Tener una subsección en la administración del espacio titulada "Equipamiento y Adicionales" con un botón de "Añadir Ítem".
- Permitir ingresar el nombre del adicional (ej. "Proyector HD"), una breve descripción y el costo asociado (fijo o por hora), validando que el precio sea mayor o igual a 0.
- Si se intenta guardar un adicional sin nombre o con un precio inválido, resaltar el campo y mostrar el mensaje *"Debe ingresar un nombre válido y una tarifa para el adicional"*.
- Permitir eliminar o editar cualquier adicional creado mediante botones dedicados en la interfaz.
- Visualizar los adicionales disponibles con sus precios en la pantalla de detalle y selección de reservas del arrendatario, permitiéndole seleccionarlos opcionalmente para recalcular el monto total a pagar.

> **Nota:** Incluye la interfaz asociada a la gestión de adicionales en el panel del anfitrión y su vista en el checkout.

---

## HU10 - Búsqueda general de espacios

**Como** arrendatario,
**Quiero** ingresar términos de búsqueda en una barra principal de texto (por ejemplo, por nombre, comuna o tipo de espacio),
**Para que** el sistema me devuelva un listado preliminar con los anuncios que coincidan con lo que estoy buscando.

### Criterios de Aceptación
- Tener una barra de búsqueda prominente en la página de inicio y en la cabecera principal de la plataforma web y móvil.
- Permitir ingresar palabras clave con un mínimo de 3 caracteres; si se ingresan menos, mostrar un aviso sutil *"Ingrese al menos 3 caracteres para iniciar la búsqueda"*.
- Si la búsqueda de texto no arroja resultados coincidentes, mostrar una vista vacía con el mensaje *"No se encontraron resultados para '[término_buscado]', intente con otra palabra clave"*.
- Al presionar enter o hacer clic en la lupa, actualizar dinámicamente la vista mostrando las tarjetas de los espacios coincidentes ordenadas por relevancia.

> **Nota:** Incluye la interfaz asociada a la barra de búsqueda global y la grilla de resultados preliminares.

---

## HU11 - Filtrado avanzado de espacios

**Como** arrendatario,
**Quiero** aplicar filtros múltiples (rango de precios, categoría de espacio, capacidad de personas y comuna),
**Para que** los resultados de búsqueda se acoten exclusivamente a los espacios que cumplen con mis requerimientos específicos.

### Criterios de Aceptación
- Tener un panel lateral o desplegable de filtros avanzados que incluya selectores de categorías, controles deslizantes de precio mínimo/máximo y selector de capacidad de personas.
- Si el usuario establece un precio mínimo mayor al precio máximo, mostrar de inmediato una validación en pantalla *"El precio mínimo no puede superar al precio máximo"* y deshabilitar el botón de aplicar filtros.
- Permitir restablecer o limpiar todos los filtros aplicados haciendo clic en un botón de "Limpiar filtros", el cual recargará el listado general predeterminado.
- Los resultados filtrados deben actualizarse de manera asíncrona (sin recargar la página completa) en la interfaz de usuario.

> **Nota:** Incluye la interfaz asociada al panel de filtros avanzados y controles de selección múltiple.

---

## HU12 - Visualización de espacios en mapa interactivo

**Como** arrendatario,
**Quiero** visualizar la ubicación de los espacios disponibles marcados con pines interactivos dentro de un mapa digital,
**Para que** pueda evaluar geográficamente qué tan cerca o accesible se encuentra el espacio respecto a mi ubicación o zona de interés.

### Criterios de Aceptación
- Integrar un componente de mapa interactivo (basado en servicios como Google Maps) en la pantalla de resultados de búsqueda.
- Cada espacio activo dentro de la zona visible del mapa debe representarse mediante un pin interactivo que muestre el precio referencial por hora o día.
- Al hacer clic sobre un pin en el mapa, se debe desplegar una tarjeta flotante resumen con la foto principal, título, valoración y un enlace directo a los detalles del espacio.
- Al hacer zoom o mover el mapa, los pines visibles deben actualizarse dinámicamente en función de las coordenadas del área mostrada en pantalla.

> **Nota:** Incluye la interfaz asociada al mapa interactivo de geolocalización y tarjetas flotantes de vista previa.

---

## HU13 - Visualización de detalle completo de un espacio

**Como** arrendatario,
**Quiero** acceder a una vista detallada de un espacio seleccionado (ver galería completa de fotos, descripción detallada, reglas de uso, valoraciones y equipamiento),
**Para que** cuente con toda la información necesaria antes de tomar la decisión de solicitar una reserva.

### Criterios de Aceptación
- Al hacer clic en cualquier tarjeta de espacio o pin, redirigir a una vista de detalle estructurada en secciones: Galería de imágenes en carrusel, Descripción, Normas de uso, Equipamiento adicional disponible y Comentarios de otros usuarios.
- Permitir hacer clic en las imágenes de la galería para abrirlas en un visor maximizado (lightbox) en pantalla completa.
- Mostrar de forma destacada la información de contacto y validación de identidad (KYC verificado) del propietario del espacio.
- Incluir un bloque flotante lateral o inferior que indique permanentemente la tarifa por unidad de tiempo y un botón principal de llamada a la acción "Reservar ahora".

> **Nota:** Incluye la interfaz asociada a la vista de detalles y carrusel multimedia del inmueble.

---

## HU14 - Guardar espacios en lista de favoritos

**Como** arrendatario,
**Quiero** marcar con un icono de corazón o guardar los espacios que me interesan en una lista de "Favoritos",
**Para que** pueda revisarlos y compararlos fácilmente más adelante sin tener que volver a realizar la búsqueda.

### Criterios de Aceptación
- Incluir un botón flotante con forma de icono de corazón en la esquina superior de cada tarjeta de espacio y en la vista de detalle.
- Al hacer clic en el icono, si el usuario ha iniciado sesión, el estado del botón debe cambiar visualmente a "Marcado" (relleno de color) y guardar el registro del espacio en su lista personal de favoritos asociada a su cuenta.
- Si el usuario no ha iniciado sesión al intentar guardar un favorito, mostrar una ventana flotante o modal invitándolo a iniciar sesión o registrarse.
- Tener una sección dedicada en el perfil del arrendatario titulada "Mis Espacios Favoritos" donde se listen todas las publicaciones guardadas, permitiendo acceder a ellas o eliminarlas de la lista con un botón de remover.

> **Nota:** Incluye la interfaz asociada al botón de favoritos y al panel de gestión de espacios guardados del usuario.

---

## HU15 - Selección de bloques de fecha y hora para reserva

**Como** arrendatario,
**Quiero** seleccionar un rango de fechas y horarios disponibles en el calendario interactivo de un espacio,
**Para que** el sistema verifique la disponibilidad en tiempo real y me permita avanzar con la solicitud de arriendo.

### Criterios de Aceptación
- Tener un componente de calendario interactivo en la vista de detalle del espacio que muestre claramente los días y horas ocupadas (en color gris/bloqueado) y los disponibles (en color habilitado).
- Permitir al usuario seleccionar una fecha de inicio y una fecha/hora de término de acuerdo con el formato establecido por el propietario (por horas o por días completos).
- Si el usuario intenta seleccionar un rango de fechas que incluye días u horas previamente reservadas por otro cliente, mostrar un mensaje de error inmediato: *"El rango seleccionado contiene bloques de tiempo no disponibles, por favor elija otro horario"*.
- Validar que la fecha de reserva seleccionada sea estrictamente posterior a la fecha y hora actual del sistema; si es pasada, mostrar el mensaje *"No se pueden realizar reservas en fechas u horas pasadas"*.
- Al completar una selección válida de fechas, el sistema debe calcular automáticamente la cantidad total de horas o días seleccionados.
- Mostrar un resumen preliminar del tiempo seleccionado junto con el botón activo de "Continuar con la reserva".

> **Nota:** Incluye la interfaz asociada al selector de calendario interactivo y bloqueo de celdas temporales.

---

## HU16 - Cálculo automático de tarifas, comisiones y garantía

**Como** arrendatario,
**Quiero** visualizar un desglose detallado de los costos (tarifa base del espacio, comisión por servicio de la plataforma y monto de la garantía temporal por daños) antes de pagar,
**Para que** sepa exactamente el monto total transparente que se me cobrará por la transacción.

### Criterios de Aceptación
- Al confirmar los bloques de tiempo, el sistema debe calcular de forma automática la tarifa base multiplicando el tiempo seleccionado por el valor unitario configurado por el propietario.
- Calcular e incorporar de forma visible la comisión porcentual de la plataforma aplicada al arrendatario (ej. 5% sobre el subtotal).
- Añadir el monto de la garantía temporal por daños definida para ese espacio específico, informando claramente que dicho monto es reembolsable sujeto a inspección posterior.
- Si el usuario selecciona equipamiento adicional (adicionales de la HU09), el sistema debe sumarlos automáticamente al desglose general de costos en tiempo real.
- Mostrar una tabla resumen con los ítems desglosados: Subtotal de arriendo, Comisión de servicio, Monto de garantía, Adicionales (si aplica) y el Total a pagar final.
- Si ocurre un error de cálculo en los servicios internos del servidor, mostrar un mensaje de alerta: *"Error al calcular los costos de la reserva, por favor intente nuevamente"*, bloqueando el avance al pago hasta que se refresquen los datos.

> **Nota:** Incluye la interfaz asociada al resumen de costos en el checkout.

---

## HU17 - Integración con pasarela de pago en línea

**Como** arrendatario,
**Quiero** ser redirigido de forma segura a una pasarela de pago integrada (como Transbank o Mercado Pago) para efectuar el pago total de la reserva,
**Para que** la transacción se procese bajo estándares bancarios seguros y certificados.

### Criterios de Aceptación
- Al presionar el botón "Proceder al Pago" en el resumen de costos, validar previamente que el usuario cuente con su cuenta con estado "Verificado" (KYC aprobado).
- Si el usuario no ha completado su verificación de identidad (KYC), interrumpir el flujo y redirigirlo obligatoriamente a la pantalla de validación de documentos con un aviso explicativo.
- Generar una orden de pago con un identificador único y redirigir al usuario de forma segura a la interfaz externa de la pasarela de pago seleccionada (Transbank / Mercado Pago).
- Establecer un tiempo límite de sesión de pago de 15 minutos en la pasarela; si el usuario supera este tiempo sin pagar, la sesión expira y se libera el bloqueo temporal de la fecha en el calendario.
- Si el usuario cancela voluntariamente la transacción dentro de la pasarela de pago, retornar a la plataforma mostrando el mensaje *"El proceso de pago fue cancelado por el usuario, su reserva ha quedado en estado pendiente"*.
- Si la entidad bancaria rechaza la transacción (fondos insuficientes, tarjeta bloqueada o error de red), mostrar el mensaje: *"El pago no pudo ser procesado por el banco: [motivo_rechazo]. Por favor intente con otro medio de pago"*.

> **Nota:** Incluye la interfaz asociada al enlace de pasarela de pago externa y mensajes de retorno de estado.

---

## HU18 - Confirmación de reserva y bloqueo de calendario

**Como** sistema de la plataforma EspaciGo,
**Quiero** procesar la respuesta exitosa de la pasarela de pago,
**Para que** se confirme formalmente la reserva, se bloqueen las fechas en el calendario del propietario y se notifique a ambas partes.

### Criterios de Aceptación
- Al recibir el código de aprobación exitoso (Webhook / Retorno OK) desde la pasarela de pago, cambiar el estado de la reserva de "Pendiente" a "Confirmada" de manera automática.
- Bloquear de forma permanente los bloques de fecha y hora correspondientes en el calendario en tiempo real del espacio para evitar sobreventa o cruces de horarios.
- Generar un comprobante de reserva digital en formato PDF que incluya un código alfanumérico único de seguimiento y los datos clave del contrato temporal.
- Enviar un correo electrónico automático de confirmación al arrendatario adjuntando el comprobante digital y las instrucciones de acceso al inmueble.
- Enviar una notificación y correo electrónico automático al propietario del espacio informándole sobre la nueva reserva confirmada y los ingresos acreditados en su panel.
- Redirigir al usuario arrendatario a una pantalla de éxito dentro de la plataforma que muestre el mensaje *"¡Pago exitoso! Su reserva ha sido confirmada correctamente"* junto con un botón para ver "Mis Reservas".

> **Nota:** Incluye la interfaz asociada a la pantalla de éxito de pago, notificaciones y comprobante digital.

---

## HU19 - Cancelación de reserva y gestión de devolución

**Como** arrendatario,
**Quiero** cancelar una reserva confirmada dentro de los plazos establecidos por las políticas de cancelación del espacio,
**Para que** se gestione la anulación del servicio y la devolución de los fondos o de la garantía según corresponda.

### Criterios de Aceptación
- Tener una sección de "Mis Reservas" con un botón de "Cancelar Reserva" disponible para cada transacción que cumpla con los plazos de la política de cancelación elegida.
- Si el usuario intenta cancelar fuera del plazo límite permitido por las reglas del espacio (ej. menos de 24 horas antes), mostrar el mensaje *"No es posible cancelar la reserva debido a que se encuentra fuera del plazo establecido por la política de cancelación"*.
- Al solicitar una cancelación válida, desplegar un modal de confirmación solicitando el motivo opcional de la anulación y un botón final de "Confirmar Cancelación".
- Al confirmarse la cancelación, cambiar el estado de la reserva a "Cancelada" y liberar de inmediato los bloques de fecha y hora en el calendario del propietario.
- Ejecutar la instrucción a la pasarela de pago para iniciar el proceso de reembolso automático del monto de tarifa o garantía según aplique la regla de penalización.
- Enviar correos electrónicos automáticos a ambas partes involucradas informando que la reserva ha sido cancelada exitosamente y detallando el estado de devolución de los fondos.

> **Nota:** Incluye la interfaz asociada al panel de gestión de reservas y modales de anulación.

---

## HU20 - Gestión y sincronización del calendario de disponibilidad

**Como** propietario del espacio,
**Quiero** visualizar y gestionar un calendario interactivo en tiempo real con los estados de ocupación de mi inmueble,
**Para que** pueda llevar un control exacto de los días disponibles, reservados o bloqueados por mantenimiento.

### Criterios de Aceptación
- Tener un panel dedicado en la vista del propietario titulado "Mi Calendario" que muestre un componente de calendario mensual y semanal interactivo.
- Cada celda o bloque de tiempo en el calendario debe reflejar visualmente su estado actual mediante códigos de color diferenciados: Verde (Disponible), Rojo (Reservado/Ocupado) y Amarillo (Bloqueado por mantenimiento).
- Al hacer clic sobre cualquier fecha u hora libre en el calendario, el sistema debe desplegar un menú rápido de opciones que permita "Bloquear fecha manualmente" o "Liberar bloque".
- Si el propietario intenta bloquear un día que ya cuenta con una reserva confirmada activa, el sistema debe mostrar una alerta emergente: *"No es posible bloquear este día porque posee una reserva confirmada vigente"* y denegar la acción.
- Al actualizar cualquier estado de disponibilidad en el calendario, la base de datos debe sincronizarse de manera inmediata para reflejar el cambio en tiempo real hacia el buscador de los arrendatarios.
- Permitir navegar entre meses anteriores y futuros mediante flechas de control rápido en la interfaz del calendario sin perder la sesión activa.
- Si ocurre un error de sincronización con el servidor al intentar modificar un bloque, mostrar un mensaje de error flotante: *"Error al actualizar el calendario, por favor intente nuevamente"*.
- Incluir un botón de exportación o sincronización externa de calendario (estándar iCal) para que el propietario pueda enlazar las fechas ocupadas con sus calendarios personales externos.

> **Nota:** Incluye la interfaz asociada al panel de control de calendario del anfitrión y los selectores de estado.

---

## HU21 - Bloqueo manual de fechas por mantenimiento o uso personal

**Como** propietario del espacio,
**Quiero** seleccionar un rango de fechas u horas específicas y bloquearlas manualmente ingresando un motivo (ej. reparaciones, uso personal),
**Para que** ningún arrendatario pueda solicitar reservas en esos periodos de tiempo en los que el espacio no estará operativo.

### Criterios de Aceptación
- Tener un botón destacado en el panel de calendario llamado "Nuevo Bloqueo Manual" que active un formulario emergente de selección de rangos temporales.
- El formulario debe requerir obligatoriamente la selección de una fecha/hora de inicio, una fecha/hora de término y un campo de texto para detallar el motivo del bloqueo.
- Validar que la fecha de término del bloqueo manual sea estrictamente posterior a la fecha de inicio; si es igual o anterior, mostrar el mensaje *"La fecha de término debe ser posterior a la fecha de inicio"*.
- Si el campo de motivo se deja en blanco al intentar guardar, resaltar el campo en rojo y mostrar el aviso *"Debe ingresar obligatoriamente un motivo para el bloqueo manual"*.
- El sistema debe verificar en tiempo real que el rango seleccionado no cruce con reservas de clientes existentes; de haber cruces, mostrar el mensaje *"El rango seleccionado interfiere con una reserva activa existente"*.
- Al confirmar el bloqueo manual exitosamente, las celdas correspondientes en el calendario del propietario deben cambiar inmediatamente a estado "Bloqueado" de color amarillo.
- Permitir al propietario eliminar o revertir un bloqueo manual haciendo clic sobre el bloque en el calendario y seleccionando la opción "Desbloquear periodo".
- Registrar la acción de bloqueo manual en el historial de auditoría interno del sistema asociado al ID del espacio correspondiente.

> **Nota:** Incluye la interfaz asociada al modal de bloqueo manual y campos de justificación.

---

## HU22 - Visualización de ocupación y estadísticas temporales

**Como** propietario del espacio,
**Quiero** visualizar un reporte gráfico de los niveles de ocupación y uso de mi espacio en diferentes periodos (semanal, mensual o anual),
**Para que** pueda analizar el rendimiento de mis arriendos y la rentabilidad obtenida.

### Criterios de Aceptación
- Tener una pestaña en el panel del anfitrión titulada "Estadísticas y Rendimiento" con gráficos de barras o líneas interactivos.
- Permitir filtrar las métricas visualizadas seleccionando un rango de tiempo predefinido (Último mes, Últimos 3 meses, Último año o Rango personalizado).
- Mostrar indicadores clave de rendimiento (KPIs) en tarjetas superiores: Total de horas/días arrendados, Ingresos netos acumulados y Porcentaje de ocupación del espacio.
- Si el espacio no registra actividad ni reservas en el rango de tiempo seleccionado, el gráfico debe mostrar un estado vacío con el mensaje *"No hay datos suficientes para mostrar estadísticas en este periodo"*.
- Permitir exportar el reporte estadístico en formato descargable (PDF o CSV) haciendo clic en un botón de "Descargar Reporte".
- Validar que si el usuario selecciona un rango de fechas personalizado donde la fecha inicial supera a la final, mostrar una advertencia: *"El rango de fechas seleccionado no es válido"*.
- Los datos estadísticos deben calcularse de manera dinámica desde la base de datos cada vez que el usuario cambie los filtros temporales.
- Incluir información contextual o tooltips informativos en cada métrica para explicar al propietario cómo se calcula el porcentaje de ocupación.

> **Nota:** Incluye la interfaz asociada al panel de reportes gráficos y tarjetas de métricas del anfitrión.

---

## HU23 - Sincronización automática de estados de reserva en el calendario

**Como** sistema de la plataforma EspaciGo,
**Quiero** actualizar automáticamente los estados del calendario ante cualquier cambio en el ciclo de vida de una reserva (confirmación, cancelación o expiración),
**Para que** nunca existan discrepancias entre las reservas pagadas y la disponibilidad visualizada en el marketplace.

### Criterios de Aceptación
- Escuchar de forma continua los eventos de cambio de estado generados en el módulo de pagos y reservas mediante un servicio de escucha interna (Event Listener).
- Cuando una reserva pase a estado "Confirmada", el sistema debe actualizar de forma automática e instantánea las celdas del calendario del espacio a estado "Ocupado".
- Si una reserva en estado "Pendiente" expira por superar los 15 minutos de plazo de pago, el sistema debe liberar automáticamente las celdas temporales en el calendario devolviéndolas a estado "Disponible".
- Ante la cancelación válida de una reserva confirmada, el sistema debe ejecutar una rutina de liberación de fechas que reactive de inmediato la disponibilidad en el calendario público.
- Si ocurre un fallo de concurrencia donde dos usuarios intentan reservar el mismo bloque milimétricamente al mismo tiempo, el sistema debe aplicar un bloqueo de base de datos (Transacción ACID) para adjudicar la reserva exclusivamente al primer pago validado y rechazar el segundo.
- Enviar un registro de log interno al servidor cada vez que se ejecute una actualización automática de calendario por cambio de estado.
- Mostrar una notificación en el panel del propietario indicando: *"Se ha liberado un bloque en su calendario debido a la cancelación de la reserva #[ID_reserva]"*.
- Garantizar que el tiempo de propagación del cambio de estado en el calendario público no supere los 2 segundos tras la confirmación del pago.

> **Nota:** Incluye la interfaz asociada a los registros de eventos del sistema y la actualización en tiempo real de la disponibilidad.

---

## HU24 - Configuración de horarios recurrentes de disponibilidad

**Como** propietario del espacio,
**Quiero** definir patrones de disponibilidad recurrente (por ejemplo, habilitar mi quincho solo los fines de semana o de lunes a viernes en horario vespertino),
**Para que** el sistema bloquee automáticamente los días u horas fuera de ese patrón sin necesidad de hacerlo manualmente uno por uno.

### Criterios de Aceptación
- Tener una sección de configuración avanzada en el perfil del espacio titulada "Horarios Recurrentes de Atención".
- Permitir seleccionar qué días de la semana el espacio se encuentra operativo mediante casillas de verificación (Lunes a Domingo).
- Para cada día seleccionado como operativo, permitir ingresar un rango de horas de apertura y cierre (ej. 09:00 a 20:00 hrs).
- Validar que la hora de cierre configurada sea estrictamente posterior a la hora de apertura; de lo contrario, mostrar el mensaje *"La hora de cierre debe ser posterior a la hora de apertura"*.
- Al guardar el patrón recurrente, el sistema debe aplicar de forma masiva el bloqueo automático en el calendario para todos los bloques horarios que queden fuera del patrón establecido.
- Si el propietario intenta configurar un horario recurrente que colisiona con una reserva confirmada ya existente en el periodo excluido, mostrar una advertencia: *"No puede restringir este horario porque existen reservas activas en ese bloque"*.
- Permitir modificar o desactivar las reglas de horario recurrente haciendo clic en un botón de "Restablecer Horarios por Defecto".
- Visualizar de forma clara en la descripción del espacio para los arrendatarios cuáles son los días y horarios recurrentes permitidos por el anfitrión.

> **Nota:** Incluye la interfaz asociada a la matriz de configuración de horarios recurrentes en el panel del anfitrión.

---

## HU25 - Sistema de calificaciones y reseñas recíprocas

**Como** usuario de la plataforma (propietario o arrendatario),
**Quiero** calificar con estrellas (de 1 a 5) y dejar un comentario detallado sobre mi experiencia con la otra parte tras finalizar una reserva,
**Para que** se construya una reputación confiable dentro de la comunidad de EspaciGo.

### Criterios de Aceptación
- Tener habilitada una sección de "Calificar Experiencia" en el historial de reservas únicamente cuando el estado de la transacción sea "Completada".
- Permitir seleccionar una puntuación de estrellas entera en un rango de 1 a 5 y escribir un comentario de texto descriptivo con un límite máximo de 500 caracteres.
- Si el usuario intenta enviar una reseña dejando el campo de estrellas vacío o sin puntuación, mostrar el mensaje *"Debe seleccionar una puntuación de estrellas obligatoriamente"*.
- Si el comentario supera los 500 caracteres permitidos, mostrar un aviso de validación *"El comentario no puede exceder los 500 caracteres"*.
- Al enviar la reseña exitosamente, guardarla de forma asociada al perfil del usuario evaluado y recalcular automáticamente su promedio general de calificaciones públicas.
- Permitir que tanto el propietario como el arrendatario se califiquen mutuamente en un plazo máximo de hasta 14 días posteriores al término de la reserva.
- Mostrar las reseñas publicadas de forma pública en la vista de detalle del espacio y en los perfiles de los usuarios correspondientes.
- Si un usuario intenta enviar una segunda reseña para la misma reserva ya evaluada, el sistema debe bloquear la acción mostrando el mensaje *"Ya ha emitido una calificación para esta reserva"*.

> **Nota:** Incluye la interfaz asociada al formulario de estrellas y el bloque de reseñas públicas.

---

## HU26 - Panel de control y supervisión del administrador

**Como** administrador del sistema,
**Quiero** acceder a un panel de control general con métricas globales de la plataforma, usuarios registrados y espacios activos,
**Para que** pueda supervisar el correcto funcionamiento y la actividad general de EspaciGo.

### Criterios de Aceptación
- Tener una ruta de acceso exclusiva y protegida para el rol de Administrador, requiriendo autenticación de doble factor o credenciales elevadas.
- Visualizar un tablero principal (Dashboard) que muestre indicadores clave en tiempo real: Total de usuarios activos, Total de espacios publicados, Reservas del mes y Volumen monetario transaccionado.
- Permitir filtrar los datos globales del panel seleccionando un rango de fechas específico mediante selectores de periodo.
- Si el usuario administrador no cuenta con los permisos de rol correspondientes e intenta acceder a la ruta, el sistema debe denegar el acceso y redirigirlo a la página de inicio con un error 403.
- Incluir un listado completo de gestión de usuarios con opciones para buscar por correo, ver estado de cuenta y aplicar suspensiones manuales.
- Incluir una tabla de supervisión de espacios con accesos directos para revisar publicaciones reportadas o pendientes de revisión.
- Permitir exportar reportes generales de actividad en formato CSV directamente desde el panel de control haciendo clic en un botón de exportación.
- Registrar todas las acciones críticas ejecutadas por el administrador dentro del panel en una tabla de auditoría interna del sistema.

> **Nota:** Incluye la interfaz asociada al dashboard del administrador y las tablas globales de gestión.

---

## HU27 - Moderación y gestión de anuncios reportados

**Como** administrador del sistema,
**Quiero** revisar los espacios o reseñas que hayan sido reportados por los usuarios debido a incumplimiento de normas,
**Para que** pueda tomar decisiones de moderación como bloquear, ocultar o eliminar contenido inapropiado.

### Criterios de Aceptación
- Tener una sección en el panel de administración titulada "Moderación de Contenido" que liste todas las publicaciones o reseñas que acumulen reportes de usuarios.
- Cada ítem reportado debe mostrar el motivo del reporte, la fecha, el usuario denunciante y un enlace directo al contenido afectado.
- Permitir al administrador tomar acciones de moderación sobre el anuncio o reseña: "Desestimar reporte", "Ocultar temporalmente" o "Eliminar permanentemente".
- Si el administrador selecciona eliminar o bloquear un espacio, el sistema debe requerir obligatoriamente el ingreso de una justificación en un campo de texto de motivo.
- Al confirmar la acción de bloqueo de un espacio reportado, cambiar su estado a "Suspendido por Moderación" y ocultarlo de forma inmediata del marketplace público.
- Enviar un correo electrónico automático de notificación al propietario del espacio afectado informando el motivo por el cual su anuncio ha sido moderado o suspendido.
- Permitir al administrador reactivar un anuncio si el propietario subsana el problema y se vuelve a aprobar tras una nueva revisión.
- Registrar en la bitácora de auditoría el ID del administrador que realizó la moderación, la fecha y la sanción aplicada.

> **Nota:** Incluye la interfaz asociada a la bandeja de reportes y herramientas de moderación del administrador.

---

## HU28 - Resolución de disputas e incidencias de reservas

**Como** administrador del sistema,
**Quiero** gestionar y mediar en las disputas o reclamos reportados entre propietarios y arrendatarios (por ejemplo, daños a la propiedad o incumplimientos),
**Para que** pueda resolver el caso dictaminando la retención o devolución de la garantía económica retenida.

### Criterios de Aceptación
- Tener una sección en el panel del administrador titulada "Gestión de Disputas" donde se listen los reclamos abiertos por los usuarios dentro del plazo de garantía.
- Al abrir una disputa, el administrador debe visualizar el expediente completo que incluya: datos de la reserva, comprobantes, chat de soporte y fotografías de evidencia subidas por ambas partes.
- Permitir al administrador emitir una resolución formal seleccionando entre dos veredictos: "Devolución total de garantía al arrendatario" o "Retención parcial/total de garantía a favor del propietario".
- Si el administrador intenta cerrar la disputa sin seleccionar un veredicto o sin ingresar una nota de resolución, mostrar una alerta *"Debe emitir un veredicto y justificar la resolución del caso"*.
- Al guardar la resolución de la disputa, el sistema debe ordenar de forma automática a la pasarela de pago la ejecución de la transferencia de fondos correspondiente según el dictamen.
- Cambiar el estado de la disputa a "Resuelta" y cerrar formalmente el ticket de incidente en la base de datos.
- Enviar correos electrónicos automáticos a ambas partes involucradas notificando el cierre del caso junto con el detalle de la resolución aplicada.
- Bloquear cualquier intento posterior de abrir una nueva disputa sobre la misma reserva una vez que el estado se encuentre marcado como resuelto.

> **Nota:** Incluye la interfaz asociada al expediente de disputas y los botones de dictamen del administrador.

---

## HU29 - Soporte automatizado y centro de ayuda en línea

**Como** usuario de la plataforma (propietario o arrendatario),
**Quiero** acceder a un centro de ayuda con preguntas frecuentes (FAQs) y un formulario de contacto para soporte técnico,
**Para que** pueda resolver dudas comunes o reportar problemas operativos de forma rápida.

### Criterios de Aceptación
- Tener una sección accesible desde el menú principal titulada "Centro de Ayuda y Soporte" dividida en categorías de preguntas frecuentes (FAQs).
- Permitir buscar soluciones mediante una barra de texto predictiva que filtre las preguntas frecuentes en tiempo real según las palabras ingresadas.
- Incluir un formulario de contacto de soporte si el usuario no encuentra respuesta en las FAQs, solicitando: Asunto, Categoría del problema y Descripción detallada.
- Si el usuario deja la descripción del problema con menos de 10 caracteres al enviar el ticket, mostrar el mensaje *"La descripción del problema debe ser más detallada (mínimo 10 caracteres)"*.
- Al enviar el formulario de soporte exitosamente, generar un ticket con un código único de seguimiento y mostrar el mensaje *"Su solicitud ha sido recibida, nos pondremos en contacto pronto"*.
- Enviar un correo electrónico automático de confirmación al usuario con el número de ticket asignado y un enlace para revisar el estado de su requerimiento.
- Permitir al equipo de soporte y administradores visualizar y responder los tickets abiertos desde su panel de control interno.
- Cambiar el estado del ticket a "Cerrado" una vez que el usuario confirme la resolución de su consulta o el administrador aplique la respuesta definitiva.

> **Nota:** Incluye la interfaz asociada al centro de ayuda, buscador de FAQs y formulario de tickets.

---

## HU30 - Gestión de notificaciones y alertas en tiempo real

**Como** usuario registrado de la plataforma,
**Quiero** recibir notificaciones y alertas visuales dentro de la aplicación y por correo sobre el estado de mis reservas, pagos y mensajes,
**Para que** esté informado de cualquier movimiento importante relacionado con mi actividad en EspaciGo.

### Criterios de Aceptación
- Tener un icono de campana de notificaciones visible en la barra de navegación superior de la plataforma web y móvil con un contador de alertas no leídas.
- Al hacer clic en el icono de la campana, desplegar una lista flotante con las últimas notificaciones ordenadas cronológicamente de más reciente a más antigua.
- Permitir marcar una notificación individual como "Leída" haciendo clic sobre ella, lo cual disminuirá el contador de alertas pendientes.
- Incluir un botón de "Marcar todas como leídas" en la parte superior del listado flotante para actualizar el estado de forma masiva.
- Permitir a los usuarios configurar sus preferencias de notificación en el perfil (activar/desactivar alertas por correo electrónico o notificaciones push en el navegador).
- Si el servicio de mensajería o notificaciones push experimenta un fallo de conexión temporal, almacenar las alertas en cola para reenviarlas de manera asíncrona al restablecerse la red.
- Las notificaciones clave (como confirmación de pago o cancelación de reserva) deben enviarse de forma simultánea como alerta interna y como correo electrónico automatizado.
- Permitir acceder a un historial completo de notificaciones pasadas desde una vista dedicada dentro de la sección de configuración de cuenta del usuario.

> **Nota:** Incluye la interfaz asociada al centro de notificaciones flotante y panel de preferencias de alerta.