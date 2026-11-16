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


## H.27. Memoria actualizada de las metas de remuneración

Este apartado respalda las Tablas 20 y 21 y se actualiza con la conciliación de útiles de oficina. Los cálculos anteriores sin esa partida son un corte histórico. Se conserva su procedencia en la historia del repositorio.

El presupuesto mensual sin fundadores es CLP 514.083,02: la base parcial de CLP 491.583,02 más CLP 10.000 de útiles y CLP 12.500 de dirección tributaria. Los útiles proceden de Conciliacion costos!H9 y la periodicidad anual de la dirección es ratificada por el propietario. Con la meta conjunta inicial de CLP 600.000, se requieren CLP 1.114.083,02 de comisión neta. A ticket de CLP 50.000 y comisión neta de CLP 1.500 por cobro, el mínimo entero es 743 pagos: 742 producen CLP 1.113.000 y no alcanzan; 743 producen CLP 1.114.500. Para CLP 1.000.000 por fundador, el mínimo es 2.343 pagos.

El cálculo redondea hacia arriba (costo parcial + tres asignaciones objetivo) dividido por (ticket multiplicado por 0,03). Los costos variables propios que se determinen reducen la contribución por cobro. El script calcular_tickets_remuneraciones.py lee los componentes y genera umbrales_remuneraciones.json y umbral_sueldo_objetivo.json. La comparación con fuente y las proyecciones se documentan en H.31–H.35.

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

El flujo conserva las columnas, partidas y secuencia de Anita. El impuesto se calcula sobre la base de resultados y ajustes del ejercicio, considerando las pérdidas que correspondan al modelo. Los fondos de terceros y el IVA se separan del ingreso propio. El trabajo valorizado, la depreciación y los desembolsos se concilian para evitar doble conteo. La serie definitiva y sus indicadores requieren cerrar los demás parámetros pendientes.

La tasa de descuento del ejercicio es 12 % nominal anual, según confirmación de Anita comunicada por el propietario. Se distingue del impuesto fijo del 27 % y de la comisión del 3 % más IVA. El interés del préstamo simulado también es 12 %, pero no se confunde con la rentabilidad mínima de evaluación. El 10 % y el 25 % dejan de utilizarse como tasas principales. El Anexo H.29 fundamenta la elección metodológica y el alcance del criterio.

Fuentes del supuesto académico: informe de Anita, sección 5.3; hoja FlujoNeto, A29:F45; instrucción del propietario del 16 de noviembre de 2026. Los parámetros se conservan en 02_contraste/parametros_tributarios.json. El contraste legal anterior permanece identificado como antecedente no aplicado al cálculo académico, para no confundirlo con el criterio adoptado.


## H.29. Fundamentación de la tasa de descuento adoptada

El ejercicio adopta 12 % nominal anual como tasa de descuento, según confirmación de Anita y ratificación del propietario del 16 de noviembre de 2026. Esta decisión sustituye el criterio previo del 25 % y fija una sola tasa base para los indicadores y escenarios de la preparación actualizada. El 10 % mencionado en el informe original se conserva únicamente en la extracción histórica, sin utilizarlo como criterio principal.

La elección se fundamenta metodológicamente en mantener la tasa de referencia del estudio económico aportado y comparar los escenarios bajo una rentabilidad mínima común. La tasa se aplica con periodicidad anual y en términos nominales, coherentes con flujos que incorporan los reajustes de precios y costos definidos por el modelo. El valor del VAN es la suma de cada flujo anual dividido por (1 + 0,12) elevado al número de período; el flujo del Año 0 no se descuenta.

La fuente recibida no deriva el 12 % a partir de un modelo propio de costo de capital. La confirmación de la autora acredita el parámetro elegido y no una estimación empírica del riesgo. Sapag exige distinguir rentabilidad del proyecto, rentabilidad del inversionista y capacidad de pago, y relaciona el costo de capital con alternativas de riesgo comparable (Sapag Chain & Sapag Chain, 2008, pp. 5–6, 343–345, 353–356). El marco metodológico exige distinguir el flujo para los socios del flujo del proyecto y usar una tasa apropiada al destinatario del flujo. El estudio mantiene esa distinción al separar inversión, costo de oportunidad y financiamiento simulado. No se inventan primas de riesgo para obtener el porcentaje adoptado.

La coincidencia entre descuento del 12 % e interés del préstamo del 12 % no implica que sean el mismo concepto. El primero es la rentabilidad mínima de referencia para evaluar; el segundo corresponde al servicio de una deuda simulada. La incertidumbre comercial y tecnológica se examina con sensibilidad de demanda, precio, gastos y tasa. Un descuento menor no reduce el riesgo operativo ni aumenta por sí mismo las ventas: modifica el valor presente asignado a los flujos esperados.

