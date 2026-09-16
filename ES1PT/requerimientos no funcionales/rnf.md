# Requerimientos No Funcionales — EspaciGo
## Sistema: EspaciGo — Marketplace SaaS B2B2C de Espacios Comerciales
### Actividad 7: Levantamiento de Requerimientos No Funcionales

> **Convención de ID:** `RNF-###` (Requerimiento No Funcional).
> **Regla de Oro:** Está estrictamente prohibido usar términos ambiguos como "fácil", "rápido", "seguro" o "robusto". Todos los requerimientos contienen **métricas exactas y verificables** por el equipo de QA.

---

## PARTE 1: Clasificación ISO 25010 — Características de Calidad del Producto

---

### 1.1 Rendimiento (3 RNF)

---

#### RNF-001 — Tiempo de respuesta del motor de búsqueda

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-001 |
| **Nombre de requerimiento** | Tiempo de respuesta del motor de búsqueda de espacios |
| **Categoría / Subcategoría** | Rendimiento / Comportamiento temporal |
| **Descripción (redacción del requerimiento)** | El sistema debe retornar los resultados de búsqueda y filtrado de publicaciones de espacios comerciales en un tiempo máximo de **2 segundos** para consultas sobre un catálogo de hasta **10.000 publicaciones activas**, medido desde que el usuario confirma los parámetros de búsqueda hasta que los resultados son visibles en pantalla, bajo una carga simultánea de hasta **200 usuarios concurrentes**. |

---

#### RNF-002 — Tiempo de procesamiento de transacción Escrow

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-002 |
| **Nombre de requerimiento** | Tiempo de procesamiento del flujo de pago Escrow |
| **Categoría / Subcategoría** | Rendimiento / Comportamiento temporal |
| **Descripción (redacción del requerimiento)** | El sistema debe completar el ciclo completo del flujo de pago Escrow (desde que el usuario presiona "Confirmar Pago" hasta que el sistema recibe la confirmación de la pasarela Mercado Pago y actualiza el estado de la reserva a "Pagada_Escrow") en un tiempo máximo de **8 segundos** bajo condiciones de red normales (latencia API < 300ms). Si la respuesta de la pasarela no llega en ese plazo, el sistema debe mostrar al usuario un mensaje de estado y continuar verificando por hasta **30 segundos adicionales** antes de abortar la transacción. |

---

#### RNF-003 — Tiempo de generación del contrato PDF

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-003 |
| **Nombre de requerimiento** | Tiempo de generación y envío del contrato PDF al proveedor de firma |
| **Categoría / Subcategoría** | Rendimiento / Comportamiento temporal |
| **Descripción (redacción del requerimiento)** | El sistema debe completar el proceso de generación del contrato PDF (compilación de la plantilla HTML con datos de las partes y del inmueble, exportación a PDF y envío al proveedor FirmaVirtual) en un tiempo máximo de **10 segundos** desde que el Arrendador aprueba la reserva. El contrato generado no debe superar los **2 MB** de tamaño para garantizar la entrega exitosa dentro de los límites de la API de FirmaVirtual. |

---

### 1.2 Usabilidad — Capacidad de Interacción (3 RNF)

---

#### RNF-004 — Pasos para completar una reserva

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-004 |
| **Nombre de requerimiento** | Acceso a la funcionalidad de reserva en pocos pasos |
| **Categoría / Subcategoría** | Usabilidad / Capacidad de interacción (Operabilidad) |
| **Descripción (redacción del requerimiento)** | El sistema debe permitir al usuario Arrendatario completar el proceso de reserva de un espacio comercial (desde la selección del espacio hasta la confirmación del pago) realizando un máximo de **7 interacciones** (clics, selecciones o ingreso de datos en formulario), sin necesidad de navegar más de **3 niveles de profundidad** desde el menú principal, medido en sesiones con usuarios representativos bajo protocolo de prueba de usabilidad. |

---

#### RNF-005 — Mensajes de error comprensibles

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-005 |
| **Nombre de requerimiento** | Retroalimentación visual ante errores de validación de formularios |
| **Categoría / Subcategoría** | Usabilidad / Capacidad de interacción (Reconocimiento de errores) |
| **Descripción (redacción del requerimiento)** | El sistema debe mostrar un mensaje de error descriptivo y específico junto al campo de formulario que no cumple la validación (por ejemplo: "La contraseña debe contener al menos 8 caracteres, una mayúscula y un número") dentro de los **500 milisegundos** siguientes al evento que desencadenó la validación (submit o blur del campo), sin recargar la página. El mensaje de error no debe tener más de **120 caracteres** y debe estar redactado en idioma español. |

