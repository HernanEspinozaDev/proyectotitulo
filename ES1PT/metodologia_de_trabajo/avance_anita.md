## 1. 📐 Metodología del Proyecto

### 1.1. Elección de la Metodología
Para el desarrollo de la plataforma **EspaciGo**, se ha optado por implementar una **Metodología Híbrida**. Esta metodología combina un modelo de ciclo de vida de desarrollo de software **Iterativo e Incremental**, junto con las mejores prácticas de gestión de proyectos establecidas por el **PMBOK** (Project Management Body of Knowledge).

### 1.2. Justificación de la Metodología (Cuadro Comparativo)
La elección de una metodología híbrida no es fortuita, sino que responde directamente a la naturaleza, contexto y restricciones del proyecto EspaciGo. 

A diferencia de los proyectos ágiles puros (como Scrum), en este proyecto **los requerimientos son predecibles y estables**. EspaciGo no cuenta con un "cliente real" o un *Product Owner* externo que esté cambiando constantemente los requerimientos al final de cada iteración. No existe un clima de alta incertidumbre o volatilidad en el alcance que justifique un enfoque 100% ágil. Por el contrario, el alcance (creación de un Marketplace SaaS B2B2C con validación de identidad KYC/KYB, firma de contratos dinámicos y pasarela de pago en formato *Escrow*) ya está definido desde su concepción.

Sin embargo, adoptar un enfoque 100% tradicional o en cascada (Waterfall) limitaría la capacidad de entregar valor funcional por partes. Por ello, el modelo **Iterativo-Incremental** permite desarrollar el sistema por módulos (ej. Gestión de Usuarios, Gestión de Publicaciones, Proceso de Arriendo, Pasarela de Pagos), garantizando entregables tangibles en el tiempo. Al mismo tiempo, la incorporación de las prácticas del **PMBOK** asegura una planificación estructurada, gestión de riesgos, control de calidad y un cronograma (Carta Gantt) riguroso, aspectos indispensables para una correcta administración profesional del proyecto.

**Cuadro Comparativo de Metodologías:**

| Característica / Enfoque | Metodología Ágil (ej. Scrum) | Metodología Tradicional (Cascada / PMBOK Puro) | Metodología Híbrida (Seleccionada para EspaciGo) |
| :--- | :--- | :--- | :--- |
| **Estabilidad de Requerimientos** | Muy volátiles y cambiantes durante el ciclo de vida. | Estables, definidos y cerrados completamente al inicio. | **Predecibles y estables**, pero construidos y entregados por partes. |
| **Interacción con el Cliente** | Constante; el cliente aprueba cambios iteración a iteración. | Baja; el cliente aprueba al principio y al final del proyecto. | **Nula/Baja (Proyecto de emprendimiento/SaaS)**, no hay cliente externo que altere el alcance. |
| **Entrega de Valor** | Entregas continuas y rápidas (Sprints cortos). | Entrega única del producto al final del ciclo. | **Entregas iterativas e incrementales** (agrupadas por módulos de funcionalidad). |
| **Gestión y Control** | Flexible, basada en la auto-organización del equipo. | Altamente estructurada (cronogramas estrictos, hitos formales). | **Gestión estructurada (prácticas PMBOK)** aplicada a un flujo de desarrollo iterativo. |

### 1.3. Fases y Etapas del Proyecto
Para asegurar el correcto desarrollo de EspaciGo, el cronograma y la Carta Gantt reflejarán las iteraciones del desarrollo. Cada iteración estructurará su trabajo bajo las siguientes etapas secuenciales y claramente definidas:

1. **Planificación:** Definición del alcance de la iteración, estimación de tiempos y recursos, y asignación de tareas según los estándares de gestión de proyectos.
2. **Análisis:** Levantamiento y documentación detallada de los requerimientos (funcionales y no funcionales), reglas de negocio y flujos de usuario (ej. validaciones de identidad en el Registro Civil o SII).
3. **Diseño:** Creación de diagramas de arquitectura, modelos de base de datos, diseño de interfaces de usuario (mockups) y diagramas de casos de uso organizados por módulo.
4. **Construcción:** Codificación del backend y frontend, integración de servicios de terceros (Mercado Pago, FirmaVirtual) y desarrollo de la lógica de negocio y automatizaciones.
5. **Prueba:** Ejecución de pruebas unitarias, de integración y validación de seguridad (ej. control de concurrencia de reservas y flujos de pagos retenidos).
6. **Implementación:** Despliegue de los módulos terminados, puesta en marcha y aseguramiento de la trazabilidad de logs (Data Warehouse en BigQuery).

