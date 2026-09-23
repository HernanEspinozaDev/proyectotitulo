## Modelo de datos

Se propone un primer modelo lógico de 16 entidades y 123 atributos para identidad, publicación, reserva y su operación transaccional. Los identificadores internos y tipos son decisiones de diseño de ES2, todavía sin DDL ni base implementada. El catálogo completo está en el **Anexo A de ES2**, con claves, nulabilidad y reglas. No se declara aún cobertura de los 236 RF.

### Identidad, oferta y calendario

![Modelo inicial de identidad y reservas](imagenes/figura-datos_reservas.png){width=6.3in} <!--#fig:es2-datos-reservas--> <!--#fuente:elaboración propia a partir de los requisitos de ES1.-->

Usuario mantiene su identidad de cuenta y admite varios roles mediante rol_usuario. Verificación conserva solicitudes y decisiones KYC/KYB. Espacio pertenece a un arrendador; reserva relaciona espacio y arrendatario, con fechas e instantánea de importes y condiciones.

Ocupación reúne intervalos de reservas y bloqueos manuales. Esto permite evaluar RQF-111/RQF-112 sobre un calendario común. Se propone un intervalo semiabierto [inicio, fin), para que dos usos consecutivos puedan compartir un límite sin superponerse. PostgreSQL documenta restricciones de exclusión sobre rangos; la aplicación al calendario es una propuesta ES2 que requiere implementación y prueba concurrente [@es1anexod; @es2pgrangos].

Cada reserva podrá tener como máximo una ocupación en este primer modelo. Los bloqueos manuales no tienen reserva asociada. Una retención temporal vencida se desactiva mediante una transición registrada; no basta con comparar la hora durante una búsqueda. La creación de reserva y ocupación deberá ser atómica y comprobar el mismo espacio.

### Operaciones financieras y eventos

![Modelo inicial de pagos, garantía y liquidación](imagenes/figura-datos_finanzas.png){width=6.3in} <!--#fig:es2-datos-finanzas--> <!--#fuente:elaboración propia a partir de los requisitos de ES1.-->

Una reserva puede registrar varios intentos de pago y garantía. Liquidación admite un registro por reserva en esta propuesta; los reintentos deben referirse a la misma operación idempotente. Evento_proveedor registra eventos autenticados y su estado de procesamiento, admitiendo correlación pendiente.

Las operaciones financieras distinguen pendiente, confirmado, rechazado y por conciliar como estados técnicos propuestos. No reemplazan los estados de negocio de la reserva ni convierten la retención en una capacidad confirmada del proveedor. No se almacenan PAN ni CVV en el modelo.

### Contratos, operación y evidencia

![Modelo inicial de contratos, uso y evidencia](imagenes/figura-datos_operacion.png){width=6.3in} <!--#fig:es2-datos-operacion--> <!--#fuente:elaboración propia a partir de los requisitos de ES1.-->

Contrato conserva versiones; firma_contrato registra la respuesta de cada parte. Operación_arriendo distingue check-in, check-out y recepción. Disputa conserva el reclamo y su resolución. Documento contiene metadatos y una referencia restringida al archivo, mientras evento_auditoria registra el hecho y su correlación.

En los diagramas se muestran claves seleccionadas para facilitar lectura; el diccionario contiene los atributos completos. Las relaciones opcionales de documento responden a un único propietario por registro, controlado mediante una restricción adicional. Los vínculos a reserva no bastan para distinguir múltiples reclamos o eventos: esa asociación detallada permanece como ampliación pendiente.

### Reglas y límites del diseño

- Mantener coherencia entre importe, moneda, comisión y garantía de la reserva y sus operaciones.
- Habilitar check-in únicamente cuando estén confirmadas todas las firmas exigidas.
- Impedir liquidación mientras haya disputa abierta y verificar su resultado antes de cerrar.
- Diferenciar integridad del archivo mediante hash de la inmutabilidad de su almacenamiento.
- Conciliar retención, anonimización y referencias a usuarios antes de diseñar borrados.

[[PENDIENTE: validar el modelo con el equipo, completar los dominios y asociaciones identificados en el Anexo A, definir estados y permisos, producir DDL y ejecutar pruebas de claves, restricciones, concurrencia y migración.]]
