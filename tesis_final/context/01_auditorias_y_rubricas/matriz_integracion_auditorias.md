# Matriz de integración de las auditorías por capítulo

**Estado:** 16 auditorías de solo lectura terminadas. Las correcciones del manuscrito se integran por corte.
**Línea base auditada:** `9dd2328` en el repositorio de la memoria.
**Regla:** cada corte tiene un capítulo propietario. Un hallazgo que otro chat repite se integra una vez y se comprueba en sus referencias cruzadas.

## Orden de corrección y criterios de cierre

| Corte | Corrección aceptada para integrar | Anexo o dependencia | Criterio de cierre |
|---|---|---|---|
| 00. Preliminares | Ampliar el título del manifiesto y el resumen. Retirar la nota de portada generada si su retirada elimina la entrada artificial sin afectar la plantilla. Identificar dedicatorias y agradecimientos pendientes de los autores. | Manifiesto, portada e índice. | Título y alcance coinciden en Word y PDF. Portada y TOC se comprueban después de compilar. |
| I. Introducción | Incorporar personas y organizaciones y usos residenciales, turísticos, recreativos, comerciales e industriales. Mencionar casas de veraneo y hostales como ejemplos objetivo. Mantener las cifras de oficinas dentro de su universo. | A y B como contraste. VII es propietario de la edición del catálogo y HU05. | Diferenciar alcance objetivo, catálogo implementado y evidencia local. |
| II. Diagnóstico | Ampliar la delimitación y explicar la unidad exclusiva. Mantener la Figura 1 como escenario analítico. Hacer visible qué criterios de la Tabla 1 se miden con PT-02, PT-04, PT-06 y PT-07. | F y fuente PlantUML activa de Figura 1. | El escenario no generaliza condiciones de mercado ni confunde indicadores con mediciones. |
| III. Marco teórico | Explicar la intermediación en distintos usos. Distinguir patrones, decisiones objetivo, restricciones SQL y resultados de ensayo. Enlazar el argumento con Figura 2 y anexos. | D y E. REF concentra correcciones bibliográficas compartidas. | Cada concepto sostiene una decisión y cada afirmación empírica identifica evidencia. |
| IV. Objetivos y negocio | Alinear objetivo, segmentos del Canvas y delimitación. Presentar OE3 y OE4 como objetivos con evidencia reportada en X. Tratar comisiones y costos como hipótesis o referencias de diseño. | A, B, XII y H. | Tabla 2, alcance y objetivos coinciden. XII y H mantienen sus reservas. |
| V. Metodología | Explicitar la escala y el carácter contextual de la Tabla 3. Comparar enfoques según criterios del proyecto. Revisar referencias de EDT, RACI y riesgos. | G reservado. | Coherencia entre tablas 3 a 5 y texto. La sección 5.3 queda intacta. |
| VI. Arquitectura empresarial | Ampliar la misión y distinguir personas de representantes de organizaciones. Relacionar estructura funcional y FODA con las vistas. | C, D y E como contraste. | Se distinguen actores de negocio, permisos de operación y categorías de espacio. |
| VII. Requisitos | Normalizar HU y CU abreviados, corregir la afirmación «33 HU implementadas» y separar cobertura documental de evidencia. Alinear RQF-068, HU05, RQF-075 y Tabla 7. Trasladar rastros ES1/ES2 y matrices de cambios a contexto histórico cuando no aportan al tomo final. | **Propietario de A, B y C.** Contrasta reglas de IX y pruebas de F. | Identificadores estables y trazas por significado. Galería de 30 posiciones, titularidad, bloqueo y firma opcional coinciden. |
| VIII. Arquitectura TI | Distinguir decisiones y criterios de la Tabla 9 de resultados ejecutados. Explicitar el corte del catálogo de ocho categorías y el alcance representativo del OpenAPI versionado. | **Propietario de E**. Contrasta D. | Cada ruta citada existe en el commit indicado. El contrato no se usa como evidencia de operación. |
| IX. Procesos y datos | Relacionar cada figura con el párrafo que la interpreta. Distinguir reglas objetivo y ventanas de ensayo. Describir la unidad reservable sin inferir inventario compartido. Conciliar modelo lógico y DDL. | **Propietario de D**. A–C y E como contraste. | Coinciden reglas de titularidad, galería, cobros y alcance. Se conserva la distinción V75/V79 y sus límites. |
| X. Calidad | Relacionar LOCAL-1, F5/F6 y los ensayos posteriores con PT específicos cuando la evidencia lo permite. Indicar evidencia parcial y casos sin registro. | **Propietario de F**. Contrasta X, XI y XIII. | Tabla 10 y F.1–F.3 distinguen pruebas previstas, ejecutadas y conformes por entorno. |
| XI. Despliegue y seguridad | Vincular las afirmaciones de Cloud Build y Cloud SQL a su configuración o evidencia fechada. Precisar qué comprueba cada PT de la Tabla 11 y qué runbooks siguen sin ensayo. | D, E y F como contraste. | El diseño de nube y proveedores se distingue de la operación probada. |
| XII. Evaluación económica | Registrar el estado de reserva y revisar que las remisiones externas no presuponen resultados financieros. | H reservado. | Se conservan alertas y contenido íntegro. |
| XIII. Control | Enlazar cada objetivo de Tabla 12 a un entregable, prueba, evidencia parcial o condición pendiente. | A, F y G reservado. | Los estados de OE1–OE5 se expresan de manera comparable y sin atribuir cobertura adicional. |
| XIV. Conclusiones | Cerrar cada OE según la evidencia identificada. Aclarar alcance amplio y límites de alojamiento, integración, carga y recuperación. | A–F, Tabla 12 y XII reservado. | Cada conclusión se puede seguir hasta una fuente o se presenta como objetivo pendiente. |
| REF. Referencias y formato | Renumerar figuras en una sola pasada y actualizar remisiones de cuerpo y anexos. Corregir comentarios obsoletos de la bibliografía y revisar citas, enlaces, formato y TOC. | Manifiesto, fuentes, Word y PDF. | Rótulos y referencias coinciden. Los vínculos se verifican en sus destinos y los saltos de línea se evalúan visualmente. |

