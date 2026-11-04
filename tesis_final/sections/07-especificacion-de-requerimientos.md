# CAPÍTULO VII: ESPECIFICACIÓN DE REQUERIMIENTOS Y NIVELES DE SERVICIO

## 7.1. Identificación de Actores y Módulos del Sistema

La especificación de requerimientos de la plataforma **espaciGo** se articula en torno a la interacción de roles de arrendamiento definidos por operación, capacidades de administración e integraciones externas:

La Figura 6 sintetiza los papeles de la cuenta y la administración.

**Figura 6**  
*Diagrama de Interacción entre Actores y Módulos de la Plataforma*

![](assets/figuras/anexo_c/cu_actores.png)

*Nota.* Elaboración propia en base a la arquitectura modular de la plataforma espaciGo.

---

## 7.2. Síntesis Ejecutiva de Requerimientos Funcionales (IEEE 830)

El Anexo A utiliza el prefijo `RQF` como identificador canónico. La agrupación del catálogo sigue los módulos M01 a M11 de los casos de uso. El flujo transaccional reúne oferta y titularidad (M04), descubrimiento (M05), reserva y cobros (M06), contratación (M07), entrega (M08) y resolución de disputas (M10). Los anexos B, C y F documentan historias, casos de uso y pruebas por corte.

**Tabla 7**\
*Trazabilidad inicial del recorrido objetivo*

| Comportamiento | Requisitos | Historia o caso |
|---|---|---|
| Publicación por titularidad | RQF-082 | HU05 y CU-15 |
| Control de intervalos y bloqueo | RQF-110 a RQF-113 | HU18, CU-22 y CU-23 |
| Emisión, aceptación y firma opcional | RQF-130 a RQF-133 | HU33, CU-29 y CU-30 |
| Acreditación de renta y garantía separada | RQF-116 a RQF-120 | HU17, CU-24 y CU-25 |
| Entrega y desocupación | RQF-150, RQF-152, RQF-205 y RQF-206 | HU35, CU-34 y CU-48 |

*Nota.* Elaboración propia. Los anexos A, B y C detallan los requisitos, historias y casos. La Tabla F.1 del Anexo F documenta los criterios de prueba. La aceptación por parte se desarrolla en HU33 y CU-29.

## 7.3. Requerimientos no funcionales

El Anexo A registra los requisitos de calidad y su alcance. La Tabla 8 reúne criterios de verificación del entorno objetivo. El Capítulo X identifica las ejecuciones documentadas.

**Tabla 8**\
*Criterios de calidad y verificación*

| Requisito | Criterio objetivo | Evidencia exigida |
|---|---|---|
| RNF-001 | Respuesta de búsqueda en hasta 2 segundos bajo 200 usuarios concurrentes. | Escenario, intervalo, volumen y tiempos observados. |
| RNF-009 | Disponibilidad mensual mínima de 99,9 % para funciones críticas. | Ventana de observación y registro de disponibilidad. |
| RNF-010 | RPO máximo de 15 minutos y RTO máximo de 1 hora. | Ensayo de restauración y comprobación del estado recuperado. |
| RNF-015 | HTTPS con TLS 1.2 o superior para credenciales y datos sensibles. | Comprobación del canal en el entorno evaluado. |
| RNF-021 | Cobertura mínima de 80 % para pruebas unitarias de la capa de negocio. | Reporte de cobertura por versión y alcance. |

*Nota.* Elaboración propia con base en el Anexo A. Los umbrales corresponden a criterios objetivo. La Tabla F.2 identifica PT-09 para búsqueda, PT-11 para recuperación y PT-14 para revisión de seguridad.

## 7.4. Indicadores de operación

La evaluación comercial puede medir conversión de búsqueda a reserva, tiempo entre publicación y primera reserva, proporción de incidencias resueltas y satisfacción posterior al arriendo. Cada medición define población, período y denominador antes de asignar metas.

La evaluación técnica registra volumen de solicitudes, latencia P95 por operación, errores de integración y cobertura. El reporte diferencia pruebas sintéticas, observación de un entorno de ensayo y medición de operación.