---

#### RNF-006 — Diseño responsivo para dispositivos móviles

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-006 |
| **Nombre de requerimiento** | Compatibilidad de la interfaz con resoluciones de dispositivos móviles |
| **Categoría / Subcategoría** | Usabilidad / Estética de la interfaz de usuario (Adaptabilidad visual) |
| **Descripción (redacción del requerimiento)** | El sistema debe renderizar todas sus vistas sin pérdida de funcionalidad ni elementos visuales truncados o superpuestos en dispositivos con resoluciones de pantalla de **375px de ancho mínimo** (equivalente a iPhone SE) hasta **1920px de ancho** (escritorio Full HD). El layout debe reorganizarse automáticamente utilizando diseño responsivo (CSS Bootstrap Grid o equivalente), garantizando que los botones de acción principal (Reservar, Pagar, Firmar) sean clickeables en pantallas táctiles con un área mínima de **44x44 píxeles**, según las guías WCAG 2.1. |

---

### 1.3 Compatibilidad (2 RNF)

---

#### RNF-007 — Compatibilidad de navegadores web

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-007 |
| **Nombre de requerimiento** | Compatibilidad con versiones mínimas de navegadores web |
| **Categoría / Subcategoría** | Compatibilidad / Coexistencia e Interoperabilidad |
| **Descripción (redacción del requerimiento)** | El sistema debe ejecutarse correctamente y renderizar todas sus vistas sin errores funcionales ni de presentación en las siguientes versiones de navegadores: **Google Chrome versión 40 o superior**, **Mozilla Firefox versión 32 o superior**, **Microsoft Edge versión 18 o superior** y **Safari versión 12 o superior**. La compatibilidad debe validarse mediante pruebas automatizadas de cross-browser en los sistemas operativos Windows 10, macOS Monterey y Android 10. |

---

#### RNF-008 — Interoperabilidad con APIs externas

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-008 |
| **Nombre de requerimiento** | Tolerancia a degradación de servicios API externos |
| **Categoría / Subcategoría** | Compatibilidad / Interoperabilidad |
| **Descripción (redacción del requerimiento)** | El sistema debe establecer un tiempo de espera (timeout) máximo de **5 segundos** para cada llamada hacia las APIs externas: Registro Civil (KYC), SII (KYB), Mercado Pago (pagos) y FirmaVirtual (contratos). Si la API externa no responde dentro de ese plazo, el sistema debe: (1) registrar el error en el log de auditoría con timestamp, nombre de la API y código de respuesta, y (2) presentar al usuario un mensaje indicando que el servicio no está disponible temporalmente, sin exponer detalles técnicos internos. El sistema debe reintentar la llamada automáticamente hasta **2 veces** con un intervalo de **2 segundos** entre reintentos antes de considerar el servicio como caído. |

---

### 1.4 Fiabilidad (3 RNF)

---

#### RNF-009 — Disponibilidad del módulo de pagos

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-009 |
| **Nombre de requerimiento** | Disponibilidad continua del servicio de pagos Escrow |
| **Categoría / Subcategoría** | Fiabilidad / Disponibilidad |
| **Descripción (redacción del requerimiento)** | El sistema debe garantizar una disponibilidad mínima del **99,5%** mensual (equivalente a un máximo de **3 horas y 39 minutos** de tiempo de inactividad no planificado por mes) para el módulo de Reservas y Pagos (M06). En caso de fallo del servicio de la pasarela de pago externa (Mercado Pago), el sistema debe detectar el error en un máximo de **5 segundos**, notificar al usuario con un mensaje descriptivo y reintentar la transacción de forma automática hasta **3 veces** antes de abortar la operación. |

---

#### RNF-010 — Recuperabilidad ante fallos (Disaster Recovery)

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-010 |
| **Nombre de requerimiento** | Respaldo y recuperación de la base de datos ante fallo catastrófico |
| **Categoría / Subcategoría** | Fiabilidad / Recuperabilidad |
| **Descripción (redacción del requerimiento)** | El sistema debe ejecutar respaldos automáticos de la base de datos SQL Server con una frecuencia mínima de **una vez cada 24 horas** para respaldos completos y cada **4 horas** para respaldos incrementales. Los respaldos deben almacenarse en un repositorio físicamente separado del servidor de producción. El sistema debe poder ser restaurado íntegramente a partir de los respaldos con un **RPO (Recovery Point Objective) máximo de 4 horas** y un **RTO (Recovery Time Objective) máximo de 6 horas**, medidos desde la declaración formal del incidente hasta la reanudación del servicio en producción. |

