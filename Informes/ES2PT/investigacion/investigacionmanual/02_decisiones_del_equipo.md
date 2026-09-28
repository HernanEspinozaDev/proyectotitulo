# 02. Decisiones que debe tomar el equipo

Decisiones internas: nadie más puede tomarlas y no se cierran con más investigación. Cada una tiene consecuencia directa en una sección del informe, así que conviene resolverlas en la reunión y registrar el acuerdo con fecha.

Para cada decisión: **qué se decide**, **opciones sobre la mesa**, **qué pasa si no se decide** y **cómo se registra**.

---

## D-01. Capacidad semanal, responsables y jefatura

- **Qué se decide:** horas por integrante y por semana hasta el 3 de noviembre; responsable por bloque (datos, interfaz, infraestructura, pruebas, presupuesto); cómo rota la jefatura semanal.
- **Opciones:** (a) aceptar el supuesto de trabajo SUP-02/SUP-03 (3 × 12 h/semana durante 6 semanas = 216 h, con 20 % de reserva) y solo nombrar responsables; (b) ajustar las horas y recalcular el cronograma; (c) declarar el alcance de ES2 como no viable con la capacidad real y priorizar bloques.
- **Si no se decide:** el cronograma de la sección 7 sigue con esfuerzo relativo y sin responsables, y no se puede prometer ninguna fecha interna.
- **Se registra:** en `07_cronograma.md` y en `../../supuestos_revision.md` (reemplaza SUP-02/SUP-03). **Bloquea:** VII, KPI, pruebas.

## D-02. Alcance de la demostración del 3 de noviembre

- **Qué se decide:** qué existirá exactamente y qué no.
- **Opción sobre la mesa:** SUP-01 — registro con datos sintéticos, publicación y búsqueda en todas las categorías, consulta de disponibilidad, reserva sin solapamiento, pago y firma **simulados** y una consulta administrativa. Sin dinero real ni credenciales de terceros.
- **Alternativas:** recortar a solo catálogo y búsqueda; o ampliar con pago real si algún proveedor habilita cuentas de prueba.
- **Si no se decide:** los capítulos III, V y VII describen un alcance condicionado, y la demostración no se puede preparar ni ensayar.
- **Se registra:** en `01_introduccion.md`, `03_02_casos_uso.md`, `05_01_pruebas.md` y `07_cronograma.md`.

## D-03. Revisión de los cuatro diagramas BPMN

- **Qué se decide:** conformidad con los cuatro procesos, los once flujos de mensaje (M1–M11) y los cuatro temporizadores (T1–T4); y las condiciones de liberación, reverso y reembolso ante confirmaciones tardías de pago.
- **Si no se decide:** el marcador de 3.1 sigue abierto y las condiciones de reembolso quedan como propuesta del agente, no como acuerdo.
- **Se registra:** acta breve con observaciones resueltas; luego se retira el marcador de `03_01_bpmn.md`.

## D-04. Revisión de las siete vistas de casos de uso

- **Qué se decide:** si la selección y las relaciones de las siete vistas son correctas; si **CU-14, CU-31, CU-47 y CU-51** requieren vista propia; y si la paginación de las figuras del cierre visual es aceptable.
- **Opción sobre la mesa:** SUP-17 — mantener las siete vistas y las justificaciones existentes.
- **Se registra:** acta; retiro del marcador de `03_02_casos_uso.md`.

## D-05. Interfaces entre componentes y conciliación

- **Qué se decide:** conformidad con las interfaces de 3.3, la ejecución de la conciliación cada 15 minutos (SUP-14) y su costo dentro de la provisión.
- **Si no se decide:** la conciliación sigue como propuesta y RNF-028 no se puede declarar cubierto.
- **Se registra:** acta técnica; sostiene el marcador de `03_03_componentes.md`.

## D-06. Decisiones de red y gestión de secretos

- **Qué se decide:** dominio propio (o nombre de prueba), proveedor de red, segmentación, puertos y uso de Secret Manager (SUP-15).
- **Si no se decide:** 3.5 mantiene supuestos y no se puede desplegar nada de forma segura.

## D-07. Mecanismo de inmutabilidad y plazo de retención

- **Qué se decide:** ratificar SUP-13 (Cloud Storage con retención bloqueada + hash por lote) y **fijar el plazo de retención**, que hoy no existe.
- **Advertencia registrada:** el bloqueo es **irreversible**; el plazo no debe fijarse sin la política de conservación de D-08.
- **Si no se decide:** RNF-017 sigue sin mecanismo ratificado y el ensayo no se puede ejecutar.
- **Se registra:** en `03_00_arquitectura.md` y `03_06_infraestructura.md`.

## D-08. Política de conservación y anonimización

