# CAPÍTULO XI: ESTRATEGIA DE IMPLEMENTACIÓN, DESPLIEGUE Y SEGURIDAD

## 11.1. Pipeline de Integración y Despliegue Continuo (CI/CD)

El repositorio de desarrollo declara la configuración de construcción y despliegue en [cloudbuild.yaml](https://github.com/HernanEspinozaDev/espaciGo/blob/93b59c8352960d900b4e62bb42bced9e05dcad8c/cloudbuild.yaml) del corte `93b59c8`. El archivo identifica el procedimiento de construcción y despliegue. La ejecución de un despliegue requiere evidencia del entorno. La estrategia de entrega identifica la versión de aplicación y el estado del esquema antes de desplegar. El procedimiento de aceptación revisa compilación, pruebas, permisos y compatibilidad con las migraciones aplicadas. La versión de aplicación y el delta de base se registran por separado.

## 11.2. Topología de Infraestructura Cloud en Google Cloud Platform (GCP)

La topología objetivo utiliza servicios administrados en la región de Santiago. El registro de estrategia de base de datos del 4 de noviembre, en el contexto local de desarrollo, describe una instancia Cloud SQL zonal, con acceso privado y respaldos automáticos. La configuración observada registra PITR desactivado. La figura representa la topología de referencia para la operación objetivo.

La Figura 12 representa la topología objetivo y separa las rutas de usuario y operación.

**Figura 12**\
*Topología objetivo de aplicación, datos y operación*

![](assets/figuras/fig17_topologia_objetivo.png)

*Nota.* Elaboración propia sobre servicios gestionados en Google Cloud Platform (región `southamerica-west1`).

### Segmentación de Red y Comunicaciones Privadas
El diseño de red restringe el acceso a la base a través de la VPC y limita el acceso operativo mediante rutas y permisos definidos para cada entorno.

## 11.3. Seguridad y autorización por recurso

El diseño establece mínimo privilegio para aplicación, migraciones y operación. Como criterio de diseño, cada solicitud debe verificar el vínculo del actor con el recurso y las capacidades exigidas por la acción. La evidencia privada utiliza almacenamiento separado, y su acceso y retención dependen de su finalidad. Las revisiones documentales incluyen pruebas de denegación y comprobación de permisos efectivos.

## 11.4. Recuperación y continuidad

El procedimiento objetivo restaura PostgreSQL y los objetos privados en un entorno aislado. La aceptación exige comprobar referencias, permisos y acciones de supresión que el respaldo antecede. La medición compara el punto recuperado y el tiempo de recuperación con el RNF-010. El operador registra las divergencias y conserva aislado el destino cuando falla una comprobación.

La Figura 13 resume el ensayo objetivo de restauración. El Capítulo X y la Tabla F.3 identifican los resultados parciales y la falla de permisos observada.

**Figura 13**\
*Actividad objetivo de restauración y verificación*

![](assets/figuras/fig19_recuperacion_objetivo.png)

*Nota.* Elaboración propia. El flujo describe el criterio de aceptación del ensayo de recuperación.

## 11.5. Procedimientos operativos de referencia

El diseño de operación incluye guías para continuidad, incidentes y mantenimiento. Antes de ejecutar un procedimiento, el operador confirma destino, permisos, configuración y versión. El objetivo general de recuperación corresponde al RNF-010.

**Tabla 11**\
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


## 11.6. Condiciones de habilitación de integraciones

La habilitación de proveedores queda pendiente hasta que esté listo el código del flujo y se ejecuten sus pruebas. **Mercado Pago** es el proveedor previsto para renta y comisión mediante Checkout Pro, OAuth del vendedor y Split 1:1 [@es2mpsplit]. Su aceptación requiere comprobar acreditación, conciliación y reembolso. **SimpleFirma** es el proveedor previsto para la modalidad de firma opcional. Su aceptación requiere evidencia por emisión y firmante y comprobación de facturación y reversos. La garantía monetaria conserva su habilitación pendiente. El mecanismo y el responsable de fondos se confirman mediante pruebas de cobro, reclamos y devoluciones. La verificación externa de identidad y representación, cuando corresponda, se registra como integración pendiente de definición y validación.

La política de retención identifica finalidad, evento inicial, excepción, responsable y acción sobre datos y objetos. El ensayo de continuidad verifica que la restauración respeta esas decisiones y los permisos de acceso.
