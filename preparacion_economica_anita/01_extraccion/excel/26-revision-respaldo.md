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
