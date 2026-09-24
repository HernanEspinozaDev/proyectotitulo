## Modelo de datos

Se propone un modelo lógico de **17 entidades y 137 atributos** para identidad, publicación, reserva y su operación transaccional. Los identificadores internos, los dominios y los tipos son decisiones de diseño de ES2: el **Anexo B de ES2** reúne el catálogo con claves, nulabilidad y reglas, el catálogo de estados y transiciones, los permisos por rol, el DDL propuesto como texto y los ensayos previstos del modelo. Ese DDL no se ha aplicado en ningún servidor y no se declara cobertura de los 236 RF.

La monetización de destaques sería una **extensión posterior de este modelo parcial**, no una entidad ya incluida entre las 17. Su diseño necesitaría campaña, orden pagada, vigencia, zona/categoría, estado, política de pausa/reembolso y eventos de exposición agregados. El Anexo B registra los campos candidatos; no se le atribuye implementación ni aprobación [@es2sernacpublicidad].

### Identidad, oferta y calendario

![Modelo inicial de identidad y reservas](imagenes/figura-datos_reservas.png){width=6.3in} <!--#fig:es2-datos-reservas--> <!--#fuente:elaboración propia a partir de los requisitos de ES1.-->

Usuario mantiene su identidad de cuenta y admite varios roles mediante rol_usuario. Verificación conserva solicitudes y decisiones KYC/KYB. Espacio pertenece a un arrendador; reserva relaciona espacio y arrendatario, con fechas e instantánea de importes y condiciones.

Ocupación reúne intervalos de reservas y bloqueos manuales. Esto permite evaluar RQF-111/RQF-112 sobre un calendario común. Se propone un intervalo semiabierto [inicio, fin), para que dos usos consecutivos puedan compartir un límite sin superponerse. PostgreSQL documenta restricciones de exclusión sobre rangos; la aplicación al calendario es una propuesta ES2 que requiere implementación y prueba concurrente [@es2pgrangos].

Cada reserva podrá tener como máximo una ocupación en este primer modelo. Los bloqueos manuales no tienen reserva asociada. Una retención temporal vencida se desactiva mediante una transición registrada; no basta con comparar la hora durante una búsqueda. La creación de reserva y ocupación deberá ser atómica y comprobar el mismo espacio.

### Operaciones financieras y eventos

![Modelo inicial de pagos, garantía y liquidación](imagenes/figura-datos_finanzas.png){width=6.3in} <!--#fig:es2-datos-finanzas--> <!--#fuente:elaboración propia a partir de los requisitos de ES1.-->

Una reserva puede registrar varios intentos de pago y garantía. Liquidación admite un registro por reserva en esta propuesta; los reintentos deben referirse a la misma operación idempotente. Evento_proveedor registra eventos autenticados y su estado de procesamiento, admitiendo correlación pendiente.

Las operaciones financieras distinguen pendiente, confirmado, rechazado y por conciliar como estados técnicos propuestos. No reemplazan los estados de negocio de la reserva ni convierten la retención en una capacidad confirmada del proveedor. No se almacenan PAN ni CVV en el modelo.

### Contratos, operación y evidencia

![Modelo inicial de contratos, uso y disputas](imagenes/figura-datos_operacion.png){width=6.3in} <!--#fig:es2-datos-operacion--> <!--#fuente:elaboración propia a partir de los requisitos de ES1.-->

![Modelo inicial de documentos y auditoría](imagenes/figura-datos_evidencias.png){width=6.3in} <!--#fig:es2-datos-evidencias--> <!--#fuente:elaboración propia a partir de los requisitos de ES1.-->

Contrato conserva versiones; firma_contrato registra la respuesta de cada parte. Operación_arriendo distingue check-in, check-out y recepción. Disputa conserva el reclamo y su resolución. Documento contiene metadatos y una referencia restringida al archivo, mientras evento_auditoria registra el hecho y su correlación.

En los diagramas se muestran claves seleccionadas para facilitar lectura; el diccionario contiene los atributos completos. Las relaciones opcionales de documento responden a un único propietario por registro, controlado mediante una restricción adicional. Los vínculos a reserva no bastan para distinguir múltiples reclamos o eventos: esa asociación detallada permanece como ampliación pendiente.

### Privacidad incorporada al diseño

Aunque la Ley 21.719 entra en vigencia después de la fecha de ES2, el proyecto la adopta **desde el primer incremento** como criterio de diseño. Para cada entidad o documento se definirá finalidad, dato mínimo, acceso, proveedor, conservación y acción al terminar el tratamiento. El **Anexo B de ES2** contiene una matriz inicial de tratamientos; todavía faltan fundamentos jurídicos, plazos por categoría y revisión del equipo [@ley21719].

