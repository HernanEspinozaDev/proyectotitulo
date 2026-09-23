## Diagrama de componentes

El diseño inicial mantiene la unidad de despliegue modular definida en ES1. Los módulos del backend son responsabilidades de software, no microservicios independientes. Las llamadas a proveedores se concentran en adaptadores para que su contrato y sus fallos puedan tratarse de forma explícita [@es1formulacion; @es1anexoc].

![Componentes lógicos y artefactos previstos](imagenes/figura-componentes.png){width=6.3in} <!--#fig:es2-componentes--> <!--#fuente:elaboración propia a partir de ES1.-->

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

Los artefactos previstos son una imagen para presentación y otra para el backend, con configuración por entorno. El contrato de eventos debe identificar reserva, proveedor, operación e idempotencia; el éxito externo y el estado local no se consideran una misma transacción.

La persistencia operativa, el almacenamiento de archivos y la analítica cumplen funciones diferentes. El diagrama conserva BigQuery como propuesta de analítica, con la brecha de inmutabilidad ya registrada. Además, RNF-034–036 exigen portabilidad que todavía debe contrastarse frente a los servicios específicos de GCP [@es1anexoc].

[[PENDIENTE: definir firmas de interfaces, mecanismo de ejecución de conciliación, protección del repositorio de auditoría y evidencia de portabilidad; validar correspondencia con las vistas de infraestructura y comunicaciones.]]