El crecimiento en años posteriores se incorpora mediante cobros, comisiones y costos proyectados con sustento. El horizonte actual conserva los Años 0 a 4 del formato de Anita. Una eventual extensión al Año 5 requiere un escenario explícito, incluyendo capital de trabajo y demás partidas; no se añade un año o valor terminal únicamente para obtener un VAN positivo.

Sobre el vector original [−6.420.000, −1.278.818, 445.097, 2.104.062, 5.378.456], el VAN al 12 % es CLP −2.291.237,39 y la TIR es aproximadamente 0,85115 %. Son comprobaciones históricas y no resultados del flujo nuevo pendiente de cierre. Para un flujo convencional de inversión, el criterio compara VAN con cero y TIR con el 12 %; si no existe TIR interpretable o hay múltiples soluciones, se informa esa condición.

Fuentes: informe de Anita, sección 5.3; confirmación de la autora comunicada por el propietario el 16 de noviembre de 2026; Sapag Chain y Sapag Chain (2008, pp. 321–323, 335–336, 343–356). El libro respalda el método y la correspondencia entre flujos y tasas; no prescribe un 12 % para espaciGo. El ejemplo del libro que utiliza 12 % en la página 296 es un caso ilustrativo, no una tasa general obligatoria.

## H.30. Aplicación del método de Sapag al formato económico

### H.30.1. Fuente y alcance

La preparación utiliza como referencia principal Sapag Chain y Sapag Chain (2008), quinta edición. Las páginas citadas corresponden a la numeración impresa; en la copia local la página PDF equivale a la impresa más 18. El método se adapta a la intermediación digital y no impone partidas industriales que no correspondan al proyecto. La evaluación privada se concentra en los flujos de inversión, operación y financiamiento; no se presenta como evaluación social completa.

### H.30.2. Correspondencia del flujo

**Tabla H.30.1**
*Correspondencia entre la estructura de Sapag y el flujo de Anita*

| ID | Bloque metodológico | Aplicación al formato recibido | Respaldo impreso |
|---|---|---|---|
| 1 | Ingresos y egresos afectos | Comisiones y costos propios; separar IVA y arriendos de terceros. | pp. 293–294 |
| 2 | Gastos no desembolsables | Depreciación y amortización: efecto fiscal y ajuste de caja. | pp. 293–297 |
| 3 | Impuesto y resultado | 27 % académico; conciliar base y pérdidas. | pp. 293–297 |
| 4 | Ajustes de caja | Reincorporar gastos sin desembolso; evitar duplicidades. | pp. 294–297 |
| 5 | Inversión y capital de trabajo | Aportes iniciales, reinversión y capital de trabajo. | pp. 259–269, 295 |
| 6 | Cierre del horizonte | Valor de desecho y recuperación sin duplicaciones. | pp. 277–282, 295 |
| 7 | Flujo del inversionista | Préstamo, interés antes de impuesto y principal después. | pp. 297–298 |

*Nota.* Elaboración propia a partir de Sapag Chain y Sapag Chain (2008). La tabla relaciona conceptos y conserva la secuencia del flujo de Anita. Las cifras originales se mantienen como antecedentes; la equivalencia metodológica no certifica sus supuestos ni la viabilidad del escenario actualizado.

### H.30.3. Inversión y costos pertinentes

La memoria de recursos distingue desembolso incremental futuro, pago irreversible ya comprometido y costo de oportunidad con uso alternativo. No se elimina todo trabajo valorizado por no ser efectivo ni se agrega a caja como si fuera una compra pagada. La clasificación se realiza a la fecha de decisión y se vincula con cada recurso. Se concilian equipos aportados, compras, depreciación y reposición durante la operación (Sapag Chain & Sapag Chain, 2008, pp. 126, 259–262, 269).

### H.30.4. Calendario y capital de trabajo

El método propuesto de déficit acumulado máximo calcula cobros y pagos mensuales, antes de aportes de financiamiento, y determina la máxima necesidad de recursos acumulada. Su aplicación requiere identificar rezagos, estacionalidad y el ciclo de liquidación. La inversión y los gastos de preparación se registran por separado para no financiarlos dos veces. Los arriendos de terceros y el IVA no se convierten en caja libre del negocio. La falta persistente de ingresos para cubrir operación también debe explicarse como necesidad de financiamiento de pérdidas (Sapag Chain & Sapag Chain, 2008, pp. 134–135, 262, 267–269).

