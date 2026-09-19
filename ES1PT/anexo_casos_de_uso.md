# Especificación de Casos de Uso - Sistema EspaciGo

## Módulo: Identidad, Autenticación y Privacidad

**Diagrama de Casos de Uso (Referencia)**
* **Actores:** Usuario Visitante, Usuario Autenticado, Administrador, Sistema Externo (Registro Civil / SII)
* **Relaciones Principales:**
  * `CU-01: Registrar Cuenta` $\rightarrow$ `<<include>> Validar Unicidad de Correo`
  * `CU-05: Validar Identidad (KYC/KYB)` $\rightarrow$ `<<include>> Verificar Credenciales Externas` $\rightarrow$ `Consume (Registro Civil / SII)`

### CU-01: Registrar Cuenta

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-01 |
| **Caso de Uso** | Registrar Cuenta |
| **Actor** | Usuario Visitante |
| **Descripción** | El visitante ingresa sus datos para crear una cuenta de acceso en la plataforma. |
| **Pre-condiciones** | No poseer una cuenta activa registrada con el mismo correo electrónico. |
| **Flujo Principal** | 1. El usuario accede al formulario de registro.<br>2. Ingresa correo electrónico y contraseña bajo los parámetros permitidos.<br>3. El sistema valida la unicidad del correo en la base de datos.<br>4. El sistema registra la cuenta en estado "No Verificado" y envía un token de confirmación.<br>5. El sistema muestra mensaje de éxito. |
| **Flujos Alternativos** | **A1. Correo ya registrado (Paso 3):**<br>1. El sistema detecta que el correo ya existe.<br>2. El sistema rechaza el registro y despliega un aviso de error.<br><br>**A2. Formato inválido (Paso 2):**<br>1. El sistema detecta que la contraseña o correo no cumplen el formato requerido.<br>2. El sistema solicita corregir los campos. |
| **Post-condiciones** | Cuenta creada en estado pendiente de verificación de correo. |
| **Referencias Cruzadas** | RF-001 al RF-011 |

### CU-02: Iniciar Sesión

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-02 |
| **Caso de Uso** | Iniciar Sesión |
| **Actor** | Usuario Visitante / Autenticado |
| **Descripción** | El usuario accede a su cuenta ingresando sus credenciales de autenticación. |
| **Pre-condiciones** | Poseer una cuenta registrada y verificada. |
| **Flujo Principal** | 1. El usuario ingresa correo y contraseña en la interfaz de login.<br>2. El sistema valida que las credenciales coincidan con el registro.<br>3. El sistema genera una credencial temporal de sesión (JWT).<br>4. El usuario accede a su panel principal. |
| **Flujos Alternativos** | **A1. Credenciales incorrectas (Paso 2):**<br>1. El sistema rechaza el acceso e incrementa el contador de intentos fallidos.<br>2. Si alcanza 5 intentos fallidos, el sistema bloquea temporalmente la cuenta por 30 minutos y avisa por correo.<br><br>**A2. Cuenta no verificada:**<br>1. El sistema bloquea el inicio de sesión indicando que debe validar su correo electrónico. |
| **Post-condiciones** | Sesión activa iniciada en el sistema. |
| **Referencias Cruzadas** | RF-012 al RF-020 |

### CU-03: Recuperar Contraseña

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-03 |
| **Caso de Uso** | Recuperar Contraseña |
| **Actor** | Usuario Visitante |
| **Descripción** | Permite restablecer la contraseña en caso de olvido mediante un enlace temporal. |
| **Pre-condiciones** | Estar registrado en el sistema. |
| **Flujo Principal** | 1. El usuario solicita recuperación ingresando su correo electrónico.<br>2. El sistema valida la existencia del correo.<br>3. El sistema genera un enlace único de recuperación con expiración de 15 minutos y lo envía por correo.<br>4. El usuario ingresa al enlace y define una nueva contraseña. |
| **Flujos Alternativos** | **A1. Correo no encontrado (Paso 2):**<br>1. El sistema indica que el correo no está registrado en la plataforma.<br><br>**A2. Enlace expirado (Paso 4):**<br>1. El sistema rechaza el cambio de contraseña si han pasado más de 15 minutos y solicita un nuevo envío. |
| **Post-condiciones** | Credencial de acceso actualizada. |
| **Referencias Cruzadas** | RF-021 al RF-024 |

