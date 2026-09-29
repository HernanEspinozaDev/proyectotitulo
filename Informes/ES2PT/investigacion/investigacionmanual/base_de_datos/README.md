# Propuesta integral de base de datos para ES2

**Corte:** 29-09-2026. **Estado:** investigación que fundamenta el [Anexo B v2](../../../anexos/B_diccionario_datos.md) y la [propuesta backend v1.2](../../../investigacion/propuesta_backend_final.md), ya sincronizados como **diseño** para el producto completo. Ninguna migración, prueba, instancia ni control descrito aquí se declara implementado. El backend sigue siendo el monolito modular Go; no se agrega ningún producto al stack. La Ley 21.719 es criterio de construcción desde el primer incremento.

## Punto de partida y tesis

El núcleo preliminar de 17 entidades, 137 atributos y DDL textual PostgreSQL 16+ fue sustituido en el **Anexo B vigente** por el diccionario de 43 tablas. [11_inventario_producto_completo.md](11_inventario_producto_completo.md) conserva el diagnóstico que motivó la ampliación. PostgreSQL **18** es la versión objetivo local y Cloud SQL, condicionada a comprobar compatibilidad de imagen, extensiones, edición/costo y migraciones antes del primer despliegue. Cloud SQL documenta soporte para PostgreSQL 18 y PostGIS; esto no demuestra que EspaciGo ya lo haya aprovisionado ([Google Cloud, versiones](https://docs.cloud.google.com/sql/docs/postgres/db-versions); [extensiones](https://docs.cloud.google.com/sql/docs/postgres/extensions)).

La conversación adjunta sugiere UML de clases, despliegue, componentes, secuencia, actividad y estados. Se adoptan las vistas que explican decisiones reales, sin confundir un diagrama de clases con un modelo entidad–relación ni tratarlo como sustituto del DDL. El código de migraciones versionadas y el diccionario aprobado deberán concordar; los diagramas documentan vistas de ambos.

## Documentos

| Archivo | Contenido |
| --- | --- |
| [01_diagnostico_y_decisiones.md](01_diagnostico_y_decisiones.md) | Hallazgos, prioridades y decisiones que faltan |
| [02_modelo_conceptual_y_logico.md](02_modelo_conceptual_y_logico.md) | Dominios, cardinalidad, normalización, categorías, precios y extensiones |
| [03_diseno_fisico_postgresql18.md](03_diseno_fisico_postgresql18.md) | Tipos, claves, restricciones, índices, migraciones y consultas |
| [04_transacciones_y_eventos.md](04_transacciones_y_eventos.md) | Concurrencia, reserva, pagos, inbox/outbox y workers |
| [05_seguridad_privacidad_y_retencion.md](05_seguridad_privacidad_y_retencion.md) | Acceso, protección, tratamiento y ciclo de vida |
| [06_entornos_operacion_y_validacion.md](06_entornos_operacion_y_validacion.md) | Docker local, Cloud SQL, recuperación, observabilidad y evidencias |
| [07_diagramas_e_integracion.md](07_diagramas_e_integracion.md) | Inventario UML e inserción propuesta en el informe |
| [08_fuentes_primarias.md](08_fuentes_primarias.md) | Fuentes externas primarias y alcance de cada una |
| [09_deltas_del_diccionario.md](09_deltas_del_diccionario.md) | Especificación de campos/tablas candidatos y migración gradual |
| [10_revision_y_respuestas_para_cierre.md](10_revision_y_respuestas_para_cierre.md) | Revisión del nuevo consolidado, respuestas técnicas y decisiones que dependen del equipo |
| [11_inventario_producto_completo.md](11_inventario_producto_completo.md) | Cobertura de persistencia del producto completo y brechas del núcleo 17+1 |
| [12_comision_y_reparto_socios.md](12_comision_y_reparto_socios.md) | Comisión neta del 3 %, ejemplo de Split y reparto societario igualitario |
| [13_estados_reserva_producto.md](13_estados_reserva_producto.md) | Análisis que sustentó los estados completos del Anexo B vigente |
| [14_estado_y_siguiente_diseno.md](14_estado_y_siguiente_diseno.md) | Estado vigente y entregables para implementar/verificar el diseño |
| [15_diccionario_logico_ampliado.md](15_diccionario_logico_ampliado.md) | Inventario candidato previo al diccionario oficial del Anexo B |
| [16_revision_del_texto_consolidado_29_09.md](16_revision_del_texto_consolidado_29_09.md) | Contraste del nuevo texto recibido, correcciones del DDL mínimo y contrato para migraciones |
| [17_contrato_datos_backend.md](17_contrato_datos_backend.md) | Correspondencia oficial de diseño entre los 43 objetos de datos y los módulos del backend Go |
| [propuesta_final_arquitectura_y_datos.md](propuesta_final_arquitectura_y_datos.md) | Consolidado agregado por el equipo; sus afirmaciones se contrastan en la revisión 10 |
| [diagramas/](diagramas/) | Fuentes PlantUML propuestas, aún fuera del informe |

## Criterios de lectura

- **Conservado:** decisión ya presente en ES2 o en la propuesta oficial de backend.
- **Propuesto:** mejora técnica que aún no pasó al Anexo B/arquitectura oficial o depende de evidencia externa.
- **Por verificar:** demanda, base legal, costo, compatibilidad o comportamiento que exige evidencia empírica/externa.
- Los identificadores MD/PT/RQF/RNF se mantienen; las pruebas aquí descritas son criterios de aceptación futuros, no resultados.
- Las rutas de los diagramas son relativas a esta carpeta. El generador de ES2 espera imágenes relativas a la raíz de la entrega; antes de insertar figuras en `secciones/` habrá que copiarlas/renderizarlas por el flujo institucional.

## Orden de adopción recomendado

1. Conservar las decisiones ya registradas: unidad exclusiva por publicación, producto completo, CLP y 3 % neto de comisión versionada; precisar tarifa/calendario por categoría.
2. Validar con responsable competente las bases jurídicas y plazos específicos de la matriz vigente; implementar desde el primer incremento minimización, permisos y derechos.
3. Versionar la primera migración del núcleo, registrar `server_version`/`postgis_full_version()` y ejecutar MD-01–MD-13 en una instancia desechable con datos sintéticos.
4. Medir consultas, concurrencia, carga y restauración; recién entonces decidir índices adicionales, partición, tamaño y RPO/RTO alcanzables.
5. Actualizar las figuras del informe para representar el alcance ampliado; la prosa, diccionario y fuentes primarias ya quedaron integrados sin citar esta carpeta como fuente académica.
