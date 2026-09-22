# FORMULACIÓN DEL PROYECTO DE TÍTULO: EspaciGo

**Institución:** Inacap - Informática y Telecomunicaciones
**Asignatura:** Proyecto de Título - TIH184
**Sección:** D-IEI-N8-P1-C2/D
**Académico guía:** Teresa Jesús Tapia Soto
**Integrantes del equipo:** Hernán Espinoza, Anita Marchant, Erick Silva
**Fecha de entrega:** 15 de septiembre del 2026

---

## Introducción

El mercado inmobiliario en Chile enfrenta un desafío creciente de vacancia, especialmente en la subutilización de espacios comerciales, oficinas y quinchos (según estudios, bordeando el 10% en Santiago post-pandemia). A pesar de la alta demanda de emprendedores y pymes por espacios de uso esporádico o flexible, el modelo de arriendo tradicional (As-Is) impone severas barreras de entrada: contratos rígidos, burocracia notarial presencial, garantías excesivas y un alto riesgo de morosidad y fraude tanto para el dueño del inmueble como para el arrendatario.

Para resolver esta fricción, el presente informe detalla la formulación del proyecto de título EspaciGo, una plataforma tecnológica (SaaS Prop-Tech) que actúa como un Marketplace centralizado para la publicación, reserva y gestión de espacios flexibles.

A lo largo del documento (Evaluación Sumativa 1), se abordará la problemática desde la perspectiva de la Ingeniería de Software, definiendo rigurosamente los requerimientos del sistema a través de Historias de Usuario y Casos de Uso predictivos. Posteriormente, se fundamentará la solución bajo un marco teórico que respalda el uso de la Ley 21.461 (Ley Devuélveme mi casa) y la Ley 21.719 (Protección de Datos) como ejes centrales del modelo de negocio.

Desde el punto de vista operativo, se detallan los objetivos generales y específicos del proyecto, junto con una metodología híbrida de desarrollo y gestión, que permite abordar la ejecución en un plazo total de 16 semanas. Los requerimientos se documentan en cuatro artefactos complementarios y trazables entre sí: **236 requerimientos funcionales**, **43 requerimientos no funcionales**, **52 casos de uso** organizados en 11 módulos funcionales y **35 historias de usuario** agrupadas en 9 épicas. Finalmente, el informe culmina con el diseño y la justificación de una Arquitectura TI Cloud-Native de componentes modulares (Next.js, Go, PostgreSQL, Docker, GCP) y su alineación directa con la Arquitectura Empresarial de la Startup, evidenciando cómo la integración automatizada de la pasarela de pagos (Mercado Pago) y de la firma electrónica avanzada remota (FirmaVirtual) transforman por completo la cadena de valor del rubro inmobiliario chileno.

---

## Identificación del Problema

### Actualización y justificación del problema

**Descripción de la organización. Antecedentes de la Organización.**
El Proyecto se formula bajo la modalidad de Emprendimiento (Startup de Base Tecnológica). La iniciativa nace como un servicio digital SaaS y Marketplace para el mercado chileno, orientado a conectar la oferta de espacio físico subutilizado con la demanda de micro almacenamiento, oficinas temporales y espacios multipropósito a corto plazo.

**Diagnóstico de la situación actual.**
Para comprender la necesidad de esta solución informática, es indispensable analizar el estado actual del Mercado Inmobiliario de Inmuebles Comerciales, Corporativos e Industriales en Chile. En los últimos años, impulsado por la consolidación del trabajo remoto e híbrido post-pandemia y el ajuste económico nacional, el país ha experimentado un fenómeno crítico de desocupación física y vacancia inmobiliaria.

Según informes del sector inmobiliario (tales como reportes de la Cámara Chilena de la Construcción, Colliers y JLL), la vacancia de oficinas en Santiago ha registrado niveles históricos en los últimos periodos, superando tasas de dos dígitos en submercados clave como Santiago Centro (con tasas que oscilan entre el 12% y el 14%) y manteniendo volúmenes importantes de superficie desocupada en sectores como Providencia y Las Condes. A este escenario se suma la fluctuación en el mercado de bodegaje y galpones industriales, donde la sobreoferta de metros cuadrados construidos y la moderación del comercio masivo han incrementado la disponibilidad de bodegas vacías (alcanzando tasas de vacancia de entre el 6% y el 7% en la Región Metropolitana).

Este fenómeno de desocupación masiva genera un doble impacto económico y operativo en el mercado chileno:
*   **Impacto en los Arrendadores e Inversionistas:** Se enfrentan a activos "botados" que no generan ingresos pero continúan devengando altos costos fijos, tales como gastos comunes, contribuciones, seguros y mantenimiento. La rigidez de los contratos tradicionales a largo plazo (de 1 a 3 años) frena la reconversión de estos espacios, dejando metros cuadrados completamente ineficientes.
*   **Impacto en Pymes, Emprendedores y Creativos:** Mientras miles de metros cuadrados permanecen vacíos, las micro y pequeñas empresas de e-commerce, los realizadores audiovisuales, profesores de talleres y organizadores de eventos se ven marginados. Esto ocurre porque el mercado inmobiliario tradicional les exige garantías abusivas, avales y contratos de larga duración cuando solo necesitan espacio por un par de días, semanas o durante campañas de alta demanda (como CyberDay o Navidad).

Es dentro de este mercado de desocupación inmobiliaria donde se evidencia la brecha tecnológica. Al revisar la oferta de plataformas actuales en Chile, la respuesta al problema es deficiente:
*   **Clasificados Tradicionales (Mercado Libre, Yapo, Chilepropiedades):** Operan únicamente como vitrinas estáticas de anuncios. No cuentan con agendamiento en tiempo real, están diseñados para arriendos fijos mensuales o anuales y no ofrecen garantías integradas ni cobros automatizados por uso temporal o por hora.
*   **Corretaje Industrial y Almacenamiento Especializado (Todogalpon, Mudango):** Todogalpon actúa como un corredor de propiedades clásico enfocado en ventas o arriendos industriales a largo plazo, mientras que Mudango se enfoca en un servicio de bodegaje cerrado con logística de mudanza, sin permitir el arriendo directo y flexible "Peer-to-Peer" entre particulares o empresas.

En consecuencia, existe un vacío operativo en el mercado nacional: no existe una plataforma que democratice y dinamice los metros cuadrados improductivos, permitiendo a los dueños rentabilizarlos bajo una modalidad de flujo rotativo on-demand, ni a los arrendatarios reservar infraestructura flexible con disponibilidad inmediata.

**Descripción del problema.**
El problema principal radica en la ineficiencia operativa y financiera provocada por la improductividad de metros cuadrados vacíos en el sector inmobiliario urbano y comercial. Por un lado, los dueños asumen altos costos fijos (gastos comunes, contribuciones, mantenimiento) sin generar ingresos frente a una sobreoferta de ciertos tipos de inmuebles. Por otro lado, pequeñas empresas, e-commerce y profesionales independientes se ven marginados por la rigidez contractual y altos costos de garantía del mercado formal (contratos fijos de 12 a 24 meses), cuando solo requieren utilizar un espacio durante un período acotado (horas, días o semanas).

**Justificación del problema.**

*Relevancia del problema.*
La relevancia de este problema es de alto impacto económico y está respaldada por el comportamiento reciente del mercado de arriendos en Chile. Según informes de consultoras especializadas (como CBRE, Colliers y GPS Property), si bien existe una recuperación general, hay segmentos que mantienen una vacancia crítica y estancada:
*   **Oficinas Clase C y Antiguas:** Presentan una tasa de desocupación estimada entre el 14% y 18%, con incapacidad de competir frente a ofertas más modernas, dejando miles de metros cuadrados sin rentabilizar en sectores céntricos (INE, 2026; CBRE, 2026).
*   **Bodegas Flex y Modulares:** Exhiben una sobreoferta acentuada con un 14,5% de vacancia, sumando más de 219.000 m² disponibles solo en la Región Metropolitana (Colliers, 2026).
*   **Locales en Galerías y Ejes Secundarios:** Mantienen tasas de desocupación superiores al 15% - 20% debido a cambios en los flujos peatonales.

Esta acumulación masiva de espacio disponible representa pérdidas millonarias para los arrendadores. Al mismo tiempo, la demanda por espacios altamente flexibles y de "última milla" por parte del e-commerce ha aumentado, lo que demuestra un descalce entre la oferta rígida tradicional y las nuevas necesidades dinámicas del mercado.

