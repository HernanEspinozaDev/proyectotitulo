# Revisión de la carta Gantt de Erick para espaciGo

**Fecha de revisión:** 16 de noviembre de 2026.

**Archivo revisado:** `espacigo.mpp`, recibido en `/home/nandev/Descargas/espacigo.mpp`.

**Resultado:** la organización por incrementos sirve como base, pero el archivo **requiere correcciones antes de integrarse como cronograma vigente en la tesis**. Las principales diferencias están en las fechas, los hitos, la red de dependencias y el alcance tecnológico.

La revisión lee las tareas y propiedades internas de Microsoft Project mediante MPXJ. El archivo original no se modifica, no se reprograman actividades y no se sustituyen los apartados reservados de la tesis.

## 1. Qué contiene el archivo

| Elemento | Resultado de la lectura |
|---|---|
| Nombre interno del proyecto | `msproj11` |
| Inicio almacenado | 11 de agosto de 2009, 08:00 |
| Fin almacenado | 20 de enero de 2010, 19:00 |
| Duración del proyecto | 117 días laborables |
| Registros de tareas | 34, incluido el resumen general ID 0 |
| Filas sin el resumen general | 33: 7 fases resumen, 22 actividades y 4 hitos |
| Dependencias | 24, de fin a inicio, con desfase cero |
| Recursos con nombre | 0; existe un registro de recurso sin nombre |
| Asignaciones | 26; sus campos de trabajo suman 1.320 horas |
| Avance registrado | 0 % en todas las tareas |
| Fechas de inicio o fin real | No registradas en las tareas extraídas |
| Línea base con fechas | No registrada |
| Fecha de estado | No registrada |
| Moneda del proyecto | Euro: `€`, código `EUR` |
| Calendario base | Lunes a viernes, 09:00–13:00 y 15:00–19:00; 8 horas diarias y 40 semanales |

Las fechas de 2009–2010 aparecen en las actividades y en las propiedades del cronograma. **No se deducen únicamente de la fecha de creación del archivo.** Los metadatos indican un guardado en octubre de 2026, pero eso no actualiza las fechas programadas.

El 0 % registrado tampoco demuestra que el proyecto real no haya avanzado: indica que este archivo no contiene una actualización de avance que permita acreditarlo.

## 2. Aspectos que se pueden conservar

- La separación en inicio, identidad y acceso, oferta y búsqueda, reservas y pagos, contratación y operación, reputación/disputas y cierre.
- La identificación de actividades de backend y frontend.
- La presencia de módulos M01–M11 y de hitos de evaluación.
- Las duraciones de actividad como estimaciones iniciales para revisar con sus responsables.
- La utilización de dependencias explícitas. La extracción no detecta ciclos ni incumplimientos cronológicos en los vínculos de fin a inicio existentes.

Esta base se relaciona con el enfoque iterativo e incremental del Capítulo VI. Para completar esa correspondencia, cada incremento necesita una integración verificable, pruebas y un criterio de cierre.

## 3. Correcciones prioritarias

### G01. Fechas fuera del período del proyecto — prioridad crítica

Las actividades están programadas entre agosto de 2009 y enero de 2010. La tesis utiliza preparación en 2026 y operación desde enero de 2027. Es necesario definir la fecha real de inicio y distinguir las actividades ya ejecutadas del trabajo restante.

**Acción recomendada:** corregir la fecha del proyecto y su calendario, registrar el avance respaldado y recalcular la red. No basta con cambiar el texto del año ni desplazar todas las barras sin revisar los hitos.

Si se trasladaran las fechas diecisiete años, conservando el mismo patrón, el cierre seguiría llegando al 20 de enero de 2027. Esa observación no constituye una nueva programación aprobada ni demuestra que la defensa de diciembre o el lanzamiento de enero sean factibles.

### G02. Fechas de hitos diferentes de sus nombres — prioridad crítica

| ID de Project | Hito y fecha indicada en su nombre | Fecha programada en el archivo |
|---|---|---|
| 14 | Primera entrega: «3 de Noviembre» | 19 de octubre de 2009, 19:00 |
| 23 | Segunda entrega: «17 de Noviembre» | 7 de diciembre de 2009, 19:00 |
| 28 | Tercera entrega: «1 de Diciembre» | 30 de diciembre de 2009, 19:00 |
| 33 | Entrega y defensa: «Semana del 15 de Diciembre» | 11 de agosto de 2009, 08:00 |