### CU-04: Gestionar Perfil

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-04 |
| **Caso de Uso** | Gestionar Perfil |
| **Actor** | Usuario Autenticado |
| **Descripción** | Permite al usuario consultar y modificar sus datos personales, teléfono y foto de perfil. |
| **Pre-condiciones** | Sesión activa en el sistema. |
| **Flujo Principal** | 1. El usuario accede a la sección de configuración de perfil.<br>2. Modifica campos permitidos (nombre, teléfono o fotografía).<br>3. El sistema valida las restricciones (tamaño de foto, formato de teléfono).<br>4. El sistema guarda los cambios y muestra confirmación. |
| **Flujos Alternativos** | **A1. Archivo de imagen superior al límite (Paso 3):**<br>1. El sistema rechaza la foto si supera los 2MB y solicita un archivo menor. |
| **Post-condiciones** | Datos de perfil actualizados en la base de datos. |
| **Referencias Cruzadas** | RF-025 al RF-034, RF-055, RF-056 |

### CU-05: Validar Identidad (KYC/KYB)

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-05 |
| **Caso de Uso** | Validar Identidad (KYC/KYB) |
| **Actor** | Usuario Autenticado |
| **Descripción** | El usuario valida su identidad como persona natural (Registro Civil) o empresa (SII). |
| **Pre-condiciones** | Sesión activa y datos básicos completos. |
| **Flujo Principal** | 1. El usuario sube fotos de su cédula (KYC) o ingresa el RUT de su empresa (KYB).<br>2. El sistema consume la API externa correspondiente (Registro Civil o SII).<br>3. El sistema recibe respuesta positiva de vigencia.<br>4. El sistema cambia el estado del perfil a "Verificado" y notifica al usuario. |
| **Flujos Alternativos** | **A1. Documento vencido o empresa sin inicio de actividades (Paso 3):**<br>1. La API externa retorna estado negativo.<br>2. El sistema rechaza la validación y deriva el caso al panel de revisión manual del administrador. |
| **Post-condiciones** | Perfil con estado verificado habilitado para transaccionar. |
| **Referencias Cruzadas** | RF-035 al RF-050 |

### CU-06: Solicitar Derecho al Olvido

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-06 |
| **Caso de Uso** | Solicitar Derecho al Olvido |
| **Actor** | Usuario Autenticado |
| **Descripción** | El usuario solicita la eliminación de sus datos personales cumpliendo con la Ley 21.719. |
| **Pre-condiciones** | Sesión activa. |
| **Flujo Principal** | 1. El usuario solicita la eliminación de su cuenta desde la configuración.<br>2. El sistema verifica que no posea reservas activas, pagos pendientes o disputas abiertas.<br>3. El sistema anonimiza los datos transaccionales y elimina de forma irreversible la información personal (PII).<br>4. El sistema cierra la sesión. |
| **Flujos Alternativos** | **A1. Posee procesos activos (Paso 2):**<br>1. El sistema detecta contratos, deudas o reservas pendientes.<br>2. El sistema bloquea la eliminación de la cuenta y emite una alerta explicativa. |
| **Post-condiciones** | Datos personales eliminados/anonimizados. |
| **Referencias Cruzadas** | RF-057 al RF-063 |

### CU-07: Gestionar Validaciones Manuales

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-07 |
| **Caso de Uso** | Gestionar Validaciones Manuales |
| **Actor** | Administrador |
| **Descripción** | El administrador revisa y aprueba o rechaza las solicitudes KYC/KYB que fallaron de forma automática. |
| **Pre-condiciones** | Sesión activa con rol de Administrador. |
| **Flujo Principal** | 1. El administrador accede al panel de validaciones fallidas.<br>2. Revisa los antecedentes aportados por el usuario.<br>3. Selecciona "Aprobar" o "Rechazar" ingresando un motivo obligatorio en caso de rechazo.<br>4. El sistema actualiza el estado del perfil. |
| **Flujos Alternativos** | **A1. Falta de motivo en rechazo (Paso 3):**<br>1. El sistema exige completar el campo de texto descriptivo antes de procesar la acción. |
| **Post-condiciones** | Solicitud de identidad resuelta manualmente. |
| **Referencias Cruzadas** | RF-051 al RF-054 |

