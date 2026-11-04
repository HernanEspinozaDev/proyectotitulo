# CAPÍTULO IX: MODELAMIENTO DE PROCESOS DE NEGOCIO Y DATOS

## 9.1. Procesos de negocio objetivo

La especificación utiliza actividades UML para los flujos de oferta y contratación y para el flujo de privacidad.

### 9.1.1. Publicación de un espacio

El flujo objetivo valida la titularidad y las reglas del anuncio al publicar. La verificación de identidad de ambas partes corresponde a la emisión contractual.

La Figura 7 separa las condiciones de publicación de la verificación contractual.

**Figura 7**\
*Actividad de publicación y control de titularidad*

![](assets/figuras/fig08_publicacion_objetivo.png)

*Nota.* Elaboración propia. El diagrama UML representa las condiciones de publicación del ADR del 4 de noviembre de 2026.

### 9.1.2. Contratación, cobros y cierre

La Figura 8 representa la secuencia objetivo. El Anexo E identifica rutas de ensayo y el Capítulo XI establece condiciones para habilitar proveedores.

**Figura 8**\
*Actividad de contratación, cobros y cierre de ocupación*

![](assets/figuras/fig09_contratacion_objetivo.png){height=16.5cm}

*Nota.* Elaboración propia. El diagrama UML representa el flujo objetivo. La garantía se habilita por corte y el vencimiento opera durante las etapas de contratación.

El diseño objetivo inicia el bloqueo cuando ambas identidades están verificadas y ambas partes acuerdan el horario y el precio. La plataforma emite el contrato y registra la aceptación de cada parte. La modalidad sin firma habilita el cobro de la renta tras ambas aceptaciones. Cuando ambas partes eligen SimpleFirma, la plataforma acredita los aportes antes de habilitar las firmas y exige ambas firmas para habilitar la renta. La garantía, cuando corresponde y está habilitada, se cobra por separado después de acreditar la renta.

Para hora, bloque o sesión, la ruta principal guarda el contrato sin firma y ofrece SimpleFirma como opción. Para el arriendo mensual de inmuebles, la interfaz recomienda SimpleFirma y permite continuar sin ella. La modalidad sin firma informa «Este contrato se guarda sin firma electrónica de las partes». La emisión registra la identidad verificada por RUT y nombre completo de ambas partes y, cuando corresponde, la representación evaluada en un expediente separado.

Si ambas partes eligen SimpleFirma, la plataforma muestra el desglose. El aporte se divide por mitades o se asigna íntegramente al arrendador si ofreció firma gratis. El peso impar queda a cargo del arrendador. Para la renta, el objetivo integra Mercado Pago Checkout Pro mediante Preferences y vinculación OAuth del arrendador. Split distribuye la renta y la comisión. La garantía queda fuera del primer corte y requiere verificar su operación antes de habilitarse.

El vencimiento libera el bloqueo mediante una transición atómica. Un pago tardío ingresa a conciliación sin reactivar la reserva. La operación registra evidencia de ingreso y de entrega conforme a HU35 y los casos CU-33, CU-34 y CU-48. Tras la entrega del arrendatario, el titular confirma la desocupación y puede republicar el espacio. El sistema conserva el contrato y los demás intervalos vigentes.

Si vence un aporte antes de abrir la solicitud de firma, la plataforma devuelve los aportes acreditados. Si la solicitud ya está abierta y vence sin ambas firmas, la política del piloto devuelve los aportes y contempla el cargo irrecuperable del proveedor según el presupuesto aprobado. Si ambas firmas se completan y vence la renta, se conserva el servicio de firma y su cargo según las condiciones informadas. Los errores de plataforma se tramitan por la ruta de devolución aplicable.

La Figura 9 muestra los plazos de ensayo ratificados y el punto de inicio de cada etapa.

**Figura 9**\
*Ventanas de ensayo de contratación y cobros*

![](assets/figuras/fig09_ventanas_contratacion.png){height=11cm}

*Nota.* Elaboración propia según el ADR del 4 de noviembre de 2026. La ventana inicial con SimpleFirma comprende 30 minutos para acreditar los aportes. Los 60 minutos para firmar comienzan al acreditarlos. La ruta sin firma dispone de 15 minutos para aceptar y pagar la renta desde el inicio del bloqueo. En la ruta SimpleFirma, los 15 minutos para renta comienzan al completar ambas firmas. El plazo de garantía comienza al acreditar la renta. Cada etapa se sujeta al límite total del bloqueo y los reintentos conservan el vencimiento.

### 9.1.3. Gestión de una solicitud de privacidad

La Figura 10 representa el tratamiento objetivo de una solicitud de privacidad.

