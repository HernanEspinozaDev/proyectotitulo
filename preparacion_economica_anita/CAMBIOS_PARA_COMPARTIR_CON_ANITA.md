# Cambios de la evaluación económica integrada en la tesis de espaciGo

**Fecha:** 16 de noviembre de 2026.

**Versión de referencia:** tesis integrada en el commit `0a1bad6`.

**Material de origen:** `EspaciGo.xlsx` y `estudio_financiero_EspaciGo.docx` entregados por Anita.

## 1. Resumen para informar al equipo

El estudio económico de Anita se utiliza como base para incorporar la factibilidad económica en la tesis. Se conserva la estructura de su flujo de caja y se actualizan los datos conforme a las decisiones del proyecto: comisión del 3 % más IVA, infraestructura AWS, equipos existentes y asignaciones a fundadores condicionadas a la disponibilidad de caja.

Además de corregir diferencias entre el informe y los cuadros del libro, se agregan un calendario mensual, alternativas de financiamiento, sensibilidad, necesidades de aportes y memorias de cálculo basadas en Sapag. El contenido se incorpora al **Capítulo XIV y al Anexo H**, con tablas editables y redacción académica del equipo de espaciGo.

Los cambios comprenden **decisiones nuevas del proyecto, conciliaciones de cálculo y ajustes de presentación**. No todos corresponden a errores de la entrega original: parte de la actualización responde al cambio de arquitectura y del modelo de ingresos acordado posteriormente.

## 2. Qué se conserva del trabajo original

- **La estructura del flujo de caja:** ingresos, costos, depreciación, resultado operativo, intereses, resultado antes de impuestos, impuesto, utilidad, ajustes no desembolsables, financiamiento, inversión y amortización.
- **Las columnas Año 0–Año 4:** preparación en 2026 y cuatro años de operación, de 2027 a 2030.
- **La valorización del desarrollo de CLP 6.240.000:** 16 semanas × 20 horas semanales × 3 integrantes = 960 horas, a CLP 6.500 por hora.
- **El presupuesto de preparación y lanzamiento de CLP 1.200.000.**
- **El marketing operativo de CLP 350.000 mensuales**, separado del lanzamiento.
- **Los presupuestos de firma/API, contabilidad y coordinación**, conciliados con el resto de las partidas.
- **El reajuste del 4 % para los presupuestos en pesos**, diferenciándolo del tratamiento del componente AWS.
- **El préstamo como alternativa de evaluación:** CLP 3.720.000, interés anual del 12 % y tres cuotas anuales.
- **El 27 % de impuesto del ejercicio académico** y el **12 % de descuento confirmado por Anita**, distinguiendo ambos conceptos del interés del préstamo.
- **Los archivos originales y sus extracciones:** las 26 hojas del Excel y el contenido del informe se conservan para trazabilidad.

## 3. Comparación de los principales cambios

