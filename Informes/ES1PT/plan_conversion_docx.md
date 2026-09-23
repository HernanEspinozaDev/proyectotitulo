# Plan de conversión Markdown → DOCX · Informe EspaciGo (TIHI84)
> **Estado:** **Fase 1 EJECUTADA** (19-09-2026) — `docx/build/Informe_Final.docx` generado con 0 errores de validación.
> **Fase 2 (pendiente):** incorporar los anexos referenciados desde el informe.

---

## 0.b Estado de ejecución de la Fase 1

| Producto | Ruta | Estado |
| :--- | :--- | :--- |
| Informe final para Word | `ES1PT/docx/build/Informe_Final.docx` (863 KB) | ✅ Generado |
| Markdown intermedio (depuración) | `ES1PT/docx/build/informe_ensamblado.md` | ✅ Generado |
| Salida de Pandoc | `ES1PT/docx/build/body.docx` | ✅ Generado |
| Reporte de validaciones | `ES1PT/docx/build/reporte_validacion.md` | ✅ 18 comprobaciones, 0 errores, 1 advertencia (anexos = Fase 2) |
| Orquestador | `ES1PT/docx/generar_informe.py` | ✅ `todo` reproducible |
| Copia de trabajo del informe | `ES1PT/docx/informe.md` | ✅ Reestructurada a I–XI (el original sin cambios) |
| Bibliografía | `ES1PT/docx/referencias.bib` (16 fuentes) + `apa.csl` | ✅ Con notas PENDIENTE por verificar |
| Diagramas | `ES1PT/docx/imagenes/figura-{actores,m01…m11}.png` | ✅ 12/12 renderizados |

**Resultado del documento:** 11 capítulos numerados (I–XI), 14 subcapítulos, 32 sub-subcapítulos, 13 títulos de cuarto nivel, **19 tablas** con leyenda y bordes, **12 figuras** con leyenda, **16 citas** en formato APA 7 con su lista de referencias, portada completada con los datos del proyecto y campo de índice listo para actualizar con `F9`.

**Pendientes tras la Fase 1:** (1) abrir en Word y ejecutar `Ctrl+A` → `F9`; (2) completar el **FODA** (marcado como PENDIENTE en el documento); (3) verificar los metadatos marcados como PENDIENTE en `referencias.bib`; (4) agregar las fuentes de mercado (INE, CBRE, Colliers, JLL, GPS Property) que hoy aparecen citadas de forma narrativa; (5) validar el cronograma propuesto con la planificación académica.

---

## 0. Decisiones aprobadas (19-09-2026)

| Decisión | Resolución | Efecto en el plan |
| :--- | :--- | :--- |
| Fuente del informe | Se trabaja sobre una **copia**: `docx/informe.md`; el original `informe_del_proyecto_espacigo.md` queda intacto | §1, §4 y paso 1: la copia se reestructura a la secuencia institucional; se agrega la validación 16 (aviso si el original es más reciente que la copia) |
| Secciones sin contenido | **Redactar** cronograma (6.2), indicadores de gestión (5.2.3), niveles de servicio (5.2.4) y proceso de negocio afectado (5.2.1). **Solo el FODA** queda como `[[PENDIENTE]]` | §5 actualizado; paso 1 incluye la redacción de esas secciones |
| Bibliografía | `referencias.bib` **solo con fuentes verificables ya mencionadas**; los informes de mercado quedan marcados como pendientes | §7.2 y pendiente P-1 |
| Tablas y figuras | **Texto correlativo generado por el script** (sin campos `SEQ`/`REF`) | §6 paso 8b queda descartado; §7.1 y §7.3 |

---

## 0.c Cambios de la tercera iteración (19-09-2026, tarde)

