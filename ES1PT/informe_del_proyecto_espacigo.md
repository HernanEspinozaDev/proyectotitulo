# FORMULACIÓN DEL PROYECTO DE TÍTULO: EspaciGo

**Institución:** Inacap - Informática y Telecomunicaciones
**Asignatura:** Proyecto de Título - TIH184
**Sección:** D-IEI-N8-P1-C2/D
**Académico guía:** Teresa Jesús Tapia Soto
**Integrantes del equipo:** Hernán Espinoza, Anita Marchant, Rick Silva
**Fecha de entrega:** 15 de septiembre del 2026

---

## Introducción

El mercado inmobiliario en Chile enfrenta un desafío creciente de vacancia, especialmente en la subutilización de espacios comerciales, oficinas y quinchos (según estudios, bordeando el 10% en Santiago post-pandemia). A pesar de la alta demanda de emprendedores y pymes por espacios de uso esporádico o flexible, el modelo de arriendo tradicional (As-Is) impone severas barreras de entrada: contratos rígidos, burocracia notarial presencial, garantías excesivas y un alto riesgo de morosidad y fraude tanto para el dueño del inmueble como para el arrendatario.

Para resolver esta fricción, el presente informe detalla la formulación del proyecto de título EspaciGo, una plataforma tecnológica (SaaS Prop-Tech) que actúa como un Marketplace centralizado para la publicación, reserva y gestión de espacios flexibles.

A lo largo del documento (Evaluación Sumativa 1), se abordará la problemática desde la perspectiva de la Ingeniería de Software, definiendo rigurosamente los requerimientos del sistema a través de Historias de Usuario y Casos de Uso predictivos. Posteriormente, se fundamentará la solución bajo un marco teórico que respalda el uso de la Ley 21.461 (Ley Devuélveme mi casa) y la Ley 21.719 (Protección de Datos) como ejes centrales del modelo de negocio.

Desde el punto de vista operativo, se detallan los objetivos generales y específicos del proyecto, junto con una Metodología Ágil (Scrum) y presupuestaria que garantizan su desarrollo en un plazo de 16 semanas. Finalmente, el informe culmina con el diseño y justificación de una Arquitectura TI Cloud-Native basada en microservicios (Next.js, Golang, PostgreSQL, Docker, GCP) y su alineación directa con la Arquitectura Empresarial de la Startup, evidenciando cómo la integración automatizada de pasarelas de pago (Mercado Pago) y firma legal remota (FirmaVirtual) transforman por completo la cadena de valor del rubro inmobiliario chileno.

---

## Identificación del Problema

### Actualización y justificación del problema

**Descripción de la organización. Antecedentes de la Organización.**
El Proyecto se formula bajo la modalidad de Emprendimiento (Startup de Base Tecnológica). La iniciativa nace como un servicio digital SaaS y Marketplace para el mercado chileno, orientado a conectar la oferta de espacio físico subutilizado con la demanda de micro almacenamiento, oficinas temporales y espacios multipropósito a corto plazo.

**Diagnóstico de la situación actual.**
Para comprender la necesidad de esta solución informática, es indispensable analizar el estado actual del Mercado Inmobiliario de Inmuebles Comerciales, Corporativos e Industriales en Chile. En los últimos años, impulsado por la consolidación del trabajo remoto e híbrido post-pandemia y el ajuste económico nacional, el país ha experimentado un fenómeno crítico de desocupación física y vacancia inmobiliaria.

Según informes del sector inmobiliario (tales como reportes de la Cámara Chilena de la Construcción, Colliers y JLL), la vacancia de oficinas en Santiago ha registrado niveles históricos en los últimos periodos, superando tasas de dos dígitos en submercados clave como Santiago Centro (con tasas que oscilan entre el 12% y el 14%) y manteniendo volúmenes importantes de superficie desocupada en sectores como Providencia y Las Condes. A este escenario se suma la fluctuación en el mercado de bodegaje y galpones industriales, donde la sobreoferta de metros cuadrados construidos y la moderación del comercio masivo han incrementado la disponibilidad de bodegas vacías (alcanzando tasas de vacancia de entre el 6% y el 7% en la Región Metropolitana).

