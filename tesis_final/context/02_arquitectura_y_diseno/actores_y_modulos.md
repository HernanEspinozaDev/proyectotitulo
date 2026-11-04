# Actores del Sistema y Módulos con Requerimientos Funcionales
## Sistema: EspaciGo — Marketplace SaaS B2B2C de Espacios Comerciales

> **Versión sincronizada con el Anexo de Requerimientos Funcionales vigente: 236 RF (RQF-001 a RQF-236) = 185 RF base + 27 RF complementarios (1.ª revisión de completitud) + 24 RF complementarios (2.ª revisión, derivada de la revisión íntegra de las Historias de Usuario).**
> Este documento reemplaza la versión anterior construida sobre 220 RF. **No renumera ningún requerimiento**: cada RF conserva el ID y el texto exacto del anexo `anexo_requerimientos_funcionales.md`, de modo que ambos documentos quedan sincronizados por ID.

**Convención de nomenclatura**
- `RQF-###` = Requerimiento Funcional (se mantiene la nomenclatura del anexo para no romper la trazabilidad).
- `RNF-###` = Requerimiento No Funcional (anexo aparte).
- `CU-##` = Caso de Uso (ver `anexo_casos_de_uso.md`).
- `HU##` = Historia de Usuario (ver `anexo_historias_de_usuario.md`).

**Criterios usados para construir los módulos**
1. Un módulo agrupa requerimientos funcionales que persiguen un mismo objetivo funcional del sistema.
2. Los RF se asignan a **un único módulo**, sin duplicar IDs, y cubren el catálogo completo (185/185).
3. Los módulos se ordenan según el ciclo de vida del negocio (identidad → catálogo → reserva → pago → contrato → operación → post-servicio → gobierno).
4. Los módulos **no son requerimientos**: son agrupaciones que existen para organizar los diagramas de casos de uso (corrección de la profesora: *"no poner módulos como requerimientos funcionales, los módulos van solo en los casos de uso"*).
5. Los requerimientos de tipo técnico, de infraestructura o de calidad (cifrado de contraseñas, inmutabilidad de logs, tokenización de tarjetas, escalabilidad) **no están aquí**: pertenecen al catálogo de RNF y **no generan casos de uso**.

---

## 1. 🎭 Identificación de Actores

Se consideran actores **únicamente entidades externas** al sistema (personas/roles y sistemas o servicios de terceros). Los componentes internos de la arquitectura (frontend Next.js, API en Go, contenedores, colas, repositorios de datos, controladores) **no son actores**.

### 1.1 Actores Primarios (roles humanos)

| Actor | Alias UML | Descripción | Estado requerido |
|---|---|---|---|
| **Visitante** | `Visitante` | Usuario anónimo, sin cuenta registrada. Puede explorar el catálogo público (búsqueda, mapa, detalle y reseñas) pero no puede interactuar transaccionalmente. | Sin cuenta |
| **Usuario Registrado** | `UsuarioRegistrado` | Posee cuenta con correo verificado, pero aún sin validación de identidad. Puede iniciar sesión, gestionar su perfil, administrar sus datos y solicitar validaciones de identidad. | Correo verificado |
| **Arrendador** | `Arrendador` | Usuario con identidad verificada (KYC o KYB) que publica y administra espacios, gestiona su calendario, aprueba o rechaza solicitudes de reserva, ejecuta check-in/check-out y reclama daños. Corresponde al "Propietario" que mencionan las Historias de Usuario. | KYC/KYB aprobado |
| **Arrendatario** | `Arrendatario` | Usuario con identidad verificada (KYC o KYB) que busca espacios, cotiza, reserva, paga, firma, realiza check-in/check-out, emite reseñas y presenta descargos. | KYC/KYB aprobado |
| **Administrador** | `Administrador` | Operador interno de EspaciGo. Revisa validaciones de identidad fallidas, arbitra disputas, modera reseñas, bloquea cuentas, genera reportes y audita la trazabilidad. Accede al backoffice. | Rol interno de plataforma |

