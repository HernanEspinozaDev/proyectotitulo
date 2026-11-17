# Anexo H propuesto con las tablas del libro aportado

Esta transcripción conserva las 26 hojas del libro y su orden. Cada tabla identifica la hoja y las filas de origen. Los valores de fórmulas corresponden al resultado guardado en el archivo recibido. El registro JSON conserva las fórmulas, celdas y formatos. El signo — representa una celda vacía o una fórmula cuyo resultado guardado está vacío. La separación de columnas conserva el identificador de fila para relacionar las partes.

La versión preparada para integración requiere conciliar los modelos y sustituir la infraestructura histórica por el escenario AWS identificado en el contraste. Las tablas siguientes documentan el insumo recibido.

## H.1. Supuestos modelo

Fila 1. SUPUESTOS DEL MODELO RECONSTRUIDO

Fila 2. Completar solo con evidencia/decisión documentada. Las celdas amarillas requieren validación.

**Tabla H.1.1**
*Supuestos modelo — filas 3 a 30*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 3 | Variable | Valor | Unidad | Estado | Criterio / evidencia necesaria |
| 4 | Reservas pagadas completadas - Año 1 | 192 | reservas/año | HIPÓTESIS BASE | Derivado provisionalmente de 8 espacios promedio × 2 reservas pagadas/espacio/mes × 12. Solo 8 espacios fue confirmado; frecuencia requiere validación. |
| 5 | Crecimiento anual de reservas | 0,00 % | % | HIPÓTESIS TÉCNICA | Sin crecimiento automático de reservas en el año 1; el crecimiento plurianual queda pendiente de plan de captación. |
| 6 | Valor promedio por reserva (sin IVA) | 50.000 | CLP/reserva | DECISIÓN USUARIO | Ticket promedio fijado en $50.000 por reserva para el escenario base; validar con mix de categorías A y B. |
| 7 | Comisión EspaciGo | 14,00 % | % del GMV | HIPÓTESIS BASE | 14% usado como referencia de trabajo por política pública observada de Busho; no es tarifa acordada por EspaciGo. |
| 8 | Tarifa pasarela efectiva | — | % del GMV | PENDIENTE | Validar cotización/contrato y si incluye IVA, antifraude y cuotas. |
| 9 | Crecimiento anual valor reserva | 0,00 % | % | HIPÓTESIS TÉCNICA | Ticket nominal constante en el modelo inicial; no se aplica IPC automáticamente al precio. |
| 10 | IPC / reajuste costos | 4,00 % | % | REFERENCIAL | Se conserva el 4% del archivo original solo como supuesto editable. |
| 11 | Remuneraciones equipo operativo Año 1 | 14.400.000 | CLP/año | POR VALIDAR | La hoja Balance Personal estima $400.000 x 3 x 12; confirmar si se pagará desde Año 1. |
| 12 | Cloud GCP Año 1 | 1.800.000 | CLP/año | POR VALIDAR | Estimación interna de $150.000/mes; reemplazar por calculadora/cotización según arquitectura. |
| 13 | FirmaVirtual/API Año 1 | 600.000 | CLP/año | POR VALIDAR | $50.000/mes en hoja Insumos; confirmar plan y costo por firma/transacción. |
| 14 | Dominio Año 1 | 10.950 | CLP/año | POR VALIDAR | Precio indicado en hoja Insumos; validar renovación. |
| 15 | Marketing Año 1 | 4.200.000 | CLP/año | POR VALIDAR | Presupuesto de $350.000/mes; definir CAC y canales. |
| 16 | Contabilidad Año 1 | 600.000 | CLP/año | POR VALIDAR | Presupuesto de $50.000/mes derivado de hoja consolidada. |
| 17 | Viajes coordinación Año 1 | 180.000 | CLP/año | POR VALIDAR | 15 viajes x $12.000; confirmar necesidad y frecuencia. |
| 18 | Oficina virtual Año 1 | — | CLP/año | PENDIENTE | Se elimina $150.000 porque el archivo no especifica si es mensual o anual. No incorporar hasta confirmar periodicidad. |
| 19 | Respaldo/almacenamiento Año 1 | — | CLP/año | PENDIENTE | Se elimina $80.000 hasta cotizar almacenamiento y validar política de respaldo/retención. |
| 20 | Mantención/licencias Año 1 | — | CLP/año | PENDIENTE | Se elimina $1.200.000 hasta desglosar mantención/licencias y evitar duplicidad con otros servicios. |
| 21 | Otros costos operativos Año 1 | 0 | CLP/año | EDITABLE | Ingresar solo si están identificados y no duplicados. |
| 22 | Depreciación anual Año 1-3 | 780.000 | CLP/año | POR VALIDAR | Recalcular con costos, valores residuales y vidas útiles corregidos. |
| 23 | Inversión inicial en equipos | 2.700.000 | CLP | POR VALIDAR | La hoja Maquinaria totaliza $2.700.000; confirmar compras efectivas. |
| 24 | Gastos de puesta en marcha en efectivo | — | CLP | PENDIENTE | No repetir automáticamente $1.200.000 de marketing/preparación: desglosar y evitar duplicidad. |
| 25 | Capital de trabajo inicial | — | CLP | PENDIENTE | Calcular desde meses de caja y costos reales, no fijar $2,4m/$2,7m sin conciliación. |
| 26 | Monto de deuda recibida Año 0 | 0 | CLP | ESCENARIO | Dejar en cero hasta contar con oferta aprobada; la tasa 12% no es cotización. |
| 27 | Tasa anual deuda | — | % | PENDIENTE | Reemplazar 12% por cotización bancaria con CAE, comisiones, seguros y calendario. |
| 28 | Plazo deuda | 3 | años | ESCENARIO | Mantener 3 años solo como escenario editable. |
| 29 | Tasa impuesto primera categoría | 27,00 % | % | PENDIENTE | Validar régimen tributario aplicable; 27% no debe darse por supuesto. |
| 30 | Caja recuperable al cierre (capital trabajo) | 0 | CLP | ESCENARIO | Se deja en cero hasta definir horizonte y recuperación de capital de trabajo. |

*Nota.* Transcripción de la hoja «Supuestos modelo» de EspaciGo.xlsx, filas 3–30. Se conservan los importes y el alcance del insumo.

**Tabla H.1.2**
*Supuestos modelo — filas 32 a 33*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 32 | Alcance comercial lanzamiento | A como núcleo; B como complemento | Decisión estratégica | CONFIRMADO POR USUARIO | A: espacios comerciales/profesionales temporales. B: espacios de disponibilidad prolongada como oferta complementaria. |
| 33 | Espacios activos promedio Año 1 | 8 | espacios | DECISIÓN USUARIO | Promedio anual, no meta de cierre de año. |

*Nota.* Transcripción de la hoja «Supuestos modelo» de EspaciGo.xlsx, filas 32–33. Se conservan los importes y el alcance del insumo.

## H.2. Escenarios comerciales

Fila 1. ESCENARIOS COMERCIALES – AÑO 1

Fila 2. Solo los parámetros confirmados por el usuario se presentan como decisiones; los demás son hipótesis que requieren validación.

**Tabla H.2.1**
*Escenarios comerciales — filas 3 a 13*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 3 | Variable | Conservador | Base | Optimista | Unidad / fundamento |
| 4 | Espacios activos promedio | 4 | 8 | 15 | espacios; base confirmado por usuario, extremos son hipótesis |
| 5 | Reservas pagadas por espacio/mes | 1 | 2 | 3 | reservas; hipótesis de utilización comercial, no evidencia de demanda |
| 6 | Reservas pagadas año 1 | 48 | 192 | 540 | reservas/año |
| 7 | Ticket promedio | 35.000 | 50.000 | 65.000 | CLP/reserva; base confirmado por usuario, extremos hipótesis |
| 8 | GMV año 1 | 1.680.000 | 9.600.000 | 35.100.000 | CLP; reservas × ticket |
| 9 | Comisión plataforma | 10,00 % | 14,00 % | 18,00 % | % GMV; base 14% es referencia competitiva de Busho, no acuerdo EspaciGo |
| 10 | Ingreso bruto EspaciGo | 168.000 | 1.344.000 | 6.318.000 | CLP; GMV × comisión |
| 11 | Promedio reservas/mes | 4 | 16 | 45 | reservas/mes |
| 12 | GMV mensual promedio | 140.000 | 800.000 | 2.925.000 | CLP/mes |
| 13 | Ingreso bruto mensual promedio | 14.000 | 112.000 | 526.500 | CLP/mes |

*Nota.* Transcripción de la hoja «Escenarios comerciales» de EspaciGo.xlsx, filas 3–13. Se conservan los importes y el alcance del insumo.

Fila 16. Lectura de evidencia

Fila 17. Confirmado: 8 espacios promedio; lanzamiento A núcleo + B complemento; ticket base $50.000.

Fila 18. No confirmado: frecuencia de reservas, tasas de conversión, comisión definitiva, mix A/B y estacionalidad.

Fila 19. Los escenarios conservador y optimista son pruebas de sensibilidad, no pronósticos respaldados por demanda medida.

## H.3. Base mensual

Fila 1. ESCENARIO BASE – DISTRIBUCIÓN MENSUAL AÑO 1

Fila 2. Distribución plana de 16 reservas/mes solo para mostrar el promedio anual; no representa estacionalidad ni una curva de captación validada.

**Tabla H.3.1.1**
*Base mensual — filas 3 a 16, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 3 | Mes | Espacios activos promedio | Reservas/espacio/mes | Reservas completadas | Ticket promedio |
| 4 | Mes 1 | 8 | 2 | 16 | 50.000 |
| 5 | Mes 2 | 8 | 2 | 16 | 50.000 |
| 6 | Mes 3 | 8 | 2 | 16 | 50.000 |
| 7 | Mes 4 | 8 | 2 | 16 | 50.000 |
| 8 | Mes 5 | 8 | 2 | 16 | 50.000 |
| 9 | Mes 6 | 8 | 2 | 16 | 50.000 |
| 10 | Mes 7 | 8 | 2 | 16 | 50.000 |
| 11 | Mes 8 | 8 | 2 | 16 | 50.000 |
| 12 | Mes 9 | 8 | 2 | 16 | 50.000 |
| 13 | Mes 10 | 8 | 2 | 16 | 50.000 |
| 14 | Mes 11 | 8 | 2 | 16 | 50.000 |
| 15 | Mes 12 | 8 | 2 | 16 | 50.000 |
| 16 | TOTAL AÑO 1 | — | — | 192 | — |

*Nota.* Transcripción de la hoja «Base mensual» de EspaciGo.xlsx, filas 3–16. Se conservan los importes y el alcance del insumo.

**Tabla H.3.1.2**
*Base mensual — filas 3 a 16, parte 2*

| Fila Excel | A | F | G | H | I |
|---|---|---|---|---|---|
| 3 | Mes | GMV | Comisión | Ingreso EspaciGo | Costo pasarela |
| 4 | Mes 1 | 800.000 | 14,00 % | 112.000 | — |
| 5 | Mes 2 | 800.000 | 14,00 % | 112.000 | — |
| 6 | Mes 3 | 800.000 | 14,00 % | 112.000 | — |
| 7 | Mes 4 | 800.000 | 14,00 % | 112.000 | — |
| 8 | Mes 5 | 800.000 | 14,00 % | 112.000 | — |
| 9 | Mes 6 | 800.000 | 14,00 % | 112.000 | — |
| 10 | Mes 7 | 800.000 | 14,00 % | 112.000 | — |
| 11 | Mes 8 | 800.000 | 14,00 % | 112.000 | — |
| 12 | Mes 9 | 800.000 | 14,00 % | 112.000 | — |
| 13 | Mes 10 | 800.000 | 14,00 % | 112.000 | — |
| 14 | Mes 11 | 800.000 | 14,00 % | 112.000 | — |
| 15 | Mes 12 | 800.000 | 14,00 % | 112.000 | — |
| 16 | TOTAL AÑO 1 | 9.600.000 | — | 1.344.000 | 0 |

*Nota.* Transcripción de la hoja «Base mensual» de EspaciGo.xlsx, filas 3–16. Se conservan los importes y el alcance del insumo.

**Tabla H.3.1.3**
*Base mensual — filas 3 a 16, parte 3*

| Fila Excel | A | J |
|---|---|---|
| 3 | Mes | Ingreso tras pasarela |
| 4 | Mes 1 | — |
| 5 | Mes 2 | — |
| 6 | Mes 3 | — |
| 7 | Mes 4 | — |
| 8 | Mes 5 | — |
| 9 | Mes 6 | — |
| 10 | Mes 7 | — |
| 11 | Mes 8 | — |
| 12 | Mes 9 | — |
| 13 | Mes 10 | — |
| 14 | Mes 11 | — |
| 15 | Mes 12 | — |
| 16 | TOTAL AÑO 1 | 0 |

*Nota.* Transcripción de la hoja «Base mensual» de EspaciGo.xlsx, filas 3–16. Se conservan los importes y el alcance del insumo.

Fila 18. Costos operativos conocidos (parciales)

**Tabla H.3.2**
*Base mensual — filas 19 a 28*

| Fila Excel | A | B |
|---|---|---|
| 19 | Remuneraciones equipo | 1.200.000 |
| 20 | Cloud GCP | 150.000 |
| 21 | FirmaVirtual/API | 50.000 |
| 22 | Marketing | 350.000 |
| 23 | Contabilidad | 50.000 |
| 24 | Dominio | 912,50 |
| 25 | Viajes coordinación | 15.000 |
| 26 | Subtotal mensual conocido | 1.815.912,50 |
| 27 | Subtotal anual conocido | 21.790.950 |
| 28 | Advertencia | No incluye pasarela (tasa pendiente), oficina virtual, respaldo, mantención/licencias, costos legales/tributarios, gastos de puesta en marcha ni capital de trabajo. No es OPEX total. |

*Nota.* Transcripción de la hoja «Base mensual» de EspaciGo.xlsx, filas 19–28. Se conservan los importes y el alcance del insumo.

## H.4. Modelo reconstruido

Fila 1. MODELO FINANCIERO RECONSTRUIDO – ESPACIGO

Fila 2. Las fórmulas se activan al completar los supuestos amarillos. Celdas vacías = no hay evidencia suficiente para proyectar aún.

**Tabla H.4.1.1**
*Modelo reconstruido — filas 3 a 38, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 3 | Partida | Año 0 | Año 1 | Año 2 | Año 3 |
| 4 | Reservas pagadas completadas | — | 192 | 192 | 192 |
| 5 | Valor promedio por reserva (CLP) | — | 50.000 | 50.000 | 50.000 |
| 6 | GMV (valor bruto transado) | — | 9.600.000 | 9.600.000 | 9.600.000 |
| 7 | Comisión EspaciGo (%) | — | 14,00 % | 14,00 % | 14,00 % |
| 8 | Ingreso bruto de EspaciGo | — | 1.344.000 | 1.344.000 | 1.344.000 |
| 9 | Pasarela (% GMV) | — | — | — | — |
| 10 | Costo pasarela | — | — | — | — |
| 11 | Contribución después de pasarela | — | — | — | — |
| 12 | Remuneraciones equipo operativo | — | 14.400.000 | 14.976.000 | 15.575.040 |
| 13 | Cloud GCP | — | 1.800.000 | 1.872.000 | 1.946.880 |
| 14 | FirmaVirtual/API | — | 600.000 | 624.000 | 648.960 |
| 15 | Dominio | — | 10.950 | 11.388 | 11.843,52 |
| 16 | Marketing | — | 4.200.000 | 4.368.000 | 4.542.720 |
| 17 | Contabilidad | — | 600.000 | 624.000 | 648.960 |
| 18 | Viajes coordinación | — | 180.000 | 187.200 | 194.688 |
| 19 | Oficina virtual | — | — | — | — |
| 20 | Respaldo/almacenamiento | — | — | — | — |
| 21 | Mantención/licencias | — | — | — | — |
| 22 | Otros costos operativos | — | 0 | 0 | 0 |
| 23 | Total OPEX efectivo | — | — | — | — |
| 24 | EBITDA | — | — | — | — |
| 25 | Depreciación | — | — | — | — |
| 26 | EBIT | — | — | — | — |
| 27 | Intereses deuda | — | 0 | 0 | 0 |
| 28 | Resultado antes de impuesto | — | — | — | — |
| 29 | Impuesto estimado | — | — | — | — |
| 30 | Resultado neto | — | — | — | — |
| 31 | (+) Depreciación | — | — | — | — |
| 32 | (-) Abono a capital deuda | — | 0 | 0 | 0 |
| 33 | (+) Préstamo recibido | 0 | 0 | 0 | 0 |
| 34 | (-) Inversión en equipos | -2.700.000 | 0 | 0 | 0 |
| 35 | (-) Gastos puesta en marcha | — | 0 | 0 | 0 |
| 36 | (-) Capital de trabajo inicial | — | 0 | 0 | 0 |
| 37 | (+) Recuperación capital trabajo | — | 0 | 0 | 0 |
| 38 | FLUJO DE CAJA NETO | -2.700.000 | — | — | — |

