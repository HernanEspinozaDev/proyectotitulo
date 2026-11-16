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