> **Nota de compatibilidad terminológica:** las Historias de Usuario usan "Propietario"; los casos de uso y requerimientos usan "Arrendador". Se mantiene `Arrendador` como nombre oficial del actor y "Propietario" como sinónimo reconocido en las HU.
>
> **Nota de roles no excluyentes:** un mismo usuario puede actuar simultáneamente como Arrendador y como Arrendatario; los roles no son mutuamente excluyentes.

### 1.2 Actores Secundarios (sistemas y servicios externos)

| Actor Externo | Tipo | Rol en el sistema | Módulos donde participa |
|---|---|---|---|
| **Registro Civil** | Servicio externo (API) | Entrega la vigencia de la Cédula de Identidad durante la validación KYC. | M03 |
| **SII** (Servicio de Impuestos Internos) | Servicio externo (API) | Entrega el inicio de actividades y el giro comercial de la empresa durante la validación KYB. | M03 |
| **Mercado Pago** | Servicio externo (pasarela de pagos) | Procesa el pago retenido (Escrow), ejecuta la pre-autorización de garantía, los reembolsos, el cobro de la garantía y la transferencia de fondos (Payout). | M06, M10 |
| **FirmaVirtual** | Servicio externo (firma electrónica) | Recibe el contrato PDF y devuelve los enlaces de firma y las notificaciones de firma completada. | M07 |

### 1.3 Generalización de actores

La relación de especialización se modela porque un actor especializado **puede ejecutar todo lo que ejecuta el actor general y además funcionalidades propias** (herencia de capacidades):

```text
Visitante  ◁── UsuarioRegistrado ◁── Arrendador
                                 ◁── Arrendatario
Administrador (actor independiente, sin relación de herencia con los anteriores)
```

Justificación de cada generalización:

| Relación | Justificación funcional |
|---|---|
| `UsuarioRegistrado --|> Visitante` | Todo usuario registrado puede hacer lo que hace un visitante (buscar, filtrar, ver detalle, ver reseñas), y además autenticarse y operar con cuenta. |
| `Arrendador --|> UsuarioRegistrado` | El arrendador debe poder iniciar sesión, gestionar perfil, validar identidad y usar el catálogo: ejecuta todo lo del usuario registrado más la gestión de publicaciones y solicitudes. |
| `Arrendatario --|> UsuarioRegistrado` | Mismo razonamiento: hereda capacidades del usuario registrado y agrega reserva, pago, contrato, check-in/out y reseñas. |
| `Administrador` | **No se generaliza.** No es un usuario del marketplace: opera el backoffice con permisos propios (validaciones manuales, arbitraje, moderación, reportes, auditoría) y no ejecuta los flujos comerciales de arrendador ni de arrendatario. |

### 1.4 Exclusiones explícitas de actores (justificación)

| Elemento | Por qué NO es actor |
|---|---|
| **Google BigQuery / Data Warehouse** | Es un repositorio de datos consumido internamente por el sistema para cumplir el RNF-017 (inmutabilidad de logs). No existe un requerimiento funcional de interacción iniciada por una entidad externa con un objetivo observable, por lo que **no genera casos de uso ni actor**. |
| **Registro Civil / SII / Mercado Pago / FirmaVirtual** | **Sí son actores** (sistemas de terceros, fuera del límite del sistema), porque participan en casos de uso iniciados por un actor humano y respaldados por RF explícitos (RQF-044, RQF-051, RQF-114–118, RQF-133–139). |
| **Frontend Next.js, API Go, Docker, Cloud Run, controladores, servicios internos** | Componentes internos de la solución: se describen en la Arquitectura TI, no son actores. |
| **Encriptación de contraseñas (bcrypt)** | Es el `RNF-013` (Seguridad / Confidencialidad). **No es caso de uso ni actor** (corrección explícita de la profesora). |

---

## 2. 📦 Módulos del Sistema y Requerimientos Funcionales (236 RF)

> Los textos de los RF se reproducen **literalmente** desde `anexo_requerimientos_funcionales.md`.