*Nota.* Transcripción de la hoja «Modelo reconstruido» de EspaciGo.xlsx, filas 3–38. Se conservan los importes y el alcance del insumo.

**Tabla H.4.1.2**
*Modelo reconstruido — filas 3 a 38, parte 2*

| Fila Excel | A | F |
|---|---|---|
| 3 | Partida | Año 4 |
| 4 | Reservas pagadas completadas | 192 |
| 5 | Valor promedio por reserva (CLP) | 50.000 |
| 6 | GMV (valor bruto transado) | 9.600.000 |
| 7 | Comisión EspaciGo (%) | 14,00 % |
| 8 | Ingreso bruto de EspaciGo | 1.344.000 |
| 9 | Pasarela (% GMV) | — |
| 10 | Costo pasarela | — |
| 11 | Contribución después de pasarela | — |
| 12 | Remuneraciones equipo operativo | 16.198.041,60 |
| 13 | Cloud GCP | 2.024.755,20 |
| 14 | FirmaVirtual/API | 674.918,40 |
| 15 | Dominio | 12.317,26 |
| 16 | Marketing | 4.724.428,80 |
| 17 | Contabilidad | 674.918,40 |
| 18 | Viajes coordinación | 202.475,52 |
| 19 | Oficina virtual | — |
| 20 | Respaldo/almacenamiento | — |
| 21 | Mantención/licencias | — |
| 22 | Otros costos operativos | 0 |
| 23 | Total OPEX efectivo | — |
| 24 | EBITDA | — |
| 25 | Depreciación | — |
| 26 | EBIT | — |
| 27 | Intereses deuda | 0 |
| 28 | Resultado antes de impuesto | — |
| 29 | Impuesto estimado | — |
| 30 | Resultado neto | — |
| 31 | (+) Depreciación | — |
| 32 | (-) Abono a capital deuda | 0 |
| 33 | (+) Préstamo recibido | 0 |
| 34 | (-) Inversión en equipos | 0 |
| 35 | (-) Gastos puesta en marcha | 0 |
| 36 | (-) Capital de trabajo inicial | 0 |
| 37 | (+) Recuperación capital trabajo | 0 |
| 38 | FLUJO DE CAJA NETO | — |

*Nota.* Transcripción de la hoja «Modelo reconstruido» de EspaciGo.xlsx, filas 3–38. Se conservan los importes y el alcance del insumo.

## H.5. Conciliacion costos

Fila 1. ESPACIGO \| CONCILIACIÓN PRELIMINAR DE COSTOS

Fila 2. Primera revisión de Costos fijos, Costos y gastos generales, Insumos, Balance personal y Servicio respaldo.

Fila 3. Regla: los importes de hojas originales son antecedentes; no deben sumarse entre sí cuando representan el mismo concepto o un subtotal.

Fila 4. DECISIONES APROBADAS: remuneración de tres fundadores $600.000/mes en escenario principal; mantenimiento y licencias genéricos $1.200.000/año suspendidos ($0 en costo base), sujetos a futuras cotizaciones.

**Tabla H.5.1.1**
*Conciliacion costos — filas 5 a 18, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 5 | Concepto consolidado | Importe anual observado | Hoja/celda de origen | Tratamiento propuesto | Estado |
| 6 | Cloud GCP | 1.800.000 | Costos fijos!C8; Costos y gastos generales!C21; Insumos!F4/F17 | Contabilizar una sola vez. Mantener $1.800.000 como estimación provisional. | Estimado / cotización pendiente |
| 7 | FirmaVirtual / API | 600.000 | Insumos!F5/F18; Costos y gastos generales!C8 (incluido en $720.000) | Contabilizar una sola vez. Separar suscripción fija de cobro por firma/transacción. | Estimado / cotización pendiente |
| 8 | Dominio .cl | 10.950 | Insumos!F6/F19; Costos y gastos generales!C20 ($11.388) | Usar provisionalmente $10.950 en Año 1; aplicar reajuste solo desde el año siguiente si corresponde. | Pendiente de validación |
| 9 | Útiles de oficina | 120.000 | Insumos!F7/F20; incluido en Costos y gastos generales!C8 | Contabilizar una sola vez como $120.000 anuales si se mantiene el presupuesto. | Estimado |
| 10 | Marketing y publicidad | 4.200.000 | Costos fijos!C7; Costos y gastos generales!C10 | Contabilizar una sola vez: $350.000 mensuales / $4.200.000 anuales. | Estimado / presupuesto por justificar |
| 11 | Contabilidad | 600.000 | Costos y gastos generales!C11; Costos fijos!C10 agrupa externos por $1.200.000 | Mantener $600.000 como estimación identificable; no sumar además los $1.200.000 genéricos. | Pendiente de conciliación |
| 12 | Viajes / coordinación | 180.000 | Costos y gastos generales!C9; Base mensual!B25 ($15.000/mes) | Mantener provisionalmente $180.000 anuales, sujeto a justificar frecuencia y costo unitario. | Estimado |
| 13 | Oficina virtual / dirección tributaria | 150.000 | Costos y gastos generales!B6/C6; Supuestos modelo!B18 vacío | No incorporar aún al total base hasta confirmar si $150.000 es mensual o anual. | Pendiente |
| 14 | Respaldo / almacenamiento | 80.000 | Costos y gastos generales!C7; Servicio respaldo!B29 | Suspender los $80.000 anuales como partida separada en el escenario base. La protección actualmente observada utiliza funciones de GCP ya consideradas dentro del presupuesto de infraestructura: backups automáticos diarios de Cloud SQL (7 días), Object Versioning y Soft Delete de Cloud Storage (7 días). Crear una partida adicional solo si se contrata una solución independiente o una ampliación de retención/recuperación. | Suspendido provisionalmente |
| 15 | Mantenimiento y licencias | 1.200.000 | Costos fijos!C9 | Decisión aprobada: suspender los $1.200.000 anuales del escenario base. La tesis (cap. IX, VI y XIII) identifica Go, Next.js, PostgreSQL/PostGIS, OpenAPI, Docker, GitHub o equivalente, Cloud Build y herramientas de pruebas, pero no documenta suscripciones pagadas concretas. Mantener como riesgo futuro las tarifas de servicios cloud y planes comerciales. | Suspendido / aprobado |
| 16 | Remuneración equipo fundador (administración y soporte) | 7.200.000 | Costos fijos!C6 | Reemplazar los $9.600.000 originales por $7.200.000 anuales ($600.000 mensuales para los tres fundadores). Contabilizar una sola vez. | Decisión acordada |
| 17 | Remuneración de fundadores | 0 | Balance personal!E12:E15; Perspectivas fundadores!B7:D7 | Referencia de escenario, no es una partida adicional. La remuneración ya está consolidada en 'Remuneración equipo fundador (administración y soporte)'. | No sumar |
| 18 | Comisión de pasarela | 10.800.000 | Costos y gastos generales!C16:C17 | Retirar del escenario base actual. Recalcular como GMV x tarifa efectiva de pasarela, una vez cotizada. | Incorrecto para el volumen base / tarifa pendiente |

*Nota.* Transcripción de la hoja «Conciliacion costos» de EspaciGo.xlsx, filas 5–18. Se conservan los importes y el alcance del insumo.

**Tabla H.5.1.2**
*Conciliacion costos — filas 5 a 18, parte 2*

| Fila Excel | A | F | G | H |
|---|---|---|---|---|
| 5 | Concepto consolidado | Riesgo detectado | Acción para cerrar | Importe anual a usar ahora |
| 6 | Cloud GCP | Mismo servicio repetido en varias hojas. | Validar arquitectura, consumo y cotización/calculadora; confirmar IVA. | 1.800.000 |
| 7 | FirmaVirtual / API | Incluido en el paquete de insumos de $720.000. | Confirmar plan, número de firmas y cobros variables. | 600.000 |
| 8 | Dominio .cl | Dos importes para el mismo dominio; $11.388 parece incluir 4% en Año 1. | Verificar tarifa vigente y fecha de renovación en NIC Chile. | 10.950 |
| 9 | Útiles de oficina | El monto está incluido dentro de los $720.000 de insumos. | Confirmar si el equipo realmente tendrá este gasto en operación remota. | 120.000 |
| 10 | Marketing y publicidad | Duplicación directa entre hojas. | Desglosar canales, campañas y CAC esperado; confirmar si se desembolsa todo el año. | 4.200.000 |
| 11 | Contabilidad | Puede estar duplicado dentro de 'Otros externos (contabilidad, legal, etc.)'. | Solicitar cotización y desglosar qué cubren los $1.200.000 de externos. | 600.000 |
| 12 | Viajes / coordinación | El libro también menciona 15 viajes x $12.000; validar la base. | Definir número de desplazamientos, costo medio y si son necesarios con operación remota. | 180.000 |
| 13 | Oficina virtual / dirección tributaria | La periodicidad no está clara y el supuesto fue dejado vacío en el modelo reconstruido. | Obtener cotización y confirmar cobertura tributaria/municipal para la actividad. | — |
| 14 | Respaldo / almacenamiento | La hoja original propone un plan de 250 GB por $80.000/año sin identificar proveedor ni servicio contratado. Riesgo de duplicar Cloud SQL backups y funciones de Cloud Storage. Sin embargo, la configuración actual no acredita RPO 15 min / RTO 1 h porque PITR está deshabilitado y falta ensayo de restauración conjunta. | No sumar al OPEX por ahora. Validar con el equipo habilitación/configuración de PITR, política de retención, exportación/recuperación de objetos, prueba conjunta y costos adicionales que aparezcan en Billing. Si se requiere una solución externa, solicitar cotización y definir qué cubre que GCP no cubre. | 0 |
| 15 | Mantenimiento y licencias | La partida global de $100.000 mensuales no está respaldada por contratos, licencias pagadas ni servicios externos identificados. El trabajo de mantenimiento de fundadores ya está presupuestado como remuneración. | Validar plan/licencia por proveedor al pasar a producción; Cloud Build y consumos se revisan dentro de infraestructura, evitando duplicaciones. Si se contrata soporte externo, crear partida nueva con evidencia. | 0 |
| 16 | Remuneración equipo fundador (administración y soporte) | Los $800.000 mensuales originales correspondían al trabajo de los fundadores; no son personal externo adicional. | Vincular esta única partida al escenario de remuneración reducida. Para los otros escenarios usar $0 o $14.400.000, sin sumar una segunda línea de fundadores. | 7.200.000 |
| 17 | Remuneración de fundadores | Evita duplicar los mismos $7.200.000 anuales. | Mantener solo como referencia para alternar escenarios: $0 / $7.200.000 / $14.400.000. El flujo deberá seleccionar un único valor. | 0 |
| 18 | Comisión de pasarela | Se calculó con 3.600 reservas y $3.000 por reserva; no corresponde a 192 reservas. | Obtener tarifa, IVA, costos adicionales, split settlement y liquidación; aplicar a GMV real. | — |

*Nota.* Transcripción de la hoja «Conciliacion costos» de EspaciGo.xlsx, filas 5–18. Se conservan los importes y el alcance del insumo.

Fila 21. CONTROLES PARA EVITAR DOBLE CONTEO

**Tabla H.5.2**
*Conciliacion costos — filas 22 a 29*

| Fila Excel | A | B |
|---|---|---|
| 22 | No sumar subtotales | Costos fijos!C11 ($18.000.000), Costos y gastos generales!C12 ($5.930.000) e Insumos!F8/F21 son subtotales/resúmenes; no agregarlos encima de sus componentes. |
| 23 | Mantenimiento y licencias | Costos fijos!B9/C9 presupone $100.000 mensuales ($1.200.000/año), pero Costos y gastos generales!C25 registra $0 en Herramientas y Licencias. Mantener la partida fuera del costo base hasta contar con desglose y respaldo. |
| 24 | Marketing | Los $4.200.000 aparecen en Costos fijos y Costos y gastos generales: una sola contabilización. |
| 25 | Cloud y dominio | Se repiten entre Costos fijos, Insumos y Costos y gastos generales: una sola contabilización por servicio. |
| 26 | Respaldo | Los $80.000 de Gastos Generales y Servicio Respaldo representan el mismo servicio: una sola contabilización, una vez recalculado. |
| 27 | Remuneraciones | Los $800.000 mensuales originales de Administración y soporte corresponden a los tres fundadores. Se reemplazan por $600.000 mensuales ($7.200.000/año) en el escenario principal. No sumar otra línea de remuneraciones de fundadores. |
| 28 | Depreciación | Los $780.000 anuales son gasto contable no desembolso de caja. Se mantienen separados en resultados y se agregan de vuelta al flujo de caja operativo. |
| 29 | Protección y respaldo GCP | Configuración informada: Cloud SQL con backups automáticos diarios y retención de 7 días; PITR deshabilitado. Cloud Storage con Object Versioning y Soft Delete de 7 días. Estas funciones forman parte de los servicios GCP; no justificar por sí solas una partida externa adicional de $80.000/año. |

*Nota.* Transcripción de la hoja «Conciliacion costos» de EspaciGo.xlsx, filas 22–29. Se conservan los importes y el alcance del insumo.

Fila 31. REVISIÓN DE RESPALDO CON EL ESCENARIO COMERCIAL ACTUAL

**Tabla H.5.3**
*Conciliacion costos — filas 32 a 37*

| Fila Excel | A | B | C | D |
|---|---|---|---|---|
| 32 | Reservas anuales base | 192 | Supuestos modelo!B4 | Confirmado como hipótesis base; frecuencia aún no validada. |
| 33 | GB por reserva | 0,05 | Servicio respaldo!B6 | Supuesto técnico pendiente de medir. |
| 34 | GB de evidencias | 9,60 | Reservas x GB/reserva | Fórmula de control. |
| 35 | Base de datos operativa (GB) | 10 | Servicio respaldo!B12 | Estimación técnica pendiente de validar. |
| 36 | Total estimado Año 1 (GB) | 19,60 | Evidencias + base de datos | Resultado preliminar: 19,6 GB. |
| 37 | Capacidad 100 GB | 50.000 | Servicio respaldo!B19 | Precio estimado no cotizado; validar proveedor y alcance. |

*Nota.* Transcripción de la hoja «Conciliacion costos» de EspaciGo.xlsx, filas 32–37. Se conservan los importes y el alcance del insumo.

## H.6. Auditoria y decisiones

Fila 1. AUDITORÍA DEL ARCHIVO ORIGINAL Y CRITERIOS DE CORRECCIÓN

**Tabla H.6.1**
*Auditoria y decisiones — filas 2 a 17*

| Fila Excel | A | B | C | D |
|---|---|---|---|---|
| 2 | Hallazgo | Riesgo / efecto | Tratamiento aplicado en esta versión | Qué falta para cerrar |
| 3 | Ingresos C8 = $35.000.000 | No existe respaldo ni trazabilidad; además etiqueta GMV y comisión como si fueran lo mismo. | Se elimina como supuesto. Modelo nuevo calcula reservas × ticket promedio × comisión. | Validar reservas/año, ticket medio y comisión. |
| 4 | 3.600 reservas/año | Supuesto de volumen sin evidencia de demanda/operación. | No se incorpora como caso base. | Validar con entrevistas, encuesta y piloto. |
| 5 | Comisión 25% | Una conversación con un proveedor planteó 25% primera reserva; no fue acuerdo general ni tarifa final. | No se fija como tarifa. Se deja input vacío. | Negociación con proveedores y política para clientes recurrentes. |
| 6 | Pasarela $10.800.000 | No se conoce tasa efectiva ni base de cobro; cifra equivale a $3.000 por reserva si se mantienen 3.600 reservas. | Se sustituye por porcentaje editable aplicado al GMV, sin valor precargado. | Cotización vigente y confirmación de IVA, payout, split y contracargos. |
| 7 | OPEX fijo $18.000.000 y gastos generales $5.930.000 | Solapamiento de marketing, cloud, contabilidad, soporte y otros; riesgo de doble conteo. | No se suman ambas tablas. El modelo nuevo usa una sola lista de costos operativos. | Conciliar contratos y presupuestos; desglosar mantención y oficina virtual. |
| 8 | Personal $14.400.000/año | Existe en Balance Personal y en costos generales; no está claro si los $800.000/mes de administración y soporte del OPEX lo incluyen. | Se considera una sola línea editable de remuneraciones; se excluye el OPEX agregado de $18m. | Confirmar pagos reales a fundadores, cotizaciones y modalidad contractual. |
| 9 | Capital de trabajo $2.400.000 vs $2.700.000 | Dos valores incompatibles y bases de cálculo incompletas. | Se deja vacío en supuestos hasta recalcular según meses de caja. | Definir meses de cobertura y costos mensuales conciliados. |
| 10 | Inversión inicial $10.140.000 | Incluye $6.240.000 de trabajo de fundadores como costo de oportunidad; no es necesariamente desembolso de caja ni activo intangible capitalizable. | El flujo nuevo separa equipos, puesta en marcha y capital de trabajo; el costo oportunidad se mantiene solo en hoja original para evaluación económica. | Definir perspectiva económica vs financiera y tratamiento contable del desarrollo. |
| 11 | Deuda $3.720.000 al 12% | No hay oferta bancaria; la tasa y garantía son supuestos no demostrados. | Deuda del caso base queda en cero; tasa/plazo quedan editables. | Obtener cotización con CAE, seguros, comisiones y calendario. |
| 12 | EBT Año 1 con signo incorrecto | EBIT -510.000 menos intereses 446.400 debería ser -956.400, no +956.400. | Hallazgo documentado; hoja original se conserva sin alterar. | La hoja nueva calcula resultado antes de impuestos con fórmula. |
| 13 | Oficina virtual $150.000 | La periodicidad no está indicada; puede ser mensual o anual. | No se incorpora hasta aclarar unidad. | Confirmar proveedor, periodicidad y aceptación del domicilio para actividad real. |
| 14 | Respaldo y retención 5 años | Costo GCP y obligación de retención atribuidos a Ley 21.719 sin demostración suficiente. | No se incorpora al caso base hasta cotizar arquitectura y validar política legal de retención. | Dimensionar almacenamiento, respaldos, logs, contratos y plazos legales. |
| 15 | Depreciación maquinaria | Valor residual en F6 está como texto; depreciación de smartphone no coincide con (300.000-60.000)/3 = 80.000; notebook sí da 700.000. | Modelo conserva 780.000 como cifra provisional editable, marcada por validar. | Corregir formato y respaldar vida útil/valor residual. |
| 16 | IPC 4%, dólar 972 y TPM/tasa deuda | Supuestos macroeconómicos no se deben mezclar: TPM no equivale a tasa comercial; IPC proyectado no es necesariamente IPC observado. | 4% se conserva solo como reajuste editable de costos; tipo de cambio no alimenta este modelo porque cloud se presupuestó directamente en CLP. | Verificar serie oficial y separar dato observado, expectativa y supuesto. |
| 17 | Impuesto 27% | Puede no corresponder al régimen tributario elegido y no contempla arrastre de pérdidas. | Se deja editable y se marca pendiente. | Definir régimen tributario con contador y modelar pérdidas tributarias. |

