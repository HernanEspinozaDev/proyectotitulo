# Revisión independiente del cronograma espaciGo

**Fecha de revisión:** 16-11-2026
**Alcance:** lectura de `tesis_final/assets/diagramas_src/cronograma_espacigo.json`, `preparacion_planificacion_pmbok/04_ejecucion/calculo_cronograma.json` y `Cronograma_espaciGo_Project.xml`; comprobación independiente del XML mediante MPXJ/JPype y revisión de la lógica del generador.
**Límite:** esta revisión evalúa consistencia del programa estimado. No atribuye ejecución, avance ni horas reales.

## Dictamen

La estructura de alto nivel es consistente en recuento y esfuerzo: 28 paquetes EDT, 63 filas planificadas (54 actividades y 9 hitos), y 708 horas estimadas en total. Los hitos declarados son 1 de diciembre de 2026 (entrega), 9 de diciembre (defensa) y 1 de enero de 2027 (comienzo comercial). La fecha de inicio de la programación es 11 de agosto de 2026. El modelo explicita que es una referencia y mantiene los campos reales vacíos; la revisión no infiere avance histórico.

Hay una observación de plazo que conviene resolver antes de presentar el programa como calendario comprometido: el modelo asigna el cierre académico C0 al 30 de noviembre, con margen calculado de **cero jornadas** respecto de la entrega del 1 de diciembre. Se llega al hito, pero cualquier indisponibilidad adicional durante la ruta crítica desplaza la entrega. Además, aunque el campo general declara fin base 30 de noviembre, las fechas de inicio de actividades se nivelan contra ese corte solo mediante dependencias; no existe holgura de calendario que absorba cambios.

## Comprobaciones cuantitativas

- Los 28 paquetes tienen actividades asociadas y las horas por paquete coinciden con la suma de sus actividades. Total: 708 h.
- Distribución de los paquetes por responsable (estimación de todo el modelo): H 252 h, A 264 h y E 192 h. Distribución por etapa: base académica 632 h, preparación de defensa 36 h y transición 40 h.
- Para la etapa base, el cálculo declara capacidad de 320 h por persona (4 h/día, lunes a viernes, entre el inicio y el 30-11); el esfuerzo asignado es H 228 h, A 240 h y E 164 h. No se sobrepasa la capacidad semanal ni la diaria bajo el calendario nominal. La capacidad de equipo indicada para la base es 960 h; quedan 328 h no asignadas frente a la capacidad y 252 h frente al presupuesto valorizado de 960 h para el total de 708 h. Son magnitudes distintas y el JSON las distingue.
- La diferencia entre el origen MPP declarado (1.320 h de asignaciones, 33 filas) y las 708 h del modelo actual es material. El manifiesto la identifica como origen y no como horas del programa vigente; conviene conservar explícita esa conciliación para que nadie interprete 1.320 h como esfuerzo de esta versión.
- El hash SHA-256 del JSON de tesis coincide con `modelo_sha256` en el cálculo (`2a027663…c4ac2117b`), por lo que el cálculo corresponde a la fuente examinada.

## Dependencias y CPM

