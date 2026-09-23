# INV-007 — Disponibilidad, continuidad y mantención

- Estado: diseño operativo documental; sin infraestructura, responsables ni ensayos aprobados.
- Fecha de consulta: 2026-09-23.
- Secciones ES2: `secciones/06_01_disponibilidad.md`, `06_02_continuidad.md`, `06_03_mantencion.md`.
- Base inmutable: informe final ES1, arquitectura y niveles de servicio; anexo C, RNF-009/010/017/019/023/024/028/030/034–036; ES2, SLA-01–05 y PT-11.

## Preguntas y método

¿Cómo medir la disponibilidad de cada función, recuperar una interrupción grave y mantener la configuración sin atribuir logros aún inexistentes? Se derivaron controles de los RNF y fichas SLA. Se revisaron documentos oficiales de Google Cloud, PostgreSQL y NIST para distinguir una capacidad de herramienta de una garantía demostrada. Cloud Run, Cloud SQL y Cloud Monitoring siguen siendo alternativas de diseño: no hay evidencia de que EspaciGo los haya desplegado.

## Fuentes y hallazgos

| Fuente primaria | Posibilidad documentada | Límite para EspaciGo |
| --- | --- | --- |
| Google Cloud, [uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks) y [alertas](https://docs.cloud.google.com/monitoring/alerts) | Configurar sondeos y notificaciones. | La salud de un endpoint no prueba un flujo de negocio; hay que diseñar transacciones sintéticas y conservar mediciones. |
| PostgreSQL, [archivado continuo y PITR](https://www.postgresql.org/docs/18/continuous-archiving.html) | Combinar copia base con WAL archivado para restaurar a un punto temporal. | Requiere secuencia íntegra de WAL y pruebas; no incluye automáticamente archivos de configuración ni objetos externos. |
| Google Cloud, [restauración Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore) | Documenta recuperación puntual del servicio gestionado y sus límites. | Se aplica solo si se contrata/configura Cloud SQL; la documentación del proveedor no demuestra RPO/RTO propios. |
| NIST, [SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) | Guía para planificación y ensayo de contingencia. | Sirve como método de diseño, no como certificación ni resultado de recuperación. |
| Google Cloud, [revisiones y reversión de Cloud Run](https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration) | Puede redirigir tráfico a una revisión anterior. | La reversión de aplicación no deshace migraciones de base ni pagos ya aceptados por terceros. |

## Relación con ES1 y decisiones ES2

**Confirma:** RNF-009/010 expresan objetivos cuantificables; los servicios críticos son autenticación, búsqueda y reservas. **Amplía:** se necesitan sondeos por función, inventario de dependencias, alerta, responsable, respaldo de archivos y recuperación de operaciones externas. **Deja pendiente:** región, arquitectura de datos, frecuencia de copias, costos, responsables, horas contractuales, capacidad real, recuperación y portabilidad RNF-034–036.

El borrador 6.1 mide cada función separadamente. El 6.2 propone tres escenarios con activación, contención, restauración y prueba de retorno; PT-11 debe producir RPO/RTO observados. El 6.3 registra configuración, cambios e incidentes con campos mínimos y distingue una disputa comercial M10 de un fallo técnico. Ningún procedimiento se declara ejecutado.

[[PENDIENTE: acordar roles/autoridad/canales, escoger herramientas y ubicación de copias, presupuestar y desplegar entorno, ejecutar sondeos, ensayo PT-11, reversión y simulacro; actualizar capítulos y SLA con observaciones.]]
