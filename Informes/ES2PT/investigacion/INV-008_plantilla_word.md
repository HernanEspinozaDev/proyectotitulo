# INV-008 — Adaptación de la plantilla Word ES2

- Estado: inspección estructural y perfil preliminar; aprobación visual pendiente.
- Fecha: 2026-09-23.
- Plantilla fuente inmutable: `../plantilla/TIHI84_U2_ES2_Plantilla_informe_Guía_ABPro.docx`.
- SHA-256: `98bbe1396210e5efc8049fba7e3006a7a5bd254ba356c39b6c19404bc687b7e1`.
- Perfil de ensayo: `../plantilla/perfil_es2.json`, con `aprobado: false`.

## Pregunta y método

¿Puede el adaptador institucional de ES1 generar la estructura de ES2 sin perder portada, índices, encabezados ni pies? Se inspeccionó el paquete DOCX de ES2 y se compararon secciones, estilos, partes y campos con la plantilla ES1. La plantilla original no se modificó.

## Evidencia estructural

| Elemento | Plantilla ES2 | Impacto |
| --- | --- | --- |
| Paquete y página | 43 partes OOXML, una sección, papel carta de 12240 × 15840 twips; márgenes de 1418 twips. La propiedad del archivo dice cinco páginas, dato de caché sin render independiente. | Mantener geometría y partes propias de la plantilla. |
| Portada | Asignatura, sección, académico, integrantes, fecha y nombre del proyecto aparecen duplicados en cuadros de texto. «DESARROLLO E IMPLEMENTACIÓN / DEL PROYECTO DE TÍTULO» está dividido en dos párrafos y también duplicado. | Los campos simples usan el mapa del perfil. Para anexos se conserva el título institucional completo y se pone el nombre del anexo en el campo de proyecto. |
| Índice y cuerpo | Entradas `TDC1`/`TDC2`, seguidas por instrucciones y ejemplos de los capítulos I–X. | El adaptador reemplaza la región desde el índice y descarta instrucciones; falta comprobar visualmente cortes, páginas e índices actualizados. |
| Estilos | Están `PARRAFO`, `Ttulo1`, `Subtitulo1`, `Subtitulo2`, `Prrafodelista`, `BIBLIOGRAFA1` y `TDC1`. Los XML de estilos y numeración difieren de ES1. | Mapa preliminar compatible por ID; se requieren muestra y revisión de jerarquía, tablas, figuras y bibliografía. |
| Encabezados y pies | Hay referencias `first`, `even` y `default` a seis partes; el encabezado de primera página contiene «INFORMÁTICA Y TELECOMUNICACIONES» y el pie por defecto «Desarrollo del Proyecto de Título» y número de página. | Preservar las seis partes y revisar cada variante. Nombre de carrera y datos académicos por confirmar. |

## Decisión y verificación pendiente

`informe.json` apunta al perfil preliminar, que permanece desactivado. Se añadió una opción del motor para conservar el título multipartes de la portada en los anexos ES2 sin alterar el comportamiento de ES1. Una prueba de la sustitución en memoria confirmó las dos copias del nombre del anexo y conservó las dos copias del título institucional. El diagnóstico debe seguir rechazando la generación mientras `aprobado` sea falso. No se declara el formato Word aprobado por similitud de estilos.

El primer intento con `render_docx.py` no inició por falta de `pdf2image`; `pdfinfo` y `pdftoppm` de Poppler tampoco están en `PATH`. Los primeros intentos de exportación por COM quedaron detenidos sin tiempo límite y no produjeron PDF. El 23-09-2026 se repitió la prueba con una **copia** de la plantilla y PowerShell en modo STA, con cierre controlado y límite de 45 segundos. Word abrió el DOCX, informó cinco páginas y exportó el PDF en unos nueve segundos. El problema inicial del renderizador estaba en la ruta PDF → PNG; el bloqueo anterior de COM no se reprodujo en esta prueba acotada. No hay evidencia de corrupción del DOCX.

El render local reproducible es `python Informes/herramientas/render_docx_windows.py <archivo.docx> --out Informes/ES2PT/build/qa_render_word/reutilizable`. Usa Word instalado para PDF y PyMuPDF ya disponible para PNG, sin instalar herramientas ni tocar el DOCX de origen. La prueba dejó `build/qa_render_word/reutilizable/documento.pdf`, cinco PNG en `build/qa_render_word/reutilizable/paginas/` y `exportacion.log`. Se inspeccionaron las cinco imágenes: portada, índice y numeración son legibles, sin recortes observados. **Las páginas pares 2 y 4 muestran logotipo en el encabezado y texto en el pie; las impares 3 y 5 carecen de ambos**, aunque conservan número de página. Se debe confirmar si esa diferencia del documento institucional es intencional y comprobarla otra vez en la muestra generada. La página 3 contiene solo la instrucción de la plantilla y las páginas 4–5 contienen ejemplos; esto corresponde al DOCX institucional sin rellenar. No hay tablas, figuras reales, citas del informe ni anexos en esta prueba.

**Pendiente para aprobar:** generar una muestra con el perfil ES2 adaptado y revisar todas sus páginas, incluidas tablas, figuras, citas e índices actualizados, además de cada anexo. Resolver datos de carrera/asignatura y solo entonces considerar `aprobado: true`. El hash del perfil impedirá usar una plantilla modificada sin volver a inspeccionarla.
