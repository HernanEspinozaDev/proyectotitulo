# Plan — Normalización de los anexos al formato del informe final (APA 7)

> Proyecto: EspaciGo · Documentos: `docx/build/Anexo_A…E_*.docx`
> Fecha del diagnóstico: 20-09-2026 · Estado: **APLICADO el 20-09-2026** (ver §9)

---

## 1. Objetivo

Que cada anexo sea un documento académico autónomo con **el mismo formato del informe final**:

1. **Portada institucional** igual a la del informe, con el **nombre del anexo como título**.
2. **Índice de contenido** propio y, cuando corresponda, **índice de tablas** y **de figuras**.
3. **Rótulo APA 7 sobre cada tabla y cada figura** («**Tabla A.1** / *Título*») y **nota de fuente debajo**.
4. **Calibri 11** en el texto y **Calibri 12** en los títulos, con la misma jerarquía que el informe.

---

## 2. Estado actual (diagnóstico con evidencia)

| Anexo | H1 | H2 | H3 | Tablas | Figuras | Portada | Índice | Rótulos | Notas |
| :--- | --: | --: | --: | --: | --: | :---: | :---: | :---: | :---: |
| A — Actores y módulos | 1 | 6 | 18 | **18** | 0 | ✗ | ✗ | ✗ | ✗ |
| B — Catálogo de RF | 1 | 3 | 2 | **5** | 0 | ✗ | ✗ | ✗ | ✗ |
| C — Requerimientos no funcionales | 1 | 4 | 0 | **4** | 0 | ✗ | ✗ | ✗ | ✗ |
| D — Especificación de casos de uso | 1 | 16 | 73 | **74** | **12** | ✗ | ✗ | ✗ | ✗ |
| E — Historias de usuario | **10** | 37 | 36 | **4** | 0 | ✗ | ✗ | ✗ | ✗ |
| **Total** | | | | **105** | **12** | | | | |

Problemas concretos detectados:

1. **Sin portada ni índice.** `paso_anexos()` llama a `_ensamblar(..., con_portada=False, numerar=False)`, y esa rama **descarta todo el frente de la plantilla** (portada, «Contenido», campo TOC) y también deja `settings.xml` sin `updateFields` (verificado: `¿tiene campo TOC? False`, `¿updateFields? False`).
2. **Sin rótulos ni notas.** Las tablas de los anexos son *pipe tables* del Markdown sin marcador `<!--#tab:-->`, así que el preprocesador no las toca: se insertan «en crudo», sin «Tabla N», sin título y sin nota de fuente. Las 12 figuras del Anexo D ya llevan rótulo (*Figura D.n*) por un arreglo puntual en `preparar_anexo()`, pero **no** llevan nota.
3. **Salto de jerarquía.** `preparar_anexo()` demota **un nivel todos los títulos** («demota un nivel los títulos internos»), de modo que en los Anexos A–D el primer nivel interno queda como `Subtitulo2` directamente bajo el `Ttulo1` del anexo: **falta el nivel `Subtitulo1`**. (En el Anexo E sí funciona porque sus secciones están como H1.)
4. **Anexo E con 10 H1**: el título del documento y las 9 épicas comparten nivel, lo que confunde el índice.

---

## 3. Formato objetivo

```
ANEXO A — ACTORES Y MÓDULOS DEL SISTEMA        ← portada institucional
Asignatura: Proyecto de Título - TIH184 · Sección: D-IEI-N8-P1-C2/D · Académico: …
Integrantes: … · Fecha de entrega: …

Contenido                                        ← índice propio
1. Identificación de Actores                        2
1.1 Actores primarios …                            2

Índice de tablas                                 ← solo si el anexo tiene tablas
Tabla A.1 Actores primarios (roles humanos) …       3

**Tabla A.1**⏎                                   ← rótulo encima
*Actores primarios (roles humanos)*
| … tabla … |
Fuente: elaboración propia.                      ← nota debajo
```

