> **Estado vigente:** aplicación de la propuesta económica en 06_escenario_adoptado; consultar su estado_plan.json y ESCENARIO_ACTIVO.json. Los cortes anteriores de este archivo son historial.

# Plan de preparación de la economía de espaciGo

Fecha de corte 16 de noviembre de 2026.

**Parámetros vigentes:** descuento nominal anual 12 % confirmado por Anita; impuesto académico fijo 27 %; Año 1 en 2027. Este corte sustituye la tasa base del 25 % registrada previamente. La preparación se realiza en este directorio independiente. Los insumos provienen de Anita y se conservan con su identificación y estado. La integración posterior requiere resolver las discrepancias entre sus modelos y actualizar los resultados que dependen de AWS.

## Resultado preparado para revisión

La extracción comprende las 26 hojas de EspaciGo.xlsx, sus 2.081 celdas no vacías, 294 fórmulas y resultados guardados, así como los 219 párrafos y las 17 imágenes del informe. El Word recibido contiene cero tablas nativas. Las imágenes originales quedan como evidencia y se relacionan con las tablas editables del libro.

La propuesta contiene un borrador del Capítulo XIV con el flujo original completo del Año 0 al Año 4 y el flujo reconstruido completo. El Anexo H preparado transcribe las 26 hojas, incluidas las hojas de supuestos, auditoría, escenarios y respaldo. Los cuadros extensos se dividen en partes y conservan filas y columnas de origen.

## Estructura de trabajo

| Directorio o archivo | Contenido |
|---|---|
| 01_extraccion/manifest.json | Huellas SHA-256, inventario de hojas, fórmulas e informe. |
| 01_extraccion/excel | Un JSON, dos CSV (valores y fórmulas) y una transcripción Markdown por hoja, más el libro completo en JSON. |
| 01_extraccion/informe | Transcripción íntegra y ordenada, JSON de párrafos e imágenes originales. |
| 02_contraste | Hallazgos, correspondencia de las 17 imágenes, escenario AWS y parámetros. |
| 03_propuesta | Capítulo XIV y Anexo H editables para revisión. |
| 03_propuesta/build | Vista previa construida con DocSkill. |

## Plan y criterios de cierre

- [x] **E01. Inventariar y extraer íntegramente.** Identificar todas las hojas, celdas, fórmulas, valores guardados, combinaciones, notas y vínculos. Extraer párrafos, imágenes y tablas del informe en su orden. Comprobar los conteos y las huellas de origen.
- [x] **E02. Relacionar imágenes y tablas.** Identificar las 17 figuras del informe y su hoja/rango de origen. Registrar rótulos incorrectos y convertir la información de cada hoja en tablas editables de respaldo.
- [x] **E03. Contrastar modelos y cálculos.** Comparar el informe con FlujoNeto, Modelo reconstruido, Supuestos modelo, Conciliacion costos y Perspectivas fundadores. Recalcular VAN y TIR del flujo original y registrar las inconsistencias que afectan ingresos, OPEX, inversión y recuperación.
- [x] **E04. Preparar la sustitución AWS.** Adoptar para comparación el perfil de USD 26,41 mensuales del repositorio AWS y 972 CLP/USD del libro. Verificar suma y conversión, identificar las celdas afectadas y separar consumo bruto de cobertura por créditos.
- [x] **E05. Preparar la estructura de tesis.** Ubicar mercado, recursos, adquisiciones, flujos completos, indicadores y sensibilidad en XIV. Transcribir todas las hojas en H y relacionarlas con el cuerpo. Preparar una vista previa de revisión.
- [ ] **E06. Conciliar una base única.** Aplicar la tarifa del 3 % más IVA indicada por el propietario. La comisión y el cargo de pasarela se descuentan del importe que recibe quien publica. La comisión se aplica por cada pago procesado. Definir el mix de transacciones y la tarifa efectiva de la pasarela. Adoptar la meta provisional de CLP 200.000 por fundador y evaluar CLP 1.000.000 por persona, con desembolso condicionado a disponibilidad; resolver pasarela, oficina, mantenimiento, inversión y capital de trabajo. El préstamo es una simulación confirmada por el propietario; mantener escenarios con y sin deuda. Usar como punto de partida la estructura parametrizada de Modelo reconstruido y preservar el modelo original como antecedente.
- [ ] **E07. Recalcular el modelo AWS elegido.** Propagar costos AWS y créditos por período, depurar dobles conteos, separar flujo económico y flujo de caja, corregir amortización y calcular el flujo completo. Contrastar resultados con un cálculo independiente y obtener VAN, TIR y recuperación.
- [ ] **E08. Cerrar respaldo y sensibilidad.** Definir escenarios coherentes de demanda y capacidad, verificar cotización regional y consumos previstos, régimen tributario y condiciones financieras. Identificar cada cifra con hoja/celda o evidencia externa, y documentar fecha y alcance.
- [ ] **E09. Integrar la versión económica cerrada.** Reemplazar los bloques económicos reservados con el material de Anita conciliado, mantener su autoría y actualizar XIV, H, síntesis de conclusiones, índices y referencias. Recompilar y verificar Word/PDF y numeración después de incorporar las partes pendientes.

