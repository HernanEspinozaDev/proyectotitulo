# ANEXO C: FICHAS TÉCNICAS DE CASOS DE USO

> **Versión sincronizada con `actores_y_modulos.md` (11 módulos) y con el catálogo vigente de 236 requerimientos funcionales (RQF-001 – RQF-236 = 185 base + 51 complementarios).**
> Los casos de uso se renumeraron de forma correlativa **CU-01 a CU-52**. Los casos complementarios (**CU-47 a CU-52**) se anexan al final del módulo correspondiente para no renumerar los casos existentes.

**Sistema:** espaciGo — Plataforma de publicación y arriendo flexible de espacios
**Notación:** UML 2.5 — diagramas de casos de uso
**Total de casos de uso:** 52 | **Total de módulos:** 11 | **Catálogo de referencia:** 236 RF | **RNF relacionados:** 43

---

## 1. Convenciones de modelado aplicadas

| Convención | Regla aplicada |
|---|---|
| **Actores** | Solo entidades externas: roles humanos y sistemas/servicios de terceros. No se representan componentes internos (frontend Next.js, API Go, contenedores, controladores, repositorios). |
| **Casos de uso** | Representan objetivos observables desde un actor. No se modelan detalles de implementación ni tablas/endpoints/clases. |
| **Límite del sistema** | Cada diagrama tiene un rectángulo con el nombre del sistema y, dentro, un paquete con el nombre del módulo. Los actores quedan fuera del límite. |
| **Asociaciones** | Se trazan solo entre actores y casos de uso en los que el actor participa directamente. Sin flechas ni direcciones inventadas. |
| **`<<include>>`** | Solo cuando el caso base **requiere obligatoriamente** el caso incluido. |
| **`<<extend>>`** | Solo cuando el caso de extensión agrega comportamiento **opcional, condicional o excepcional** al caso base. |
| **Generalización** | Solo con especialización real (ver justificaciones). |
| **Nomenclatura** | `RQF-###` (requerimiento funcional), `RNF-###` (no funcional), `CU-##` (caso de uso), `HU##` (historia de usuario). |
| **IDs** | Cada caso de uso tiene ID único y correlativo; el ID se usa igual en el informe, los anexos y las fichas. |

### Exclusiones justificadas (no se convierten en casos de uso)

| Elemento | Tipo real | Motivo |
|---|---|---|
| Cifrado/hash de contraseñas | `RNF-013` | Condición de calidad (confidencialidad), no funcionalidad observable. |
| Inmutabilidad de logs en el repositorio analítico | `RNF-017` | Condición de integridad de infraestructura. |
| Tokenización de tarjetas (PCI-DSS) | `RNF-025` | Restricción externa de cumplimiento. |
| Envío asíncrono de eventos a BigQuery | Detalle de implementación | No existe RF que lo observe un actor; se cubre con RNF-017. |
| Google BigQuery / Data Warehouse | Repositorio interno | No es actor: no hay interacción iniciada por él con un objetivo observable. |

---

## 2. Modelo de Actores

### 2.1 Actores primarios

| Actor | Nombre en UML | Descripción | Módulos |
|---|---|---|---|
| Visitante | `Visitante` | Usuario anónimo que explora el catálogo público. | M01, M05, M09 |
| Usuario Registrado | `UsuarioRegistrado` | Cuenta con correo verificado, sin validación de identidad. | M01, M02, M03 |
| Arrendador | `Arrendador` | Publica y administra los espacios de su titularidad y participa en el acuerdo y el cierre. | M04, M07, M08, M09, M10 |
| Arrendatario | `Arrendatario` | Busca y participa en la contratación. Verifica su identidad antes de la emisión y firma cuando elige esa modalidad. | M05, M06, M07, M08, M09, M10 |
| Administrador | `Administrador` | Operador interno: validaciones manuales, arbitraje, moderación, reportes y auditoría. | M03, M10, M11 |

### 2.2 Actores secundarios (sistemas y servicios externos)

| Actor | Tipo | Participa en |
|---|---|---|
| Proveedor de verificación habilitado | Integración sujeta a comprobación por entorno | CU-11, CU-12 |
| Mercado Pago | Servicio externo (pasarela de pagos) | CU-24, CU-41, CU-42 |
| SimpleFirma | Servicio externo (firma electrónica) | CU-29, CU-30 |

### 2.3 Generalización de actores

**Figura C.1**  
*Modelo de Generalización de Actores del Ecosistema*

![](assets/figuras/anexo_c/cu_actores.png)

*Nota.* Elaboración propia bajo estándar UML 2.5.

| Generalización | Justificación funcional |
|---|---|
| `UsuarioRegistrado --\|> Visitante` | Un usuario registrado puede ejecutar todo lo que ejecuta un visitante (buscar, filtrar, ver detalle, ver reseñas) y además autenticarse y operar con cuenta. |
| `Arrendador --\|> UsuarioRegistrado` | Además de las capacidades del usuario registrado, gestiona publicaciones, calendario, solicitudes de reserva y reclamos. |
| `Arrendatario --\|> UsuarioRegistrado` | Además de las capacidades del usuario registrado, reserva, paga, firma, hace check-in/out y reseña. |
| `Administrador` | Sin generalización: no es usuario del marketplace ni ejecuta los flujos comerciales de arrendador/arrendatario. |

---

## 3. Casos de Uso por Módulo

---

## Módulo M01 — Autenticación y Gestión de Cuenta

**RF cubiertos:** RQF-001 a RQF-023 + RQF-186 a RQF-188 + RQF-213 a RQF-218 (32 RF)
**Actores participantes:** Visitante, Usuario Registrado
**Casos de uso:** CU-01, CU-02, CU-03, CU-04, CU-05, CU-06, CU-50

### Diagrama de Casos de Uso

**Figura C.2**  
*Casos de Uso del Módulo M01: Autenticación y Gestión de Cuenta*

![](assets/figuras/anexo_c/cu_m01_autenticacion.png)

*Nota.* Elaboración propia bajo estándar UML 2.5.

**Justificación de las relaciones**

| Relación | Tipo | Justificación |
|---|---|---|
| CU-02 → CU-01 | `<<extend>>` | La verificación por correo es **condicional**: la cuenta ya queda creada en CU-01 y la extensión se ejecuta cuando el visitante consume el token (RQF-009). CU-01 puede completarse sin la extensión. |
| CU-04 → CU-03 | `<<extend>>` | El bloqueo solo ocurre si se alcanzan 5 intentos fallidos consecutivos (RQF-015): comportamiento excepcional que extiende el caso base "Iniciar Sesión", que puede finalizar exitosamente sin la extensión. |
| CU-05, CU-06, CU-50 | Sin relación | Son objetivos independientes del usuario; no agregan comportamiento a otro caso de uso ni son obligatorios para otro. La recuperación (CU-05) y el cambio con sesión iniciada (CU-50) comparten la política de contraseña, pero no existe obligatoriedad entre ellos. |

### CU-01: Registrar una cuenta

| Atributo | Detalle |
|---|---|
| **ID** | CU-01 |
| **Caso de Uso** | Registrar una cuenta |
| **Actor** | Visitante |
| **Descripción** | El visitante crea una cuenta con correo, contraseña y aceptación de términos. |
| **Precondiciones** | Formulario y términos vigentes disponibles |
| **Flujo Principal** | Ingresar correo y contraseña y aceptar los términos aplicables. La plataforma valida y registra la cuenta. |
| **Flujos Alternativos** | Informar entradas inválidas o el estado del envío. |
| **Postcondiciones** | Cuenta pendiente de verificación. El registro prescinde de una preferencia inicial. |
| **Referencias Cruzadas** | RQF-001 a RQF-009 · RQF-186, RQF-187 y RQF-213 · HU01 |

### CU-02: Verificar Cuenta por Correo Electrónico

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-02 |
| **Caso de Uso** | Verificar Cuenta por Correo Electrónico |
| **Actor** | Visitante |
| **Descripción** | Extensión de CU-01 que envía el token de verificación, confirma la cuenta y restringe el acceso mientras no esté verificada. |
| **Precondiciones** | Haber completado el registro de la cuenta (CU-01). |
| **Flujo Principal** | 1. El sistema envía al correo electrónico un token de verificación.<br>2. El visitante abre el enlace y consume el token.<br>3. El sistema cambia el estado de la cuenta a "Verificado".<br>4. El sistema informa la verificación exitosa y habilita el inicio de sesión. |
| **Flujos Alternativos** | **A1. Token inválido o expirado:**<br>1. El sistema rechaza la verificación.<br>2. El sistema permite reenviar el correo de verificación, generando un nuevo token.<br><br>**A2. Intento de inicio de sesión sin verificar (RQF-010):**<br>1. El sistema bloquea el inicio de sesión de cuentas en estado "No Verificado".<br>2. El sistema indica que debe confirmar su correo electrónico. |
| **Postcondiciones** | Cuenta habilitada para autenticarse en el sistema. |
| **Referencias Cruzadas** | RQF-008 al RQF-010 · RQF-188 · extiende CU-01 · HU01 |

### CU-03: Iniciar Sesión

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-03 |
| **Caso de Uso** | Iniciar Sesión |
| **Actor** | Usuario Registrado |
| **Descripción** | El usuario autentica su identidad con correo y contraseña y obtiene una sesión temporal. |
| **Precondiciones** | Poseer una cuenta registrada y verificada por correo electrónico. |
| **Flujo Principal** | 1. El usuario ingresa correo y contraseña en la interfaz de acceso.<br>2. El sistema valida que las credenciales correspondan a una cuenta registrada.<br>3. El sistema genera una sesión temporal.<br>4. El sistema redirige al usuario a su panel según su rol. |
| **Flujos Alternativos** | **A1. Credenciales incorrectas (Paso 2):**<br>1. El sistema rechaza el acceso y despliega un mensaje genérico de seguridad.<br>2. El sistema incrementa el contador de intentos fallidos (deriva en CU-04 al llegar a 5).<br><br>**A2. Cuenta no verificada:**<br>1. El sistema bloquea el acceso y deriva a CU-02. |
| **Postcondiciones** | Sesión temporal activa en el sistema. |
| **Referencias Cruzadas** | RQF-011 al RQF-013 · RQF-018 · CU-04 (extensión) · HU02 |

