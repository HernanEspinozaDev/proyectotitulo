# Guía de Operación para Agentes de IA (AGENTS.md)
**Proyecto de Título: espaciGo — INACAP**

Este archivo contiene el contexto operativo, reglas inmutables, directrices de estilo y procedimientos técnicos que cualquier agente de Inteligencia Artificial (o colaborador automatizado) DEBE cumplir al trabajar en este repositorio.

---

## 1. Misión del Proyecto y Estructura del Repositorio

El repositorio contiene la **Memoria de Título final** para optar al Título Profesional de Ingeniero en Tecnologías de Información y Ciberseguridad en INACAP, correspondiente a la plataforma **espaciGo**.

### Estructura de Directorios Clave
- **`tesis_final/`**: Directorio principal de trabajo.
  - `document.json`: Manifiesto de compilación DocSkill. Define los metadatos y la secuencia exacta de capítulos (`sections/`) y anexos (`appendices/`).
  - `sections/`: 15 capítulos en Markdown (`00-preliminares.md` a `14-conclusiones-y-trabajos-futuros.md`).
  - `appendices/`: 8 anexos técnicos (`a-requerimientos-ieee830.md` a `h-evaluacion-economica-detallada.md`).
  - `assets/diagramas_src/`: Código fuente editable de todos los diagramas (`.puml` y `.mmd`).
  - `assets/imagenes/`: Renders PNG de alta resolución insertados en el documento.
  - `scripts/`: Herramientas de soporte, renderizado y postprocesamiento.
  - `context/`: **Base de conocimiento centralizada**:
    - `00_material_docente/`: Guías de actividades oficiales de INACAP (ACT0 a ACT9).
    - `01_auditorias_y_rubricas/`: Rúbricas de evaluación, correcciones docentes previas y análisis forense comparativo.
    - `02_arquitectura_y_diseno/`: Documento rector de diseño técnico (`DESIGN_espaciGo.md`), actores, módulos y bibliografía.
    - `03_insumos_anita_erick_finanzas/`: Scripts Python de simulación Monte Carlo / Bootstrap (`evaluacion_economica.py`, `simular_bootstrap.py`), notas de investigación económica (`INV-009`, `INV-011`, etc.) y supuestos JSON para el Capítulo XII y Anexo H.
    - `04_insumos_anita_erick_gantt/`: Matriz de trazabilidad, backlog de sprints, supuestos de planificación y documentación para el Capítulo V y Anexo G.
  - `build/`: Salidas compiladas (`Tesis_Final_espaciGo.docx` y `Tesis_Final_espaciGo.pdf`).
- **`build_thesis.py`**: Script de orquestación en la raíz para compilar la tesis de principio a fin.
- **`docskill/`**: Motor documental que utiliza Pandoc y perfiles de estilo OOXML.

---

## 2. Reglas Inmutables y Restricciones Absolutas

1. **Secciones Reservadas de Integrantes (Anita Marchant y Erick Silva)**:
   - **NUNCA** redactar, alterar o inventar datos financieros (flujos de caja, VAN, TIR, Payback) ni cronogramas Gantt detallados.
   - Esas secciones pertenecen a **Anita Marchant Silva** y **Erick Silva Espinoza**.
   - En el **Capítulo XII**, **Anexo H**, **Capítulo V (Sección 5.3)** y **Anexo G**, se DEBE respetar la presencia de las alertas visuales verdes:
     ```markdown
     > 🟢 **[SECCIÓN RESERVADA PARA INTEGRACIÓN — ANITA MARCHANT Y ERICK SILVA]**
     ```
   - Si se requiere consultar los insumos preparados para ellos, remitirse a `tesis_final/context/03_insumos_anita_erick_finanzas/` y `tesis_final/context/04_insumos_anita_erick_gantt/`.

2. **Regla de Formato APA 7 para Figuras e Imágenes**:
   - **Cero bloques de código crudos**: En los capítulos o anexos **JAMÁS** debe haber bloques ```mermaid o ```plantuml en el texto principal. Todo diagrama debe estar renderizado en PNG e insertado como imagen.
   - **Ubicación de fuentes**: Las fuentes editables residen en `tesis_final/assets/diagramas_src/` (`.puml` o `.mmd`) y los renders en `tesis_final/assets/imagenes/`.
   - **Estructura en Markdown**:
     ```markdown
     **Figura X.Y**
     *Título descriptivo de la figura en cursiva*

     ![](../assets/imagenes/figXY_nombre_diagrama.png)

     *Nota.* Descripción breve del contenido. Adaptado de... / Fuente: Elaboración propia a partir de la especificación técnica de espaciGo.
     ```
   - **Alt text vacío**: El corchete de la imagen debe ser estrictamente `![](...)` sin texto interno para evitar que Pandoc duplique el pie de foto al exportar a Word.

3. **Regla de Formato APA 7 para Tablas**:
   - Toda tabla debe poseer bordes visibles (cuadrícula completa de 1/2 pt en negro), encabezados oscurecidos/sombreados y su respectivo rótulo superior y nota de elaboración inferior:
     ```markdown
     **Tabla X.Y**
     *Título de la tabla en cursiva*

     | Encabezado 1 | Encabezado 2 |
     |---|---|
     | Dato 1 | Dato 2 |

     *Nota.* Fuente: Elaboración propia / Adaptado de...
     ```

4. **Tono y Redacción Académica**:
   - Todo el contenido debe estar redactado en **Español Técnico Formal**, en **tercera persona singular en presente** («la plataforma implementa», «el sistema procesa», «la arquitectura comprende»).
   - Prohibido el uso de primera persona («hicimos», «desarrollé», «nuestro equipo»).

---

## 3. Procedimiento de Compilación y Verificación

Para compilar el documento tras realizar cambios en el Markdown o en los diagramas:

```bash
# Compilación completa (DocSkill + Layout + PDF):
python3 build_thesis.py

# Si solo se modificó texto y se requiere probar rápido el DOCX:
python3 build_thesis.py --no-pdf

# Si se modificó un archivo .puml o .mmd en diagramas_src/:
python3 build_thesis.py --diagrams
```

### Flujo Interno de Compilación:
1. `DocSkillProject.open('tesis_final').build()` genera el archivo Word base `Tesis_Final_espaciGo.docx`.
2. `tesis_final/scripts/postprocess_tesis_layout.py` modifica el OOXML del DOCX para:
   - Inyectar saltos de página limpios (`<w:pageBreakBefore/>`) antes de cada capítulo y anexo mayor.
   - Configurar la cuadrícula de bordes completos en las más de 200 tablas.
   - Aplicar el estilo nativo `ImageCaption` y `<w:keepNext/>` en los títulos de figuras.
3. `libreoffice --headless --convert-to pdf` produce `Tesis_Final_espaciGo.pdf` (más de 560 páginas).

---

## 4. Trazabilidad y Consulta de Contexto

Antes de redactar o modificar capítulos técnicos, consulta las carpetas correspondientes en `tesis_final/context/`:
- **¿Dudas de requerimientos o casos de uso?** Revisa `context/02_arquitectura_y_diseno/actores_y_modulos.md` y `DESIGN_espaciGo.md`.
- **¿Dudas sobre criterios de evaluación de la profesora Teresa Tapia?** Revisa `context/01_auditorias_y_rubricas/correcciones_profesora.md` y las rúbricas de evaluación.
- **¿Dudas sobre cómo modelar o estructurar según INACAP?** Revisa `context/00_material_docente/` donde están las guías oficiales de actividades (ACT0 a ACT9).
