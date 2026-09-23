# Plan B — Citas, referencias y fuentes administrables en Word (APA 7)

> Estado: **propuesta pendiente de aprobación**. No se ha modificado ningún archivo del informe todavía.
> Plan complementario: `plan_diagramas_cuerpo.md` (diagramas del cuerpo).

---

## B.0 Diagnóstico verificado (19-09-2026)

### Lo que existe hoy

| Elemento | Estado real |
| :--- | :--- |
| `docx/referencias.bib` | **16 entradas** (3 leyes, 2 libros, 1 artículo, 1 norma ISO, 1 estándar PCI, 8 documentaciones oficiales) |
| Citas en el cuerpo | **16 claves distintas** citadas con sintaxis Pandoc `[@clave]`, distribuidas en ~40 puntos del texto |
| Render de las citas | **Pandoc + `--citeproc` + `apa.csl`** → produce **texto plano**, no campos de Word |
| Lista de referencias | Generada por citeproc en el bloque `::: {#refs}` del capítulo "Referencias bibliográficas" → **texto plano** |
| Fuentes en "Administrar fuentes" de Word | **Vacío.** El DOCX no contiene ningún elemento `<b:Sources>` ni parte `customXml` bibliográfica |
| Citas escritas a mano | **2** en el capítulo 2: `(INE, 2026; CBRE, 2026)` (línea 61) y `(Colliers, 2026)` (línea 62) |
| Menciones sin cita | Reportes de *Cámara Chilena de la Construcción, Colliers y JLL* (línea 37); consultoras *CBRE, Colliers y GPS Property* (línea 59); competidores *Mercado Libre, Yapo, Chilepropiedades, Todogalpon, Mudango* (línea 39); afirmación "según estudios, bordeando el 10%" (línea 15) |
| Citas textuales con página | **Ninguna** (no existen citas literales en el documento) |
| Fuentes en tablas y figuras | Ninguna tabla ni figura declara fuente externa. La tabla de evidencia digital dice "(Adaptada)" sin indicar de qué |
| Fuentes mencionadas en anexos | **Anexo C** menciona "categorías y subcategorías del estándar **ISO/IEC 25010** y del modelo de **Sommerville**" sin cita; el resto de los anexos no menciona fuentes |
| Entradas incompletas | **8** con nota `PENDIENTE` (leyes 21.461/21.719/19.799, ISO 25010, PCI-DSS, y las 5 documentaciones que requieren fecha de consulta/versión) |
| Entradas duplicadas | **Ninguna** detectada |

### Limitación técnica que hay que declarar de entrada

**Pandoc no puede crear fuentes bibliográficas nativas de Word.** `citeproc` genera texto y una lista; no existe ninguna opción de Pandoc que escriba la parte `customXml` de fuentes ni campos `CITATION`/`BIBLIOGRAPHY`. Por lo tanto, este plan **no** se apoya en Pandoc para las citas: usa Pandoc solo para *calcular el texto APA 7* y hace la conversión a campos nativos mediante cirugía XML, igual que ya se hace con la portada, la numeración y las tablas.

---

## B.0.b Estado de ejecución (19-09-2026)

**Ejecutado y verificado. El informe final ya tiene citas y bibliografía administrables desde Word.**

### Calibración (resuelta con tus propios documentos)

Se creó `docx/calibrar_word.py` (extrae la plantilla de un `.docx` real) y `docx/calibrar_tipos.py` (recorre una carpeta y resume los tipos de fuente). Resultados obtenidos de tus archivos, en `docx/calibracion/`:

| Dato calibrado | Valor real de tu Word |
| :--- | :--- |
| Raíz de la parte de fuentes | `<b:Sources SelectedStyle="\APASixthEditionOfficeOnline.xsl" StyleName="APA" Version="6">` |
| Campo de cita | ` CITATION <Tag> \l 13322 ` (es-CL) |
| Campo de la lista | ` BIBLIOGRAPHY \l 13322 ` |
| Orden de elementos de `<b:Source>` | **No hay orden fijo**: Word escribió 20 órdenes distintos. El esquema es de tipo `all`, así que no hay que replicar ninguna secuencia |
| Autor institucional | `<b:Corporate>` dentro de `<b:Author>` |
| Relación de la parte | De `word/_rels/document.xml.rels`, tipo `…/customXml`, a `../customXml/itemN.xml` |
| Content types | `Default` para `xml` + `Override` por cada `itemPropsN.xml` |

**Hallazgo que simplificó todo:** la plantilla institucional **ya contiene** la parte de fuentes vacía (`customXml/item4.xml` con `<b:Sources>` y su `itemProps4.xml` con el `schemaRef` de la bibliografía). El pipeline ahora **rellena esa parte** en lugar de crear una nueva: no se tocan content types ni relaciones, y la parte queda exactamente con los atributos que Word espera.

### Implementación

| Componente | Función |
| :--- | :--- |
| `docx/bibliografia.py` | Lee el `.bib`, lo traduce a `<b:Source>` (con GUID estable derivado de la clave para no duplicar fuentes), y construye los campos `CITATION` y `BIBLIOGRAPHY` |
| Paso `bibliografia` | Escribe `build/sources.xml`, calcula con citeproc el **texto APA 7 en caché** de cada cita y genera `build/auditoria_citas.md` |
| Doble pasada de Pandoc | Pasada 1 con `--citeproc` (texto APA 7 y entradas de la lista) y pasada 2 **sin** citeproc, que produce el cuerpo donde se insertan los campos |
| Marcadores | `[@clave]` → `CITA__clave` (o `CITA__clave1__clave2`) y `::: {#refs}` → `BIBLIOGRAFIA__WORD` |
| Cirugía XML | Los marcadores se convierten en campos `CITATION`; las entradas de la lista de Pandoc se envuelven en un único campo `BIBLIOGRAPHY` multi-párrafo, conservando el estilo institucional |
| Atribuciones | Nota `Fuente:` bajo **cada** tabla y figura (`PIEDEFODO`, 56 notas), con `<!--#fuente:…-->` para indicar una fuente distinta de «elaboración propia» |

### Resultado verificado

| Comprobación | Valor |
| :--- | :--- |
| Fuentes en la parte bibliográfica del DOCX | **16** (`customXml/item4.xml`) |
| Campos `CITATION` con su texto APA 7 en caché | **34** |
| Campo `BIBLIOGRAPHY` en el capítulo 10 | **1**, con las 16 entradas |
| Citas → fuente y fuente → cita | 16/16 en ambos sentidos |
| Notas de fuente en tablas y figuras | **56** (20 tablas + 36 figuras) |
| Validaciones del pipeline | **31**, con 0 errores y 0 advertencias |

### Correcciones de citas aplicadas

- Se retiraron las **2 citas manuales** `(INE, 2026; CBRE, 2026)` y `(Colliers, 2026)`: no son convertibles porque no existe una fuente identificable. En su lugar quedó un **aviso visible** en el capítulo 2 que enumera las seis fuentes de mercado a completar (CChC, CBRE, Colliers, INE, JLL y GPS Property) con lo que falta de cada una. **No se inventó ningún dato.**
- Se añadió la atribución de la tabla de evidencia digital y de la figura de magnitud de la vacancia.
- No había citas narrativas ni textuales con página en el documento (verificado): no hubo páginas que inventar.

### Limitaciones registradas en la auditoría (requisito 15)