### CU-04: Bloquear Cuenta por Intentos Fallidos

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-04 |
| **Caso de Uso** | Bloquear Cuenta por Intentos Fallidos |
| **Actor** | Usuario Registrado (caso automático desencadenado por el sistema) |
| **Descripción** | Extensión de CU-03 que bloquea temporalmente la cuenta tras 5 intentos fallidos consecutivos, alerta al usuario y libera el acceso automáticamente. |
| **Precondiciones** | Haber alcanzado 5 intentos fallidos consecutivos (punto de extensión de CU-03). |
| **Flujo Principal** | 1. El sistema detecta el 5.º intento fallido consecutivo.<br>2. El sistema bloquea la cuenta de usuario.<br>3. El sistema envía un correo de alerta de seguridad.<br>4. El sistema mantiene el bloqueo durante 30 minutos.<br>5. El sistema libera automáticamente la cuenta al cumplirse el plazo. |
| **Flujos Alternativos** | **A1. Intento de acceso durante el bloqueo:**<br>1. El sistema rechaza el inicio de sesión e informa el tiempo restante de bloqueo. |
| **Postcondiciones** | Cuenta liberada automáticamente y contador de intentos reiniciado. |
| **Referencias Cruzadas** | RQF-014 al RQF-017 · extiende CU-03 · HU02 |

### CU-05: Recuperar Contraseña

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-05 |
| **Caso de Uso** | Recuperar Contraseña |
| **Actor** | Usuario Registrado |
| **Descripción** | Permite restablecer la contraseña mediante un enlace temporal de un solo uso enviado al correo electrónico. |
| **Precondiciones** | Poseer una cuenta registrada. |
| **Flujo Principal** | 1. El usuario solicita la recuperación de contraseña.<br>2. El sistema envía un enlace único al correo electrónico.<br>3. El usuario abre el enlace dentro del plazo de vigencia de 15 minutos.<br>4. El usuario define la nueva contraseña y el sistema la actualiza. |
| **Flujos Alternativos** | **A1. Enlace expirado (Paso 3):**<br>1. El sistema rechaza el cambio al superar los 15 minutos y solicita generar un nuevo enlace.<br><br>**A2. Correo no registrado (Paso 2):**<br>1. El sistema informa que no es posible continuar con el correo ingresado. |
| **Postcondiciones** | Credencial de acceso actualizada. |
| **Referencias Cruzadas** | RQF-019 al RQF-022 · HU03 |

### CU-06: Cerrar Sesión

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-06 |
| **Caso de Uso** | Cerrar Sesión |
| **Actor** | Usuario Registrado |
| **Descripción** | El usuario finaliza su sesión activa e invalida la credencial temporal. |
| **Precondiciones** | Sesión activa en el sistema. |
| **Flujo Principal** | 1. El usuario selecciona la opción de cerrar sesión.<br>2. El sistema invalida la sesión temporal activa.<br>3. El sistema redirige al usuario al catálogo público. |
| **Flujos Alternativos** | **A1. Sesión ya expirada:**<br>1. El sistema detecta que la sesión no es válida y redirige al catálogo público sin error. |
| **Postcondiciones** | Sesión finalizada y token invalidado. |
| **Referencias Cruzadas** | RQF-023 |

> **Caso de uso complementario (2.ª revisión, derivada de las Historias de Usuario):** CU-50 se incorpora al módulo M01 sin alterar la numeración de los casos existentes.

### CU-50: Cambiar Contraseña

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-50 |
| **Caso de Uso** | Cambiar Contraseña |
| **Actor** | Usuario Registrado |
| **Descripción** | El usuario autenticado cambia su contraseña indicando la contraseña actual y una nueva que cumpla la política de seguridad y las restricciones de reutilización. |
| **Precondiciones** | Sesión activa en el sistema. |
| **Flujo Principal** | 1. El usuario accede a la configuración de seguridad de su cuenta.<br>2. Ingresa la contraseña actual, la contraseña nueva y la repetición de la nueva.<br>3. El sistema valida que la contraseña actual coincida con la registrada.<br>4. El sistema valida que la contraseña nueva cumpla la política de seguridad (mínimo 8 caracteres, una mayúscula, un número y un carácter especial).<br>5. El sistema verifica que la contraseña nueva no coincida con la actual ni con una utilizada en los últimos 3 meses.<br>6. El sistema actualiza la contraseña y notifica el cambio al usuario por correo electrónico. |
| **Flujos Alternativos** | **A1. Contraseña actual incorrecta (Paso 3):**<br>1. El sistema rechaza la operación y muestra "La contraseña actual no es correcta".<br><br>**A2. Contraseña nueva inválida (Pasos 4 y 5):**<br>1. El sistema rechaza el cambio e indica el requisito incumplido (política de seguridad, igualdad con la contraseña actual o reutilización dentro de los 3 meses).<br><br>**A3. Repetición no coincidente (Paso 2):**<br>1. El sistema solicita volver a ingresar la contraseña nueva y su repetición. |
| **Postcondiciones** | Credencial de acceso actualizada y usuario notificado del cambio. |
| **Referencias Cruzadas** | RQF-214 al RQF-218 · CU-05 (recuperación de contraseña) · HU03 |

---

## Módulo M02 — Perfil y Privacidad del Usuario

**RF cubiertos:** RQF-024 a RQF-037 + RQF-189 a RQF-191 (17 RF)
**Actores participantes:** Usuario Registrado (Arrendador y Arrendatario heredan estas capacidades por generalización)
**Casos de uso:** CU-07, CU-08, CU-09

### Diagrama de Casos de Uso

**Figura C.3**  
*Casos de Uso del Módulo M02: Perfil y Privacidad del Usuario*

![](assets/figuras/anexo_c/cu_m02_perfil.png)

*Nota.* Elaboración propia bajo estándar UML 2.5.

**Justificación de las relaciones**

| Relación | Tipo | Justificación |
|---|---|---|
| CU-07, CU-08, CU-09 | Sin relaciones | No existe comportamiento obligatorio compartido ni extensión condicional entre ellos: son objetivos independientes respaldados por RF distintos. Los bloqueos de CU-09 (RQF-035 a RQF-037) son validaciones de su propio flujo, no un caso de uso aparte. |

### CU-07: Gestionar Perfil de Usuario

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-07 |
| **Caso de Uso** | Gestionar Perfil de Usuario |
| **Actor** | Usuario Registrado |
| **Descripción** | El usuario consulta y actualiza sus datos de perfil: nombre, teléfono y fotografía. |
| **Precondiciones** | Sesión activa en el sistema. |
| **Flujo Principal** | 1. El usuario accede a la configuración de su perfil.<br>2. El sistema muestra los datos actuales del perfil.<br>3. El usuario modifica su nombre, y el sistema valida que contenga únicamente caracteres alfabéticos y espacios.<br>4. El usuario modifica su teléfono, y el sistema valida que contenga exactamente 9 dígitos.<br>5. El usuario carga una fotografía de perfil, y el sistema valida que no supere los 2MB.<br>6. El sistema guarda los cambios y confirma la actualización. |
| **Flujos Alternativos** | **A1. Datos con formato inválido (Pasos 3 y 4):**<br>1. El sistema rechaza el valor ingresado y solicita corregirlo.<br><br>**A2. Fotografía superior al límite (Paso 5):**<br>1. El sistema rechaza la carga por superar los 2MB.<br><br>**A3. Eliminación de fotografía:**<br>1. El usuario solicita eliminar su fotografía y el sistema la elimina del perfil. |
| **Postcondiciones** | Datos de perfil actualizados en la plataforma. |
| **Referencias Cruzadas** | RQF-024 al RQF-031 · HU31 |

### CU-08: Gestionar Cuenta Bancaria

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-08 |
| **Caso de Uso** | Gestionar Cuenta Bancaria |
| **Actor** | Usuario Registrado |
| **Descripción** | El usuario mantiene la cuenta bancaria en la que recibirá los pagos de los arriendos: la registra, consulta, modifica o elimina. |
| **Precondiciones** | Sesión activa y RUT validado en el perfil. |
| **Flujo Principal** | 1. El usuario accede a los datos de cobro de su perfil.<br>2. El sistema despliega la cuenta bancaria registrada, si existe.<br>3. El usuario registra una nueva cuenta bancaria o modifica la vigente.<br>4. El sistema valida que el RUT de la cuenta coincida con el RUT del usuario.<br>5. El sistema asocia la cuenta bancaria al perfil y confirma la operación.<br>6. El usuario puede eliminar la cuenta bancaria registrada. |
| **Flujos Alternativos** | **A1. RUT no coincidente (Paso 4):**<br>1. El sistema rechaza la operación e indica que el titular debe coincidir con el usuario verificado.<br><br>**A2. Eliminación con liquidaciones en proceso (Paso 6):**<br>1. El sistema advierte que existen pagos en proceso y mantiene la cuenta hasta completar su liquidación. |
| **Postcondiciones** | Cuenta bancaria registrada, actualizada o eliminada según la operación ejecutada. |
| **Referencias Cruzadas** | RQF-032, RQF-033 · RQF-189 al RQF-191 · CU-42 (uso de la cuenta en la liquidación) · HU31 |

### CU-09: Solicitar Eliminación de Cuenta

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-09 |
| **Caso de Uso** | Solicitar Eliminación de Cuenta |
| **Actor** | Usuario Registrado |
| **Descripción** | El usuario solicita la eliminación de su cuenta y de sus datos personales, conforme al derecho de supresión de datos. |
| **Precondiciones** | Sesión activa en el sistema. |
| **Flujo Principal** | 1. El usuario solicita la eliminación de su cuenta desde la configuración.<br>2. El sistema verifica que no existan reservas activas.<br>3. El sistema verifica que no existan pagos pendientes.<br>4. El sistema verifica que no existan disputas abiertas.<br>5. El sistema ejecuta la eliminación de la cuenta y la anonimización de la información transaccional histórica.<br>6. El sistema cierra la sesión activa. |
| **Flujos Alternativos** | **A1. Procesos activos (Pasos 2 a 4):**<br>1. El sistema detecta reservas, pagos o disputas vigentes.<br>2. El sistema rechaza la eliminación e informa el motivo y las condiciones para reintentar. |
| **Postcondiciones** | Datos personales eliminados y data transaccional anonimizada (plazo administrativo conforme a RNF-026). |
| **Referencias Cruzadas** | RQF-034 al RQF-037 · RNF-018, RNF-026, RNF-029 · HU32 |

---

## Módulo M03 — Verificación de Identidad (KYC / KYB)

**RF cubiertos:** RQF-038 a RQF-059 + RQF-192 a RQF-194 + RQF-219, RQF-220 (27 RF)
**Actores participantes:** Usuario registrado, operador autorizado y proveedor habilitado cuando corresponde
**Casos de uso:** CU-10 (abstracto), CU-11, CU-12, CU-13, CU-14