### 📌 M01 — Autenticación y Gestión de Cuenta
**RF del módulo:** RQF-001 a RQF-023 (23 RF) + complementarios RQF-186 a RQF-188 (3 RF) + RQF-213 a RQF-218 (6 RF) = **32 RF**
**Objetivo del módulo:** permitir que un visitante se convierta en usuario registrado verificado aceptando los términos y condiciones, y que pueda autenticarse, gestionar su contraseña (cambiarla y recuperarla) y cerrar sesión de forma segura.
**Actores primarios:** Visitante, Usuario Registrado.
**Actores externos:** —
**Casos de uso asociados:** CU-01, CU-02, CU-03, CU-04, CU-05, CU-06, CU-50.

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
| RQF-186 | El sistema debe exigir la aceptación de los términos y condiciones durante el registro de la cuenta. |
| RQF-187 | El sistema debe registrar la fecha y la versión de los términos y condiciones aceptados. |
| RQF-188 | El sistema debe permitir reenviar el correo de verificación de la cuenta. |
| RQF-213 | El sistema debe registrar la preferencia de uso del usuario durante el registro de la cuenta. |
| RQF-214 | El sistema debe permitir al usuario autenticado cambiar su contraseña. |
| RQF-215 | El sistema debe validar la contraseña actual al solicitar un cambio de contraseña. |
| RQF-216 | El sistema debe rechazar una contraseña nueva igual a la contraseña actual. |
| RQF-217 | El sistema debe rechazar una contraseña nueva utilizada en los últimos 3 meses. |
| RQF-218 | El sistema debe notificar al usuario el cambio de contraseña realizado. |

---

### 📌 M02 — Perfil y Privacidad del Usuario
**RF del módulo:** RQF-024 a RQF-037 (14 RF) + complementarios RQF-189 a RQF-191 (3 RF) = **17 RF**
**Objetivo del módulo:** permitir al usuario mantener sus datos personales y de cobro (incluyendo la gestión completa de su cuenta bancaria) y ejercer su derecho de eliminación de datos personales.
**Actores primarios:** Usuario Registrado (heredan Arrendador y Arrendatario).
**Actores externos:** —
**Casos de uso asociados:** CU-07, CU-08, CU-09.

| ID | Descripción del Requerimiento Funcional |
| :--- | :--- |
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
| RQF-189 | El sistema debe permitir consultar la cuenta bancaria registrada en el perfil. |
| RQF-190 | El sistema debe permitir modificar la cuenta bancaria asociada al perfil. |
| RQF-191 | El sistema debe permitir eliminar la cuenta bancaria asociada al perfil. |

---

### 📌 M03 — Verificación de Identidad (KYC / KYB)
**RF del módulo:** RQF-038 a RQF-059 (22 RF) + complementarios RQF-192 a RQF-194 (3 RF) + RQF-219, RQF-220 (2 RF) = **27 RF**
**Objetivo del módulo:** acreditar la identidad de personas naturales (KYC) y de empresas (KYB) para habilitar la operación transaccional, permitiendo consultar el estado de la validación y resolviendo manualmente los casos que fallan.
**Actores primarios:** Usuario Registrado, Administrador.
**Actores externos:** Registro Civil, SII.
**Casos de uso asociados:** CU-10 (general), CU-11, CU-12, CU-13, CU-14.

| ID | Descripción del Requerimiento Funcional |
| :--- | :--- |
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
| RQF-192 | El sistema debe permitir capturar una fotografía tipo selfie durante la validación KYC. |
| RQF-193 | El sistema debe permitir consultar el estado de la validación de identidad. |
| RQF-194 | El sistema debe notificar al usuario el resultado de su validación KYB. |
| RQF-219 | El sistema debe validar que las imágenes de la cédula no superen los 10MB. |
| RQF-220 | El sistema debe cambiar el estado del perfil a "Pendiente de Verificación" al recibir los documentos de identidad. |

---

### 📌 M04 — Gestión de Publicaciones
**RF del módulo:** RQF-060 a RQF-093 (34 RF) + complementarios RQF-195 a RQF-198 (4 RF) + RQF-221 a RQF-226 (6 RF) = **44 RF**
**Objetivo del módulo:** que el arrendador verificado registre, publique, ilustre, calendarice y mantenga vigente y actualizada la oferta de espacios del marketplace.
**Actores primarios:** Arrendador (la consulta pública del catálogo se modela en M05).
**Actores externos:** —
**Casos de uso asociados:** CU-15, CU-16, CU-17, CU-18.