*Complejidad del problema.*
La resolución de esta problemática mediante una plataforma TI requiere abordar múltiples dimensiones técnicas, operativas y legales interconectadas:
1.  **Complejidad Legal y Normativa:** El arriendo, aunque sea temporal, debe proveer seguridad jurídica para facilitar eventuales desalojos. Esto exige el cumplimiento estricto de la Ley 21.461 ("Devuélveme mi Casa"), lo que obliga al sistema a generar contratos dinámicos que se integren vía API con un proveedor externo de firma electrónica avanzada remota. Además, el manejo de documentos de identidad debe cumplir con los altos estándares de privacidad y protección de datos personales de la Ley 21.719. Cabe precisar que estas funcionalidades se orientan a **apoyar** el cumplimiento de los requisitos legales aplicables: el sistema incorpora los mecanismos tecnológicos de generación, firma y resguardo documental, mientras que la validez y los efectos jurídicos de cada contrato se rigen por la normativa vigente y la voluntad de las partes.
2.  **Complejidad Financiera y de Confianza:** Existe el riesgo de daños al inmueble o no pago. El sistema debe implementar transacciones ACID (atomicidad, consistencia, aislamiento, durabilidad) y un modelo Escrow (bóveda de retención de fondos) mediante integraciones complejas (como Mercado Pago Split Payments y bloqueos de cupo en tarjetas), garantizando que los fondos solo se liberen si el check-in/out fotográfico no presenta disputas.
3.  **Sincronización Transaccional Concurrente:** La gestión de múltiples calendarios por hora y día requiere de un backend robusto capaz de manejar alta concurrencia (Goroutines) y evitar las sobre-reservas (Double-Booking), junto con una inyección asíncrona de logs hacia data warehouses (BigQuery) para auditoría.

---

## Levantamiento de Requerimientos

### Determinación de los instrumentos a utilizar
Con el propósito de documentar con precisión las necesidades del mercado, los clientes (arrendadores y arrendatarios) y los requisitos legales para el desarrollo de la solución informática EspaciGo, se determinó la aplicación de métodos mixtos. Los instrumentos de levantamiento de información utilizados fueron:
1.  **Encuestas Digitales (Cuantitativo):** Para recopilar datos sobre patrones de uso de bodegaje temporario y disposición a pago flexible por horas/días.
2.  **Entrevistas En Profundidad (Cualitativo):** Para comprender las barreras legales (Ley 21.461) y de seguridad que preocupan a los dueños de espacios, administradores y corredores de propiedades.
3.  **Estudio de Mercado y Benchmark Competitivo:** Para identificar brechas de diseño funcional frente a competidores tradicionales (Mercado Libre, Mudango).
4.  **Grupos de Discusión Técnicos:** Para definir la arquitectura Cloud-Native, el flujo de retención (Escrow) y la trazabilidad de datos (Ley 21.719) junto al equipo de desarrollo.

### Documentar los Requerimientos
Para reflejar la envergadura de una plataforma SaaS Cloud-Native y cumplir con los más altos estándares de Ingeniería de Software, se ha seleccionado una metodología híbrida. Esta combina un modelo de procesos iterativo-incremental para la construcción técnica, junto con las mejores prácticas del PMBOK para la gestión del proyecto.
Se justifica el uso de este enfoque predictivo e iterativo debido a que los requerimientos de la plataforma (financieros, legales y de seguridad) son estables y predecibles, no existiendo un cliente final que cambie los requerimientos estructurales constantemente. La documentación se estructura separando los requerimientos funcionales (estándar IEEE 830) de las historias de usuario y casos de uso, los cuales se desarrollarán en las siguientes iteraciones del proyecto.

La documentación de requisitos se organiza en cuatro catálogos complementarios y trazables entre sí. Por su extensión, el cuerpo de este informe presenta el resumen, los extractos más representativos y las referencias cruzadas, mientras que el detalle completo se desarrolla en los anexos:

*Tabla. Resumen de los artefactos de requisitos del proyecto.*

| Artefacto | Cantidad | Identificadores | Organización | Ubicación del detalle completo |
| :--- | :--- | :--- | :--- | :--- |
| Requerimientos funcionales | **236** | `RQF-001` a `RQF-236` | 11 módulos funcionales (M01–M11) | Anexo de Requerimientos Funcionales (extracto en la Tabla 1) |
| Requerimientos no funcionales | **43** | `RNF-001` a `RNF-043` | 11 categorías ISO 25010, mínimo 3 por categoría | Anexo de Requerimientos No Funcionales (extracto en la Tabla 2) |
| Casos de uso | **52** | `CU-01` a `CU-52` | 11 módulos funcionales, un diagrama UML por módulo | Anexo de Casos de Uso (extracto en la sección de Especificación de Casos de Uso) |
| Historias de usuario | **35** | `HU01` a `HU35` | 9 épicas (E1–E9) | Anexo de Historias de Usuario (extracto en la Tabla 3) |

> **Nota de nomenclatura:** el catálogo de requerimientos funcionales utiliza el identificador `RQF-###` de forma unificada en todos los documentos del proyecto; en el texto corrido se emplea la abreviatura "RF". Los requerimientos no funcionales se identifican como `RNF-###`, los casos de uso como `CU-##` y las historias de usuario como `HU##`.

### Identificación de Actores del Sistema
Se han identificado los siguientes actores que interactuarán directa o indirectamente con el sistema EspaciGo:

**Actores Primarios (Humanos)**
*   **Visitante:** Usuario anónimo, sin cuenta registrada.
*   **Usuario Registrado:** Posee cuenta con correo verificado pero aún sin validación de identidad.
*   **Arrendador:** Usuario con identidad verificada (KYC/KYB) que publica y gestiona espacios comerciales.
*   **Arrendatario:** Usuario con identidad verificada (KYC/KYB) que busca, reserva y paga por espacios comerciales.
*   **Administrador:** Operador interno de EspaciGo con acceso al panel de control y auditoría.

**Actores Secundarios (Sistemas y Servicios Externos)**
*   **Registro Civil:** API para validar la vigencia de la cédula de identidad.
*   **SII:** API para validar el inicio de actividades de las empresas (KYB) y para el timbrado de la boleta de comisión.
*   **Mercado Pago:** Pasarela de pagos externa con tokenización y retención de fondos (Escrow).
*   **FirmaVirtual:** Proveedor externo de firma electrónica avanzada.

> **Exclusión explícita de actores:** Google BigQuery **no** se modela como actor de casos de uso, porque no inicia ni observa ninguna funcionalidad del sistema: es el repositorio analítico de destino de la auditoría, cuya inmutabilidad se especifica como requerimiento no funcional (RNF-017). La justificación completa de esta exclusión —junto con la generalización de actores, donde Arrendador y Arrendatario heredan de Usuario Registrado y este de Visitante— se documenta en el anexo de Casos de Uso.

### Requerimientos Funcionales (RF)
Los Requerimientos Funcionales definen el comportamiento interno del sistema y cubren todo el ecosistema B2B/B2C. A continuación, se presenta un extracto con los requerimientos principales del flujo core, redactados bajo la norma estricta de un solo verbo atómico por requerimiento y enfocados exclusivamente en el comportamiento observable, delegando los detalles técnicos y de infraestructura hacia la arquitectura. El catálogo completo de los 236 requerimientos funcionales (185 base y 51 complementarios incorporados en las revisiones de completitud, con 10 redacciones corregidas en la auditoría de verbos atómicos sin alterar ningún identificador), con su identificador único, su agrupación en 11 módulos funcionales y los actores asociados, se presenta en el anexo de Requerimientos Funcionales.

*Tabla 1. Requerimientos Funcionales (RQF).*