### Diagrama de Casos de Uso

**Figura C.4**  
*Casos de Uso del Módulo M03: Verificación de Identidad (KYC / KYB)*

![](assets/figuras/anexo_c/cu_m03_identidad.png)

*Nota.* Elaboración propia bajo estándar UML 2.5.

**Justificación de las relaciones**

| Relación | Tipo | Justificación |
|---|---|---|
| CU-11 → CU-10 | Generalización | Especialización real: mismo objetivo (acreditar identidad) y misma post-condición (perfil verificado), con reglas, artefactos y organismo validador distintos (Registro Civil vs SII). CU-10 es abstracto y no se ejecuta por sí solo. |
| CU-12 → CU-10 | Generalización | Ídem anterior para personas jurídicas. |
| CU-13 | Sin relación | El arbitraje manual es un objetivo propio del Administrador (RQF-054 a RQF-057); no es comportamiento obligatorio ni opcional de CU-11/CU-12, sino el tratamiento de sus resultados fallidos (se documenta como flujo alternativo derivado). |
| CU-14 | Sin relación | Reintentar la validación es una acción autónoma del usuario (RQF-058, RQF-059) iniciada desde su perfil, no una extensión de la validación en curso. |

### CU-10: Validar Identidad (caso de uso abstracto)

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-10 |
| **Caso de Uso** | Validar Identidad (abstracto) |
| **Actor** | Usuario Registrado (actor general) |
| **Descripción** | Caso de uso abstracto que representa el objetivo común de acreditar la identidad del usuario ante un organismo externo, habilitándolo para operar en el marketplace. |
| **Precondiciones** | Sesión activa y datos básicos del perfil completos. |
| **Flujo Principal** | 1. El caso de uso no se instancia directamente.<br>2. Se ejecuta a través de sus especializaciones CU-11 (persona natural) y CU-12 (empresa). |
| **Flujos Alternativos** | No aplica (caso de uso abstracto). |
| **Postcondiciones** | Perfil del usuario en estado verificado y habilitado para transaccionar. |
| **Referencias Cruzadas** | RQF-038 al RQF-053 (a través de CU-11 y CU-12) |

### CU-11: Verificar identidad de persona natural

| Atributo | Detalle |
|---|---|
| **ID** | CU-11 |
| **Caso de Uso** | Verificar identidad de persona natural |
| **Actor** | Parte solicitante y operador autorizado |
| **Descripción** | La persona acredita su identidad mediante los datos y evidencias requeridos. |
| **Precondiciones** | Cuenta autenticada y expediente disponible |
| **Flujo Principal** | Evaluar RUT y nombre completo según el documento y el mecanismo habilitado. |
| **Flujos Alternativos** | Registrar antecedentes insuficientes y permitir reintentar mediante CU-14. |
| **Postcondiciones** | Resultado de verificación disponible para la emisión. |
| **Referencias Cruzadas** | RQF-038 a RQF-047 · HU04 |

### CU-12: Verificar representación empresarial

| Atributo | Detalle |
|---|---|
| **ID** | CU-12 |
| **Caso de Uso** | Verificar representación empresarial |
| **Actor** | Representante y operador autorizado |
| **Descripción** | La persona acredita la representación de una empresa mediante un expediente separado. |
| **Precondiciones** | Cuenta autenticada y representación aplicable |
| **Flujo Principal** | Registrar por separado la empresa y la acreditación de su representante. Evaluar ambos antecedentes. |
| **Flujos Alternativos** | Registrar la falta de antecedentes y solicitar subsanación. |
| **Postcondiciones** | Facultades evaluadas disponibles para la emisión. |
| **Referencias Cruzadas** | RQF-048 a RQF-053 · HU04 |

### CU-13: Revisar Validación Manual

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-13 |
| **Caso de Uso** | Revisar Validación Manual |
| **Actor** | Administrador |
| **Descripción** | El administrador revisa las validaciones de identidad que fallaron automáticamente y resuelve aprobando o rechazando con motivo obligatorio. |
| **Precondiciones** | Sesión activa con rol de Administrador y existencia de validaciones fallidas. |
| **Flujo Principal** | 1. El administrador consulta el listado de validaciones fallidas.<br>2. El sistema despliega los antecedentes aportados por el usuario.<br>3. El administrador selecciona aprobar o rechazar la validación.<br>4. Al rechazar, el administrador ingresa el motivo obligatorio.<br>5. El sistema actualiza el estado del perfil y notifica al usuario. |
| **Flujos Alternativos** | **A1. Rechazo sin motivo (Paso 4):**<br>1. El sistema exige completar el motivo antes de procesar el rechazo. |
| **Postcondiciones** | Validación de identidad resuelta manualmente. |
| **Referencias Cruzadas** | RQF-054 al RQF-057 · CU-11/CU-12 (origen del caso) · CU-14 (reintento) |

### CU-14: Reintentar Validación Rechazada

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-14 |
| **Caso de Uso** | Reintentar Validación Rechazada |
| **Actor** | Usuario Registrado |
| **Descripción** | El usuario corrige los antecedentes rechazados y solicita un nuevo intento de validación de identidad. |
| **Precondiciones** | Contar con una validación de identidad previamente rechazada. |
| **Flujo Principal** | 1. El usuario consulta el estado de su validación de identidad.<br>2. El sistema despliega el estado de la validación y, si corresponde, el motivo del rechazo.<br>3. El usuario modifica los antecedentes rechazados.<br>4. El usuario solicita un nuevo intento de validación.<br>5. El sistema reingresa la solicitud al flujo de validación (CU-11 o CU-12). |
| **Flujos Alternativos** | **A1. Antecedentes sin modificar:**<br>1. El sistema no habilita el nuevo intento y solicita corregir los datos observados. |
| **Postcondiciones** | Solicitud de validación reingresada para evaluación. |
| **Referencias Cruzadas** | RQF-058, RQF-059 · RQF-193 · CU-13 (origen del rechazo) |

---

## Módulo M04 — Gestión de Publicaciones

**RF cubiertos:** RQF-060 a RQF-093 + RQF-195 a RQF-198 + RQF-221 a RQF-226 (44 RF)
**Actores participantes:** Arrendador
**Casos de uso:** CU-15, CU-16, CU-17, CU-18

### Diagrama de Casos de Uso

**Figura C.5**  
*Casos de Uso del Módulo M04: Gestión de Publicaciones*

![](assets/figuras/anexo_c/cu_m04_publicaciones.png)

*Nota.* Elaboración propia bajo estándar UML 2.5.

**Justificación de las relaciones**

| Relación | Tipo | Justificación |
|---|---|---|
| CU-15 ↔ CU-16 | Sin relación | Se evaluó un `<<include>>`, pero la galería **no es obligatoria** para registrar la publicación (la publicación existe en estado "Borrador" sin fotografías, RQF-081). Al no existir obligatoriedad, no corresponde `<<include>>`. |
| CU-17, CU-18 | Sin relación | Objetivos independientes: calendarizar (RQF-083 a RQF-085) y mantener vigente la publicación (RQF-086 a RQF-093) no son obligatorios ni condicionales entre sí. |

### CU-15: Publicar un espacio

| Atributo | Detalle |
|---|---|
| **ID** | CU-15 |
| **Caso de Uso** | Publicar un espacio |
| **Actor** | Titular vigente |
| **Descripción** | El titular prepara y publica una unidad reservable según las reglas de la oferta. |
| **Precondiciones** | Sesión activa y borrador disponible |
| **Flujo Principal** | Preparar el borrador y solicitar publicación. La plataforma comprueba titularidad y reglas del anuncio. |
| **Flujos Alternativos** | Denegar por falta de titularidad o conservar borrador con observaciones. |
| **Postcondiciones** | La publicación válida se vuelve visible. |
| **Referencias Cruzadas** | RQF-081 y RQF-082 · HU05 · Figura 7 |

### CU-16: Administrar la galería

| Atributo | Detalle |
|---|---|
| **ID** | CU-16 |
| **Caso de Uso** | Administrar la galería |
| **Actor** | Titular vigente |
| **Descripción** | El titular administra las imágenes, su orden y la portada del espacio. |
| **Precondiciones** | Espacio propio y sesión activa |
| **Flujo Principal** | Reservar posición, incorporar imagen válida, ordenar y definir portada. |
| **Flujos Alternativos** | Rechazar al ocupar 30 posiciones, incluidas las reservadas. Resolver revisiones concurrentes. |
| **Postcondiciones** | Galería asociada al espacio y orden conservado. |
| **Referencias Cruzadas** | RQF-074 a RQF-078 · HU05 |

### CU-17: Configurar Calendario de Disponibilidad

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-17 |
| **Caso de Uso** | Configurar Calendario de Disponibilidad |
| **Actor** | Arrendador |
| **Descripción** | El arrendador administra la disponibilidad de su espacio bloqueando y desbloqueando fechas en el calendario de la publicación. |
| **Precondiciones** | Publicación de espacio existente. |
| **Flujo Principal** | 1. El arrendador accede al calendario de disponibilidad generado para su publicación.<br>2. Selecciona un rango de fechas u horas para bloquear e ingresa el motivo del bloqueo.<br>3. El sistema valida que la fecha de término sea posterior a la de inicio y que el motivo esté ingresado.<br>4. El sistema verifica que el rango no se superponga con reservas existentes y aplica el bloqueo.<br>5. El sistema actualiza la disponibilidad consultada por el motor de búsqueda.<br>6. El arrendador desbloquea fechas previamente bloqueadas cuando corresponde. |
| **Flujos Alternativos** | **A1. Superposición con reservas existentes (Paso 4):**<br>1. El sistema impide el bloqueo para no interferir con una reserva vigente (deriva de RQF-112).<br><br>**A2. Motivo no ingresado (Paso 3):**<br>1. El sistema exige el motivo del bloqueo antes de aplicarlo.<br><br>**A3. Fecha de término inválida (Paso 3):**<br>1. El sistema rechaza el bloqueo e indica que la fecha de término debe ser posterior a la de inicio. |
| **Postcondiciones** | Calendario de la publicación actualizado y consistente con las reservas vigentes. |
| **Referencias Cruzadas** | RQF-083 al RQF-085 · RQF-225, RQF-226 · CU-19 (consumo de la disponibilidad) · CU-23 (validación de disponibilidad) · HU20, HU21 |

