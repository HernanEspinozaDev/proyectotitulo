# Ajustes del cronograma

## Revisión de carta Gantt o desarrollo de fases

El equipo informó que ES2 se entrega el **3 de noviembre de 2026** y que el desarrollo funcional se iniciará en paralelo al informe. Por tanto, la planificación parte de un estado sin funcionalidades implementadas y debe coordinar la redacción con evidencias técnicas progresivas. La fecha fue comunicada por el usuario; queda pendiente su contraste con el calendario académico.

La planificación de ES1 abarca 16 semanas y presenta una diferencia entre los seis incrementos mencionados en su texto y los cinco incrementos enumerados antes del cierre. Esta entrega conserva ese antecedente y propone fases con productos verificables, sin trasladar automáticamente sus fechas.

*Tabla. Propuesta inicial de fases hasta la entrega de ES2.* <!--#tab:es2-fases-iniciales-->

| Período de 2026 | Informe e investigación | Desarrollo paralelo propuesto | Evidencia al cierre |
| --- | --- | --- | --- |
| 23–29 de septiembre | Base, brechas, trazabilidad y análisis inicial de tecnologías | Acordar alcance y preparar entorno del prototipo | Inventario y decisiones iniciales; evidencia de entorno si se completa |
| 30 de septiembre–6 de octubre | Comparativas, BPMN, casos y modelo de datos | Construir un recorrido acotado de catálogo y disponibilidad | Modelos revisados y demostración del alcance efectivamente construido |
| 7–13 de octubre | Componentes, comunicaciones, infraestructura y KPI/SLA | Avanzar reserva y probar la integración habilitada de mayor riesgo | Diseño consistente y resultados de experimento o bloqueo documentado |
| 14–20 de octubre | Pruebas, normas, disponibilidad y continuidad | Ejecutar pruebas sobre los flujos disponibles | Casos ejecutados, hallazgos y plan de corrección |
| 21–27 de octubre | Mantención, ajuste del cronograma y revisión del cuerpo | Corregir defectos y estabilizar el alcance demostrable | Evidencias actualizadas y limitaciones identificadas |
| 28 de octubre–2 de noviembre | Introducción, conclusiones, APA 7, anexos y revisión Word | Preparar versión y demostración con alcance declarado | Informe revisado y material de demostración existente |
| 3 de noviembre | Entrega ES2 | Presentar el avance real conforme a lo solicitado | Constancia de entrega cuando se realice |

**Nota.** Propuesta de planificación elaborada para ES2. Las actividades de desarrollo son objetivos por acordar, no compromisos aceptados ni avances ejecutados. Las fases no implican implementar los 236 RF antes del vencimiento.

La revisión debe ajustar la carga por persona, dependencias, tiempo disponible y alcance de evaluación. Si una integración no se habilita, se registrará su impacto y cualquier simulación usada para probar el flujo; ese resultado no se contará como integración real.

### Incrementos de ES1 y fases de ES2

El informe de ES1 declara «seis incrementos funcionales más una etapa de iniciación y una de cierre» y titula su tabla «Cronograma del proyecto en 16 semanas (6 incrementos)», pero el cuerpo de esa tabla enumera solo cinco incrementos y el cierre, mientras su indicador de avance declara «6 de 6». La diferencia se registra aquí y no se corrige en ES1, que permanece cerrada. ES2 tampoco reutiliza esas fechas: define fases propias con entregables verificables y deja el denominador de KPI-05 por fijar al acordar el alcance.

### Hitos verificables

*Tabla. Hitos, evidencia de cierre y estado documental.* <!--#tab:es2-hitos-->

