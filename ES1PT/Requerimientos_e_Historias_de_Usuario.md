# Levantamiento de Requerimientos - espaciGo
*(Documento adaptado a los lineamientos de Actividad 4 y Actividad 7 - Estándar IEEE 830, ISO/IEC 25010 y Sommerville)*

## 1. Módulos Funcionales del Sistema
| ID | Descripción |
|---|---|
| 01 | Módulo de Identidad y Seguridad Legal (KYC/KYB) |
| 02 | Módulo de Catálogo y Reservas |
| 03 | Módulo de Generación y Legalización de Contratos |
| 04 | Módulo Financiero, Escrow y Trazabilidad (FinTech) |

## 2. Actores del Sistema
| ID | Descripción | Responsabilidad, Funciones o actividades |
|---|---|---|
| **ACT1** | Arrendador (Propietario / B2B) | Publicar espacios, configurar tarifas/calendario, aprobar reservas, firmar contratos, solicitar retiros de fondos, seleccionar modelo de liquidez. |
| **ACT2** | Arrendatario (Usuario / B2C) | Buscar espacios, pagar reservas (Escrow), subir fotos de check-in/out, firmar contratos remotos, calificar espacios. |
| **ACT3** | Administrador de Plataforma | Auditar logs transaccionales, resolver disputas con evidencia fotográfica, gestionar devoluciones de garantías. |
| **ACT4** | Sistema Core (Backend) | Enrutar firmas legales (FEA vs ANF), ejecutar *Split Payments*, enviar logs a BigQuery asíncronamente. |

---

## 3. Requerimientos Funcionales (RF)
*Redactados bajo el formato formal: "El sistema debe permitir [verbo] + [acción]", alineado a buenas prácticas.*

| ID REQ | Módulo | Descripción del requerimiento |
|---|---|---|
| **REQF1.1** | 01 | El sistema debe permitir **registrar** una cuenta de usuario unificada manejada mediante JWT. |
| **REQF1.2** | 01 | El sistema debe permitir **validar** la Cédula de Identidad chilena mediante consumo de API externa (KYC). |
| **REQF1.3** | 01 | El sistema debe permitir **validar** el giro comercial de empresas (SII) para verificar aptitud inmobiliaria (KYB). |
| **REQF1.4** | 01 | El sistema debe permitir **solicitar** la eliminación y anonimización de los datos de la cuenta (Derecho al olvido). |
| **REQF2.1** | 02 | El sistema debe permitir **publicar** un espacio inyectando fotos, dimensiones, tipo de uso y reglas. |
| **REQF2.2** | 02 | El sistema debe permitir **bloquear** fechas y horas en un calendario interactivo para evitar sobre-reservas. |
| **REQF2.3** | 02 | El sistema debe permitir **buscar** espacios mediante un mapa geolocalizado interactivo aplicando filtros. |
| **REQF2.4** | 02 | El sistema debe permitir **aprobar** o rechazar solicitudes de reserva recibidas dentro de un límite de tiempo. |
| **REQF3.1** | 03 | El sistema debe permitir **generar** dinámicamente un contrato PDF inyectando variables transaccionales en una plantilla. |
| **REQF3.2** | 03 | El sistema debe permitir **editar** colaborativamente cláusulas del borrador de contrato antes de su congelamiento. |
| **REQF3.3** | 03 | El sistema debe permitir **enviar** el documento final a FirmaVirtual para su firma (FEA o ANF). |
| **REQF4.1** | 04 | El sistema debe permitir **retener** los fondos del pago inicial en una bóveda de custodia digital (Escrow). |
| **REQF4.2** | 04 | El sistema debe permitir **bloquear** un cupo en la tarjeta de crédito del arrendatario por concepto de garantía (Pre-autorización). |
| **REQF4.3** | 04 | El sistema debe permitir **liberar** automáticamente los fondos al arrendador (Payout) descontando la comisión. |
| **REQF4.4** | 04 | El sistema debe permitir **seleccionar** la preferencia de dispersión del dinero (Liquidez inmediata vs diferida). |
| **REQF4.5** | 04 | El sistema debe permitir **subir** fotografías de evidencia para realizar el check-in y check-out del espacio. |

