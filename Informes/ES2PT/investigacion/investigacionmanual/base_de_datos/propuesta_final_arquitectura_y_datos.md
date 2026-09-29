# Propuesta consolidada de arquitectura y base de datos (ES2)

**Fecha de consolidación:** 29 de septiembre de 2026.
**Nota de vigencia:** el [Anexo B v2](../../../anexos/B_diccionario_datos.md) y la [propuesta backend v1.2](../../../investigacion/propuesta_backend_final.md) contienen el contrato oficial de diseño sincronizado. Este consolidado conserva el razonamiento y se lee como antecedente cuando difiere en nombre de tabla, estado o trabajo pendiente.
**Estado del proyecto:** investigación y diseño del **producto completo**, con todas las categorías de ES1. El usuario descartó acotar esta propuesta a una demo. **No consta DDL aplicado, backend implementado, proveedores integrados ni infraestructura desplegada.** Las decisiones aquí descritas orientan la implementación incremental; impuestos, proveedores, retención y costos que requieren evidencia externa se identifican como pendientes. La [revisión técnica](10_revision_y_respuestas_para_cierre.md), el [inventario de cobertura](11_inventario_producto_completo.md) y el [flujo de comisión](12_comision_y_reparto_socios.md) detallan los cambios frente al primer borrador de este archivo.

---

## 1. Definiciones de Negocio y Modelo de Datos (DDL)

Se fijan las siguientes directrices del modelo transaccional:

*   **Modelo de Unidad Exclusiva:** Cada espacio publicado representa una unidad exclusiva de arriendo. Se adopta el modelo de inventario estricto manteniendo la tabla `ocupacion(espacio_id, intervalo)` con una restricción a nivel de motor `EXCLUDE USING gist` para evitar atómicamente cualquier solapamiento.
*   **Gestión del tiempo y zonas horarias:** `ocupacion.intervalo` utiliza `tstzrange` semiabierto `[inicio, fin)` sobre instantes; `espacio.zona_horaria` conserva una zona IANA, por ejemplo `America/Santiago`, para interpretar horarios civiles y tarifas. La conversión se documenta para cambios de hora.
*   **Tipos de arriendo y flexibilidad tarifaria:** el arrendador define el precio dentro de reglas comerciales verificables. `categoria_espacio` y `regla_tarifa` versionada registran unidad temporal, duración mínima/máxima, valor, moneda y vigencia. Hora/día/mes cubren el requisito original; semana/año se habilitan solo con semántica de calendario y cotización definida. El RQF-073 vigente exige precio base superior a 5.000 CLP; eso no demuestra rentabilidad de cada reserva.
*   **Snapshot contractual:** `reserva` cambia de estado, pero conserva sin sobrescritura el desglose económico y la política aceptados, con versión de tarifa/comisión, instante de aceptación y referencia contractual. El desglose separa arriendo de tercero, comisión neta EspaciGo, IVA de cada componente si corresponde, garantía y total; no mezcla ingresos propios con fondos de terceros.
*   **Archivos:** fotos, contratos y KYC binarios residen en **Cloud Storage privado**; `documento` guarda metadatos, dueño verificable, hash, estado y referencia al objeto. La API decide acceso. El hash no garantiza por sí solo inmutabilidad del bucket.

---

## 2. Definiciones Financieras y Transaccionales