| ID | Descripción del Requerimiento Funcional |
| :--- | :--- |
| RQF-001 | El sistema debe permitir registrar una cuenta de usuario. |
| RQF-011 | El sistema debe permitir iniciar sesión. |
| RQF-034 | El sistema debe permitir solicitar la eliminación de la cuenta de usuario. |
| RQF-044 | El sistema debe validar la vigencia de la cédula ante el organismo correspondiente. |
| RQF-051 | El sistema debe consultar el inicio de actividades de la empresa. |
| RQF-082 | El sistema debe cambiar el estado a "Activa" al confirmar la creación. |
| RQF-094 | El sistema debe permitir buscar publicaciones ingresando texto en una barra de búsqueda. |
| RQF-101 | El sistema debe excluir de los resultados las publicaciones sin disponibilidad en las fechas consultadas. |
| RQF-107 | El sistema debe mostrar el desglose de cobro (Estadía + Comisión + Garantía). |
| RQF-111 | El sistema debe validar la disponibilidad del espacio para el intervalo solicitado. |
| RQF-113 | El sistema debe registrar la reserva en estado "Pendiente de Pago" al confirmar disponibilidad. |
| RQF-114 | El sistema debe permitir al usuario seleccionar un método de pago mediante la pasarela integrada. |
| RQF-117 | El sistema debe mantener retenidos los fondos de la reserva hasta que se cumplan las condiciones de liberación. |
| RQF-118 | El sistema debe ejecutar una pre-autorización por el monto de la garantía. |
| RQF-124 | El sistema debe permitir al arrendador aprobar una solicitud de reserva. |
| RQF-132 | El sistema debe generar un documento de contrato incorporando los datos legales de las partes y el inmueble. |
| RQF-137 | El sistema debe almacenar el contrato final asociado a la reserva tras la confirmación de todas las firmas. |
| RQF-148 | El sistema debe cambiar el estado de la reserva a "En_Curso" tras procesar el Check-in. |
| RQF-162 | El sistema debe bloquear la liberación de fondos de una reserva al detectar un reclamo registrado. |
| RQF-168 | El sistema debe permitir al administrador registrar un fallo a favor del arrendatario. |

### Requerimientos No Funcionales (RNF)
Los requerimientos no funcionales establecen los límites físicos, de calidad y legislativos del sistema. A continuación se presenta un extracto con los 8 requerimientos más críticos del proyecto, clasificados según el estándar ISO 25010. El catálogo completo de los **43 requerimientos no funcionales** se presenta en el anexo de Requerimientos No Funcionales: están clasificados en 11 categorías (Rendimiento, Usabilidad, Fiabilidad, Seguridad, Flexibilidad, Mantenibilidad, Compatibilidad, Portabilidad, Implementación, Almacenamiento y Requerimientos Externos) con un mínimo de 3 requerimientos por categoría, redactados en el formato estándar "El sistema debe [condición de calidad]", y cada uno declara su trazabilidad hacia los requerimientos funcionales y los módulos que condiciona. Ninguno de ellos describe comportamiento funcional: las acciones observables por los actores se especifican exclusivamente en el catálogo de requerimientos funcionales.

*Tabla 2. Requerimientos No Funcionales (RNF).*

| ID | Categoría / Subcategoría | Descripción del Requerimiento No Funcional |
| :--- | :--- | :--- |
| RNF-001 | Rendimiento / Comportamiento temporal | El sistema debe retornar los resultados de búsqueda en un tiempo máximo de 2 segundos bajo una carga concurrente de 200 usuarios, medido desde que el usuario confirma los parámetros. |
| RNF-005 | Usabilidad / Operabilidad | El sistema debe permitir al usuario completar el proceso de reserva en un máximo de 7 interacciones (clics) y sin superar los 3 niveles de profundidad de navegación. |
| RNF-009 | Fiabilidad / Disponibilidad | El sistema debe garantizar una disponibilidad mínima del 99,9% mensual para las funciones críticas de autenticación, búsqueda y reservas. |
| RNF-011 | Fiabilidad / Tolerancia a fallos | El sistema debe garantizar la atomicidad transaccional ejecutando un rollback automático (revirtiendo el estado de la base de datos) ante cualquier fallo en el flujo de pagos. |
| RNF-013 | Seguridad / Confidencialidad | El sistema debe almacenar las contraseñas exclusivamente en formato de hash irreversible utilizando bcrypt con un factor de costo mínimo de 12 rounds, prohibiendo su almacenamiento en texto plano. |
| RNF-017 | Seguridad / Integridad | El sistema debe almacenar los logs de auditoría transaccional en un repositorio inmutable, bloqueando a nivel de infraestructura cualquier intento de modificación o eliminación de los registros. |
| RNF-019 | Flexibilidad / Escalabilidad | El sistema debe soportar un escalamiento horizontal automático para absorber incrementos del 200% de carga, desplegando nuevas instancias en un tiempo máximo de 10 minutos. |
| RNF-025 | Requerimientos Externos / Estándares (PCI-DSS) | El sistema debe procesar los pagos exclusivamente mediante tokenización, sin almacenar en la base de datos los datos PAN o CVV, para dar estricto cumplimiento al estándar PCI-DSS. |

---

## Especificación de Casos de Uso y Referencias Cruzadas (Predictivo)

Los diagramas de casos de uso modelan la interacción funcional entre los actores del sistema (roles humanos y sistemas o servicios externos) y los límites de la plataforma EspaciGo. El sistema se organiza en **11 módulos funcionales**, cada uno con su propio diagrama de casos de uso, y cada caso de uso posee un **identificador único correlativo (CU-01 a CU-52)** que lo referencia con su ficha descriptiva.

A continuación se presentan los casos de uso más críticos y representativos de cada módulo. La totalidad de los diagramas —**12 diagramas PlantUML en notación UML 2.x**: 11 correspondientes a los módulos funcionales y 1 correspondiente al modelo de actores y su generalización— junto con las fichas completas de casos de uso —actor, descripción, precondiciones, flujo principal, flujos alternativos, postcondiciones y referencias cruzadas hacia RF, RNF y HU— se encuentran en el anexo de Casos de Uso, con trazabilidad directa y verificada sobre los 236 requerimientos funcionales.

### Módulo M01: Autenticación y Gestión de Cuenta
*   **CU-01: Registrar Cuenta** (Crítico para la captura y alta segura de usuarios).
*   **CU-03: Iniciar Sesión** (Base de la autenticación y del control de acceso por rol).
*   **CU-50: Cambiar Contraseña** (Gestión de credenciales con sesión iniciada).
*(Ref: Imagen 1. Casos de uso. Autenticación y Gestión de Cuenta)*

### Módulo M02: Perfil y Privacidad del Usuario
*   **CU-07: Gestionar Perfil de Usuario** (Mantiene la vigencia de los datos personales).
*   **CU-09: Solicitar Eliminación de Cuenta** (Ejercicio del derecho de supresión de datos, Ley 21.719).
*(Ref: Imagen 2. Casos de uso. Perfil y Privacidad del Usuario)*

### Módulo M03: Verificación de Identidad (KYC/KYB)
*   **CU-11: Validar Identidad de Persona Natural (KYC)** (Cumplimiento normativo con la API del Registro Civil).
*   **CU-12: Validar Identidad de Empresa (KYB)** (Habilita la operación de empresas verificadas ante el SII).
*(Ref: Imagen 3. Casos de uso. Verificación de Identidad (KYC/KYB))*

### Módulo M04: Gestión de Publicaciones
*   **CU-15: Registrar Publicación de Espacio** (El núcleo de la oferta de valor del Marketplace).
*   **CU-17: Configurar Calendario de Disponibilidad** (Esencial para la gestión de disponibilidad temporal).
*(Ref: Imagen 4. Casos de uso. Gestión de Publicaciones)*

### Módulo M05: Búsqueda y Cotización de Espacios
*   **CU-19: Buscar Espacios** (Mapa y filtros; clave para la experiencia del arrendatario).
*   **CU-21: Cotizar Estadía** (Transparencia del desglose: estadía, comisión y garantía).
*(Ref: Imagen 5. Casos de uso. Búsqueda y Cotización de Espacios)*

### Módulo M06: Reservas y Pagos (Escrow)
*   **CU-22: Solicitar Reserva** (Evita colisiones de fechas mediante la validación de disponibilidad en tiempo real).
*   **CU-24: Pagar Reserva y Retener en Escrow** (El pilar financiero de confianza del Marketplace).
*   **CU-47: Consultar Historial de Reservas** (Seguimiento del estado de cada reserva por ambas partes).
*   **CU-51: Cancelar Reserva** (Cancelación del arrendatario conforme a la política del espacio).
*(Ref: Imagen 6. Casos de uso. Reservas y Pagos (Escrow))*

### Módulo M07: Contratos y Firma Electrónica
*   **CU-29: Generar y Enviar Contrato a Firma** (Soporta los requisitos de la Ley 21.461 "Devuélveme mi casa").
*   **CU-30: Firmar Contrato Electrónicamente** (Resguarda el contrato firmado y habilita el check-in).
*(Ref: Imagen 7. Casos de uso. Contratos y Firma Electrónica)*

