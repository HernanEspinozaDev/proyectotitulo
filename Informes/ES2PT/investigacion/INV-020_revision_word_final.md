# INV-020 — Cierre institucional en Word: generación, APA 7 y revisión visual

- Estado: documento generado y revisado visualmente; el perfil queda aprobado con esta evidencia y los pendientes que permanecen son de contenido, no de formato.
- Fecha: 2026-09-23; segunda generación y revisión el 2026-09-24 (ver § Revisión del 24-09-2026).
- Secciones ES2 relacionadas: todas; perfil institucional, anexos A/B/C, referencias y portada.
- Referencia de línea base: procedimiento de campos de ES1 (auditoría final §6.4 y §7.1) e inspección de plantilla de INV-008.

## Pregunta

¿Puede generarse y entregarse el informe con sus tres anexos usando el perfil institucional, sin degradar las citas APA 7 y con calidad visual verificable?

## Flujo validado

| Paso | Comando | Resultado |
| --- | --- | --- |
| Diagramas | `generar.py diagramas ES2PT --plantuml <jar>` | 21 figuras PNG regeneradas con PlantUML (`.puml`) e Inkscape (`.svg`) |
| Ensamblado | `generar.py ensamblar ES2PT` | `build/informe_ensamblado.md` sin errores de fuente ni de cita |
| Generación | `generar.py generar ES2PT --plantuml <jar>` | `Informe_Final.docx` (84 páginas, 33 tablas, 21 figuras, 87 enlaces) y los anexos A (31 páginas), B (9) y C (22); 82, 1, 4 y 49 fuentes escritas en la parte bibliográfica con `\APASeventhEdition.xsl` |
| Índices | `actualizar_campos.ps1 -Carpeta build -SoloIndices` | 3, 2, 1 y 2 índices actualizados; 145, 33, 18 y 24 entradas; 0 errores de campo |
| Render | `render_docx_windows.py` (Word + PyMuPDF) | PDF y PNG por página en `build/render_informe/` y `build/render_anexo_*/` |

## Decisión sobre APA 7

1. **Causa reproducida** en INV-008: al actualizar campos `CITATION`, el formateador de Word aplica la marca `RepeatedAuthor` e inserta el título dentro del paréntesis, además de deshacer los sufijos `2026a`/`2026b`. El corpus de ES2 cita varios informes del mismo equipo y del mismo año, condición que ES1 no tenía.
2. **Decisión**: entregar con las citas **generadas por citeproc** —APA 7— y **no actualizar** los campos `CITATION` ni `BIBLIOGRAPHY`; la única actualización de campos es la de índices con `-SoloIndices`, igual que en el procedimiento de ES1.
3. **Verificación en el render final**: citas en el texto como «(Espinoza et al., 2026c)» y «(Servicio Nacional del Consumidor, s. f.)»; lista de referencias con sangría francesa, orden alfabético, cursivas, «s. f.» en las fuentes sin fecha y sufijos `2026a`/`2026b` intactos.
4. **Corrección de un hallazgo propio**: las 63 fuentes del `.bib` sin año **no** producen un defecto APA, porque el estilo genera «s. f.» cuando no hay fecha. La observación anterior queda rectificada.

## Revisión visual

- **Portada del informe**: Asignatura, Sección, Académico guía, Integrantes del equipo y Fecha de entrega correctos. Se retiró de la portada el marcador pendiente del código de asignatura, que aparecía como texto visible; el contraste del código sigue documentado en INV-025.
- **Índices**: «Contenido» y «Índice de tablas y figuras» con números de página correctos, en páginas propias antes del capítulo 1.
- **Numeración**: diez títulos de capítulo numerados y secciones correlativas; 33 tablas y 21 figuras con rótulo y «Fuente:».
- **Figuras**: las 21 son legibles. Se corrigió `cu_identidad`, que medía 12,9 in de alto al ancho de página y se recortaba en el Word, aplicándole los mismos parámetros que las otras siete vistas; con ello el informe pasó de 86 a 84 páginas.
- **Tablas**: cabeceras repetidas cuando la tabla continúa en otra página; ninguna partida.
- **Citas y bibliografía**: revisadas en el texto y en la lista final, sin degradación.
- **Anexos**: portadas con su rótulo y sin marcadores; el Anexo B incluye su propio índice con las secciones nuevas; los Anexos C y C sin incidencias.
- **Encabezados y pies**: reproducen la configuración de la plantilla institucional —página par con logotipo y pie, impar solo con número—, de modo que la diferencia es intencional y no un defecto.