---

## Módulo: Gestión de Catálogo y Publicaciones

**Diagrama de Casos de Uso (Referencia)**
* **Actor:** Arrendador Verificado
* **Relaciones Principales:**
  * `CU-08: Crear Publicación de Inmueble` $\rightarrow$ `<<include>> Validar Estado KYC/KYB Previo`

### CU-08: Crear Publicación de Inmueble

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-08 |
| **Caso de Uso** | Crear Publicación de Inmueble |
| **Actor** | Arrendador Verificado |
| **Descripción** | Permite al propietario registrar un nuevo espacio comercial especificando dimensiones, reglas y ubicación. |
| **Pre-condiciones** | El usuario debe contar con validación de identidad KYC/KYB aprobada. |
| **Flujo Principal** | 1. El arrendador accede al panel de creación de publicaciones.<br>2. Ingresa título, descripción, superficie en metros cuadrados, tipo de inmueble, capacidad máxima, reglas y precio base diario.<br>3. Ingresa la dirección física, la cual el sistema transforma automáticamente en coordenadas geográficas (latitud/longitud).<br>4. El sistema valida que todos los campos cumplan con los límites permitidos.<br>5. El sistema guarda la publicación en estado "Borrador" de manera automática y luego cambia a "Activa" tras confirmar el formulario. |
| **Flujos Alternativos** | **A1. Usuario no verificado (Paso 1):**<br>1. El sistema detecta que el host no tiene KYC/KYB aprobado.<br>2. El sistema bloquea el acceso al panel de publicaciones.<br><br>**A2. Datos fuera de rango o campos incompletos (Paso 4):**<br>1. El sistema rechaza el registro y detalla los errores de validación (ej. título muy largo o descripción menor a 100 caracteres). |
| **Post-condiciones** | Publicación creada y visible de forma activa en la plataforma. |
| **Referencias Cruzadas** | RF-064 al RF-076, RF-082 al RF-085 |

### CU-09: Gestionar Galería Fotográfica

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-09 |
| **Caso de Uso** | Gestionar Galería Fotográfica |
| **Actor** | Arrendador Verificado |
| **Descripción** | Permite subir, ordenar, seleccionar portada y eliminar imágenes asociadas a la publicación del inmueble. |
| **Pre-condiciones** | Poseer una publicación creada previamente (borrador o activa). |
| **Flujo Principal** | 1. El arrendador selecciona archivos de imagen desde su dispositivo para agregarlos a la galería.<br>2. El sistema valida que la cantidad total no exceda las 10 unidades y que el peso por archivo sea menor a 5MB.<br>3. El sistema procesa la carga y permite al usuario definir una fotografía como portada principal.<br>4. El sistema almacena la galería vinculada al inmueble. |
| **Flujos Alternativos** | **A1. Exceso de peso o límite de fotos (Paso 2):**<br>1. El sistema rechaza la carga de archivos que superen los 5MB o si se intenta subir la fotografía número 11.<br>2. El sistema despliega un mensaje de error indicando la restricción. |
| **Post-condiciones** | Galería de imágenes actualizada en el anuncio. |
| **Referencias Cruzadas** | RF-077 al RF-081 |

### CU-10: Configurar Calendario y Tarifas

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-10 |
| **Caso de Uso** | Configurar Calendario y Tarifas |
| **Actor** | Arrendador Verificado |
| **Descripción** | Permite al propietario gestionar la disponibilidad de su inmueble bloqueando o desbloqueando fechas específicas. |
| **Pre-condiciones** | Publicación de inmueble existente. |
| **Flujo Principal** | 1. El arrendador accede al calendario interactivo de su publicación.<br>2. Selecciona un rango de fechas y aplica la acción de bloqueo o desbloqueo manual.<br>3. El sistema actualiza en tiempo real los estados de disponibilidad del inmueble en la base de datos. |
| **Flujos Alternativos** | Ninguno relevante a nivel de excepción de bloqueos manuales. |
| **Post-condiciones** | Fechas bloqueadas o habilitadas para futuras búsquedas de arrendatarios. |
| **Referencias Cruzadas** | RF-086 al RF-088 |

