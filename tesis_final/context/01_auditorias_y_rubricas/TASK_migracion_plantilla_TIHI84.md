# Plan de migración a la plantilla final TIHI84 Santiago Centro

**Estado:** migración implementada y verificada.\
**Línea base de espaciGo:** `f5b211d`, Word y PDF de 503 páginas.\
**Material docente:** «Plantilla Informe Final TIHI84 Santiago Centro_F_2026O.docx», «comparacion Formato de Informe.xlsx» y «Rúbrica Examen de Título.xlsx».

La plantilla Word fija la estructura y presentación de destino. La hoja **Informe Final** de la planilla contiene 95 rótulos, incluidos títulos de capítulo, encabezados internos y preliminares. La hoja **Informe comparativa** muestra correspondencias con entregas previas. Se utiliza para contrastar cobertura junto con las hojas **Informe 1** e **Informe2**. La rúbrica aporta criterios de exposición, demostración y defensa. Sus datos de ejemplo quedan fuera de los artefactos del proyecto.

## Diferencias comprobadas de formato

| Elemento | Plantilla docente | Memoria actual | Acción prevista |
|---|---|---|---|
| Orden y títulos | 18 capítulos de Introducción a Anexos. Los títulos incluyen un encabezado de capítulo y un encabezado interior cuando corresponde. | 14 capítulos temáticos, Referencias y ocho anexos. | Usar los rótulos y la jerarquía docente y ubicar los apartados adicionales dentro de cada capítulo. |
| Portada y aprobación | Dos páginas de identificación con carrera, nombre del proyecto, autores y guía. La portada incluye sede y fecha. La segunda página contiene firma y calificación. | Portada y hoja de aprobación con otra distribución. | Completar los campos con datos reales del proyecto. Los campos de firma y calificación quedan para la autoridad correspondiente. |
| Preliminares | Dedicatoria, Agradecimientos, Tabla de Contenido, Índice de Tablas, Índice de Figuras, Resumen y Abstract. | Hoja de aprobación, índices y resumen en español. | Crear los tres apartados faltantes y cambiar el rótulo del resumen. El Abstract traduce el resumen y conserva sus cifras y alcance. Dedicatoria y Agradecimientos se completan con texto de los autores. |
| Maquetación | Papel carta. Márgenes superior e izquierdo de aproximadamente 4 cm y derecho e inferior de 2,5 cm. Secciones diferenciadas, preliminares en romanos y reinicio a 1 en el cuerpo. | Papel carta, una sección, márgenes próximos a 2,5 cm e índice con numeración arábiga. | Derivar la referencia de DocSkill de una copia de la plantilla y probar anchos, saltos, encabezados, pies y numeración. |
| Índices | Tabla de contenido con niveles hasta 7 y listas de tablas y figuras. | Índice general hasta nivel 3 y listas generadas. | Adaptar los niveles y generar de nuevo los tres índices. Comparar el número impreso con el destino físico después del reinicio del cuerpo. |

## Matriz de migración por capítulo

Los números en «Origen actual» corresponden a la memoria antes de migrar. Los títulos de destino siguen la plantilla docente.

