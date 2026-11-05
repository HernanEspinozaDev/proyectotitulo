# Plan de correcciones posteriores a la migración TIHI84

Línea base auditada: `53ef620`, PDF de 589 páginas, fuentes DocSkill y plantilla docente original. Se contrastan las observaciones de la revisión v6–v7 con la salida actual. La tabla de contraste conserva el diagnóstico inicial. Las casillas y el registro de ejecución documentan el cierre. Las páginas indicadas son las impresas en la línea base.

## Contraste con la salida actual

| Observación | Estado | Evidencia |
|---|---|---|
| Estructura, nombres y preliminares | Conforme | Los 18 capítulos mantienen el orden docente. Portada y hoja de aprobación muestran los apellidos primero. Resumen y Abstract están en xxiii y xxiv. El cuerpo reinicia en 1. |
| Listas de metodología y arquitectura | Conservar | Las listas de 6.1.1, 6.1.4.1 y 6.1.4.3 están separadas. La Figura 7 identifica el proceso BPMN objetivo. |
| Resumen y Abstract | Corregir | Faltan los cuatro conteos documentales. Los términos actuales son genéricos y están en la misma línea que el rótulo. La plantilla presenta «Palabras Claves» y «Keywords» como rótulos independientes. |
| Antecedentes y diagnóstico | Corregir | Los cuatro párrafos de 2.1.1.1 reproducen 8.1. La sección 2.1.1.2 solo remite al FODA. |
| Figura 5, Capítulo VI | Corregir | Ambas menciones de la nota apuntan a la Tabla 5, que es la matriz multicriterio. La Tabla 6 contiene los riesgos. |
| Tabla 10, Capítulo XI | Corregir | OE1 apunta a la Tabla 7 (RACI). OE4 apunta a la Tabla 8 (decisiones de arquitectura) y a la propia Tabla 10. Los destinos semánticos son la Tabla 2 para OE1 y las tablas 3 y 11 para OE4. |
| Jerarquía de títulos | Resolver según plantilla | La plantilla sí exige el encabezado de capítulo y, cuando figura en ella, su título interior. El tercer «Introducción» se confirma en 1.1. La jerarquía de XVI y XVII combina rótulos sin numerar y subtítulos decimales. El Capítulo XVIII y su encabezado interior «Anexos» existen también en la plantilla. |
| URLs de LeyChile y PostGIS | Conforme en la línea base | El texto visible en las pp. 71–72, los destinos PDF y el BibTeX contienen completos los enlaces de Ley 21.461, Ley 21.719 y ST_DWithin. La Ley 19.799 tiene su destino propio en la p. 71. Conservar y verificar tras recompilar. |
| Apartados económicos breves | Reservado | 14.2.1 y 14.2.2 son destinos de integración. Mantener rótulos, texto y bloques reservados del Capítulo XIV y el Anexo H. |
| Tecnologías en 9.2 | Ampliar | Hay explicación de roles y referencias a D, E y F. Falta una vista sintética que separe versión declarada, versión ensayada y componente previsto. |

## Tareas por corte