### Módulo M08: Check-in y Check-out
*   **CU-33: Realizar Check-in con Evidencia** (Documenta el estado de entrega del espacio).
*   **CU-48: Confirmar Recepción del Espacio** (El arrendador deja evidencia de la devolución del espacio).
*   **CU-34: Realizar Check-out** (Cierra la estadía e inicia el período de reclamos).
*(Ref: Imagen 8. Casos de uso. Check-in y Check-out)*

### Módulo M09: Comunicación y Reputación
*   **CU-35: Registrar Reseña y Calificación** (Construye la reputación de la oferta).
*   **CU-49: Reportar Reseña** (Habilita la moderación de reseñas que incumplen las reglas).
*   **CU-37: Enviar Mensajes en el Chat de la Reserva** (Comunicación trazable entre las partes).
*(Ref: Imagen 9. Casos de uso. Comunicación y Reputación)*

### Módulo M10: Disputas, Payout y Facturación
*   **CU-39: Registrar Reclamo por Daños** (Mecanismo de protección ante conflictos post-servicio).
*   **CU-42: Ejecutar Payout y Emitir Boleta de Comisión** (Liquidación automática y cierre financiero).
*(Ref: Imagen 10. Casos de uso. Disputas, Payout y Facturación)*

### Módulo M11: Administración y Auditoría
*   **CU-41: Resolver Disputa en Backoffice** (Arbitraje administrativo de la garantía).
*   **CU-46: Consultar y Exportar Historial de Auditoría** (Herramienta administrativa de trazabilidad forense).
*   **CU-52: Consultar Publicaciones de la Plataforma** (Supervisión del catálogo publicado).
*(Ref: Imagen 11. Casos de uso. Administración y Auditoría)*

---

## Historias de Usuario (Metodología Adaptativa)
Para la planificación iterativa e incremental (iteraciones e incrementos del ciclo de vida híbrido), se desglosó el proyecto en **35 Historias de Usuario (HU01–HU35)** agrupadas en **9 épicas** (Identidad y Acceso; Gestión de Espacios; Búsqueda y Selección; Reservas, Pagos y Contratos; Disponibilidad y Calendario; Reputación y Comunicación; Administración y Moderación; Soporte y Notificaciones; Operación del Arriendo), redactadas en formato "Como [rol], quiero [acción], para [beneficio]" y completadas con sus respectivos criterios de aceptación para la fase de testing.

Cada historia declara su épica, su prioridad, los requerimientos funcionales que la implementan y los casos de uso donde está especificada, de modo que existe trazabilidad directa entre HU, RF y CU. Los criterios que describen funcionalidad fuera del alcance declarado de esta entrega se identifican explícitamente en su bloque "Fuera del alcance de la ES1". A continuación se presenta un extracto con las 8 historias más críticas del flujo principal de negocio, en formato "Como / Quiero / Para" y con un resumen de sus criterios de aceptación. El conjunto completo de las **35 historias** —cada una con sus criterios de aceptación detallados, su tabla de trazabilidad HU ↔ RF ↔ CU, la cobertura de los 11 módulos funcionales y el detalle de las correcciones aplicadas— se presenta en el anexo de Historias de Usuario.

*Tabla 3. Historias de Usuario (extracto de las 8 historias más críticas).*

| Código | Épica | Como (rol) | Quiero (acción) | Para (beneficio) | Criterios de aceptación (resumen) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| HU01 | E1 Identidad y Acceso | Visitante de la plataforma | Registrarme ingresando mis datos personales y señalando mi intención de uso (ofrecer espacios o arrendar espacios). | Acceder a las funcionalidades del sistema con mi propia cuenta. | La cuenta se crea en estado "No Verificado"; el correo debe ser válido y no estar registrado; la contraseña exige mínimo 8 caracteres, una mayúscula, un número y un carácter especial; los términos y condiciones se aceptan registrando fecha y versión; el acceso se habilita solo con la cuenta verificada. |
| HU04 | E1 Identidad y Acceso | Usuario Registrado | Acreditar mi identidad como persona natural (KYC) o la de mi empresa (KYB). | Que mi perfil quede verificado y pueda publicar y reservar espacios de forma segura. | Carga de la cédula de identidad por anverso y reverso (máximo 10 MB por archivo); el perfil pasa a "Pendiente de Verificación"; se valida la vigencia de la cédula ante el Registro Civil; el KYB valida el inicio de actividades ante el SII; el rechazo exige motivo y habilita un nuevo intento de validación. |
| HU05 | E2 Gestión de Espacios | Arrendador con identidad verificada | Registrar y publicar los detalles de mi espacio físico (quinchos, bodegas, estacionamientos, parcelas u otros). | Que los interesados puedan visualizarlo, conocer sus características y solicitar su arriendo de forma digital. | Publicación restringida a identidad verificada; título de máximo 70 caracteres; descripción de al menos 100 caracteres; precio base superior a $5.000 CLP; hasta 10 fotografías de 5 MB; la publicación se guarda como "Borrador" y luego se activa; se genera el calendario de disponibilidad asociado. |
| HU10 | E3 Búsqueda y Selección | Arrendatario | Buscar espacios escribiendo términos en una barra de texto (nombre, comuna o tipo de espacio). | Obtener un listado preliminar de anuncios coincidentes. | Búsqueda disponible sin sesión iniciada; los resultados se actualizan sin recargar la página completa; se excluyen las publicaciones sin disponibilidad en el rango consultado; si no hay coincidencias se muestra una vista vacía con el término buscado. |
| HU15 | E4 Reservas, Pagos y Contratos | Arrendatario | Seleccionar un rango de fechas y horarios disponibles en el calendario del espacio. | Que el sistema verifique la disponibilidad y me permita avanzar con la solicitud de arriendo. | Calendario según modalidad tarifaria (hora, día o mes) con bloques ocupados y disponibles; validación de fechas futuras y de término posterior al inicio; mensaje cuando el rango contiene bloques no disponibles; revalidación de la disponibilidad contra la base de datos al confirmar; resumen del tiempo seleccionado antes de reservar. |
| HU17 | E4 Reservas, Pagos y Contratos | Arrendatario | Pagar la reserva a través de la pasarela de pago integrada (Mercado Pago). | Que la transacción se procese con tokenización y estándares de seguridad del sector financiero. | La reserva queda en "Pendiente de Pago" y se exige identidad verificada antes de pagar; no se capturan ni almacenan datos de tarjeta; los fondos permanecen retenidos en custodia (Escrow) hasta cumplir las condiciones de liberación; se ejecuta la pre-autorización de la garantía; si el pago no se completa en 15 minutos, la reserva se cancela y las fechas se liberan. |
| HU18 | E4 Reservas, Pagos y Contratos | Sistema (automatización de la plataforma) | Procesar la respuesta exitosa de la pasarela de pago y bloquear las fechas reservadas. | Que la reserva quede formalmente confirmada sin riesgo de sobreventa y que las partes sean notificadas. | Cambio automático de la reserva a "Pagada"; bloqueo de los bloques de fecha y hora sin superposiciones con otras reservas o bloqueos; notificación al arrendador indicando que los fondos están retenidos en custodia (no acreditados); la reserva queda visible en el historial con las acciones habilitadas según su estado. |
| HU28 | E7 Administración y Moderación | Administrador | Mediar en las disputas entre arrendador y arrendatario. | Resolver el caso determinando la retención o la devolución de la garantía. | El expediente muestra los antecedentes de la reserva, las fotografías de check-in y check-out, la confirmación de recepción y los descargos; el fallo puede favorecer a cualquiera de las partes y exige el monto cuando implica retención; se ejecuta el cobro de la pre-autorización de garantía y se libera el saldo; ambas partes son notificadas; no se permite reabrir una reserva ya cerrada. |

---

## Matriz de Trazabilidad

La trazabilidad del proyecto se documenta de forma integral: cada **historia de usuario** (necesidad del usuario) se implementa mediante **requerimientos funcionales** (comportamiento observable del sistema), se especifica en **casos de uso** (interacción con los actores), queda condicionada por **requerimientos no funcionales** (condiciones de calidad) y se materializa en un **componente técnico** de la arquitectura.

En primer lugar, la matriz relaciona los requisitos del negocio con su verificación técnica:

*Tabla. Del requisito del negocio a la validación técnica.*

