## Diagrama de infraestructura

La infraestructura siguiente es un **diseño propuesto**, coherente con la alternativa Cloud Run de ES1 y con dos artefactos de contenedor descritos en 3.3. Cloud Run ejecuta servicios sobre infraestructura administrada, pero el equipo todavía debe elegir región, recursos, política de escalado, red y servicios de datos. No existe evidencia de despliegue de EspaciGo [@es1formulacion; @es2cloudrunoverview].

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

Los objetivos de **99,9 % mensual**, **RPO máximo de 4 horas** y **RTO máximo de 6 horas** proceden de RNF-009/010 de ES1. El diagrama no demuestra esos resultados: requieren arquitectura de respaldo, ventanas de medición, restauración ensayada y registro de incidentes. Asimismo, RNF-019 y RNF-030 fijan escalado y capacidad por verificar; sin escenarios de carga y costos no corresponde escoger CPU, memoria ni número de instancias [@es1anexoc].

Se propone separar desarrollo, ensayo y entrega final por configuración y credenciales, con datos sintéticos en las pruebas. RNF-034–036 exige portabilidad; adoptar servicios específicos de GCP requiere documentar interfaces sustituidas y comprobar la reproducción local y otro proveedor. La comparación económica de 2.1 debe incluir cómputo, base, archivos, red, registros, copias y terceros [@es1anexoc; @es2cloudrunpricing].

[[PENDIENTE: acordar proveedor y servicios de datos, inventariar hardware, estimar tráfico/almacenamiento, calcular costo fechado y probar despliegue, escalado, respaldo y recuperación.]]
