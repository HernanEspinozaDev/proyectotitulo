## Diagrama de infraestructura

La infraestructura siguiente es un **diseño propuesto**, coherente con la alternativa Cloud Run de ES1 y con dos artefactos de contenedor descritos en 3.3. Cloud Run ejecuta servicios sobre infraestructura administrada, pero el equipo todavía debe elegir región, recursos, política de escalado, red y servicios de datos. No existe evidencia de despliegue de EspaciGo [@es2cloudrunoverview].

![Infraestructura virtual propuesta para EspaciGo](imagenes/figura-infraestructura_propuesta.png){width=6.3in} <!--#fig:es2-infraestructura--> <!--#fuente:elaboración propia a partir de la propuesta de ES1.-->

*Tabla. Recursos de diseño y evidencia para dimensionarlos.* <!--#tab:es2-recursos-infra-->

| Recurso | Función prevista | Decisión o evidencia pendiente |
| --- | --- | --- |
| Dispositivos del equipo y usuarios | Desarrollo y uso web | Inventario real de CPU, RAM, sistema operativo, conexión y navegadores; soporte de RNF-007/022 |
| Entrada HTTPS y dos servicios de contenedor | Acceso público, presentación y API modular | Dominio, certificados, región, CPU/RAM, límites, concurrencia, instancias mínimas/máximas y prueba de carga |
| PostgreSQL con PostGIS | Transacciones, calendario y geodatos exigidos por RNF-038 | Servicio y versión, capacidad, acceso privado, índices, respaldos y prueba de recuperación |
| Almacenamiento de archivos | Imágenes, contratos y evidencias | Servicio, volumen, cifrado, permisos, ciclo de vida y costo |
| Analítica y registros de auditoría | Consulta y conservación de eventos | Destino analítico, protección efectiva contra modificación de RNF-017, retención y costo |
| Adaptadores y ejecución de conciliación | Integraciones y revisión periódica RNF-028 | Mecanismo de ejecución, acceso autorizado, colas o agenda si se requieren, observabilidad y tratamiento de fallos |

Los objetivos de **99,9 % mensual**, **RPO máximo de 4 horas** y **RTO máximo de 6 horas** proceden de RNF-009/010 de ES1. El diagrama no demuestra esos resultados: requieren arquitectura de respaldo, ventanas de medición, restauración ensayada y registro de incidentes. Asimismo, RNF-019 y RNF-030 fijan escalado y capacidad por verificar; sin escenarios de carga y costos no corresponde escoger CPU, memoria ni número de instancias.

Se propone separar desarrollo, ensayo y entrega final por configuración y credenciales, con datos sintéticos en las pruebas. RNF-034–036 exige portabilidad; adoptar servicios específicos de GCP requiere documentar interfaces sustituidas y comprobar la reproducción local y otro proveedor. La comparación económica de 2.1 debe incluir cómputo, base, archivos, red, registros, copias y terceros [@es2cloudrunpricing].

### Perfil presupuestario propuesto

El Anexo A asigna cantidades para estimar caja sin declarar la infraestructura implementada. En el piloto se simulan SQL Enterprise General Purpose con 2 vCPU/8 GiB durante 730 horas, 20 GiB SSD y 20 GiB de copias; dos servicios Cloud Run suman un millón de solicitudes, 50 GiB de objetos y 100 GiB de salida mensual. Se agregan balanceador, cinco reglas WAF, logs, compilación, secretos, correo y una bolsa acotada para staging. El SQL zonal no es HA ni demuestra RNF-009/010 [@es2cloudsqlpricing; @es2cloudrunpricing].

*Tabla. Escenarios de costo mensual de infraestructura en tarifas de Santiago.* <!--#tab:es2-infra-costos-->

| Entorno simulado | Tarifas de Santiago, USD | Presupuesto neto CLP | Necesidad de caja CLP con IVA supuesto |
| --- | ---: | ---: | ---: |
| Ensayo restringido | 24,65 | 24.650 | 29.334 |
| Piloto público | 237,82 | 237.819 | 283.005 |
| HA de referencia | 494,65 | 494.648 | 588.632 |