---

#### RNF-011 — Integridad transaccional

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-011 |
| **Nombre de requerimiento** | Consistencia transaccional en flujos de pago y cambio de estado de reserva |
| **Categoría / Subcategoría** | Fiabilidad / Madurez (Tolerancia a fallos) |
| **Descripción (redacción del requerimiento)** | El sistema debe garantizar la atomicidad de todas las operaciones que involucren simultáneamente el cambio de estado de una reserva y una operación financiera (pago, reembolso, payout). Si ocurre un fallo en cualquier paso de la transacción compuesta (por ejemplo, la pasarela confirma el pago pero la actualización del estado en la base de datos falla), el sistema debe ejecutar un mecanismo de reversión automática (rollback) que deje la base de datos en el estado anterior al inicio de la operación, registrando el incidente en el log de errores. En ningún caso el sistema debe quedar en un estado donde se haya cobrado al usuario sin que la reserva refleje el estado "Pagada_Escrow". |

---

### 1.5 Seguridad (4 RNF)

---

#### RNF-012 — Almacenamiento de contraseñas

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-012 |
| **Nombre de requerimiento** | Almacenamiento de contraseñas con algoritmo de hash irreversible |
| **Categoría / Subcategoría** | Seguridad / Confidencialidad |
| **Descripción (redacción del requerimiento)** | El sistema debe almacenar todas las contraseñas de usuario en la base de datos exclusivamente en formato de hash irreversible, utilizando el algoritmo **bcrypt** con un factor de costo (cost factor) mínimo de **12 rounds**. Ningún componente del sistema debe registrar ni transmitir la contraseña en texto plano en logs, correos electrónicos ni respuestas de API. El cumplimiento es verificable mediante inspección directa de la base de datos, confirmando que ningún registro en la tabla de usuarios contiene un campo de contraseña en texto legible. |

---

#### RNF-013 — Cifrado de datos bancarios en reposo

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-013 |
| **Nombre de requerimiento** | Cifrado de datos bancarios sensibles almacenados en la base de datos |
| **Categoría / Subcategoría** | Seguridad / Confidencialidad |
| **Descripción (redacción del requerimiento)** | El sistema debe almacenar los datos bancarios del usuario (número de cuenta, RUT del titular, banco asociado) en la base de datos en formato cifrado utilizando el algoritmo **AES-256** con clave gestionada por un servicio de gestión de claves separado del servidor de base de datos. Los datos bancarios no deben almacenarse nunca en texto plano. El proceso de cifrado y descifrado debe ser transparente para la capa de negocio y debe completarse en un tiempo máximo de **100 milisegundos** por operación. |

---

#### RNF-014 — Expiración de sesión por inactividad

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-014 |
| **Nombre de requerimiento** | Invalidación automática de sesión por inactividad del usuario |
| **Categoría / Subcategoría** | Seguridad / Autenticidad |
| **Descripción (redacción del requerimiento)** | El sistema debe invalidar automáticamente la credencial temporal de sesión del usuario (token de sesión) si no se registra ninguna actividad por parte de éste durante un periodo de **30 minutos** continuos. Tras la expiración, el sistema debe redirigir al usuario a la pantalla de inicio de sesión y descartar cualquier operación pendiente no confirmada. La duración máxima absoluta de una sesión activa, independientemente de la actividad, no debe superar las **8 horas**, tras lo cual el sistema debe exigir una nueva autenticación. |

---

#### RNF-015 — Protección de documentos legales firmados

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-015 |
| **Nombre de requerimiento** | Cifrado y control de acceso a los contratos PDF firmados digitalmente |
| **Categoría / Subcategoría** | Seguridad / No repudio e Integridad |
| **Descripción (redacción del requerimiento)** | El sistema debe cifrar cada contrato PDF firmado y certificado utilizando el algoritmo **AES-256** antes de almacenarlo en el repositorio de archivos. El acceso al documento debe realizarse exclusivamente mediante **URLs firmadas temporales** con expiración de **15 minutos**, generadas bajo demanda por el sistema en respuesta a una solicitud autenticada del Arrendador o Arrendatario involucrado en esa reserva específica. Ningún usuario, incluido el Administrador, debe poder acceder al contrato de otro usuario mediante una URL directa permanente. El hash SHA-256 del documento debe calcularse al momento del almacenamiento y verificarse en cada descarga para garantizar su integridad. |

