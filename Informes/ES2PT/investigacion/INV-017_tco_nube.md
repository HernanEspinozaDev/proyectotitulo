# INV-017 — TCO comparable de Cloud Run y máquinas virtuales

- Consulta documental: 23-09-2026. Base de ES1: Next.js, Go, PostgreSQL y GCP son tecnologías **propuestas**, sin despliegue ni telemetría comprobada. Continuidad de [INV-010](INV-010_infraestructura_y_formalizacion.md) y del [Anexo A](../anexos/A_evaluacion_economica.md).
- Estado: ejercicio de ingeniería con tarifas públicas de **Iowa (`us-central1`)** y cantidades hipotéticas, sin cotización comercial, factura ni medición de EspaciGo. La región de producción y el tratamiento internacional de datos siguen pendientes.
- Pregunta: ¿cuánto cambia el costo de la capa de aplicación si se mantiene igual demanda, base de datos, respaldo, almacenamiento, protección y balanceo?

## Fuentes oficiales y precisión de los precios

| Recurso | Tarifa pública consultada para Iowa, sin descuento | Fuente y límite |
| --- | --- | --- |
| Cloud Run, facturación por solicitudes | CPU activa USD 0,000024/vCPU-s; RAM activa USD 0,0000025/GiB-s; USD 0,40/millón de solicitudes. Para instancias mínimas inactivas, CPU y RAM USD 0,0000025 por unidad-s | [Google Cloud Run, precios](https://cloud.google.com/run/pricing). Se excluye el nivel gratuito, créditos y CUD para no depender de elegibilidad o consumo de otros proyectos. El tiempo facturable real depende de latencia, concurrencia, instancias y configuración. |
| Compute Engine E2 | `e2-standard-2` (2 vCPU, 8 GiB): USD 0,06701142/h bajo demanda | [Google, máquinas de propósito general](https://cloud.google.com/products/compute/pricing/general-purpose). Sin compromisos ni Spot. |
| Disco de arranque VM | Balanced Persistent Disk: USD 0,000136986/GiB-h | [Google, discos](https://cloud.google.com/compute/disks-image-pricing). Los discos VM son adicionales al precio de máquina. |
| Cloud SQL PostgreSQL Enterprise regional (HA) | CPU USD 0,0826/vCPU-h; RAM USD 0,014/GiB-h; SSD HA USD 0,000465753/GiB-h; respaldos usados USD 0,000109589/GiB-h | [Google Cloud SQL, precios](https://cloud.google.com/sql/pricing) y [descripción de HA](https://docs.cloud.google.com/sql/docs/postgres/high-availability). HA se cobra con sus propias tarifas; no multiplicar otra vez por dos. No se incluye recuperación entre regiones. |
| Storage, balanceador y Armor | Storage Standard USD 0,000027397/GiB-h; primera agrupación de cinco reglas globales USD 0,025/h; procesamiento regional de entrada/salida USD 0,008/GiB; Armor Standard USD 0,006849315/política-h + 0,001369863/regla-h + 0,75/millón de solicitudes globales | [Storage](https://cloud.google.com/storage/pricing), [balanceador](https://cloud.google.com/load-balancing/pricing), [Armor](https://cloud.google.com/armor/pricing). Operaciones Storage, salida a Internet y SKU adicionales se deben medir por separado. |

El [precio de Cloud Run](https://cloud.google.com/run/pricing) clasifica Santiago (`southamerica-west1`) como **Tier 2**, mientras Iowa es Tier 1. El sitio publica tarifas dependientes de región para los demás servicios. Por tanto, el factor 1,35 de `supuestos_bootstrap.json` es solo una **provisión de ES2** y no representa los SKU verificados de Santiago. Se necesita presupuesto del Pricing Calculator o lista de SKU en la cuenta y moneda real antes de elegir región.

## Carga y arquitectura idénticas donde corresponde

Mes tipo de 730 horas, sin descuentos: 1.000.000 solicitudes HTTP, **200.000 vCPU-s activos** y **100.000 GiB-s activos** en Cloud Run. Eso supone un contenedor de 2 vCPU/1 GiB y 100.000 segundos agregados de instancia activa; es una hipótesis de facturación, no un perfil medido ni una promesa de rendimiento. Ambas alternativas atienden la misma demanda, publican por un balanceador externo y aplican cinco reglas de Armor. Comparten Cloud SQL Enterprise **HA de 2 vCPU/8 GiB, 20 GiB SSD, 20 GiB de respaldo usado**, 50 GiB de objetos, 100 GiB de transferencia de salida y 100 GiB procesados por el balanceador. Se reservan idénticos USD 30/mes de observabilidad, compilación, secretos/DNS, correo y staging. Estas bolsas son provisiones de INV-010, no tarifas ilimitadas.

La salida a Internet se valora **provisionalmente** en USD 0,20/GiB × 100 = USD 20 en ambos casos; su SKU real depende del destino, modalidad de red y producto. Los costos de operaciones de Storage, IP/NAT y posibles conectores no están cerrados. Para Cloud Run, la [conexión privada a Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/connect-run) puede usar Direct VPC egress; no se ha probado su configuración ni cuantificado todo su tráfico. La base HA y el respaldo se presupuestan para ambas alternativas; ninguna de ellas acredita por sí sola los SLA completos de EspaciGo ni una restauración ensayada.

- **Opción A:** Cloud Run en Iowa, facturación por solicitudes, mínimo cero instancias; tolera arranque en frío sujeto a prueba. Se muestran también mínimos de una y dos instancias *siempre templadas*, manteniendo la misma actividad agregada.
- En la sensibilidad, **mínimo 1** representa una instancia templada en **solo uno** de los dos servicios (frontend o API); el otro puede arrancar en frío. **Mínimo 2** representa una instancia templada por servicio, suponiendo la misma forma de 2 vCPU/1 GiB para el cálculo. No se interpreta «mínimo 1» como disponibilidad inmediata de ambos servicios. La distribución de los 100.000 segundos activos entre ellos y el costo real se deben perfilar.
- **Opción B:** grupo administrado regional de **dos VM `e2-standard-2`** en zonas distintas, 20 GiB de disco Balanced por VM y balanceador común. [Google documenta la distribución por zonas](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups); hace falta configurar autohealing, actualización y capacidad por zona. Las VM reservan 4 vCPU y 16 GiB en conjunto, frente al cobro elástico de Cloud Run: ese sobredimensionamiento mínimo es parte del costo de mantener dos réplicas disponibles. La equivalencia de latencia, concurrencia y capacidad necesita prueba de carga.

## Cálculo mensual reproducible

| Partida común | Fórmula USD/mes | USD/mes |
| --- | ---: | ---: |
| Cloud SQL HA CPU y RAM | `2×730×0,0826 + 8×730×0,014` | 202,36 |
| SQL SSD HA y respaldo usado | `20×730×0,000465753 + 20×730×0,000109589` | 8,40 |
| Storage Standard | `50×730×0,000027397` | 1,00 |
| Transferencia externa, **provisión** | `100×0,20` | 20,00 |
| Balanceador: regla y bytes | `730×0,025 + 100×0,008` | 19,05 |
| Armor: política, cinco reglas, 1 M solicitudes | `730×0,006849315 + 5×730×0,001369863 + 0,75` | 10,75 |
| Bolsas operativas comunes, **provisiones** | `5+3+2+10+10` | 30,00 |
| **Subtotal compartido** | suma sin redondeo intermedio | **291,56** |

| Capa de aplicación | Fórmula USD/mes | Aplicación | Total con comunes USD/mes | Total USD/año constante |
| --- | ---: | ---: | ---: | ---: |
| Cloud Run, mínimo 0 | `200.000×0,000024 + 100.000×0,0000025 + 1×0,40` | 5,45 | **297,01** | 3.564,07 |
| Cloud Run, mínimo 1 | `5,45 + (730×3600−100.000)×(2+1)×0,0000025` | 24,41 | **315,97** | 3.791,59 |
| Cloud Run, mínimo 2 | `5,45 + (2×730×3600−100.000)×(2+1)×0,0000025` | 44,12 | **335,68** | 4.028,11 |
| Dos VM E2, discos incluidos | `2×730×0,06701142 + 2×20×730×0,000136986` | 101,84 | **393,39** | 4.720,71 |

Los cálculos son **USD netos referenciales** para un mes repetido doce veces, sin IVA chileno, tipo de cambio, aumento de carga o ajuste anual. A USD/CLP 1.000 **supuesto**, los USD 297,01 equivaldrían a CLP 297.006/mes antes de la provisión regional; no son un precio Santiago. La diferencia Cloud Run mínimo cero frente a dos VM es USD 96,39/mes en este escenario, pero depende de los 200.000 vCPU-s imputados. El umbral simple de la capa de aplicación, manteniendo memoria y solicitudes constantes, sería `(101,84−0,25−0,40)/0,000024 ≈ 4,22 millones de vCPU-s/mes`; antes de ese punto podrían cambiar concurrencia, autoescalado y tamaño de VM, por lo que **no** es una frontera comercial definitiva.

## Conciliación con el presupuesto actual y decisión pendiente

El perfil `piloto` de [supuestos_bootstrap.json](supuestos_bootstrap.json) usa Cloud SQL **no HA** y Cloud Run mínimo cero: USD **192,43/mes de Iowa** con las mismas bolsas y egress provisional, antes del factor regional 1,35. Este ejercicio de continuidad sustituye en *ambas* alternativas la base SQL por HA y agrega, en VM, dos discos: USD 297,01 frente a USD 393,39. No se deben comparar los USD 192,43 de disponibilidad menor con la VM de dos zonas para afirmar ahorro. Tampoco se debe cambiar ahora el VAN del Anexo A sin conciliar perfil, impuestos, fecha de operación y capacidad financiera del equipo.

**Inferencia técnica, no selección aprobada:** con la carga supuesta, Cloud Run favorece bajo consumo y reduce operación de VM; la base HA, red y seguridad concentran cerca de todo el gasto. Si el objetivo de ES2 admite una sola zona de base de datos durante el piloto, el presupuesto vigente es una hipótesis distinta y más barata, pero con mayor exposición a falla zonal. Mantener una o dos instancias mínimas en Cloud Run mejora la disponibilidad inmediata percibida y eleva costo; necesita medir arranque en frío y tráfico real. El SLA publicado de [Cloud Run](https://cloud.google.com/run/sla) es un compromiso del proveedor para ese servicio, no un SLA extremo a extremo de EspaciGo.

[[PENDIENTE: obtener cotización real de `southamerica-west1` para CPU/RAM/SSD/backup/Storage/LB/Armor/red, facturación en CLP e IVA; decidir residencia de datos y transfronterizos con la matriz de privacidad; perfilar solicitudes, duración, concurrencia, bytes, almacenamiento y picos por categoría; probar rendimiento y failover de Cloud Run/VM y Cloud SQL; presupuestar operación humana, NAT/IP, logs, snapshots y staging reales; entonces actualizar `supuestos_bootstrap.json`, simular de nuevo y conciliar el Anexo A.]]
