# Modelo conceptual y lógico propuesto

## Límites y vocabulario

El núcleo actual de 17 entidades de negocio + `outbox_evento` permanece como punto de partida. Para leerlo académicamente se distinguen **entidad** (objeto de identidad propia), **relación** (asociación/cardinalidad), **atributo**, **invariante** y **evento histórico**. Se normalizan hechos con distinta dependencia funcional; los snapshots deliberadamente redundantes de reserva documentan el acuerdo aceptado y no se recalculan después de cambiar el anuncio. Un diagrama UML de clases con estereotipos muestra cardinalidades, pero el diccionario y las migraciones precisan la semántica relacional.

## Agregados y cardinalidades existentes

| Agregado | Relaciones principales | Regla que debe explicarse en Anexo B |
| --- | --- | --- |
| Identidad | `usuario` 1:N `rol_usuario`, 1:N `verificacion`, 1:N `solicitud_titular` | Dos roles comerciales pueden coexistir. El acceso administrativo exige decisión y auditoría separadas. |
| Oferta | `usuario` 1:N `espacio`; `espacio` 1:N `reserva` | El propietario de una reserva se obtiene por espacio; evitar duplicarlo salvo snapshot motivado. |
| Calendario | `espacio` 1:N `ocupacion`; `reserva` 0..1 `ocupacion` | Una sola exclusión activa por unidad reservable; bloqueos manuales sin reserva. |
| Finanzas | `reserva` 1:N `pago`, 1:N `garantia`, 0..1 `liquidacion`; `evento_proveedor` 0..1 `reserva` | Pago es intento/operación, no sinónimo de reserva confirmada. Referencia externa puede llegar antes de correlación. |
| Contrato/uso | `reserva` 1:N `contrato`; `contrato` 1:N `firma_contrato`; `reserva` 1:N `operacion_arriendo`/`disputa` | La versión firmada debe estar ligada a contenido/hash inalterado y firmantes exigidos. |
| Evidencia | `documento` pertenece exactamente a un recurso entre seis FK; `evento_auditoria` registra actor/recurso/acción | Un archivo en Cloud Storage no implica permiso de lectura; el hash no es prueba de inmutabilidad del bucket. |
| Integración | Cambio de dominio 1:N `outbox_evento` en la misma transacción | Consumo al menos una vez, con deduplicación posterior. |

## Extensiones necesarias para el producto multcategoría

**Catálogo de categorías** (`categoria_espacio`): clave estable, nombre, activo, versión de definición y descripción de atributos permitidos. `espacio.categoria_id` pasa a FK; migración inicial mapea todos los valores actuales y falla si aparece un código desconocido. La tabla admite todas las categorías ES1 desde el diseño del producto. Los atributos comunes (superficie, ubicación, aforo/capacidad cuando aplique) conservan columnas tipadas. Los atributos específicos se incorporan en tablas relacionadas cuando son filtrables, obligatorios o sujetos a integridad; JSONB solo para metadatos poco estructurados sin reglas críticas. Un JSONB genérico para precio/capacidad impediría documentar bien dependencias, consultas e invariantes.

**Unidad reservable y capacidad:** la decisión posterior fija una publicación `espacio` por unidad exclusiva para el producto. Cinco estacionamientos físicos se representan como cinco espacios, aunque el anfitrión pueda administrarlos como grupo en la interfaz. `aforo_personas` limita personas autorizadas, no número de reservas. Si más adelante se venden cupos fungibles o unidades bajo una única publicación, se requerirá `unidad_reservable`/inventario por tramo y otra política transaccional antes de aceptar dos reservas simultáneas; el `EXCLUDE` actual por espacio no cubre esa modalidad.

**Tarifas y condiciones:** `regla_tarifa(id, espacio_id, version, unidad_temporal, importe, moneda, vigente_desde, vigente_hasta, mínimo, política_id)` más detalle de días/horarios solo si una categoría lo exige. Evitar solapar reglas activas para el mismo ámbito de aplicación; definir precedencia cuando haya promociones. Una cotización identifica la versión utilizada, guarda desglose y vencimiento; la reserva persiste `estadia`, `comision`, `garantia`, `moneda`, impuestos si corresponden y `politica_snapshot`. El redondeo debe ser determinista y expresado en moneda mínima. No crear tarifas por categoría con los precios publicados de INV-011 como si fueran precios contratados o demanda observada.

**Historial de estados:** el campo `reserva.estado` indica el estado actual. Una tabla append-only `reserva_transicion` es propuesta si se necesita probar actor, origen, motivo, instante y versión anterior/nueva de cada salto; `evento_auditoria` genérico puede cubrirlo solo si tiene esos atributos y restricciones. Evitar doble fuente de verdad sin un contrato claro. El producto completo debe mapear explícitamente pagos, aprobación del anfitrión, firmas, cancelaciones, check-in/out, disputa y liquidación ya presentes en ES1/Anexo B.

**Finanzas:** proponer `movimiento_financiero` insert-only para hechos de cobro/reembolso/contracargo, con tipo, importe, moneda, dirección, operación externa e intento origen; los tipos externos concretos dependen del sandbox y contrato. No reemplazar `pago`: su estado operativo se reconcilia. La liquidación debe conciliar comprador, cargo de proveedor, **3 % neto de comisión EspaciGo**, IVA aplicable y neto vendedor. El reparto posterior de utilidades entre tres socios iguales pertenece a la SpA, no al Split 1:1 ni a la reserva. Cuenta de cobro del arrendador y detalle tributario son dominios pendientes, con acceso/retención propios; no almacenar credenciales de proveedor ni datos de tarjeta.

**Funciones fuera del núcleo:** `campaña/entitlement`, `respuesta_nps`, notificaciones, mensajes y reseñas se modelan solo cuando su alcance se apruebe. Las métricas agregadas no deben introducir datos de visitantes identificables en el núcleo. BigQuery no sustituye los derechos de acceso del vendedor ni los hechos operativos PostgreSQL.

## Normalización y coherencia temporal

1. Catálogo y reglas de precio separan valores estables de anuncios cambiantes: evita repetir reglas en cada espacio y facilita nuevas categorías como datos.
2. La reserva guarda la instantánea económica aceptada: duplicación controlada con finalidad contractual y trazabilidad de versión.
3. Los eventos del proveedor y outbox son hechos distintos: uno entra desde tercero y el otro publica un cambio interno. No fusionarlos por tener `payload`.
4. La vigencia de precios y la disponibilidad usan tiempo de forma diferente: `timestamptz` para instantes, `tstzrange` semiabierto `[inicio, fin)` para ocupación. Definir zona de presentación y reglas de horario local/DST para cotización; almacenar instantes en UTC y zona de negocio identificada cuando sea necesaria.
5. La relación `documento` con seis propietarios potenciales exige el `CHECK` actual y FK reales. Si se agregan más tipos, evaluar subtablas por clase documental. Una referencia polimórfica `owner_type/owner_id` sin FK pierde integridad.

## Vistas derivadas

Una consulta o vista SQL puede presentar calendario disponible, importe conciliado o métricas de operación, pero debe declarar filtros de autorización en la API. Las vistas materializadas solo se justifican por costo de cálculo medido, política de refresco y tolerancia a datos atrasados. Las métricas premium agregadas pertenecen a BigQuery y su acceso requiere `entitlement` operacional aprobado, no una tabla de visitas por usuario en PostgreSQL.
