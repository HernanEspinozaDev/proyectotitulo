# V. Objetivos del Proyecto

## 5.1 Solución Tecnológica

### 5.1.1 Formulación de la Solución

Se desarrollará e implementará **EspaciGo**, una Plataforma Web SaaS (Software as a Service) orientada a la gestión, arriendo flexible y legalización de espacios comerciales. La solución opera bajo una arquitectura *Cloud-Native* distribuida en contenedores (Docker), garantizando **alta disponibilidad** mediante auto-escalado en Google Cloud Run. Para asegurar la **seguridad y performance**, se separa el desarrollo en un *Frontend* rápido renderizado del lado del servidor (Next.js) y un *Backend* concurrente (Golang) diseñado para orquestar transacciones financieras sin bloqueos.

La plataforma se **integra fuertemente con sistemas externos críticos**, consumiendo APIs de entidades financieras (Mercado Pago) para la retención condicional de fondos (*Escrow*), y plataformas Legal-Tech (FirmaVirtual) para la automatización de contratos notariales. Esto reduce drásticamente la fricción burocrática del modelo tradicional.

### 5.1.2 Alcance y Restricciones

*   **Alcance:** La plataforma cubre el registro de usuarios con validación de identidad (KYC/KYB), catálogo geolocalizado de inmuebles, pasarela de pagos con retención *Escrow*, generación dinámica de contratos con firma notarial remota, panel de administración de reservas, y un módulo de auditoría histórica inmutable en BigQuery.
*   **Fuera del Alcance:** El sistema no incluye la gestión domótica de los accesos físicos a los inmuebles (ej. cerraduras inteligentes). Asimismo, EspaciGo opera estrictamente como un intermediario tecnológico, no asumiendo responsabilidad civil o penal por daños a la propiedad, ni actuando como representante legal de ninguna de las partes en tribunales.

## 5.2 Impacto de la Solución

### 5.1.1 Proceso de Negocio Afectado y Diagrama de Contexto

El proyecto rediseña radicalmente el proceso de **"Acuerdo Comercial Inmobiliario"**. En el modelo tradicional (*As-Is*), este proceso es lento y presencial, requiriendo coordinación para visitas a notarías, transferencias bancarias de alto riesgo y un nulo resguardo de los documentos privados (violando la Ley 21.719).
Con EspaciGo (*To-Be*), el proceso se digitaliza, automatizando la confianza entre desconocidos mediante validaciones de identidad en tiempo real, retención segura de fondos y firmas legales a un clic.

**Diagrama de Contexto (Nivel 0):**

```mermaid
flowchart TD
    A(("🧍 Arrendatario")) <-->|Busca, Reserva y Paga| C{"☁️ Sistema EspaciGo\n(Plataforma Central)"}
    B(("🧍 Arrendador")) <-->|Publica y Administra| C
    C <-->|Verifica Identidad (KYC/KYB)| D[("🏛️ Registro Civil / SII")]
    C <-->|Procesa y Retiene Pagos (Escrow)| E[("💳 Mercado Pago API")]
    C <-->|Envía Contratos para Firma Notarial| F[("📝 FirmaVirtual API")]
    C <-->|Almacena Logs Inmutables| G[("📊 Google BigQuery")]
```
*(Nota: Adjuntar imagen del Diagrama de Contexto exportada en alta calidad).*

### 5.2.2 Registro de Interesados (Stakeholders - PMBOK)

| Nombre / Rol | Tipo de Interesado | Interés en el Proyecto | Nivel de Poder / Influencia |
| :--- | :--- | :--- | :--- |
| **Arrendadores (B2B/B2C)** | Externo (Cliente) | Rentabilizar espacios ociosos con seguridad legal y pago garantizado. | Alto (Deciden si adoptan la app). |
| **Arrendatarios (Usuarios)** | Externo (Cliente) | Encontrar espacios flexibles rápidamente y pagar sin riesgo de estafa. | Alto (Generan el flujo de caja). |
| **Teresa Jesús Tapia Soto** | Interno (Docente Guía) | Evaluar el cumplimiento académico, rigor ingenieril y ético del proyecto. | Muy Alto (Aprobación final ES1). |
| **Hernán Espinoza** | Interno (Arquitecto Cloud) | Asegurar la escalabilidad de bases de datos, CI/CD y seguridad de contenedores. | Alto (Ejecución técnica). |
| **Erick Silva** | Interno (Backend/APIs) | Integrar eficientemente las APIs (Pagos, Firmas) y programar reglas de negocio. | Alto (Ejecución técnica). |
| **Anita Marchant** | Interno (Frontend/UI) | Proveer una experiencia de usuario (UX) ágil e interfaces atractivas. | Alto (Ejecución técnica). |
| **Mercado Pago / FirmaVirtual** | Externo (Partners) | Mantener una correcta integración de sus APIs para generar volumen transaccional. | Bajo (Proveedores de servicio). |

### 5.2.3 Indicadores de Gestión (KPIs)
*   **Tiempo de Ciclo de Contratación:** Tiempo promedio medido desde que un usuario envía la solicitud de reserva hasta que el contrato PDF está firmado legalmente por ambas partes.
*   **Tasa de Disputas Resueltas:** Porcentaje de reservas que finalizan con problemas vs. reservas liberadas automáticamente (*Payout*).

### 5.2.4 Niveles de Servicio (SLA)
*   **Disponibilidad:** 99.9% de *Uptime* garantizado gracias a la arquitectura Serverless (Google Cloud Run) distribuida en múltiples zonas.
*   **Privacidad:** Trazabilidad absoluta de accesos. Toda acción generará un log asíncrono en BigQuery con una latencia de escritura menor a 3 segundos.

## 5.3 Objetivos del Proyecto

### 5.3.1 Objetivo General
Desarrollar e implementar una plataforma web transaccional basada en arquitectura Cloud para la gestión y arriendo flexible de espacios comerciales, automatizando la firma notarial y retención condicional de pagos, asegurando el estricto cumplimiento de la normativa legal (Leyes 21.461 y 21.719) bajo un modelo altamente auditable.

### 5.3.2 Objetivos Específicos
1. **Diseñar e implementar** la infraestructura operativa basada en contenedores (Docker) para su despliegue continuo (CI/CD) en entornos escalables de Google Cloud Platform.
2. **Desarrollar** el núcleo lógico de la aplicación construyendo un *Backend* concurrente en Golang y un *Frontend* optimizado para indexación web en Next.js.
3. **Integrar** los servicios críticos de validación externa, consumiendo la API de Mercado Pago para orquestar retenciones financieras (*Escrow*), y la API de FirmaVirtual para la legalización de contratos.
4. **Configurar** un módulo de auditoría asíncrono y bases de datos bimodales (PostgreSQL/BigQuery) para registrar eventos inmutables, dando trazabilidad absoluta a la gestión documental y financiera.