## Reorganización del informe recibido

| Material del informe de Anita | Destino propuesto |
|---|---|
| Introducción y alcance comercial | 14.1 y explicación del escenario dentro de las nueve categorías. |
| Capítulo 1, parámetros macroeconómicos | 14.1 y supuestos explícitos del modelo. Detalle y fuentes en H. |
| Capítulo 2, inversión, mano de obra y equipos | 14.2.1 y tablas de inversión, valorización y depreciación en H. |
| Capítulo 2, capital de trabajo | 14.2 y cálculo dependiente del flujo actualizado. |
| Capítulo 3, alternativas y amortización | 14.2 y 14.3. Respaldo completo de la deuda en H. |
| Capítulo 4, personal, cloud, firma, gastos y respaldo | 14.2.2 y componentes conciliados en H. |
| Capítulo 5, flujo, VAN, TIR y sensibilidad | Flujo completo en 14.3, indicadores en 14.4 y sensibilidad en 14.5. |
| Conclusiones del informe | Síntesis financiera después del recálculo y remisión al cierre general de la tesis. |
| Referencias e imágenes | Referencias verificables y tablas de H; imágenes originales solo como evidencia de extracción. |

## Decisiones propuestas

La estructura parametrizada del libro ofrece una base de trabajo más trazable que los valores pegados en FlujoNeto. Se propone consolidar esa estructura y completar sus parámetros, conservando el flujo original para explicar las diferencias.

El escenario AWS de revisión adopta USD 26,41 mensuales, el cambio de 972 del libro y región us-east-2. Esas decisiones permiten comparar partidas. El costo bruto anual equivale a CLP 308.046,24. Si seis meses están íntegramente cubiertos por créditos vigentes y elegibles, la salida del primer año sería CLP 154.023,12. El calendario de créditos y los costos por volumen se cierran con evidencia.

El flujo original se reproduce desde A29:F45 porque corrige el signo del EBT que aparece invertido en C15. El flujo reconstruido conserva sus casillas pendientes. La presentación de ambos permite revisar la selección del modelo sin atribuir resultados cerrados a los parámetros incompletos.

## Criterio de confirmación

Un parámetro puede adoptarse para evaluar un escenario. Una suma, conversión o indicador puede verificarse mediante recálculo. Un consumo, una tarifa contratada o una condición financiera se confirma con su evidencia. Se mantiene esa distinción para que la redacción final de la tesis sea comprobable.

## Actualización del modelo de ingresos

El propietario indica una comisión del 3 % más IVA. La tarifa pasa a ser común entre los escenarios. El detalle y las preguntas pendientes se registran en 02_contraste/decisiones_modelo_ingresos.md. Los importes del libro y de la vista previa inicial conservan su condición de antecedentes. El recálculo de los escenarios de ingresos se conserva en parametros_ingresos.json.

