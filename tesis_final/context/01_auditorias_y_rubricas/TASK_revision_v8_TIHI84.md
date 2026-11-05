# Plan de correcciones de la revisión v8 de la memoria espaciGo

**Línea base:** `1917fdd`, PDF de 590 páginas. Este plan distingue los cambios pendientes de las observaciones que no se reproducen en la salida actual. Las páginas citadas corresponden a la numeración impresa de la línea base.

## Contraste inicial

| Observación | Comprobación | Decisión |
|---|---|---|
| Ajustes aceptados de la revisión anterior | Resumen y Abstract bilingües, antecedentes y diagnóstico, Tabla 10, referencias de las tablas 11–13 y jerarquía de I, XVI y XVII presentes. | Conservarlos y comprobar que sobreviven a la nueva compilación. |
| Ley 21.719 y PostGIS en 17.2 | En la p. 73 del PDF publicado aparecen completos `idNorma=1209272` y `ST_DWithin.html`. Las anotaciones del PDF contienen ambos destinos completos. El BibTeX ya conserva las URLs canónicas. | Reproducir la observación en la salida final y verificar texto visible y destino en Word y PDF. Cambiar la generación solo si se confirma una discrepancia. |
| Glosario 17.1 | La fuente y el texto extraído del PDF presentan viñetas y rayas. El cambio propuesto mejora la uniformidad. | Aplicar dos puntos a las nueve entradas y revisar las que ocupan más de una línea. |
| Rótulo del resumen, HU01 y encabezado de XVIII | Las tres observaciones se reproducen en las fuentes. | Aplicar los cambios puntuales y comprobar que mantienen la estructura y la trazabilidad. |
| KPI y SLA | XI describe los indicadores en prosa y remite a otros apartados para los umbrales. La Tabla 3 incluye RNF-001, RNF-009 y RNF-010. RNF-002 consta en el Anexo A, fuera de la selección actual de la Tabla 3. | Definir métricas reproducibles en 11.1 e incorporar los cuatro umbrales en 11.2, con su alcance y estado de verificación. |
| Aporte de ciberseguridad | X describe autorización por recurso e `If-Match`. XII y F delimitan la evidencia documental F5/F6 y registran que el ensayo GCP03 se detiene al restaurar permisos de aplicación. | Distinguir el diseño, la evidencia local y las validaciones pendientes al ampliar 16.2. |

## Tareas por capítulo y anexo

