## Análisis cualitativo y cuantitativo de las tecnologías que serán implementadas

### Necesidades que orientan la comparación

La selección debe responder al ciclo de publicación, búsqueda, reserva, pago y contratación de EspaciGo. La línea base propone Next.js para la presentación, Go para el backend modular, PostgreSQL con PostGIS para los datos operativos y Docker sobre GCP para el despliegue. Estas decisiones constituyen las candidatas iniciales que se examinan en ES2.

La entrega anterior fija condiciones que permiten orientar la evaluación: búsqueda en un máximo de dos segundos con 200 usuarios concurrentes (RNF-001), idempotencia de pagos (RNF-012), disponibilidad mensual de 99,9 % (RNF-009), recuperación con RPO máximo de cuatro horas y RTO máximo de seis horas (RNF-010), y capacidad de 500 usuarios concurrentes y 100 escrituras por segundo (RNF-030). Son objetivos declarados; no son mediciones obtenidas por el producto.

### Comparación cualitativa por capa

**Presentación.** La documentación de Next.js permite sustentar la composición de componentes de servidor y de cliente. Para EspaciGo, se propone evaluar esa separación en las páginas públicas del catálogo y en la interacción de búsqueda y reserva. Como alternativa, una aplicación React iniciada desde cero requiere seleccionar y configurar soluciones para enrutamiento y acceso a datos. La comparación debe considerar ese trabajo de integración y el comportamiento de la interfaz; no basta con atribuir mejor rendimiento a un framework por su nombre [@es2nextcomponents; @es2reactapp].

**Backend.** Go documenta goroutines y canales; Node.js organiza la atención de trabajo mediante su event loop y mecanismos auxiliares, con la precaución de evitar operaciones que lo bloqueen. Ambos constituyen alternativas que deben contrastarse bajo el mismo flujo funcional. Para conservar la continuidad del diseño se mantiene Go como candidato inicial, pero su ventaja de latencia, memoria o esfuerzo de desarrollo no se considera demostrada en EspaciGo [@es2goconcurrency; @es2nodeeventloop].

**Persistencia.** PostgreSQL documenta transacciones atómicas y PostGIS permite evaluar proximidad mediante `ST_DWithin`. Son capacidades pertinentes para reservas y búsqueda geográfica. MySQL/InnoDB también documenta transacciones y soporte geoespacial, por lo que se compara como alternativa técnica. Sin embargo, RNF-038 fija PostgreSQL como base: reemplazarlo exigiría registrar y justificar un cambio de requisito en ES2. Se propone contrastar restricciones para evitar reservas incompatibles, consultas por distancia, índices y esfuerzo de implementación con datos equivalentes [@es2pgtransactions; @es2postgiswithin; @es2mysqlinnodb].

**Ejecución.** Cloud Run ofrece una plataforma gestionada para ejecutar aplicaciones y contenedores. Compute Engine permite configurar instancias con sistema operativo, recursos de máquina y almacenamiento. La primera opción coincide con la propuesta de ES1; la segunda permite evaluar un despliegue en máquinas virtuales. La preferencia inicial por un servicio gestionado se fundamenta en reducir tareas operativas del equipo, como inferencia de diseño; todavía deben compararse costos y requisitos de cada escenario [@es2cloudrunoverview; @es2computeinstances].

**Auditoría.** La base propone BigQuery como repositorio analítico inmutable. Sin embargo, su documentación incluye operaciones `UPDATE` y `DELETE`. En consecuencia, su selección no satisface por sí sola RNF-017. ES2 deberá definir el modelo de permisos, retención y protección contra alteración, y diseñar una prueba que verifique esas propiedades. Esta observación actualiza el análisis de la propuesta, conservando la formulación entregada en la entrega anterior [@es2bigquerydml].

### Comparación metodológica

La propuesta de la entrega anterior combina desarrollo iterativo e incremental con prácticas de gestión del PMBOK. La literatura consultada distingue enfoques predictivos, iterativos/incrementales y adaptativos según incertidumbre, cambio y forma de entrega [@es2burgan2014; @pmbok7].

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