Este fenómeno de desocupación masiva genera un doble impacto económico y operativo en el mercado chileno:
*   **Impacto en los Propietarios e Inversionistas:** Se enfrentan a activos "botados" que no generan ingresos pero continúan devengando altos costos fijos, tales como gastos comunes, contribuciones, seguros y mantenimiento. La rigidez de los contratos tradicionales a largo plazo (de 1 a 3 años) frena la reconversión de estos espacios, dejando metros cuadrados completamente ineficientes.
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

Esta acumulación masiva de espacio disponible representa pérdidas millonarias para los propietarios. Al mismo tiempo, la demanda por espacios altamente flexibles y de "última milla" por parte del e-commerce ha aumentado, lo que demuestra un descalce entre la oferta rígida tradicional y las nuevas necesidades dinámicas del mercado.

*Complejidad del problema.*
La resolución de esta problemática mediante una plataforma TI requiere abordar múltiples dimensiones técnicas, operativas y legales interconectadas:
1.  **Complejidad Legal y Normativa:** El arriendo, aunque sea temporal, debe proveer seguridad jurídica para facilitar eventuales desalojos. Esto exige el cumplimiento estricto de la Ley 21.461 ("Devuélveme mi Casa"), lo que obliga al sistema a generar contratos dinámicos que se integren vía API con servicios de firma notarial remota (Firma Electrónica Avanzada). Además, el manejo de documentos de identidad debe cumplir con los altos estándares de privacidad de la Ley 21.719.
2.  **Complejidad Financiera y de Confianza:** Existe el riesgo de daños al inmueble o no pago. El sistema debe implementar transacciones ACID (atomicidad, consistencia, aislamiento, durabilidad) y un modelo Escrow (bóveda de retención de fondos) mediante integraciones complejas (como Mercado Pago Split Payments y bloqueos de cupo en tarjetas), garantizando que los fondos solo se liberen si el check-in/out fotográfico no presenta disputas.
3.  **Sincronización Transaccional Concurrente:** La gestión de múltiples calendarios por hora y día requiere de un backend robusto capaz de manejar alta concurrencia (Goroutines) y evitar las sobre-reservas (Double-Booking), junto con una inyección asíncrona de logs hacia data warehouses (BigQuery) para auditoría.

---

## Levantamiento de Requerimientos

### Determinación de los instrumentos a utilizar
Con el propósito de documentar con precisión las necesidades del mercado, los clientes (propietarios y arrendatarios) y los requisitos legales para el desarrollo de la solución informática EspaciGo, se determinó la aplicación de métodos mixtos. Los instrumentos de levantamiento de información utilizados fueron:
1.  **Encuestas Digitales (Cuantitativo):** Para recopilar datos sobre patrones de uso de bodegaje temporario y disposición a pago flexible por horas/días.
2.  **Entrevistas En Profundidad (Cualitativo):** Para comprender las barreras legales (Ley 21.461) y de seguridad que preocupan a los dueños de espacios, administradores y corredores de propiedades.
3.  **Estudio de Mercado y Benchmark Competitivo:** Para identificar brechas de diseño funcional frente a competidores tradicionales (Mercado Libre, Mudango).
4.  **Grupos de Discusión Técnicos:** Para definir la arquitectura Cloud-Native, el flujo de retención (Escrow) y la trazabilidad de datos (Ley 21.719) junto al equipo de desarrollo.

