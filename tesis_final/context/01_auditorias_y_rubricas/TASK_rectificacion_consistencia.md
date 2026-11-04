# Tarea de rectificación de la memoria de espaciGo

**Estado:** rectificación documental verificada.

La auditoría compara dos versiones del PDF. Esta tarea contrasta los hallazgos con los archivos que entran en `document.json` y conserva como controles de regresión el alcance amplio, la secuencia de 14 figuras del cuerpo, las 35 historias y los 52 casos de uso.

## Fuente técnica y criterio de evidencia

El ADR `espaciGo/planning/decisiones/adr_objetivo_espacios_contratacion_cobros.md` se ratifica el 4 de noviembre de 2026. Su última versión registrada en Git es `4e26d52b57d9687c4b6b7a778e89dbbb5be855e5`. La copia de trabajo añade Inmuebles como novena categoría y lo vincula con `db/migrations/V000067__inmuebles_residential_rentals.sql`. El OpenAPI local incorpora `If-Match` para cambiar la portada. La evidencia local `planning/frontend_next/evidence/espacios-wizard-galeria-local-20261104.md` declara el corte en ejecución. Cada cambio en la memoria identifica si proviene del ADR, de una especificación versionada, de una modificación local o de un ensayo con resultado registrado.

El flujo objetivo comienza con identidad verificada de ambas partes y acuerdo de horario y precio. Sigue un bloqueo exclusivo, la emisión del contrato inmutable y la aceptación de ambas partes. Si se opta por SimpleFirma, se acreditan los aportes y se completan ambas firmas antes de habilitar la renta. La garantía, cuando corresponda y esté habilitada, se cobra por separado después de la renta. La confirmación exige todos los cobros aplicables. Al vencer se libera el bloqueo de forma atómica y el pago tardío se concilia sin reactivar la reserva.

## Cola de corrección

