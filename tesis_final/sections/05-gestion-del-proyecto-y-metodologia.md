# CAPÍTULO V: GESTIÓN DEL PROYECTO, MARCO METODOLÓGICO Y PLANIFICACIÓN

## 5.1. Selección y Justificación Metodológica del Enfoque Híbrido

En el ámbito de la Ingeniería de Software contemporánea, la gestión de proyectos no debe confundirse con el modelo de desarrollo de código. La literatura especializada y los estándares internacionales (Project Management Institute [PMI], 2021) recomiendan desacoplar la **gobernanza directiva del proyecto** del **ciclo de vida constructivo del producto informático**.

### 5.1.1. Gobernanza (PMBOK) y Ciclo de Vida del Software (Iterativo-Incremental)

Para garantizar el cumplimiento de los objetivos académicos e industriales de **espaciGo**, se adopta formalmente un **Enfoque Metodológico Híbrido**:
1. **Marco de Gobernanza y Gestión:** Se fundamenta en las mejores prácticas del estándar **PMBOK** (*Project Management Body of Knowledge*, 7ma Edición). Este marco proporciona la estructura formal para definir y controlar la **Línea Base del Alcance** mediante la **Estructura de Desglose del Trabajo (EDT/WBS)**, la gestión de riesgos sistémicos, la asignación de recursos y el aseguramiento del cronograma.
2. **Modelo de Ciclo de Vida de Construcción:** Se adopta un modelo **Iterativo e Incremental**. La ingeniería de detalle, codificación y pruebas se organizan en ciclos sucesivos e incrementales donde cada fase entrega un incremento funcional, verificable e integrable de la plataforma, mitigando riesgos de arquitectura de forma temprana.

### 5.1.2. Matriz Multicriterio de Decisión Metodológica

Para fundamentar técnicamente la selección del modelo Híbrido frente a paradigmas alternativos (Cascada tradicional y Scrum ágil puro), se formula la siguiente matriz multicriterio ponderada:

**Tabla 3**  
*Matriz Multicriterio Ponderada de Selección Metodológica*

| Criterio de Selección | Ponderación | Cascada Tradicional | Scrum Puro | **Modelo Híbrido (PMBOK + Iterativo)** | Justificación Técnica |
|---|:---:|:---:|:---:|:---:|---|
| **Predictibilidad y Control del Alcance** | 25% | 4 / 5 | 2 / 5 | **5 / 5** | El proyecto cuenta con un alcance contractual cerrado (236 requerimientos funcionales aprobados). Scrum asume alcance volátil y dinámico; PMBOK gobierna el alcance mediante la EDT. |
| **Fijeza de Plazos Académicos Institucionales** | 25% | 3 / 5 | 2 / 5 | **5 / 5** | Las fechas de titulación universitaria son inflexibles. Scrum no ofrece garantías de fecha fija para un alcance cerrado sin recortar funcionalidad. |
| **Mitigación Temprana de Riesgos Técnicos** | 20% | 1 / 5 | 5 / 5 | **4 / 5** | Cascada posterga las pruebas y despliegue al final del ciclo de vida (riesgo inaceptable). El modelo iterativo valida módulos de software en cada incremento. |
| **Control Formal de EDT y Recursos** | 15% | 4 / 5 | 1 / 5 | **5 / 5** | La pauta de titulación y la auditoría docente exigen expresamente una EDT y asignación de esfuerzo por persona, artefactos nativos de PMBOK inexistentes en Scrum. |
| **Trazabilidad de Pruebas y Calidad (QA)** | 15% | 2 / 5 | 4 / 5 | **5 / 5** | Permite vincular cada paquete de trabajo de la EDT con matrices de prueba unitarias, de integración y rendimiento. |
| **Puntaje Ponderado Total** | **100%** | **2.95 / 5.0** | **2.65 / 5.0** | **4.75 / 5.0** | **Selección Ganadora: Modelo Híbrido** |

*Nota.* Elaboración propia en base a directrices del estándar PMI (2021).

### 5.1.3. Modelo de Fases e Incrementos del Ciclo de Vida

El ciclo de desarrollo se estructura en cinco fases continuas gobernadas por compuertas de decisión (*gates*), garantizando la coherencia terminológica exigida por la pauta docente:

**Figura 4**  
*Modelo de Proceso del Ciclo de Vida Híbrido por Fases e Incrementos*

![](assets/figuras/fig04_ciclo_vida_hibrido_fases.png)

*Nota.* Elaboración propia según estándares de gestión PMI (2021).

---

## 5.2. Gestión del Alcance del Proyecto

La gestión del alcance asegura que el proyecto incluya todo el trabajo requerido, y únicamente el trabajo necesario, para culminar con éxito la plataforma **espaciGo**.

### 5.2.1. Criterios de Delimitación y Línea Base del Alcance