---

### 1.6 Flexibilidad (2 RNF)

---

#### RNF-016 — Escalabilidad horizontal

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-016 |
| **Nombre de requerimiento** | Escalabilidad horizontal del servicio de publicaciones ante aumento de carga |
| **Categoría / Subcategoría** | Flexibilidad / Escalabilidad |
| **Descripción (redacción del requerimiento)** | El sistema debe soportar un incremento del **200%** en la carga de usuarios concurrentes (de 200 a 600 usuarios simultáneos) en el módulo de Búsqueda y Exploración (M05) mediante el despliegue de instancias adicionales de la capa de aplicación, sin requerir cambios en el código fuente ni modificaciones en el esquema de la base de datos. El tiempo de incorporación de una nueva instancia no debe superar los **10 minutos** desde que se detecta el umbral de saturación. |

---

#### RNF-017 — Configurabilidad de parámetros de negocio

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-017 |
| **Nombre de requerimiento** | Modificación de parámetros de negocio sin redespliegue de la aplicación |
| **Categoría / Subcategoría** | Flexibilidad / Modificabilidad |
| **Descripción (redacción del requerimiento)** | El sistema debe permitir que los siguientes parámetros de negocio sean modificables por el Administrador a través del panel de configuración, sin necesidad de recompilar ni redesplegar el archivo .WAR de la aplicación: (1) porcentaje de comisión de servicio EspaciGo (valor actual configurable entre **1% y 30%**), (2) tiempo de espera para aprobar/rechazar reserva (valor actual: **24 horas**, configurable entre 12 y 72 horas), y (3) tiempo de bloqueo de cuenta por intentos fallidos (valor actual: **30 minutos**, configurable entre 15 y 120 minutos). Los cambios deben aplicarse en un plazo máximo de **60 segundos** sin reinicio del servidor. |

---

### 1.7 Mantenibilidad (2 RNF)

---

#### RNF-018 — Cobertura de pruebas unitarias

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-018 |
| **Nombre de requerimiento** | Cobertura mínima de pruebas unitarias automatizadas |
| **Categoría / Subcategoría** | Mantenibilidad / Analizabilidad y Testeabilidad |
| **Descripción (redacción del requerimiento)** | El sistema debe mantener una cobertura de pruebas unitarias automatizadas mínima del **80%** sobre la capa de negocio (clases de servicio y lógica de dominio), medida con la herramienta **JaCoCo** integrada en el pipeline de integración continua. El pipeline debe fallar automáticamente si la cobertura desciende por debajo de dicho umbral en cualquier módulo crítico: M06 (Pagos), M07 (Contratos) y M09 (Disputas). |

---

#### RNF-019 — Registro de errores de la aplicación

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-019 |
| **Nombre de requerimiento** | Sistema de registro y rotación de logs de error de la aplicación |
| **Categoría / Subcategoría** | Mantenibilidad / Analizabilidad |
| **Descripción (redacción del requerimiento)** | El sistema debe registrar automáticamente en un archivo de log estructurado (formato **Log4j**) todos los errores de nivel ERROR y FATAL que ocurran en la capa de negocio e integración, incluyendo: timestamp en formato ISO-8601, módulo de origen, tipo de excepción, mensaje descriptivo y stack trace completo. El archivo de log debe aplicar rotación automática cuando alcance un tamaño de **50 MB**, conservando los últimos **30 archivos** de log históricos (equivalente a un mínimo de **90 días** de trazabilidad en condiciones normales de operación). Los logs no deben contener datos personales ni credenciales en texto plano. |

---

### 1.8 Portabilidad (2 RNF)

---

#### RNF-020 — Instalabilidad en entorno de servidor

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-020 |
| **Nombre de requerimiento** | Empaquetado e instalación del sistema en entorno de servidor de producción |
| **Categoría / Subcategoría** | Portabilidad / Instalabilidad |
| **Descripción (redacción del requerimiento)** | El sistema debe poder ser desplegado íntegramente en un servidor que ejecute **Oracle Linux 6.0 o 5.0** sobre hardware Intel Server mediante la ejecución de un único script de instalación automatizada, sin intervención manual adicional. El proceso completo de despliegue desde cero (incluida la configuración del servidor de aplicaciones JBoss 6.0.1 y la inicialización del esquema de base de datos en SQL Server) no debe exceder los **30 minutos** en condiciones de red corporativa estándar (velocidad de descarga mínima de 10 Mbps). |

---

