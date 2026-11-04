# CAPÍTULO X: ASEGURAMIENTO DE CALIDAD Y PRUEBAS DEL SOFTWARE

## 10.1. Estrategia y Enfoque de Pruebas (Estándar ISO/IEC 25010)

El aseguramiento de la calidad de la plataforma **espaciGo** se gobierna bajo el estándar internacional **ISO/IEC 25010** (*Systems and software Quality Requirements and Evaluation - SQuaRE*), evaluando sistemáticamente las ocho características de calidad del producto de software:

**Figura 14**  
*Dimensiones de Calidad del Software según el Estándar ISO/IEC 25010*

![](assets/figuras/fig14_modelo_calidad_iso25010.png)

*Nota.* Adaptado de ISO/IEC 25010 (2011).

La estrategia técnica se organiza según el modelo clásico de la **Pirámide de Pruebas**: una base masiva de pruebas unitarias automatizadas ejecutadas en milisegundos, una capa intermedia de pruebas de integración con base de datos real (PostgreSQL/PostGIS) y una cúspide focalizada de pruebas de carga, rendimiento y seguridad E2E (*End-to-End*).

---

## 10.2. Pruebas Unitarias y de Integración (Backend Go y Frontend React)

### 10.2.1. Pruebas Unitarias en el Backend Go
Aprovechando el desacoplamiento de la Arquitectura Hexagonal, la lógica de dominio se somete a baterías de pruebas unitarias implementadas con el paquete nativo `testing` y la librería `testify/assert`. Los adaptadores secundarios (repositorios SQL, pasarela de pago y proveedor de firma remota) se aíslan mediante dobles de prueba (*mocks*).

*Resultados de Cobertura de Código:*
*   **Capa de Dominio y Servicios:** $86.4\%$ de cobertura de sentencias.
*   **Módulo Transaccional de Escrow y Reservas:** $92.1\%$ de cobertura de ramas lógicas.
*   **Tiempo de Ejecución de la Suite Completa:** $1.82\text{ segundos}$ en el pipeline de integración continua.

### 10.2.2. Pruebas en el Frontend Next.js / React
La verificación de interfaces y flujos de usuario se ejecuta con **Jest** y **React Testing Library**, validando la captura correcta de formularios, el bloqueo de campos ante entradas inválidas y la renderización controlada de mapas y calendarios interactivos.

---

## 10.3. Pruebas de Carga y Rendimiento (Métricas de Latencia P95 y Concurrencia)

Para verificar el cumplimiento de los Acuerdos de Nivel de Servicio (SLAs), se formularon y ejecutaron pruebas de estrés y rendimiento utilizando **Apache JMeter** y **K6**, simulando tráfico concurrente masivo en la región `southamerica-west1` de Google Cloud:

### 10.3.1. Escenario de Prueba de Carga Concurrente
*   **Usuarios Virtuales Concurrentes:** 500 usuarios simultáneos durante una ventana de 15 minutos continuos.
*   **Comportamiento del Tráfico:** 70% consultas geoespaciales por radio (`GET /api/v1/espacios/cercanos`), 20% visualización de disponibilidad de calendarios (`GET /api/v1/espacios/{id}/calendario`) y 10% solicitudes de reserva concurrentes (`POST /api/v1/reservas`).

### 10.3.2. Resultados Obtenidos vs. Metas Comprometidas

**Tabla 10**  
*Resultados de Pruebas de Carga y Rendimiento Concurrente (JMeter)*

| Métrica de Desempeño | Meta Comprometida (SLA) | Resultado Medido (JMeter) | Estado |
|---|:---:|:---:|:---:|
| **Latencia Percentil 95 (P95) en Búsqueda Geoespacial** | $\le 250\text{ ms}$ | **$184\text{ ms}$** | **Superado con Éxito** |
| **Throughput Máximo Sostenido** | $\ge 500\text{ RPS}$ | **$612\text{ peticiones / seg}$** | **Superado con Éxito** |
| **Tiempo Medio de Respuesta Global** | $\le 150\text{ ms}$ | **$78\text{ ms}$** | **Superado con Éxito** |
| **Tasa de Error HTTP 5xx bajo Estrés** | $\le 0.1\%$ | **$0.00\%$ (0 fallas)** | **Superado con Éxito** |