### H.30.5. Horizonte y valor de cierre

El caso base conserva cuatro años de operación y un Año 0 de preparación. La evaluación debe resolver el valor remanente de activos o de continuidad y justificar sus datos. Si se usa un método económico que incorpora el negocio funcionando, no se añade nuevamente la recuperación de capital de trabajo. El valor patrimonial de cierre se distingue del efectivo disponible. Se puede estudiar un quinto año mediante un escenario completo, sin prolongar ingresos aisladamente ni introducir una perpetuidad para cambiar el signo del VAN (Sapag Chain & Sapag Chain, 2008, pp. 277–282, 292, 295).

### H.30.6. Indicadores y sensibilidad

El VAN se calcula sobre una serie identificada, con Año 0 sin descuento, y la TIR se interpreta según los signos del flujo. Se distingue recuperación simple de descontada. El umbral operativo de la sección 14.6 no equivale al volumen que produce VAN igual a cero. La sensibilidad modifica variables desde una base única y revela los puntos de quiebre; las probabilidades y distribuciones no se inventan cuando solo se dispone de escenarios ilustrativos (Sapag Chain & Sapag Chain, 2008, pp. 129–130, 321–323, 329–330, 371, 398–400, 406).

### H.30.7. Condiciones de cierre de la preparación

El escenario actualizado requiere completar demanda mensual, costos, inversión pertinente, caja con IVA, tratamiento de pérdidas con impuesto académico, capital de trabajo, valor de cierre y deuda simulada. Los flujos puro y financiado se presentan completos en el cuerpo cuando se concilien; el anexo respalda los supuestos y cálculos. Las tareas abiertas no se identifican como resultados financieros obtenidos. El 12 % de descuento y el 27 % de impuesto continúan como decisiones del ejercicio, sin atribuir su prescripción al libro.

### H.30.8. Referencia metodológica

Sapag Chain, N., & Sapag Chain, R. (2008). Preparación y evaluación de proyectos (5.ª ed.). McGraw-Hill Interamericana.

## H.31. Proyección comercial agregada y categorías

La referencia conserva ocho espacios promedio, dos pagos mensuales por espacio y ticket de CLP 50.000. No se añade crecimiento de volumen o precio sin una decisión respaldada. El archivo proyeccion_mensual_2027_2030.csv registra los 48 meses con comisión, IVA y fondos de publicadores separados. La tabla siguiente no reparte los ocho espacios entre categorías, porque ese dato aún no está definido. Nueve categorías disponibles no implica nueve espacios activos ni demanda validada en todas ellas.

**Tabla H.31.1**
*Estado de asignación de la oferta por categoría*

| ID | Categoría | Espacios y pagos | Ticket y mezcla |
|---|---|---|---|
| 1 | Oficina | Pendiente de asignar | Pendiente de ratificar |
| 2 | Sala multipropósito | Pendiente de asignar | Pendiente de ratificar |
| 3 | Bodega | Pendiente de asignar | Pendiente de ratificar |
| 4 | Estacionamiento | Pendiente de asignar | Pendiente de ratificar |
| 5 | Local flexible | Pendiente de asignar | Pendiente de ratificar |
| 6 | Stand | Pendiente de asignar | Pendiente de ratificar |
| 7 | Quincho | Pendiente de asignar | Pendiente de ratificar |
| 8 | Parcela de eventos | Pendiente de asignar | Pendiente de ratificar |
| 9 | Inmuebles | Pendiente de asignar | Pendiente de ratificar |

*Nota.* Catálogo de nueve categorías comunicado por el propietario. No se sustituyen datos faltantes por ceros observados. La referencia agregada puede calcularse sin atribuir ventas a una categoría. La mezcla de modalidades previa se conserva como ejemplo no ratificado.

**Tabla H.31.2**
*Proyección comercial agregada sin crecimiento automático*

| Año | Pagos anuales | GMV CLP | Comisión neta CLP | IVA de comisión CLP |
|---|---|---|---|---|
| 2027 | 192 | 9.600.000,00 | 288.000,00 | 54.720,00 |
| 2028 | 192 | 9.600.000,00 | 288.000,00 | 54.720,00 |
| 2029 | 192 | 9.600.000,00 | 288.000,00 | 54.720,00 |
| 2030 | 192 | 9.600.000,00 | 288.000,00 | 54.720,00 |

*Nota.* Elaboración con los parámetros agregados ratificados como referencia provisional. El total transado no es ingreso propio de espaciGo. Por mes, el saldo de publicadores antes de Mercado Pago es CLP 771.440; el abono final no se determina sin la tarifa y liquidación efectivas.