| Tema | Entrega original o diferencia encontrada | Versión integrada en la tesis | Motivo del cambio |
|---|---|---|---|
| Alcance comercial | El informe se centra principalmente en espacios comerciales y profesionales. | Se describe el alcance de las nueve categorías de espaciGo, incluidos usos personales, industriales, comerciales y habitacionales. | Alinear la evaluación con el alcance vigente del proyecto. |
| Comisión de espaciGo | El informe utiliza 10 %; el modelo reconstruido del libro contiene 14 %. | Comisión neta del **3 % más IVA por cada pago procesado**. | Aplicar la decisión comercial del proyecto y unificar los parámetros. |
| Responsable de los cargos | El flujo original registra la pasarela como costo de la plataforma. | La comisión de espaciGo y el cargo de Mercado Pago se descuentan al **arrendador o publicador**. El cargo de la pasarela no se duplica como gasto propio. | Reflejar quién soporta los costos según el modelo definido. |
| Base de ingresos | El informe proyecta CLP 35.000.000 de ingresos por comisiones en el Año 1, con crecimiento del 10 % anual; otra base del libro utiliza ocho espacios y 192 operaciones anuales. | Se utiliza una sola base: **8 espacios × 2 pagos mensuales × CLP 50.000**. Resulta en 16 pagos y CLP 800.000 transados al mes, con **CLP 24.000 mensuales de comisión neta**. | Evitar combinar ingresos de escenarios comerciales diferentes. |
| Unidad de cálculo | Se utiliza principalmente el número de reservas. | Se utiliza el **pago procesado**: una cuota mensual, un pago diario o un pago anual completo, según la operación. | Aplicar correctamente la comisión cuando un contrato tiene uno o varios pagos. |
| Crecimiento de ventas | El informe incorpora crecimiento anual del 10 %. | El escenario base mantiene constantes pagos y ticket; sus variaciones se evalúan por separado. | Medir el punto de partida sin hacer depender la conclusión de crecimiento automático. |
| Infraestructura | Se utilizan costos de GCP; una base del libro registra CLP 1.800.000 anuales. | Se adopta el presupuesto AWS del piloto Single-AZ: **USD 26,41 mensuales × 972 CLP/USD = CLP 25.670,52 mensuales**, o CLP 308.046,24 anuales. | Incorporar la arquitectura vigente. El importe corresponde al perfil piloto, no a cualquier escala o configuración. |
| Créditos cloud | Su utilización puede confundirse con una reducción permanente del costo. | No se descuentan créditos promocionales del costo operativo recurrente de la proyección. | Separar un beneficio temporal del costo que debe sostener la operación. |
| Dominio | El libro contiene CLP 10.950 anuales. | Se presupuesta **CLP 9.990 anuales** para el primer año, con referencia a NIC Chile. | Actualizar la referencia del dominio. |
| Oficina virtual o dirección tributaria | La periodicidad de CLP 150.000 no resulta uniforme en los antecedentes. | **CLP 150.000 anuales**, pagados en enero. | Aplicar la periodicidad acordada y evitar tratar el importe como gasto mensual. |
| Equipos | El informe ya señala el uso de equipos personales, mientras algunos cuadros incorporan inversión o depreciación. | Se mantiene su valoración de referencia de CLP 2.700.000, pero **sin compra inicial, transferencia patrimonial, depreciación fiscal ni venta de esos bienes en el flujo**. | Hacer coherente el cálculo con el uso personal y compartido de los equipos. |
| Desarrollo valorizado | Los CLP 6.240.000 forman parte de la inversión y del flujo histórico utilizado para los indicadores. | Se conserva la valorización y se evalúa su recuperación por separado; no se registra como pago efectivo del flujo base. | Distinguir trabajo aportado, evaluación económica y desembolso de caja. |
| Lanzamiento | Se presenta un total de CLP 1.200.000. | Se mantiene el total y se desglosa en formalización/asesoría, contenidos, campaña y contingencia. Incluye constitución y trámites. | Explicar su composición y evitar repetir gastos legales o de marketing. |
| Asignaciones a fundadores | El informe utiliza CLP 400.000 por integrante; otros cuadros consideran CLP 200.000. | Meta inicial de **CLP 200.000 por cada uno de los tres integrantes**, con pago conjunto completo o cero según caja propia. Se agrega una meta de CLP 1.000.000 por persona. | Unificar la política acordada y calcular el volumen necesario para financiarla. |
| Capital de trabajo | El balance inicial fija CLP 2.700.000 como cobertura de un mes de operación. | Se calcula la necesidad de aportes a partir del calendario y del déficit acumulado, sin volver a sumar las pérdidas como inversión inicial. | Evitar doble conteo y reflejar cuándo se necesitan recursos. |
| Cobro de la comisión | El flujo anual no desarrolla el rezago mensual de cobro. | Calendario de siete días y escenario de tensión de treinta días, con cuenta por cobrar y liquidación al cierre. | Diferenciar ingreso devengado de dinero cobrado. Son parámetros de evaluación, no acreditación de plazos contractuales. |
| Cierre del horizonte | El informe plantea ampliar el horizonte o incorporar valor terminal para evaluar la rentabilidad posterior. | Se conservan cuatro años de operación, sin venta de activos/software ni perpetuidad; la comisión por cobrar se recupera aparte. | Mantener un cierre explícito sin añadir ingresos futuros únicamente para obtener VAN positivo. |

## 4. Conciliaciones y correcciones de cálculo

### 4.1. Una sola base para ingresos y costos

Se evita mezclar la proyección de CLP 35.000.000 de comisiones del informe con la base de ocho espacios del libro. Todos los flujos integrados utilizan la misma comisión, volumen, ticket y presupuesto operativo antes de modificar la variable de cada escenario.

El costo operativo del primer año queda en **CLP 6.168.036,24**, equivalente a **CLP 514.003,02 mensuales en promedio**. El promedio sirve para calcular umbrales; los pagos de caja siguen su calendario. Por ejemplo, enero concentra dominio y dirección tributaria, por lo que sus pagos operativos ascienden a CLP 660.660,52.

### 4.2. Signos y consistencia entre resultados y caja