Los nombres de estos hitos no incluyen año. Incluso antes de resolver ese año, los meses y días programados no coinciden con los rótulos.

**Acción recomendada:** confirmar las fechas del calendario académico y registrarlas como fechas límite o compromisos apropiados, con predecesoras y holgura verificables. Un texto que menciona una fecha no impide que Project programe el hito en otra.

### G03. Hito final desconectado — prioridad crítica

El ID 33 no tiene predecesoras. Está programado al inicio del proyecto y figura dentro de la fase de cierre como WBS `10.4`, aunque su nombre comienza con «11 Hito Final».

Esto provoca que la fase resumen ID 29, denominada cierre, comience también el 11 de agosto de 2009 y abarque 117 días, mientras sus actividades de administración, pruebas y documentación se sitúan entre diciembre y enero.

**Acción recomendada:** enlazar la entrega/defensa con los entregables que exige su cierre y revisar su ubicación en la jerarquía. El hito final debe representar la culminación de los trabajos requeridos.

### G04. Actividades importantes que no condicionan la entrega — prioridad alta

Las siguientes actividades no tienen sucesoras:

| ID | Actividad | Holgura total almacenada |
|---|---|---|
| 3 | Arquitectura y decisiones ADR | 107 días |
| 8 | Backend de verificación de identidad | 92 días |
| 12 | Backend de búsqueda y cotización con PostGIS | 72 días |
| 17 | Integración de Mercado Pago | 52 días |
| 21 | Backend de check-in/check-out con evidencia | 34 días |
| 26 | Backend de disputas y liquidación | 17 días |

Por ejemplo, el hito ID 14 depende del frontend ID 13, pero no tiene como condición el cierre del backend de búsqueda ID 12. La continuación del bloque de pagos depende del frontend ID 18 y no exige cerrar la integración ID 17. El mismo patrón se repite en otros incrementos.

Las barras pueden terminar antes del hito en la programación actual, pero **la red no garantiza que sigan siendo requisito de cierre si esas actividades se retrasan**.

**Acción recomendada:** crear hitos de incremento integrado y verificado que reúnan las dependencias necesarias de backend, frontend, pruebas y proveedores cuando correspondan. No se propone encadenar artificialmente todo: los vínculos deben reflejar la dependencia real del entregable.

### G05. Ruta crítica incompleta respecto del cierre — prioridad alta

El archivo marca como críticas estas filas no resumidas:

`2 → 4 → 6 → 9 → 11 → 13 → 14 → 16 → 18 → 20 → 22 → 23 → 25 → 27 → 28 → 30 → 31 → 32`

Sus duraciones suman 117 días laborables. El recorrido termina en documentación, ID 32, y no en el hito final ID 33.

**Acción recomendada:** recalcular la ruta crítica después de corregir fechas, dependencias y cierre. El resaltado de Project describe la red que contiene el archivo; no valida por sí mismo que esa red incluya todas las condiciones necesarias para entregar el proyecto.

## 4. Diferencias con las decisiones vigentes de espaciGo