- [x] **R00 · Contraste inicial.** Identificar el ADR local y su diferencia frente a Git, localizar los hallazgos de la auditoría en las fuentes y definir pruebas de cierre.
- [x] **R01 · Capítulo VII y anexos A–C.** Corregir RQF-122 y HU30 para que la notificación de nueva solicitud preceda al acuerdo y al cobro. Alinear HU14, CU-47 y CU-51 con las etapas objetivo, dejando las enumeraciones históricas identificadas como tales cuando corresponda. Distinguir cancelación, vencimiento y conciliación. Cerrar cuando las fichas, tablas y diagramas vinculados coincidan con la secuencia del ADR y cada regla conserve su identificador.
- [x] **R02 · Capítulo VII y anexos A–C, mismo corte que R01.** Restituir en HU35 el check-in y el cierre del arriendo, con RQF-143–152, RQF-203–206 y CU-33, CU-34 y CU-48. Actualizar la tabla del capítulo, la ficha, el resumen y los vínculos de retorno en C. En HU19, cambiar RQF-226–231 por RQF-228–231 en ficha y resumen, conservando las demás referencias pertinentes. Añadir CU-23 a HU15 y CU-52 a HU26. Actualizar el conteo de 30 a 35 HU en A y eliminar los dos rastros de retroalimentación docente de A y C. Cerrar al comprobar las referencias en ambos sentidos y justificar cada relación por su contenido.
- [x] **R03 · Capítulo VII y anexos A–C, mismo corte que R01.** Unificar la estructura de las fichas HU17, HU18, HU23, HU33 y HU35 y ampliar sus criterios con condiciones comprobables. Completar las nueve filas de CU-01, CU-11, CU-12, CU-15, CU-16, CU-22, CU-24 a CU-32, CU-34, CU-39, CU-41, CU-42 y CU-48, con caso de uso, descripción y rótulos homogéneos. Comprobar 35 fichas HU y 52 tablas CU, revisar el enlace del capítulo con cada anexo y comprobar en el PDF las tablas ajustadas y las figuras afectadas.
- [x] **R04 · Capítulo V.** Sustituir la referencia a la pauta docente por el criterio metodológico aplicado. Corregir `tsrange` por `tstzrange` en la Tabla 5, riesgo R-01. Contrastar la mitigación con el Capítulo IX y el Anexo D. Verificar que la sección 5.3 y el Anexo G coincidan con el estado anterior.
- [x] **R05 · Capítulo VIII y Anexo E.** Diferenciar el OpenAPI fijado a Git, el ajuste local `If-Match` y el alcance observado en la evidencia del asistente de publicación y la galería. Verificar el catálogo de nueve categorías, el máximo de 30 posiciones de galería y el control de portada contra los contratos y las fuentes correspondientes. Conservar la distinción entre el catálogo de un artefacto histórico y el vigente.
- [x] **R06 · Capítulo IX y Anexo D.** Sustituir la referencia `f4bc7bd` como fuente única por la procedencia verificable del ADR y su actualización local. Contrastar Inmuebles y sus subtipos con V000067, y revisar ocupación exclusiva, titularidad, contrato inmutable, vencimientos, pagos y republicación en el cuerpo, figuras y mapeo físico. Usar 15 minutos para la ruta sin firma y 30/60/15 para aportes, firmas y renta en el ensayo con firma, con 15 adicionales para garantía habilitada. Identificar esos plazos como valores de ensayo. Regenerar cualquier figura incoherente desde su fuente editable.
- [x] **R07 · Capítulo X y Anexo F.** Contrastar las pruebas del recorrido con las correcciones del VII y IX. Distinguir check-in, checkout, confirmación, liberación del intervalo y pago tardío en casos trazables. Registrar como pendientes la habilitación de Mercado Pago para renta y comisión, SimpleFirma y la modalidad/proveedor de garantía monetaria según sus condiciones de validación. Mantener pendientes las pruebas integrales, de carga y de condiciones dependientes del código o del entorno objetivo. Conservar como evidencia acotada los ensayos locales que tengan resultados registrados.
- [x] **R08 · Referencias.** Revisar `referencias.bib` y las anotaciones del PDF. La URL de Ley 21.461 ya contiene `idNorma=1178004` en el fuente, y la auditoría anterior comprobó el destino íntegro. Revisar su presentación. Validar el destino de Ley 21.719 y comprobar el cambio de `i=1209272` a `idNorma=1209272` en la salida.
- [x] **R09 · Verificación transversal final.** Recorrer en orden todos los capítulos y los anexos para verificar remisiones, términos, numeración, tablas y figuras. Si aparece una discrepancia fuera del corte actual, abrir un ítem para su capítulo. Compilar con DocSkill, verificar índice y enlaces en PDF y revisar visualmente las páginas afectadas. Comprobar que V §5.3, XII, G y H conservan el contenido reservado y sus alertas. Cualquier observación tipográfica en esas zonas se registra para sus autores.

## Registro de entrega

Por cada corte se registra el estado, archivos y figuras corregidos, comandos y comprobaciones ejecutados, hallazgos pendientes y commit publicado en `origin/main`. Se trabaja con un capítulo activo y sus anexos asociados. Las referencias hacia otros capítulos se verifican durante el corte y las ediciones de esos capítulos se programan en su turno. Las figuras nuevas o reemplazadas conservan fuente editable, PNG, rótulo, título y nota. El Word y el PDF se generan con `python3 build_thesis.py`, con `--diagrams` si cambian fuentes de diagramas.

- **Capítulo VII y anexos A–C.** DocSkill y exportación PDF completados. Comprobados 35 identificadores HU, 52 fichas CU con nueve campos, trazabilidad de check-in y cierre, y páginas de muestra de la Tabla 7, HU35 y M08.

- Capítulo V. Tabla 5 y sección 5.1.3 corregidas, sección 5.3 comparada byte a byte y compilación DocSkill completada.

- Capítulo VIII y Anexo E. Contrato fijado, requisito local de portada y evidencia observada cotejados con OpenAPI, código y registro del ensayo. Compilación DocSkill completada.

- Capítulo IX y Anexo D. Contrastados V000067, las restricciones de ocupación, el ADR local y las ventanas del ensayo. Figura 8 regenerada desde PlantUML. Compilación DocSkill completada.