| ID | Descripción del Requerimiento Funcional |
| :--- | :--- |
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
| RQF-195 | El sistema debe permitir modificar la descripción de una publicación existente. |
| RQF-196 | El sistema debe permitir modificar las reglas de uso de una publicación existente. |
| RQF-197 | El sistema debe permitir modificar la capacidad máxima de una publicación existente. |
| RQF-198 | El sistema debe permitir modificar la modalidad tarifaria de una publicación existente. |
| RQF-221 | El sistema debe validar que el precio base modificado sea mayor a \$5.000 CLP. |
| RQF-222 | El sistema debe validar que la regla de uso personalizada no exceda los 250 caracteres. |
| RQF-223 | El sistema debe permitir configurar la política de cancelación de la publicación. |
| RQF-224 | El sistema debe mostrar las reglas de uso y la política de cancelación en el detalle de la publicación. |
| RQF-225 | El sistema debe exigir un motivo al registrar un bloqueo manual de fechas. |
| RQF-226 | El sistema debe validar que la fecha de término del bloqueo manual sea posterior a la fecha de inicio. |

---

### 📌 M05 — Búsqueda y Cotización de Espacios
**RF del módulo:** RQF-094 a RQF-107 (14 RF) = **14 RF**
**Objetivo del módulo:** que cualquier visitante encuentre espacios disponibles según ubicación, precio, tipo y fechas, y que el arrendatario conozca el desglose del costo antes de reservar.
**Actores primarios:** Visitante, Usuario Registrado, Arrendatario.
**Actores externos:** —
**Casos de uso asociados:** CU-19, CU-20, CU-21.

| ID | Descripción del Requerimiento Funcional |
| :--- | :--- |
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

---

### 📌 M06 — Reservas y Pagos (Escrow)
**RF del módulo:** RQF-108 a RQF-129 (22 RF) + complementarios RQF-199 a RQF-201 (3 RF) + RQF-227 a RQF-231 (5 RF) = **30 RF**
**Objetivo del módulo:** registrar la reserva sin colisiones, permitir el seguimiento y la cancelación de las reservas del usuario, cobrar el pago retenido en custodia (Escrow), bloquear la garantía y obtener la aprobación o el rechazo del arrendador.
**Actores primarios:** Arrendatario, Arrendador.
**Actores externos:** Mercado Pago.
**Casos de uso asociados:** CU-22, CU-23, CU-24, CU-25, CU-26, CU-27, CU-28, CU-47, CU-51.

| ID | Descripción del Requerimiento Funcional |
| :--- | :--- |
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
| RQF-199 | El sistema debe permitir consultar el historial de reservas asociadas al usuario. |
| RQF-200 | El sistema debe liberar las fechas bloqueadas al cancelar una reserva. |
| RQF-201 | El sistema debe notificar al arrendatario cuando el pago sea rechazado. |
| RQF-227 | El sistema debe rechazar la reserva si el usuario no cuenta con su identidad verificada. |
| RQF-228 | El sistema debe permitir al arrendatario cancelar una reserva conforme a la política de cancelación. |
| RQF-229 | El sistema debe calcular el monto a reembolsar según la política de cancelación aplicada. |
| RQF-230 | El sistema debe ejecutar el reembolso al arrendatario tras la cancelación de la reserva. |
| RQF-231 | El sistema debe notificar a las partes la cancelación de la reserva. |

---

### 📌 M07 — Contratos y Firma Electrónica
**RF del módulo:** RQF-130 a RQF-142 (13 RF) + complementario RQF-202 (1 RF) = **14 RF**
**Objetivo del módulo:** generar el contrato con los datos legales de las partes y del inmueble, gestionarlo ante el proveedor de firma electrónica (incluyendo el rechazo de firma) y resguardar el documento firmado.
**Actores primarios:** Arrendador, Arrendatario.
**Actores externos:** FirmaVirtual.
**Casos de uso asociados:** CU-29, CU-30, CU-31, CU-32.

