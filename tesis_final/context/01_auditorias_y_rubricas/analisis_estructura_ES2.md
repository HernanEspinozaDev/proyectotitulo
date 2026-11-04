# Análisis Estructural: Evaluación Sumativa 2 (ES2) — Proyecto espaciGo

**Documentos analizados:**
- Plantilla oficial INACAP: `TIHI84_U2_ES2_Plantilla_informe_Guía_ABPro.docx` y `TIHI84_U2_ES2_GUÍA_ABPro.docx`.
- Rúbrica oficial: `rubrica_de_calificacion.md` (17 criterios, 60 puntos totales).
- Informe modular previo: `/home/nandev/Documentos/projects/Proyectotitulo/Informes/ES2PT/` (secciones 01 a 08, anexos A-C, `flujodecaja/estudios.md` y `07_cronograma.md`).
- Informe técnico actualizado: `/home/nandev/Documentos/projects/espaciGo/ES2/Informe_Desarrollo_e_Implementacion_espaciGo_ES2.md` (394 KB, versión con arquitectura hexagonal en Go, PostGIS, 110 tablas, ADRs y Ley 21.719).

---

## 1. Estructura Formal de la Plantilla Institucional (TIHI84 - U2)

La plantilla institucional de INACAP para la Evaluación Sumativa 2 exige la siguiente estructura de 10 secciones principales:

```
PRELIMINARES
├── Portada Oficial Institucional (Carrera, Asignatura, Título, Integrantes, Profesor Guía, Fecha)
├── Índice de Contenido / Tabla de Contenido
├── Índice de Tablas
└── Índice de Figuras / Ilustraciones

CUERPO DEL INFORME (ES2)
├── I. Introducción
├── II. Detalle de las Tecnologías a implementar
│   ├── 2.1. Análisis cualitativo/cuantitativo de las tecnologías que serán implementadas
│   └── 2.2. Herramientas, aplicaciones, lenguajes y componentes que serán implementados
├── III. Detalle de la Arquitectura a implementar
│   ├── 3.1. Diagrama BPMN (mínimo 3 procesos principales con subprocesos)
│   ├── 3.2. Diagramas de caso de uso (UML por subsistema)
│   ├── 3.3. Diagrama de componentes
│   ├── 3.4. Modelo de datos (Conceptual, Lógico y Diccionario de datos)
│   ├── 3.5. Topología de comunicaciones (Desarrollo vs. Producción)
│   ├── 3.6. Diagrama de Infraestructura (Cloud, balanceo, bases de datos)
│   └── 3.7. Diagrama de Arquitectura (Patrón de capas / hexagonal)
├── IV. Implementación de los KPI y SLA
│   ├── 4.1. Descripción de KPI (Fichas SMART con método de cálculo y metas)
│   └── 4.2. Descripción de SLA (Acuerdos de Nivel de Servicio con clientes/usuarios)
├── V. Plan de Pruebas y Aseguramiento de Calidad
│   ├── 5.1. Plan de Pruebas (Estrategia, alcance y diseño de casos de prueba)
│   └── 5.2. Normas y Estándares (ISO/IEC 25010, ISO/IEC 27001, OWASP, Ley 21.719)
├── VI. Plan de Implementación
│   ├── 6.1. Gestión de Disponibilidad (Niveles de servicio y redundancia)
│   ├── 6.2. Gestión de Continuidad (Planes proactivos y reactivos BCP/DRP)
│   └── 6.3. Plan de Mantención (Gestión de cambios y gestión de incidentes)
├── VII. Ajustes del Cronograma
│   └── 7.1. Revisión de Carta Gantt o desarrollo de fases (Justificación de adaptaciones)
├── VIII. Conclusiones
├── IX. Referencias bibliográficas (Norma APA 7ma Edición)
└── X. Anexos
```

---

## 2. Rúbrica Oficial de Calificación (60 Puntos Totales)