#### RNF-021 — Capacidad de almacenamiento de archivos multimedia

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-021 |
| **Nombre de requerimiento** | Capacidad del repositorio de almacenamiento de archivos multimedia |
| **Categoría / Subcategoría** | Portabilidad / Capacidad de reemplazamiento |
| **Descripción (redacción del requerimiento)** | El repositorio de archivos del sistema (imágenes de publicaciones, fotografías de Check-in, contratos PDF) debe estar diseñado para almacenar un mínimo de **100.000 publicaciones activas**, considerando un promedio de **10 imágenes por publicación** de hasta **5 MB** cada una, más los contratos PDF de hasta **2 MB** por reserva, lo que representa una capacidad mínima planificada de **6 TB** de almacenamiento bruto. El sistema de archivos debe soportar una tasa de lectura concurrente de hasta **500 peticiones simultáneas** sin degradación de velocidad de descarga por debajo de **5 MB/s** por sesión. |

---

## PARTE 2: Clasificación de Sommerville — Tipos de Requerimientos No Funcionales

---

### 2.1 Requerimiento de Entrega

---

#### RNF-022 — Formato y medio de entrega del sistema

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-022 |
| **Nombre de requerimiento** | Formato y medio de entrega del sistema |
| **Categoría / Subcategoría** | Requerimientos de Proceso / Entrega |
| **Descripción (redacción del requerimiento)** | El sistema debe ser entregado al cliente en forma de un paquete desplegable compuesto por: (1) un archivo `.WAR` ejecutable sobre JBoss 6.0.1, (2) un script SQL de inicialización y migración de la base de datos compatible con **SQL Server 2014 o superior**, y (3) un manual de instalación en formato PDF de un máximo de **20 páginas**. La entrega debe realizarse a través del repositorio de código fuente corporativo (GitHub) en una rama etiquetada como `release/v1.0`, con al menos **72 horas de anticipación** a la fecha de puesta en producción acordada, incluyendo un archivo CHANGELOG.md con la descripción de todos los cambios incluidos en la versión. |

---

### 2.2 Requerimiento de Implementación

---

#### RNF-023 — Stack tecnológico obligatorio

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-023 |
| **Nombre de requerimiento** | Stack tecnológico obligatorio de la plataforma |
| **Categoría / Subcategoría** | Requerimientos de Proceso / Implementación |
| **Descripción (redacción del requerimiento)** | El sistema debe ser implementado respetando **obligatoriamente** la siguiente arquitectura tecnológica por capas: **(1) Capa Cliente:** HTML5, Bootstrap y CSS, compatible con Mozilla Firefox >= 32 y Google Chrome >= 40. **(2) Capa de Presentación y Control:** Spring MVC con JSP 2.5 y Servlet 3.0, desplegado sobre el servidor de aplicaciones **JBoss 6.0.1**. **(3) Capa de Negocio:** Clases POJO gestionadas mediante el framework **Spring 3.0.3**. **(4) Capa de Integración a Datos:** **JPA 2.1** con implementación **Hibernate 3**. **(5) Capa de Datos:** Motor de base de datos **SQL Server** ejecutándose sobre **Oracle Linux 6.0 / 5.0** en hardware Intel Server. El uso de cualquier tecnología no contemplada en esta matriz requiere aprobación formal del Comité de Arquitectura mediante documento escrito. |

---

### 2.3 Requerimiento de Estándares (2 RNF)

---

#### RNF-024 — Estándar de codificación y documentación

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-024 |
| **Nombre de requerimiento** | Estándar de codificación y documentación del código fuente |
| **Categoría / Subcategoría** | Requerimientos de Proceso / Estándares |
| **Descripción (redacción del requerimiento)** | El sistema debe ser desarrollado bajo el estándar de codificación **Sun Java Coding Conventions** (revisión vigente). Todo método o clase pública del código fuente debe incluir documentación **Javadoc** con descripción, parámetros (@param) y valor de retorno (@return). El incumplimiento de estas convenciones debe ser detectado automáticamente por la herramienta **Checkstyle** integrada en el proceso de compilación, el cual debe generar un error de build si se superan los **5 warnings** de estilo por clase. Adicionalmente, el control de versiones del código fuente debe seguir el flujo de trabajo **Git Flow**, con ramas nombradas según el estándar feature/, release/ y hotfix/. |

---