| ID o bloque | Contenido de la Gantt | Ajuste recomendado para alinearlo con la tesis |
|---|---|---|
| 4 | Docker y pipeline CI/CD en GCP. | Actualizar a la construcción y entrega en AWS. Separar preparación del entorno, calidad, despliegue y validación del destino. |
| 21 | Evidencia fotográfica en «Cloud Storage». | Referir el adaptador de almacenamiento y S3 del diseño vigente, incluyendo permisos y acceso a la evidencia. |
| 30 | Auditoría inmutable en BigQuery. | Vincular la tarea al mecanismo de auditoría definido por el proyecto. No sustituir BigQuery por CloudWatch automáticamente: observabilidad y auditoría de aplicación no son equivalentes. |
| 20 | FirmaVirtual y firma electrónica avanzada. | Alinear con la contratación bilateral y la firma opcional prevista con SimpleFirma. Diferenciar el recorrido sin firma de la integración externa y sus verificaciones. |
| 15 y 17 | Reservas/pagos «Escrow», tokenización y retención de fondos. | Planificar el recorrido previsto de Mercado Pago, OAuth del vendedor y Split 1:1. Mantener la garantía y cualquier mecanismo de retención como alcance condicionado a definición y pruebas. |
| 26 | Arbitraje de garantía y payout como parte ordinaria del bloque. | Separar las funciones del recorrido base de las integraciones o condiciones de garantía todavía no habilitadas. |
| 8 | KYC/KYB «con Registro Civil y SII». | Distinguir la validación propia de la plataforma de una integración externa. El nombre de la tarea no debe dar por disponible una API, un convenio o una habilitación. |
| 11 y 13 | Publicaciones, calendario, catálogo y mapa sin un criterio explícito del catálogo vigente. | Incluir en la aceptación las nueve categorías y el perfil de atributos correspondiente; mantener la unidad reservable exclusiva del alcance vigente. |
| 17 y 18 | Pago sin detallar el criterio económico del proyecto. | Incorporar como aceptación la comisión neta del 3 % más IVA por pago, descontada al publicador junto con el cargo de pasarela, y la conciliación de conceptos. |

La tesis mantiene pendientes las habilitaciones de proveedores y las pruebas que dependen de completar el código. La Gantt puede y debe planificar ese trabajo, pero debe distinguir **desarrollo, ensayo controlado y habilitación real**, sin presentarlos como integraciones ya operativas.

## 5. Recursos, esfuerzo y seguimiento

### No hay responsables identificados en Project

Existe un registro de recurso sin nombre y 26 asignaciones. Las asignaciones se muestran al 100 %, pero no identifican a Hernán, Anita o Erick. Por ello, el archivo no permite verificar la distribución real de responsabilidades ni la sobrecarga de cada integrante.

Los ID 3 y 4, por ejemplo, coinciden en fechas y contienen asignaciones al 100 %. Es necesario distribuirlas entre responsables y disponibilidad real antes de interpretar esa simultaneidad como viable o como sobrecarga individual.

**Recomendación:** registrar los tres integrantes con calendarios de disponibilidad acordados y asignar cada tarea. La asignación debe ser coherente con los roles de la matriz RACI del Capítulo VI.

### Las horas necesitan conciliación

Los campos de trabajo de las asignaciones suman **1.320 horas**, mientras que los campos de trabajo de las tareas leídos del archivo muestran cero. Esa diferencia debe revisarse en Project y conciliarse antes de utilizar el esfuerzo como respaldo de costos o avance.

La evaluación económica utiliza **960 horas de desarrollo preoperativo valorizado**. Los 1.320 h de la Gantt cubren también preparación, pruebas y documentación. **No se puede afirmar que la diferencia sea un sobrecosto probado:** primero hay que mapear los alcances y distinguir duración, esfuerzo planificado y trabajo ejecutado.

El calendario base representa 40 horas semanales y las asignaciones están al 100 %. Debe revisarse su relación con la dedicación parcial utilizada en la valoración económica y con la disponibilidad real de cada persona.

### Falta una base de seguimiento actualizada

No se encuentran fechas de línea base, fecha de estado ni inicios/finales reales en la extracción. Todas las tareas muestran 0 %.

**Recomendación:** registrar una fecha de corte y actualizar con evidencia las tareas realizadas y el trabajo restante. La línea base debe reflejar un plan acordado. Sin ella no corresponde afirmar variaciones contra una planificación aprobada ni calcular indicadores de desempeño basados en una referencia inexistente. El número de commits no equivale automáticamente a horas trabajadas o porcentaje completado.

### Moneda y título del archivo

La configuración utiliza `EUR`/`€` y el nombre `msproj11`. Antes de vincular costos con la evaluación económica, corresponde revisar moneda, tarifas y unidades para trabajar coherentemente con CLP. Cambiar el símbolo no convierte importes de una moneda a otra.

## 6. Cobertura de etapas y entregables de la tesis

La estructura actual representa incrementos de construcción, pero requiere una correspondencia explícita con las ramas de la EDT del Capítulo VI. Los códigos WBS de Project y los de la tesis no deben darse por equivalentes únicamente porque contengan números.