### CU-11: Modificar o Dar de Baja Anuncio

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-11 |
| **Caso de Uso** | Modificar o Dar de Baja Anuncio |
| **Actor** | Arrendador Verificado |
| **Descripción** | Permite editar detalles de la publicación, cambiar su visibilidad (oculta/activa) o eliminarla permanentemente. |
| **Pre-condiciones** | Ser propietario de la publicación registrada. |
| **Flujo Principal** | 1. El arrendador selecciona una de sus publicaciones en el panel "Mis Inmuebles".<br>2. Modifica datos permitidos (título, precio base) o cambia el estado a "Oculta" / solicita eliminación permanente.<br>3. El sistema valida las restricciones vigentes y actualiza el estado de la publicación. |
| **Flujos Alternativos** | **A1. Intentar eliminar un inmueble con reservas futuras (Paso 2):**<br>1. El sistema detecta que existen reservas futuras pendientes asociadas al anuncio.<br>2. El sistema rechaza la eliminación permanente y emite una advertencia. |
| **Post-condiciones** | Anuncio modificado, oculto o eliminado de la plataforma según corresponda. |
| **Referencias Cruzadas** | RF-089 al RF-096 |

---

## Módulo: Búsqueda, Filtrado y Motor de Reservas

**Diagrama de Casos de Uso (Referencia)**
* **Actor:** Arrendatario
* **Relaciones Principales:**
  * `CU-12: Buscar Espacios (Mapa / Filtros)` $\rightarrow$ `<<include>> Validar Colisión en Tiempo Real`
  * `CU-14: Solicitar Reserva` $\rightarrow$ `<<include>> CU-13: Cotizar Estadía`
  * `CU-14: Solicitar Reserva` $\rightarrow$ `<<include>> Validar Colisión en Tiempo Real`

### CU-12: Buscar Espacios (Mapa / Filtros)

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-12 |
| **Caso de Uso** | Buscar Espacios (Mapa / Filtros) |
| **Actor** | Arrendatario |
| **Descripción** | Permite al usuario buscar inmuebles disponibles interactuando con un mapa geolocalizado (PostGIS) y aplicando filtros avanzados. |
| **Pre-condiciones** | Conexión a internet estable y publicaciones en estado "Activa" registradas en la plataforma. |
| **Flujo Principal** | 1. El arrendatario accede a la sección de búsqueda y navega por el mapa interactivo o ingresa texto libre.<br>2. Aplica filtros opcionales (precio mínimo/máximo, tipo de inmueble, metros cuadrados mínimos y rango de fechas).<br>3. El sistema consulta la base de datos geoespacial y excluye automáticamente los inmuebles que posean fechas bloqueadas o reservadas en el rango consultado.<br>4. El sistema renderiza los pines correspondientes en el mapa y despliega la cuadrícula de tarjetas con los resultados coincidentes. |
| **Flujos Alternativos** | **A1. Sin resultados coincidentes (Paso 3):**<br>1. El sistema detecta que no hay inmuebles que cumplan con todos los filtros estrictos ingresados.<br>2. El sistema muestra un mensaje indicando que no hay disponibilidad y sugiere relajar los criterios de búsqueda. |
| **Post-condiciones** | Visualización de listado de espacios y pines geolocalizados disponibles. |
| **Referencias Cruzadas** | RF-097 al RF-108 |

### CU-13: Cotizar Estadía

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-13 |
| **Caso de Uso** | Cotizar Estadía |
| **Actor** | Arrendatario |
| **Descripción** | Calcula el desglose económico total de la estadía considerando el precio base, la comisión de servicio y el porcentaje de garantía. |
| **Pre-condiciones** | Selección de un inmueble y un rango de fechas válido. |
| **Flujo Principal** | 1. El arrendatario selecciona las fechas de estadía dentro del detalle de la publicación.<br>2. El sistema multiplica el precio base diario por la cantidad de días seleccionados para obtener el costo total de la estadía.<br>3. El sistema calcula el monto de la comisión de servicio (Fee) y el porcentaje de garantía exigido por el arrendador.<br>4. El sistema muestra el panel de cotización con el desglose transparente de cobros (Estadía + Comisión + Garantía). |
| **Flujos Alternativos** | Ninguno relevante en el cálculo base. |
| **Post-condiciones** | Montos claros y calculados desplegados en pantalla listos para el proceso de reserva. |
| **Referencias Cruzadas** | RF-109 al RF-112 |