*Tabla. Valoración documental ilustrativa por capa, escala 0–4.* <!--#tab:es2-valoracion-tecnologias-->

| Capa y alternativa | Adec. | Integ. | Costo | Factib. | Oper. | Pond. |
| ---------------------------- | -----: | -----: | -----: | ------: | -----: | -----: |
| Presentación: Next.js sobre React | 4 | 3 | 3 | 3 | 3 | 82,35 |
| Presentación: React desde cero | 3 | 3 | 2 | 2 | 2 | 63,24 |
| Backend: Go | 4 | 3 | 3 | 3 | 3 | 82,35 |
| Backend: Node.js | 4 | 3 | 3 | 3 | 3 | 82,35 |
| Persistencia: PostgreSQL/PostGIS | 4 | 4 | 3 | 3 | 3 | 88,24 |
| Persistencia: MySQL/InnoDB | 3 | 3 | 3 | 2 | 3 | 70,59 |
| Ejecución: Cloud Run | 3 | 3 | NE | 3 | 3 | 75,00 |
| Ejecución: Compute Engine (VM) | 3 | 3 | NE | 2 | 2 | 66,07 |
| Auditoría: Cloud Storage bloqueado | 3 | 3 | 2 | 3 | 3 | 70,59 |
| Auditoría: BigQuery como garantía | 1 | 1 | 3 | 3 | 2 | 45,59 |

**Nota.** Elaboración propia a partir de la documentación citada en esta sección y de las fuentes primarias del inventario de 2.2. Es una **valoración ilustrativa de trabajo** (SUP-04), no un benchmark ni una medición. Los encabezados abrevian los criterios y su peso: **Adec.** es adecuación funcional (25 %); **Integ.**, integridad, seguridad y recuperación (20 %); **Costo**, costo total del escenario (15 %); **Factib.**, factibilidad de implementación (15 %); **Oper.**, operación y mantenimiento (10 %); y **Pond.**, el ponderado documental renormalizado. El criterio «Rendimiento y capacidad» (15 %) queda **NE, no evaluado**, en todas las capas porque no existe ningún ensayo ejecutado; por eso el ponderado se recalcula sobre el peso evaluado, que es **85 %** en presentación, backend, persistencia y auditoría y **70 %** en ejecución, donde el costo de Santiago tampoco pudo compararse. Ninguna celda usa el nivel 4, reservado a la adecuación verificada en el escenario de evaluación, y «NE» no equivale a cero.

El resultado separa con claridad dos capas y deja tres diferencias menores. La persistencia y la auditoría concentran la mayor distancia documental: PostgreSQL con PostGIS conserva ventaja por cobertura funcional, integridad y continuidad del diseño, y la retención bloqueada de Cloud Storage supera a BigQuery como garantía de inmutabilidad porque la documentación de BigQuery incluye `UPDATE` y `DELETE`. En cambio, **Go y Node.js quedan igualados**: la ventaja de latencia, memoria o esfuerzo de desarrollo que suele atribuirse a uno u otro no está medida en EspaciGo, de modo que la continuidad de Go se sostiene por menor cambio de diseño y no por superioridad demostrada. Cloud Run supera a las máquinas virtuales en factibilidad y operación, pero **su costo en Santiago queda sin evaluar**: el ejercicio propio de 2.1 se hizo con precios de Iowa y una carga hipotética, sin exportación del calculador ni SKU comparables. La consecuencia práctica es que la valoración **no autoriza** a declarar qué alternativa es mejor en rendimiento ni en costo; solo sustenta la decisión provisional de continuidad (SUP-04) con Next.js, Go, PostgreSQL/PostGIS, contenedores y Cloud Run en Santiago, y deja el ensayo comparativo como el trabajo que sustituiría esta tabla.

*Tabla. Mediciones iniciales previstas a partir de los requisitos de ES1.* <!--#tab:es2-mediciones-previstas-->

