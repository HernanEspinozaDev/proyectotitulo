# INV-019 — Integración y control de coherencia del informe ES2

**Actualización posterior (23-09-2026):** las cifras de esta revisión corresponden al escenario histórico con oficina LOF. El equipo eligió después Oficina Express y propuso 631200 principal + 731001 complementaria; 682000 queda como consulta por la comisión. El presupuesto vigente está en [INV-029](INV-029_domicilio_patente_y_dom.md) y el Anexo A: salida del año 1 4.815.743 CLP, VAN de caja −1.791.437 CLP. Se proyecta una sola patente para la SpA en el domicilio.

**Nota de estado posterior:** la aprobación de perfil mencionada en rondas históricas de este registro no aplica a la salida actual, cuyos anexos se renombraron después. El perfil volvió a `aprobado: false`; el [plan de cierre](../plan_cierre_pendientes.md) exige nueva generación y revisión visual al final del contenido.

**Fecha:** 23-09-2026. **Estado:** revisión de investigación documental y actualización del borrador; no constituye aprobación académica, comercial, tributaria ni técnica del producto. ES1 permanece como línea base cerrada. La entrega ES2 informada es el 3 de noviembre de 2026.

## Evidencia incorporada

| Registro | Hallazgo que puede afirmarse | Integración y límite |
| --- | --- | --- |
| [INV-014](INV-014_giro_publicidad.md) | El catálogo SII clasifica 731001 como servicio publicitario afecto a IVA; un oficio sobre publicidad en app es análogo. | Se añadió como **giro candidato** al análisis y Anexo A. No se afirma consulta particular, registro ni régimen definitivo. Comisión, destaque y arriendo del tercero conservan documentos separados. |
| [INV-015](INV-015_captacion_meta.md) | Meta ofrece objetivos, reportes y herramientas de medición; la subasta no tiene tarifa fija por reserva. | Se separa gasto de Meta Ads del ingreso potencial por destaques. Los 357.000 CLP de caja de captación ya presupuestados son un techo supuesto, no una campaña ni otra partida. Las reglas de vivienda descritas por Meta para ciertos países no se extrapolan a Chile. |
| [INV-016](INV-016_metodologia_demanda.md) | SII, ELE-7 y Censo contextualizan mercado/zona, pero no miden reservas de EspaciGo. | Se enlazó un protocolo para **todas** las categorías y modalidades. No se convierten entrevistas, anuncios ni contactos en ventas. El ticket de 100.000 CLP y 0/720/1.800 reservas siguen supuestos. |
| [INV-017](INV-017_tco_nube.md) | Con carga hipotética y SQL HA comunes en Iowa, Cloud Run mínimo 0 cuesta USD 297,01/mes y dos VM E2 USD 393,39/mes. | Se añadió comparación al cuerpo y Anexo A **sin cambiar el VAN**: el piloto presupuestado de USD 192,43/mes usa SQL zonal. Se aclaró que «mínimo 1» deja templado solo uno de dos servicios; «mínimo 2» representa uno por servicio. Precios de Santiago, rendimiento y disponibilidad extrema a extrema no comprobados. |
| [INV-018](INV-018_comparacion_split.md) | Mercado Pago documenta 1:1 y tarifa del procesador descontada primero al vendedor. La API Flow documenta comercios asociados, no una comisión 1:1 al marketplace en la información revisada. TUU consultado describe POS. | Se conserva Mercado Pago como **candidato**, no contrato. No se confunden medio de pago, pasarela, split ni custodia de garantía. La incidencia económica de tarifa supuesta en el Anexo A requiere acuerdo, comprobantes y ensayo. |

## Coherencia del flujo económico

Con la decisión de región del 23-09-2026 y las tarifas de Santiago aplicadas, la salida del primer año es de **4.889.743 CLP**, el VAN de caja de **-1.970.676 CLP**, la TIR de caja de **-11,14 %** y el VAN económico de **-78.741.536 CLP**; son los resultados de `supuestos_bootstrap.json` y `simular_bootstrap.py` con el modelo actualizado. No se han introducido ventas por publicidad ni se ha adoptado la variante HA en el flujo base. El escenario de 27 % de impuesto y 4 % de IPC sigue etiquetado como ejercicio académico; el régimen real de una SpA chilena requiere elección y fecha. La comisión propia no incluye ingresos del arriendo de un tercero. El 25 % es meta de margen sobre ingreso propio y no se declaró conseguido.

## Decisión de región y su efecto (23-09-2026)

