# Tarea de cierre documental de espaciGo

**Unidad de trabajo:** un capítulo y sus materiales asociados por vez.
**Estado:** capítulos editables revisados, Word y PDF regenerados con DocSkill.

| Corte | Estado | Entrega |
|---|---|---|
| I | Validado en DocSkill | Alcance, fuentes de vacancia y límites de interpretación. |
| II | Validado en DocSkill | Diagnóstico, matriz de causas y Figura 1 actualizada. |
| III | Validado en DocSkill | Marco teórico, citas, bibliografía y nueva Figura 2. |
| IV | Validado en DocSkill | Objetivos verificables, Canvas y condiciones coherentes con el ADR. |
| V | Validado en DocSkill | Ciclo iterativo, matriz, EDT, riesgos y Figura 4. Sección 5.3 intacta. |
| VI | Validado en DocSkill | Estructura funcional, objetivos, FODA y Figura 5. |
| VII y A–C | Validado en DocSkill | Criterios de calidad, requisitos y fichas del recorrido principal. M06 y M07 tienen diagramas UML propios y remiten al flujo del Capítulo IX. Se actualizan además los diagramas de actores, M03, M04, M08 y M10. |
| VIII y E | Validado en DocSkill | Vistas, módulos observados, Figura 7 y OpenAPI versionado. |
| IX y D | Validado en DocSkill | Flujos de oferta, contratación y privacidad. Modelo lógico, mapeo físico y figura nueva de ventanas de ensayo. |
| X y F | Validado en DocSkill | Evidencia por corte y 16 casos de prueba actualizados con trazabilidad. |
| XI | Validado en DocSkill | Topología objetivo, restauración, seguridad y procedimientos. |
| XII, G y H | Reservado | Fuentes y alertas conservadas. |
| XIII | Validado en DocSkill | Registro de cobertura, evidencia por objetivo y criterio de actualización. |
| XIV | Validado en DocSkill | Cierre por objetivo y próximos incrementos según dependencias. |
| Índice paginado | Verificado en PDF | LibreOffice actualiza el campo TOC generado por DocSkill durante la exportación. Las entradas I, IX y Anexo C coinciden con sus páginas reales. |
| Anexos secundarios | Seguimiento | Se mantienen fichas y figuras de módulos periféricos que requieren conciliación adicional por significado y evidencia. |

El flujo de generación es `python3 build_thesis.py`, que invoca DocSkill. Las salidas compiladas se tratan como artefactos generados.

La compilación produce un PDF de 509 páginas. Se comprueba en el PDF la paginación del índice y se revisan visualmente las figuras 9.1, C.7 y C.8.

La [revisión comparativa](auditoria_comparativa_cierre_tesis.md) registra las rectificaciones posteriores, el cierre F5/F6 y la comprobación de los 22 destinos principales del índice.

## Verificaciones de fondo

La [verificación de fondo](verificacion_de_fondo_tesis.md) registra el contraste de fichas con OpenAPI, las condiciones de proveedores y la reejecución aislada del ensayo de restauración. El ensayo local V1–V61 queda verificado. La integración de reputación requiere corregir el orden de bootstrap del banco de pruebas. Permanecen abiertas la habilitación de proveedores y retención por finalidad, y la prueba de carga y restauración conjunta en el entorno objetivo.

La [auditoría de tablas y anexos](auditoria_tablas_y_anexos.md) comprueba las 12 tablas del cuerpo y sus remisiones. Las pruebas de reputación pasan con el banco adaptado en una copia desechable. El ensayo de carga SQL local pasa dentro de su alcance. El ejecutor de restauración conserva una falla en la fase de permisos.

## Revisión por capítulos

El [plan de revisión por capítulo](plan_revision_por_capitulo.md) registra la instrucción de alcance amplio, las auditorías separadas y la publicación de cada corte verificado en `main`.

Las 16 auditorías de los chats terminaron. La [matriz de integración](matriz_integracion_auditorias.md) asigna propietario, dependencia y verificación de cierre a cada corrección. El siguiente corte es preliminares y manifiesto.