| Destino | Origen actual | Qué trasladar o completar |
|---|---|---|
| **I. Introducción** | I | Reubicar contexto, propósito y pertinencia. Conservar el alcance multisectorial y remitir al diagnóstico y objetivos bajo la nueva numeración. |
| **II. Identificación del Problema** | I, II y VI §6.1–6.4 | Crear 2.1 Actualización y justificación del problema con 2.1.1 Descripción de la organización, 2.1.1.1 Antecedentes, 2.1.1.2 Diagnóstico y 2.1.2 Descripción del problema. En 2.2 Justificación del problema, separar Relevancia y Complejidad. Distinguir la organización del proyecto y su situación documentada de los actores del mercado. |
| **III. Levantamiento de Requerimientos** | VII y anexos A–C | Nombrar 3.1 Especificación de Requerimientos (IEEE 830/1998) y 3.2 Especificación de Restricciones. Agregar inventario de restricciones verificables con origen y efecto. Conservar los identificadores y los catálogos íntegros. Trasladar indicadores al XI y el diagrama de actores al X donde corresponda. |
| **IV. Marco Teórico** | III | Reubicar las cinco secciones temáticas y sus citas. Conservar la explicación de puertos y adaptadores, persistencia, pagos y privacidad. |
| **V. Objetivos del Proyecto** | IV, II, VI y VII | En 5.1 Solución Tecnológica separar Formulación y Alcance y restricciones. En 5.2 Impacto de la solución distinguir Proceso de negocio afectado, Registro de interesados, Indicadores de gestión y Niveles de servicio. El registro de interesados se construye desde actores y funciones documentados. En 5.3 Objetivos del proyecto separar Objetivo general y Objetivos específicos. Conservar el Canvas como subsección adicional. Los indicadores y niveles de servicio se sintetizan aquí y se especifican en XI. |
| **VI. Metodología de trabajo** | V y G | Distribuir el enfoque híbrido, EDT y riesgos en 6.1 Metodología y Desarrollo de la solución. Incorporar 6.2 Duración y cronograma con el bloque reservado, 6.3 Equipo de trabajo con RACI y 6.4 Plan de recursos con recursos verificables y remisión al apartado financiero. |
| **VII. Definición de Arquitectura TI** | VIII §8.1, §8.4 y XI §11.2–11.3 | Sintetizar las decisiones de TI, sus límites y controles. Remitir a X para las figuras de detalle y a XIII para operación. |
| **VIII. Reconocimiento de Arquitectura Empresarial** | VI | Conservar identidad estratégica, objetivos, estructura funcional, FODA y vistas. Referenciar los antecedentes de II desde el análisis organizacional. |
| **IX. Detalle de las Tecnologías a implementar** | III, VIII, IX y XI | Crear 9.1 Análisis cualitativo/cuantitativo con criterios comparables, fundamentos y métricas que tengan evidencia. Crear 9.2 Herramientas, aplicaciones, lenguajes y componentes con rol, versión o corte cuando conste y estado de implementación. La comparación distingue datos medidos de criterios de diseño. |
| **X. Detalle de la Arquitectura a implementar** | II, VII, VIII, IX, XI y anexos C–E | 10.1 Diagrama BPMN se incorpora con fuente y render propios, cotejado con el ADR. Las actividades UML y la máquina de estados se conservan como complemento. 10.2 Diagrama de casos de uso conserva la vista de actores y remite al Anexo C. 10.3 Diagrama de componentes reutiliza el esquema Next.js/Go. 10.4 Modelo de datos distingue Modelo lógico, Modelo Físico y Diccionario de datos del Anexo D. 10.5 Topología de comunicaciones identifica rutas y límites de red. 10.6 Diagrama de Infraestructura reutiliza la topología GCP. 10.7 Diagrama de Arquitectura presenta una vista integrada y remite a los diagramas especializados. |
| **XI. Implementación de los KPI y SLA** | VII §7.3–7.4, X, XIII y anexos A/F | Crear 11.1 Descripción de KPI y 11.2 Descripción de SLA. Cada KPI identifica fórmula, fuente y periodicidad. Cada SLA identifica umbral, ventana, método y estado de verificación. Conservar el control de avance y trazabilidad del XIII actual como ampliación de este capítulo. |
| **XII. Plan de Pruebas y Aseguramiento de Calidad** | X y Anexo F | Crear 12.1 Plan de Pruebas y 12.2 Normas y Estándares. Conservar los casos, evidencias por corte, límites y pruebas pendientes del desarrollo. Este capítulo recibe calidad, mientras el capítulo financiero actual pasa a XIV. |
| **XIII. Plan de Implementación** | XI y X | Crear 13.1 Gestión de Disponibilidad, 13.2 Gestión de Continuidad y 13.3 Plan de Mantención. Reubicar CI/CD, seguridad, recuperación, procedimientos y condiciones de habilitación. Completar mantención con responsabilidades, cadencias, disparadores y evidencias verificables, identificando las medidas propuestas. |
| **XIV. Factibilidad Económica** | I §1.2, IV §4.3, XII y Anexo H | Crear 14.1 Estudio de Mercado como apartado visible y reutilizar el contexto disponible con sus límites por segmento. Incorporar 14.2 Costos del Proyecto, 14.2.1 Recursos, 14.2.2 Adquisiciones y 14.3 Flujo de Caja como destinos para la integración de Anita y Erick. Preservar sus bloques de costos, flujo, VAN, TIR, Payback, sensibilidad y el Anexo H. |
| **XV. Ajustes del Cronograma** | V §5.3, V §5.4.2, XIII y Anexo G | Crear 15.1 Revisión de Carta Gantt o desarrollo de fases. Usar evidencia por incremento para explicar las fases y el criterio de revisión. Los ajustes detallados, fechas y comparaciones plan–real se reservan a Anita y Erick cuando exista su planificación. |
| **XVI. Conclusiones y Recomendaciones** | XIV | Separar Conclusiones y Recomendaciones. Preservar el cierre cuantitativo por objetivo, aporte, limitaciones y trabajos futuros, reubicando la hoja de ruta con las recomendaciones. |
| **XVII. Referencias Bibliográficas** | Referencias y términos dispersos | Incorporar Glosario antes de Referencias bibliográficas. Conservar BibTeX, CSL, citas, sangría y enlaces. El glosario define los términos técnicos que usa el informe. |
| **XVIII. Anexos** | Anexos A–H y material complementario | Crear el encabezado Anexos y el apartado Material Complementario (Apéndices). Conservar A–H con identificadores vigentes. Seleccionar para el material complementario solo fuentes editables, registros y artefactos pertinentes, con ubicación y versión. |

