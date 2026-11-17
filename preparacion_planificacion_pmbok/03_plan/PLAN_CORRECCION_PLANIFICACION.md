# Plan de corrección de planificación y carta Gantt de espaciGo

**Fecha:** 16 de noviembre de 2026.
**Objetivo:** completar la planificación académica, reconstruir la Gantt y sincronizarla con la evaluación económica, conservando la plantilla institucional de la tesis.

## 1. Decisiones rectoras

| Decisión | Criterio de trabajo |
|---|---|
| Inicio académico | **11 de agosto de 2026**, confirmado por el propietario. |
| Dedicación del equipo | **20 horas semanales por integrante**, tres integrantes; confirmación recibida durante esta revisión. |
| Entrega de proyecto e informe | **1 de diciembre de 2026**. Debe identificar versión de código, informe y evidencia de ese corte. |
| Continuación tras la entrega | Se mantienen ajustes y desarrollo para la defensa hasta el **9 de diciembre de 2026**, como tramo diferenciado. |
| Defensa | **9 de diciembre de 2026**. Es un hito distinto de la entrega y del lanzamiento comercial. |
| Fase comercial | Desde el **1 de enero de 2027**. El Año 0 económico permanece en 2026 y el horizonte operativo en 2027–2030. |
| Base de la Gantt | Reutilizar el inventario y los incrementos de Erick; reconstruir fechas, recursos, vínculos y criterios. No se conserva su calendario de 2009–2010. |
| Referencia metodológica | Utilizar la **sexta edición, PMI 2017**, que corresponde al PDF entregado, para los procesos y páginas revisados. La referencia existente a la séptima se distingue y se conserva solo donde respalde el contenido citado. |
| Adaptación académica | Gestión basada en prácticas PMBOK y desarrollo iterativo e incremental. No convertir los grupos de procesos en fases consecutivas ni presentar PMBOK como una metodología única de programación. |
| Responsabilidad de edición | El propietario autoriza elaborar y corregir la planificación, incluida la parte antes reservada. Esa autorización permite sustituir los marcadores de 6.2 y G al integrar contenido real, sin inventar aprobación de terceros. |
| Presentación | Mantener capítulos, encabezados, plantilla TIHI84, estilos, notas e índices. Gantt sintética en el cuerpo y detalle legible en G. |

El diagnóstico se desarrolla en `02_diagnostico/MATRIZ_BRECHAS_PMBOK.md`. La conciliación de fechas y costos está en `02_diagnostico/CONCILIACION_TIEMPOS_Y_COSTOS.md`.

## 2. Qué falta realmente

La tesis dispone de metodología, EDT, riesgos, RACI y evidencia técnica. La ampliación debe concentrarse en:

1. Una definición compacta de gobierno y de aceptación de entregables.
2. El diccionario completo de los 28 paquetes de la EDT y su correspondencia con actividades.
3. Un calendario que respete disponibilidad, fechas académicas y comienzo comercial.
4. Un modelo único de actividades, dependencias, esfuerzo y responsables, con red y holguras comprobables.
5. Seguimiento que distinga programación, ejecución respaldada y cambios, sin reconstruir una aprobación histórica inexistente.
6. Un registro operativo de riesgos, comunicaciones, interesados y cambios, adaptado al tamaño del equipo.
7. La relación entre el trabajo académico, el presupuesto valorizado y los desembolsos del negocio.
8. Figuras y tablas legibles, reproducibles y coherentes con el anexo.

No se requiere reproducir todos los procesos ni todas las plantillas del PMBOK. Se deben justificar las prácticas seleccionadas y mostrar su aplicación al proyecto (PMI, 2017, p. 28 / PDF 64).

## 3. Secuencia de tareas y criterios de cierre

Las tareas se ejecutan en orden. Una tarea solo se marca terminada cuando existe el entregable y supera su comprobación. El estado editable se conserva en `estado_tareas.json`.

