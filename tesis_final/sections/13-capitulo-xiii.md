# CAPÍTULO XIII: Plan de Implementación

## 13. Plan de Implementación

### 13.1. Gestión de Disponibilidad

La configuración de infraestructura de la plataforma declara controles de construcción y calidad mediante GitHub Actions y módulos Terraform para red, RDS, S3, IAM, SSM y logs [@espacigoaws2026]. La entrega objetivo publica imágenes en ECR y actualiza una tarea ECS Fargate con autenticación temporal OIDC. La configuración inspeccionada requiere completar recursos ECS/ECR, permisos de entrega e inyección segura de secretos. El procedimiento registra revisión de aplicación, digest de imágenes, región, versión del esquema y resultado de aceptación.

El diseño establece mínimo privilegio para aplicación, migraciones y operación. Como criterio de diseño, cada solicitud debe verificar el vínculo del actor con el recurso y las capacidades exigidas por la acción. La evidencia privada utiliza almacenamiento separado, y su acceso y retención dependen de su finalidad. Las revisiones documentales incluyen pruebas de denegación y comprobación de permisos efectivos.

### 13.2. Gestión de Continuidad

El procedimiento objetivo recupera RDS PostgreSQL mediante respaldo o PITR y selecciona las versiones compatibles de los objetos privados en S3 dentro de la región habilitada. La restauración se realiza en un entorno aislado. La aceptación exige comprobar referencias, permisos y acciones de supresión que el respaldo antecede. La medición compara el punto recuperado y el tiempo de recuperación con el RNF-010. El operador registra las divergencias y conserva aislado el destino cuando falla una comprobación.

La Figura 18 resume el ensayo objetivo de restauración. La comprobación de permisos es una condición de reapertura del servicio, porque la recuperación de los datos por sí sola no acredita que se conserva su control de acceso. La Tabla F.3 conserva la falla histórica observada en esa etapa. El ensayo AWS requiere su propio resultado.

**Figura 18**\
*Actividad objetivo de restauración y verificación*

![](assets/imagenes/fig17_recuperacion_aws.png){height=13cm}

*Nota.* Elaboración propia. El flujo describe el ensayo objetivo de recuperación conjunta de RDS y S3, con verificación de permisos y supresiones.

### 13.3. Plan de Mantención

El diseño de operación incluye guías para continuidad, incidentes y mantenimiento. Antes de ejecutar un procedimiento, el operador confirma destino, permisos, configuración y versión. El objetivo general de recuperación corresponde al RNF-010.

**Tabla 13**\
*Procedimientos operativos y criterio de comprobación*

| Código | Contingencia | Criterio de comprobación |
|---|---|---|
| RB-01 | Indisponibilidad de base de datos | Verificar restauración o conmutación, consistencia de datos y salud de aplicación. Medir RPO y RTO. |
| RB-02 | Indisponibilidad de pagos | Suspender nuevos cobros cuando proceda y conciliar eventos tardíos. Mantener el vencimiento original del bloqueo. |
| RB-03 | Incidente de seguridad | Contener, revocar accesos afectados, conservar evidencia y activar el procedimiento de comunicación aplicable. |
| RB-04 | Regresión de despliegue | Restablecer una revisión compatible con el esquema y ejecutar pruebas de humo. |
| RB-05 | Degradación de índices | Identificar el índice afectado, evaluar reconstrucción y medir la consulta crítica. |
| RB-06 | Indisponibilidad DNS | Confirmar la causa y validar resolución y propagación después de una intervención autorizada. |

*Nota.* Elaboración propia a partir del diseño operativo de espaciGo. PT-11 del Anexo F define el criterio de verificación de RB-01. La recuperación conjunta y los tiempos objetivo quedan pendientes de ensayo. RB-02 se vincula con PT-04 y PT-05. RB-03 aporta el contexto operativo de PT-14 y PT-16. Estas remisiones cubren comprobaciones parciales. RB-04, RB-05 y RB-06 quedan como procedimientos objetivo pendientes de ensayo específico.

El plan prevé revisión por incremento de dependencias, permisos y procedimientos. El responsable del componente registra la intervención y sus verificaciones. Los incidentes y cambios de esquema activan los controles específicos de la tabla operativa.

### 13.4. Condiciones de habilitación de integraciones

La habilitación de proveedores queda pendiente hasta que esté listo el código del flujo y se ejecuten sus pruebas. **Mercado Pago** es el proveedor previsto para renta y comisión mediante Checkout Pro, OAuth del vendedor y Split 1:1 [@es2mpsplit]. Su aceptación requiere comprobar acreditación, conciliación y reembolso. **SimpleFirma** es el proveedor previsto para la modalidad de firma opcional. Su aceptación requiere evidencia por emisión y firmante y comprobación de facturación y reversos. La garantía monetaria conserva su habilitación pendiente. El mecanismo y el responsable de fondos se confirman mediante pruebas de cobro, reclamos y devoluciones. La verificación externa de identidad y representación, cuando corresponda, se registra como integración pendiente de definición y validación.

La política de retención identifica finalidad, evento inicial, excepción, responsable y acción sobre datos y objetos. El ensayo de continuidad verifica que la restauración respeta esas decisiones y los permisos de acceso.

### 13.5. Secuencia de habilitación de la infraestructura AWS

1. Confirmar la región seleccionada del proyecto y la disponibilidad de Fargate, RDS PostgreSQL, sus extensiones y los servicios de soporte.
2. Revisar Terraform, sustituir marcadores de secretos, restringir ingreso y comprobar la política de acceso a S3 y parámetros. Conciliar la versión del motor declarada con la versión validada.
3. Completar las definiciones de tarea y servicio ECS, imágenes ECR, roles y entrega OIDC. Validar endpoints regionales y credenciales temporales del adaptador S3.
4. Configurar el borde Cloudflare, TLS hacia el origen, acceso de evaluadores y actualización del origen cuando cambia la tarea. Comprobar que la API y la base conservan sus límites de acceso.
5. Aplicar y verificar migraciones, datos y objetos en un entorno de aceptación. Ejecutar pruebas funcionales, denegación, carga y recuperación con registros de versión y entorno.
6. Habilitar el servicio cuando se acredita el criterio de cada control. Registrar disponibilidad, incidentes y consumo de recursos durante la operación.

La configuración inicial Single-AZ exige valorar el efecto de una interrupción zonal en el objetivo de disponibilidad. El paso a Multi-AZ conserva su condición de compuerta del diseño para la operación comercial. La configuración de respaldo, por sí sola, requiere un ensayo para acreditar RPO y RTO.

La planificación del Anexo G relaciona esta secuencia con las actividades de adecuación del diseño y revisión de infraestructura AWS. La transición preoperativa identifica responsables de preparación técnica, legal y de proveedores. La frontera comercial del 1 de enero de 2027 corresponde al estudio económico. La puesta en servicio efectiva exige acreditar los controles de este capítulo mediante sus evidencias de aceptación.
