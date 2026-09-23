# Matriz de trazabilidad de ES2

Actualización: 2026-09-23. Los estados describen el avance documental, no cumplimiento académico aprobado. Aún no hay funcionalidades implementadas, según información del usuario.

Fuentes ES1: **Informe** = [informe fuente](../../ES1PT/docx/informe.md); **A–E** = [anexos de la línea base](../../ES1PT/docx/anexos/). La autoridad de la entrega cerrada sigue siendo el informe final y los anexos Word. **Plantilla/rúbrica** = documentos incorporados en `../plantilla/`.

| Criterio | Sección ES2 | Referencia ES1 | Investigación | Entregable | Estado y evidencia disponible |
| --- | --- | --- | --- | --- | --- |
| 2.1.1.1 | 2.1 | Informe: arquitectura, metodología y recursos; C | INV-002 | [Análisis](../secciones/02_01_analisis.md) | Borrador con fuentes; pesos propuestos; costos, puntuaciones y pruebas pendientes |
| 2.1.1.2 | 2.2 | Informe: arquitectura; A | INV-002/003 | [Inventario](../secciones/02_02_herramientas.md) | Borrador y fuentes públicas de integración; versiones, licencias, hardware, acceso y pruebas pendientes |
| 2.1.2.3 | 3.1 | Informe: procesos; A/B/D | INV-001/004 | [BPMN](../secciones/03_01_bpmn.md) | Tres diagramas y seis subprocesos en borrador; colaboración, temporizadores y revisión pendientes |
| 2.1.2.4 | 3.2 y 3.3 | A/D/E; Informe: arquitectura | INV-001/002/004 | [Casos de uso](../secciones/03_02_casos_uso.md) y [componentes](../secciones/03_03_componentes.md) | Tres vistas CU con 20 casos y dos vistas de componentes; cobertura, interfaces y revisión pendientes |
| 2.1.2.5 | 3.4 y Anexo A ES2 | B/D; Informe: persistencia | INV-004/006 | [Modelo](../secciones/03_04_datos.md) y [diccionario](../anexos/A_diccionario_datos.md) | Modelo parcial de 16 entidades y 123 atributos con cuatro vistas y matriz inicial de privacidad; DDL, política y pruebas pendientes |
| 2.1.2.6 | 3.5 | Informe: topología; C | INV-004 | [Comunicaciones](../secciones/03_05_comunicaciones.md) | Topología y tabla de canales en borrador; red, secretos y pruebas pendientes |
| 2.1.2.7 | 3.6 | Informe: topología y recursos; C | INV-002/004 | [Infraestructura](../secciones/03_06_infraestructura.md) | Diseño virtual propuesto; inventario físico, costos, dimensionamiento y despliegue pendientes |
| 2.1.2.8 | 3.7 | Informe: arquitectura TI | INV-002/004 | [Arquitectura](../secciones/03_07_arquitectura.md) | Vista integrada y recorrido de reserva en borrador; validación de fallos y RNF pendiente |
| 2.1.3.9 | 4.1 | Informe: ocho indicadores; C, RNF-021 | INV-005 | [KPI](../secciones/04_01_kpi.md) | Once fichas propuestas; alcance, responsables, presupuesto y mediciones pendientes |
| 2.1.3.10 | 4.2 | Informe: niveles de servicio; C | INV-005 | [SLA](../secciones/04_02_sla.md) | Cinco fichas de servicio propuestas; autorización, monitoreo y ensayos pendientes |
| 2.1.4.11 | 5.1 | B/C/D/E | INV-004/005/006 | [Pruebas](../secciones/05_01_pruebas.md) y [Anexo B](../anexos/B_casos_de_prueba.md) | Plan y dieciséis casos detallados, incluido PT-16 de privacidad; todos sin ejecutar, entornos y responsables pendientes |
| 2.1.4.12 | 5.2 | Informe: marco teórico; C | INV-006 | [Normas](../secciones/05_02_normas.md) | Matriz con cinco estándares y referencias jurídicas; Ley 21.719 adoptada desde el diseño, con revisión de aplicabilidad y evidencia pendientes |
| 2.1.5.13 | 6.1 | C, RNF-009/019/023 | INV-007 | [Disponibilidad](../secciones/06_01_disponibilidad.md) | Servicios, dependencias, sondeos y respuesta propuestos; sin herramienta ni mediciones |
| 2.1.5.14 | 6.2 | C, RNF-010 | INV-007 | [Continuidad](../secciones/06_02_continuidad.md) | Tres procedimientos de escenario y recursos propuestos; PT-11 y RPO/RTO sin ensayar |
| 2.1.5.15 | 6.3 | C; Informe: metodología | INV-007 | [Mantención](../secciones/06_03_mantencion.md) | Flujo de cambios e incidentes y campos de registro; roles, aplicación y simulacro pendientes |
| 2.1.6.16 | 7.1 | Informe: cronograma y equipo | INV-001; fecha informada por usuario | [Fases](../secciones/07_cronograma.md) | Propuesta fechada; capacidad y asignaciones por acordar |
| 2.1.6.17 | 7.1 | Informe: objetivos, alcance y cronograma | INV-001, brechas B-02/B-03 | [Justificación](../secciones/07_cronograma.md) | Motivo de replanificación documentado; revisión docente pendiente |

## Requisitos transversales

- Introducción y conclusiones: se cerrarán cuando el cuerpo represente el trabajo realizado.
- Bibliografía: se añadieron fuentes primarias para el primer borrador y referencias al material ES1. Verificación de APA 7 pendiente del documento final.
- Anexos: diccionario y matriz inicial de privacidad como Anexo A ES2; catálogo de dieciséis pruebas planificadas como Anexo B. Ninguno acredita implementación ni aprobación.
- Perfil Word: perfil preliminar con hash y estructura inspeccionada en INV-008; `aprobado: false` hasta la revisión visual. La plantilla original permanece intacta.
- Conservación: cotejar hashes con `linea_base_es1_sha256.json`; no generar sobre ES1.
- Responsables y revisores: por acordar con el equipo; ninguna sección tiene aprobación docente registrada.

Para cerrar una fila se requiere contenido completo, evidencia suficiente, revisión de coherencia y actualización de los pendientes. Tener un archivo o un título no equivale a satisfacer el criterio.

## Comprobación del borrador actual

- `ensamblar ES2PT` terminó correctamente: 25 archivos de sección configurados, diez capítulos en el ensamblado y dos anexos declarados.
- La comprobación de fuentes no encontró citas sin fuente, identificadores duplicados ni recursos ausentes; informa los pendientes del cuerpo y de ambos anexos.
- Pandoc procesó las citas con el CSL APA del repositorio y generó `build/vista_previa.html` con 41 referencias citadas, 15 imágenes y ninguna cita sin resolver. El Anexo B tiene vista previa independiente con sus cuatro referencias; esta comprobación textual no sustituye la revisión del Word institucional.
- Los 192 hashes de ES1 coinciden con la instantánea previa al trabajo, conservada en `linea_base_es1_sha256.json`. La generación de compatibilidad aislada y `comprobar_es1.py` terminaron sin diferencias.
- `validar ES2PT --final` devuelve código 1 por marcadores de borrador, código académico sin confirmar, tareas abiertas y ausencia de Word generado; el perfil institucional sigue desactivado. Es el resultado esperado para este estado.
- Las 26 pruebas `unittest` pasan. `diagnostico ES2PT` identifica el perfil institucional sin aprobar; el DOCX está incorporado. Los diagramas se renderizaron previamente con el JAR indicado mediante `--plantuml` e Inkscape para SVG.
