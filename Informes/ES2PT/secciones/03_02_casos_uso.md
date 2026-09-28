## Diagramas de caso de uso

Se presentan siete vistas que conservan identificadores y objetivos del anexo D de ES1, ordenadas según los módulos M01–M11: identidad y acceso, perfil y privacidad, oferta, búsqueda, reserva y contrato, operación y cierre, y reputación y administración. En conjunto representan 41 de los 52 casos del catálogo; los once restantes se explican al final de la sección y ninguno se excluye del alcance de ES2. Las asociaciones expresan participación directa del actor y las relaciones `include`, `extend` y de generalización se mantienen solo donde el anexo D las justifica. La selección no acredita implementación y las relaciones temporales se explican en el BPMN.

### Identidad y acceso

![Casos de uso de identidad y acceso](imagenes/figura-cu_identidad.png){width=6.3in} <!--#fig:es2-cu-identidad--> <!--#fuente:elaboración propia a partir del anexo D de ES1.-->

CU-01, CU-02 y CU-03 cubren registro, correo y acceso. CU-11 y CU-12 distinguen persona natural y empresa; CU-13 permite la revisión manual de validaciones fallidas. CU-10 sigue siendo el caso abstracto del catálogo y no se representa como operación ejecutable en esta vista. Registro Civil y SII permanecen como actores previstos con acceso pendiente.

### Perfil, privacidad y cuenta

![Perfil, privacidad y cuenta](imagenes/figura-cu_perfil.png){width=6.3in} <!--#fig:es2-cu-perfil--> <!--#fuente:elaboración propia a partir del anexo D de ES1.-->

CU-07, CU-08 y CU-09 pertenecen al módulo M02 y CU-50 al M01. El Usuario Registrado es el único actor de los cuatro casos, y Arrendador y Arrendatario heredan la capacidad. La cuenta bancaria de CU-08 se utiliza después en la liquidación de CU-42, y CU-09 es el caso donde el derecho de supresión convive con la retención de hechos financieros: la regla de anonimización y conservación sigue sin aprobarse en ES2 y su verificación está planificada en PT-16.

### Oferta de espacios

![Oferta de espacios](imagenes/figura-cu_oferta.png){width=6.3in} <!--#fig:es2-cu-oferta--> <!--#fuente:elaboración propia a partir del anexo D de ES1.-->

CU-15 a CU-18 pertenecen al módulo M04 y los ejecuta el Arrendador con identidad verificada. La vista conserva la decisión del anexo D de no declarar `include` entre CU-15 y CU-16, porque la galería no es obligatoria para registrar la publicación. CU-17 mantiene el calendario que consume la búsqueda y que CU-23 valida al reservar; un bloqueo manual no puede superponerse a reservas vigentes.

### Búsqueda y cotización

![Búsqueda y cotización](imagenes/figura-cu_busqueda.png){width=6.3in} <!--#fig:es2-cu-busqueda--> <!--#fuente:elaboración propia a partir del anexo D de ES1.-->

CU-19, CU-20 y CU-21 pertenecen al módulo M05. La generalización `Visitante ◁— Usuario Registrado ◁— Arrendatario` explica por qué la búsqueda alcanza a los usuarios registrados y la cotización queda en el arrendatario. Los tres casos se mantienen independientes, como en la base: cotizar no exige buscar y consultar el detalle no exige cotizar. CU-20 muestra las reseñas de CU-36 dentro del detalle sin convertirlo en un `include`.

### Reserva y contrato

![Casos de uso de reserva y contrato](imagenes/figura-cu_reserva.png){width=6.3in} <!--#fig:es2-cu-reserva--> <!--#fuente:elaboración propia a partir del anexo D de ES1.-->

CU-22 incluye obligatoriamente CU-23 y CU-24 incluye CU-25, conforme a la base. CU-26 corresponde a la decisión del arrendador; CU-29 y CU-30 cubren generación y firma de ambas partes. Los casos automáticos de vencimiento CU-27, CU-28 y CU-32 no se dibujan aquí y se mantienen como excepciones descritas en el proceso; no desaparecen del alcance documental.

### Operación y cierre

![Casos de uso de operación y cierre](imagenes/figura-cu_operacion.png){width=6.3in} <!--#fig:es2-cu-operacion--> <!--#fuente:elaboración propia a partir del anexo D de ES1.-->

CU-33, CU-34 y CU-48 representan ingreso, salida y recepción como objetivos independientes. CU-39, CU-40 y CU-41 describen reclamo, descargos y resolución; CU-42 aborda liquidación y comprobante. La dependencia de proveedores financieros y tributarios se conserva como pendiente de verificación.
Se conserva la relación `extend` de CU-39 hacia CU-42 indicada en el catálogo de ES1: el reclamo altera el cierre financiero previsto. Su semántica y punto de extensión se revisarán con el equipo antes de pasar a una especificación ejecutable.

### Reputación y comunicación

![Reputación y comunicación](imagenes/figura-cu_reputacion.png){width=6.3in} <!--#fig:es2-cu-reputacion--> <!--#fuente:elaboración propia a partir del anexo D de ES1.-->

