# CAPÍTULO VII: Definición de Arquitectura TI

## 7. Definición de Arquitectura TI

### 7.1. Vistas de arquitectura

La vista de negocio define oferta, búsqueda, contratación y entrega. La vista de aplicaciones ubica la interfaz, la API y los módulos. La vista de datos asigna autoridades a ocupación, contrato y pagos y separa los archivos privados. La vista de infraestructura identifica los entornos y los controles de despliegue que desarrolla el Capítulo XIII.

El Capítulo X detalla los componentes y la comunicación entre la interfaz, el núcleo y sus adaptadores.

### 7.2. Decisiones y criterios de revisión

**Tabla 8**\
*Decisiones arquitectónicas y criterio de verificación*

| Decisión | Consecuencia técnica | Verificación |
|---|---|---|
| Backend modular | La coordinación entre módulos conserva límites de responsabilidad. | Revisar paquetes y contratos del corte. |
| PostgreSQL y PostGIS | La búsqueda espacial y la exclusión temporal operan mediante mecanismos separados. | Probar consultas y concurrencia en la base. |
| Autorización por recurso | El papel de la cuenta depende de la operación y del vínculo con el espacio o la reserva. | Probar titular, participante y tercero. |
| Adaptadores externos | La simulación y el proveedor utilizan criterios de habilitación distintos. | Registrar entorno, eventos y resultado por integración. |

*Nota.* Elaboración propia con base en la arquitectura del repositorio y el ADR del 4 de noviembre de 2026. La Tabla D.1 identifica relaciones físicas, la Tabla E.1 identifica operaciones y las tablas F.1 y F.2 documentan escenarios de verificación.

### 7.3. Decisión de plataforma y alcance construido

Los ADR-AWS-01 a ADR-AWS-05 del 15 de noviembre fijan como destino Cloudflare en el borde, una tarea ECS Fargate con Next.js y Go, RDS PostgreSQL Single-AZ inicialmente, S3 por finalidad y Zoho para el correo. La región inicial declarada es us-east-2 y Chile queda sujeto a disponibilidad y habilitación. La selección busca reducir el costo de operación y aprovechar los créditos informados para el proyecto [@espacigoaws2026].

La implementación local dispone de adaptadores S3 y de módulos Terraform para almacenamiento, parámetros, logs y roles emulados. La configuración aws-main declara red, RDS y componentes de soporte. Las definiciones ECS y ECR, la entrega OIDC, el ingreso seguro y la gestión de secretos forman parte de la preparación del despliegue. El Capítulo XIII establece las comprobaciones que permiten aceptar esa preparación.
