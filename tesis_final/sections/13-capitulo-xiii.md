# CAPÍTULO XIII: Plan de Implementación

## 13. Plan de Implementación

### 13.1. Gestión de Disponibilidad

El repositorio de desarrollo declara la configuración de construcción y despliegue en [cloudbuild.yaml](https://github.com/HernanEspinozaDev/espaciGo/blob/93b59c8352960d900b4e62bb42bced9e05dcad8c/cloudbuild.yaml) del corte `93b59c8`. El archivo identifica el procedimiento de construcción y despliegue. La ejecución de un despliegue requiere evidencia del entorno. La estrategia de entrega identifica la versión de aplicación y el estado del esquema antes de desplegar. El procedimiento de aceptación revisa compilación, pruebas, permisos y compatibilidad con las migraciones aplicadas. La versión de aplicación y el delta de base se registran por separado.

El diseño establece mínimo privilegio para aplicación, migraciones y operación. Como criterio de diseño, cada solicitud debe verificar el vínculo del actor con el recurso y las capacidades exigidas por la acción. La evidencia privada utiliza almacenamiento separado, y su acceso y retención dependen de su finalidad. Las revisiones documentales incluyen pruebas de denegación y comprobación de permisos efectivos.

### 13.2. Gestión de Continuidad

El procedimiento objetivo restaura PostgreSQL y los objetos privados en un entorno aislado. La aceptación exige comprobar referencias, permisos y acciones de supresión que el respaldo antecede. La medición compara el punto recuperado y el tiempo de recuperación con el RNF-010. El operador registra las divergencias y conserva aislado el destino cuando falla una comprobación.

La Figura 17 resume el ensayo objetivo de restauración. La comprobación de permisos es una condición de reapertura del servicio, porque la recuperación de los datos por sí sola no acredita que se conserva su control de acceso. La Tabla F.3 registra la falla observada en esa etapa.

**Figura 17**\
*Actividad objetivo de restauración y verificación*

![](assets/figuras/fig19_recuperacion_objetivo.png)

*Nota.* Elaboración propia. El flujo describe el criterio de aceptación del ensayo de recuperación.

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