| ID | Tarea | Entregable y criterio de finalización | Dependencia |
|---|---|---|---|
| P01 | Revisar la fuente PMBOK y su edición. | Referencia verificada, huella del PDF y mapa de páginas de los temas utilizados. **Completada en este corte.** | — |
| P02 | Contrastar tesis, Gantt y evaluación económica. | Matriz B01–B21, diagnóstico de tiempos/costos y fechas rectoras confirmadas. **Completada en este corte.** | P01 |
| P03 | Definir la adaptación de gestión y el mapa de entregables. | Cuadro de prácticas aplicadas, ficha de gobierno, alcance de entrega/defensa y arquitectura documental. Diferencia entre acta del proyecto y constitución societaria. | P02 |
| P04 | Completar EDT y diccionario. | Los 28 paquetes quedan descritos y vinculados a actividades, responsables, aceptación y evidencia. Si se revisa un paquete, se registra el motivo y su relación con el alcance anterior. | P03 |
| P05 | Consolidar calendario y registro maestro. | Fechas 11-08, 01-12, 09-12 y 01-01; recursos con nombre y disponibilidad; actividades con ID estable, esfuerzo, duración, tipo y criterio de aceptación. Evidencia histórica separada de estimaciones. | P04 |
| P06 | Reconstruir la Gantt y comprobar su factibilidad. | Red sin ciclos, cierres vinculados, calendario consistente, cálculos de ruta/holgura y control de sobrecarga. Fechas objetivo contrastadas con el resultado; ninguna demora se oculta cambiando un rótulo. | P05 |
| P07 | Conciliar cronograma y evaluación económica. | Matriz de horas/costos, tratamiento del tramo posterior a entrega y reemplazo de la ventana antigua de 360 h. Sin cambios injustificados en caja, comisión o impuestos; recálculo de indicadores si cambia una partida pertinente. | P06 |
| P08 | Preparar Gantt, red y figuras editables. | Fuentes de datos, código generador, SVG/PNG y exportación compatible con Project. Vistas legibles al tamaño de la plantilla, no capturas extensas reducidas. | P06–P07 |
| P09 | Corregir el Capítulo VI y su Anexo G. | Metodología, EDT, riesgos, 6.2, equipo y recursos completos; anexo con detalle y remisiones verificadas. Se retiran sus marcadores de reserva al integrar el contenido. | P03–P08 |
| P10 | Corregir el Capítulo XV y sincronizar las secciones relacionadas. | Registro de cambios, cronograma vigente y cortes de entrega/defensa. V, XI–XIV, XVI, XVIII y H coinciden con el plan. Referencias PMBOK correctas. | P09 |
| P11 | Compilar y realizar revisión documental completa. | DocSkill genera Word/PDF; índices y numeración coinciden; figuras legibles y tablas completas. Revisión de páginas modificadas y comprobaciones de integridad de las demás secciones. | P10 |
| P12 | Publicar y entregar el corte para revisión. | Fuentes, informe, Gantt y verificación versionados en `main`; Word/PDF completos enlazados y registro claro de lo integrado y de las comprobaciones que dependen del desarrollo. | P11 |

## 4. Cómo se utilizará la Gantt de Erick

Se conserva como antecedente y como inventario de actividades. La nueva carta se construye con trazabilidad a sus ID; no se presenta una simple sustitución del año como corrección suficiente.

### Elementos recuperables

- Secuencia general por incrementos y módulos.
- Separación de backend y frontend.
- Hitos académicos como concepto, reemplazando sus fechas inconsistentes.
- Duraciones como estimaciones iniciales para contrastar con recursos y alcance.

### Elementos por reconstruir

- El calendario de 117 días que actualmente va de 2009 a 2010.
- Las 24 dependencias, en particular los seis extremos sin sucesoras y la defensa desconectada.
- Los cierres que dependen solo del frontend y omiten integración o backend.
- Las asignaciones al recurso sin nombre y las horas que no se concilian con los campos de tarea.
- Los nombres y criterios que conservan GCP, BigQuery, FirmaVirtual, escrow e integraciones no habilitadas.
- La identificación de pruebas, implantación, documentación y aceptación por incremento.

Se verifican los módulos y decisiones contra la tesis y el corte vigente del repositorio, sin cambiar arquitectura ni desplegar recursos durante este trabajo documental.

## 5. Construcción del modelo de cronograma

### Registro mínimo por actividad

ID estable; paquete EDT; fase o incremento; entregable; descripción; responsable; recursos de apoyo; esfuerzo en horas-persona; duración calculada; calendario; predecesoras y tipo de relación; restricciones y fechas límite; fecha programada; inicio/fin real si existe evidencia; avance acreditado; referencia de evidencia; criterio de aceptación; costo valorizado; desembolso y partida económica cuando corresponda.

### Reglas de cálculo y control