| Cambio solicitado | Implementación |
| :--- | :--- |
| **Los anexos deben ser DOCX individuales**, no contenido del informe | El informe conserva el capítulo **11. Anexos** con la descripción y los subtítulos `Anexo A…E`, cada uno con el nombre del documento que se adjunta como objeto. Se generan **5 documentos independientes** en `docx/build/` (sin portada ni índice, con los estilos y encabezados institucionales) |
| **Quitar la numeración romana** de capítulos | La numeración institucional pasa a **decimal arábiga** en los cuatro niveles: `1.`, `1.1`, `1.1.1`, `1.1.1.1` (antes los capítulos usaban números romanos heredados de la plantilla) |
| **Crear el FODA** | Análisis FODA redactado en 8.1 a partir de los antecedentes del proyecto (fortalezas, oportunidades, debilidades y amenazas, con conclusiones), como tabla con leyenda |
| **Completar la portada** | La portada se completa en sus dos copias de campos con: Asignatura, Sección, Académico guía, Integrantes, Fecha de entrega y el nombre del proyecto (**EspaciGo**) bajo el rótulo institucional "FORMULACIÓN DEL PROYECTO DE TÍTULO" |

**Documentos generados en `docx/build/`**

| Documento | Tamaño | Contenido |
| :--- | :--- | :--- |
| `Informe_Final.docx` | ~868 KB | Informe completo (11 capítulos, 20 tablas, 12 figuras, 16 referencias) |
| `Anexo_A_Actores_y_modulos_del_sistema.docx` | 216 KB | 25 títulos, 18 tablas |
| `Anexo_B_Catalogo_de_requerimientos_funcionales.docx` | 208 KB | 6 títulos, 5 tablas |
| `Anexo_C_Requerimientos_no_funcionales.docx` | 207 KB | 5 títulos, 4 tablas |
| `Anexo_D_Especificacion_de_casos_de_uso.docx` | 863 KB | 90 títulos, 74 tablas, 12 diagramas |
| `Anexo_E_Historias_de_usuario.docx` | 225 KB | 83 títulos, 4 tablas |

**Correcciones técnicas de esta iteración:** fusión de las definiciones de numeración de listas que Pandoc genera (la plantilla no las tenía, por lo que viñetas y numeración de listas no se mostraban); lectura tolerante de BOM en los archivos fuente; llenado de la portada en todas sus copias y sin sobrescribir campos con datos vacíos; aviso explícito cuando un documento está abierto en Word y no se puede reescribir.

---

| Elemento | Definición |
| :--- | :--- |
| Entrada | `ES1PT/docx/informe.md` (**copia de trabajo** reestructurada a la secuencia institucional) |
| Origen de la copia | `ES1PT/informe_del_proyecto_espacigo.md` (se conserva intacto como fuente de contenido) |
| Plantilla | `ES1PT/TIHI84_U1_Plantilla_informe_Guía_ABPro.docx` (plantilla institucional, se conserva tal cual) |
| Salida | `ES1PT/docx/build/Informe_Final.docx` |
| Intermedio | `ES1PT/docx/build/informe_ensamblado.md` (Markdown único ensamblado, útil para depurar) |
| Reporte | `ES1PT/docx/build/reporte_validacion.md` (resultado de las 15 validaciones) |
| Motor | Pandoc 3.10 (ya instalado y verificado) + Python 3.14 del `.venv` como orquestador |
| Regla | El Markdown es la fuente editable; el DOCX es el producto final. **No** se convierten los `.md` por separado. |

**Decisión de base:** no se crea un DOCX desde cero ni se usa una plantilla APA genérica. El documento final se construye **dentro de la plantilla institucional** (portada, estilos, numeración, encabezados, pies y tabla de contenidos de la plantilla se conservan).

---

## 1. Objetivo y alcance

Transformar el informe y los anexos del proyecto **EspaciGo** (`.md`) en documentos Word institucionales (`.docx`), usando la plantilla TIHI84 como `reference-doc`, sin perder la estructura, estilos, portada, encabezados ni la tabla de contenidos, y con referencias en APA 7 generadas desde un único archivo `referencias.bib`.

---

## 2. Diagnóstico del entorno (verificado el 19-09-2026)

