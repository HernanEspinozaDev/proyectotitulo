# Auditoría final del informe EspaciGo (ES1) — fuentes, citas y rúbrica

> Fecha: 20-09-2026 · Documento auditado: `docx/build/Informe_Final.docx` (11 capítulos, 21 tablas, 36 figuras, 28 fuentes)
> Última revisión: ronda de investigación y mejoras opcionales aplicadas (ver Parte 6)

---

## Parte 1 — ¿Están bien las fuentes del administrador de Word?

**Sí, están completas y ninguna sobra.** Las 28 fuentes registradas están citadas en el texto y todas las citas del texto tienen su fuente. No hay fuentes huérfanas ni citas sin respaldo.

| Comprobación | Resultado |
| :--- | :--- |
| Fuentes en el catálogo (`referencias.bib`) | **28** |
| Fuentes registradas en el documento de Word (`customXml/item4.xml`) | **28** (verificado: `Document.Bibliography.Sources.Count = 28`) |
| Campos de cita en el cuerpo | **51** |
| Fuentes del catálogo sin cita en el texto | **0** |
| Citas sin fuente en el catálogo | **0** |
| Fuentes duplicadas / incompletas / con datos por verificar | **0 / 0 / 0** |

### 1.1 Menciones del texto que **sí** requerían fuente y ya se corrigieron

| Mención | Situación anterior | Corrección aplicada |
| :--- | :--- | :--- |
| «Cámara Chilena de la Construcción, Colliers y JLL» con cifras de 12–14% y 6–7% | Mención sin cita y con cifras sin respaldo verificable | Párrafo reescrito: las cifras ahora son las verificadas de **Colliers (9,9% ≈ 255.000 m²)** y **CBRE (9,64% / 9,22%)**, con cita; se eliminaron las cifras sin fuente y las menciones a organismos de los que no se obtuvo dato |
| «estándar IEEE 830» (2 apariciones) | Norma mencionada sin entrada | Se agregó la fuente **IEEE Std 830-1998** y se citó en ambos puntos |
| `(INE, 2026; CBRE, 2026)` y `(Colliers, 2026)` | Citas escritas a mano, sin fuente identificable | Retiradas y reemplazadas por citas con campo de Word |
| «según estudios, bordeando el 10%» (§1) | Afirmación sin respaldo | Se sustituyó por el dato verificado de Colliers/CBRE citado |

### 1.2 Menciones que **no requieren** entrada bibliográfica (criterio APA 7)

| Tipo | Ejemplos del informe | Por qué no requiere fuente |
| :--- | :--- | :--- |
| Actores y organismos que interactúan con el sistema | Registro Civil, SII, Mercado Pago, FirmaVirtual, Google Cloud, BigQuery | Son actores o proveedores del sistema, no fuentes consultadas; se describen como parte de la solución |
| Competidores y referentes de mercado | Mercado Libre, Yapo, Chilepropiedades, Todogalpon, Mudango, Airbnb, Uber | Se nombran como ejemplos de modelos de negocio, no se reproducen datos suyos |
| Entidades y tecnologías | PostgreSQL, PostGIS, Docker, Next.js, Go, Cloud Run | Tecnologías documentadas: **sí están citadas** por su documentación oficial (8 entradas) |

### 1.3 Menciones que eran opcionales y ya se resolvieron