| Escenario | Objetivo de la base | Datos que se registrarán | Estado |
| --- | --- | --- | --- |
| Búsqueda de espacios | RNF-001: máximo 2 s con 200 usuarios | Tiempos individuales, máximo, percentiles auxiliares y errores | Sin ejecutar |
| Capacidad de persistencia | RNF-030: 500 usuarios y 100 escrituras/s | Carga, escrituras completadas, tiempos, errores e integridad | Sin ejecutar |
| Reserva simultánea | Validación de disponibilidad, CU-23 | Operaciones concurrentes, estados y reservas aceptadas | Sin ejecutar |
| Reintento de pago | RNF-012: idempotencia | Claves, intentos y efectos registrados | Sin ejecutar |

**Nota.** Elaboración propia a partir de los criterios de la entrega anterior. Un percentil no sustituirá el límite máximo especificado; cualquier cambio del criterio deberá justificarse.

### Factibilidad económica

La entrega anterior eligió la **comisión por transacción** como modelo de negocio. Para ES2 se investiga un segundo ingreso posible: un destaque pagado por el arrendador dentro del catálogo, limitado a una publicación, categoría, zona y duración. Es una ampliación propuesta, no una decisión validada ni ingreso actual. No debe confundirse con **Meta Ads**, que sería un gasto de EspaciGo para atraer usuarios. La subasta de Meta combina puja, probabilidad de acción y calidad, de modo que el presupuesto no garantiza reservas; un experimento necesitaría medir adquisición y conversión por categoría [@es2metasubasta].

Para medir la captación se separan los dos embudos: el de arrendadores, con publicaciones aprobadas y disponibles, y el de arrendatarios, con reservas pagadas no anuladas, en la misma zona, categoría y modalidad. El gasto de **357.000 CLP de caja** que el Anexo A asigna hipotéticamente a captación durante seis meses es un techo presupuestario a distribuir, no una campaña Meta ejecutada ni una nueva partida de igual monto. Meta Blueprint permite elegir objetivos y revisar resultados, pero ninguna tarifa fija por reserva o retorno de EspaciGo se desprende de ello. La segmentación permitida y las reglas de vivienda deben comprobarse para cada anuncio en Chile; Pixel o API de Conversiones requerirían antes una revisión de datos personales [@es2metaobjetivos; @es2metapresupuesto; @es2metavivienda].

La propuesta de ordenamiento reserva como máximo un cupo identificado como «Patrocinado» por bloque de resultados y solo entre espacios que cumplen filtro, disponibilidad y controles. Los demás resultados conservan orden orgánico por pertinencia y preferencia del usuario. Esta separación toma como referencia la publicidad de publicaciones de Mercado Libre y el criterio de identificación clara de publicidad nativa de SERNAC; el diseño y sus términos quedan pendientes de validación [@es2mercadoads; @es2sernacpublicidad].

La estimación de la entrega anterior valoró el costo de oportunidad del equipo en 14.400.000 CLP: tres integrantes por 16 semanas, 20 horas semanales y 15.000 CLP por hora. Además, consignó 10.950 CLP para dominio y 50.000 CLP para servicios cloud, sumando 14.460.950 CLP. Son antecedentes presupuestarios de la formulación; no constituyen una cotización para el nuevo período.

El **Anexo A** desarrolla el escenario vigente de autofinanciación. El primer ejercicio económico de esta entrega, que suponía ventas desde el primer año y VAN positivo, queda como antecedente pedagógico superado; no representa el presupuesto actual. Siguiendo los componentes de inversión, operación, flujos y riesgo de la evaluación de proyectos, se separan caja, fondos de terceros y tiempo no remunerado de los fundadores [@es2sapag2014]. El usuario informó que todavía no existen ingresos ni funcionalidades implementadas. Para simular con prudencia se fija **año 1 sin ventas**; los años 2–3 contienen demanda hipotética, no una previsión confirmada.

