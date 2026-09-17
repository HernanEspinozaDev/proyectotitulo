# IV. Marco teórico corregido y coherente con la arquitectura real de EspaciGo

El presente capítulo desarrolla el marco teórico y conceptual que fundamenta la solución tecnológica de **EspaciGo**. Su objetivo no es funcionar como un diccionario técnico general, sino como una justificación de las decisiones de diseño, arquitectura y operación adoptadas por el proyecto. En este sentido, cada concepto se relaciona con una necesidad funcional concreta, un requisito de negocio o una decisión técnica que define el producto.

La coherencia principal de este marco es que defiende la arquitectura real del proyecto: una plataforma web SaaS cloud-native construida con **Next.js** en la capa de experiencia, **Golang** para la lógica de negocio, **PostgreSQL** como base transaccional, **Google Cloud Run** como entorno de despliegue y **BigQuery** como repositorio analítico de auditoría y trazabilidad.

---

## 4.1 Modelo de distribución: SaaS cloud-native como elección de arquitectura

La decisión entre un software local (*On-Premise*) y un servicio disponible desde la nube no es menor. En el modelo On-Premise, la empresa debe adquirir infraestructura, licencias, servidores, mantenimiento y soporte técnico; esto incrementa la complejidad operativa y reduce la agilidad del producto. En cambio, el modelo SaaS permite entregar la solución como un servicio continuo y accesible a través de internet, con actualizaciones centralizadas y un costo inicial más bajo.

En una plataforma de intermediación como EspaciGo, esta diferencia es decisiva. El sistema debe estar disponible para usuarios, administradores y agentes externos en cualquier momento, soportar múltiples operaciones concurrentes, mantener datos seguros y sincronizados, y facilitar la evolución del producto sin depender de instalaciones físicas por cliente.

> **Justificación arquitectónica:** EspaciGo se diseña como una plataforma **SaaS cloud-native** basada en servicios web. Esto justifica el uso de una interfaz web moderna en **Next.js**, un backend concurrente en **Golang**, un almacenamiento transaccional en **PostgreSQL** y un despliegue administrado en **Cloud Run**. La plataforma no se entrega como software instalado localmente; se ofrece como servicio centralizado y operado en la nube.

---

## 4.2 Marketplace B2B2C: modelo de negocio y estructura de valor

Un marketplace es una plataforma digital que facilita la interacción entre dos o más grupos de usuarios, vinculando oferta y demanda sin necesidad de que la plataforma posea directamente los bienes o servicios. En el caso de EspaciGo, la empresa actúa como intermediario entre propietarios de espacios y personas o empresas que los necesitan.

Este modelo se clasifica como **B2B2C** porque conecta:

- un proveedor de activos o espacio (arrendador)
- un cliente final o usuario de ese activo (arrendatario)
- la plataforma como facilitador tecnológico, financiero y legal

La lógica del negocio no radica en vender un producto estático, sino en reducir la fricción entre oferta y demanda. Para ello, EspaciGo debe garantizar visibilidad del inventario, control de disponibilidad, seguridad de pago, formalización contractual y respuesta ante disputas.

> **Justificación de implementación:** El modelo B2B2C exige una separación clara de roles, permisos y procesos. Esto se refleja en la arquitectura del sistema, donde la capa de experiencia y la capa de negocio están diseñadas para distinguir usuarios, propietarios, administradores y sistemas externos. La lógica del marketplace también explica la necesidad de un backend robusto en **Golang** para gestionar la concurrencia y la coordinación de reglas de negocio.

---

## 4.3 Pagos electrónicos, retención de fondos y escrow

En plataformas de intermediación, el riesgo de fraude y la falta de confianza son factores críticos. Por ello, la transferencia de dinero no puede tratarse como un simple pago directo. La solución adecuada es un mecanismo de retención de fondos, conocido como **escrow**, donde el dinero queda custodiado por un tercero digital hasta que se cumplen condiciones contractuales o de servicio.

Para EspaciGo, la pasarela de pago elegida es **Mercado Pago**, por su capacidad para integrar webhooks, tokenización, split payments y flujos de retención. Esto es especialmente importante en un marketplace donde el dinero debe transferirse solo cuando se verifica la prestación del servicio o se resuelven desencuentros.

En la práctica, el flujo consiste en que el arrendatario paga a través de la plataforma; los fondos quedan retenidos en una bóveda virtual; luego, una vez que se cumple la operación y/o se resuelven disputas, se realiza el desembolso correspondiente al arrendador. Este mecanismo reduce el riesgo de incumplimiento y cumple con los requerimientos de seguridad y trazabilidad del sistema.

> **Justificación arquitectónica:** El uso de **Mercado Pago** como servicio de pago externo explica dos decisiones clave de diseño: no almacenar datos sensibles de tarjetas dentro de la base principal y coordinar cada operación con una trazabilidad clara. La lógica de negocio y la coordinación con el proveedor se implementan en el backend, mientras la base transaccional en **PostgreSQL** conserva el estado del pago y la reserva sin exponer información sensible.

---

## 4.4 Dominio del problema: disponibilidad, reservas y concurrencia

Un espacio comercial no es un producto estático; es un recurso escaso sujeto a condiciones de tiempo, disponibilidad y planificación. En procesos de alquiler flexible, la gestión del inventario debe considerar horarios, fechas, restricciones legales y capacidad de uso.

