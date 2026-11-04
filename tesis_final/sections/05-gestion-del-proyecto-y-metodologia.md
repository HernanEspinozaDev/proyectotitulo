# CAPÍTULO V: GESTIÓN DEL PROYECTO, MARCO METODOLÓGICO Y PLANIFICACIÓN

## 5.1. Selección y Justificación Metodológica del Enfoque Híbrido

En el ámbito de la Ingeniería de Software contemporánea, la gestión de proyectos no debe confundirse con el modelo de desarrollo de código. La literatura especializada y los estándares internacionales [@pmbok7] recomiendan desacoplar la **gobernanza directiva del proyecto** del **ciclo de vida constructivo del producto informático**.

### 5.1.1. Gobernanza (PMBOK) y Ciclo de Vida del Software (Iterativo-Incremental)

Para garantizar el cumplimiento de los objetivos académicos e industriales de **espaciGo**, se adopta formalmente un **Enfoque Metodológico Híbrido**:
1. **Marco de Gobernanza y Gestión:** Se fundamenta en las mejores prácticas del estándar **PMBOK** (*Project Management Body of Knowledge*, 7ma Edición). Este marco proporciona la estructura formal para definir y controlar la **Línea Base del Alcance** mediante la **Estructura de Desglose del Trabajo (EDT/WBS)**, la gestión de riesgos sistémicos, la asignación de recursos y el aseguramiento del cronograma.
2. **Modelo de Ciclo de Vida de Construcción:** Se adopta un modelo **Iterativo e Incremental**. La ingeniería de detalle, codificación y pruebas se organizan en ciclos sucesivos e incrementales donde cada fase entrega un incremento funcional, verificable e integrable de la plataforma, mitigando riesgos de arquitectura de forma temprana.

### 5.1.2. Matriz Multicriterio de Decisión Metodológica

Para fundamentar la selección del enfoque híbrido frente a alternativas (Cascada tradicional y Scrum ágil puro), se formula la siguiente matriz multicriterio ponderada:

**Tabla 3**  
*Matriz Multicriterio Ponderada de Selección Metodológica*

| Criterio de Selección | Ponderación | Cascada Tradicional | Scrum Puro | **Modelo Híbrido (PMBOK + Iterativo)** | Justificación Técnica |
|---|:---:|:---:|:---:|:---:|---|
| **Predictibilidad y Control del Alcance** | 25% | 4 / 5 | 2 / 5 | **5 / 5** | El Anexo A fija una línea base de 236 requisitos funcionales. La EDT registra cambios de alcance por incremento. |
| **Fijeza de Plazos Académicos Institucionales** | 25% | 3 / 5 | 2 / 5 | **5 / 5** | Las fechas de titulación universitaria son inflexibles. La evaluación pondera la capacidad de organizar entregas parciales dentro del calendario académico. |
| **Mitigación Temprana de Riesgos Técnicos** | 20% | 1 / 5 | 5 / 5 | **4 / 5** | La evaluación compara la frecuencia con que cada propuesta del proyecto incorpora pruebas y revisión de riesgos. |
| **Control Formal de EDT y Recursos** | 15% | 4 / 5 | 1 / 5 | **5 / 5** | La evaluación considera el grado de integración de la EDT y la asignación de responsabilidades con los controles del proyecto. |
| **Trazabilidad de Pruebas y Calidad (QA)** | 15% | 2 / 5 | 4 / 5 | **5 / 5** | Permite vincular cada paquete de trabajo de la EDT con matrices de prueba unitarias, de integración y rendimiento. |
| **Puntaje Ponderado Total** | **100%** | **2,85 / 5,00** | **2,75 / 5,00** | **4,80 / 5,00** | **Selección Ganadora: Modelo Híbrido** |

*Nota.* Elaboración propia. Cada criterio se valora de 1 a 5 para este proyecto, donde 1 indica ajuste bajo y 5 ajuste alto. El total suma cada valoración multiplicada por su ponderación [@pmbok7].

