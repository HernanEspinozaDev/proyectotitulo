# VIII. Reconocimiento de Arquitectura Empresarial

## 8.1 Identificación del Tipo de Organización y su Estructura

Para asegurar el éxito de la plataforma, el proyecto se concibe bajo el modelo de un **Emprendimiento Tecnológico de alto crecimiento (Startup Prop-Tech y Legal-Tech)**. Su núcleo de negocio opera como un *Marketplace Multisided* (Plataforma Multilateral) B2B2C, donde la empresa actúa como un facilitador transaccional que conecta la oferta (propietarios de inmuebles) con la demanda (arrendatarios y pymes), cobrando un *Take Rate* (comisión) por intermediación.

### 8.1.1 Estructura Organizacional

Dado el modelo de negocio digital, la estructura de la empresa adopta una jerarquía plana, ágil y centrada en el producto (basada en metodologías *Lean Startup*). A diferencia de una corredora de propiedades tradicional, el volumen de empleados no crece linealmente con la cantidad de arriendos, sino que la escalabilidad es sostenida por la automatización tecnológica.

**Organigrama Propuesto:**

```mermaid
flowchart TD
    CEO[Dirección General / CEO\nVisión, Estrategia e Inversión]
    
    CEO --> TECH[Área de Producto y Tecnología\n(Core Team)]
    CEO --> COM[Área Comercial y Growth\n(Adquisición)]
    CEO --> OPS[Área Operaciones y Legal\n(Soporte B2B/B2C)]

    TECH --> BD[Arquitectura Cloud / DevOps]
    TECH --> BACK[Ingeniería Backend e Integraciones]
    TECH --> FRONT[UI/UX y Desarrollo Frontend]

    COM --> B2B[Captación de Oferta (Host B2B)]
    COM --> B2C[Adquisición de Demanda (Ads B2C)]

    OPS --> SUP[Customer Success / Soporte Tier 1]
    OPS --> COMP[Compliance, KYC y Disputas Legales]
```

## 8.2 Procesos de Negocio Afectados y Transformados

La implementación de la solución TI de EspaciGo rediseña la **Cadena de Valor** del rubro inmobiliario. A continuación, se detallan los procesos *Core* que son optimizados drásticamente al pasar de un estado tradicional (*As-Is*) a un estado digitalizado (*To-Be*):

### 8.2.1 Proceso de Onboarding e Integración de Oferta (B2B)
*   **Estado Actual (As-Is):** Altamente friccionado. Un corredor físico debe visitar la propiedad, solicitar escrituras en papel, validar identidad presencialmente y firmar un mandato físico. Tiempo de ciclo: 1 a 3 semanas.
*   **Estado Transformado (To-Be):** Proceso *Self-service* automatizado. El propietario se registra online, el sistema realiza validaciones automáticas KYC (Know Your Customer) mediante la API del Registro Civil/SII, y el inmueble queda publicado en la plataforma. Tiempo de ciclo: Menor a 24 horas.

### 8.2.2 Proceso de Retención Financiera y Fideicomiso (Escrow)
*   **Estado Actual (As-Is):** Arrendatarios y dueños negocian el pago directo por transferencia bancaria o cheques. Existe un alto riesgo de fraude (estafas) y un desgaste administrativo enorme para conciliar los pagos a fin de mes.
*   **Estado Transformado (To-Be):** EspaciGo automatiza el proceso mediante *Split Payments*. El arrendatario paga en la plataforma web, pero el dinero queda congelado en **Mercado Pago**. Solo cuando el arrendatario utiliza el espacio sin reclamos, el sistema libera los fondos (*Payout*) al dueño, descontando automáticamente la comisión de EspaciGo.

### 8.2.3 Proceso de Legalización Contractual (Ley 21.461)
*   **Estado Actual (As-Is):** Las partes coordinan una visita presencial a una Notaría en horario hábil, generando pérdida de tiempo, costos de notaría altos y acumulación de papel.
*   **Estado Transformado (To-Be):** El sistema (Golang) genera un contrato PDF dinámico. Mediante la integración con la API de **FirmaVirtual**, ambas partes firman desde su *smartphone* (Autorización Notarial de Firma), lo cual es plenamente válido para procesos de desalojo express según la Ley "Devuélveme mi Casa".

## 8.3 Compatibilidad de la Solución TI con la Arquitectura Empresarial

Para cumplir con el marco de **Arquitectura Empresarial**, existe un alineamiento perfecto entre los objetivos estratégicos del negocio y las decisiones técnicas adoptadas en el Capítulo 7:

1. **Alineación de Costos (Cloud-Native vs. Bootstrapping):** Al ser una *Startup* sin alto capital inicial, la empresa no puede permitirse comprar servidores físicos ni pagar licencias costosas. La arquitectura basada en *Google Cloud Run* y herramientas *Open Source* asegura que los costos de TI ($210.950 CLP iniciales) sean viables para el organigrama actual.
2. **Alineación de Procesos (APIs vs. Empleados):** En lugar de contratar a 10 asistentes legales para redactar contratos y 5 contadores para conciliar pagos (inflando el Área de Operaciones), la Arquitectura Empresarial delega estas funciones en las integraciones de software (API FirmaVirtual y Mercado Pago). Esto permite mantener un organigrama ágil y concentrar el capital humano en el Área de Producto y Adquisición.
3. **Alineación Legal (BigQuery vs. Compliance):** El modelo de negocio exige operar con el RUT, cuentas bancarias y cédulas de identidad de miles de chilenos. Para evitar multas millonarias bajo la nueva Ley de Datos Personales (21.719), el Área Legal/Compliance se sustenta en el diseño bimodal de la capa de persistencia (uso de BigQuery como bitácora inmutable de auditoría), lo que blinda a la empresa frente a juicios civiles.
