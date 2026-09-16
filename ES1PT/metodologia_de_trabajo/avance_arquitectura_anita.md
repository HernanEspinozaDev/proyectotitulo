## 7. 🏗️ Arquitectura Empresarial

Para sustentar el modelo de negocio SaaS (Software as a Service) de **EspaciGo** y asegurar el correcto funcionamiento del Marketplace B2B2C de espacios comerciales, se ha estructurado una arquitectura empresarial integral. Esta arquitectura permite alinear los objetivos de negocio con los procesos, los datos y la tecnología que soportan la plataforma.

### 7.1. Identidad Organizacional de EspaciGo

Como empresa tecnológica y desarrolladora de la plataforma, se ha definido una identidad estratégica clara:

*   **Misión:** Transformar y simplificar la gestión y arriendo de espacios comerciales a corto y mediano plazo, eliminando la fricción burocrática y el riesgo de fraude mediante un ecosistema seguro, automatizado y centrado en la confianza entre propietarios y arrendatarios.
*   **Visión:** Consolidarnos como la plataforma líder en el mercado de arriendos comerciales flexibles (SaaS B2B2C), siendo el estándar de seguridad y transparencia a través de la integración de identidad verificada y contratos digitales inteligentes.
*   **Objetivos Estratégicos:**
    *   Proveer un proceso de arriendo "End-to-End" 100% digital, reduciendo los tiempos de validación legal y de pagos.
    *   Garantizar alta seguridad y disponibilidad en las transacciones mediante un modelo de pago en garantía (*Escrow*).
    *   Cumplir con las normativas legales de privacidad (Ley 21.719) y mantener una trazabilidad inmutable de todas las operaciones críticas.
*   **FODA (Análisis Estratégico):**
    *   **Fortalezas:** Alto nivel de seguridad (validaciones KYC/KYB), automatización total de contratos (FirmaVirtual) y sistema de pagos protegido (*Escrow*).
    *   **Oportunidades:** Creciente demanda de flexibilidad en espacios comerciales, digitalización de las PYMES y profesionales independientes.
    *   **Debilidades:** Marca nueva sin base de usuarios inicial (problema de adquisición en marketplaces), alta dependencia técnica de APIs de terceros (Mercado Pago, FirmaVirtual).
    *   **Amenazas:** Cambios en la legislación de subarriendos comerciales o tributación digital, competidores indirectos tradicionales (corredoras de propiedades) adoptando nuevas tecnologías.

### 7.2. Organigrama y Roles del Equipo

El equipo fundador e implementador de la empresa está compuesto por tres profesionales (Analistas Programadores) que asumen roles estratégicos diferenciados para cubrir todas las áreas de gestión de la organización:

1.  **Rol de Gerencia / Gestión General:**
    *   **Responsabilidades:** Toma de decisiones estratégicas a nivel de negocio y finanzas. Encargado del control presupuestario, negociaciones (ej. con proveedores de APIs) y gestión general de riesgos del proyecto.
2.  **Rol de Gestión de Personas / Análisis:**
    *   **Responsabilidades:** Lidera el levantamiento y validación de los requerimientos funcionales y no funcionales. Supervisa la calidad del producto (QA), la experiencia del usuario (UX/UI), y gestiona el flujo de trabajo del equipo.
3.  **Rol de Desarrollo / Arquitectura Tecnológica:**
    *   **Responsabilidades:** Define la infraestructura tecnológica y lidera la programación. Encargado de la arquitectura cloud, despliegue en contenedores, seguridad, automatizaciones y gestión de la base de datos.

### 7.3. Los 4 Dominios de la Arquitectura Empresarial

La estructura operativa de EspaciGo se divide en cuatro arquitecturas fundamentales que operan de forma orquestada:

#### 1. Arquitectura de Procesos
Define *qué* hace el negocio y cómo operan los flujos de valor centrales de la empresa:
*   **Proceso de Verificación de Identidad:** Flujo automatizado de KYC (Personas con Registro Civil) y KYB (Empresas con SII) para mitigar fraude y habilitar la transaccionalidad.
*   **Proceso de Reserva y Gestión de Pagos:** Flujo de retención de fondos y bloqueo de garantía en tarjeta de crédito (*Escrow*), con liberación de pagos (*Payout*) automatizada tras finalizar la estadía.
*   **Proceso de Legalización y Contratos:** Inyección dinámica de datos verificados en plantillas legales, envío de documentos para firma electrónica y resguardo del contrato firmado.
*   **Proceso de Resolución de Disputas:** Flujo de levantamiento de reclamos post-arriendo (con evidencias de check-in/out fotográfico) para retención cautelar y mediación administrativa.

#### 2. Arquitectura de Aplicación
Define *qué sistemas* se construyen y utilizan para automatizar los procesos anteriores:
*   **Marketplace EspaciGo (Core App):** La plataforma SaaS central a la cual acceden Arrendadores y Arrendatarios para publicar, buscar y gestionar espacios.
*   **Módulo de Panel de Administración (Backoffice):** Interfaz exclusiva para administradores de la empresa para fallar disputas, revisar validaciones KYC manuales y supervisar auditorías.
*   **Integraciones Externas (Servicios Conectados):** El sistema interactúa nativamente con sistemas de terceros como Mercado Pago y FirmaVirtual.

#### 3. Arquitectura de Datos
Define *cómo se estructura, fluye y resguarda la información*:
*   **Modelo Relacional (Datos Transaccionales):** Base de datos estructurada para gestionar usuarios, publicaciones, reservas y configuraciones del catálogo.
*   **Flujo de Información Segura:** Los datos sensibles viajan cifrados. Las contraseñas se almacenan fuertemente encriptadas (ej. con bcrypt) y los contratos generados se almacenan resguardados de accesos no autorizados.
*   **Data Warehouse de Trazabilidad:** Almacenamiento analítico e inmutable (ej. BigQuery o similar) para mantener un log completo de toda acción crítica (firmas, pagos, ingresos) con propósitos de auditoría legal irrefutable.

#### 4. Arquitectura de Infraestructura Tecnológica
Define el *soporte físico, virtual y de plataformas* donde operan las aplicaciones:
*   **Entorno Cloud (Nube):** La plataforma se aloja en infraestructura cloud garantizando alta disponibilidad, seguridad física de los servidores y escalabilidad ante fluctuaciones de tráfico.
*   **Contenedores:** El sistema estará automatizado y empaquetado mediante tecnología de contenedores (como **Docker**), asegurando despliegues confiables e idénticos en cualquier entorno.
*   **Frameworks y Motor de Base de Datos:** Utilización de frameworks modernos para el desarrollo web backend y frontend, en conjunto con un robusto motor de base de datos relacional (ej. MariaDB).