*(Nota: Esta secuencia se repetirá iterativamente, y dichas iteraciones deben quedar plasmadas explícitamente en el cronograma del proyecto).*

### 1.4. Duración y Cronograma (Paso 6.2)
El proyecto EspaciGo contempla un tiempo estimado de desarrollo y despliegue de **[Insertar cantidad de Semanas o Meses]** (plazo que será detallado en la Carta Gantt del proyecto). Las fases concretas del desarrollo siguen la estructura del ciclo de vida iterativo-incremental previamente mencionado.

Para asegurar un desarrollo secuencial y estructurado, el calendario prioriza las actividades por módulos funcionales. Dentro de cada iteración y etapa, se establecen plazos fijos para tareas clave, tales como:
- **Recolección y preparación:** Definición de la arquitectura técnica, configuración de repositorios y entornos de desarrollo, investigación de APIs de terceros (Mercado Pago, FirmaVirtual) y revisión de normativas vigentes (ej. Ley 21.719, validaciones KYC/KYB).
- **Ejecución y Seguimiento:** Programación estructurada del backend y frontend, reuniones de control de avance adaptadas al modelo híbrido y configuración de infraestructura.
- **Validación:** Pruebas de calidad y auditoría de los flujos críticos del negocio (Escrow, generación de contratos dinámicos, retención de fondos).

### 1.5. Equipo de Trabajo y Matriz RACI (Paso 6.3)
El equipo de desarrollo está compuesto por 3 analistas programadores que, para efectos de la estructura empresarial y la correcta gestión del proyecto, asumen roles diferenciados que cubren las áreas estratégicas de la organización:
- **Gerencia / Gestión General:** Toma de decisiones estratégicas, control presupuestario y gestión de riesgos.
- **Gestión de Personas / Análisis:** Levantamiento de requerimientos, diseño funcional de los casos de uso, control de calidad (QA) y diseño de la experiencia de usuario.
- **Desarrollo / Arquitectura:** Configuración de la infraestructura tecnológica, codificación, integración de APIs, despliegue y gestión de bases de datos.

A continuación, se presenta la **Matriz RACI** (Responsable, Aprobador, Consultado, Informado) para asignar las responsabilidades de cada integrante de acuerdo con la metodología escogida:

| Tareas / Entregables | Gerencia | Gestión / Análisis | Desarrollo / Arquitectura |
| :--- | :---: | :---: | :---: |
| Planificación del cronograma y presupuesto | R / A | C | I |
| Levantamiento y documentación de requerimientos | I | R / A | C |
| Diseño de Arquitectura y Base de Datos | I | C | R / A |
| Desarrollo de Módulos (Backend / Frontend) | I | C | R / A |
| Pruebas de Software y QA | I | R | C |
| Implementación y Despliegue a Producción | A | C | R |

*(R = Responsible / Ejecutor, A = Accountable / Aprobador final, C = Consulted / Consultado, I = Informed / Informado)*

### 1.6. Plan de Recursos (Paso 6.4)
Para la ejecución exitosa de EspaciGo, se requiere un conjunto específico de recursos que respaldan tanto la arquitectura tecnológica como el desarrollo humano. El presupuesto detallado y justificado (disponible en la sección de Costos y Presupuesto del informe final) se estructura en las siguientes categorías principales:

- **Personal:** 3 Analistas Programadores asumiendo los roles de gerencia, análisis y desarrollo (valorizado en horas-hombre).
- **Equipamiento y Hardware:** Equipos computacionales para el desarrollo local y pruebas (laptops/PC), y dispositivos para testing responsive.
- **Bienes y Servicios (Software e Infraestructura):**
  - **Servicios Cloud:** Hosting para contenedores Docker, almacenamiento, base de datos relacional (MariaDB) y Data Warehouse (BigQuery).
  - **Servicios de Terceros (APIs):** Integración con Mercado Pago (Pasarela y modalidad Escrow) y FirmaVirtual (Generación de contratos dinámicos).
  - **Herramientas de Gestión:** Licencias de software para control de versiones (ej. GitHub), gestión de proyectos y diseño de interfaces (Figma).