- [x] **R01 · Preliminares.** Incorporar la propuesta bilingüe de abajo. Contrastar conteos con anexos A–C, DDL y evidencia F5/F6 con D/F y Capítulo XII. Usar bloques separados para las palabras clave con los rótulos de la plantilla. Mantener paridad de cifras y alcance y revisar composición y destinos en ambos índices.
- [x] **R02 · Capítulos I–II y VIII.** Revisar I y eliminar la repetición textual de 1.1 mediante un subtítulo descriptivo si la matriz docente permite el cambio. En 2.1.1.1 exponer el origen de la iniciativa, la intermediación entre personas y organizaciones y las nueve categorías con arriendos por hora, día o mes. En 2.1.1.2 sintetizar los canales dispersos, la actualización manual de disponibilidad y la falta de trazabilidad antes de remitir a 8.4. Mantener Misión, Visión y Principios en 8.1. Cruzar el relato con Tabla 1 y Figura 1.
- [x] **R03 · Capítulos III–V.** Verificar catálogos e identificadores de A–C, correspondencia de tablas 2–3 y anexos con los objetivos de V, y citas de IV con XVII. Conservar contenido conforme. Las nueve categorías corresponden al alcance vigente del ADR, no a nueve segmentos de mercado ya validados.
- [x] **R04 · Capítulo VI y Anexo G.** Cambiar ambas remisiones de la nota de Figura 5 a Tabla 6. Comparar códigos y clasificación de riesgo con la figura y conservar el PNG si coincide. Preservar listas, Gantt y reservas de 6.2, XV y G.
- [x] **R05 · Capítulos VII, IX y X, anexos C, D y E.** Verificar que cada vista dirija al modelo, diagrama o anexo que desarrolla su contenido. En IX §9.2 agregar una tabla breve con Go, Next.js, PostgreSQL, PostGIS, OpenAPI, Docker y Cloud Build, con rol, versión o corte y estado. El repositorio local en `4289139` declara Go 1.27.1 y Next.js 16.4.3. Confirmar su pertinencia para el corte de la memoria antes de consignarlas. Separar PostgreSQL 18.6 ensayado, versión de PostGIS acreditada, contrato OpenAPI y herramientas de despliegue según evidencia. Si se inserta una tabla, revisar la numeración final en toda la memoria. Usar el ADR ratificado el 4 de noviembre como línea base y registrar los avances posteriores por evidencia y corte.
- [x] **R06 · Capítulos XI–XIII y Anexo F.** En la actual Tabla 10, OE1 debe remitir a trazabilidad inicial (Tabla 2) y OE4 a criterios de calidad y resultados por corte (tablas 3 y 11), además de F.1–F.3 según corresponda. Verificar los números en la compilación final y contrastar KPI, SLA y estados de pruebas con F. Mantener pendientes Mercado Pago, SimpleFirma, la definición y validación de verificación externa de identidad y representación cuando corresponda, garantía monetaria, carga de extremo a extremo y recuperación conjunta. Mantener separado el ensayo SQL local.
- [x] **R07 · Capítulos XIV–XV y anexos G–H.** Verificar cobertura de títulos y remisiones. Conservar íntegros los bloques de Anita Marchant Pacheco y Erick Silva Quezada, incluidos costos, recursos, adquisiciones, flujo, rentabilidad y cronograma detallado. Verificar que el estudio de mercado delimite la evidencia por segmento.
- [x] **R08 · Capítulos XVI–XVIII.** Probar una jerarquía uniforme en XVI (16.1 Conclusiones por objetivo, 16.2 Aporte de ingeniería, 16.3 Limitaciones y 16.4 Recomendaciones) y XVII (17.1 Glosario y 17.2 Referencias bibliográficas). Mantener reconocibles los rótulos docentes y sus destinos en el índice. En XVIII conservar «Anexos» y «Material Complementario (Apéndices)» con niveles coherentes y revisar el acceso a A–H. Verificar URLs visibles y clicables de las tres leyes y PostGIS en Word y PDF.
- [x] **R09 · Compilación y cierre.** Ejecutar `python3 build_thesis.py`. Validar los 18 capítulos y los tres índices, paginación romana y arábiga, correspondencia de todas las menciones afectadas con rótulos y destinos, legibilidad de figuras y tablas, referencias y bloques reservados. Registrar por capítulo y anexo qué se corrigió, qué se conservó y qué queda reservado. Publicar en `main` tras verificar Word y PDF.

Cada capítulo se corrige y se valida antes de pasar al siguiente. Los anexos y las secciones vinculadas se consultan para verificar cada cambio. Si la corrección exige editar otro capítulo, esa edición se realiza en su corte.

## Registro de ejecución