### CU-18: Modificar o Dar de Baja Publicación

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-18 |
| **Caso de Uso** | Modificar o Dar de Baja Publicación |
| **Actor** | Arrendador |
| **Descripción** | El arrendador consulta su listado de publicaciones y modifica, oculta, reactiva o elimina una publicación. |
| **Precondiciones** | Ser propietario de la publicación y tener sesión activa. |
| **Flujo Principal** | 1. El arrendador consulta su listado de publicaciones.<br>2. Selecciona la publicación que desea gestionar.<br>3. Modifica el título, la descripción, el precio base, las reglas de uso, la capacidad máxima, la modalidad tarifaria o la política de cancelación de la publicación.<br>4. El sistema valida el precio base modificado (mayor a \$5.000 CLP) y las reglas personalizadas (máximo 250 caracteres).<br>5. El sistema publica las reglas de uso y la política de cancelación en el detalle de la publicación.<br>6. Cambia el estado a "Oculta", quedando excluida de los resultados públicos.<br>7. Cambia el estado de "Oculta" a "Activa" cuando corresponde.<br>8. Solicita la eliminación permanente de la publicación. |
| **Flujos Alternativos** | **A1. Eliminación con reservas futuras (Paso 8):**<br>1. El sistema detecta reservas futuras pendientes asociadas a la publicación.<br>2. El sistema rechaza la eliminación permanente y emite una advertencia.<br><br>**A2. Datos modificados fuera de rango (Paso 4):**<br>1. El sistema rechaza el valor ingresado y detalla las validaciones incumplidas (precio base o largo de la regla personalizada). |
| **Postcondiciones** | Publicación modificada, con reglas y política de cancelación publicadas, o bien oculta, reactivada o eliminada según la acción ejecutada. |
| **Referencias Cruzadas** | RQF-086 al RQF-093 · RQF-195 al RQF-198 · RQF-221 al RQF-224 · HU06, HU07, HU08 |

---

## Módulo M05 — Búsqueda y Cotización de Espacios

**RF cubiertos:** RQF-094 a RQF-107 (14 RF)
**Actores participantes:** Visitante, Arrendatario (Usuario Registrado hereda la capacidad de búsqueda)
**Casos de uso:** CU-19, CU-20, CU-21

### Diagrama de Casos de Uso

**Figura C.6**  
*Casos de Uso del Módulo M05: Búsqueda y Cotización de Espacios*

![](assets/figuras/anexo_c/cu_m05_busqueda.png)

*Nota.* Elaboración propia bajo estándar UML 2.5.

**Justificación de las relaciones**

| Relación | Tipo | Justificación |
|---|---|---|
| `VIS <\|-- USR <\|-- ARREN` | Generalización de actores | El usuario registrado y el arrendatario heredan la capacidad de buscar y consultar el catálogo; el arrendatario agrega la cotización como paso previo a la reserva. |
| CU-19, CU-20, CU-21 | Sin relaciones entre CU | La cotización no es un `<<include>>` de la búsqueda (el usuario puede cotizar sin buscar, accediendo al detalle directo) y el detalle no es obligatorio para buscar. Al no existir obligatoriedad, se mantienen independientes. |

### CU-19: Buscar Espacios

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-19 |
| **Caso de Uso** | Buscar Espacios |
| **Actor** | Visitante (el Usuario Registrado y el Arrendatario heredan esta capacidad) |
| **Descripción** | El visitante busca espacios combinando texto libre, mapa interactivo y filtros, y el sistema excluye las publicaciones sin disponibilidad en el rango consultado. |
| **Precondiciones** | Existencia de publicaciones en estado "Activa". |
| **Flujo Principal** | 1. El visitante ingresa términos de búsqueda en la barra de texto.<br>2. El sistema renderiza el mapa interactivo con las ubicaciones de los espacios.<br>3. El sistema despliega la cuadrícula de tarjetas con el resumen de las publicaciones.<br>4. El visitante aplica filtros de precio mínimo y máximo, tipo de inmueble, metros cuadrados mínimos y rango de fechas.<br>5. El sistema excluye las publicaciones sin disponibilidad en las fechas consultadas.<br>6. El visitante limpia todos los filtros aplicados para reiniciar la búsqueda. |
| **Flujos Alternativos** | **A1. Sin resultados coincidentes (Paso 5):**<br>1. El sistema informa que no se encontraron espacios disponibles.<br>2. El sistema sugiere ampliar o relajar los criterios de búsqueda. |
| **Postcondiciones** | Listado geolocalizado de espacios disponibles según los criterios aplicados. |
| **Referencias Cruzadas** | RQF-094 al RQF-102 · CU-20 (siguiente paso) · HU10 |

### CU-20: Consultar Detalle de Publicación

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-20 |
| **Caso de Uso** | Consultar Detalle de Publicación |
| **Actor** | Visitante |
| **Descripción** | El visitante consulta la información completa de un espacio publicado, incluyendo sus fotografías, reglas y reseñas. |
| **Precondiciones** | Publicación en estado "Activa". |
| **Flujo Principal** | 1. El visitante selecciona una tarjeta de resultado.<br>2. El sistema despliega los detalles completos de la publicación.<br>3. El sistema muestra las reseñas y calificaciones del espacio (ver CU-36). |
| **Flujos Alternativos** | **A1. Publicación no disponible (Paso 1):**<br>1. El sistema informa que la publicación ya no está disponible y vuelve a los resultados (deriva de RQF-089). |
| **Postcondiciones** | Información completa del espacio desplegada para el visitante. |
| **Referencias Cruzadas** | RQF-103 · CU-36 (reseñas) · CU-21 (cotización) |

### CU-21: Cotizar Estadía

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-21 |
| **Caso de Uso** | Cotizar Estadía |
| **Actor** | Arrendatario |
| **Descripción** | Calcula y muestra el desglose económico del uso del espacio considerando precio base, comisión de servicio y garantía cuando corresponde y está habilitada. |
| **Precondiciones** | Publicación activa y rango de tiempo de uso seleccionado. |
| **Flujo Principal** | 1. El arrendatario selecciona el tiempo de uso del espacio.<br>2. El sistema calcula el costo total multiplicando el precio base por el tiempo seleccionado.<br>3. El sistema calcula el monto de la comisión de servicio.<br>4. El sistema calcula el monto de la garantía si corresponde y está habilitada.<br>5. El sistema muestra el desglose de cobro (Estadía + Comisión + Garantía). |
| **Flujos Alternativos** | **A1. Cambio del rango de tiempo (Paso 2):**<br>1. El arrendatario modifica el rango y el sistema recalcula el desglose antes de continuar. |
| **Postcondiciones** | Desglose de cobro disponible para iniciar el proceso de reserva. |
| **Referencias Cruzadas** | RQF-104 al RQF-107 · CU-22 (reserva) · HU15 |

---

## Módulo M06 — Reservas y cobros

**RF cubiertos:** RQF-108 a RQF-129 + RQF-199 a RQF-201 + RQF-227 a RQF-231 (30 RF)
**Actores participantes:** Arrendatario, Arrendador; Mercado Pago (pasarela externa)
**Casos de uso:** CU-22, CU-23, CU-24, CU-25, CU-26, CU-27, CU-28, CU-47, CU-51

**Figura C.7**\
*Casos de uso de reservas y cobros*

![](assets/figuras/anexo_c/cu_m06_reservas_escrow.png)

*Nota.* Elaboración propia. La figura representa los casos de uso del alcance objetivo según el ADR.

El flujo de actividad de la Figura 8 del Capítulo IX documenta las ramas de cobro y vencimiento. CU-23 verifica disponibilidad durante CU-22. CU-26 registra el acuerdo bilateral requerido antes de activar el bloqueo. CU-25 se ejecuta cuando la garantía corresponde y está habilitada. CU-27 y CU-28 describen expiración y conciliación.

### CU-22: Solicitar un intervalo de reserva

| Atributo | Detalle |
|---|---|
| **ID** | CU-22 |
| **Caso de Uso** | Solicitar un intervalo de reserva |
| **Actor** | Arrendatario y titular |
| **Descripción** | Las partes acuerdan un intervalo y un precio antes de bloquear la disponibilidad. |
| **Precondiciones** | Espacio y solicitud de intervalo identificados |
| **Flujo Principal** | Validar el intervalo y notificar al titular de la solicitud. Registrar el acuerdo de horario y precio, verificar ambas identidades y activar un bloqueo único. |
| **Flujos Alternativos** | Rechazar intervalos inválidos o solapados y conservar la ocupación previa. |
| **Postcondiciones** | Un bloqueo activo para la reserva cuando se cumplen las condiciones. |
| **Referencias Cruzadas** | RQF-110 a RQF-113 y RQF-122 · HU15, HU18 y HU30 · CU-23 · PT-01 y PT-02 |

### CU-23: Validar Disponibilidad en Tiempo Real

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-23 |
| **Caso de Uso** | Validar Disponibilidad en Tiempo Real |
| **Actor** | Sin actor propio: caso de uso incluido obligatoriamente por CU-22 |
| **Descripción** | Verifica contra la base de datos operativa que el intervalo solicitado no se superponga con reservas confirmadas ni con bloqueos de calendario, evitando la doble reserva. |
| **Precondiciones** | Intervalo de fechas u horas definido por el arrendatario (CU-22, paso 1). |
| **Flujo Principal** | 1. El sistema consulta la disponibilidad del intervalo solicitado.<br>2. El sistema confirma que no existen superposiciones y retorna el resultado a CU-22. |
| **Flujos Alternativos** | **A1. Superposición detectada (Paso 1):**<br>1. El sistema rechaza la reserva cuando existe superposición temporal con otra reserva o bloqueo.<br>2. El sistema retorna el rechazo a CU-22. |
| **Postcondiciones** | Disponibilidad del intervalo confirmada o rechazada. |
| **Referencias Cruzadas** | RQF-111, RQF-112 · incluido por CU-22 · HU15 |

### CU-24: Acreditar la renta

| Atributo | Detalle |
|---|---|
| **ID** | CU-24 |
| **Caso de Uso** | Acreditar la renta |
| **Actor** | Arrendatario y pasarela |
| **Descripción** | El arrendatario paga la renta al cumplir las condiciones de su emisión. |
| **Precondiciones** | Bloqueo vigente y modalidad contractual cumplida |
| **Flujo Principal** | Informar vencimiento, habilitar renta y acreditar el evento conciliado. |
| **Flujos Alternativos** | Procesar duplicado sin cambiar estado. Derivar evento tardío a conciliación. |
| **Postcondiciones** | Renta acreditada y, si corresponde, etapa de garantía disponible. |
| **Referencias Cruzadas** | RQF-116 a RQF-120 · HU17 |

