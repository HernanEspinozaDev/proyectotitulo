# Verificación de fondo de espaciGo

**Corte:** 4 de noviembre de 2026. **Repositorio de desarrollo:** `93b59c8`. El corte distingue revisión documental, comprobación de contrato, pruebas locales y validación en el entorno objetivo.

## 1. Fichas secundarias y trazabilidad

La revisión compara las fichas con OpenAPI y con la separación entre reglas objetivo y capacidades de ensayo. El Anexo C registra el alcance por módulo. La condición de participante y la visibilidad de cada reseña, los permisos administrativos, la limitación de reportes y el carácter diferido de la recurrencia se aclaran en A, B y C.

| Alcance | Evidencia revisada | Resultado y límite |
|---|---|---|
| Disponibilidad | Rutas de disponibilidad, bloqueos y horario semanal | El horario semanal del espacio se distingue de la recurrencia de reservas, diferida por el ADR. |
| Mensajería y reputación | Rutas de mensajes y reseñas del ensayo y consulta de reseñas del espacio | La escritura de ensayo exige contexto de reserva y participante. La consulta pública y la evaluación de una persona tienen proyecciones distintas. |
| Administración | Rutas de cuentas, auditoría, publicaciones, indicadores y capacidades | La existencia de un endpoint acredita el contrato. Los reportes integrales de operación y finanzas requieren su propia definición y evidencia. |
| Pruebas Go sin DSN | 11 paquetes con pruebas exitosas y dos sin archivos de prueba | La ejecución acredita las pruebas sin integración con base. |
| Reputación PostgreSQL | `TestSyntheticReviewReciprocityModerationRetentionAndRuntimePermissions` | Falló durante la preparación: el test migra antes de crear `espacigo_runtime` y V74 ya requiere ese rol. No se alcanzan las aserciones de reputación. Requiere corregir el orden de bootstrap del banco y repetir en un entorno desechable. |

## 2. Proveedores y retención

| Componente | Comprobación | Criterio de habilitación pendiente |
|---|---|---|
| Mercado Pago | La documentación oficial confirma Checkout Pro, token OAuth del vendedor, Preferences y `marketplace_fee` para Split 1:1. En ese modelo la falta de saldo del vendedor limita el reembolso total desde el marketplace. | Ensayar con cuentas de prueba y registrar vinculación, acreditación, evento repetido y tardío, devolución total y parcial, vendedor sin saldo y conciliación. |
| SimpleFirma | La introducción oficial documenta ambientes de prueba y producción, documentos, solicitudes de firma y webhooks HMAC. La lectura directa detallada devolvió timeout durante el corte. | Confirmar solicitud con dos firmantes, trazabilidad por emisión, evidencia descargable, vencimiento, duplicados y condiciones de facturación o reverso. |
| Garantía | El ADR define cobro separado después de acreditar renta y excluye la garantía del primer corte. | Comprobar el mecanismo real, responsable de fondos, devoluciones, plazos y reclamos antes de ofrecerla. |
| Retención | V82 protege la fecha de retención más restrictiva en cambios de titularidad. La evidencia F5 registra pruebas locales. La nueva regresión V82 se omite porque su guardia exige el entorno F5 y el DSN exactos. | Aprobar política por finalidad, plazo o evento inicial, excepción, actor, acción sobre datos/objetos y verificación tras restauración. Repetir en el entorno F5 autorizado si se requiere evidencia actual. |

Fuentes de proveedor: [Mercado Pago Split 1:1](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/integration-configuration/integrate-marketplace) y [SimpleFirma Empresas](https://developers.simplefirma.cl/developers).

## 3. Capacidad y recuperación

- **Restauración local ejecutada:** el ensayo `TestSyntheticRestoreRehearsalPostgres18` supera la comprobación sobre PostgreSQL/PostGIS aislado sin red, con fixture sintético y migraciones V1–V61. Verifica checksum, objetos y permisos de su alcance, operaciones espaciales y un único ganador ante solapamiento concurrente. La suite tarda 2,21 s. Ese valor corresponde a la prueba local y no se usa como RTO. Evidencia privada generada por el banco de pruebas: `tesis-1793783741/restore-evidence.json`.
- **Antecedente cloud:** el registro GCP03 conserva una restauración sintética V1–V61 con comprobaciones de esquema, ownership, disponibilidad de funciones espaciales y exclusión. Su alcance corresponde al corte histórico.
- **Verificación pendiente del entorno objetivo:** fijar versión, esquema, configuración, datos sintéticos y destino. Para PT-09, ejecutar la búsqueda con los 200 usuarios concurrentes del RNF-001 y registrar distribución de latencias, errores, duración y volumen. Para PT-11, restaurar base y objetos a destino aislado, comprobar referencias, ACL y acciones de privacidad, y medir pérdida de datos y tiempo hasta disponibilidad comprobada. Comparar con RPO de 15 minutos y RTO de 1 hora. La selección y ejecución del ensayo online quedan sujetas a la autorización específica del entorno.

El corte no usa cuentas reales ni modifica código o infraestructura del repositorio de desarrollo.