1. La duración se obtiene del esfuerzo, la dedicación y el calendario aplicable. No se confunden veinte horas semanales con una jornada de ocho horas diarias.
2. Se incluyen actividades de análisis, diseño, construcción, pruebas, documentación y corrección por incremento. Las reuniones y gestión consumen capacidad del mismo equipo.
3. Los hitos tienen duración cero y predecesoras coherentes. Un rótulo no sustituye una restricción o fecha límite.
4. Se calcula la red y su ruta crítica; después se revisan los límites de recursos y la nivelación. El CPM por sí solo no valida disponibilidad de personas (PMI, 2017, p. 210 / PDF 246).
5. Se evalúan contingencias y el efecto de retrasos en actividades críticas. Monte Carlo no es obligatorio ni se emplean probabilidades inventadas.
6. Si el resultado no cabe antes de la fecha comprometida, se informa la diferencia y se documenta la medida: redistribución válida, cambio de secuencia, revisión del esfuerzo o ajuste de alcance acordado. No se inventan avances ni se superponen tareas incompatibles para que la figura parezca cumplir.
7. El registro separa el corte de entrega del 1 de diciembre de la versión posterior utilizada para la defensa del día 9.
8. El comienzo comercial del 1 de enero se conserva como frontera del modelo económico; las condiciones de habilitación operativa mantienen su verificación propia.

### Evidencia y línea base

El tramo agosto–fecha de corte se reconstruye con entregables, documentos, versiones y pruebas disponibles. Cuando no existe una fecha real precisa, se identifica esa limitación; no se rellena con una fecha ficticia ni se supone que todo empezó de nuevo porque el MPP registra 0 %.

La nueva programación debe identificar su fecha de elaboración y la reconstrucción histórica utilizada. No se afirma que el equipo aprobó en agosto una línea base que no se conserva. La línea base se fija y versiona a partir del acuerdo real que exista para el plan; los cambios posteriores se registran.

El control mínimo utiliza hitos, actividades aceptadas y trabajo restante. SPI, CPI o valor ganado solo se calculan si existen alcance, presupuesto temporal y datos de avance/costo apropiados. Una valorización de horas no es un costo efectivo pagado.

## 6. Integración sección por sección

| Ubicación | Modificación prevista |
|---|---|
| V, 5.2.2 | Completar registro de interesados y conectar expectativas con aceptación y comunicaciones. Mantener alcance y objetivos del producto. |
| VI, 6.1 | Corregir edición y citas, justificar adaptación, distinguir grupos de procesos y fases de software. Conservar la matriz de elección, revisando que sus argumentos reflejen la aplicación real. |
| VI, 6.1.4 | Conciliar EDT y diccionario, diferenciar entregables y actividades, y remitir a las fichas completas del Anexo G. Revisar las afirmaciones que hoy dan por completo un diccionario no integrado. |
| VI, 6.1.5 | Ampliar riesgos con dueño, disparador, respuesta, reserva y seguimiento. Precisar las escalas y regenerar el mapa si cambian las valoraciones. |
| VI, 6.1, subsección complementaria | Presentar gobierno, comunicaciones, configuración y control de cambios en un bloque compacto. Evitar un plan separado y extenso por cada área del libro. |
| VI, 6.2 | Incorporar horizonte académico/comercial, calendario, hitos, Gantt maestro, ruta crítica y reglas de actualización. Es la principal sección por completar. |
| VI, 6.3 | Mantener RACI y nombres correctos; añadir asignación por actividad, disponibilidad y método de registro de esfuerzo. |
| VI, 6.4 | Relacionar recursos, presupuestos y adquisiciones con el cronograma; distinguir equipos compartidos, trabajo valorizado y gastos efectivos. |
| XI | Incorporar seguimiento del proyecto separado de KPI de operación comercial y SLA; mantener los límites de la evidencia técnica. |
| XII–XIII y F | Relacionar pruebas y habilitación con actividades, hitos y aceptación. No convertir pruebas pendientes en resultados aprobados por aparecer en la Gantt. |
| XIV y H | Sincronizar fechas y esfuerzo; sustituir H.5 y sus fuentes que conservan la ventana de seis semanas hasta diciembre. Mantener el formato del flujo y sus datos salvo cambios justificados por la conciliación. |
| XV, 15.1 | Desarrollar comparación entre antecedente recibido, reconstrucción y programa vigente; causas de ajuste, impacto, respuesta y versiones de entrega/defensa. Mantener el nombre del capítulo y la sección de la plantilla. |
| XVI | Actualizar conclusiones y limitaciones de planificación: qué está programado, qué evidencia existe y qué depende de pruebas o habilitaciones. |
| XVII | Incorporar PMBOK sexta edición 2017; diferenciarla de la séptima y utilizar páginas correctas. Evitar bibliografía duplicada dentro del anexo. |
| XVIII y G | Sustituir la reserva por el anexo de planificación, con su estructura detallada y referencias desde VI/XV. Actualizar la organización de anexos. |