| Mención | Estado |
| :--- | :--- |
| Mercado Pago (23 menciones) | **Resuelto**: fuente `mercadopago` con la documentación oficial de desarrolladores (Split de pagos 1:1) y cita en §4.6 y §7.1 |
| FirmaVirtual (10 menciones) | **Resuelto**: fuente `firmavirtual` con la ficha oficial del proveedor y cita en §4.9 |
| Competidores del análisis competitivo | **Resuelto**: fuentes `mercadolibre`, `yapo`, `chilepropiedades`, `todogalpon` y `mudango` (tipo *InternetSite`) y citas en §2.1.2 y §3.1 |
| Anexo C (menciona ISO/IEC 25010 y Sommerville) | Sin cambio: se citan en el cuerpo; los anexos no llevan campos de cita porque la lista bibliográfica es única (capítulo 10) |

---

## Parte 2 — Auditoría contra la rúbrica oficial (Escala de Apreciación N°1)

**Resultado global: 14 de 14 indicadores cumplen.** No se detectaron incumplimientos; sí hay mejoras opcionales, indicadas en la Parte 3.

| Indicador | Pts | Dónde se cumple (evidencia en el informe) | Veredicto |
| :--- | :--- | :--- | :--- |
| **1.1.1.1** Selecciona un tipo de organización justificando su elección según los estándares tecnológicos actuales | 3,6 | §2.1.1 (startup de base tecnológica, modalidad de emprendimiento), §8.1 (estructura plana de tres roles, misión y visión), §4.1 (modelo SaaS comparado con On-Premise + figura), §5.1 y §7.1 (plataforma SaaS Marketplace B2B2C sobre arquitectura cloud-native) | **Cumple.** La elección se justifica con el modelo de servicio, el patrón de arquitectura y su comparación explícita con la alternativa descartada |
| **1.1.1.2** Identifica el problema considerando su relevancia y complejidad | 6,0 | §2.1.2 diagnóstico (figura de magnitud con cifras CBRE/Colliers citadas y árbol de causas), §2.2 descripción del problema, §2.3 relevancia (cifras verificadas) y complejidad (legal, financiera y de concurrencia, en tres dimensiones) | **Cumple con evidencia cuantitativa.** La relevancia ya se apoya en fuentes verificables y la complejidad se desglosa en tres frentes |
| **1.1.1.3** Documenta los requerimientos (IEEE 830 o historias de usuario) | 4,8 | §3.2.2 RF (236, con cita a IEEE 830), §3.2.3 RNF (43, ISO/IEC 25010 citada), §3.2.4 casos de uso (52 fichas + 11 diagramas UML), §3.3 HU (35 en 9 épicas con criterios de aceptación), §3.4 matriz de trazabilidad, anexos A–E | **Cumple con creces:** documenta los dos enfoques (predictivo y adaptativo) y agrega trazabilidad verificable |
| **1.1.2.4** Búsqueda, análisis y selección de fuentes que sustenten la propuesta | 4,8 | §4 completo (11 apartados, cada uno cierra con «Decisión de implementación»), capítulo 10 con bibliografía APA 7 en español, **28 fuentes** administrables en Word (incluye 1 artículo revisado por pares y 1 libro de referencia sobre plataformas) | **Cumple con evidencia de investigación.** Ver Parte 6 |
| **1.1.2.5** Formula la solución sustentada en el marco teórico | 3,6 | §5.1 formulación de la solución + lienzo canvas, §7.1 decisiones tecnológicas, y los §4.1–§4.11 que justifican cada decisión antes de formularla | **Cumple.** La secuencia marco teórico → decisión → solución es explícita y trazable |
| **1.1.2.6** Formula el objetivo general y los objetivos específicos | 6,0 | §5.3 objetivo general (uno) y cuatro objetivos específicos, con figura de árbol de objetivos; §5.2.3 indicadores de gestión y §5.2.4 niveles de servicio que los verifican | **Cumple.** Los objetivos son medibles y cada uno tiene indicador o compromiso asociado |
| **1.1.3.7** Plantea la metodología acorde al problema | 4,8 | §6.1 metodología híbrida (iterativo-incremental + PMBOK citado) con justificación, figura de ciclo incremental, §5.2.1 proceso de negocio rediseñado, §4.11 marco metodológico | **Cumple.** La elección se argumenta por la estabilidad de los requerimientos y el control de riesgos |
| **1.1.3.8** Define duración, cronograma, equipo y plan de recursos | 3,0 | §6.2 duración (16 semanas, 6 incrementos, tabla + cronograma gráfico), §6.3 equipo y roles, §6.4 plan de recursos con presupuesto valorizado ($14.460.950 CLP) | **Cumple.** Ver R3 sobre fechas absolutas del cronograma |
| **1.1.4.9** Define la arquitectura TI verificando la necesidad de integración con otros sistemas | 3,6 | §7.1 arquitectura modular cloud-native con patrón bimodal OLTP/OLAP, **figura de contexto** (Registro Civil, SII, Mercado Pago, FirmaVirtual, Cloud Storage, BigQuery) y **figura de topología** del despliegue | **Cumple.** La necesidad de integración está modelada explícitamente, no solo descrita |
| **1.1.4.10** Justifica el uso de la arquitectura TI seleccionada | 3,6 | §7.1 decisiones tecnológicas una a una (Next.js, Go, PostgreSQL/PostGIS, Cloud Run, Docker, BigQuery), §4.4 comparación monolito/módulos/microservicios, §4.11 + figura de estilos arquitectónicos | **Cumple.** Cada tecnología declara su criterio de elección y las alternativas descartadas |
| **1.1.5.11** Reconoce las características de la arquitectura empresarial: tipo de organización y estructura | 3,0 | §8.1 tipo de organización, estructura plana y **organigrama**, misión y visión; §5.2.2 registro de interesados con roles y poder; §3.2.1 actores del sistema | **Cumple.** Ver R4 sobre el marco de referencia de arquitectura empresarial |
| **1.1.5.12** Define la solución de manera compatible con la arquitectura empresarial | 3,6 | §8.2 los cuatro dominios (negocio, aplicaciones, datos, tecnología) con figura, §5.2.1 procesos de negocio rediseñados y §7.1 stack alineado con esos procesos | **Cumple.** La solución se despliega sobre la estructura empresarial descrita, dominio por dominio |
| **1.1.6.13** Utiliza un lenguaje formal y técnico | 4,8 | Todo el documento; terminología homogénea (RQF, RNF, CU, HU, Escrow, KYC/KYB, ACID, SLA), secciones numeradas, tablas y figuras rotuladas con fuente | **Cumple.** Ver R2 sobre dos párrafos repetidos |
| **1.1.6.14** Demuestra coherencia entre problema, solución y conclusión | 4,8 | §2 problema (vacancia, rigidez contractual, garantías, falta de trazabilidad) → §5 solución (marketplace con identidad verificada, retención de fondos, firma electrónica y evidencia) → §9 conclusiones que retoman exactamente esos ejes, con la matriz de trazabilidad de §3.4 como respaldo | **Cumple.** La matriz encadena objetivos → épicas → HU → RF → casos de uso → componentes técnicos |

---

## Parte 3 — Recomendaciones priorizadas (opcionales)

> **Estado: R1 a R7 aplicadas.** Ver el detalle en la Parte 6. Se mantiene aquí el registro de lo que recomendaba la auditoría inicial.

| # | Recomendación | Impacto | Esfuerzo |
| :-- | :--- | :--- | :--- |
| **R1** | Reforzar el marco teórico con 2 a 3 fuentes académicas (artículos revisados por pares o libros sobre SaaS, marketplaces y arquitecturas cloud) | Medio-alto en el indicador 1.1.2.4: hoy la mayoría de las fuentes son normas, documentación oficial e informes de mercado | Medio: requiere buscar y leer las fuentes |
| **R2** | Unificar los dos párrafos casi idénticos sobre la separación de requerimientos según IEEE 830 (aparecen en el capítulo 3 y en el capítulo 6) | Bajo: mejora la lectura y evita repetición | Muy bajo |
| **R3** | Agregar fechas absolutas al cronograma (hoy usa semanas 1–16 relativas, con nota que remite al calendario académico) | Medio: el indicador 1.1.3.8 pide «duración y cronograma» | Muy bajo: basta fijar la fecha de inicio |
| **R4** | Declarar el marco de arquitectura empresarial utilizado (por ejemplo TOGAF o el modelo de dominios de Zachman) en §8 | Medio en el indicador 1.1.5.11: hoy los dominios se describen sin nombrar el marco | Bajo |
| **R5** | Presentar la matriz RACI como tabla R/A/C/I (hoy es una lista de roles y responsabilidades) | Bajo-medio en 1.1.3.8 | Bajo |
| **R6** | Nombrar formalmente los objetivos específicos (OE1–OE4) y vincular cada uno con su indicador de §5.2.3 | Bajo-medio en 1.1.2.6 | Bajo |
| **R7** | Etiquetar los objetivos específicos con verbo en infinitivo medible y resultado esperado (hoy son correctos, pero genéricos) | Bajo | Bajo |

---

## Parte 4 — Correcciones aplicadas en esta ronda

1. **Párrafo del diagnóstico (§2.1.2)** reescrito: se eliminaron las cifras sin fuente (12–14%, 6–7%) y las menciones a la Cámara Chilena de la Construcción y JLL; ahora usa las cifras verificadas de Colliers y CBRE con cita.
2. **Nueva fuente `ieee830`** (IEEE Std 830-1998) agregada al catálogo y citada en los dos puntos donde se menciona la norma.
3. **Figura de magnitud** rehecha solo con las cifras respaldadas, atribuida a CBRE y Colliers.
4. **28 fuentes** en el catálogo, **51 campos de cita** en el cuerpo, **28 entradas** en la bibliografía del capítulo 10, **21 tablas** y **36 figuras** con su nota de fuente.
5. Validaciones del pipeline: **0 errores y 0 advertencias**; auditoría de citas sin pendientes, duplicados ni fuentes incompletas.

---

## Parte 5 — Verificación que depende de Word

| Paso | Estado |
| :--- | :--- |
| `Referencias → Administrar fuentes` muestra las fuentes del documento | **Verificado**: 28 fuentes listadas en el administrador (armbrust2010 … yapo) |
| Las citas del cuerpo se resuelven como campos | **Verificado**: 51 campos `CITATION` + 1 campo `BIBLIOGRAPHY`, con **0** apariciones de «Fuente especificada no válida» |
| El estilo de la lista es APA 7 | **Verificado**: `SelectedStyle="\APASeventhEdition.xsl"`, con el render de Word idéntico al texto APA 7 del CSL |
| El índice se genera con los capítulos y sus páginas | **Verificado**: 62 entradas (11 capítulos, 19 subcapítulos, 32 sub-subcapítulos) y 62 PAGEREF resueltos, sin «Error! Marcador no definido» |
| Actualizar campos con `Ctrl+A` → `F9` | **Ya no es obligatorio ni riesgoso.** `settings.xml` lleva `updateFields`, así que Word reconstruye índice, citas y lista al abrir el documento. Para dejarlo por escrito antes de entregar: `powershell -File docx\actualizar_campos.ps1` (ver Parte 7) |

---

## Parte 6 — Ronda de investigación y mejoras aplicadas (20-09-2026)

### 6.1 Fuentes nuevas incorporadas por investigación

Todas las direcciones se verificaron en línea el 20-09-2026; las dos obras académicas se validaron por su DOI e ISBN, no por referencia indirecta.

| Clave | Tipo en Word | Dato verificado | Dónde se cita |
| :--- | :--- | :--- | :--- |
| `mercadopago` | InternetSite | Documentación oficial *Split de pagos 1:1 para marketplaces* (`www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/overview`) | §4.6, §7.1 |
| `firmavirtual` | InternetSite | Ficha oficial del proveedor de notaría online y firma electrónica avanzada (`firmavirtual.legal`) | §4.9 |
| `mercadolibre` | InternetSite | Sitio oficial del clasificado (`www.mercadolibre.cl`) | §2.1.2, §3.1 |
| `yapo` | InternetSite | Sitio oficial del clasificado (`www.yapo.cl`) | §2.1.2 |
| `chilepropiedades` | InternetSite | Portal inmobiliario (`chilepropiedades.cl`) | §2.1.2 |
| `todogalpon` | InternetSite | Corretaje industrial (`www.todogalpon.cl`) | §2.1.2 |
| `mudango` | InternetSite | Bodegaje y mudanzas (`mudango.com/cl`) | §2.1.2, §3.1 |
| `armbrust2010` | JournalArticle | Armbrust et al. (2010). *A view of cloud computing*. **Communications of the ACM, 53**(4), 50–58. DOI `10.1145/1721654.1721672` | §4.1, §4.4 |
| `tiwana2014` | Book | Tiwana, A. (2014). *Platform Ecosystems: Aligning Architecture, Governance, and Strategy*. Morgan Kaufmann. ISBN `9780124080669` | §4.2 |

Con esto el análisis competitivo de §2.1.2 y §3.1 queda respaldado con los sitios de cada competidor, y las decisiones de §4 (SaaS, marketplace) se apoyan además en literatura revisada por pares y en una obra de referencia sobre ecosistemas de plataforma.

### 6.2 Mejoras opcionales aplicadas (R1–R7)

| # | Recomendación | Estado | Cómo quedó |
| :-- | :--- | :--- | :--- |
| **R1** | Reforzar el marco teórico con fuentes académicas | **Aplicada** | Se incorporaron `armbrust2010` (artículo revisado por pares) y `tiwana2014` (libro), citados en §4.1, §4.2 y §4.4 |
| **R2** | Unificar los dos párrafos repetidos sobre IEEE 830 | **Aplicada** | La cita se conserva en §6.1 (metodología) y el párrafo de §3.1 se reescribió para tratar la trazabilidad de los incrementos sin repetir la norma |
| **R3** | Agregar fechas absolutas al cronograma | **Aplicada** | Nota de §6.2: derivada de la fecha de entrega (15-09-2026 = cierre de la semana 16), la semana 1 corresponde al 26 de mayo de 2026 y el cierre a la primera quincena de septiembre |
| **R4** | Declarar el marco de arquitectura empresarial | **Aplicada** | §8.1 explicita el enfoque por dominios (negocio, aplicaciones, datos, tecnología) y su compatibilidad con marcos como TOGAF |
| **R5** | Presentar la matriz RACI como tabla | **Aplicada** | §6.3 ahora es una tabla RACI de 9 actividades por 4 roles, con convención R/A/C/I y nota de unicidad de responsable y aprobador |
| **R6** | Nombrar los objetivos específicos y vincularlos a indicadores | **Aplicada** | §5.3 rotula **OE1–OE4** (infraestructura, núcleo lógico, integraciones, auditoría y datos) y declara su vínculo con los indicadores de gestión y niveles de servicio |
| **R7** | Objetivos específicos con verbo medible y resultado esperado | **Aplicada** | Cada OE conserva el verbo en infinitivo y ahora declara el dominio que cubre y el resultado verificable |

### 6.3 Defecto detectado y corregido en la bibliografía (idioma y mayúsculas)

Al auditar el texto realmente almacenado en el DOCX se detectó que citeproc, sin locale declarado, generaba la bibliografía en **inglés** y en minúscula los nombres propios: «Retrieved September 20, 2026, from», «(n.d.)», «arriendo en **chile**», «**Cloud run** Documentation», «**The go programming** language documentation».

| Antes (locale en-US por omisión) | Después (`lang: es-CL`) |
| :--- | :--- |
| `Retrieved 20 de septiembre de 2026, from` | `Recuperado 20 de septiembre de 2026, de` |
| `(n.d.)` | `(s.f.)` |
| `en chile`, `Cloud run`, `go programming` | `en Chile`, `Cloud Run`, `The Go Programming Language` |

La corrección se aplicó en tres puntos del pipeline para que no quede ningún caso sin cubrir: el `lang: es-CL` del YAML de `informe.md`, `--metadata=lang:es-CL` en la sonda que calcula el texto en caché de las citas y en las dos pasadas de Pandoc del cuerpo (más la de los anexos). Verificación sobre el DOCX generado: **0** apariciones de «Retrieved», **0** de «(n.d.)», **14** de «Recuperado» y 28 entradas con los nombres propios intactos.

### 6.4 Limitación resuelta: APA 7 también dentro de Word

Word no usa el archivo `apa.csl` para dibujar la bibliografía: usa un **XSL de estilo** propio. Esta instalación solo traía `APASixthEditionOfficeOnline.xsl` (APA 6), lo que quedó registrado como limitación en la ronda anterior.

**Ya está resuelto:** se incorporó el archivo `APASeventhEdition.xsl` en `%APPDATA%\Microsoft\Bibliography\Style` (carpeta de estilos del usuario, que Word enumera sin necesidad de permisos de administrador). El pipeline ahora declara ese estilo en la parte de fuentes (`SelectedStyle="\APASeventhEdition.xsl"`), y la validación 32 comprueba que el DOCX final lo mantiene.

Verificación de que el cambio es real y no cosmético, tras `F9`:

| Comprobación | Antes (APA 6) | Ahora (APA 7) |
| :--- | :--- | :--- |
| Autores de un artículo con 11 firmas | lista recortada con `et al.` | **11 autores**, como exige APA 7 |
| Páginas de revista | `53, págs. 50--58` | `53(4), 50–58` |
| DOI | ausente | `https://doi.org/10.1145/1721654.1721672` |
| Sitio web | `Recuperado el … de https://…` | `Recuperado el … de Mercado Pago Developers. https://…` |

Resultado: el texto guardado (calculado con `apa.csl`) y el que Word regenera al abrir el documento coinciden entrada por entrada. El usuario puede pulsar `Ctrl+A` y `F9` sin riesgo: la lista sigue siendo APA 7.

### 6.5 Estado de las validaciones automáticas del pipeline

33 comprobaciones, **0 errores y 0 advertencias** (`docx/build/reporte_validacion.md`), incluidas las 6 propias del sistema de citas: cada cita del texto tiene fuente (26), cada fuente del catálogo se cita (27), sin fuentes incompletas (28), la parte de fuentes está en el documento (29), cada cita es un campo `CITATION` con su fuente (30) y el estilo bibliográfico declarado es el del generador (32). El registro detallado de las 28 fuentes y sus citas está en `docx/build/auditoria_citas.md`.

---

## Parte 7 — Ronda de cierre: APA 7 en Word y tres defectos corregidos

> Esta ronda se hizo al incorporar `APASeventhEdition.xsl` y revisar el documento terminado.

### 7.1 Defecto 1 — la parte de fuentes seguía declarando APA 6

El estilo se fijaba en un solo lugar (`bibliografia.ROOT_ATTRS`), pero el ensamblador **conservaba la raíz `<b:Sources>` de la plantilla** y solo sustituía las entradas. Es decir: el estilo APA 7 se escribía en `build/sources.xml` y se perdía al armar el documento.

* Corrección: `_inyectar_fuentes` ahora reescribe la raíz con los atributos del generador.
* Prevención: **validación 32** — compara el `SelectedStyle` del DOCX final con el declarado por el generador. Este defecto habría sido detectado automáticamente.

### 7.2 Defecto 2 — el índice estaba roto y mostraba su propia instrucción

El corte del cuerpo de la plantilla se hacía en el **primer** `fldChar end`, que pertenece al PAGEREF de la primera entrada del índice, no al cierre del campo TOC. Consecuencias reales en el documento entregado:

* el campo TOC quedaba sin cerrar y Word lo interpretaba como **texto**: se veía la instrucción ` TOC \h \z \t "Título1;1;Subtitulo1;2;Subtitulo2;3" `;
* la única entrada en caché apuntaba a un marcador inexistente y mostraba **«¡Error! Marcador no definido.»**;
* el índice ni siquiera aparecía como tabla de contenido en Word (`TablesOfContents.Count = 0`).

* Corrección: se reemplaza toda la región del índice (del primer párrafo `TDC1` al párrafo que cierra el campo) por un **campo TOC bien formado** (`begin` + instrucción + `separate` + aviso + `end`), conservando el estilo `TDC1`.
* Prevención: **validación 15** (el campo TOC está completo y `updateFields` está activo) y **validación 33** (no quedan textos de error de campo).

### 7.3 Defecto 3 — los anexos se numeraban «1.1.», «1.2.»…

Las cabeceras `Anexo A … E` no llevan numeración a propósito, pero al no escribir un `numPr` directo heredaban la numeración del estilo `Subtitulo1` y aparecían como «1.1.», «1.2.» tanto en el cuerpo como en el índice.

* Corrección: para los anexos se escribe `numId 0` (sin numeración), que anula la del estilo.

### 7.4 Otras dos correcciones de datos

| Hallazgo | Corrección |
| :--- | :--- |
| Los artículos de revista se declaraban como *ConferenceProceedings*: Word los imprimía como «53, págs. 50--58», sin número de fascículo | Tipo `JournalArticle` y normalización de páginas a `50–58` (guion de rango) |
| Un apellido conservaba LaTeX y Word lo imprimía literal: `Mazi{\`e}res` | Dato corregido a `Mazières` **y** conversión defensiva de acentos LaTeX en `bibliografia.py` (`Garc{\'i}a` → `García`, etc.) |

### 7.5 Índice final verificado

| Comprobación | Resultado |
| :--- | :--- |
| Entradas del índice | **62** (11 capítulos + 19 subcapítulos + 32 sub-subcapítulos) |
| Números de página | Todos resueltos (`1. Introducción` pág. 5 … `11. Anexos` pág. 77) |
| Anexos en el índice | «Anexo A – Actores y módulos del sistema», … sin numeración espuria |
| PAGEREF / marcadores | 62 / 62, todos resueltos |
| Errores de campo | 0 («Marcador no definido», «Fuente especificada no válida») |

### 7.6 Cómo dejar el documento con los campos actualizados

```
powershell -NoProfile -ExecutionPolicy Bypass -File ES1PT\docx\actualizar_campos.ps1
```

Actualiza índice, citas y bibliografía con Word y guarda. Recorre **todas** las historias del documento (`StoryRanges`), porque el índice vive en un cuadro de texto y `Fields.Update()` por sí solo no lo alcanza. Avisa y no hace nada si el archivo está abierto en Word. Es opcional: `settings.xml` lleva `updateFields`, así que Word también lo hace al abrir el documento.

### 7.7 Rúbrica tras la ronda

Los 14 indicadores de la Escala de Apreciación N°1 se vuelven a verificar sobre el documento final: **14 de 14 cumplen**. Evidencia comprobada en el DOCX entregado:

* portada con los datos institucionales completos (asignatura `TIH184`, sección `D-IEI-N8-P1-C2/D`, académico, los tres integrantes, fecha);
* 11 capítulos numerados en decimal, 21 tablas y 36 figuras, todas con título y nota de fuente (93 párrafos de pie);
* requerimientos RQF y RNF con IEEE 830 e ISO/IEC 25010 citados, casos de uso, historias de usuario y matriz de trazabilidad;
* TOGAF, matriz RACI y objetivos OE1–OE4 ya integrados (mejoras R1–R7);
* 51 citas de campo y 28 fuentes administrables, con estilo APA 7 en el documento;
* índice real con páginas y anexos como documentos independientes.

---

## Parte 8 — Rótulos APA 7, índice de ilustraciones y tipografía (20-09-2026)

> Plan aplicado: `ES1PT/plan_rotulos_y_fuentes.md` (diagnóstico, decisiones y verificación).

### 8.1 Qué cambió

| Tema | Antes | Ahora |
| :--- | :--- | :--- |
| Rótulo de tabla | «Tabla 4. Escenarios de monetización» en una línea, texto plano | «**Tabla 4** / *Escenarios de monetización*» encima de la tabla (negrita y cursiva), nota `Fuente:` debajo |
| Rótulo de figura | El título se dibujaba **debajo** de la imagen, con el estilo de las notas (9 pt) | «**Figura 7** / *Título*» encima de la imagen; la imagen ya no lleva pie |
| Índice de ilustraciones | No existía | Página con «Índice de tablas y figuras»: 21 entradas de tablas y 36 de figuras, con número de página |
| Tipografía | Capítulos a 14 pt en *Calibri Light*, subtítulos a 11, texto de tablas a 10 y notas a 9 | **Calibri 12** en títulos (capítulos, subtítulos y títulos de sección) y **Calibri 11** en todo lo demás |

### 8.2 Por qué algunos textos se veían más grandes

Los títulos no heredaban el 11 pt del documento: el estilo `Ttulo1` de la plantilla fija 14 pt y usa la fuente mayor del tema (*Calibri Light*), y el rótulo «Contenido» traía 14 pt aplicados directamente en el texto. Además, las entradas del índice llevaban 12 pt directos, y en el sentido contrario el texto de las tablas (10 pt) y las notas (9 pt) quedaban más chicos que el cuerpo. Se corrigió en el estilo y se eliminaron los tamaños directos de los párrafos del cuerpo, de modo que ninguna excepción gane sobre el estilo. La portada conserva su diseño institucional.

### 8.3 Defecto adicional detectado y corregido

El capítulo de referencias apuntaba a un estilo **inexistente** (`BIBLIOGRAFÍA1`): el estilo real de la plantilla es `BIBLIOGRAFA1`, que es el que aporta la **sangría francesa** de APA 7. Las 28 referencias se imprimían sin sangría. Corregido el mapeo en `MAPA_ESTILOS`; la validación 14 ahora comprueba el estilo correcto.

### 8.4 Estado de las validaciones

**39 comprobaciones, 0 errores y 0 advertencias.** Nuevas en esta ronda:

| # | Comprobación |
| :-- | :--- |
| 34 | Cada tabla lleva su rótulo encima y su nota debajo |
| 35 | Cada figura lleva su rótulo encima y su nota debajo |
| 36 | Ninguna imagen conserva el pie de Pandoc debajo (`ImageCaption`) |
| 37 | El documento tiene índice de tablas y de figuras |
| 38 | Tamaños de letra uniformes: 11 pt en el texto y 12 pt en los títulos |
| 39 | Todos los estilos usan la fuente Calibri |

Las comprobaciones 34–36 y 38 miden solo el cuerpo: la portada institucional (con su logo y sus 24/14 pt) queda fuera por decisión expresa.

### 8.5 Cómo se ve en Word

* Índice general: 62 entradas con página.
* Índice de tablas: 21 entradas («Tabla 1 Resumen de los artefactos de requisitos del proyecto… 16»).
* Índice de figuras: 36 entradas («Figura 1 Mapa de capítulos del informe… 8»).
* 0 «Fuente especificada no válida», 0 «Marcador no definido», 28 fuentes administrables.
* Anexo D: 12 rótulos «Figura D.1 … D.12» sobre sus diagramas.

---

## Parte 9 — Normalización de los anexos (20-09-2026)

> Plan aplicado: `ES1PT/plan_normalizacion_anexos.md`.

Los cinco anexos eran documentos «planos»: sin portada, sin índice, con las tablas sin rótulo ni nota y con un salto de jerarquía entre el título del anexo y sus secciones. Ahora son documentos académicos autónomos con el mismo formato del informe.

### 9.1 Qué cambió

| Tema | Antes | Ahora |
| :--- | :--- | :--- |
| Portada | No tenían | Portada institucional igual a la del informe: «PROYECTO DE TÍTULO: EspaciGo» y el **nombre del anexo como título grande**, más los datos del equipo |
| Índice de contenido | No tenían | Campo TOC propio, con números de página |
| Índice de tablas y figuras | No tenían | Se agregan **según el contenido** del anexo: tablas en A, B, C, E; tablas y figuras en D |
| Rótulos de tabla | Ninguno | 105 rótulos «**Tabla X.n** / *Título*» encima de cada tabla |
| Notas de fuente | Ninguna | 117 notas «Fuente: elaboración propia.» debajo de cada tabla y figura |
| Jerarquía | `Ttulo1` → `Subtitulo2` (nivel saltado) | `Ttulo1` → `Subtitulo1` → `Subtitulo2` → `Prrafodelista`, sin saltos |
| Tipografía | Calibri heredado, tablas a 10 pt y notas a 9 pt | Calibri **11** en el texto y **12** en los títulos (con las validaciones 44 y 39) |

### 9.2 Números verificados

| Anexo | Índices | Entradas | Tablas rotuladas | Figuras rotuladas | Notas |
| :--- | :---: | --: | --: | --: | --: |
| A — Actores y módulos | 2 | 43 | 18 | — | 18 |
| B — Catálogo de RF | 2 | 11 | 5 | — | 5 |
| C — Requerimientos no funcionales | 2 | 9 | 4 | — | 4 |
| D — Especificación de casos de uso | 3 | 176 | 74 | 12 | 86 |
| E — Historias de usuario | 2 | 51 | 4 | — | 4 |
| **Total** | 11 | **290** | **105** | **12** | **117** |

Los títulos de las tablas se derivan del título de sección que las precede (sin numeración ni emoji): «Actores Primarios (roles humanos)», «RF del módulo: RQF-001 a RQF-023…», «CU-01: Registrar Cuenta», «Cobertura de los módulos del sistema por historias de usuario», etc. Si se quiere un título distinto, basta anteponer `*Tabla. <título>*` a la tabla en la fuente del anexo.

### 9.3 Defecto detectado y corregido

Al implementar el reemplazo del título de la portada, la edición se aplicaba sobre el XML **durante** el recorrido, mientras el resto de las ediciones de portada se aplican al final por posición: el desfase dejó XML inválido en tres anexos. Lo detectó la validación 18 (integridad XML) y se corrigió tratando esa edición como las demás.

### 9.4 Estado

**45 validaciones, 0 errores y 0 advertencias.** Los seis documentos (informe + 5 anexos) tienen sus índices construidos y guardados, con **0 errores de campo**: ningún «Fuente especificada no válida» y ningún «Error! Marcador no definido».

## Parte 10 — Limpieza de contenido de los anexos e inconsistencias (20-09-2026)

Los anexos ya tenían formato académico (Parte 9) pero conservaban rastros de documento de trabajo: iconos en los títulos, reglas horizontales decorativas, referencias a archivos `.md` y secciones que hablaban del proceso («versión sincronizada», «control de cambios respecto de la versión anterior», «observaciones abiertas»). La instrucción fue tratarlos como la fuente final del informe y revisarlos **uno por uno**.

### 10.1 Qué se quitó o neutralizó en cada anexo

| Anexo | Iconos en títulos | Reglas `---` | Referencias a `.md` | Secciones de proceso | Otros |
| :--- | :---: | :---: | :---: | :--- | :--- |
| A — Actores y módulos | 16 títulos | 15 | 6 | §5 «Control de cambios respecto de la versión anterior» (45 líneas) | notas de versión del encabezado, cita de la corrección de la profesora |
| B — Catálogo de RF | — | 2 | — | «Brechas cerradas…» renombrado a «Origen de los requerimientos complementarios» | total intermedio «212 RF» eliminado; encabezado de secciones «revisión de completitud»/«segunda revisión» |
| C — Requerimientos no funcionales | — | 4 | — | §4 «Cambios aplicados respecto de la versión anterior (27 RNF)» | nota «Versión corregida (19-09-2026)» y referencias a la retroalimentación |
| D — Casos de uso | 1 título (flechas) | 16 | 2 | §5 «Estado de las brechas y observaciones» (5.1, 5.2, 5.3) | bloque de versión y de estadísticas del encabezado |
| E — Historias de usuario | — | 36 | — | §«Correcciones aplicadas respecto de la versión anterior» | nota «Versión revisada (19-09-2026)» y «convenciones aplicadas en esta revisión» |

Además, las referencias internas pasaron a nombrar los anexos por su letra («ver Anexo D», «catálogo completo en el Anexo B») en lugar de citar archivos `.md`.

### 10.2 Inconsistencias detectadas y corregidas

| # | Anexo | Inconsistencia | Corrección |
| --: | :--- | :--- | :--- |
| 1 | A | La tabla resumen de actores por módulo asignaba a M11 «CU-43 … CU-46» y cerraba en **51 CU**, pero el Anexo D asigna **CU-52 a M11** y las estadísticas del propio A decían 52 | M11 → «CU-43 … CU-46, CU-52» y total **52** (filas y declaración del módulo) |
| 2 | A | M05 declaraba como actores primarios a «Visitante, Usuario Registrado, Arrendatario», mientras la tabla resumen y el Anexo D usan «Visitante, Arrendatario (el Usuario Registrado hereda la capacidad)» | Unificado con la convención del Anexo D |
| 3 | A | CU-10 se describía como «(general)» y en el Anexo D como «(abstracto)» | Terminología UML unificada: «(abstracto)» |
| 4 | B | Cierre de la primera sección complementaria con un total intermedio («212 requerimientos») que no es el total del catálogo | Eliminado; solo queda el cierre de 236 RF |
| 5 | B / D | Afirmaban «las 30 Historias de Usuario», pero el Anexo E contiene **35 HU** | Eliminado al retirar el lenguaje de revisiones |
| 6 | E | La tabla de cambios decía «HU19 … (RQF-226 a RQF-231)», pero `RQF-226` es el bloqueo manual del calendario; la cancelación de reserva corresponde a `RQF-228 a RQF-231` | Se eliminó la sección; hallazgo registrado aquí |

**Comprobación cruzada** (reproducible): ningún anexo cita un RF o un CU inexistente — A cita los 236 RF y los 52 CU, B los 236 RF, D los 52 CU, E los 52 CU y C 37 RF y 22 CU de apoyo.

### 10.3 Figuras nuevas del Anexo A (PlantUML)

| Figura | Contenido | Fuente |
| :--- | :--- | :--- |
| A.1 | Los 11 módulos agrupados por etapa del ciclo de vida del negocio, con el total de RF de cada uno (76 + 58 + 30 + 14 + 14 + 11 + 33 = 236) | `diagramas/a-etapas-modulos.puml` |
| A.2 | Actores primarios y módulos en los que participan, con la nota de herencia de capacidades | `diagramas/a-actores-primarios.puml` |
| A.3 | Actores secundarios (Registro Civil, SII, Mercado Pago, FirmaVirtual) y los módulos en que participan | `diagramas/a-actores-secundarios.puml` |

Las tres se insertan con rótulo «**Figura A.n** / *Título*» arriba y «Fuente: elaboración propia.» debajo, entran al índice de figuras y se dimensionan con `{height=…}` para caber en una página A4.

### 10.4 Mejoras del pipeline que sostienen el cambio

| Cambio | Efecto |
| :--- | :--- |
| `_sin_emoji()` aplicada a los títulos de los anexos | Ningún icono llega al documento ni al índice de contenido (validación **46**) |
| Descarte de reglas `---` en `preparar_anexo` | La separación la dan los estilos y no aparecen líneas horizontales en Word (validación **47**) |
| Título explícito `*Tabla. <título>*` | Permite títulos legibles en el índice de ilustraciones (antes salían cadenas como «RF del módulo: RQF-001 a RQF-023…»); aplicado a las 11 tablas de módulo del Anexo A |
| Líneas de imagen en los anexos | `![Título](imagenes/….png){height=…}` genera rótulo, imagen y nota numerados con la letra del anexo |
| Validaciones tolerantes al guardado de Word | Word renombra `ROTULOTABLA`→`RotuloTabla`, elimina `updateFields` y borra el `rFonts` de `Subtitulo1/2` (queda heredado del tema, que es Calibri): las validaciones 15, 34, 35, 39, 41 y 43 aceptan ahora ese estado, que antes producía errores falsos |

### 10.5 Estado

**47 validaciones, 0 errores y 0 advertencias.** Los seis documentos se regeneraron y se guardaron con sus índices actualizados (**0 errores de campo**): informe 3 índices/119 entradas; Anexo A 3 índices/41 entradas; B 2/11; C 2/7; D 3/170; E 2/49. El Anexo A sumó 3 figuras (17 tablas + 3 figuras) y el Anexo D quedó con 72 tablas + 12 figuras.

### 10.6 Cierre de las dos observaciones abiertas (20-09-2026)

**1. `RNF-022` reformulado.** Fijaba «Chrome ≥40, Firefox ≥32, Edge ≥18 y Safari ≥12» (versiones de 2015) y quedaba incoherente con el stack del proyecto. Ahora dice:

| ID | Nombre | Descripción |
| :--- | :--- | :--- |
| RNF-022 | Compatibilidad con navegadores actuales | El sistema debe ejecutarse correctamente en las **dos últimas versiones estables** de Chrome, Firefox, Edge y Safari. |

Aplicado en `docx/anexos/C_requerimientos_no_funcionales.md` y en el archivo original `ES1PT/anexo_requerimientos_no_funcionales.md`. La cantidad de RNF (43) y su clasificación (Compatibilidad / Interoperabilidad) no cambian.

**2. Anexo A sin duplicación del catálogo.** El Anexo A reproducía los 236 textos de RF (una tabla por módulo, 44 en M04), es decir 258 filas idénticas a las del Anexo B. Se eliminaron las 11 tablas y su rótulo; cada módulo conserva su encabezado con **rango de RF base + complementarios + total**, el objetivo, los actores y los casos de uso, y la sección 2 remite al catálogo:

> Cada módulo declara los rangos de requerimientos funcionales que agrupa, sus objetivos, sus actores y sus casos de uso; **el texto completo de los 236 requerimientos está en el Anexo B**, que es el catálogo de referencia.

Efecto en el Anexo A: de 480 a 212 líneas de fuente; de 17 a **6 tablas** (las cuatro de actores y las dos de resumen) y **3 figuras**; el índice de ilustraciones pasa a 30 entradas (antes 41) y ya no repite los textos del catálogo. La trazabilidad módulo→RF→CU sigue completa por los rangos y por la tabla resumen de la sección 3.

**Estado final: 47 validaciones, 0 errores y 0 advertencias**, con los seis documentos regenerados y guardados (informe 119 entradas de índice; A 30; B 11; C 7; D 170; E 49; 0 errores de campo).

## Parte 11 — Anexo E en formato de tarjeta, según `hu.pdf` (20-09-2026)

> Plan aplicado: `ES1PT/plan_anexo_E_tarjetas_hu.md`.

El documento de referencia `hu.pdf` (30 páginas, una historia por página) presenta cada historia de usuario como **una tabla de 3 secciones**: código y nombre, relato (Como / Quiero / Para que) y criterios de aceptación. El Anexo E las mostraba como texto suelto con una lista.

### 11.1 Qué se hizo

| Tema | Antes | Ahora |
| :--- | :--- | :--- |
| Forma de cada historia | Título + metadatos + relato + `### Criterios de Aceptación` + lista | Tabla de 3 secciones: encabezado `**Código y Nombre de la Historia:** HUxx - …`, relato en tres párrafos y criterios con viñetas |
| Texto de las historias | — | **sin cambios**: la conversión la hace el generador leyendo el mismo contenido (el archivo fuente del Anexo E queda intacto) |
| Trazabilidad | Líneas «Épica / Rol / Prioridad / RF / CU» sobre el relato | Las mismas líneas, debajo de la tabla (como la línea «Nota:» del PDF) |
| Notas | `> (criterio de interfaz)`, `> Fuera del alcance de la ES1` | Igual, después de la tabla |
| «Criterios de Aceptación» | Título de nivel 4 en Word | Primera línea de la tercera sección de la tarjeta |
| Rótulos de tabla | — | Las tarjetas **no** llevan «Tabla E.n» ni «Fuente:»: son el formato de la historia, no ilustraciones (el índice de tablas de E mantiene sus 3 tablas) |
| Paginación | Flujo continuo | Cada historia empieza en una página nueva y la tarjeta no se parte entre páginas (`cantSplit` + `keepNext`), como el PDF de referencia |

### 11.2 Cómo se implementó

- `_tarjeta_hu()` reparte el bloque de cada historia en las tres secciones; `_tabla_grid()` emite una tabla grid de Pandoc de una columna con los bordes alineados al ancho de la línea más larga (sin recortar texto). La lista de criterios se convierte en una lista real de viñetas dentro de la celda.
- `preparar_anexo()` reconoce los títulos `## HUxx - …` y consume el bloque completo (incluido el subtítulo de criterios) para emitir la tarjeta; admite la constante `HU_UNA_POR_PAGINA`.
- En el armado del DOCX, las tablas de tarjeta reciben `cantSplit` por fila y `keepNext` en las filas de encabezado y relato; los estilos `Subtitulo1`/`Subtitulo2` ahora llevan `keepNext` (`_estilo_junto`).
- La validación 43 se ajusta para no exigir rótulo ni nota en las tarjetas.

### 11.3 Verificación

| Comprobación | Resultado |
| :--- | :--- |
| Tarjetas | 35, todas de 3 filas, una por historia |
| Estructura | fila 1 = 1 párrafo · fila 2 = 3 párrafos · fila 3 = título + 7 viñetas (HU01) |
| Texto | sin pérdidas: relato, criterios, metadatos y notas presentes |
| Paginación | 45 páginas; cada encabezado de tarjeta comparte página con sus criterios (las tarjetas más largas que una página continúan en la siguiente, sin alternativa) |
| Índice de ilustraciones de E | 3 tablas (Épicas, Resumen de trazabilidad, Cobertura de los módulos) |
| Validaciones | 43, 44, 45, 46 y 47 en OK |

### 11.4 Observación detectada en el informe

Al correr las validaciones después de este cambio, el control 35 («cada figura lleva su rótulo encima y su nota debajo») señaló **una figura sin rótulo en el informe**: el párrafo del título «6. Metodología de Trabajo» contiene una imagen incrustada y texto suelto («310007012763500»), y el documento tiene 38 imágenes frente a las 36 del cuerpo generado por Pandoc. Es un artefacto introducido por el documento abierto en Word (el script de actualización de campos informó que `Informe_Final.docx` estaba bloqueado), no un cambio del generador: `build/body.docx` y `build/body_citas.docx` no lo contienen. Se corrige regenerando el informe con `generar_informe.py todo` con el documento cerrado.




