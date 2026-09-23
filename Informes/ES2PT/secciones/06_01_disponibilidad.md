## Gestión de disponibilidad

La meta heredada RNF-009 es **99,9 % mensual** para autenticación, búsqueda y reservas; no cubre automáticamente la disponibilidad de pagos, firma o verificaciones externas. La medición y sus exclusiones se definen en 4.2. Un mes de 30 días permitiría como máximo 43,2 minutos de indisponibilidad para cada función si no se acuerdan exclusiones. Es una traducción aritmética de la meta, no una medición ni un SLA vigente [@es1anexoc].

*Tabla. Servicios, controles propuestos y evidencia de disponibilidad.* <!--#tab:es2-disponibilidad-->

| Servicio y objetivo | Dependencias críticas | Supervisión y respuesta prevista | Evidencia por obtener |
| --- | --- | --- | --- |
| Autenticación; ≥ 99,9 % mensual | Web, API, base de usuarios, sesión, DNS y certificado | Sondeo de inicio de sesión con cuenta sintética protegida; distinguir fallo HTTP, error funcional y certificado; alertar al operador y comprobar sesión tras recuperación. | Registro de sondeos, incidentes y prueba de humo CU-01. |
| Búsqueda; ≥ 99,9 % y RNF-001 | Web, API, PostgreSQL/PostGIS e índices | Consulta sintética sobre catálogo fijo; medir errores y latencia bajo carga separadamente; revisar consultas lentas, conexiones y espacio. | Series de disponibilidad y reporte PT-09 con entorno/carga. |
| Reserva; ≥ 99,9 % y consistencia RQF-111/112 | API, calendario transaccional, base y, para pago, proveedor externo | Ensayo sintético sin cargo real; vigilar conflictos, fallas de escritura, cola de eventos y conciliación. Ante incertidumbre financiera, conservar estado pendiente y consultar al proveedor antes de reintentar o liberar fechas. | Eventos correlacionados, PT-02/04 y trazas de conciliación. |
| Contrato, firma y pagos; niveles por acordar | Archivos, generador PDF, pasarela y firma | Medir disponibilidad propia y del tercero por separado. Si falla un tercero, suspender solo la operación dependiente, preservar idempotencia y mostrar estado pendiente verificable. | Estado de proveedor, incidente y pruebas de recuperación; condiciones contractuales. |
| Datos y respaldos; RPO ≤ 4 h, RTO ≤ 6 h | Base, copias, archivos, claves y configuración | Vigilar edad/estado de copia y archivos de recuperación, capacidad, permisos y posibilidad de restaurar. La salud de una copia no equivale a recuperación validada. | Inventario de copias, alertas y ensayo PT-11. |

### Supervisión y operación diaria propuesta

Un sondeo público de infraestructura permite detectar caída del endpoint, pero **no prueba** que la autenticación o una reserva funcionen. Se combinarán transacciones sintéticas de extremo a extremo con métricas de API, base y adaptadores. Cloud Monitoring ofrece comprobaciones de disponibilidad y políticas de alerta para un eventual despliegue en GCP; la herramienta, frecuencia, umbral y canal efectivo siguen por seleccionar [@es2uptime; @es2alerts]. Los eventos llevarán hora sincronizada, servicio, entorno, versión y un identificador correlativo sin datos sensibles.

El operador revisará los sondeos, los fallos repetidos, la ocupación de recursos y el estado de respaldos; abrirá un incidente si falla una función crítica o hay riesgo de pérdida de integridad. Se propone alerta por **dos sondeos fallidos consecutivos** y revisión manual del estado antes de declarar indisponibilidad; este umbral es un diseño inicial que debe contrastarse con la frecuencia elegida y los falsos positivos. Una alerta de capacidad debe anticipar saturación de conexiones, CPU, memoria, disco o cuota, y conducir a una prueba de carga para RNF-019/030, no a prometer escalado sin medición.

El mantenimiento planificado requerirá solicitud y autorización según 6.3, aviso de ventana y prueba de humo posterior. Hasta acordar exclusiones con el cliente, esos minutos cuentan en el cálculo de 4.2. Ante degradación: identificar servicio y hora de inicio, detener nuevas operaciones de pago/reserva si no se puede preservar consistencia, comprobar dependencia propia o externa, ejecutar recuperación o reversión aprobada, repetir humo y cerrar con hora y causa. La disponibilidad de terceros se registrará separadamente de la plataforma.

[[PENDIENTE: seleccionar y costear herramientas/infraestructura, fijar horarios, sondas, umbrales, alertas, responsables y canales; desplegar el servicio y medir al menos un período representativo; acordar exclusiones y ensayar capacidad y escalado.]]
