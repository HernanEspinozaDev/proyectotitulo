# INV-023 — Operación, Continuidad y Herramientas (Sección VI)

- Consulta documental: 23-09-2026.
- Estado: Decisiones operativas para la sección VI del informe ES2PT.
- Objetivo: Establecer herramientas y responsables formales para monitoreo, respaldos y mantención para los capítulos 06_01, 06_02 y 06_03.

## Selección de Herramientas y Operación

### Monitoreo (Disponibilidad)
Para medir los SLA de los requisitos (RNF-009, RNF-001) y activar las alertas de indisponibilidad:
- **Herramienta Elegida:** Google Cloud Monitoring (Uptime Checks y Alerting).
- **Sondas y Umbrales:** Sondas HTTPS distribuidas globalmente hacia los *endpoints* principales de autenticación y búsqueda. Se establece un umbral de **2 fallos consecutivos cada 5 minutos** para gatillar la alerta de indisponibilidad del servicio principal.
- **Canales de Alerta:** Integración de Google Cloud Monitoring con canal de **Slack** (`#espacigo-ops`) y correo del responsable de guardia.
- **Ventanas y Exclusiones:** El mantenimiento planificado se acordará para la madrugada (03:00 - 05:00 AM) de los domingos y sus minutos se descontarán del umbral de indisponibilidad al momento del cálculo mensual del SLA.

### Continuidad (RPO / RTO)
Para asegurar RPO ≤ 4 h y RTO ≤ 6 h (RNF-010):
- **Base de Datos (PostgreSQL):** Cloud SQL con *Automated Backups* (respaldos diarios, retención 7 días) y *Point-in-Time Recovery* (PITR) activado mediante el archivo de WAL (RPO cercano a 0).
- **Archivos Estáticos/Adjuntos:** Google Cloud Storage con *Object Versioning* habilitado para prevención contra sobrescritura o eliminación accidental.
- **Ensayo de Restauración (PT-11):** Se planifica ejecutar el ensayo de restauración semestralmente (o antes de un pase grande), en el cual el custodio restaurará la base de datos de producción a una instancia Cloud SQL temporal en la VPC de Staging para validar integridad y tiempos de levantamiento (RTO). 

### Mantención e Incidentes
- **Herramienta de Registro:** **GitHub Issues**. Se utilizará para incidentes (*label: incident*, *severity: critical/high*) y cambios ordinarios (*label: enhancement*).
- **Responsables y Aprobaciones:** Los miembros del equipo técnico serán los "Propietarios". Cualquier paso a producción requerirá un cambio evaluado mediante un Pull Request (PR) y la **aprobación explícita (review) de al menos una persona distinta** al desarrollador (4-eyes principle).
- **Reversión (Rollback):** Las versiones se implementarán como imágenes de contenedor inmutables en Cloud Run. En caso de fallo en humo, el *Traffic Splitting* permite devolver inmediatamente el tráfico al 100% de la revisión de código anterior, en tanto la base de datos sea retro-compatible o se evalúe recuperar desde respaldo.