| Aspecto | Decisión registrada | Evidencia y límite |
| --- | --- | --- |
| Región de operación | **Santiago (`southamerica-west1`)**, por decisión del usuario | Tarifas publicadas compiladas en INV-021; no son factura ni contrato |
| Tratamiento de la provisión del 35 % | Eliminada: las partidas con tarifa publicada se expresan en precios de Santiago | El presupuesto del Anexo A y `supuestos_bootstrap.json` se recalcularon con el simulador del repositorio |
| Efecto en el piloto | Baja de USD 259,78 netos (Iowa con provisión) a **USD 237,82** | La provisión se aplicaba también a partidas sin alza regional, por lo que era más cara que la tarifa publicada |
| Efecto en el flujo | Salida del año 1 de 5.052.056 a **4.889.743 CLP**; VAN de caja de -2.448.407 a **-1.970.676 CLP**; TIR de -16,04 % a **-11,14 %** | Resultado aritmético del cambio de tarifas, no una mejora de capacidad ni una medición |
| Comparación de INV-017 | Conserva precios de Iowa como control documental entre Cloud Run y máquinas virtuales | No es el presupuesto vigente y no se reescribe |
| Pendientes que permanecen | IVA y crédito fiscal sin comprobantes; bolsas de registros, compilación, secretos, correo y staging sin cotizar; inventario físico y pruebas de carga y restauración | Ninguna tarifa se convierte en costo incurrido por este cambio |

## Brechas que aún impiden cerrar II y el Anexo A

1. Medir demanda, precio final, duración, capacidad, cancelaciones y comisión aceptada por modalidad y zona; levantar respuestas de personas reales con consentimiento.
2. Cotizar y probar split, tarifa y reparto por RUT, reembolso, contracargo, garantía y DTE; confirmar los giros y documentos con contador/SII. Una comparación documental no reemplaza esas tareas.
3. Elegir región y perfil de infraestructura, obtener SKU/cotización aplicables y medir carga, failover y costos operativos antes de actualizar el simulador y el VAN.
4. Definir con el equipo si se implementarán destaques en ES2 o fase futura; comprobar tráfico y capacidad de posiciones antes de vender exposición. Ejecutar una campaña Meta solo con presupuesto aprobado y medición preparada.
5. Completar comparaciones tecnológicas, recursos y evidencia de implementación. Word y APA visual continúan al cierre del contenido. Se detectó una aprobación prematura de `perfil_es2.json`; tras esta revisión volvió a `aprobado: false`, pues la rotación de anexos dejó obsoleta aquella salida.

El tablero y la bitácora en `../coordinacion/` registran qué agente produjo cada investigación y su estado. La revisión anterior deja disponibles los registros para una siguiente IA sin presentar las cinco tareas documentales como validaciones empíricas.

## Ronda de integración del capítulo III y cierre de coherencia (23-09-2026)

| Cambio integrado | Evidencia | Límite que se conserva |
| --- | --- | --- |
| Capítulo III completado: siete vistas de casos de uso con 41 de los 52 casos y los once restantes justificados; BPMN de colaboración con once mensajes (M1–M11), la reentrada R1 y cuatro temporizadores (T1–T4); modelo de 17 entidades y 137 atributos con estados, permisos, registro de solicitudes de titulares y DDL propuesto | Secciones 3.1 a 3.7 y Anexo B | El diseño no ha sido validado por el equipo, el DDL no se aplicó en ningún servidor y los ensayos MD-01 a MD-12 no se ejecutaron |
| Capítulo IV: método de medición de once KPI y cinco SLA, con ventana, entradas, exclusiones y evidencia; la fuente y el umbral de disponibilidad provienen de 6.1 e INV-023 | Secciones 4.1 y 4.2 | El registro de mediciones está vacío y no hay responsables asignados |
| Capítulo VII: siete hitos con evidencia de cierre, dependencias, esfuerzo relativo, seguimiento y seis riesgos; se documentó la diferencia de incrementos de ES1 con su evidencia textual | Sección 7.1 | Capacidad semanal, hitos formativos y revisión docente siguen pendientes |
| Anexo A: se agregó inicialmente el escenario de Santiago de INV-021 —cálculo corregido a USD 384,23 al mes frente a USD 297,01 en Iowa, razón cercana a 1,29— como referencia preliminar | INV-021; Anexo A | Esta fila registra el estado inicial de integración: posteriormente Santiago se aplicó al presupuesto, se retiró la provisión del 35 % y se recalcularon flujo, VAN y TIR; faltan auditoría SKU y cotización contractual |
| Matriz de trazabilidad: filas 2.1.2.3 a 2.1.2.8, 2.1.3.9, 2.1.3.10 y 2.1.6.16–2.1.6.17 actualizadas al estado real; el modelo pasa de 16 entidades y 123 atributos a 17 y 137 | Matriz y Anexo B | Las filas siguen sin revisión docente y varias dependen de acuerdos del equipo |
| Registros: INV-024 indexa la investigación con su pregunta, hallazgo y límite, e INV-025 contrasta la guía con la rúbrica | INV-024 e INV-025 | El contraste con el instrumento oficial EA4 y el calendario académico sigue pendiente |
| Sin claves bibliográficas nuevas: las secciones incorporadas citan fuentes ya presentes en `referencias.bib` | `validar ES2PT` sin citas sin fuente | La verificación APA 7 del documento final permanece diferida |
| Perfil institucional: una revisión anterior lo dejó en `aprobado: true` antes de la rotación de anexos | Inspección del archivo; instrucción del usuario y AGENTS.md | Corregido a `aprobado: false`; la salida actual requiere generación y revisión visual cuando cierre el contenido |

