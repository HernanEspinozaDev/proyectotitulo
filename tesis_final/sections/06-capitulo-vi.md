# CAPÍTULO VI: Metodología de trabajo

## 6. Metodología de trabajo

### 6.1. Metodología y Desarrollo de la solución

#### 6.1.1. Gobierno y ciclo de vida

La gestión se fundamenta en prácticas adaptadas de la Guía del PMBOK, sexta edición de 2017 [@pmbok6, pp. 19, 23, 28]. La guía organiza procesos de inicio, planificación, ejecución, monitoreo/control y cierre; estos procesos se aplican durante el proyecto y no equivalen a fases consecutivas de construcción del software. El desarrollo adopta un ciclo iterativo e incremental, con análisis, diseño, construcción y verificación por incremento.

El enfoque híbrido combina entregables y fechas académicas definidas con refinamiento técnico progresivo. El registro distingue especificación del producto, evidencia local e integración en el entorno objetivo. La programación consolidada al 16 de noviembre de 2026 constituye una referencia de trabajo; no se presenta como una línea base aprobada en agosto ni como reconstrucción de horas efectivamente trabajadas.

#### 6.1.2. Selección del enfoque

La matriz compara el ajuste de tres enfoques a las restricciones de este proyecto. La aplicación utiliza controles de alcance y recursos proporcionados a un equipo de tres integrantes.

**Tabla 5**\
*Matriz Multicriterio Ponderada de Selección Metodológica*

| Criterio de selección | Peso | Valoraciones | Justificación técnica |
|--------------------------|:----------:|---------------------|-----------------------------------------|
| **Predictibilidad y Control del Alcance** | 25% | 4/5 · 2/5 · **5/5** | El Anexo A fija una línea base de 236 requisitos funcionales. La EDT registra cambios de alcance por incremento. |
| **Fijeza de Plazos Académicos Institucionales** | 25% | 3/5 · 2/5 · **5/5** | Las fechas de titulación universitaria son inflexibles. La evaluación pondera la capacidad de organizar entregas parciales dentro del calendario académico. |
| **Mitigación Temprana de Riesgos Técnicos** | 20% | 1/5 · 5/5 · **4/5** | La evaluación compara la frecuencia con que cada propuesta del proyecto incorpora pruebas y revisión de riesgos. |
| **Control Formal de EDT y Recursos** | 15% | 4/5 · 1/5 · **5/5** | La evaluación considera el grado de integración de la EDT y la asignación de responsabilidades con los controles del proyecto. |
| **Trazabilidad de Pruebas y Calidad (QA)** | 15% | 2/5 · 4/5 · **5/5** | Permite vincular cada paquete de trabajo de la EDT con matrices de prueba unitarias, de integración y rendimiento. |
| **Puntaje Ponderado Total** | **100%** | **2,85/5,00** · **2,75/5,00** · **4,80/5,00** | **Selección Ganadora: Modelo Híbrido** |

*Nota.* Elaboración propia. Cada criterio se valora de 1 a 5 para este proyecto, donde 1 indica ajuste bajo y 5 ajuste alto. Las valoraciones se presentan en el orden cascada, Scrum y modelo híbrido. El total suma cada valoración multiplicada por su ponderación. Las ponderaciones y valoraciones corresponden al juicio técnico del proyecto; PMI no prescribe estos puntajes.

#### 6.1.3. Fases e incrementos

La Figura 3 representa las actividades que se repiten y revisan en el ciclo de construcción. La secuencia se concreta en cinco incrementos: identidad y cuenta; catálogo y búsqueda; aceptación y cobros; documentos y avisos; administración y auditoría. Cada incremento integra componentes y una revisión identificada Q01–Q05 antes del hito M01–M05. Las revisiones locales de rendimiento y recuperación pueden ejecutarse sobre componentes disponibles; la aceptación del sistema integrado conserva su evidencia propia.

**Figura 3**\
*Ciclo de construcción y revisión por incremento*

![](assets/figuras/fig04_ciclo_vida_objetivo.png){height=11cm}