### CU-25: Acreditar garantía cuando corresponde

| Atributo | Detalle |
|---|---|
| **ID** | CU-25 |
| **Caso de Uso** | Acreditar garantía cuando corresponde |
| **Actor** | Arrendatario |
| **Descripción** | El arrendatario paga por separado la garantía habilitada y exigible. |
| **Precondiciones** | Renta acreditada y garantía aplicable y habilitada |
| **Flujo Principal** | Registrar y acreditar la garantía como cobro separado. |
| **Flujos Alternativos** | Omitir la etapa sin garantía. Si vence, liberar el bloqueo. |
| **Postcondiciones** | Acreditación o devolución trazada al pagador original. |
| **Referencias Cruzadas** | RQF-118 y RQF-141 · HU17 |

### CU-26: Acordar horario y precio

| Atributo | Detalle |
|---|---|
| **ID** | CU-26 |
| **Caso de Uso** | Acordar horario y precio |
| **Actor** | Arrendatario y titular |
| **Descripción** | Las partes acuerdan el horario y el precio de la solicitud. |
| **Precondiciones** | Solicitud identificada |
| **Flujo Principal** | Registrar la conformidad de ambas partes sobre horario y precio o el rechazo de la solicitud. |
| **Flujos Alternativos** | Conservar el motivo aplicable cuando se rechaza la solicitud. |
| **Postcondiciones** | Acuerdo registrado para evaluar el bloqueo. |
| **Referencias Cruzadas** | RQF-123 a RQF-127 |

### CU-27: Procesar el vencimiento de la etapa

| Atributo | Detalle |
|---|---|
| **ID** | CU-27 |
| **Caso de Uso** | Procesar el vencimiento de la etapa |
| **Actor** | Proceso automático |
| **Descripción** | La plataforma libera el bloqueo al vencer la etapa contractual o de cobro. |
| **Precondiciones** | Etapa de contratación con bloqueo activo |
| **Flujo Principal** | Detectar vencimiento y liberar el bloqueo atómicamente. |
| **Flujos Alternativos** | Un reintento conserva el vencimiento original. |
| **Postcondiciones** | Intervalo liberado y transición registrada. |
| **Referencias Cruzadas** | RQF-129 y RQF-140 · PT-05 |

### CU-28: Conciliar un pago tardío

| Atributo | Detalle |
|---|---|
| **ID** | CU-28 |
| **Caso de Uso** | Conciliar un pago tardío |
| **Actor** | Operador y proveedor |
| **Descripción** | La plataforma concilia un pago tardío y mantiene el vencimiento. |
| **Precondiciones** | Pago posterior al vencimiento |
| **Flujo Principal** | Registrar el evento para conciliación y, si corresponde, vincular la devolución al pago original. |
| **Flujos Alternativos** | Un duplicado conserva el estado. |
| **Postcondiciones** | Ocupación liberada y resultado financiero trazable. |
| **Referencias Cruzadas** | RQF-128 y RQF-141 · PT-04 |

### CU-47: Consultar Historial de Reservas

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-47 |
| **Caso de Uso** | Consultar Historial de Reservas |
| **Actor** | Arrendatario · Arrendador |
| **Descripción** | El usuario consulta las reservas asociadas a su cuenta y su etapa vigente, desde la solicitud y el acuerdo hasta la contratación, el cobro, la operación y el cierre. |
| **Precondiciones** | Sesión activa con identidad verificada (KYC o KYB aprobado). |
| **Flujo Principal** | 1. El usuario accede a su panel de reservas.<br>2. El sistema despliega el historial de reservas asociadas a su cuenta.<br>3. El usuario selecciona una reserva y el sistema muestra su detalle y estado.<br>4. El sistema habilita las acciones disponibles según la etapa, la modalidad y el papel del usuario en la reserva. |
| **Flujos Alternativos** | **A1. Cuenta sin reservas (Paso 2):**<br>1. El sistema muestra el estado vacío del historial.<br><br>**A2. Reserva finalizada seleccionada (Paso 3):**<br>1. El sistema despliega el detalle en modo de solo lectura y no habilita acciones operativas. |
| **Postcondiciones** | Historial y estado de las reservas consultado por el usuario según su rol. |
| **Referencias Cruzadas** | RQF-199 · CU-24 (pago), CU-26 (acuerdo), CU-31 (contrato), CU-33/CU-34 (check-in y check-out), CU-42 (cierre) |

> **Caso de uso complementario (2.ª revisión, derivada de las Historias de Usuario):** CU-51 se incorpora al módulo M06 sin alterar la numeración de los casos existentes.

### CU-51: Cancelar Reserva

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-51 |
| **Caso de Uso** | Cancelar Reserva |
| **Actor** | Arrendatario |
| **Descripción** | El arrendatario cancela una reserva vigente conforme a la política de cancelación del espacio, gestionando la devolución de los fondos según corresponda. |
| **Precondiciones** | Sesión activa del arrendatario asociado a la reserva. La etapa y el plazo deben admitir cancelación conforme a la política aplicable. El vencimiento se procesa por CU-27. |
| **Flujo Principal** | 1. El arrendatario selecciona la reserva desde su historial de reservas.<br>2. El sistema muestra la política de cancelación aplicable y el monto estimado a devolver.<br>3. El arrendatario confirma la cancelación e ingresa un motivo opcional.<br>4. El sistema cambia el estado de la reserva a "Cancelada" y libera las fechas bloqueadas.<br>5. El sistema calcula el monto a reembolsar según la política de cancelación configurada.<br>6. Si procede una devolución, el sistema la vincula al pago y al pagador originales y registra su resultado.<br>7. El sistema notifica a ambas partes la cancelación y el estado de la devolución de los fondos. |
| **Flujos Alternativos** | **A1. Cancelación fuera del plazo permitido:**<br>1. El sistema rechaza la cancelación e informa que se encuentra fuera del plazo de la política de cancelación.<br><br>**A2. Rechazo del reembolso por la pasarela:**<br>1. El sistema registra el fallo, reintenta conforme a las políticas de conciliación (RNF-028) y mantiene la reserva cancelada con la devolución pendiente.<br><br>**A3. Reserva con disputa abierta:**<br>1. El sistema no habilita la cancelación y deriva el caso al flujo de resolución de disputas (CU-41). |
| **Postcondiciones** | Reserva cancelada, fechas liberadas, reembolso ejecutado o en proceso y partes notificadas del estado de devolución. |
| **Referencias Cruzadas** | RQF-228 al RQF-231 · CU-18 (política de cancelación) · CU-27 (liberación de fechas) · CU-24 (acreditación de renta) · CU-47 (acceso a la reserva) · HU19 |

---

## Módulo M07 — Contratos y Firma Electrónica

**RF cubiertos:** RQF-130 a RQF-142 + RQF-202 (14 RF)
**Actores participantes:** Arrendador, Arrendatario; SimpleFirma (servicio externo)
**Casos de uso:** CU-29, CU-30, CU-31, CU-32

**Figura C.8**\
*Casos de uso de contratación y firma opcional*

![](assets/figuras/anexo_c/cu_m07_contratos_firma.png)

*Nota.* Elaboración propia. La figura representa los casos de uso del alcance objetivo según el ADR.

La Figura 8 del Capítulo IX documenta las dos modalidades de contratación. CU-29 registra la aceptación. CU-30 se ejecuta cuando ambas partes eligen la firma opcional. CU-31 permite consultar la emisión y CU-32 trata el vencimiento de la etapa de firma.

### CU-29: Emitir y aceptar el contrato

| Atributo | Detalle |
|---|---|
| **ID** | CU-29 |
| **Caso de Uso** | Emitir y aceptar el contrato |
| **Actor** | Arrendatario y titular |
| **Descripción** | La plataforma emite el contrato y registra la aceptación de cada parte. |
| **Precondiciones** | Ambas identidades verificadas y acuerdo sobre horario y precio |
| **Flujo Principal** | Emitir documento inmutable y registrar la aceptación por parte. |
| **Flujos Alternativos** | Un cambio origina otra emisión. La elección bilateral de SimpleFirma activa CU-30. |
| **Postcondiciones** | La ruta sin firma habilita renta tras ambas aceptaciones. |
| **Referencias Cruzadas** | RQF-130 a RQF-133 · HU33 |

### CU-30: Firmar electrónicamente de forma opcional

| Atributo | Detalle |
|---|---|
| **ID** | CU-30 |
| **Caso de Uso** | Firmar electrónicamente de forma opcional |
| **Actor** | Arrendatario, titular y SimpleFirma |
| **Descripción** | Las partes completan las firmas cuando eligen la modalidad opcional. |
| **Precondiciones** | Ambas partes eligen la modalidad y los aportes exigibles se acreditan |
| **Flujo Principal** | Solicitar firmas para la emisión y registrar cada resultado. |
| **Flujos Alternativos** | Procesar vencimiento mediante CU-32. |
| **Postcondiciones** | Las dos firmas habilitan renta. |
| **Referencias Cruzadas** | RQF-133 a RQF-141 · HU33 |

### CU-31: Consultar la emisión contractual

| Atributo | Detalle |
|---|---|
| **ID** | CU-31 |
| **Caso de Uso** | Consultar la emisión contractual |
| **Actor** | Parte autorizada |
| **Descripción** | La parte autorizada accede al contrato de su emisión. |
| **Precondiciones** | Emisión asociada al arriendo y disponible |
| **Flujo Principal** | Consultar o descargar el documento de la emisión con su modalidad. |
| **Flujos Alternativos** | Denegar acceso a un tercero. |
| **Postcondiciones** | Documento y modalidad identificados. |
| **Referencias Cruzadas** | RQF-142 |

### CU-32: Procesar vencimiento de firma opcional

| Atributo | Detalle |
|---|---|
| **ID** | CU-32 |
| **Caso de Uso** | Procesar vencimiento de firma opcional |
| **Actor** | Proceso automático |
| **Descripción** | La plataforma procesa el vencimiento de la firma opcional y aplica su política de reversos. |
| **Precondiciones** | Etapa de firma opcional activa |
| **Flujo Principal** | Procesar vencimiento, liberar el bloqueo y tramitar reversos según la política ratificada. |
| **Flujos Alternativos** | Conservar el historial ante una firma tardía. |
| **Postcondiciones** | Intervalo liberado y conciliación trazable. |
| **Referencias Cruzadas** | RQF-140 y RQF-141 |

