# INV-021 — Estimación preliminar de Google Cloud en Santiago (southamerica-west1)

- Consulta documental: 23-09-2026. Base de ES1 y continuidad de [INV-017](INV-017_tco_nube.md).
- Estado revisado: **estimación documental, no cotización formal ni aprobación técnica, tributaria o legal**. Falta guardar SKU/precios de la cuenta o exportación del calculador, fecha, moneda y condiciones. La [lista oficial de precios de Cloud Run](https://cloud.google.com/run/pricing) identifica Santiago como Tier 2; las tarifas de cada servicio y los volúmenes de este documento deben auditarse por separado antes de usarlos como precio contratado.
- Pregunta: ¿Cuáles son las tarifas reales para la región local y su impacto fiscal en EspaciGo (SpA)?

## Tasas utilizadas para la estimación de southamerica-west1

A diferencia de Iowa (`us-central1`), Cloud Run clasifica Santiago como región Tier 2. La tabla reúne tasas anotadas en la estimación inicial: su correspondencia exacta con cada SKU, servicio y región aún requiere auditoría.

| Recurso | Tarifa pública para Santiago (`southamerica-west1`) | Diferencia vs Iowa (aprox.) |
| --- | --- | --- |
| Cloud Run | CPU activa USD 0,0000336/vCPU-s; RAM activa USD 0,0000035/GiB-s; USD 0,40/millón de solicitudes. | +40% en CPU/RAM |
| Compute Engine E2 | `e2-standard-2` (2 vCPU, 8 GiB): USD 0,093816/h bajo demanda. | +40% |
| Disco de arranque VM | Balanced Persistent Disk: USD 0,192/GiB-mes (aprox USD 0,000263/GiB-h). | +40% |
| Cloud SQL PostgreSQL HA | CPU USD 0,11564/vCPU-h; RAM USD 0,0196/GiB-h; SSD HA USD 0,476/GiB-mes; Respaldos USD 0,112/GiB-mes. | +40% |
| Storage | Standard: USD 0,038/GiB-mes. | +38% |
| Transferencia de salida | USD 0,20/GiB (hacia América). | Mismo precio |
| Load Balancer y Armor | Cargos globales base iguales (USD 0,025/h + 0,008/GiB procesado). | Mismo precio |

## Nuevo cálculo mensual para Santiago

Aplicando las tarifas de Santiago al mismo escenario de uso y bolsas de [INV-017](INV-017_tco_nube.md):

1. **Cloud SQL HA:** `2×730×0,11564 + 8×730×0,0196` = USD 283,30/mes.
2. **Almacenamiento SQL y Backup:** `20×0,476 + 20×0,112` = USD 11,76/mes.
3. **Storage Standard:** `50×0,038` = USD 1,90/mes.
4. **Cloud Run (Mínimo 0):** `200.000×0,0000336 + 100.000×0,0000035 + 0,40` = USD 7,47/mes.
5. **Componentes comunes (Egress, LB, Armor, Bolsas):** USD 79,80/mes con los supuestos de INV-017.

**Total aritmético Cloud Run (mínimo 0) en Santiago: USD 384,23/mes** con las tasas aquí anotadas, antes de validar sus SKU y sin IVA. El costo comparable de Iowa en INV-017 era USD 297,01/mes. La razón aritmética aproximada es 1,29; no constituye un «factor real» contractual aplicable a otros perfiles.

## Implicancias de Facturación y Tributación en Chile

1. **IVA y facturación:** la [guía tributaria de Google Cloud](https://docs.cloud.google.com/billing/docs/resources/vat-overview) advierte que los SKU no incluyen impuestos y que el tratamiento depende de la ubicación y la cuenta. El [SII](https://www.sii.cl/preguntas_frecuentes/iva_serv_digitales/001_200_7773.htm) indica factura de compra para ciertas adquisiciones de servicios remotos de un extranjero cuando el beneficiario es contribuyente de IVA y lo informa al prestador. No se ha verificado el emisor, tipo de cuenta, factura, crédito fiscal ni eventual impuesto adicional de EspaciGo; no afirmar retención cero ni recuperación automática del 19 %.
2. **Moneda:** Google indica que [cada cuenta de facturación tiene una moneda definida al crearla](https://docs.cloud.google.com/billing/docs/resources/currency); algunas cuentas convierten desde USD a moneda local. No hay cuenta ni factura de la futura SpA. USD/CLP = 1.000 es una hipótesis de simulación, no la moneda ni el tipo de cambio contratados.
3. **Residencia de datos:** [Cloud SQL permite elegir Santiago](https://docs.cloud.google.com/sql/docs/postgres/locations), pero la [guía de residencia de Google](https://docs.cloud.google.com/assured-workloads/docs/data-residency) distingue datos del cliente, metadatos y servicios configurables. Seleccionar una región para recursos no demuestra por sí solo residencia de **todos** los datos ni cumplimiento de Ley 21.719. Revisar producto por producto, copias, registros, soporte, transferencia internacional y contrato.

## Decisión y Siguientes Pasos

- **No aprobado como cotización:** `supuestos_bootstrap.json` ya usa tarifas regionales como escenario provisional; conservar esa trazabilidad y auditar SKU, cantidades y factura antes de llamar «exacta» la caja.
- **Siguiente paso:** cotejar las tasas de Cloud Run, Cloud SQL, Storage, Compute Engine, red, balanceador y Armor con la tabla de precios o exportación SKU de la cuenta; documentar diferencias y recalcular el simulador. Un contador deberá revisar el tratamiento tributario de los comprobantes reales.