*Nota.* Elaboración propia. El ciclo se aplica a cada incremento; los procesos de gestión acompañan su desarrollo [@pmbok6].

#### 6.1.4. Gestión del alcance y diccionario EDT

El alcance del Capítulo V, la EDT y su diccionario organizan la referencia de alcance del proyecto [@pmbok6, pp. 156, 161–162]. La Figura 4 conserva seis ramas y 28 paquetes de entregables. La actualización precisa sus nombres, distingue el acuerdo de gobierno de la constitución societaria y separa la preparación comercial de su realización efectiva.

**Figura 4**\
*Estructura de desglose del trabajo de espaciGo*

![](assets/figuras/edt_paquetes.png){width=16cm}

*Nota.* Elaboración propia. Los 28 identificadores se conservan y vinculan el diccionario G.2 con las actividades G.3.

El Anexo G.2 desarrolla una ficha para cada paquete: responsable de coordinación, producto, criterio de aceptación, actividades, esfuerzo, recursos, límites, riesgo y referencia de evidencia. El responsable del paquete coordina su aceptación; las actividades pueden asignarse a otro integrante según su especialidad. El modelo separa entregables de la EDT y tareas del cronograma. Ninguna ficha se considera aceptada por la sola existencia de una fecha programada.

#### 6.1.5. Gestión de riesgos

La evaluación utiliza probabilidad de 1 (muy baja) a 5 (muy alta) e impacto de 1 (menor) a 5 (crítico). El producto de ambos valores define prioridad baja entre 1 y 4, media entre 5 y 10 y alta entre 11 y 25. La escala es ordinal y no representa probabilidades estadísticas. El Anexo G.9 agrega dueño, disparador y seguimiento. El responsable revisa los riesgos por corte y cuando cambia su disparador [@pmbok6, pp. 417, 419, 437, 442].

**Figura 5**\
*Mapa de probabilidad e impacto de los riesgos*

![](assets/figuras/mapa_riesgos.png){width=13cm}

*Nota.* Elaboración propia a partir de la Tabla 6. Las posiciones muestran valoraciones cualitativas del proyecto.

**Tabla 6**\
*Registro resumido de riesgos*

| ID | Riesgo | Evaluación | Respuesta |
| --- | --- | --- | --- |
| R01 | Doble reserva concurrente | 3 × 5 = 15; alta | Exclusión temporal e idempotencia; verificar concurrencia antes de aceptar el flujo. |
| R02 | Degradación del proveedor de pagos | 2 × 5 = 10; media | Reintentos idempotentes, conciliación y reversos; mantener la habilitación externa condicionada. |
| R03 | Exposición de datos privados | 2 × 5 = 10; media | Autorización por recurso y finalidad, pruebas negativas y verificación tras restauración. |
| R04 | Incumplimiento de entrega | 3 × 4 = 12; alta | Revisión semanal y diaria del tramo crítico; congelar alcance del corte y registrar impacto. |
| R05 | Inadecuación de evidencia contractual | 1 × 4 = 4; baja | Revisar modalidades y documentos; separar aceptación bilateral y firma opcional. |
| R06 | Disponibilidad personal inferior al calendario | 3 × 4 = 12; alta | Registrar excepciones y recalcular; reasignar solo con competencias y capacidad verificadas. |
| R07 | Diferencia entre entorno local y entorno objetivo | 2 × 4 = 8; media | Revisar artefactos y preparar ensayo independiente; no inferir aceptación cloud del emulador. |
| R08 | Volumen comercial insuficiente | 2 × 4 = 8; media | Contrastar demanda y sensibilidad del Capítulo XIV; escalonar gasto según caja disponible. |

*Nota.* Elaboración propia a partir del registro maestro del cronograma, corte 16-11-2026.

#### 6.1.6. Gobierno, integración y control

El propósito académico consiste en entregar el informe institucional, el repositorio identificable, la demostración del corte y sus evidencias de ingeniería. El equipo decide los ajustes técnicos dentro del alcance documentado; la evaluación y cualquier cambio de fecha institucional corresponden a la autoridad académica. La ficha de gobierno del Anexo G no sustituye un acta institucional firmada. El acuerdo de funcionamiento del proyecto y la futura constitución de la empresa tienen finalidades diferentes.

