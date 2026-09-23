## Herramientas, aplicaciones, lenguajes y componentes que serán implementados

El inventario inicial deriva de la arquitectura de ES1 y del contraste documental de esta entrega. Las herramientas se presentan como componentes previstos; su inclusión no acredita instalación, despliegue ni integración del producto [@es1formulacion].

*Tabla. Inventario inicial de componentes previstos para EspaciGo.* <!--#tab:es2-inventario-tecnologico-->

| Componente | Función prevista | Alcance | Verificación pendiente |
| --- | --- | --- | --- |
| Next.js sobre React | Interfaz del catálogo y flujos de usuario | M01–M11 según interfaz | Versión, dependencias y prueba de interfaz |
| Go | API y reglas de negocio del backend modular | M01–M11 | Versión, estructura y pruebas del flujo seleccionado |
| PostgreSQL y PostGIS | Datos operativos y consulta geográfica | Reservas, publicaciones y relaciones transaccionales | Versión, alojamiento, esquema e índices |
| Docker | Construcción de imágenes para los componentes desplegables | Desarrollo y despliegue | Imágenes base, versiones y configuración |
| Cloud Run | Ejecución prevista de frontend y API | Infraestructura | Región, recursos, red y costo |
| BigQuery | Análisis y consulta de eventos previstos en ES1 | Auditoría M11 | Diseño que satisfaga RNF-017; no atribuir inmutabilidad automática |
| Almacenamiento de archivos | Contratos e imágenes de evidencia | M04, M07 y M08 | Servicio, acceso, cifrado, retención y costo |
| Mercado Pago | Procesamiento de pagos propuesto | M06 y M10 | Producto, acceso y compatibilidad del flujo financiero |
| FirmaVirtual | Servicio de firma propuesto | M07 | Modalidad, API y entorno de prueba |
| Registro Civil y SII | Verificación de identidad/empresa y servicios tributarios previstos | M03 y M10 según servicio | Acceso autorizado y capacidades de cada servicio |

**Nota.** Elaboración propia basada en ES1. Las integraciones externas permanecen sin verificación de acceso. La atribución de una función refleja la propuesta del proyecto, no una garantía del proveedor.

Docker distingue la imagen de su instancia en ejecución y advierte que los cambios sin almacenamiento persistente se pierden al eliminar el contenedor. En el diseño de EspaciGo se propone mantener la persistencia de datos y archivos separada del ciclo de vida de los contenedores y documentar la configuración de cada entorno [@es2dockeroverview].

La selección de hardware deberá contemplar las estaciones reales del equipo y los recursos de ejecución del prototipo: sistema operativo, CPU, memoria, almacenamiento y conectividad. Todavía no se dispone de ese inventario ni de mediciones para dimensionar la nube. Tampoco se fijan versiones a partir de la fecha de consulta de la documentación: se registrarán las efectivamente seleccionadas y probadas.

Para cada componente se completará una ficha con versión, licencia o términos de servicio, entorno, responsable, dependencia, costo y evidencia. Los servicios de integración requerirán además registrar la diferencia entre funcionamiento real y simulación de pruebas. Los secretos de acceso se gestionarán fuera del informe.

[[PENDIENTE: completar fichas de versiones y licencias, hardware disponible, herramientas de desarrollo/pruebas/CI, alojamiento de PostgreSQL y almacenamiento; resolver las preguntas de acceso de INV-003.]]