- No se detectaron predecesoras lógicas inexistentes ni ciclos en el grafo declarado. Se incorporan 31 vínculos de secuencia de recursos; no se encontró vínculo de recurso que duplique una predecesora lógica.
- El cálculo informa como ruta crítica nivelada `W01 → W02 → Q08 → (Q09 y R03 en paralelo) → R04 → C0`, con fin el 30-11-2026 a las 13:00. CPM lógico y nivelado coinciden en fecha final y ruta crítica en esta versión. Es coherente con el margen cero para ENT.
- La salida CPM tiene terminal académico C0. Los hitos posteriores ENT, DEF y COM y las actividades de defensa/transición no reciben holgura CPM (`null` en el JSON); por ello, la ruta crítica y holguras publicadas no describen CPM del programa completo hasta el comienzo comercial. Las fechas de esos tramos se generan por liberaciones y compromisos fijos.
- La comprobación de hitos fija ENT 01-12, DEF 09-12 y COM 01-01-2027 no demuestra holgura positiva: la regla solo exige que la actividad llegue antes o en su fecha objetivo. DEF tiene dos jornadas nominales completas entre el término previsto de las actividades de preparación (04-12) y el hito (09-12), y la transición termina el 15-12, con amplio espacio hasta COM; ese espacio no se convierte en holgura calculada.
- El 01-01-2027 es viernes y feriado legal; además, es obligatorio e irrenunciable para dependientes del comercio, con las excepciones previstas por ley ([Ley 19.973, BCN](https://www.bcn.cl/leychile/Navegar?idLey=19973)). El XML exporta todos los días de lunes a viernes como laborables y no incorpora excepciones. Como COM es un hito de fecha, esto no altera duración de trabajo modelada antes del hito; sí vuelve engañosa la representación del inicio comercial como jornada laborable y puede afectar cualquier tarea que se programe ese día. Registrar el calendario de feriados/no disponibilidad que corresponda y recalcular, sin presumir trabajo en feriado.

## Calendario y fechas

- La fecha inicial programada del primer trabajo es 11-08-2026, a las 09:00. El calendario de referencia representa lunes-viernes, cuatro horas diarias entre 09:00 y 13:00, equivalente a 20 h por semana/persona.
- El calendario tiene `excepciones: []`; por tanto, no modela feriados, vacaciones ni indisponibilidades. El propio texto del modelo advierte que no se presume trabajo en feriados, pero las fechas calculadas sí asumen disponibilidad en todo día hábil nominal. Esto no es una prueba de que las actividades ocurrieran en esas fechas. Si el objetivo es un calendario comprometido, falta una lista de excepciones y su recálculo.
- La programación base cierra C0 el 30-11; ENT cae al día hábil siguiente. DEF está fijada al 09-12. La transición se ubica del 10 al 15-12, antes del hito COM 01-01-2027. La secuencia no contiene una actividad entre defensa y comienzo comercial que se extienda al 31-12; no se debe leer ese intervalo como trabajo programado ni como avance.

## Exportación XML / interoperabilidad

- MPXJ leyó el XML correctamente: 63 tareas, 3 recursos y 54 asignaciones; fechas de proyecto 11-08-2026 09:00 a 01-01-2027 09:00. El XML conserva el calendario semanal de 09:00–13:00 de lunes a viernes y presenta los hitos con fecha.
- El XML es una lista plana: todas las tareas llevan `OutlineLevel=1`; el campo `WBS` contiene el ID de actividad (por ejemplo, `G01`), no el código EDT del paquete. El código EDT queda en `Notes` y en la fuente JSON, pero no queda utilizable como jerarquía/WBS en Project. La representación puede dificultar agrupar y revisar los 28 paquetes en MS Project u otra herramienta que dependa de WBS.
- El XML crea enlaces de predecesor para dependencias lógicas y de recursos con tipo Finish-to-Start. La secuencia de recursos es, por tanto, exportada como dependencia obligatoria; al editar o recalcular el archivo en otra herramienta, esos enlaces pueden fijar una secuencia más restrictiva que la red lógica original.
- La exportación define `FinishDate` de proyecto como 01-01-2027 y no estructura las actividades como tareas resumen de fase/paquete. El lector interpreta el XML y los valores guardados; esta verificación no ejecutó un recálculo nativo de Microsoft Project. Se recomienda comparar las fechas tras abrir/recalcular en el destino previsto antes de usar el XML como artefacto de control.

## Hallazgos priorizados

1. **Alto — margen nulo para entrega:** ruta crítica académica termina C0 el 30-11 y ENT está el 01-12. El calendario no reserva contingencia. Presentar como compromiso requiere explicitar aceptación del riesgo o revisar secuencias/esfuerzo y capacidad.
2. **Alto — días no laborables omitidos:** calendario vacío de excepciones, incluyendo feriados/no disponibilidad. Esto hace optimista cualquier fecha que dependa de esos días; COM cae el 01-01, feriado en Chile.
3. **Medio — CPM parcial:** CPM/holguras terminan en C0; el programa incluye además defensa, transición y comienzo comercial, pero esas etapas no tienen CPM de extremo a extremo.
4. **Medio — EDT se pierde en jerarquía XML:** XML plano con `WBS` de actividad y nivel 1; códigos de paquete solo en notas. El XML se parsea, pero la estructura EDT no se conserva para gestión jerárquica.
5. **Medio — conciliación de 1.320 h vs. 708 h:** se identifica el origen previo, pero conviene mantener una explicación de alcance/versionado visible junto al cronograma para evitar que se confundan asignaciones heredadas con estimación actual.

## Veredicto de avance

Los campos `inicio_real`, `fin_real` y `avance_real` se conservan nulos en la fuente y el cálculo indica explícitamente que el avance no se infiere. Los eventos de corte documentados no autorizan a convertir las fechas programadas en historial de ejecución. No se encontró en este examen una atribución de avance histórico derivada del cronograma.

## Resolución de exportación EDT (16-11-2026)

Se actualizó exclusivamente `export_xml` en `tesis_final/scripts/calcular_cronograma.py`. El XML regenerado queda con 28 tareas resumen, una por paquete EDT, en nivel 1 y con WBS igual al código del paquete; las 63 actividades/hitos quedan en nivel 2, con OutlineNumber y WBS jerárquico subordinado al paquete. Los UID de resúmenes se derivan del orden estable de paquetes y los de actividades del orden estable de IDs de la fuente; cada tarea actividad conserva además su ID de actividad y EDT en Notes. Las relaciones lógicas y de recursos siguen apuntando a los UID de actividad correctos. Las tareas resumen presentan inicio y término de sus hijos y Work cero; no reciben asignaciones. Las 54 asignaciones permanecen solo en las tareas ejecutables y suman 708 h.

Los nueve hitos actuales llevan un código EDT válido en la fuente, por lo que se agrupan en sus paquetes correspondientes. La exportación crea el resumen `Cierres` si posteriormente recibe hitos/filas cuyo EDT no exista entre los 28 paquetes.

**Validación posterior:** lectura XML directa y MPXJ/JPype. Ambos reconocen 91 tareas en total (28 resumen + 63 actividad/hito), dos niveles de jerarquía, 3 recursos y 54 asignaciones; el total de trabajo asignado es 708 h. Se verificó para cada resumen que sus fechas coinciden con el mínimo inicio y máximo fin de sus hijos, y que Work del resumen es cero. No se ejecutó `main()` ni se modificaron el cálculo JSON o el CSV; la regeneración invocó únicamente `export_xml` usando ambos JSON existentes. No se alteraron datos de avance real.

## Tratamiento en la integración académica

El cuerpo y G.1/G.5 explicitan el calendario como dedicación personal nominal, con excepciones por actualizar ante disponibilidad efectiva; no se afirma que sea calendario contractual ni que se haya trabajado en feriados. COM corresponde a una frontera del período financiero, con duración y esfuerzo cero, y no programa una jornada de trabajo el 1 de enero. El CPM publicado se delimita expresamente a C0 y los hitos posteriores conservan sus fechas fijas, sin atribuirles holguras calculadas. El margen cero se informa como riesgo alto, con revisión diaria del tramo crítico y limitación de funciones. Esta revisión no convierte la referencia reconstruida en compromiso histórico ni en línea base aprobada. La conciliación de 1.320 h de asignaciones de origen frente a 708 h estimadas se integra en XV y G.8.
