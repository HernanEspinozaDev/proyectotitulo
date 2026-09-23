# INV-001 — Línea base y brechas para iniciar ES2

- Estado: inventario documental inicial completado; brechas abiertas.
- Fecha: 2026-09-23.
- Alcance: lectura de la entrega ES1 y preparación del informe ES2.
- Información del equipo: el usuario confirma entrega de ES2 el 3 de noviembre y que todavía no hay funcionalidades implementadas; desarrollará el producto en paralelo. Se registra el año 2026 por el calendario de esta entrega. La confirmación proviene del usuario, no de una consulta a AAI.

## Evidencias de partida

La autoridad documental es el [informe final](../../ES1PT/docx/build/Informe_Final.docx) y los anexos finales del mismo directorio: `Anexo_A_Actores_y_modulos_del_sistema.docx`, `Anexo_B_Catalogo_de_requerimientos_funcionales.docx`, `Anexo_C_Requerimientos_no_funcionales.docx`, `Anexo_D_Especificacion_de_casos_de_uso.docx` y `Anexo_E_Historias_de_usuario.docx`.

Para localizar contenido se consultaron [informe.md](../../ES1PT/docx/informe.md) y [las fuentes de anexos](../../ES1PT/docx/anexos/). El inventario de conservación `linea_base_es1_sha256.json` registra los 192 archivos de ES1 al inicio de este trabajo. Los nombres y secciones siguientes permiten volver a la fuente sin depender de un número de página que cambie al actualizar campos Word.

| Elemento | Base documentada | Ubicación en ES1 | Uso en ES2 |
| --- | --- | --- | --- |
| Problema y objetivo | Arriendo flexible de espacios comerciales y trazabilidad de la operación | Informe: Identificación del Problema; Objetivos del Proyecto | Introducción, criterios de comparación y conclusiones |
| Alcance | Marketplace SaaS B2B2C con registro, oferta, búsqueda, reserva, pago, firma, operación, disputas y auditoría | Informe: Solución tecnológica / Alcance y restricciones | Delimitar diseño y demostración |
| Actores | Visitante, Usuario Registrado, Arrendador, Arrendatario, Administrador; terceros propuestos | Anexo A, Modelo de actores | BPMN, casos de uso e integraciones |
| Módulos | M01–M11 | Anexo A, Módulos del Sistema | Componentes y planificación |
| Requerimientos funcionales | Catálogo declarado de 236 RF, RQF-001–RQF-236 | Anexo B | Trazabilidad y pruebas |
| Calidad | 43 RNF, RNF-001–RNF-043 | Anexo C | Comparaciones, SLA y operación |
| Casos de uso | Catálogo declarado de 52 CU | Anexo D | UML y comportamiento esperado |
| Historias | 35 HU, nueve épicas | Anexo E | Aceptación y alcance incremental |
| Arquitectura | Next.js, backend modular Go, PostgreSQL/PostGIS, Docker, GCP, BigQuery | Informe: Definición de arquitectura TI | Alternativas y diseño detallado |
| Metodología | Ciclo iterativo e incremental con prácticas de gestión del PMBOK | Informe: Metodología de Trabajo | Comparación metodológica y fases |
| KPI | Cobertura documental, avance, cronograma, pruebas y presupuesto | Informe: Indicadores de gestión | Fichas SMART; distinguir gestión y producto |
| SLA | Metas declaradas de rendimiento, disponibilidad, seguridad y recuperación | Informe: Niveles de servicio; anexo C | Plan de medición y pruebas |
| Recursos | Tres integrantes; estimación histórica de 16 semanas y 20 h por persona/semana | Informe: Equipo de trabajo; Plan de recursos | Reestimar capacidad actual, sin asumirla confirmada |

## Exclusiones que deben mantenerse visibles

ES1 excluye domótica de accesos y atribuye al proyecto un papel de intermediación tecnológica. También identifica funcionalidades sin RF asociados: favoritos, equipamiento con tarifa propia, disponibilidad recurrente por horarios, estadísticas del arrendador, soporte por tickets, centro de notificaciones/push, doble factor administrativo, métricas globales y moderación de anuncios. Algunas aparecen como historias o antecedentes; su presencia no autoriza a declararlas implementadas ni a incorporarlas silenciosamente al alcance ES2.

No se ha verificado aquí la interpretación jurídica de la intermediación. ES2 deberá investigar los instrumentos aplicables antes de formular conclusiones legales.

## Brechas y tratamiento

| ID | Hallazgo y evidencia | Tratamiento en ES2 | Estado |
| --- | --- | --- | --- |
| B-01 | Anexo A menciona «185/185» en sus criterios, pero declara catálogo ampliado de 236 | Usar anexo B como catálogo e identificar el desfase histórico; conservar ES1 | Registrado |
| B-02 | El informe menciona seis incrementos; su tabla enumera cinco más cierre | Construir fases ES2 con entregables y fechas explícitos | Abierto |
| B-03 | ES1 deriva fechas desde su entrega de septiembre; la ES2 vence el 03-11-2026 según el usuario | Replanificar; no reutilizar fechas de ES1 | Borrador en 7.1 |
| B-04 | ES1 afirma ventajas de rendimiento de tecnologías sin una medición comparativa localizada en el apartado arquitectónico | Distinguir capacidades documentadas, valoración y benchmark; verificar antes de puntuar | INV-002 |
| B-05 | BigQuery se caracteriza como inmutable, vinculado a RNF-017 | Revisar operaciones permitidas, permisos y retención; evidencia técnica en INV-002 | Abierto |
| B-06 | Retención de pagos, firma y consultas de identidad figuran como capacidades previstas | Confirmar servicio, acceso, condiciones y pruebas para cada integración | INV-003 |
| B-07 | KPI de cobertura documental no acreditan eficacia del producto | Completar métricas de solución, instrumentos y medición inicial | Abierto |
| B-08 | Metas RNF no están acompañadas por pruebas del producto en esta entrega | Diseñar pruebas y conservar ejecuciones cuando haya implementación | Abierto |
| B-09 | La tabla resumida de la guía omite mantención y difiere en cronograma respecto de la rúbrica | Cubrir los 17 criterios; cotejar con el instrumento oficial antes del cierre | Abierto |
| B-10 | Código `TIH184` en ES1/JSON frente a `TIHI84` en guía transcrita | Confirmar metadatos académicos antes de la portada final | Abierto |
| B-11 | RNF-011 exige rollback; falta detallar el tratamiento de efectos fuera de la base operativa | Diseñar reconciliación/compensación del pago externo y probar fallos | Abierto |

## Decisiones de arranque

1. La arquitectura de ES1 es la candidata inicial de diseño; su idoneidad se contrasta con evidencia en ES2.
2. Ningún catálogo, diagrama o porcentaje documental se presenta como funcionalidad implementada.
3. La fecha de entrega se registra como 2026-11-03, informada por el usuario. El desarrollo paralelo aún no tiene avance funcional acreditado.
4. Se inicia la redacción de tecnologías y se habilitan las restantes secciones con pendientes concretos.

## Próximas evidencias

- Alcance de la primera demostración y capacidad semanal acordada por el equipo.
- Resultados reproducibles de un flujo de búsqueda/reserva y de pruebas de integraciones.
- Costos con región, volumen, período y moneda; no reutilizar los montos de ES1 como cotización actual.
- Revisión docente de las fases y confirmación de metadatos académicos.
