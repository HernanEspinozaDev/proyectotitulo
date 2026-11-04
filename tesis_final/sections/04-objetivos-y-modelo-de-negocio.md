# CAPÍTULO IV: OBJETIVOS DEL PROYECTO Y MODELO DE NEGOCIO

## 4.1. Objetivo General

Diseñar, desarrollar e implementar una plataforma web transaccional y multilateral para la intermediación y gestión de arriendos flexibles de espacios comerciales e industriales no residenciales (oficinas, bodegas modulares, locales comerciales y estacionamientos) en Chile, mediante una arquitectura de software desacoplada en Go y Next.js sobre Google Cloud Platform, persistencia geoespacial en PostgreSQL/PostGIS y mecanismos fiduciarios de custodia de fondos (*escrow*), con el propósito de erradicar el riesgo de sobre-reserva concurrente, reducir los tiempos de vacancia inmobiliaria y garantizar la seguridad jurídica y protección de datos personales conforme a la Ley N° 21.719.

---

## 4.2. Objetivos Específicos

1. **OE1 — Diagnóstico y Levantamiento de Requerimientos:**  
   Levantar y especificar exhaustivamente los requerimientos funcionales y no funcionales del sistema bajo el estándar IEEE 830, modelando casos de uso, historias de usuario y procesos de negocio actuales (*As-Is*) para formalizar la línea base del alcance y los acuerdos de nivel de servicio (SLAs).
2. **OE2 — Diseño Arquitectónico y Modelamiento de Ingeniería:**  
   Diseñar la arquitectura empresarial bajo el estándar TOGAF en sus cuatro capas (Negocio, Datos, Aplicaciones e Infraestructura) e implementar una arquitectura de software Hexagonal (*Ports and Adapters*) en Go con una capa de presentación BFF (*Backend for Frontend*) en Next.js, definiendo un modelo de datos relacional y geoespacial en PostgreSQL/PostGIS con restricciones de exclusión temporal para prevenir sobre-reservas.
3. **OE3 — Construcción Transaccional, Integración y Seguridad:**  
   Construir el núcleo operativo de la plataforma incorporando módulos de autenticación segura (OAuth2/JWT con RBAC), validación de identidad KYC/KYB, gestión de publicaciones y calendarios, pasarela de pagos con retención en garantía (*escrow*) y generación dinámica de contratos con firma electrónica remota alineada con la Ley N° 21.461.
4. **OE4 — Aseguramiento de Calidad, Pruebas y Resiliencia:**  
   Verificar y validar la calidad del sistema mediante la formulación y ejecución de un plan de pruebas integral bajo el estándar ISO/IEC 25010 (pruebas unitarias, de integración, rendimiento con JMeter para latencias P95 y pruebas de continuidad operativa que certifiquen un RPO $\le 15$ minutos y un RTO $\le 1$ hora).
5. **OE5 — Planificación de Despliegue, Continuidad y Factibilidad Económica:**  
   Formular la estrategia de puesta en producción automatizada (CI/CD) sobre infraestructura contenerizada en Google Cloud Platform, integrando el protocolo de recuperación ante desastres con purga anti-restauración según la Ley N° 21.719, junto con la evaluación societaria y viabilidad económica del emprendimiento.

---

## 4.3. Modelo de Negocio (Lienzo Canvas)

La articulación económica del proyecto se formula mediante el **Lienzo de Modelo de Negocio (Canvas)** (Osterwalder & Pigneur, 2010), adaptado a la dinámica de una plataforma tecnológica multilateral:

**Tabla 2**  
*Lienzo del Modelo de Negocio (Canvas) para espaciGo*

