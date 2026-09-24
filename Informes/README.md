# Informes académicos de EspaciGo

Proceso común de redacción Markdown → Word institucional, basado en ES1. **ES1 está cerrado y se conserva sin modificaciones.** ES2 tiene plantilla, rúbrica, estructura por secciones y un borrador iniciado. Su [perfil Word preliminar](ES2PT/plantilla/perfil_es2.json) permanece desactivado hasta la revisión visual; ver [INV-008](ES2PT/investigacion/INV-008_plantilla_word.md). Consultar el [plan de ES2](ES2PT/plan_de_trabajo.md) y su [matriz de avance](ES2PT/investigacion/matriz_trazabilidad_es2.md).

## Prioridad vigente de ES2

Por instrucción del usuario, completar investigación, cuerpo y anexos antes de retomar Word, PDF/PNG, campos APA, índices o aprobación del perfil. No ejecutar esas comprobaciones tras cada tarea. Los comandos de Word descritos abajo quedan como referencia para el cierre, no como rutina de redacción. Mantener `aprobado: false` hasta la revisión final real.

El presupuesto vigente se investiga en [INV-010](ES2PT/investigacion/INV-010_infraestructura_y_formalizacion.md) y se desarrolla en el [Anexo A](ES2PT/anexos/A_evaluacion_economica.md). [INV-009](ES2PT/investigacion/INV-009_evaluacion_economica.md) conserva un primer ejemplo pedagógico superado que suponía ventas inmediatas. La skill personal `$evaluacion-proyectos-chile` aporta el procedimiento; datos y calculadora quedan en el repositorio. Para recalcular sin Word:

```powershell
python Informes/herramientas/simular_bootstrap.py Informes/ES2PT/investigacion/supuestos_bootstrap.json --salida Informes/ES2PT/build/simulacion_bootstrap.json
```

El escenario fija un primer año sin ventas, tres fundadores sin sueldo pagado y costos legales/municipales provisionados. Son supuestos académicos: sustituir demanda, tarifas, tributación y elegibilidad de oficina/patente por evidencia antes de aprobar presupuesto o inversión.

## Investigación en paralelo

El [tablero de ES2](ES2PT/coordinacion/README.md) coordina agentes que comparten archivos. `tareas.json` define investigaciones independientes y dependencias; un registro SQLite local reserva cada tarea y [bitacora.md](ES2PT/coordinacion/bitacora.md) deja visible quién avanzó y qué falta. Antes de redactar, cada agente lee el contexto y toma una tarea libre. La integración de secciones y bibliografía espera los registros independientes.

```powershell
python Informes/coordinar.py contexto
python Informes/coordinar.py tablero
python Informes/coordinar.py tomar --agente codex-investigacion-1
```

El comando `tomar` entrega un identificador de reserva para registrar avances y cerrar o liberar la tarea. Los detalles y el caso de worktrees distintos están en la guía; las casillas de `pendientes.md` solo se cierran con evidencia, no por el estado del tablero.

`nuevo ES3PT` incluye un tablero vacío en `coordinacion/`, para crear tareas desde su rúbrica sin copiar scripts ni la lista específica de ES2.

## Dónde trabajar

- `contexto/`: continuidad del proyecto, decisiones y vínculos a evidencias.
- `ES2PT/`: contexto de la entrega, pendientes, configuración, secciones, anexos y fuentes.
- `herramientas/`: motor común. No copiar scripts a cada entrega.
- `recursos/`: APA 7, ejemplos y perfiles Word revisados.
- `plantillas/nueva_entrega/`: estructura inicial que utiliza `nuevo`.
- `ES1PT/`: referencia histórica, incluidos scripts y planes antiguos.

Leer contexto compartido → contexto de la entrega → rúbrica y plantilla → secciones pertinentes. Markdown y JSON son fuentes editables. Los Word, imágenes renderizadas y ensamblados de `build/` son productos regenerables, no lugares para mantener cambios permanentes.

## Preparar el entorno

