# VII. Definición y Justificación de Arquitectura TI (ADR)

## 7.1 Tipo de arquitectura TI y compatibilidad

Con el objetivo de garantizar una alta disponibilidad, seguridad financiera y resiliencia ante picos de tráfico, se define que EspaciGo utilizará una **Arquitectura Cloud-Native orientada a Microservicios basada en Contenedores**. Adicionalmente, el sistema implementa un patrón de bases de datos bimodales, separando la capa transaccional en tiempo real (OLTP) de la capa analítica de auditoría legal (OLAP).

Para visualizar la integración y el flujo de la aplicación con los sistemas externos, se presenta la siguiente Topología de Sistemas:

### Topología del Sistema (Diagrama de Arquitectura)

```mermaid
flowchart TD
    subgraph "Capa de Presentación (Frontend)"
        A[Next.js Container\nSSR, UI/UX]
    end

    subgraph "Capa Lógica y Orquestación (Backend)"
        B[Golang Core Container\nGoroutines, JWT, Reglas de Negocio]
        M_PDF[Microservicio Generador PDF\nContenedor Aislado]
    end

    subgraph "Capa de Persistencia y Auditoría"
        C[(PostgreSQL\nOLTP Transaccional)]
        D[(Cloud Storage\nBuckets Cifrados)]
        E[(BigQuery\nOLAP Auditoría Legal)]
    end

    subgraph "APIs y Sistemas Externos"
        F[Mercado Pago\nEscrow]
        G[FirmaVirtual\nANF Legal]
        H[Registro Civil / SII\nKYC / KYB]
    end

    A -->|Peticiones HTTP/REST| B
    B -->|Transacciones ACID| C
    B -->|Envía HTML| M_PDF
    M_PDF -->|Retorna PDF Inmutable| B
    B -->|Almacena URLs y Documentos| D
    B -.->|Streaming Inserts (Logs)| E
    
    B <-->|Valida y Retiene Fondos| F
    B <-->|Certifica Contratos| G
    B <-->|Valida Usuarios| H
```
*(Nota: Adjuntar imagen de arquitectura generada gráficamente).*

## 7.2 Matrices de Decisión Arquitectónica (ADR) y Descarte Tecnológico

Para justificar las elecciones tecnológicas de manera robusta, se evaluaron al menos 4 alternativas del mercado por cada capa arquitectónica, priorizando las necesidades de un SaaS B2B/B2C escalable.

### 7.2.1 Desarrollo Frontend (Capa de Presentación)

| Criterio Técnico | **Next.js (Elegido)** | React puro SPA (Descartado) | Angular (Descartado) | Vue.js / Nuxt (Descartado) |
| :--- | :--- | :--- | :--- | :--- |
| **SEO y Renderizado** | Excelente (SSR nativo en servidor). | Pobre (Renderiza en el cliente). | Complejo (Requiere SSR Universal). | Bueno, pero menor adopción corporativa en Chile. |
| **Tiempo de Carga** | Muy Rápido (Server Components). | Lento (Carga todo el JS inicial). | Lento (Bundle muy pesado). | Rápido. |
| **Integraciones UI** | Altísima compatibilidad con librerías modernas. | Alta compatibilidad. | Curva de aprendizaje alta. | Ecosistema más fragmentado. |
| **Decisión Final** | **SELECCIONADO** | DESCARTADO | DESCARTADO | DESCARTADO |
* **Justificación:** Un Marketplace necesita aparecer en los primeros resultados de Google. React SPA penaliza severamente el SEO. Next.js soluciona esto pre-renderizando el catálogo en el servidor, superando a Angular en agilidad de desarrollo y a Vue en cuota de mercado.

### 7.2.2 Desarrollo Backend (Capa Lógica y Orquestación)