| Requisito del negocio | Caso de uso | Componente técnico | Validación esperada |
| :--- | :--- | :--- | :--- |
| El espacio no puede reservarse dos veces | Reserva de espacio (CU-22, CU-24) | Backend Go + PostgreSQL | Validación de solapamiento y transacción ACID |
| El pago debe confirmarse antes | Confirmación (CU-24, CU-26) | Backend Go + Mercado Pago | Estado de pago y retención de fondos coherentes |
| El contrato debe estar firmado antes del uso | Aceptación (CU-29, CU-30) | Servicio de contratos + FirmaVirtual | Documento firmado asociado a la operación |
| Auditar las acciones críticas | Disputa / revisión (CU-41, CU-46) | BigQuery + logs inmutables | Evidencia histórica consultable y exportable |

En segundo lugar, la matriz de trazabilidad completa del proyecto, construida desde los catálogos de los anexos:

*Tabla. Matriz de trazabilidad integral (HU → RF → RNF → CU → Módulo → Componente).*

| HU | Épica | Historia de usuario | RF | RNF | CU | Módulo | Componente |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| HU01 | E1 Identidad y Acceso | Registro de nuevo usuario | RQF-001, RQF-010, RQF-186, RQF-187, RQF-213 | RNF-013, RNF-015, RNF-016 | CU-01, CU-02 | M01 | Go/Auth + PostgreSQL |
| HU02 | E1 Identidad y Acceso | Inicio de sesión en la plataforma | RQF-010, RQF-018, RQF-023 | RNF-013, RNF-015, RNF-016 | CU-03, CU-04, CU-06 | M01 | Go/Auth + PostgreSQL |
| HU03 | E1 Identidad y Acceso | Cambiar y recuperar la contraseña | RQF-019, RQF-022, RQF-214, RQF-218 | RNF-013, RNF-015, RNF-016 | CU-05, CU-50 | M01 | Go/Auth + PostgreSQL |
| HU04 | E1 Identidad y Acceso | Verificación de identidad (KYC / KYB) | RQF-038, RQF-059, RQF-192, RQF-194, RQF-219, RQF-220 | — | CU-10, CU-14 | M03 | Go/APIs externas (Registro Civil, SII) |
| HU05 | E2 Gestión de Espacios | Publicar un espacio físico | RQF-060, RQF-085 | RNF-019, RNF-031 | CU-15, CU-17 | M04 | Next.js + Go + PostGIS |
| HU06 | E2 Gestión de Espacios | Editar y actualizar información de un espacio | RQF-086, RQF-087, RQF-195, RQF-198, RQF-221 | RNF-020 | CU-18 | M04 | Next.js + Go + PostGIS |
| HU07 | E2 Gestión de Espacios | Establecer reglas de uso y políticas del espacio | RQF-070, RQF-196, RQF-222, RQF-224 | RNF-019, RNF-020, RNF-031 | CU-15, CU-18, CU-20 | M04 | Next.js + Go + PostGIS |
| HU08 | E2 Gestión de Espacios | Pausar o reactivar un espacio | RQF-088, RQF-092 | RNF-020 | CU-18 | M04 | Next.js + Go + PostGIS |
| HU09 | E2 Gestión de Espacios | Describir el equipamiento y las condiciones del espacio | RQF-064, RQF-070, RQF-195, RQF-196 | RNF-019, RNF-020, RNF-031 | CU-15, CU-18, CU-20 | M04 | Next.js + Go + PostGIS |
| HU10 | E3 Búsqueda y Selección | Búsqueda general de espacios | RQF-094, RQF-096, RQF-101 | RNF-001, RNF-030 | CU-19 | M05 | Next.js (SSR) + Go + PostGIS |
| HU11 | E3 Búsqueda y Selección | Filtrado avanzado de espacios | RQF-097, RQF-102 | RNF-001, RNF-030 | CU-19 | M05 | Next.js (SSR) + Go + PostGIS |
| HU12 | E3 Búsqueda y Selección | Visualización de espacios en mapa interactivo | RQF-095, RQF-096, RQF-103 | RNF-001, RNF-030 | CU-19, CU-20 | M05 | Next.js (SSR) + Go + PostGIS |
| HU13 | E3 Búsqueda y Selección | Visualización del detalle de un espacio | RQF-103, RQF-155 | — | CU-20, CU-36 | M05, M09 | Next.js (SSR) + Go + PostGIS; Go + PostgreSQL |
| HU14 | E3 Búsqueda y Selección | Consultar el historial de reservas propias | RQF-199 | — | CU-47 | M06 | Go/Escrow + Mercado Pago |
| HU15 | E4 Reservas, Pagos y Contratos | Selección de bloques de fecha y hora para reserva | RQF-071, RQF-108, RQF-112 | RNF-001, RNF-005, RNF-006, RNF-020, RNF-030 | CU-19, CU-21, CU-22, CU-23 | M04, M06 | Next.js + Go + PostGIS; Go/Escrow + Mercado Pago |
| HU16 | E4 Reservas, Pagos y Contratos | Cálculo automático de tarifas, comisiones y garantía | RQF-104, RQF-107 | RNF-005, RNF-006, RNF-020 | CU-21 | M05 | Next.js (SSR) + Go + PostGIS |
| HU17 | E4 Reservas, Pagos y Contratos | Pago de la reserva mediante pasarela integrada | RQF-113, RQF-122, RQF-201, RQF-227 | RNF-001, RNF-002, RNF-005, RNF-006, RNF-011, RNF-012, RNF-019, RNF-025, RNF-028, RNF-030, RNF-031 | CU-22, CU-24, CU-25 | M06 | Go/Escrow + Mercado Pago |
| HU18 | E4 Reservas, Pagos y Contratos | Confirmación de reserva y bloqueo de calendario | RQF-113, RQF-116, RQF-117, RQF-121, RQF-122 | RNF-002, RNF-005, RNF-006, RNF-011, RNF-012, RNF-019, RNF-025, RNF-028, RNF-031 | CU-24, CU-26, CU-47 | M06 | Go/Escrow + Mercado Pago |
| HU19 | E4 Reservas, Pagos y Contratos | Cancelación de reserva y gestión de devolución | RQF-117, RQF-200, RQF-223, RQF-226, RQF-231 | RNF-002, RNF-011, RNF-012, RNF-020, RNF-027, RNF-028 | CU-42, CU-51 | M04, M06 | Next.js + Go + PostGIS; Go/Escrow + Mercado Pago |
| HU20 | E5 Disponibilidad y Calendario | Gestión del calendario de disponibilidad | RQF-083, RQF-085, RQF-112 | RNF-001, RNF-030 | CU-17, CU-19 | M04, M06 | Next.js + Go + PostGIS; Go/Escrow + Mercado Pago |
| HU21 | E5 Disponibilidad y Calendario | Bloqueo manual de fechas por mantenimiento o uso personal | RQF-084, RQF-085, RQF-112, RQF-225, RQF-226 | — | CU-17 | M04, M06 | Next.js + Go + PostGIS; Go/Escrow + Mercado Pago |
| HU22 | E5 Disponibilidad y Calendario | Consultar la actividad y las reservas del espacio | RQF-199 | — | CU-47 | M06 | Go/Escrow + Mercado Pago |
| HU23 | E5 Disponibilidad y Calendario | Sincronización automática de estados en el calendario | RQF-112, RQF-120, RQF-129, RQF-200 | RNF-001, RNF-002, RNF-005, RNF-006, RNF-011, RNF-012, RNF-028, RNF-030 | CU-17, CU-22, CU-27, CU-28, CU-51 | M06 | Go/Escrow + Mercado Pago |
| HU24 | E5 Disponibilidad y Calendario | Configuración de disponibilidad recurrente | Sin RF (fuera del alcance de la ES1) | — | — | — | — |
| HU25 | E6 Reputación y Comunicación | Sistema de calificaciones y reseñas | RQF-153, RQF-155, RQF-207, RQF-232, RQF-235 | — | CU-35, CU-36, CU-49 | M09 | Go + PostgreSQL |
| HU26 | E7 Administración y Moderación | Panel de control y supervisión del administrador | RQF-178, RQF-180, RQF-183, RQF-185, RQF-212, RQF-236 | RNF-017, RNF-043 | CU-43, CU-45, CU-46, CU-52 | M11 | Backoffice (Next.js) + BigQuery |
| HU27 | E7 Administración y Moderación | Moderación de contenido reportado | RQF-181, RQF-182, RQF-207 | — | CU-44, CU-49 | M09, M11 | Go + PostgreSQL; Backoffice (Next.js) + BigQuery |
| HU28 | E7 Administración y Moderación | Resolución de disputas e incidencias de reservas | RQF-159, RQF-175, RQF-209, RQF-210 | RNF-002, RNF-011, RNF-012, RNF-027, RNF-028, RNF-042 | CU-39, CU-40, CU-41, CU-42 | M10 | Go/Liquidación + Mercado Pago |
| HU29 | E8 Soporte y Notificaciones | Centro de ayuda y soporte | Sin RF (fuera del alcance de la ES1) | — | — | — | — |
| HU30 | E8 Soporte y Notificaciones | Notificaciones y alertas de la plataforma | RQF-047, RQF-121, RQF-122, RQF-139, RQF-149, RQF-164, RQF-194, RQF-201, RQF-210, RQF-218, RQF-231 | RNF-002, RNF-011–016, RNF-019, RNF-025, RNF-028, RNF-031, RNF-042 | CU-02, CU-03, CU-24, CU-30, CU-33, CU-41, CU-50, CU-51 | M01, M03, M06, M07, M08, M10 | Servicio de notificaciones sobre Go + proveedores externos |
| HU31 | E1 Identidad y Acceso | Administrar mi perfil y mi cuenta bancaria | RQF-024, RQF-033, RQF-189, RQF-191 | RNF-014 | CU-07, CU-08 | M02 | Go/API de usuario + Cloud Storage |
| HU32 | E1 Identidad y Acceso | Ejercer el derecho de eliminación de mi cuenta | RQF-034, RQF-037 | RNF-018, RNF-026, RNF-029 | CU-09 | M02 | Go/API de usuario + Cloud Storage |
| HU33 | E4 Reservas, Pagos y Contratos | Generar y firmar el contrato de arriendo | RQF-130, RQF-142, RQF-202 | RNF-003, RNF-014, RNF-023, RNF-024, RNF-042 | CU-29, CU-30, CU-31, CU-32 | M07 | Go + FirmaVirtual |
| HU34 | E6 Reputación y Comunicación | Comunicarme con la contraparte durante la reserva | RQF-156, RQF-158 | — | CU-37, CU-38 | M09 | Go + PostgreSQL |
| HU35 | E9 Operación del Arriendo | Registrar check-in, check-out y confirmar la recepción | RQF-143, RQF-152, RQF-203, RQF-206 | RNF-042 | CU-33, CU-34, CU-48 | M08 | Go + Cloud Storage |