#### RNF-025 — Estándar PCI-DSS para manejo de datos de tarjetas

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-025 |
| **Nombre de requerimiento** | Cumplimiento del estándar PCI-DSS en el tratamiento de datos de tarjetas de pago |
| **Categoría / Subcategoría** | Requerimientos de Proceso / Estándares |
| **Descripción (redacción del requerimiento)** | El sistema no debe almacenar, en ninguna capa de la aplicación ni en la base de datos, los datos completos de tarjetas de pago del usuario (número de tarjeta PAN, CVV/CVC ni fecha de expiración). El procesamiento de datos de tarjeta debe realizarse **exclusivamente** a través del SDK oficial de Mercado Pago, que tokeniza los datos en el dispositivo del usuario antes de transmitirlos, de modo que el servidor de EspaciGo solo reciba un token opaco. El cumplimiento de este requerimiento debe ser verificable mediante análisis estático del código fuente, confirmando la ausencia de campos de tipo VARCHAR que contengan patrones de número de tarjeta (16 dígitos) en cualquier tabla de la base de datos. |

---

### 2.4 Requerimientos Legislativos (2 RNF)

---

#### RNF-026 — Protección de datos Ley 21.719

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-026 |
| **Nombre de requerimiento** | Protección de datos personales conforme a la Ley 21.719 |
| **Categoría / Subcategoría** | Requerimientos Externos / Legislativos |
| **Descripción (redacción del requerimiento)** | El sistema debe cumplir íntegramente con los preceptos de la **Ley N° 21.719 de Protección de Datos Personales de Chile** (vigente desde 2024). En cumplimiento de lo anterior: (1) El sistema debe permitir al usuario solicitar la **eliminación irreversible** de sus datos personales (nombre, RUT, teléfono, correo, cuenta bancaria) en un plazo máximo de **72 horas** desde la recepción de la solicitud, siempre que no existan transacciones o disputas activas; (2) El sistema debe registrar en un log de auditoría inmutable **100% de los accesos** realizados sobre datos personales sensibles (RUT, cédula de identidad, datos bancarios), conservando dicho registro por un mínimo de **5 años**; (3) Los datos personales de usuarios que no hayan accedido a la plataforma en los últimos **24 meses** deben ser anonimizados automáticamente mediante un proceso programado de ejecución mensual. |

---

#### RNF-027 — Emisión de boleta electrónica conforme al SII

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-027 |
| **Nombre de requerimiento** | Generación de boleta electrónica conforme a normativa del SII Chile |
| **Categoría / Subcategoría** | Requerimientos Externos / Legislativos |
| **Descripción (redacción del requerimiento)** | El sistema debe generar las boletas electrónicas correspondientes a la comisión de servicio cobrada por EspaciGo en cada transacción completada, cumpliendo íntegramente la normativa del **Servicio de Impuestos Internos (SII) de Chile** para Documentos Tributarios Electrónicos (DTE), incluyendo: (1) la boleta debe generarse en formato **XML estructurado** firmado digitalmente con certificado tributario vigente; (2) debe ser timbrada mediante el servicio web del SII dentro de las **24 horas** siguientes a la confirmación de la transacción; (3) el documento en formato PDF debe enviarse al correo electrónico del Arrendatario en un plazo máximo de **1 hora** tras obtener el timbre electrónico del SII. |

---

### 2.5 Requerimientos complementarios de calidad

#### RNF-028 — Disponibilidad global del sistema

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-028 |
| **Nombre de requerimiento** | Disponibilidad global de la plataforma |
| **Categoría / Subcategoría** | Fiabilidad / Disponibilidad |
| **Descripción (redacción del requerimiento)** | El sistema debe mantener una disponibilidad mensual mínima de **99,9%** para las funciones de autenticación, búsqueda, reservas, contratos y consulta de operaciones, excluyendo mantenimientos programados comunicados con al menos **24 horas** de anticipación. |

#### RNF-029 — Cifrado de comunicaciones

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-029 |
| **Nombre de requerimiento** | Protección de comunicaciones y credenciales |
| **Categoría / Subcategoría** | Seguridad / Confidencialidad |
| **Descripción (redacción del requerimiento)** | El sistema debe transmitir credenciales, datos personales, datos bancarios, documentos y respuestas de APIs externas exclusivamente mediante **HTTPS con TLS 1.2 o superior**, rechazando protocolos y suites criptográficas consideradas débiles. Los tokens de sesión no deben enviarse mediante parámetros de URL. |

#### RNF-030 — Entrega de notificaciones

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-030 |
| **Nombre de requerimiento** | Disponibilidad y trazabilidad de notificaciones |
| **Categoría / Subcategoría** | Fiabilidad / Recuperabilidad |
| **Descripción (redacción del requerimiento)** | El sistema debe registrar cada notificación generada con destinatario, canal, fecha, estado y motivo de entrega. Para notificaciones por correo, debe iniciar el envío dentro de **60 segundos** desde el evento y reintentar hasta **3 veces** ante un error, conservando el resultado final del envío. |