La Línea Base del Alcance se integra por tres componentes oficiales:
1. El Enunciado del Alcance del Proyecto (detallado en el Capítulo IV).
2. La **Estructura de Desglose del Trabajo (EDT/WBS)**.
3. El **Diccionario de la EDT**.

### 5.2.2. Estructura de Desglose del Trabajo (EDT / WBS) a 3 Niveles

A continuación se presenta la descomposición jerárquica orientada a entregables de la totalidad del trabajo del proyecto:

```text
1. PROYECTO DE TITULACIÓN "espaciGo"
├── 1.1. Gestión y Gobernanza del Proyecto (PMBOK)
│   ├── 1.1.1. Acta de Constitución y Formalización del Equipo
│   ├── 1.1.2. Plan de Gestión del Alcance y Línea Base (EDT)
│   ├── 1.1.3. Cronograma Maestro y Ruta Crítica (Carta Gantt)
│   ├── 1.1.4. Gestión de Costos, Presupuesto y Adquisiciones Cloud
│   └── 1.1.5. Matriz de Gestión de Riesgos y Control de Cambios
├── 1.2. Diagnóstico, Análisis y Requerimientos
│   ├── 1.2.1. Levantamiento de Procesos Actuales (BPMN As-Is) y Contexto
│   ├── 1.2.2. Especificación Formal de Requerimientos Funcionales (236 RF)
│   ├── 1.2.3. Especificación de Requerimientos No Funcionales (43 RNF / SLAs)
│   ├── 1.2.4. Modelado de Casos de Uso (52 CU) e Historias de Usuario (35 HU)
│   └── 1.2.5. Matriz de Trazabilidad de Requerimientos
├── 1.3. Arquitectura del Sistema y Diseño de Ingeniería
│   ├── 1.3.1. Arquitectura Empresarial (TOGAF 4 Capas: Procesos, Datos, Apps, Infra)
│   ├── 1.3.2. Diseño de Arquitectura de Software (Hexagonal en Go / BFF Next.js)
│   ├── 1.3.3. Modelado de Datos Relacional y Geoespacial (PostgreSQL / PostGIS)
│   ├── 1.3.4. Diseño de Seguridad, Autenticación (JWT/OAuth2) y Ley 21.719
│   └── 1.3.5. Especificación de Contratos de Interfaz (Catálogo OpenAPI / REST)
├── 1.4. Construcción y Desarrollo Incremental
│   ├── 1.4.1. Iteración 1: Núcleo de Autenticación, Usuarios y Control de Acceso (RBAC)
│   ├── 1.4.2. Iteración 2: Catálogo de Inmuebles, Publicación y Búsqueda Geoespacial
│   ├── 1.4.3. Iteración 3: Motor Transaccional de Arriendos y Pagos Escrow
│   ├── 1.4.4. Iteración 4: Módulo de Contratos Digitales y Notificaciones
│   └── 1.4.5. Iteración 5: Panel de Administración, Métricas y Auditoría
├── 1.5. Aseguramiento de Calidad y Pruebas (QA)
│   ├── 1.5.1. Pruebas Unitarias y de Integración (Backend Go y Frontend React)
│   ├── 1.5.2. Pruebas de Carga y Rendimiento (JMeter / K6 con métricas P95)
│   ├── 1.5.3. Pruebas de Resiliencia, Respaldo y Recuperación (Validación RPO/RTO)
│   └── 1.5.4. Auditoría de Ciberseguridad y Escaneo de Vulnerabilidades (OWASP ZAP)
└── 1.6. Puesta en Marcha, Evaluación Económica y Cierre
    ├── 1.6.1. Automatización de Despliegue CI/CD y Topología en GCP
    ├── 1.6.2. Evaluación Financiera (Flujo de Caja, VAN, TIR, Payback)
    ├── 1.6.3. Constitución Societaria (SpA) y Aspectos Legales Tributarios
    └── 1.6.4. Informe Final de Titulación y Defensa de Grado
```

### 5.2.3. Diccionario de la EDT y Entregables Principales

Cada paquete de trabajo de nivel 3 cuenta con una ficha técnica que define su alcance y criterios de aceptación. A modo de síntesis ejecutiva:
*   **Paquete 1.3.3 (Modelado de Datos Geoespacial):** Entrega el esquema DDL de 110 tablas en PostgreSQL con índices GiST para operadores espaciales y rangos `tsrange`. Criterio de aceptación: 100% de consultas espaciales ejecutadas en menos de 50 ms.
*   **Paquete 1.4.3 (Motor Transaccional y Escrow):** Entrega la integración con pasarelas de pago y el circuito de congelamiento y liquidación de garantías. Criterio de aceptación: Cero discrepancias en conciliación de pagos en pruebas automatizadas.
*(Para la totalidad de fichas del Diccionario de la EDT, remitirse al Anexo correspondiente).*