### Documentar los Requerimientos
Para reflejar la envergadura de una plataforma SaaS Cloud-Native y cumplir con los más altos estándares de Ingeniería de Software, se ha seleccionado una metodología híbrida. Esta combina un modelo de procesos iterativo-incremental para la construcción técnica, junto con las mejores prácticas del PMBOK para la gestión del proyecto.
Se justifica el uso de este enfoque predictivo e iterativo debido a que los requerimientos de la plataforma (financieros, legales y de seguridad) son estables y predecibles, no existiendo un cliente final que cambie los requerimientos estructurales constantemente. La documentación se estructura separando los requerimientos funcionales (estándar IEEE 830) de las historias de usuario y casos de uso, los cuales se desarrollarán en las siguientes iteraciones del proyecto.

### Identificación de Actores del Sistema
Se han identificado los siguientes actores que interactuarán directa o indirectamente con el sistema EspaciGo:

**Actores Primarios (Humanos)**
*   **Visitante:** Usuario anónimo, sin cuenta registrada.
*   **Usuario Registrado:** Posee cuenta con correo verificado pero aún sin validación de identidad.
*   **Arrendador:** Usuario con identidad verificada (KYC/KYB) que publica y gestiona espacios comerciales.
*   **Arrendatario:** Usuario con identidad verificada (KYC/KYB) que busca, reserva y paga por espacios comerciales.
*   **Administrador:** Operador interno de EspaciGo con acceso al panel de control y auditoría.

**Actores Secundarios (Sistemas Externos)**
*   **Registro Civil:** API para validar la vigencia de la cédula de identidad.
*   **SII:** API para validar el inicio de actividades de empresas.
*   **Mercado Pago:** Pasarela de pagos externa.
*   **FirmaVirtual:** Proveedor de servicios de firma electrónica.
*   **BigQuery:** Repositorio externo para almacenamiento inmutable de logs.

### Requerimientos Funcionales (RF)
Los Requerimientos Funcionales definen el comportamiento interno del sistema y cubren todo el ecosistema B2B/B2C. A continuación, se presenta un extracto con los requerimientos principales del flujo core, redactados bajo la norma estricta de un solo verbo atómico por requerimiento y enfocados exclusivamente en el comportamiento observable, delegando los detalles técnicos y de infraestructura hacia la arquitectura.

*Tabla 1. Requerimientos Funcionales (RQF).*

| ID | Descripción del Requerimiento Funcional |
| :--- | :--- |
| RQF-001 | El sistema debe permitir registrar una cuenta de usuario. |
| RQF-011 | El sistema debe permitir iniciar sesión. |
| RQF-034 | El sistema debe permitir solicitar la eliminación de la cuenta de usuario. |
| RQF-044 | El sistema debe validar la vigencia de la cédula ante el organismo correspondiente. |
| RQF-051 | El sistema debe consultar el inicio de actividades de la empresa. |
| RQF-082 | El sistema debe cambiar el estado de la publicación a "Activa" al confirmar la creación. |
| RQF-094 | El sistema debe permitir buscar publicaciones ingresando texto en una barra de búsqueda. |
| RQF-101 | El sistema debe excluir de los resultados las publicaciones sin disponibilidad en las fechas consultadas. |
| RQF-107 | El sistema debe mostrar el desglose de cobro (Estadía + Comisión + Garantía). |
| RQF-111 | El sistema debe validar la disponibilidad del espacio para el intervalo solicitado. |
| RQF-113 | El sistema debe registrar la reserva en estado "Pendiente de Pago" al confirmar disponibilidad. |
| RQF-114 | El sistema debe permitir al usuario seleccionar un método de pago mediante la pasarela integrada. |
| RQF-117 | El sistema debe mantener retenidos los fondos de la reserva hasta que se cumplan las condiciones de liberación. |
| RQF-118 | El sistema debe realizar una pre-autorización por el monto de la garantía. |
| RQF-124 | El sistema debe permitir al arrendador aprobar una solicitud de reserva. |
| RQF-132 | El sistema debe generar un documento de contrato incorporando los datos legales de las partes y el inmueble. |
| RQF-137 | El sistema debe almacenar el contrato final asociado a la reserva tras la confirmación de todas las firmas. |
| RQF-148 | El sistema debe cambiar el estado de la reserva a "En_Curso" tras procesar el Check-in. |
| RQF-162 | El sistema debe bloquear la liberación de fondos de una reserva al detectar un reclamo registrado. |
| RQF-168 | El sistema debe permitir al administrador registrar un fallo a favor del arrendatario. |