| Criterio | Descripción del Criterio | Puntos Exc. | Puntos Bueno | Puntos Ins. |
|---|---|:---:|:---:|:---:|
| **2.1.1.1** | Análisis comparativo cualitativo/cuantitativo para selección de tecnologías y metodologías con factibilidad técnica, económica e implementativa. | 3.0 pts | 2.0 pts | 0.0 pts |
| **2.1.1.2** | Describe herramientas, aplicaciones, lenguajes, componentes de HW y servicios TI. | 2.4 pts | 1.6 pts | 0.0 pts |
| **2.1.2.3** | Confecciona y describe BPMN de al menos 3 procesos principales con subprocesos. | 4.8 pts | 3.2 pts | 0.0 pts |
| **2.1.2.4** | Confecciona y describe diagramas UML de casos de uso y diagrama de componentes. | 3.0 pts | 2.0 pts | 0.0 pts |
| **2.1.2.5** | Confecciona diagrama del modelo de datos e incluye el diccionario de datos respectivo. | 4.8 pts | 3.2 pts | 0.0 pts |
| **2.1.2.6** | Confecciona y describe el diagrama de Topología de comunicación. | 3.0 pts | 2.0 pts | 0.0 pts |
| **2.1.2.7** | Confecciona diagrama de diseño de infraestructura TI de soporte. | 3.0 pts | 2.0 pts | 0.0 pts |
| **2.1.2.8** | Confecciona y describe diagrama de Arquitectura (SW y HW). | 3.0 pts | 2.0 pts | 0.0 pts |
| **2.1.3.9** | Detalle SMART de indicadores clave (KPI) para medir eficiencia. | 4.8 pts | 3.2 pts | 0.0 pts |
| **2.1.3.10** | Detalla acuerdos de nivel de servicio (SLA) con resultados esperados. | 4.8 pts | 3.2 pts | 0.0 pts |
| **2.1.4.11** | Elabora Plan de Pruebas determinando y detallando las pruebas a realizar. | 4.8 pts | 3.2 pts | 0.0 pts |
| **2.1.4.12** | Especifica y justifica normas y estándares incorporados (ISO/IEC, seguridad, legal). | 3.6 pts | 2.4 pts | 0.0 pts |
| **2.1.5.13** | Define aspectos de servicios TI para cumplir objetivos de disponibilidad. | 3.6 pts | 2.4 pts | 0.0 pts |
| **2.1.5.14** | Describe procedimientos proactivos y reactivos ante desastres (BCP/DRP). | 3.6 pts | 2.4 pts | 0.0 pts |
| **2.1.5.15** | Define procedimientos para control de cambios y gestión de incidentes. | 3.0 pts | 2.0 pts | 0.0 pts |
| **2.1.6.16** | Presenta planificación en Carta Gantt o detalle de fases. | 2.4 pts | 1.6 pts | 0.0 pts |
| **2.1.6.17** | Revisa y justifica adecuación del cronograma en funcionalidad y capacidad. | 2.4 pts | 1.6 pts | 0.0 pts |
| **TOTAL** | **17 Criterios Evaluativos** | **60.0 pts** | **40.0 pts** | **0.0 pts** |

---

## 3. Contraste de las Dos Versiones Existentes de ES2

Para el proyecto espaciGo existen dos versiones de trabajo del informe ES2 con fortalezas y vacíos complementarios:

| Dimensión | Versión Previa (`ES2PT`) | Versión Actualizada (`espaciGo/ES2`) | Estado para la Tesis Final |
|---|---|---|---|
| **Estructura de Secciones** | Dividida en archivos modulares `01_` a `08_`. | Documento consolidado de 394 KB con alta densidad técnica. | Se adopta el modelo consolidado para el cuerpo. |
| **Backend y Arquitectura** | API genérica en Go. | **Arquitectura Hexagonal formal (Ports & Adapters)** con Go 1.27 + Next.js 16 (BFF). | **espaciGo/ES2 es superior.** |
| **Base de Datos** | PostgreSQL relacional clásico (30 tablas). | **PostgreSQL 18 con extensión PostGIS 3.6 y exclusión GiST** (110 tablas documentadas). | **espaciGo/ES2 es infinitamente superior.** |
| **Decisiones Técnicas** | Tablas cuali/cuanti simples. | **7 Registros de Decisiones de Arquitectura (ADRs)** formales + matrices multicriterio. | Incorporar los ADRs como estándar en Anexos. |
| **Procesos BPMN** | Flujos básicos de arriendo. | **3 Procesos BPMN complejos:** Reserva/Escrow, KYC/KYB y Ejercicio de Derechos ARCO (Ley 21.719). | Cumple al 100% el criterio 2.1.2.3. |
| **Pruebas y QA** | Matriz general de pruebas. | **16 Casos de Prueba Críticos (PT-01 a PT-16)** con pruebas de concurrencia y GiST. | Formato ideal para el Anexo de pruebas. |
| **Operación y Resiliencia** | Procedimientos narrativos breves. | **6 Runbooks Operacionales (RB-01 a RB-06)** con protocolos SRE paso a paso. | Eleva el nivel profesional del Plan de Implementación. |
| **Planificación y Carta Gantt** | **Presente** en `07_cronograma.md` (hitos, fases y riesgos). | **Omitida temporalmente** (dejada como pendiente en el informe). | **Debe rescatarse de ES2PT e integrarse.** |
| **Evaluación Económica** | **Presente** en `flujodecaja/estudios.md` y `anexos/A_evaluacion_economica.md`. | **Omitida** (solo contiene un presupuesto cloud mensual). | **Debe rescatarse de ES2PT y expandirse.** |