La adaptación integra las diez áreas de gestión: integración mediante control de versiones y cambios; alcance mediante EDT y requisitos; cronograma mediante dependencias y recursos; costos mediante conciliación de G/H; calidad mediante criterios del Anexo F; recursos mediante responsables y calendario; comunicaciones e interesados mediante G.9; riesgos mediante la Tabla 6; y adquisiciones mediante los criterios de habilitación y presupuesto. Esta aplicación evita atribuir cumplimiento integral o certificación PMI al proyecto.

Una solicitud de cambio registra origen, motivo, entregables afectados, impacto en horas, fechas, caja y riesgos, decisión y versión. El responsable del frente analiza el impacto y el equipo resuelve el ajuste técnico; una fecha académica no se modifica sin la autorización correspondiente. El Capítulo XV conserva la comparación de versiones. El plan de comunicaciones de G.9 define destinatarios y frecuencia, sin atribuir comunicaciones o aprobaciones aún no realizadas.

### 6.2. Duración y cronograma

#### 6.2.1. Calendario, fechas y estimación

El desarrollo se programa desde el 11 de agosto hasta el 30 de noviembre de 2026. La entrega corresponde al 1 de diciembre, la defensa al 9 de diciembre y el inicio de la fase comercial al 1 de enero de 2027. El tramo del 2 al 9 de diciembre se reserva para preparación de defensa; la transición posterior se distingue de la entrega académica.

Cada integrante dispone de veinte horas semanales. El calendario nominal distribuye cuatro horas diarias de lunes a viernes, de 09:00 a 13:00, como unidad de programación de dedicación personal. No representa un horario contractual ni acredita trabajo en feriados. No se registran excepciones de disponibilidad en esta referencia; cualquier excepción efectiva requiere incorporarse y recalcular antes de usar el programa como compromiso de ejecución. Entre el 11 de agosto y el 30 de noviembre existen ochenta jornadas nominales: 320 horas por persona y 960 del equipo.

El esfuerzo se estima por juicio técnico y desglose de entregables, en bloques de cuatro horas. La duración de una actividad corresponde al esfuerzo dividido por cuatro cuando una persona concentra su ejecución; el tiempo calendario incluye fines de semana, liberaciones y esperas. Las fechas previas al corte son posiciones del programa reconstruido y no fechas reales verificadas. Los campos reales permanecen sin atribución hasta contar con registro por actividad.

#### 6.2.2. Programación, dependencias y recursos

El registro maestro contiene 63 nodos, con actividades y hitos de duración cero. La red utiliza relaciones fin a comienzo. La revisión de arquitectura puede comenzar con el alcance preliminar y se concilia después con requisitos; la documentación progresa durante los incrementos. Las compuertas reúnen frontend, backend y revisión. Las tareas W01/W02 conservan una liberación el 16 de noviembre para conciliar la decisión AWS documentada en el corte, sin trasladarla ficticiamente a agosto.

El cálculo determina fechas tempranas y tardías y holgura; después reproduce la secuencia de cada persona mediante vínculos de disponibilidad. El Anexo G distingue predecesoras lógicas y de recurso, verifica ausencia de ciclos y comprueba que ninguna persona supera cuatro horas diarias o veinte semanales. La selección de esta secuencia factible no demuestra que sea la única ni la óptima [@pmbok6, pp. 210–215].

**Figura 6**\
*Cronograma maestro del desarrollo, defensa y transición*

![](assets/figuras/gantt_maestro.png){width=16cm}

*Nota.* Elaboración propia a partir del modelo de programación de espaciGo. Las barras representan fechas programadas y no avance real.

#### 6.2.3. Ruta crítica y límites de factibilidad

El cierre del desarrollo se calcula para el 30 de noviembre de 2026 a las 13:00. La entrega se mantiene el 1 de diciembre. La holgura disponible en jornadas completas antes de esa entrega es cero. El tramo crítico del cierre reúne W01, W02, Q08, las ramas Q09 y R03, R04 y el hito C0. El Anexo G.5 presenta la red y la holgura de todas las actividades académicas. Las fechas de defensa e inicio comercial se tratan como hitos fijos; no se utilizan para inflar la holgura del trabajo académico.

