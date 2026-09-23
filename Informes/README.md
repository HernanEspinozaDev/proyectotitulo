# Informes académicos de EspaciGo

Proceso común de redacción Markdown → Word institucional, basado en ES1. **ES1 está cerrado y se conserva sin modificaciones.** ES2 tiene plantilla, rúbrica, estructura por secciones y un borrador iniciado. Su perfil de Word sigue pendiente de adaptación. Consultar el [plan de ES2](ES2PT/plan_de_trabajo.md) y su [matriz de avance](ES2PT/investigacion/matriz_trazabilidad_es2.md).

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

Para Word: Pandoc 3.x en `PATH`. Para diagramas: Java y un `plantuml.jar` local. Para actualizar campos: Windows, Microsoft Word y `APASeventhEdition.xsl` instalado. Estos programas no se instalan automáticamente.

```powershell
$env:PLANTUML_JAR = 'C:\ruta\plantuml.jar'
python Informes/generar.py diagnostico ES2PT
```

El diagnóstico de ES2 termina con código 1 mientras falte adaptar su perfil institucional, aunque el DOCX de plantilla ya esté incorporado. `--plantuml C:/ruta/plantuml.jar` permite indicar el JAR por ejecución.

## Recorrido de una entrega

1. **Iniciar:** `python Informes/generar.py nuevo ES3PT`. Crea carpetas y archivos sin scripts ni capítulos supuestos. Falla si la entrega existe. `--inicializar-existente` agrega solo archivos ausentes.
2. **Incorporar instrucciones:** guardar rúbrica y plantilla original en `plantilla/`. Registrar alcance, fecha y criterios reales. Seguir la [guía de perfiles](recursos/perfiles/README.md).
3. **Definir secciones:** crear `secciones/01_introduccion.md`, etc., según la rúbrica. Reemplazar `00_borrador.md` en la lista `secciones` del JSON; esa lista, no el orden alfabético, manda.
4. **Redactar con evidencia:** revisar el contexto, conservar identificadores y marcar `[[PENDIENTE: qué falta]]`. No inventar resultados, fechas, aprobaciones ni fuentes.
5. **Agregar anexos y recursos:** declarar cada anexo en el JSON. Mantener imágenes en `imagenes/` y PlantUML en `diagramas/`. Consultar [ejemplos de autoría](recursos/ejemplos.md).
6. **Gestionar bibliografía:** mantener `referencias.bib` propio. ES2 contiene una copia del catálogo de ES1; revisar pertinencia y vigencia. `nuevo` crea un catálogo vacío. Copiar las referencias necesarias de la entrega anterior conservando claves.
7. **Generar y revisar:** actualizar campos y examinar visualmente portada, índices, referencias, tablas, imágenes y anexos. Cerrar pendientes con evidencia antes de validar como final.

```powershell
python Informes/generar.py ensamblar ES2PT
python Informes/generar.py generar ES2PT
python Informes/generar.py validar ES2PT
python Informes/generar.py actualizar-word ES2PT
python Informes/generar.py validar ES2PT --final
```

`ensamblar` funciona sin Word ni plantilla; escribe `build/informe_ensamblado.md`. `generar` produce `Informe_Final.docx`, los anexos declarados, intermedios, auditorías bibliográficas y un manifiesto. Si falla, devuelve código distinto de cero; una generación incompleta no se acepta. Se rechazan documentos desactualizados tras cambios en fuentes o motor.

`validar --final` exige metadatos completos, ausencia de marcadores pendientes, fuentes citadas completas y ninguna tarea abierta en `pendientes.md`. No sustituye la revisión humana de la rúbrica ni la comprobación visual. `generar --final` aplica las mismas exigencias.

## Configuración por entrega

`informe.json` usa `version: 1`, `id`, `metadatos`, `secciones`, `anexos`, `bibliografia`, `plantilla` y `perfil`. Las rutas de fuentes e imágenes son relativas a la raíz de la entrega, incluso desde `secciones/` o `anexos/`. No usar rutas fuera de la entrega ni imágenes remotas. El CSL APA 7 permanece en `recursos/`.

Los títulos usan `#`, con niveles siguientes `##` a `####`; no escribir manualmente los números. Por defecto se agregan Referencias y el índice de anexos. Si la rúbrica fija otro lugar, escribirlos explícitamente y desactivar `agregar_referencias` o `agregar_indice_anexos`. La lista bibliográfica utiliza `::: {#refs}` seguida de `:::`.

Los anexos declaran letra, título, archivo, salida y transformación. `general` usa Markdown con rótulos explícitos; `casos_uso` activa la interpretación histórica de módulos M## y bloques PlantUML; `historias_usuario` convierte HU## a tarjetas. No elegir las dos últimas para otro contenido.

## Citas APA 7 y Word

Usar `[@clave]` o `[@clave1; @clave2]`. El motor conserva el texto APA 7 de Pandoc y escribe campos nativos y únicamente las fuentes citadas en cada documento. Citas narrativas y localizadores como `[@clave, p. 3]` se rechazan para no perder información; requieren ampliar el motor.

La actualización automática de campos al abrir Word está desactivada. `actualizar-word` verifica primero el XSL y selecciona APA 7. Para otra ubicación, usar `--estilo-apa C:/ruta/APASeventhEdition.xsl`. Word puede reformatear citas agrupadas: comprobarlas visualmente. Véase [BibliographyStyle de Microsoft](https://learn.microsoft.com/en-us/office/vba/api/word.bibliography.bibliographystyle).

## Comprobación del motor

```powershell
python -m unittest discover -s Informes/tests -v
python Informes/generar.py generar recursos/compatibilidad_es1.json --plantuml C:/ruta/plantuml.jar
python Informes/herramientas/comprobar_es1.py
```

La compatibilidad lee ES1 y escribe exclusivamente en `Informes/build/compatibilidad_es1/`. La comparación usa contenido, estructura, citas y anexos, no igualdad binaria de ZIPs. Los hashes de conservación y la evidencia de esta normalización quedan en `Informes/build/normalizacion/`; son locales e ignorados por Git.
