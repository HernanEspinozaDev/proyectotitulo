# Diagnóstico y decisiones de diseño

## Evidencia documental examinada

Se cotejaron `contexto/README.md`, `decisiones.md`, contexto/pendientes/JSON de ES2, secciones 3.3–3.7 y 5–6, el Anexo B, el catálogo de casos del Anexo C, `INV-004`, la propuesta oficial de backend y la conversación adjunta. El Anexo B es la versión más desarrollada del modelo; `INV-004` conserva un recuento anterior y no debe utilizarse para afirmar el número actual de entidades. Los cuatro diagramas `datos_*.puml` son vistas parciales. No existe evidencia de que el DDL esté aplicado ni de resultados MD/PT.

## Brechas priorizadas

| Prioridad | Hecho actual | Mejora propuesta y razón | Decisión/evidencia de cierre |
| --- | --- | --- | --- |
| P0 | `ocupacion` excluye solapamientos activos; la reserva es una por espacio | **Decisión posterior:** cada `espacio` es unidad exclusiva; aforo no crea cupos simultáneos. Varias unidades físicas se publican separadas. | MD-02/PT-02; para inventario compartido futuro se requerirá otro modelo. |
| P0 | `espacio.tipo` es texto libre; el backend habla de catálogo extensible | Crear catálogo referenciado por FK y tabla de reglas/tarifas versionadas; mantener snapshot contractual en reserva. | Códigos de categoría, unidad temporal, capacidad, impuestos y reglas de redondeo aprobados. |
| P0 | El backend oficial anterior acota una demo y usa estados resumidos; el usuario decidió planificar el producto completo | Conservar los hitos de pago, aprobación, firma, check-in/out, cancelación y liquidación de ES1; mapa de estados del producto y actualización de backend/informe. | Contrato de transiciones y pruebas de transición. |
| P0 | Matriz de tratamiento del Anexo B afirma política aprobada, supresión ≤72 h y conservación 5 años; 3.4 y pendientes dicen bases/plazos sin aprobar | Corregir el estatus a **propuesto/por revisar**. No ejecutar eliminación o bloqueo irreversible a partir de esta matriz. | Decisión jurídica/documental por finalidad, plazo y responsable; PT-16. |
| P0 | Pagos, garantía y liquidación usan montos, pero faltan modelo de impuestos, moneda/escala y trazabilidad de reversos parciales | Definir contrato de importes y, si el flujo lo requiere, `movimiento_pago`/ajuste relacionado al intento original; no inferir escrow. | Investigación separada de Mercado Pago, fiscalidad y sandbox. |
| P1 | DDL `PostgreSQL 16+`; conversación solicita PostgreSQL 18 local→Cloud SQL | Adoptar 18 como objetivo; fijar imagen local PostGIS compatible y verificar versión/edición de Cloud SQL y extensiones al desplegar. | Inventario reproducible con versiones reales y costo. |
| P1 | Existen PK/FK, GiST geográfico y exclusión; casi no hay índices de lectura por FK/consulta | Diseñar índices desde consultas de reserva, dashboard de anfitrión y trabajos; medir antes de crearlos. PostgreSQL no crea automáticamente índice en el lado referenciante de una FK. | SQL de consultas y `EXPLAIN (ANALYZE, BUFFERS)` con datos representativos. |
| P1 | Outbox tiene lease temporal, pero no propietario/fencing ni estado de revisión | Añadir token/versión de reclamo, estado y resultado de publicación; impedir que worker con lease vencido marque el trabajo ajeno. | Diseño de reintento, ensayo de caída y duplicado. |
| P1 | Documento acepta seis FK opcionales con `exactamente uno` | Mantener inicialmente por integridad fuerte; definir ownership/autorización y evaluar tablas por propósito si crece complejidad. Evitar reemplazarlo por `tipo,id` sin FK real. | Casos de acceso y volumen de documentos. |
| P1 | No hay plan de migración, rollback y restauración de DB como artefacto reproducible | Migraciones SQL numeradas con `expand/contract`, ensayo de restauración y trazabilidad versión app/esquema. | Pipeline y evidencia MD-12/PT-11. |
| P2 | Se proponen analítica premium y NPS, pero el DDL nuclear no contiene campañas/entitlements/NPS | Mantenerlos como extensión condicionada al alcance funcional y privacidad. BigQuery no decide permisos ni hechos de pago. | Decisión de producto y contrato de eventos. |
| P2 | Se sugieren particiones, UUIDv7 y JSONB en conversación | Evaluar con volumen y planes; no aplicar por moda. Particionar `ocupacion` por fecha puede romper la exclusión global de solapamiento. | Métricas, pruebas de integridad, costo de mantenimiento. |

## Decisiones de arquitectura propuestas

1. **Sistema de registro:** PostgreSQL almacena decisiones transaccionales; Cloud Storage guarda binarios; Pub/Sub/BigQuery recibe hechos seleccionados de forma asíncrona. Los pagos externos no participan en ACID local.
2. **Mayor objetivo:** PostgreSQL 18/PostGIS en local y Cloud SQL; el DDL 16+ actual continúa como borrador compatible hasta migración y ensayo. No se requiere una función nueva de 18 para el primer incremento.
3. **Modelo evolutivo:** conservar 17+1 como base parcial; agregar tablas solo para reglas observables del producto. La categoría no se codifica en el esquema como una única demo.
4. **Restricciones estructurales:** priorizar FK, `CHECK`, unicidad y exclusión cuando expresen invariantes por fila/tabla. Las transiciones, permisos y reglas entre servicios quedan en casos de uso y pruebas.
5. **Identificadores:** conservar UUIDv4 del DDL mientras no se mida problema real de localidad. `uuidv7()` existe en PostgreSQL 18, pero su adopción necesita evaluar exposición de tiempo de creación, compatibilidad y migración; no obliga a cambiar todas las PK ([PostgreSQL 18, funciones UUID](https://www.postgresql.org/docs/18/functions-uuid.html)).

## Respuestas y bloqueos remanentes

Las seis preguntas iniciales tienen [respuesta técnica desarrollada](10_revision_y_respuestas_para_cierre.md): unidad exclusiva por publicación; CLP y cálculo exacto con regla de calendario/versión; snapshot económico y contractual; máquinas separadas de reserva, pago y disputa para el producto completo; tratamiento por finalidad; y Cloud SQL dimensionado por costo/ensayo. El [inventario de producto](11_inventario_producto_completo.md) recoge dominios que faltan al núcleo 17+1.

**Decisiones posteriores aplicadas:** el usuario fijó 3 % neto de comisión más IVA de la comisión cuando corresponda y participación societaria igualitaria de tres fundadores, separada del Split 1:1. El [Anexo A](../../../anexos/A_evaluacion_economica.md) ya recalcula el escenario con 3 % y una instancia mínima de Cloud Run para los workers internos: a 100.000 CLP de arriendo, la comisión neta de 3.000 CLP iguala el costo variable propio supuesto de 3.000 CLP por reserva. Siguen pendientes IVA/documentos por flujo, plazos y bases de tratamiento, capacidad contractual de Mercado Pago y costo/recuperación reales en GCP. No se resuelven mediante una restricción SQL ni con un diagrama.
