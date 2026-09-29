# Cambios candidatos al diccionario y migraciones

Este archivo especifica **deltas propuestos** sobre las 18 tablas del Anexo B. No es un DDL ejecutable ni sustituye el diccionario vigente. Cada tabla nueva exige una decisión de producto y migración probada; los campos marcados “condicional” no se incorporan al primer incremento sin evidencia.

## Catálogo y precio: especificación mínima

| Objeto/campo | Tipo orientativo | Nulabilidad/regla propuesta | Justificación |
| --- | --- | --- | --- |
| `categoria_espacio.codigo` | `text` | PK, código estable de catálogo | Evita valores libres en `espacio.tipo`; etiquetas pueden cambiar sin alterar IDs. |
| `categoria_espacio.nombre` | `text` | NOT NULL | Nombre para interfaz e informe. |
| `categoria_espacio.activa` | `boolean` | NOT NULL | Desactiva nuevas publicaciones sin borrar historia. |
| `espacio.categoria_codigo` | `text` | FK, NOT NULL tras backfill | Reemplazo gradual de `tipo`, con soporte para todas las categorías. |
| `espacio.capacidad_personas` | `integer` | Condicional, `> 0` cuando aplique | Aforo y ocupación simultánea son conceptos distintos. |
| `espacio.zona_horaria` | `text` | Validación contra catálogo IANA, si tarifa usa horas locales | Cotización reproducible ante horario local/cambio de hora. |
| `regla_tarifa.id` | `uuid` | PK | Identidad de regla. |
| `regla_tarifa.espacio_id` | `uuid` | FK espacio, NOT NULL | Dueño de precio. |
| `regla_tarifa.version` | `integer` | NOT NULL, `>0`, UNIQUE con `espacio_id` según alcance | Rastrear reglas aceptadas; no sobreescribir historia. |
| `regla_tarifa.unidad` | `text` | Hora/día/mes del RF; semana/año/bloque bajo regla de calendario aprobada | No convertir mes a horas ni bloque de stand a día sin regla. |
| `regla_tarifa.duracion_minima` | `interval` o unidad entera | `>0`; tipo exacto tras decidir modalidad | Distingue bloque mínimo y granularidad de reservación. |
| `regla_tarifa.importe` | `numeric(14,0)` para CLP, tras migración | Precio base `>5.000` CLP según RQF-073; moneda explícita | Precio de oferta, no importe capturado; no garantiza margen positivo. |
| `regla_tarifa.moneda` | `char(3)` | NOT NULL; solo códigos autorizados | Evita sumar monedas distintas. |
| `regla_tarifa.vigencia` | `tstzrange` | Finita, `[)`, no vacía | Fechas de aplicación; definir si se elige por cotización o por estadía. |
| `regla_tarifa.politica_version` | `text`/FK | NOT NULL tras acordar catálogo | Políticas de cancelación aceptadas. |
| `reserva.tarifa_version` | referencia estable | NOT NULL cuando se migre | Une snapshot a fuente sin recalcularlo después. |
| `reserva.desglose_snapshot` | columnas tipadas/tabla hija | Condicional; suma controlada | Impuestos/cargos solo tras investigación fiscal/pagos. |

La cartera de mercado mencionada en ES2 comprende oficinas, salas o espacios multipropósito, microbodegas/bodegas, estacionamientos, locales/stands, quinchos y parcelas/eventos, además de categorías que se incorporen posteriormente. Son **clases de producto**, no siete tarifas equivalentes. Cada ficha de categoría debe registrar modalidad, duración mínima/máxima, capacidad, unidad de inventario, zona horaria, costo por transacción y precio final observado. `INV-011` solo aporta una muestra dirigida de avisos; no prueba demanda ni promedio de mercado. Un catálogo con estos códigos es una propuesta de estructura, no una decisión de precio.

## Inventario: dos modelos mutuamente excluyentes según negocio