---

## 5.3. Planificación Temporal y Carta Gantt Maestra

> [!TIP]
> 🟢 **[SECCIÓN RESERVADA PARA INTEGRACIÓN — ANITA MARCHANT Y ERICK SILVA]**  
> Anita y Erick agregarán esta parte (planificación detallada con Carta Gantt, ruta crítica CPM, dependencias y duraciones de tareas).

---

## 5.4. Plan de Gestión de Recursos y Equipo de Trabajo

La ejecución del proyecto está a cargo del equipo fundador, conformado por tres ingenieros con roles de responsabilidad complementarios:

### 5.4.1. Roles y Matriz de Asignación de Responsabilidades (RACI)

La asignación de responsabilidades sobre los paquetes principales de la EDT se define bajo la matriz RACI (*Responsible, Accountable, Consulted, Informed*):

**Tabla 4**  
*Matriz de Asignación de Responsabilidades (RACI) del Equipo Fundador*

| Paquete de Trabajo de la EDT | Hernán Espinoza (Líder Arquitectura y Backend) | Anita Marchant (Líder Frontend y Negocio) | Erick Silva (Líder Ciberseguridad y DevOps) |
|---|:---:|:---:|:---:|
| **1.1. Gestión y Gobernanza del Proyecto** | **C** | **A / R** | **C** |
| **1.2. Requerimientos y Modelado BPMN** | **R** | **A / R** | **C** |
| **1.3. Arquitectura TOGAF y Hexagonal** | **A / R** | **C** | **R** |
| **1.4. Construcción Backend (Go / PostGIS)** | **A / R** | **I** | **C** |
| **1.4. Construcción Frontend (Next.js)** | **C** | **A / R** | **I** |
| **1.5. Pruebas de Rendimiento y Seguridad** | **R** | **C** | **A / R** |
| **1.6. Despliegue GCP y Evaluación Financiera** | **C** | **A / R** | **A / R** |

*Convención: **R** = Responsable de ejecutar la tarea; **A** = Aprobador último / Responsable final; **C** = Consultado técnicamente; **I** = Informado.*

*Nota.* Elaboración propia.

### 5.4.2. Estimación de Esfuerzo y Carga Horaria por Integrante

La estimación de esfuerzo combina dos aproximaciones metodológicas:
1. **Estimación Top-Down por Puntos de Casos de Uso (UCP - Karner):** Basada en los 4 actores del sistema y los 52 casos de uso ponderados con los factores técnicos (TCF) y ambientales (ECF), arrojando un esfuerzo industrial teórico de 1.140 horas de desarrollo.
2. **Estimación Bottom-Up por Desglose de Tareas (EDT):** Distribuye un total de 480 horas netas por integrante (1.440 horas de equipo acumuladas a lo largo de 16 semanas académicas), dedicadas a la construcción, depuración, redacción técnica y aseguramiento de calidad del MVP funcional.

---

## 5.5. Plan de Gestión de Riesgos del Proyecto

La gestión de riesgos identifica, evalúa y mitiga tempranamente amenazas técnicas y operacionales:

### 5.5.1. Matriz de Probabilidad e Impacto de Riesgos

**Tabla 5**  
*Matriz de Probabilidad e Impacto de Riesgos del Proyecto*

| ID | Riesgo Identificado | Categoría | Probabilidad | Impacto | Severidad | Estrategia de Mitigación |
|:---:|---|:---:|:---:|:---:|:---:|---|
| **R-01** | Doble reserva concurrente en inmuebles de alta demanda. | Técnico | Media (3) | Crítico (5) | **Alta (15)** | Implementación de índices de exclusión GiST (`tsrange`) a nivel de motor de datos en PostgreSQL 18. |
| **R-02** | Caída o degradación de la pasarela de pagos durante un arriendo. | Externo | Baja (2) | Crítico (5) | **Media (10)** | Manejo de reintentos idempotentes y registro de transacciones con estado *Pending* para conciliación asíncrona. |
| **R-03** | Vulnerabilidad de datos personales sensibles (Ley 21.719). | Ciberseguridad | Baja (2) | Crítico (5) | **Media (10)** | Cifrado AES-256 en reposo, TLS 1.3 en tránsito y protocolo de purga *anti-replay* en backups. |
| **R-04** | Desajuste en el calendario académico y fechas de entrega. | Gestión | Media (3) | Mayor (4) | **Alta (12)** | Control estricto de la EDT y congelamiento de alcance en compuertas de fase (*phase gates*). |
| **R-05** | Rechazo legal de contratos generados dinámicamente. | Legal | Baja (1) | Mayor (4) | **Baja (4)** | Asesoría con abogados especialistas y cumplimiento formal de la Ley N° 21.461. |

*Nota.* Elaboración propia según metodología de gestión de riesgos PMBOK (PMI, 2021).