1. Pandoc no genera campos ni fuentes nativas: toda la conversión es post-proceso OOXML.
2. La caché está generada con `apa.csl` (APA 7); al pulsar `F9` Word recompone con **su** estilo, que en esta instalación es el XSL de **APA 6** (`\APASixthEditionOfficeOnline.xsl`). Si tu versión de Word ofrece APA 7, cámbialo en Referencias → Estilo; el texto en caché seguirá mostrando APA 7 mientras no actualices campos.
3. Las leyes chilenas se registran como `Misc` porque Word no tiene un tipo propio para legislación.
4. Las citas con más de una fuente llevan un campo por fuente: el resultado visible es APA correcto, pero al pulsar `F9` Word puede componer cada campo con sus propios paréntesis.
5. La fecha de consulta de las fuentes en línea no se escribe mientras no esté verificada.
6. Los 5 anexos no llevan campos de cita ni parte de fuentes: no citan nada y la obra bibliográfica es única (capítulo 10 del informe).

### Verificación manual pendiente

1. Abrir `Informe_Final.docx` en Word.
2. **Referencias → Administrar fuentes**: deben aparecer las 16 fuentes del documento.
3. `Ctrl+A` → `F9` y comprobar que las citas y la lista se mantienen.
4. Revisar el aviso de pendientes del capítulo 2 y completar los datos de las fuentes de mercado cuando los tengas.

---

## B.1 Qué necesita exactamente Word (base técnica)

### B.1.1 Parte de fuentes (lo que alimenta "Administrar fuentes")

| Elemento del paquete | Contenido |
| :--- | :--- |
| `customXml/item1.xml` | Raíz `<b:Sources xmlns:b="http://schemas.openxmlformats.org/officeDocument/2006/bibliography" SelectedStyle="…" StyleName="APA" Version="6">` con un `<b:Source>` por obra |
| `customXml/itemProps1.xml` | `<ds:datastoreItem>` con `<ds:schemaRef ds:uri="http://schemas.openxmlformats.org/officeDocument/2006/bibliography"/>` |
| `_rels/.rels` | Relación de la raíz a `customXml/item1.xml`, tipo `…/relationships/customXml` |
| `customXml/_rels/item1.xml.rels` | Relación a `itemProps1.xml`, tipo `…/customXmlProps` |
| `[Content_Types].xml` | Override de `customXml/itemProps1.xml` como `…customXmlProperties+xml` y de `customXml/item1.xml` como `application/xml` |

Estructura de cada obra (ejemplo con los elementos que se usarán):

```xml
<b:Source>
  <b:Tag>sommerville</b:Tag>
  <b:SourceType>Book</b:SourceType>
  <b:Guid>{9f1c1c4e-…}</b:Guid>
  <b:Author>
    <b:Author>
      <b:NameList>
        <b:Person><b:Last>Sommerville</b:Last><b:First>Ian</b:First></b:Person>
      </b:NameList>
    </b:Author>
  </b:Author>
  <b:Title>Software Engineering</b:Title>
  <b:Year>2016</b:Year>
  <b:City>Boston, MA</b:City>
  <b:Publisher>Pearson Education</b:Publisher>
  <b:Edition>10</b:Edition>
</b:Source>
```

> **Orden de los elementos:** el esquema `CT_SourceType` es una **secuencia** y Word es estricto con el orden (el mismo problema que ya se resolvió con `tblStyle→tblW→tblBorders…` y con `abstractNum` antes de `num`). El orden exacto **no se adivina**: se copia del archivo que produce la propia instalación de Word (ver B.2, calibración).

### B.1.2 Citas en el cuerpo (campos, no texto)

```xml
<w:r><w:fldChar w:fldCharType="begin"/></w:r>
<w:r><w:instrText xml:space="preserve"> CITATION sommerville \l 13322 </w:instrText></w:r>
<w:r><w:fldChar w:fldCharType="separate"/></w:r>
<w:r><w:t xml:space="preserve">(Sommerville, 2016)</w:t></w:r>
<w:r><w:fldChar w:fldCharType="end"/></w:r>
```