- Capítulo X y Anexo F. PT-04 y PT-08 alineados con los requisitos y la evidencia disponible. Compilación DocSkill completada.

- Referencias. Ley 21.461 y Ley 21.719 comprobadas en BCN y en las anotaciones del PDF. El primer enlace conserva su destino íntegro.

- Capítulo VII y Anexo C, revisión del chat de auditoría. Figura C.7 reemplazada, actores y relación de acuerdo conciliados con las fichas, y vencimiento modelado como proceso autónomo. Compilación DocSkill completada.

- Capítulo VIII y Anexo E, revisión del chat de auditoría. Confirmados los ocho valores del filtro local de búsqueda y los nueve perfiles del catálogo de producto. La selección de portada queda identificada en la prueba integrada dependiente del desarrollo.

- Capítulo V, verificación visual. Se redistribuye el ancho de las tablas 3, 4 y 5. Se conservan valoraciones, responsables y riesgos, y se verifica otra vez la integridad de 5.3.

- Capítulo VII y Anexo C. Las 52 fichas mantienen nueve atributos y asignan más espacio al detalle. Los pasos numerados conservan su separación en Word y PDF.

- Capítulo IX y Anexo D, revisión del chat de auditoría. Figura 11 regenerada desde Mermaid con cardinalidad de cero o una ocupación por reserva, según el núcleo de referencia. Se amplía la Figura 8 y se identifica el commit de V000067.

## Commits de los cortes

- Capítulo VII y anexos A–C. `7f20655`, `707eb00`, `fda4eb6`.
- Capítulo V. `10a7022`, `a9120e4`.
- Capítulo VIII y Anexo E. `e89224a`, `7dd56a5`.
- Capítulo IX y Anexo D. `6515fd7`, `77542e6`.
- Capítulo X y Anexo F. `f715d14`.
- Referencias. `b8c1ea1`.
- Maquetación transversal. `60689e0`.

- Cierre transversal. PDF de 497 páginas y render de Word revisados por muestras. Se comprueban 24 fuentes, 22 destinos del índice, 14 figuras y 12 tablas del cuerpo, 208 tablas DOCX, 236 RQF, 43 RNF, 35 HU, 52 CU y 16 PT. Las cuatro áreas reservadas se verifican byte a byte. Los pendientes de desarrollo y proveedores quedan en XI y F.

## Ajustes de la tercera revisión

Se uniforman los separadores de las valoraciones y los totales de la Tabla 3 en las páginas 30 y 31. HU22 utiliza las acciones de la etapa, modalidad y papel del participante en la página 139. La tabla de relaciones UML presenta R-12 antes de R-13 en la página 232.

La revisión visual de la página 70 confirma que la URL de la Ley 21.461 se muestra completa. El enlace del PDF y la relación del Word conservan el destino oficial. La grafía «SILVAJ» no aparece en el Capítulo XII ni en el PDF generado. Las cuatro áreas reservadas conservan sus fuentes.

## Plan de la cuarta revisión

- [x] Verificar y fijar la presentación del enlace de la Ley 21.461 en la salida.
- [x] Conciliar los anexos A–C con el ADR y revisar la separación de pasos.
- [x] Ajustar la EDT del Capítulo V y separar objetivos y trazabilidad en el IV.
- [x] Quitar la hoja preliminar vacía, incorporar índices de tablas y figuras y rehacer el resumen ejecutivo.
- [x] Mejorar la lectura de los capítulos editables y explicar las decisiones de concurrencia y procesamiento diferido.
- [x] Sustentar las conclusiones por objetivo con cifras y verificar Word, PDF, remisiones y áreas reservadas.

La salida PDF de 499 páginas comprueba los 22 destinos principales del índice de contenidos y los destinos de 20 tablas numeradas y 26 figuras. El Word conserva los campos de índice actualizables. La URL de la Ley 21.461 aparece íntegra en su propia línea. La revisión visual incluye los nuevos índices, el resumen y la referencia legal. Se verifica la integridad de V §5.3, XII y los anexos G y H. Los proveedores y las pruebas dependientes del desarrollo conservan su estado.

