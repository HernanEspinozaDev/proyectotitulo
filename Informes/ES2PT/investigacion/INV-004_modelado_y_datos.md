# INV-004 — Procesos, componentes y modelo de datos

- Estado: propuesta de análisis en revisión; no hay implementación ni aprobación del equipo.
- Fecha: 2026-09-23.
- Base: informe final ES1 y anexos A–E, especialmente procesos, CU y requisitos RQF/RNF.
- Secciones: 3.1–3.7; Anexo A de ES2.

## Pregunta y fuentes

¿Qué diseño permite explicar el ciclo de EspaciGo sin dar por implementadas las capacidades propuestas en ES1? Se contrastaron los procesos, módulos, CU y RNF de la entrega cerrada con la [notación BPMN 2.0.2](https://www.omg.org/spec/BPMN/2.0.2), las [restricciones de rango de PostgreSQL](https://www.postgresql.org/docs/18/rangetypes.html) y la [descripción de Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run). Estas fuentes sustentan capacidades de herramientas o notación; las decisiones particulares siguientes son inferencias de diseño para ES2 y requieren revisión y prueba.

## Método y productos

Se seleccionaron tres procesos que cubren identidad, reserva y cierre. Los diagramas BPMN de `diagramas/bpmn*.svg` contienen dos subprocesos expandidos por proceso; las vistas de CU, componentes y datos son PlantUML en la misma carpeta. Las imágenes se generan en `build/imagenes/`, para que las fuentes sigan editables. Los BPMN son modelos de análisis con una coordinación interna: faltan pools entre organizaciones, mensajes y temporizadores explícitos antes de darlos por cerrados. La referencia de notación es [OMG BPMN 2.0.2](https://www.omg.org/spec/BPMN/2.0.2).

Las vistas `topologia_comunicaciones`, `infraestructura_propuesta` y `arquitectura_general` extienden el diseño a 3.5–3.7. Su red, recursos virtuales y hardware del cliente están propuestos, sin despliegue acreditado. Cloud Run es la opción heredada de ES1; región, capacidades, servicios de datos y costos siguen por decidir. La portabilidad RNF-034–036 y la inmutabilidad RNF-017 son brechas explícitas.

| Decisión propuesta en ES2 | Evidencia de partida | Verificación pendiente |
| --- | --- | --- |
| Conservar CU y módulos de ES1, agrupando 20 CU representativos en tres vistas | Anexo D y arquitectura ES1 | Completar vistas del resto del catálogo; revisar asociación y extensión con el equipo |
| Mantener backend modular como unidad de despliegue | Arquitectura ES1 | Especificar interfaces, configuración y recorrido de errores de terceros |
| Modelar reserva y bloqueo manual sobre un calendario común `ocupacion` | RQF-111/RQF-112; CU-22/23 | DDL, restricción para intervalos solapados y prueba concurrente |
| Usar intervalos semiabiertos `[inicio, fin)` y una restricción de exclusión por espacio | [PostgreSQL: Range Types](https://www.postgresql.org/docs/18/rangetypes.html) | Definir zona horaria, intervalos válidos, filas activas, expiración y migraciones |
| Separar intento financiero, garantía, evento de proveedor y liquidación | RNF-012/024/028; CU-24–30/39–42 | Compatibilidad del producto real, estados, idempotencia y reconciliación |
| Versionar contrato y guardar firma por parte | CU-29/30/32 | Regla de vencimiento y validez de cada modalidad de firma |
| Guardar metadatos de documentos fuera de su archivo y eventos de auditoría identificables | ES1 M11 y RNF-017 | Acceso, retención, protección efectiva contra alteración y borrados permitidos |
| Aplicar la Ley 21.719 como criterio desde el primer diseño de datos, con matriz de tratamientos por categoría | Decisión del usuario en ES2; RNF-018/026/029/042/043; INV-006 | Completar finalidades, fundamentos, permisos, conservación y modelo de solicitudes; ejecutar PT-16 sin declarar cumplimiento anticipado |
| Separar borde público de datos operativos y exigir controles en webhooks | RNF-015/023/024/028 y flujo de ES1 | Red, servicio de secretos, TLS interno, producto externo y ensayo de fallos |
| Modelar web y API como dos contenedores propuestos | Topología de ES1 y [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) | Dimensionamiento, precio, despliegue local, segunda nube y recuperación |

El Anexo A contiene un **primer modelo parcial de 16 entidades y 123 atributos**. Esa cifra describe campos documentados, no cobertura completa de los 236 RF de ES1. Las cuatro vistas de datos muestran claves seleccionadas y deben leerse junto con el diccionario.

## Invariantes para diseño y pruebas

1. La reserva, ocupación activa y espacio deben referirse a la misma unidad; una transacción no puede confirmar dos intervalos solapados para un mismo espacio.
2. Una respuesta financiera incierta conserva su identificador y estado por conciliar; no habilita repetir el cobro con otra clave.
3. Una reserva solo habilita ingreso con las firmas exigidas confirmadas. Un reclamo abierto bloquea la liquidación según la base.
4. Un hash demuestra integridad de bytes verificados, no inmutabilidad del almacenamiento. El diseño de auditoría de RNF-017 sigue abierto.
5. La baja de una cuenta no borra en cascada hechos financieros ni documentos: cada dato se trata según una regla aprobada de supresión, anonimización o conservación, con decisión trazable.

## Cobertura y preguntas abiertas

Faltan perfiles detallados, sesiones y recuperación de cuenta, catálogos y tarifas, mensajería, reputación, notificaciones, comprobantes tributarios y asociaciones específicas de evidencias. También falta mapear íntegramente estados del ES1 al esquema, cerrar permisos y protección de datos, elegir operación de expiración, generar DDL y probar restricciones concurrentes. El modelo se revisará a medida que el producto avance; cada cambio de la base se registra aquí y no modifica ES1.

Para las vistas de infraestructura faltan inventario físico, carga prevista, dimensionamiento, selección de red/servicios, costos, respaldos probados y revisión de portabilidad. El diagrama general se revisará junto con el recorrido de reserva y los planes de pruebas y operación; su existencia no certifica RNF de disponibilidad o seguridad.