## Módulo M08 — Check-in y Check-out

**RF cubiertos:** RQF-143 a RQF-152 + RQF-203 a RQF-206 (14 RF)
**Actores participantes:** Arrendatario (inicia), Arrendador (recibe notificación y confirma la recepción)
**Casos de uso:** CU-33, CU-34, CU-48

### Diagrama de Casos de Uso

**Figura C.9**  
*Casos de Uso del Módulo M08: Check-in y Check-out*

![](assets/figuras/anexo_c/cu_m08_checkin_checkout.png)

*Nota.* Elaboración propia bajo estándar UML 2.5.

**Justificación de las relaciones**

| Relación | Tipo | Justificación |
|---|---|---|
| `ARR -- CU-33` | Asociación | El arrendador participa en CU-33 al recibir la notificación del ingreso del arrendatario (RQF-149); no participa en CU-34, cuyos RF (RQF-150 a RQF-152) son ejecutados solo por el arrendatario. |
| CU-33 ↔ CU-34 | Sin relación | Son objetivos independientes y distantes en el tiempo (inicio y término del arriendo). Se evaluó `<<include>>`, pero el check-out no forma parte de la ejecución del check-in, ni el check-in es condición condicional del check-out. |
| CU-48 → CU-34 | Sin relación (evaluado) | Se evaluó `<<extend>>` desde CU-48 hacia CU-34. Se descartó: la confirmación de recepción la ejecuta un **actor distinto** (Arrendador), ocurre **después** de que el caso base finaliza y no modifica el comportamiento del check-out (RQF-205). Se modela como caso de uso independiente con la entrega registrada como precondición. |

### CU-33: Realizar Check-in con Evidencia

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-33 |
| **Caso de Uso** | Realizar Check-in con Evidencia |
| **Actor** | Arrendatario (inicia) · Arrendador (recibe notificación) |
| **Descripción** | El arrendatario documenta la recepción del espacio mediante fotografías y comentarios, registrándose la fecha y ubicación del ingreso. |
| **Precondiciones** | Reserva confirmada y fecha actual coincidente con el día de inicio. La modalidad de firma corresponde a la emisión aceptada. |
| **Flujo Principal** | 1. El sistema habilita la opción de check-in únicamente el día de inicio de la reserva.<br>2. El arrendatario carga las fotografías del estado del espacio.<br>3. El arrendatario ingresa comentarios de texto asociados al ingreso.<br>4. El sistema registra la fecha y la ubicación al procesar el check-in.<br>5. El sistema cambia el estado de la reserva a "En_Curso".<br>6. El sistema notifica al arrendador que el arrendatario procesó el ingreso. |
| **Flujos Alternativos** | **A1. Check-in fuera de la fecha de inicio (Paso 1):**<br>1. El sistema bloquea la posibilidad de realizar check-in.<br><br>**A2. Envío sin fotografías (Paso 2):**<br>1. El sistema rechaza el formulario y exige al menos una evidencia fotográfica. |
| **Postcondiciones** | Evidencia de entrada registrada y reserva en estado "En_Curso". |
| **Referencias Cruzadas** | RQF-143 al RQF-149 · RQF-203 · CU-24 (reserva confirmada) · CU-41 y CU-48 (evidencia) · RNF-042 · HU35 |

### CU-34: Registrar la entrega

| Atributo | Detalle |
|---|---|
| **ID** | CU-34 |
| **Caso de Uso** | Registrar la entrega |
| **Actor** | Arrendatario |
| **Descripción** | El arrendatario registra evidencia de la entrega del espacio. |
| **Precondiciones** | Arriendo en curso y participante autorizado |
| **Flujo Principal** | Registrar la entrega con al menos una fotografía de evidencia. |
| **Flujos Alternativos** | Rechazar el registro sin fotografías y derivar las inconsistencias de operación al flujo de revisión. |
| **Postcondiciones** | Entrega disponible para confirmar en CU-48. |
| **Referencias Cruzadas** | RQF-150 a RQF-152 y RQF-204 · CU-48 · HU35 |

### CU-48: Confirmar la desocupación

| Atributo | Detalle |
|---|---|
| **ID** | CU-48 |
| **Caso de Uso** | Confirmar la desocupación |
| **Actor** | Titular |
| **Descripción** | El titular confirma la desocupación a partir de la entrega registrada. |
| **Precondiciones** | Entrega registrada |
| **Flujo Principal** | Confirmar desocupación, registrar fecha y ubicación y liberar solo el bloqueo correspondiente. |
| **Flujos Alternativos** | Denegar a quien carece de titularidad o si falta entrega. |
| **Postcondiciones** | Contrato conservado y republicación disponible. |
| **Referencias Cruzadas** | RQF-205 y RQF-206 · HU35 · PT-08 |

## Módulo M09 — Comunicación y Reputación

**RF cubiertos:** RQF-153 a RQF-158 + RQF-207 + RQF-232 a RQF-235 (11 RF)
**Actores participantes:** Arrendatario, Arrendador, Visitante
**Casos de uso:** CU-35, CU-36, CU-37, CU-38, CU-49

### Diagrama de Casos de Uso

**Figura C.10**  
*Casos de Uso del Módulo M09: Comunicación y Reputación*

![](assets/figuras/anexo_c/cu_m09_reputacion.png)

*Nota.* Elaboración propia bajo estándar UML 2.5.

**Justificación de las relaciones**

| Relación | Tipo | Justificación |
|---|---|---|
| CU-35 ↔ CU-36 | Sin relación | Se evaluó `<<extend>>` de la consulta hacia la vista de detalle, pero son objetivos con actores distintos (arrendatario que reseña y visitante que consulta) sin obligatoriedad entre sí. Se mantienen independientes. |
| CU-37 ↔ CU-38 | Sin relación | Consultar el historial no es obligatorio para enviar mensajes ni viceversa; no corresponde `<<include>>` ni `<<extend>>`. |
| Cuatro casos, sin relaciones | — | No existe comportamiento obligatorio compartido ni extensión condicional justificable con los RF 153 a 158. |
| CU-49 | Sin relación | Reportar una reseña es un objetivo autónomo del arrendador (RQF-207); no es obligatorio ni condicional respecto de CU-35, CU-36 o CU-44. |

### CU-35: Registrar Reseña y Calificación

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-35 |
| **Caso de Uso** | Registrar Reseña y Calificación |
| **Actor** | Arrendatario · Arrendador |
| **Descripción** | El arrendatario califica y reseña el espacio, y el arrendador califica y reseña al arrendatario, una vez finalizada la reserva. |
| **Precondiciones** | Reserva finalizada y usuario participante de la reserva. |
| **Flujo Principal** | 1. El usuario accede al formulario de reseña de una reserva finalizada.<br>2. El arrendatario registra la calificación numérica y la reseña del espacio.<br>3. El arrendador registra la calificación numérica y la reseña del arrendatario.<br>4. El sistema registra las evaluaciones y recalcula el promedio de calificaciones del espacio.<br>5. El sistema publica la reseña del espacio en la vista de detalle de la publicación. |
| **Flujos Alternativos** | **A1. Reserva no finalizada:**<br>1. El sistema no habilita el formulario de reseña mientras la reserva no esté finalizada.<br><br>**A2. Segunda reseña de la misma reserva (Paso 4):**<br>1. El sistema rechaza el registro si el mismo participante ya emitió su reseña para esa reserva.<br><br>**A3. Envío sin calificación numérica (Paso 2):**<br>1. El sistema exige seleccionar la puntuación y no registra la reseña. |
| **Postcondiciones** | Calificaciones y reseñas registradas, con el promedio de calificaciones del espacio actualizado. |
| **Referencias Cruzadas** | RQF-153, RQF-154 · RQF-232 al RQF-235 · CU-36 (visualización de reseñas), CU-47 (historial de reservas), CU-49 (reporte de reseña) · HU25 |

### CU-36: Consultar Reseñas y Calificaciones

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-36 |
| **Caso de Uso** | Consultar Reseñas y Calificaciones |
| **Actor** | Visitante |
| **Descripción** | El visitante consulta las reseñas y calificaciones publicadas de un espacio desde su vista de detalle. |
| **Precondiciones** | Publicación en estado "Activa". |
| **Flujo Principal** | 1. El visitante accede al detalle del espacio.<br>2. El sistema despliega las reseñas y calificaciones registradas. |
| **Flujos Alternativos** | **A1. Espacio sin reseñas:**<br>1. El sistema muestra el estado vacío indicando que aún no existen evaluaciones. |
| **Postcondiciones** | Evaluaciones del espacio consultadas por el visitante. |
| **Referencias Cruzadas** | RQF-155 · CU-20 (vista de detalle) · CU-44 (moderación por el administrador) |

### CU-37: Enviar Mensajes en el Chat de la Reserva

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-37 |
| **Caso de Uso** | Enviar Mensajes en el Chat de la Reserva |
| **Actor** | Arrendador · Arrendatario |
| **Descripción** | Las partes intercambian mensajes asociados a la reserva mediante el chat interno de la plataforma. |
| **Precondiciones** | Existencia de una reserva entre las partes. |
| **Flujo Principal** | 1. El arrendatario envía mensajes en el chat de la reserva.<br>2. El arrendador envía mensajes en el chat de la reserva.<br>3. El sistema asocia cada mensaje al hilo de la reserva correspondiente. |
| **Flujos Alternativos** | **A1. Intento de envío sin reserva asociada:**<br>1. El sistema no habilita el chat y no registra el mensaje. |
| **Postcondiciones** | Mensajes registrados en el hilo de la reserva. |
| **Referencias Cruzadas** | RQF-156, RQF-157 · CU-38 (historial) · HU34 |

### CU-38: Consultar Historial de Mensajes

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-38 |
| **Caso de Uso** | Consultar Historial de Mensajes |
| **Actor** | Arrendador · Arrendatario |
| **Descripción** | Las partes consultan el historial completo de mensajes asociado a la reserva. |
| **Precondiciones** | Existencia de una reserva con mensajes registrados. |
| **Flujo Principal** | 1. La parte abre el hilo de la reserva.<br>2. El sistema despliega el historial de mensajes de la reserva. |
| **Flujos Alternativos** | **A1. Hilo sin mensajes:**<br>1. El sistema muestra el estado vacío del chat. |
| **Postcondiciones** | Historial de mensajes consultado por la parte solicitante. |
| **Referencias Cruzadas** | RQF-158 · CU-37 (origen de los mensajes) · HU34 |

