# Plan de trabajo del informe ES2 de EspaciGo

Este plan organiza la investigación y redacción de cada sección de ES2. Parte del informe final de ES1 y sus anexos como **línea base congelada**, y sigue la estructura de la plantilla institucional. Los archivos y productos propuestos abajo se crearán al ejecutar cada actividad; este plan no acredita investigación, implementación ni pruebas realizadas.

Para el estado actual de los bloqueos, responsables por definir y fechas objetivo hasta el 3 de noviembre, seguir el [plan de cierre de pendientes](plan_cierre_pendientes.md). Las tablas siguientes conservan el recorrido por sección y antecedentes del borrador; sus estados históricos no sustituyen la matriz de trazabilidad. El cierre documental del 24-09-2026 con supuestos trazables está en [INV-033](investigacion/INV-033_cierre_borrador.md).

## 1. Fuentes y reglas de trabajo

**Avance al 23-09-2026:** se ejecutó el inventario inicial y se creó la [matriz de trazabilidad](investigacion/matriz_trazabilidad_es2.md). Las secciones están configuradas; 2.1–2.2 tienen investigación inicial, 3.1–3.7 cuentan con modelos de análisis y un diccionario de datos parcial, IV contiene fichas propuestas de KPI/SLA, V incorpora el catálogo de pruebas sin ejecutar y la matriz normativa inicial, y VI contiene procedimientos operativos propuestos. La fecha informada por el usuario es el 03-11-2026; todavía no hay funcionalidades implementadas. El seguimiento vigente está en [pendientes](pendientes.md). Las actividades de cierre descritas abajo siguen abiertas.

- **Base del proyecto:** [informe final ES1](../ES1PT/docx/build/Informe_Final.docx) y anexos finales A–E en su misma carpeta. Para consultar texto y trazabilidad, usar [informe fuente](../ES1PT/docx/informe.md) y [fuentes de los anexos](../ES1PT/docx/anexos/). Conservar todos los archivos de ES1.
- **Estructura de ES2:** [plantilla transcrita](plantilla/plantilla_informe_ES2.md), contrastada con el DOCX institucional antes de cerrar la entrega.
- **Cobertura de evaluación:** los 17 criterios de [la rúbrica incorporada](plantilla/rubrica_de_calificacion.md), que declara 60 puntos máximos.
- **Orientaciones:** [guía de recomendaciones](plantilla/guia_recomendaciones_ES2.md) y su DOCX original. Su tabla resumida omite mantención y difiere en las ponderaciones del cronograma respecto de la rúbrica. Registrar y contrastar esa diferencia con el instrumento oficial antes de usar ponderaciones para priorizar; incluir todos los contenidos mientras tanto.

La cadena de evidencia será: **referencia de ES1 → pregunta de investigación → fuente o prueba → hallazgo → decisión de ES2 → sección y criterio evaluado**. Conservar identificadores `RQF`, `RNF`, `CU`, `HU` y módulos M01–M11. Cada cambio se explica en ES2, con su impacto; ES1 no se reescribe.

## 2. Prioridad vigente y preparación

**Decisión del usuario, 23-09-2026:** dedicar primero el trabajo a investigación, cuerpo y anexos. Dejar DOCX, render PDF/PNG, campos APA 7, índices y aprobación del perfil para cuando el contenido esté completo, salvo petición expresa posterior. No repetir comprobaciones Word por sección. El perfil quedó `aprobado` el 24-09-2026 por autorización expresa del usuario, tras generar y revisar el render (INV-020); INV-008 conserva los diagnósticos previos.

Durante la redacción, comprobar fuentes, coherencia y cálculos cuando cambien; ensamblar Markdown al cerrar un bloque útil. No ejecutar pruebas del generador, compatibilidad ES1 ni diagnósticos Word por cambios de prosa. Los cálculos nuevos admiten comprobaciones numéricas enfocadas sin Word.

### Preparación registrada

