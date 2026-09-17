# 11. Arquitectura de software, requisitos y metodologías de desarrollo

## 11.1 Concepto teórico: la arquitectura como respuesta a los requisitos

La arquitectura de software define la estructura lógica y técnica de un sistema para cumplir objetivos de funcionalidad, seguridad, mantenibilidad, escalabilidad y evolución. La ingeniería de requisitos, a su vez, permite transformar las necesidades del negocio en especificaciones claras, verificables y rastreables.

En un proyecto digital con distintos actores, reglas de negocio complejas, pagos, identidad, disponibilidad y evidencia legal, la arquitectura no puede diseñarse como una solución abstracta. Debe responder directamente a los requisitos operativos del sistema y a la lógica del negocio que lo sustenta.

## 11.2 Requisitos funcionales y no funcionales

Los requisitos funcionales describen lo que el sistema debe hacer; los no funcionales describen cómo debe comportarse bajo condiciones reales de operación.

Ejemplos de requisitos funcionales en EspaciGo:

- registrar espacios y disponibilidades
- reservar un espacio por fecha y horario
- gestionar pagos y retenciones
- generar un contrato digital
- validar identidad y documentos
- registrar alertas o incidencias

Ejemplos de requisitos no funcionales:

- la API debe responder en tiempos aceptables bajo carga
- el sistema debe mantener integridad en reservas concurrentes
- la información sensible debe estar protegida
- las auditorías deben conservar trazabilidad completa
- la plataforma debe ser mantenible y extensible para nuevos tipos de espacio

La diferencia es clave: los funcionales responden al “qué”, los no funcionales responden al “cómo de bien” debe operar el sistema.

## 11.3 Arquitectura de software en EspaciGo

La arquitectura del proyecto se articula en torno a una lógica modular y orientada a servicios, con roles claramente diferenciados:

- Frontend en Next.js: experiencia de usuario y visualización de la aplicación
- Backend en Go: lógica de negocio, reglas, servicios y coordinación
- PostgreSQL: base de datos transaccional para reservas, usuarios, pagos y estado operativo
- Cloud Run: despliegue de servicios en contenedores para ejecución cloud-native
- BigQuery: almacenamiento analítico y evidencia para auditoría y reporting

Esta estructura permite separar la capa de presentación, la capa de negocio, la capa de persistencia y la capa analítica. La arquitectura no es solo una decisión técnica: es una respuesta a la necesidad de manejar simultáneamente disponibilidad, pago, seguridad, legalidad y trazabilidad.

## 11.4 Requisitos de negocio y trazabilidad

Un sistema de marketplace con múltiples actores no puede basarse solo en funcionalidades aisladas. Debe existir trazabilidad desde:

- el requisito del negocio
- la historia de usuario o caso de uso
- la regla de negocio implementada
- la estructura técnica correspondiente
- la validación funcional y legal

Esto es especialmente relevante en EspaciGo, donde el sistema integra pagos, contratos, disponibilidad, propiedad de espacios e identidad de usuarios. Un cambio en una regla de negocio puede afectar varias capas del sistema; por eso la trazabilidad resulta esencial para evitar errores de coordinación.

## 11.5 Metodologías de desarrollo y su adaptación al proyecto

Un proyecto con alta regulación, más de una categoría de usuario y varios procesos críticos no puede depender solo de una metodología pura. Para EspaciGo, se recomienda una metodología híbrida que combine:

- enfoque iterativo e incremental para desarrollo funcional
- principios de gestión de proyectos PMBOK para alcance, costos, riesgos y planificación
- trazabilidad documental y de requisitos
- validación continua de reglas y entregables

Esto permite desarrollar módulos complejos sin perder rigor en la gestión del proyecto. La parte operativa requiere agilidad, pero la parte contractual, financiera y legal exige disciplina y control.

## 11.6 Decisión de implementación

Se adopta una metodología híbrida para EspaciGo con las siguientes características:

- planificación estratégica por entregas y fases
- desarrollo incremental por módulos: reservas, pagos, contratos, identidad, administración y reportes
- trazabilidad de requisitos desde la especificación hasta la validación
- coordinación entre negocio, desarrollo y validación legal
- control de riesgos para cambios en reglas críticas

La intención es combinar velocidad de entrega con una estructura sólida de gobernanza. En proyectos de este tipo, la rapidez sin trazabilidad puede poner en riesgo tanto la calidad del producto como la seguridad del negocio.

## 11.7 Implicación técnica

Esto exige implementar mecanismos como:

- matriz de trazabilidad de requisitos
- casos de uso y reglas de negocio bien documentados
- validación funcional por módulo
- pruebas para condiciones críticas de reserva, pago y contrato
- separación de responsabilidades entre frontend, backend, base de datos y analítica
- registro de cambios y auditoría de decisiones relevantes

Además, el sistema debe permitir que cada requisito se relacione con su implementación real. Por ejemplo, la regla “no puede existir doble reserva para el mismo horario” debe documentarse, probarse y comprobarse tanto en la lógica del backend como en la persistencia de datos.

### 11.7.1 Matriz de trazabilidad requisito → implementación

| Requisito del negocio | Caso de uso | Componente técnico | Validación esperada |
|---|---|---|---|
| El espacio no puede reservarse dos veces en el mismo horario | Reserva de espacio | Backend + PostgreSQL | Validación de solapamiento y transacción ACID |
| El pago debe confirmarse antes de liberar el espacio | Confirmación de reserva | Backend + pasarela | Estado de pago y retención coherentes |
| El contrato debe estar firmado antes del uso | Aceptación de condiciones | Contrato + firma digital | Documento firmado y asociado a la operación |
| La plataforma debe auditar acciones críticas | Disputa o revisión | BigQuery + logs de eventos | Evidencia histórica y consulta posterior |

## 11.8 Arquitectura y requisitos como base de la calidad

La arquitectura y los requisitos forman una relación de dependencia: la arquitectura debe satisfacer los requisitos, y los requisitos deben mantenerse alineados con la realidad técnica del sistema.

En EspaciGo, esta alineación es particularmente importante porque la plataforma no sirve solo para mostrar información, sino para ejecutar transacciones complejas, garantizar confianza y mantener evidencia de operación. Por eso, la calidad del software no depende solo de la tecnología elegida, sino también de la claridad de los requisitos y de la capacidad de la arquitectura para responder a ellos.

## 11.9 Conclusión

La arquitectura de software y la ingeniería de requisitos son elementos inseparables del diseño de EspaciGo. La plataforma necesita una estructura modular y cloud-native, pero también necesita un marco de trabajo que permita convertir objetivos del negocio en decisiones técnicas verificables.

La combinación entre requisitos bien definidos, metodología híbrida y arquitectura modular es lo que permite a la solución escalar, ser segura y mantener consistencia entre negocio, tecnología y cumplimiento. En este sentido, la arquitectura de EspaciGo no es solo una decisión técnica, sino una estrategia para sostener la operación completa del marketplace.

## 11.10 Fuentes consultadas

- Sommerville, I. (2011). *Software Engineering*.
- Pressman, R. S. (2014). *Software Engineering: A Practitioner’s Approach*.
- PMI. (2021). *PMBOK Guide*.
- IEEE. (1998). *Recommended Practice for Software Requirements Specifications*.
- Martin, R. C. (2017). *Clean Architecture*.
- Google Cloud. (2024). *Cloud-native architecture patterns and application design*.
