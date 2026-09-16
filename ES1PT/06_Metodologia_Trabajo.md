# VI. Metodología de Trabajo

## 6.1 Metodología de Desarrollo del Proyecto

Dada la naturaleza innovadora y la arquitectura de microservicios propuesta para EspaciGo, se determinó utilizar una **metodología adaptativa (Ágil)** basada en el marco de trabajo **Scrum**, fuertemente apoyada por la cultura **DevOps**. 

Se descartan las metodologías predictivas (como Cascada) debido a su rigidez, ya que la integración de APIs externas (Mercado Pago, FirmaVirtual) exige iteraciones cortas, pruebas tempranas y flexibilidad ante cambios en la documentación técnica de terceros.

**Mecanismos de Desarrollo (Cultura DevOps):**
1. **Entornos Aislados (Docker):** El equipo utilizará Docker para asegurar que los entornos locales de los tres ingenieros sean idénticos ("En mi máquina sí funciona"), erradicando conflictos de versiones.
2. **Control de Versiones (Git Flow):** Todo el código fuente se hospedará en GitHub. Se trabajará en ramas separadas (*Branches*) que convergerán en la rama principal (*Main*) mediante *Pull Requests* revisados por pares.
3. **Integración y Despliegue Continuo (CI/CD):** Mediante GitHub Actions, cada vez que se apruebe código, el sistema compilará la imagen de Docker, ejecutará pruebas automáticas y desplegará la nueva versión directamente en Google Cloud Run sin intervención humana manual.

## 6.2 Duración y Cronograma

El proyecto tiene una duración estimada de **16 semanas (4 meses)**, estructurado en 4 fases de desarrollo (*Sprints* macro de 4 semanas cada uno):

| Fase | Semanas | Actividades Principales | Entregables Esperados |
| :--- | :--- | :--- | :--- |
| **Fase 1** | Semanas 1 a 4 | Levantamiento de requerimientos, diseño relacional (PostgreSQL), configuración de repositorios GitHub y contenedores locales (Docker). Maquetación de UI base (Next.js). | Documento ES1, Modelamiento Entidad-Relación, Maqueta UI. |
| **Fase 2** | Semanas 5 a 8 | Desarrollo de autenticación (JWT), manejo de sesiones, y programación del backend concurrente transaccional en Golang. | Módulo de registro y Login funcional. |
| **Fase 3** | Semanas 9 a 12 | Integración de APIs de terceros (Mercado Pago para retenciones Escrow, FirmaVirtual para contratos). Configuración de logs en BigQuery. | Pasarela operativa y PDFs generándose. |
| **Fase 4** | Semanas 13 a 16 | Despliegue final mediante pipelines CI/CD a Google Cloud Platform. Pruebas de carga, estrés transaccional y revisión legal (Ley 21.719). | Plataforma SaaS 100% online y funcional. Defensa final. |

## 6.3 Equipo de Trabajo (Matriz RACI)

El equipo está conformado por tres estudiantes de Ingeniería en Informática. Para asegurar la rendición de cuentas, se estructuró la siguiente **Matriz RACI** *(Responsible, Accountable, Consulted, Informed)*:

*   **Hernán Espinoza:** Arquitecto Cloud y Backend (Diseño BD y DevOps).
*   **Erick Silva:** Especialista en Lógica Core e Integraciones (Desarrollo en Go y APIs).
*   **Anita Marchant:** Desarrolladora Frontend y UX/UI (Desarrollo en Next.js).

| Actividad / Tarea del Proyecto | Hernán E. | Erick S. | Anita M. |
| :--- | :--- | :--- | :--- |
| Definir Arquitectura Cloud y DevOps | R/A | C | I |
| Diseñar Base de Datos (PostgreSQL) | R/A | C | I |
| Configurar Integración Continua (CI/CD) | R | I | I |
| Programar Backend Concurrente (Golang) | C | R/A | I |
| Integrar Pasarela de Pagos (Mercado Pago) | C | R | I |
| Integrar API Legal (FirmaVirtual) | C | R | I |
| Diseñar Experiencia de Usuario (UI/UX) | I | C | R/A |
| Programar Frontend Server-Side (Next.js) | I | C | R |
| Conectar Frontend con API REST (Axios/Fetch) | C | C | R |
| Documentación e Informe Técnico (ES1) | R | R | R |

*(Leyenda: **R** = Responsable de ejecutar la tarea; **A** = Aprobador/Rinde cuentas finales; **C** = Consultado experto; **I** = Informado del avance).*

## 6.4 Plan de Recursos y Presupuesto

Para garantizar la viabilidad del proyecto como emprendimiento (Startup), se estimó un presupuesto conservador a 4 meses, valorizando el capital humano y la infraestructura Cloud.

### 6.4.1 Recursos Humanos (Horas Hombre)
Asumiendo una dedicación Part-Time (20 horas semanales por integrante) durante 16 semanas:
*   Hernán Espinoza (Arquitecto Cloud): 320 horas a \$15.000/hr = \$4.800.000 CLP.
*   Erick Silva (Desarrollador Backend): 320 horas a \$15.000/hr = \$4.800.000 CLP.
*   Anita Marchant (Desarrolladora Frontend): 320 horas a \$15.000/hr = \$4.800.000 CLP.
*   **Subtotal RRHH (Costo Oportunidad):** \$14.400.000 CLP.

### 6.4.2 Recursos Tecnológicos (Infraestructura y Software)
La arquitectura Serverless en Google Cloud Platform permite iniciar con costos muy bajos (Pay-as-you-go).
*   **Hardware:** 3 Computadores personales (Propiedad de los estudiantes) con Docker Desktop = \$0.
*   **Google Cloud Platform (GCP):** Cloud Run, Cloud SQL y BigQuery = Estimado \$50.000 CLP mensuales x 4 meses = \$200.000 CLP. *(Nota: Inicialmente se absorberá con el crédito gratuito de \$300 USD de Google).*
*   **Dominio Web (.cl):** NIC Chile = \$10.950 CLP anual.
*   **GitHub Team / GitHub Actions:** Nivel gratuito universitario = \$0.
*   **Costos Operativos APIs:** Mercado Pago cobra comisión por transacción (Take Rate absorbido en el flujo), FirmaVirtual cobra un costo variable por firma ANF (traspasado al usuario final). Costo base de integración = \$0.
*   **Subtotal Tecnológico Directo:** \$210.950 CLP.

### 6.4.3 Presupuesto Total del Proyecto
*   **Costo Real de Inversión Inicial (Cash-out):** \$210.950 CLP.
*   **Costo de Valorización Total del Proyecto (Sumando HH):** \$14.610.950 CLP.

**Justificación de Viabilidad:** La alta valoración en Horas Hombre demuestra la densidad técnica del proyecto. Sin embargo, gracias al enfoque *Cloud-Native Serverless* y al uso de software Open Source (Docker, Postgres, Go), el equipo no necesita inversión inicial de capital (*Cash-out*), lo que hace que EspaciGo sea financieramente viable para desarrollarse como Proyecto de Título.