## Cortes de ejecución y criterios de cierre

- [x] **M00 · Contraste inicial.** Identificar los títulos, el orden, los elementos preliminares y las diferencias de maquetación. Cruzar el Word docente con la planilla comparativa y la memoria.
- [x] **M01 · Prototipo de plantilla.** Mantener intacto el archivo docente. Preparar una copia de trabajo como base de referencia, inspeccionar sus estilos y secciones, y ensayar con portada, preliminares, un capítulo con niveles profundos, una figura, una tabla ancha y un anexo. Mantener las fuentes Markdown de DocSkill. Verificar que el postprocesador preserve el aspecto docente y permita los estilos APA adoptados, y adaptar el exportador si el nuevo esquema de secciones modifica la numeración.
- [x] **M02 · Inventario de cobertura.** Crear una lista de control por rótulo de la plantilla, con número, origen actual, destino, acción y evidencia. Clasificar cada punto como trasladado, ampliado, nuevo o reservado. Hacer también un inventario inverso de contenidos de espaciGo para detectar pérdidas al repartir capítulos.
- [x] **M03 · Preliminares e I a VI.** Completar elementos de presentación y reubicar diagnóstico, requisitos, marco, objetivos y metodología. Integrar restricciones, interesados y plan de recursos según la matriz. Validar cada corte antes de continuar.
- [x] **M04 · VII a X.** Separar definición TI, arquitectura empresarial, tecnologías y arquitectura de detalle. Crear el BPMN requerido con fuente editable y render. Cotejar el recorrido con el ADR y preservar diagramas UML, ERD y contratos.
- [x] **M05 · XI a XV.** Separar indicadores, pruebas, implementación, factibilidad y ajustes. Distinguir metas, mediciones locales y condiciones de validación. Proteger las alertas y el texto de las secciones reservadas aunque cambie su ubicación. Exigir comprobación específica de los nuevos títulos 14.2.1, 14.2.2 y 15.1.
- [x] **M06 · XVI a XVIII.** Separar conclusiones y recomendaciones, agregar glosario y organizar anexos y material complementario. Comprobar el uso de cada anexo desde el cuerpo y la existencia de su destino.
- [x] **M07 · Integración y entrega.** Actualizar el manifiesto y reconstruir referencias cruzadas. Compilar Word y PDF con DocSkill, inspeccionar portada, márgenes, listas, saltos y muestras de capítulos y anexos. Contrastar la secuencia y niveles de la Tabla de Contenido con el Word docente y la hoja Informe Final. Verificar los destinos y números impresos de los tres índices. Publicar en `main` la migración verificada.

El inventario inverso conserva las nueve categorías, 236 requerimientos funcionales, 43 no funcionales, 35 historias, 52 casos de uso, 16 casos de prueba, las 29 figuras existentes y los ocho anexos. El BPMN y otros diagramas requeridos se contabilizan como ampliaciones. Se preservan las métricas con su corte de evidencia y el estado pendiente de proveedores y pruebas dependientes del código. Los rótulos y números internos se actualizan con la nueva estructura. Los identificadores técnicos permanecen trazables.

## Control por rótulo de la hoja Informe Final