| Criterio Técnico | **Golang - Go (Elegido)** | Node.js (Descartado) | Python / Django (Descartado) | Java / Spring Boot (Descartado) |
| :--- | :--- | :--- | :--- | :--- |
| **Concurrencia** | Nativa y ligera (*Goroutines*). | *Single-threaded* (Event Loop). | Lento (Bloqueo GIL). | Hilos nativos pesados (Alto consumo RAM). |
| **Rendimiento Cloud**| Binario compilado (Arranca en ms). | Requiere cargar motor V8. | Requiere intérprete Python. | Arranque lento (JVM calienta). |
| **Costo Serverless** | Muy Bajo (consume escasa RAM). | Medio. | Medio - Alto. | Muy Alto. |
| **Decisión Final** | **SELECCIONADO** | DESCARTADO | DESCARTADO | DESCARTADO |
* **Justificación:** El backend debe procesar peticiones de pagos, generar PDFs y enviar logs asíncronos a BigQuery simultáneamente. Golang maneja alta concurrencia consumiendo mínimos recursos frente a Java o Node.js, abaratando drásticamente los costos operativos en Cloud Run.

### 7.2.3 Base de Datos Operativa (Capa de Persistencia Financiera)

| Criterio Técnico | **PostgreSQL (Elegido)** | MongoDB (Descartado) | MySQL (Descartado) | Firebase RTDB (Descartado) |
| :--- | :--- | :--- | :--- | :--- |
| **Integridad y ACID** | 100% (Bloqueos y *Rollbacks* atómicos). | Consistencia eventual (Riesgoso). | Alta, pero bloqueos menos óptimos. | Baja para reglas financieras estrictas. |
| **Búsqueda / Filtros** | Flexible (Múltiples JOINS y Geoespacial). | Rígida (Requiere modelado previo). | Buena. | Muy rígida (Sin JOINS nativos). |
| **Decisión Final** | **SELECCIONADO** | DESCARTADO | DESCARTADO | DESCARTADO |
* **Justificación:** Al retener dinero (Escrow), es inaceptable una falla de integridad (ej. que se cobre pero no se registre la reserva). PostgreSQL garantiza transacciones ACID perfectas y ofrece extensiones geolocalizadas (PostGIS) ideales para el mapa de inmuebles.

### 7.2.4 Infraestructura Cloud y Despliegue

| Criterio Técnico | **GCP - Cloud Run (Elegido)** | VPS Tradicional (Descartado) | Servidor On-Premise (Descartado) | AWS EC2 (Descartado) |
| :--- | :--- | :--- | :--- | :--- |
| **Gestión** | Administrado (*Serverless*). | Manual (*SysAdmin*, Linux, SSL). | Mantenimiento físico local. | Requiere configuración de Auto-Scaling. |
| **Escalabilidad** | Automática (De 0 a miles de instancias). | Manual (Upgrades rígidos). | Nula resiliencia a picos de tráfico. | Automática, pero compleja. |
| **Costos Iniciales** | \$0 (Paga por milisegundos de uso). | Costo fijo mensual. | Altísimo costo de hardware. | Pago por hora encendida. |
| **Decisión Final** | **SELECCIONADO** | DESCARTADO | DESCARTADO | DESCARTADO |
* **Justificación:** Un VPS o servidor físico obligaría al equipo a gastar semanas en tareas operativas (firewalls, caídas de red). Cloud Run permite desplegar contenedores con auto-escalado inmediato, cobrando solo cuando hay tráfico.

### 7.2.5 Empaquetado y Entorno de Desarrollo (DevOps)

