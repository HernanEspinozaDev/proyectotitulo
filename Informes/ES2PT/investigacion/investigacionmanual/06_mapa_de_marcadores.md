# 06. Mapa de los 14 marcadores `[[PENDIENTE: ...]]`

Estos marcadores son texto visible en el informe y son lo que bloquea `validar ES2PT --final`. **No se borran por corrección editorial**: cada uno se retira cuando llega la evidencia o cuando el equipo decide y lo registra. Al retirar uno hay que regenerar el Word.

Situación: quedan **14** (11 en secciones, 1 en el Anexo A y 2 en el Anexo B). El 24-09-2026 se cerraron tres decisiones documentales —comparación técnica, fichas de herramientas e inmutabilidad de RNF-017— y se redujeron otros dos a su parte empírica; ver [`INV-033_cierre_borrador.md`](../INV-033_cierre_borrador.md).

| # | Archivo | Qué exige | Origen | Lo cierra | Sección de esta carpeta |
| --- | --- | --- | --- | --- | --- |
| 1 | [`02_01_analisis.md`](../../secciones/02_01_analisis.md) | Sustituir el ticket único y el reparto sintético por precio final, duración, capacidad, ocupación, rechazos y demanda medidos; confirmar giro, régimen, patente, oficina y capital; comparar Cloud Run frente a VM en Santiago con SKU y cotización | Terceros + producto | Trabajo de campo, contador y municipio, y ensayo comparativo | `03` filas 5–7 · `04` P-10 · `05` E-01 a E-03 |
| 2 | [`03_01_bpmn.md`](../../secciones/03_01_bpmn.md) | Revisar los cuatro diagramas con el equipo, validar M1–M11 y T1–T4 con proveedores reales y resolver liberación, reverso y reembolso ante confirmaciones tardías | Equipo + terceros | Acta de revisión y condiciones contractuales | `02` D-03 · `03` fila 1 |
| 3 | [`03_02_casos_uso.md`](../../secciones/03_02_casos_uso.md) | Validar las siete vistas y sus relaciones, decidir si CU-14, CU-31, CU-47 y CU-51 requieren vista propia, enlazar el alcance de demostración y revisar la paginación de las figuras | Equipo | Acta de revisión | `02` D-04 |
| 4 | [`03_03_componentes.md`](../../secciones/03_03_componentes.md) | Validar las interfaces con el equipo y cada proveedor, ensayar la retención bloqueada de RNF-017 y demostrar la portabilidad de RNF-034–036 | Equipo + producto | Acta técnica + pruebas | `02` D-05 · `04` P-07 y P-11 |
| 5 | [`03_04_datos.md`](../../secciones/03_04_datos.md) | Validar el modelo y los catálogos de estados, acordar la política de conservación y anonimización, aplicar el DDL y ejecutar MD-01 a MD-12; completar las entidades fuera del alcance parcial | Equipo + producto | Acta + DDL aplicado + ensayos fechados | `02` D-04 y D-08 · `04` P-01, P-02, P-13, P-14 |
| 6 | [`03_05_comunicaciones.md`](../../secciones/03_05_comunicaciones.md) | Aprobar dominio, proveedor de red, segmentación, puertos y servicio de secretos; validar la autenticación de cada integración y ensayar saldos, reparto, reverso y garantía | Equipo + terceros | Acuerdo + ensayo en entorno autorizado | `02` D-06 · `03` filas 1–2 |
| 7 | [`03_06_infraestructura.md`](../../secciones/03_06_infraestructura.md) | Confirmar los servicios de datos administrados y el inventario físico del equipo, y probar despliegue, escalado, respaldo y recuperación en la región decidida | Producto | Mediciones fechadas | `04` P-01, P-05, P-06, P-08, P-12 |
| 8 | [`03_07_arquitectura.md`](../../secciones/03_07_arquitectura.md) | Validar la secuencia completa con el equipo, reproducir los fallos de la tabla cuando exista producto, demostrar la portabilidad y cerrar el diseño de continuidad con el ensayo de auditoría | Equipo + producto | Acta + reproducción de fallos | `02` D-03 · `04` P-07, P-09, P-11 |
| 9 | [`04_01_kpi.md`](../../secciones/04_01_kpi.md) | Confirmar alcance, fases y presupuesto, designar responsables de medición, habilitar el entorno de carga y llenar el registro de mediciones | Equipo + producto | Registro con resultados fechados | `02` D-01 · `04` P-04, P-06 |
| 10 | [`04_02_sla.md`](../../secciones/04_02_sla.md) | Validar clientes, gestor, autorización, vigencia y ubicación contractual; acordar la exclusión de la ventana de mantención; fijar la zona horaria; ensayar disponibilidad, tiempos, capacidad, respaldos y recuperación | Equipo + producto | Acuerdo de servicio + mediciones | `02` D-15 · `04` P-04, P-05, P-08 |
| 11 | [`07_cronograma.md`](../../secciones/07_cronograma.md) | Confirmar la capacidad semanal y los responsables, acordar el alcance de demostración, incorporar los hitos formativos cuando exista calendario y registrar la revisión docente solo con evidencia | Equipo + docente | Acuerdo registrado + retroalimentación real | `02` D-01, D-02, D-11, D-12 |
| 12 | [`anexos/A_evaluacion_economica.md`](../../anexos/A_evaluacion_economica.md) | Confirmar giro, régimen y domicilio; cotizar honorarios, aseo, Split, firmas e identidad y el crédito de IVA; acordar aportes, pacto y horas; sustituir el escenario segmentado sintético por mediciones; validar impuestos; inventariar activos y costo de subsistencia | Terceros + equipo | Cotizaciones, contratos y mediciones | `03` filas 1–6 · `05` completo |
| 13 | [`anexos/B_diccionario_datos.md`](../../anexos/B_diccionario_datos.md) | Completar perfil y cuenta bancaria, sesiones y tokens, tarifas y catálogos, mensajería, reseñas, detalle tributario y notificaciones; revisar el tratamiento de los autores automáticos de documentos | Equipo + producto | Diccionario ampliado sin afirmar cobertura total | `04` P-14 |
| 14 | [`anexos/B_diccionario_datos.md`](../../anexos/B_diccionario_datos.md) | Mapear los literales de estado de ES1 a los propuestos y acordarlos, validar cardinalidades, aplicar el DDL y ejecutar MD-01 a MD-12 | Equipo + producto | Tabla de correspondencia + ensayos | `02` D-04 · `04` P-01, P-02, P-13 |

## Cómo se retira un marcador

1. Llega la evidencia y se registra (en un `INV-0xx` o en `../../supuestos_revision.md`).
2. Se reescribe el párrafo afectado con el dato confirmado y **sin** afirmar más de lo que la evidencia permite.
3. Se elimina el bloque `[[PENDIENTE: ...]]` completo.
4. Se regenera y valida: `generar` → `actualizar-word` → `validar`.
5. Se actualiza `06_mapa_de_marcadores.md` (esta tabla) y el conteo en [`pendientes.md`](../../pendientes.md).

## Advertencia

Un marcador que dependa de terceros, del equipo o de pruebas no ejecutadas **se conserva**. Borrarlo para que `validar --final` pase sería declarar como resuelto algo que no lo está, y ese es justamente el riesgo que el informe debe evitar.