Ninguno de estos cambios convierte una hipótesis en hecho: el DDL es texto no aplicado, las mediciones no existen, la cotización de Santiago es una tarifa y no un contrato, y la validación docente no tiene evidencia. `pendientes.md` se actualizó para marcar solo lo que sí está documentado y dejar abierto el resto.

## Convención de citas del informe (23-09-2026)

| Regla | Motivo | Verificación |
| --- | --- | --- |
| El informe cita **solo fuentes primarias**: documentación de proveedores, normas, leyes, precios publicados y estudios de mercado | Los registros `INV-*.md` son material de trabajo interno, no una publicación citable; las fuentes que los sustentan sí lo son | Se eliminaron 95 menciones a registros internos en 19 archivos y se sustituyeron por las fuentes que los respaldan o por referencias a las propias secciones |
| No se autocita la **línea base ES1** (informe ni anexos) como fuente con autor y año | Evita atribuir a la entrega anterior hechos que provienen de terceros y evita la cita del propio equipo a su trabajo previo; el material anterior se menciona en prosa («la entrega anterior», «el catálogo de ES1») | Se retiraron las cinco claves `es1*` de todas las citas y la lista de referencias pasó de 82 a 78 entradas en el informe |
| Los identificadores de requisitos, casos de uso y módulos se conservan como códigos, no como citas | `RNF-###`, `CU-##`, `HU##` y `M01–M11` son trazabilidad, no fuentes | Sin cambios |
| En el Word final no debe aparecer ninguna mención a un registro interno ni una autocita | Es una condición verificable del entregable | Comprobado sobre el render: 0 menciones `INV-0xx` y 0 citas «Espinoza et al., 2026» en el informe (84 páginas) y en el Anexo A (22 páginas) |

## Ronda de revisión bibliográfica y de anexos (23-09-2026)

| Comprobación | Resultado verificado | Límite que se conserva |
| --- | --- | --- |
| Entradas del `.bib` frente a las citas | 115 entradas y 90 claves distintas citadas; **ninguna cita sin entrada** | La comprobación es textual sobre los archivos Markdown, no sobre el Word final |
| Completitud de las fuentes citadas | Ninguna entrada citada carece de los campos obligatorios de su tipo y la auditoría del repositorio no reporta fuentes incompletas ni con datos por verificar | La verificación visual de APA 7 en Word sigue diferida al cierre del contenido |
| Fechas de las fuentes citadas | 63 de las 90 fuentes citadas usan `urldate` con la fecha de consulta y no declaran año | Verificado en el render de [INV-020](INV-020_revision_word_final.md): el estilo emite **«s. f.»** y la lista cumple APA 7, por lo que no es un defecto |
| Entradas sin cita vigente | 25, todas heredadas de ES1 o de uso potencial; no aparecen en la lista de referencias, que se genera desde las citas | Se conservan: retirarlas podría eliminar el respaldo de contenido que aún no cita en el borrador |
| Ejemplos ajenos de la plantilla | No se encontraron claves ni campos de ejemplo en el archivo | — |
| Anexos citados y sintetizados | Cada anexo se cita en al menos una sección y los tres están declarados en `informe.json` | — |
| **Orden de primera referencia de los anexos** | En la ronda original, las letras seguían C, A y B según la primera mención | Resuelto después con rotación: A económico, B datos, C pruebas; el Word anterior no demuestra el resultado nuevo |

La rotación se ejecutó en Markdown y configuración antes de cerrar el contenido: el informe nombra primero el Anexo A económico, luego el B de datos y después el C de pruebas. La generación institucional y su comprobación visual permanecen en la última fase del [plan de cierre](../plan_cierre_pendientes.md).
