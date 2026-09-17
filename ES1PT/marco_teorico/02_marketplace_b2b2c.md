# 2. Marketplace, B2B2C y confianza en la intermediación digital

## 2.1 Concepto teórico: ¿qué es un marketplace?

Un marketplace es una plataforma digital que conecta a varios grupos de actores para facilitar la interacción, la negociación y la transacción comercial. Su valor no radica en ser el propietario del bien o servicio que se ofrece, sino en reducir la fricción entre oferta y demanda y en generar confianza entre los participantes.

En términos de estrategia digital, un marketplace es una plataforma multisided: crea valor al unir, al menos, dos grupos de usuarios con intereses complementarios. Por ejemplo, un grupo ofrece un activo o servicio y otro lo requiere; la plataforma actúa como intermediario que organiza la relación, la información, la seguridad y la operación.

Esto es especialmente relevante en el contexto inmobiliario y de uso temporal, donde la complejidad no está solo en “mostrar una propiedad”, sino en coordinar identidad, disponibilidad, precio, pago, legalidad y resolución de conflictos.

## 2.2 Tipologías de marketplace y su relación con EspaciGo

Los marketplaces más comunes se clasifican según su estructura de relación comercial:

- B2B: empresa a empresa
- B2C: empresa a consumidor
- B2B2C: plataforma + proveedor + consumidor

| Modelo | Estructura | Ejemplo típico | Valor principal |
|---|---|---|---|
| B2B | Empresa a empresa | Proveedores industriales | Negociación entre actores corporativos |
| B2C | Empresa a consumidor | Comercio electrónico | Venta directa al cliente final |
| B2B2C | Plataforma con participantes de dos lados | Airbnb, Uber, marketplace inmobiliario | Intermediación y coordinación de confianza |

### 2.2.1 Alternativas y criterio de decisión

El problema de EspaciGo no es solo conectar oferta y demanda; es gestionar una operación con riesgo financiero, datos personales, documentación legal y disputa potencial. Por eso, no bastaría con un modelo B2C simple ni con un modelo B2B tradicional. El valor de la plataforma no está únicamente en la venta del espacio sino en la reducción de fricción para la operación completa: disponibilidad, pago, validación, contrato, evidencia y cierre.

### 2.2.2 Aplicación a EspaciGo

EspaciGo encaja en la categoría B2B2C porque no es solo una plataforma de venta directa ni un sistema interno de una empresa. La plataforma conecta a:

- arrendadores, que ofrecen espacios comerciales o de uso temporal
- arrendatarios, que requieren ese espacio para operar, alquilar o utilizarlo
- la propia plataforma, que facilita la transacción, la validación y la traza de la operación

### 2.2.3 Decisión de diseño

> Decisión de diseño: la plataforma se diseña como un marketplace B2B2C con roles diferenciados, validación de identidad, gestión de pagos, contratos y auditoría para asegurar confianza entre actores.

### 2.2.4 Implicación técnica

Esto exige:

- separación por perfil y permisos
- validación de identidad y documentos
- registro de eventos y logs de operación
- gestión de contratos, pagos y disputas desde la misma capa del negocio

## 2.3 ¿Por qué el marketplace exige confianza?

En un marketplace digital, la confianza es un componente crítico del producto. No basta con ofrecer un catálogo de espacios o una interfaz bonita; el usuario debe sentirse seguro de que:

- el otro participante es quien dice ser
- el espacio realmente existe y está disponible
- el pago se realizará de forma segura
- el contrato tendrá validez legal
- la plataforma actuará como autoridad de evidencia si ocurre una disputa

En EspaciGo este problema es aún más sensible porque la operación incluye un activo físico, dinero real, datos personales y acuerdos de uso temporal con implicancias legales. Por eso, la confianza no se logra únicamente con buena UX; debe construirse en la arquitectura del sistema.

### Riesgos principales del marketplace

- fraude en identidad o documentos
- uso de datos falsos o incompletos
- doble reserva del mismo espacio
- pagos no confirmados o cobrados sin operación real
- disputas por servicio no cumplido o daño a la propiedad
- ausencia de evidencia para resolver conflictos

## 2.4 Confianza, reputación y gobernanza digital

La confianza en una plataforma multisided se construye a partir de varios mecanismos:

1. validación de identidad
2. reputación y historial de comportamiento
3. control de disponibilidad y reservas
4. retención de fondos y protección financiera
5. contratos electrónicos y evidencia digital
6. trazabilidad de todos los eventos relevantes

En un sistema como EspaciGo, estos mecanismos no son opcionales. Deben estar integrados como parte del flujo de operación. Por ejemplo, si un arrendador publica un espacio, debe poder demostrar que es el propietario o el autorizado para arrendarlo; si un arrendatario reserva, debe poder pagar con respaldo financiero y tener evidencia del contrato; si ocurre un conflicto, la plataforma debe contar con una bitácora verificable de acciones.

## 2.5 Aplicación directa a EspaciGo

El modelo B2B2C explica varias decisiones fundamentales del sistema:

- separación por roles y permisos de usuario
- validación de identidad y verificación KYB/KYC
- control del ciclo de vida de una reserva
- gestión de pagos con escrow y payout
- generación y registro de contratos digitales
- almacenamiento de eventos en BigQuery para auditoría
- resolución de disputas con trazabilidad y evidencia acumulada

En otras palabras, la plataforma no solo conecta personas; conecta un conjunto de procesos de negocio que deben ser confiables. Por eso, la arquitectura tiene que soportar autenticación, autorización, validación, eventos, pago y evidencia legal.

## 2.6 Decisión de implementación: cómo se refleja el modelo B2B2C en la arquitectura

La lógica del marketplace afecta el diseño del sistema en varios niveles:

| Dimension del marketplace | Decisión en EspaciGo | Justificación |
|---|---|---|
| Roles y permisos | Diferenciación entre arrendador, arrendatario, administrador y sistema externo | Evita acceso indebido y protege operaciones sensibles |
| Identidad | KYC/KYB y verificación documental | Aumenta la confianza en participantes y reduce fraude |
| Pago | Escrow y split payments | Reduce riesgo financiero para ambas partes |
| Contratos | Firma electrónica y documentos legales | Genera evidencia jurídica y formaliza la operación |
| Auditoría | Registro inmutable en BigQuery | Permite rastrear eventos y resolver disputas con prueba |
| Disponibilidad | Plataforma SaaS cloud-native | Soporta reservas concurrentes y operaciones 24/7 |

Este conjunto de decisiones muestra que el modelo B2B2C no es solo una clasificación económica; es una guía para la arquitectura del software.

## 2.7 Implicación técnica en la solución

El modelo B2B2C obliga a implementar mecanismos técnicos específicos:

- módulos separados por tipo de actor y permisos
- autenticación con identidad digital y roles
- validaciones de negocio antes de confirmar reservas
- servicios de pago y retención de fondos
- registro de eventos transaccionales y de auditoría
- flujos de contratación, disputas y resolución
- almacenamiento analítico para eventos históricos

En la práctica, esto se refleja en la solución actual con un frontend en Next.js, un backend en Go, una base de datos relacional en PostgreSQL y un repositorio analítico en BigQuery. La empresa no solo necesita una pantalla web; necesita un sistema coordinado que pueda validar, pagar, documentar y auditar cada transacción.

## 2.8 Conclusión

El modelo B2B2C es el enfoque más adecuado para EspaciGo porque la plataforma no vende un activo directamente, sino que facilita el encuentro entre oferta y demanda en un entorno donde la confianza es esencial. En mercados de uso temporal, la mayor parte del valor no está en la simple publicación de un espacio, sino en la seguridad de la operación.

Por ello, la plataforma debe diseñarse como un sistema de mediación digital con capacidades de identificación, pago, documentación y trazabilidad. La confianza es el eje que hace viable el marketplace; sin ella, la oferta de espacios no se transformaría en transacciones reales.

## 2.9 Fuentes consultadas

- Hagiu, A., & Wright, J. (2015). Multi-sided platforms. *International Journal of Industrial Organization, 43*, 162-174.
- Eisenmann, T. (2006). Strategies for two-sided markets. *Harvard Business Review*.
- Rochet, J. C., & Tirole, J. (2003). Platform competition in two-sided markets. *Journal of the European Economic Association, 1*(4), 990-1029.
- Parker, G. G., Van Alstyne, M. W., & Choudary, S. P. (2016). *Platform Revolution*. W. W. Norton & Company.
- Evans, D. S., & Schmalensee, R. (2016). *Matchmakers: The New Economics of Multisided Platforms*. Harvard Business Review Press.