## H.32. Recursos y presupuesto conciliado

Los tres notebooks y el teléfono son personales y compartidos, según el propietario. Su compra inicial se fija en cero y no se presume transferencia de dominio a la empresa proyectada. Se mantienen separados el uso alternativo y eventuales costos incrementales; no se asigna a la empresa una depreciación o venta de bienes personales sin respaldo. El presupuesto de CLP 1.200.000 de lanzamiento se mantiene provisional en el Año 0, sin duplicarlo con marketing operativo.

**Tabla H.32.1**
*Componentes del presupuesto identificado del Año 1*

| ID | Componente | Mensual CLP | Anual CLP |
|---|---|---|---|
| C01 | AWS | 25.670,52 | 308.046,24 |
| C02 | Firma y API | 50.000,00 | 600.000,00 |
| C03 | Marketing | 350.000,00 | 4.200.000,00 |
| C04 | Contabilidad | 50.000,00 | 600.000,00 |
| C05 | Dominio | 912,50 | 10.950,00 |
| C06 | Coordinación | 15.000,00 | 180.000,00 |
| C07 | Útiles de oficina | 10.000,00 | 120.000,00 |
| C08 | Dirección tributaria | 12.500,00 | 150.000,00 |
| Total | Subtotal parcial | 514.083,02 | 6.168.996,24 |

*Nota.* Presupuestos de Base mensual!B21:B25 y Conciliacion costos!H9, con sustitución de GCP por el escenario AWS adoptado y dirección tributaria anual ratificada. Los útiles y la dirección se cuentan una sola vez. El importe anual de dirección se prorratea como referencia, sin afirmar facturación mensual efectiva. Se mantienen fuera los subtotales genéricos y los conceptos suspendidos de mantenimiento o respaldo sin alcance independiente. La tabla no equivale a costos contratados o facturados.

La constitución y los trámites se incluyen en los CLP 1.200.000 de lanzamiento y no se suman otra vez. Las cargas de contratación, costos residuales propios, recursos de uso alternativo y reposiciones carecen de valoración completa. Se registran como pendientes y no como cero real. La depreciación no se reconoce en el subtotal hasta definir el eventual aporte de equipos. Los CLP 6.240.000 de desarrollo valorizado tampoco se suman como pago inicial: se debe distinguir trabajo pasado, compromiso irreversible y trabajo incremental futuro.

## H.33. Caja de referencia y necesidad de financiación

Los costos identificados se proyectan mensualmente, con reajuste del 4 % anual para presupuestos CLP y costo AWS constante bajo el USD y cambio adoptados. La proyección no aplica créditos y no garantiza capacidad cloud para otros volúmenes. El IVA de comisión se reserva separado; el crédito por compras y las fechas efectivas de remisión permanecen pendientes. El impuesto del ejercicio se liquida al cierre anual por convención de la simulación, no como calendario fiscal real.

El caso de pago condicionado a fundadores utiliza solo excedente propio después de costos identificados, reserva de servicio de deuda y provisión académica de impuesto. Nunca utiliza préstamos, IVA o fondos de publicadores para activar la distribución. En la referencia agregada, el pago es cero durante el horizonte. Los escenarios con CLP 200.000 y CLP 1.000.000 efectivamente presupuestados por persona se calculan por separado, sin afirmar que exista caja para pagarlos. En el ejercicio se tratan como egreso de personal; la modalidad jurídica y la deducibilidad real se mantienen pendientes.

**Tabla H.33.1**
*Resultados operativos parciales del escenario agregado*

| Año | Comisión neta CLP | Costos identificados CLP | Pago condicionado CLP | Flujo operativo parcial CLP |
|---|---|---|---|---|
| 2027 | 288.000,00 | 6.168.996,24 | 0,00 | -5.880.996,24 |
| 2028 | 288.000,00 | 6.403.434,24 | 0,00 | -6.115.434,24 |
| 2029 | 288.000,00 | 6.647.249,76 | 0,00 | -6.359.249,76 |
| 2030 | 288.000,00 | 6.900.817,92 | 0,00 | -6.612.817,92 |

*Nota.* Caso sin deuda, antes de partidas excluidas. La compra de equipos es cero; el lanzamiento presupuestado de CLP 1.200.000 figura en el Año 0 del flujo del cuerpo. La necesidad acumulada de financiación parcial, incluyendo ese lanzamiento, alcanza CLP 26.168.498,16. Es financiación de déficit persistente, no capital de trabajo del ciclo determinado. No se suma nuevamente al Año 0 además de las pérdidas operativas.