---

## 4. Jerarquía Detallada de la Versión Actualizada (`espaciGo/ES2`)

La versión de `/home/nandev/Documentos/projects/espaciGo/ES2/Informe_Desarrollo_e_Implementacion_espaciGo_ES2.md` posee una estructura de ingeniería de software sobresaliente:

```
# 1. Detalle de las Tecnologías a Implementar
├── 1.1. Análisis cualitativo y cuantitativo de tecnologías
├── 1.2. Selección y justificación del stack tecnológico
│   ├── 1.2.1. Comparación metodológica y marco de desarrollo
│   ├── 1.2.2. Backend Core: Go 1.27 y Arquitectura Hexagonal
│   ├── 1.2.3. Frontend Web: Next.js 16, React 19 y Tailwind CSS 4
│   └── 1.2.4. Persistencia: PostgreSQL 18 con PostGIS y GiST
├── 1.3. Factibilidad técnica y condiciones del entorno
│   ├── 1.3.1. Condiciones del entorno de desarrollo de ingeniería
│   └── 1.3.2. Factibilidad técnica de la arquitectura
└── 1.4. Factibilidad económica y presupuesto de operación
    ├── 1.4.1. Presupuesto mensual de infraestructura cloud (Piloto Santiago)
    └── 1.4.2. Modelo de comisiones, costos transaccionales y punto de equilibrio

# 2. Modelamiento de la solución
├── 2.1. Modelamiento de procesos de negocio (BPMN)
│   ├── 2.1.1. BPMN 1: Flujo de Reserva, Custodia Financiera (Escrow), Firma y Operación
│   ├── 2.1.2. BPMN 2: Acreditación de Identidad (KYC/KYB), Multimedia y Moderación
│   └── 2.1.3. BPMN 3: Ejercicio de derechos ARCO y supresión de datos (Ley 21.719)
├── 2.2. Especificación de los casos de uso
│   ├── A. Diagrama General de Casos de Uso UML del Ecosistema
│   ├── B. Matriz de Mapeo Arquitectónico de Casos de Uso Canónicos
│   └── C. Fichas Técnicas Individuales de Casos de Uso (UC-01 a UC-14)
├── 2.3. Diagrama de Arquitectura de Software Hexagonal e Integración Frontend BFF
├── 2.4. Modelo Lógico Relacional y Geoespacial (Núcleo PostGIS)
│   ├── A. Diagrama Lógico Entidad-Relación Núcleo
│   └── B. Diccionario de Datos de Entidades Transaccionales (3 Dominios)
├── 2.5. Topología de Comunicaciones y Segmentación de Red
│   ├── A. Diagrama de Red y Segmentación de Comunicaciones
│   └── B. Especificación Técnica de Protocolos, Puertos y Formatos
├── 2.6. Diagrama de Infraestructura Cloud en Google Cloud Platform
└── 2.7. Diagrama de Arquitectura Global de la Solución espaciGo

# 3. Implementación de KPI y SLA
├── 3.1. Descripción y Fichas SMART de Indicadores Clave (KPI)
└── 3.2. Descripción de Acuerdos de Nivel de Servicio (SLA)
    ├── A. Ficha Formal de Especificación del SLA
    └── B. Matriz Resumen de Objetivos de Nivel de Servicio (SLO)

# 4. Plan de Pruebas y Aseguramiento de Calidad
├── 4.1. Plan de Pruebas
│   ├── A. Pirámide de Pruebas y Estrategia de Verificación
│   └── B. Matriz de Casos de Prueba Críticos
└── 4.2. Normas y Estándares de Ingeniería de Software
    ├── A. Modelo de Calidad ISO/IEC 25010:2011
    ├── B. Seguridad ISO/IEC 27001 y OWASP Top 10
    └── C. Normativa Chilena de Protección de Datos Personales: Ley N° 21.719

# 5. Plan de Implementación y Operación
├── 5.1. Gestión de Disponibilidad y Continuidad Operacional
│   ├── A. Objetivos de Nivel de Servicio y Metas de Recuperación
│   └── B. Arquitectura de Alta Disponibilidad y Resiliencia
├── 5.2. Gestión de Seguridad, Contingencia y Recuperación ante Desastres (DRP)
│   ├── A. Matriz de Riesgos Operacionales y Estrategias de Mitigación
│   ├── B. Procedimientos Operativos Estandarizados (Runbooks de Contingencia)
│   └── C. Diagrama de Respaldo, DRP y Replay Anti-Restauración
└── 5.3. Plan de Mantención, Gestión de Cambios y Respuesta a Incidentes
    ├── A. Tipologías de Mantención de Software
    ├── B. Procedimiento Formal de Gestión de Cambios (Change Management)
    └── C. Gestión de Incidentes, Protocolo de Escalamiento y Monitoreo SRE

ANEXOS TÉCNICOS INTEGRADOS EN ESPACIGO/ES2
├── Anexo A — Decisiones de Arquitectura (ADR-001 a ADR-007) y Matriz Multicriterio
├── Anexo B — Diccionario de Datos del Esquema Físico PostgreSQL (110 Tablas)
├── Anexo C — Catálogo de Casos de Prueba Detallados (PT-01 a PT-16)
├── Anexo D — Runbooks Operacionales y Procedimientos de Contingencia (RB-01 a RB-06)
├── Anexo E — Especificación Canónica de Contratos de API REST (OpenAPI 3.1)
├── Anexo F — Cumplimiento Técnico y Regulatorio de la Ley N° 21.719
├── Anexo G — Registro de Brechas, Decisiones y Deuda Técnica Controlada
└── Anexo H — Matriz de Trazabilidad Global de Requerimientos (RF-01 a RF-25 y RNF-01 a RNF-15)
```