## Estado de la validación

- `validar ES2PT` termina en **0**: fuentes, imágenes, citas y documentos al día.
- `validar ES2PT --final` devuelve **1** con cuatro errores, todos de contenido: marcadores pendientes en el informe y en los anexos A y C, y tareas abiertas en `pendientes.md`. No hay errores de perfil, plantilla, campos ni estructura.

## Decisión sobre el perfil

`plantilla/perfil_es2.json` queda **aprobado** con esta evidencia. La aprobación cubre la plantilla, los estilos, la portada, los índices y el render; no declara resuelto el contenido pendiente. Se cumplieron las condiciones que INV-008 exigía: geometría y estilos inspeccionados, flujo APA 7 resuelto sin degradar citas, y el informe completo con sus tres anexos generado y revisado.

## Pendientes

[[PENDIENTE: completar el contenido pendiente —acceso a proveedores, mediciones y acuerdos del equipo— para retirar los marcadores de borrador y superar `validar ES2PT --final`; confirmar el código de asignatura con el instrumento oficial antes de la entrega; y volver a generar y revisar el Word si el contenido cambia después de esta generación, porque la validación detecta documentos desactualizados.]]

## Revisión del 24-09-2026 (salida vigente)

Tras la rotación de anexos y el cierre documental de [INV-033](INV-033_cierre_borrador.md), y con autorización expresa del usuario, se regeneró el Word y se revisó de nuevo. La salida del 23-09 queda como antecedente histórico; esta es la vigente.

| Paso | Comando | Resultado |
| --- | --- | --- |
| Generación | `generar.py generar ES2PT` | `Informe_Final.docx` (91 páginas, 30 tablas, 21 figuras, 92 enlaces) y anexos A (25 páginas), B (30) y C (8); 92, 52, 0 y 0 fuentes escritas en la parte bibliográfica |
| Índices | `generar.py actualizar-word ES2PT` | 3, 2, 2 y 1 índices con 150, 26, 32 y 17 entradas; 0 errores de campo |
| Render | `render_docx_windows.py` (Word + PyMuPDF) | PDF y PNG por página en `build/revision/` |
| Validación | `generar.py validar ES2PT` | **0 errores**, 3 avisos por marcadores deliberados |

**Defecto encontrado y corregido.** La tabla de valoración documental de 2.1 tenía ocho columnas y en el render los encabezados se partían a mitad de palabra («Adecuaci/ón», «Ponderad/o»). Se retiró la columna «Peso evaluado» —su contenido pasó a la nota—, se abreviaron los encabezados y se declararon anchos proporcionales en la fila de guiones del Markdown, porque Pandoc reparte el ancho según esa fila. Verificado en el render corregido: las diez filas caben en una página y ningún encabezado se corta.

**Comprobaciones automáticas** sobre los PDF exportados: ninguna imagen se sale de la página y no hay páginas vacías en los cuatro documentos.

**Páginas revisadas:** portada del informe; índice general y de tablas y figuras; Tabla 2 de valoración por capa; Tabla 5 del escenario segmentado; Tabla 7 de fichas de versiones y licencias; portadas de los tres anexos; y la Tabla A.10 del Anexo A. Los índices listan las tablas 1 a 30 con numeración correlativa.

**Consecuencia:** `perfil_es2.json` queda aprobado para esta salida. La aprobación cubre formato, portadas, índices, tablas, figuras y citas; **no** cierra los 14 marcadores de contenido del borrador.
