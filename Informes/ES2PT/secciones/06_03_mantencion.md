## Plan de mantención

La mantención debe conservar coherentes código, esquema, configuración, documentación y procedimientos. Hasta disponer de un producto desplegado, este apartado define un flujo **propuesto**; no hay solicitudes aprobadas ni incidentes operativos registrados. Se usa control de versiones para repetir una instalación y relacionar cada defecto con un entregable y su prueba.

### Configuración y entregables

El inventario mínimo contendrá repositorio y revisión de código, versión de frontend/API, migraciones de PostgreSQL, imagen y digest de contenedor, variables no secretas, identificador de secretos, infraestructura, dependencias, contratos de integración y procedimientos de respaldo. Cada elemento registrará propietario, entorno, fecha, relación con RQF/RNF y enlace a su configuración verificable. Los secretos se referencian por identificador y custodia, nunca se copian al inventario. La versión de un anexo o documento ES2 se registrará junto al cambio que lo actualice; ES1 permanece congelado.

### Solicitud, aprobación y despliegue de cambios

1. **Registrar** identificador, solicitante, fecha, motivo, entregables afectados y requisitos asociados; clasificar cambio ordinario o urgente.
2. **Evaluar** efecto sobre reservas, pagos, firma, privacidad, datos y portabilidad; estimar ventana, costo, riesgo, migración y reversión. Un cambio de esquema debe declarar compatibilidad hacia atrás y tratamiento de datos existentes.
3. **Autorizar** por una persona distinta de quien propone cuando el equipo la designe. Sin autorización registrada, no promover a un entorno compartido; la ruta urgente conserva justificación y revisión posterior.
4. **Probar** en entorno separado con casos unitarios, integrales y de humo pertinentes; conservar versión y resultados. Si afecta pago o firma, distinguir simulación de sandbox/proveedor real.
5. **Desplegar** una revisión identificable, verificar métricas y ejecutar humo. En Cloud Run se puede redirigir tráfico a una revisión anterior, pero ello no revierte por sí solo cambios de datos ni solicitudes externas ya aceptadas; la reversión debe cubrir cada componente afectado [@es2cloudrunrollback].
6. **Cerrar** con hora, autorización, resultados, incidentes derivados y documentación actualizada. Si falla, detener tráfico, restaurar la versión compatible, evaluar datos y abrir incidente.

### Gestión de incidentes

El registro recogerá identificador, detector, hora de inicio/detección, servicio y entorno, síntomas, versión, impacto, operaciones afectadas, severidad, responsable, acciones, comunicaciones, hora de restauración y causa confirmada o por investigar. Se propone **crítico** si existe riesgo de pérdida de datos, cargo duplicado, doble reserva o indisponibilidad de una función RNF-009; **alto** si se degrada una función importante sin pérdida de integridad; **normal** para un defecto con alternativa segura. Estos niveles y tiempos de escalamiento deben acordarse con el equipo y los SLA.

El operador registra y contiene; escala a la persona responsable de aplicación/datos o a un proveedor según origen. Se preservan identificadores de transacción sin exponer PII. El cierre requiere prueba de humo, confirmación de operaciones pendientes, comunicación a afectados cuando proceda y acción preventiva trazada a un cambio. Una disputa sobre daños, garantía o resolución de arriendo pertenece al proceso de negocio M10/CU-41; solo se abre incidente técnico si falló el software, el dato o la integración que la soporta.

*Tabla. Campos mínimos de los formatos de mantención.* <!--#tab:es2-formatos-operacion-->

| Registro | Campos obligatorios antes de cierre | Enlace de evidencia |
| --- | --- | --- |
| Cambio | ID, motivo, requisitos, versiones inicial/final, riesgo, aprobación, pruebas, ventana, reversión, decisión y responsable | Solicitud, revisión de código, resultado de CI, despliegue y humo |
| Incidente | ID, línea de tiempo, servicio, impacto, severidad, contención, escalamiento, recuperación, causa y acción preventiva | Alertas, logs depurados, estado de proveedor, prueba de retorno y cambio correctivo |

La gestión de cambios e incidentes operará sobre **GitHub Issues** e integrará el flujo de **Pull Requests** para las autorizaciones, garantizando que ninguna implementación llegue a entornos productivos sin revisión de al menos un par cruzado. En caso de fallas durante humo post-despliegue, Cloud Run permite reversión de tráfico en instantes hacia la revisión anterior sana, mitigando impactos directos al cliente final.
