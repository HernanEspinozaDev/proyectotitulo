# Investigación manual pendiente de ES2

Carpeta de trabajo **interna del equipo**. No forma parte del informe, no se cita en él y no reemplaza a `pendientes.md` ni a la matriz de trazabilidad. Su propósito es uno: reunir en un solo lugar **todo lo que todavía hay que investigar, confirmar, decidir o medir** antes de cerrar ES2, para discutirlo en reunión y repartir el trabajo.

- Corte: **24-09-2026**. Entrega informada: **03-11-2026**.
- Estado del informe: contenido redactado de punta a punta; Word generado y revisado (`Informe_Final.docx`, 91 páginas, más anexos A/B/C). `validar ES2PT` = **0 errores**; `validar ES2PT --final` = **1** porque quedan **14 marcadores** y tareas abiertas.
- El bloqueo que queda es **de contenido, no de formato**.

## Reglas de trabajo

1. **Un `[x]` exige evidencia registrada.** Una meta, un plan o una intención no demuestran un resultado.
2. **No se inventan** cotizaciones, entrevistas, credenciales, aprobaciones, contratos ni resultados de pruebas. Si algo no se consiguió, se anota como pendiente con su consecuencia.
3. Toda decisión nueva se registra con fecha, quién la tomó y qué cambia; si afecta a un supuesto, se actualiza en `../../supuestos_revision.md`.
4. Distinguir siempre **diseño** de **cumplimiento probado**. La Ley 21.719 entra en vigencia el 01-12-2026: en ES2 es criterio de diseño, no cumplimiento acreditado.

## Contenido

| Archivo | Para qué sirve |
| --- | --- |
| [01_estado_verificado.md](01_estado_verificado.md) | Qué ya está decidido, documentado con fuentes y verificado. Sirve para **no volver a decidir** en la reunión |
| [02_decisiones_del_equipo.md](02_decisiones_del_equipo.md) | Las decisiones que solo el equipo puede tomar, con opciones y consecuencia |
| [03_pendientes_con_terceros.md](03_pendientes_con_terceros.md) | Todo lo que exige cotización, credencial, contrato, respuesta escrita o entrevista |
| [04_trabajo_del_producto.md](04_trabajo_del_producto.md) | Todo lo que exige producto desplegado, entorno y medición |
| [05_economia_a_confirmar.md](05_economia_a_confirmar.md) | Cada supuesto económico vigente y con qué evidencia se reemplaza |
| [06_mapa_de_marcadores.md](06_mapa_de_marcadores.md) | Los 14 marcadores del informe uno por uno, con qué los cierra y quién |
| [07_orden_del_dia_y_reparto.md](07_orden_del_dia_y_reparto.md) | Guion de la reunión y tabla de asignación de trabajo |

## Cómo se cierra una tarea de esta carpeta

1. Se consigue la **evidencia** (documento, cotización, medición, acta, captura).
2. Se registra en un archivo `INV-0xx` nuevo o se actualiza `../../supuestos_revision.md`.
3. Se corrige la sección o anexo que dependía del supuesto.
4. Se retira el marcador `[[PENDIENTE: ...]]` del informe (ver `06_mapa_de_marcadores.md`).
5. Se regenera y valida el Word.

```powershell
$env:PLANTUML_JAR="$env:TEMP\plantuml.jar"
python Informes/generar.py generar ES2PT
python Informes/generar.py actualizar-word ES2PT
python Informes/generar.py validar ES2PT
```

## Referencias útiles

- Lista académica general: [`pendientes.md`](../../pendientes.md) y [`plan_cierre_pendientes.md`](../../plan_cierre_pendientes.md)
- Supuestos de trabajo vigentes: [`supuestos_revision.md`](../../supuestos_revision.md)
- Trazabilidad con la rúbrica: [`matriz_trazabilidad_es2.md`](../matriz_trazabilidad_es2.md)
- Cierre documental del 24-09-2026: [`INV-033_cierre_borrador.md`](../INV-033_cierre_borrador.md)
- Consultas ya preparadas para terceros: [`INV-027_gestion_terceros.md`](../INV-027_gestion_terceros.md) y [`INV-026_mercado_pago_split.md`](../INV-026_mercado_pago_split.md)