- **Qué se decide:** plazos de conservación por tipo de dato, regla de anonimización de hechos financieros cuando un titular ejerce supresión, y tratamiento de los autores automáticos de documentos.
- **Contexto:** la Ley 21.719 entra en vigencia el 01-12-2026; en ES2 es criterio de diseño y la regla concreta sigue sin aprobarse. La verificación está planificada en PT-16.
- **Si no se decide:** el Anexo B mantiene dos marcadores abiertos y no se puede fijar la retención de D-07.

## D-09. Aportes, pacto de socios, propiedad intelectual y poderes

- **Qué se decide:** cuánto aporta cada fundador y cómo; qué se pacta sobre propiedad intelectual y decisiones de gasto; con qué poderes se firmará.
- **Opción sobre la mesa:** SUP-12 — financiamiento ilustrativo de 5.778.891 CLP para el primer año (≈ 1.926.297 por fundador), 3.000 acciones iguales y dos revisores para compromisos de gasto.
- **Importante:** nada de esto constituye la sociedad ni otorga poderes; se acuerda **antes** de los estatutos y no se contrata durante el estudio.

## D-10. Reparto de giros y capital pagable

- **Qué se decide:** ratificar **631200 principal y 731001 complementaria**, y cuánto capital se pagará realmente.
- **Abierto:** si la comisión transaccional queda cubierta por 631200 o exige **682000 u otra actividad**; esa es consulta al contador/SII (ver `03_pendientes_con_terceros.md`, fila 5), no decisión interna.
- **Se registra:** en `02_01_analisis.md` y el Anexo A cuando el contador responda.

## D-11. Metadatos académicos

- **Qué se decide:** **código de asignatura (TIH184 o TIHI84)**, sección, académico guía y fechas formativas.
- **Estado:** la portada mantiene los datos actuales y omite el código a propósito (SUP-18) para no inventar un dato académico.
- **Si no se decide:** no se puede afirmar que la entrega cumple el instrumento.

## D-12. Revisión docente

- **Qué se decide:** cuándo se envía la versión de contenido al docente y quién registra la retroalimentación de los **17 criterios** y del cronograma.
- **Regla:** la revisión docente **solo** se registra con evidencia real recibida.

## D-13. Ratificación técnica

- **Qué se decide:** ratificar la continuidad de Next.js, Go, PostgreSQL/PostGIS, contenedores y Cloud Run, y aceptar que la valoración ponderada es **ilustrativa** (SUP-04/SUP-19), sin declarar superioridad de rendimiento ni de costo.
- **Alternativa real:** cambiar de base exigiría modificar **RNF-038** y justificarlo, cosa que hoy no se propone.

## D-14. Alcance del destaque pagado

- **Qué se decide:** si el destaque pagado entra en ES2 o queda como fase posterior; y si entra, con qué precio, zona, cupos y política de pausas y reembolsos.
- **Opción sobre la mesa:** SUP-10 — fuera de la demostración y con cero ingresos en el flujo hasta medir aceptación y canibalización.
- **Si no se decide:** la segunda fuente de ingresos sigue como propuesta no aprobada y el VAN mantiene cero por publicidad.

## D-15. Zona horaria y ventana de mantención

- **Qué se decide:** fijar **America/Santiago** para los informes operativos y acordar si la mantención se excluye del cálculo de disponibilidad.
- **Opción sobre la mesa:** SUP-16 — contarla como indisponibilidad mientras no exista acuerdo de exclusión, para no obtener 99,9 % excluyendo caídas por decisión unilateral.

## D-16. Herramientas de desarrollo, prueba e integración

- **Qué se decide:** repositorio, flujo de ramas, pruebas automáticas y verificación de privacidad en el flujo de integración (propuesto en el capítulo V) y quién lo administra.
- **Si no se decide:** el capítulo V describe un flujo sin responsable ni evidencia de ejecución.

---

## Resumen para la reunión

| # | Decisión | Bloquea a | Prioridad |
| --- | --- | --- | --- |
| D-01 | Capacidad, responsables y jefatura | VII, KPI, pruebas | **Alta** |
| D-02 | Alcance de la demostración | III, V, VII | **Alta** |
| D-11 | Metadatos académicos | Portada y entrega | **Alta** |
| D-08 | Conservación y anonimización | Anexo B, D-07 | **Alta** |
| D-07 | Inmutabilidad y plazo de retención | 3.0, 3.3, 3.6 | Media |
| D-04 | Vistas de casos de uso | 3.2 | Media |
| D-03 | Diagramas BPMN | 3.1 | Media |
| D-13 | Ratificación técnica | 2.1, 3.0 | Media |
| D-14 | Alcance del destaque | 2.1, Anexo A | Media |
| D-05 | Interfaces y conciliación | 3.3 | Media |
| D-06 | Red y secretos | 3.5 | Media |
| D-15 | Zona horaria y mantención | IV–VI | Baja |
| D-16 | Herramientas y CI | V | Baja |
| D-09 | Aportes, pacto y poderes | Formalización | Fuera del informe |
| D-10 | Giros y capital pagable | Anexo A | Espera al contador |
| D-12 | Revisión docente | Rúbrica | Depende de terceros |