- El `Tag` del campo debe coincidir con `<b:Tag>` de la fuente → **el citekey del `.bib` pasa a ser el tag** y el texto `[@clave]` del markdown no cambia.
- Texto entre `separate` y `end` = caché visible en el documento. Al pulsar `F9`, Word lo recalcula con **su** estilo APA.
- `\l 13322` corresponde a es-CL. Si tu Word escribe otro valor, se usa el que aparezca en la calibración.

### B.1.3 Lista de referencias (un solo campo)

`::: {#refs}` se reemplaza por un campo `BIBLIOGRAPHY`:

```xml
<w:fldSimple w:instr=" BIBLIOGRAPHY \l 13322 ">
  <w:r><w:t>…entradas APA 7 (una por párrafo con estilo BIBLIOGRAFÍA1)…</w:t></w:r>
</w:fldSimple>
```

Ventaja: la lista deja de ser texto duplicado y pasa a **derivarse de las fuentes citadas**, que es exactamente lo que pide el requisito 8 (no mantener una lista manual desincronizable).

---

## B.2 Fase B-1 — Calibración con Word (paso previo, 15 minutos, evita todo el ensayo y error)

Se crea en Word un documento de prueba `docx/calibracion/calibracion.docx` con:

1. **Una fuente por tipo** (Libro, Artículo de revista, Artículo de congreso, Sitio web, Informe, Norma, Caso, Misceláneo).
2. **Cuatro citas distintas**: parentética simple `(Autor, Año)`; múltiple `(Autor1, Año; Autor2, Año)`; **narrativa con autor omitido** `Autor (Año) señala…` (usando *Editar cita → Omitir autor*); y **cita textual con página** `(Autor, Año, p. 45)`.
3. Guardar y extraer de ese DOCX: `customXml/item*.xml`, su `itemProps`, `[Content_Types].xml`, `_rels/.rels` y los `w:instrText` de las 4 citas.

**Resultado:** el orden exacto de los elementos de `<b:Source>`, el valor real de `SelectedStyle`/`StyleName` y los conmutadores exactos de los campos. Todo el generador se construye sobre esa plantilla real, no sobre suposiciones.

> Si tu Word no ofrece APA 7 como estilo (solo APA 6), el documento lo dirá explícitamente y el texto en caché seguirá siendo APA 7 (generado con `apa.csl`), pero al pulsar F9 Word recompondría con el estilo seleccionado. Ese punto es `[REVISAR EN WORD]` y se informará en la auditoría.

---

## B.3 Fase B-2 — Auditoría y normalización del `.bib`

1. **Clasificación al tipo de fuente de Word** (`b:SourceType`):

| Tipo en el `.bib` | Obras | `b:SourceType` |
| :--- | :--- | :--- |
| `@book` | Sommerville (2016), PMBOK 7 (2021) | `Book` |
| `@article` (actas USENIX) | Provos & Mazières (1999) | `ConferenceProceedings` |
| `@misc` → ley/norma chilena | Ley 21.461, 21.719, 19.799 | `Case` (norma legal) — `[REVISAR]`: determinar si se documenta como norma o como sitio institucional BCN |
| `@misc` → norma técnica | ISO/IEC 25010:2011, PCI-DSS v4.0 | `Report` (con `b:StandardNumber`) |
| `@misc` → documentación oficial en línea | Go, Next.js, PostgreSQL, PostGIS, Docker, Cloud Run, BigQuery, W3C WCAG 2.1 | `InternetSite` (con `b:InternetSiteTitle`, `b:URL`, `b:YearAccessed`, `b:MonthAccessed`, `b:DayAccessed`) |