**Tabla H.33.2**
*Comparación parcial de los escenarios de demanda del insumo*

| Escenario | Pagos mensuales | Ticket CLP | Comisión Año 1 CLP | VAN parcial al 12 % CLP |
|---|---|---|---|---|
| conservador | 4 | 35.000 | 50.400,00 | -20.776.704,15 |
| base | 16 | 50.000 | 288.000,00 | -20.055.029,94 |
| optimista | 45 | 65.000 | 1.053.000,00 | -17.731.457,69 |

*Nota.* Sin probabilidades atribuidas y sin ajuste de demanda para producir rentabilidad. El costo cloud y otros consumos deben reestimarse al cambiar el volumen; la comparación es un primer cálculo parcial, no una evaluación cerrada de capacidad o viabilidad.

## H.34. Corrección de la deuda simulada

Se calcula el préstamo de CLP 3.720.000 al 12 % anual y tres años con cuotas anuales, como el insumo. La cuota de referencia redondeada es CLP 1.548.818. La última cuota incorpora CLP 1 adicional para extinguir la deuda y conciliar capital amortizado con capital recibido. La simulación no acredita contratación, CAE, seguros ni comisiones.

**Tabla H.34.1**
*Amortización conciliada hasta saldo cero*

| Año | Saldo inicial CLP | Interés CLP | Amortización CLP | Cuota CLP | Saldo final CLP |
|---|---|---|---|---|---|
| 1 | 3.720.000 | 446.400 | 1.102.418 | 1.548.818 | 2.617.582 |
| 2 | 2.617.582 | 314.110 | 1.234.708 | 1.548.818 | 1.382.874 |
| 3 | 1.382.874 | 165.945 | 1.382.874 | 1.548.819 | 0 |

*Nota.* El principal amortizado totaliza CLP 3.720.000 y el saldo final es cero. La entrada del préstamo no se incluye como ingreso por comisiones. El flujo financiado del cuerpo presenta el efecto de la deuda y sus pagos.

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

## H.36. Coherencia y sensibilidad del segundo corte

La comprobación conserva la comisión neta del 3 %, la tasa de descuento base del 12 %, el impuesto académico del 27 % y los cuatro años 2027 a 2030. Cada sensibilidad cambia un solo parámetro y mantiene los demás. Los cambios de menos y más 20 % son rangos exploratorios definidos en esta revisión; no provienen de distribuciones observadas ni expresan certeza estadística. El caso base mantiene 16 cobros de CLP 50.000 al mes y pago condicionado cero.

**Tabla H.36.1**
*Sensibilidad individual del VAN parcial del caso base*

| Variable | Prueba | VAN parcial CLP | Cambio del VAN CLP |
|---|---|---|---|
| Cobros mensuales | -20 % de variación | -20.229.981 | -174.951 |
| Cobros mensuales | 20 % de variación | -19.880.079 | 174.951 |
| Ticket medio | -20 % de variación | -20.229.981 | -174.951 |
| Ticket medio | 20 % de variación | -19.880.079 | 174.951 |
| Costos identificados | -20 % de variación | -16.109.073 | 3.945.957 |
| Costos identificados | 20 % de variación | -24.000.987 | -3.945.957 |
| CLP por USD | -20 % de variación | -19.867.901 | 187.129 |
| CLP por USD | 20 % de variación | -20.242.159 | -187.129 |
| Tasa de descuento | 10 % anual | -20.894.880 | -839.850 |
| Tasa de descuento | 12 % anual | -20.055.030 | 0 |
| Tasa de descuento | 25 % anual | -15.783.221 | 4.271.809 |

*Nota.* Elaboración mediante el modelo reproducible. Valores redondeados a pesos para presentación. La variación cambiaria afecta solo a AWS; la de costos afecta a las ocho partidas identificadas. No se modifican el lanzamiento ni la comisión. Se mantienen las exclusiones del corte base. Un VAN menos negativo al elevar la tasa sobre flujos de salida no acredita menor riesgo. No se estiman costos cloud de escalamiento ni efectos de demanda cruzados.

**Tabla H.36.2**
*Umbrales operativos parciales por año sin deuda*

| Año | Costo mensual CLP | Pagos para $200.000 por persona | Pagos para $1.000.000 por persona |
|---|---|---|---|
| 2027 | 514.083 | 743 | 2.343 |
| 2028 | 533.620 | 756 | 2.356 |
| 2029 | 553.937 | 770 | 2.370 |
| 2030 | 575.068 | 784 | 2.384 |