## Próximo corte

Completar E06 y E07 produce el primer flujo único actualizado a AWS. Hasta ese cierre, el borrador es un documento de comparación y preparación. La tesis principal conserva la versión publicada y sus secciones reservadas.

## Verificación de la preparación

Se comprueban 26 hojas, 2.081 celdas no vacías, 294 fórmulas, 219 párrafos y 17 imágenes. Las huellas SHA-256 confirman que los insumos originales conservan sus bytes. El documento de revisión contiene 81 tablas nativas; el número de páginas se comprueba en cada compilación. La vista previa se construye con DocSkill y se renderiza para revisar tablas, continuidad y presencia de los dos flujos completos. La carpeta de la tesis principal conserva sus archivos publicados.

El propietario mantiene provisionalmente ocho espacios, frecuencia de dos reservas por espacio y ticket de CLP 50.000. La preparación evoluciona hacia un modelo de cobros mensuales por modalidad. La aclaración posterior asigna los cargos a quien publica mediante descuento de su liquidación y fija la comisión por pago procesado. Esta decisión sustituye las selecciones anteriores.

La vista previa se actualiza con la comisión vigente y el modelo mensual por modalidad. Incorpora 80 tablas nativas, conservando los flujos del insumo como antecedentes identificados. El ejemplo de distribución por modalidad es ilustrativo y requiere ratificación.

## Decisiones conciliadas en este corte

- [x] Registrar al publicador como responsable de comisión e IVA y del costo de Mercado Pago mediante descuento.
- [x] Registrar la comisión en cada pago, según el calendario real de cuotas o pago único.
- [x] Identificar el préstamo como simulación, sin atribuir contratación.
- [x] Sustituir la ausencia inicial de monto objetivo por la meta provisional de CLP 200.000 por fundador.
- [x] Calcular tickets necesarios para metas de CLP 200.000 y CLP 1.000.000 por fundador, separando IVA, costos y desembolso.
- [ ] Precisar calendario de revisión de caja y formalización del pago condicionado.
- [ ] Confirmar tarifa de pasarela y mezcla mensual de cobros antes del flujo único.

El corte anterior produce 76 páginas y 78 tablas nativas. Se corrigen encabezados Markdown que se mostraban como texto, anchos de las tablas de flujo, separación de filas entre páginas y continuidad entre rótulos y tablas. El constructor reproducible queda en scripts/build_preview.py. Se verifican los importes de comisión e IVA y la integridad de los originales.

## Actualización de remuneraciones y tickets

El propietario adopta la meta provisional de Anita de CLP 200.000 por integrante, condicionada a disponibilidad para distribuir CLP 600.000 conjuntos. Se propone verificar esa disponibilidad después de obligaciones operativas. Se incorpora CLP 1.000.000 por integrante como objetivo adicional. La sección 14.6 documenta componentes, fórmula, sensibilidad de ticket y brecha de demanda. Los costos parciales AWS sin fundadores son CLP 491.583,02 mensuales. E06 continúa abierto por las partidas excluidas; E07 no se declara cerrado con un umbral parcial.

La vista previa de remuneraciones contiene 79 páginas y 80 tablas nativas. Se comprueban los mínimos enteros en ambos objetivos y cuatro tickets, la suma de componentes desde Base mensual, la integridad de las extracciones y la correspondencia de 14.6 con H.27. Las 69 páginas de transcripción del anexo original son visualmente idénticas al corte anterior, con desplazamiento por las páginas añadidas. Se revisan las páginas modificadas y se conserva la tesis principal sin cambios.

## Formato rector del flujo y usuarios activos

- [x] Registrar la instrucción de conservar el formato de flujo que entrega Anita y solicita la profesora: Año 0 a Año 4, estructura completa de resultados y ajustes de caja; VAN, TIR y recuperación posteriores al flujo.
- [x] Estimar publicadores y arrendatarios activos bajo distintas frecuencias de pago, sin confundirlos con usuarios registrados ni sumar roles como personas únicas.
- [x] Identificar tasas históricas y descartar el 25 % como rentabilidad garantizada o tarifa vigente.
- [ ] Justificar la tasa de descuento del flujo actualizado, diferenciando socios y proyecto; conciliar régimen tributario y cierre de serie anual.