CU-35 a CU-38 y CU-49 pertenecen al módulo M09. Las dos partes participan en la reseña y en el chat, y el Visitante solo consulta. CU-49 es un objetivo autónomo del Arrendador que habilita la moderación del Administrador en CU-44: la dependencia se describe aquí y no se dibuja como relación UML porque el anexo D no la declara. Los mensajes y reseñas contienen datos personales y quedan sujetos a la matriz de tratamiento del Anexo B; su conservación sigue supeditada a la regla aún no aprobada.

### Administración y auditoría

![Administración y auditoría](imagenes/figura-cu_administracion.png){width=6.3in} <!--#fig:es2-cu-administracion--> <!--#fuente:elaboración propia a partir del anexo D de ES1.-->

CU-43 a CU-46 y CU-52 pertenecen al módulo M11 y los ejecuta el Administrador, que en la base no hereda del Usuario Registrado. CU-46 se apoya en el repositorio de auditoría cuya inmutabilidad exige RNF-017, todavía sin mecanismo seleccionado: la vista muestra el objetivo del actor, no la garantía técnica. CU-43 y CU-44 dejan trazas que ese mismo historial debe registrar.

*Tabla. Trazabilidad de las vistas UML seleccionadas.* <!--#tab:es2-cu-trazabilidad-->

| Vista | Casos representados | Módulo | Actores | Referencias principales |
| --- | --- | --- | --- | --- |
| Identidad y acceso | CU-01, CU-02, CU-03, CU-11, CU-12, CU-13 | M01/M03 | Visitante, Usuario Registrado y Administrador; Registro Civil y SII previstos | RQF-001–023, 038–059; HU01, HU02, HU04 |
| Perfil, privacidad y cuenta | CU-07, CU-08, CU-09, CU-50 | M02/M01 | Usuario Registrado (Arrendador y Arrendatario heredan) | RQF-024–037, 213–218; HU03, HU31, HU32 |
| Oferta de espacios | CU-15, CU-16, CU-17, CU-18 | M04 | Arrendador con identidad verificada | RQF-060–093; HU05–HU08, HU20, HU21 |
| Búsqueda y cotización | CU-19, CU-20, CU-21 | M05 | Visitante y Arrendatario (Usuario Registrado hereda) | RQF-094–107; HU10, HU15 |
| Reserva y contrato | CU-22, CU-23, CU-24, CU-25, CU-26, CU-29, CU-30 | M06/M07 | Arrendatario y Arrendador; Mercado Pago y FirmaVirtual previstos | RQF-108–142; HU15, HU17, HU18, HU33 |
| Operación y cierre | CU-33, CU-34, CU-48, CU-39, CU-40, CU-41, CU-42 | M08/M10 | Arrendatario, Arrendador y Administrador; Mercado Pago y SII previstos | RQF-143–177; HU28, HU35 |
| Reputación y comunicación | CU-35, CU-36, CU-37, CU-38, CU-49 | M09 | Visitante, Arrendador y Arrendatario | RQF-153–158, 207; HU25, HU34 |
| Administración y auditoría | CU-43, CU-44, CU-45, CU-46, CU-52 | M11 | Administrador | RQF-178–185, 212, 236; HU26 |

*Tabla. Casos del catálogo no representados en las siete vistas.* <!--#tab:es2-cu-no-representados-->

| Casos | Módulo | Motivo de no representarlos aquí |
| --- | --- | --- |
| CU-04, CU-05, CU-06 | M01 | Bloqueo por intentos fallidos, recuperación de contraseña y cierre de sesión: son flujos excepcionales o alternativos del acceso ya descrito. CU-04 se declara como extensión de CU-03 en la base. |
| CU-10 | M03 | Caso abstracto: se ejecuta a través de CU-11 y CU-12, que sí están representados. |
| CU-14 | M03 | Reintento de una validación rechazada; recuperación posterior a CU-13, cuya vista ampliada sigue por decidir con el equipo. |
| CU-27, CU-28, CU-32 | M06/M07 | Vencimientos automáticos sin actor iniciador; se representan como temporizadores T1–T3 en la sección correspondiente al BPMN. |
| CU-31 | M07 | Descarga del contrato firmado: objetivo de las partes sobre un contrato ya generado; se incorporará a la vista de contratos cuando el equipo cierre su alcance. |
| CU-47, CU-51 | M06 | Historial y cancelación de reservas vigentes: la vista de reserva priorizó la creación y el pago; ambos son objetivos del arrendatario sobre reservas existentes. |

**Nota.** La trazabilidad detallada RF–CU permanece en el anexo D; estas agrupaciones no crean, renumeran ni excluyen requisitos. Ninguna vista acredita implementación ni prueba de integración.

[[PENDIENTE: validar con el equipo la selección y las relaciones de estas siete vistas, decidir si CU-14, CU-31, CU-47 y CU-51 requieren vista propia, enlazar el alcance de demostración y revisar el tamaño y la paginación de las figuras en el cierre visual del contenido.]]
