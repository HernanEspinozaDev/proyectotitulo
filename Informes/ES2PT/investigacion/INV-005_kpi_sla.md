# INV-005 — Indicadores y niveles de servicio

- Estado: recuperación de la línea base y diseño de medición; sin resultados del producto.
- Fecha de consulta: 2026-09-23.
- Base inmutable: informe final ES1, apartado «Indicadores de gestión» y tabla «Niveles de servicio»; anexo C, RNF-001–003, 009–012, 019, 021, 030 y 042–043.
- Secciones ES2: 4.1, 4.2 y relación con 5.1 y 6.1–6.2.

## Pregunta y método

¿Qué indicadores de ES1 sirven para evaluar el avance documental y cuáles permiten medir la eficiencia del producto en ES2? Se cotejaron las dos tablas del informe final con el catálogo RNF. Las cifras son **metas declaradas en ES1**, no mediciones, acuerdos vigentes ni evidencia de ejecución. La implementación del producto aún no ha comenzado según la información comunicada por el usuario.

## Ocho indicadores heredados

| Indicador ES1 | Meta original | Decisión de medición ES2 |
| --- | --- | --- |
| Cobertura RF–CU | 100 % (236/236) | Recalcular sobre RF incluidos en un alcance ES2 aprobado; conservar el conteo 236 como referencia histórica. |
| Trazabilidad HU–RF–CU | 100 % (35/35) | Comprobar enlaces completos y consistentes sobre las HU del alcance aprobado. |
| Cobertura funcional de módulos | 100 % (11/11) | Verificar al menos una HU por módulo del alcance, sin inferir que el módulo está construido. |
| Categorías de calidad | 100 % (11/11) | Medir la integridad del catálogo RNF, no la calidad lograda por el software. |
| Avance incremental | 6/6 al término de la semana 16 | Mantener como antecedente; ES1 enumera cinco incrementos y una etapa de cierre en otra tabla. Definir denominador e hitos de ES2 con el equipo. |
| Cumplimiento del cronograma | 100 % de hitos en semana prevista | Rebasar contra fechas y responsables aprobados para ES2; no trasladar semanas históricas. |
| Cobertura de pruebas unitarias | ≥ 80 % de capa de negocio | Medir con instrumento, exclusiones y reporte del producto; el motor de informes no cuenta. |
| Ejecución presupuestaria | costo real / presupuesto = 100 % | La igualdad no distingue ahorro de sobrecosto. Proponer costo real / presupuesto aprobado ≤ 100 %, con partidas completas; requerirá aprobación del equipo y presupuesto valorizado. |

Los primeros cuatro son indicadores de **calidad de planificación y trazabilidad**, no pruebas de eficiencia de la solución. El quinto y el octavo necesitan una decisión nueva; no se atribuye esa corrección a ES1. Para evaluar el producto se proponen además el cumplimiento de búsqueda de RNF-001, la ausencia de doble reserva según RQF-111/112 y la idempotencia de RNF-012. Se medirán con casos y datos reproducibles. Una prueba con un simulador financiero solo evidencia la lógica local, no la ausencia de cargos reales duplicados.

## Metas de servicio y condiciones de cálculo

La tabla de ES1 incluye disponibilidad mensual 99,9 %, búsqueda ≤ 2 s con 200 usuarios concurrentes, procesamiento interno de pago ≤ 8 s sin contar la pasarela, PDF de contrato ≤ 10 s y < 2 MB, capacidad de 500 usuarios concurrentes y 100 escrituras/s, escalado ante +200 % de carga en ≤ 10 minutos, RPO ≤ 4 h y RTO ≤ 6 h. El anexo C detalla cada RNF. Las metas de seguridad, retención y tramitación también aparecen en la tabla histórica, pero su aplicabilidad técnica y normativa debe revisarse; no se declara cumplimiento legal por copiarlas.

Para comparar mediciones se debe fijar inicio y fin de cada operación, datos de carga, tamaño del entorno, reloj, zona horaria, ventana de observación y tratamiento de mantenimiento. Los resultados de pagos separarán latencia interna y externa, y los registros distinguirán falla conocida de respuesta incierta. La disponibilidad de los servicios externos no puede atribuirse a EspaciGo sin condiciones contractuales propias.

## Decisiones pendientes

1. Acordar alcance, responsables y fases de ES2; revisar las metas históricas que dependen de ellos.
2. Definir servicio, cliente, gestor, autorización, horario y mantenimiento de cada ficha SLA. La fecha de entrega académica no equivale a inicio de vigencia de un SLA.
3. Elegir herramientas de monitoreo, CI, prueba de carga y respaldo, con datos sintéticos y trazas verificables.
4. Revisar costos y factibilidad de metas de disponibilidad, escalado y recuperación contra la infraestructura propuesta.

[[PENDIENTE: registrar decisiones aprobadas, mediciones iniciales y resultados cuando exista producto; validar con el equipo las fichas 4.1–4.2 y el presupuesto.]]