**Lectura de la matriz**
* **HU (35):** necesidades de usuario documentadas. `HU24` y `HU29` no tienen RF asociado porque están declaradas fuera del alcance de la ES1.
* **RF (236):** requerimientos funcionales del catálogo. Cada RF tiene un único caso de uso responsable, por lo que la cobertura es verificable uno a uno.
* **RNF (43):** requerimientos no funcionales que condicionan la historia, sea por sus RF o por los casos de uso que la implementan. Los RNF transversales de arquitectura y construcción (RNF-021, RNF-032 a RNF-040) aplican al sistema completo y por eso no se repiten en cada fila.
* **CU (52):** casos de uso donde la historia queda especificada.
* **Módulo (11):** módulo funcional (M01–M11) que agrupa los RF y los CU de la historia.
* **Componente:** componente técnico de la arquitectura TI que materializa la funcionalidad.

**Cadenas de trazabilidad verificadas**
* **Objetivo general → objetivos específicos → épicas → historias de usuario.**
* **RF → CU:** los 236 requerimientos funcionales están cubiertos por los 52 casos de uso, sin omisiones ni duplicaciones (salvo el caso de uso abstracto `CU-10`, cuya cobertura se reparte entre sus especializaciones `CU-11` y `CU-12`).
* **RNF → RF y RNF → módulos:** declarada en el anexo de Requerimientos No Funcionales.
* **RF → módulo:** declarada en el anexo de Requerimientos Funcionales y en el resumen módulo → casos de uso → requerimientos funcionales del anexo de Casos de Uso.
* **HU → criterios de aceptación:** cada historia declara los criterios que permiten verificar su cumplimiento durante las pruebas.
* **Cobertura de módulos:** los 11 módulos funcionales cuentan con al menos una historia de usuario asociada.

---

## Marco Teórico

El presente capítulo presenta el marco teórico que sustenta la solución tecnológica EspaciGo. A diferencia de una revisión conceptual genérica, este apartado se orienta a justificar cada decisión de diseño, arquitectura y operación del sistema.

### Plataforma digital y modelo SaaS
El modelo SaaS entrega la aplicación como servicio en la nube, accediendo a ella mediante navegador. Esto reduce costos iniciales, permite actualizaciones centralizadas y facilita la disponibilidad global del sistema.

*Tabla 4. Comparación SaaS vs On-Premise.*

| Aspecto | SaaS | On-Premise | Relevancia para EspaciGo |
| :--- | :--- | :--- | :--- |
| Infraestructura | Almacenamiento y servidores en la nube | Hardware propio | Se evita depender de cada cliente o instalación local |
| Mantenimiento | Centralizado por proveedor | De la organización | Reduce carga operativa y acelera evolución del producto |
| Costos iniciales | Menores y escalables | Altos | Facilita validación del modelo de negocio |
| Escalabilidad | Alta y elástica | Limitada por infraestructura fija | Necesaria para picos temporales de demanda |
| Actualizaciones | Centralizadas y continuas | Manuales y dependientes | Importante para pagos, seguridad y contratos |
| Disponibilidad | Gestionada a nivel de servicio | Dependiente local | Es clave para reservas y pagos en tiempo real |
| Acceso | Web y multiusuario | Más restringido | El marketplace requiere acceso constante |

**Decisión de implementación:** EspaciGo se diseña como una solución web basada en la nube, con acceso centralizado y escalado automático.

### Marketplace y modelo B2B2C
Un marketplace es una plataforma digital que conecta dos o más grupos de actores para facilitar la interacción y transacción.

*Tabla 5. Marketplace y modelo B2B2C.*

| Modelo | Estructura | Ejemplo típico | Valor principal |
| :--- | :--- | :--- | :--- |
| B2B | Empresa a empresa | Proveedores industriales | Negociación entre actores corporativos |
| B2C | Empresa a consumidor | Comercio electrónico | Venta directa al cliente final |
| B2B2C | Plataforma con participantes de dos lados | Airbnb, Uber, EspaciGo | Intermediación y coordinación de confianza |

**Decisión de implementación:** EspaciGo se ubica en un modelo B2B2C porque conecta a arrendadores con arrendatarios y la propia plataforma facilita la transacción, validación y trazabilidad.

### Modelos de negocio y monetización digital

*Tabla 6. Modelos de monetización frecuentes.*

| Modelo | Descripción | Ventaja principal | Riesgo principal |
| :--- | :--- | :--- | :--- |
| Suscripción | Cobro periódico por acceso al servicio | Ingreso estable y predecible | Puede desalentar adopción inicial |
| Freemium | Servicio base gratis y funciones premium | Incrementa volumen de usuarios | Conversión incierta |
| Pago por uso | Cobro por cada operación o unidad | Flexibilidad para distintos perfiles | Costos difíciles de proyectar |
| Comisión transaccional | Cobro por porcentaje de la operación | Alinea ingreso con actividad real | Depende del volumen operativo |
| Tarifa fija | Cobro por publicación o gestión | Simple de explicar | Puede desalentar operaciones pequeñas |

**Decisión de implementación:** EspaciGo adopta un modelo basado en comisión transaccional.

### Cloud Computing, arquitectura web y APIs

*Tabla 7. Arquitectura monolítica vs distribuida.*

| Enfoque | Ventaja principal | Limitación principal | ¿Es adecuado para EspaciGo? |
| :--- | :--- | :--- | :--- |
| Monolítica | Simplicidad inicial | Acoplamiento fuerte y menor evolución | No |
| Arquitectura modular | Separación de dominios y mejor mantenibilidad | Mayor complejidad de integración | **Sí (enfoque adoptado)** |
| Microservicios | Escalado independiente y especialización | Mayor coordinación, observabilidad y costo operativo | No para esta ES1 (no se justifica con el tamaño del equipo ni del alcance) |

**Decisión de implementación:** Arquitectura **modular cloud-native**, con servicios encapsulados para frontend, negocio, persistencia, pago, identidad, documento y auditoría. Los módulos se despliegan como una unidad contenerizada sobre un servicio serverless gestionado, por lo que no se adoptan microservicios con despliegue, datos y ciclo de vida independientes. Esta decisión es la que se formaliza en la sección "Definición de arquitectura TI".