**Modelo A, unidad exclusiva — seleccionado:** cada `espacio` publicado se reserva como un todo. Se conserva `ocupacion(espacio_id, intervalo)` y su exclusión actual. La capacidad de personas es atributo de admisión, no contador de reservas.

**Modelo B, varias unidades físicas — cambio futuro no adoptado:** `unidad_reservable(id, espacio_id, codigo, estado, capacidad)` identifica puesto, bodega o estacionamiento específico. `ocupacion.unidad_id` sería FK NOT NULL en reservas de esa modalidad y la exclusión se aplicaría a `(unidad_id, intervalo)`. Un bloqueo de toda la publicación requeriría crear ocupaciones por unidad o una regla global sincronizada. Si se venden cupos fungibles sin unidad, este modelo todavía no basta: se requeriría inventario por tramo/capacidad y bloqueo de contador o serialización.

No elegir B solo porque una sala tiene diez personas. Tampoco permitir dos reservas de un único estacionamiento por tener capacidad mayor que uno en una columna genérica.

## Historia, integración y operación: campos candidatos

| Objeto | Campos/regla | Motivo/condición |
| --- | --- | --- |
| `reserva_transicion` (condicional) | `id`, `reserva_id`, `version_anterior`, `version_nueva`, `desde`, `hacia`, `actor_id` o proceso, `motivo`, `ocurrio_en`, `correlacion` | Solo si `evento_auditoria` no prueba adecuadamente transiciones; insertar en el mismo commit de estado. |
| `outbox_evento` | `lease_token uuid`, `estado`, `reclama_en`, `ultimo_error_codigo` saneado | Evita confirmación tardía por worker con lease vencido y permite revisión de poison messages. |
| `evento_proveedor` | `tipo`, `version_payload`, `verificado_en`, `procesado_en`, `resultado_codigo` | Trazar autenticación, procesamiento y conciliación sin guardar secretos. |
| `pago` | `moneda`, `operacion_origen_id` para reverso, `importe_proveedor`, `importe_plataforma` si semántica confirmada | Conciliar montos sin afirmar custodia ni split disponible para cuenta real. |
| `documento` | `estado_validacion`, `objeto_version`/generación, `retencion_clase` aprobada | Probar vínculo entre metadatos y objeto, ciclo de acceso y borrado. |
| `solicitud_titular` | `plazo_aplicable`, `base_decision`, `evidencia_ref` minimizada | Solo tras política jurídica aprobada; no fijar 72 h por suposición. |

## Secuencia de migración del esquema actual

1. **Inventario:** ejecutar el DDL actual en base vacía PG18/PostGIS de ensayo y registrar errores; no declarar compatibilidad hasta hacerlo. Revisar datos de `tipo` y estados si existieran.
2. **Expandir:** crear catálogo, cargar categorías aprobadas, añadir FK nullable a espacio y nueva tabla de tarifas sin eliminar `tipo/precio_base`.
3. **Backfill y comparación:** mapear todo `espacio.tipo`; registrar filas sin equivalencia, comparar precio/unidad con la regla; confirmar suma y muestreo por categoría. En ausencia de datos reales, validar con fixtures sintéticos que incluyan todas las clases.
4. **Activar escritura/lectura nuevas:** API escribe la nueva representación y conserva snapshot; detectar discrepancias antes de imponer `NOT NULL`/UNIQUE. Aplicar constraints en etapa con locks medidos.
5. **Contraer:** retirar columnas antiguas únicamente tras versión de API compatible, backup probado y decisión de preservación histórica. No prometer que un `down` recupera datos eliminados.
6. **Publicar diccionario:** actualizar conteos de entidades/atributos, diagramas, trazabilidad RQF/RNF, citas y estado de evidencia; mantener ES1 intacto.

El ensayo MD-10 del Anexo B hoy dice “migrar y revertir sin pérdida”. Ese resultado no es general para cambios destructivos; proponer que su criterio distinga rollback de aplicación, reversión de esquema compatible y restauración desde backup para pérdida de datos. MD-12 queda reservado para restauración efectiva y PT-11 para RPO/RTO.