**Figura 10**\
*Actividad de evaluación y tratamiento de una solicitud de privacidad*

![](assets/figuras/fig10_privacidad_objetivo.png)

*Nota.* Elaboración propia. El flujo objetivo distingue la solicitud, la decisión, la acción sobre datos y objetos y el registro del resultado.

## 9.2. Casos de uso y componentes

El Anexo C organiza los casos de uso por módulo. Arrendador y arrendatario representan papeles de una cuenta en una operación. El administrador actúa con capacidades separadas. Los proveedores participan como sistemas externos en las operaciones que requieren su intervención. La arquitectura de componentes se describe en el Capítulo VIII y el contrato de interfaz se identifica en el Anexo E.

## 9.3. Modelo de datos objetivo y esquema físico de referencia

La persistencia utiliza PostgreSQL 18 y PostGIS 3.6. El diseño distingue el modelo lógico ratificado, el catálogo derivado de migraciones y el estado observado en cada entorno. La línea base del diseño de oferta, contratación y cobros corresponde al ADR de espaciGo ratificado el 4 de noviembre de 2026, registrado en `planning/decisiones/adr_objetivo_espacios_contratacion_cobros.md` en el commit `4e26d52b57d9687c4b6b7a778e89dbbb5be855e5`. La copia de trabajo del ADR incorpora explícitamente la novena categoría. Su incorporación al catálogo físico se registra por separado en V000067, commit `b1b38d1`. El Anexo D distingue esta decisión del perfil físico sembrado por la migración.

### 9.3.1. Modelo lógico objetivo

El espacio representa una unidad reservable exclusiva con un titular vigente. La categoría Inmuebles distingue casa, departamento, habitación y cabaña. Cada publicación corresponde a la unidad que se arrienda, como una casa completa o una habitación de uso exclusivo. El inventario compartido y la asignación de múltiples unidades requieren un modelo y pruebas específicos. La publicación, la titularidad y la ocupación tienen estados independientes. La galería administra hasta 30 posiciones, incluidas las cargas reservadas. El modelo separa los medios públicos de la evidencia documental privada y asigna a cada clase sus permisos y su ciclo de vida.

La emisión contractual vincula la reserva con las identidades verificadas, las facultades de representación cuando corresponda, el horario y los importes acordados. Cada emisión conserva un identificador, una huella y sus condiciones. Un cambio de condiciones genera otra emisión. La aceptación de cada parte y la firma electrónica opcional mantienen registros independientes.

El modelo separa los aportes de firma, la renta y la garantía en obligaciones identificables. El registro financiero distingue pagador, intento, evento externo y movimiento acreditado. La devolución referencia el pago y su pagador original. La confirmación de desocupación cierra el bloqueo de la reserva y conserva el vínculo histórico con el contrato y los demás intervalos vigentes.

### 9.3.2. Relación entre el modelo lógico y el esquema físico

La Figura 11 relaciona las entidades lógicas que la Tabla D.1 vincula con el esquema físico.

**Figura 11**\
*Modelo lógico del núcleo transaccional*

![](assets/figuras/fig13_modelo_logico_objetivo.png){height=11cm}

*Nota.* Elaboración propia. La figura representa relaciones lógicas objetivo. La reserva se vincula con cero o una ocupación en el núcleo representado. Una ocupación manual puede existir sin reserva. La aceptación se registra por parte y por emisión. El Anexo D documenta las tablas derivadas del DDL y el alcance de su comparación con el catálogo local.

La Tabla D.1 vincula las entidades lógicas con sus relaciones físicas de referencia. El Anexo D distingue las 110 tablas de aplicación derivadas del DDL de las 104 tablas de aplicación de la captura local V000075. Las seis relaciones adicionales corresponden a la verificación documental declarada en V000079. La evolución física del modelo objetivo parte del mapeo de entidades a tablas vigentes y del análisis de las restricciones que exige cada incremento.

### 9.3.3. Integridad temporal y concurrencia

La migración V000009 de espaciGo declara en `public.ocupacion` la columna `intervalo` de tipo `tstzrange`. La restricción de exclusión GiST compara la igualdad de `espacio_id` y el solapamiento de `intervalo` mediante el operador de rangos `&&`, con un predicado que limita la comparación a las filas activas. El operador temporal pertenece a PostgreSQL. PostGIS se utiliza para las consultas geoespaciales.

El criterio objetivo utiliza una autoridad de ocupación y un bloqueo activo por reserva. La verificación contempla solapamientos, intervalos adyacentes, vencimiento atómico, duplicados y pagos tardíos que ingresan a conciliación. Los resultados se registran por versión y entorno en el Capítulo X y el Anexo F.