| Hito | Fecha | Evidencia de cierre | Estado documental |
| --- | --- | --- | --- |
| H1 Base, brechas y trazabilidad | 29 de septiembre de 2026 | Inventario de brechas y matriz de trazabilidad versionados | Cumplido en lo documental |
| H2 Diseño del capítulo III cerrado | 13 de octubre de 2026 | Secciones 3.1–3.7 y Anexo B con contenido completo y pendientes acotados | Contenido completo; faltan validación del equipo y ensayos |
| H3 Medición y calidad | 20 de octubre de 2026 | Fichas de KPI y SLA con método y catálogo de pruebas | Método definido; pruebas sin ejecutar |
| H4 Operación y planificación | 27 de octubre de 2026 | Procedimientos de gestión y este cronograma ajustado | Redactados; falta el acuerdo del equipo |
| H5 Cierre del contenido | 2 de noviembre de 2026 | Introducción, conclusiones, referencias y anexos sin pendientes de redacción | Pendiente |
| H6 Entrega de ES2 | 3 de noviembre de 2026 | Constancia de entrega y material de demostración existente | Pendiente |
| Revisión docente | Sin fecha registrada | Retroalimentación recibida y registrada | Pendiente; no hay evidencia de una revisión |

El estado describe el avance documental, no una aceptación docente. Los hitos formativos del calendario académico no se incorporan porque no existe una fecha verificada, y la entrega del 3 de noviembre proviene de la comunicación del usuario, no del calendario de la asignatura.

### Dependencias y esfuerzo

*Tabla. Dependencias y esfuerzo relativo por bloque.* <!--#tab:es2-fases-esfuerzo-->

| Bloque | Depende de | Esfuerzo relativo | Riesgo principal |
| --- | --- | --- | --- |
| III Diseño | Línea base de ES1 y la investigación de modelado | Alto | Validación del equipo |
| IV Medición | Metas de ES1 y el diseño del capítulo III | Medio | Sin producto no hay medición |
| V Pruebas y normas | Diseño, metas y acceso a proveedores | Medio | Entornos y credenciales |
| VI Operación | Diseño, SLA y herramientas | Medio | Ensayos de respaldo e incidentes |
| VII Cronograma y cierre de contenido | Cuerpo y anexos completos | Medio | Introducción y conclusiones al final |
| Actualización económica | Evidencia de precios, demanda y tarifas | Alto | Depende de terceros y de trabajo de campo |
| Cierre institucional en Word | Contenido cerrado y solución APA validada | Alto | Se ejecuta una sola vez, al final |

El esfuerzo es una comparación relativa entre bloques y no una estimación en horas: convertirla exige la capacidad semanal de los tres integrantes declarados en los metadatos, que sigue sin confirmar. Tampoco se asignan responsables nominales por bloque.

### Seguimiento y riesgos

El avance se revisa contra `pendientes.md`, que solo marca una tarea cuando existe evidencia. El cronograma se versiona en el repositorio y la investigación paralela se coordina con el tablero de la entrega, cuya bitácora registra quién tomó cada tarea, qué archivo cambió y con qué resultado. Una fase no se declara cerrada por haber transcurrido su período: se cierra con su evidencia.

*Tabla. Riesgos del cronograma, efecto y mitigación propuesta.* <!--#tab:es2-riesgos-cronograma-->

| Riesgo | Efecto | Mitigación propuesta | Señal de activación |
| --- | --- | --- | --- |
| Capacidad semanal sin confirmar | Fechas propuestas sin respaldo | Acordarla y recalcular las fases | Sin acuerdo al cierre de septiembre |
| Acceso a proveedores no habilitado | Las pruebas de pago, webhook y firma quedan condicionadas | Registrar el bloqueo y sustituir por simulación declarada | Sin credenciales ni entorno de pruebas |
| Evidencia de demanda y precios ausente | El Anexo A permanece condicional | Ejecutar el protocolo de medición por categoría o declarar la limitación | Sin entrevistas ni cotizaciones |
| Cierre institucional diferido | Cuello de botella en la última semana | Reservar la etapa de cierre completa y resolver APA en copia | Contenido cerrado tarde |
| Preservación de la línea base | Pérdida o alteración de ES1 | Cotejar los hashes antes de entregar | Diferencia contra la instantánea de ES1 |
| Indisponibilidad de un integrante | Retraso del bloque que llevaba | Traspaso por bitácora y pendientes acotados | Sin avance durante dos sesiones |

[[PENDIENTE: confirmar con el equipo la capacidad semanal y los responsables, acordar el alcance de demostración, incorporar los hitos formativos cuando exista calendario y registrar la revisión docente solo con evidencia.]]

