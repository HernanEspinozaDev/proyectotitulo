# Plan de actualización de la arquitectura de la memoria a AWS

Fecha de corte documental 16 de noviembre de 2026. Línea base de la memoria `2824feb`. Fuente de implementación `espacigo-aws`, commit `3dc1c18fd7e8ff7cd3d310b16615c1c8c97ec2c3`.

## Decisiones de actualización

La documentación de arquitectura de los días 15–16 de noviembre y los ADR-AWS-01 a ADR-AWS-05 prevalecen para describir el destino. La inspección de código y Terraform determina qué está construido. El entorno local utiliza PostgreSQL Docker, adaptadores S3 y aws-emulator. El destino inicial comprende Cloudflare, una tarea ECS Fargate con web y API, RDS PostgreSQL Single-AZ, S3, SSM, CloudWatch y correo Zoho. ECR y entrega con GitHub Actions/OIDC forman parte del diseño de despliegue.

El anuncio oficial de Amazon del 11 de noviembre de 2026 confirma acceso anticipado a la región de Chile para clientes seleccionados. El anuncio de AWS de mayo de 2025 proyecta tres zonas de disponibilidad al lanzamiento. La tesis identifica Chile como región objetivo futura y Ohio como región inicial del diseño. La habilitación regional y la disponibilidad de servicios se verifican antes del despliegue. El código regional de Chile y los tiempos de latencia de la propuesta local quedan sujetos a confirmación oficial y medición.

El propietario informa USD 200 de créditos para el proyecto. El programa público concede USD 100 iniciales y permite obtener hasta USD 100 adicionales, bajo sus condiciones. La motivación de costos se documenta como criterio de selección. El cálculo financiero de costos y ahorros conserva su integración reservada a Anita y Erick.

## Inventario y ejecución por sección

- [x] **AWS-01. Contexto y fuentes.** Registrar el corte, las decisiones rectoras, las diferencias con guías anteriores y las fuentes oficiales de Chile, Free Tier, red Fargate, RDS y S3.
- [x] **AWS-02. Preliminares e introducción.** Incorporar el destino AWS y la construcción local al resumen y abstract, manteniendo cifras históricas como cortes. Añadir en I la evolución de infraestructura y sus motivos.
- [x] **AWS-03. III–VIII.** Incorporar restricciones regionales y separación local/nube en III, fundamento de nube y regiones en IV, criterios de habilitación en V, EDT AWS en VI y decisiones de despliegue en VII. Conservar los objetivos y el alcance de nueve categorías y revisar la coherencia de VIII.
- [x] **AWS-04. IX.** Sustituir Cloud Build por la combinación de GitHub Actions, Terraform, AWS SDK para Go, emulador y servicios destino. Identificar versiones y configuración disponibles y las piezas cloud pendientes.
- [x] **AWS-05. X y diagramas.** Reemplazar las figuras 9, 12 y 17 con fuentes PlantUML y PNG editables. Distinguir BFF por loopback, red VPC, Fargate, RDS Single-AZ, S3 privado, IAM, SSM, CloudWatch, borde Cloudflare y ruta de entrega objetivo. Retirar del directorio de fuentes compilables los diagramas obsoletos de GCP y conservarlos como archivo histórico.
- [x] **AWS-06. XI–XIII y F.** Mantener objetivos RNF y actualizar evidencia, continuidad y despliegue AWS. La configuración cloud inspeccionada requiere completar ECS/ECR y entrega OIDC, endurecer ingreso, gestionar secretos y verificar TLS. Los ensayos anteriores conservan sus resultados y fecha. Las pruebas del emulador y la configuración local requieren su propia evidencia. PT-11/PT-16 se ejecutan en RDS/S3 para acreditar recuperación objetivo.
- [x] **AWS-07. D y E.** Identificar como histórico el catálogo DDL de 110 tablas y la captura V75. Registrar la evolución hasta V98 en el repositorio AWS, sin atribuirle la comparación histórica. Mantener identificadores SQL heredados que siguen en migraciones y advertir su procedencia. Cotejar adaptadores y contratos actuales con los anexos de referencia.
- [x] **AWS-08. XVI–XVIII y bibliografía.** Actualizar cierre, limitaciones y glosario. Integrar referencias APA de fuentes oficiales y del corte del repositorio. Preservar XIV, XV y anexos G/H y los bloques reservados. Registrar la motivación económica en la decisión técnica.
- [x] **AWS-09. Construcción y verificación.** Compilar con DocSkill, comprobar índices, enlaces, numeración y figuras renderizadas, contrastar archivos reservados y registrar referencias heredadas justificadas. Publicar Word, PDF y fuentes en main.

## Hallazgos que condicionan la redacción

El README y la guía general presentan alternativas anteriores con ALB, Multi-AZ, SSE-KMS y SES. Los ADR recientes seleccionan Cloudflare, Fargate co-ubicado, Single-AZ, SSE-S3 y Zoho. La tesis sigue los ADR y delimita el estado de implementación.

Terraform `aws-main` declara VPC, dos subredes públicas y dos privadas, endpoint S3, RDS, IAM, SSM y logs. El ingreso de la tarea aún admite cualquier origen en el puerto 4000, la contraseña de RDS es un marcador y no se declaran recursos ECS/ECR. Esas condiciones se documentan como controles de aceptación pendientes. El código del cliente S3 tiene valores locales por defecto, por lo que el uso de credenciales temporales de tarea y endpoints regionales requiere configuración y prueba del destino.

Los identificadores `gcp06_test_access_batch_audit`, `cli_gcp06` y los literales `gcs` siguen en migraciones del repositorio AWS. Su sustitución textual en el diccionario falsearía el esquema. Se conservan como evidencia histórica y deuda de evolución, con explicación en D. Los adaptadores de ejecución actuales seleccionan S3 o sistema de archivos.


## Resultado de ejecución

El Word y el PDF se reconstruyen con DocSkill y LibreOffice del runtime documental. El PDF final tiene 522 páginas. La diferencia con la línea base también refleja la composición tipográfica del runtime utilizado. Se comprueba la presencia de los identificadores de 236 RF, 43 RNF, 35 HU, 52 CU y las 110 fichas históricas de tablas. Se verifican 18 destinos de capítulo, 21 entradas del índice de tablas y 30 del índice de figuras.

Las figuras 9, 12 y 17 tienen fuentes PlantUML y renders PNG nuevos en assets/imagenes. Sus destinos en el PDF son las páginas impresas 39, 44 y 60. Se archivan 19 fuentes obsoletas y sus renders fuera del directorio compilable. El generador de diagramas resuelve la ubicación de las figuras AWS. El exportador admite la ruta explícita de LibreOffice y copia el entorno de ejecución para aislar el arranque del servidor UNO.

La revisión visual se concentra en las páginas afectadas, índices y figuras. La Figura 18 se ajusta a 14 cm para conservar el texto asociado en su página. Los enlaces de Chile, Free Tier, la Ley 21.719 y PostGIS mantienen destinos PDF verificables.

Los capítulos XIV y XV y los anexos G y H conservan identidad con la línea base. Las alertas de integración siguen presentes. El cuerpo deja de describir infraestructura GCP. El Anexo D conserva nombres SQL heredados que siguen en migraciones, con explicación de su origen y de la conciliación pendiente con S3. Los resultados históricos de pruebas mantienen su corte y el despliegue AWS conserva sus condiciones de habilitación.

El cambio incorpora un plan y contexto de consulta que distinguen el diseño objetivo, el código local y la evidencia cloud pendiente. Los archivos financieros de trabajo presentes en la raíz quedan fuera de esta actualización.