### CU-14: Solicitar Reserva

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-14 |
| **Caso de Uso** | Solicitar Reserva |
| **Actor** | Arrendatario |
| **Descripción** | Permite enviar una solicitud formal de reserva tras validar restricciones de fechas y disponibilidad atómica en tiempo real. |
| **Pre-condiciones** | Usuario autenticado y cotización de estadía generada. |
| **Flujo Principal** | 1. El arrendatario presiona el botón "Reservar" tras verificar las fechas (validando que la fecha de inicio sea mayor a la actual y la de fin sea mayor a la de inicio).<br>2. El sistema ejecuta una consulta en tiempo real para verificar que no exista colisión de fechas de último minuto.<br>3. El sistema registra la solicitud con estado "Pendiente de Pago" y redirige al usuario hacia la interfaz de pagos. |
| **Flujos Alternativos** | **A1. Colisión de fechas detectada (Paso 2):**<br>1. El sistema identifica que otro usuario reservó el espacio en paralelo durante los mismos días.<br>2. El sistema rechaza la solicitud de reserva e informa al usuario que debe seleccionar un nuevo rango de fechas. |
| **Post-condiciones** | Intento de reserva registrado a la espera de confirmación de pago. |
| **Referencias Cruzadas** | RF-113 al RF-118 |

---

## Módulo: Sistema Transaccional, Pagos y Escrow

**Diagrama de Casos de Uso (Referencia)**
* **Actores:** Arrendatario, Arrendador, Sistema Core / Automático, Sistema Externo (Pasarela Mercado Pago)
* **Relaciones Principales:**
  * `CU-15: Pagar Reserva y Retener (Escrow)` $\rightarrow$ `<<include>> Procesar Transacción Externa` $\rightarrow$ `Consume (Pasarela Mercado Pago)`
  * `CU-16: Bloquear Garantía (Pre-autorización)` $\rightarrow$ `<<include>> Procesar Transacción Externa`

### CU-15: Pagar Reserva y Retener en Escrow

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-15 |
| **Caso de Uso** | Pagar Reserva y Retener en Escrow |
| **Actor** | Arrendatario |
| **Descripción** | Permite procesar el pago de la estadía a través de la pasarela externa, reteniendo los fondos en una bóveda virtual segura. |
| **Pre-condiciones** | Solicitud de reserva previamente registrada en estado "Pendiente de Pago". |
| **Flujo Principal** | 1. El arrendatario ingresa los datos de su tarjeta de crédito o débito en la interfaz de pagos.<br>2. El sistema envía el token de pago y los montos correspondientes a la API de la pasarela de pagos externa.<br>3. La pasarela procesa y aprueba la transacción de forma exitosa.<br>4. El sistema recibe la confirmación y cambia el estado de la reserva a "Pagada_Escrow", manteniendo el dinero retenido temporalmente. |
| **Flujos Alternativos** | **A1. Fondos insuficientes o rechazo bancario (Paso 3):**<br>1. La pasarela rechaza la transacción de pago.<br>2. El sistema cambia el estado de la reserva a "Cancelada_Por_Pago" e informa al usuario para que reintente con otro medio. |
| **Post-condiciones** | Fondos retenidos de forma segura bajo el modelo de fideicomiso (Escrow). |
| **Referencias Cruzadas** | RF-119 al RF-125 |

### CU-16: Bloquear Garantía (Pre-autorización)

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-16 |
| **Caso de Uso** | Bloquear Garantía (Pre-autorización) |
| **Actor** | Sistema Core / Automático |
| **Descripción** | Ejecuta un bloqueo de cupo (pre-autorización) por el monto de la garantía en la tarjeta de crédito del arrendatario sin realizar un cargo monetario efectivo inicial. |
| **Pre-condiciones** | Proceso de pago de reserva completado exitosamente (CU-15). |
| **Flujo Principal** | 1. De forma automatizada tras el pago, el Sistema Core solicita a la pasarela realizar una pre-autorización por el monto exacto de la garantía.<br>2. La pasarela aprueba y aplica el bloqueo temporal de cupo en la tarjeta del usuario.<br>3. El sistema registra el éxito del bloqueo en la base de datos operativa. |
| **Flujos Alternativos** | **A1. Tarjeta sin cupo para garantía (Paso 2):**<br>1. La pasarela rechaza la pre-autorización por límite excedido.<br>2. El sistema anula la reserva por incumplimiento de garantías y gatilla el reembolso del pago de estadía. |
| **Post-condiciones** | Cupo de garantía retenido temporalmente en la tarjeta del arrendatario. |
| **Referencias Cruzadas** | RF-126 |