### Gestión de espacios, disponibilidad y riesgo de doble reserva
El problema central es el double booking (doble reserva). La gestión de inventario requiere controlar la disponibilidad por fecha y horario.

**Decisión de implementación:** El sistema implementa validaciones transaccionales en PostgreSQL para prevenir solapamientos y generar bloqueos lógicos del intervalo.

### Sistemas de pago electrónico, retención de fondos y escrow
El escrow es un mecanismo de custodia de fondos en el que un tercero retiene el dinero hasta que se cumplen condiciones definidas, reduciendo el riesgo de fraude.

*Tabla 8. Comparación de mecanismos de pago.*

| Proveedor o mecanismo | Fortalezas | Limitaciones | Aplicación en EspaciGo |
| :--- | :--- | :--- | :--- |
| Webpay | Confianza institucional y uso generalizado | Menor flexibilidad para flujos complejos | Adecuado, pero menos flexible para marketplace dinámico |
| Flow | Integración simple para comercio digital | Menor soporte para retenciones y split | No es la mejor opción para EspaciGo |
| Mercado Pago | APIs modernas, webhooks, split, retención | Requiere mayor integración técnica | Es la opción más alineada con el negocio |
| Escrow | Reducción del riesgo de fraude | Debe estar bien modelado | Es clave para la operación |

**Decisión de implementación:** Utilizar Mercado Pago con soporte a retención de fondos (Escrow) y webhooks.

### KYC, KYB, identidad digital y autenticación
*Tabla 9. Diferencia entre KYC y KYB.*

| Criterio | KYC | KYB |
| :--- | :--- | :--- |
| Usuario | Persona natural | Empresa o entidad |
| Objetivo | Verificar identidad personal | Verificar identidad legal y operativa |
| Riesgo principal | Suplantación, fraude, identidad falsa | Lavado de dinero, entidad no real |
| Relevancia | Usuarios individuales | Arrendadores (particulares o empresas) |

**Decisión de implementación:** EspaciGo adopta identidad verificada con KYC/KYB cruzando datos con el Registro Civil y SII.

### Seguridad, privacidad y protección de datos personales
La normativa chilena (Ley 21.719) establece principios como finalidad, minimización, transparencia, seguridad y eliminación.

*Tabla 10. Matriz de seguridad y privacidad.*

| Área | Seguridad | Privacidad |
| :--- | :--- | :--- |
| Objetivo | Proteger la información frente a amenazas | Garantizar tratamiento adecuado y justo |
| Ejemplo | Cifrado, MFA, TLS, control de acceso | Minimización, transparencia, eliminación |
| Riesgo | Robo, manipulación, vulnerabilidades | Uso indebido, tratamiento excesivo |
| Relevancia | Datos financieros, autenticación e identidad | Datos personales, documentos y auditoría |

**Decisión de implementación:** Privacidad por diseño y seguridad aplicada por capas.

### Contratos digitales, firma electrónica y gestión documental
*Tabla 11. Firma electrónica.*

| Tipo de firma | Nivel de seguridad | Uso típico | Relevancia para EspaciGo |
| :--- | :--- | :--- | :--- |
| Firma simple | Baja | Aceptación de T&C | Útil para consentimientos básicos |
| Firma avanzada | Media-alta | Documentos comerciales | Adecuada para mayoría de contratos |
| Firma cualificada | Máxima | Exigencia legal/financiera | Recomendable para contratos críticos |

**Decisión de implementación:** Flujo de contratos digitales con generación automática e integración con FirmaVirtual.

### Auditoría, trazabilidad y resolución de disputas
*Tabla 12. Tabla de evidencia digital.* (Adaptada)

| Evento | Evidencia relevante | Valor para EspaciGo |
| :--- | :--- | :--- |
| Reserva | Usuario, horario, disponibilidad, estado | Permite validar la operación comercial |
| Pago | Monto, token, estado, timestamp | Confirma la transacción financiera |
| Contrato | Documento firmado y metadata | Soporta la relación legal entre partes |
| Check-in/out | Registro fotográfico, ubicación, estado | Ayuda a resolver conflictos de acceso o daños |
| Reclamo | Documentación, mensajes, historial | Facilita la investigación y respuesta |

**Decisión de implementación:** Modelo de auditoría basado en eventos utilizando Google BigQuery.

### Arquitectura de software y metodologías
El proyecto adopta una **arquitectura de componentes modulares** desplegada en contenedores sobre un servicio serverless gestionado, en lugar de un monolito tradicional o de un modelo de microservicios con despliegue independiente. La comparación de estilos arquitectónicos presentada en este capítulo justifica la decisión: se obtiene el aislamiento y la portabilidad que entregan los contenedores, junto con el escalamiento automático del proveedor cloud, sin asumir el costo operativo de coordinar servicios autónomos con bases de datos y ciclos de despliegue independientes.

Respecto de la metodología, la construcción se organiza mediante un ciclo de vida iterativo e incremental —con incrementos funcionales verificables al cierre de cada iteración— y la gestión del proyecto se apoya en las prácticas del PMBOK para el alcance, el cronograma, los riesgos y los interesados. La correspondencia entre los requisitos del negocio, los casos de uso, los componentes técnicos y su validación se detalla en la sección "Matriz de Trazabilidad" de este informe.

---

## Objetivos del Proyecto

### Objetivo General
Desarrollar e implementar una plataforma web transaccional basada en arquitectura Cloud para la gestión y el arriendo flexible de espacios comerciales, automatizando la firma electrónica avanzada y la retención condicional de pagos (Escrow), e incorporando las funcionalidades orientadas a apoyar el cumplimiento de la normativa legal aplicable (Leyes 21.461 y 21.719) bajo un modelo auditable y trazable.

### Objetivo Específico
1.  Diseñar e implementar la infraestructura operativa basada en contenedores (Docker) para su despliegue continuo (CI/CD) en Google Cloud Platform.
2.  Desarrollar el núcleo lógico construyendo un Backend concurrente en Golang y un Frontend en Next.js.
3.  Integrar servicios críticos consumiendo la API de Mercado Pago (Escrow) y la API de FirmaVirtual.
4.  Configurar un módulo de auditoría y bases de datos bimodales (PostgreSQL/BigQuery) para registrar eventos inmutables.

---

## Formulación de la Solución

### Alcance y restricciones
*   **Alcance:** registro con validación de identidad (KYC/KYB), gestión de perfil y cuenta bancaria, catálogo geolocalizado con búsqueda y filtros, motor de reservas con validación de disponibilidad, pasarela de pagos con retención de fondos (Escrow) y tokenización, pre-autorización de garantía, generación de contratos y firma electrónica, check-in y check-out con evidencia, confirmación de recepción del espacio, historial y cancelación de reservas, reseñas y mensajería entre las partes, resolución de disputas, liquidación de fondos, panel de administración y auditoría inmutable en BigQuery.
*   **Fuera del Alcance de la ES1:** gestión domótica de accesos físicos (cerraduras inteligentes) y responsabilidad civil o penal por daños a la propiedad (EspaciGo es estrictamente intermediario tecnológico). Adicionalmente, producto de la revisión de las Historias de Usuario, se declaran fuera del alcance de esta entrega: lista de espacios favoritos; equipamiento adicional con tarifa propia; disponibilidad recurrente por horarios; panel de estadísticas de ocupación y rentabilidad del arrendador; centro de ayuda con tickets de soporte; centro de notificaciones dentro de la aplicación y notificaciones push; autenticación de doble factor para administradores; tablero de métricas globales; y moderación o suspensión de anuncios reportados (solo se modera reseñas reportadas). Estas funcionalidades no cuentan con requerimientos funcionales asociados en el catálogo vigente.

### Registro de Interesados
*Tabla 13. Registro de Interesados.*

| Nombre / Rol | Tipo de Interesado | Interés en el Proyecto | Nivel de Poder / Influencia |
| :--- | :--- | :--- | :--- |
| Arrendadores (B2B/B2C) | Externo (Cliente) | Rentabilizar espacios ociosos con seguridad. | Alto |
| Arrendatarios | Externo (Cliente) | Encontrar espacios flexibles y pagar sin riesgo. | Alto |
| Teresa Jesús Tapia Soto | Interno (Docente) | Evaluar el cumplimiento académico. | Muy Alto (Aprobación final ES1) |
| Hernán Espinoza | Interno (Arquitecto) | Asegurar escalabilidad, BD y seguridad. | Alto (Ejecución técnica) |
| Erick Silva | Interno (Backend) | Integrar APIs y programar reglas de negocio. | Alto (Ejecución técnica) |
| Anita Marchant | Interno (Frontend) | Proveer una UX ágil e interfaces atractivas. | Alto (Ejecución técnica) |
| Mercado Pago / FirmaVirtual | Externo (Partners) | Volumen transaccional por integración API. | Bajo (Proveedores) |