*   **Moneda y redondeo:** se opera en CLP; importes finales se expresan en pesos enteros (`numeric(14,0)` propuesto, sujeto a migración desde el dominio actual). Tasas y cálculos intermedios usan decimal exacto y una regla de redondeo contractual/tributaria versionada. La Ley 20.956 regula redondeo de **pagos en efectivo** y no fundamenta redondear un checkout digital a la decena ([BCN, reglamento](https://www.bcn.cl/leychile/navegar?idNorma=1111243)).
*   **Comisión e IVA:** decisión del usuario: **3 % neto del arriendo para EspaciGo**, más IVA de la comisión cuando corresponda. La comisión se parametriza y se congela en cada reserva. El [Anexo A](../../../anexos/A_evaluacion_economica.md) ya calcula 3 %; el 12 % de comisión es un escenario histórico y el 25 % del estudio de Shiva era hipotético. La tasa de descuento del VAN permanece en 12 % como supuesto académico independiente de la comisión. El tratamiento del IVA del arriendo, la emisión de documentos y la tarifa real de la pasarela siguen pendientes de validación.
*   **Split y socios:** Mercado Pago Split 1:1, si se confirma contractualmente, reparte el pago entre **vendedor y marketplace**, no entre los tres fundadores ([Mercado Pago, integración](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/integration-configuration/integrate-marketplace)). Los socios participan igualitariamente en las utilidades **distribuibles** de la SpA, fuera del checkout. Si el monto distribuible es 12 millones CLP, corresponde 4 millones a cada uno; 12 millones de ingresos o de cobros totales no equivalen a monto distribuible.
*   **Cifras de Split pendientes:** la referencia inicial del usuario a 3,19 % de Split, cargo adicional de Checkout API y ≈7 % menos para el propietario sigue siendo **hipótesis comercial por verificar** en el anexo de Mercado Pago. `3 % + IVA` de la comisión equivale a **3,57 % del arriendo** con IVA supuesto de 19 %; 3,19 % es una tarifa pública referencial del proveedor, no un resultado de aplicar IVA al 3 %. El caso base del Anexo A muestra comprador **100.000 CLP**, comisión propia neta **3.000 CLP**, IVA de esa comisión **570 CLP**, tarifa de pasarela de **3.190 CLP** más **606,10 CLP** de IVA y neto ilustrativo del arrendador de **92.633,90 CLP**. El proveedor documenta descuento de su tarifa primero al vendedor. La base separará comisión, IVA, tarifa del proveedor, importe del comprador y neto real del arrendador; la liquidación efectiva se conciliará con el contrato y reportes del proveedor.
*   **Precio mínimo y margen:** conservar la validación de RQF-073 (>5.000 CLP de precio base). Con ticket ilustrativo de 100.000 CLP, la comisión propia neta de 3.000 CLP iguala los 3.000 CLP de costos variables propios supuestos por reserva: no queda contribución para cubrir costos fijos. La simulación segmentada por categoría del Anexo A arroja contribución negativa. Definir duración mínima o política comercial adicional por categoría exige demanda y costos medidos; la regla técnica de RQF-073 no es una prueba de rentabilidad.
*   **Movimientos financieros:** registrar cobro, reembolso parcial, contracargo y ajuste como hechos nuevos vinculados al origen; no reescribir un movimiento confirmado. `pago.estado` sí cambia por reconciliación. Una tabla de movimientos no se llamará libro mayor de partida doble sin asientos y cuentas balanceadas.

---

## 3. Estados de Reserva y Actores

Se diseña el ciclo de vida del producto completo. La máquina de estados debe respetar los hitos y restricciones de ES1/Anexo B; la lista abreviada del borrador anterior no los sustituye:

*   **Retención transaccional:** crear `reserva` pendiente, `ocupacion` activa con `expira_en` y `outbox_evento` en un commit. La exclusión GiST rechaza solapes. Al vencer sin pago confirmado, el worker libera la ocupación en una transición persistida. No existe una lista de espera FIFO por el solo hecho de expirar una retención.
*   **Estados y actores:** preservar `pendiente_de_pago`, `pagada`, `aprobada_host`, `firma_parcial`, `lista_para_checkin`, `en_curso`, `finalizada` y cierre/liquidación, además de cancelaciones con causa y disputa. La confirmación de pago procede de simulador autorizado en desarrollo o webhook verificado/**consulta de conciliación** en sandbox; el anfitrión aprueba/rechaza; las partes autorizadas registran check-in/out; administrador resuelve disputa; los workers gestionan vencimientos y conciliación. El reloj no genera check-in ni check-out.
*   **Disputa:** `disputa` es entidad propia y bloquea liquidación mientras esté abierta. Si `reserva.estado` se muestra como `en_disputa`, conservar la etapa previa para resolverla sin saltos ambiguos. Cada transición registra actor, fecha, motivo y versión.

---

## 4. Tratamiento de Datos, Privacidad y Retención (Ley 21.719)

*   **Matriz por finalidad:** cuenta/perfil, KYC, arriendo, comisión/tributos, contrato, disputa, auditoría, analítica y derechos de titulares tendrán propósito, fundamento, destinatarios, acceso y plazo propios. Las bases legales particulares y documentos tributarios requieren revisión con contador/asesoría; la Ley 21.719 es criterio de diseño de ES2, vigente desde 01-12-2026, sin cumplimiento probado ([BCN, Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272)).
*   **Retención:** no fijar cinco años universales. El SII describe seis años para ciertos libros/documentos contables y excepciones ([SII, conservación](https://www.sii.cl/preguntas_frecuentes/declaracion_renta/001_140_4628.htm)); el plazo aplicable se decidirá por clase de dato y fundamento.
*   **Baja y derechos:** no usar `ON DELETE CASCADE` en hechos financieros. Eliminar identificadores directos y mantener UUID/FK puede ser **seudonimización**, no anonimización irreversible; la supresión y conservación se resuelven por solicitud fundada y se propagan a objetos y derivados cuando corresponda.
*   **Restauración:** se propone un registro protegido de supresiones/tombstones para aplicar decisiones posteriores a la fecha del backup **antes de reabrir** una copia restaurada. El procedimiento y su seguridad se probarán en PT-16/PT-11; no se declaran implementados.

---

## 5. Infraestructura Cloud (GCP) y Operación a Escala

El perfil de nube se dimensionará contra carga y presupuesto, sin equiparar el nombre de una edición con capacidad probada:

*   **Perfil de operación:** búsquedas espaciales e inserciones transaccionales son cargas previstas; volumen, índices adicionales y capacidad se medirán en PT-09/PT-10.
*   **Cloud SQL (PostgreSQL 18):**
    *   *Edición:* **Enterprise** como perfil inicial a presupuestar; comparar HA y Enterprise Plus si carga/objetivos lo justifican. PostgreSQL 18 está disponible en ambas ediciones ([Google Cloud, ediciones](https://docs.cloud.google.com/sql/docs/postgres/choose-edition)).
    *   *Disponibilidad:* HA multizona como escenario de producción a evaluar y costear; entorno de ensayo puede ser zonal. La edición y topología finales se registrarán en Anexo A.
    *   *Backups:* copias automáticas y PITR a configurar. RPO ≤4 h/RTO ≤6 h son objetivos del RNF-010 que se acreditarán con restauración y medición PT-11; activarlos no garantiza por sí mismo esos tiempos ([Google Cloud, PITR](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr)).
*   **Cloud Run y costos de workers:** se propone mínimo una instancia con CPU disponible fuera de solicitudes para workers internos, más límite máximo/pool de conexiones. Las instancias pueden reiniciarse; el trabajo vive en PostgreSQL. El Anexo A **ya incorpora** esta instancia en el perfil piloto y estima **USD 307,724/mes** netos bajo sus precios y consumos académicos; no representa una factura ni garantiza disponibilidad.
*   **Estrategia de Cambios (Docs-as-Code y Migraciones):** Los cambios de esquema seguirán el patrón **Expand/Contract** mediante archivos de migración numerados. No se permitirán alteraciones destructivas (`ALTER TABLE DROP`) en caliente sin antes haber migrado el código de la API.
*   **Analítica y BigQuery:** `outbox_evento` persiste eventos seleccionados desde el primer incremento; Pub/Sub y BigQuery se implementarán en un incremento posterior del **mismo producto**, con contratos versionados y permisos. No se utiliza Datastream ni BigQuery como fuente de estados de reserva/pago.
