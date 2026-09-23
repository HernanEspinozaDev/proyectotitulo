## Análisis cualitativo y cuantitativo de las tecnologías que serán implementadas

### Necesidades que orientan la comparación

La selección debe responder al ciclo de publicación, búsqueda, reserva, pago y contratación de EspaciGo. La línea base propone Next.js para la presentación, Go para el backend modular, PostgreSQL con PostGIS para los datos operativos y Docker sobre GCP para el despliegue. Estas decisiones constituyen las candidatas iniciales que se examinan en ES2 [@es1formulacion].

El anexo C de ES1 fija condiciones que permiten orientar la evaluación: búsqueda en un máximo de dos segundos con 200 usuarios concurrentes (RNF-001), idempotencia de pagos (RNF-012), disponibilidad mensual de 99,9 % (RNF-009), recuperación con RPO máximo de cuatro horas y RTO máximo de seis horas (RNF-010), y capacidad de 500 usuarios concurrentes y 100 escrituras por segundo (RNF-030). Son objetivos declarados; no son mediciones obtenidas por el producto [@es1anexoc].

### Comparación cualitativa por capa

**Presentación.** La documentación de Next.js permite sustentar la composición de componentes de servidor y de cliente. Para EspaciGo, se propone evaluar esa separación en las páginas públicas del catálogo y en la interacción de búsqueda y reserva. Como alternativa, una aplicación React iniciada desde cero requiere seleccionar y configurar soluciones para enrutamiento y acceso a datos. La comparación debe considerar ese trabajo de integración y el comportamiento de la interfaz; no basta con atribuir mejor rendimiento a un framework por su nombre [@es2nextcomponents; @es2reactapp].

**Backend.** Go documenta goroutines y canales; Node.js organiza la atención de trabajo mediante su event loop y mecanismos auxiliares, con la precaución de evitar operaciones que lo bloqueen. Ambos constituyen alternativas que deben contrastarse bajo el mismo flujo funcional. Para conservar la continuidad del diseño se mantiene Go como candidato inicial, pero su ventaja de latencia, memoria o esfuerzo de desarrollo no se considera demostrada en EspaciGo [@es2goconcurrency; @es2nodeeventloop].

**Persistencia.** PostgreSQL documenta transacciones atómicas y PostGIS permite evaluar proximidad mediante `ST_DWithin`. Son capacidades pertinentes para reservas y búsqueda geográfica. MySQL/InnoDB también documenta transacciones y soporte geoespacial, por lo que debe tratarse como una alternativa real. Se propone comparar restricciones para evitar reservas incompatibles, consultas por distancia, índices y esfuerzo de implementación con datos equivalentes [@es2pgtransactions; @es2postgiswithin; @es2mysqlinnodb].

**Ejecución.** Cloud Run ofrece una plataforma gestionada para ejecutar aplicaciones y contenedores. Compute Engine permite configurar instancias con sistema operativo, recursos de máquina y almacenamiento. La primera opción coincide con la propuesta de ES1; la segunda permite evaluar un despliegue en máquinas virtuales. La preferencia inicial por un servicio gestionado se fundamenta en reducir tareas operativas del equipo, como inferencia de diseño; todavía deben compararse costos y requisitos de cada escenario [@es2cloudrunoverview; @es2computeinstances].

**Auditoría.** La base propone BigQuery como repositorio analítico inmutable. Sin embargo, su documentación incluye operaciones `UPDATE` y `DELETE`. En consecuencia, su selección no satisface por sí sola RNF-017. ES2 deberá definir el modelo de permisos, retención y protección contra alteración, y diseñar una prueba que verifique esas propiedades. Esta observación actualiza el análisis de la propuesta, conservando la formulación entregada en ES1 [@es1formulacion; @es1anexoc; @es2bigquerydml].

### Comparación metodológica

La propuesta de ES1 combina desarrollo iterativo e incremental con prácticas de gestión del PMBOK. La literatura consultada distingue enfoques predictivos, iterativos/incrementales y adaptativos según incertidumbre, cambio y forma de entrega [@es1formulacion; @es2burgan2014].

Para EspaciGo, el catálogo existente permite planificar, pero el acceso a integraciones externas y la capacidad real aún requieren validación. Como valoración del proyecto, se propone conservar incrementos verificables y revisar el alcance después de cada evidencia técnica. Un enfoque exclusivamente predictivo exigiría resolver antes esas incertidumbres; adoptar un marco adaptativo específico exigiría definir roles, prácticas y disponibilidad de retroalimentación. La metodología definitiva se revisará con el equipo antes de cerrar el cronograma.

### Método de evaluación cuantitativa

Se propone una matriz ponderada por capa, con criterios definidos antes de puntuar alternativas. Los pesos siguientes son una propuesta del análisis, pendiente de revisión del equipo; no son una ponderación institucional.

*Tabla. Criterios propuestos para comparar alternativas tecnológicas.* <!--#tab:es2-criterios-tecnologias-->