*Nota.* Ticket de CLP 50.000, comisión de CLP 1.500 por pago y tres personas. El costo mensual es un prorrateo presupuestario, no una fecha contractual de pago. Los útiles, la dirección tributaria y el dominio no acreditan facturación mensual. La meta se mantiene nominal constante y los costos CLP se reajustan 4 %. La regla de pago condicionado a 743 cobros activa CLP 600.000 al mes solo en el Año 1 y cero en los demás. Los umbrales cubren costos y asignaciones del año; no incorporan recuperación del lanzamiento, deuda, costos omitidos ni VAN cero.

**Tabla H.36.3**
*Quiebre del VAN anual parcial con asignaciones presupuestadas constantes*

| Meta por persona CLP | Pagos mensuales mínimos | VAN con un pago menos CLP | VAN con el mínimo CLP |
|---|---|---|---|
| 200.000 | 791 | -37.544 | 2.367 |
| 1.000.000 | 2.391 | -37.544 | 2.367 |

*Nota.* Búsqueda numérica del volumen mensual uniforme a ticket de CLP 50.000. Se presupuestan las asignaciones completas como gasto académico, con independencia de que el escenario disponga de caja; no se cambia la decisión de pago condicionado. El flujo es puro, el Año 0 incluye CLP 1.200.000 de lanzamiento, el impuesto académico considera compensación de pérdidas y el VAN se descuenta al 12 % al cierre de cada año. El cálculo redondea hacia arriba el cruce y verifica los dos enteros adyacentes. El costo identificado no aumenta por volumen en esta prueba; antes de una decisión comercial se deben valorar escalamiento, recursos de oportunidad, cargas de contratación, capital del ciclo y cierre. El resultado no es una meta de captación validada.

### H.36.4. Convenciones de fechas y límites de cierre

La tasa mensual equivalente es (1 + 0,12) elevado a 1/12 menos 1, equivalente a 0,948879 %. El VAN anual rector del subtotal puro es CLP -20.055.029,94. Si los importes prorrateados se ubican al final de cada mes, el VAN es CLP -21.070.841,39, diferencia de CLP -1.015.811,45. Se informa el contraste porque adelantar egresos modifica su valor presente. No se reemplaza el formato anual docente ni se afirma que el prorrateo sea un calendario efectivo de caja.

Los flujos vigentes se vinculan con las Tablas 18 a 21, H.27 y H.31 a H.36. Las Tablas 15 a 17 y H.1 a H.26 preservan los antecedentes recibidos; sus valores GCP, tasas o inversiones anteriores no constituyen decisiones activas. La reconstrucción conserva su contenido para la comparación solicitada.

El caso base no presenta recuperación simple ni descontada dentro de los cuatro años: sus flujos propios son negativos. El valor de cierre y el capital del ciclo siguen sin cuantificarse. El cierre no adopta cero como valor económico definitivo ni convierte automáticamente el déficit persistente en capital de trabajo recuperable. La conclusión se limita al subtotal modelado; la evaluación integral continúa abierta conforme a los criterios de Sapag.

## H.37. Liquidez y memoria del déficit acumulado

### H.37.1. Aportes mínimos y déficit persistente

Se recorre el saldo mensual con lanzamiento, operación y deuda, cuando corresponde. Si el saldo antes de aporte es negativo, el aporte mínimo es su valor absoluto; si es positivo, el aporte es cero. La caja de cierre después del aporte se mantiene no negativa. La suma de aportes coincide con el déficit acumulado máximo antes de aportes. Se conservan los 49 momentos en aportes_minimos_condicionada_puro.csv y aportes_minimos_condicionada_financiado.csv. El cálculo distingue necesidad de financiación de pérdidas de capital de trabajo del ciclo (Sapag Chain & Sapag Chain, 2008, pp. 267–269).

**Tabla H.37.1**
*Conciliación de la financiación adicional acumulada*

| Escenario | Aporte adicional Año 0 CLP | Aportes adicionales totales CLP | Caja final tras aportes CLP |
|---|---|---|---|
| Sin deuda | 1.200.000 | 26.168.498 | 0 |
| Con deuda simulada | 0 | 27.094.953 | 0 |

*Nota.* El aporte inicial de cero en la alternativa financiada se explica por el préstamo que excede el lanzamiento identificado. No significa ausencia de inversión o de aportes posteriores. Los aportes son una necesidad calculada, no un compromiso confirmado de los socios. El excedente prestado no es utilidad ni habilita remuneraciones por sí solo.

### H.37.2. Cobertura de las cuotas de deuda