El problema central es la **reserva concurrente** o *double booking*. Si dos usuarios intentan reservar el mismo espacio para la misma franja horaria al mismo tiempo, una mala implementación puede generar un cobro doble o una disponibilidad inconsistente. Este riesgo es particularmente crítico en sistemas de marketplace con alta demanda y transacciones simultáneas.

> **Justificación de implementación:** La necesidad de evitar dobles reservas requiere un diseño transaccional serio. Por eso, EspaciGo se apoya en **PostgreSQL** como base de datos relacional con propiedades ACID, lo que permite asegurar integridad en operaciones complejas. El backend en **Golang** coordina y validad procesos de negocio, mientras que la base de datos garantiza la consistencia de estados de reserva, disponibilidad y pago.

---

## 4.5 Marco legal y contratos digitales

El entorno de EspaciGo no es solo tecnológico; también es legal. Chile establece marcos normativos relevantes tanto para la protección de datos como para la formalización de contratos, y la plataforma debe operar dentro de esos límites. La firma electrónica y la evidencia digital cobran mayor importancia cuando la operación incluye arriendo, uso temporal y retención de dinero.

La Ley N° 21.461 y otras normas relacionadas estructuran la forma en que deben documentarse y validarse las relaciones inmobiliarias y de uso de espacios. En este contexto, la plataforma no puede depender exclusivamente de un “aceptar términos y condiciones” genérico; debe formalizar la operación con contratos, estados y evidencia progresiva.

> **Justificación técnica:** EspaciGo requiere integración con servicios legales y de documentos para generar contratos firmados, verificar identidad y registrar evidencia. Estas decisiones conectan directamente con la arquitectura del sistema: el backend interactúa con proveedores externos, la base de datos conserva el estado del contrato y la trazabilidad se registra en **BigQuery** para auditoría y evidencias legales.

---

## 4.6 Privacidad, seguridad y trazabilidad de datos

La gestión de información personal y financiera en EspaciGo incluye datos sensibles, como identidades, documentos, montos, pagos y detalles de contratos. En este tipo de sistema, la seguridad no es un complemento; es parte central de la propuesta de valor.

La Ley N° 21.719 introduce obligaciones relevantes sobre protección de datos, privacidad por diseño y tratamiento responsable de la información. A la vez, la plataforma debe conservar evidencia para soportar disputas, auditorías y procesos legales sin violar los principios de privacidad.

> **Justificación arquitectónica:** La separación entre datos transaccionales y datos analíticos es necesaria. La base de datos operativa en **PostgreSQL** mantiene los registros necesarios para operar, mientras que **BigQuery** funciona como repositorio analítico e inmutable para eventos, auditoría y trazabilidad. Esta diversificación permite cumplir con las exigencias legales sin comprometer la usabilidad ni la integridad del sistema.

---

## 4.7 Ingeniería de requisitos y metodología

Un proyecto con estas características no puede gestionarse solo como una colección de historias de usuario generales. Requiere una gestión de requisitos clara, trazable y alineada con los riesgos legales, financieros y técnicos del sistema.

Por esta razón, EspaciGo se desarrolla bajo una metodología ágil con disciplina de ingeniería de requisitos: se priorizan entregas iterativas, pero el levantamiento de requisitos se realiza con rigor. Esto permite adaptar el producto sin perder control del alcance, la seguridad ni la regulatoria.

> **Justificación de implementación:** Las decisiones de arquitectura y negocio deben ser trazables a requisitos. En este marco, el frontend, backend, base de datos, servicios externos y almacenamiento analítico responden a necesidades explícitas del proyecto y no a elecciones improvisadas. Este principio de trazabilidad es clave para sostener la validez técnica y académica del proyecto.

---

### Referencias bibliográficas

*   Benlian, A., Hess, T., & Buxmann, P. (2011). Drivers of SaaS adoption – An empirical study of different application types. *Business & Information Systems Engineering, 3*, 157-169.
*   Hagiu, A., & Wright, J. (2015). Multi-sided platforms. *International Journal of Industrial Organization, 43*, 162-174.
*   Biblioteca del Congreso Nacional de Chile. (2022). *Ley 21.461: Modifica la ley N° 18.101 y el Código de Procedimiento Civil...* Recuperado de https://bcn.cl/leychile
*   Biblioteca del Congreso Nacional de Chile. (2024). *Ley 21.719: Sobre protección de la vida privada.* Recuperado de https://bcn.cl/leychile
*   IBM. (s.f.). What is SaaS? Recuperado de https://www.ibm.com/think/topics/saas
*   NIST. (s.f.). Cloud computing. Recuperado de https://www.nist.gov/itl/applied-cybersecurity/cloud-computing
*   Mercado Pago Developers. (2024). Documentación oficial de pagos y escrow. Recuperado de https://www.mercadopago.cl/developers/
*   Sommerville, I. (2011). *Software Engineering*. Addison-Wesley.

---

### Nota de coherencia de arquitectura

La versión anterior del borrador incorporaba tecnologías que ya no corresponden a la solución final del proyecto (JBoss, Spring MVC y SQL Server). Esta versión corrige ese desalineamiento y deja explícita la justificación del stack real de EspaciGo: **Next.js, Go, PostgreSQL, Cloud Run y BigQuery**. La coherencia entre el marco teórico, la arquitectura TI y la propuesta del proyecto es esencial para sostener la validez del trabajo final.