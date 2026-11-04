# CAPÍTULO I: INTRODUCCIÓN Y CONTEXTO DEL PROYECTO

## 1.1. Introducción

El presente proyecto de titulación expone la fundamentación, diseño arquitectónico, desarrollo e implementación de **espaciGo**, una plataforma web transaccional y multilateral concebida para abordar y resolver las ineficiencias estructurales que afectan al mercado de arrendamiento de espacios físicos no residenciales en Chile. 

Históricamente, el sector inmobiliario comercial, corporativo e industrial opera bajo paradigmas rígidos heredados de modelos analógicos. La intermediación tradicional impone barreras de entrada considerables: contratos forzosos de 12 a 36 meses de duración, solicitudes desmedidas de avales y garantías bancarias, procesos manuales de redacción contractual y prolongados períodos de vacancia física entre arrendatarios sucesivos. Esta estructura contractualmente estática genera una severa asimetría entre propietarios de inmuebles —quienes asumen el devengo continuo de gastos comunes, contribuciones territoriales y seguros operacionales sin retorno económico— y una demanda creciente de microempresas, emprendedores de comercio electrónico (*e-commerce*), profesionales independientes y productores logísticos que demandan acceso flexible e inmediato a infraestructura física por días, semanas o meses (Cámara Chilena de la Construcción [CChC], 2024).

Frente a este escenario, la Ingeniería en Tecnologías de Información y Ciberseguridad provee los mecanismos técnicos idóneos para desacoplar el uso productivo del espacio físico de las ataduras del arrendamiento tradicional. La plataforma **espaciGo** se proyecta como una solución tecnológica integral basada en el modelo de *Prop-Tech* (*Property Technology*), estructurada sobre una arquitectura desacoplada de alto rendimiento en Google Cloud Platform (GCP). El sistema integra un motor de persistencia relacional geoespacial (PostgreSQL 18 y PostGIS 3.6), sincronización transaccional concurrente para erradicar el problema de sobre-reserva (*double-booking*), una pasarela financiera con custodia temporal de fondos (*escrow*) y un estricto protocolo de protección de datos personales alineado con la Ley N° 21.719.

El presente documento organiza deductivamente el ciclo de vida del proyecto de titulación: parte con el diagnóstico cuantitativo del mercado y la delimitación del problema; continúa con el marco teórico y la gobernanza metodológica fundamentada en el estándar PMBOK junto con la Estructura de Desglose del Trabajo (EDT); expone la arquitectura en cuatro capas bajo el estándar TOGAF; y culmina con las matrices de pruebas de calidad, resiliencia operativa y la estrategia de puesta en marcha.

---

## 1.2. Contexto de Negocio y Mercado Inmobiliario en Chile

Para fundamentar la necesidad de la solución informática, resulta indispensable examinar la transformación macroeconómica y operativa que experimenta el mercado inmobiliario no residencial en Chile durante el período post-pandemia. La consolidación de modelos laborales híbridos, la reorganización de las cadenas de suministro urbanas y los cambios de hábitos de consumo han provocado un desacople estructural entre la oferta física construida y los patrones modernos de demanda.

### 1.2.1. Dinámica del Mercado de Oficinas y Vacancia Post-Pandemia

El mercado corporativo y de oficinas presenta los niveles de desocupación más pronunciados de la última década. De acuerdo con los informes sectoriales de CBRE (2024) y Colliers International (2024), la tasa de vacancia promedio del mercado de oficinas en el Gran Santiago se sitúa en un 11,8%, alcanzando cifras críticas de entre el 14,0% y el 18,2% en submercados consolidados como Santiago Centro y sectores tradicionales de Providencia.

Esta acumulación de superficie disponible impacta con mayor gravedad a los activos de Clase B y C, los cuales carecen de la flexibilidad para competir contra edificios corporativos de última generación. Los propietarios de estas superficies enfrentan períodos de vacancia que superan los 18 meses continuos, viéndose obligados a costear gastos comunes ordinarios y contribuciones municipales mientras los inmuebles permanecen improductivos. Al mismo tiempo, pequeñas empresas y equipos de consultoría rehúyen comprometerse con contratos de arrendamiento a largo plazo, buscando alternativas de acceso por demanda que el mercado tradicional es incapaz de articular (Colliers International, 2024).

### 1.2.2. Mercado de Bodegaje Industrial y Centros Logísticos de Última Milla