El soporte de esta aclaración se registra en 02_contraste/usuarios_formato_y_tasas.md. Las tablas de tickets complementan el flujo de Anita y no reemplazan su formato. La comparación de cobertura adicional o margen del 25 % queda como explicación metodológica, sin ratificar un nuevo objetivo.

## Aclaración de tasa de evaluación e impuesto

- [x] Registrar el 25 % como tasa anual de descuento académica según la indicación docente comunicada por el propietario; las tasas de 10 % y 12 % quedan como antecedentes y sensibilidad.
- [x] Confirmar presencia de impuesto del 27 % en el flujo original y contrastar su aplicación por régimen y año con SII y ley vigente.
- [x] Definir Pro Pyme General como régimen proyectado, empresa aún no constituida, Año 0 en 2026 y Año 1 en 2027.
- [ ] Conciliar base tributaria y momento de pago por período; verificar acogimiento efectivo al formalizar la empresa.

El 25 % de descuento no se incorpora como recargo de costos ni se usa para fijar artificialmente la TIR. La preparación Word/PDF previa conserva su corte; esta aclaración se incorpora en el próximo cierre del flujo completo respetando el formato de Anita.

## Corte de incorporación tributaria

Se incorporan el régimen proyectado y calendario en 14.3 y H.28 y el descuento académico del 25 % en 14.4. Se preservan las tablas y resultados originales como antecedentes. El formato del flujo de Anita continúa siendo rector. La comisión de intermediación se separa de fondos de terceros e IVA; el impuesto se parametriza por año y régimen, sin atribuir inscripción existente.

La vista previa tributaria contiene 81 páginas y 81 tablas nativas. Se comprueban calendario 2027–2030, estado de empresa proyectada, tasas por año y descuento académico. Las 69 páginas de transcripción fuente conservan identidad visual con el corte anterior. Se revisan las páginas modificadas y el respaldo nuevo H.28; se conservan intactos los insumos recibidos y la tesis principal.

## Ratificación del impuesto del ejercicio

- [x] Conservar 27 % fijo en los cuatro años del cálculo académico, por instrucción docente comunicada por el propietario.
- [x] Sustituir en 14.3, H.28 y parámetros activos la secuencia de tasas legales por el supuesto académico fijo; conservar el contraste anterior como antecedente identificado.
- [x] Mantener separado impuesto académico 27 %, descuento académico 25 % e interés simulado 12 %. Anita utiliza originalmente descuentos del 10 % y 12 %.

El régimen Pro Pyme continúa como proyección y la empresa no se presenta como constituida. El cierre del flujo definitivo conserva sus tareas pendientes; esta ratificación no atribuye un recálculo completo a una serie aún no conciliada.

La vista previa del criterio fijo conserva 81 páginas y 81 tablas nativas. Se comprueba 27 % en los cuatro períodos y correspondencia entre 14.3 y H.28. Las 69 páginas de transcripción original mantienen identidad visual. La revisión del informe y las hojas no identifica una derivación adicional de las tasas de descuento referenciales de Anita; la distinción con la exigencia académica del 25 % queda registrada.

## Decisión vigente de descuento confirmado por Anita

- [x] Registrar 12 % nominal anual como única tasa principal, según confirmación de Anita comunicada por el propietario.
- [x] Sustituir el 25 % principal y retirar el 10 % como alternativa base en parámetros, 14.4, H.28 y README.
- [x] Incorporar justificación metodológica y límites en H.29, sin inventar una derivación empírica de costo de capital.
- [x] Conservar impuesto académico 27 % y formato original Año 0 a Año 4.

El escenario actualizado continúa pendiente de cierre de costos y caja; los indicadores históricos al 12 % no se presentan como resultados del flujo AWS. La justificación documental de la tasa queda resuelta como supuesto metodológico adoptado, mientras la evidencia de mercado para calibrar el costo de capital no se atribuye al material recibido.

