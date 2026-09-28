## Plan de pruebas

El plan verifica el diseño de los capítulos III y IV frente a RF, RNF, CU y criterios de aceptación de ES1. Los casos detallados se encuentran en el **Anexo C de ES2**. Todos tienen estado **planificado**: no hay resultados del producto ni acceso acreditado a las integraciones externas. Una prueba del generador de informes no demuestra funcionamiento de EspaciGo.

### Alcance, niveles y entornos

Se priorizan las reglas que pueden producir una reserva doble, un cargo duplicado, una firma incompleta o una liquidación improcedente. Las pruebas **unitarias** ejercitarán reglas puras de fechas, estados e importes; las **integrales** comprobarán API, PostgreSQL y adaptadores; las de **humo** recorrerán un camino mínimo después de desplegar. Las de **carga y estrés** medirán latencia, capacidad, saturación y recuperación. Las pruebas **alfa** se realizarán con el equipo en entorno controlado; las **beta** requerirán usuarios y alcance autorizados; la aceptación contrastará requisitos y evidencia con el responsable designado. El despliegue y los participantes de estas etapas todavía no están definidos.

Se prevén tres entornos separados: pruebas locales automatizadas con base temporal y reloj controlable; ensayo con servicios configurados y datos sintéticos; y, cuando haya autorización, sandbox de proveedores reales. El simulador de pago o firma verifica lógica local y nunca se informará como integración productiva. Versiones, herramientas, semillas de datos, permisos y recursos de cada entorno se registrarán antes de ejecutar. Los secretos y datos personales no se adjuntarán a los reportes.

**Entrada a una ejecución:** requisito y resultado esperado confirmados, versión del código y del esquema identificada, datos de prueba disponibles, entorno reproducible y permisos necesarios. **Salida:** se conserva resultado, fecha, ejecutor, logs o capturas, defectos y nueva ejecución cuando se corrijan. Para aceptar el flujo crítico deben pasar todos los casos prioritarios aplicables sin defectos abiertos que permitan doble reserva, cargo duplicado, acceso indebido o liquidación durante disputa. Los umbrales de cobertura y rendimiento proceden de RNF-021, RNF-001 y RNF-030 y se informarán con su entorno, sin declarar cumplimiento mediante una sola captura.

*Tabla. Catálogo planificado y trazabilidad principal; pasos y oráculos en el Anexo C.* <!--#tab:es2-pruebas-catalogo-->

| Caso | Tipo | Regla principal | Resultado que se comprobará |
| --- | --- | --- | --- |
| PT-01 | Unitaria | RQF-108–112, CU-22/23 | Fechas inválidas y solapadas se rechazan; límites adyacentes se tratan según la regla aprobada |
| PT-02 | Integral y concurrencia | RQF-111/112, RNF-030 | Dos solicitudes simultáneas no confirman intervalos incompatibles |
| PT-03 | Integral y tiempo | RQF-120, CU-27 | Vencimiento de 15 minutos sin convertir respuesta financiera incierta en rechazo |
| PT-04 | Integral y fallos | RNF-012/024/028 | Reintentos y webhooks repetidos no producen doble operación |
| PT-05 | Integral y tiempo | RQF-123–129, CU-26/28 | Vencimiento de 24 horas y tratamiento coherente del reembolso |
| PT-06 | Integral | RQF-130–142, CU-29–32 | No se habilita ingreso sin todas las firmas |
| PT-07 | Seguridad funcional | RQF-166–171, CU-41 | Solo quien tenga permiso puede resolver una disputa |
| PT-08 | Integral | RQF-159–177, CU-39–42 | Reclamo abierto bloquea liquidación y permite cierre tras resolución |
| PT-09 | Carga | RNF-001 | Búsqueda ≤ 2 s bajo 200 usuarios concurrentes en el escenario definido |
| PT-10 | Capacidad y estrés | RNF-030/019 | 500 usuarios, 100 escrituras/s y degradación medidos sin pérdida de integridad |
| PT-11 | Recuperación | RNF-010 | RPO ≤ 4 h y RTO ≤ 6 h con restauración efectiva |
| PT-12 | Rendimiento | RNF-003 | PDF de contrato en ≤ 10 s y tamaño < 2 MB |
| PT-13 | Humo | CU-01/22/24/29/30/33 | Camino básico recorre etapas habilitadas en el entorno disponible |
| PT-14 | Alfa y aceptación interna | HU y criterios del alcance acordado | El equipo registra defectos y conformidad por criterio verificable |
| PT-15 | Beta y aceptación externa | HU y criterios del alcance autorizado | Usuarios autorizados validan tareas reales con evidencia y consentimiento |
| PT-16 | Privacidad e integración | RQF-034–037, RNF-018/026/029/042/043 | Solicitudes de derechos, acceso y cierre de cuenta respetan la matriz de tratamiento aprobada |

El catálogo distingue **resultado esperado** de **resultado observado**. PT-16 traduce desde ahora la Ley 21.719 en verificaciones del desarrollo, aunque su entrada en vigencia sea posterior a ES2; requiere aprobar primero las reglas de tratamiento y retención del Anexo B [@ley21719]. No se calcularán porcentajes de aprobación, cobertura o cumplimiento SLA hasta ejecutar pruebas con código y conservar reportes. Los casos sobre proveedor real y beta quedan condicionados a acceso y participantes autorizados.

### Herramientas y Entornos de Prueba

Para la ejecución de este catálogo se han definido los siguientes entornos y responsables:
- **Automatización CI:** Las pruebas unitarias e integrales menores (PT-01, PT-04, PT-05) se ejecutarán mediante **GitHub Actions** en cada solicitud de cambio.
- **Entorno de Staging en GCP:** Se dispondrá de un entorno réplica en Google Cloud para la ejecución de pruebas de humo (PT-13), pruebas de privacidad (PT-16) y pruebas concurrentes (PT-02).
- **Carga y Estrés:** Las pruebas de rendimiento (PT-09, PT-10) utilizarán **k6** inyectando tráfico al entorno de staging, registrando latencia bajo 200 y 500 usuarios concurrentes.

El responsable de calidad del equipo será el encargado de revisar los casos de la rúbrica, enlazar la evidencia fechada (reportes de GitHub Actions y k6) y registrar los defectos identificados en el rastreador de incidentes del proyecto.