1. Crear `investigacion/INV-001_base_y_brechas.md`: inventariar alcance, exclusiones, objetivos, actores, requisitos, arquitectura, KPI, SLA y cronograma de ES1. Registrar las referencias exactas y las contradicciones encontradas.
2. Crear `investigacion/matriz_trazabilidad_es2.md` con columnas: criterio, sección ES2, referencia ES1, investigación, entregable, estado y evidencia de revisión. Usar los 17 criterios de la sección 4 de este plan.
3. Confirmar con el equipo el alcance que se diseñará y demostrará, la capacidad disponible, los responsables y la rotación de jefatura indicada por la guía. Los roles de ES1 son antecedentes; no acreditan asignaciones actuales.
4. Verificar en el calendario oficial la fecha de ES2 y los hitos formativos. La guía menciona semanas académicas 12, 13 y 14; no convertirlas a fechas sin ese calendario. Revisar también el código de asignatura: el JSON contiene `TIH184` y la guía transcrita `TIHI84`.
5. Crear los Markdown del mapa siguiente con sus encabezados y marcadores `[[PENDIENTE: ...]]`, y luego registrar su orden en `informe.json`, sustituyendo la referencia a `00_borrador.md` cuando corresponda.

**Salida de preparación:** alcance de trabajo registrado, matriz inicial, preguntas abiertas y esquema ensamblable. Las consultas pendientes no impiden investigar ni redactar borradores.

## 3. Archivos previstos y orden del informe

Las rutas siguientes son relativas a `Informes/ES2PT/`. Los números de archivo organizan el trabajo; no se escriben como numeración manual dentro de los títulos Markdown.

| Parte institucional | Archivo previsto | Momento de redacción |
| --- | --- | --- |
| I. Introducción | `secciones/01_introduccion.md` | Al terminar el cuerpo |
| II. Tecnologías | `secciones/02_00_tecnologias.md`, `02_01_analisis.md`, `02_02_herramientas.md` | Primera investigación técnica |
| III. Arquitectura | `secciones/03_00_arquitectura.md` y `03_01_bpmn.md` a `03_07_arquitectura.md` | Después del alcance y selección preliminar |
| IV. KPI y SLA | `secciones/04_00_kpi_sla.md`, `04_01_kpi.md`, `04_02_sla.md` | Recuperar metas al inicio; completar tras el diseño |
| V. Pruebas y calidad | `secciones/05_00_calidad.md`, `05_01_pruebas.md`, `05_02_normas.md` | Con requisitos, diseño y metas disponibles |
| VI. Implementación | `secciones/06_00_implementacion.md`, `06_01_disponibilidad.md`, `06_02_continuidad.md`, `06_03_mantencion.md` | Con arquitectura y SLA definidos |
| VII. Cronograma | `secciones/07_cronograma.md` | Estimación inicial y ajuste tras definir el trabajo |
| VIII. Conclusiones | `secciones/08_conclusiones.md` | Al terminar el cuerpo |
| IX. Referencias bibliográficas | `referencias.bib` y bloque generado por el motor | Durante toda la investigación |
| X. Anexos | `anexos/` y lista `anexos` de `informe.json` | Junto con la sección que los utiliza |

Los archivos `XX_00` contendrán el título de capítulo con `#`; las subsecciones usarán `##`. El orden definitivo estará en el JSON. Revisar que referencias e índice de anexos se generen una sola vez y que sus rótulos y numeración respeten la plantilla.

## 4. Trabajo por sección y criterio de cierre

### I. Introducción

**Base:** problema, objetivos y alcance del informe ES1. **Trabajo:** explicar el paso de formulación a desarrollo del proyecto y resumir los contenidos efectivamente incluidos en ES2. Redactar al final, siguiendo la recomendación de aproximadamente una página de la plantilla. **Cierre:** coincide con el cuerpo, identifica alcance y no anuncia resultados ausentes.

### 2.1 Análisis cualitativo y cuantitativo de tecnologías

**Criterio 2.1.1.1.** Leer «Definición de arquitectura TI», metodología y plan de recursos de ES1. Investigar alternativas por capa frente a las propuestas Next.js, Go, PostgreSQL/PostGIS, Docker y GCP, además de la metodología de desarrollo. Definir criterios, escala y pesos antes de puntuar; fundamentar factibilidad técnica, económica e implementativa con fuentes oficiales, costos fechados y supuestos explícitos. Si se comparan mediciones, documentar entorno y procedimiento.

**Producto y cierre:** `02_01_analisis.md`, matriz comparativa y decisión justificada por capa y metodología. Distinguir puntuación valorativa de medición; no presentar estimaciones como resultados. Fuentes en `INV-002_tecnologias_y_factibilidad.md`.