---

## 5. La Pieza Faltante: Planificación y Economía (Rescate desde `ES2PT`)

Para que este contenido ensamble de forma perfecta en la Tesis de Grado final, se deben rescatar e integrar los dos componentes que quedaron fuera de `espaciGo/ES2` pero que existen en `ES2PT`:

### 5.1. El Capítulo de Ajustes del Cronograma (Rescate de `secciones/07_cronograma.md`):
- En la plantilla institucional U2, este acápite corresponde al **Capítulo VII**. En la tesis final, pasará a ser el **Capítulo XIV**.
- Debe contener la tabla de fases operativas, los hitos verificables documentales (H1 a H6), la matriz de riesgos del cronograma y la justificación de por qué la arquitectura hexagonal y la modularidad de Go reducen los tiempos de integración y desarrollo.

### 5.2. El Estudio de Factibilidad Económica (Rescate de `flujodecaja/estudios.md` y `anexos/A_evaluacion_economica.md`):
- En la plantilla U2 este punto solo se toca superficialmente en el criterio 2.1.1.1. Pero en la Tesis Final de Grado, constituye el monumental **Capítulo XIII (Factibilidad Económica)**.
- Debe estructurarse formalmente con:
  1. Estudio de Mercado Estratégico (PESTEL, Porter, Segmentación STP, FODA, 4P).
  2. Balances de Inversión y Operación (Mano de obra, Servidores Cloud GCP, Costos transaccionales de Mercado Pago y FirmaVirtual, Capital de trabajo).
  3. Flujo de Caja Proyectado a 5 años con evaluación financiera completa: cálculo de **VAN, TIR, Payback y ROI** bajo modelo CAPM con tasa Ke.
