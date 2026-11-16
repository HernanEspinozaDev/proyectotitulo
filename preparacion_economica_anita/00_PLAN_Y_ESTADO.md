# Plan de preparación de la economía de espaciGo

Fecha de corte 16 de noviembre de 2026. La preparación se realiza en este directorio independiente. Los insumos provienen de Anita y se conservan con su identificación y estado. La integración posterior requiere resolver las discrepancias entre sus modelos y actualizar los resultados que dependen de AWS.

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
- [ ] **E06. Conciliar una base única.** Aplicar la tarifa del 3 % más IVA indicada por el propietario. Se asignan la comisión y el cargo de pasarela a quien reserva. Definir el calendario de cobro de los arriendos mensuales, el mix de transacciones y la tarifa efectiva de la pasarela. Resolver remuneración (400 mil o 200 mil por fundador), pasarela, oficina, mantenimiento, inversión, crédito y capital de trabajo. Usar como punto de partida la estructura parametrizada de Modelo reconstruido y preservar el modelo original como antecedente.
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

Se comprueban 26 hojas, 2.081 celdas no vacías, 294 fórmulas, 219 párrafos y 17 imágenes. Las huellas SHA-256 confirman que los insumos originales conservan sus bytes. El documento de revisión contiene 77 tablas nativas y el PDF tiene 74 páginas. La vista previa se construye con DocSkill y se renderiza para revisar tablas, continuidad y presencia de los dos flujos completos. La carpeta de la tesis principal conserva sus archivos publicados.

El propietario mantiene provisionalmente ocho espacios, frecuencia de dos reservas por espacio y ticket de CLP 50.000. La preparación evoluciona hacia un modelo de cobros mensuales por modalidad. Las selecciones asignan los cargos a quien reserva. Permanecen consultados el calendario de comisión mensual y la aclaración del reparto de fondos.

La vista previa se actualiza con la comisión vigente y el modelo mensual por modalidad. Incorpora 78 tablas nativas, conservando los flujos del insumo como antecedentes identificados. El ejemplo de distribución por modalidad es ilustrativo y requiere ratificación.