*Nota.* Transcripción de la hoja «Auditoria y decisiones» de EspaciGo.xlsx, filas 2–17. Se conservan los importes y el alcance del insumo.

Fila 19. REGLAS PARA USAR EL MODELO

Fila 20. 1. No completar celdas amarillas con cifras intuitivas; cada cifra debe tener fuente, entrevista, cotización o decisión explícita.

Fila 21. 2. GMV no es ingreso de EspaciGo. El ingreso de la plataforma es la comisión (salvo otros ingresos debidamente definidos).

Fila 22. 3. La comisión de pasarela debe calcularse sobre la base real que cobre el proveedor de pagos, no asumir que siempre es el GMV.

Fila 23. 4. No incluir simultáneamente los $18m de OPEX y los $5,93m de gastos generales; consolidar cada costo una sola vez.

Fila 24. 5. Este modelo es una estructura de trabajo y no un flujo listo para presentar: faltan supuestos comerciales, deuda, impuestos y validaciones.

**Tabla H.6.2**
*Auditoria y decisiones — filas 25 a 28*

| Fila Excel | A | B | C | D |
|---|---|---|---|---|
| 25 | Escenario base confirmado parcialmente | 8 espacios promedio y ticket de $50.000 definidos; la frecuencia de reservas y comisión aún no están validadas. | Se parametriza un caso base provisional de 192 reservas/año (8 × 2 × 12) y 14% de comisión para sensibilidad. | Validar 2 reservas/espacio/mes y 14% con entrevistas, pruebas comerciales y acuerdos. |
| 26 | Categorías de lanzamiento | La estrategia es A núcleo y B complemento; no hay mix porcentual observado. | Se documenta el alcance, pero no se inventa un porcentaje de reservas A/B. | Medir mix de demanda y GMV por categoría en piloto. |
| 27 | Costos mensuales parciales | Las partidas conocidas suman una base operativa, pero hay conceptos sin periodicidad/cotización. | Se añade subtotal parcial visible en Base mensual; no se declara como costo total. | Completar oficina virtual, almacenamiento, mantenimiento, pasarela, legal/tributario y capital de trabajo. |
| 28 | Oficina virtual, respaldo y mantención sin periodicidad/cotización suficiente | Los valores anteriores podían inflar o distorsionar el OPEX; además existe riesgo de duplicidad. | Se vacían los tres supuestos hasta validar monto, periodicidad y alcance. | Obtener cotizaciones y desglosar servicios antes de cerrar OPEX. |

*Nota.* Transcripción de la hoja «Auditoria y decisiones» de EspaciGo.xlsx, filas 25–28. Se conservan los importes y el alcance del insumo.

## H.7. IPC

**Tabla H.7.1**
*IPC — filas 1 a 7*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | Seccion | Descripcion del parametro | Valor | Unidad | Fuente/Justificacion |
| 2 | MACROECONOMÍA | Año Base de Evaluación | 2.026 | Año | Inicio de operaciones del proyecto. |
| 3 | MACROECONOMÍA | Variación IPC Anual Proyectada | 4.00 | Porcentaje (%) | Meta del Banco Central para proyectar OPEX (Años 1 al 4). |
| 4 | MACROECONOMÍA | Tipo de Cambio USD a CLP | 972 | CLP / USD | Dólar observado para conversión de servicios Cloud. |
| 5 | AJUSTE IPC | Costo Histórico (Ej. Licencias 2020) | 10.000 | CLP Antiguo | Valor referencial base. |
| 6 | AJUSTE IPC | Variación IPC Acumulada 2020-2026 | 45,20 | Porcentaje (%) | Variación acumulada según calculadora INE |
| 7 | AJUSTE IPC | Costo Ajustado a Hoy (2026) | 14.520 | CLP Actualizado | Actualización monetaria para la evaluación inicial. |

*Nota.* Transcripción de la hoja «IPC» de EspaciGo.xlsx, filas 1–7. Se conservan los importes y el alcance del insumo.

**Tabla H.7.2**
*IPC — filas 9 a 10*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 9 | CONVERSION USD | Costo Mensual Cloud (GCP Cloud Run) | 154 | USD | Consumo estimado de la arquitectura base. |
| 10 | CONVERSION USD | Costo Mensual Cloud en CLP | 149.688 | CLP Actualizado | $154  x 972$ (Aproximado a los $150.000 utilizados en el Flujo). |

*Nota.* Transcripción de la hoja «IPC» de EspaciGo.xlsx, filas 9–10. Se conservan los importes y el alcance del insumo.

## H.8. sercicio de distriibucion googl

Fila 2. Servicio de Distribución de Aplicación Móvil por Google PlayStore

**Tabla H.8.1**
*sercicio de distriibucion googl — filas 3 a 5*

| Fila Excel | B | C |
|---|---|---|
| 3 | Detalle | Valor Unitario SIN IVA |
| 4 | Abono de Cuenta de Programador | 25 dólar |
| 5 | Total | 24.183 |

*Nota.* Transcripción de la hoja «sercicio de distriibucion googl» de EspaciGo.xlsx, filas 3–5. Se conservan los importes y el alcance del insumo.

Fila 7. https://www.google.com/search?q=dolar&rlz=1C1YTUH_esCL1155CL1155&oq=dolar&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7Mg0IARAAGIMBGLEDGIAEMg0IAhAAGIMBGLEDGIAEMgoIAxAAGLEDGIAEMg0IBBAAGIMBGLEDGIAEMgcIBRAAGIAEMg0IBhAAGIMBGLEDGIAEMg0IBxAAGIMBGLEDGIAEMg0ICBAAGIMBGLEDGIAEMg0ICRAAGJIDGIAEGIoF0gEIMTEwNGowajeoAgCwAgA&sourceid=chrome&source=chrome.ob&ie=UTF-8

Fila 8. https://support.google.com/googleplay/android-developer/answer/6112435?hl=es&ref_topic=3450769&sjid=17686474820315071286-SA#zippy=%2Cpaso-reg%C3%ADstrate-para-obtener-una-cuenta-de-desarrollador-de-play-console%2Cpaso-acepta-el-acuerdo-de-distribuci%C3%B3n-para-desarrolladores%2Cpaso-paga-la-cuota-de-registro%2Cpaso-elige-un-tipo-de-cuenta-de-desarrollador

## H.9. mano de obra

Fila 2. Balance Mano de Obra (Desarrollo del Software)

**Tabla H.9.1.1**
*mano de obra — filas 3 a 7, parte 1*

| Fila Excel | B | C | D | E | F |
|---|---|---|---|---|---|
| 3 | Cargo | Cantidad | Horas | Tiempo (meses)  | Costo Unitario (Salario Bruto) |
| 4 | Gerencia / Arquitecto Cloud | 1 | 320 | 4 | 520.000 |
| 5 | Gestión de Personas y Análisis / Backend | 1 | 320 | 4 | 520.000 |
| 6 | Desarrollo y Arquitectura / UI-UX | 1 | 320 | 4 | 520.000 |
| 7 | Total | 3 | 960 | — | 1.560.000 |

*Nota.* Transcripción de la hoja «mano de obra» de EspaciGo.xlsx, filas 3–7. Se conservan los importes y el alcance del insumo.

**Tabla H.9.1.2**
*mano de obra — filas 3 a 7, parte 2*

| Fila Excel | B | G |
|---|---|---|
| 3 | Cargo | Costo Total Proyecto (Salario Bruto) |
| 4 | Gerencia / Arquitecto Cloud | 2.080.000 |
| 5 | Gestión de Personas y Análisis / Backend | 2.080.000 |
| 6 | Desarrollo y Arquitectura / UI-UX | 2.080.000 |
| 7 | Total | 6.240.000 |

*Nota.* Transcripción de la hoja «mano de obra» de EspaciGo.xlsx, filas 3–7. Se conservan los importes y el alcance del insumo.

Fila 11. Hernán Espinoza: Gerencia / Arquitecto Cloud.

Fila 13. Erick Silva: Gestión de Personas y Análisis / Backend.

Fila 15. Anita Marchant: Desarrollo y Arquitectura / UI-UX.

Fila 17. En cuanto al plan de recursos, el documento detalla las siguientes métricas para el costo de oportunidad:

Fila 19. Cantidad por cargo: 1 persona por cada rol.

Fila 21. Tiempo del proyecto: 16 semanas (lo que equivale a 4 meses).

Fila 23. Horas dedicadas: 20 horas a la semana por integrante. Esto se traduce en 320 horas totales por persona durante las 16 semanas.

Fila 25. Costo Unitario / Salario Bruto: El informe indica un costo de $6.500 por hora. <br>Si calculamos el salario mensual (80 horas al mes por $6.500), el costo unitario mensual sería de $520.000 por persona.

Fila 27. Costo Total por persona: 320 horas por $6.500/hr da un total de $2.080.000 por cada integrante.

Fila 29. Costo Total del Proyecto (RRHH): $6.240.000 CLP.

## H.10. balance de inversion inicial

**Tabla H.10.1**
*balance de inversion inicial — filas 1 a 5*

| Fila Excel | A | B | C | D |
|---|---|---|---|---|
| 1 | Detalle de la Inversión | Tipo de Inversión | Monto Total (CLP) | Porcentaje (%) |
| 2 | Desarrollo del Software (Valorizado / Costo de oportunidad) | Activo Intangible | 6.240.000 | 61,54 % |
| 3 | Preparación y lanzamiento (Efectivo) | Activos / Gastos pre-operativos | 1.200.000 | 11,83 % |
| 4 | Capital de Trabajo (Equivalente a 1 mes de OPEX) | Capital de Trabajo | 2.700.000 | 26,63 % |
| 5 | Total Inversión Inicial | — | 10.140.000 | 100,00 % |

*Nota.* Transcripción de la hoja «balance de inversion inicial » de EspaciGo.xlsx, filas 1–5. Se conservan los importes y el alcance del insumo.

Fila 7. El peso del desarrollo: Como puedes ver, el ~62% de la inversión inicial corresponde al esfuerzo del equipo base (los $6.240.000 que vienen del balance de mano de obra). Al estar valorizado como costo de oportunidad, es un dinero que el equipo "invierte" con su tiempo, no necesariamente sacándolo del bolsillo en efectivo.

Fila 9. Capital de Trabajo: Los $2.700.000 aseguran que tengan liquidez<br> para cubrir los primeros costos fijos <br>(1 mes de sueldos part-time, marketing, servidores, etc.)<br> mientras las reservas empiezan a generar volumen.

Fila 11. Desembolso Real y Préstamo: Se asume un préstamo<br> comercial PYME por el 50% de los Activos e Intangibles<br> ($6.240.000 + $1.200.000). Por lo tanto, el monto del crédito será de $3.720.000,<br> inyectando efectivo inicial para mitigar el desembolso de los fundadores.

## H.11. costos fijos

Fila 1. 1. Balance de Costos Fijos (Desglose OPEX - Año 1)

Fila 3. Aquí distribuimos los $18.000.000 anuales (que equivalen a $1.500.000 mensuales) en las categorías que menciona tu estudio.

**Tabla H.11.1**
*costos fijos — filas 5 a 11*

| Fila Excel | A | B | C | D |
|---|---|---|---|---|
| 5 | Detalle del Costo Fijo | Costo Mensual Estimado | Costo Total Anual (Año 1) | % del Total |
| 6 | Administración y Soporte (Personal/Honorarios) | 800.000 | $$9.600.000 | 53,30 % |
| 7 | Difusión, Marketing y Publicidad | 350.000 | $$4200000 | 23,30 % |
| 8 | Servicios Cloud (GCP) e Infraestructura | 150.000 | 1.800.000 | 10,00 % |
| 9 | Mantención de Plataforma y Licencias | 100.000 | 1.200.000 | 6,70 % |
| 10 | Otros Externos (Contabilidad, Legal, etc.) | 100.000 | 1.200.000 | — |
| 11 | Total Costos Fijos (OPEX) | 1.500.000 | 18.000.000 | 100,00 % |

*Nota.* Transcripción de la hoja «costos fijos» de EspaciGo.xlsx, filas 5–11. Se conservan los importes y el alcance del insumo.

Fila 13. 2. Proyección de Costos Fijos (Ajuste IPC 4%)

Fila 15. Esta es la tabla exacta que refleja la inflación proyectada en tu estudio para el Flujo de Caja

**Tabla H.11.2**
*costos fijos — filas 17 a 19*

| Fila Excel | A | B | C | D |
|---|---|---|---|---|
| 17 | Ítem | Año 1 | Año 2 | Año 3 |
| 18 | Costos Fijos Totales | 18.000.000 | 18.720.000 | 19.468.800 |
| 19 | Tasa de Reajuste (IPC) | Base | 4,00 % | 4,00 % |

*Nota.* Transcripción de la hoja «costos fijos» de EspaciGo.xlsx, filas 17–19. Se conservan los importes y el alcance del insumo.

## H.12. cuadro amortizacion

Fila 1. Los datos clave del préstamo son:

Fila 3. Monto del Préstamo (Capital): $$3.720.000 CLP.

Fila 5. Tasa de Interés Anual: 12% (Crédito Comercial PYME con Garantía Estatal).

Fila 7. Plazo: 3 años.

Fila 9. Sistema de Amortización: Cuota fija (método francés), calculada en $$1.548.818 anuales.

Fila 11. Cuadro de Amortización de Deuda (Préstamo Bancario)

**Tabla H.12.1**
*cuadro amortizacion — filas 13 a 17*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 13 | Período (Año) | Capital Insoluto | Amortización  | Interés (12%) | Pago Cuota  |
| 14 | 0 | 3.720.000 | - | - | - |
| 15 | 1 | $2,617,582 | 1.102.418 | 446.400 | 1.548.818 |
| 16 | 2 | 1.382.874 | 1.234.708 | 314.110 | 1.548.818 |
| 17 | 3 | 1 | 1.382.873 | 165.945 | 1.548.818 |

*Nota.* Transcripción de la hoja «cuadro amortizacion» de EspaciGo.xlsx, filas 13–17. Se conservan los importes y el alcance del insumo.

Fila 21. Los Intereses ($446.400, $314.110, $165.945): Se consideran un "Gasto Financiero" y reducen tu utilidad (escudo fiscal).

Fila 23. La Amortización ($1.102.418, $1.234.708, $1.382.874): Es la devolución real del capital, descontada en los flujos no operacionales.

Fila 25. El Ingreso del Préstamo (Año 0): Los $3.720.000 entran como un flujo positivo en el Año 0.

## H.13. maquinaria

Fila 1. Balance Maquinaria (Equipamiento Informático EspaciGo)

**Tabla H.13.1.1**
*maquinaria — filas 3 a 6, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 3 | Detalle | Cantidad | Costo Unitario | Costo Total | Vida Útil |
| 4 | Notebook (Desarrollo y Arquitectura) | 3 | 800.000 | 2.400.000 | 3 años |
| 5 | Smartphone (Pruebas UI/UX y QA) | 1 | 300.000 | 300.000 | 3 años |
| 6 | Total | — | 1.100.000 | 2.700.000 | — |