| Rótulo de evaluación | Origen anterior | Ubicación tras la migración | Estado |
|---|---|---|---|
| Dedicatoria | Preliminares | Preliminares | Rótulo incorporado. Texto de autores pendiente |
| Agradecimientos | Preliminares | Preliminares | Rótulo incorporado. Texto de autores pendiente |
| Índice de Tablas | Preliminares | Preliminares | Trasladado o reorganizado |
| Índice de Figuras | Preliminares | Preliminares | Trasladado o reorganizado |
| Resumen | Preliminares | Preliminares | Trasladado o reorganizado |
| Abstract | Preliminares | Preliminares | Incorporado o ampliado |
| Capítulo I: Introducción | I | Capítulo I | Trasladado o reorganizado |
| 1. Introducción | I | Capítulo I §1 | Trasladado o reorganizado |
| Capítulo II: Identificación del Problema | I, II y VI | Capítulo II | Trasladado o reorganizado |
| 2. Identificación del Problema | I, II y VI | Capítulo II §2 | Trasladado o reorganizado |
| 2.1. Actualización y justificación del problema | I, II y VI | Capítulo II §2.1 | Trasladado o reorganizado |
| 2.1.1. Descripción de la organización | I, II y VI | Capítulo II §2.1.1 | Trasladado o reorganizado |
| 2.1.1.1. Antecedentes | I, II y VI | Capítulo II §2.1.1.1 | Trasladado o reorganizado |
| 2.1.1.2. Diagnóstico | I, II y VI | Capítulo II §2.1.1.2 | Trasladado o reorganizado |
| 2.1.2. Descripción del problema | I, II y VI | Capítulo II §2.1.2 | Trasladado o reorganizado |
| 2.2. Justificación del problema | I, II y VI | Capítulo II §2.2 | Trasladado o reorganizado |
| 2.2.1. Relevancia del problema | I, II y VI | Capítulo II §2.2.1 | Trasladado o reorganizado |
| 2.2.2. Complejidad del problema | I, II y VI | Capítulo II §2.2.2 | Trasladado o reorganizado |
| Capítulo III: Levantamiento de Requerimientos | VII y A–C | Capítulo III | Trasladado o reorganizado |
| 3. Levantamiento de Requerimientos | VII y A–C | Capítulo III §3 | Trasladado o reorganizado |
| 3.1. Especificación de Requerimientos (IEEE 830/1998) | VII y A–C | Capítulo III §3.1 | Trasladado o reorganizado |
| 3.2. Especificación de Restricciones | VII y A–C | Capítulo III §3.2 | Incorporado o ampliado |
| Capítulo IV: Marco Teórico | III | Capítulo IV | Trasladado o reorganizado |
| 4. Marco Teórico | III | Capítulo IV §4 | Trasladado o reorganizado |
| Capítulo V: Objetivos del Proyecto | II, IV, VI y VII | Capítulo V | Trasladado o reorganizado |
| 5. Objetivos del Proyecto | II, IV, VI y VII | Capítulo V §5 | Trasladado o reorganizado |
| 5.1. Solución Tecnológica | II, IV, VI y VII | Capítulo V §5.1 | Trasladado o reorganizado |
| 5.1.1. Formulación de la solución | II, IV, VI y VII | Capítulo V §5.1.1 | Trasladado o reorganizado |
| 5.1.2. Alcance y restricciones | II, IV, VI y VII | Capítulo V §5.1.2 | Trasladado o reorganizado |
| 5.2. Impacto de la solución | II, IV, VI y VII | Capítulo V §5.2 | Trasladado o reorganizado |
| 5.2.1. Proceso de negocio afectado | II, IV, VI y VII | Capítulo V §5.2.1 | Trasladado o reorganizado |
| 5.2.2. Registro de interesados | II, IV, VI y VII | Capítulo V §5.2.2 | Incorporado o ampliado |
| 5.2.3. Indicadores de gestión | II, IV, VI y VII | Capítulo V §5.2.3 | Trasladado o reorganizado |
| 5.2.4. Niveles de servicio | II, IV, VI y VII | Capítulo V §5.2.4 | Trasladado o reorganizado |
| 5.3. Objetivos del proyecto | II, IV, VI y VII | Capítulo V §5.3 | Trasladado o reorganizado |
| 5.3.1. Objetivo general | II, IV, VI y VII | Capítulo V §5.3.1 | Trasladado o reorganizado |
| 5.3.2. Objetivos específicos | II, IV, VI y VII | Capítulo V §5.3.2 | Trasladado o reorganizado |
| Capítulo VI: Metodología de trabajo | V y G | Capítulo VI | Trasladado o reorganizado |
| 6. Metodología de Trabajo | V y G | Capítulo VI §6 | Trasladado o reorganizado |
| 6.1. Metodología y Desarrollo de la solución | V y G | Capítulo VI §6.1 | Trasladado o reorganizado |
| 6.2. Duración y cronograma | V y G | Capítulo VI §6.2 | Rótulo incorporado. Integración reservada |
| 6.3. Equipo de trabajo | V y G | Capítulo VI §6.3 | Trasladado o reorganizado |
| 6.4. Plan de recursos | V y G | Capítulo VI §6.4 | Incorporado o ampliado |
| Capítulo VII: Definición de Arquitectura TI | VIII y XI | Capítulo VII | Trasladado o reorganizado |
| 7. Definición de Arquitectura TI | VIII y XI | Capítulo VII §7 | Trasladado o reorganizado |
| Capítulo VIII: Reconocimiento de Arquitectura Empresarial | VI | Capítulo VIII | Trasladado o reorganizado |
| 8. Reconocimiento de arquitectura empresarial | VI | Capítulo VIII §8 | Trasladado o reorganizado |
| Capítulo IX: Detalle de las Tecnologías a implementar | III, VIII, IX y XI | Capítulo IX | Trasladado o reorganizado |
| 9. Detalle de las Tecnologías a implementar | III, VIII, IX y XI | Capítulo IX §9 | Trasladado o reorganizado |
| 9.1. Análisis cualitativo/cuantitativo de las tecnologías que serán implementadas | III, VIII, IX y XI | Capítulo IX §9.1 | Incorporado o ampliado |
| 9.2. Herramientas, aplicaciones, lenguajes y componentes que serán implementados | III, VIII, IX y XI | Capítulo IX §9.2 | Incorporado o ampliado |
| Capítulo X: Detalle de la Arquitectura a implementar | II, VII–IX, XI y C–E | Capítulo X | Trasladado o reorganizado |
| 10. Detalle de la Arquitectura a implementar | II, VII–IX, XI y C–E | Capítulo X §10 | Trasladado o reorganizado |
| 10.1. Diagrama BPMN | II, VII–IX, XI y C–E | Capítulo X §10.1 | Incorporado o ampliado |
| 10.2. Diagrama de casos de uso | II, VII–IX, XI y C–E | Capítulo X §10.2 | Trasladado o reorganizado |
| 10.3. Diagrama de componentes | II, VII–IX, XI y C–E | Capítulo X §10.3 | Trasladado o reorganizado |
| 10.4. Modelo de datos | II, VII–IX, XI y C–E | Capítulo X §10.4 | Trasladado o reorganizado |
| 10.4.1. Modelo lógico | II, VII–IX, XI y C–E | Capítulo X §10.4.1 | Trasladado o reorganizado |
| 10.4.2. Modelo Físico | II, VII–IX, XI y C–E | Capítulo X §10.4.2 | Trasladado o reorganizado |
| 10.4.3. Diccionario de datos (puede ir como anexo) | II, VII–IX, XI y C–E | Capítulo X §10.4.3 | Trasladado o reorganizado |
| 10.5. Topología de comunicaciones | II, VII–IX, XI y C–E | Capítulo X §10.5 | Trasladado o reorganizado |
| 10.6. Diagrama de Infraestructura | II, VII–IX, XI y C–E | Capítulo X §10.6 | Trasladado o reorganizado |
| 10.7. Diagrama de Arquitectura | II, VII–IX, XI y C–E | Capítulo X §10.7 | Trasladado o reorganizado |
| Capítulo XI: Implementación de los KPI y SLA | VII, X, XIII y A/F | Capítulo XI | Trasladado o reorganizado |
| 11. Implementación de los KPI y SLA | VII, X, XIII y A/F | Capítulo XI §11 | Trasladado o reorganizado |
| 11.1. Descripción de KPI | VII, X, XIII y A/F | Capítulo XI §11.1 | Incorporado o ampliado |
| 11.2. Descripción de SLA | VII, X, XIII y A/F | Capítulo XI §11.2 | Incorporado o ampliado |
| Capítulo XII: Plan de Pruebas y Aseguramiento de Calidad | X y F | Capítulo XII | Trasladado o reorganizado |
| 12. Plan de Pruebas y Aseguramiento de Calidad | X y F | Capítulo XII §12 | Trasladado o reorganizado |
| 12.1. Plan de Pruebas | X y F | Capítulo XII §12.1 | Trasladado o reorganizado |
| 12.2. Normas y Estándares | X y F | Capítulo XII §12.2 | Incorporado o ampliado |
| Capítulo XIII: Plan de Implementación | XI | Capítulo XIII | Trasladado o reorganizado |
| 13. Plan de Implementación | XI | Capítulo XIII §13 | Trasladado o reorganizado |
| 13.1. Gestión de Disponibilidad | XI | Capítulo XIII §13.1 | Trasladado o reorganizado |
| 13.2. Gestión de Continuidad | XI | Capítulo XIII §13.2 | Trasladado o reorganizado |
| 13.3. Plan de Mantención | XI | Capítulo XIII §13.3 | Incorporado o ampliado |
| Capítulo XIV: Factibilidad Económica | I, IV, XII y H | Capítulo XIV | Trasladado o reorganizado |
| 14. Factibilidad Económica | I, IV, XII y H | Capítulo XIV §14 | Trasladado o reorganizado |
| 14.1. Estudio de Mercado | I, IV, XII y H | Capítulo XIV §14.1 | Incorporado o ampliado |
| 14.2. Costos del Proyecto | I, IV, XII y H | Capítulo XIV §14.2 | Rótulo incorporado. Integración reservada |
| 14.2.1. Recursos | I, IV, XII y H | Capítulo XIV §14.2.1 | Rótulo incorporado. Integración reservada |
| 14.2.2. Adquisiciones | I, IV, XII y H | Capítulo XIV §14.2.2 | Rótulo incorporado. Integración reservada |
| 14.3. Flujo de Caja | I, IV, XII y H | Capítulo XIV §14.3 | Rótulo incorporado. Integración reservada |
| Capítulo XV: Ajustes del Cronograma | V, XIII y G | Capítulo XV | Trasladado o reorganizado |
| 15. Ajustes del Cronograma | V, XIII y G | Capítulo XV §15 | Trasladado o reorganizado |
| 15.1. Revisión de Carta Gantt o desarrollo de fases | V, XIII y G | Capítulo XV §15.1 | Rótulo incorporado. Integración reservada |
| Capítulo XVI: Conclusiones y Recomendaciones | XIV | Capítulo XVI | Trasladado o reorganizado |
| Conclusiones | XIV | Capítulo XVI | Trasladado o reorganizado |
| Recomendaciones | XIV | Capítulo XVI | Trasladado o reorganizado |
| Capítulo XVII: Referencias Bibliográficas | Referencias | Capítulo XVII | Trasladado o reorganizado |
| Glosario | Referencias | Capítulo XVII | Incorporado o ampliado |
| Referencias bibliográficas | Referencias | Capítulo XVII | Trasladado o reorganizado |
| Capítulo XVIII: Anexos | A–H | Capítulo XVIII | Trasladado o reorganizado |
| Anexos | A–H | Capítulo XVIII | Trasladado o reorganizado |
| Material Complementario (Apéndices) | A–H | Capítulo XVIII | Incorporado o ampliado |


