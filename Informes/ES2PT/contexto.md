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

El [inventario de la base y brechas](investigacion/INV-001_base_y_brechas.md) y la [matriz de trazabilidad](investigacion/matriz_trazabilidad_es2.md) permiten seguir los 17 criterios de la rúbrica. La [investigación de tecnologías](investigacion/INV-002_tecnologias_y_factibilidad.md) sustenta un primer borrador de 2.1–2.2. La [consulta inicial de integraciones](investigacion/INV-003_integraciones.md) identifica fuentes públicas y capacidades aún sin probar. El [registro de modelado](investigacion/INV-004_modelado_y_datos.md) documenta decisiones provisionales de 3.1–3.7. [INV-005](investigacion/INV-005_kpi_sla.md) separa metas heredadas de mediciones todavía inexistentes.

La [revisión normativa INV-006](investigacion/INV-006_calidad_y_normativa.md) fundamenta el borrador 5.2 y [INV-007](investigacion/INV-007_operacion_y_mantencion.md) documenta el diseño inicial de disponibilidad, continuidad y mantención de VI. El JSON ordena las secciones; referencias e índice de anexos completan la estructura institucional. El diccionario de datos (Anexo A) contiene un modelo inicial parcial y una matriz de tratamiento de datos; el Anexo B propone dieciséis pruebas, todas sin ejecutar. La [inspección de plantilla INV-008](investigacion/INV-008_plantilla_word.md) produjo un perfil Word preliminar desactivado hasta completar la revisión visual.

## Cambios respecto de la entrega anterior

Registrar cada cambio con fecha, motivo, evidencia e impacto sobre requisitos o decisiones. Mantener los identificadores existentes; no modificar ES1 para hacerla coincidir con decisiones posteriores.

- 2026-09-23: se separa la capacidad analítica de BigQuery de la garantía de inmutabilidad exigida por RNF-017; fundamento y acciones en INV-002. No se ha seleccionado ni implementado un mecanismo sustituto.
- 2026-09-23: se preparan fases hasta la fecha informada de ES2, sustituyendo para esta entrega la reutilización de las fechas históricas de ES1. Es una propuesta pendiente de acuerdo del equipo y revisión docente.
- 2026-09-23: se propone calendario común de ocupación para reservas y bloqueos, con intervalos semiabiertos. La decisión responde a RQF-111/RQF-112 y necesita DDL y prueba concurrente; ver INV-004.
- 2026-09-23: RNF-038 fija PostgreSQL en ES1. MySQL se conserva solo como alternativa comparativa; cambiar la base exigiría justificar el cambio del requisito en ES2.
- 2026-09-23: se propone medir la ejecución presupuestaria de ES2 como costo real / presupuesto aprobado ≤ 100 %, frente a la meta histórica de igualdad del 100 % de ES1. Falta presupuesto y aprobación del ajuste; ver INV-005.
- 2026-09-23: por decisión del usuario, la Ley 21.719 es criterio de diseño **desde el inicio del desarrollo ES2**, aun con entrada en vigencia diferida al 01-12-2026. La matriz del Anexo A y PT-16 trasladan esa decisión a datos y pruebas. Durante ES2 se revisa también la Ley 19.628 vigente. RNF-026 conserva la meta interna de 72 horas sin atribuirla a un plazo legal verificado; ver INV-006.
- 2026-09-23: se proponen sondeos por servicio, restauración verificable y control de cambios para RNF-009/010; son procedimientos documentales sin despliegue ni ensayo. Ver INV-007.
- 2026-09-23: la inspección OOXML de la plantilla ES2 permitió crear un perfil Word preliminar desactivado y ajustar la portada de los anexos para conservar el título institucional multipartes. Falta el render y la revisión visual; ver INV-008.

## Evidencias de implementación

Todavía no registradas en esta entrega. Vincular pruebas, código, resultados o capturas concretas antes de afirmar que una funcionalidad está implementada.