**Paquete económico vigente:** `INV-010_infraestructura_y_formalizacion.md`, `INV-011_muestra_precios_y_demanda.md`, `INV-012_pagos_firma_identidad.md`, `anexos/A_evaluacion_economica.md` e `investigacion/supuestos_bootstrap.json`, apoyados por la skill `$evaluacion-proyectos-chile`. INV-009 conserva el ejercicio pedagógico anterior con ventas inmediatas, ahora superado. Con orientación Sapag, separar mercado, ingeniería, inversión, operación, capital de trabajo, impuestos, flujo y riesgo. Aplicar 25 % de margen, IPC supuesto del 4 % e impuesto académico del 27 % sin atribuirlos a la rúbrica ni a toda SpA. Mantener 36 meses de caja, VAN, TIR, equilibrio y sensibilidad; sustituir supuestos por cotizaciones, demanda y costo de capital sustentados.

### 2.2 Herramientas, aplicaciones, lenguajes y componentes

**Criterio 2.1.1.2.** Convertir las decisiones de 2.1 en un inventario con función, versión por verificar, licencia, hardware, entorno, servicio, costo y relación con módulos. Investigar el acceso real a Mercado Pago, FirmaVirtual, Registro Civil y SII, incluidas restricciones, credenciales y posibilidades de pruebas.

**Producto y cierre:** `02_02_herramientas.md` e `INV-003_integraciones.md`. Identificar cada integración como propuesta, acceso confirmado, simulada o probada, según evidencia. No asumir que retención de fondos, firma o consulta de identidad están disponibles por aparecer en ES1.

### 3.1 Diagrama BPMN

**Criterio 2.1.2.3.** Partir de los seis procesos descritos en «Proceso de negocio afectado» y de los anexos A, B y D. Modelar **al menos tres procesos principales con sus subprocesos**. Como selección inicial: registro/verificación; búsqueda, reserva y pago; operación, cierre y disputas. Ubicar contratación y firma en el flujo correspondiente y justificar la cobertura.

**Producto y cierre:** `03_01_bpmn.md`, fuentes editables en `diagramas/` y exportaciones legibles en `imagenes/`. Describir participantes, eventos, decisiones, mensajes y excepciones. El diagrama de actividades de ES1 es un antecedente: verificar que los nuevos modelos utilicen BPMN y sean coherentes con los requisitos.

### 3.2 Diagramas de caso de uso

**Criterio 2.1.2.4, junto con 3.3.** Consultar actores del anexo A, fichas y diagramas del D, y criterios de aceptación del E. Seleccionar y organizar las vistas necesarias para explicar el alcance de ES2; conservar sus identificadores. Registrar qué casos se mantienen, amplían o quedan fuera del alcance de esta entrega.

**Producto y cierre:** `03_02_casos_uso.md`, diagramas UML y descripciones trazables a RF/HU. Explicar actores, límites, precondiciones, flujo y excepciones; toda modificación debe quedar registrada en ES2.

### 3.3 Diagrama de componentes

**Criterio 2.1.2.4, junto con 3.2.** Desarrollar el diseño modular de ES1 con presentación, backend, persistencia, integraciones y auditoría. Mostrar interfaces y dependencias lógicas, y relacionarlas con los artefactos desplegables. Revisar especialmente la coordinación de reservas, pagos y contratos.

**Producto y cierre:** `03_03_componentes.md` y diagrama UML consistente con 2.2 y 3.7. Una eventual separación en microservicios requiere una decisión nueva documentada; ES1 plantea un backend modular desplegado como unidad.

### 3.4 Modelo de datos

**Criterio 2.1.2.5.** Derivar entidades, relaciones y reglas desde RF y casos de uso: usuarios, espacios, disponibilidad, reservas, pagos, contratos, evidencias y disputas, según el alcance confirmado. Diseñar claves, cardinalidades, restricciones, estados, información geográfica y relación entre datos operativos y analíticos.

**Producto y cierre:** `03_04_datos.md`, modelo lógico y **diccionario de datos en anexo**. El diccionario incluirá significado, tipos, nulabilidad, claves, restricciones y reglas; debe corresponder con el modelo y permitir seguir los flujos críticos. Registrar decisiones de modelado en `INV-004_modelado_y_datos.md`.