| ID | Descripción del Requerimiento Funcional |
| :--- | :--- |
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
| RQF-202 | El sistema debe registrar el rechazo de firma notificado por el proveedor de firma electrónica. |

---

### 📌 M08 — Check-in y Check-out
**RF del módulo:** RQF-143 a RQF-152 (10 RF) + complementarios RQF-203 a RQF-206 (4 RF) = **14 RF**
**Objetivo del módulo:** documentar con evidencia fotográfica obligatoria, fecha y ubicación la entrega y la devolución del espacio, incluyendo la confirmación de recepción del arrendador, y habilitar el estado operativo de la reserva.
**Actores primarios:** Arrendatario, Arrendador.
**Actores externos:** —
**Casos de uso asociados:** CU-33, CU-34, CU-48.

| ID | Descripción del Requerimiento Funcional |
| :--- | :--- |
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
| RQF-203 | El sistema debe exigir la carga de al menos una fotografía para procesar el Check-in. |
| RQF-204 | El sistema debe exigir la carga de al menos una fotografía para registrar el Check-out. |
| RQF-205 | El sistema debe permitir al arrendador confirmar la recepción del espacio tras el Check-out. |
| RQF-206 | El sistema debe registrar la fecha y la ubicación al confirmar la recepción del espacio. |

---

### 📌 M09 — Comunicación y Reputación
**RF del módulo:** RQF-153 a RQF-158 (6 RF) + complementario RQF-207 (1 RF) + RQF-232 a RQF-235 (4 RF) = **11 RF**
**Objetivo del módulo:** permitir la calificación y reseña de los espacios, el reporte de reseñas que incumplen las reglas y la comunicación trazable entre las partes durante la reserva.
**Actores primarios:** Arrendatario, Arrendador, Visitante (consulta de reseñas).
**Actores externos:** —
**Casos de uso asociados:** CU-35, CU-36, CU-37, CU-38, CU-49.

| ID | Descripción del Requerimiento Funcional |
| :--- | :--- |
| RQF-153 | El sistema debe permitir al arrendatario registrar una calificación numérica del espacio. |
| RQF-154 | El sistema debe permitir al arrendatario registrar una reseña de texto del espacio. |
| RQF-155 | El sistema debe mostrar las reseñas y calificaciones en la vista de detalle de la publicación. |
| RQF-156 | El sistema debe permitir al arrendatario enviar mensajes en el chat de la reserva. |
| RQF-157 | El sistema debe permitir al arrendador enviar mensajes en el chat de la reserva. |
| RQF-158 | El sistema debe permitir a las partes consultar el historial de mensajes de la reserva. |
| RQF-207 | El sistema debe permitir reportar una reseña publicada. |
| RQF-232 | El sistema debe permitir al arrendador registrar una calificación numérica del arrendatario. |
| RQF-233 | El sistema debe permitir al arrendador registrar una reseña de texto del arrendatario. |
| RQF-234 | El sistema debe rechazar el registro de una segunda reseña para la misma reserva. |
| RQF-235 | El sistema debe calcular el promedio de calificaciones del espacio. |

---

### 📌 M10 — Disputas, Payout y Facturación
**RF del módulo:** RQF-159 a RQF-177 (19 RF) + complementarios RQF-208 a RQF-211 (4 RF) = **23 RF**
**Objetivo del módulo:** resolver el cierre económico del servicio: liberar los fondos al arrendador, liberar la garantía en el flujo sin reclamos o ejecutarla según el fallo, resolver reclamos por daños y emitir y enviar la boleta de la comisión.
**Actores primarios:** Arrendador, Arrendatario, Administrador.
**Actores externos:** Mercado Pago.
**Casos de uso asociados:** CU-39, CU-40, CU-41, CU-42.

| ID | Descripción del Requerimiento Funcional |
| :--- | :--- |
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
| RQF-208 | El sistema debe liberar la totalidad de la garantía al arrendatario cuando la reserva finalice sin reclamos. |
| RQF-209 | El sistema debe permitir al administrador consultar la confirmación de recepción vinculada a la disputa. |
| RQF-210 | El sistema debe notificar el resultado de la disputa a las partes. |
| RQF-211 | El sistema debe enviar la boleta electrónica al correo del arrendador. |