| Componente | Estado | Detalle |
| :--- | :--- | :--- |
| Pandoc | ✅ Disponible | `pandoc 3.10` en el PATH (instalado vía WinGet) |
| Python | ✅ Disponible | `c:\Users\herna\Documents\Proyectotitulo\.venv\Scripts\python.exe` (3.14) |
| Plantilla DOCX | ✅ Disponible | `TIHI84_U1_Plantilla_informe_Guía_ABPro.docx` |
| `python-docx` | ❌ No instalado | Se instala o se usa solo la stdlib (ver riesgo R-1) |
| `referencias.bib` | ❌ No existe | Hay que crearlo (ver §7.2 y pendiente P-1) |
| `apa.csl` | ❌ No existe | Se descarga el CSL oficial de APA 7 (ver §6, paso 2) |
| `imagenes/` | ❌ No existe | Hay que crearla; los 12 diagramas PlantUML se pueden renderizar localmente |
| `anexos/` | ⏸ Fase 2 | Los 5 anexos están hoy como `ES1PT/anexo_*.md` |
| Citas en el Markdown | ❌ 0 citas | El informe no tiene todavía sintaxis `[@clave]` |

---

## 3. Hallazgos técnicos que condicionan el pipeline

Analicé el XML de la plantilla y ejecuté una conversión de prueba con Pandoc. Estos son los hechos que definen el diseño:

### 3.1 Estilos institucionales disponibles (hay que reutilizarlos, no reemplazarlos)

| Nivel institucional | Ejemplo | `styleId` | Numeración |
| :--- | :--- | :--- | :--- |
| Capítulo | `I. Introducción` | `Ttulo1` (nombre interno "Título1") | Automática: `numId 5`, nivel 0, **romano** (`I.`, `II.`, …) heredada del estilo |
| Subcapítulo | `2.1 Actualización…` | `Subtitulo1` | Automática: `numPr` directo `numId 19`, nivel 1 → `x.y` |
| Sub-subcapítulo | `2.1.1 Descripción…` | `Subtitulo2` | Automática: `numPr` directo `numId 19`, nivel 2 → `x.y.z` |
| Cuarto nivel | `2.1.1.1 Antecedentes…` | `Prrafodelista` | Automática: `numPr` directo `numId 19`, nivel 3 → `x.y.z.w` |
| Cuerpo de texto | párrafos | `PARRAFO` | — |
| Cita/destacado | blockquote | `DESTACADO` | — |
| Título de tabla | `Tabla 4. Comparación…` | `TABLATTULO` | — |
| Texto y encabezado de tabla | celdas | `TABLAPRRAFO` | — |
| Pie de figura | `Figura 1. …` | `PIEDEFOTO` | — |
| Índice (entradas) | TOC | `TDC1`, `TDC2`, `TDC3` | — |
| Instrucciones de la plantilla | texto guía | `Estilo3`, `Estilo4`, `NormalWeb` | **Se eliminan** del documento final |

**Consecuencia importante:** la numeración institucional **no** viene de la jerarquía de Pandoc, sino de propiedades `numPr` en el párrafo. La plantilla usa:
- capítulos: numeración romana dada por el estilo `Ttulo1`;
- subniveles: `numPr` explícito con `numId 19` y `ilvl` 1, 2 y 3.

Por eso el paso de remapeo de estilos debe además **inyectar el `numPr` correcto** en cada título según su nivel.

### 3.2 Qué hace Pandoc con la plantilla como `reference-doc` (probado)

| Elemento | Resultado de Pandoc | Acción requerida |
| :--- | :--- | :--- |
| `# Título` | estilo `Ttulo10` (Title/Heading 1 en inglés) | remapear → `Ttulo1` |
| `## Subtítulo` | estilo `Ttulo2` | remapear → `Subtitulo1` |
| `### Sub-subtítulo` | estilo `Ttulo3` | remapear → `Subtitulo2` |
| `#### Nivel 4` | estilo `Ttulo4` | remapear → `Prrafodelista` |
| Párrafos | `FirstParagraph`, `BodyText`, `Compact` | remapear → `PARRAFO` (respetando párrafos de lista) |
| Listas | `Compact`, `ListParagraph` + `numId 1001` | conservar (la plantilla no numera listas) |
| Citas | `BlockText` | remapear → `DESTACADO` |
| Tablas | `w:tblStyle="Table"` (no existe en la plantilla) | → `Tablanormal` + bordes directos + celdas `TABLAPRRAFO` |
| Encabezados y pies | ✅ Se conservan | nada |
| Márgenes, tipografía, `settings.xml` | ✅ Se conservan | nada |
| **Portada** | ❌ No se conserva | reensamblar desde la plantilla |
| **Tabla de contenidos** | ❌ No se conserva | conservar el campo TOC de la plantilla |
| Imágenes de la plantilla | ✅ Se copian a `word/media` | nada |