El perfil técnico presupuestado usa Cloud Run para dos servicios y PostgreSQL/PostGIS en Cloud SQL, además de almacenamiento, salida de datos, balanceador, WAF, registros y un entorno de ensayo limitado. La referencia tarifaria vigente es **Santiago** (`southamerica-west1`), aplicada por decisión del usuario del 23-09-2026 con las tarifas publicadas por Google Cloud para esa región; ya no se usa la provisión regional del 35 % sobre precios de Iowa. El piloto suma **USD 237,82/mes de tarifas**, equivalentes a **237.819 CLP netos** o **283.005 CLP de caja** bajo un supuesto de IVA adicional del 19 %. La arquitectura no está dimensionada ni desplegada y debe contrastarse con ensayos de capacidad. El ejercicio comparativo propio conserva precios de Iowa como control documental entre Cloud Run y máquinas virtuales; no es el presupuesto vigente [@es2cloudsqlpricing; @es2cloudrunpricing; @es2gcspricing].

Para evitar comparar configuraciones de distinta disponibilidad, se recalcula un escenario **separado** en Iowa con la misma carga simulada, Cloud SQL regional de alta disponibilidad, almacenamiento, red, balanceador y protección para Cloud Run y dos VM E2. Resulta en **USD 297,01/mes** con Cloud Run sin instancias mínimas y **USD 393,39/mes** con dos VM, antes de impuestos y provisión regional. La diferencia de USD 96,39 se refiere a esta carga hipotética; no mide rendimiento ni equivale a precio para Santiago. El piloto vigente de USD 237,82 usa una base sin alta disponibilidad y no puede presentarse como alternativa equivalente de continuidad. Las capacidades y los SKU de la región elegida siguen por comprobar [@es2cloudrunpricing; @es2computeprecios; @es2cloudsqlpricing].

Se evalúa constituir una SpA con **3.000 acciones iguales: 1.000 para cada uno de los tres fundadores**. La propuesta del equipo es inscribir **631200 (Portales web) como actividad principal y 731001 (Servicios de publicidad prestados por empresas) como complementaria**. La comisión por reserva obliga a consultar al contador/SII si esa prestación queda cubierta por 631200 o requiere **682000 u otra actividad**; 682000 no forma parte de la propuesta actual. Se presupuesta una sola patente comercial para la SpA en ese domicilio, independientemente del número de giros, con un mínimo ilustrativo de **1 UTM anual**. El domicilio elegido para la simulación es Oficina Express en Santiago Centro: **50.000 CLP/año IVA incluido**, más **5.000 CLP una vez** por firma electrónica del contrato. La oferta no prueba aceptación municipal del domicilio ni liquidación del importe [@es2resacciones; @es2siiactividades; @es2ineciiu; @es2oficinaexpress; @es2rentasmunicipales; @es2utm2026].

El complemento **731001** se propone por el destaque pagado previsto, aunque todavía no hay ventas de ese servicio. El SII clasifica esa actividad como afecta a IVA; su oficio sobre anuncios en una aplicación móvil ofrece una analogía de facturación del servicio propio, no un pronunciamiento sobre EspaciGo. La comisión, el destaque y el arriendo del tercero requieren bases y documentos separados. El objeto social, la clasificación definitiva y el emisor de cada documento continúan sujetos a revisión del contador/SII [@es2siicatalogo; @es2siipublicidadapp].

El 25 % se interpreta como **margen sobre ingresos propios de comisión**, no como recargo sobre costo ni porcentaje de rentabilidad del capital. El modelo supone una comisión neta del 12 % del arriendo y cobra pasarela sobre el pago completo; firma, identidad y devolución se provisionan aparte. El IPC anual del **4 %** es supuesto y distinto del dato observado; el **27 % de Primera Categoría** se mantiene para el ejercicio solicitado, sin atribuirlo automáticamente a toda SpA. Pro Pyme General y sus tasas según ejercicio comercial requieren revisión particular [@es2ineipc202608; @es2siitasas; @es2siipro_pyme; @es2mptarifas].

*Tabla. Resultado de la simulación bootstrap a tres años.* <!--#tab:es2-resumen-economico-->