### CU-17: Gestionar Expiraciones y Timeouts

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-17 |
| **Caso de Uso** | Gestionar Expiraciones y Timeouts |
| **Actor** | Sistema Core / Automático |
| **Descripción** | Proceso en segundo plano que cancela automáticamente reservas por falta de pago o solicitudes ignoradas por el arrendador. |
| **Pre-condiciones** | Existencia de reservas en estado pendiente con tiempo límite cumplido. |
| **Flujo Principal** | 1. El sistema ejecuta tareas programadas (CronJobs) para monitorear el tiempo transcurrido en las solicitudes.<br>2. Detecta reservas en estado "Pendiente de Pago" con más de 15 minutos de inactividad o solicitudes de reserva no respondidas por el host en 24 horas.<br>3. El sistema cancela de forma automática la solicitud y libera los bloqueos temporales correspondientes. |
| **Flujos Alternativos** | Ninguno a nivel de excepción del motor de tareas. |
| **Post-condiciones** | Liberación de fechas bloqueadas y cancelación de solicitudes expiradas. |
| **Referencias Cruzadas** | RF-127, RF-128, RF-137 |

### CU-18: Aprobar o Rechazar Solicitud

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-18 |
| **Caso de Uso** | Aprobar o Rechazar Solicitud |
| **Actor** | Arrendador |
| **Descripción** | Permite al propietario revisar una solicitud de reserva pagada y decidir si la aprueba o la rechaza. |
| **Pre-condiciones** | Solicitud con pago retenido en Escrow pendiente de revisión en el panel del host. |
| **Flujo Principal** | 1. El arrendador visualiza la solicitud entrante en su panel y selecciona "Aprobar" o "Rechazar".<br>2. Si aprueba, el sistema cambia el estado a "Aprobada_Host" y da inicio al proceso legal.<br>3. Si rechaza, el sistema exige ingresar un motivo predefinido y ejecuta automáticamente el reembolso total del dinero al arrendatario. |
| **Flujos Alternativos** | **A1. Falta de selección de motivo en rechazo (Paso 3):**<br>1. El sistema exige completar obligatoriamente la causa del rechazo antes de procesar el reembolso. |
| **Post-condiciones** | Reserva aprobada para contrato o rechazada con reembolso automatizado. |
| **Referencias Cruzadas** | RF-130 al RF-136 |

---

## Módulo: Marco Legal, Firma Notarial y Operativa

**Diagrama de Casos de Uso (Referencia)**
* **Actores:** Sistema Core, Arrendatario, Arrendador, Administrador, Sistema Externo (FirmaVirtual API)
* **Relaciones Principales:**
  * `CU-19: Generar y Enviar Contrato a Firma` $\rightarrow$ `<<include>> Consumir Servicio Externo de Firma` $\rightarrow$ `Consume (FirmaVirtual API)`

### CU-19: Generar y Enviar Contrato a Firma

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-19 |
| **Caso de Uso** | Generar y Enviar Contrato a Firma |
| **Actor** | Sistema Core |
| **Descripción** | Automatiza la creación del contrato PDF inyectando variables legales (Ley 21.461) y enviándolo al proveedor externo de Firma Electrónica Avanzada. |
| **Pre-condiciones** | Reserva aprobada por el arrendador. |
| **Flujo Principal** | 1. Tras la aprobación, el sistema recopila los datos legales del arrendador, arrendatario e inmueble.<br>2. Inyecta las variables en la plantilla HTML, compila el documento y exporta un archivo PDF inmutable almacenado en Cloud Storage.<br>3. El sistema envía el documento a la API de FirmaVirtual y distribuye los enlaces de firma únicos por correo a ambas partes.<br>4. Al recibir los webhooks de firma completada, descarga el PDF certificado y cambia el estado de la reserva a "Lista_Para_Checkin". |
| **Flujos Alternativos** | **A1. Falta de firma dentro del plazo (CronJob diario):**<br>1. Si llega la fecha de inicio y el contrato no está firmado, el sistema cancela automáticamente la reserva y ejecuta el reembolso al arrendatario. |
| **Post-condiciones** | Contrato firmado digitalmente con validez notarial resguardado en buckets cifrados. |
| **Referencias Cruzadas** | RF-142 al RF-158 |