## Plan de revisión de figuras

| Corte | Figura anterior | Decisión y verificación |
|---|---|---|
| V §5.2.2 y §5.5.1 | EDT textual y Tabla 5 | Agregar árbol EDT con identificadores de los tres niveles y mapa de los cinco riesgos. Contrastar paquetes y coordenadas con sus fuentes. |
| VIII §8.1–8.3 | Cuatro cajas de vistas | Reemplazar por componentes Next.js, Go, puertos y adaptadores. Separar integraciones pendientes. |
| IX §9.1.2 | Actividad de contratación | Reemplazar por máquina de estados objetivo. Conservar el gráfico de ventanas, y distinguir vencimiento, cancelación, disputa y pago tardío. |
| IX §9.3.2 | Modelo lógico sin atributos | Conservar el modelo lógico y añadir una figura física con claves y tipos cotejados contra migraciones y Anexo D. |
| XI §11.2 | Topología genérica | Reemplazar por topología regional con ruta de entrega, Cloud Run, red privada, base y almacenamiento por finalidad. |
| Cierre | 14 figuras del cuerpo y 12 del Anexo C | Renumerar en orden de lectura y verificar destinos del índice, URL de la Ley 21.461 y secciones reservadas. |

La edición de cada diagrama se realiza en su fuente Mermaid o PlantUML. El segundo paso renderiza el PNG con `tesis_final/scripts/render_all_diagrams.py`. DocSkill incorpora la imagen con rótulo, título y nota. Las figuras organizacional y de trabajos futuros mantienen su función de síntesis.

### Entrega de figuras

| Figura | Resultado | Fuente editable |
|---|---|---|
| 4 | EDT de seis ramas y 28 paquetes de nivel 3. El desglose textual conserva los nombres completos. | `assets/diagramas_src/edt_paquetes.puml` |
| 5 | Grilla de probabilidad e impacto contrastada con los cinco riesgos de la Tabla 5. | `assets/diagramas_src/mapa_riesgos.mmd` |
| 8 | Componentes Next.js/BFF, entrada Go, módulos, puertos y adaptadores. | `assets/diagramas_src/fig07_arquitectura_togaf_capas.mmd` |
| 10 | Máquina de estados objetivo con bloqueo, cobros y salidas por vencimiento, cancelación y disputa. | `assets/diagramas_src/fig09_contratacion_objetivo.puml` |
| 14 | ERD físico del ensayo con claves, huella contractual, exclusión temporal y geografía sintética. Complementa la Figura 13. | `assets/diagramas_src/erd_fisico_ensayo.mmd` |
| 15 | Topología regional con Cloud Build, Artifact Registry, Cloud Run, rutas privadas y separación de almacenamiento. | `assets/diagramas_src/fig17_topologia_objetivo.mmd` |

Los seis PNG se guardan con el mismo nombre base en `assets/figuras/`. Se regeneran de forma selectiva pasando el nombre base al script de diagramas. La numeración del cuerpo se verifica del 1 al 17, con 12 figuras del Anexo C. La URL de la Ley 21.461 se verifica por su texto completo en una línea y por la anotación del PDF.

**Cierre verificado.** DocSkill genera un PDF de 503 páginas. Se comprueban 29 destinos del índice de figuras en una página, 20 del índice de tablas y 22 entradas principales del índice de contenidos. Se revisan visualmente las figuras nuevas y reemplazadas, y se comprueba la integridad de las cuatro áreas reservadas.

## Plan de pulido APA 7 posterior a la revisión de la versión 6

**Línea base:** commit `f0785cc`, PDF de 503 páginas. Plan aplicado y verificado en Word y PDF.

