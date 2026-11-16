# Sustitución de infraestructura GCP por el escenario AWS

La arquitectura se toma del corte 3dc1c18 de espacigo-aws. El escenario inicial sitúa Fargate y RDS Single-AZ en us-east-2 y utiliza Cloudflare, S3, ECR, SSM y CloudWatch. La fuente FinOps contiene estimaciones internas. La comprobación siguiente verifica su suma y conversión para los parámetros adoptados. El respaldo de tarifas por región y nivel de uso conserva su validación pendiente.

Se adopta el perfil de 1 GB, USD 26,41 mensuales y el cambio de 972 CLP/USD de IPC!C4. El documento AWS utiliza 980. Esta propuesta mantiene el parámetro del libro para obtener una base única de conversión.

| Componente | USD/mes | CLP/mes a 972 | CLP/año a 972 |
|---|---|---|---|
| RDS cómputo | 11,68 | 11.352,96 | 136.235,52 |
| RDS almacenamiento | 2,30 | 2.235,60 | 26.827,20 |
| Fargate 1 GB | 8,51 | 8.271,72 | 99.260,64 |
| IPv4 | 3,65 | 3.547,80 | 42.573,60 |
| S3 | 0,12 | 116,64 | 1.399,68 |
| ECR | 0,15 | 145,80 | 1.749,60 |
| Total | 26,41 | 25.670,52 | 308.046,24 |

La base GCP de Supuestos modelo!B12 contiene CLP 1.800.000 anuales. La sustitución aislada resulta en CLP 308.046,24 antes de créditos y una diferencia de CLP 1.491.953,76. Ese cálculo cubre únicamente la partida cloud.

## Créditos

El propietario informa USD 200. Como escenario, si los primeros seis meses coinciden con la vigencia, todo el consumo es elegible y no hay cargos adicionales, USD 158,46 cubren esos seis meses. El desembolso cloud del primer año sería CLP 154.023,12. El costo económico bruto anual permanece en CLP 308.046,24. Saldo, fechas y elegibilidad determinan el calendario real. La cobertura temporal se separa del ingreso por reservas.

## Celdas y conceptos afectados

| Ubicación | Cambio previsto |
|---|---|
| Supuestos modelo!A12:B12 | Identificar AWS y su presupuesto por período. |
| Base mensual!B20 | Vincular el costo mensual y separar la cobertura por crédito. |
| Modelo reconstruido!C13:F13 | Actualizar infraestructura, cambio y crecimiento por período. |
| IPC!B9:E10 | Sustituir GCP y su conversión. |
| Insumos, Costos fijos y Costos y gastos generales | Sustituir cloud una sola vez y recomponer subtotales. |
| Capital de trabajo | Recalcular necesidad de caja y meses de cobertura. |
| Servicio respaldo y Revision respaldo | Actualizar RDS, PITR, S3, volúmenes y retención. |
| FlujoNeto y Modelo reconstruido | Propagar cambios después de conciliar la base comercial y financiera. |

La referencia AWS parte de 5 GB de S3, mientras Revision respaldo plantea 9,6 GB de objetos anuales bajo su hipótesis de 192 reservas. Se debe conciliar volumen, solicitudes y versiones retenidas. El perfil Fargate requiere comprobar memoria para web, API y procesamiento documental. Multi-AZ constituye otro escenario de costo y nivel de servicio.

## Fuentes

- Propuesta interna docs/architecture/aws-proposal/05-cost-analysis.md, 15 de noviembre de 2026.
- AWS Fargate Pricing, consulta del 16 de noviembre de 2026. https://aws.amazon.com/fargate/pricing/
- Amazon RDS for PostgreSQL Pricing. https://aws.amazon.com/rds/postgresql/pricing/
- Amazon S3 Pricing. https://aws.amazon.com/s3/pricing/
- AWS Free Tier. https://aws.amazon.com/free/
