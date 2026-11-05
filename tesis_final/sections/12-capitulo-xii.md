# CAPÍTULO XII: Plan de Pruebas y Aseguramiento de Calidad

## 12. Plan de Pruebas y Aseguramiento de Calidad

### 12.1. Plan de Pruebas

El modelo de calidad de producto orienta la selección de características verificables [@iso25010]. El plan organiza las pruebas en niveles de dominio, integración, recorrido de usuario y operación. El Anexo F conserva el diseño de pruebas y distingue el resultado esperado del resultado observado. Cada registro identifica versión, entorno, datos, procedimiento, resultado y límite.

**Tabla 12**\
*Resultados documentados por corte de verificación*

| Corte | Resultado registrado | Alcance de la evidencia |
|---|---|---|
| LOCAL-1 | La matriz de cierre registra la aceptación del recorrido sintético y la comprobación posterior a la integración de V53 y V54. | Búsqueda, reserva, cobros simulados y controles del alcance local. |
| Verificación documental F5 | El registro del 4 de noviembre documenta 86 pruebas de primer nivel aprobadas, sin fallas ni omisiones en el paquete documental. Backend `8d33dcf`. | Ensayo local sobre V83 con cambios del corte. Incluye las comprobaciones documentadas de escaneo, revocación, retención y permisos dentro del paquete. La Tabla F.3 identifica su relación parcial con PT-07 y PT-16. |
| Recorrido F6 | El cierre técnico registra 2 pruebas aprobadas de borrador y 4 del perfil documental, sin fallas ni omisiones en esos perfiles. Frontend `cc2fdc3`. | Ensayo sintético de borrador y del perfil documental. El segundo incluye navegador, BFF, API, base, almacenamiento y escáner dentro del recorrido descrito en la evidencia. La evidencia corresponde a ramas de ensayo y se conserva separada de la aceptación visual y del despliegue en nube. |
| Reputación local | Dos pruebas PostgreSQL pasan en una copia desechable con el banco preparado para los cortes V37 y V80. | Reciprocidad, moderación, retención y permisos de su alcance. La preparación adaptada no certifica la suite original ni el esquema actual completo. |
| Carga SQL local | 200 conexiones durante 15 s sobre 10.000 puntos sintéticos. 42.636 consultas completadas, cero fallos y latencia media de 70,222 ms. | Consulta PostGIS aislada en PostgreSQL 18.6. La medición excluye navegador, API y red del entorno objetivo. |

*Nota.* Elaboración propia a partir de la matriz de cierre LOCAL-1 y la evidencia técnica F5/F6 del repositorio de desarrollo, registrada en el [cierre técnico del repositorio de desarrollo](https://github.com/HernanEspinozaDev/espaciGo/blob/93b59c8352960d900b4e62bb42bced9e05dcad8c/planning/frontend_next/evidence/f5-f6-recovered-live-20261104.md), y a partir de los ensayos locales documentados en el registro de verificación. La Tabla F.3 relaciona los resultados con su alcance.

#### 12.1.1. Ensayo local de restauración

El ensayo sintético de PostgreSQL/PostGIS sobre migraciones V1–V61 supera las comprobaciones de restauración de base y solapamiento concurrente. El ensayo independiente del ejecutor GCP03 en PostgreSQL desechable se detiene al restaurar los permisos de aplicación. La restauración conjunta de base y objetos, la carga de extremo a extremo y la medición de RPO y RTO permanecen como verificaciones separadas.

El recorrido de aceptación comprende oferta por titularidad, búsqueda, contrato sin firma, pago simulado y cierre. Los casos PT-01 a PT-08 y PT-12 del Anexo F contrastan ese recorrido con fallos de autorización, concurrencia, expiración y procesamiento de eventos. PT-08 comprueba el ingreso, la entrega y la confirmación de desocupación de HU35. La matriz distingue el criterio de cada etapa de su estado de ejecución. La firma opcional y la garantía requieren escenarios de aceptación por proveedor, pagador y emisión.

Los objetivos de rendimiento y continuidad se definen en el Capítulo XI. La comprobación de capacidad, latencia, seguridad y recuperación requiere el código del flujo correspondiente listo para probar y registros reproducibles del entorno evaluado. La Tabla F.4 enumera las pruebas pendientes de ese cierre. Los resultados locales tampoco acreditan cobertura de todas las categorías objetivo. El ensayo de recuperación mide RPO y RTO y verifica permisos y referencias entre la base y los archivos privados.

### 12.2. Normas y Estándares

El modelo de calidad se organiza según ISO/IEC 25010 [@iso25010]. Los criterios de aceptación remiten a los requerimientos funcionales y no funcionales y a los registros reproducibles del Anexo F.