---

### 📌 M11 — Administración y Auditoría
**RF del módulo:** RQF-178 a RQF-185 (8 RF) + complementarios RQF-212 y RQF-236 (2 RF) = **10 RF**
**Objetivo del módulo:** entregar al administrador las herramientas de gobierno de la plataforma: búsqueda y bloqueo de cuentas, moderación, reportes y consulta/exportación de la trazabilidad.
**Actores primarios:** Administrador.
**Actores externos:** — (la inmutabilidad del repositorio de logs corresponde al RNF-017, no a un actor).
**Casos de uso asociados:** CU-43, CU-44, CU-45, CU-46.

| ID | Descripción del Requerimiento Funcional |
| :--- | :--- |
| RQF-178 | El sistema debe permitir al administrador bloquear el acceso a una cuenta de usuario. |
| RQF-179 | El sistema debe permitir al administrador desbloquear una cuenta de usuario. |
| RQF-180 | El sistema debe permitir al administrador consultar el motivo de bloqueo de una cuenta. |
| RQF-181 | El sistema debe permitir al administrador ocultar una reseña reportada. |
| RQF-182 | El sistema debe exigir al administrador registrar un motivo al ocultar una reseña. |
| RQF-183 | El sistema debe permitir al administrador generar reportes de gestión de la plataforma. |
| RQF-184 | El sistema debe permitir al administrador consultar el historial de auditoría de un usuario filtrando por RUT. |
| RQF-185 | El sistema debe permitir al administrador exportar los registros de auditoría consultados. |
| RQF-212 | El sistema debe permitir al administrador buscar una cuenta de usuario. |
| RQF-236 | El sistema debe permitir al administrador consultar el listado de espacios publicados. |

---

## 3. 🗺️ Resumen: Actores por Módulo

| Módulo | RF base | RF complementarios | Total RF | Actores Primarios | Actores Externos | Casos de Uso |
|---|---|---|---|---|---|---|
| M01 — Autenticación y Gestión de Cuenta | 001–023 | 186–188, 213–218 | 32 | Visitante, Usuario Registrado | — | CU-01 … CU-06, CU-50 |
| M02 — Perfil y Privacidad del Usuario | 024–037 | 189–191 | 17 | Usuario Registrado | — | CU-07 … CU-09 |
| M03 — Verificación de Identidad (KYC/KYB) | 038–059 | 192–194, 219–220 | 27 | Usuario Registrado, Administrador | Registro Civil, SII | CU-10 … CU-14 |
| M04 — Gestión de Publicaciones | 060–093 | 195–198, 221–226 | 44 | Arrendador | — | CU-15 … CU-18 |
| M05 — Búsqueda y Cotización de Espacios | 094–107 | — | 14 | Visitante, Arrendatario | — | CU-19 … CU-21 |
| M06 — Reservas y Pagos (Escrow) | 108–129 | 199–201, 227–231 | 30 | Arrendatario, Arrendador | Mercado Pago | CU-22 … CU-28, CU-47, CU-51 |
| M07 — Contratos y Firma Electrónica | 130–142 | 202 | 14 | Arrendador, Arrendatario | FirmaVirtual | CU-29 … CU-32 |
| M08 — Check-in y Check-out | 143–152 | 203–206 | 14 | Arrendatario, Arrendador | — | CU-33, CU-34, CU-48 |
| M09 — Comunicación y Reputación | 153–158 | 207, 232–235 | 11 | Arrendatario, Arrendador, Visitante | — | CU-35 … CU-38, CU-49 |
| M10 — Disputas, Payout y Facturación | 159–177 | 208–211 | 23 | Arrendador, Arrendatario, Administrador | Mercado Pago | CU-39 … CU-42 |
| M11 — Administración y Auditoría | 178–185 | 212, 236 | 10 | Administrador | — | CU-43 … CU-46 |
| **Total** | **185** | **51** | **236** | — | — | **51** |

---

## 4. 📊 Estadísticas del Catálogo