### CU-20: Realizar Check-in con Evidencia

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-20 |
| **Caso de Uso** | Realizar Check-in con Evidencia |
| **Actor** | Arrendatario |
| **Descripción** | Permite al arrendatario documentar el estado de recepción del inmueble mediante fotografías con metadatos de tiempo y geolocalización. |
| **Pre-condiciones** | Contrato firmado y fecha actual coincidente con el inicio de la reserva. |
| **Flujo Principal** | 1. El arrendatario accede al panel de su reserva el día de inicio y presiona "Check-in".<br>2. Carga fotografías del espacio con resolución mínima requerida, adjuntando opcionalmente comentarios de texto.<br>3. El sistema registra de forma automática la marca de tiempo (timestamp) y la ubicación GPS del dispositivo.<br>4. El sistema valida las imágenes y cambia el estado de la reserva a "En_Curso". |
| **Flujos Alternativos** | **A1. Intento de check-in fuera de fecha (Paso 1):**<br>1. El sistema bloquea la habilitación del botón de check-in si no corresponde al día estipulado.<br><br>**A2. Imágenes corruptas o sin fotos (Paso 2):**<br>1. El sistema rechaza el envío si no se adjunta al menos una fotografía válida. |
| **Post-condiciones** | Evidencia de entrada registrada formalmente en el sistema. |
| **Referencias Cruzadas** | RF-159 al RF-167 |

### CU-21: Abrir Disputa por Daños

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-21 |
| **Caso de Uso** | Abrir Disputa por Daños |
| **Actor** | Arrendador |
| **Descripción** | Permite al propietario reportar daños detectados tras el check-out, congelando la devolución de la garantía. |
| **Pre-condiciones** | Reserva finalizada y ventana de tiempo posterior al check-out vigente (menor a 24 horas). |
| **Flujo Principal** | 1. El arrendador selecciona la reserva finalizada y accede al formulario de reclamo de daños.<br>2. Ingresa un texto descriptivo e incorpora fotografías de evidencia del perjuicio.<br>3. El sistema valida que el reporte esté dentro de las 24 horas de plazo, cambia el estado a "En_Disputa" y pausa el reembolso de la garantía y el payout. |
| **Flujos Alternativos** | **A1. Fuera de plazo (Paso 1):**<br>1. El sistema rechaza la apertura de disputa si han transcurrido más de 24 horas desde el fin de la estadía. |
| **Post-condiciones** | Garantía congelada y ticket de disputa generado para revisión administrativa. |
| **Referencias Cruzadas** | RF-168 al RF-173 |

### CU-22: Resolver Disputas en Backoffice

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-22 |
| **Caso de Uso** | Resolver Disputas en Backoffice |
| **Actor** | Administrador |
| **Descripción** | Permite al administrador evaluar las evidencias de ambas partes (contratos, fotos de check-in y reclamos) para emitir un fallo sobre la garantía. |
| **Pre-condiciones** | Existencia de un ticket de disputa en estado abierto. |
| **Flujo Principal** | 1. El administrador ingresa al panel de soporte y revisa la documentación comparativa de la reserva en disputa.<br>2. Emite un veredicto seleccionando un fallo a favor del arrendatario o del arrendador.<br>3. Si falla a favor del arrendador, ingresa el monto exacto a retener; si es a favor del arrendatario, libera el total de la garantía.<br>4. El sistema ejecuta la orden en la pasarela de pagos, cierra la reserva y notifica a las partes. |
| **Flujos Alternativos** | **A1. Falta de monto en fallo a favor del host (Paso 3):**<br>1. El sistema exige completar obligatoriamente la cifra monetaria a deducir antes de cerrar el caso. |
| **Post-condiciones** | Disputa resuelta y fondos de garantía distribuidos según veredicto. |
| **Referencias Cruzadas** | RF-174 al RF-182 |

