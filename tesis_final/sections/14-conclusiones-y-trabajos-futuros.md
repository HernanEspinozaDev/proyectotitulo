# CAPÍTULO XIV: CONCLUSIONES Y TRABAJOS FUTUROS

## 14.1. Conclusiones Integradas por Objetivo Específico

El proyecto de titulación **espaciGo** culmina exitosamente el diseño, construcción, validación y planificación de una plataforma web transaccional y multilateral para el arriendo flexible de inmuebles comerciales e industriales en Chile. A continuación se presentan las conclusiones integradas derivadas del cumplimiento de cada uno de los objetivos específicos:

1. **Respecto al Diagnóstico y Levantamiento de Requerimientos (OE1):**  
   Se logró caracterizar exhaustivamente la problemática de asimetría de información y vacancia ociosa en el mercado no residencial chileno, formalizando un catálogo de **236 Requerimientos Funcionales y 43 Requerimientos No Funcionales** bajo el estándar IEEE 830, articulados con 52 casos de uso y 35 historias de usuario. El levantamiento demostró que la barrera principal no era la falta de metros cuadrados, sino la ausencia de una infraestructura tecnológica que posibilitara contratos dinámicos y pagos protegidos.
2. **Respecto al Diseño Arquitectónico y Modelamiento (OE2):**  
   La adopción de TOGAF en sus cuatro capas y la implementación de una **Arquitectura Hexagonal en Go** permitieron aislar completamente la lógica de negocio de las dependencias externas. Asimismo, el modelado de persistencia en **PostgreSQL 18 y PostGIS 3.6** resolvió matemáticamente el desafío crítico de la sobre-reserva concurrente mediante índices de exclusión temporal `GiST` sobre tipos `tsrange`, erradicando fallas de doble reserva a nivel de base de datos con un rendimiento superior a cualquier esquema de bloqueos en memoria.
3. **Respecto a la Construcción Transaccional, Integración y Seguridad (OE3):**  
   Se construyó con éxito el ecosistema transaccional integrando autenticación sin estado con tokens JWT criptográficos, validación de identidad civil (KYC) y tributaria (KYB), generación automatizada de contratos PDF dinámicos para firma electrónica remota (Ley N° 21.461) y la operatoria fiduciaria de **pagos en custodia (*escrow*) con división de pagos (*split payments*)**, eliminando el riesgo moral y la desconfianza mutua entre las partes.
4. **Respecto al Aseguramiento de Calidad y Resiliencia (OE4):**  
   Las pruebas automatizadas bajo el estándar ISO/IEC 25010 certificaron una calidad de nivel empresarial: el backend alcanzó un **$86.4\%$ de cobertura de código**, las pruebas de estrés con 500 usuarios concurrentes arrojaron una latencia percentil 95 de apenas **$184\text{ ms}$** (superando la meta de $250\text{ ms}$) y una capacidad de procesamiento de **$612\text{ peticiones por segundo}$** con cero errores. Asimismo, los simulacros de contingencia en Google Cloud validaron empíricamente un **RPO de $2.5\text{ minutos}$** (meta $\le 15$ min) y un **RTO de $8.5\text{ minutos}$** (meta $\le 1$ hora), certificando la continuidad operativa del servicio.
5. **Respecto al Despliegue, Continuidad y Viabilidad (OE5):**  
   Se implementó un pipeline automatizado de CI/CD sobre **Google Cloud Run** en la región de Santiago, integrando políticas de ciberseguridad *Zero Trust* y un innovador **protocolo de purga anti-restauración (*anti-replay*)**, garantizando que los respaldos históricos respeten plenamente los derechos de supresión de datos consagrados en la nueva **Ley N° 21.719**.

---

## 14.2. Aportes y Contribución a la Industria Inmobiliaria y Ciberseguridad

El proyecto aporta a la ingeniería aplicada y al mercado nacional en tres dimensiones clave:
*   **Pionero en Prop-Tech Flexible en Chile:** Transforma el concepto tradicional de arriendo pasivo anual hacia un modelo dinámico de *Space-as-a-Service* (SPaaS), permitiendo a microempresas y emprendedores de *e-commerce* acceder a bodegas, oficinas y locales comerciales por días o semanas con plena validez jurídica.
*   **Referente Técnico en Privacidad por Diseño (Ley N° 21.719):** Constituye una de las primeras arquitecturas universitarias chilenas en diseñar formalmente el ciclo de vida de los datos personales con protocolos de no reactivación post-restauración (*anti-replay restoration*).
*   **Gobernanza Híbrida Rigurosa:** Evidencia la efectividad de combinar la gobernanza estructurada de PMBOK (mediante la EDT y el control de variaciones) con ciclos iterativos e incrementales de desarrollo de software.

---

## 14.3. Limitaciones Encontradas durante el Ciclo de Vida

A lo largo del proyecto se identificaron las siguientes limitaciones:
1. **Dependencia de Servicios Externos de Identidad:** La disponibilidad de las consultas automatizadas hacia los servicios gubernamentales (Registro Civil y SII) experimenta ventanas de mantenimiento nocturno no programadas, requiriendo colas de reintento asíncronas para no bloquear la experiencia de registro del usuario.
2. **Curva de Adopción Digital en Propietarios Tradicionales:** Propietarios de inmuebles de mayor edad presentan resistencia al uso exclusivo de billeteras digitales y firmas remotas, lo que exige diseñar interfaces web extremadamente intuitivas y asistidas paso a paso.

---

## 14.4. Trabajos Futuros y Hoja de Ruta de Evolución de espaciGo

Como hoja de ruta para la evolución y madurez de la plataforma en fases posteriores de emprendimiento, se contemplan las siguientes líneas de desarrollo:

**Figura 23**  
*Línea de Tiempo de la Hoja de Ruta Tecnológica de espaciGo (2027 - 2029)*

![](assets/figuras/fig23_hoja_ruta_tecnologica.png)

*Nota.* Elaboración propia en base a la planificación de fases evolutivas del emprendimiento tecnológico espaciGo SpA.

1. **Integración con Cerraduras Inteligentes e Internet de las Cosas (IoT):**  
   Desarrollar una pasarela de comunicación con cerraduras inteligentes (*Smart Locks*) habilitadas por Bluetooth de Baja Energía (BLE) y Wi-Fi, permitiendo que la plataforma genere códigos de acceso temporales o llaves digitales que se activen automáticamente a la hora del *check-in* y caduquen en el *check-out*, eliminando la necesidad de entrega física de llaves.
2. **Motor de Fijación Dinámica de Precios (*Dynamic Pricing* con Machine Learning):**  
   Implementar modelos predictivos de aprendizaje automático que sugieran tarifas óptimas a los arrendadores en tiempo real, considerando estacionalidad (días hábiles vs. fines de semana), eventos de alta demanda en el entorno urbano (conciertos, ferias comerciales) y tasas de vacancia zonales.
3. **Módulo de Microseguros Inmobiliarios On-Demand:**  
   Establecer convenios API con compañías aseguradoras para emitir pólizas de cobertura de daños y responsabilidad civil por día, cobradas de manera transparente junto al canon de arriendo.
4. **Expansión Internacional a Mercados Emergentes:**  
   Adaptar la capa de localización y pasarelas de pago para iniciar operaciones en ciudades con problemas similares de vacancia y alta informalidad inmobiliaria en la región, tales como Lima y Bogotá.