| Indicador | Resultado | Interpretación |
| --- | ---: | --- |
| Salida de caja del primer año, sin ventas ni sueldos | 4.815.743 CLP | Incluye 1.022.000 iniciales y 3.793.743 de operación |
| Fondo recomendado para el primer año con reserva del 20 % | 5.778.891 CLP | Cerca de 1.926.297 por fundador si financian en partes iguales |
| Déficit máximo acumulado en 36 meses | 6.246.529 CLP | Ocurre en el mes 19 bajo las ventas simuladas |
| VAN de caja, tasa nominal supuesta del 12 % | -1.791.437 CLP | Horizonte de 36 meses; sin sueldo pagado a fundadores |
| TIR del flujo de caja | -9,20 % | Resultado matemático del escenario, no retorno observado |
| Costo de oportunidad del trabajo del primer año | 43.200.000 CLP | Se informa aparte, sin convertirlo en desembolso ni capital social |

**Nota.** Elaboración propia con entradas reproducibles en el Anexo A. El margen operativo modelado del año 3 es **23,35 %**, inferior a la meta de 25 %, aun sin remuneración fundadora. La evaluación económica que valora ese trabajo es más desfavorable. No se concluye viabilidad comercial: faltan evidencia de demanda, precios aceptados, tarifa e incidencia real de pagos divididos, cotizaciones locales, régimen tributario y pruebas de capacidad. La liquidación publicada de Split asigna inicialmente la tarifa al vendedor, distinta de la absorción económica supuesta en la caja [@es2mpsplitflujo].

La muestra de precios publicados recogida para esta entrega confirma que los precios corresponden a **unidades distintas**: oficina y sala por hora, stand por bloque de días, minibodega y local por mes, estacionamiento por hora y parcela por jornada cotizada. EspaciGo mantendrá el alcance de todos los tipos de arriendo; cada uno requiere demanda, precio, capacidad y costo por operación propios. Una reserva de 100.000 CLP no es un promedio de mercado. Manteniendo el volumen hipotético del cálculo, tickets uniformes de 30.000 y 50.000 CLP llevan el VAN de caja a **-14,36 y -10,43 millones** respectivamente; 150.000 CLP lo vuelve positivo en **4,51 millones**, condicionado a un precio y una demanda sin comprobar. El caso de 30.000 CLP ni siquiera cubre los costos variables de la reserva bajo las tarifas asumidas [@es2lofespacios; @es2coworkcentro; @es2bltprecios; @es2saba; @es2busho; @es2espaciotemporal; @es2palmas].

El protocolo de medición definido para esta entrega establece cómo sustituir esos supuestos por evidencia: fichas comparables por `categoría × modalidad × comuna`, entrevistas de ambos lados, búsqueda asistida y, solo tras habilitar el producto, reservas pagadas conciliadas. Las estadísticas de empresas y población permiten contextualizar zonas, pero no estiman reservas de EspaciGo. Una cuota exploratoria o un contacto tampoco representa demanda transaccional. Se conservarán numeradores, denominadores y rechazos por cohorte antes de alimentar los 36 meses de cada segmento [@es2siiestadisticas; @es2ele7; @es2censo2024; @es2aaporpracticas].

### Contraste con un escenario segmentado por categoría

Para medir cuánto depende el resultado del ticket único se ejecutó un **escenario segmentado explícitamente sintético** con entradas reproducibles en `investigacion/supuestos_segmentado.json`. Conserva el **mismo volumen hipotético** de 0, 720 y 1.800 reservas al año y lo reparte en cinco categorías, usando como arriendo unitario los **precios de lista** ya transcritos en la muestra dirigida: una hora de oficina privada (7.140 CLP), un bloque mínimo de dos horas de sala (42.245 CLP), un mes de minibodega (55.000 CLP), una hora de estacionamiento (2.940 CLP) y el bloque mínimo de cuatro días de stand (83.000 CLP). No se inventó ningún precio ni se promediaron unidades distintas; lo sintético es el reparto del volumen, decidido por el análisis para poder calcular.