### 3.3 Estructura del documento plantilla

- Portada construida con **cuadros de texto** (`txbxContent`): título del proyecto, asignatura, sección, académico guía, integrantes, fecha (con marcadores de ejemplo).
- Una sección (`sectPr`) única, con `header1/2` y `footer1/2`.
- Campo TOC real (`TOC \o …`) con resultado en caché, precedido por el título **"Contenido"** (`Estilo4`) en página propia.
- Cuerpo de la plantilla con los títulos institucionales y párrafos de instrucción que deben eliminarse.

**Estrategia elegida:** usar la plantilla como **documento base** y sustituir su cuerpo de contenido (dejando portada + "Contenido" + campo TOC + encabezados/pies + estilos), insertando el cuerpo generado por Pandoc con los estilos remapeados. Así se cumple "no crear un DOCX nuevo si es posible evitarlo".

---

## 4. Arquitectura del pipeline

```
ES1PT/
├── informe_del_proyecto_espacigo.md      ← ORIGINAL intacto (fuente de contenido)
├── anexo_*.md                            ← FUENTE (Fase 2)
├── TIHI84_U1_Plantilla_informe_Guía_ABPro.docx   ← original intacto
└── docx/
    ├── informe.md                        ← copia de trabajo reestructurada (entrada de Pandoc)
    ├── plantilla.docx                    ← copia de trabajo de la plantilla
    ├── referencias.bib                   ← fuentes bibliográficas (claves Pandoc)
    ├── apa.csl                           ← estilo APA 7.ª ed. para citeproc
    ├── imagenes/                         ← figura-01.png … figura-11.png, actores.png
    ├── anexos/                           ← (Fase 2) copias/alias de los anexos .md
    ├── build/
    │   ├── informe_ensamblado.md
    │   ├── body.docx
    │   ├── Informe_Final.docx            ← PRODUCTO
    │   └── reporte_validacion.md
    └── generar_informe.py                ← orquestador (un solo script)
```

`generar_informe.py` se ejecuta con `--fase 1` (informe) y `--fase 2` (informe + anexos), y con `--validate` para correr solo las comprobaciones.

**Responsabilidades:** Pandoc hace Markdown → DOCX (tablas, listas, citas con `--citeproc`, bibliografía APA). Python hace: pre-procesamiento del Markdown, validaciones, remapeo de estilos, inyección de numeración, armado con la plantilla, captions/campos y reporte. No se reimplementa APA en Python.

---

## 5. Mapa de la estructura institucional

Contraste entre la estructura obligatoria de la plantilla y el contenido actual del informe.