Desde la raíz del repositorio, con Python 3.10 o superior:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r Informes/requirements.txt
```

No se necesitan paquetes PyPI. Al mover un entorno virtual pueden quedar rutas absolutas inválidas: crea uno nuevo en la raíz; no dependas del `.venv` trasladado a `Informes/`.

Para Word: Pandoc 3.x en `PATH`. Para PlantUML: Java y un `plantuml.jar` local. Los SVG editables de BPMN se exportan con Inkscape en `PATH` o mediante `INKSCAPE_BIN`. Para actualizar campos: Windows, Microsoft Word y `APASeventhEdition.xsl` instalado. Estos programas no se instalan automáticamente.

Para revisar visualmente un DOCX en Windows con Office 365, si PyMuPDF ya está disponible en el Python local, usar `python Informes/herramientas/render_docx_windows.py ruta/al/documento.docx --out Informes/ES2PT/build/qa_word`. El script copia el DOCX, exporta con Word mediante COM (45 s de límite por defecto) y genera `documento.pdf`, `paginas/page-001.png`, etc. en la carpeta de salida. No aprueba por sí mismo el perfil Word: hay que inspeccionar todas las páginas y anexos. Ver [diagnóstico ES2](ES2PT/investigacion/INV-008_plantilla_word.md).

Para ensayar el perfil ES2 todavía desactivado: `python Informes/herramientas/previsualizar_perfil.py ES2PT`. Produce una muestra parcial en `ES2PT/build/qa_perfil/`, fuera de la generación oficial. Sus índices pueden actualizarse sin tocar citas mediante `powershell -NoProfile -STA -File Informes/herramientas/actualizar_campos.ps1 -Carpeta Informes/ES2PT/build/qa_perfil -SoloIndices`. En este entorno, la actualización completa de campos APA 7 falla en Word y no debe utilizarse para la entrega hasta resolver el problema registrado en INV-008.

```powershell
$env:PLANTUML_JAR = 'C:\ruta\plantuml.jar'
python Informes/generar.py diagnostico ES2PT
```

El diagnóstico de ES2 termina con código 1 mientras su perfil institucional tenga `aprobado: false`, aunque el DOCX de plantilla ya esté incorporado. `--plantuml C:/ruta/plantuml.jar` permite indicar el JAR por ejecución.

## Recorrido de una entrega

1. **Iniciar:** `python Informes/generar.py nuevo ES3PT`. Crea carpetas y archivos sin scripts ni capítulos supuestos. Falla si la entrega existe. `--inicializar-existente` agrega solo archivos ausentes.
2. **Incorporar instrucciones:** guardar rúbrica y plantilla original en `plantilla/`. Registrar alcance, fecha y criterios reales. Seguir la [guía de perfiles](recursos/perfiles/README.md).
3. **Definir secciones:** crear `secciones/01_introduccion.md`, etc., según la rúbrica. Reemplazar `00_borrador.md` en la lista `secciones` del JSON; esa lista, no el orden alfabético, manda.
4. **Redactar con evidencia:** revisar el contexto, conservar identificadores y marcar `[[PENDIENTE: qué falta]]`. No inventar resultados, fechas, aprobaciones ni fuentes.
5. **Agregar anexos y recursos:** declarar cada anexo en el JSON. Mantener imágenes propias en `imagenes/` y fuentes PlantUML o SVG en `diagramas/`. Consultar [ejemplos de autoría](recursos/ejemplos.md).
6. **Gestionar bibliografía:** mantener `referencias.bib` propio. ES2 contiene una copia del catálogo de ES1; revisar pertinencia y vigencia. `nuevo` crea un catálogo vacío. Copiar las referencias necesarias de la entrega anterior conservando claves.
7. **Solo con el contenido terminado, generar y revisar:** actualizar solo índices mientras siga pendiente el problema APA 7 de Word; examinar portada, referencias en caché, tablas, imágenes y anexos. Cerrar pendientes con evidencia antes de validar como final.

```powershell
python Informes/generar.py ensamblar ES2PT
python Informes/generar.py diagramas ES2PT --plantuml C:/ruta/plantuml.jar
python Informes/generar.py generar ES2PT
python Informes/generar.py validar ES2PT
# Mantiene intactos CITATION/BIBLIOGRAPHY hasta resolver INV-008
powershell -NoProfile -STA -File Informes/herramientas/actualizar_campos.ps1 -Carpeta Informes/ES2PT/build -SoloIndices
python Informes/generar.py validar ES2PT --final
```

`ensamblar` funciona sin Word ni plantilla; escribe `build/informe_ensamblado.md`. `generar` produce `Informe_Final.docx`, los anexos declarados, intermedios, auditorías bibliográficas y un manifiesto. Si falla, devuelve código distinto de cero; una generación incompleta no se acepta. Se rechazan documentos desactualizados tras cambios en fuentes o motor.

`diagramas` permite obtener PNG de revisión en `build/imagenes/` antes de adaptar el perfil Word. Por ejemplo, `diagramas/bpmn02_reserva.svg` se cita como `imagenes/figura-bpmn02_reserva.png`; el motor genera la imagen y conserva el SVG editable. Los nombres base de SVG y PlantUML deben ser distintos.

`validar --final` exige metadatos completos, ausencia de marcadores pendientes, fuentes citadas completas y ninguna tarea abierta en `pendientes.md`. No sustituye la revisión humana de la rúbrica ni la comprobación visual. `generar --final` aplica las mismas exigencias.

## Configuración por entrega

`informe.json` usa `version: 1`, `id`, `metadatos`, `secciones`, `anexos`, `bibliografia`, `plantilla` y `perfil`. Las rutas de fuentes e imágenes son relativas a la raíz de la entrega, incluso desde `secciones/` o `anexos/`. No usar rutas fuera de la entrega ni imágenes remotas. El CSL APA 7 permanece en `recursos/`.

Los títulos usan `#`, con niveles siguientes `##` a `####`; no escribir manualmente los números. Por defecto se agregan Referencias y el índice de anexos. Si la rúbrica fija otro lugar, escribirlos explícitamente y desactivar `agregar_referencias` o `agregar_indice_anexos`. La lista bibliográfica utiliza `::: {#refs}` seguida de `:::`.

