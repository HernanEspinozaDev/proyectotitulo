# Contexto de ES2PT

## Punto de partida: línea base congelada

El informe final de ES1 y sus anexos son la entrega cerrada que sirve como base para ES2: no se modifican ni regeneran desde ES2. Leer primero el contexto compartido y la línea base congelada antes de investigar.

## Método de investigación

Las preguntas, fuentes, resultados y decisiones de ES2 se registran en [`investigacion/`](investigacion/README.md). Cada investigación debe identificar la afirmación de ES1 que usa como base, indicar sus fuentes y fecha de consulta, y declarar si confirma, amplía, contradice o deja pendiente esa base.

Leer primero [contexto compartido](../contexto/README.md) y las evidencias de ES1 que correspondan al tema. ES1 documenta la formulación del proyecto; no demuestra que el software o las integraciones estén implementados.

## Alcance de esta entrega

ES2 corresponde al desarrollo del proyecto: selección de tecnologías, diseño de arquitectura, KPI/SLA, plan de pruebas y calidad, implementación y ajuste del cronograma. La estructura y los criterios recibidos se organizan en el [plan de trabajo por sección](plan_de_trabajo.md), basado en la plantilla, la guía y la rúbrica de `plantilla/`.

El usuario informó el 23 de septiembre de 2026 que la entrega es el **3 de noviembre** y que todavía no hay funcionalidades implementadas. Se registra **3 de noviembre de 2026** como fecha de ES2 y se trabajará en el producto en paralelo al informe. La procedencia es la comunicación del usuario; no se ha consultado el calendario de AAI.

[[PENDIENTE: acordar alcance de demostración, responsables y capacidad semanal; confirmar hitos formativos y el código académico TIH184/TIHI84.]]

## Avance documental

El [inventario de la base y brechas](investigacion/INV-001_base_y_brechas.md) y la [matriz de trazabilidad](investigacion/matriz_trazabilidad_es2.md) permiten seguir los 17 criterios de la rúbrica. Se inició la [investigación de tecnologías](investigacion/INV-002_tecnologias_y_factibilidad.md), con fuentes verificadas y redacción inicial de 2.1–2.2. Las integraciones tienen [preguntas de verificación abiertas](investigacion/INV-003_integraciones.md).

El JSON ya ordena los archivos de las secciones; referencias e índice de anexos completan la estructura institucional. Los apartados sin desarrollar conservan marcadores de pendiente. El diccionario de datos está configurado como Anexo A ES2, aún por completar. El perfil de Word continúa pendiente de adaptación.

## Cambios respecto de la entrega anterior

Registrar cada cambio con fecha, motivo, evidencia e impacto sobre requisitos o decisiones. Mantener los identificadores existentes; no modificar ES1 para hacerla coincidir con decisiones posteriores.

- 2026-09-23: se separa la capacidad analítica de BigQuery de la garantía de inmutabilidad exigida por RNF-017; fundamento y acciones en INV-002. No se ha seleccionado ni implementado un mecanismo sustituto.
- 2026-09-23: se preparan fases hasta la fecha informada de ES2, sustituyendo para esta entrega la reutilización de las fechas históricas de ES1. Es una propuesta pendiente de acuerdo del equipo y revisión docente.

## Evidencias de implementación

Todavía no registradas en esta entrega. Vincular pruebas, código, resultados o capturas concretas antes de afirmar que una funcionalidad está implementada.
