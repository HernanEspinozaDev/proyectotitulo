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