* Numeración por anexo: **`Tabla A.1 … A.18`**, `Tabla D.1 … D.74`, `Figura D.1 … D.12` (misma convención que ya usan las figuras del Anexo D).
* Los índices de tablas y figuras se incluyen **solo si el anexo tiene** tablas o figuras (Anexo C: solo tablas; Anexo D: tablas y figuras; Anexos A, B, E: solo tablas).
* Jerarquía de títulos sin saltos: `Ttulo1` (anexo) → `Subtitulo1` → `Subtitulo2` → `Prrafodelista`.

---

## 4. Cambios propuestos

### 4.1 `docx/generar_informe.py` — rótulos y notas de tablas de anexo (`preparar_anexo`)

Hoy la función recorre líneas y solo cambia títulos y bloques PlantUML. Se extiende para:

1. **Detectar bloques de tabla**: desde la línea de cabecera `| … |` y su separador `|---|` hasta la última fila que empiece con `|`.
2. **Numerar y titular** cada tabla con un contador por anexo y el título obtenido según esta prioridad:
   1. línea `*Tabla. <título>*` inmediatamente encima (convención nueva, opcional, igual que en el informe);
   2. **título de contexto**: la última cabecera (`#`…`####`) vista antes de la tabla, quitándole la numeración de texto (`1.`, `2.1`) y los emoji;
   3. **línea en negrita** anterior (`**Justificación de las relaciones**`), que es el caso de 12 tablas del Anexo D;
   4. respaldo: «Datos de la sección».
3. **Emitir el rótulo antes** de la tabla, con el mismo formato del informe (`custom-style="ROTULOTABLA"`, etiqueta en negrita + salto + título en cursiva) y **la nota `Fuente: elaboración propia.` después** de la última fila (estilo `PIEDEFOTO`).
4. Añadir **la nota** también bajo las 12 figuras que ya rotula.

### 4.2 `docx/generar_informe.py` — jerarquía de títulos de anexo

Regla nueva en `preparar_anexo()`:

* si el anexo tiene **un solo H1** (A, B, C, D): ese H1 es el título del documento y **no se demota nada** → H2 → `Subtitulo1`, H3 → `Subtitulo2`, H4 → `Prrafodelista`;
* si tiene **varios H1** (E, con las 9 épicas): se demota un nivel (como hoy) → H1→`Subtitulo1`, H2→`Subtitulo2`, H3→`Prrafodelista`.

Resultado: ninguna sección queda saltándose un nivel y el índice de contenido queda con tres niveles útiles.

### 4.3 `docx/generar_informe.py` — portada, índice e índices de ilustraciones

* `_ensamblar()` recibe dos datos nuevos (por ejemplo `portada_anexo=(letra, titulo)`) y `ilustraciones=(n_tablas, n_figuras)`:
  * usa la **rama con portada** (la del informe) para que se conserven portada, «Contenido», encabezados y pies;
  * `_rellenar_portada()` con `meta` = el YAML del informe pero con **`proyecto` = «Anexo A — Actores y módulos del sistema»**, que es el campo «Nombre o título del proyecto» de la portada;
  * inserta el **índice de contenido** (`_campo_toc()`, igual que el informe) y, según `ilustraciones`, la página de **índice de tablas** y/o **de figuras** (`_indice_ilustraciones()` parametrizada, con los encabezados «Índice de tablas» e «Índice de figuras»);
  * **no** inyecta las 28 fuentes bibliográficas ni el campo `BIBLIOGRAPHY` (los anexos no llevan bibliografía propia, la lista es única en el informe);
  * mantiene `updateFields` para que Word construya los tres índices al abrir.
* `paso_anexos()` pasa esos parámetros por anexo y registra en el log cuántas tablas y figuras tiene cada uno.

### 4.4 Tipografía