| Sección institucional | Contenido actual (origen) | Estado |
| :--- | :--- | :--- |
| **I. Introducción** | `## Introducción` | ✅ |
| **II. Identificación del Problema** | `## Identificación del Problema` | ✅ |
| 2.1 Actualización y justificación del problema | `### Actualización y justificación del problema` | ✅ |
| 2.1.1 Descripción de la organización | rótulo en negrita dentro de 2.1 | 🟡 hay que separar en título |
| 2.1.1.1 Antecedentes de la Organización | primer bloque del rótulo anterior | 🟡 separar |
| 2.1.1.2 Diagnóstico de la situación actual | rótulo en negrita | 🟡 separar |
| 2.1.2 Descripción del problema | rótulo en negrita | 🟡 separar |
| 2.2 Justificación del problema | rótulo en negrita | 🟡 separar |
| 2.2.1 Relevancia del problema | *Relevancia del problema.* (cursiva) | 🟡 separar |
| 2.2.2 Complejidad del problema | *Complejidad del problema.* (cursiva) | 🟡 separar |
| **III. Levantamiento de Requerimientos** | `## Levantamiento de Requerimientos` | ✅ |
| 3.1 Determinación de los instrumentos a utilizar | `### Determinación de los instrumentos a utilizar` | ✅ |
| 3.2 Detalle de los requerimientos | `### Documentar los Requerimientos` + resumen de artefactos | ✅ |
| 3.2.1 Identificación de actores del sistema | `### Identificación de Actores del Sistema` | ✅ |
| 3.2.2 Requerimientos funcionales | `### Requerimientos Funcionales (RF)` + Tabla | ✅ |
| 3.2.3 Requerimientos no funcionales | `### Requerimientos No Funcionales (RNF)` + Tabla | ✅ |
| 3.2.4 Especificación de casos de uso | `## Especificación de Casos de Uso…` (11 módulos) | ✅ mover |
| 3.2.5 Historias de usuario | `## Historias de Usuario (Metodología Adaptativa)` | ✅ mover |
| 3.2.6 Matriz de trazabilidad | `## Matriz de Trazabilidad` | ✅ mover |
| **IV. Marco Teórico** | `## Marco Teórico` | ✅ |
| 4.1 Investigación Bibliográfica | los 11 bloques temáticos + "Arquitectura de software y metodologías" | 🟡 renumerar como 4.1.x y **agregar citas** |
| **V. Objetivos del Proyecto** | `## Objetivos del Proyecto` + `## Formulación de la Solución` | ✅ reorganizar |
| 5.1.1 Formulación de la Solución | intro de `## Formulación de la Solución` | 🟡 redactar párrafo introductorio |
| 5.1.2 Alcance y restricciones | `### Alcance y restricciones` | ✅ |
| 5.2.1 Proceso de negocio afectado | — | � **redactar** (derivado de los procesos: registro, publicación, reserva, contratación, check-in, disputas) |
| 5.2.2 Registro de Interesados | `### Registro de Interesados` + Tabla 13 | ✅ |
| 5.2.3 Indicadores de gestión | — | 🟡 **redactar** (derivado de las 9 épicas: cumplimiento de criterios de aceptación, cobertura de módulos, tiempos de flujo) |
| 5.2.4 Niveles de servicio | — | 🟡 **redactar** (derivado de RNF-009 disponibilidad 99,9%, RNF-001 búsqueda < 2 s, RNF-023/RNF-024 resiliencia) |
| 5.3.1 Objetivo General | `### Objetivo General` | ✅ |
| 5.3.2 Objetivo Específico | `### Objetivo Específico` | ✅ |
| **VI. Metodología de Trabajo** | `## Metodología de Desarrollo del Proyecto` | ✅ |
| 6.1 Metodología de desarrollo de la solución | párrafo de metodología híbrida | ✅ |
| 6.2 Duración y cronograma | párrafo de 16 semanas | � **redactar** (cronograma en 6 incrementos sobre 16 semanas, alineado a la metodología) |
| 6.3 Equipo de trabajo | equipo y roles (RACI) | ✅ |
| 6.4 Plan de recursos | presupuesto | ✅ |
| **VII. Definición de arquitectura TI** | `## Definición de arquitectura TI` | ✅ |
| 7.1 Tipo de arquitectura TI requerida | decisiones tecnológicas | ✅ |
| **VIII. Reconocimiento de arquitectura empresarial** | `## Reconocimiento de arquitectura empresarial` | ✅ |
| 8.1 Tipo de organización y estructura | misión, visión, organigrama, 4 dominios | 🟡 falta FODA y objetivos estratégicos |
| **IX. Conclusiones** | `## Conclusiones` | ✅ |
| **X. Referencias bibliográficas** | — | � **generar** con citeproc desde `referencias.bib` (fuentes verificables; ver P-1) |
| **XI. Anexos** | — | ⏸ Fase 2 |

Las secciones marcadas 🔴 se crean con el título institucional y un marcador visible `[[PENDIENTE: …]]` (estilo `DESTACADO2`), y se listan en el reporte. Así el documento queda estructurado y se ve exactamente qué falta.

---

## 6. Pasos de la Fase 1

