# CAPÍTULO VII: ESPECIFICACIÓN DE REQUERIMIENTOS Y NIVELES DE SERVICIO

## 7.1. Identificación de Actores y Módulos del Sistema

La especificación de requerimientos de la plataforma **espaciGo** se articula en torno a la interacción de cuatro actores principales (tres roles humanos y un componente de integración externo), distribuidos a través de siete módulos funcionales:

**Figura 6**  
*Diagrama de Interacción entre Actores y Módulos de la Plataforma*

![](assets/figuras/fig06_actores_modulos_sistema.png)

*Nota.* Elaboración propia en base a la arquitectura modular de la plataforma espaciGo.

---

## 7.2. Síntesis Ejecutiva de Requerimientos Funcionales (IEEE 830)

La ingeniería de requerimientos del proyecto levantó y formalizó un total de **236 Requerimientos Funcionales (RF)**, estructurados rigurosamente bajo el estándar IEEE 830 y redactados mediante verbos atómicos (*"El sistema debe [verbo] [objeto]"*).

Para preservar la fluidez analítica del cuerpo principal y en estricta conformidad con las pautas de evaluación docente, la totalidad de los 236 requerimientos se respalda en el **Anexo A: Especificación Detallada de Requerimientos (IEEE 830)**, presentando a continuación su distribución por subsistema funcional:

**Tabla 7**  
*Distribución de Requerimientos Funcionales (IEEE 830) por Módulo de Software*

| Módulo Funcional | Código Base | Cantidad de RF | Descripción del Alcance Técnico |
|---|:---:|:---:|---|
| **M1: Identidad y Seguridad** | `RF-001` al `RF-038` | 38 | Registro de usuarios, autenticación multifactor (MFA), verificación KYC (cédula) y KYB (RUT de empresa ante el SII), gestión de roles y permisos RBAC. |
| **M2: Gestión de Espacios** | `RF-039` al `RF-076` | 38 | Alta, edición y categorización de espacios, carga y optimización de galerías fotográficas, configuración de tarifas por hora/día y reglas de uso. |
| **M3: Búsqueda Geoespacial** | `RF-077` al `RF-104` | 28 | Consultas espaciales por radio (`ST_DWithin`), filtrado facetado por características físicas, renderizado de mapas interactivos y ordenamiento por relevancia. |
| **M4: Reservas y Calendarios** | `RF-105` al `RF-142` | 38 | Gestión de disponibilidad en tiempo real, bloqueos automáticos con rangos `tsrange`, cotización dinámica, políticas de cancelación y reintentos. |
| **M5: Pagos y Custodia Escrow** | `RF-143` al `RF-174` | 32 | Integración con pasarela de pago, ejecución de *split payments*, retención fiduciaria en bóveda digital, bloqueo y liberación de garantías, liquidación a propietarios. |
| **M6: Contratos Digitales** | `RF-175` al `RF-204` | 30 | Inyección dinámica de variables contractuales, generación de contratos PDF, despacho hacia proveedor de firma electrónica remota y archivado seguro cifrado. |
| **M7: Evidencias y Disputas** | `RF-205` al `RF-236` | 32 | Captura de fotografías con marcas de tiempo en *Check-in* y *Check-out*, levantamiento de reclamos por daños, chat interno probatorio y panel de arbitraje. |
| **TOTAL** | — | **236 RF** | *(Ver catálogo completo en Anexo A)* |

*Nota.* Elaboración propia. La totalidad de los 236 requerimientos se detalla en el Anexo A.

*(Adicionalmente, la trazabilidad de interacción ágil se respalda en el **Anexo B: 35 Historias de Usuario con Criterios INVEST** y el modelado analítico en el **Anexo C: 52 Fichas Técnicas de Casos de Uso**).*

---

## 7.3. Especificación de Requerimientos No Funcionales (RNF)

El sistema define **43 Requerimientos No Funcionales** que gobiernan la seguridad, el rendimiento, la disponibilidad y la resiliencia operativa.

### 7.3.1. Requerimiento Crítico RNF-010: Continuidad Operativa y Respaldo de Base de Datos

En atención directa a las observaciones docentes de optimización de resiliencia y el compromiso de ingeniería Cloud:

> **RNF-010 — Resiliencia y Continuidad Operativa de Persistencia:**  
> *"El sistema contempla una política de continuidad operativa automatizada en Google Cloud Platform. Para la persistencia de datos (OLTP en PostgreSQL 18), se configuran respaldos automáticos incrementales y copias de seguridad continuas (Continuous WAL Archiving) que garantizan un Objetivo de Punto de Recuperación (RPO) no mayor a 15 minutos. Asimismo, ante una contingencia de infraestructura crítica, el despliegue contenerizado gestionado (Google Cloud Run) y la automatización de réplicas permiten la restauración y levantamiento de los servicios con un Objetivo de Tiempo de Recuperación (RTO) máximo de 1 hora."*

