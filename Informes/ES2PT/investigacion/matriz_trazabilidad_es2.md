# Matriz de trazabilidad de ES2

Actualización: 2026-09-23. Los estados describen el avance documental, no cumplimiento académico aprobado. Aún no hay funcionalidades implementadas, según información del usuario.

Fuentes ES1: **Informe** = [informe fuente](../../ES1PT/docx/informe.md); **A–E** = [anexos de la línea base](../../ES1PT/docx/anexos/). La autoridad de la entrega cerrada sigue siendo el informe final y los anexos Word. **Plantilla/rúbrica** = documentos incorporados en `../plantilla/`.

| Criterio | Sección ES2 | Referencia ES1 | Investigación | Entregable | Estado y evidencia disponible |
| --- | --- | --- | --- | --- | --- |
| 2.1.1.1 | 2.1 | Informe: arquitectura, metodología y recursos; C | INV-002 | [Análisis](../secciones/02_01_analisis.md) | Borrador con fuentes; pesos propuestos; costos, puntuaciones y pruebas pendientes |
| 2.1.1.2 | 2.2 | Informe: arquitectura; A | INV-002/003 | [Inventario](../secciones/02_02_herramientas.md) | Borrador; versiones, licencias, hardware y acceso pendientes |
| 2.1.2.3 | 3.1 | Informe: procesos; A/B/D | INV-001; modelado por abrir | [BPMN](../secciones/03_01_bpmn.md) | Procesos candidatos descritos; diagramas y subprocesos pendientes |
| 2.1.2.4 | 3.2 y 3.3 | A/D/E; Informe: arquitectura | INV-001/002; modelado por abrir | [Casos de uso](../secciones/03_02_casos_uso.md) y [componentes](../secciones/03_03_componentes.md) | Base localizada; UML de ES2 pendiente |
| 2.1.2.5 | 3.4 y Anexo A ES2 | B/D; Informe: persistencia | Modelado por abrir | [Modelo](../secciones/03_04_datos.md) y [diccionario](../anexos/A_diccionario_datos.md) | Estructura; entidades, relaciones y atributos pendientes |
| 2.1.2.6 | 3.5 | Informe: topología; C | Diseño de comunicaciones por abrir | [Comunicaciones](../secciones/03_05_comunicaciones.md) | Estructura; diagrama y protocolos pendientes |
| 2.1.2.7 | 3.6 | Informe: topología y recursos; C | INV-002; dimensionamiento pendiente | [Infraestructura](../secciones/03_06_infraestructura.md) | Estructura; diagrama y recursos pendientes |
| 2.1.2.8 | 3.7 | Informe: arquitectura TI | INV-002; diseño por completar | [Arquitectura](../secciones/03_07_arquitectura.md) | Estructura; vista integrada pendiente |
| 2.1.3.9 | 4.1 | Informe: indicadores; C, RNF-021 | INV-001; fichas SMART por completar | [KPI](../secciones/04_01_kpi.md) | Dos fichas iniciales; mediciones, responsables e indicadores de producto pendientes |
| 2.1.3.10 | 4.2 | Informe: niveles de servicio; C | INV-001; fichas de servicio por completar | [SLA](../secciones/04_02_sla.md) | Metas recuperadas; acuerdo y cumplimiento no acreditados |
| 2.1.4.11 | 5.1 | C/D/E | Plan de pruebas por abrir | [Pruebas](../secciones/05_01_pruebas.md) | Riesgos prioritarios identificados; catálogo y ejecución pendientes |
| 2.1.4.12 | 5.2 | Informe: marco teórico; C | Investigación normativa por abrir | [Normas](../secciones/05_02_normas.md) | Estructura; verificación de aplicabilidad y versiones pendiente |
| 2.1.5.13 | 6.1 | C, RNF-009/019/023 | Operación por abrir | [Disponibilidad](../secciones/06_01_disponibilidad.md) | Estructura; procedimientos pendientes |
| 2.1.5.14 | 6.2 | C, RNF-010 | Operación por abrir | [Continuidad](../secciones/06_02_continuidad.md) | Estructura; procedimientos y ensayo pendientes |
| 2.1.5.15 | 6.3 | C; Informe: metodología | Operación por abrir | [Mantención](../secciones/06_03_mantencion.md) | Estructura; configuración, cambios e incidentes pendientes |
| 2.1.6.16 | 7.1 | Informe: cronograma y equipo | INV-001; fecha informada por usuario | [Fases](../secciones/07_cronograma.md) | Propuesta fechada; capacidad y asignaciones por acordar |
| 2.1.6.17 | 7.1 | Informe: objetivos, alcance y cronograma | INV-001, brechas B-02/B-03 | [Justificación](../secciones/07_cronograma.md) | Motivo de replanificación documentado; revisión docente pendiente |

## Requisitos transversales

- Introducción y conclusiones: se cerrarán cuando el cuerpo represente el trabajo realizado.
- Bibliografía: se añadieron fuentes primarias para el primer borrador y referencias al material ES1. Verificación de APA 7 pendiente del documento final.
- Anexos: diccionario de datos configurado como Anexo A ES2, todavía sin contenido de modelo aprobado.
- Perfil Word: pendiente de adaptación; la plantilla institucional ya está incorporada.
- Conservación: cotejar hashes con `linea_base_es1_sha256.json`; no generar sobre ES1.
- Responsables y revisores: por acordar con el equipo; ninguna sección tiene aprobación docente registrada.

Para cerrar una fila se requiere contenido completo, evidencia suficiente, revisión de coherencia y actualización de los pendientes. Tener un archivo o un título no equivale a satisfacer el criterio.

## Comprobación del primer borrador

- `ensamblar ES2PT` terminó correctamente: 25 archivos de sección configurados, diez capítulos en el ensamblado y un anexo declarado.
- La comprobación de fuentes no encontró citas sin fuente, identificadores duplicados ni recursos ausentes; informa los pendientes del cuerpo y del diccionario.
- Pandoc procesó las citas con el CSL APA del repositorio y generó `build/vista_previa.html` con 16 referencias citadas. Esta comprobación textual no sustituye la revisión del Word institucional.
- Los 192 hashes de ES1 coinciden con la instantánea previa al trabajo, conservada en `linea_base_es1_sha256.json`.
- La comprobación final de fuentes rechaza los pendientes de contenido, el código académico sin confirmar y las tareas abiertas, como corresponde al borrador.
- `diagnostico ES2PT` informa el requisito pendiente de plantilla/perfil: el DOCX está incorporado, pero el perfil sigue sin adaptar. También falta configurar `PLANTUML_JAR` para futuros diagramas PlantUML.