*Tabla. Escenario segmentado sintético frente al caso base, CLP.* <!--#tab:es2-escenario-segmentado-->

| Concepto | Caso base, ticket único de 100.000 CLP | Escenario segmentado sintético |
| --- | ---: | ---: |
| Reservas de los años 2 y 3 | 720 y 1.800 | 720 y 1.800, repartidas en cinco categorías |
| Contribución del año 3, ingresos propios menos costos variables | 10.424.507 | 350.688 |
| Costos fijos netos del año 3 | 4.968.346 | 4.968.346 |
| VAN de caja a 36 meses, tasa nominal supuesta del 12 % | -1.791.437 | -12.771.812 |
| Déficit máximo acumulado en 36 meses | 6.246.529 | 15.891.086 |
| TIR del flujo de caja | -9,20 % | No definida: los tres flujos anuales son negativos |

**Nota.** Elaboración propia con `Informes/herramientas/simular_bootstrap.py`; el detalle mensual y por segmento queda en los JSON de `build/`. La contribución por categoría en el año 3 es **-935.862 CLP** en oficina por hora, **+206.114** en sala por dos horas, **+621.038** en bodega mensual, **-1.072.489** en estacionamiento por hora y **+1.531.886** en stand por bloque. El signo reproduce la frontera ya calculada: con 12 % de comisión, 3,19 % de pasarela sobre el cobro y unos 3.000 CLP de cargos variables por reserva, ninguna reserva bajo 35.909 CLP de arriendo cubre sus propios costos variables.

El contraste no mide demanda y no reemplaza al caso base: cambia solo la composición del catálogo. Su utilidad es mostrar que **el ticket medio de 100.000 CLP oculta categorías que no cubren sus costos variables** y que el resultado depende tanto de la mezcla como del volumen. Un catálogo que abarque todas las categorías con reservas cortas no puede evaluarse con un ticket uniforme, y esa conclusión refuerza el protocolo de medición por `categoría × modalidad` descrito arriba en lugar de sustituirlo.

[[PENDIENTE: sustituir el ticket único y el reparto sintético por precio final, duración, capacidad, ocupación, rechazos y demanda medidos en cada tipo de arriendo; confirmar giro, régimen, patente, oficina y capital con profesionales y municipio; y comparar el costo de Cloud Run frente a VM en Santiago con SKU y cotización antes de aprobar presupuesto.]]

### Factibilidad de implementación y decisión provisional

El equipo desarrollará el producto en paralelo a la documentación, con entrega ES2 informada para el 3 de noviembre de 2026. El primer experimento propuesto debe comprobar un recorrido acotado de catálogo, consulta de disponibilidad y reserva, seguido de la validación de integración que resulte habilitada. Esta secuencia es una propuesta de trabajo y requiere acordar capacidad, responsables y alcance de demostración.

Se mantienen Next.js, Go y PostgreSQL/PostGIS como candidatos de continuidad; Docker y Cloud Run permanecen como propuesta de empaquetado y ejecución. La selección final queda condicionada a la evaluación comparativa, al costo y a las pruebas. La función de BigQuery y el acceso a pagos, firma e identidad requieren resolver las brechas registradas antes de afirmar factibilidad integral.

**Decisión provisional documentada (SUP-04).** Con los pesos definidos antes de puntuar, las alternativas inventariadas y el ponderado documental calculado, la parte documental de esta decisión queda resuelta: se conservan Next.js, Go, PostgreSQL/PostGIS, contenedores y Cloud Run en Santiago, y BigQuery se mantiene solo como analítica, nunca como garantía de inmutabilidad. Lo que falta no es redacción sino evidencia: ejecutar los ensayos comparativos con entorno registrado —incluido el costo con SKU comparables en la región decidida— y ratificar la elección con el equipo. Esa obligación empírica queda registrada en la sección de producto de [pendientes](../pendientes.md) y **no se marca como cumplida**.