| # | Paso | Salida | Responsable |
| :--- | :--- | :--- | :--- |
| 0 | **Preflight:** verificar plantilla, informe y pandoc; crear `docx/`, `docx/build/`, `imagenes/`, `anexos/`; copiar la plantilla a `docx/plantilla.docx` y el informe a `docx/informe.md` | estructura de carpetas + copias | script |
| 1 | **Reestructurar la copia** `docx/informe.md` a la secuencia institucional de §5 (mover bloques, separar los rótulos en negrita en títulos de nivel) y **redactar** 5.2.1, 5.2.3, 5.2.4 y 6.2; solo el FODA queda como `[[PENDIENTE]]` | `docx/informe.md` reestructurado | agente + revisión del usuario |
| 2 | **Preparar APA:** descargar `apa.csl` oficial (repositorio CSL) y crear `referencias.bib` con las fuentes verificables | `docx/apa.csl`, `docx/referencias.bib` | script + usuario (P-1) |
| 3 | **Convertir captions y referencias:** normalizar `*Tabla N. Título.*` → caption institucional; detectar referencias "véase la Tabla 3" / "Imagen 1" para vincularlas | `informe_ensamblado.md` | script |
| 4 | **Renderizar figuras (opcional recomendado):** los 12 diagramas PlantUML a PNG en `docx/imagenes/` e insertarlos en 3.2.4 como `Figura N` | `imagenes/*.png` | script (PlantUML local) |
| 5 | **Ensamblar el Markdown final** (metadatos, cuerpo, referencias; soporte de `{{ANEXO: …}}` ya implementado pero inactivo en Fase 1) | `build/informe_ensamblado.md` | script |
| 6 | **Pandoc:** `pandoc informe_ensamblado.md -o build/body.docx --reference-doc=docx/plantilla.docx --citeproc --bibliography=referencias.bib --csl=apa.csl` | `build/body.docx` | script |
| 7 | **Remapeo dentro de la plantilla:** abrir `docx/plantilla.docx` como documento base; eliminar párrafos de instrucción; insertar el cuerpo de `body.docx`; por cada título aplicar estilo institucional + `numPr` correcto; tablas → `Tablanormal` + bordes + `TABLAPRRAFO`/`TABLATTULO`; citas → `DESTACADO`; figuras → `PIEDEFOTO` | `build/Informe_Final.docx` | script |
| 8 | **Campos:** conservar el TOC de la portada/índice, numerar páginas si la plantilla lo hace, marcar `w:updateFields=true` en `settings.xml` para que Word actualice índice y referencias al abrir | `build/Informe_Final.docx` | script |
| 9 | **Validaciones + reporte** (§8) y resumen final (§9) | `build/reporte_validacion.md` | script |
| 10 | **Revisión en Word:** abrir, `Ctrl+A` → `F9`, verificar numeración romana y x.y, tabla de contenidos, y completar los `[[PENDIENTE]]` | documento revisado | usuario |

**Nota sobre referencias cruzadas (decisión aprobada):** los captions se emiten como **texto correlativo generado por el script** (consistente y estable). No se usan campos `SEQ`/`REF` de Word.

**Nota sobre la copia de trabajo:** `docx/informe.md` es la entrada de composición. Cuando se edite el original `informe_del_proyecto_espacigo.md`, hay que regenerar la copia antes de recompilar (la validación 16 avisa si el original es más reciente).

---

## 7. Reglas de contenido

### 7.1 Tablas
- Cada tabla del informe se emite como **tabla real de Word** (`w:tbl`), nunca como imagen.
- Estructura institucional: caption con estilo `TABLATTULO` (`Tabla N. Título.`), tabla, y `Nota. …` cuando corresponda.
- El script numera los captions de forma correlativa (1…N) según el orden real del documento, incluyendo las 3 tablas hoy sin número (resumen de artefactos, negocio→validación, matriz de trazabilidad).
- Encabezado de tabla en negrita y repetido entre páginas; bordes visibles aplicados de forma directa porque la plantilla solo tiene `Tablanormal`.

### 7.2 Citas y referencias
- Fuente única de datos: `referencias.bib`. Sintaxis en el Markdown: `[@clave]` o `[@clave1; @clave2]`.
- `apa.csl` genera citas y lista final en APA 7.ª edición vía `--citeproc`.
- La sección final se titula **`X. Referencias bibliográficas`** y se genera automáticamente.
- **No se inventan fuentes ni metadatos.** Se reportan como advertencia: citas sin entrada en el `.bib` y entradas del `.bib` que no se citan (no se eliminan automáticamente).
- Hoy el informe **no tiene citas**; hay afirmaciones de mercado (INE, CBRE, Colliers, JLL, GPS Property) sin respaldo y normativa (Leyes 21.461 y 21.719) que deben citarse. **Alcance aprobado:** el `.bib` incluye únicamente fuentes verificables ya mencionadas en los archivos (normativa, ISO 25010, PMBOK, PCI-DSS, documentación de las herramientas del stack); los informes de mercado se incorporan solo cuando el usuario aporte el dato exacto (ver P-1).