### Requerimientos No Funcionales (RNF)
Los requerimientos no funcionales establecen los límites físicos, de calidad y legislativos del sistema. A continuación, se presenta un extracto con los 8 requerimientos más críticos del proyecto, clasificados según el estándar ISO 25010 y el modelo de Sommerville.

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

Los diagramas de casos de uso modelan la interacción funcional entre los actores del sistema (usuarios y sistemas externos) y los límites de la plataforma EspaciGo. A continuación, se presenta una selección de los casos de uso más críticos y representativos clasificados por cada módulo operativo del sistema.

### Módulo 1: Identidad, Autenticación y Privacidad
*   **CU-01: Registrar Cuenta** (Crítico para la captura y alta segura de usuarios).
*   **CU-05: Validar Identidad (KYC/KYB)** (Crucial para el cumplimiento normativo con APIs externas del Registro Civil y SII).
*(Ref: Imagen 1. Casos de uso. Identidad, Autenticación y Privacidad)*

### Módulo 2: Gestión de Catálogo y Publicaciones
*   **CU-08: Crear Publicación de Inmueble** (El núcleo de la oferta de valor del Marketplace).
*   **CU-10: Configurar Calendario y Tarifas** (Esencial para la gestión de disponibilidad temporal).
*(Ref: Imagen 2. Casos de uso. Gestión de Catálogo y Publicaciones)*

### Módulo 3: Búsqueda, Filtrado y Motor de Reservas
*   **CU-12: Buscar Espacios (Mapa / Filtros)** (Clave para la experiencia del arrendatario).
*   **CU-14: Solicitar Reserva** (Crucial para evitar colisiones de fechas en tiempo real).
*(Ref: Imagen 3. Casos de uso. Búsqueda, Filtrado y Motor de Reservas)*

### Módulo 4: Sistema Transaccional, Pagos y Escrow
*   **CU-15: Pagar Reserva y Retener (Escrow)** (El pilar financiero de confianza del Marketplace).
*   **CU-18: Aprobar o Rechazar Solicitud** (Control operativo del propietario sobre la demanda).
*(Ref: Imagen 4. Casos de uso. Sistema Transaccional, Pagos y Escrow)*

### Módulo 5: Marco Legal, Firma Notarial y Operativa
*   **CU-19: Generar y Enviar Contrato a Firma** (Esencial para cumplir la Ley 21.461 "Devuélveme mi casa").
*   **CU-21: Abrir Disputa por Daños** (Mecanismo de protección ante conflictos post-servicio).
*(Ref: Imagen 5. Marco Legal, Firma Notarial y Operativa)*

### Módulo 6: Auditoría Inmutable y Analítica
*   **CU-24: Transmitir Logs Transaccionales** (Garantiza el cumplimiento normativo de la Ley 21.719).
*   **CU-25: Consultar Historial Inmutable** (Herramienta administrativa para trazabilidad forense).
*(Ref: Imagen 6. Casos de uso. Auditoría Inmutable y Analítica)*

---

## Historias de Usuario (Metodología Adaptativa)
Para la planificación iterativa (Sprints), se desglosó el proyecto en 30 Historias de Usuario (HU) agrupadas en Épicas, completadas con sus respectivos criterios de aceptación para la fase de testing. A continuación, se presenta un extracto con las 8 historias más críticas del flujo principal de negocio.

*Tabla 3. Historias de Usuario.*