| Corte | Resultado |
|---|---|
| Preliminares | Se incorporan versiones de 219 palabras en español y 197 en inglés, con cifras equivalentes y un bloque de términos por idioma. El ensayo SQL identifica PostgreSQL 18.6 con PostGIS y el alcance sintético. |
| I, II y VIII | 1.1 pasa a «Propósito y alcance de la memoria». II desarrolla el origen de la intermediación y el diagnóstico con la Figura 1, la Tabla 1 y 8.4. VIII conserva la identidad estratégica. |
| III–V y anexos A–C | Se conservan el marco teórico, los objetivos y los catálogos. Se verifican 236 RF, 43 RNF, 35 HU y 52 CU y las remisiones al catálogo, a la arquitectura y a las pruebas. |
| VI y Anexo G | La nota de la Figura 5 remite dos veces a la Tabla 6. El diagrama se conserva porque sus cinco riesgos, puntuaciones y niveles corresponden a la matriz. |
| VII–X y anexos C–E | Se conservan las vistas, BPMN, modelos y catálogos. IX incorpora la Tabla 10 con roles, versiones declaradas por corte y distinción entre diseño, ensayo y configuración de despliegue. |
| XI–XIII y Anexo F | La matriz de control pasa a Tabla 11, los resultados por corte a Tabla 12 y los procedimientos operativos a Tabla 13. OE1 apunta a Tabla 2, OE4 a tablas 3 y 12 y OE5 a Tabla 13. F remite a Tabla 12. Se conservan los estados pendientes de proveedores y pruebas dependientes del desarrollo. |
| XIV–XV y anexos G–H | Se conservan los textos y apartados reservados. Los capítulos XIV y XV y los anexos G y H son idénticos a la línea base. |
| XVI–XVIII | XVI y XVII adoptan subtítulos decimales. XVIII conserva los rótulos docentes y la entrada de material complementario. Se comprueban los cuatro enlaces de LeyChile y PostGIS en Word y PDF. |

El PDF final tiene 590 páginas. Se verifica la paginación, los 18 destinos de capítulo, las 21 entradas del índice de tablas y las 30 del índice de figuras. La revisión visual se concentra en las páginas modificadas y en los índices. La Tabla 10 queda completa en la página impresa 36.

## Resumen propuesto

La dispersión de los anuncios, la incertidumbre sobre la disponibilidad y la coordinación manual dificultan el arriendo flexible de espacios en Chile. El proyecto diseña espaciGo, una plataforma web de intermediación para personas y organizaciones que ofrecen o arriendan espacios de uso residencial, turístico, recreativo, comercial e industrial. El catálogo contempla nueve categorías. Mediante un enfoque iterativo e incremental, el proyecto define una arquitectura hexagonal con Go, Next.js y PostgreSQL con PostGIS. El diseño incorpora búsqueda geográfica, control de solapamientos de reservas y aceptación bilateral del contrato, con firma electrónica opcional.

La especificación reúne 236 requerimientos funcionales, 43 no funcionales, 35 historias de usuario y 52 casos de uso. El inventario DDL identifica 110 tablas de aplicación, de las cuales 104 coinciden por nombre con la captura local V000075. El corte F5 registra 86 pruebas aprobadas de verificación documental y F6 registra seis pruebas aprobadas en los perfiles de borrador y documentos. En un ensayo aislado con datos sintéticos, 200 conexiones completan 42.636 consultas geoespaciales en 15 segundos sin fallos, con una latencia media de 70,22 ms. La propuesta establece reglas verificables para buscar, reservar y contratar espacios. La validación de carga de extremo a extremo, la recuperación conjunta de datos y archivos y la habilitación de proveedores quedan pendientes en el entorno objetivo.

**Palabras Claves**

Arriendo flexible de espacios, arquitectura hexagonal, concurrencia espaciotemporal, PostgreSQL, PostGIS.

## Proposed abstract

Scattered listings, uncertain availability, and manual coordination complicate flexible space rental in Chile. The project designs espaciGo, a web platform that connects individuals and organizations offering or renting residential, tourism, recreational, commercial, and industrial spaces. The catalog covers nine categories. The project uses an iterative and incremental approach and defines a hexagonal architecture with Go, Next.js, and PostgreSQL with PostGIS. The design supports geographic search, prevents overlapping bookings, and records acceptance by both parties, with an optional electronic signature.

The specification includes 236 functional requirements, 43 nonfunctional requirements, 35 user stories, and 52 use cases. The DDL inventory identifies 110 application tables, 104 of which match the V000075 local snapshot by name. The F5 verification run records 86 passing document verification tests, and F6 records six passing tests across the draft and document profiles. In an isolated test with synthetic data, 200 connections complete 42,636 geospatial queries in 15 seconds without failures, with a mean latency of 70.22 ms. The proposed design establishes verifiable rules for searching, booking, and contracting spaces. End-to-end load validation, joint recovery of data and files, and provider enablement remain pending in the target environment.

**Keywords**

Flexible space rental, hexagonal architecture, spatiotemporal concurrency, PostgreSQL, PostGIS.
