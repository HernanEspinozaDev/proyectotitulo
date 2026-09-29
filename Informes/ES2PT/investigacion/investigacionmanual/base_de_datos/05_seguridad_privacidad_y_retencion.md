# Seguridad, privacidad y ciclo de vida de los datos

## Modelo de amenazas y acceso

Los riesgos prioritarios son lectura cruzada entre arrendadores/arrendatarios, escalada administrativa, fuga por respaldos/exports/logs, cambio de estado por webhook, abuso del acceso a documentos y conservación excesiva. Cada consulta de la API verifica actor, rol, recurso y acción; los filtros `WHERE propietario/participante` deben ser parte del SQL o del repositorio, no solo del frontend. El DDL actual no define RLS. Mantener autorización en la API como decisión inicial y considerar RLS como defensa adicional solo cuando se diseñen contexto por sesión, pools, roles y pruebas de aislamiento. Activar RLS sin un modelo de identidades de DB puede dar una protección aparente o filtrar datos por `search_path`/conexión reutilizada.

## Privilegio mínimo en PostgreSQL y GCP

Proponer roles separados: **owner/migrator** para DDL en despliegue, **app_rw** para DML mínimo, **app_ro** si existe consumidor autorizado, y **backup/operación** con permisos propios. La API no usa credencial propietaria ni `SUPERUSER`; revocar acceso por defecto a esquemas, funciones y secuencias, y revisar privilegios heredados/default. Cloud Run usa cuenta de servicio por ambiente, conectividad privada o conector autenticado según diseño probado, Secret Manager para secretos y rotación. Ninguna contraseña/URL firmada entra en Git, imagen, variables del plan IaC ni logs. La separación de ambientes incluye bases, cuentas, buckets, datasets y datos sintéticos; no restaurar producción en desarrollo sin desidentificación aprobada. Google documenta [IAM para Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication) y [conexiones privadas](https://docs.cloud.google.com/sql/docs/postgres/private-ip).

## Inventario por dato y propósito

La matriz final debería tener, por cada campo o clase documental: responsable, titular, finalidad, base jurídica **por confirmar**, origen, destinatarios/encargados, sensibilidad, ubicación, cifrado, roles con acceso, plazo y evento inicial del plazo, acción de cierre, copias/derivados, evidencia de ejecución y excepción fundada. Diferenciar cuenta, KYC, medios de pago, reservas/tributación, contrato, evidencia de disputa, auditoría técnica, analítica y solicitud de derechos. No inferir que un UUID es anónimo: puede vincularse a una persona. No incluir PAN/CVV, credenciales del proveedor, cuerpo completo de webhook ni documentos en BigQuery. El Anexo B ya tiene una matriz inicial, pero algunas celdas se presentan como aprobadas y fijan 72 h/5 años mientras la propia sección 3.4 dice que base y plazos faltan. Debe corregirse antes de que sea política ejecutable. Ley 21.719 es **criterio de diseño desde ES2**; su vigencia es 01-12-2026 y no se declara cumplimiento probado ([Biblioteca del Congreso Nacional, Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272)).

## Supresión, bloqueo y retención sin romper integridad

1. Resolver una solicitud solo tras verificación de identidad, inventario de registros vinculados, revisión de causal/retención y decisión fundada; `solicitud_titular` conserva trazabilidad mínima sin repetir el dato suprimido.
2. Para hechos financieros o contractuales cuya conservación se apruebe, separar identidad directa del hecho o anonimizar referencias cuando sea jurídicamente posible. Una FK `NOT NULL` a `usuario` impide simplemente borrar la cuenta: diseñar seudonimización/tabla de identidad separada, estado de cuenta o eliminación diferida por flujo. No usar `ON DELETE CASCADE` en reservas, pagos, contratos ni auditoría.
3. Propagar la acción a objetos Cloud Storage, exportaciones analíticas, índices de búsqueda, cachés y respaldos dentro de política aprobada. La restauración de una copia antigua debe reproducir decisiones de supresión posteriores mediante un registro seguro de tombstones/operaciones, evitando reactivar PII por accidente.
4. Documentar retención por tabla/objeto y evento inicial (alta, cierre, pago, resolución de disputa), responsable, revisión periódica y evidencia de purga. No prometer un plazo universal de 72 h ni cinco años sin base y alcance acreditados.
5. La propuesta RNF-017 de retención bloqueada en Cloud Storage puede ser irreversible. Definir plazo y efecto sobre derechos antes de activarla; el hash del documento demuestra detección de cambio frente a un hash confiable, no inmutabilidad del repositorio.

## Auditoría y cifrado

`evento_auditoria` registra actor (o proceso), acción, recurso, resultado, motivo, instante y correlación sin secretos ni contenido íntegro. Controlar quién puede leerla, quién puede escribirla y quién puede corregirla; el diseño de exportación con retención bloqueada debe probarse antes de llamarlo inmutable. Cifrar tránsito con TLS y almacenamiento según capacidades de Cloud SQL/GCS; la decisión de claves administradas por cliente necesita evaluación de costo/operación, no se impone por defecto. Los respaldos y logs también son datos tratados y entran en la matriz. Usar datos sintéticos en MD/PT salvo autorización y minimización explícitas.

## Casos verificables

- PT-16: arrendatario A no consulta documentos/contratos/reservas de B ni por ID conocido; administrador consulta solo con acción auditada; solicitud de acceso exporta únicamente datos propios.
- Solicitud de supresión aplica la matriz aprobada sin borrar evidencia obligatoria ni dejar PII innecesaria en outbox/analítica; la restauración no revive dato eliminado.
- Webhook inválido no modifica negocio; un usuario de aplicación no puede ejecutar DDL ni leer tabla de migraciones/secretos.
- Copia de respaldo y exportaciones se pueden localizar, restaurar y eliminar/expirar según política, con evidencia y permisos limitados.
