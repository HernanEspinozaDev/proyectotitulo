#!/usr/bin/env python3
"""Aplica correcciones D11 y D12 sobre appendices/a-anexo.md"""
from pathlib import Path

anexo_a_path = Path('ES2/informe_docskill/appendices/a-anexo.md')

content = r"""# Anexo A — Decisiones de Arquitectura y Matriz Multicriterio Extendida

Este anexo compila el marco formal de decisiones técnicas de **espaciGo**. Se estructura en dos componentes fundamentales: **(A.1)** El Registro de Decisiones de Arquitectura (*Architecture Decision Records* — ADR) que documenta la evolución del sistema y su estado de vigencia, y **(A.2)** La Matriz Cuantitativa Multicriterio Extendida con el análisis comparativo detallado de alternativas tecnológicas.

---

## A.1 Registro de Decisiones de Arquitectura (ADRs)

### ADR-001: Adopción de Arquitectura Hexagonal (Ports & Adapters) en Backend Go
- **Estado**: Aceptado y Verificado en Código.
- **Fecha**: 10 de marzo de 2026.
- **Requerimientos Vinculados**: RNF-01 (Mantenibilidad), RNF-02 (Modularidad), RNF-07 (Desacoplamiento Tecnológico).

#### Contexto y Planteamiento del Problema
El backend de espaciGo orquesta integraciones con pasarelas de pago (Mercado Pago), servicios de correo transaccional (SMTP/Zoho), almacenamiento de medios en nube (Cloud Storage) y motores geoespaciales. Un acoplamiento directo entre la lógica de negocio y las librerías de infraestructura dificultaría las pruebas unitarias aisladas, impediría la sustitución de proveedores y degradaría la mantenibilidad del sistema a mediano plazo.

#### Opciones Evaluadas
1. **Arquitectura en capas tradicional (Layered)**: Controlador -> Servicio -> Repositorio. Sencilla de inicio, pero propensa a fugas de abstracción y dependencias transitivas del framework hacia el dominio.
2. **Microservicios distribuidos**: Segregación física por dominios (usuarios, reservas, pagos). Introduce sobrecarga operacional desmedida, latencia de red y transacciones distribuidas complejas innecesarias para la fase actual.
3. **Arquitectura Hexagonal (Ports & Adapters)**: El núcleo de dominio define contratos e interfaces (puertos) independientes de cualquier framework. Los adaptadores de entrada y salida implementan estas interfaces.

#### Decisión Adoptada
Se adopta **Arquitectura Hexagonal** estructurada en el paquete `internal/` de Go:
- `internal/domain/`: Entidades de negocio puras, reglas invariantes, máquinas de estado y errores centinela (sin dependencias externas).
- `internal/ports/`: Interfaces de entrada (casos de uso) e interfaces de salida (repositorios, clientes de notificación, procesadores de pago).
- `internal/adapters/`: Implementaciones concretas de puertos de salida (repositorio PostgreSQL con `pgx/v5`, cliente Mercado Pago, cliente de correo, almacenamiento).
- `internal/handlers/`: Adaptadores de entrada HTTP que validan peticiones, invocan casos de uso y serializan respuestas JSON.

#### Consecuencias Técnicas
- **Positivas**: Testabilidad unitaria completa sin requerir base de datos activa; sustituibilidad inmediata de adaptadores de infraestructura; código idiomático y mantenible.
- **Costos Mitigados**: Mayor número de interfaces intermedias, mitigado agrupando puertos por caso de uso cohesivo.

---

### ADR-002: Motor Relacional PostgreSQL 18 con PostGIS 3.6 y Exclusión Temporal GiST
- **Estado**: Aceptado y Verificado en Base de Datos.
- **Fecha**: 12 de marzo de 2026 (Actualizado a PostgreSQL 18 / PostGIS 3.6).
- **Requerimientos Vinculados**: RF-05 (Búsqueda Geoespacial), RF-07 (Prevención de Doble Reserva), RNF-04 (Integridad Transaccional ACID).

#### Contexto y Planteamiento del Problema
El sistema requiere calcular distancias esferoidales sobre el elipsoide WGS84 para resolver búsquedas por radio y cercanía. Simultáneamente, el motor debe garantizar de forma matemáticamente estricta que un espacio no sea reservado dos veces en intervalos temporales solapados bajo alta concurrencia.

#### Opciones Evaluadas
1. **Bases de datos NoSQL documentales (MongoDB Atlas)**: Soporta geoespacial básico, pero carece de restricciones de exclusión temporal atómicas a nivel de motor y garantías ACID multi-documento débiles.
2. **MySQL 8.4 (InnoDB Spatial)**: Soporta funciones espaciales 2D pero carece de tipos de rango nativos indexables con operadores de exclusión temporal GiST, obligando a sincronizar bloqueos pesados en aplicación.
3. **PostgreSQL 18 + PostGIS 3.6 + btree_gist**: Estándar industrial geoespacial (`ST_DWithin`, índices GiST). Soporta rangos temporales `tstzrange` con restricciones físicas `EXCLUDE USING gist (espacio_id WITH =, intervalo WITH &&)`.

#### Decisión Adoptada
Se adopta **PostgreSQL 18 con extensión geoespacial PostGIS 3.6 y btree_gist**. La tabla `public.ocupacion` implementa una restricción de exclusión física GiST sobre `(espacio_id WITH =, intervalo WITH &&) WHERE (activo)`, complementada con bloqueos consultivos `pg_advisory_xact_lock` durante el checkout transaccional.

#### Consecuencias Técnicas
- **Positivas**: Imposibilidad matemática de solapamiento de reservas en concurrencia (overbooking cero garantizado a nivel de motor); consultas espaciales de catálogo en menos de 15 ms.
- **Costos Mitigados**: Requisito de habilitar extensiones en la migración inicial (`CREATE EXTENSION IF NOT EXISTS postgis;` y `btree_gist`).

---

### ADR-003: Integración de Mercado Pago Checkout Pro con Split de Pagos para Custodia (Escrow)
- **Estado**: Aceptado y Diseñado con Adaptadores de Integración.
- **Fecha**: 15 de marzo de 2026.
- **Requerimientos Vinculados**: RF-08 (Procesamiento de Pagos), RF-10 (Custodia Escrow), RF-13 (Liquidación), RNF-05 (Cumplimiento PCI-DSS SAQ-A).

#### Contexto y Planteamiento del Problema
espaciGo intermedia arriendos donde los fondos deben retenerse en custodia hasta que el arrendatario realiza el check-in conforme. La plataforma no debe almacenar datos de tarjetas de crédito para mantenerse en el alcance mínimo de cumplimiento PCI-DSS SAQ-A.

#### Opciones Evaluadas
1. **Transbank Webpay Plus Tradicional**: Amplio uso en Chile pero carece de split nativo para marketplaces en modalidad estándar, exigiendo transferencias bancarias manuales posteriores.
2. **Stripe Connect**: Excelente soporte pero con presencia y costos menos favorables en el mercado local al inicio del análisis.
3. **Mercado Pago Marketplace (Checkout Pro + Split)**: Soporta cuentas conectadas mediante OAuth, redirección segura a Checkout Pro (cero exposición de tarjetas en espaciGo), retención de fondos y deducción automática de comisión.

#### Decisión Adoptada
Se adopta **Mercado Pago Checkout Pro en modalidad Split/Marketplace**. Los webhooks se reciben en `/api/v1/payments/webhook`, se valida la firma HMAC-SHA256 y se procesan de forma idempotente mediante una tabla de eventos transaccionales.

#### Consecuencias Técnicas
- **Positivas**: Cero datos de tarjeta en servidores de espaciGo (PCI-DSS SAQ-A); liquidación automatizada post check-in conforme.
- **Costos Mitigados**: Manejo de intermitencia externa mediante circuit breaker y reconciliación batch diferida.

---

### ADR-004: Evaluación de Angular con Standalone Components y Signals
- **Estado**: Superado / Prototipo Histórico (Evaluado en fase preliminar; sustituido por ADR-007 para producción).
- **Fecha**: 18 de marzo de 2026.
- **Requerimientos Vinculados**: RNF-08 (Reactividad Frontend), RNF-01 (Rendimiento), RNF-07 (Mantenibilidad UI).

#### Contexto y Planteamiento del Problema
En la fase inicial de prototipado se evaluó Angular (v18/19) para la construcción de la interfaz reactiva, evaluando componentes autónomos (*standalone*) y reactividad granular con *Signals*.

#### Dictamen de Evolución Arquitectónica
Si bien el prototipo demostró excelente reactividad cliente en paneles privados, la necesidad crítica de indexación en motores de búsqueda (SEO) para el catálogo público comercial inmobiliario y la optimización del tiempo hasta el primer byte (TTFB) motivaron la adopción de un framework con renderizado en servidor (SSR) nativo de alto rendimiento. En consecuencia, el equipo adoptó formalmente **Next.js 16 con React 19** como arquitectura definitiva de producción (ADR-007), conservando la experiencia de Signals como antecedente técnico documentado.

---

### ADR-005: Autenticación mediante Sesiones con Cookies HttpOnly y Protección CSRF
- **Estado**: Aceptado y Verificado en Seguridad.
- **Fecha**: 20 de marzo de 2026.
- **Requerimientos Vinculados**: RF-01 (Autenticación), RNF-06 (Seguridad de Sesiones, OWASP A07).

#### Contexto y Planteamiento del Problema
El almacenamiento de tokens JWT en `localStorage` o `sessionStorage` expone las credenciales a exfiltración directa mediante ataques de Cross-Site Scripting (XSS). Se requiere un mecanismo de gestión de sesiones seguro y revocable del lado del servidor.

#### Opciones Evaluadas
1. **JWT en LocalStorage**: Sin estado en el backend, pero vulnerable a robo mediante XSS y difícil de revocar de forma inmediata ante compromiso.
2. **Tokens en memoria volátil**: Seguro contra persistencia, pero se pierde la sesión en cada recarga de página.
3. **Sesiones de Servidor con Cookies HttpOnly / Secure / SameSite**: La cookie de sesión no es accesible por JavaScript en el navegador, mitigando el robo por XSS. La validez de la sesión se comprueba contra la base de datos en cada petición sensible.

#### Decisión Adoptada
Se adopta **autenticación de sesión con cookies HttpOnly, Secure y SameSite=Lax**. Cada inicio de sesión genera un identificador criptográfico aleatorio de 32 bytes persistido en `public.sesion`. Al cerrar sesión o suprimir la cuenta, la revocación es instantánea del lado del servidor.

#### Consecuencias Técnicas
- **Positivas**: Inmunidad frente a lectura de tokens vía XSS; capacidad de cierre de sesión remoto inmediato; auditoría de sesiones activas.
- **Costos Mitigados**: Consulta a base de datos por sesión mitigada mediante índices primarios rápidos y pool transaccional en Go.

---

### ADR-006: Cumplimiento de la Ley N° 21.719 mediante Arquitectura de Privacidad por Diseño
- **Estado**: Aceptado y Verificado en Privacidad.
- **Fecha**: 22 de marzo de 2026.
- **Requerimientos Vinculados**: RF-20 (Derechos ARCO), RF-21 (Supresión de Datos), RNF-06 (Cumplimiento Legal).

#### Contexto y Planteamiento del Problema
La Ley N° 21.719 sobre Protección de Datos Personales impone obligaciones estrictas de supresión, minimización y confidencialidad ante la Agencia de Protección de Datos Personales. Un problema crítico de ingeniería radica en que la restauración de respaldos de base de datos post-desastre (DRP) podría reincorporar datos de usuarios que ya habían ejercido su derecho al olvido.

#### Opciones Evaluadas
1. **Borrado físico directo (DELETE)**: Elimina datos pero no previene su reaparición si se restaura un backup antiguo.
2. **Marcado lógico (soft-delete)**: Conserva los datos personales en la base de datos, violando el principio de supresión efectiva de la ley.
3. **Anonimización Irreversible + Replay Anti-Restauración**: Se anonimizan los registros del usuario en las tablas principales y se inserta un resumen criptográfico HMAC en la tabla inmutable `usuario_eliminado_replay`. En cualquier restauración de DRP, un script automático reaplica la purga sobre los registros restaurados.

#### Decisión Adoptada
Se adopta **Anonimización Irreversible con Replay Anti-Restauración**. Los datos identificatorios se ofuscan irrevocablemente y la huella criptográfica asegura que ningún proceso de recuperación vulnere la supresión legalmente concedida.

#### Consecuencias Técnicas
- **Positivas**: Plena conformidad jurídica con la Ley N° 21.719; preservación de integridad referencial histórica en transacciones financieras pasadas.
- **Costos Mitigados**: Lógica adicional en el pipeline de restauración de respaldos, automatizada en el runbook `RB-01`.

---

### ADR-007: Adopción de Next.js 16 con React 19 y Server-Side Rendering (BFF) en Frontend de Producción
- **Estado**: Aceptado y Verificado en Frontend.
- **Fecha**: 25 de marzo de 2026 (Sustituye a ADR-004 para entorno productivo).
- **Requerimientos Vinculados**: RF-03 (Catálogo Público), RNF-01 (Rendimiento Web), RNF-08 (SEO y Accesibilidad WCAG 2.1 AA).

#### Contexto y Planteamiento del Problema
El marketplace requiere que las páginas públicas de espacios comerciales se encuentren completamente indexadas por motores de búsqueda (Google, Bing) con etiquetas OpenGraph dinámicas para captación orgánica de arrendatarios, logrando un First Contentful Paint (FCP) inferior a 1,2 segundos.

#### Opciones Evaluadas
1. **Single Page Application pura (Vite + React CSR)**: Rápido desarrollo pero nula indexación SEO inicial y exposición de rutas privadas de API al navegador.
2. **Nuxt 3 (Vue 3 SSR)**: Excelente framework SSR pero con menor ecosistema de componentes accesibles validados para estándares WCAG 2.1 AA en React.
3. **Next.js 16 (React 19 + TypeScript)**: App Router con Server Components y Server-Side Rendering (SSR) optimizado para SEO, empaquetado standalone en contenedor OCI y patrón BFF integrado para gestión segura de cookies de sesión `HttpOnly`.

#### Decisión Adoptada
Se adopta **Next.js 16 con React 19** como framework oficial de producción. Las rutas públicas se renderizan en servidor con caché perimetral, mientras que la capa BFF intermedia las solicitudes transaccionales autenticadas hacia el backend Go.

#### Consecuencias Técnicas
- **Positivas**: Indexación completa de catálogo; tiempos de carga inicial sub-segundo; tipado estricto extremo a extremo generado con `openapi-typescript`.
- **Costos Mitigados**: Requisito de ejecución de Node.js en servidor, mitigado con el empaquetado standalone liviano (< 90 MB) en Google Cloud Run.

---

## A.2 Matriz Cuantitativa Multicriterio Extendida

A continuación se detalla la evaluación multicriterio completa que sustenta la selección tecnológica de **espaciGo**. Se evalúan cuatro capas arquitectónicas bajo cinco criterios técnicos ponderados:

1. **Rendimiento y Latencia ($W_1 = 30\%$):** Concurrencia, procesamiento geoespacial y latencia P95.
2. **Seguridad por Diseño ($W_2 = 25\%$):** Superficie de ataque, tipado estricto y primitivas criptográficas.
3. **Costo Operativo Cloud ($W_3 = 20\%$):** Consumo de memoria RAM/CPU en reposo y cold start serverless.
4. **Madurez del Ecosistema ($W_4 = 15\%$):** Estabilidad de librerías, generación OpenAPI y suites de prueba.
5. **Adecuación Legal Chilena ($W_5 = 10\%$):** Trazabilidad append-only, huso horario continental y Ley 21.719.

La escala de evaluación comprende calificaciones de 1,0 (deficiente) a 5,0 (óptimo). El puntaje ponderado se calcula como $P = \sum_{i=1}^5 (C_i \times W_i)$ con redondeo aritmético a dos posiciones decimales.

### A.2.1 Capa 1: Backend Core y Servicios Asíncronos

| Alternativa Evaluada | Rendimiento (30%) | Seguridad (25%) | Costo Cloud (20%) | Ecosistema (15%) | Dominio Legal (10%) | Puntaje Ponderado | Dictamen Técnico Detallado |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **Go 1.27 (`net/http` + `pgx/v5`) [Seleccionada]** | **5,0** | **5,0** | **5,0** | **4,5** | **5,0** | **4,93** | Binario estático ELF compilado sin runtime pesado; consumo basal < 25 MB RAM. Goroutines nativas permiten miles de conexiones concurrentes para reservas y búsquedas geoespaciales sin saturación de hilos. Soporte nativo de `pgxpool` con transacciones ACID directas. |
| Alternativa A: Node.js 22 (NestJS + Prisma) | 3,5 | 4,0 | 3,8 | 4,8 | 4,0 | 3,93 | Gran ecosistema npm y productividad inicial. Sin embargo, el bucle de eventos monohilo (*event loop*) sufre bloqueos ante tareas intensivas de CPU (procesamiento de imágenes WebP y foliado criptográfico de contratos PDF). Mayor huella basal de memoria (> 180 MB por instancia). |
| Alternativa B: Java 21 LTS (Spring Boot 3 + Hibernate) | 4,5 | 4,8 | 3,0 | 4,5 | 4,8 | **4,31** | Robusto tipado y ecosistema empresarial maduro. No obstante, el tiempo de arranque en frío (*cold start*) en contenedores serverless supera los 4 segundos y la huella basal en reposo excede los 250 MB RAM, encareciendo sensiblemente el escalado automático cloud. (Cálculo exacto: $4,5 \times 0,30 + 4,8 \times 0,25 + 3,0 \times 0,20 + 4,5 \times 0,15 + 4,8 \times 0,10 = 1,35 + 1,20 + 0,60 + 0,675 + 0,48 = 4,305 \rightarrow \mathbf{4,31}$). |

### A.2.2 Capa 2: Frontend Web y Capa BFF

| Alternativa Evaluada | Rendimiento (30%) | Seguridad (25%) | Costo Cloud (20%) | Ecosistema (15%) | Dominio Legal (10%) | Puntaje Ponderado | Dictamen Técnico Detallado |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **Next.js 16 (React 19 + TypeScript) [Seleccionada]** | **4,8** | **5,0** | **4,5** | **5,0** | **4,8** | **4,82** | App Router con Server Components y Server-Side Rendering (SSR). Indexación SEO inmediata del catálogo de espacios comerciales en buscadores. Capa BFF integrada que aísla tokens y secretos del cliente mediante cookies `HttpOnly`. Empaquetado standalone liviano para Docker. |
| Alternativa A: SPA React pura (Vite CSR) | 3,5 | 4,2 | 4,8 | 4,5 | 3,8 | 4,12 | Excelente velocidad de desarrollo y bajo costo de alojamiento estático. Sin embargo, carece de renderizado en servidor, impidiendo la indexación orgánica en Google del catálogo comercial y exponiendo endpoints de backend a llamadas directas sin intermediación BFF. |
| Alternativa B: Nuxt 3 (Vue 3 + Nitro) | 4,5 | 4,3 | 4,4 | 4,0 | 4,2 | **4,33** | Sólido soporte SSR y empaquetado optimizado sobre Nitro. No obstante, la disponibilidad de librerías accesibles certificadas para estándares WCAG 2.1 AA es menor en comparación con el ecosistema React/Radix. (Cálculo exacto: $4,5 \times 0,30 + 4,3 \times 0,25 + 4,4 \times 0,20 + 4,0 \times 0,15 + 4,2 \times 0,10 = 1,35 + 1,075 + 0,88 + 0,60 + 0,42 = 4,325 \rightarrow \mathbf{4,33}$). |

### A.2.3 Capa 3: Persistencia Relacional y Geoespacial

| Alternativa Evaluada | Rendimiento (30%) | Seguridad (25%) | Costo Cloud (20%) | Ecosistema (15%) | Dominio Legal (10%) | Puntaje Ponderado | Dictamen Técnico Detallado |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **PostgreSQL 18 + PostGIS 3.6 (`btree_gist`) [Seleccionada]** | **5,0** | **5,0** | **4,5** | **5,0** | **5,0** | **4,90** | Soporte estricto de restricciones físicas de exclusión temporal GiST (`tstzrange`) que imposibilitan overbooking a nivel de motor. Extensión PostGIS 3.6 para cálculo de distancias esferoidales (`ST_DWithin`). Plena conformidad ACID y soporte nativo de auditoría inmutable. |
| Alternativa A: MongoDB Atlas (NoSQL) | 3,8 | 3,0 | 3,5 | 4,2 | 2,5 | 3,47 | Flexibilidad en documentos JSON y escalado horizontal. Sin embargo, carece de tipos de rango temporales continuos nativos indexables con exclusión y no garantiza aislamiento transaccional estricto ante solapamiento concurrente de reservas. |
| Alternativa B: MySQL 8.4 (InnoDB Spatial) | 4,2 | 4,0 | 4,5 | 4,5 | 3,8 | 4,22 | Motor relacional ampliamente difundido con soporte espacial 2D. No obstante, no soporta restricciones de exclusión GiST sobre intervalos temporales, forzando a delegar la prevención de colisiones en bloqueos pesados a nivel de aplicación. |

### A.2.4 Capa 4: Infraestructura Cloud y Orquestación

| Alternativa Evaluada | Rendimiento (30%) | Seguridad (25%) | Costo Cloud (20%) | Ecosistema (15%) | Dominio Legal (10%) | Puntaje Ponderado | Dictamen Técnico Detallado |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **Google Cloud Run + Cloud SQL (Santiago) [Seleccionada]** | **4,8** | **5,0** | **4,8** | **4,7** | **5,0** | **4,86** | Despliegue en región chilena `southamerica-west1` (Santiago) con latencias sub-20 ms a usuarios nacionales. Conexión privada Serverless VPC Access hacia Cloud SQL sin IP pública. Escalado automático a cero y costos predecibles. (Cálculo exacto: $4,8 \times 0,30 + 5,0 \times 0,25 + 4,8 \times 0,20 + 4,7 \times 0,15 + 5,0 \times 0,10 = 1,44 + 1,25 + 0,96 + 0,705 + 0,50 = 4,855 \rightarrow \mathbf{4,86}$). |
| Alternativa A: Google Kubernetes Engine (GKE Autopilot) | 4,8 | 4,8 | 2,5 | 3,5 | 4,8 | 4,15 | Máxima flexibilidad de orquestación y portabilidad OCI. Sin embargo, introduce un costo fijo mensual de plano de control y una complejidad operativa injustificada para una topología acotada de dos servicios web y base de datos relacional. |
| Alternativa B: AWS ECS Fargate + RDS PostgreSQL | 4,5 | 4,8 | 3,8 | 4,5 | 4,5 | **4,44** | Excelente madurez de servicios serverless de contenedores. No obstante, al momento de la evaluación no contaba con zona local completa con paridad de servicios serverless gestionados en Santiago de Chile con facturación y soporte local comparable. (Cálculo exacto: $4,5 \times 0,30 + 4,8 \times 0,25 + 3,8 \times 0,20 + 4,5 \times 0,15 + 4,5 \times 0,10 = 1,35 + 1,20 + 0,76 + 0,675 + 0,45 = 4,435 \rightarrow \mathbf{4,44}$). |
"""

anexo_a_path.write_text(content.strip() + '\n', encoding='utf-8')
print(f'Actualizado {anexo_a_path} exitosamente ({len(content)} caracteres).')
