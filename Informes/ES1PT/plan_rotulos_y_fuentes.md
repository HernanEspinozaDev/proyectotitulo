# Plan — Rótulos APA 7, índice de ilustraciones y fuentes del informe

> Proyecto: EspaciGo · Documento: `docx/build/Informe_Final.docx`
> Fecha del diagnóstico: 20-09-2026 · Estado: **APLICADO el 20-09-2026** (ver §9)

---

## 1. Objetivo

1. **Rótulo arriba**: cada tabla y cada figura debe llevar **arriba** el rótulo `Tabla N` / `Figura N` en negrita y el **título en cursiva** (formato APA 7), y **abajo** solo la nota de fuente (que hoy ya está bien).
2. **Índice de ilustraciones**: agregar un índice de tablas y de figuras, con esos mismos rótulos, con número de página.
3. **Tipografía homogénea**: **Calibri 11** en todo el informe y **Calibri 12** en los títulos, eliminando los textos que hoy quedan más grandes (o más chicos) por estilos heredados de la plantilla.

---

## 2. Diagnóstico (qué pasa hoy, con evidencia)

### 2.1 Rótulos

Estado actual generado por `paso_preprocesar()` en `docx/generar_informe.py`:

| Elemento | Hoy | Problema |
| :--- | :--- | :--- |
| Tabla | `::: TABLATTULO` → `Tabla 4. Escenarios de monetización` **arriba** de la tabla | Formato APA incorrecto: rótulo y título en una sola línea, sin negrita/cursiva |
| Figura | `![Figura 7. Flujo de reservas](…png)` → el alt de Pandoc se dibuja **debajo** de la imagen con estilo `PIEDEFOTO` | El título queda **abajo** y con el aspecto de una nota (por eso «aparece un texto como figura») |
| Nota | `::: PIEDEFOTO` → `Fuente: elaboración propia.` debajo | **Correcto**, se mantiene |

### 2.2 Fuentes y tamaños reales del documento

Medición sobre el DOCX final (tamaño efectivo por estilo; `docDefaults` = tema **minorFont = Calibri**, `sz=22` = **11 pt**):

| Estilo | Dónde se usa | Tamaño hoy | Debería ser |
| :--- | :--- | :--- | :--- |
| `PARRAFO` (238 párr.) | cuerpo | 11 pt ✔ | 11 |
| `Bibliografa` (28) | bibliografía | 11 pt ✔ | 11 |
| `Prrafodelista` (13) | listas | 11 pt ✔ | 11 |
| `Ttulo1` (11) | **títulos de capítulo** | **14 pt (Calibri Light)** ✗ | **12** |
| `Subtitulo1` (19) / `Subtitulo2` (32) | subtítulos | 11 pt ✗ | **12** |
| `Estilo4` («Contenido») | título del índice | **14 pt** ✗ | 12 |
| `TABLAPRRAFO` (829) | texto de tablas | **10 pt** ✗ | 11 |
| `PIEDEFOTO` (93) | notas de fuente | **9 pt** ✗ | 11 |
| `TABLATTULO` (21) | rótulo de tabla | 11 pt | 11 (reformateado) |
| `TDC1/2/3` (57) | entradas del índice | **12 pt directo** ✗ | 11 |
| `Estilo1`, párrafos sin estilo | **portada** | 14 y 24 pt | *a confirmar* |

**Respuesta al «¿por qué hay algunos textos más grandes?»**: los títulos de capítulo y el rótulo «Contenido» no heredan el 11 pt del documento sino que traen tamaño fijo de la plantilla (14 pt, `sz=28`), y los títulos usan la fuente *Calibri Light* (fuente mayor del tema) en vez de Calibri. En el sentido contrario, el texto de tablas (10 pt) y las notas (9 pt) quedan más chicos que el cuerpo. Las entradas del índice llevan 12 pt aplicados directamente en el texto, no por estilo.

---

## 3. Formato objetivo (APA 7)