| Métrica | Valor |
|---|---|
| Total de Requerimientos Funcionales | **236** (185 base RQF-001 – RQF-185 + 27 complementarios de la 1.ª revisión + 24 complementarios de la 2.ª revisión, RQF-186 – RQF-236), sin duplicados |
| Total de Módulos funcionales | **11** |
| Total de Requerimientos No Funcionales | **43** (anexo aparte, clasificados en 11 categorías con al menos 3 requerimientos por categoría) |
| Total de Casos de Uso | **52** (CU-01 – CU-52, ver `anexo_casos_de_uso.md`) |
| Actores Primarios | **5** (Visitante, Usuario Registrado, Arrendador, Arrendatario, Administrador) |
| Actores Secundarios (sistemas externos) | **4** (Registro Civil, SII, Mercado Pago, FirmaVirtual) |
| Módulo con más RF | M04 — Gestión de Publicaciones (44 RF) |
| Módulo con menos RF | M11 — Administración y Auditoría (10 RF) |
| Promedio de RF por módulo | 21,5 |

**Distribución de RF por módulo**

```text
M01 Autenticación y Cuenta      ████████████████████████████████ 32
M02 Perfil y Privacidad         █████████████████ 17
M03 Identidad KYC/KYB           ███████████████████████████ 27
M04 Publicaciones               ████████████████████████████████████████████ 44
M05 Búsqueda y Cotización       ██████████████ 14
M06 Reservas y Pagos            ██████████████████████████████ 30
M07 Contratos y Firma           ██████████████ 14
M08 Check-in y Check-out        ██████████████ 14
M09 Comunicación y Reputación   ███████████ 11
M10 Disputas, Payout y Boleta   ███████████████████████ 23
M11 Administración y Auditoría  ██████████ 10
                                                     Total: 236
```

---

## 5. 🔁 Control de Cambios respecto de la versión anterior (220 RF / 11 módulos)

| Cambio aplicado | Detalle |
|---|---|
| **Catálogo base** | Se abandona el catálogo de 220 RF y se adopta como fuente única el catálogo validado de **185 RF** del anexo vigente. |
| **IDs** | Se conservan los IDs y textos del anexo vigente (RQF-001…RQF-185). **No se renumeró nada**, por lo que la trazabilidad con el anexo de RF, las HU y los CU se mantiene por ID. |
| **Requerimiento "encriptar contraseña"** | Deja de ser RF y pasa al catálogo RNF como `RNF-013` (Seguridad / Confidencialidad, bcrypt ≥ 12 rounds). No genera caso de uso. |
| **Datos de tarjeta (PAN/CVV) como RF** | Se eliminan del catálogo funcional: el sistema no captura datos de tarjeta directamente, se opera con tokenización según `RNF-025` (PCI-DSS). |
| **Envío/almacenamiento de logs hacia el Data Warehouse** | Deja de ser RF y se cubre con `RNF-017` (inmutabilidad e integridad). Se mantiene como función solo la consulta y exportación de evidencia para el administrador (RQF-184, RQF-185). |
| **Módulos** | Los 11 módulos se reconstruyeron sobre los 185 RF base (rangos contiguos, sin solapamiento) y posteriormente absorben los 51 RF complementarios, cubriendo **236/236** requerimientos sin duplicar ninguno entre módulos. |
| **Actores** | Se retira **BigQuery** como actor y se documentan las exclusiones. Se mantienen 5 actores primarios y 4 sistemas externos. |
| **Trazabilidad** | Cada módulo declara sus actores y sus casos de uso; cada caso de uso declara su rango de RF (ver `anexo_casos_de_uso.md`, sección de trazabilidad). |
| **Requerimientos complementarios (revisión de completitud)** | Se agregaron **27 RF nuevos (RQF-186 a RQF-212)** al final del catálogo para cerrar brechas detectadas entre los RF, el contexto narrativo, las Historias de Usuario y los casos de uso. Ningún ID previo fue renumerado ni modificado, por lo que la trazabilidad existente se mantiene intacta. |
| **Requerimientos complementarios (2.ª revisión, Historias de Usuario)** | Tras revisar íntegramente las 30 HU se agregaron **24 RF (RQF-213 a RQF-236)** para respaldar criterios que no tenían requerimiento, y se corrigieron las HU para eliminar contradicciones numéricas, unificar la terminología de actores y declarar explícitamente lo que queda fuera del alcance de la ES1. |

