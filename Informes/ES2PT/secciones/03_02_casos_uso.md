## Diagramas de caso de uso

Se presentan tres vistas de los procesos priorizados, conservando identificadores y objetivos del anexo D de ES1. La selección contiene 20 casos distintos y no sustituye el catálogo de 52 ni acredita implementación. Las asociaciones expresan participación; las relaciones temporales se explican en el BPMN [@es1anexod].

### Identidad y acceso

![Casos de uso de identidad y acceso](imagenes/figura-cu_identidad.png){width=6.3in} <!--#fig:es2-cu-identidad--> <!--#fuente:elaboración propia a partir del anexo D de ES1.-->

CU-01, CU-02 y CU-03 cubren registro, correo y acceso. CU-11 y CU-12 distinguen persona natural y empresa; CU-13 permite la revisión manual de validaciones fallidas. CU-10 sigue siendo el caso abstracto del catálogo y no se representa como operación ejecutable en esta vista. Registro Civil y SII permanecen como actores previstos con acceso pendiente.

### Reserva y contrato

![Casos de uso de reserva y contrato](imagenes/figura-cu_reserva.png){width=6.3in} <!--#fig:es2-cu-reserva--> <!--#fuente:elaboración propia a partir del anexo D de ES1.-->

CU-22 incluye obligatoriamente CU-23 y CU-24 incluye CU-25, conforme a la base. CU-26 corresponde a la decisión del arrendador; CU-29 y CU-30 cubren generación y firma de ambas partes. Los casos automáticos de vencimiento CU-27, CU-28 y CU-32 no se dibujan aquí y se mantienen como excepciones descritas en el proceso; no desaparecen del alcance documental.

### Operación y cierre

![Casos de uso de operación y cierre](imagenes/figura-cu_operacion.png){width=6.3in} <!--#fig:es2-cu-operacion--> <!--#fuente:elaboración propia a partir del anexo D de ES1.-->

CU-33, CU-34 y CU-48 representan ingreso, salida y recepción como objetivos independientes. CU-39, CU-40 y CU-41 describen reclamo, descargos y resolución; CU-42 aborda liquidación y comprobante. La dependencia de proveedores financieros y tributarios se conserva como pendiente de verificación.
Se conserva la relación `extend` de CU-39 hacia CU-42 indicada en el catálogo de ES1: el reclamo altera el cierre financiero previsto. Su semántica y punto de extensión se revisarán con el equipo antes de pasar a una especificación ejecutable.

*Tabla. Trazabilidad de las vistas UML seleccionadas.* <!--#tab:es2-cu-trazabilidad-->

| Vista | Casos representados | Referencias principales |
| --- | --- | --- |
| Identidad | CU-01, CU-02, CU-03, CU-11, CU-12, CU-13 | M01/M03; HU01, HU02, HU04 |
| Reserva y contrato | CU-22, CU-23, CU-24, CU-25, CU-26, CU-29, CU-30 | M06/M07; HU15, HU17, HU18, HU33 |
| Operación y cierre | CU-33, CU-34, CU-48, CU-39, CU-40, CU-41, CU-42 | M08/M10; HU28, HU35 |

**Nota.** La trazabilidad detallada RF–CU permanece en el anexo D; estas agrupaciones no crean ni renumeran requisitos.

[[PENDIENTE: validar selección y relaciones, completar las vistas de oferta, búsqueda, perfiles, reputación y administración, y enlazar el alcance de demostración que acuerde el equipo.]]