*Nota.* Transcripción de la hoja «maquinaria» de EspaciGo.xlsx, filas 3–6. Se conservan los importes y el alcance del insumo.

**Tabla H.13.1.2**
*maquinaria — filas 3 a 6, parte 2*

| Fila Excel | A | F | G |
|---|---|---|---|
| 3 | Detalle | Valor residual Total | Depreciación Total Anual |
| 4 | Notebook (Desarrollo y Arquitectura) | 300.000 | 700.000 |
| 5 | Smartphone (Pruebas UI/UX y QA) | 60.000 | 80.000 |
| 6 | Total | 360.000 | 780.000 |

*Nota.* Transcripción de la hoja «maquinaria» de EspaciGo.xlsx, filas 3–6. Se conservan los importes y el alcance del insumo.

Fila 9. Detalle y Cantidad: Se asigna un Notebook estándar de desarrollo a cada uno de los 3 integrantes del equipo.<br> Se suma 1 Smartphone de prueba, fundamental para que tú (rol de UI/UX) valides el diseño responsivo de la plataforma.

Fila 11. Vida Útil: En Chile, el Servicio de Impuestos Internos (SII) establece que<br> los equipos computacionales tienen una vida útil normal de 3 años.

Fila 13. Costo Unitario y Valor Residual: Como el informe del proyecto no declara compra de hardware físico, se utilizan valores de mercado estimados (Notebooks a $800 mil y Smartphone a $300 mil).<br> El valor residual es el precio estimado de reventa de esos equipos usados al pasar los 3 años.

Fila 15. Depreciación Total Anual: Corresponde a la pérdida de valor anual del equipo, <br>que contablemente te sirve para rebajar impuestos. Se calcula con la fórmula: (Costo Total - Valor residual Total) / Vida Útil.

## H.14. herramientas

**Tabla H.14.1.1**
*herramientas — filas 1 a 11, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | Detalle | Cantidad | Costo Unitario Sin IVA | Costo Total Sin IVA | Valor en Dólar USD |
| 2 | Windows 10 / 11 (Sistema Operativo Base) | 3 | 0 | - USD | (-)USD |
| 3 | Visual Studio Code (IDE de Desarrollo) | 3 | 0 | - USD | (-)USD |
| 4 | Go / Golang (Lenguaje Backend) | 3 | 0 | - USD | (-)USD |
| 5 | Next.js / React (Framework Frontend) | 3 | 0 | - USD | (-)USD |
| 6 | PostgreSQL + PostGIS (Base de Datos Local) | 3 | 0 | - USD | (-)USD |
| 7 | Docker (Empaquetado y Contenedores) | 3 | 0 | - USD | (-)USD |
| 8 | Figma (Diseño UI/UX y Prototipado) | 1 | 0 | - USD | (-)USD |
| 9 | PlantUML (Modelado de Casos de Uso y UML) | 3 | 0 | - USD | (-)USD |
| 10 | Git / GitHub (Control de Versiones) | 3 | 0 | - USD | (-)USD |
| 11 | Microsoft Office (Documentación del Proyecto) | 3 | 0 | — | (-)USD |

*Nota.* Transcripción de la hoja «herramientas» de EspaciGo.xlsx, filas 1–11. Se conservan los importes y el alcance del insumo.

**Tabla H.14.1.2**
*herramientas — filas 1 a 11, parte 2*

| Fila Excel | A | F | H |
|---|---|---|---|
| 1 | Detalle | Vigencia | Cantidad: La mayoría de las herramientas tienen cantidad "3" porque son instaladas en los equipos de los tres integrantes del grupo para el desarrollo y documentación conjunta. Figma tiene cantidad "1" porque la matriz RACI asigna específicamente el "Prototipado en Figma" a Anita Marchant. |
| 2 | Windows 10 / 11 (Sistema Operativo Base) | Indefinida | — |
| 3 | Visual Studio Code (IDE de Desarrollo) | Indefinida | Costos ($0): Las tecnologías elegidas (Go, Next.js, PostgreSQL, Docker) son de uso libre y gratuito (Open Source).<br> Figma, GitHub y PlantUML cuentan con planes gratuitos o académicos que cubren completamente las necesidades <br>de un proyecto de título. Microsoft Office y Windows se asumen provistos por licencias académicas institucionales de INACAP. |
| 4 | Go / Golang (Lenguaje Backend) | Indefinida | — |
| 5 | Next.js / React (Framework Frontend) | Indefinida | Exclusión de Infraestructura: Es importante notar que Google Cloud Platform (Cloud Run, BigQuery), Mercado Pago<br> y FirmaVirtual no van en esta tabla. Esos son servicios en la nube de pago por uso o cobro por transacción, <br>por lo que pertenecen al Balance de Insumos o a los Costos Operativos (OPEX), no a las herramientas de desarrollo local. |
| 6 | PostgreSQL + PostGIS (Base de Datos Local) | Indefinida | — |
| 7 | Docker (Empaquetado y Contenedores) | Indefinida | — |
| 8 | Figma (Diseño UI/UX y Prototipado) | Indefinida | — |
| 9 | PlantUML (Modelado de Casos de Uso y UML) | Indefinida | — |
| 10 | Git / GitHub (Control de Versiones) | Indefinida | — |
| 11 | Microsoft Office (Documentación del Proyecto) | Indefinida | — |

*Nota.* Transcripción de la hoja «herramientas» de EspaciGo.xlsx, filas 1–11. Se conservan los importes y el alcance del insumo.

Fila 12. Total

## H.15. insumos

Fila 1. 1. Balance de Insumos (Operación Base)

**Tabla H.15.1.1**
*insumos — filas 3 a 8, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 3 | Ítem | Unidad de Medida | Cantidad Mensual | Costo Unitario | Costo Mensual |
| 4 | Servicios Cloud (GCP: Hosting, BD, Storage) | Mes | 1 | 150.000 | 150.000 |
| 5 | Paquete Transacciones API FirmaVirtual | Lote | 1 | 50.000 | 50.000 |
| 6 | Dominio Web (.cl) | Año | 0,083* | 10.950 | 913 |
| 7 | Útiles de Oficina (Apuntes, resmas y lápices para el equipo) | Kit | 1 | 10.000 | 10.000 |
| 8 | Total | — | — | — | 210.913 |

*Nota.* Transcripción de la hoja «insumos» de EspaciGo.xlsx, filas 3–8. Se conservan los importes y el alcance del insumo.

**Tabla H.15.1.2**
*insumos — filas 3 a 8, parte 2*

| Fila Excel | A | F |
|---|---|---|
| 3 | Ítem | Costo Anual |
| 4 | Servicios Cloud (GCP: Hosting, BD, Storage) | 1.800.000 |
| 5 | Paquete Transacciones API FirmaVirtual | 600.000 |
| 6 | Dominio Web (.cl) | 10.950 |
| 7 | Útiles de Oficina (Apuntes, resmas y lápices para el equipo) | 120.000 |
| 8 | Total | 2.530.950 |

*Nota.* Transcripción de la hoja «insumos» de EspaciGo.xlsx, filas 3–8. Se conservan los importes y el alcance del insumo.

Fila 10. *(Nota : El dominio se paga una vez al año, por lo que la cantidad mensual es 1/12 o 0,083 para reflejar el prorrateo del costo mensual).

Fila 12. 2. Insumos según Horizonte de Planeación SIN IVA

Fila 14. Aquí aplicamos la tasa de reajuste por inflación del 4% anual definida en el estudio de antigrativy para proyectar los costos en los siguientes periodos.

**Tabla H.15.2.1**
*insumos — filas 16 a 21, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 16 | Ítem | Cantidad Anual | Precio Unitario | Periodo 1 (Año 1) | Periodo 2 (+4%) |
| 17 | Servicios Cloud GCP | 12 | 150.000 | 1.800.000 | 1.872.000 |
| 18 | API FirmaVirtual | 12 | 50.000 | 600.000 | 624.000 |
| 19 | Dominio Web (.cl) | 1 | 10.950 | 10.950 | 11.388 |
| 20 | Útiles de Oficina | 12 | 10.000 | 120.000 | 124.800 |
| 21 | Total | — | — | 2.530.950 | 2.632.188 |

*Nota.* Transcripción de la hoja «insumos» de EspaciGo.xlsx, filas 16–21. Se conservan los importes y el alcance del insumo.

**Tabla H.15.2.2**
*insumos — filas 16 a 21, parte 2*

| Fila Excel | A | F | G |
|---|---|---|---|
| 16 | Ítem | Periodo 3 (+4%) | Periodo 4 (+4%) |
| 17 | Servicios Cloud GCP | 1.946.880 | 2.024.755 |
| 18 | API FirmaVirtual | 648.960 | 674.918 |
| 19 | Dominio Web (.cl) | 11.844 | 12.318 |
| 20 | Útiles de Oficina | 129.792 | 134.984 |
| 21 | Total | 2.737.476 | 2.846.975 |

*Nota.* Transcripción de la hoja «insumos» de EspaciGo.xlsx, filas 16–21. Se conservan los importes y el alcance del insumo.

Fila 23. 3. Detalle Fuentes y Precios

Fila 25. Tal como en tu ejemplo, esta tabla justifica de dónde sacaste los precios unitarios

**Tabla H.15.3**
*insumos — filas 27 a 31*

| Fila Excel | A | B | C | E |
|---|---|---|---|---|
| 27 | Artículo | Precios Sin Iva | URL / Fuente | — |
| 28 | Servicios Cloud (GCP) | 150.000 | cloud.google.com/pricing (Estimado OPEX) | — |
| 29 | Dominio Web | 10.950 | nic.cl / Informe del Proyecto | deberia |
| 30 | API FirmaVirtual | 50.000 | firmavirtual.legal/planes | — |
| 31 | Útiles de Oficina (Kit) | 10.000 | mercadolibre.cl/utiles-oficina | — |

*Nota.* Transcripción de la hoja «insumos» de EspaciGo.xlsx, filas 27–31. Se conservan los importes y el alcance del insumo.

## H.16. hardware

Fila 1. Costo Hardware (SaaS Cloud-Native)

**Tabla H.16.1.1**
*hardware — filas 3 a 6, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 3 | Detalle | Valor Unitario SIN IVA | Periodo 1 | Valor Periodo 1 | Periodo 2 |
| 4 | Dispositivos Físicos / IoT (No aplica) | 0 | 0 | 0 | 0 |
| 5 | Servidores Locales / On-Premise | 0 | 0 | 0 | 0 |
| 6 | Total | 0 | — | 0 | — |

*Nota.* Transcripción de la hoja «hardware» de EspaciGo.xlsx, filas 3–6. Se conservan los importes y el alcance del insumo.

**Tabla H.16.1.2**
*hardware — filas 3 a 6, parte 2*

| Fila Excel | A | F | G | H | I |
|---|---|---|---|---|---|
| 3 | Detalle | Valor Periodo 2 | Periodo 3 | Valor Periodo 3 | Periodo 4 |
| 4 | Dispositivos Físicos / IoT (No aplica) | 0 | — | — | — |
| 5 | Servidores Locales / On-Premise | 0 | — | — | — |
| 6 | Total | 0 | — | — | — |

*Nota.* Transcripción de la hoja «hardware» de EspaciGo.xlsx, filas 3–6. Se conservan los importes y el alcance del insumo.

**Tabla H.16.1.3**
*hardware — filas 3 a 6, parte 3*

| Fila Excel | A | J |
|---|---|---|
| 3 | Detalle | Valor periodo 4 |
| 4 | Dispositivos Físicos / IoT (No aplica) | — |
| 5 | Servidores Locales / On-Premise | — |
| 6 | Total | — |

*Nota.* Transcripción de la hoja «hardware» de EspaciGo.xlsx, filas 3–6. Se conservan los importes y el alcance del insumo.

Fila 8. EspaciGo es un SaaS Cloud-Native. La infraestructura se procesa en la nube de Google (GCP) bajo un modelo de pago por uso (OPEX), por lo que no existe gasto en activos de hardware (CAPEX) más allá de la inversión i<br>nicial en los computadores de desarrollo. Nuestros verdaderos costos variables son digitales (consultas a la API de FirmaVirtual y comisiones de la pasarela de pagos).

## H.17. servicio respaldo

Fila 1. 1. Parámetros (Base del cálculo)

Fila 3. Esta es la tabla inferior de tu imagen, adaptada a las reservas de EspaciGo.

**Tabla H.17.1**
*servicio respaldo — filas 5 a 12*

| Fila Excel | A | B |
|---|---|---|
| 5 | Parámetros | Valores |
| 6 | Peso Promedio por Reserva (Fotos Check-in/out + Contrato) en GB | 0,05 GB (aprox 50 MB) |
| 7 | Cantidad de Reservas Anuales Base | 3.600 |
| 8 | Cantidad Reservas Periodo 1 (Año 1) | 3.600 |
| 9 | Cantidad Reservas Periodo 2 (Crecimiento 20%) | 4.320 |
| 10 | Cantidad Reservas Periodo 3 (Crecimiento 20%) | 5.184 |
| 11 | Cantidad Reservas Periodo 4 (Crecimiento 20%) | 6.220 |
| 12 | Base de Datos Operativa (PostgreSQL + Logs) por periodo | ~10 GB fijos |

*Nota.* Transcripción de la hoja «servicio respaldo» de EspaciGo.xlsx, filas 5–12. Se conservan los importes y el alcance del insumo.

Fila 14. 2. Tramos de Almacenamiento y Consumo

Fila 16. Esta es la tabla central de tu imagen. Cruzamos el consumo de GB acumulados con los planes de respaldo (ej. precios de tramos de Google Cloud Storage o Google Workspace).

**Tabla H.17.2**
*servicio respaldo — filas 18 a 22*

| Fila Excel | A | B | D | E |
|---|---|---|---|---|
| 18 | Cantidad Espacio | Valor Respaldo Anual (Base) | Periodos | GB Evidencias + Datos Acumulados |
| 19 | 100GB | 50.000 | Periodo 1 (Servicio 250GB) | 190 GB (180GB reservas + 10GB BD) |
| 20 | 250GB | 80.000 | Periodo 2 (Servicio 500GB) | 416 GB (190 + 216GB res. + 10GB BD) |
| 21 | 500GB | 120.000 | Periodo 3 (Servicio 1000GB) | 685 GB (416 + 259GB res. + 10GB BD) |
| 22 | 1000GB | 190.000 | Periodo 4 (Servicio 1000GB) | 996 GB (685 + 311GB res. + 10GB BD) |

*Nota.* Transcripción de la hoja «servicio respaldo» de EspaciGo.xlsx, filas 18–22. Se conservan los importes y el alcance del insumo.

Fila 24. 3. Servicio de respaldo en la nube (Flujo ajustado)

Fila 26. Esta es la tabla superior de tu imagen. Muestra el costo que irá a tu Flujo de Caja. Toma el plan que necesitas según los GB de arriba, y le aplica el 4% de inflación anual desde el Periodo 2 en adelante.

**Tabla H.17.3**
*servicio respaldo — filas 28 a 30*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 28 | Detalle | Periodo 1 | Periodo 2 | Periodo 3 | Periodo 4 |
| 29 | Servicio de Respaldo GCP | 80.000 | 124.800 | 205.504 | 213.724 |
| 30 | Total | 80.000 | 124.800 | 205.504 | 213.724 |

*Nota.* Transcripción de la hoja «servicio respaldo» de EspaciGo.xlsx, filas 28–30. Se conservan los importes y el alcance del insumo.

Fila 32. ¿Por qué aumentan los GB? A diferencia de un negocio tradicional, la plataforma por ley (Ley 21.719) y por operatividad debe guardar el historial inmutable (BigQuery), los contratos firmados y las fotos de daños de cada reserva por 5 años. Por ende, el almacenamiento se acumula año a año.

Fila 34. ¿Cómo se calcula el valor del periodo? En el Periodo 1 necesitas el tramo de 250GB ($80.000). En el Periodo 2 saltas al tramo de 500GB ($120.000), pero como es el año 2, se le aplica el 4% de inflación ($120.000 * 1.04 = $124.800). En el Periodo 3 saltas a 1000GB ($190.000) aplicando dos años de inflación ($190.000 * 1.04^2 = $205.504).

## H.18. balance personal

Fila 7. 2. Balance Personal Proyectado a 4 años

Fila 9. Aquí proyectamos los sueldos en el tiempo aplicando el reajuste del 4% (IPC) estimado en tu modelo financiero.

**Tabla H.18.1**
*balance personal — filas 11 a 15*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 11 | Cargo Operativo (Rol en el Equipo) | Cantidad | Modalidad | Costo Bruto Mensual | Costo Anual |
| 12 | Administrador Cloud y Gerencia (Hernán E.) | 1 | Part-Time | 400.000 | 4.800.000 |
| 13 | Mantenimiento Backend e Integraciones (Erick S.) | 1 | Part-Time | 400.000 | 4.800.000 |
| 14 | Soporte UI/UX y Atención Usuarios (Anita M.) | 1 | Part-Time | 400.000 | 4.800.000 |
| 15 | Total Nómina Operativa | 3 | — | 1.200.000 | 14.400.000 |

