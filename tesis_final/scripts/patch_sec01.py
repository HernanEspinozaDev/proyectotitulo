#!/usr/bin/env python3
"""Aplica correcciones D11 y D02 sobre sections/01-tecnologias.md"""
from pathlib import Path

sec01_path = Path('ES2/informe_docskill/sections/01-tecnologias.md')

content = """# 1. Detalle de las Tecnologías a Implementar

## 1.1 Análisis cualitativo y cuantitativo de tecnologías

La selección tecnológica de la plataforma **espaciGo** responde a las exigencias operativas, transaccionales, geoespaciales y regulatorias inherentes a un mercado digital de dos lados (*two-sided marketplace*) para el arriendo flexible de espacios comerciales y profesionales por hora, día y mes en Chile. El sistema actúa como plataforma mediadora y de orquestación transaccional técnica: descubre inventario georreferenciado en mapas interactivos, previene matemáticamente colisiones de agenda mediante exclusión temporal en base de datos, orquesta la retención condicional de pagos a través de pasarelas adquirentes autorizadas, compila contratos de arriendo en PDF con hash inmutable y ejecuta la anonimización de datos personales bajo la Ley N° 21.719.

Desde una perspectiva cualitativa y metodológica, la evaluación de alternativas se estructuró sobre cuatro capas arquitectónicas fundamentales: **(i) Backend Core y Servicios Asíncronos**, **(ii) Frontend Web y Capa BFF (*Backend for Frontend*)**, **(iii) Motor de Persistencia Relacional y Geoespacial**, y **(iv) Plataforma Cloud e Infraestructura como Código (IaC)**. Para cada capa se definieron cinco criterios técnicos ponderados:

1. **Rendimiento, latencia y concurrencia ($W_1 = 30\%$):** Capacidad de sostener búsquedas geoespaciales sub-250 ms en percentil 95 (P95), procesar imágenes WebP sin saturar hilos y serializar reservas concurrentes sin condiciones de carrera.
2. **Seguridad por diseño y tipado estricto ($W_2 = 25\%$):** Superficie de ataque mínima en contenedores, aislamiento entre capas, verificación estricta de tipos y soporte nativo de algoritmos criptográficos (`bcrypt`, `HMAC-SHA256`, `AES-256-GCM`).
3. **Costo operativo cloud y huella de recursos ($W_3 = 20\%$):** Consumo basal de memoria RAM y CPU en reposo, velocidad de arranque en frío (*cold start*) en modelos serverless y previsibilidad de costos operativos mensuales.
4. **Madurez del ecosistema y mantenibilidad ($W_4 = 15\%$):** Disponibilidad de librerías estables, herramientas de generación de código a partir de especificaciones `OpenAPI 3.1` y soporte robusto de pruebas automatizadas.
5. **Adecuación al dominio legal y normativo chileno ($W_5 = 10\%$):** Capacidad para implementar auditoría forense inmutable (*append-only*), cálculo temporal sobre huso horario continental de Chile (`America/Santiago`) y mecanismos deterministas de supresión de datos.

La ponderación final se calcula mediante la fórmula lineal estándar de agregación multicriterio: **Puntaje Ponderado = ∑ (Puntaje Criterio_i × W_i)** (para $i = 1 \dots 5$), donde la escala de evaluación comprende notas de 1,0 (deficiente) a 5,0 (óptimo), aplicando redondeo aritmético a dos posiciones decimales. A fin de optimizar la legibilidad y evitar fragmentación de columnas en el cuerpo principal, la **Tabla 1** presenta la síntesis ejecutiva de la evaluación multicriterio (el desglose extendido con las matrices analíticas de ocho columnas, criterios parciales y sensibilidad se documenta íntegramente en el **Anexo A.2**):

**Tabla 1.** Síntesis de evaluación cuantitativa multicriterio de alternativas tecnológicas.

| Capa Tecnológica | Solución Adoptada | Puntaje | Alternativas Evaluadas y Dictamen de Selección |
|---|---|:---:|---|
| **1. Backend Core** | **Go 1.27 (`net/http` + `pgx/v5`)** | **4,93** | Supera a **Java 21 LTS (4,31)** y **Node.js 22 (3,93)**. Binario estático compilado (< 25 MB RAM en reposo), goroutines nativas para alta concurrencia transaccional y pool `pgx` optimizado. Java penaliza por huella de memoria (> 250 MB) y Node.js por bloqueo de event loop en compresión pesada de imágenes. |
| **2. Frontend Web y BFF** | **Next.js 16 (React 19 + TypeScript)** | **4,82** | Supera a **Nuxt 3 (4,33)** y **SPA React pura (4,12)**. Soporte nativo de Server-Side Rendering (SSR) esencial para SEO e indexación de catálogo comercial, empaquetado standalone, tipado estricto con OpenAPI y manejo seguro de cookies `HttpOnly` en capa BFF. |
| **3. Persistencia Relacional** | **PostgreSQL 18 + PostGIS 3.6 (`btree_gist`)** | **4,90** | Supera a **MySQL 8.4 (4,22)** y **MongoDB Atlas (3,47)**. Soporte estricto de restricciones físicas de exclusión temporal GiST (`tstzrange`) para overbooking cero, tipos espaciales geodésicos nativos y transacciones ACID completas con bloqueo consultivo. |
| **4. Infraestructura Cloud** | **Google Cloud Run + Cloud SQL (Santiago)** | **4,86** | Supera a **AWS ECS Fargate (4,44)** y **GKE Autopilot (4,15)**. Región local `southamerica-west1` (latencia < 20 ms), Serverless VPC Access a Cloud SQL privado, escalado automático a cero y costos previsibles en moneda local. GKE introduce sobrecosto fijo desproporcionado de plano de control. |


## 1.2 Selección y justificación del stack tecnológico

### 1.2.1 Comparación metodológica y marco de desarrollo de software

En cumplimiento del criterio de evaluación de alternativas metodológicas para proyectos de ingeniería de software, se contrastaron formalmente tres marcos de gestión para determinar la estrategia óptima de desarrollo y gobierno de **espaciGo**:

**Tabla 2.** Comparación de metodologías de desarrollo de software para el proyecto.

| Dimensión Metodológica | Marco Cascada (Secuencial) | Marco Ágil Puro (Scrum Genérico) | Marco Híbrido Iterativo-Incremental (Adoptado) |
|---|---|---|---|
| **Gestión de Requerimientos** | Congelamiento rígido en fase inicial; alto costo de cambio. | *Backlog* dinámico priorizado; riesgo de dispersión de alcance. | Requerimientos normativos y de seguridad congelados en línea base; funcionalidades de negocio refinadas en iteraciones cortas. |
| **Gobierno y Control de Riesgos** | Validación tardía en fase final; detección tardía de fallas críticas. | Foco exclusivo en velocidad de entrega; descuido de controles regulatorios. | Hitos de revisión técnica formal (*gates*) por dominio arquitectónico antes de promover cambios a la rama principal. |
| **Adaptación Normativa (Ley 21.719)** | Inflexible ante ajustes regulatorios o circulares interpretativas. | Proclive a parches ad-hoc sin modelado formal de auditoría. | Modelado formal previo de privacidad por diseño complementado con pruebas automatizadas continuas en cada sprint. |
| **Dictamen de Selección** | Descartado: Incompatible con la incertidumbre comercial del marketplace. | Descartado: Insuficiente para auditoría legal, contratos y custodia financiera. | **Seleccionado:** Equilibra agilidad de entrega con estricta gobernanza técnica, transaccional y jurídica. |

Bajo este marco híbrido, el desarrollo se estructuró en iteraciones incrementales organizadas en seis hitos de entrega verificada: (1) Base Arquitectónica y Persistencia, (2) Identidad y Gobernanza, (3) Catálogo Geoespacial y Medios, (4) Motor de Reservas y Exclusión GiST, (5) Contratos Digitales y Operación, y (6) Administración Global GADM.

### 1.2.2 Backend Core: Go 1.27 y Arquitectura Hexagonal
El núcleo transaccional se implementa en **Go 1.27.1** utilizando exclusivamente la librería estándar `net/http` para enrutamiento HTTP estricto. La persistencia relacional se gestiona mediante `github.com/jackc/pgx/v5` (v5.11.0) con pool de conexiones transaccionales seguras y `cloud.google.com/go/cloudsqlconn` (v1.25.2) para el túnel seguro hacia Cloud SQL. La seguridad criptográfica se implementa mediante `golang.org/x/crypto` con hashing `bcrypt` (factor de costo 12) para credenciales y tokens opacos de sesión de 256 bits almacenados en base de datos.

El procesamiento de imágenes hacia formato `image/webp` se realiza con `github.com/deepteams/webp` (v1.2.8) limitando la dimensión máxima a 1600 px, configurado con un factor de calidad balanceado (calidad 80) para optimizar el almacenamiento y transferencia sin pérdida visual perceptible. La generación y foliado de contratos de arriendo en formato PDF se implementa mediante `github.com/pdfcpu/pdfcpu` (v0.16.3), garantizando archivos estructurados deterministas con estampas temporales y hashes inmutables.

### 1.2.3 Frontend Web: Next.js 16, React 19 y Tailwind CSS 4
La interfaz de usuario se construye con **Next.js 16.4.3** y **React 19.3.0** sobre TypeScript 5 en modo estricto. El framework implementa el patrón BFF (*Backend for Frontend*): las peticiones públicas de catálogo se renderizan en servidor (SSR) para máxima velocidad e indexación en motores de búsqueda, mientras que las operaciones autenticadas se enrutan mediante Server Components hacia el backend Go a través de la red interna, ocultando tokens de infraestructura y manejando cookies `HttpOnly` seguras.

El diseño visual responsivo se basa en **Tailwind CSS 4.3.3** complementado con primitivas accesibles de `@base-ui/react` (v1.9.0) y `radix-ui` (v1.4.2). El consumo de la API se encuentra tipado de extremo a extremo mediante `openapi-fetch` (v0.17.0) generado directamente desde la especificación `openapi.yaml` por `openapi-typescript` (v7.13.0). Las pruebas automatizadas de interfaz y accesibilidad se ejecutan con `@playwright/test` (v1.64.1) y `@axe-core/playwright` (v4.14.0) bajo el estándar WCAG 2.1 nivel AA.

*(Nota de trazabilidad técnica)*: En la fase inicial del proyecto se evaluó y prototipó una versión exploratoria basada en Angular con Signals (documentada en el histórico ADR-004), determinándose finalmente migrar y consolidar la arquitectura de producción en Next.js 16 y React 19 por su superior capacidad de renderizado en servidor (SSR) para el catálogo inmobiliario y su integración nativa con el empaquetado de contenedores standalone (formalizado en el ADR-007 del Anexo A).

### 1.2.4 Persistencia: PostgreSQL 18 con PostGIS y GiST
El motor relacional es **PostgreSQL 18**, enriquecido con la extensión geoespacial **PostGIS 3.6** y la extensión **btree_gist**. Esta configuración permite indexar coordenadas geodésicas (`geography(Point, 4326)`) para búsquedas espaciales y de proximidad en metros mediante `ST_DWithin` y definir restricciones físicas de exclusión temporal en la tabla `public.ocupacion`:
```sql
ALTER TABLE public.ocupacion
    ADD CONSTRAINT ocupacion_no_solapa_excl
    EXCLUDE USING gist (espacio_id WITH =, intervalo WITH &&) WHERE (activo);
```
Esta regla garantiza a nivel de motor de almacenamiento que resulte matemáticamente imposible confirmar dos reservas simultáneas para el mismo espacio en una franja horaria coincidente.


## 1.3 Factibilidad técnica y condiciones del entorno

### 1.3.1 Condiciones del entorno de desarrollo de ingeniería
Para asegurar la reproducibilidad estricta de compilaciones y pruebas locales de forma independiente de servicios de nube, el entorno de ingeniería se encuentra estandarizado en las siguientes estaciones de trabajo locales:
- **Hardware de Desarrollo:** Estaciones x86_64 con procesadores de 8 núcleos / 16 hilos (frecuencia base 3,6 GHz), 32 GB memoria RAM DDR4/DDR5 y unidades de estado sólido NVMe PCIe 4.0.
- **Sistema Operativo y Virtualización:** Linux (Debian 12 / Ubuntu 24.04 LTS kernel 6.x), Docker Engine 27.x y Docker Compose v2.
- **Herramientas de Construcción:** Compilador Go 1.24/1.27, Node.js 22 LTS, utilitarios de PostgreSQL 18 (`psql`, `pg_dump`), Make y utilitarios de verificación estática de código.
- **Topología Local Contenerizada:** Aislamiento de red mediante puente Docker (`espacigo-net`), ejecutando contenedores locales para frontend (`espacigo-frontend`), backend (`espacigo-backend`) y base de datos relacional (`espacigo-db` con imagen `postgis/postgis:18-3.6-alpine`).

### 1.3.2 Factibilidad técnica de la arquitectura
La viabilidad técnica de la solución se sustenta en tres pilares de compatibilidad:
1. **Compatibilidad de Plataformas OCI:** Todos los componentes se empaquetan en imágenes de contenedor estándar OCI bajo Linux Alpine y Distroless, permitiendo su ejecución indistinta en el entorno local contenerizado y en la nube (Google Cloud Run).
2. **Contratos Formales OpenAPI 3.1:** La comunicación entre frontend y backend se rige estrictamente por esquemas OpenAPI versionados, asegurando sincronización de tipos y serialización JSON sin discrepancias de modelo.
3. **Aislamiento de Red y Privacidad:** La base de datos reside en una subred privada de Google Cloud SQL sin IP pública, accesible únicamente mediante Serverless VPC Access desde los contenedores de aplicación.

*(Declaración explícita de alcance y adaptadores)*: Para efectos de la presente entrega académica y las suites de verificación local, las integraciones con servicios externos (pasarela de pagos Mercado Pago Split/Escrow, OCR biométrico de identidad KYC y firma electrónica avanzada) se implementan y validan mediante **Adaptadores de Integración controlados (Mocks de alta fidelidad)** que emulan fielmente los contratos HTTP y códigos de estado de producción. La custodia efectiva de fondos financieros y la validez legal de firma ante ministros de fe constituyen capacidades operacionales sujetas a contratos comerciales y homologación bancaria para el despliegue productivo final.


## 1.4 Factibilidad económica y presupuesto de operación

El análisis financiero del proyecto delimita con estricto rigor el presupuesto operativo mensual requerido para sostener la plataforma en su **Escenario de Referencia: Fase Piloto Inicial** desplegado en Google Cloud Platform en la región de Santiago (`southamerica-west1`). Se distingue con claridad el costo mensual de infraestructura cloud de los costos de desarrollo y comisiones transaccionales.

### 1.4.1 Presupuesto mensual de infraestructura cloud (Piloto Santiago)
El dimensionamiento contempla una carga proyectada de hasta 10.000 usuarios mensuales activos y 1.500 reservas en el piloto:

| Componente Cloud GCP | Especificación Técnica de Capacidad | Estimación USD/mes | Estimación CLP/mes |
|---|---|:---:|:---:|
| **Google Cloud Run (Frontend BFF)** | Contenedor Next.js 16 (1 vCPU, 1 GB RAM, escalado 0 a 5 instancias con auto-reposo) | $14,00 | $13.580 |
| **Google Cloud Run (Backend Core)** | Contenedor Go 1.27 (1 vCPU, 512 MB RAM, escalado 0 a 10 instancias con auto-reposo) | $14,00 | $13.580 |
| **Cloud SQL for PostgreSQL 18** | Instancia administrada `db-custom-2-7680` (2 vCPU, 7.5 GB RAM, SSD 20 GB con auto-aumento y backups diarios retenidos 7 días) | $135,00 | $130.950 |
| **Google Cloud Storage (GCS)** | Buckets regionales en Santiago (almacenamiento WebP, PDF de contratos y evidencias) | $8,50 | $8.245 |
| **Networking & Egress** | Direct VPC Egress hacia Cloud SQL y transferencia saliente CDN perimetral | $9,50 | $9.215 |
| **Seguridad Perimetral (Cloud Armor + DNS)** | Reglas WAF básicas OWASP y gestión de zona DNS gestionada | $25,00 | $24.250 |
| **Google Secret Manager** | Rotación y custodia de credenciales y claves criptográficas de sesión | $2,00 | $1.940 |
| **Total Mensual Infraestructura Cloud** | **Arquitectura completa en región southamerica-west1 (Santiago)** | **$208,00 USD** | **$201.760 CLP** |

*(Tipo de cambio de referencia: 1 USD = 970 CLP)*.

### 1.4.2 Modelo de comisiones, costos transaccionales y punto de equilibrio
El modelo económico del marketplace separa claramente el costo fijo de infraestructura del margen transaccional:
1. **Comisión del Marketplace espaciGo:** La plataforma aplica una comisión por servicio del **10% sobre el subtotal de cada arriendo formalizado**, descontada automáticamente en la liquidación final al anfitrión.
2. **Tarifa Adquirente de Procesamiento de Pagos:** La comisión del procesador de pagos (Mercado Pago Checkout Pro) en Chile corresponde al **3,19% + IVA (3,80% efectivo)** por transacción aprobada, deducida del flujo de cobro.
3. **Margen Neto Operativo de Plataforma:** Por cada transacción, espaciGo obtiene un margen bruto del **10%** ($10.000 CLP para un arriendo promedio de $100.000 CLP), mientras que el anfitrión recibe el 90% restante sujeto a los costos adquirentes correspondientes.

**Cálculo Explícito del Punto de Equilibrio de Infraestructura:**
- Costo fijo mensual de infraestructura cloud: **$201.760 CLP**.
- Ticket promedio de arriendo mensual estimado (oficinas privadas, bodegas flexibles o módulos profesionales): **$100.000 CLP**.
- Ingreso bruto por comisión unitaria (10%): **$10.000 CLP por arriendo**.
- Volumen mensual de equilibrio: `Punto de Equilibrio = $201.760 CLP / $10.000 CLP = 20,18 arriendos`.

Con un promedio de **21 arriendos mensuales** formalizados a través de la plataforma, el marketplace cubre íntegramente su costo fijo de infraestructura cloud en Santiago. Para tickets de arriendo de mayor escala ($150.000 CLP promedio), el punto de equilibrio se alcanza con tan solo **14 arriendos mensuales**, demostrando una sólida factibilidad económica y bajo riesgo operacional de inicio.
"""

sec01_path.write_text(content.strip() + '\n', encoding='utf-8')
print(f'Actualizado {sec01_path} exitosamente ({len(content)} caracteres).')