### 7.3 Figuras
- Imágenes reales insertadas, sin deformar (se respeta proporción).
- Estructura: `Figura N` + título (`PIEDEFOTO`), imagen, `Nota.` si hay fuente o adaptación.
- Se conservan las atribuciones existentes en el Markdown (por ejemplo, la Tabla de evidencia digital adaptada) y no se inventan fuentes.

### 7.4 Anexos (Fase 2)
- Sintaxis soportada: `{{ANEXO: anexo-01.md}}` o enlace Markdown equivalente.
- El script localiza el archivo en `docx/anexos/`, lo inserta en `XI. Anexos`, respeta el orden de referenciación y **fuerza salto de página** al inicio de cada anexo.
- Si existe un anexo que nunca se referencia, se informa como advertencia y no se incorpora sin confirmación.

---

## 8. Validaciones automáticas (implementadas en `--validate`)

| # | Validación | Acción si falla |
| :--- | :--- | :--- |
| 1 | Existe el informe principal | error: detener |
| 2 | Existe la plantilla DOCX | error: detener |
| 3 | Existe `referencias.bib` | advertencia + bibliografía vacía |
| 4 | Existe `apa.csl` | advertencia + citas sin formato |
| 5 | Todos los anexos referenciados existen | error del anexo faltante + continuar |
| 6 | Todas las imágenes referenciadas existen | advertencia + marcador `[[FALTA IMAGEN: …]]` |
| 7 | Todas las citas existen en el `.bib` | advertencia + reporte de claves faltantes |
| 8 | No hay enlaces locales rotos | advertencia |
| 9 | Jerarquía de títulos correcta (saltos de nivel) | advertencia |
| 10 | Numeración de capítulos y subcapítulos coherente | advertencia |
| 11 | Toda tabla tiene título | advertencia + caption generado |
| 12 | Toda figura tiene título | advertencia + caption generado |
| 13 | Los anexos están referenciados en el cuerpo | advertencia |
| 14 | La bibliografía se genera correctamente | error si citeproc falla |
| 15 | La tabla de contenidos corresponde a la estructura final | aviso: requiere `F9` en Word |
| 16 | La copia `docx/informe.md` no está desactualizada respecto del original | advertencia: regenerar la copia |

Todas las comprobaciones se registran en `build/reporte_validacion.md`. Las fallas no bloqueantes permiten continuar y generan el DOCX igualmente.

---

## 9. Resumen final que emitirá el script

Secciones detectadas · anexos incorporados · tablas · figuras · citas · referencias · advertencias · errores · rutas de salida.

---

## 10. Riesgos, contingencias y decisiones pendientes

| ID | Riesgo / decisión | Mitigación / propuesta |
| :--- | :--- | :--- |
| R-1 | `python-docx` no está instalado y `pip` podría requerir red | Instalar en el `.venv`; si falla, implementar el armado con `zipfile` + `xml.etree` (solo stdlib). El plan no depende de la librería |
| R-2 | La numeración automática de la plantilla (`numId 19`) puede reiniciar de forma inesperada al mezclar capítulos romanos y subtítulos decimales | Replicar el patrón exacto de la plantilla y validar en Word; si no reinicia por capítulo, aplicar `w:lvlOverride`/`startOverride` con un `numId` por capítulo |
| R-3 | Pandoc no reconoce los estilos en español y los títulos salen sin numeración | Ya resuelto en el plan: remapeo explícito (`Ttulo10→Ttulo1`, `Ttulo2→Subtitulo1`, `Ttulo3→Subtitulo2`, `Ttulo4→Prrafodelista`) + inyección de `numPr` |
| R-4 | Las tablas pueden salir sin bordes (no existe estilo de tabla con bordes) | `tblStyle = Tablanormal` + bordes directos + encabezado repetido |
| R-5 | El índice y los campos muestran caché vieja | `w:updateFields=true` + paso manual `Ctrl+A`, `F9` |
| R-6 | Reestructurar el informe mueve secciones y puede duplicar o perder contenido | Reestructuración en un solo paso revisable, con verificación de que el conteo de párrafos/tablas antes y después coincide |
| P-1 | **Faltan las fuentes bibliográficas** (`referencias.bib`) y no se pueden inventar | Definir con el usuario el listado de fuentes reales (informes INE/CBRE/Colliers/JLL/GPS Property, leyes, ISO 25010, PMBOK, PCI-DSS, bcrypt, docs de herramientas) |
| P-2 | Falta el **FODA** (única sección aprobada como pendiente) | Se crea con `[[PENDIENTE]]`; 5.2.1, 5.2.3, 5.2.4 y 6.2 se redactan en el paso 1 |
| P-3 | Los datos de portada (carrera, área académica, fecha definitiva) no aparecen en el Markdown | Completar solo con información de los archivos fuente; si falta, dejar marcador visible |
| P-4 | ~~Decisión sobre referencias cruzadas automáticas~~ | **Cerrado:** numeración correlativa como texto (§0) |