| Criterio Técnico | **Docker / Contenedores (Elegido)** | Instalación Nativa (Descartado) | Máquinas Virtuales (Descartado) | FTP / Hosting Compartido (Descartado) |
| :--- | :--- | :--- | :--- | :--- |
| **Consistencia** | Garantizada ("Funciona en todas partes"). | Fricción ("En mi máquina sí funciona"). | Alta, pero consume demasiada RAM local. | Nulo control de versiones. |
| **Agilidad** | Excelente (*docker-compose up*). | Conflictos de versiones (Go, Node). | Lento de encender. | Riesgo de sobreescribir código en PRD. |
| **Decisión Final** | **SELECCIONADO** | DESCARTADO | DESCARTADO | DESCARTADO |
* **Justificación:** Docker aísla todo el ecosistema (BD, Frontend, Backend). Esto garantiza que el entorno local de todos los integrantes del equipo sea idéntico al que se ejecutará en los servidores de Google, eliminando errores de dependencias.

### 7.2.6 Almacenamiento de Logs y Auditoría Legal (Ley 21.719)

| Criterio Técnico | **Google BigQuery (Elegido)** | Tabla Logs en PostgreSQL (Descartado) | Archivos Planos S3/GCS (Descartado) | ElasticSearch / ELK (Descartado) |
| :--- | :--- | :--- | :--- | :--- |
| **Naturaleza** | Data Warehouse (OLAP), escalable a PB. | Base Transaccional (OLTP). | Almacenamiento de Objetos. | Motor de Búsqueda NoSQL. |
| **Impacto Web** | Nulo (Se procesa en clústeres separados). | Alto (Saturaría RAM de base operativa). | Nulo. | Requiere servidor 24/7 de alto costo. |
| **Capacidad Query** | Excelente (SQL nativo súper rápido). | Limitada si la tabla crece masivamente. | Nula (Imposible hacer queries rápidos). | Excelente, pero de mantenimiento caro. |
| **Decisión Final** | **SELECCIONADO** | DESCARTADO | DESCARTADO | DESCARTADO |
* **Justificación:** Almacenar el historial de auditoría en la misma BD de reservas ralentizaría el sistema. Archivos planos no permiten auditorías rápidas. BigQuery ofrece retención inmutable y consultas SQL sobre petabytes a un costo ínfimo.

### 7.2.7 Integraciones Clave: Pasarela de Pagos (Escrow)

| Criterio Técnico | **Mercado Pago API (Elegido)** | Transferencia Manual (Descartado) | Transbank Webpay Plus (Descartado) | PayPal (Descartado) |
| :--- | :--- | :--- | :--- | :--- |
| **Retención / Escrow** | Nativa (Permite autorizar y capturar después).| Imposible de automatizar. | Alta burocracia para retenciones largas. | Altas comisiones de retiro internacional. |
| **Split de Pagos** | Sí (Separa la comisión de EspaciGo del total).| Requiere conciliación manual. | Complejo de implementar en Marketplace. | Difícil tributariamente en Chile. |
| **Decisión Final** | **SELECCIONADO** | DESCARTADO | DESCARTADO | DESCARTADO |
* **Justificación:** Se descartan transferencias manuales por riesgo de estafa. Transbank es poco amigable para flujos de retención prolongados. Mercado Pago ofrece *Split Payments* y congelamiento de fondos (Garantías) vía API de forma nativa.

### 7.2.8 Integraciones Clave: Motor de Legalización (Ley 21.461)

| Criterio Técnico | **FirmaVirtual API (Elegido)** | Firma Simple (FES / Checkbox) (Descartado) | Notaría Física Presencial (Descartado) | DocuSign (Descartado) |
| :--- | :--- | :--- | :--- | :--- |
| **Validez Ley 21.461** | Sí (Autorización Notarial y FEA). | Inválido (Nulo para desalojo express). | Sí, pero rompe modelo digital. | Carece de integración notarial chilena. |
| **Decisión Final** | **SELECCIONADO** | DESCARTADO | DESCARTADO | DESCARTADO |
* **Justificación:** Un "Checkbox" de términos y condiciones (Firma Simple) no tiene peso en tribunales bajo la Ley "Devuélveme mi casa". FirmaVirtual permite enrutar PDFs a notarios chilenos vía API, manteniendo el SaaS 100% online y jurídicamente blindado.
