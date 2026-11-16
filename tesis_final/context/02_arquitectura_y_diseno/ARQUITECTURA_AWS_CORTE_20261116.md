# Fuentes y contraste de arquitectura AWS para la memoria

Repositorio consultado `/home/nandev/Documentos/projects/espacigo-aws`, commit `3dc1c18fd7e8ff7cd3d310b16615c1c8c97ec2c3`. Consulta del 16 de noviembre de 2026, mediante lectura de archivos versionados. El análisis no consulta ni modifica recursos cloud.

## Evidencia de construcción

- `go.mod` declara AWS SDK para Go v2 y Go 1.27.1. El adaptador `internal/adapters/s3storage` implementa objetos, medios y registro de supresiones. `documents3` conserva la capa documental cifrada.
- `cmd/api/runtime_storage.go` admite S3 y sistema de archivos. El cliente S3 apunta por defecto al emulador y requiere adaptación explícita al endpoint y las credenciales temporales del destino.
- `infra/terraform/environments/local-emulator/main.tf` configura endpoints de S3, SSM, logs, IAM y STS del emulador. Su etiqueta regional por defecto es `us-east-1`, independiente de la región cloud inicial.
- `infra/terraform/modules/s3_storage/main.tf` separa cinco finalidades, activa versionado, bloqueo de acceso público y SSE-S3 AES256.
- `infra/terraform/environments/aws-main` parametriza la región inicial `us-east-2`, descubre dos zonas, configura subredes, RDS con respaldos siete días y Single-AZ por defecto, y módulos de soporte. El motor está fijado a 18.1 en IaC y el entorno local declara 18.6. La compatibilidad de versión y extensiones requiere comprobación previa.
- `.github/workflows/application-quality.yml`, `database-quality.yml`, `frontend-quality.yml` e `iac-quality.yml` aportan controles de construcción y calidad. La entrega OIDC a ECS/ECR sigue como objetivo del plan.
- Las migraciones versionadas alcanzan `V000098__space_inventory_and_calendar_rules.sql`. El catálogo D de la memoria conserva el corte previo V83 como referencia, identificado expresamente.

## Decisiones rectoras

`docs/architecture/aws-proposal/04-recommended-architecture.md` y `09-risks-and-decisions.md`, actualizados el 15 de noviembre, documentan ADR-AWS-01 a ADR-AWS-05. Se eligen Cloudflare, tarea Fargate co-ubicada, RDS Single-AZ inicialmente, S3 SSE-S3 y correo Zoho. La región Chile queda como objetivo condicionado a disponibilidad y habilitación. Las guías que muestran ALB, Multi-AZ inicial o SES representan alternativas anteriores.

La selección procura reducir costos y aprovechar los créditos comunicados por el propietario. Las estimaciones numéricas de la propuesta no se trasladan a la evaluación financiera reservada ni se presentan como facturación comprobada.

## Respaldo oficial consultado

- Charles Clark, Amazon, 11 de noviembre de 2026. Acceso anticipado de AWS South America (Chile) para clientes seleccionados, con disponibilidad general prevista. https://www.aboutamazon.com/news/aws/aws-south-america-chile-region-launch
- Elizabeth Fuentes, AWS, 7 de mayo de 2025. Anuncio de región Chile con tres zonas de disponibilidad al lanzamiento. https://aws.amazon.com/blogs/aws/coming-soon-aws-south-america-chile-region/
- AWS Free Tier. Créditos iniciales de USD 100 y hasta USD 100 adicionales, con condiciones de elegibilidad y duración. https://aws.amazon.com/free/
- Amazon ECS. Red awsvpc, interfaz por tarea y comunicación entre sus contenedores por localhost. https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-networking.html
- Amazon RDS. Versiones PostgreSQL y extensiones. https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-versions.html
- Amazon RDS. Respaldos y restauración. https://docs.aws.amazon.com/AmazonRDS/latest/gettingstartedguide/managing-backup-restore.html
- Amazon S3. Cifrado SSE-S3. https://docs.aws.amazon.com/AmazonS3/latest/userguide/specifying-s3-encryption.html

## Verificaciones del destino

Completar definiciones ECS, servicio y ECR, entrega OIDC, gestión de secretos y TLS, restringir el ingreso al origen autorizado y validar cuotas, motor y extensiones. Probar caducidad de permisos, acceso a objetos, restauración de versiones compatibles, replay de supresión, RPO/RTO, disponibilidad y carga de extremo a extremo. La emulación local acredita sus escenarios documentados y conserva separación respecto de las pruebas cloud.