No se renumeran los capítulos ni se reemplaza la plantilla. Los nuevos rótulos de figuras y tablas se concilian con la numeración correlativa ya utilizada, incluidos los cuadros económicos, sin modificar sus cifras.

## 7. Formato de Gantt y entregables visuales

El cronograma maestro del cuerpo debe comunicar el período agosto–diciembre de 2026, los hitos del 1 y 9 de diciembre y la frontera comercial del 1 de enero de 2027. Se mostrarán paquetes o incrementos, no decenas de actividades diminutas.

El detalle se distribuye en el Anexo G por fases o ventanas temporales, manteniendo los mismos ID, calendario y datos. La especificación de generación y legibilidad se encuentra en `ESPECIFICACION_GANTT_Y_ANEXO_G.md`.

Se entregarán datos y código editable, imágenes insertables y un archivo Microsoft Project XML compatible. No se promete generar un MPP nativo con una herramienta que solo exporta otros formatos.

## 8. Sincronización con el estudio económico

El intervalo del **11 de agosto al 30 de noviembre** contiene dieciséis semanas. A 20 h semanales por integrante, la capacidad nominal conjunta es **960 h**. Esto ofrece una correspondencia con la valoración de **CLP 6.240.000** del estudio económico, sin acreditar horas ejecutadas ni garantizar factibilidad de todas las actividades.

La entrega del 1 de diciembre se representa como hito. Las horas necesarias para entregar, mejorar el producto y preparar la defensa se identifican en el tramo correspondiente. La preparación posterior de operación comercial también se identifica por separado. Si estos trabajos modifican la valoración total o implican pagos, se refleja el efecto en la memoria económica y se recalculan las series afectadas.

El plan no utilizará las 960 h para ocultar horas adicionales ni sumará las 1.320 h de la carta original sin revisar su alcance. Tampoco mantendrá la capacidad antigua de 360 h hasta el 31 de diciembre como si correspondiera al plazo académico recién confirmado.

## 9. Criterios de cierre del plan de corrección

- Las fechas rectoras coinciden en cronograma, capítulos, anexos y fuentes generadoras.
- Todos los paquetes y actividades tienen trazabilidad; los entregables necesarios condicionan sus hitos.
- Cada asignación identifica una persona y calendario, sin sobrecargas ocultas.
- Los cálculos de duración, holgura, esfuerzo y costo se pueden reproducir.
- La entrega del 1 de diciembre, la defensa del día 9 y la operación desde enero no se confunden.
- El modelo de horas y la evaluación económica coinciden por alcance y etapa, sin doble conteo.
- Se conserva el formato del flujo de caja y la plantilla institucional.
- Las verificaciones se adaptan al alcance autorizado: los registros anteriores de integración económica conservan sus huellas históricas, y las comprobaciones nuevas aceptan la edición de VI/G y la renumeración necesaria sin eliminar la comparación de cifras.
- Gantt y red se leen en la página final, con fuentes y código editables conservados.
- Las secciones de planificación antes reservadas están completas; las verificaciones dependientes del desarrollo conservan su estado verificable.
- Word y PDF se compilan con DocSkill, sus índices están actualizados y el corte queda publicado en `main`.

## Estado de esta entrega

Este corte **completa el análisis y el plan**, con las fechas y dedicación confirmadas. La ejecución comienza en P03 y se sigue por capítulo y anexo. La tesis y el MPP recibido conservan todavía su contenido mientras se prepara esa corrección; no se presenta este plan como una Gantt ya reconstruida.

## Ejecución del plan

La aplicación desarrolla las tareas P03–P12 con el registro actualizado en `estado_tareas.json`. Las 21 correcciones y sus destinos se documentan en `../04_ejecucion/CIERRE_DE_BRECHAS.md`. La programación mantiene explícitos el margen temporal cero, el calendario nominal y la ausencia de horas reales por actividad. Las verificaciones de estructura, finanzas, XML y Word/PDF se conservan junto a los entregables; las tareas se cierran con esas evidencias.
