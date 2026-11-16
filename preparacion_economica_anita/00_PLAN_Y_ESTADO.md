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