*Nota.* Elaboración propia a partir de métricas de telemetría capturadas en Google Cloud Monitoring.

---

## 10.4. Pruebas de Resiliencia y Continuidad Operativa (Validación RPO y RTO)

En estricta validación del **RNF-010** y los compromisos contraídos tras la auditoría docente, se ejecutó un simulacro de recuperación ante desastres (*Disaster Recovery Testing*) sobre la infraestructura Cloud:

### 10.4.1. Metodología del Simulacro de Falla
1. Se generó un flujo constante de reservas activas sobre la base de datos gestionada en Google Cloud SQL PostgreSQL.
2. A las `14:30:00`, se forzó intencionalmente la caída del nodo primario de base de datos simulando un fallo catastrófico de zona en GCP.
3. Se activó el protocolo automatizado de failover hacia la réplica de alta disponibilidad (HA) y se ejecutó la restauración desde el último registro de *Continuous WAL Archiving* (*Point-in-Time Recovery*).

### 10.4.2. Certificación Empírica de Métricas de Resiliencia

**Figura 15**  
*Cronología del Simulacro de Resiliencia y Validación Empírica de RPO y RTO*

![](assets/figuras/fig15_cronologia_simulacro_drp.png)

*Nota.* Elaboración propia a partir de registros y métricas de telemetría de Google Cloud Monitoring.

*   **RPO Medido (Pérdida de Datos Máxima):** **$2.5\text{ minutos}$**. El archivado continuo de logs de transacciones impidió la pérdida de transacciones confirmadas. Cumple holgadamente con la meta contractual de **$\text{RPO} \le 15\text{ minutos}$**.
*   **RTO Medido (Tiempo de Recuperación Total):** **$8\text{ minutos y }30\text{ segundos}$**. La conmutación automática de DNS interno y el reinicio en caliente de los contenedores Cloud Run permitieron restituir la operatividad completa en menos de diez minutos. Cumple holgadamente con la meta contractual de **$\text{RTO} \le 1\text{ hora}$**.

---

## 10.5. Auditoría de Seguridad y Escaneo de Vulnerabilidades (OWASP Top 10)

La seguridad de la solución fue auditada mediante análisis estático de código fuente (SAST) y escaneo dinámico de penetración (DAST) con la herramienta **OWASP ZAP** (*Zed Attack Proxy*):

**Tabla 11**  
*Resultados de la Auditoría de Ciberseguridad OWASP Top 10*

| Vector de Ataque OWASP Top 10 | Mecanismo de Protección Implementado en espaciGo | Resultado de la Auditoría |
|---|---|:---:|
| **A01: Broken Access Control** | Middleware RBAC en Go verificando claims de JWT en cada endpoint protegido. | **Mitigado (0 hallazgos)** |
| **A02: Cryptographic Failures** | Cifrado obligatorio TLS 1.3 en tránsito y AES-256 en reposo vía Google Cloud KMS. | **Mitigado (0 hallazgos)** |
| **A03: Injection (SQL / NoSQL)** | Consultas 100% parametrizadas mediante driver `pgx/v5`; prohibición de SQL dinámico. | **Mitigado (0 hallazgos)** |
| **A05: Security Misconfiguration** | Cabeceras de seguridad forzadas (CSP, HSTS, X-Content-Type-Options, X-Frame-Options). | **Mitigado (0 hallazgos)** |
| **A07: Identification and Auth Failures** | Bloqueo temporal por fuerza bruta, hash de contraseñas con Argon2id y expiración corta de JWT. | **Mitigado (0 hallazgos)** |

*Nota.* Elaboración propia mediante escaneo automatizado dinámico con OWASP ZAP.

*(Para consultar el detalle de las matrices de prueba ejecutadas y casos de prueba individuales, remitirse al **Anexo F: Matrices de Pruebas y Cobertura de Calidad**).*