Los anexos declaran letra, título, archivo, salida y transformación. `general` usa Markdown con rótulos explícitos; `casos_uso` activa la interpretación histórica de módulos M## y bloques PlantUML; `historias_usuario` convierte HU## a tarjetas. No elegir las dos últimas para otro contenido.

## Citas APA 7 y Word

Usar `[@clave]` o `[@clave1; @clave2]`. El motor conserva el texto APA 7 de Pandoc y escribe campos nativos y únicamente las fuentes citadas en cada documento. Citas narrativas y localizadores como `[@clave, p. 3]` se rechazan para no perder información; requieren ampliar el motor.

La actualización automática de campos al abrir Word está desactivada. El DOCX declara `SelectedStyle="\APASeventhEdition.xsl"` en sus fuentes, como ES1; el XSL se instaló manualmente en el perfil del usuario. `actualizar-word` comprueba su presencia, pero en este equipo la asignación COM del estilo falla y una prueba de actualización de citas sin esa asignación alteró el formato. Hasta resolverlo, usar `-SoloIndices` para revisar índices y conservar las citas APA 7 en caché; no presentar esa revisión parcial como validación final. El antecedente exacto está en [ES1](ES1PT/auditoria_final_ES1.md) (§6.4 y §7.1) y el fallo actual en [INV-008](ES2PT/investigacion/INV-008_plantilla_word.md).

## Comprobación del motor

```powershell
python -m unittest discover -s Informes/tests -v
python Informes/generar.py generar recursos/compatibilidad_es1.json --plantuml C:/ruta/plantuml.jar
python Informes/herramientas/comprobar_es1.py
```

La compatibilidad lee ES1 y escribe exclusivamente en `Informes/build/compatibilidad_es1/`. La comparación usa contenido, estructura, citas y anexos, no igualdad binaria de ZIPs. Los hashes de conservación y la evidencia de esta normalización quedan en `Informes/build/normalizacion/`; son locales e ignorados por Git.
