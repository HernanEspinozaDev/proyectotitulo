# Investigación de ES2

Esta carpeta contiene la investigación nueva de ES2. La entrega final de ES1 y sus anexos son la línea base congelada; ningún archivo de esta carpeta puede usarse para reescribirlos.

Crear un archivo por tema, por ejemplo `INV-001_nombre-del-tema.md`, con esta estructura:

```markdown
# INV-001 — Nombre del tema
- Estado: pendiente | verificado | rechazado
- Fecha de consulta: AAAA-MM-DD
- Sección ES2 relacionada: `secciones/XX_nombre.md`
- Referencia de línea base: archivo, capítulo o anexo concreto de ES1

## Pregunta
## Fuentes y evidencias
## Método
## Hallazgos
## Relación con ES1
## Impacto y decisión
```

Las fuentes deben conservar autor o entidad, título, enlace o identificador, fecha de publicación y fecha de consulta. Las afirmaciones que entren al informe deben enlazar este registro y su referencia bibliográfica.

El [índice INV-024](INV-024_indice_investigacion.md) resume, para cada registro, su pregunta, su hallazgo y su límite; esta lista solo mantiene los enlaces, y la [matriz de trazabilidad](matriz_trazabilidad_es2.md) relaciona los registros con los criterios de la rúbrica.

- [INV-001, línea base y brechas](INV-001_base_y_brechas.md) · [INV-002, tecnologías y factibilidad](INV-002_tecnologias_y_factibilidad.md) · [INV-003, integraciones](INV-003_integraciones.md) · [INV-004, modelado y datos](INV-004_modelado_y_datos.md) · [INV-005, KPI y SLA](INV-005_kpi_sla.md)
- [INV-006, calidad y normativa](INV-006_calidad_y_normativa.md) · [INV-007, operación y mantención](INV-007_operacion_y_mantencion.md) · [INV-008, plantilla Word](INV-008_plantilla_word.md) · [INV-009, ejercicio económico histórico](INV-009_evaluacion_economica.md) · [INV-010, infraestructura y formalización](INV-010_infraestructura_y_formalizacion.md)
- [INV-011, precios y demanda](INV-011_muestra_precios_y_demanda.md) · [INV-012, pagos, firma e identidad](INV-012_pagos_firma_identidad.md) · [INV-013, comisión y promoción](INV-013_monetizacion_pagos_y_promocion.md) · [INV-014, giro y publicidad](INV-014_giro_publicidad.md) · [INV-015, captación con Meta](INV-015_captacion_meta.md)
- [INV-016, metodología de demanda](INV-016_metodologia_demanda.md) · [INV-017, TCO de nube](INV-017_tco_nube.md) · [INV-018, comparación de split](INV-018_comparacion_split.md) · [INV-019, integración y coherencia](INV-019_integracion_coherencia.md) · [INV-021, GCP Santiago](INV-021_gcp_santiago.md)
- [INV-020, cierre Word](INV-020_revision_word_final.md) · [INV-022, pruebas y privacidad](INV-022_pruebas_y_privacidad.md) · [INV-023, operación y herramientas](INV-023_operacion_y_herramientas.md) · [INV-024, índice de investigación](INV-024_indice_investigacion.md) · [INV-025, metadatos y rúbrica](INV-025_metadatos_y_rubrica.md)
- [INV-026, Mercado Pago, tarifa, pruebas y giros](INV-026_mercado_pago_split.md)
- [INV-027, gestión de evidencias con terceros](INV-027_gestion_terceros.md)
- [INV-028, sensibilidad de costos de terceros](INV-028_sensibilidad_costos_terceros.md)
- [INV-029, Oficina Express, patente y DOM](INV-029_domicilio_patente_y_dom.md)
- [INV-030, auditoría de pendientes](INV-030_auditoria_pendientes.md) · [INV-031, fuentes para cerrar decisiones](INV-031_fuentes_cierre.md) · [INV-032, tecnologías e inventario](INV-032_tecnologias_cierre.md) · [INV-033, cierre documental del borrador](INV-033_cierre_borrador.md)

**Trabajo manual pendiente del equipo:** la carpeta [`investigacionmanual/`](investigacionmanual/README.md) reúne en un solo lugar todo lo que falta por investigar, confirmar o medir, las decisiones abiertas y la tabla para repartir el trabajo en reunión. Es material interno: no se cita en el informe.

Todos los registros previstos existen; el índice [INV-024](INV-024_indice_investigacion.md) los reúne con su pregunta, hallazgo y límite. Cada registro conserva su estructura, sus fuentes fechadas y su límite declarado.

Durante esta fase, investigar y redactar cuerpo/anexos; Word se retoma solo al cierre del contenido. Para costos vigentes, editar `supuestos_bootstrap.json`, recalcular con `../../herramientas/simular_bootstrap.py` y seguir INV-010 y el Anexo A. El caso actual conserva reservas y ticket agregados como hipótesis. Cuando se mida cada tipo de arriendo, reemplazar `reservas` por `segmentos` con calendario de 36 meses y supuestos documentados por modalidad, como indica INV-011. El contraste del ticket único con un reparto **sintético** por categoría se ejecuta con `supuestos_segmentado.json` (SUP-21) y queda descrito en INV-033; el caso base agregado sigue vigente en `supuestos_bootstrap.json`. El modelo de INV-009 queda disponible para estudiar el método, no para presupuestar la SpA actual.