---

## 7.4. Matriz de Niveles de Servicio (SLAs)

Los Acuerdos de Nivel de Servicio (*Service Level Agreements*) formalizan los compromisos de calidad cuantificables que la plataforma garantiza ante sus usuarios:

**Tabla 8**  
*Matriz de Compromisos y Acuerdos de Nivel de Servicio (SLAs)*

| Parámetro de Servicio | Indicador Métrico | Meta Comprometida (SLA) | Estrategia de Aseguramiento Tecnológico |
|---|---|:---:|---|
| **Disponibilidad de Servicio** | Uptime mensual | **$\ge 99.9\%$** | Arquitectura contenerizada en Google Cloud Run con escalado automático multi-zona y balanceador de carga global HTTPS con Cloud CDN. |
| **Objetivo de Punto de Recuperación** | **RPO** | **$\le 15\text{ minutos}$** | Respaldos continuos de archivos WAL (*Write-Ahead Logging*) y *Point-in-Time Recovery* (PITR) automatizado en Google Cloud SQL PostgreSQL. |
| **Objetivo de Tiempo de Recuperación** | **RTO** | **$\le 1\text{ hora}$** | Infraestructura como Código (IaC), contenedores preconstruidos en Artifact Registry y failover gestionado de base de datos. |
| **Latencia de Respuesta API** | Tiempo de respuesta P95 | **$\le 250\text{ ms}$** | Backend compilado en Go nativo con pool de conexiones optimizado (`pgx/v5`) e índices espaciales GiST en memoria RAM. |
| **Seguridad de Comunicaciones** | Cifrado en tránsito | **100% TLS 1.3** | Terminación TLS en Google Cloud Load Balancing con certificados SSL/TLS gestionados automáticamente y HSTS forzado. |
| **Seguridad de Almacenamiento** | Cifrado en reposo | **AES-256** | Cifrado transparente de discos persistentes en Cloud SQL y buckets de Cloud Storage con claves gestionadas por Google Cloud KMS. |

*Nota.* Elaboración propia conforme a los acuerdos de servicio y capacidades de Google Cloud Platform (2024).

---

## 7.5. Indicadores Clave de Rendimiento (KPIs) del Negocio y del Sistema

Subsanando de raíz el error diagnosticado en la pauta docente (donde se habían listado avances de tareas documentales como KPIs), se establecen a continuación los verdaderos **Indicadores Clave de Rendimiento** orientados al impacto operacional y al rendimiento del software:

### 7.5.1. KPIs del Negocio Inmobiliario (Impacto Operacional)
1. **Tasa de Conversión de Búsqueda a Reserva:**  
   *Fórmula de Medición:* `Tasa Conversión = (Reservas Confirmadas / Sesiones de Búsqueda Activas) * 100` (Meta: $\ge 12.5\%$).
2. **Tiempo Promedio de Colocación de Espacios Ociosos:**  
   Reducción del tiempo que un espacio nuevo tarda en registrar su primera reserva, disminuyendo desde los 90 días tradicionales del corretaje analógico a una meta de **$\le 7\text{ días}$** en la plataforma.
3. **Tasa de Eficacia en Resolución de Disputas:**  
   Porcentaje de reclamos resueltos mediante evidencia fotográfica objetiva sin requerir arbitraje judicial externo, con una meta de **$\ge 95.0\%$**.
4. **Índice de Satisfacción Neta del Usuario (CSAT):**  
   Calificación promedio bilateral otorgada por arrendadores y arrendatarios al finalizar la estadía: **$\ge 4.6\text{ / }5.0$**.

### 7.5.2. KPIs Técnicos de Ingeniería de Software
1. **Throughput de Capacidad Concurrente:**  
   Capacidad de procesamiento del backend Go sin degradación: **$\ge 500\text{ peticiones por segundo (RPS)}$**.
2. **Latencia P95 de Consultas Geoespaciales:**  
   Tiempo de respuesta en búsquedas complejas por radio y filtros combinados: **$\le 200\text{ ms}$**.
3. **Tasa de Error en Pasarela de Pagos (*Payment Failure Rate*):**  
   Porcentaje de transacciones fallidas atribuibles a fallas de integración o *timeouts*: **$\le 0.5\%$**.
4. **Tasa de Cobertura de Pruebas Unitarias y de Integración:**  
   Porcentaje de líneas y ramas de lógica crítica de dominio cubiertas por tests automatizados: **$\ge 80.0\%$**.