2. **Campos obligatorios por tipo:** se valida que cada entrada tenga lo mínimo para ser una fuente identificable (autor/institución, título, año, y según el tipo: editorial y ciudad, congreso, nombre y URL del sitio, fecha de consulta, número de norma). Lo que falte **no se inventa**: queda listado.
3. **Duplicados:** normalización de autor+año+título para detectar la misma obra registrada dos veces (hoy: ninguna).
4. **Entradas incompletas (8 hoy):** se mantienen en el catálogo con los datos verificables y una nota `REVISAR FUENTE` que se refleja tanto en el documento como en el informe de auditoría con el dato exacto que falta.
5. **Fuentes de mercado no identificables:** *Cámara Chilena de la Construcción, CBRE, Colliers, INE, JLL y GPS Property* se incorporan a un registro aparte (`build/fuentes_pendientes.md`) con la afirmación concreta que respaldan y los datos que faltan (informe, período, URL, fecha). **No se crean fuentes con datos inventados** y **no se mantienen como citas falsas** en el texto.

---

## B.4 Fase B-3 — Módulo nuevo `docx/bibliografia.py`

| Función | Responsabilidad |
| :--- | :--- |
| `leer_bib()` | Parser del `.bib` (entradas, tipos, campos, notas `PENDIENTE`) |
| `a_fuente_word(entrada, plantilla)` | Traduce la entrada al XML `<b:Source>` usando el orden y los atributos de la plantilla de calibración |
| `guid_estable(tag)` | UUIDv5 derivado del tag → re-ejecutar el pipeline **no duplica** fuentes |
| `escribir_parte(path)` | Escribe `customXml/item1.xml` + `itemProps1.xml` y sus relaciones + content types |
| `campo_cita(tag, modo, pagina, cache)` | Construye el XML del campo `CITATION` según los conmutadores calibrados (`parentetica`, `narrativa`, `textual`, `multiple`) |
| `campo_bibliografia(entradas)` | Construye el campo `BIBLIOGRAPHY` con las entradas en caché |
| `auditar()` | Genera `build/auditoria_citas.md` con las métricas del punto B-8 |

**Doble pasada de Pandoc (clave del diseño):**

| Pasada | Entrada | Salida | Para qué |
| :--- | :--- | :--- | :--- |
| **1 (se conserva la actual)** | `informe_ensamblado.md` con `[@clave]` + `--citeproc --csl=apa.csl` | `build/body.docx` | Obtener el **texto APA 7 exacto** de cada cita y de cada entrada de la lista (se usa como caché de los campos) |
| **2 (nueva)** | `informe_ensamblado_citas.md` con marcadores `[[CITA:clave:modo]]` y **sin** `--citeproc` | `build/body_citas.docx` | Documento que se ensambla en la plantilla; los marcadores se convierten en campos `CITATION` y el bloque `#refs` en el campo `BIBLIOGRAPHY` |

Así la apariencia APA 7 sigue siendo la de tu `apa.csl`, y al mismo tiempo las citas quedan vinculadas a fuentes administrables.

---

## B.5 Fase B-4 — Conversión de las citas dentro del documento

| Caso | Tratamiento |
| :--- | :--- |
| **Parentética simple** `[@sommerville]` | Campo `CITATION` con caché `(Sommerville, 2016)` |
| **Múltiple** `[@docker; @cloudrun]` | Campos por fuente con el separador exacto que use Word (según calibración) y caché `(Google Cloud, s.f.; Docker Inc., s.f.)` |
| **Narrativa** `Autor (Año) señala…` | Se conserva la forma narrativa APA (requisito 6): el autor queda como texto y el campo aporta el año, replicando el mecanismo "omitir autor" que Word usa internamente (según calibración) |
| **Textual con página** | Hoy **no existe** ninguna. Si se agrega alguna, el campo llevará la página y la caché incluirá `, p. N`. Si falta la página, se inserta el aviso `[REVISAR FUENTE: falta la página de la cita textual]` y se lista en la auditoría (requisito 7: no inventar páginas) |
| **Cita manual `(INE, 2026; CBRE, 2026)` / `(Colliers, 2026)`** | No se pueden convertir (no hay fuente identificable). Se retiran como cita y se reemplazan por una **nota visible en estilo `DESTACADO2`**: `PENDIENTE: registrar la fuente del dato de vacancia (informe, período, URL)`. Igual tratamiento para las menciones sin cita de la línea 37, la línea 59 y la afirmación de la línea 15 |
| **Nunca duplicar** | Se verifica que ninguna referencia quede a la vez como texto manual y como campo (requisito 2) |
| **Un solo `<b:Source>` por obra** | El tag es el citekey: aunque una obra se cite 5 veces, hay **una** fuente (requisito 3) |