- [x] **V8-01 · Preliminares.** Cambiar el rótulo a «Palabras clave» en singular y conservar su bloque separado. Comprobar que el Resumen y el Abstract mantienen cifras y términos equivalentes y sus destinos en el índice.
- [x] **V8-02 · Capítulo III y Anexo A.** Cotejar RNF-001, RNF-002, RNF-009 y RNF-010 con el catálogo. Incorporar RNF-002 a la Tabla 3 con su evidencia exigida, ya que esa tabla sirve como síntesis de calidad. Preservar los identificadores y el texto del catálogo. Si el Anexo F carece de una medición específica del tiempo de acreditación interna, registrar esa comprobación como pendiente en el corte correspondiente.
- [x] **V8-03 · Capítulo V y Capítulo XI, sección 11.1.** Alinear 5.2.3 con los indicadores operativos de XI y distinguirlos de los indicadores comerciales complementarios. En XI definir conversión como reservas confirmadas por cada 100 recorridos de contratación iniciados, mediana de minutos desde la solicitud hasta el acuerdo y número de incidencias por cada 100 arriendos de la población definida. Para cada uno, indicar evento inicial y final cuando corresponda, fuente, período, segmento y población elegible. La cohorte de conversión debe poder asociar cada inicio con su resultado. Definir el tratamiento de denominadores iguales a cero. Usar «cotizaciones iniciadas» solo si ese evento existe, es trazable y se adopta expresamente como denominador. Mantener las fórmulas en texto legible y evitar afirmar resultados productivos sin medición.
- [x] **V8-04 · Capítulo XI, sección 11.2, y Anexo F.** Explicitar RNF-001 (búsqueda en hasta 2 s con 200 usuarios concurrentes, desde la confirmación de parámetros), RNF-002 (acreditación interna de renta en hasta 8 s, excluido el tiempo del proveedor), RNF-009 (disponibilidad mensual mínima de 99,9 % para funciones críticas) y RNF-010 (RPO de hasta 15 min y RTO de hasta 1 h). Distinguir objetivos técnicos y conformidad demostrada. Cotejar con la Tabla 3, resultados del Capítulo XII y procedimientos del XIII. Vincular PT-09 con búsqueda y PT-11 con recuperación. Para acreditación y disponibilidad, identificar la medición o el registro requerido según la evidencia disponible.
- [x] **V8-05 · Capítulo XVI, sección 16.2.** Añadir un párrafo de ciberseguridad y privacidad por diseño. Vincular autorización por recurso y por finalidad con X y XIII, `If-Match` con selección de portada y F5 con sus verificaciones documentales de escaneo, revocación, retención y permisos. Referir el límite observado de GCP03 y la comprobación pendiente tras la recuperación conjunta. Si se mencionan bcrypt de 12 rondas o AES-256, cotejar RNF-013/RNF-014 y exigir evidencia del corte y del componente para calificarlos como implementados. Describir la Ley 21.719 como marco de diseño y conservar el alcance de la evidencia.
- [x] **V8-06 · Capítulo XVII.** Uniformar las nueve entradas de 17.1 como viñetas con término y dos puntos en negrita, definición iniciada con mayúscula y punto final. En 17.2 comprobar la Ley 21.719 y `ST_DWithin` en el BibTeX, texto visible, destino de hipervínculo y PDF renderizado. Conservar el guion bajo literal en la URL canónica si pasa la prueba. Si se confirma un fallo, aislar la etapa que lo introduce y aplicar un ajuste localizado con verificación de regresión para las otras dos leyes.
- [x] **V8-07 · Capítulo XVIII y Anexo B.** Numerar el encabezado interior como «18.1. Organización de los anexos» bajo «CAPÍTULO XVIII: Anexos» y cotejarlo con los rótulos de evaluación. Preservar el acceso a A–H y a «Material Complementario (Apéndices)». En la quinta viñeta de HU01 retirar la aclaración «(no “activo”)» y comprobar que se mantienen el estado «No Verificado», el envío y reenvío del token y su correspondencia con HU02 y el caso de uso de registro.
- [x] **V8-08 · Compilación y cierre.** Ejecutar `python3 build_thesis.py`. Validar PDF y Word, inspeccionar las páginas modificadas y los saltos de página, y comprobar los destinos de los tres índices y los enlaces bibliográficos. Registrar el resultado por tarea, verificar por comparación los bloques reservados y publicar en `main` una vez validadas las salidas.

Las correcciones se aplican a un capítulo por vez, con verificación de sus anexos y remisiones. Los bloques reservados de Anita Marchant Pacheco y Erick Silva Quezada en 6.2, XIV, XV y anexos G–H conservan su contenido. La habilitación de proveedores y las pruebas dependientes del desarrollo mantienen su estado pendiente.


## Registro de ejecución

| Tarea | Resultado |
|---|---|
| V8-01 | «Palabras clave» queda como rótulo separado. Se conservan los dos resúmenes y sus cinco términos por idioma. |
| V8-02 | La Tabla 3 incorpora RNF-002 con trazabilidad al Anexo A. El catálogo de requisitos permanece intacto. |
| V8-03 | V distingue los indicadores operativos y comerciales. XI fija fórmulas, fuentes, población, ventanas de seguimiento y tratamiento de conjuntos vacíos. La conversión conserva como base los recorridos de contratación iniciados. |
| V8-04 | XI incorpora los cuatro umbrales. La Tabla F.4 explicita las comprobaciones pendientes de acreditación interna y disponibilidad mensual. |
| V8-05 | XVI documenta autorización por recurso y finalidad, control de concurrencia de la portada, evidencia local de F5 y el límite del ensayo GCP03. El texto conserva pendiente la comprobación de permisos tras la recuperación conjunta. |
| V8-06 | XVII uniforma las nueve definiciones. Se conservan las URLs canónicas de la Ley 21.719 y de PostGIS al reproducirse completas y con el destino correcto. |
| V8-07 | XVIII incorpora 18.1. HU01 conserva estado y token, elimina la aclaración residual y queda alineada con CU-01, CU-02 y HU02 en los datos de registro y el orden de verificación y acceso. |
| V8-08 | DocSkill genera Word y PDF. El PDF de 592 páginas verifica 18 destinos de capítulos, 21 de tablas y 30 de figuras. Se comprueban paginación, preliminares, enlaces bibliográficos y bloques reservados. La revisión visual de las páginas afectadas permite eliminar un salto que aislaba la remisión a la Figura 18. |