La vista previa del descuento ratificado contiene 82 páginas y 81 tablas nativas. Se verifica descuento activo del 12 %, impuesto del 27 % en los cuatro períodos, VAN histórico al 12 % y coherencia entre 14.4, H.28 y H.29. Se revisan las páginas modificadas; las 69 páginas de transcripción fuente conservan identidad visual con el corte previo. La tesis principal permanece sin cambios en esta preparación separada.

## Revisión y correcciones con Sapag 2008

- [x] Verificar libro adjunto, edición, autores y correspondencia de páginas impresas/PDF.
- [x] Comparar 16 criterios con originales, preparación separada y bloques de la tesis publicada.
- [x] Incorporar Sapag como referencia metodológica principal y corregir clasificación del flujo financiado, capital de trabajo, cierre, tasa, indicadores y sensibilidad en XIV propuesto y H.29–H.30.
- [ ] Ejecutar SP04–SP13 del plan Sapag: cerrar entradas comerciales y costos, inversión, caja mensual, capital de trabajo, cierre del horizonte, flujos, indicadores, sensibilidad e integración.

Soportes: 02_contraste/sapag2008_fuente.json, sapag2008_matriz_brechas.md y sapag2008_plan_correcciones.md. Se respetan las decisiones del 12 % y 27 % y el formato de Anita. La revisión documental no se confunde con el cierre numérico del modelo.

El corte Sapag contiene 86 páginas y 82 tablas nativas. Se verifican 16 criterios con referencias impresas/PDF y 13 tareas (3 documentales terminadas y 10 financieras o de integración abiertas), la huella del libro y las decisiones 12 % / 27 %. La revisión visual cubre el cuerpo modificado y H.27–H.30; las 69 páginas de transcripción fuente mantienen identidad visual con el corte anterior. Los insumos originales y la tesis principal conservan sus archivos.

## Primer corte de ejecución financiera del plan Sapag

Se registran equipos existentes sin compra inicial y lanzamiento provisional de CLP 1.200.000. Se generan 48 meses de referencia y dos flujos parciales en el cuerpo, junto con seis perfiles de caja para comparación. El costo mensual parcial se corrige a CLP 514.083,02 por los útiles de oficina omitidos. Los umbrales al ticket de CLP 50.000 son 743 y 2.343 pagos para las dos metas por fundador. La deuda simulada cierra en cero y se demuestra la diferencia del impuesto histórico si se aplica la compensación de pérdidas que describe Anita.

El modelo no convierte costos pendientes en ceros reales ni el déficit persistente en capital de trabajo adicional al Año 0. SP04–SP08 y SP10–SP12 quedan en curso, SP09 y SP13 pendientes. No se marca cierre definitivo de caja, costo de oportunidad, valor terminal o demanda. Se preservan 12 % de descuento, 27 % de impuesto académico y las fuentes originales.

El propietario ratifica marketing operativo separado del lanzamiento y dirección tributaria de CLP 150.000 al año como presupuesto provisional. Esta última suma CLP 12.500 mensuales al costo identificado. El subtotal vigente es CLP 514.083,02 y los umbrales finales de este corte son 743 y 2.343 pagos al ticket de CLP 50.000. Los valores de 735 y 2.335 corresponden al cálculo intermedio antes de esta respuesta.

La vista previa del primer corte ejecutado contiene 93 páginas y 91 tablas nativas. Se comprueban seis perfiles de 48 meses, agregación anual y caja, separación de fondos, deuda a saldo cero, pérdida e impuesto académico, VAN por cálculo independiente y respuesta a cambios de presupuesto. El límite de pago se comprueba con 742 y 743 cobros. Se verifican los originales por SHA-256 y las 69 páginas de transcripción fuente mantienen identidad visual con la versión anterior. Se revisa el cuerpo y los anexos modificados, con números de tabla correlativos y sin cifras partidas entre líneas en los flujos. La preparación continúa separada de la tesis principal.