Se concilian los bloques duplicados del flujo original, que contenían diferencias de signo y de Año 0. El resultado antes de impuestos se relaciona con el resultado operativo y los intereses. El flujo distingue la utilidad de los movimientos de caja, la entrada del préstamo y el abono de capital.

La depreciación no se conserva automáticamente cuando la proyección no contempla activos propios adquiridos o transferidos. El desarrollo valorizado tampoco se transforma en un desembolso efectivo por aparecer en el balance de inversión.

### 4.3. Deuda hasta saldo cero

Se conserva el principal y la tasa de la alternativa de préstamo. Se ajusta el redondeo de la última cuota para que el total amortizado coincida con CLP 3.720.000 y el saldo final sea cero. El préstamo se presenta como alternativa de evaluación y no como obligación contratada.

### 4.4. Impuesto y pérdidas

Se mantiene el **27 % del ejercicio académico**. Se aplica al resultado positivo después de compensar las pérdidas del modelo, conciliando la explicación del informe con el cálculo. En el escenario base actualizado existen pérdidas durante los cuatro años, por lo que el impuesto proyectado es cero.

El documento distingue ese criterio académico de la determinación tributaria efectiva de la empresa. También separa el IVA de la comisión del ingreso neto disponible de espaciGo.

### 4.5. VAN, TIR y recuperación

Los indicadores se recalculan sobre los nuevos flujos. Se mantiene el **12 % de descuento**, se distinguen las fechas anuales y mensuales y se descuenta la comisión final en su fecha de liquidación.

Se retira la conclusión de recuperación en el Año 2 del modelo anterior, porque no corresponde a los flujos actualizados. El escenario base integrado no recupera la inversión dentro del horizonte evaluado. La TIR se informa numéricamente cuando permite una interpretación financiera útil; no se publica una raíz extrema del escenario base como si acreditara rentabilidad.

## 5. Qué se agrega a la evaluación

| Incorporación | Contenido agregado | Ubicación en la tesis |
|---|---|---|
| Método de evaluación | Aplicación de *Preparación y evaluación de proyectos*, de Sapag Chain y Sapag Chain, quinta edición de 2008. | Capítulo XIV, Anexo H y bibliografía del Capítulo XVII. |
| Cuatro flujos completos | Proyecto sin deuda, alternativa financiada, reposición de equipamiento y cobro de comisión a treinta días. | **Tablas 17–20** del cuerpo. |
| Liquidación final | Recuperación de CLP 5.600 a siete días o CLP 24.000 a treinta días después del corte, según escenario. | Tabla 21 y Anexo H.6. |
| Calendario mensual | Proyección de 48 meses, cobros, pagos, cuentas por cobrar y conciliación con los cuatro años. | Anexo H.6 y memorias de cálculo conservadas en el repositorio. |
| Sensibilidad cuantificada | Once pruebas sobre pagos, ticket, costos, tipo de cambio y descuento; comparación comercial conservadora, base y optimista. | Sección 14.5 y Anexo H.10. |
| Volumen para asignaciones | Pagos necesarios para las metas de CLP 200.000 y CLP 1.000.000 por integrante. | Tabla 23 y Anexos H.1 y H.11. |
| Quiebre del VAN | Número mínimo de pagos para VAN no negativo, con verificación del entero inmediatamente anterior. Incluye una evaluación separada de recuperación del desarrollo valorizado. | Anexo H.11. |
| Liquidez y deuda | Aportes mínimos, reservas internas y cobertura del servicio de deuda con caja propia. | Tabla 24 y Anexo H.12. |
| Recuperación simple y descontada | Distinción entre ambas mediciones y entre las fechas de valoración. | Sección 14.4 y Anexo H.13. |
| Reposición | Compra de estrés de CLP 900.000 en 2029 y reserva de CLP 25.000 durante 36 meses, sin duplicar reserva y gasto. | Tabla 19 y Anexo H.14. |

## 6. Resultados principales de la versión integrada

| Indicador | Resultado |
|---|---:|
| Ticket promedio del escenario base | CLP 50.000 |
| Pagos mensuales de referencia | 16 |
| Monto transado mensual | CLP 800.000 |
| Ingreso neto mensual por comisión | CLP 24.000 |
| Costo operativo mensual promedio del primer año | CLP 514.003,02 |
| Desembolso de lanzamiento en el Año 0 | CLP 1.200.000 |
| VAN base sin deuda al 12 %, con liquidación final | **−CLP 20.053.400,45** |
| Aportes acumulados requeridos por el caso base sin deuda | CLP 26.170.021,53 |
| Asignaciones efectivamente activadas en el caso base | CLP 0 |

