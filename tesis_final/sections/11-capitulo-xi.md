# CAPÍTULO XI: Implementación de los KPI y SLA

## 11. Implementación de los KPI y SLA

### 11.1. Descripción de KPI

- **Tasa de conversión de contratación.** Divide el número de recorridos que terminan en reserva confirmada por el total de recorridos iniciados en el período y multiplica por 100. El historial de solicitudes y reservas vincula cada inicio con su desenlace mediante el identificador del recorrido. El registro fija un plazo de seguimiento común para la cohorte.
- **Tiempo mediano de coordinación.** Calcula la mediana de los minutos transcurridos entre el registro de la solicitud y el registro del acuerdo sobre horario y precio. El historial de contratación aporta las marcas de tiempo de las solicitudes iniciadas en el período que alcanzan un acuerdo dentro del plazo de seguimiento.
- **Incidencias por cada cien arriendos.** Divide el número de incidencias distintas vinculadas a los arriendos finalizados en el período por el total de esos arriendos y multiplica por 100. Los registros de incidencias y arriendos permiten asociar cada incidencia con su operación y aplicar un plazo de seguimiento común.

Cada medición identifica período, segmento, plazo de seguimiento y corte. Si el denominador es cero o no hay observaciones para calcular la mediana, el indicador se registra como no calculable. El reporte conserva el volumen de observaciones para interpretar el resultado.

### 11.2. Descripción de SLA

La Tabla 3 y el Anexo A establecen los siguientes objetivos técnicos.

- **RNF-001. Búsqueda.** Respuesta en hasta 2 segundos con 200 usuarios concurrentes, medida desde la confirmación de los parámetros. PT-09 define el ensayo de extremo a extremo. El ensayo SQL del Capítulo XII caracteriza una consulta aislada.
- **RNF-002. Acreditación de renta.** Procesamiento interno en hasta 8 segundos, excluido el tiempo de respuesta del proveedor. La comprobación requiere un registro de tiempos que separe ambos tramos.
- **RNF-009. Disponibilidad.** Disponibilidad mensual mínima de 99,9 % para autenticación, búsqueda y reservas. Su comprobación requiere un registro de disponibilidad de esas funciones en la ventana mensual y el entorno evaluado.
- **RNF-010. Recuperación.** RPO máximo de 15 minutos y RTO máximo de 1 hora en el entorno objetivo. PT-11 contrasta los tiempos, el estado recuperado y los permisos conforme al procedimiento del Capítulo XIII.

El Anexo F identifica las mediciones pendientes. Los resultados locales acreditan únicamente el escenario y la versión registrados en el Capítulo XII.

### 11.3. Control por incremento

El enfoque híbrido del Capítulo VI vincula los entregables de la EDT con incrementos verificables. Cada revisión registra alcance, versión, entorno, evidencia y decisión de cierre. La Tabla 11 utiliza esos antecedentes para distinguir por objetivo el diseño documentado, la ejecución de pruebas y la conformidad observada. El Anexo G.7 define el registro por actividad: fecha de estado, esfuerzo real y restante, versión, entorno, revisión y fecha prevista. Los hitos M01–M05 de la programación son compuertas y no porcentajes de avance observados. El indicador de desempeño del cronograma y los indicadores de costo se informan como no calculables hasta contar con línea base y mediciones reales comparables. El Capítulo XV conserva los ajustes del programa de referencia.

### 11.4. Control de decisiones y configuración

El ADR del 4 de noviembre de 2026 fija la línea base de titularidad, contratación y cobros. La matriz de cierre LOCAL-1 documenta la aceptación del alcance sintético. La evidencia documental F5/F6 registra un corte posterior y distingue el cierre técnico local del recorrido sintético de la aceptación visual y la integración productiva. Los cambios se identifican por commit y las diferencias del esquema por migración y entorno.

### 11.5. Registro de cobertura

La matriz vincula objetivo, RQF o RNF, historia o caso de uso, contrato técnico, prueba y resultado. El estado de un caso cambia a conforme cuando el resultado observado satisface su criterio en el entorno identificado. El Anexo F documenta las pruebas y sus límites.

**Tabla 11**\
*Control documental por objetivo y evidencia disponible*

| Objetivo | Evidencia o entregable de referencia | Estado del corte |
|---|---|---|
| OE1 | Diagnóstico y Tabla 2. Catálogos y fichas de los anexos A, B y C. | Diseño objetivo documentado. La evaluación de mercado y la comprobación por categoría requieren evidencia propia. |
| OE2 | Vistas de arquitectura y modelo lógico de VII, VIII y X. Correspondencia física en Tabla D.1. | Diseño documentado. PT-02 aporta evidencia local de exclusión temporal para el corte ensayado. |
| OE3 | LOCAL-1, F5/F6 y contrato del Anexo E. | Evidencia de ensayo local según el alcance de cada perfil del Capítulo XII. |
| OE4 | Tablas 3 y 12 y pruebas de las tablas F.1 y F.2. | Evidencia parcial en F.3. Carga de extremo a extremo y recuperación conjunta pendientes. |
| OE5 | Capítulo XIII y Tabla 13. Capítulo XIV, Tablas 14–24 y Anexo H. | Evaluación económica integrada: VAN base negativo al 12 % con 16 pagos mensuales. Se calculan aportes, sensibilidad y metas de volumen. |

*Nota.* Elaboración propia a partir de los entregables y evidencias de la memoria.

### 11.6. Criterio de actualización

Cada incremento registra su relación con la EDT y con los requisitos afectados. Si cambia una regla de producto, la revisión identifica la decisión, las fuentes modificadas y las pruebas que se repiten. Si cambia la implementación, el registro identifica el commit, el entorno y el resultado observado. El cierre de un incremento conserva explícitas las verificaciones pendientes.

La transición a AWS conserva los umbrales del catálogo. La aceptación del destino requiere medir la ruta completa Cloudflare, Next.js, API y RDS e identificar región, revisión de tarea y versión de esquema. La emulación local y el ensayo SQL histórico conservan su propio alcance. CloudWatch y el registro de operación aportan las fuentes previstas para disponibilidad y tiempos cuando exista un despliegue verificable.