| Bloque del Modelo | Descripción y Estrategia de espaciGo |
|---|---|
| **1. Propuesta de Valor** | • **Para Arrendadores:** Monetización inmediata de metros cuadrados ociosos, selección confiable de usuarios mediante validación KYC/KYB, contratos automatizados y cobertura de garantía mediante depósito en custodia (*escrow*).<br>• **Para Arrendatarios:** Acceso flexible por días o semanas sin avales bancarios ni contratos forzosos anuales, confirmación de disponibilidad en tiempo real, reserva 100% digital y protección de fondos ante fraudes o incumplimientos. |
| **2. Segmentos de Clientes** | • **Lado Oferta (Arrendadores):** Propietarios individuales de bodegas o locales, inversionistas de oficinas Clase B y C, empresas inmobiliarias con inventario disponible y operadores de estacionamientos comerciales.<br>• **Lado Demanda (Arrendatarios):** Microempresas y emprendedores de *e-commerce*, productoras de eventos y agencias de publicidad, profesionales independientes y comerciantes estacionales. |
| **3. Canales de Distribución** | • Aplicación web responsiva optimizada para navegación móvil y de escritorio (*Single Page Application* con SSR).<br>• Posicionamiento orgánico (SEO) geoespacial por comunas y tipologías de espacio.<br>• Campañas de marketing digital B2B en LinkedIn y Google Ads.<br>• Alianzas estratégicas con asociaciones gremiales de Pymes (ASECH) y centros de emprendimiento. |
| **4. Relación con Clientes** | • Autoservicio automatizado (*self-service*) transparente y guiado paso a paso.<br>• Soporte técnico y canal de resolución de disputas asistido por evidencia fotográfica.<br>• Sistema de reputación bilateral con calificaciones y reseñas auditables. |
| **5. Fuentes de Ingresos** | • **Comisión Transaccional (*Take Rate*):** Cobro porcentual del 8% al 12% sobre el valor neto de cada arriendo completado exitosamente a través de la plataforma.<br>• **Servicios de Destaque (*Promoted Listings*):** Tarifas fijas para posicionar anuncios en las primeras posiciones de búsqueda.<br>• **Servicios de Firma Electrónica Avanzada:** Cargo operacional por la generación y notarización remota del contrato digital. |
| **6. Recursos Clave** | • Infraestructura Cloud elástica en Google Cloud Platform (Cloud Run, Cloud SQL PostgreSQL, Cloud Storage).<br>• Motor de persistencia geoespacial PostGIS y algoritmos de sincronización de calendarios.<br>• Contratos inteligentes y plantillas legales redactadas por especialistas inmobiliarios.<br>• Base de datos de espacios y perfiles verificados. |
| **7. Actividades Clave** | • Desarrollo continuo, soporte, mantenimiento y monitoreo de la plataforma web.<br>• Moderación activa de publicaciones y verificación de antecedentes de usuarios (KYC/KYB).<br>• Mediación técnica y arbitraje imparcial en el proceso de resolución de disputas.<br>• Gestión de ciberseguridad, respaldo de datos y cumplimiento de la Ley N° 21.719. |
| **8. Alianzas Clave** | • Pasarela de pagos digitales certificada (Mercado Pago / Transbank Webpay).<br>• Proveedor de firma electrónica remota acreditada (FirmaVirtual).<br>• Entidades gubernamentales de consulta de identidad (Servicio de Registro Civil e Identificación y SII).<br>• Asociaciones gremiales y redes de corredores digitales. |
| **9. Estructura de Costos** | • Costos de infraestructura Cloud (servidores contenerizados, base de datos gestionada, balanceadores y CDN).<br>• Tarifas de pasarela de pago por procesamiento transaccional.<br>• Costo por firma digital y validación documental notarial remota.<br>• Gastos legales, tributarios (SpA, patentes municipales) y marketing de captación inicial. |

*Nota.* Elaboración propia adaptada de Osterwalder y Pigneur (2010).

---

## 4.4. Alcances, Condiciones de Servicio y Limitaciones del Proyecto

En conformidad con las directrices docentes, la delimitación operativa se formaliza bajo el estándar de **Condiciones Contractuales de Servicio (Términos y SLAs)**:

### 4.4.1. Condiciones y Cláusulas del Servicio
1. **Cláusula de Identificación y Capacidad Legal (KYC/KYB):**  
   Todo usuario que actúe en calidad de Arrendador o Arrendatario debe superar satisfactoriamente la validación de identidad digital. Las personas naturales deben aportar cédula de identidad nacional vigente; las personas jurídicas deben acreditar poder de representación legal y personería vigente. La plataforma se reserva el derecho de rechazar perfiles con antecedentes falsificados o inconsistentes.
2. **Cláusula de Reserva, Pago y Operatoria Escrow:**  
   La confirmación de una reserva se perfecciona únicamente con el pago íntegro del canon de arriendo y la autorización del bloqueo de cupo por garantía en la tarjeta de crédito del Arrendatario. Los fondos permanecen en la cuenta de custodia temporal de la plataforma. Si el Arrendador rechaza la solicitud en un plazo superior a 24 horas, el sistema revierte el cargo de forma íntegra y automática sin costos para el solicitante.
3. **Cláusula de Políticas de Cancelación y Reembolso:**  
   El Arrendador puede seleccionar una de tres políticas de cancelación estandarizadas:
   - *Flexible:* Reembolso del 100% de la renta si la cancelación se produce hasta 48 horas antes del inicio del arriendo.
   - *Moderada:* Reembolso del 50% de la renta si la cancelación se produce entre 7 días y 48 horas previas al inicio.
   - *Estricta:* Sin derecho a reembolso de renta una vez confirmada la reserva, procediéndose únicamente a la liberación del 100% de la garantía.
4. **Cláusula de Verificación Fotográfica (Check-in / Check-out):**  
   Para la validez de cualquier reclamación sobre garantías, ambas partes deben registrar las evidencias fotográficas de ingreso y egreso en la plataforma dentro de los márgenes horarios pactados. La ausencia de registro fotográfico por una de las partes priva a dicha parte del derecho a disputar el estado del inmueble.
5. **Cláusula de Resolución de Disputas y Arbitraje Técnico:**  
   Si se levanta un reclamo por daños en las 24 horas posteriores al *check-out*, la garantía permanece congelada. Un administrador de espaciGo evalúa el contraste fotográfico y la bitácora del sistema emitiendo una resolución técnica inapelable en un plazo máximo de 5 días hábiles.

### 4.4.2. Limitaciones Operativas y Tecnológicas
*   **Delimitación Territorial:** La cobertura del sistema se acota durante la fase operativa inicial a las comunas de la Región Metropolitana de Santiago.
*   **Inmuebles Excluidos:** Se excluye explícitamente el arrendamiento de viviendas residenciales habituales (casas y departamentos habitacionales), manteniéndose el foco exclusivo en bienes de uso comercial, logístico y corporativo.
*   **Exclusión de Responsabilidad Material:** La plataforma no asume la custodia física de mercaderías almacenadas en las bodegas ni responde por hurtos o incendios que acontezcan dentro de los recintos, debiendo las partes contratar los seguros correspondientes según las cláusulas de servicio.
