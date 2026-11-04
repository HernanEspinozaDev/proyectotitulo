# CAPÍTULO X: ASEGURAMIENTO DE CALIDAD Y PRUEBAS DEL SOFTWARE

## 10.1. Estrategia y criterios de verificación

El modelo de calidad de producto orienta la selección de características verificables [@iso25010]. El plan organiza las pruebas en niveles de dominio, integración, recorrido de usuario y operación. El Anexo F conserva el diseño de pruebas y distingue el resultado esperado del resultado observado. Cada registro identifica versión, entorno, datos, procedimiento, resultado y límite.

## 10.2. Evidencia de los incrementos

**Tabla 10**  
*Resultados documentados por corte de verificación*

| Corte | Resultado registrado | Alcance de la evidencia |
|---|---|---|
| LOCAL-1 | La matriz de cierre registra la aceptación del recorrido sintético y la comprobación posterior a la integración de V53 y V54. | Búsqueda, reserva, cobros simulados y controles del alcance local. |
| Verificación documental F5 | El registro del 4 de noviembre documenta 86 pruebas de primer nivel aprobadas, sin fallas ni omisiones en el paquete documental. Backend `8d33dcf`. | Ensayo local sobre V83 con cambios del corte. Incluye escaneo, revocación, retención y permisos. |
| Recorrido F6 | El cierre técnico registra 2 pruebas aprobadas de borrador y 4 del perfil documental, sin fallas ni omisiones en esos perfiles. Frontend `cc2fdc3`. | Ensayo sintético de navegador, BFF, API, base, almacenamiento y escáner. La evidencia corresponde a ramas de ensayo y se conserva separada de la aceptación visual y del despliegue en nube. |
| Reputación local | Dos pruebas PostgreSQL pasan en una copia desechable con el banco preparado para los cortes V37 y V80. | Reciprocidad, moderación, retención y permisos de su alcance. La preparación adaptada no certifica la suite original ni el esquema actual completo. |
| Carga SQL local | 200 conexiones durante 15 s sobre 10.000 puntos sintéticos. 42.636 consultas completadas, cero fallos y latencia media de 70,222 ms. | Consulta PostGIS aislada en PostgreSQL 18.6. La medición excluye navegador, API y red del entorno objetivo. |

*Nota.* Elaboración propia a partir de la matriz de cierre LOCAL-1 y la evidencia técnica F5/F6 del repositorio de desarrollo, registrada en el commit documental `93b59c8`, y a partir de los ensayos locales documentados en el registro de verificación. La Tabla F.3 relaciona los resultados con su alcance.

### Ensayo local de restauración

El ensayo sintético de PostgreSQL/PostGIS sobre migraciones V1–V61 supera las comprobaciones de restauración de base y solapamiento concurrente. El ensayo independiente del ejecutor GCP03 en PostgreSQL desechable se detiene al restaurar los permisos de aplicación. La restauración conjunta de base y objetos, la carga de extremo a extremo y la medición de RPO y RTO permanecen como verificaciones separadas.

## 10.3. Pruebas de aceptación del flujo objetivo

El primer recorrido de aceptación cubre oferta por titularidad, búsqueda, contrato sin firma, pago simulado y cierre. Los casos PT-01 a PT-08 y PT-12 del Anexo F identifican las comprobaciones principales. La verificación incluye tercero no autorizado, intervalos concurrentes, expiración atómica, evento duplicado y pago tardío. La firma opcional y la garantía requieren escenarios de aceptación por proveedor, pagador y emisión.

## 10.4. Rendimiento, seguridad y recuperación

Los objetivos de rendimiento y continuidad se definen en el Capítulo VII. La comprobación de capacidad, latencia, seguridad y recuperación requiere registros reproducibles del entorno evaluado. El ensayo de recuperación mide RPO y RTO y verifica permisos y referencias entre la base y los archivos privados.
