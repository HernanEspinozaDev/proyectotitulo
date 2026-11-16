# CAPÍTULO IX: Detalle de las Tecnologías a implementar

## 9. Detalle de las Tecnologías a implementar

### 9.1. Análisis cualitativo/cuantitativo de las tecnologías que serán implementadas

La selección contrasta compatibilidad con los requisitos, integridad temporal, separación de dependencias y operación. PostgreSQL aporta exclusión de intervalos y PostGIS las consultas espaciales. Go mantiene el núcleo y los adaptadores en módulos de aplicación. Next.js reúne vistas y el BFF. Como evidencia cuantitativa acotada, el ensayo SQL procesa 42.636 consultas en 15 segundos con 70,22 ms de latencia media. Las verificaciones comparables de extremo a extremo se especifican en el Capítulo XII.

### 9.2. Herramientas, aplicaciones, lenguajes y componentes que serán implementados

El punto de entrada de la API reside en `cmd/api`. El repositorio agrupa responsabilidades en paquetes bajo `internal`, entre ellos `spaces`, `occupancy`, `booking`, `contract` y `documentverification`. Los adaptadores PostgreSQL se organizan bajo `internal/adapters/postgres`. La estructura refleja límites de responsabilidad y permite verificar componentes con dependencias controladas.

El diseño asigna la ocupación a PostgreSQL para que dos solicitudes simultáneas se resuelvan bajo la misma restricción de integridad. PostGIS selecciona candidatos por ubicación y distancia. El Capítulo X desarrolla la exclusión temporal y el Anexo D vincula el diseño con el esquema físico.

La interfaz Next.js consume la API Go a través de los adaptadores de la aplicación y de la ruta BFF cuando corresponde. El contrato de acceso debe preservar la autorización sobre cada recurso desde la entrada hasta la operación de dominio. La Tabla F.3 registra evidencia parcial de denegación en el perfil documental. El Anexo E identifica el corte de OpenAPI y separa las rutas de ensayo.

La Tabla 10 resume las responsabilidades del stack y la evidencia disponible para cada componente.

**Tabla 10**\
*Tecnologías, funciones y estado documentado*

| Tecnología | Función | Versión o evidencia |
|---|---|---|
| Go | API, dominio y adaptadores. | 1.27.1 declarada. |
| Next.js | Interfaz y BFF. | 16.4.3 declarada. |
| PostgreSQL | Datos y exclusión temporal. | Serie 18. Ensayo en 18.6. |
| PostGIS | Búsqueda por ubicación. | Serie 3.6 de diseño. |
| OpenAPI | Contrato HTTP de la API. | Especificación 3.1 (Anexo E). |
| Docker | Empaquetado en imágenes. | Receta `Dockerfile`. |
| AWS SDK para Go v2 | Acceso a objetos S3. | Adaptadores s3storage y documents3. |
| aws-emulator | Servicios AWS locales. | Endpoints de S3, SSM, IAM y logs. |
| Terraform | Infraestructura como código. | Entornos local-emulator y aws-main. |
| GitHub Actions | Construcción y calidad. | Flujos de aplicación, frontend, base e IaC. |
| ECS Fargate y ECR | Ejecución y registro de imágenes. | Destino de despliegue pendiente de completar. |
| RDS, S3, SSM y CloudWatch | Datos, objetos, parámetros y logs. | Componentes cloud declarados por entorno. |
| Cloudflare y Zoho | Borde, acceso y correo. | Servicios del diseño objetivo. |

*Nota.* Elaboración propia a partir del repositorio espacigo-aws, corte 3dc1c18 del 16 de noviembre de 2026 [@espacigoaws2026]. Los capítulos X, XII y XIII distinguen el código local, la infraestructura declarada y las comprobaciones de despliegue.

El entorno local utiliza Go 1.27.1 y Next.js 16.4.3, según sus manifiestos. PostgreSQL 18.6 corresponde al entorno de desarrollo y al ensayo SQL histórico. La configuración aws-main fija 18.1 para RDS, por lo que la selección de versión y PostGIS requiere conciliación con el catálogo regional antes del despliegue. El cliente S3 utiliza endpoints locales y autenticación del emulador por defecto. La ejecución en Fargate requiere configurar el endpoint regional y comprobar el uso del rol de tarea.
