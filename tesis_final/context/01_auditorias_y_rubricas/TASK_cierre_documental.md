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

## Aplicación de las auditorías por capítulo

Los chats propietarios reciben el commit de su corte para revisar el diff en modo de solo lectura. El cierre transversal incorpora los hallazgos confirmados de esos recibos.

| Corte | Commit de edición | Cambio principal |
|---|---|---|
| Preliminares | `2631f16` | Título y resumen de alcance amplio. Se retiran textos provisionales de portada, dedicatoria y agradecimientos. |
| I | `ef70cb1` | Oferentes, usos y ejemplos objetivo. Mercado de oficinas acotado a su segmento. |
| II | `d4c731f` | Diagnóstico transversal y unidad exclusiva. Se retira la fuente Mermaid divergente de la Figura 1. |
| III | `3faa830` | Marco teórico alineado al dominio, referencias a arquitectura, datos y evidencia. |
| IV | `ee6ce13` | Objetivo, segmentos, Canvas y reglas de servicio objetivo. |
| V | `bd15857` | Escala, método de ponderación y justificación contextual. Sección 5.3 intacta. |
| VI | `ac8171b` | Misión amplia, funciones y distinción entre persona, representación y permisos. |
| VII y A–C | `a56c29f` | Cinco HU y veinte CU recuperan estructura uniforme. Se corrige la cobertura documental y se archivan notas históricas. Se actualizan los diagramas que restringían el sistema a espacios comerciales. |
| VIII y E | `5958a71` | Contrato por commit y ocho categorías del corte, diferenciadas del alcance objetivo. |
| IX y D | `49c8017` | Referencias explícitas a figuras. Unidad exclusiva y diferencia entre capacidad, categoría e inventario compartido. |
| X y F | `80d4fd2` | Evidencia por perfil, límites por categoría y trazabilidad parcial a PT-07. |
| XI | `90b969d` | Configuración fechada, autorización como criterio y ensayos operativos pendientes. |
| XII, G y H | Reservado | Contenido intacto. Se revisan las remisiones externas. |
| XIII | `989a889` | Estados de objetivos y vínculos a evidencia. |
| XIV | `c0c5551` | Conclusiones por alcance, resultado y dependencia externa. |
| Referencias y cierre | Commit de exportación | Numeración correlativa de 14 figuras y 12 tablas. Se concilian las trazas de las fichas con sus tablas resumen y se verifican referencias e índice. |

Los archivos compilados se regeneran juntos desde el conjunto final de fuentes. La revisión conserva 236 RQF, 43 RNF, 35 HU, 52 CU y 16 PT. El alcance objetivo incluye casas de veraneo y hostales. Su incorporación al catálogo, el inventario compartido, las integraciones externas y las pruebas en el entorno objetivo conservan sus condiciones propias de verificación.

La exportación del cierre contiene 498 páginas. Se verifican los 22 destinos principales del índice, los 14 rótulos de figuras y los 12 de tablas del cuerpo. La revisión visual incluye portada, índice y una muestra de figuras y fichas. El hipervínculo de la Ley 21.461 conserva su destino completo.

### Catálogo vigente y pruebas condicionadas al código

El proyecto confirma nueve categorías. La Tabla E.2 incorpora Inmuebles con casa, departamento, habitación y cabaña. La Tabla E.1 conserva su versión de OpenAPI y el texto distingue ese corte del catálogo vigente. El Capítulo XI identifica Mercado Pago y SimpleFirma como proveedores previstos, ambos pendientes de habilitación. La Tabla F.4 registra las verificaciones de proveedores, garantía, catálogo, carga y recuperación que se integran cuando el código correspondiente está listo y existe evidencia de ejecución.