El esquema y las API deberán permitir identificar y tramitar solicitudes de titulares sin borrar indiscriminadamente reservas, pagos o evidencia. El Anexo B incorpora la entidad `solicitud_titular`, con tipo de derecho, identidad verificada, fecha, estado, decisión fundada, responsable y resultado, vinculada al historial de auditoría. Su implementación, el plazo de respuesta y el mecanismo de exportación o bloqueo siguen pendientes. RNF-018/029 exigen eliminación o anonimización tras la baja, mientras RNF-042/043 prevén conservación por cinco años: la regla concreta depende del dato, finalidad y obligación aplicable. Hasta resolverla, no se ejecutará un borrado en cascada sobre hechos financieros ni documentos [@ley21719].

### Dominios, estados y permisos

El Anexo B declara tres dominios reutilizables (monto no negativo, monto estrictamente positivo y hash hexadecimal) y las restricciones de cada entidad: claves, unicidad, nulabilidad condicionada y coherencia entre columnas. Los **estados** se separan en literales verificados en ES1 —Pendiente de Pago, Pagada, Aprobada_Host, Firma_Parcial, Lista_Para_Checkin, En_Curso, Finalizada y Cancelada_Por_Pago— y estados propuestos que aún deben mapearse, como el rechazo del arrendador o las cancelaciones por vencimiento y por falta de firma. Las transiciones de la reserva quedan enumeradas con su disparador y su referencia; su validación corresponde a la aplicación, porque una restricción de dominio no impide un salto de estado.

Los **permisos** se definen por rol con su alcance y sus restricciones: el visitante solo accede al catálogo público, cada parte opera sobre sus propios registros, el administrador no tiene rol comercial y toda cuenta de servicio queda por diseñar. El DDL no crea roles de base de datos ni políticas de fila: la autorización se resuelve en la API y en las consultas, y la minimización de RNF-018/029 debe comprobarse en cada exportación.

### DDL propuesto y ensayos previstos

El Anexo B incluye el **DDL propuesto como texto** para PostgreSQL 16 o superior con PostGIS y `btree_gist`. Declara claves primarias y foráneas, la coherencia entre el espacio de una reserva y el de su ocupación mediante clave foránea compuesta, la exclusión de solapamiento por espacio con `EXCLUDE USING gist` sobre el rango semiabierto, la unicidad de idempotencia por proveedor, la deduplicación de eventos externos y la coherencia entre la categoría de un documento y su propietario. No declara transiciones de estado, permisos, retención, anonimización, inmutabilidad del repositorio de auditoría ni emisión de boleta: eso requiere lógica de aplicación o procesos programados. Tampoco se ha aplicado a un servidor; su comprobación es textual y de coherencia con el diccionario.

El Anexo B enumera **doce ensayos previstos** (MD-01 a MD-12) de claves, restricciones, concurrencia, vencimiento, privacidad, migración, retención y restauración, cada uno con el caso del Anexo C que corresponda (PT-01 a PT-04, PT-08, PT-11 y PT-16). **Ninguno se ha ejecutado**: requieren base desplegada, producto y entorno autorizado, y se mantienen separados del catálogo de pruebas del producto.

### Reglas y límites del diseño

- Mantener coherencia entre importe, moneda, comisión y garantía de la reserva y sus operaciones.
- Habilitar check-in únicamente cuando estén confirmadas todas las firmas exigidas.
- Impedir liquidación mientras haya disputa abierta y verificar su resultado antes de cerrar.
- Diferenciar integridad del archivo mediante hash de la inmutabilidad de su almacenamiento.
- Aplicar minimización y acceso por rol desde el modelo inicial; conciliar retención, anonimización y referencias a usuarios antes de diseñar borrados.
- Validar las transiciones de estado en la aplicación y conservar en la base solo la garantía estructural: dominio, unicidad, exclusión de solapamiento y coherencia entre columnas.
- Tratar el vínculo entre evidencia y su evento o reclamo como propietario único del documento, sin duplicar registros ni permisos.

[[PENDIENTE: validar con el equipo el modelo y los catálogos de estados, acordar la política de conservación y anonimización de la matriz de tratamiento, aplicar el DDL en un entorno autorizado y ejecutar los ensayos MD-01 a MD-12 con evidencia fechada; completar las entidades que siguen fuera de este alcance parcial.]]