### 3.5 Topología de comunicaciones

**Criterio 2.1.2.6.** Consultar la topología propuesta en ES1 y los RNF de seguridad y rendimiento. Precisar conexiones, dirección de los flujos, protocolos, cifrado, puntos de acceso, redes y fronteras de confianza.

**Producto y cierre:** `03_05_comunicaciones.md`, diagrama y tabla de comunicaciones. Cada enlace debe tener propósito y extremos identificados, consistentes con los componentes y servicios seleccionados.

### 3.6 Diagrama de infraestructura

**Criterio 2.1.2.7.** Detallar los recursos de ejecución que soportarán la propuesta: cómputo, almacenamiento, base de datos, red, entornos y servicios externos. Relacionar capacidad y costo con 2.1 y los RNF; distinguir infraestructura prevista de recursos desplegados con evidencia.

**Producto y cierre:** `03_06_infraestructura.md`, diagrama e inventario de recursos con dimensionamiento justificado. Revisar coherencia con disponibilidad, respaldos y restricciones presupuestarias.

### 3.7 Diagrama de arquitectura

**Criterio 2.1.2.8.** Integrar componentes, datos, comunicaciones e infraestructura en una vista de conjunto. Explicar responsabilidades, flujos, decisiones, dependencias externas y correspondencia entre software y hardware o recursos virtuales.

**Producto y cierre:** `03_07_arquitectura.md` y vista arquitectónica descrita. Los nombres y relaciones deben coincidir con 3.3–3.6, y las decisiones responder a objetivos y RNF. Verificar el recorrido completo de una reserva y sus fallos.

### 4.1 Descripción de KPI

**Criterio 2.1.3.9.** Recuperar «Indicadores de gestión» de ES1 y explicar qué mide cada uno. Completar fichas SMART con objetivo, fórmula, unidad, fuente, periodicidad, responsable por confirmar, meta, plazo y método de verificación. Distinguir indicadores documentales/de gestión de indicadores de eficiencia de la solución; justificar los nuevos que resulten necesarios.

**Producto y cierre:** `04_01_kpi.md` e `INV-005_kpi_sla.md`. Cada indicador es medible y trazable. Cuando falte una medición inicial o final, marcarla pendiente; una meta de ES1 no acredita cumplimiento.

### 4.2 Descripción de SLA

**Criterio 2.1.3.10.** Recuperar la tabla de niveles de servicio de ES1 y el anexo C. Entre los valores a contrastar están 99,9 % mensual, RPO máximo de 4 horas y RTO máximo de 6 horas. Son compromisos declarados en la base, sujetos a verificación técnica en ES2.

**Producto y cierre:** `04_02_sla.md`, fichas por servicio con resultado esperado, cliente, gestor, fecha/lugar/autorización cuando consten, criticidad, activos, horario, mantenimiento, disponibilidad, capacidad, respuesta y continuidad. Definir cálculo, ventana de medición, exclusiones y evidencia. Un SLA propuesto no se presenta como acordado ni alcanzado.

### 5.1 Plan de pruebas

**Criterio 2.1.4.11.** Derivar casos de prueba desde RF, RNF, CU, HU y KPI/SLA. Detallar pruebas unitarias, integración, humo, alfa, beta, carga/estrés y aceptación según aplicabilidad; justificar exclusiones. Priorizar doble reserva, pagos y notificaciones repetidas, fallos de terceros, permisos, firma y recuperación.

**Producto y cierre:** `05_01_pruebas.md` y catálogo de casos con identificador, requisito, precondición, datos, pasos, resultado esperado, entorno, criterio de aprobación y evidencia prevista. Distinguir pruebas planificadas de ejecutadas. La meta de cobertura del producto en ES1 no se acredita con las pruebas del generador de informes.

### 5.2 Normas y estándares

**Criterio 2.1.4.12.** Revisar normas y referencias de ES1, su edición, vigencia y aplicabilidad con fuentes primarias. Relacionar cada selección con controles, actividades o pruebas concretas de calidad, seguridad, accesibilidad y tratamiento de información. Adoptar la Ley 21.719 como criterio de diseño desde ES2, antes de su entrada en vigencia, y comprobar su traducción a la matriz de tratamientos del Anexo B y PT-16. Investigar los instrumentos jurídicos aplicables sin inferir cumplimiento por mera mención.