---

## 4. Requerimientos No Funcionales (RNF)

### 4.1 Clasificación Norma ISO/IEC 25010 (Calidad del Producto)
| ID REQ | Nombre del Requerimiento | Categoría (ISO 25010) | Descripción |
|---|---|---|---|
| **RNF1** | Encriptación de Bóveda | Seguridad / Confidencialidad | El sistema debe resguardar contratos y carpetas tributarias en buckets de almacenamiento cifrado y servirlos mediante *Signed URLs* efímeras. |
| **RNF2** | Transacciones ACID | Fiabilidad / Tolerancia a fallos | El sistema debe utilizar bases de datos relacionales (PostgreSQL) para garantizar que ante un fallo, los pagos no se descuadren (Rollback). |
| **RNF3** | Tiempos de Búsqueda | Rendimiento / Eficiencia | El sistema debe renderizar el mapa de resultados geolocalizados en un tiempo inferior a 2.5 segundos. |
| **RNF4** | Alta Concurrencia | Rendimiento / Capacidad | El sistema backend (Golang) debe manejar peticiones simultáneas de pagos y firmas sin bloquear los hilos principales (*Goroutines*). |
| **RNF5** | Responsividad Web | Usabilidad / Operabilidad | El sistema debe proveer una interfaz adaptable a móviles (Next.js) que permita concretar una reserva en menos de 4 pasos. |

### 4.2 Clasificación de Sommerville
| ID REQ | Tipo (Sommerville) | Nombre | Descripción |
|---|---|---|---|
| **RNF6** | Legislativo (Externo) | Cumplimiento Ley 21.719 (Privacidad) | El sistema debe almacenar logs inmutables y asíncronos en BigQuery de cada acción del usuario para responder a auditorías legales. |
| **RNF7** | Legislativo (Externo) | Cumplimiento Ley 21.461 (Arriendos) | El sistema debe forzar firmas notariales online (ANF) cuando los arriendos superen un umbral de riesgo, para asegurar viabilidad de desalojo. |
| **RNF8** | Organizacional | Optimización de Costos (FinOps) | La arquitectura Cloud debe ser desplegada mediante servicios *Serverless* (Cloud Run) para evitar exceder los $300 USD de presupuesto estudiantil. |
| **RNF9** | Implementación | Consistencia DevOps (Docker) | El sistema debe estar 100% contenerizado para garantizar que los entornos locales de los 3 estudiantes funcionen idénticamente. |
| **RNF10** | Entrega | Integración Continua (CI/CD) | El sistema debe utilizar GitHub Actions para automatizar las pruebas y despliegues a Google Cloud en cada *Merge* a la rama de producción. |

---

## 5. Priorización de Casos de Uso (Ejecución)
Relación y orden para el desarrollo de la aplicación.

| ID CU | Nombre del Caso de Uso | Prioridad | Dificultad | Asignado a |
|---|---|---|---|---|
| **CU01** | Publicar y configurar espacio comercial | Alta | Media | Anita Marchant (Next.js) / Hernán Espinoza (BD) |
| **CU02** | Buscar y solicitar reserva de espacio | Alta | Media | Anita Marchant (Next.js) |
| **CU03** | Procesar validaciones legales (KYC/KYB) | Alta | Alta | Erick Silva (APIs) |
| **CU04** | Procesar pago y retener fondos (Escrow) | Alta | Alta | Erick Silva (APIs) / Hernán Espinoza (BD) |
| **CU05** | Generar y firmar contrato remoto dinámico | Media | Alta | Hernán Espinoza (Gotenberg) / Erick Silva (FirmaVirtual) |
| **CU06** | Subir fotos de Check-in y liberar pagos | Media | Media | Anita Marchant (UI) / Erick Silva (Payouts) |
| **CU07** | Auditar logs asíncronos en BigQuery | Baja | Baja | Hernán Espinoza (GCP BigQuery) |