## Hallazgos que requieren adjudicación

- **F6.** Una auditoría interpreta como pendiente el estado completo. El registro posterior `93b59c8`, sección «F6 — resultado técnico local final», sí documenta 2 pruebas del borrador y 4 del perfil documental aprobadas. Se conserva el resultado acotado y se precisan los perfiles, el entorno y lo que queda pendiente. Evitar revertir evidencia por una nota de planificación anterior.
- **Figura 1.** El manuscrito referencia el PNG del escenario actual. La fuente Mermaid histórica con el mismo nombre base contiene otro recorrido. El corte II debe confirmar la correspondencia con PlantUML. El cierre de formato debe resolver la colisión de fuentes para que la regeneración produzca la figura correcta.
- **Ley 21.461.** `pdfinfo -url` confirma que el PDF conserva el destino íntegro con `idNorma=1178004`. El salto visual no es una URL truncada. Solo corresponde ajuste de legibilidad si se requiere.
- **Galería.** RQF-075 y HU05 vigentes ya coinciden en 30 posiciones. El valor 10 que aparece en el resumen histórico del Anexo B se retira del tomo final o se traslada al contexto histórico.
- **Catálogo.** La inclusión de casas y hostales es objetivo. Antes de presentar su soporte se requiere una fuente del catálogo por versión y, para inventario compartido o múltiples unidades, reglas y pruebas propias. La aceptación del alcance no cambia automáticamente el contrato del código.

## Protocolo de integración

El chat principal abre cada corte en orden, consulta el diagnóstico completo del chat propietario y aplica únicamente correcciones verificadas. Después comprueba el diff, las referencias cruzadas y el contenido reservado. Cuando cambia el manuscrito, genera Word y PDF con DocSkill, revisa la exportación y publica el corte en `main` tras verificar el SHA remoto. La numeración global se deja para REF para evitar renumeraciones parciales durante la edición.

**Siguiente corte de edición:** preliminares y manifiesto.