**Producto y cierre:** `05_02_normas.md` e `INV-006_calidad_y_normativa.md`, con matriz norma/versión → motivo → alcance → aplicación → evidencia. Toda afirmación de conformidad requiere soporte; registrar las limitaciones de acceso a las fuentes.

### 6.1 Gestión de disponibilidad

**Criterio 2.1.5.13.** Derivar el plan desde servicios, infraestructura, riesgos y SLA. Especificar supervisión, alertas, capacidad, mantenimiento, dependencias externas y respuesta ante degradación, con funciones y responsables por confirmar.

**Producto y cierre:** `06_01_disponibilidad.md` y relación servicio → objetivo → medida → herramienta → evidencia. Justificar cómo el diseño permite evaluar las metas y qué restricciones impiden garantizarlas todavía.

### 6.2 Gestión de continuidad

**Criterio 2.1.5.14.** Definir escenarios de pérdida de datos, caída de infraestructura y fallo de terceros. Escribir medidas proactivas de prevención y respaldo, y procedimientos reactivos de restauración, comunicación, validación y retorno al servicio, vinculados con RPO/RTO.

**Producto y cierre:** `06_02_continuidad.md` y procedimientos ejecutables con disparador, rol, pasos, recursos, comprobación y evidencia esperada. Una restauración solo se declara exitosa después de ejecutarla y conservar su resultado.

### 6.3 Plan de mantención

**Criterio 2.1.5.15.** Definir inventario y versiones de configuración; solicitud, evaluación, aprobación, prueba, despliegue y reversión de cambios; y registro, clasificación, escalamiento y cierre de incidentes. Distinguir soporte técnico de las disputas comerciales del negocio.

**Producto y cierre:** `06_03_mantencion.md`, procedimientos y formatos de cambio/incidente. Registrar las decisiones de 6.1–6.3 en `INV-007_operacion_y_mantencion.md`. Incluir esta sección aunque falte en la tabla resumida de ponderaciones de la guía.

### 7.1 Revisión de carta Gantt o desarrollo de fases

**Criterios 2.1.6.16 y 2.1.6.17.** Comparar la planificación de ES1 con avance real, dependencias, esfuerzo y capacidad del equipo. ES1 menciona seis incrementos, mientras su tabla enumera cinco incrementos y una etapa de cierre; documentar la diferencia en ES2 antes de establecer la nueva planificación.

**Producto y cierre:** `07_cronograma.md`, Gantt o fases coherentes con la metodología, hitos verificables, estimaciones, responsables confirmados y justificación de ajustes. Incorporar diseño, construcción, pruebas, documentación y revisión. La validación docente se registra únicamente cuando exista evidencia; las fechas históricas de ES1 no se trasladan automáticamente.

### VIII. Conclusiones

Sintetizar las decisiones sustentadas, su contribución a los objetivos de EspaciGo, las limitaciones y el trabajo posterior. **Producto y cierre:** `08_conclusiones.md`, coherente con los hallazgos del informe y sin incorporar resultados nuevos ni declarar implementación que no esté acreditada.

### IX. Referencias bibliográficas

Revisar la pertinencia de las fuentes heredadas en `referencias.bib`, conservar sus claves y agregar las nuevas verificadas. Usar `[@clave]`, registrar los datos bibliográficos durante la investigación y comprobar la presentación APA 7 en el cierre final. **Cierre:** toda cita tiene fuente completa, las fuentes citadas aparecen en referencias y se eliminan los ejemplos ajenos de la plantilla.

### X. Anexos

El diccionario de datos es un anexo exigido. Otros candidatos son matrices comparativas extensas, trazabilidad, fichas de prueba y procedimientos operativos; incorporarlos solo si sustentan el cuerpo. Definir títulos y orden según su primera referencia, y configurar los Word independientes en `informe.json`. **Cierre:** cada anexo se cita y sintetiza en una sección, tiene fuente editable y no duplica innecesariamente los anexos cerrados de ES1.

## 5. Secuencia de ejecución y revisiones