Nada nuevo que programar: los anexos ya pasan por `_estilos_institucionales()` y `_limpiar_tamanos()`, así que **Calibri 11/12 ya está aplicado** (verificado: `ROTULOFIGURA` con Calibri en el Anexo D). Se agrega solo una validación que lo compruebe en cada anexo.

### 4.5 Validaciones nuevas (`paso_validar`)

| # | Comprobación |
| :-- | :--- |
| 40 | Cada anexo tiene portada con su nombre como título |
| 41 | Cada anexo tiene índice de contenido (campo TOC con `updateFields`) |
| 42 | Cada anexo con tablas o figuras tiene su índice de tablas y/o de figuras |
| 43 | Cada tabla de anexo lleva rótulo `Tabla <letra>.n` encima y nota debajo |
| 44 | Cada figura de anexo lleva rótulo `Figura <letra>.n` encima y nota debajo |
| 45 | Los anexos usan Calibri 11/12 sin tamaños directos y sin saltos de jerarquía |

### 4.6 Documentación

* `ES1PT/auditoria_final_ES1.md`: nueva parte con esta normalización.
* `/memories/repo/es1pt_docx_pipeline.md`: reglas de títulos y de rótulos automáticos en anexos.

---

## 5. Verificación posterior

1. `python docx\generar_informe.py todo` → 0 errores / 0 advertencias (con 40–45).
2. Estructura de cada anexo por XML: portada con el nombre, 1 campo TOC (+ los de ilustraciones), 105 rótulos de tabla, 12 de figura, 117 notas.
3. `docx\actualizar_campos.ps1` por anexo (o extenderlo a los cinco) → índices con número de página, 0 «Error! Marcador no definido».
4. Inventario de fuentes/tamaños por anexo: Calibri 11 y 12, sin excepciones.
5. Muestra de títulos generados automáticamente para revisar que sean coherentes (se imprimirá la lista de las 105 tablas con su título para validación visual).

---

## 6. Riesgos y planes B

| Riesgo | Plan B |
| :--- | :--- |
| Algún título automático queda poco descriptivo (p. ej. «Datos de la sección») | Añadir la línea `*Tabla. <título>*` en la fuente del anexo: el generador la respeta y tiene prioridad |
| Las 74 fichas del Anexo D suman 74 rótulos y 74 notas: documento más largo | Mantenerlos (es lo que exige APA) o limitar los rótulos a las tablas que no son fichas de caso de uso |
| Un anexo con 74 tablas genera un índice de tablas largo | Incluirlo igualmente; es el comportamiento correcto y así lo pidió el usuario |
| Word tarda en recalcular tres índices en documentos largos | `actualizar_campos.ps1` los fija una vez y se guarda el resultado |

---

## 7. Decisiones a confirmar

* **D1 — Portada.** (a) mantener el rótulo estático «FORMULACIÓN DEL PROYECTO DE TÍTULO» y el nombre «EspaciGo», poniendo el nombre del anexo en el campo «Nombre o título del proyecto» **(recomendado)**, o (b) reemplazar también el bloque grande del título por «ANEXO A — …».
* **D2 — Numeración.** Por letra del anexo (`Tabla A.1`, `Figura D.3`, **recomendado**, coherente con las figuras actuales) o correlativa dentro de cada documento (`Tabla 1`, `Tabla 2`).
* **D3 — Fichas de caso de uso.** ¿Cada una de las 52 fichas del Anexo D lleva su «Tabla D.n» y aparece en el índice de tablas? (Recomendado: sí.)

---

## 9. Estado: aplicado y verificado (20-09-2026)

Decisiones tomadas con el usuario: portada con el **nombre del anexo como título grande** (además del campo «Nombre o título del proyecto»), **numeración por letra** del anexo, y **todas** las fichas de caso de uso rotuladas.

### 9.1 Resultado por anexo

