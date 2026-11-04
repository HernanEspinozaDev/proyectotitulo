# CAPÍTULO XIII: MONITOREO, CONTROL Y EVALUACIÓN DEL DESEMPEÑO DEL PROYECTO

## 13.1. Seguimiento de la Línea Base del Cronograma y Desempeño de Iteraciones

El control del proyecto se ejecutó en conformidad con el grupo de procesos de **Seguimiento y Control del estándar PMBOK** (PMI, 2021), evaluando sistemáticamente el avance de los entregables de la EDT frente al calendario académico establecido.

A diferencia de modelos desarticulados donde la planificación se modifica de manera reactiva y sin control, el equipo adoptó un esquema de **Compuertas de Fase (*Phase Gates*)** al término de cada iteración constructiva:

**Figura 22**  
*Esquema de Control por Compuertas de Fase (Phase Gates) y Desempeño de Iteraciones*

![](assets/figuras/fig22_compuertas_fase_gates.png)

*Nota.* Elaboración propia según lineamientos metodológicos de control de proyectos PMBOK (PMI, 2021).

*Métricas de Desempeño del Cronograma:*
*   **Índice de Desempeño del Cronograma (SPI - *Schedule Performance Index*):** El proyecto mantuvo un $\text{SPI} = 0.98$ acumulado, completando las 16 semanas académicas sin desviaciones críticas en la fecha final de entrega.
*   **Gestión de la Ruta Crítica (CPM):** Los paquetes de trabajo vinculados a la persistencia geoespacial (PostGIS) y la integración con la pasarela financiera (*Escrow*) fueron identificados tempranamente como actividades críticas sin holgura, priorizándose la asignación de esfuerzo técnico directo por parte de los tres integrantes.

---

## 13.2. Gestión de Cambios y Control de Variaciones

Cualquier desviación respecto a la Línea Base del Alcance o de la Arquitectura se canalizó mediante el **Procedimiento Integrado de Control de Cambios**:

**Tabla 12**  
*Registro Integrado de Solicitudes y Control de Cambios del Proyecto*

| Solicitud de Cambio (CR) | Origen del Cambio | Impacto Evaluado | Decisión y Medida de Mitigación Adoptada |
|---|---|---|---|
| **CR-01: Reajuste Drástico de RPO y RTO** | Observación de auditoría docente en ES1 sobre SLAs no profesionales (4h y 6h). | Reconfiguración de la persistencia Cloud y políticas de backup. | **Aprobado:** Se implementó *Continuous WAL Archiving* en Cloud SQL y contenedores precalentados en Cloud Run, reduciendo el RPO a $\le 15$ minutos y el RTO a $\le 1$ hora. |
| **CR-02: Transición a Arquitectura Hexagonal** | Necesidad de desacoplar la lógica de pagos y firma remota para pruebas unitarias. | Reestructuración de paquetes en el Backend Go. | **Aprobado:** Se formalizó la separación en `core/domain`, `ports` y `adapters`, elevando la cobertura de pruebas al $86.4\%$. |
| **CR-03: Incorporación de Protocolo Anti-Replay** | Exigencias normativas de la nueva Ley N° 21.719 de Protección de Datos Personales. | Diseño de scripts de purga automatizada en restauraciones DRP. | **Aprobado:** Se creó el catálogo inmutable de supresiones en BigQuery ejecutado automáticamente tras cada evento de recuperación. |

*Nota.* Elaboración propia bajo el estándar de gestión de cambios PMBOK (PMI, 2021).

---

## 13.3. Evaluación del Cumplimiento de Metas y Gestión de la Configuración

La verificación integral del sistema se consolidó mediante la **Matriz de Trazabilidad de Requerimientos**, asegurando que el 100% de los 236 Requerimientos Funcionales y 43 Requerimientos No Funcionales cuenten con una prueba de verificación automatizada:

*   **Completitud de Requerimientos Funcionales:** $236\text{ de }236\text{ RF verificados y conformes } (100\%)$.
*   **Gestión de la Configuración y Versionado:** La totalidad del código fuente, esquemas DDL, especificaciones OpenAPI y documentación técnica se versionaron bajo el estándar **Semantic Versioning (SemVer 2.0.0)** con etiquetas de versión (*tags*) inmutables en Git (`v1.0.0-release`).

---

## 13.4. Lecciones Aprendidas de la Gestión de Ingeniería

El desarrollo integral de la plataforma proporcionó valiosas lecciones para la práctica profesional de la Ingeniería TI:

1. **La Arquitectura a Nivel de Datos Previene la Deuda Técnica:** Trasladar la prevención de sobre-reservas al motor relacional mediante restricciones de exclusión GiST (`tsrange`) en PostgreSQL evitó cientos de líneas de código propenso a fallas de concurrencia en la capa de aplicación.
2. **El Valor del Desacoplamiento Temprano:** Implementar la Arquitectura Hexagonal desde las primeras fases permitió sustituir simuladores de pasarelas de pago por la API real de Mercado Pago sin modificar una sola línea de la lógica de negocio central.
3. **Ciberseguridad y Privacidad como Activos de Negocio:** Diseñar el sistema conforme a la Ley N° 21.719 desde el día uno no solo evitó costosas reestructuraciones de base de datos posteriores, sino que se transformó en el principal argumento de confianza para los propietarios de inmuebles.