**Nota.** Elaboración propia: conversión supuesta de 1.000 CLP/USD sobre las tarifas públicas usadas para `southamerica-west1`, **sin provisión regional**. Cada tarifa y cantidad requiere auditoría por SKU. El 19 % adicional es reserva de caja, cuya facturación y crédito fiscal deben verificarse. Cada mes usa un perfil; no se suman las tres filas. La fila HA y el comparador documental son configuraciones distintas de carga, almacenamiento y respaldos; ninguna demuestra una capacidad operativa contratada [@es2gcspricing; @es2lbpricing; @es2armorpricing].

La decisión del usuario del 23-09-2026 fija **Santiago** como región de operación. El ejercicio comparativo propio conserva precios de Iowa como control documental de la comparación entre Cloud Run y máquinas virtuales, no como presupuesto vigente [@es2cloudrunpricing].

Durante el primer año sin ventas se estiman seis meses de ensayo y seis de piloto, con **1.874.031 CLP de salida cloud** bajo el IVA supuesto. Se requiere confirmar los servicios de datos administrados, levantar el inventario físico y ejecutar las pruebas de carga y restauración en la región decidida; el diferencial frente a Compute Engine también debe incorporar operación, respaldo y seguridad comparables.

### Dimensionamiento propuesto

*Tabla. Perfiles de recursos y su justificación.* <!--#tab:es2-dimensionamiento-->

| Perfil | Ejecución | Datos y archivos | Supuesto que lo respalda | Estado |
| --- | --- | --- | --- | --- |
| Ensayo | Web y API con mínimo 0 instancias y una tarea de conciliación | PostgreSQL zonal y 20 GiB de objetos | Tráfico interno y datos sintéticos | Propuesta; sin desplegar |
| Piloto | Web y API con concurrencia limitada y mínimo 0 o 1 | PostgreSQL de 2 vCPU y 8 GiB con 20 GiB de SSD y 20 GiB de respaldos; 50 GiB de objetos; un millón de solicitudes mensuales | Perfil presupuestario del Anexo A | Propuesta; capacidad por medir |
| Alta disponibilidad | Servicios con instancias mínimas y base con conmutación | Base HA con respaldos continuos | RNF-009/010 | Escenario comparativo; no es un diseño probado |

El dimensionamiento no se deduce de los objetivos. RNF-001 exige 200 usuarios concurrentes con búsqueda bajo 2 segundos y RNF-030 fija 500 usuarios concurrentes y 100 escrituras por segundo: solo una prueba de carga puede contrastar esas cifras. Hasta entonces, CPU, memoria, instancias mínimas y tamaño de base son **parámetros de escenario**, no capacidades contratadas. PT-09 y PT-10 describen esos ensayos.

Las tarifas públicas usadas para **Santiago** se aplicaron como **supuestos del presupuesto vigente**; falta cotejar SKU, volúmenes y condiciones de facturación. Con Cloud SQL HA, 20 GiB de SSD, 20 GiB de respaldo, 50 GiB de objetos y Cloud Run con mínimo 0, el comparador aritmético alcanza USD 384,23 al mes frente a USD 297,01 de una configuración comparable en Iowa. El piloto de la tabla cuesta USD 237,82 porque usa SQL zonal; la fila HA de USD 494,65 tiene otra carga y mayores cantidades de almacenamiento y respaldo, por lo que no es directamente comparable. El presupuesto dejó de usar la provisión regional del 35 %; su efecto está cuantificado en el Anexo A. La conversión a CLP conserva el supuesto de 1.000 CLP/USD y el tratamiento de IVA sigue sin verificar con comprobantes. El inventario físico del equipo —CPU, memoria, sistema operativo, conexión y navegadores de trabajo— todavía no se ha levantado.

[[PENDIENTE: confirmar los servicios de datos administrados y el inventario físico del equipo, y probar despliegue, escalado, respaldo y recuperación con evidencia fechada en la región decidida.]]