```
**Tabla 4**⏎
*Escenarios de monetización y comisión*
                                  ← (aquí va la tabla)
Fuente: elaboración propia.

**Figura 7**⏎
*Flujo de reserva, pago con retención y liquidación*
                                  ← (aquí va la imagen)
Fuente: elaboración propia.
```

* Rótulo (`Tabla 4` / `Figura 7`) en **negrita**, en su propio renglón.
* Título en *cursiva* en el renglón siguiente, alineado a la izquierda.
* `Fuente:`/`Nota.` **debajo** del objeto, sin negrita.
* Los números siguen siendo los del pipeline (contadores `tab`/`fig` de `paso_preprocesar`), así que **no cambian** las referencias del texto («Tabla 3», «Tabla 4»…).

---

## 4. Cambios propuestos

### 4.1 `docx/generar_informe.py` — rótulos (`paso_preprocesar`)

En `rep_caption_tabla` y `rep_figura`:

* **Tabla:** emitir el rótulo con estilo propio y dos renglones dentro del mismo párrafo (salto de línea `\` para no crear dos párrafos, que duplicarían la entrada del índice):

  ```
  ::: {custom-style="ROTULOTABLA"}
  **Tabla 4**\
  *Escenarios de monetización y comisión*
  :::
  ```

* **Figura:** mover el rótulo **antes** de la imagen y dejar la imagen sin pie:

  ```
  ::: {custom-style="ROTULOFIGURA"}
  **Figura 7**\
  *Flujo de reserva, pago con retención y liquidación*
  :::

  ![](imagenes/figura-s4-doble-reserva.png){width=6.3in}

  ::: {custom-style="PIEDEFOTO"}
  Fuente: elaboración propia.
  :::
  ```

  La imagen pasa a tener **alt vacío** para que Pandoc no genere el párrafo `ImageCaption` (que es lo que hoy pone el título debajo). Si Pandoc igual emite un párrafo de pie vacío, se elimina en `_preparar_cuerpo()`.

### 4.2 `docx/generar_informe.py` — estilos nuevos (`_estilos_institucionales`)

Función nueva que devuelve el `styles.xml` con:

* **Estilos nuevos** (definidos por el pipeline, porque la plantilla no los trae):
  * `ROTULOTABLA` (nombre `RotuloTabla`): Calibri 11, `keepNext` (para que no se separe de la tabla), espacio antes 12 / después 0, sin numeración.
  * `ROTULOFIGURA` (nombre `RotuloFigura`): ídem.
* **Ajustes de tamaño** sobre estilos existentes:

| Estilo | Cambio |
| :--- | :--- |
| `Ttulo1` | `sz=24` (12 pt) y `rFonts` explícito **Calibri** (hoy hereda *Calibri Light* a 14 pt) |
| `Subtitulo1`, `Subtitulo2` | `sz=24` (12 pt), Calibri, `keepNext` |
| `Estilo4` | `sz=24` (12 pt) |
| `TABLAPRRAFO` | `sz=22` (11 pt) |
| `PIEDEFOTO` | `sz=22` (11 pt) |
| `TDC1`, `TDC2`, `TDC3` | `sz=22` (11 pt) |
| `NOTAALPIE`, `Piedepgina` | sin cambio (pie institucional) |
| `TABLATTULO` | queda disponible pero **sin uso** (se reemplaza por `ROTULOTABLA`) |

* **Barrido de tamaños y fuentes directos** en los párrafos del cuerpo: quitar `<w:sz>` y `<w:rFonts>` de los `rPr` de los runs (dejando negrita/cursiva), porque cualquier tamaño puesto directamente gana sobre el estilo. Cubre las entradas de índice con 12 pt y los restos que trae el cuerpo de Pandoc.
* **Portada**: ver decisión D1 en §7.

### 4.3 `docx/generar_informe.py` — índice de ilustraciones

1. Generalizar `_campo_toc()` a `_campo_indice(instruccion, aviso="")`, con dos usos nuevos:
   * ` TOC \h \z \t "RotuloTabla;1" `
   * ` TOC \h \z \t "RotuloFigura;1" `
   (mismo mecanismo que el índice general, que ya usa `\t "Título1;1;Subtitulo1;2;Subtitulo2;3"`; las entradas llevan el rótulo «Tabla N …» / «Figura N …» que pidió).
2. En `_ensamblar(con_portada=True)`, después del índice general y antes del salto de página, insertar una página nueva:

   ```
   salto de página
   «Índice de tablas y figuras»        (estilo Estilo4, como «Contenido»: no entra al índice general)
   «Tablas»                            (estilo RotuloTabla, sin numeración)
   [campo TOC de tablas]
   «Figuras»                           (estilo RotuloFigura, sin numeración)
   [campo TOC de figuras]
   salto de página (inicio del capítulo 1)
   ```
3. `settings.xml` ya lleva `updateFields`, así que Word rellena los tres índices al abrir; `docx/actualizar_campos.ps1` (que ya recorre `StoryRanges` y `TablesOfContents`) los fija antes de entregar.

### 4.4 Validaciones nuevas (`paso_validar`)

| # | Comprobación |
| :-- | :--- |
| 34 | Cada tabla tiene su rótulo `Tabla N` (negrita) **inmediatamente antes** de la tabla y su nota después |
| 35 | Cada figura tiene su rótulo `Figura N` **inmediatamente antes** de la imagen y su nota después |
| 36 | Ninguna imagen conserva el pie de Pandoc (`ImageCaption`) |
| 37 | El documento incluye los dos campos de índice de ilustraciones |
| 38 | Tamaños: ningún run del cuerpo tiene 14 pt ni más; los títulos están a 12 pt y el cuerpo a 11 |
| 39 | Fuente Calibri declarada en los estilos de cuerpo y títulos (sin *Calibri Light*) |

### 4.5 Documentación

* Actualizar `ES1PT/auditoria_final_ES1.md` (nueva ronda) y `/memories/repo/es1pt_docx_pipeline.md`.
* Anotar en `ES1PT/plan_conversion_docx.md` que las notas van debajo y los rótulos arriba.

---

## 5. Verificación posterior

1. `python docx\generar_informe.py todo` → 0 errores / 0 advertencias (con las validaciones 34–39).
2. Comprobación estructural del DOCX: 21 rótulos de tabla, 36 de figura, 57 entradas de índice de ilustraciones, 0 `ImageCaption`.
3. `docx\actualizar_campos.ps1` → los 3 índices con páginas y sin errores de campo.
4. Inventario de fuentes/tamaños sobre el archivo final: `Calibri 11` en cuerpo, tablas, notas y bibliografía; `Calibri 12` en capítulos y subtítulos; 0 textos de 14 pt salvo la portada (según D1).
5. Verificación en Word por COM: `Sources.Count = 28`, `TablesOfContents.Count = 3`, 0 «Fuente especificada no válida», 0 «Marcador no definido».

---

## 6. Orden de ejecución

| Paso | Contenido | Riesgo |
| :-- | :--- | :--- |
| 1 | Rótulos arriba (tablas y figuras) en `paso_preprocesar` + comprobar que Pandoc no emite pie | Bajo |
| 2 | Estilos nuevos + ajustes de tamaño/fuente (§4.2) | Bajo |
| 3 | Índice de tablas y figuras (§4.3) | Medio: depende del `\t` de Word |
| 4 | Validaciones 34–39 | Bajo |
| 5 | Regenerar, actualizar campos y verificar (§5) | Bajo |

---

## 7. Decisiones a confirmar

* **D1 — Portada.** La portada (estilo `Estilo1` y cuadros de texto) usa 24 pt para «EspaciGo» y 14 pt en los rótulos institucionales. ¿Se deja como está (es el diseño de la plantilla) o también se lleva a 12/11? Recomendación: **dejarla como está**; el pedido de 11/12 aplica al cuerpo y a los títulos.
* **D2 — Entradas del índice general.** Hoy están a 12 pt. Con la regla «títulos 12, resto 11», el índice general es una lista → **11 pt** (los capítulos dentro del índice no son títulos de sección). Alternativa: capítulos del índice a 12 y subniveles a 11.
* **D3 — Índice de ilustraciones.** Propuesto: dos listas («Tablas» y «Figuras») en una misma página. Alternativa: una sola lista combinada en orden de aparición (`TOC \t "RotuloTabla;1;RotuloFigura;1"`).
* **D4 — Ubicación.** El índice de ilustraciones va en página nueva **después** del índice general (antes del capítulo 1). Alternativa: al final del documento.

---

## 8. Riesgos y planes B

**Prueba de viabilidad ya realizada** (documento de prueba convertido con Pandoc usando `plantilla.docx` como `--reference-doc`):

| Suposición | Resultado |
| :--- | :--- |
| Pandoc conserva `custom-style="ROTULOTABLA"` aunque el estilo no exista en la plantilla | **Confirmado**: los `pStyle` `ROTULOTABLA` y `ROTULOFIGURA` llegan intactos al DOCX; basta inyectar los estilos al ensamblar |
| El salto de línea `\` mantiene rótulo y título en un solo párrafo | **Confirmado**: un párrafo con `<w:br/>` y los dos textos (`Tabla 1`⏎`Título`) → una sola entrada de índice |
| `![](imagen)` con alt vacío deja la imagen sin pie | **Confirmado**: no se genera ningún párrafo `ImageCaption` |

| Riesgo | Plan B |
| :--- | :--- |
| Word no resuelve `TOC \t "RotuloTabla;1"` | Usar `\c "Tabla"` con campos `SEQ Tabla` reales, o dejar una lista estática sin números de página |
| Cambiar tamaños rompe la paginación del índice | Regenerar y volver a ejecutar `actualizar_campos.ps1` (los números de página se recalculan) |
| Los rótulos nuevos quedan huérfanos al final de una página | `keepNext` en los estilos de rótulo (para que no se separen de la tabla o de la imagen) |

---

## 9. Estado: aplicado y verificado (20-09-2026)

Se aplicaron los cuatro apartados. Decisiones tomadas con el usuario: portada sin cambios, índice de ilustraciones en dos listas (Tablas y Figuras) después del índice general.

**Resultado verificado sobre el DOCX final:**

| Comprobación | Resultado |
| :--- | :--- |
| Rótulo sobre cada tabla | 21 rótulos `ROTULOTABLA`, formato «**Tabla N** / *Título*» (negrita + salto + cursiva), nota `Fuente:` debajo |
| Rótulo sobre cada figura | 36 rótulos `ROTULOFIGURA` («**Figura N** / *Título*»), imagen y nota debajo |
| Pie de Pandoc bajo las imágenes | 0 párrafos `ImageCaption` |
| Índices | 3 campos: contenido (62 entradas), tablas (21) y figuras (36) = **119 entradas con número de página** |
| Tipografía del cuerpo | Calibri 11 en cuerpo, tablas, notas, bibliografía e índices (sin tamaños directos) |
| Tipografía de títulos | Calibri 12 en capítulos, subtítulos y títulos de sección |
| Portada | intacta (24 pt y 14 pt del diseño institucional) |
| Anexos | Anexo D con 12 rótulos «Figura D.n» sobre sus diagramas y Calibri 11 |
| Validaciones | 39 comprobaciones, **0 errores y 0 advertencias** (nuevas: 34–39) |

**Hallazgo adicional corregido en esta ronda:** el mapeo de la bibliografía apuntaba a un estilo inexistente (`BIBLIOGRAFÍA1`); el estilo real de la plantilla es `BIBLIOGRAFA1`, que es el que trae la **sangría francesa** de APA. Las referencias quedaban sin sangría; ahora la tienen.