## Resultado de la migración

La referencia `templates/reference-tihi84.docx` es una copia idéntica a la plantilla docente, con SHA-256 `b804dddcb37e4563ec7276765ae96c681c8d9a7e267e9eb6e1f87e5622b8a43a`. DocSkill compila las fuentes Markdown con sus estilos. El postprocesado traslada las páginas de presentación y sus recursos, conserva el diseño de los encabezados y pies, y separa la paginación preliminar del cuerpo. La portada utiliza el subtítulo breve «espaciGo — Arriendo flexible de espacios» para mantener los campos en las páginas de presentación. El título completo se conserva en los metadatos.

Se verifican 18 capítulos con destino correcto, 20 entradas del índice de tablas y 30 del índice de figuras, de las cuales 18 corresponden al cuerpo. El BPMN tiene fuente editable con información gráfica BPMN DI y PNG renderizado. La salida PDF tiene 589 páginas. La revisión visual por muestras incluye presentación, aprobación, índices, inicio del cuerpo, BPMN y anexos. La compilación comprueba los identificadores técnicos, los cinco bloques reservados del cuerpo y la identidad de los anexos G y H con la línea base.

Dedicatoria y Agradecimientos conservan un espacio para texto de los autores. La firma y la calificación quedan para la docente. La integración de planificación y finanzas, los proveedores y las pruebas dependientes del desarrollo se mantienen en sus estados respectivos.