La factibilidad es condicionada: una jornada adicional en W01 o W02 desplaza el cierre al 1 de diciembre y compromete la preparación previa a la entrega. La capacidad sin asignar no constituye reserva temporal en la ruta crítica y la reserva presupuestaria no compra automáticamente disponibilidad especializada. El control prioriza ese tramo, limita nuevas funciones y recalcula ante una ausencia o cambio. Las pruebas externas no terminadas se conservan como condiciones de habilitación; sus resultados no se sustituyen con un hito de calendario.

### 6.3. Equipo de trabajo

#### 6.3.1. Responsabilidad y revisión

El equipo está formado por Hernán Espinoza Castillo, Anita Marchant Pacheco y Erick Silva Quezada. La siguiente matriz sintetiza responsabilidad de coordinación; G.2/G.3 conserva la asignación por paquete y actividad.

**Tabla 7**\
*Asignación de responsabilidades del equipo*

| Frente | Hernán Espinoza Castillo | Anita Marchant Pacheco | Erick Silva Quezada |
| --- | --- | --- | --- |
| Gobierno, alcance y costos | C | A/R | C |
| Análisis y requisitos | C | A/R | R |
| Arquitectura, backend y datos | A/R | C | R |
| Frontend y experiencia | C | A/R | C |
| Calidad, seguridad y cronograma | R | C | A/R |
| Infraestructura y despliegue | R | C | A/R |
| Economía y preparación legal | C | A/R | C |
| Informe y defensa | R | A/R | R |

*Nota.* Elaboración propia. R: ejecuta; A: coordina la conformidad del frente; C: consulta. Cada fila tiene una sola A. La aceptación académica corresponde a la autoridad institucional.

#### 6.3.2. Esfuerzo y seguimiento

La programación asigna 228 horas académicas a Hernán Espinoza, 240 a Anita Marchant y 164 a Erick Silva: 632 en total. La preparación de defensa asigna doce horas a cada integrante, y la transición agrega doce, doce y dieciséis, respectivamente. El total del programa es 708 horas estimadas. El Anexo G.6 verifica carga y distribución semanal. Estas cifras no se presentan como horas reales ni como remuneraciones.

El registro de seguimiento identifica actividad, fecha de estado, esfuerzo real, esfuerzo restante, evidencia, revisión y fecha prevista de cierre. El avance se reconoce por entregable comprobado; una fecha pasada no acredita terminación. Sin línea base aprobada y medidas reales comparables, SPI, CPI y variaciones de ejecución se informan como no calculables. Los indicadores operativos del Capítulo XI mantienen su finalidad propia.

### 6.4. Plan de recursos

El trabajo utiliza equipos personales compartidos, repositorio, herramientas de desarrollo y entornos de ensayo. La capacidad nominal académica de 960 horas deja 328 horas sin asignar en esa etapa. El presupuesto de trabajo valorizado conserva 960 horas a CLP 6.500: CLP 6.240.000. Al asignar expresamente 76 horas a defensa y transición, el programa completo consume 708 horas valorizadas en CLP 4.602.000 y conserva una reserva presupuestaria de 252 horas, CLP 1.638.000. La capacidad libre académica y la reserva de todo el programa tienen bases temporales diferentes.

La valorización mide recursos del proyecto y se separa de pagos al equipo y del flujo de caja comercial. El Capítulo XIV y el Anexo H mantienen la inversión monetaria y los costos comerciales desde enero de 2027. La conciliación no modifica el flujo por convertir horas disponibles en egresos ficticios.

La planificación de adquisiciones identifica los servicios previstos, responsable, partida y prueba de aceptación en G.9. La arquitectura AWS y sus adaptadores se revisan como artefactos; la configuración regional, contratación, despliegue y aceptación externa siguen los controles del Capítulo XIII. La modalidad opcional de firma y los pagos requieren validación independiente de sus proveedores antes de habilitación.