| Criterio | Peso | Evidencia que permitirá valorar |
| --- | ---: | --- |
| Adecuación funcional | 25 % | Cobertura del flujo y de los requisitos de la capa |
| Integridad, seguridad y recuperación | 20 % | Controles, limitaciones y pruebas vinculadas a RNF |
| Rendimiento y capacidad | 15 % | Latencia, concurrencia, errores y consumo en un escenario reproducible |
| Costo total del escenario | 15 % | Tarifas, volúmenes, licencias y esfuerzo de operación |
| Factibilidad de implementación | 15 % | Acceso, competencias y esfuerzo estimado o registrado |
| Operación y mantenimiento | 10 % | Despliegue, observabilidad, respaldo y reversión |

**Nota.** Elaboración propia para ES2. Los pesos suman 100 %. Ninguna alternativa recibe todavía un puntaje global.

La escala propuesta es de 0 a 4: 0 indica incumplimiento documentado; 1, brechas sustanciales; 2, cumplimiento condicionado a adaptaciones; 3, adecuación documentada con limitaciones identificadas; y 4, adecuación verificada en el escenario de evaluación. La falta de evidencia se registra como **NE: no evaluado**, no como cero. Cada celda debe conservar la justificación y la fuente o prueba correspondiente.

Cuando todas las celdas estén sustentadas, el puntaje será `P = suma(peso_porcentual × valoración / 4)`, en una escala de 0 a 100. La valoración no reemplaza un benchmark: se publicarán por separado las mediciones originales. La interpretación del criterio se fijará para cada capa; no se comparará una herramienta de presentación con una base de datos usando un mismo ranking.

*Tabla. Mediciones iniciales previstas a partir de los requisitos de ES1.* <!--#tab:es2-mediciones-previstas-->

| Escenario | Objetivo de la base | Datos que se registrarán | Estado |
| --- | --- | --- | --- |
| Búsqueda de espacios | RNF-001: máximo 2 s con 200 usuarios | Tiempos individuales, máximo, percentiles auxiliares y errores | Sin ejecutar |
| Capacidad de persistencia | RNF-030: 500 usuarios y 100 escrituras/s | Carga, escrituras completadas, tiempos, errores e integridad | Sin ejecutar |
| Reserva simultánea | Validación de disponibilidad, CU-23 | Operaciones concurrentes, estados y reservas aceptadas | Sin ejecutar |
| Reintento de pago | RNF-012: idempotencia | Claves, intentos y efectos registrados | Sin ejecutar |

**Nota.** Elaboración propia a partir de los anexos C y D de ES1. Un percentil no sustituirá el límite máximo especificado; cualquier cambio del criterio deberá justificarse [@es1anexoc; @es1anexod].

### Factibilidad económica

ES1 estimó el costo de oportunidad del equipo en 14.400.000 CLP: tres integrantes por 16 semanas, 20 horas semanales y 15.000 CLP por hora. Además, consignó 10.950 CLP para dominio y 50.000 CLP para servicios cloud, sumando 14.460.950 CLP. Son antecedentes presupuestarios de la formulación; no constituyen una cotización para el nuevo período [@es1formulacion].

El presupuesto ES2 deberá usar un escenario común para las alternativas. Se propone registrar región, entornos, período de operación, volumen de solicitudes, recursos de cómputo, almacenamiento, tráfico, respaldos y servicios externos. La tarifa de Cloud Run distingue modalidades de facturación y señala costos adicionales, como Cloud Build y Artifact Registry; por tanto, un cálculo limitado al contenedor no representa el costo completo [@es2cloudrunpricing].

El cálculo de trabajo será `costo del período = servicios recurrentes + consumo variable + integraciones + costos iniciales + esfuerzo valorizado`. Se registrarán moneda, fecha de tarifa y conversión usada, separando desembolso efectivo y costo de oportunidad. No se asume que el nivel gratuito de un proveedor cubra las necesidades del proyecto.

[[PENDIENTE: definir el escenario de consumo y obtener tarifas para todas sus partidas; revisar licencias y asignar puntajes económicos solo después de completar el cálculo.]]

### Factibilidad de implementación y decisión provisional

El equipo desarrollará el producto en paralelo a la documentación, con entrega ES2 informada para el 3 de noviembre de 2026. El primer experimento propuesto debe comprobar un recorrido acotado de catálogo, consulta de disponibilidad y reserva, seguido de la validación de integración que resulte habilitada. Esta secuencia es una propuesta de trabajo y requiere acordar capacidad, responsables y alcance de demostración.

Se mantienen Next.js, Go y PostgreSQL/PostGIS como candidatos de continuidad; Docker y Cloud Run permanecen como propuesta de empaquetado y ejecución. La selección final queda condicionada a la evaluación comparativa, al costo y a las pruebas. La función de BigQuery y el acceso a pagos, firma e identidad requieren resolver las brechas registradas antes de afirmar factibilidad integral.

[[PENDIENTE: revisar pesos, completar alternativas y valoraciones, ejecutar experimentos con entorno registrado y cerrar la decisión técnica con el equipo.]]