| Elemento de la tesis | Situación en la Gantt | Complemento recomendado |
|---|---|---|
| Planificación y gobierno | Fase inicial con requerimientos, arquitectura y entorno. | Vincular línea base, riesgos, control de cambios y responsables con los entregables de gestión. |
| Análisis y diseño | Requerimientos y ADR concentrados en el inicio. | Identificar modelado de datos, seguridad, contratos de interfaz y criterios de aceptación según el alcance de cada incremento. |
| Construcción iterativa | Está representada por bloques de módulos. | Conservar la base y añadir integración y verificación por incremento. |
| Pruebas | ID 31 reúne UAT, estrés y correcciones en cinco días al final. | Diferenciar pruebas unitarias/integración, aceptación, carga y recuperación; planificar correcciones y repetición de los ensayos. |
| Implementación | «Despliegue final» aparece en el nombre de la fase resumen, sin una actividad hoja específica de despliegue productivo. | Incorporar despliegue del piloto, configuración, comprobación operativa y criterio de aceptación, con responsables y dependencias. |
| Continuidad y ciberseguridad | No se distinguen tareas específicas de restauración conjunta y verificación RPO/RTO. | Relacionar los ensayos necesarios con los capítulos XII–XIII y el Anexo F. |
| Evaluación económica | No se identifica una actividad específica equivalente al paquete financiero de la EDT. | Relacionar el entregable ya integrado en XIV/H con su fecha y evidencia, sin volver a planificarlo como si no existiera. |
| Informe y defensa | Existen los ID 32 y 33. | Vincularlos entre sí y con los requisitos reales de entrega; diferenciar aceptación académica y preparación operativa. |

El objetivo de lanzamiento en enero de 2027 y las entregas académicas necesitan hitos distintos. La defensa no implica que todos los proveedores estén habilitados, y el fin de desarrollo no sustituye la validación operativa del piloto.

## 7. Orden recomendado para corregirla

1. Confirmar fecha de inicio, calendario académico, fecha de estado y objetivo de lanzamiento. Conservar una copia del MPP recibido.
2. Identificar lo ejecutado con evidencia y separar lo restante; no reiniciar todo el trabajo como pendiente por el 0 % del archivo.
3. Actualizar los nombres y el alcance de las tareas que conservan GCP, BigQuery, FirmaVirtual, escrow o integraciones no habilitadas.
4. Corregir la jerarquía y las dependencias de los hitos, especialmente el ID 33 y los cierres de incremento.
5. Completar la relación con la EDT y añadir los entregables de pruebas, implementación y evaluación que correspondan al alcance.
6. Asignar responsables, disponibilidad y esfuerzo, y conciliar las horas con el estudio económico.
7. Recalcular fechas, holguras y ruta crítica; contrastar el resultado con las fechas límite antes de fijar una línea base aprobada.
8. Exportar una vista legible y las tablas de respaldo. Solo después, integrar el resumen en **6.2**, la comparación de ajustes en **15.1** y el detalle en el **Anexo G**.

## 8. Evidencias y alcance de la revisión

- `01_extraccion/INVENTARIO_TAREAS.md`: todas las filas con ID, WBS, fechas, duración, predecesoras y holgura.
- `01_extraccion/extraccion_normalizada.json`: campos leídos para tareas, recursos y asignaciones.
- `01_extraccion/proyecto_mpxj.json`: exportación del modelo leído por MPXJ.
- `01_extraccion/resultados_auditoria.json`: conteos y comprobaciones de la red.
- SHA-256 del archivo recibido: `5140243dc56e6c7555ef9e7b0899b7e2ee11f9f12ac7b067d3116191ed5ba2a3`.

Contraste documental: Capítulo VI, Capítulo XIII, Capítulo XIV, Capítulo XV, Anexos F–H y correcciones docentes conservadas en el repositorio. La extracción usa MPXJ 16.10.0 y JPype1 1.7.1. El método de lectura sigue la [documentación oficial de MPXJ](https://www.mpxj.org/howto-start/).

Esta revisión verifica lo que contiene el archivo y su coherencia documental. No certifica fechas institucionales, avance real, aceptación de responsables o disponibilidad contractual de proveedores. **El MPP y los apartados de Gantt de la tesis permanecen sin cambios.**