Con ticket de CLP 50.000, los volúmenes calculados son:

| Objetivo | Pagos mensuales |
|---|---:|
| Cubrir costo promedio y CLP 200.000 por integrante | 743 |
| Cubrir costo promedio y CLP 1.000.000 por integrante | 2.343 |
| Alcanzar VAN no negativo sin asignaciones | 392 |
| Alcanzar VAN no negativo con CLP 200.000 por integrante presupuestados | 793 |
| Alcanzar VAN no negativo con CLP 1.000.000 por integrante presupuestados | 2.397 |

**Los umbrales operativos y los de VAN no son equivalentes.** Los primeros utilizan costo mensual promedio; los segundos consideran el horizonte completo, inversión, reajustes y descuento. Tampoco representan usuarios únicos ni ventas observadas. Su cálculo mantiene el presupuesto del perfil piloto y no demuestra capacidad para operar a cualquier escala.

El VAN original del informe y el VAN integrado **no deben compararse como si solo hubiera cambiado el costo cloud**. Cambian la comisión, la base comercial, el tratamiento del trabajo valorizado, las asignaciones, los costos y el calendario. La nueva conclusión se explica principalmente por la distancia entre el ingreso del escenario de dieciséis pagos y el gasto recurrente presupuestado.

## 7. Cambios de redacción, formato y ubicación

- Se adapta el informe independiente a la estructura institucional de la tesis: **Capítulo XIV, Factibilidad Económica**, y **Anexo H, memoria de cálculo**.
- Se conservan los nombres de los apartados de la plantilla: estudio de mercado, costos, recursos, adquisiciones, flujo de caja, indicadores y sensibilidad. Los apoyos adicionales se incorporan dentro del mismo capítulo y su anexo.
- Se reemplazan las imágenes de cuadros financieros por **tablas nativas editables en Word**.
- La redacción presenta el estudio como trabajo del **equipo de espaciGo**, sin atribuir cálculos a una integrante dentro del cuerpo académico.
- Las notas utilizan **«Elaboración propia»** y explican el cálculo. Se eliminan del texto publicable las referencias a filas, celdas y transcripciones del Excel.
- Se incorporan **11 tablas económicas en el cuerpo, numeradas 14–24, y 16 en el Anexo H**. Cada flujo completo mantiene 16 partidas y las columnas Año 0–Año 4.
- Las 26 hojas originales permanecen conservadas como respaldo documental; **no se insertan literalmente sus cuadros históricos con GCP, otras comisiones o celdas incompletas en la versión final del anexo**. El Anexo H contiene la información consolidada y vigente.
- Se actualizan el Canvas, el seguimiento del objetivo OE5, las conclusiones y la organización de anexos para que reconozcan la evaluación incorporada.
- Se centraliza la bibliografía en el Capítulo XVII y se actualizan los índices de contenidos y tablas.
- Se mantienen la plantilla institucional y los apartados de planificación Gantt del Capítulo VI y del Anexo G.

## 8. Dónde revisar la integración

La tesis de referencia tiene **543 páginas**. Estos números corresponden al corte integrado indicado al inicio del documento:

| Contenido | Página del archivo PDF | Numeración impresa del informe |
|---|---|---|
| Capítulo XIV completo | 90–101 | 64–75 |
| Flujo sin deuda, Tabla 17 | 94 | 68 |
| Flujo financiado, Tabla 18 | 95 | 69 |
| Flujo con reposición, Tabla 19 | 96 | 70 |
| Flujo con cobro a treinta días, Tabla 20 | 97 | 71 |
| Indicadores, Tabla 22 | 99 | 73 |
| Anexo H y cierre documental | 533–543 | 507–517 |

Archivos principales del repositorio:

- PDF: `tesis_final/build/Tesis_Final_espaciGo.pdf`.
- Word: `tesis_final/build/Tesis_Final_espaciGo.docx`.
- Capítulo editable: `tesis_final/sections/14-capitulo-xiv.md`.
- Anexo editable: `tesis_final/appendices/h-evaluacion-economica-detallada.md`.

La integración verifica la igualdad de las 27 tablas con la edición económica corregida, la conservación de las partidas del flujo, las referencias entre capítulo y anexo y los destinos del índice. Los presupuestos y resultados se presentan como **proyección financiera del proyecto**, sin convertirlos en ingresos reales o contratos ejecutados.