## Segundo corte de coherencia y sensibilidad Sapag

Se revisa el cuerpo, el anexo, los parámetros, el código generador y las memorias. Se corrige el umbral intermedio de 2.335 que permanecía en el generador y se actualizan las equivalencias de publicadores y arrendatarios al presupuesto vigente. Las Tablas 18–19 son los flujos parciales, y las Tablas 20–21 son los apoyos de costos y cobros; las referencias anteriores se rectifican.

Se distingue el umbral operativo parcial del Año 1 (743 y 2.343 pagos) de los años posteriores y del quiebre de VAN anual parcial (791 y 2.391 pagos constantes). Se incorporan once sensibilidades deterministas, prueba cambiaria limitada al componente USD y contraste del VAN anual frente a importes mensuales prorrateados. El 12 % sigue como base y el 27 % como impuesto académico; no se atribuyen a Sapag como tasas prescritas.

La vista previa actual contiene 96 páginas y 94 tablas nativas. Se revisan visualmente las 13 páginas que cambian; otras 83 páginas mantienen identidad de píxeles con el corte anterior a igual resolución, incluyendo las 69 páginas de transcripción original. La disposición de los dos flujos vigentes permite leer cada tabla completa. Se verifican los originales y la propuesta interna de costos AWS por SHA-256, las fórmulas por métodos independientes, los enteros adyacentes de VAN y la regeneración sin cambios de contenido. Se conserva el contenido fuente de H.1 a H.26.

El plan no está terminado: faltan mezcla comercial respaldada, desglose y oportunidad de recursos, costos completos, liquidaciones/IVA de compras, capital del ciclo, reposiciones y cierre. Se mantiene el material separado de la tesis principal hasta completar la conciliación. SP12 registra el avance calculado; no se declaran cerrados los padres de evaluación integral por tener sensibilidades de un subtotal.

## Tercer corte ejecutado y ratificaciones de preoperación

- [x] Completar déficit acumulado máximo, calendarios de aportes y cobertura de las cuotas de deuda.
- [x] Completar indicadores interpretables, recuperación simple/descontada y escenario de quiebre sin asignaciones de 391 pagos.
- [x] Incorporar capacidad de pago y conclusión delimitada en 14.7–14.8; respaldos H.37–H.39.
- [x] Incluir constitución y trámites en el presupuesto de lanzamiento, sin duplicar ese gasto.
- [x] Clasificar equipos personales compartidos sin compra ni transferencia presumida.
- [x] Interpretar el desarrollo como valorización total preoperativa hacia enero de 2027, sin afirmar pago ni reparto pasado/futuro.
- [x] Evaluar su recuperación por separado en H.40: quiebres parciales de 548, 948 y 2.548 pagos para etapa sin asignaciones y las dos metas.
- [x] Reconstruir y auditar Word/PDF, comprobando cálculos y correspondencia cuerpo/anexo.

La entrega contiene 101 páginas y 101 tablas editables. Las 69 páginas de transcripción del libro conservan identidad visual con el corte anterior. Se inspeccionan las páginas nuevas o modificadas, se corrigen cifras partidas y filas aisladas, y se conserva el formato del flujo de Anita. Los originales no cambian por SHA-256. La preparación sigue separada de la tesis principal.

Se completan los cálculos disponibles y las tres aclaraciones recibidas. El cierre integral aún requiere entradas, no una nueva revisión genérica: mezcla y demanda respaldadas, reparto de esfuerzo pasado/futuro para evaluación incremental, condiciones y costos definitivos de proveedores, ciclo efectivo y valoración de reposiciones/cierre. Los padres SP04–SP13 no se marcan completos contrariando sus criterios. El presupuesto y las simulaciones no se presentan como contratos o demanda verificados.

## Aplicación del escenario académico adoptado