| Código | Nombre de la Historia | Rol (Como...) | Acción (Quiero...) |
| :--- | :--- | :--- | :--- |
| HU01 | Registro de nuevo usuario | Visitante de la plataforma | Registrarme ingresando mis datos personales y seleccionando mi perfil principal (Propietario o Arrendatario). |
| HU04 | Verificación de identidad (KYC) | Usuario de la plataforma | Subir y verificar mis documentos de identidad oficial para validar mi perfil. |
| HU05 | Publicar un espacio físico | Propietario | Registrar y publicar los detalles de mi espacio físico (como quinchos, bodegas, estacionamientos o parcelas) en la plataforma. |
| HU10 | Búsqueda general de espacios | Arrendatario | Ingresar términos de búsqueda en una barra principal de texto (por ejemplo, por nombre, comuna o tipo de espacio). |
| HU15 | Selección de bloques de fecha y hora | Arrendatario | Seleccionar un rango de fechas y horarios disponibles en el calendario interactivo de un espacio. |
| HU17 | Integración con pasarela de pago | Arrendatario | Ser redirigido de forma segura a una pasarela de pago integrada (como Transbank o Mercado Pago) para efectuar el pago total de la reserva. |
| HU18 | Confirmación de reserva y bloqueo | Sistema EspaciGo | Procesar la respuesta exitosa de la pasarela de pago para confirmar formalmente la reserva y bloquear las fechas. |
| HU28 | Resolución de disputas | Administrador del sistema | Gestionar y mediar en las disputas o reclamos reportados entre propietarios y arrendatarios (por ejemplo, daños a la propiedad). |

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
| Arquitectura modular | Separación de dominios y mejor mantenibilidad | Mayor complejidad de integración | Sí |
| Microservicios | Escalado independiente y especialización | Mayor coordinación y operación | Sí, bajo criterio razonable |

**Decisión de implementación:** Arquitectura modular cloud-native, con servicios encapsulados para frontend, negocio, persistencia, pago, identidad, documento y auditoría.

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
| Relevancia | Usuarios individuales | Propietarios o operadores empresariales |

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
*Tabla 13. Tabla de evidencia digital.* (Adaptada)

| Evento | Evidencia relevante | Valor para EspaciGo |
| :--- | :--- | :--- |
| Reserva | Usuario, horario, disponibilidad, estado | Permite validar la operación comercial |
| Pago | Monto, token, estado, timestamp | Confirma la transacción financiera |
| Contrato | Documento firmado y metadata | Soporta la relación legal entre partes |
| Check-in/out | Registro fotográfico, ubicación, estado | Ayuda a resolver conflictos de acceso o daños |
| Reclamo | Documentación, mensajes, historial | Facilita la investigación y respuesta |

**Decisión de implementación:** Modelo de auditoría basado en eventos utilizando Google BigQuery.

### Arquitectura de software y metodologías
*Tabla 15. Matriz de trazabilidad.*

| Requisito del negocio | Caso de uso | Componente técnico | Validación esperada |
| :--- | :--- | :--- | :--- |
| El espacio no puede reservarse dos veces | Reserva de espacio | Backend + PostgreSQL | Validación de solapamiento y transacción ACID |
| El pago debe confirmarse antes | Confirmación | Backend + pasarela | Estado de pago y retención coherentes |
| El contrato debe estar firmado antes del uso | Aceptación | Contrato + firma | Documento firmado asociado a la operación |
| Auditar acciones críticas | Disputa/revisión | BigQuery + logs | Evidencia histórica y consulta |

---

## Objetivos del Proyecto

### Objetivo General
Desarrollar e implementar una plataforma web transaccional basada en arquitectura Cloud para la gestión y arriendo flexible de espacios comerciales, automatizando la firma notarial y retención condicional de pagos, asegurando el estricto cumplimiento de la normativa legal (Leyes 21.461 y 21.719) bajo un modelo altamente auditable.