---

## B.6 Fase B-5 — Atribuciones en tablas y figuras (requisito 10)

1. **Inventario:** se recorren las **20 tablas** y las figuras del cuerpo y de los 5 anexos revisando si el contenido proviene de una fuente externa.
2. **Hoy:** solo la tabla de evidencia digital dice "(Adaptada)" → se reemplaza por `Fuente: elaboración propia a partir de …` con el campo de cita correspondiente si el origen es una obra registrada; el resto de tablas y todas las figuras son **elaboración propia** y quedan con la línea `Fuente: elaboración propia.`
3. **Datos de mercado (vacancia):** las tablas/figuras que muestren cifras de terceros **solo se atribuyen cuando la fuente exista**; hasta entonces llevan el marcador de pendiente. No se inventan atribuciones.
4. Los diagramas nuevos del Plan A (topología, contexto, canvas, etc.) son **elaboración propia** salvo los que representen datos de terceros.

---

## B.7 Fase B-6 — Anexos

- **Anexo C** menciona ISO/IEC 25010 y Sommerville: se convierten en citas con campo (aplicando el mismo generador) y cada anexo recibe **la misma parte de fuentes** en su DOCX, de modo que Word pueda resolver las citas también allí.
- Los anexos **no** llevan lista de referencias propia: es una decisión explícita, porque la obra es única y la lista vive en el capítulo 10 del informe. Queda declarado en la auditoría.

---

## B.8 Fase B-7 — Auditoría completa (requisito 14)

Salida: `docx/build/auditoria_citas.md` con estas métricas y el detalle de cada hallazgo:

| Métrica | Cómo se calcula |
| :--- | :--- |
| Fuentes encontradas | Entradas del `.bib` + fuentes detectadas en el texto |
| Fuentes incorporadas a Word | Nodos `<b:Source>` escritos en la parte `customXml` |
| Citas detectadas | Marcadores y `[@clave]` localizados en el markdown |
| Citas corregidas | Citas manuales convertidas o retiradas + citas reasignadas |
| Fuentes duplicadas eliminadas | Pares autor+año+título normalizados coincidentes |
| Fuentes incompletas | Entradas sin los campos obligatorios de su tipo |
| Citas sin fuente | Citas que no resuelven a ninguna entrada |
| Fuentes sin cita | Entradas del catálogo no citadas en el texto (hoy: 0) |
| Figuras con fuente | Figuras con línea de atribución externa |
| Tablas con fuente | Tablas con línea de atribución externa |
| Requieren revisión manual | Todo lo marcado `[REVISAR FUENTE]` / `PENDIENTE`, con el dato que falta |

---

## B.9 Fase B-8 — Validaciones nuevas (se suman a las del Plan A)

| # | Validación |
| :--- | :--- |
| 29 | Toda cita del texto resuelve a una entrada del catálogo (A: cita → fuente) |
| 30 | Toda entrada del catálogo está citada al menos una vez (B: fuente → cita) |
| 31 | Sin fuentes duplicadas |
| 32 | Sin fuentes incompletas para su tipo |
| 33 | Cada campo `CITATION` tiene un `<b:Tag>` con fuente correspondiente en la parte de fuentes |
| 34 | La parte `customXml` de fuentes existe, es XML bien formado y está declarada en relaciones y content types |
| 35 | Existe el campo `BIBLIOGRAPHY` en el capítulo 10 y su caché no está vacía |
| 36 | No quedan patrones de cita manual (`(Autor, 2024)`) sin fuente asociada |
| 37 | No coexiste cita manual y cita de campo para la misma obra |
| 38 | Todo `[REVISAR FUENTE]` del documento aparece en la auditoría |
| 39 | El paquete completo sigue siendo válido (se extiende la validación 18 a las partes nuevas) |