| Anexo | Portada | Índices | Rótulos de tabla | Rótulos de figura | Notas | Errores de campo |
| :--- | :---: | :---: | --: | --: | --: | --: |
| A — Actores y módulos | ✔ | 2 (contenido + tablas) | 18 | — | 18 | 0 |
| B — Catálogo de RF | ✔ | 2 (contenido + tablas) | 5 | — | 5 | 0 |
| C — Requerimientos no funcionales | ✔ | 2 (contenido + tablas) | 4 | — | 4 | 0 |
| D — Especificación de casos de uso | ✔ | 3 (contenido + tablas + figuras) | 74 | 12 | 86 | 0 |
| E — Historias de usuario | ✔ | 2 (contenido + tablas) | 4 | — | 4 | 0 |

Entradas del índice de cada anexo: A 43, B 11, C 9, D 176, E 51 (contenido + tablas + figuras), todas con número de página.

### 9.2 Portada

En los dos cuadros de texto de la portada:

```
PROYECTO DE TÍTULO: EspaciGo          (24 pt, sustituye a «FORMULACIÓN DEL PROYECTO DE TÍTULO»)
Anexo A — Actores y módulos del sistema   (24 pt, negrita: el título del anexo)
Asignatura: Proyecto de Título - TIH184 · Sección: D-IEI-N8-P1-C2/D · Académico guía: …
Integrantes del equipo: Hernán Espinoza, Anita Marchant, Erick Silva · Fecha de entrega: …
```

### 9.3 Rótulos y títulos generados automáticamente

Los títulos salen del título de sección que precede a cada tabla (sin su numeración ni emoji). Muestra:

| Anexo | Tabla | Título generado |
| :--- | :--- | :--- |
| A | A.1 | Actores Primarios (roles humanos) |
| A | A.5 | RF del módulo: RQF-001 a RQF-023 (23 RF) + complementarios… |
| B | B.3 | Brechas cerradas y módulo al que se incorpora cada RF |
| C | C.2 | Resumen por categoría (mínimo 3 RNF por categoría) |
| D | D.1 | Convenciones de modelado aplicadas |
| D | D.7 | CU-01: Registrar Cuenta |
| E | E.3 | Cobertura de los módulos del sistema por historias de usuario |

Formato final de cada rótulo: «**Tabla D.7**» / *CU-01: Registrar Cuenta*, encima de la tabla, con «Fuente: elaboración propia.» debajo. Las figuras mantienen «**Figura D.n**» + título.

### 9.4 Jerarquía de títulos

Se aplicó la regla de §4.2: los Anexos A–D (un solo H1) no se demotan (H2 → `Subtitulo1`) y el Anexo E (10 H1, con las 9 épicas) sí (H1 → `Subtitulo1`). Resultado: **0 saltos de jerarquía** en los cinco documentos.

### 9.5 Defecto corregido durante la aplicación

Al añadir el reemplazo de la línea institucional de la portada, la edición se aplicaba **inmediatamente** sobre el XML mientras las demás ediciones de la portada se aplican al final por posición: eso desfasaba las posiciones y dejaba el XML inválido en tres anexos (lo detectó la validación 18). Se corrigió acumulando también esa edición en la lista y aplicándola junto con las demás.

### 9.6 Validaciones

**45 comprobaciones, 0 errores y 0 advertencias.** Nuevas: 40 (portada con el nombre del anexo), 41 (índice de contenido y `updateFields`), 42 (índices de ilustraciones según contenido), 43 (rótulo y nota en cada tabla y figura de anexo), 44 (Calibri 11/12 en los anexos), 45 (sin saltos de jerarquía).

### 9.7 Cómo fijar los índices

```
powershell -NoProfile -ExecutionPolicy Bypass -File ES1PT\docx\actualizar_campos.ps1
```

Procesa el informe y los cinco anexos (una instancia de Word por documento, para que un documento grande no arrastre al resto) y guarda. Verificado: 6/6 documentos, 0 errores de campo.