### Brechas cerradas en la 1.ª revisión de completitud (RF y casos de uso)

1. **Liberación de la garantía en el flujo sin reclamos** → `RQF-208`, integrado al caso de uso CU-42 (Ejecutar Payout y Emitir Boleta de Comisión).
2. **Acción del arrendador al término de la reserva** → `RQF-205` y `RQF-206`, que dan origen al caso de uso **CU-48 (Confirmar Recepción del Espacio)** en M08.
3. **Seguimiento de las reservas por parte del usuario** → `RQF-199`, que da origen al caso de uso **CU-47 (Consultar Historial de Reservas)** en M06.
4. **Origen del reporte de reseñas** → `RQF-207`, que da origen al caso de uso **CU-49 (Reportar Reseña)** en M09.
5. **Aceptación de términos y condiciones** (ejemplo explícito de la retroalimentación de la profesora) → `RQF-186` y `RQF-187`, integrados a CU-01.
6. **CRUD incompleto sobre entidades** (cuenta bancaria, campos editables de la publicación, estado de la validación de identidad) → `RQF-189` a `RQF-193` y `RQF-195` a `RQF-198`.
7. **Obligatoriedad de evidencia fotográfica** en Check-in y Check-out → `RQF-203` y `RQF-204`.

### Brechas cerradas en la 2.ª revisión (Historias de Usuario)

1. **Preferencia de uso en el registro** (HU01) → `RQF-213`.
2. **Cambio de contraseña con sesión iniciada** y sus validaciones (HU03): `RQF-214` a `RQF-218`.
3. **Límite de peso de los documentos KYC** y estado "Pendiente de Verificación" (HU04) → `RQF-219`, `RQF-220`.
4. **Validación de la tarifa al modificar** una publicación (HU06) → `RQF-221`.
5. **Reglas de uso de 250 caracteres**, **política de cancelación** configurable y su publicación en el detalle (HU07) → `RQF-222`, `RQF-223`, `RQF-224`.
6. **Motivo obligatorio y validación de fechas en el bloqueo manual** del calendario (HU21) → `RQF-225`, `RQF-226`.
7. **Exigencia de identidad verificada antes de pagar** (HU17) → `RQF-227`.
8. **Cancelación de la reserva por el arrendatario** con cálculo de devolución, reembolso y notificación (HU19) → `RQF-228` a `RQF-231`.
9. **Reputación recíproca**: calificación y reseña del arrendatario entre pares, una reseña por reserva y promedio del espacio (HU25) → `RQF-232` a `RQF-235`.
10. **Listado de espacios publicados** para el administrador (HU26) → `RQF-236`.

### Observaciones abiertas (no bloqueantes)

1. **Solapamiento RF/RNF resuelto:** `RNF-027` se reformuló para expresar únicamente el cumplimiento normativo (timbrado del SII, formatos XML/PDF y plazo máximo de 24 horas), dejando la acción funcional en `RQF-176` y `RQF-211`. En la misma revisión se corrigieron los RNF que contenían verbos funcionales (RNF-002, RNF-003, RNF-004) y se separaron los que mezclaban dos condiciones (RNF-012 y RNF-018). El catálogo de RNF quedó en **43 requerimientos**, con al menos 3 por categoría.
2. **Alcance declarado formalmente:** las funcionalidades identificadas como fuera de alcance (HU24 y HU29, además de favoritos, adicionales con tarifa, estadísticas del arrendador, notificaciones dentro de la aplicación, 2FA de administrador, tablero de métricas globales y moderación de anuncios) quedaron registradas en la sección **Alcance y restricciones** del informe. Si el equipo decide incorporarlas, corresponden nuevos RF, casos de uso e historias de usuario.
3. **Contexto narrativo actualizado:** se incorporaron al relato la cancelación de la reserva por el arrendatario y la confirmación de recepción del arrendador (`RQF-205`, `RQF-206`), en coherencia con los requerimientos y casos de uso.