---

## 11. Fase 2 (adelanto): anexos

### 11.b Estado de ejecución de la Fase 2 (19-09-2026) — **EJECUTADA**

Cinco anexos incorporados, cada uno en página nueva y sin numeración de capítulo (aparecen en el índice como nivel 1):

| Anexo | Archivo fuente | Contenido | Figuras |
| :--- | :--- | :--- | :--- |
| **A — Actores y módulos del sistema** | `actores_y_modulos.md` | Modelo de actores, generalización, 11 módulos con sus RF, resumen y control de cambios | — |
| **B — Catálogo de requerimientos funcionales** | `anexo_requerimientos_funcionales.md` | Los 236 RF en orden de identificador + revisiones de completitud y brechas cerradas | — |
| **C — Requerimientos no funcionales** | `anexo_requerimientos_no_funcionales.md` | Los 43 RNF, resumen por categoría, trazabilidad y cambios aplicados | — |
| **D — Especificación de casos de uso** | `anexo_casos_de_uso.md` | Convenciones, modelo de actores, 11 módulos con diagrama y 52 fichas, trazabilidad y relaciones UML | 12 (Figura D.1–D.12) |
| **E — Historias de usuario** | `anexo_historias_de_usuario.md` | 35 HU con criterios de aceptación, trazabilidad, cobertura y correcciones | — |

**Orden de los anexos:** el de actores y módulos abre la serie porque es el primero referenciado en el cuerpo (sección de identificación de actores), seguido por el catálogo de RF, los RNF, los casos de uso y las historias de usuario. Así se respeta el criterio de la plantilla ("numerando en orden de referenciación en el informe").

**Decisiones de formato aplicadas:** los títulos internos de cada anexo se demotaron un nivel; cada anexo empieza con salto de página; las figuras de los anexos se numeran con la letra del anexo (`Figura D.n`) para no colisionar con las del cuerpo (`Figura 1–12`); las tablas de los anexos conservan su formato de tabla real sin leyenda propia, porque son catálogos que se identifican por la sección que los contiene.

**Verificación:** 21 validaciones automáticas sin errores ni advertencias; el documento final queda con 11 capítulos + 5 anexos, 124 tablas, 24 figuras (12 en el cuerpo y 12 en el anexo D), 16 citas y 16 referencias con hipervínculos.

**Pendientes tras la Fase 2:** los mismos de la Fase 1 (abrir en Word y `F9`, completar el FODA, verificar metadatos marcados como PENDIENTE en el `.bib`, aportar las fuentes de mercado y validar el cronograma).

### 11.a Especificación original de la fase

1. Copiar los 5 anexos a `docx/anexos/` con nombres normalizados.
2. Insertar en el cuerpo las referencias `{{ANEXO: …}}` en el punto correcto (III para requerimientos y casos de uso, IV para el marco de referencia, etc.).
3. Los anexos entran bajo `XI. Anexos`, en orden de referenciación, cada uno con salto de página.
4. Cada anexo conserva sus propias tablas y diagramas (las fichas de casos de uso usan tablas; los diagramas PlantUML ya están validados).
5. Numeración de tablas por anexo (`Tabla A.1`, `A.2`, …) para no colisionar con la del informe.
6. Se ejecuta el mismo `--validate` ampliado: anexos referenciados ↔ anexos existentes.