| Etapa | Trabajo | Condición para pasar a la siguiente |
| --- | --- | --- |
| A. Base y alcance | Preparación, matriz y recuperación preliminar de RNF/KPI/SLA | Referencias ES1 y preguntas identificadas |
| B. Investigación técnica y económica | 2.1–2.2, INV-010 y Anexo A; completar normativa e integraciones | Supuestos trazables, flujo reproducible y cotizaciones comparables |
| C. Diseño | 3.1–3.7 y diccionario de datos | Procesos, casos, componentes y datos consistentes |
| D. Medición y calidad | Completar 4.1–4.2 y 5.1–5.2 | Metas, medios de medición y pruebas trazables |
| E. Operación y planificación | 6.1–6.3 y ajuste de 7.1 | Procedimientos, recursos, hitos y restricciones documentados |
| F. Cierre del contenido | Introducción, conclusiones, bibliografía y anexos terminados | Coherencia y cobertura documental de la rúbrica |
| G. Cierre Word | Resolver APA/índices, renderizar informe y todos los anexos, revisar y decidir perfil | Solo después de F; evidencia visual real y validación final |

Estas etapas fijan dependencias, no fechas ni aprobaciones. Las comprobaciones Word quedan exclusivamente en G; no condicionan el avance de investigación o redacción. Para el hito formativo, preparar los capítulos II–V según la guía; para ES2 sumar VI–VII e integrar la retroalimentación. La investigación o los SLA pueden exigir revisar decisiones técnicas anteriores dentro de ES2.

Las investigaciones documentales de la etapa B pueden distribuirse entre agentes con el [tablero de coordinación](coordinacion/README.md): cada uno reserva una tarea, registra fuentes y límites en su INV asignado y deja un traspaso. La integración del cuerpo, anexos, referencias y pendientes espera esos registros; la bitácora muestra el agente activo y evita duplicar trabajo sobre archivos compartidos. Esta coordinación no reemplaza la revisión del equipo ni autoriza la etapa G de Word.

En cada sección: investigar → registrar evidencia → redactar → revisar trazabilidad y citas → ensamblar → actualizar estado. Estados sugeridos: pendiente, investigación, borrador, revisión y cerrado. Registrar quién redacta y quién revisa cuando el equipo lo acuerde.

## 6. Verificación de cierre

- Confirmar cobertura de los 17 criterios y todas las partes I–X de la plantilla.
- Comprobar coherencia de nombres, identificadores, alcance, cifras, diagramas y metas entre secciones.
- Resolver pendientes académicos, fuentes y contradicciones; registrar revisiones y retroalimentación reales.
- Adaptar y revisar el perfil institucional de ES2: la plantilla y un perfil preliminar existen, pero `aprobado` sigue en `false` hasta verificar páginas, portada, índices y anexos.
- Generar el informe y los anexos en `ES2PT/build/`; actualizar los índices mediante `-SoloIndices` y revisar visualmente portada, índices, tablas, diagramas, citas en caché y anexos. No actualizar campos `CITATION`/`BIBLIOGRAPHY` mientras la prueba de Word siga alterando el formato.
- Mantener ES1 intacto y cerrar las tareas de `pendientes.md` solo con evidencia.

### Comandos durante investigación y redacción

```powershell
python Informes/herramientas/simular_bootstrap.py Informes/ES2PT/investigacion/supuestos_bootstrap.json --salida Informes/ES2PT/build/simulacion_bootstrap.json
python Informes/generar.py ensamblar ES2PT
```

Generación, actualización de Word, compatibilidad histórica y validación final se reservan para G. Antes de actualizar campos, recuperar INV-008 y verificar la solución APA en copia. No aprobar el perfil por haber generado un PDF o una muestra parcial.

## 7. Avance y siguiente bloque

**Avance del 23-09-2026:** INV-009 registra el ejercicio inicial de Sapag como antecedente pedagógico; INV-010 y el Anexo A vigente incorporan el escenario sin ingresos durante el primer año, infraestructura, costos legales y municipales, SpA igualitaria, IVA, caja mensual y una evaluación negativa bajo las hipótesis actuales. Las dos calculadoras son reproducibles sin Word, pero solo `simular_bootstrap.py` alimenta el presupuesto vigente. Se distingue tarifa Iowa de cotización Santiago y 27 % académico de régimen tributario por definir.