#### RNF-031 — Idempotencia de operaciones externas

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-031 |
| **Nombre de requerimiento** | Idempotencia y conciliación de pagos y reembolsos |
| **Categoría / Subcategoría** | Fiabilidad / Integridad |
| **Descripción (redacción del requerimiento)** | El sistema debe asignar una clave de idempotencia única a cada pago, reembolso y transferencia, de modo que la recepción duplicada de una respuesta o webhook no genere más de una operación financiera. Los eventos sin confirmación definitiva deben conciliarse automáticamente al menos cada **5 minutos** y quedar registrados para revisión administrativa. |

#### RNF-032 — Trazabilidad administrativa

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-032 |
| **Nombre de requerimiento** | Registro de acciones administrativas |
| **Categoría / Subcategoría** | Seguridad / Responsabilidad |
| **Descripción (redacción del requerimiento)** | El sistema debe registrar el identificador del administrador, acción, recurso afectado, fecha, hora, dirección IP, resultado y motivo para toda acción de aprobación, rechazo, bloqueo, desbloqueo, modificación de parámetros o resolución de disputas. Estos registros no deben poder ser modificados desde la interfaz de administración. |

#### RNF-033 — Escritura de auditoría

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-033 |
| **Nombre de requerimiento** | Latencia máxima de registro de auditoría |
| **Categoría / Subcategoría** | Rendimiento / Comportamiento temporal |
| **Descripción (redacción del requerimiento)** | El sistema debe persistir cada evento de auditoría en un plazo máximo de **3 segundos** desde la confirmación de la operación que lo origina. Si el repositorio de auditoría no está disponible, el evento debe conservarse en una cola duradera para reintento sin bloquear la operación del usuario. |

#### RNF-034 — Eliminación y anonimización verificables

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-034 |
| **Nombre de requerimiento** | Trazabilidad de solicitudes de eliminación y anonimización |
| **Categoría / Subcategoría** | Externos / Legislativos |
| **Descripción (redacción del requerimiento)** | El sistema debe registrar cada solicitud de eliminación o anonimización con fecha de recepción, usuario, validaciones realizadas, decisión, fecha de ejecución y resultado. El proceso debe completarse dentro del plazo legal aplicable y no debe eliminar los registros transaccionales que deban conservarse por obligación legal; estos deben quedar anonimizados. |

#### RNF-035 — Recuperación de webhooks

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-035 |
| **Nombre de requerimiento** | Recepción y recuperación de eventos externos |
| **Categoría / Subcategoría** | Compatibilidad / Interoperabilidad |
| **Descripción (redacción del requerimiento)** | El sistema debe validar la autenticidad, identificador y fecha de cada webhook recibido desde Mercado Pago y FirmaVirtual, almacenarlo antes de procesarlo y reintentar su procesamiento hasta **5 veces** con intervalos crecientes. Un webhook repetido debe marcarse como duplicado y no debe cambiar nuevamente el estado de la operación. |

#### RNF-036 — Accesibilidad de controles principales

| Campo | Detalle |
|---|---|
| **Número de requerimiento** | RNF-036 |
| **Nombre de requerimiento** | Accesibilidad de los flujos principales |
| **Categoría / Subcategoría** | Usabilidad / Accesibilidad |
| **Descripción (redacción del requerimiento)** | Los flujos de registro, búsqueda, reserva, pago, firma y reclamo deben poder utilizarse mediante teclado, mantener un orden de foco visible y proporcionar etiquetas accesibles para controles y mensajes. La validación debe realizarse contra los criterios aplicables de **WCAG 2.1 nivel AA**. |

---

## Resumen del Catálogo de RNF