> **Caso de uso complementario (revisión de completitud):** CU-49 se incorpora al módulo M09 sin alterar la numeración de los casos de uso existentes.

### CU-49: Reportar Reseña

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-49 |
| **Caso de Uso** | Reportar Reseña |
| **Actor** | Arrendador |
| **Descripción** | El arrendador reporta una reseña publicada sobre su espacio cuando considera que incumple las reglas de publicación, habilitando su revisión por parte del administrador. |
| **Precondiciones** | Sesión activa y existencia de una reseña publicada sobre un espacio del arrendador. |
| **Flujo Principal** | 1. El arrendador accede a las reseñas de su espacio (CU-36).<br>2. Selecciona la reseña que desea reportar.<br>3. El sistema registra el reporte y cambia la reseña al estado "Reportada".<br>4. El sistema notifica la reseña reportada al administrador para su moderación (CU-44). |
| **Flujos Alternativos** | **A1. Reseña ya reportada (Paso 3):**<br>1. El sistema informa que la reseña se encuentra en revisión y no duplica el reporte. |
| **Postcondiciones** | Reseña reportada y disponible para la moderación del administrador. |
| **Referencias Cruzadas** | RQF-207 · CU-36 (visualización), CU-44 (moderación) |

---

## Módulo M10 — Disputas y conciliación

**RF cubiertos:** RQF-159 a RQF-177 + RQF-208 a RQF-211 (23 RF)
**Actores participantes:** Arrendador, Arrendatario, Administrador; Mercado Pago (pasarela externa)
**Casos de uso:** CU-39, CU-40, CU-41, CU-42

### Diagrama de Casos de Uso

**Figura C.11**  
*Casos de Uso del Módulo M10: Disputas y conciliación*

![](assets/figuras/anexo_c/cu_m10_disputas_payout.png)

*Nota.* Elaboración propia bajo estándar UML 2.5.

El reclamo y la conciliación conservan trazas independientes. La confirmación de desocupación pertenece al módulo M08. Los efectos sobre garantías requieren que la modalidad esté habilitada.

### CU-39: Registrar reclamo por daños

| Atributo | Detalle |
|---|---|
| **ID** | CU-39 |
| **Caso de Uso** | Registrar reclamo por daños |
| **Actor** | Titular |
| **Descripción** | La parte autorizada registra un reclamo por daños y adjunta evidencia. |
| **Precondiciones** | Reserva y evidencia de entrega identificadas |
| **Flujo Principal** | Registrar reclamo, motivo y evidencia. |
| **Flujos Alternativos** | Denegar acceso sin autorización o solicitar antecedentes. |
| **Postcondiciones** | Caso disponible para evaluación. |
| **Referencias Cruzadas** | RQF-159 a RQF-162 · CU-41 |

### CU-40: Presentar Descargos ante Disputa

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-40 |
| **Caso de Uso** | Presentar Descargos ante Disputa |
| **Actor** | Arrendatario |
| **Descripción** | El arrendatario presenta su defensa con texto y fotografías frente a un reclamo por daños (extensión de CU-39). |
| **Precondiciones** | Existencia de una disputa abierta y notificada al arrendatario (punto de extensión de CU-39). |
| **Flujo Principal** | 1. El arrendatario revisa el reclamo registrado.<br>2. Ingresa el texto de defensa.<br>3. Adjunta las fotografías de respaldo.<br>4. El sistema incorpora los antecedentes a la disputa para la revisión del administrador. |
| **Flujos Alternativos** | **A1. El arrendatario no presenta descargos:**<br>1. La extensión no se ejecuta y el administrador resuelve con la evidencia disponible (CU-41). |
| **Postcondiciones** | Antecedentes de defensa incorporados a la disputa. |
| **Referencias Cruzadas** | RQF-165 · extiende CU-39 · CU-41 · HU28 |

### CU-41: Resolver una disputa

| Atributo | Detalle |
|---|---|
| **ID** | CU-41 |
| **Caso de Uso** | Resolver una disputa |
| **Actor** | Operador autorizado |
| **Descripción** | La plataforma resuelve una disputa a partir de los antecedentes y descargos. |
| **Precondiciones** | Reclamo abierto |
| **Flujo Principal** | Revisar antecedentes y descargos, registrar decisión y notificar. |
| **Flujos Alternativos** | Derivar un ajuste de garantía habilitada a CU-42. |
| **Postcondiciones** | Resultado y trazabilidad de la disputa conservados. |
| **Referencias Cruzadas** | RQF-166 a RQF-171 · CU-39 y CU-42 |

### CU-42: Conciliar cobros y reversos

| Atributo | Detalle |
|---|---|
| **ID** | CU-42 |
| **Caso de Uso** | Conciliar cobros y reversos |
| **Actor** | Operador y proveedor |
| **Descripción** | La plataforma concilia los cobros y reversos asociados a la operación. |
| **Precondiciones** | Cobro o reverso identificado |
| **Flujo Principal** | Conciliar obligación, pagador, estado y eventos externos. |
| **Flujos Alternativos** | Deduplicar y tramitar devolución contra el pago original. |
| **Postcondiciones** | Movimiento trazable, independiente del bloqueo. |
| **Referencias Cruzadas** | RQF-128, RQF-141 y RQF-172 a RQF-177 |

## Módulo M11 — Administración y Auditoría

**RF cubiertos:** RQF-178 a RQF-185 + RQF-212 + RQF-236 (10 RF)
**Actores participantes:** Administrador
**Casos de uso:** CU-43, CU-44, CU-45, CU-46, CU-52

### Diagrama de Casos de Uso

**Figura C.12**  
*Casos de Uso del Módulo M11: Administración y Auditoría*

![](assets/figuras/anexo_c/cu_m11_administracion.png)

*Nota.* Elaboración propia bajo estándar UML 2.5.

**Justificación de las relaciones**

| Relación | Tipo | Justificación |
|---|---|---|
| CU-43 a CU-46, CU-52 | Sin relaciones | Son objetivos administrativos independientes. No existen RF que establezcan obligatoriedad o extensión condicional entre ellos. La inmutabilidad del repositorio de auditoría que respalda CU-46 es un RNF (RNF-017) y no genera caso de uso. |

### CU-43: Gestionar Bloqueo de Cuentas de Usuario

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-43 |
| **Caso de Uso** | Gestionar Bloqueo de Cuentas de Usuario |
| **Actor** | Administrador |
| **Descripción** | El administrador bloquea, consulta el motivo y desbloquea el acceso de una cuenta de usuario. |
| **Precondiciones** | Sesión activa con rol de Administrador. |
| **Flujo Principal** | 1. El administrador busca la cuenta del usuario.<br>2. El administrador bloquea el acceso a la cuenta de usuario.<br>3. El sistema registra la acción con su motivo.<br>4. El administrador consulta el motivo de bloqueo registrado.<br>5. El administrador desbloquea la cuenta dejándola habilitada nuevamente. |
| **Flujos Alternativos** | **A1. Cuenta ya bloqueada:**<br>1. El sistema informa el estado actual y el motivo registrado, sin duplicar la acción. |
| **Postcondiciones** | Estado de acceso de la cuenta actualizado y trazable. |
| **Referencias Cruzadas** | RQF-178 al RQF-180 · RQF-212 · CU-46 (trazabilidad) |

### CU-44: Moderar Reseñas Reportadas

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-44 |
| **Caso de Uso** | Moderar Reseñas Reportadas |
| **Actor** | Administrador |
| **Descripción** | El administrador oculta una reseña reportada que incumple las reglas de publicación, registrando el motivo de la acción. |
| **Precondiciones** | Existencia de una reseña reportada. |
| **Flujo Principal** | 1. El administrador accede a la reseña reportada.<br>2. El administrador oculta la reseña.<br>3. El administrador registra el motivo obligatorio de la moderación.<br>4. El sistema deja la reseña fuera de la vista pública. |
| **Flujos Alternativos** | **A1. Moderación sin motivo (Paso 3):**<br>1. El sistema exige registrar el motivo antes de aplicar la acción. |
| **Postcondiciones** | Reseña moderada y oculta de la vista pública. |
| **Referencias Cruzadas** | RQF-181, RQF-182 · CU-36 (visualización de reseñas) · CU-49 (origen del reporte) |

### CU-45: Generar Reportes de Gestión

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-45 |
| **Caso de Uso** | Generar Reportes de Gestión |
| **Actor** | Administrador |
| **Descripción** | El administrador genera reportes de reservas, pagos y disputas para el control de la operación. |
| **Precondiciones** | Sesión activa con rol de Administrador. |
| **Flujo Principal** | 1. El administrador selecciona el tipo de reporte requerido.<br>2. El sistema genera el reporte de reservas, pagos y disputas.<br>3. El administrador consulta el reporte generado. |
| **Flujos Alternativos** | **A1. Período sin datos:**<br>1. El sistema informa que no existen registros para los criterios seleccionados. |
| **Postcondiciones** | Reporte de gestión disponible para el administrador. |
| **Referencias Cruzadas** | RQF-183 |

### CU-46: Consultar y Exportar Historial de Auditoría

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-46 |
| **Caso de Uso** | Consultar y Exportar Historial de Auditoría |
| **Actor** | Administrador |
| **Descripción** | El operador autorizado consulta eventos de auditoría con los filtros de OpenAPI y exporta los resultados permitidos. |
| **Precondiciones** | Sesión activa con rol de Administrador. |
| **Flujo Principal** | 1. El operador selecciona los filtros autorizados para la consulta.<br>2. El sistema consulta y despliega el historial de auditoría asociado.<br>3. El administrador exporta los registros de auditoría consultados. |
| **Flujos Alternativos** | **A1. Filtros sin coincidencias (Paso 2):**<br>1. El sistema informa que no existen trazas de auditoría para el identificador ingresado.<br><br>**A2. Sin consulta previa (Paso 3):**<br>1. El sistema no habilita la exportación hasta ejecutar una consulta. |
| **Postcondiciones** | Historial de auditoría consultado y, si corresponde, exportado. |
| **Referencias Cruzadas** | RQF-184, RQF-185 · RNF-017 (inmutabilidad del repositorio) |

> **Caso de uso complementario (2.ª revisión, derivada de las Historias de Usuario):** CU-52 se incorpora al módulo M11 sin alterar la numeración de los casos existentes.

### CU-52: Consultar Publicaciones de la Plataforma