*Nota.* Transcripción de la hoja «balance personal» de EspaciGo.xlsx, filas 11–15. Se conservan los importes y el alcance del insumo.

Fila 16. 2. Balance Personal Proyectado a 4 años

Fila 18. Aquí proyectamos los sueldos del equipo aplicando el reajuste del 4% (IPC) anual.

**Tabla H.18.2.1**
*balance personal — filas 19 a 23, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 19 | Cargo | Costo Anual Base | Cantidad | Modalidad | Periodo 1 (Año 1) |
| 20 | Admin. Cloud (Hernán) | 4.800.000 | 1 | Part-Time | 4.800.000 |
| 21 | Mantenimiento (Erick) | 4.800.000 | 1 | Part-Time | 4.800.000 |
| 22 | Soporte (Anita) | 4.800.000 | 1 | Part-Time | 4.800.000 |
| 23 | Total | 14.400.000 | — | — | 14.400.000 |

*Nota.* Transcripción de la hoja «balance personal» de EspaciGo.xlsx, filas 19–23. Se conservan los importes y el alcance del insumo.

**Tabla H.18.2.2**
*balance personal — filas 19 a 23, parte 2*

| Fila Excel | A | F | G | H | I |
|---|---|---|---|---|---|
| 19 | Cargo | Cantidad | Periodo 2 (+4%) | Cantidad | Periodo 3 (+4%) |
| 20 | Admin. Cloud (Hernán) | 1 | 4.992.000 | 1 | 5.191.680 |
| 21 | Mantenimiento (Erick) | 1 | 4.992.000 | 1 | 5.191.680 |
| 22 | Soporte (Anita) | 1 | 4.992.000 | 1 | 5.191.680 |
| 23 | Total | — | 14.976.000 | — | 15.575.040 |

*Nota.* Transcripción de la hoja «balance personal» de EspaciGo.xlsx, filas 19–23. Se conservan los importes y el alcance del insumo.

**Tabla H.18.2.3**
*balance personal — filas 19 a 23, parte 3*

| Fila Excel | A | J | K |
|---|---|---|---|
| 19 | Cargo | Cantidad | Periodo 4 (+4%) |
| 20 | Admin. Cloud (Hernán) | 1 | 5.399.347 |
| 21 | Mantenimiento (Erick) | 1 | 5.399.347 |
| 22 | Soporte (Anita) | 1 | 5.399.347 |
| 23 | Total | — | 16.198.041 |

*Nota.* Transcripción de la hoja «balance personal» de EspaciGo.xlsx, filas 19–23. Se conservan los importes y el alcance del insumo.

Fila 25. 3. Detalle Costos Sueldos y Fuentes

Fila 27. Justificamos que estos sueldos corresponden a una etapa inicial de emprendimiento.

**Tabla H.18.3**
*balance personal — filas 29 a 30*

| Fila Excel | A | B | C |
|---|---|---|---|
| 29 | Ocupación | Costo Bruto Mensual | URL / Fuente |
| 30 | Equipo Operativo Fundador (3 roles Part-Time) | $ 400.000 (c/u) | Estimación interna Startup (Equivalente a sueldo base part-time para mantención SaaS). |

*Nota.* Transcripción de la hoja «balance personal» de EspaciGo.xlsx, filas 29–30. Se conservan los importes y el alcance del insumo.

Fila 32. En la fase de pre-inversión (Año 0), esos 14,4 millones representan el "Costo de Oportunidad" del equipo trabajando 16 semanas full-time para programar el software (el activo intangible).

Fila 34. En la fase de operación (Años 1 al 4), la plataforma ya está construida, por lo que el equipo pasa a modalidad "Part-Time" para dar soporte técnico y mantener la nube. Esos nuevos 14,4 millones anuales son dinero real (OPEX) que debe salir de los ingresos de las reservas para pagarles a ustedes por operar el negocio.

## H.19. gastos conexos

Fila 1. 1. Cantidad de Viajes

**Tabla H.19.1**
*gastos conexos — filas 3 a 6*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 3 | Detalle | Periodo 1 | Periodo 2 | Periodo 3 | Periodo 4 |
| 4 | Reuniones presenciales de equipo (1 mensual) | 12 | 12 | 12 | 12 |
| 5 | Reuniones extraordinarias / Imprevistos | 3 | 4 | 4 | 5 |
| 6 | Total Viajes Anuales (Hernán a Stgo) | 15 | 16 | 16 | 17 |

*Nota.* Transcripción de la hoja «gastos conexos» de EspaciGo.xlsx, filas 3–6. Se conservan los importes y el alcance del insumo.

Fila 8. 2. Gastos Conexos - Transporte para Coordinación del Servicio

Fila 10. Aquí cruzamos la cantidad de viajes con el costo de Hernán ($12.000 base), aplicando el 4% de IPC anual desde el Periodo 2 para la inflación de los pasajes.

**Tabla H.19.2.1**
*gastos conexos — filas 12 a 14, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 12 | Detalle | Coste pasaje Ida y Vuelta (Bus Cartagena + Metro) | Total Periodo 1 | Total Periodo 2 | Total Periodo 3 |
| 13 | Coste Total Anual | 12.000 | 180.000 | 199.680 | 207.667 |
| 14 | Cantidad de Viajes | — | 15 | 16 | 16 |

*Nota.* Transcripción de la hoja «gastos conexos» de EspaciGo.xlsx, filas 12–14. Se conservan los importes y el alcance del insumo.

**Tabla H.19.2.2**
*gastos conexos — filas 12 a 14, parte 2*

| Fila Excel | A | F |
|---|---|---|
| 12 | Detalle | Total Periodo 4 |
| 13 | Coste Total Anual | 229.467 |
| 14 | Cantidad de Viajes | 17 |

*Nota.* Transcripción de la hoja «gastos conexos» de EspaciGo.xlsx, filas 12–14. Se conservan los importes y el alcance del insumo.

Fila 16. # IPC Agregado para los periodos: 4% anual (según tu estudio financiero).

Fila 18. # Cada viaje consta de un pasaje de ida y vuelta para Hernán; Anita y Erick tienen costo $0.

Fila 20. # Fórmula aplicada: coste base ($12.000) x cantidad de viajes del periodo x IPC acumulado.

Fila 24. Ejemplo Periodo 1: $12.000 x 15 viajes = $180.000

Fila 26. Ejemplo Periodo 2: ($12.000 * 1,04) x 16 viajes = $12.480 x 16 = $199.680

Fila 28. # Se considera en la estimación:<br> La cantidad de reuniones de planificación en Santiago,<br> junto con un margen para viajes extraordinarios.

## H.20. costos y gastos generales

Fila 1. 1. Balance de Costos y Gastos Generales (EspaciGo)

**Tabla H.20.1.1**
*costos y gastos generales — filas 3 a 3, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 3 | Detalle / Período Anual | 0 (Inversión) | 1 | 2 (+4%) | 3 (+4%) |

*Nota.* Transcripción de la hoja «costos y gastos generales» de EspaciGo.xlsx, filas 3–3. Se conservan los importes y el alcance del insumo.

**Tabla H.20.1.2**
*costos y gastos generales — filas 3 a 3, parte 2*

| Fila Excel | A | F |
|---|---|---|
| 3 | Detalle / Período Anual | 4 (+4%) |

*Nota.* Transcripción de la hoja «costos y gastos generales» de EspaciGo.xlsx, filas 3–3. Se conservan los importes y el alcance del insumo.

Fila 4. GASTOS

**Tabla H.20.2.1**
*costos y gastos generales — filas 5 a 12, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 5 | Co-Working / Oficina (100% Remoto) | 0 | 0 | 0 | 0 |
| 6 | Oficina Virtual (Dirección Tributaria SII) | 150.000 | 150.000 | 156.000 | 162.240 |
| 7 | Servicio Respaldo (Evidencias/Contratos) | 0 | 80.000 | 124.800 | 205.504 |
| 8 | Insumos (API FirmaVirtual + Útiles) | 0 | 720.000 | 748.800 | 778.752 |
| 9 | Gastos Conexos (Viajes Coordinación) | 0 | 180.000 | 199.680 | 207.667 |
| 10 | Marketing, Publicidad y Difusión | 1.200.000 | 4.200.000 | 4.368.000 | 4.542.720 |
| 11 | Outsourcing Contador | 0 | 600.000 | 624.000 | 648.960 |
| 12 | Gastos Totales | 1.350.000 | 5.930.000 | 6.221.280 | 6.545.843 |

*Nota.* Transcripción de la hoja «costos y gastos generales» de EspaciGo.xlsx, filas 5–12. Se conservan los importes y el alcance del insumo.

**Tabla H.20.2.2**
*costos y gastos generales — filas 5 a 12, parte 2*

| Fila Excel | A | F |
|---|---|---|
| 5 | Co-Working / Oficina (100% Remoto) | 0 |
| 6 | Oficina Virtual (Dirección Tributaria SII) | 168.730 |
| 7 | Servicio Respaldo (Evidencias/Contratos) | 213.724 |
| 8 | Insumos (API FirmaVirtual + Útiles) | 809.902 |
| 9 | Gastos Conexos (Viajes Coordinación) | 229.467 |
| 10 | Marketing, Publicidad y Difusión | 4.724.428 |
| 11 | Outsourcing Contador | 674.918 |
| 12 | Gastos Totales | 6.821.169 |

*Nota.* Transcripción de la hoja «costos y gastos generales» de EspaciGo.xlsx, filas 5–12. Se conservan los importes y el alcance del insumo.

Fila 14. COSTOS VARIABLES

**Tabla H.20.3.1**
*costos y gastos generales — filas 15 a 17, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 15 | Costos por Hardware | 0 | 0 | 0 | 0 |
| 16 | Comisión Pasarela (Mercado Pago) | 0 | 10.800.000 | 11.232.000 | 11.681.280 |
| 17 | Total Costos Variables | 0 | 10.800.000 | 11.232.000 | 11.681.280 |

*Nota.* Transcripción de la hoja «costos y gastos generales» de EspaciGo.xlsx, filas 15–17. Se conservan los importes y el alcance del insumo.

**Tabla H.20.3.2**
*costos y gastos generales — filas 15 a 17, parte 2*

| Fila Excel | A | F |
|---|---|---|
| 15 | Costos por Hardware | 0 |
| 16 | Comisión Pasarela (Mercado Pago) | 12.148.531 |
| 17 | Total Costos Variables | 12.148.531 |

*Nota.* Transcripción de la hoja «costos y gastos generales» de EspaciGo.xlsx, filas 15–17. Se conservan los importes y el alcance del insumo.

Fila 19. COSTOS FIJOS

**Tabla H.20.4.1**
*costos y gastos generales — filas 20 a 26, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 20 | Dominio NIC (.cl) | 10.950 | 11.388 | 11.844 | 12.318 |
| 21 | Servicios Cloud y Hosting (GCP) | 0 | 1.800.000 | 1.872.000 | 1.946.880 |
| 22 | Depreciación (Equipos Informáticos) | 0 | 780.000 | 780.000 | 780.000 |
| 23 | Mano de Obra (Desarrollo del Software) | 6.240.000 | 0 | 0 | 0 |
| 24 | Personal Operativo (Equipo Fundador) | 0 | 14.400.000 | 14.976.000 | 15.575.040 |
| 25 | Herramientas y Licencias de Software | 0 | 0 | 0 | 0 |
| 26 | Total Costos Fijos | 6.250.950 | 16.991.388 | 17.639.844 | 18.314.238 |

*Nota.* Transcripción de la hoja «costos y gastos generales» de EspaciGo.xlsx, filas 20–26. Se conservan los importes y el alcance del insumo.

**Tabla H.20.4.2**
*costos y gastos generales — filas 20 a 26, parte 2*

| Fila Excel | A | F |
|---|---|---|
| 20 | Dominio NIC (.cl) | 12.811 |
| 21 | Servicios Cloud y Hosting (GCP) | 2.024.755 |
| 22 | Depreciación (Equipos Informáticos) | 0 |
| 23 | Mano de Obra (Desarrollo del Software) | 0 |
| 24 | Personal Operativo (Equipo Fundador) | 16.198.041 |
| 25 | Herramientas y Licencias de Software | 0 |
| 26 | Total Costos Fijos | 18.235.607 |

*Nota.* Transcripción de la hoja «costos y gastos generales» de EspaciGo.xlsx, filas 20–26. Se conservan los importes y el alcance del insumo.

**Tabla H.20.5.1**
*costos y gastos generales — filas 28 a 28, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 28 | TOTAL GENERAL (Gastos + Costos) | 7.600.950 | 33.721.388 | 35.093.124 | 36.541.361 |

*Nota.* Transcripción de la hoja «costos y gastos generales» de EspaciGo.xlsx, filas 28–28. Se conservan los importes y el alcance del insumo.

**Tabla H.20.5.2**
*costos y gastos generales — filas 28 a 28, parte 2*

| Fila Excel | A | F |
|---|---|---|
| 28 | TOTAL GENERAL (Gastos + Costos) | 37.205.307 |

*Nota.* Transcripción de la hoja «costos y gastos generales» de EspaciGo.xlsx, filas 28–28. Se conservan los importes y el alcance del insumo.

Fila 31. (Nota: En el año 4 la depreciación baja a $0 porque la vida útil contable de los computadores es de 3 años).

Fila 33. 2. Cuadros Comparativos (Sección Derecha de tu Imagen)

Fila 37. Cuadro Comparativo Infraestructura Cloud 1.1

**Tabla H.20.6**
*costos y gastos generales — filas 39 a 42*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 39 | Opción | Compañía | Plan / Modelo | Precio Anual (Estimado) | Decisión |
| 40 | A | GCP Cloud Run | Serverless / Pago por uso | 1.800.000 | Seleccionado |
| 41 | B | AWS EC2 | Instancias Fijas 24/7 | 2.450.000 | Descartado |
| 42 | C | VPS Tradicional | Servidor Privado Virtual | 1.200.000 | Descartado (No escala) |

*Nota.* Transcripción de la hoja «costos y gastos generales» de EspaciGo.xlsx, filas 39–42. Se conservan los importes y el alcance del insumo.

Fila 44. Cuadro Comparativo Motor Legal (Ley 21.461) 1.2

**Tabla H.20.7**
*costos y gastos generales — filas 46 a 49*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 46 | Opción | Compañía | Servicio | Validez Legal | Decisión |
| 47 | A | FirmaVirtual | Firma Electrónica Avanzada Remota | Alta (Permite desalojos) | Seleccionado |
| 48 | B | DocuSign | Firma Simple Cloud | Cuestionable en Chile | Descartado |
| 49 | C | Notaría Presencial | Trámite Físico | Alta | Descartado (Rompe UX) |

*Nota.* Transcripción de la hoja «costos y gastos generales» de EspaciGo.xlsx, filas 46–49. Se conservan los importes y el alcance del insumo.

Fila 51. Cuadro Comparativo Pasarela de Pagos 1.3

**Tabla H.20.8**
*costos y gastos generales — filas 53 a 56*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 53 | Opción | Compañía | Soporte Escrow (Retención) | Soporte Split (División) | Decisión |
| 54 | A | Mercado Pago | Sí (Nativo vía API) | Sí | Seleccionado |
| 55 | B | Transbank Webpay | Burocrático / Lento | Complejo B2B2C | Descartado |
| 56 | C | Flow | No Nativo | Parcial | Descartado |

*Nota.* Transcripción de la hoja «costos y gastos generales» de EspaciGo.xlsx, filas 53–56. Se conservan los importes y el alcance del insumo.

Fila 58. Al presentar esta hoja consolidada, estás demostrando que los $14,4 millones iniciales<br> de "Mano de Obra" (construcción) solo ocurren en el Periodo 0, y que luego el modelo muta a un costo de "Personal Operativo" y "Comisiones de Mercado Pago", lo que refleja un profundo entendimiento de la diferencia entre crear una Startup y operarla financieramente

## H.21. capital de trabajo

Fila 1. Se asume una inversión en Capital de Trabajo correspondiente a 1 mes de costos operativos (Aprox. $2.400.000 CLP).

Fila 3. Capital de Trabajo (Equivalente a 1 Mes de Operación)

**Tabla H.21.1**
*capital de trabajo — filas 5 a 10*

| Fila Excel | A | B | D |
|---|---|---|---|
| 5 | Ítem | Valor | — |
| 6 | Remuneraciones (Personal Operativo - 1 Mes) | 1.200.000 | Remuneraciones: Corresponde al sueldo de los 3 integrantes operando la plataforma part-time durante el primer mes ($400.000 x 3). |
| 7 | Costos Variables (Comisiones Mercado Pago - 1 Mes) | 900.000 | — |
| 8 | Servicios Cloud e Infraestructura GCP (1 Mes) | 150.000 | Costos Variables: Corresponde a 1 mes del costo variable total del Año 1 ($10.800.000 / 12 meses). |
| 9 | Gastos de Administración, Marketing y Difusión (1 Mes) | 450.000 | — |
| 10 | Total Capital de Trabajo | 2.700.000 | Servicios Cloud: 1 mes estimado de servidores para mantener la plataforma arriba. |