| ID | Nombre del Requerimiento | Categoría / Subcategoría | Estándar |
|---|---|---|---|
| **RNF-001** | Tiempo de respuesta del motor de búsqueda | Rendimiento / Comportamiento temporal | ISO 25010 |
| **RNF-002** | Tiempo de procesamiento del flujo de pago Escrow | Rendimiento / Comportamiento temporal | ISO 25010 |
| **RNF-003** | Tiempo de generación y envío del contrato PDF | Rendimiento / Comportamiento temporal | ISO 25010 |
| **RNF-004** | Acceso a funcionalidad de reserva en pocos pasos | Usabilidad / Operabilidad | ISO 25010 |
| **RNF-005** | Retroalimentación visual ante errores de validación | Usabilidad / Reconocimiento de errores | ISO 25010 |
| **RNF-006** | Compatibilidad con resoluciones de dispositivos móviles | Usabilidad / Adaptabilidad visual | ISO 25010 |
| **RNF-007** | Compatibilidad con versiones mínimas de navegadores | Compatibilidad / Interoperabilidad | ISO 25010 |
| **RNF-008** | Tolerancia a degradación de servicios API externos | Compatibilidad / Interoperabilidad | ISO 25010 |
| **RNF-009** | Disponibilidad continua del servicio de pagos Escrow | Fiabilidad / Disponibilidad | ISO 25010 |
| **RNF-010** | Respaldo y recuperación ante fallo catastrófico | Fiabilidad / Recuperabilidad | ISO 25010 |
| **RNF-011** | Consistencia transaccional en flujos de pago | Fiabilidad / Tolerancia a fallos | ISO 25010 |
| **RNF-012** | Almacenamiento de contraseñas con hash bcrypt | Seguridad / Confidencialidad | ISO 25010 |
| **RNF-013** | Cifrado AES-256 de datos bancarios en reposo | Seguridad / Confidencialidad | ISO 25010 |
| **RNF-014** | Invalidación automática de sesión por inactividad | Seguridad / Autenticidad | ISO 25010 |
| **RNF-015** | Cifrado y control de acceso a contratos PDF firmados | Seguridad / No repudio e Integridad | ISO 25010 |
| **RNF-016** | Escalabilidad horizontal del servicio de publicaciones | Flexibilidad / Escalabilidad | ISO 25010 |
| **RNF-017** | Modificación de parámetros de negocio sin redespliegue | Flexibilidad / Modificabilidad | ISO 25010 |
| **RNF-018** | Cobertura mínima de pruebas unitarias automatizadas | Mantenibilidad / Testeabilidad | ISO 25010 |
| **RNF-019** | Sistema de registro y rotación de logs de error | Mantenibilidad / Analizabilidad | ISO 25010 |
| **RNF-020** | Instalación del sistema en servidor de producción | Portabilidad / Instalabilidad | ISO 25010 |
| **RNF-021** | Capacidad del repositorio de archivos multimedia | Portabilidad / Capacidad | ISO 25010 |
| **RNF-022** | Formato y medio de entrega del sistema | Proceso / Entrega | Sommerville |
| **RNF-023** | Stack tecnológico obligatorio de la plataforma | Proceso / Implementación | Sommerville |
| **RNF-024** | Estándar de codificación y documentación | Proceso / Estándares | Sommerville |
| **RNF-025** | Cumplimiento PCI-DSS en datos de tarjetas de pago | Proceso / Estándares | Sommerville |
| **RNF-026** | Protección de datos conforme a Ley 21.719 | Externos / Legislativos | Sommerville |
| **RNF-027** | Boleta electrónica conforme a normativa SII Chile | Externos / Legislativos | Sommerville |
| **RNF-028** | Disponibilidad global de la plataforma | Fiabilidad / Disponibilidad | ISO 25010 |
| **RNF-029** | Protección de comunicaciones y credenciales | Seguridad / Confidencialidad | ISO 25010 |
| **RNF-030** | Disponibilidad y trazabilidad de notificaciones | Fiabilidad / Recuperabilidad | ISO 25010 |
| **RNF-031** | Idempotencia y conciliación de pagos y reembolsos | Fiabilidad / Integridad | ISO 25010 |
| **RNF-032** | Registro de acciones administrativas | Seguridad / Responsabilidad | ISO 25010 |
| **RNF-033** | Latencia máxima de registro de auditoría | Rendimiento / Comportamiento temporal | ISO 25010 |
| **RNF-034** | Trazabilidad de solicitudes de eliminación y anonimización | Externos / Legislativos | Sommerville |
| **RNF-035** | Recepción y recuperación de eventos externos | Compatibilidad / Interoperabilidad | ISO 25010 |
| **RNF-036** | Accesibilidad de los flujos principales | Usabilidad / Accesibilidad | ISO 25010 |

**Total: 36 Requerimientos No Funcionales**
- ISO 25010 y calidad del producto: 29 RNF
- Sommerville y requisitos externos/de proceso: 7 RNF

---

> *Para mayor detalle sobre los requerimientos funcionales asociados al sistema, ver Anexo C con la totalidad de los RQF (220 requerimientos).*