| Atributo | Detalle |
| :--- | :--- |
| **ID** | CU-52 |
| **Caso de Uso** | Consultar Publicaciones de la Plataforma |
| **Actor** | Administrador |
| **Descripción** | El administrador consulta el listado de espacios publicados en la plataforma para su supervisión. |
| **Precondiciones** | Sesión activa con rol de Administrador. |
| **Flujo Principal** | 1. El administrador accede al listado de espacios publicados.<br>2. El sistema despliega las publicaciones con sus datos principales (título, arrendador, tipo de inmueble, estado y precio base).<br>3. El administrador selecciona una publicación y el sistema muestra su detalle. |
| **Flujos Alternativos** | **A1. Plataforma sin publicaciones:**<br>1. El sistema muestra el estado vacío del listado. |
| **Postcondiciones** | Publicaciones de la plataforma consultadas por el administrador. |
| **Referencias Cruzadas** | RQF-236 · CU-44 (moderación), CU-45 (reportes), CU-46 (auditoría) · HU26 |

---

## Alcance de verificación por módulo

**Tabla C.1**\
*Contratos y evidencia de los módulos revisados*

| Módulo | Contrato o evidencia de referencia | Alcance de la comprobación |
|---|---|---|
| M01 y M02 | Registro, sesión, exportación y solicitud de supresión en OpenAPI. | La ejecución de derechos y el tratamiento de archivos dependen de finalidad, autorización y entorno. |
| M03 y M04 | Evidencia F5/F6 de verificación documental, borrador y galería. | El ensayo sintético distingue capacidad técnica, publicación por titularidad y verificación contractual. |
| M05 | Rutas de búsqueda, cotización y disponibilidad. | El horario semanal y los bloqueos describen oferta. La recurrencia de reservas permanece diferida. |
| M09 | Rutas de mensajería y reseñas por reserva y consulta de reseñas de espacio. | La escritura requiere la participación autorizada. La proyección pública del espacio se distingue de la evaluación de personas. |
| M11 | Rutas de cuentas, publicaciones, auditoría e indicadores administrativos. | Cada operación exige una capacidad. Los reportes integrales de operación y finanzas conservan su propio alcance y criterio de aceptación. |

*Nota.* Elaboración propia a partir del contrato de desarrollo y de la evidencia por corte. Una ruta documentada identifica la interfaz y su alcance.

## 4. Trazabilidad y Cobertura

### 4.1 Resumen módulo → casos de uso → requerimientos funcionales

| Módulo | Casos de uso | RF base | RF complementarios | Total RF |
|---|---|---|---|---|
| M01 — Autenticación y Gestión de Cuenta | CU-01 … CU-06, CU-50 | RQF-001 – RQF-023 | RQF-186 – RQF-188, RQF-213 – RQF-218 | 32 |
| M02 — Perfil y Privacidad del Usuario | CU-07 … CU-09 | RQF-024 – RQF-037 | RQF-189 – RQF-191 | 17 |
| M03 — Verificación de Identidad (KYC/KYB) | CU-10 … CU-14 | RQF-038 – RQF-059 | RQF-192 – RQF-194, RQF-219 – RQF-220 | 27 |
| M04 — Gestión de Publicaciones | CU-15 … CU-18 | RQF-060 – RQF-093 | RQF-195 – RQF-198, RQF-221 – RQF-226 | 44 |
| M05 — Búsqueda y Cotización de Espacios | CU-19 … CU-21 | RQF-094 – RQF-107 | — | 14 |
| M06 — Reservas y cobros | CU-22 … CU-28, CU-47, CU-51 | RQF-108 – RQF-129 | RQF-199 – RQF-201, RQF-227 – RQF-231 | 30 |
| M07 — Contratos y Firma Electrónica | CU-29 … CU-32 | RQF-130 – RQF-142 | RQF-202 | 14 |
| M08 — Check-in y Check-out | CU-33, CU-34, CU-48 | RQF-143 – RQF-152 | RQF-203 – RQF-206 | 14 |
| M09 — Comunicación y Reputación | CU-35 … CU-38, CU-49 | RQF-153 – RQF-158 | RQF-207, RQF-232 – RQF-235 | 11 |
| M10 — Disputas y conciliación | CU-39 … CU-42 | RQF-159 – RQF-177 | RQF-208 – RQF-211 | 23 |
| M11 — Administración y Auditoría | CU-43 … CU-46, CU-52 | RQF-178 – RQF-185 | RQF-212, RQF-236 | 10 |
| **Total** | **52 CU** | **185 RF** | **51 RF** | **236 RF** |

**Verificación de cobertura:** cada uno de los **236 requerimientos funcionales** queda asignado a exactamente un caso de uso —**185** del catálogo base y **51** complementarios—, sin duplicación ni omisión. El detalle RF ↔ CU está declarado en la fila **Referencias Cruzadas** de cada ficha.

> **Excepción documentada:** CU-10 (caso de uso abstracto) declara el rango RQF-038 a RQF-053 porque sus dos especializaciones, CU-11 (KYC) y CU-12 (KYB), cubren ese rango. No es duplicación: CU-10 no se instancia de forma directa.

**Verificación de los requerimientos complementarios**

| RF | Caso de uso que lo implementa | Módulo |
|---|---|---|
| RQF-186, RQF-187 | CU-01 | M01 |
| RQF-188 | CU-02 | M01 |
| RQF-189, RQF-190, RQF-191 | CU-08 | M02 |
| RQF-192 | CU-11 | M03 |
| RQF-193 | CU-14 | M03 |
| RQF-194 | CU-12 | M03 |
| RQF-195, RQF-196, RQF-197, RQF-198 | CU-18 | M04 |
| RQF-199 | CU-47 | M06 |
| RQF-200 | CU-27 | M06 |
| RQF-201 | CU-24 | M06 |
| RQF-202 | CU-30 | M07 |
| RQF-203 | CU-33 | M08 |
| RQF-204 | CU-34 | M08 |
| RQF-205, RQF-206 | CU-48 | M08 |
| RQF-207 | CU-49 | M09 |
| RQF-208 | CU-42 | M10 |
| RQF-209, RQF-210 | CU-41 | M10 |
| RQF-211 | CU-42 | M10 |
| RQF-212 | CU-43 | M11 |
| RQF-213 | CU-01 | M01 |
| RQF-214, RQF-215, RQF-216, RQF-217, RQF-218 | CU-50 | M01 |
| RQF-219, RQF-220 | CU-11 | M03 |
| RQF-221, RQF-222, RQF-223, RQF-224 | CU-18 | M04 |
| RQF-225, RQF-226 | CU-17 | M04 |
| RQF-227 | CU-22 | M06 |
| RQF-228, RQF-229, RQF-230, RQF-231 | CU-51 | M06 |
| RQF-232, RQF-233, RQF-234, RQF-235 | CU-35 | M09 |
| RQF-236 | CU-52 | M11 |

### 4.2 Relaciones UML modeladas (resumen global)

| Relación | Origen → Destino | Tipo | Base funcional |
|---|---|---|---|
| R-01 | CU-02 → CU-01 | `<<extend>>` | RQF-009 (verificación condicional posterior al registro) |
| R-02 | CU-04 → CU-03 | `<<extend>>` | RQF-015 a RQF-017 (bloqueo por 5 intentos fallidos) |
| R-03 | CU-11 → CU-10 | Generalización | Especialización KYC (RQF-038 a RQF-047) |
| R-04 | CU-12 → CU-10 | Generalización | Especialización KYB (RQF-048 a RQF-053) |
| R-05 | CU-22 → CU-23 | `<<include>>` | RQF-111 (validación de disponibilidad obligatoria) |
| R-06 | CU-25 → CU-24 | `<<extend>>` | RQF-118 (garantía aplicable y habilitada) |
| R-07 | CU-27 | Autónomo | RQF-129 y RQF-140 (vencimiento en etapas contractuales y de cobro) |
| R-08 | CU-28 | Autónomo | RQF-128 (conciliación de pago tardío) |
| R-09 | CU-32 → CU-30 | `<<extend>>` | RQF-140 (cancelación condicional por falta de firma) |
| R-10 | CU-39 y CU-42 | Autónomos | El reclamo aporta evidencia. La conciliación registra movimientos. |
| R-11 | CU-30 → CU-29 | `<<extend>>` | RQF-133 (elección bilateral y aportes acreditados) |
| R-13 | CU-22 → CU-26 | `<<include>>` | RQF-125 (acuerdo obligatorio antes de activar el bloqueo) |
| R-12 | Visitante ◁— Usuario Registrado ◁— Arrendador / Arrendatario | Generalización de actores | Herencia de capacidades (ver sección 2.3) |

### 4.3 Relaciones evaluadas y descartadas (justificación)

| Relación evaluada | Se descartó porque |
|---|---|
| `<<include>>` CU-15 → CU-16 (galería dentro de la publicación) | La galería no es obligatoria para registrar la publicación; el `<<include>>` exige obligatoriedad. |
| `<<include>>` CU-26 → CU-29 (contrato al aprobar la solicitud) | La dependencia es real (RQF-130) pero se documenta como pre-condición para no acoplar dos módulos diferentes en un mismo diagrama. |
| `<<include>>` CU-29 → CU-30 (firma tras el envío) | La firma la ejecutan las partes con un proveedor externo, de forma asíncrona; no es una ejecución obligatoria sincrónica del envío. |
| `<<include>>` CU-19 → CU-21 / CU-20 → CU-36 (detalle y reseñas) | No existe obligatoriedad: se puede buscar sin cotizar, y consultar el detalle no exige ver reseñas. |
| `<<extend>>` CU-13 → CU-11/CU-12 (revisión manual) | La revisión manual es un objetivo autónomo del Administrador, no un comportamiento opcional del caso base. Se documenta como flujo alternativo derivado. |
| Caso de uso "Cifrar contraseña" | Corresponde al requisito no funcional `RNF-013`. |
| Caso de uso "Transmitir logs a BigQuery" | Es `RNF-017`; no existe RF observable por un actor. |
| Caso de uso "Consultar Mis Publicaciones" | El RQF-093 se integra como primer paso de CU-18 y no requiere ficha independiente. |
| Generalización Administrador → Usuario Registrado | No hay especialización real: el administrador no ejecuta los flujos comerciales del marketplace. |
| Relación entre los casos complementarios CU-47, CU-48 y CU-49 y los casos existentes | Se evaluó `<<extend>>` / `<<include>>` hacia casos del mismo módulo y se descartó: son objetivos autónomos (consultar, confirmar evidencia, reportar), no obligatorios para otro caso de uso; además CU-48 y CU-49 son iniciados por actores distintos a los del caso base. |

---