- [x] **APA-00 · Contrastar la auditoría.** La versión exportada contiene las 29 figuras y los rótulos numerados. La Figura 5 ya es un PNG generado desde PlantUML. Las tres URL de LeyChile y la de PostGIS conservan destinos íntegros. En las páginas 76–77, la Ley 21.461 se lee completa en una línea y `ST_DWithin.html` conserva el guion bajo. No se reproduce la hipótesis de un recorte por caracteres matemáticos. Las Figuras 8, 10, 14 y 15 ya se exportan a 300 ppp efectivos y el PDF utiliza compresión JPEG para esas imágenes.
- [x] **APA-01 · Preliminares.** Aplicar cursiva y dos puntos solo a la etiqueta «Palabras clave», conservar las cinco expresiones y retirar el punto final. Cotejar la pauta docente para el resumen ejecutivo. La guía APA de artículos indica un párrafo y un máximo habitual de 250 palabras, con posibilidad de requisitos institucionales distintos. Mantener el contenido y las métricas aprobadas. Cierre mediante revisión visual del resumen y su línea de palabras clave.
- [x] **APA-02 · Capítulo V.** Separar las listas de 5.1.1 y 5.2.1 de sus párrafos introductorios y convertir los dos paquetes de 5.2.3 en viñetas reales. Verificar la estructura de lista de Word y la separación vertical en PDF. Comparar §5.3 byte a byte con la línea base.
- [x] **APA-03 · Capítulo V y Figura 5.** Mejorar el mapa gráfico existente con ejes, leyenda de severidad y color de celda que pueda interpretarse junto con sus etiquetas. Conservar las cinco posiciones y comprobar puntuaciones y clases contra la Tabla 5. Mantener una fuente editable y un PNG en el flujo vigente.
- [x] **APA-04 · Figuras 8, 10, 14 y 15.** Priorizar texto interno más grande, menos saltos dentro de etiquetas y mejor uso del ancho útil. Probar compresión sin pérdida en una exportación de control y evaluar el efecto sobre claridad y tamaño. Regenerar los PNG desde sus fuentes cuando cambie el diseño. Cerrar con inspección al tamaño de lectura y al ampliar, comprobación de márgenes y revisión de rótulos, notas y anclajes. La densidad de píxeles se usa como control, junto con el tamaño efectivo del texto.
- [x] **APA-05 · Referencias.** Conservar los destinos verificados de LeyChile y PostGIS. Clasificar las fuentes por versión y estabilidad. Omitir la fecha de recuperación en la documentación estable y versionada, y conservarla para el contenido cambiante sin archivo. Si se conserva una fecha en español, emitir «Recuperado el …, de …» desde CSL y comprobar el alcance del cambio. Revisar sangría francesa y correspondencia cita–referencia por muestra, y cotejar el criterio institucional para legislación chilena. Cierre con lectura visual y comprobación de los destinos de Word y PDF.
- [x] **APA-06 · Control institucional y publicación.** La cuadrícula completa y el encabezado sombreado de las tablas responden a AGENTS.md. APA 7 recomienda limitar los bordes y evitar líneas verticales. Registrar esta diferencia y conservar el estilo institucional indicado. Revisar una muestra de los capítulos y anexos para comprobar números, títulos, notas y remisiones. Regenerar Word y PDF con DocSkill, comprobar los tres índices y la integridad de V §5.3, XII, G y H. Publicar el corte verificado en `main`.

Fuentes de contraste: [guía APA de resumen y palabras clave](https://apastyle.apa.org/instructional-aids/abstract-keywords-guide.pdf), [formato APA de tablas](https://apastyle.apa.org/style-grammar-guidelines/tables-figures/tables) y [referencias APA de páginas web](https://apastyle.apa.org/style-grammar-guidelines/references/examples/webpage-website-references).

**Resultado.** Se conserva el resumen ejecutivo de dos párrafos de la memoria y se corrige su etiqueta de palabras clave. Se verifican siete elementos de lista en Word, la clasificación de cinco riesgos y la máquina de estados completa. Las figuras se exportan sin pérdida. Las referencias usan sangría francesa y PostgreSQL 18 conserva sus enlaces versionados sin fecha de recuperación. El PDF tiene 503 páginas. Se comprueban 20 destinos de tablas, 29 de figuras y 22 entradas principales del índice de contenidos. Los cuatro apartados reservados conservan su contenido fuente.
