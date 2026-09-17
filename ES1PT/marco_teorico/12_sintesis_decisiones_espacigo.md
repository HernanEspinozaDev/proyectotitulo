# 12. Síntesis de decisiones teóricas y de implementación para EspaciGo

## 12.1 Relación entre teoría y sistema

El marco teórico de un proyecto de ingeniería no debe limitarse a definir conceptos de manera general. Debe demostrar que cada teoría se traduce en una decisión técnica, de negocio o legal del sistema. En EspaciGo, cada área del conocimiento aporta una justificación concreta de la arquitectura y del modelo operativo.

La coherencia del proyecto no depende solo de la innovación del concepto, sino de su capacidad para resolver un problema real: conectar espacios, usuarios, pagos, contratos, seguridad y evidencia.

## 12.2 Síntesis de decisiones por concepto

| Concepto teórico | Problema que resuelve | Alternativas relevantes | Decisión tomada en EspaciGo | Impacto técnico |
|---|---|---|---|---|
| SaaS | Necesidad de acceso constante y centralizado | SaaS, On-Premise, software licenciado | SaaS cloud-native | Despliegue en la nube y acceso web centralizado |
| Marketplace B2B2C | Conectar oferta y demanda con confianza | B2B, B2C, B2B2C | B2B2C con roles diferenciados | Módulos de arrendador, arrendatario y administración |
| Modelos de monetización | Generar ingresos sostenibles | Suscripción, freemium, por uso, comisión | Comisión por operación | Cálculo de take rate y payout |
| Cloud computing y APIs | Escalabilidad y conexión de servicios | Monolito, modular, microservicios | Modular y cloud-native | APIs REST, servicios desacoplados y Cloud Run |
| Disponibilidad y reservas | Evitar doble reserva | Calendario manual, validación simple, estado transaccional | Control transaccional por intervalo | PostgreSQL y validación antes de confirmar |
| Pagos digitales y escrow | Riesgo de fraude y falta de confianza | Pago directo, cobro sin retención, escrow | Pago con retención y webhook | Integración con pasarela y estados financieros |
| KYC/KYB y autenticación | Validar identidad y reducir fraude | Sin validación, validación mínima, verificación formal | KYC/KYB + autorización por roles | Seguridad y control de acceso |
| Privacidad y protección de datos | Proteger información personal | Seguridad aislada, privacidad por diseño | Privacidad por diseño | Cifrado, minimización y separación de bases |
| Contratos digitales | Formalización de la relación y reducción de riesgo | Contrato manual, contrato digital sin firma, firma digital | Contrato digital con firma electrónica | Documentos, metadata y evidencia |
| Auditoría y trazabilidad |Resolver disputas y sostener evidencia | Logs básicos, auditoría aislada, audit trail estructurado | Audit trail con eventos y BigQuery | Evidencia histórica y análisis |
| Arquitectura de software | Mantener coherencia y escalabilidad | Monolito, modular, microservicios | Arquitectura modular con stack real | Next.js, Go, PostgreSQL, Cloud Run, BigQuery |

## 12.3 La teoría como base racional del diseño del sistema

Cada una de estas decisiones no surge de una intuición aislada, sino de la intersección entre requisitos funcionales, normativa, seguridad y experiencia de usuario. Por ejemplo:

- el modelo SaaS justifica la disponibilidad de la plataforma como servicio digital
- el marketplace B2B2C explica la necesidad de distinguir roles y responsabilidades
- la monetización explica por qué existe un modelo de comisión y reglas de retención
- la gestión de disponibilidad justifica la necesidad de concurrencia y consistencia de datos
- la seguridad y la privacidad explican por qué los datos deben dividirse, protegerse y limitarse
- la firma digital y la auditoría respaldan la validez jurídica y la evidencia para disputas

La teoría no es un adorno académico; es la explicación racional de por qué EspaciGo está construido de esa forma.

## 12.4 Integración de la arquitectura tecnológica con la lógica del negocio

La arquitectura elegida para EspaciGo refleja de manera directa el modelo de negocio y la complejidad del servicio:

- Next.js facilita la experiencia web y la interacción con el usuario final
- Go permite una lógica backend robusta, eficiente y escalable
- PostgreSQL ofrece consistencia y soporte transaccional para reservas, pagos y usuarios
- Cloud Run facilita la ejecución de servicios en un modelo cloud-native
- BigQuery permite análisis, trazabilidad y evidencia histórica con fines operativos y legales

La elección de estos componentes no es arbitraria, sino que responde a la naturaleza del producto: una plataforma de intermediación con transacciones, usuarios distintos, validación de identidad, trazabilidad y cumplimiento.

## 12.5 Conclusión

EspaciGo se fundamenta en una combinación de decisiones de negocio, tecnología y regulación. El marco teórico no solo permite comprender el problema, sino también justificar por qué la solución adopta el enfoque que adopta.

La aportación del marco teórico está en mostrar que la innovación del sistema no reside únicamente en la idea de negocio, sino en la integración coherente de múltiples conocimientos: software, seguridad, comercio digital, privacidad, pagos, contratos y gestión documental.

En este sentido, el marco teórico es la base epistemológica del proyecto: explica, valida y sostiene el diseño de EspaciGo como una solución tecnológica viable, segura y alineada con el contexto real de operación.

## 12.6 Bibliografía consolidada

Se incluye la bibliografía completa desarrollada en cada archivo del marco teórico, consolidando las referencias de los conceptos tratados en SaaS, marketplace, monetización, cloud computing, disponibilidad, pagos, identidad, seguridad, contratos, auditoría, arquitectura y requisitos.
