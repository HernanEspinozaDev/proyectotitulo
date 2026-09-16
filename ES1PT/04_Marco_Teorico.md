# IV. Marco Teórico

El presente capítulo desarrolla el marco teórico que fundamenta la solución tecnológica **EspaciGo**. La investigación bibliográfica se divide en dos grandes ejes: el marco normativo chileno que justifica las reglas de negocio (Prop-Tech y Legal-Tech), y el marco tecnológico que sustenta las decisiones arquitectónicas de la plataforma bajo estándares internacionales de Ingeniería de Software.

## 4.1 Investigación Bibliográfica

### 4.1.1 Marco Legal y Normativo

Para operar como un intermediario en el mercado inmobiliario chileno y mitigar el riesgo de los propietarios, la plataforma debe cumplir con las siguientes normativas:

* **Ley 21.461 (Ley "Devuélveme mi casa"):** Promulgada para agilizar la restitución de propiedades arrendadas. Esta ley exige que, para acceder a un juicio monitorio rápido por morosidad, los contratos deben estar firmados ante notario. En un entorno digital, esto requiere la integración con APIs de Firma Electrónica Avanzada (FEA) o Autorización Notarial de Firma (ANF). La plataforma EspaciGo automatiza este flujo legal (Biblioteca del Congreso Nacional de Chile, 2022).
* **Ley 21.719 (Sobre Protección de la Vida Privada y Datos Personales):** Basada en el Reglamento General de Protección de Datos (GDPR) europeo, esta ley consagra el principio de "Privacidad desde el Diseño" (*Privacy by Design*). Impone el resguardo cifrado de datos sensibles (PII) y el derecho al olvido. Esto justifica arquitectónicamente que las carpetas tributarias, cédulas y contratos se aíslen en *Buckets* seguros (Cloud Storage) y no en bases de datos relacionales públicas (Biblioteca del Congreso Nacional de Chile, 2024).

### 4.1.2 Patrones Arquitectónicos y de Diseño

La envergadura transaccional de EspaciGo requiere patrones de diseño escalables:

* **Arquitectura Orientada a Microservicios (Cloud-Native):** A diferencia de arquitecturas monolíticas, este enfoque desacopla los módulos del sistema (ej. Pasarela de Pagos, Generación de Contratos PDF, Autenticación) en contenedores independientes. Según Bass, Clements y Kazman (2021), esto reduce el impacto de fallos sistémicos y permite escalar solo los módulos bajo estrés.
* **Modelo Bimodal de Datos (OLTP y OLAP):** Para evitar que las consultas históricas ralenticen la operativa transaccional de reservas, el diseño adopta un enfoque bimodal. Las transacciones financieras en vivo utilizan bases de datos OLTP (Procesamiento de Transacciones en Línea), mientras que los registros inmutables de auditoría (logs) se derivan a un almacén OLAP (Procesamiento Analítico en Línea) para análisis legal y de negocio (Google Cloud, 2024).
* **Flujo Escrow (Split Payments):** Consiste en un modelo de fideicomiso digital donde un tercero imparcial (la plataforma) retiene el dinero del arrendatario hasta que se cumplan las condiciones del servicio, dispersando luego los fondos (Mercado Pago Developers, 2024).

### 4.1.3 Tecnologías de Desarrollo, Despliegue y Persistencia

Para materializar la arquitectura descrita, se seleccionó un *stack* tecnológico que garantiza concurrencia, rendimiento SEO y escalabilidad:

* **Frontend SSR con Next.js:** React puro (Single Page Applications) penaliza la indexación en motores de búsqueda (SEO). Next.js resuelve este problema mediante Renderizado del Lado del Servidor (SSR), entregando HTML pre-renderizado al cliente, lo cual es crítico para que los espacios publicados en el *Marketplace* se posicionen orgánicamente en Google (Vercel, 2024).
* **Backend Concurrente en Golang (Go):** Lenguaje tipado y compilado creado por Google. Go utiliza hilos ligeros (*Goroutines*) gestionados por su propio entorno de ejecución en lugar del sistema operativo. Esto permite que el servidor procese miles de transacciones de pago, generación de PDFs y envío de correos de forma concurrente, consumiendo una fracción mínima de RAM frente a alternativas como Node.js o Python (Donovan & Kernighan, 2015).
* **Persistencia ACID con PostgreSQL:** Base de datos relacional de código abierto que garantiza las propiedades ACID (Atomicidad, Consistencia, Aislamiento, Durabilidad). Dado que la plataforma gestiona retenciones monetarias (Escrow), el bloqueo transaccional atómico de PostgreSQL asegura que nunca se ejecute una reserva si la retención de garantía falla (PostgreSQL Global Development Group, 2024).
* **Auditoría con Google BigQuery:** Plataforma de Data Warehouse de nivel empresarial, completamente administrada (*Serverless*). Se utiliza como repositorio inmutable para cumplir con la Ley 21.719, recibiendo logs en tiempo real (*Streaming Inserts*) sobre cada acción crítica del sistema (Google Cloud, 2024).
* **Contenedores Docker y Google Cloud Run:** Docker aísla el software de su entorno, erradicando el problema de "en mi máquina funciona" durante el desarrollo en equipo. En producción, estos contenedores se despliegan en Google Cloud Run, una plataforma Serverless que autoescala desde cero instancias hasta miles según la demanda del tráfico, cobrando solo por el tiempo exacto de cómputo (Docker Inc., 2024).