*Nota.* Transcripción de la hoja «capital de trabajo» de EspaciGo.xlsx, filas 5–10. Se conservan los importes y el alcance del insumo.

Fila 12. Gastos de Administración: La suma prorrateada a un mes del resto de gastos fijos (publicidad, contador, insumos)

## H.22. TasaInteresCredito

Fila 1. Cuadro Comparativo de Opciones de Financiamiento (EspaciGo)

**Tabla H.22.1**
*TasaInteresCredito — filas 2 a 5*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 2 | Opción de Crédito | Institución / Instrumento | Tasa de Interés Anual (Referencial) | Requisitos y Viabilidad para EspaciGo | Decisión |
| 3 | Opción A: Crédito Comercial PYME (con Garantía Corfo) | BancoEstado / Banco BCI (FOGAPE / FOGAIN) | ~12% a 14% nominal anual | Requiere iniciación de actividades y la garantía estatal (FOGAPE) cubre el riesgo al no tener historial de ventas. | Seleccionado. Es la vía formal más lógica para una Startup tecnológica. |
| 4 | Opción B: Crédito de Consumo Personal | Bancos Comerciales (Evaluación como persona natural) | ~18% a 24% nominal anual | Los fundadores piden el crédito a su nombre y lo inyectan a la empresa. Tasa mucho más alta (TMC) y riesgo personal. | Descartado. Encarece el costo de capital de la empresa innecesariamente. |
| 5 | Opción C: Capital Semilla / Fondos Concursables | CORFO / Sercotec (Semilla Inicia) | 0% (Subsidio no reembolsable) | Aporte de hasta $15.000.000. Requiere cofinanciamiento del 25% y adjudicarse un concurso competitivo. | Plan B. Se considera como alternativa, pero para el Flujo de Caja se evalúa el peor escenario (deuda bancaria). |

*Nota.* Transcripción de la hoja «TasaInteresCredito» de EspaciGo.xlsx, filas 2–5. Se conservan los importes y el alcance del insumo.

Fila 7. Fuentes:

Fila 9. 1. Tasas de Interés Comercial: Banco Central de Chile (Estadísticas de Tasas de Interés del Sistema Financiero). La tasa promedio comercial en Chile fluctúa históricamente entre el 10% y el 14% dependiendo de la TPM (Tasa de Política Monetaria).

Fila 11. 2. Tasas de Crédito de Consumo: Comisión para el Mercado Financiero (CMF) - Simulador de Cuotas.

Fila 13. 3. Garantías PYME: Portal Corfo (Programas FOGAIN y Créditos Corfo PYME).

**Tabla H.22.2**
*TasaInteresCredito — filas 15 a 19*

| Fila Excel | A | B | C | D |
|---|---|---|---|---|
| 15 | Fuente de Financiamiento | Detalle / Base de Cálculo | Monto (CLP) | Participación (%) |
| 16 | Crédito Comercial PYME | 50% de Desarrollo ($6.240.000) + Preparación ($1.200.000) | 3.720.000 | 36,69 % |
| 17 | Aporte Propio Valorizado | 50% restante del Desarrollo del Software (Costo oportunidad) | 3.720.000 | 36,69 % |
| 18 | Aporte Propio en Efectivo | Financiamiento directo del Capital de Trabajo Inicial | 2.700.000 | 26,63 % |
| 19 | TOTAL FINANCIAMIENTO | Equivalente al 100% de la Inversión Inicial (Año 0) | 10.140.000 | 100,00 % |

*Nota.* Transcripción de la hoja «TasaInteresCredito» de EspaciGo.xlsx, filas 15–19. Se conservan los importes y el alcance del insumo.

## H.23. FlujoNeto

Fila 1. La Lógica de Decisión detrás del <br>Flujo de Caja

**Tabla H.23.1**
*FlujoNeto — filas 3 a 3*

| Fila Excel | A | C | E | G |
|---|---|---|---|---|
| 3 | 1.Decisión de Inversión y Apalancamiento (Año 0):<br> El proyecto requiere un total de $10.140.000 (Desarrollo + Preparación + Capital de Trabajo).<br> Gracias a la decisión de apalancamiento financiero,<br> se solicita un crédito comercial PYME por el 50% de los activos e intangibles<br> ($3.720.000 a 3 años y 12% de interés). Esto reduce el esfuerzo en efectivo de los socios en el Año 0,<br> dejando un desembolso inicial real (Flujo de Caja Neto del Año 0) de -$6.420.000. | 2.Decisión Operativa (Ingresos vs. Costos):<br> Los ingresos de EspaciGo provienen de la comisión de intermediación del marketplace B2B2C. Para que el negocio sea rentable, los ingresos deben cubrir holgadamente los costos variables (pasarela de pago Mercado Pago) y los costos fijos operativos (sueldos part-time de los 3 socios reajustados por el 4% de IPC anual, servidores GCP, marketing y respaldo). | 3.Decisión Tributaria y Escudo Fiscal (Años 1 al 3):<br>Aquí aplicamos la normativa chilena (Impuesto de Primera Categoría del 27%). La gracia financiera es que antes de pagar impuestos, restamos dos elementos que no son salidas de efectivo inmediatas o reducen base imponible:<br><br>La depreciación de los equipos (780 mil anuales los primeros 3 años).<br><br>Los intereses del préstamo (que actúan como "escudo fiscal", haciendo que pagues menos impuestos al rebajar la utilidad). | 4.Flujo de Caja Neto (Disponibilidad Real):<br>A la utilidad después de impuestos le sumamos nuevamente la depreciación (porque no es plata que salió de la caja) y restamos la amortización real del préstamo (la devolución del capital al banco). El resultado final es el dinero fresco que genera la plataforma año a año. |

*Nota.* Transcripción de la hoja «FlujoNeto» de EspaciGo.xlsx, filas 3–3. Se conservan los importes y el alcance del insumo.

Fila 5. Cuadro del Flujo Neto de Caja (EspaciGo)

**Tabla H.23.2.1**
*FlujoNeto — filas 7 a 23, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 7 | Partida / Período (Años) | Año 0 | Año 1 | Año 2 (+4% IPC) | Año 3 (+4% IPC) |
| 8 | (+) Ingresos por Comisiones (GMV) | 0 | 35.000.000 | 38.500.000 | 42.350.000 |
| 9 | (-) Costos Variables (Comisión Pasarela) | 0 | 10.800.000 | 11.232.000 | 11.681.280 |
| 10 | (-) Costos Fijos Operativos (OPEX) | 0 | 18.000.000 | 18.720.000 | 19.468.800 |
| 11 | (-) Gastos de Administración y Marketing | -1.350.000 | 5.930.000 | 6.221.280 | 6.545.843 |
| 12 | (-) Depreciación de Activos (Maquinaria) | 0 | 780.000 | 780.000 | 780.000 |
| 13 | (=) Resultado Operativo (EBIT) | -1.350.000 | -510.000 | 1.546.720 | 3.874.077 |
| 14 | (-) Gastos Financieros (Intereses del Préstamo) | 0 | 446.400 | 314.110 | 165.945 |
| 15 | (=) Utilidad Antes de Impuestos (EBT) | -1.350.000 | 956.400 | 1.232.610 | 3.708.132 |
| 16 | (-) Impuesto a la Renta (27%) | 0 | 0 | 332.805 | 1.001.196 |
| 17 | (=) Utilidad Neta | -1.350.000 | -956.400 | 899.805 | 2.706.936 |
| 18 | (+) Ajuste por Depreciación (No desembolsable) | 0 | 780.000 | 780.000 | 780.000 |
| 19 | (+) Préstamo Bancario Recibido | 3.720.000 | 0 | 0 | 0 |
| 20 | (-) Inversiones en Activos e Intangibles | -7.440.000 | 0 | 0 | 0 |
| 21 | (-) Capital de Trabajo Inicial | -2.700.000 | 0 | 0 | 0 |
| 22 | (-) Amortización de la Deuda (Abono Capital) | 0 | 1.102.418 | 1.234.708 | 1.382.874 |
| 23 | (=) FLUJO DE CAJA NETO (FNC) | -6.420.000 | -1.278.818 | 445.097 | 2.104.062 |

*Nota.* Transcripción de la hoja «FlujoNeto» de EspaciGo.xlsx, filas 7–23. Se conservan los importes y el alcance del insumo.

**Tabla H.23.2.2**
*FlujoNeto — filas 7 a 23, parte 2*

| Fila Excel | A | F |
|---|---|---|
| 7 | Partida / Período (Años) | Año 4 (+4% IPC) |
| 8 | (+) Ingresos por Comisiones (GMV) | 46.585.000 |
| 9 | (-) Costos Variables (Comisión Pasarela) | 12.148.531 |
| 10 | (-) Costos Fijos Operativos (OPEX) | 20.247.552 |
| 11 | (-) Gastos de Administración y Marketing | 6.821.169 |
| 12 | (-) Depreciación de Activos (Maquinaria) | 0 |
| 13 | (=) Resultado Operativo (EBIT) | 7.367.748 |
| 14 | (-) Gastos Financieros (Intereses del Préstamo) | 0 |
| 15 | (=) Utilidad Antes de Impuestos (EBT) | 7.367.748 |
| 16 | (-) Impuesto a la Renta (27%) | 1.989.292 |
| 17 | (=) Utilidad Neta | 5.378.456 |
| 18 | (+) Ajuste por Depreciación (No desembolsable) | 0 |
| 19 | (+) Préstamo Bancario Recibido | 0 |
| 20 | (-) Inversiones en Activos e Intangibles | 0 |
| 21 | (-) Capital de Trabajo Inicial | 0 |
| 22 | (-) Amortización de la Deuda (Abono Capital) | 0 |
| 23 | (=) FLUJO DE CAJA NETO (FNC) | 5.378.456 |

*Nota.* Transcripción de la hoja «FlujoNeto» de EspaciGo.xlsx, filas 7–23. Se conservan los importes y el alcance del insumo.

**Tabla H.23.3.1**
*FlujoNeto — filas 29 a 45, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 29 | Partida / Período (Años) | Año 0 | Año 1 | Año 2 (+4% IPC) | Año 3 (+4% IPC) |
| 30 | (+) Ingresos por Comisiones (GMV) | 0 | 35.000.000 | 38.500.000 | 42.350.000 |
| 31 | (-) Costos Variables (Comisión Pasarela) | 0 | 10.800.000 | 11.232.000 | 11.681.280 |
| 32 | (-) Costos Fijos Operativos (OPEX) | 0 | 18.000.000 | 18.720.000 | 19.468.800 |
| 33 | (-) Gastos de Administración y Marketing | 0 | 5.930.000 | 6.221.280 | 6.545.843 |
| 34 | (-) Depreciación de Activos (Maquinaria) | 0 | 780.000 | 780.000 | 780.000 |
| 35 | (=) Resultado Operativo (EBIT) | 0 | -510.000 | 1.546.720 | 3.874.077 |
| 36 | (-) Gastos Financieros (Intereses Préstamo) | 0 | 446.400 | 314.110 | 165.945 |
| 37 | (=) Utilidad Antes de Impuestos (EBT) | 0 | -956.400 | 1.232.610 | 3.708.132 |
| 38 | (-) Impuesto a la Renta (27%) | 0 | 0 | 332.805 | 1.001.196 |
| 39 | (=) Utilidad Neta | 0 | -956.400 | 899.805 | 2.706.936 |
| 40 | (+) Ajuste por Depreciación (No desembolsable) | 0 | 780.000 | 780.000 | 780.000 |
| 41 | (+) Préstamo Bancario Recibido | 3.720.000 | 0 | 0 | 0 |
| 42 | (-) Inversiones en Activos e Intangibles | -7.440.000 | 0 | 0 | 0 |
| 43 | (-) Capital de Trabajo Inicial | -2.700.000 | 0 | 0 | 0 |
| 44 | (-) Amortización de la Deuda (Abono Capital) | 0 | 1.102.418 | 1.234.708 | 1.382.874 |
| 45 | (=) FLUJO DE CAJA NETO (FNC) | -6.420.000 | -1.278.818 | 445.097 | 2.104.062 |

*Nota.* Transcripción de la hoja «FlujoNeto» de EspaciGo.xlsx, filas 29–45. Se conservan los importes y el alcance del insumo.

**Tabla H.23.3.2**
*FlujoNeto — filas 29 a 45, parte 2*

| Fila Excel | A | F |
|---|---|---|
| 29 | Partida / Período (Años) | Año 4 (+4% IPC) |
| 30 | (+) Ingresos por Comisiones (GMV) | 46.585.000 |
| 31 | (-) Costos Variables (Comisión Pasarela) | 12.148.531 |
| 32 | (-) Costos Fijos Operativos (OPEX) | 20.247.552 |
| 33 | (-) Gastos de Administración y Marketing | 6.821.169 |
| 34 | (-) Depreciación de Activos (Maquinaria) | 0 |
| 35 | (=) Resultado Operativo (EBIT) | 7.367.748 |
| 36 | (-) Gastos Financieros (Intereses Préstamo) | 0 |
| 37 | (=) Utilidad Antes de Impuestos (EBT) | 7.367.748 |
| 38 | (-) Impuesto a la Renta (27%) | 1.989.292 |
| 39 | (=) Utilidad Neta | 5.378.456 |
| 40 | (+) Ajuste por Depreciación (No desembolsable) | 0 |
| 41 | (+) Préstamo Bancario Recibido | 0 |
| 42 | (-) Inversiones en Activos e Intangibles | 0 |
| 43 | (-) Capital de Trabajo Inicial | 0 |
| 44 | (-) Amortización de la Deuda (Abono Capital) | 0 |
| 45 | (=) FLUJO DE CAJA NETO (FNC) | 5.378.456 |

*Nota.* Transcripción de la hoja «FlujoNeto» de EspaciGo.xlsx, filas 29–45. Se conservan los importes y el alcance del insumo.

## H.24. Perspectivas fundadores

Fila 1. ESPACIGO \| TRES NIVELES DE REMUNERACION

**Tabla H.24.1**
*Perspectivas fundadores — filas 3 a 16*

| Fila Excel | A | B | C | D |
|---|---|---|---|---|
| 3 | Variable | Sin remuneracion | Reducida (base) | Original (sensibilidad) |
| 4 | Fundadores activos | 3 | 3 | 3 |
| 5 | Pago mensual por fundador | 0 | 200.000 | 400.000 |
| 6 | Pago mensual total | 0 | 600.000 | 1.200.000 |
| 7 | Pago anual total | 0 | 7.200.000 | 14.400.000 |
| 8 | Otros costos mensuales parciales | 615.912,50 | 615.912,50 | 615.912,50 |
| 9 | Costos mensuales parciales | 615.912,50 | 1.215.912,50 | 1.815.912,50 |
| 10 | Ticket promedio | 50.000 | 50.000 | 50.000 |
| 11 | Comision sobre ticket | 14,00 % | 14,00 % | 14,00 % |
| 12 | Ingreso bruto por reserva | 7.000 | 7.000 | 7.000 |
| 13 | Reservas equilibrio bruto/mes | 88 | 174 | 260 |
| 14 | Reservas actuales/mes (hipotesis) | 16 | 16 | 16 |
| 15 | Brecha de reservas/mes | 72 | 158 | 244 |
| 16 | Ingresos mensuales brutos actuales | 112.000 | 112.000 | 112.000 |

*Nota.* Transcripción de la hoja «Perspectivas fundadores» de EspaciGo.xlsx, filas 3–16. Se conservan los importes y el alcance del insumo.

Fila 18. IMPORTANTE: resultados preliminares; NO son punto de equilibrio definitivo

Fila 19. No incluye pasarela, otros costos variables, ni costos fijos sin validar.

Fila 20. Los $200.000 son una hipotesis financiera, no sueldo de mercado ni contrato laboral.

Fila 21. Los tres fundadores trabajan durante el primer ano; sin pago no significa trabajo sin valor.

Fila 22. Antes de usar como remuneracion contractual, validar obligaciones laborales y tributarias.

Fila 23. La base comercial supone 2 reservas por espacio por mes; aun no validada.

## H.25. Herramientas tesis

**Tabla H.25.1**
*Herramientas tesis — filas 1 a 10*