**Comprobación final manual (irremplazable):** abrir `Informe_Final.docx` en Word y verificar que **Referencias → Administrar fuentes** lista las fuentes del documento, que el índice se actualiza con `Ctrl+A` → `F9` y que las citas siguen mostrando el texto APA 7 correcto.

---

## B.10 Límites técnicos que se informarán (requisito 15: no ocultarlos)

1. **Pandoc no genera campos de Word.** El 100 % de las citas nativas se produce por post-proceso XML; Pandoc solo aporta el texto APA 7 de la caché.
2. **La caché y el recálculo pueden diferir.** El texto que se ve está generado con `apa.csl` (APA 7). Si el usuario pulsa `F9`, Word recompone las citas con **su** implementación de APA, que puede diferir en detalles ("&" vs "y", umbral de "et al.", formato de normas legales, "s.f." vs "sin fecha"). Se informará caso por caso.
3. **Estilo APA 7 en Word.** Depende de la versión instalada de Word. Si solo ofrece APA 6, el documento seguirá mostrando texto APA 7 en caché y se avisará explícitamente.
4. **Normas legales chilenas.** Word no tiene un tipo de fuente específico para legislación; se documenta la correspondencia elegida y su efecto en el renderizado.
5. **Citas narrativas y con página.** Dependen de conmutadores internos que solo se conocen con certeza tras la calibración; si alguno no se puede reproducir, esas citas quedarán como **texto APA 7 correcto pero sin campo**, y la auditoría dirá exactamente cuáles y por qué.
6. **Fuentes sin datos suficientes.** Se listan como pendientes; no se completan con datos inventados.

---

## B.11 Orden de ejecución propuesto

| Fase | Contenido | Entregable |
| :--- | :--- | :--- |
| **B-1** | Calibración con Word (requiere que tú abras y guardes el documento de prueba) | `docx/calibracion/plantilla_word/` con el XML real |
| **B-2** | Auditoría y normalización del `.bib` | `referencias.bib` normalizado + `build/fuentes_pendientes.md` |
| **B-3** | Módulo `bibliografia.py` y generación de la parte de fuentes | `build/sources.xml` + parte dentro del DOCX |
| **B-4** | Doble pasada de Pandoc + cirugía de campos en el cuerpo | `build/body_citas.docx` |
| **B-5** | Citas manuales, menciones sin fuente y atribuciones de tablas y figuras | markdown corregido |
| **B-6** | Anexos (parte de fuentes + cita del Anexo C) | 5 DOCX regenerados |
| **B-7** | Validaciones 29-39 + auditoría | `build/auditoria_citas.md` |
| **B-8** | Ensamblado final y verificación manual en Word | `build/Informe_Final.docx` |

**Rollback:** el `build/body.docx` y la copia actual del informe se conservan; si la parte de fuentes diera problemas en Word, se puede generar una variante "sin fuentes nativas" (citas y lista en texto APA 7) sin perder el trabajo hecho.

---

## B.12 Criterios de aceptación

1. Conserva la plantilla institucional, la portada, los encabezados y la numeración de capítulos.
2. Las citas del texto son campos de Word con caché APA 7 y **una sola fuente por obra**.
3. El capítulo 10 es un campo `BIBLIOGRAPHY` derivado de las fuentes citadas.
4. `Referencias → Administrar fuentes` muestra las fuentes **del documento**.
5. Correspondencia verificada en ambos sentidos (cita → fuente y fuente → cita).
6. Ninguna referencia inventada; todo dato faltante está marcado `[REVISAR FUENTE]` con lo que falta.
7. Sin citas duplicadas ni inconsistentes.
8. La auditoría declara qué quedó como campo nativo y qué quedó como texto, con el motivo.