El sector logístico y de almacenamiento metropolitano experimenta un reajuste tras la expansión acelerada originada por el auge del comercio electrónico entre 2020 y 2022. Hacia el cierre del año 2024, la tasa de vacancia en el segmento de bodegas industriales *flex* y centros de almacenamiento modular alcanza un 14,5% en la Región Metropolitana, sumando una superficie disponible superior a los 219.000 metros cuadrados distribuidos principalmente en las zonas poniente y norte de Santiago (Colliers International, 2024).

Pese a esta sobreoferta global en grandes superficies fabriles, las micro y pequeñas empresas de *e-commerce*, comerciantes independientes y emprendedores urbanos experimentan severas restricciones para arrendar módulos de almacenamiento de pequeña escala (5 a 50 metros cuadrados) por períodos transitorios (CyberDay, temporadas comerciales o contingencias de inventario). Las empresas inmobiliarias de bodegaje masivo imponen requisitos operativos desproporcionados para operaciones menores, mientras que las soluciones existentes de arriendo temporal operan con tarifas intermediadas opacas y esquemas cerrados de mudanza que no permiten la gestión directa entre privados.

### 1.2.3. Dinámica de Locales Comerciales y Espacios de Estacionamiento

El impacto de la digitalización del comercio y la redistribución de los flujos peatonales urbanos se refleja nítidamente en los locales comerciales y las playas de estacionamiento:

1. **Locales Comerciales Urbanos:** Los reportes de la Cámara Nacional de Comercio, Servicios y Turismo de Chile [CNC] (2024) evidencian que los locales ubicados en galerías comerciales céntricas y ejes secundarios de la capital mantienen tasas de desocupación que fluctúan entre el 15,2% y el 20,4%. La rigidez de los arriendos anuales impide a comerciantes de temporada, tiendas efímeras (*pop-up stores*) y creadores artísticos utilizar estos locales por días o semanas para exhibición directa.
2. **Estacionamientos Comerciales y Corporativos:** El modelo de trabajo híbrido genera una subutilización de la infraestructura de estacionamientos subterráneos y comerciales en polos corporativos como El Golf, Nueva Las Condes y Ciudad Empresarial. Diversos relevamientos urbanos indican una tasa de desocupación diurna del 25% al 35% durante los días lunes y viernes (Automóvil Club de Chile, 2023). Estos espacios representan infraestructura física de alta plusvalía que permanece ociosa en horarios clave debido a la inexistencia de plataformas de reserva fraccionada en tiempo real.

---

## 1.3. Relevancia y Pertinencia del Proyecto para la Ingeniería TI

La problemática expuesta no radica en una escasez de infraestructura física, sino en una **falla de intermediación tecnológica y asimetría de información**. Los canales tradicionales (clasificados estáticos, publicaciones de redes sociales y corredores analógicos) carecen de mecanismos para modelar la disponibilidad temporal en tiempo real, autenticar fehacientemente la identidad jurídica de las partes, garantizar la seguridad del pago y mitigar el riesgo de incumplimiento o deterioro del activo.

La pertinencia del proyecto dentro del ámbito de la Ingeniería en Tecnologías de Información y Ciberseguridad se fundamenta en los siguientes pilares técnicos:

1. **Gestión Concurrente de Disponibilidad Espaciotemporal:** El arriendo por horas y días exige modelar la disponibilidad de un espacio en múltiples dimensiones (ubicación geográfica, intervalo temporal y restricciones de uso). Esto demanda la implementación de estructuras de datos especializadas y bloqueos transaccionales a nivel de motor de base de datos (PostgreSQL/PostGIS) para garantizar la atomicidad en operaciones de concurrencia elevada.
2. **Arquitectura Segura de Pagos con Retención en Custodia (*Escrow*):** Para neutralizar la desconfianza mutua, el sistema debe actuar como un intermediario técnico imparcial. Mediante la integración segura con pasarelas de pago y bóvedas digitales, la solución custodia los montos de arrendamiento y retiene las garantías operativas, liberándolos únicamente tras la verificación fotográfica del estado del inmueble en los eventos de ingreso (*check-in*) y salida (*check-out*).
3. **Ciberseguridad y Gobernanza de Datos (Ley N° 21.719):** Al procesar documentos de identidad civil (KYC), antecedentes societarios y giros tributarios (KYB), la solución diseña su ciclo de vida conforme al principio de *Privacidad desde el Diseño y por Defecto*, implementando almacenamiento cifrado en reposo (AES-256), comunicaciones TLS 1.3, segregación de privilegios de red y protocolos de supresión segura ante el ejercicio de derechos ARCO.

La conjunción de estos dominios demuestra que la construcción de la plataforma **espaciGo** constituye una respuesta rigurosa de ingeniería aplicada para transformar un mercado históricamente ineficiente en un ecosistema digital dinámico, seguro y verificable.