**Tabla H.37.2**
*Caja propia frente al servicio de la deuda simulada*

| Año | Caja antes de cuota CLP | Intereses y principal CLP | Cobertura veces |
|---|---|---|---|
| 2027 | -5.880.996 | 1.548.818 | -3,797 |
| 2028 | -6.115.434 | 1.548.818 | -3,948 |
| 2029 | -6.359.250 | 1.548.819 | -4,106 |
| 2030 | -6.612.818 | 0 | No aplica |

*Nota.* La caja propia antes de cuota resta OPEX, asignaciones pagadas e impuesto académico de las comisiones netas. No incluye préstamo, aportes nuevos, IVA ni arriendos de terceros. La razón es un diagnóstico auxiliar; no se afirma que una entidad financiera apruebe el préstamo. La falta de cuota en 2030 no elimina el déficit operativo.

### H.37.3. Sensibilidad aislada de la comisión por cobrar

**Tabla H.37.3**
*Efecto auxiliar de inmovilizar comisión neta por distintos plazos*

| Días ilustrativos | Comisión por cobrar CLP | Efecto en VAN CLP |
|---|---|---|
| 0 | 0 | 0,00 |
| 7 | 5.600 | -2.041,10 |
| 30 | 24.000 | -8.747,57 |

*Nota.* Se utiliza la comisión neta de CLP 24.000 mensuales y un mes de 30 días, con cobros uniformes. Los plazos 0, 7 y 30 días son pruebas, no condiciones de Mercado Pago. El stock auxiliar se aporta en el Año 0 y se recupera íntegro en el Año 4 para aislar su efecto: variación del VAN = menos stock más stock descontado al cierre. No se aplica este ajuste al caso activo ni se identifica como capital completo del ciclo. Faltan pagos anticipados, plazos de proveedores, IVA de compras y devoluciones. El IVA recaudado y los fondos de publicadores se excluyen de caja libre.

## H.38. Indicadores y recuperación de los escenarios delimitados

Se calcula VAN con momento cero sin descuento y cierres anuales al 12 %. La TIR solo se informa como rentabilidad cuando existe un flujo de inversión con un cambio de signo. Una serie de egresos no tiene TIR; una entrada inicial seguida de pagos corresponde a otro patrón y no se presenta como rentabilidad de los socios. La recuperación simple acumula importes nominales y la descontada acumula importes descontados (Sapag Chain & Sapag Chain, 2008, pp. 321–323, 329–330).

**Tabla H.38.1**
*VAN y TIR de la referencia y los quiebres parciales*

| Escenario | Pagos al mes | VAN parcial CLP | TIR anual |
|---|---|---|---|
| Base sin deuda | 16 | -20.055.029,94 | No existe |
| Base con deuda | 16 | -20.055.030,16 | No interpretable como inversión |
| Quiebre sin asignaciones | 391 | 2.367,04 | 12,1225 % |
| Meta CLP 200.000 por persona | 791 | 2.367,04 | 12,1225 % |
| Meta CLP 1.000.000 por persona | 2.391 | 2.367,04 | 12,1225 % |

*Nota.* El quiebre sin asignaciones es el primer entero con VAN no negativo antes de activarse la meta conjunta: se comprueba que con 390 pagos el VAN es negativo y con 391 no lo es. Los otros dos quiebres presuponen asignaciones completas como egreso académico; no reemplazan la decisión de pago condicionado del caso base. Sus flujos se conservan en liquidez_indicadores_y_cierre.json. El costo identificado no se reestima por volumen en estas pruebas, por lo que los resultados excluyen escalamiento, capital completo del ciclo, oportunidad y cierre. El VAN positivo de unos pocos miles de pesos no constituye margen para absorber partidas desconocidas. No se asume costo económico cero del trabajo por carecer de pago.

**Tabla H.38.2**
*Recuperación simple y descontada de las series anuales*

| Escenario | Simple en años | Descontada en años |
|---|---|---|
| Base sin deuda | No se recupera | No se recupera |
| Base con deuda | No aplica al patrón | No aplica al patrón |
| Quiebre sin asignaciones | 2,359 | 3,963 |
| Meta CLP 200.000 por persona | 2,359 | 3,963 |
| Meta CLP 1.000.000 por persona | 2,359 | 3,963 |

*Nota.* Se interpola linealmente entre cierres anuales para expresar fracciones de año. Esa interpolación no identifica una fecha contractual ni sustituye la convención anual del VAN. No se trasladan estas recuperaciones al caso comercial de 16 pagos ni se confunde recuperación nominal con cumplimiento de la tasa de descuento.