### CU-23: Ejecutar Payouts y Liberación

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-23 |
| **Caso de Uso** | Ejecutar Payouts y Liberación |
| **Actor** | Sistema Core / Automático |
| **Descripción** | Transfiere de forma automática los fondos netos al arrendador y libera las garantías si finaliza el período post-servicio sin disputas. |
| **Pre-condiciones** | Check-out completado y transcurso del plazo de gracia de 24 horas sin reportes de daños. |
| **Flujo Principal** | 1. Un proceso automatizado (CronJob) detecta las reservas finalizadas que no registran apertura de disputas.<br>2. El sistema calcula el take rate (comisión de EspaciGo) sobre el monto total de la estadía.<br>3. Instruye a la pasarela de pagos transferir los fondos netos al arrendador y liberar el 100% del bloqueo de garantía al arrendatario.<br>4. El sistema genera la boleta electrónica de comisión, la envía por correo y cierra formalmente la reserva. |
| **Flujos Alternativos** | Ninguno a nivel de excepción del motor de liquidaciones automáticas. |
| **Post-condiciones** | Fondos liquidados al host, garantía liberada y ciclo de reserva cerrado con éxito. |
| **Referencias Cruzadas** | RF-183 al RF-192 |

---

## Módulo: Auditoría Inmutable y Analítica

**Diagrama de Casos de Uso (Referencia)**
* **Actores:** Sistema Core, Administrador, Sistema Externo (Google BigQuery)
* **Relaciones Principales:**
  * `CU-24: Transmitir Logs Transaccionales` $\rightarrow$ `<<include>> Registrar Evento Asíncrono` $\rightarrow$ `Stream Logs (Google BigQuery)`

### CU-24: Transmitir Logs Transaccionales

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-24 |
| **Caso de Uso** | Transmitir Logs Transaccionales |
| **Actor** | Sistema Core |
| **Descripción** | Captura y envía de manera asíncrona cada evento crítico de la plataforma hacia el Data Warehouse analítico para garantizar trazabilidad forense. |
| **Pre-condiciones** | Ocurrencia de una acción transaccional o sensible en el sistema (ej. login, pago, firma, eliminación). |
| **Flujo Principal** | 1. El microservicio de auditoría intercepta el evento crítico y lo empaqueta en una estructura estandarizada.<br>2. El sistema encola el registro y realiza un "Streaming Insert" asíncrono hacia Google BigQuery.<br>3. Los registros se almacenan en un repositorio de solo lectura, protegiéndolos contra modificaciones o borrados. |
| **Flujos Alternativos** | **A1. Falla de conectividad con el Data Warehouse (Paso 2):**<br>1. El sistema reencola el mensaje localmente mediante reintentos exponenciales para asegurar que ningún log crítico se pierda. |
| **Post-condiciones** | Registro de auditoría inmutable almacenado de forma segura en la capa OLAP. |
| **Referencias Cruzadas** | RF-193 al RF-196 |

### CU-25: Consultar Historial Inmutable

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-25 |
| **Caso de Uso** | Consultar Historial Inmutable |
| **Actor** | Administrador |
| **Descripción** | Permite al administrador auditar el comportamiento y las acciones históricas de un usuario filtrando por su RUT, cumpliendo con la normativa de privacidad. |
| **Pre-condiciones** | Sesión activa con rol de Administrador. |
| **Flujo Principal** | 1. El administrador accede al panel de auditoría e ingresa el RUT del usuario a consultar.<br>2. El sistema ejecuta consultas SQL analíticas sobre BigQuery cruzando los eventos inmutables.<br>3. El sistema despliega el historial detallado de acciones y permite exportar los resultados en un formato estructurado para reportes legales. |
| **Flujos Alternativos** | **A1. RUT sin registros asociados (Paso 2):**<br>1. El sistema retorna un conjunto de datos vacío notificando que no existen trazas de auditoría para el identificador ingresado. |
| **Post-condiciones** | Reporte de auditoría legal generado y consultado con éxito. |
| **Referencias Cruzadas** | RF-197 al RF-200 |