| Fila Excel | A | B | C | D |
|---|---|---|---|---|
| 1 | Tecnología / servicio | Uso en tesis | Costo de licencia asumido en modelo | Nota de validación |
| 2 | Go | Backend y adaptadores | 0 | Sin licencia pagada identificada |
| 3 | Next.js | Frontend y BFF | 0 | Sin licencia pagada identificada |
| 4 | PostgreSQL y PostGIS | Persistencia y geolocalización | 0 | Infraestructura/operación se cotiza aparte |
| 5 | OpenAPI | Contrato de API | 0 | Sin licencia pagada identificada |
| 6 | Docker | Contenedores | 0 | Revisar condiciones según uso y producto |
| 7 | GitHub o equivalente | Control de versiones | 0 | Plan gratuito provisional; verificar necesidades del equipo |
| 8 | Cloud Build | CI/CD | — | Consumo potencial dentro de Cloud; no sumarlo como licencia fija sin presupuesto |
| 9 | JMeter/k6 y OWASP ZAP | Pruebas | 0 | No se identificó plan pagado; verificar modalidad |
| 10 | Soporte externo | Mantenimiento contratado | — | No identificado en tesis; no presupuestar sin alcance/cotización |

*Nota.* Transcripción de la hoja «Herramientas tesis» de EspaciGo.xlsx, filas 1–10. Se conservan los importes y el alcance del insumo.

## H.26. Revision respaldo

Fila 1. ESPACIGO \| REVISIÓN DE ALMACENAMIENTO, RESPALDOS Y RECUPERACIÓN

Fila 2. Conciliación entre la hoja original Servicio respaldo, la configuración GCP reportada y la facturación observada.

Fila 3. Decisión preliminar: suspender la partida separada de $80.000/año; mantener la protección GCP dentro del presupuesto Cloud de $150.000/mes y cerrar la brecha de recuperación.

**Tabla H.26.1.1**
*Revision respaldo — filas 5 a 13, parte 1*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 5 | Elemento | Evidencia disponible | Lectura financiera/técnica | Tratamiento en el modelo | Estado |
| 6 | Cloud SQL backups | Respaldos automáticos diarios; retención 7 días. | Es una función del servicio Cloud SQL. Su costo debe estar contenido en el consumo Cloud SQL observado/proyectado, sujeto a confirmar desglose de SKU. | No crear una segunda partida de respaldo por el mismo alcance. | Configuración reportada |
| 7 | Cloud SQL PITR | PITR aparece deshabilitado en la captura. | La copia diaria no equivale a recuperación a un punto en el tiempo. La tesis exige RPO máximo 15 min y RTO máximo 1 h. | No afirmar cumplimiento del RNF-010. Evaluar habilitar PITR y presupuestar su costo incremental. | Brecha técnica |
| 8 | Cloud Storage Object Versioning | Versionado de objetos activo en bucket de aplicación. | Conserva versiones previas de objetos; puede aumentar almacenamiento facturable al retener versiones antiguas. | Considerar dentro de Cloud Storage, no como servicio externo separado. | Configuración reportada |
| 9 | Cloud Storage Soft Delete | Soft Delete de 7 días. | Protege ante eliminación accidental dentro de su ventana; no equivale a archivo histórico de largo plazo. | Considerar dentro de Cloud Storage, no sumar nuevamente. | Configuración reportada |
| 10 | Bucket de aplicación | Un bucket; aproximadamente 2,01 GB usados; ubicación Santiago. | Uso real de pruebas. La facturación Cloud Storage reporta $340 en 9 días; proyección lineal de 30 días ≈ $1.133 antes de IVA, no necesariamente consumo comercial. | Mantener dentro de Cloud GCP ($150.000/mes provisional). | Consumo observado en pruebas |
| 11 | Modelo original de respaldo | 50 MB por reserva; 3.600 reservas/año; plan 250 GB a $80.000/año. | La cantidad de reservas contradice el escenario base actual de 192 reservas/año. El proveedor del plan no está identificado. La capacidad fija de 250 GB no se justifica con el uso actual. | Suspender $80.000/año como partida independiente; valor en costo base: $0. | Suspendido provisionalmente |
| 12 | Volumen de evidencias del escenario base | 192 reservas/año × 0,05 GB = 9,6 GB/año teóricos. | Es una hipótesis de 50 MB por reserva, no una medición. No sumar automáticamente 10 GB de Cloud SQL a los GB de objetos como si fueran un mismo bucket. | Conservar como estimación técnica separada del uso observado de 2,01 GB. | Estimación no validada |
| 13 | Requisito de continuidad | RNF-010: RPO máximo 15 minutos y RTO máximo 1 hora; ensayo conjunto pendiente. | La configuración actual no demuestra el cumplimiento del requisito, especialmente con PITR deshabilitado. | Registrar brecha de implementación; no convertirla en gasto inventado. | Pendiente de aceptación |

*Nota.* Transcripción de la hoja «Revision respaldo» de EspaciGo.xlsx, filas 5–13. Se conservan los importes y el alcance del insumo.

**Tabla H.26.1.2**
*Revision respaldo — filas 5 a 13, parte 2*

| Fila Excel | A | F |
|---|---|---|
| 5 | Elemento | Pendiente para cerrar |
| 6 | Cloud SQL backups | Confirmar costo de almacenamiento de backups en el detalle de facturación y política de retención. |
| 7 | Cloud SQL PITR | Habilitar o justificar alternativa; ejecutar restauración y medir RPO/RTO. |
| 8 | Cloud Storage Object Versioning | Definir ciclo de vida, limpieza y retención de versiones. |
| 9 | Cloud Storage Soft Delete | Confirmar alcance y costo según objetos recuperables. |
| 10 | Bucket de aplicación | Validar si el volumen incluye datos de prueba y medir crecimiento real por reserva. |
| 11 | Modelo original de respaldo | Solo reactivar si se contrata un proveedor o una solución independiente con alcance y cotización. |
| 12 | Volumen de evidencias del escenario base | Medir tamaño medio real de fotos/documentos por reserva y política de retención. |
| 13 | Requisito de continuidad | Prueba de restauración conjunta de PostgreSQL y objetos privados; documentar resultados. |

*Nota.* Transcripción de la hoja «Revision respaldo» de EspaciGo.xlsx, filas 5–13. Se conservan los importes y el alcance del insumo.

Fila 16. COMPROBACIONES CUANTITATIVAS

**Tabla H.26.2**
*Revision respaldo — filas 17 a 24*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 17 | Reservas anuales escenario base | 192 | reservas/año | Supuestos comerciales actuales | Hipótesis; frecuencia no validada |
| 18 | Tamaño estimado por reserva | 0,05 | GB/reserva | Hoja Servicio respaldo | Supuesto no medido |
| 19 | Evidencias estimadas por año | 9,60 | GB/año | 192 × 0,05 | 9,6 GB/año teóricos |
| 20 | Bucket observado actualmente | 2,01 | GB | Informe técnico GCP | Uso de pruebas; no equivale a crecimiento anual |
| 21 | Cloud Storage facturado en 9 días | 340 | CLP | CSV de Billing | Costo bruto observado; cubierto por créditos |
| 22 | Proyección lineal a 30 días | 1.133,33 | CLP/mes | Solo referencia de consumo actual | No extrapolar como costo comercial definitivo |
| 23 | Partida separada de respaldo original | 80.000 | CLP/año | Excel original | Se suspende para escenario base |
| 24 | Partida separada de respaldo aprobada | 0 | CLP/año | Decisión de conciliación | No hay servicio independiente acreditado |

*Nota.* Transcripción de la hoja «Revision respaldo» de EspaciGo.xlsx, filas 17–24. Se conservan los importes y el alcance del insumo.

Fila 27. DECISIÓN PARA EL MODELO FINANCIERO

**Tabla H.26.3**
*Revision respaldo — filas 28 a 30*

| Fila Excel | A | B | C | D |
|---|---|---|---|---|
| 28 | Partida 'Servicio de respaldo' independiente | 0 | CLP/año | Suspendida provisionalmente |
| 29 | Infraestructura GCP | 150.000 | CLP/mes | Se mantiene presupuesto provisional integrado: incluye servicios cloud observados y funciones de protección configuradas. |
| 30 | Brecha RNF-010 | Pendiente | — | PITR y restauración conjunta deben validarse; cualquier costo incremental se agregará después de cotizar/configurar. |

*Nota.* Transcripción de la hoja «Revision respaldo» de EspaciGo.xlsx, filas 28–30. Se conservan los importes y el alcance del insumo.


## H.27. Umbrales y regla de asignaciones adoptados

Este apartado respalda las Tablas 24 y 25. El presupuesto medio identificado es CLP 514.003,02. A ticket de CLP 50.000, los umbrales promedio siguen siendo 743 y 2.343 pagos para las dos metas por persona. La caja del mes puede no permitirlas, aunque el promedio las cubra: enero paga anualidades y el lanzamiento tiene comisión por cobrar.

La regla verifica recaudación del mes menos OPEX pagado, reserva de cuota y provisión académica de impuesto después de la meta; en estrés también reserva CLP 25.000 durante 36 meses para reposición. Si alcanza, paga la meta completa; en otro caso paga cero. Las reservas no se suman a los egresos de caja ya registrados por sus conceptos. La provisión no utiliza pérdidas fiscales para aumentar disponibilidad; el impuesto anual sí concilia las pérdidas del ejercicio académico. No se presupone relación laboral formal ni costo económico cero del trabajo.

## H.28. Supuesto fiscal académico y calendario de evaluación

La empresa aún no se constituye. La preparación mantiene Pro Pyme General como régimen proyectado, sin afirmar inscripción vigente ante el SII. La actividad se modela como intermediación: los publicadores arriendan sus espacios y la plataforma cobra su comisión. Para el cálculo académico se conserva el impuesto fijo del 27 % utilizado por Anita, según la instrucción docente comunicada por el propietario. Esta elección metodológica no se presenta como tasa legal del régimen proyectado.

**Tabla H.28.1**
*Tasa de impuesto adoptada para el ejercicio académico*

| Período | Año comercial | Año tributario | Tasa académica |
|---|---|---|---|
| 1 | 2027 | 2028 | 27 % |
| 2 | 2028 | 2029 | 27 % |
| 3 | 2029 | 2030 | 27 % |
| 4 | 2030 | 2031 | 27 % |

*Nota.* Elaboración a partir del modelo de Anita y del criterio docente comunicado por el propietario el 16 de noviembre de 2026. Se utiliza 27 % fijo como supuesto de evaluación académica. El Año 0 de preparación corresponde a 2026. La tabla no constituye una determinación de la tasa legal aplicable al régimen proyectado.

El flujo conserva las columnas, partidas y secuencia de Anita. El impuesto se calcula sobre la base de resultados y ajustes del ejercicio, considerando las pérdidas que correspondan al modelo. Los fondos de terceros y el IVA se separan del ingreso propio. El trabajo valorizado, la depreciación y los desembolsos se concilian para evitar doble conteo. La simulación adoptada completa las fechas y partidas definidas; las condiciones reales no respaldadas permanecen identificadas.

La tasa de descuento del ejercicio es 12 % nominal anual, según confirmación de Anita comunicada por el propietario. Se distingue del impuesto fijo del 27 % y de la comisión del 3 % más IVA. El interés del préstamo simulado también es 12 %, pero no se confunde con la rentabilidad mínima de evaluación. El 10 % y el 25 % dejan de utilizarse como tasas principales. El Anexo H.29 fundamenta la elección metodológica y el alcance del criterio.

Fuentes del supuesto académico: informe de Anita, sección 5.3; hoja FlujoNeto, A29:F45; instrucción del propietario del 16 de noviembre de 2026. Los parámetros se conservan en 02_contraste/parametros_tributarios.json. El contraste legal anterior permanece identificado como antecedente no aplicado al cálculo académico, para no confundirlo con el criterio adoptado.


## H.29. Fundamentación de la tasa de descuento adoptada

El ejercicio adopta 12 % nominal anual como tasa de descuento, según confirmación de Anita y ratificación del propietario del 16 de noviembre de 2026. Esta decisión sustituye el criterio previo del 25 % y fija una sola tasa base para los indicadores y escenarios de la preparación actualizada. El 10 % mencionado en el informe original se conserva como antecedente y prueba de sensibilidad, sin utilizarlo como criterio principal.

La elección se fundamenta metodológicamente en mantener la tasa de referencia del estudio económico aportado y comparar los escenarios bajo una rentabilidad mínima común. La tasa se aplica con periodicidad anual y en términos nominales, coherentes con flujos que incorporan los reajustes de precios y costos definidos por el modelo. El valor del VAN es la suma de cada flujo anual dividido por (1 + 0,12) elevado al número de período; el flujo del Año 0 no se descuenta. El escenario adoptado añade el cobro posterior de comisión en su momento 4 + días/360. H.38 distingue el VAN sin liquidación, el VAN con liquidación y el control mensual.

La fuente recibida no deriva el 12 % a partir de un modelo propio de costo de capital. La confirmación de la autora acredita el parámetro elegido y no una estimación empírica del riesgo. Sapag exige distinguir rentabilidad del proyecto, rentabilidad del inversionista y capacidad de pago, y relaciona el costo de capital con alternativas de riesgo comparable (Sapag Chain & Sapag Chain, 2008, pp. 5–6, 343–345, 353–356). El marco metodológico exige distinguir el flujo para los socios del flujo del proyecto y usar una tasa apropiada al destinatario del flujo. El estudio mantiene esa distinción al separar inversión, costo de oportunidad y financiamiento simulado. No se inventan primas de riesgo para obtener el porcentaje adoptado.

La coincidencia entre descuento del 12 % e interés del préstamo del 12 % no implica que sean el mismo concepto. El primero es la rentabilidad mínima de referencia para evaluar; el segundo corresponde al servicio de una deuda simulada. La incertidumbre comercial y tecnológica se examina con sensibilidad de demanda, precio, gastos y tasa. Un descuento menor no reduce el riesgo operativo ni aumenta por sí mismo las ventas: modifica el valor presente asignado a los flujos esperados.

El crecimiento en años posteriores se incorpora mediante cobros, comisiones y costos proyectados con sustento. El horizonte actual conserva los Años 0 a 4 del formato de Anita. Una eventual extensión al Año 5 requiere un escenario explícito, incluyendo capital de trabajo y demás partidas; no se añade un año o valor terminal únicamente para obtener un VAN positivo.

Sobre el vector original [−6.420.000, −1.278.818, 445.097, 2.104.062, 5.378.456], el VAN al 12 % es CLP −2.291.237,39 y la TIR es aproximadamente 0,85115 %. Son comprobaciones históricas y no resultados de la simulación adoptada. Para un flujo convencional de inversión, el criterio compara VAN con cero y TIR con el 12 %; si no existe TIR interpretable o hay múltiples soluciones, se informa esa condición.

Fuentes: informe de Anita, sección 5.3; confirmación de la autora comunicada por el propietario el 16 de noviembre de 2026; Sapag Chain y Sapag Chain (2008, pp. 321–323, 335–336, 343–356). El libro respalda el método y la correspondencia entre flujos y tasas; no prescribe un 12 % para espaciGo. El ejemplo del libro que utiliza 12 % en la página 296 es un caso ilustrativo, no una tasa general obligatoria.

## H.30. Aplicación metodológica y alcance

La preparación utiliza Sapag Chain y Sapag Chain (2008), quinta edición. La referencia diferencia rentabilidad del proyecto, de los socios y capacidad de servicio de deuda; clasifica inversión, costos pertinentes, capital del ciclo y valor final (pp. 5–6, 126, 259–269, 277–282, 291–298). Los indicadores se calculan por flujos y fechas coherentes, distinguiendo recuperación nominal y descontada (pp. 321–323, 329–330).

Las hipótesis elegidas permiten terminar la simulación académica sin denominarlas demanda observada, facturas, contratos o tasas de mercado estimadas. Las salidas de partidas desconocidas quedan fuera de su alcance. Los originales H.1–H.26 conservan diferencias históricas de GCP, porcentajes y recursos para el contraste solicitado; los cálculos vigentes de H.27–H.40 utilizan el nuevo escenario. Los cortes calculados anteriores se conservan en el historial de preparación y en Git, separados de los resultados activos.

Referencia: Sapag Chain, N., & Sapag Chain, R. (2008). Preparación y evaluación de proyectos (5.ª ed.). McGraw-Hill Interamericana. En la copia aportada, la página PDF equivale a la impresa más 18.

## H.31. Referencia comercial y plan de validación

Se conservan ocho espacios activos promedio, dos pagos por espacio y mes y ticket de CLP 50.000. Las nueve categorías son catálogo disponible; no se reparten los ocho espacios ni se atribuyen ventas a todas ellas sin evidencia. El crecimiento de cobros y precio se mantiene en cero como referencia, y no como certeza comercial.

**Tabla H.31.1**
*Categorías y evidencia por recopilar*

| ID | Categoría | Estado de oferta y pagos |
|---|---|---|
| 1 | Oficina | Por validar con fichas y pagos observados |
| 2 | Sala multipropósito | Por validar con fichas y pagos observados |
| 3 | Bodega | Por validar con fichas y pagos observados |
| 4 | Estacionamiento | Por validar con fichas y pagos observados |
| 5 | Local flexible | Por validar con fichas y pagos observados |
| 6 | Stand | Por validar con fichas y pagos observados |
| 7 | Quincho | Por validar con fichas y pagos observados |
| 8 | Parcela de eventos | Por validar con fichas y pagos observados |
| 9 | Inmuebles | Por validar con fichas y pagos observados |

