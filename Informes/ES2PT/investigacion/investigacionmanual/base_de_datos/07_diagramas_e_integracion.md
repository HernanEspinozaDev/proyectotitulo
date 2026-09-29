# Diagramas UML propuestos e integración académica

## Criterio de diagramación

La conversación adjunta recomienda UML y PlantUML. Para dar profundidad sin repetir las cuatro figuras `datos_*.puml` existentes se proponen siete vistas con preguntas distintas. La notación de clases permite ver atributos y multiplicidades, pero PK/FK, exclusión, índices, transacciones, permisos y retención se completan en diccionario y DDL. Los estereotipos `<<PK>>`, `<<FK>>`, `<<EXCLUDE>>` y `<<propuesta>>` son **convención documental local**, no restricciones UML o SQL automáticas. Un ER conceptual podría añadirse si la rúbrica lo exige; no se afirma que la clase UML sea literalmente un ER ([PlantUML, clases](https://plantuml.com/class-diagram); [OMG, UML 2.5.1](https://www.omg.org/spec/UML/2.5.1/)).

| Figura fuente | Pregunta que resuelve | Ubicación futura sugerida | Lectura obligatoria |
| --- | --- | --- | --- |
| [01_modelo_conceptual.puml](diagramas/01_modelo_conceptual.puml) | ¿Qué dominios se relacionan y dónde caben nuevas categorías? | 3.4, antes de los cuatro diagramas existentes | Distinguir entidades vigentes de extensiones propuestas (color). |
| [02_modelo_fisico_reserva.puml](diagramas/02_modelo_fisico_reserva.puml) | ¿Qué claves/invariantes impiden doble reserva? | Anexo B, junto al DDL de `reserva/ocupacion` | `EXCLUDE` y FK compuesta se detallan en SQL, no se infieren de las líneas UML. |
| [03_despliegue_local.puml](diagramas/03_despliegue_local.puml) | ¿Cómo se reproduce el entorno Go + PG18/PostGIS en Linux/Docker? | 3.6 o anexo técnico de entornos | Imagen/digest, extensiones y volumen son pendientes de ejecución. |
| [04_despliegue_cloud.puml](diagramas/04_despliegue_cloud.puml) | ¿Dónde residen datos, archivos, secretos y analítica en GCP? | 3.6, como vista de datos del despliegue general | No representa infraestructura existente ni datos reales. |
| [05_secuencia_reserva.puml](diagramas/05_secuencia_reserva.puml) | ¿Qué se confirma atómicamente y qué ocurre tras un conflicto? | 3.4 o 3.7 | Pago ocurre después del commit; la excepción de exclusión es el árbitro. |
| [06_secuencia_outbox.puml](diagramas/06_secuencia_outbox.puml) | ¿Cómo sobrevive una publicación a reinicios y duplicados? | 3.3/3.4 | Lease y token de reclamo, idempotencia downstream. |
| [07_estados_reserva_producto.puml](diagramas/07_estados_reserva_producto.puml) | ¿Qué hito y actor permite cada transición del producto? | 3.4 y Anexo B | El DDL textual debe agregar `en_disputa`, `cerrada` y cancelación del arrendatario tras acordar literales. |

Se añadió una vista de estados porque el producto completo exige más hitos que la antigua demo y el `CHECK` del Anexo B omite estados requeridos por ES1. Un diagrama de componentes puede incorporarse si se necesita describir `pgx/sqlc`, migrador e interfaces, pero la vista de arquitectura 3.3/3.7 ya hace esa función. La selección privilegia evidencia y legibilidad sobre cantidad de figuras.

## Esquema de integración al informe

| Lugar | Adición concreta | Fuente externa primaria y condición |
| --- | --- | --- |
| `secciones/03_04_datos.md` | Subapartado de unidad reservable, categoría y vigencia de tarifas; explicar snapshot y límites del modelo 17+1. Agregar figuras 01/02/05 con captions que digan “propuesta”. | PostgreSQL constraints/ranges y PostGIS. Validar cardinalidades con requisitos por categoría. |
| `secciones/02_01_analisis.md` y Anexo A | Recalculado con 3 % neto + IVA supuesto de comisión, tarifa de proveedor descontada al vendedor y costo de instancia API mínima; 12 %/25 % de comisión quedan como escenarios históricos identificados. Faltan tarifa contractual, documentos y prueba de Split. | Decisión del usuario, supuestos versionados y tarifas/capacidades externas verificadas. |
| `anexos/B_diccionario_datos.md` | Corregir afirmación de política “aprobada”; añadir catálogo, regla tarifaria/unidad exclusiva, comisión versionada al 3 % neto, diccionario de campos propuestos y mapa completo de estados; versión PostgreSQL 18 objetivo; plan de migraciones. | Fuentes de PostgreSQL/Cloud SQL, decisión del usuario sobre alcance/tasa y revisión tributaria. |
| `secciones/03_03_componentes.md` y propuesta oficial de backend | Sustituir el alcance de demo acotada por diseño del producto completo; completar ciclo inbox/outbox con lease token, retry y terminal de revisión; incluir figura 06 sin duplicar el diagrama de outbox existente si este ya cubre lo mismo. | Nueva decisión del usuario y requisitos ES1; PostgreSQL `SKIP LOCKED`/transacciones, documentación Pub/Sub. |
| `secciones/03_06_infraestructura.md` | Registrar paridad local/nube, versión/extension, pool y backup/PITR; figura 03/04 como vistas de persistencia si aportan más que la figura de infraestructura actual. Corregir presupuesto de Cloud Run mínimo uno y edición de Cloud SQL. | Google Cloud/Docker, cifras de costo actualizadas. |
| `secciones/05_01_pruebas.md` y Anexo C | Agregar criterios de aceptación de migración, aislamiento, idempotencia y recuperación sin afirmar resultados; trazar MD-13 y PT-11/PT-16. | Evidencia de ejecución futura, no una cita para “aprobado”. |
| `secciones/06_01_disponibilidad.md`, `06_02_continuidad.md`, `06_03_mantencion.md` | Indicadores de pool/outbox/backups, restauración aislada, gestión de cambios expand/contract y responsable. | Cloud SQL backup/connection docs; ensayo real para RPO/RTO. |
| Bibliografía e `informe.json` | Citar **fuentes primarias externas**, no estos archivos; decidir si las figuras van al cuerpo o anexo y respetar orden de primera referencia de anexos. | Política editorial del repositorio. |

El Anexo B existente se llama **B de ES2**; los `anexo a/b/c` minúsculos del ES1 congelado no deben renumerarse. `ES2PT` solo debe modificar Markdown de `secciones/`/`anexos/` durante integración coordinada. Esta carpeta de investigación permanece independiente y no se copia directamente a `build/`.

La [especificación de deltas](09_deltas_del_diccionario.md) sirve para transformar las decisiones aprobadas en migraciones y para corregir el criterio irreal de reversión sin pérdida de MD-10 antes del ensayo.

## Criterio de calidad para cada figura

Pie con propósito, fuente y “diseño propuesto”; multiplicidades legibles, leyenda de convenciones, fecha/versión del modelo y distinción visual entre núcleo actual y extensión. Cada flecha debe poder rastrearse a un campo FK o a un flujo explicado. No mostrar contraseñas, direcciones reales, claves ni endpoints secretos. Renderizar PlantUML cuando se abra la fase de integración visual; no se declara que estas fuentes ya hayan generado figuras finales.
