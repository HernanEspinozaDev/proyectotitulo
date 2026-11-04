# Plan de revisión por capítulo y publicación de espaciGo

**Fecha:** 4 de noviembre de 2026.  
**Ejecución:** el chat principal integra y publica. Cada chat de capítulo realiza una auditoría de solo lectura con GPT-6 Luna y conserva sus hallazgos. La edición se realiza en orden, con un solo corte activo. Un anexo compartido se modifica en el corte propietario de la regla y se revisa en los capítulos que lo citan.

## Regla de alcance ratificada para la revisión

espaciGo facilita la publicación y el arriendo flexible de espacios ofrecidos por personas y organizaciones. El alcance objetivo admite usos residenciales y turísticos, recreativos, comerciales e industriales. Los ejemplos incluyen casas de veraneo, hostales, quinchos, parcelas, oficinas, locales, bodegas y estacionamientos. La oferta depende del tipo de espacio, la modalidad y las reglas que le correspondan. La figura de una unidad reservable exclusiva se conserva como regla del ADR vigente. El alojamiento con inventario compartido, capacidad o múltiples unidades requiere especificar su alcance por separado antes de atribuirle soporte.

La revisión mantiene tres estados diferenciados: alcance objetivo, categorías y flujos efectivamente implementados en un corte, y evidencia de ensayo. La inclusión de casas u hostales en el alcance objetivo no implica que el catálogo vigente del código los admita ni que sus requisitos operativos estén ya verificados. La evidencia de vacancia de oficinas se conserva como ejemplo de un segmento, sin extrapolarla a alojamiento o industria.

## Cortes y anexos

| Corte | Anexos y materiales de contraste | Resultado esperado |
|---|---|---|
| 00. Preliminares | Manifiesto, portada, resumen, índice | Título, resumen y metadatos consistentes con el alcance amplio. Pendientes editoriales identificados. |
| I. Introducción | A y B, contraste de categorías y HU05 | Dominio amplio, sujetos oferentes y diferencia entre datos sectoriales y alcance del producto. |
| II. Diagnóstico | F, Tabla 1 y Figura 1 | Problema transversal, proceso de referencia y trazas a pruebas. |
| III. Marco teórico | D y E, bibliografía y Figura 2 | Conceptos conectados con decisiones. Citas y URLs verificables. |
| IV. Objetivos y negocio | A, B y H, Tabla 2 | Objetivos, segmentos y ejemplos alineados. H permanece reservado. |
| V. Metodología | G, EDT, tablas 3–5 | Tono académico, cálculo y responsabilidades coherentes. 5.3 y G permanecen intactos. |
| VI. Arquitectura empresarial | C, D y E, Tabla 6 | Funciones, actores y vistas consistentes con los distintos tipos de oferentes. |
| VII. Requisitos | A, B y C, tablas 7 y 8 | Conciliar 236 RQF, 43 RNF, 35 HU y 52 CU según su significado. Normalizar cabeceras y fichas. |
| VIII. Arquitectura TI | D y E, Tabla 9 | Módulos, contrato versionado y límites de lo implementado. |
| IX. Procesos y datos | A–E, figuras de flujos y modelo | Reglas de titularidad, galería, bloqueo, firma, cobros y alcance por tipo. Separar 110 tablas derivadas y 104 tablas observadas en V75. |
| X. Calidad | F, Tabla 10 | Evidencia LOCAL-1, F5/F6 y pruebas posteriores con sus límites. Conciliar PT-01 a PT-16. |
| XI. Despliegue y seguridad | D, E y F, Tabla 11 | Alinear operación y controles con evidencia por entorno. |
| XII. Evaluación económica | H y referencias desde IV, IX y XI | Auditoría de enlaces y estado de integración. Edición reservada a Anita Marchant y Erick Silva. |
| XIII. Control | A, F y G, Tabla 12 | Cobertura por objetivo, cambios y estado. G permanece intacto. |
| XIV. Conclusiones | A–F y referencias desde XII, figura de ruta | Cierre por objetivo, alcance amplio y límites probados. |
| Referencias y cierre de formato | Manifiesto, citas, tablas, figuras y PDF | Numeración correlativa y remisiones actualizadas, referencias APA, verificación del hipervínculo en el PDF y control visual. |

## Prompts operativos

### A. Coherencia y evidencia

Audita únicamente el capítulo asignado y las partes pertinentes de sus anexos. Entrega una tabla con ubicación exacta, fragmento, discrepancia, fuente y corrección propuesta. Comprueba los identificadores por significado y no solo por existencia. Contrasta límites de galería, plazos, estados, firma, garantía, reclamos, retención, categorías y derechos por recurso. Usa el alcance amplio indicado arriba y distingue los ejemplos del catálogo implementado. Clasifica cada afirmación como objetivo, implementada, ensayada o diferida. Señala cualquier afirmación que requiera evidencia externa o ejecución en un entorno autorizado.

### B. Fichas y residuos históricos

Busca etiquetas ES1, ES2, evaluaciones, notas de corrección y decisiones obsoletas. Conserva su trazabilidad en el contexto histórico y propone lenguaje de memoria final. Para HU identifica épica, rol, prioridad, historia, criterios positivos y negativos y RQF/CU. Para CU identifica actor, precondiciones, flujo principal, alternativas, postcondiciones y traza. Prioriza HU17, HU18, HU23, HU33 y HU35 y las fichas CU-01, CU-11, CU-12, CU-15, CU-16 y CU-22. Mantén IDs estables. Los bloques reservados se identifican sin editarlos.

### C. Estilo, tablas y referencias

Audita tercera persona, presente y tono técnico. Revisa título, rótulo, nota, referencia en el texto y vínculo con el anexo de cada tabla o figura. Señala saltos y remisiones afectadas. La renumeración se aplica en un solo corte global al cerrar el contenido. Para referencias distingue un salto visual de línea de una URL realmente truncada en el hipervínculo. Identifica marcadores pendientes y clasifica los reservados.

## Verificación y publicación por corte

1. Revisar el diagnóstico del chat y comparar con las fuentes de desarrollo y el ADR. El chat auditor entrega propuestas. El chat principal edita las fuentes y registra los cambios.
2. Revisar el diff de un capítulo y sus anexos propietarios. Comprobar IDs, rótulos, imágenes, citas y contenido reservado. Compilar con `python3 build_thesis.py` cuando cambian fuentes compiladas y verificar una muestra del PDF y las entradas afectadas del índice.
3. Comparar `main` con `origin/main`, incluir únicamente archivos del corte, crear el commit, subir a `origin/main` sin reescribir historial y comprobar el SHA remoto. Registrar el SHA y el estado de las comprobaciones en el chat del capítulo o en el registro central.
4. Pasar al capítulo siguiente tras verificar el corte anterior. Los chats de auditoría trabajan en paralelo sobre una misma instantánea y sus conclusiones se vuelven a contrastar si otro corte cambia una fuente compartida.