*Nota.* Catálogo indicado por el propietario. Los registros vacíos no se sustituyen por ceros observados.

**Tabla H.31.2**
*Objetivos exploratorios de validación*

| Registro | Objetivo | Evidencia disponible |
|---|---|---|
| Fichas de oferta | 8 | Sin fichas de campo en esta preparación |
| Entrevistas a publicadores | 10 | Objetivo, no entrevistas realizadas |
| Entrevistas a arrendatarios | 20 | Objetivo, sin representatividad estadística atribuida |

*Nota.* El piloto observa enero-marzo de 2027. Se registra categoría, modalidad, disponibilidad, precio, pagos completos, devoluciones, GMV y recurrencia. Una intención no equivale a un pago. Los datos generales del INE sobre alojamiento solo contextualizan ese segmento, no la captación ni todas las categorías.

## H.32. Costos y lanzamiento adoptados

**Tabla H.32.1**
*Componentes del Año 1*

| ID | Componente | Promedio mensual CLP | Presupuesto anual CLP |
|---|---|---|---|
| C01 | AWS | 25.670,52 | 308.046,24 |
| C02 | Firma y API | 50.000,00 | 600.000,00 |
| C03 | Marketing | 350.000,00 | 4.200.000,00 |
| C04 | Contabilidad | 50.000,00 | 600.000,00 |
| C05 | Dominio | 832,50 | 9.990,00 |
| C06 | Coordinación | 15.000,00 | 180.000,00 |
| C07 | Útiles de oficina | 10.000,00 | 120.000,00 |
| C08 | Dirección tributaria | 12.500,00 | 150.000,00 |
| Total | Subtotal identificado | 514.003,02 | 6.168.036,24 |

*Nota.* Presupuestos originales conciliados sin duplicar subtotales, más dirección tributaria ratificada. El dominio usa la tarifa pública NIC directo. Los servicios siguen sin contratación acreditada. Útiles y dirección se contabilizan una vez.

NIC Chile publica CLP 9.990 por año .cl, exento de IVA, consultado el 16 de noviembre de 2026: https://www.nic.cl/dominios/tarifas.html. Se asume continuidad para 2027 y reajuste presupuestario posterior del 4 %; no se garantiza la tarifa futura. El presupuesto cloud conserva USD 26,41 del perfil piloto Single-AZ de la propuesta interna, convertido a 972 CLP/USD. La descripción Multi-AZ con balanceador del README requiere presupuesto separado; el importe piloto no acredita ese alcance o capacidad de carga. No se verifica facturación AWS ni se aplican créditos sin evidencia de vigencia.

**Tabla H.32.2**
*Desglose presupuestario de lanzamiento*

| Componente | CLP |
|---|---|
| Formalización y asesoría | 300.000 |
| Contenidos y materiales | 300.000 |
| Campaña previa | 400.000 |
| Contingencia preoperativa | 200.000 |
| Total | 1.200.000 |

*Nota.* Asignaciones del presupuesto, no cotizaciones o gastos realizados. La campaña previa corresponde al Año 0 y se distingue del marketing operativo de 2027. El caso máximo utiliza todo el presupuesto en el Año 0; un margen no ejecutado se ajusta cuando existe evidencia. No se suma otra constitución por separado.

## H.33. Devengo, pagos y comisión por cobrar

El dominio y la dirección tributaria se pagan en enero de cada año; los demás componentes se distribuyen mensualmente, conciliando centavos en el último mes. El gasto devengado permite calcular resultado e impuesto; el calendario pagado determina caja. Los importes CLP aumentan 4 % al año y AWS permanece constante en los USD y cambio adoptados.

Para la comisión se adopta siete días y mes de treinta días. Saldo por cobrar = comisión mensual devengada × días/30. Cobro del mes = comisión devengada + saldo inicial por cobrar − saldo final por cobrar. No se agregan otra vez esos saldos al Año 0 como capital de trabajo. Se mide un componente del ciclo; IVA de compras, retenciones y condiciones reales sin respaldo no se convierten en cifras confirmadas.

**Tabla H.33.1**
*Calendario de los primeros tres meses*

| Mes | Comisión cobrada CLP | OPEX pagado CLP | CxC final CLP | Flujo neto CLP |
|---|---|---|---|---|
| 2027-01 | 18.400,00 | 660.660,52 | 5.600,00 | -642.260,52 |
| 2027-02 | 24.000,00 | 500.670,52 | 5.600,00 | -476.670,52 |
| 2027-03 | 24.000,00 | 500.670,52 | 5.600,00 | -476.670,52 |

*Nota.* Referencia sin deuda ni asignaciones pagadas. El IVA de la comisión y los fondos de publicadores se mantienen fuera de caja libre. El abono final al publicador no se determina sin tarifa de pasarela. Las fechas son convenciones de simulación, no facturas o plazos contratados.

La última comisión por cobrar se cobra siete días después del corte de diciembre de 2030. En estrés se utilizan treinta días. La Tabla 22 muestra ambos saldos. Este cobro liquida operaciones del horizonte y no supone un quinto año de nuevos arriendos. Para el descuento, la fecha financiera es 4 + días/360. La documentación de Split 1:1 no confirma el plazo particular de espaciGo; se mantiene como hipótesis adoptada.

## H.34. Servicio de la deuda simulada

**Tabla H.34.1**
*Amortización hasta saldo cero*

| Año | Saldo inicial CLP | Interés CLP | Capital CLP | Cuota CLP | Saldo final CLP |
|---|---|---|---|---|---|
| 1 | 3.720.000 | 446.400 | 1.102.418 | 1.548.818 | 2.617.582 |
| 2 | 2.617.582 | 314.110 | 1.234.708 | 1.548.818 | 1.382.874 |
| 3 | 1.382.874 | 165.945 | 1.382.874 | 1.548.819 | 0 |

*Nota.* Principal CLP 3.720.000, interés 12 % y tres cuotas anuales. La última suma CLP 1 por redondeo. No se acredita contratación, seguros o comisiones financieras. El capital amortizado coincide con el recibido.

## H.35. Conciliación demostrativa de pérdidas históricas

Esta comprobación conserva el 27 % y aplica el criterio de compensar pérdidas que describe el informe de Anita. Supone pérdidas iniciales cero y utiliza solo el EBT del bloque histórico corregido. No determina una base fiscal real ni reemplaza la conciliación del escenario actualizado.

**Tabla H.35.1**
*Impuesto histórico frente a compensación de pérdidas del ejercicio*

| Año | EBT CLP | Pérdida compensada CLP | Impuesto fuente CLP | Impuesto recalculado CLP | Diferencia CLP |
|---|---|---|---|---|---|
| 1 | -956.400 | 0 | 0 | 0 | 0 |
| 2 | 1.232.610 | 956.400 | 332.805 | 74.577 | 258.228 |
| 3 | 3.708.132 | 0 | 1.001.196 | 1.001.196 | 0 |
| 4 | 7.367.748 | 0 | 1.989.292 | 1.989.292 | 0 |

*Nota.* En el Año 2, CLP 1.232.610 menos CLP 956.400 deja una base de CLP 276.210. Al 27 %, el impuesto es CLP 74.576,70, redondeado a CLP 74.577. La diferencia con CLP 332.805 del origen es CLP 258.228. La corrección concilia la explicación con la tabla bajo este supuesto, sin alterar la extracción original.

## H.36. Sensibilidad y quiebres de VAN

**Tabla H.36.1**
*Sensibilidad desde la misma referencia*

| Variable | Prueba | VAN con liquidación CLP | Cambio CLP |
|---|---|---|---|
| Cobros | -20 % | -20.228.062 | -174.662 |
| Cobros | 20 % | -19.878.739 | 174.662 |
| Ticket | -20 % | -20.228.062 | -174.662 |
| Ticket | 20 % | -19.878.739 | 174.662 |
| Costos | -20 % | -16.108.059 | 3.945.342 |
| Costos | 20 % | -23.998.742 | -3.945.342 |
| CLP/USD | -20 % | -19.866.272 | 187.129 |
| CLP/USD | 20 % | -20.240.529 | -187.129 |
| Descuento | 10 % anual | -20.892.938 | -839.537 |
| Descuento | 12 % anual | -20.053.400 | 0 |
| Descuento | 25 % anual | -15.783.036 | 4.270.364 |

*Nota.* Pruebas deterministas sin probabilidades. Se altera una variable cada vez y se conserva la comisión del 3 %. El cambio afecta solo AWS; los rangos no acreditan capacidad de escalamiento. Cambiar descuento no modifica el riesgo ni las ventas.

**Tabla H.36.2**
*Primer entero de pagos mensuales con VAN no negativo*

| Meta por persona | Pagos al mes | VAN con un pago menos CLP | VAN con el mínimo CLP |
|---|---|---|---|
| Sin asignaciones | 392 | -30.794,00 | 9.026,21 |
| $200.000 | 793 | -27.197,10 | 12.623,11 |
| $1.000.000 | 2.397 | -12.809,51 | 27.010,70 |

*Nota.* Ticket CLP 50.000. Incluye liquidación diferida y descuento 12 %. La búsqueda usa escenarios de asignaciones fijas para evitar saltos de la regla condicionada. Los mínimos son analíticos y no demanda proyectada. Se mantienen fuera costos residuales y escalamiento.

**Tabla H.36.3**
*Escenarios comerciales de Anita con comisión común del 3 %*

| Escenario | Pagos al mes | Ticket CLP | VAN con liquidación CLP |
|---|---|---|---|
| conservador | 4 | 35.000 | -20.773.879 |
| base | 16 | 50.000 | -20.053.400 |
| optimista | 45 | 65.000 | -17.733.677 |

*Nota.* Se conservan los volúmenes y tickets del insumo y se aplican el mismo calendario y la comisión del 3 %. No son probabilidades ni ventas observadas. Se mantiene el costo piloto sin validar capacidad de escalamiento. La fila base coincide con la referencia adoptada.

## H.37. Aportes mínimos y cobertura de cuotas

Se recorren los 49 momentos de caja, incluido Año 0. Aporte mínimo = máximo entre cero y reserva objetivo menos caja antes del aporte. Se acumula la reserva de cuota durante cada año y la de reposición hasta la compra; al pagar se libera el monto reservado. La suma se concilia con el déficit máximo respecto de ese piso de liquidez, sin restar las reservas de nuevo como gasto. En la referencia sin reservas, el piso es cero. Después se cobra la cuenta pendiente, dejando caja al corte ampliado; ese retorno no borra los déficits que antes requieren financiamiento.

**Tabla H.37.1**
*Aportes y caja después de la liquidación*

| Escenario | Aporte mínimo acumulado CLP | CxC liquidada CLP | Caja final con aportes CLP |
|---|---|---|---|
| Base sin deuda | 26.170.021,53 | 5.600,00 | 5.600,00 |
| Base financiado | 27.096.476,53 | 5.600,00 | 5.600,00 |
| Reposición 2029 | 27.070.021,53 | 5.600,00 | 5.600,00 |
| Cobro a 30 días | 26.188.421,53 | 24.000,00 | 24.000,00 |

*Nota.* Aportes no confirmados. La alternativa financiada incluye su préstamo antes de calcular necesidades adicionales. La liquidación de comisión recupera un activo del ciclo; no es beneficio operativo adicional ni una venta de equipos.

**Tabla H.37.2**
*Cobertura propia antes de cuotas*

| Año | Caja antes de cuota CLP | Cuota CLP | Cobertura veces |
|---|---|---|---|
| 2027 | -5.885.636 | 1.548.818 | -3,800 |
| 2028 | -6.114.436 | 1.548.818 | -3,948 |
| 2029 | -6.358.211 | 1.548.819 | -4,105 |
| 2030 | -6.611.738 | 0 | No aplica |

*Nota.* Caja propia cobrada menos OPEX, asignaciones e impuesto, dividida por intereses más capital cuando hay cuota. Un resultado negativo no acredita capacidad propia de pago, aunque existan aportes o un préstamo inicial.

## H.38. Indicadores y fechas

El VAN rector considera los cierres anuales del formato docente y la comisión liquidada en su fecha diferida. No se adelanta esa recuperación al último cierre anual. Se informa además un control que descuenta cada importe mensual con (1 + 0,12) elevado a período/12, y la liquidación con su momento en años. La diferencia responde a fechas de egresos e ingresos, no a dos tasas base.

**Tabla H.38.1**
*Convenciones de valoración del caso de referencia*

| Cálculo | VAN CLP |
|---|---|
| Operación hasta diciembre de 2030 | -20.056.951,52 |
| Cierres anuales más liquidación | -20.053.400,45 |
| Control mensual más liquidación | -21.098.116,97 |

*Nota.* Los tres importes corresponden a convenciones identificadas de la misma referencia. Las raíces de H.36 utilizan cierres anuales más liquidación, al igual que la Tabla 23. No se comparan como si tuvieran las mismas fechas.

En la referencia, los flujos operativos son negativos. Añadir el cobro final del pequeño saldo por cobrar genera una entrada positiva tardía, pero no se publica una raíz negativa extrema como indicador útil de inversión. El VAN y la ausencia de recuperación dentro del horizonte ampliado describen su resultado. El patrón de la alternativa financiada tampoco es una inversión convencional.

**Tabla H.38.2**
*Recuperación de los volúmenes de quiebre*

| Escenario | Pagos al mes | Recuperación simple años | Recuperación descontada años |
|---|---|---|---|
| Sin asignaciones | 392 | 2,708 | 4,017 |
| Meta $200.000 | 793 | 3,107 | 4,018 |
| Meta $1.000.000 | 2.397 | 4,006 | 4,018 |

*Nota.* Interpolación auxiliar entre momentos anuales y, si corresponde, liquidación. No es fecha contractual. La referencia y los dos estreses no recuperan la inversión; las metas de quiebre no acreditan oferta, adquisición de usuarios o costos completos de operación.

## H.39. Reposición y cierre prudente

Los equipos existentes permanecen personales y compartidos. La referencia no compra ni vende esos bienes como si fueran propiedad de la empresa. El estrés sí programa una nueva compra de CLP 900.000 en 2029, sin deducción o depreciación fiscal atribuida. El importe deriva del notebook de CLP 800.000 del insumo, reajustado con el supuesto del 4 % durante tres años y redondeado presupuestariamente; no es cotización futura.

La reserva objetivo de CLP 25.000 durante 36 meses mantiene un piso de liquidez para la compra y restringe asignaciones. Si la operación no la financia, el calendario de aportes cubre ese piso. No es gasto adicional y se libera al pagar la adquisición. La salida de caja se registra una vez al adquirir. El caso prudente establece cero cobro por venta de activos y software y no incorpora perpetuidad. No se afirma que la empresa o sus activos valgan cero. Sapag diferencia valoración de desecho de caja disponible (2008, pp. 277–282, 292–295).

El capital modelado de comisión por cobrar ya está en el flujo por variación de saldos y se recupera en su fecha diferida. No se recuperan pérdidas persistentes como si fueran un activo. El resto del ciclo —IVA de compras, retenciones, devoluciones y proveedores— exige evidencia para una evaluación operativa real; no se confirma por adoptar esta simulación.

## H.40. Desarrollo, decisiones y trazabilidad

El cronograma académico vigente asigna 632 horas entre el 11 de agosto y el 30 de noviembre de 2026. La capacidad nominal del bloque es de 960 horas, equivalente a 320 por integrante y veinte horas semanales durante dieciséis semanas. A CLP 6.500 por hora, el presupuesto valorizado asciende a CLP 6.240.000. No existen horas reales acreditadas; el importe no representa remuneraciones ni egreso de caja.

Después del bloque académico se asignan 36 horas a la defensa y 40 horas a la transición preoperativa, para un total de 708 horas. La reserva presupuestaria es de 252 horas, equivalente a CLP 1.638.000, mientras que el valor de las horas asignadas asciende a CLP 4.602.000. La capacidad nominal base libre es de 328 horas, 76 horas superior a la reserva, porque esta última también descuenta las actividades posteriores a la entrega. La transición se programa del 10 al 31 de diciembre y la operación comienza el 1 de enero de 2027. El registro no acredita ejecución ni pago.

**Tabla H.40.1**
*Quiebre al exigir recuperar también la valorización global*

| Meta por persona | Pagos al mes | VAN con un pago menos CLP | VAN con el mínimo CLP |
|---|---|---|---|
| Sin asignaciones | 549 | -19.020,69 | 20.799,52 |
| $200.000 | 950 | -15.423,80 | 24.396,42 |
| $1.000.000 | 2.554 | -1.036,20 | 38.784,01 |

*Nota.* La prueba añade CLP 6.240.000 una vez al momento cero, sin deducción fiscal ni incorporación a aportes de efectivo. No estima el costo de oportunidad incremental a la fecha de decisión. Los flujos de caja de las Tablas 18–21 permanecen separados de esa valorización.
