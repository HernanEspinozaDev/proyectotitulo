# II. Identificación del Problema

## 2.1 Actualización y justificación del problema

### 2.1.1 Descripción de la organización.

**Antecedentes de la Organización:**
El Proyecto se formula bajo la modalidad de Emprendimiento (Startup de Base Tecnológica). La iniciativa nace como un servicio digital SaaS y Marketplace para el mercado chileno, orientado a conectar la oferta de espacio físico subutilizado con la demanda de micro almacenamiento, oficinas temporales y espacios multipropósito a corto plazo. 

**Lienzo CANVAS del Proyecto (EspaciGo):**

| Elemento | Descripción |
| :--- | :--- |
| **Segmentos de Clientes** | **1. Arrendadores (B2B):** Propietarios de oficinas (Clase B/C), bodegas flex, salones y espacios libres vacantes.<br>**2. Arrendatarios (B2C/B2B):** Emprendedores, pymes, productoras y profesionales independientes que requieren espacios flexibles por horas/días. |
| **Propuesta de Valor** | Flexibilización del arriendo comercial sin burocracia presencial. Garantiza seguridad jurídica (firma remota con validación notarial - Ley 21.461) y protección financiera (sistema Escrow). |
| **Canales** | Plataforma Web (SaaS) y Aplicación Móvil (PWA). Marketing digital en LinkedIn y Google Ads. Alianzas con corredoras de propiedades. |
| **Relación con Clientes** | Autoservicio automatizado a través de la plataforma. Soporte técnico y legal para resolución de disputas (mediante evidencia fotográfica de check-in/out). |
| **Fuentes de Ingresos** | Comisión transaccional por reserva completada (porcentaje descontado al liberar los fondos al arrendador). |
| **Recursos Clave** | Plataforma Cloud-Native (GCP), Integraciones API (Mercado Pago, FirmaVirtual), Base de Datos de usuarios validados (KYC/KYB). |
| **Actividades Clave** | Desarrollo y mantenimiento de la plataforma, verificación de antecedentes, gestión de bóveda de contratos dinámicos, auditoría de transacciones. |
| **Asociaciones Clave** | Proveedores de Firma Electrónica (FirmaVirtual), Pasarela de Pagos (Mercado Pago), Registro Civil/SII (para validación de identidad y giro). |
| **Estructura de Costes** | Costos de infraestructura Cloud (GCP: Cloud Run, Cloud SQL, BigQuery), costos por transacciones de APIs de terceros, marketing y mantenimiento de software. |

### 2.1.2 Descripción del problema.

El problema principal radica en la ineficiencia operativa y financiera provocada por la improductividad de metros cuadrados vacíos en el sector inmobiliario urbano y comercial. Por un lado, los dueños asumen altos costos fijos (gastos comunes, contribuciones, mantenimiento) sin generar ingresos frente a una sobreoferta de ciertos tipos de inmuebles. Por otro lado, pequeñas empresas, e-commerce y profesionales independientes se ven marginados por la rigidez contractual y altos costos de garantía del mercado formal (contratos fijos de 12 a 24 meses), cuando solo requieren utilizar un espacio durante un período acotado (horas, días o semanas).

## 2.2 Justificación del problema.

### 2.2.1 Relevancia del problema.

La relevancia de este problema es de alto impacto económico y está respaldada por el comportamiento reciente del mercado de arriendos en Chile. Según informes de consultoras especializadas (como CBRE, Colliers y GPS Property), si bien existe una recuperación general, hay segmentos que mantienen una **vacancia crítica y estancada**:

- **Oficinas Clase C y Antiguas:** Presentan una tasa de desocupación estimada entre el **14% y 18%**, con incapacidad de competir frente a ofertas más modernas, dejando miles de metros cuadrados sin rentabilizar en sectores céntricos (INE, 2026; CBRE, 2026).
- **Bodegas Flex y Modulares:** Exhiben una sobreoferta acentuada con un **14,5%** de vacancia, sumando más de 219.000 m² disponibles solo en la Región Metropolitana (Colliers, 2026).
- **Locales en Galerías y Ejes Secundarios:** Mantienen tasas de desocupación superiores al **15% - 20%** debido a cambios en los flujos peatonales.

Esta acumulación masiva de espacio disponible representa pérdidas millonarias para los propietarios. Al mismo tiempo, la demanda por espacios altamente flexibles y de "última milla" por parte del e-commerce ha aumentado, lo que demuestra un descalce entre la oferta rígida tradicional y las nuevas necesidades dinámicas del mercado.

### 2.2.2 Complejidad del problema.

La resolución de esta problemática mediante una plataforma TI requiere abordar múltiples dimensiones técnicas, operativas y legales interconectadas:

1. **Complejidad Legal y Normativa:** El arriendo, aunque sea temporal, debe proveer seguridad jurídica para facilitar eventuales desalojos. Esto exige el cumplimiento estricto de la **Ley 21.461 ("Devuélveme mi Casa")**, lo que obliga al sistema a generar contratos dinámicos que se integren vía API con servicios de firma notarial remota (Firma Electrónica Avanzada). Además, el manejo de documentos de identidad debe cumplir con los altos estándares de privacidad de la **Ley 21.719**.
2. **Complejidad Financiera y de Confianza:** Existe el riesgo de daños al inmueble o no pago. El sistema debe implementar transacciones ACID (atomicidad, consistencia, aislamiento, durabilidad) y un **modelo Escrow** (bóveda de retención de fondos) mediante integraciones complejas (como Mercado Pago <i>Split Payments</i> y bloqueos de cupo en tarjetas), garantizando que los fondos solo se liberen si el check-in/out fotográfico no presenta disputas.
3. **Sincronización Transaccional Concurrente:** La gestión de múltiples calendarios por hora y día requiere de un backend robusto capaz de manejar alta concurrencia (Goroutines) y evitar las sobre-reservas (Double-Booking), junto con una inyección asíncrona de logs hacia data warehouses (BigQuery) para auditoría.