---

## Metodología de Desarrollo del Proyecto

Se ha optado por implementar una **Metodología Híbrida**, combinando un ciclo Iterativo e Incremental con las mejores prácticas de gestión del PMBOK.

### Cronograma y Equipo de Trabajo
El proyecto contempla 16 semanas de desarrollo en fases incrementales, distribuidas en etapas de análisis, diseño, construcción, validación y cierre. La planificación se estructura como una secuencia iterativa con entregables definidos por etapa para mantener trazabilidad entre requerimientos, arquitectura y validación.

**Equipo y Roles (Matriz RACI)**
*   **Hernán Espinoza (Gerencia / Arquitecto Cloud):** Definición de la infraestructura, diseño BD (PostgreSQL), CI/CD y riesgos.
*   **Erick Silva (Gestión de Personas / Análisis):** Levantamiento de requerimientos, Backend Go, integración Mercado Pago y FirmaVirtual.
*   **Anita Marchant (Desarrollo / Arquitectura UI):** Frontend UX/UI, prototipado en Figma, desarrollo en Next.js.

### Plan de recursos
*   **RRHH (Costo Oportunidad):** 3 integrantes x 16 semanas x 20 hrs/semana x \$15.000/hr = \$14.400.000 CLP.
*   **Tecnológicos (Inversión Inicial Cash-out):** Dominio Web (\$10.950) + Servicios Cloud (\$50.000) = \$60.950 CLP.
*   **Presupuesto Total Valorizado:** \$14.460.950 CLP.

---

## Definición de arquitectura TI

EspaciGo utilizará una **Arquitectura Cloud-Native de componentes modulares basada en contenedores** y un patrón de bases de datos bimodales (OLTP/OLAP). Se denomina *modular* y no *microservicios* porque la solución se compone de una capa de presentación (Next.js) y de un backend Go organizado en módulos funcionales que se despliegan como una unidad contenerizada, complementado con servicios gestionados de la nube e integraciones externas por API; no existen servicios con despliegue, datos y ciclo de vida independientes que justifiquen el modelo de microservicios.

La elección tecnológica se sustenta en una comparación de alternativas por capa, expresada como matrices de decisión arquitectónica (ADR), con el objetivo de justificar no solo la selección de cada componente, sino también la coherencia del conjunto. Para la capa de presentación, `Next.js` fue preferido frente a React puro, Angular y Vue porque ofrece renderizado SSR/SSG nativo, mejor SEO para un marketplace, mejor rendimiento inicial y compatibilidad con una experiencia de usuario moderna. Para la capa de lógica y orquestación, `Go` resultó superior a Node.js, Python y Java porque maneja la concurrencia de forma nativa, consume menos recursos y presenta mejor comportamiento ante tareas intensivas como pagos, generación de documentos y logs simultáneos en entornos cloud. En la capa de persistencia, `PostgreSQL` se escogió frente a MongoDB, MySQL y Firebase por su integridad transaccional, soporte de consultas complejas y capacidades geoespaciales con PostGIS, lo cual es imprescindible para reservas, pagos y ubigeografía de propiedades. En infraestructura, `GCP Cloud Run` se eligió antes que VPS, EC2 o infraestructura on-premise porque administra la escalabilidad, reduce la carga operativa del equipo y optimiza costos con un modelo de pago por uso. En el almacenamiento de auditoría, `BigQuery` fue seleccionado sobre PostgreSQL, archivos planos y Elasticsearch porque ofrece un repositorio analítico inmutable y consultable, compatible con la Ley 21.719 y sin afectar el rendimiento de la base transaccional. Finalmente, `Mercado Pago API` y `FirmaVirtual API` fueron adoptadas porque resuelven de forma nativa las necesidades críticas del negocio: retención de fondos con split de pagos y firma electrónica con valor jurídico para contratos digitales. En conjunto, estas decisiones permiten equilibrar rendimiento, seguridad, cumplimiento legal, costo operativo y escalabilidad, condiciones que definen la viabilidad técnica de EspaciGo como plataforma SaaS B2B/B2C.

**Decisiones Tecnológicas:**
*   **Capa de Presentación:** `Next.js` (Elegido por su SEO vía SSR frente a React SPA puro o Angular).
*   **Capa Lógica (Backend):** `Go` (Golang) (Elegido por su manejo concurrente nativo, bajo consumo y compatibilidad con despliegues en GCP, descartando Node.js y Java como estándar oficial del proyecto).
*   **Base de Datos Operativa (OLTP):** `PostgreSQL` (garantiza transacciones ACID y aporta PostGIS para la geolocalización de las publicaciones).
*   **Infraestructura Cloud:** `GCP Cloud Run` (Serverless, pago por uso).
*   **Empaquetado:** `Docker` (Garantiza consistencia entre entornos).
*   **Auditoría y Logs (OLAP):** `Google BigQuery` (Almacenamiento inmutable para cumplir Ley 21.719).
*   **Integraciones:** `Mercado Pago API` (Escrow/Split Payments y tokenización de medios de pago) y `FirmaVirtual API` (firma electrónica avanzada remota).

---

## Reconocimiento de arquitectura empresarial

**Misión:** Transformar y simplificar la gestión de arriendos comerciales a corto plazo en Chile mediante un ecosistema digital seguro.
**Visión:** Consolidarse como la plataforma líder y estándar de seguridad/transparencia en micro-bodegaje y espacios flexibles.

### Organigrama de Funciones
```text
                    +------------------------------------+
                    | Rol de Gerencia / Dirección General|
                    |        (Líder de Proyecto)         |
                    +------------------------------------+
                                     |
           +-------------------------+-------------------------+
           |                                                   |
+------------------------------------+      +------------------------------------+
| Rol de Gestión de Personas/Análisis|      | Rol de Desarrollo / Arquitectura   |
| Tecnológica                        |      |                                    |
|   (QA, UX/UI, Requerimientos)      |      |   (Cloud, Backend, Frontend, DB)   |
+------------------------------------+      +------------------------------------+
```

### Dominios de la Arquitectura Empresarial
*   **Business Architecture:** Procesos de Registro (KYC), Publicación, Reserva (Escrow), Contratación Digital, Check-in y Disputas.
*   **Application Architecture:** Plataforma Web (Next.js), Backoffice Admin, Core API REST en Go, Integraciones externas.
*   **Data Architecture:** DB Relacional (PostgreSQL), Almacenamiento de archivos (Cloud Storage), Data Warehouse inmutable (BigQuery).
*   **Technology Architecture:** GCP, Docker, Go, Next.js.

---

## Conclusiones
La formulación del proyecto EspaciGo permite concluir que existe viabilidad técnica, comercial y legal para implementar una plataforma SaaS Prop-Tech orientada a la gestión y el arriendo flexible de espacios. La orquestación de APIs modernas (Mercado Pago y FirmaVirtual), soportada por una arquitectura Cloud-Native compuesta por una capa de presentación en Next.js y servicios backend desarrollados en Go, está diseñada para favorecer la escalabilidad y la resiliencia operativa del sistema.

La solución propuesta aborda las principales dificultades identificadas en el mercado tradicional —rigidez contractual, garantías excesivas y ausencia de trazabilidad— mediante funcionalidades concretas: validación de identidad (KYC/KYB), motor de reservas con control de disponibilidad, retención condicional de fondos (Escrow), contratación con firma electrónica avanzada, evidencia fotográfica de check-in y check-out, y auditoría inmutable de las acciones críticas. Estas funcionalidades se orientan a apoyar el cumplimiento de la Ley 21.461 y de la Ley 21.719, en el entendido de que la validez jurídica de cada contrato y el tratamiento de los datos personales se rigen por la normativa vigente y por las condiciones aceptadas por las partes.

Finalmente, la documentación de requisitos alcanza un nivel de detalle verificable y trazable: **236 requerimientos funcionales** cubiertos por **52 casos de uso**, **43 requerimientos no funcionales** que establecen las condiciones de calidad y **35 historias de usuario** agrupadas en **9 épicas** —con cobertura de los **11 módulos funcionales**—, lo que permite sostener que el proyecto está formulado con un alcance delimitado, criterios de aceptación definidos y una arquitectura alineada con los objetivos planteados.