## H.39. Horizonte y condiciones para cerrar la evaluación integral

### H.39.1. Método de cierre y límite del cálculo

El caso de referencia conserva cuatro años de operación. El procedimiento requiere inventariar activos y derechos efectivamente atribuibles al proyecto, su uso alternativo, vida remanente y posibles desembolsos de reposición. Después se estima un valor comercial neto de realización con respaldo o, si existe una proyección sostenible posterior, se evalúa un valor de continuidad que no duplique recuperaciones ya incluidas. El libro distingue métodos contable, comercial y económico; el valor contable no acredita por sí solo dinero de venta (Sapag Chain & Sapag Chain, 2008, pp. 277–282, 292–295).

Para que un único cobro terminal neto adicional en el Año 4 neutralice el VAN del subtotal base, se requiere CLP 31.556.977,88. Se obtiene multiplicando el valor absoluto del VAN por (1 + 0,12) elevado a cuatro. Este umbral algebraico no tasa equipos, software o empresa; no demuestra la existencia de comprador ni de flujos posteriores. No se incorpora a las Tablas 18 y 19 como ingreso esperado.

### H.39.2. Datos y decisiones que no se sustituyen por supuestos confirmados

El cierre comercial requiere ratificar distribución de espacios, pagos, ticket y estacionalidad entre las nueve categorías. La referencia agregada no inventa ventas por categoría. Los CLP 1.200.000 de lanzamiento incluyen constitución y trámites por decisión del propietario; el desglose y la ejecución efectiva se documentan sin duplicar la partida.

El desarrollo valorizado se separa en trabajo pasado, compromisos irreversibles y trabajo incremental futuro. Los equipos existentes no generan nueva compra; se precisa su propiedad, aporte y uso alternativo antes de asignar depreciación o valor de cierre. Ausencia de pago no equivale a costo de oportunidad cero.

Antes de integrar se precisan costos y condiciones de proveedores, pasarela, devoluciones, retenciones, liquidaciones y formalización de asignaciones. Se conserva el impuesto académico del 27 % sin afirmar liquidación fiscal real. Con esas entradas se recalculan flujos, capital del ciclo, indicadores y conclusión. La preparación mantiene las reservas de la tesis principal y las secciones de planificación de Erick.

## H.40. Ratificación de decisiones preoperativas

El propietario ratifica que el lanzamiento se prevé en enero de 2027, los CLP 1.200.000 de preparación y lanzamiento incluyen constitución y trámites, y los equipos permanecen personales y compartidos. La inclusión de trámites evita duplicar el desembolso. El uso compartido no acredita transferencia patrimonial ni ingreso de venta final de equipos a la empresa.

La aclaración interpreta los CLP 6.240.000 como valorización del esfuerzo total para desarrollar el producto funcional antes del lanzamiento. No determina cuánto está ejecutado, cuánto falta ni un pago contratado. Se distingue la valoración global de origen del costo incremental pertinente a la fecha de decisión. El caso de caja conserva cero desembolso de desarrollo adicional confirmado; ello no declara cero su costo económico (Sapag Chain & Sapag Chain, 2008, pp. 126, 259–262).

Para observar qué volumen permitiría recuperar también esa valoración, se añade CLP 6.240.000 una sola vez al momento cero de una prueba separada, junto con el lanzamiento de CLP 1.200.000. El total de referencia pasa a CLP 7.440.000, sin sumar los equipos personales. No se incluye depreciación, amortización contable ni escudo tributario por esa valoración sin evidencia de su procedencia. No es una nueva salida de efectivo ni una valoración legal del software.

**Tabla H.40.1**
*Quiebre parcial al exigir recuperar la valoración global de desarrollo*

| Escenario | Pagos mensuales mínimos | VAN con un pago menos CLP | VAN con el mínimo CLP |
|---|---|---|---|
| Sin asignaciones | 548 | -11.552,77 | 28.358,00 |
| Meta CLP 200.000 por persona | 948 | -11.552,77 | 28.358,00 |
| Meta CLP 1.000.000 por persona | 2.548 | -11.552,77 | 28.358,00 |

*Nota.* Ticket constante de CLP 50.000, comisión neta del 3 %, cuatro años y descuento del 12 %. Los gastos de lanzamiento ya incluyen trámites. El caso de 16 pagos, al exigir recuperar además la valoración global, produce VAN de CLP -26.295.029,94. Esta prueba mantiene los costos identificados independientes del volumen y no sustituye la caja de las Tablas 18 y 19 ni estima el costo de oportunidad incremental real. Las partidas aún no valoradas continúan excluidas.