Se adopta la propuesta por instrucción del propietario: dominio de CLP 9990 para 2027, pagos de dominio y dirección tributaria en enero, siete días de cobro de comisión con estrés de treinta, compra de reposición de estrés por CLP 900000 en 2029 y cierre prudente sin venta ni perpetuidad. La liquidación posterior de CxC se descuenta en su fecha propia, sin inventar un quinto año de nueva operación. El presupuesto medio es CLP 514003,02 por mes; el desembolso de enero es distinto.

Se calculan ocho perfiles de 48 meses y cuatro flujos completos visibles en el cuerpo, preservando la secuencia de Anita. Los umbrales promedio costo-volumen se distinguen de los mínimos de VAN y de la activación mensual de asignaciones. Los mínimos de VAN con cierres anuales y liquidación son 392, 793 y 2397 pagos mensuales al ticket de CLP 50000 para las tres metas. El caso de 16 pagos mantiene resultado negativo y no habilita asignaciones.

Los presupuestos y métodos del escenario quedan adoptados; no se atribuyen contratos, pagos observados, entrevistas realizadas ni horas ejecutadas. La simulación académica puede revisarse como resultado delimitado. La integración a la tesis principal y las validaciones reales se mantienen diferenciadas del cálculo terminado. El historial numérico anterior se conserva en 04_modelo_sapag y en 06_escenario_adoptado/historial.

## Cierre de la aplicación y verificación

- [x] A01–A08: adopción, costos, calendario, cobro, reservas, escenarios, indicadores, cuerpo/anexo y auditoría numérica.
- [x] A09: Word/PDF inspeccionados; 96 páginas y 103 tablas nativas. Se conservan las 69 páginas de transcripción fuente con identidad visual y H.1–H.26 sin cambios.
- [x] A10: entrega preparada para commit y publicación en main, con verificación del remoto al finalizar.

La referencia activa es 06_escenario_adoptado. Se conservan los archivos originales; no se altera la tesis principal. Las evidencias de demanda, horas realizadas, cotizaciones y condiciones efectivas continúan identificadas; no se sustituyen por afirmaciones de verificación. El método de simulación está aplicado y auditado, sin declarar viabilidad comercial.

## Edición académica para integración

Se completa la redacción del Capítulo XIV y del Anexo H en 07_texto_para_tesis. El contenido presenta la evaluación como elaboración del equipo de espaciGo, elimina atribuciones personales y notas de transcripción de hojas/celdas, y expresa las decisiones adoptadas como criterios de la proyección. Las 27 tablas poseen numeración, título y nota de elaboración propia. Las fuentes externas mantienen su cita metodológica o bibliográfica.

La entrega editorial contiene 25 páginas y 27 tablas editables. Se comprueban cifras y referencias cuerpo/anexo, se inspeccionan las páginas y se elimina una página final con un solo párrafo. El modelo 06 y sus resultados permanecen idénticos. Las transcripciones de las 26 hojas y el informe original se conservan fuera de la edición publicable; la tesis principal no se modifica todavía.

## Integración autorizada a la tesis principal

El propietario solicita incorporar la evaluación respetando la estructura de la tesis y la plantilla del flujo de caja. Se integran el Capítulo XIV y el Anexo H, con once tablas del cuerpo numeradas 14–24 y dieciséis tablas del anexo. Se mantienen las cuatro alternativas de flujo y sus dieciséis partidas; las cifras coinciden con la edición académica corregida. La bibliografía se centraliza en el Capítulo XVII.

El Canvas, el seguimiento de OE5, las conclusiones y la organización de anexos se actualizan para reflejar la evaluación integrada. El manifiesto, la plantilla institucional y los apartados de Gantt permanecen intactos. El seguimiento y las comprobaciones se registran en tesis_final/context/01_auditorias_y_rubricas/TASK_integracion_economica.md y verificacion_integracion_economica.json.

La integración final queda compilada y revisada: 543 páginas, 237 tablas nativas y 27 tablas económicas. Los flujos completos y las referencias del índice se verifican en el PDF. La entrega principal ya corresponde a tesis_final/build/Tesis_Final_espaciGo.docx y .pdf.