### 5.1.3. Modelo de Fases e Incrementos del Ciclo de Vida

El ciclo de desarrollo se estructura en las etapas de planificación, análisis, diseño, construcción, pruebas e implementación, garantizando la coherencia terminológica exigida por la pauta docente:

**Figura 3**\
*Modelo de Proceso del Ciclo de Vida Híbrido por Fases e Incrementos*

![](assets/figuras/fig04_ciclo_vida_objetivo.png){height=11cm}

*Nota.* Elaboración propia según el marco de gestión del proyecto [@pmbok7].

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
│   ├── 1.4.3. Iteración 3: Contratación y Cobros Diferenciados
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
*   **Paquete 1.3.3 (Modelado de Datos Geoespacial):** Entrega el esquema DDL de 110 tablas en PostgreSQL con índices GiST para operadores espaciales y rangos `tstzrange`. Criterio de aceptación: consultas y restricciones verificadas contra los criterios del Capítulo VII.
*   **Paquete 1.4.3 (Contratación y Cobros Diferenciados):** Entrega un recorrido sintético de reserva y conciliación y define los criterios de habilitación externa. Criterio de aceptación: La aceptación requiere comprobar la conciliación según el alcance del ensayo y los criterios del Anexo F.
El Capítulo XIII registra el avance y la evidencia de cada incremento.

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
| **1.6.1. Automatización de despliegue y topología** | **C** | **C** | **A / R** |

*Convención: **R** = Responsable de ejecutar la tarea; **A** = Aprobador último / Responsable final; **C** = Consultado técnicamente; **I** = Informado.*

*Nota.* Elaboración propia. La fila 1.6.1 identifica el responsable operativo de despliegue. La planificación y evaluación económica detalladas se conservan en la sección 5.3, el Capítulo XII y los anexos G y H.

### 5.4.2. Registro de esfuerzo

La EDT identifica los paquetes que requieren estimación. La comparación entre esfuerzo previsto y observado requiere un registro por paquete, responsable y período. La sección 5.3 conserva el espacio de integración de la planificación detallada.

## 5.5. Plan de Gestión de Riesgos del Proyecto

La gestión de riesgos identifica, evalúa y mitiga tempranamente amenazas técnicas y operacionales:

### 5.5.1. Matriz de Probabilidad e Impacto de Riesgos

**Tabla 5**  
*Matriz de Probabilidad e Impacto de Riesgos del Proyecto*

| ID | Riesgo Identificado | Categoría | Probabilidad | Impacto | Severidad | Estrategia de Mitigación |
|:---:|---|:---:|:---:|:---:|:---:|---|
| **R-01** | Doble reserva concurrente en espacios de alta demanda. | Técnico | Media (3) | Crítico (5) | **Alta (15)** | Implementación de índices de exclusión GiST (`tsrange`) a nivel de motor de datos en PostgreSQL 18. |
| **R-02** | Caída o degradación de la pasarela de pagos durante un arriendo. | Externo | Baja (2) | Crítico (5) | **Media (10)** | Manejo de reintentos idempotentes y registro de transacciones con estado *Pending* para conciliación asíncrona. |
| **R-03** | Vulnerabilidad de datos personales sensibles (Ley 21.719). | Ciberseguridad | Baja (2) | Crítico (5) | **Media (10)** | Control de acceso por finalidad, protección de archivos y comprobación de permisos tras restaurar. |
| **R-04** | Desajuste en el calendario académico y fechas de entrega. | Gestión | Media (3) | Mayor (4) | **Alta (12)** | Control estricto de la EDT y congelamiento de alcance en compuertas de fase (*phase gates*). |
| **R-05** | Rechazo legal de contratos generados dinámicamente. | Legal | Baja (1) | Mayor (4) | **Baja (4)** | Revisar las modalidades, sus condiciones y la evidencia requerida antes de habilitar integraciones. |

*Nota.* Elaboración propia según metodología de gestión de riesgos PMBOK [@pmbok7].