### Objetivo Específico
1.  Diseñar e implementar la infraestructura operativa basada en contenedores (Docker) para su despliegue continuo (CI/CD) en Google Cloud Platform.
2.  Desarrollar el núcleo lógico construyendo un Backend concurrente en Golang y un Frontend en Next.js.
3.  Integrar servicios críticos consumiendo la API de Mercado Pago (Escrow) y la API de FirmaVirtual.
4.  Configurar un módulo de auditoría y bases de datos bimodales (PostgreSQL/BigQuery) para registrar eventos inmutables.

---

## Formulación de la Solución

### Alcance y restricciones
*   **Alcance:** Registro con validación de identidad, catálogo geolocalizado, pasarela de pagos Escrow, generación de contratos, firma remota, panel de administración y auditoría inmutable en BigQuery.
*   **Fuera del Alcance:** Gestión domótica de accesos físicos. Responsabilidad civil o penal por daños a la propiedad (EspaciGo es estrictamente intermediario tecnológico).

### Registro de Interesados
*Tabla 17. Registro de Interesados.*

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
El proyecto contempla 5 semanas de desarrollo en fases incrementales.

**Equipo y Roles (Matriz RACI)**
*   **Hernán Espinoza (Gerencia / Arquitecto Cloud):** Definición de la infraestructura, diseño BD (PostgreSQL), CI/CD y riesgos.
*   **Erick Silva (Gestión de Personas / Análisis):** Levantamiento de requerimientos, Backend Go, integración Mercado Pago y FirmaVirtual.
*   **Anita Marchant (Desarrollo / Arquitectura UI):** Frontend UX/UI, prototipado en Figma, desarrollo en Next.js.

### Plan de recursos
*   **RRHH (Costo Oportunidad):** 3 integrantes x 100 hrs x \$15.000/hr = \$4.500.000 CLP.
*   **Tecnológicos (Inversión Inicial Cash-out):** Dominio Web (\$10.950) + Servicios Cloud (\$50.000) = \$60.950 CLP.
*   **Presupuesto Total Valorizado:** \$4.560.950 CLP.

---

## Definición de arquitectura TI

EspaciGo utilizará una Arquitectura Cloud-Native orientada a Microservicios basada en Contenedores y un patrón de bases de datos bimodales (OLTP/OLAP).

**Decisiones Tecnológicas:**
*   **Capa de Presentación:** `Next.js` (Elegido por su SEO vía SSR frente a React SPA puro o Angular).
*   **Capa Lógica (Backend):** `Golang` (Go) (Elegido por su manejo concurrente nativo y bajo consumo en Cloud Run, descartando Node.js y Java).
*   **Base de Datos Operativa (OLTP):** `PostgreSQL` (Garantiza transacciones ACID y posee PostGIS para geolocalización, descartando MongoDB).
*   **Infraestructura Cloud:** `GCP Cloud Run` (Serverless, pago por uso).
*   **Empaquetado:** `Docker` (Garantiza consistencia entre entornos).
*   **Auditoría y Logs (OLAP):** `Google BigQuery` (Almacenamiento inmutable para cumplir Ley 21.719).
*   **Integraciones:** `Mercado Pago API` (Escrow/Split Payments) y `FirmaVirtual API` (Autorización Notarial).

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
*   **Application Architecture:** Plataforma Web (React/Next.js), Backoffice Admin, Core API REST, Integraciones externas.
*   **Data Architecture:** DB Relacional (PostgreSQL), Almacenamiento de archivos (Cloud Storage), Data Warehouse inmutable (BigQuery).
*   **Technology Architecture:** GCP, Docker, Node.js/Go.

---

## Conclusiones
La formulación del proyecto EspaciGo demuestra la viabilidad técnica, comercial y legal de implementar una plataforma SaaS Prop-Tech disruptiva. La orquestación inteligente de APIs modernas (Mercado Pago, FirmaVirtual), soportada por una arquitectura Cloud-Native con microservicios en Golang y Next.js, garantiza la resiliencia operativa y la escalabilidad requerida. El sistema resuelve el problema del mercado tradicional cumpliendo cabalmente con los desafíos de seguridad, confianza y normativa legal en Chile.