**Contraste de mercado documental:** INV-011 registra precios públicos de oficinas, salas, bodegas, estacionamientos, stands, locales flexibles y parcelas con quincho, con duraciones distintas. La muestra no valida un ticket medio uniforme. La sensibilidad del Anexo A de 30.000/50.000/150.000 CLP por reserva es una prueba matemática con volumen constante, no una proyección por categoría. La decisión del equipo es abarcar todos los tipos de arriendo: medir oferta, duración, conversión, capacidad y aceptación de comisión por cada modalidad, sin extrapolar vacancia a reservas.

**Liquidación y terceros:** INV-012 documenta que Split 1:1 publica la deducción de su tarifa al vendedor antes de repartir la comisión; el presupuesto actual asigna ese costo a EspaciGo como hipótesis económica. La firma pública FES se tarifa por documento, mientras la API sigue sin cotización. El comparador KYC en USD tampoco equivale a un contrato ni a cumplimiento de privacidad. Antes de aceptar el VAN, definir precio final, quién soporta cada cargo, IVA, saldo de ambas partes y contingencia de devolución; después actualizar modelo, 2.2, 3.5 y Anexo A.

**Monetización y adquisición:** INV-013 mantiene la comisión transaccional decidida en ES1 y propone estudiar destaques pagados, con ranking orgánico separado de un cupo «Patrocinado» sujeto a zona, categoría, disponibilidad y rotación. Meta Ads sería gasto de captación de EspaciGo; vender destaques sería ingreso propio distinto. El Anexo A muestra solo una sensibilidad unitaria y conserva **cero ingresos por destaques** en el VAN. Mercado Pago Split es candidato condicionado a prueba; varios medios de pago dentro de un checkout pueden dar elección al cliente sin integrar varias pasarelas. Stripe no lista Chile como país Payments y Haulmer/Flow requieren prueba documental de reparto 1:1. Para la SpA, el equipo propone 631200 como principal y 731001 como complementario, pendientes de revisión fiscal.

**Siguiente bloque, en este orden:**

1. Obtener para 2.1–2.2 y 3.6 un presupuesto verificable: seleccionar región, SKUs y carga para GCP/VM; solicitar condiciones de Split, firma y KYC; inventariar los equipos reales y los gastos no cubiertos (las versiones y licencias objetivo ya están documentadas en 2.2, SUP-20). Conservar fecha, impuestos, moneda y exclusiones de cada precio. Para Split pedir liquidación detallada y probar reembolso con vendedor sin saldo; para firma cotizar por documento y modalidad jurídica; para KYC separar usuarios nuevos de reservas repetidas.
2. Contrastar con un asesor y el municipio la propuesta 631200/731001, régimen, IVA, domicilio Oficina Express y **una patente** para la SpA. Preguntar por separado si la comisión exige 682000 u otra actividad; verificar actuaciones DOM y aseo. Acordar entre los tres socios el capital realmente pagable, préstamos, reparto exacto, propiedad intelectual y poderes antes de preparar estatutos. No constituir ni contratar durante este estudio.
3. Levantar muestras comparables de oferta y entrevistas separadas a arrendadores/arrendatarios para **todos los tipos de arriendo** declarados, desagregando categoría, modalidad, duración y comuna. Sustituir el ticket uniforme y las reservas supuestas por precios finales, cantidad de espacios, ocupación y conversión observadas en cada tipo. Alimentar la lista `segmentos` del simulador solo con evidencia identificada, reemplazando el reparto sintético ya calculado en INV-033; recalcular VAN, TIR, margen y déficit y revisar 2.1, 3.6 y Anexo A. Medir también tráfico y aceptación de destaques por zona/categoría antes de agregar esta segunda fuente al flujo; INV-011 e INV-013 son evidencia documental, no demanda validada.
4. Completar coherencia del cuerpo III–VI y anexos A/B/C; contrastar datos, privacidad, procesos, contratos, medición y operación. Los ensayos del producto siguen pendientes hasta existir implementación.
5. Ajustar cronograma con recursos y responsables reales; cerrar introducción, conclusiones y bibliografía. Al terminar el contenido, retomar G y las comprobaciones Word/APA/visuales, sin modificar ES1 ni anticipar aprobación del perfil.
