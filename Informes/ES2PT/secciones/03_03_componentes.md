## Diagrama de componentes

El diseño inicial mantiene la unidad de despliegue modular definida en ES1. Los módulos del backend son responsabilidades de software, no microservicios independientes. Las llamadas a proveedores se concentran en adaptadores para que su contrato y sus fallos puedan tratarse de forma explícita.

![Componentes lógicos del backend modular](imagenes/figura-componentes_flujos.png){width=6.3in} <!--#fig:es2-componentes-flujos--> <!--#fuente:elaboración propia a partir de ES1.-->

![Interfaces de persistencia y proveedores previstas](imagenes/figura-componentes_integraciones.png){width=6.3in} <!--#fig:es2-componentes-integraciones--> <!--#fuente:elaboración propia a partir de ES1.-->

*Tabla. Responsabilidades e interfaces previstas.* <!--#tab:es2-componentes-interfaces-->

| Componente | Responsabilidad | Interfaz o dependencia propuesta |
| --- | --- | --- |
| Presentación Next.js | Interacción y visualización | HTTPS/JSON hacia API; no acceso directo a credenciales de proveedores |
| API y autorización | Entrada, validación y control de permisos | Contrato OpenAPI requerido por RNF-032 |
| Identidad/perfiles M01–M03 | Cuenta, roles y solicitudes de verificación | Persistencia y adaptador de identidad |
| Oferta/búsqueda M04–M05 | Publicación, ubicación, tarifas y consulta | PostgreSQL/PostGIS y calendario |
| Reservas/contratos M06–M07 | Estado transaccional, pagos y formalización | Persistencia, pago, firma y archivos |
| Operación/reputación M08–M09 | Evidencias de uso y relación entre partes | Reserva y almacenamiento |
| Disputas/liquidación M10 | Fallo y cierre financiero | Pago, garantía y servicio tributario |
| Administración/auditoría M11 | Supervisión y consulta de acciones | Datos operativos y repositorio de eventos |
| Conciliación/eventos | Deduplicación, reintentos y reconciliación | Bandeja de eventos y adaptadores; mecanismo de ejecución por decidir |

Como extensión **propuesta** de ES2, no incluida en los módulos validados de ES1, oferta/búsqueda podría gestionar campañas de destaque con vigencia, zona y categoría, y la API de pagos cobraría ese servicio **directamente a EspaciGo**, por separado del split de una reserva. Un selector consultaría solo publicaciones aprobadas y disponibles, rotaría candidatos en un cupo visible «Patrocinado» y registraría métricas agregadas. No está implementado ni se promete posición fija; antes de incorporarlo al alcance técnico debe aprobarse con el equipo y trazar sus nuevos casos y pruebas [@es2sernacpublicidad].

Los artefactos previstos son una imagen para presentación y otra para el backend, con configuración por entorno. El contrato de eventos debe identificar reserva, proveedor, operación e idempotencia; el éxito externo y el estado local no se consideran una misma transacción.

La persistencia operativa, el almacenamiento de archivos y la analítica cumplen funciones diferentes. El diagrama conserva BigQuery como propuesta de analítica, con la brecha de inmutabilidad ya registrada. Además, RNF-034–036 exigen portabilidad que todavía debe contrastarse frente a los servicios específicos de GCP.

### Interfaces propuestas

*Tabla. Contratos entre componentes.* <!--#tab:es2-interfaces-componentes-->

| Interfaz | Provee | Consume | Operaciones previstas | Entrada y salida | Control y error |
| --- | --- | --- | --- | --- | --- |
| API pública | API modular | Web y usuarios | Consultas y comandos de M01–M11 | JSON con sesión o token; respuestas paginadas | OpenAPI de RNF-032, validación, permisos y límite de tasa |
| Repositorio operativo | PostgreSQL/PostGIS | Módulos de dominio | Lecturas, escrituras y transacción de reserva | Filas y tuplas del Anexo B | Restricciones, exclusión de solapamiento y respaldo |
| Almacén de objetos | Servicio de archivos | Módulos de oferta, contrato y operación | Cargar, obtener y eliminar objetos | Clave de objeto, metadatos y hash | URL firmada de corta vida, permisos y ciclo de vida |
| Adaptador de pago | Backend | Proveedor de pago | Iniciar el cobro, autorizar y capturar la garantía, reembolsar y consultar estado | Clave de idempotencia y referencia externa | Timeout de 5 s y dos reintentos de RNF-023; estado por conciliar |
| Adaptador de firma | Backend | Proveedor de firma | Crear la solicitud, consultar estado y obtener el documento | Referencia y versión del contrato | Vencimiento y verificación de todas las firmas |
| Adaptador de identidad | Módulos M03 | Registro Civil y SII previstos | Iniciar y consultar la verificación | Referencias, sin datos sensibles en los registros | Rechazo, reintento y revisión manual |
| Entrada de eventos | Proveedores | Conciliación y módulos | Recibir, deduplicar y procesar webhooks | Evento firmado y hash de contenido | Firma obligatoria; hasta cinco reintentos con retroceso |
| Salida de notificaciones | Módulos de dominio | Servicio de correo | Enviar correo transaccional | Plantilla y destinatario | Reintento y registro sin datos sensibles |

Las firmas concretas, los tipos y las versiones se documentarán en el OpenAPI de RNF-032 y en el catálogo de eventos; aquí se fija la responsabilidad y el límite de cada interfaz, no un código ejecutable.

### Ejecución de la conciliación

La conciliación de RNF-028 necesita un disparador explícito. Se propone un **trabajo programado** que revisa los intentos en estado por conciliar y los eventos sin procesar, más una ejecución **a solicitud** desde administración para un caso concreto. Cada corrida debe ser idempotente, registrar su resultado en `evento_auditoria` y nunca repetir una operación financiera con otra clave. Quedan por decidir el periodo, el servicio que la ejecuta, el tratamiento de un proveedor caído durante la corrida y quién puede forzarla; su ensayo corresponde a PT-03 y PT-04.

### Protección del repositorio de auditoría

RNF-017 exige inmutabilidad y sigue sin mecanismo seleccionado. Se comparan tres opciones: una tabla con **cadena de hash** y permisos restringidos, un **objeto con retención bloqueada** en el almacén y un **destino analítico de solo anexado**. Ninguna se ha probado ni contratado. Cualquiera de ellas mantiene el límite ya registrado: un hash demuestra integridad de los bytes verificados, pero no impide que una cuenta con privilegios altere el almacenamiento. La decisión requiere costo, alcance de retención y una prueba de alteración que falle como se espera.

[[PENDIENTE: validar estas interfaces con el equipo y con cada proveedor, ensayar la retención bloqueada propuesta en 3.0 para RNF-017 y demostrar la portabilidad de RNF-034–036 antes de declarar cumplimiento.]]
