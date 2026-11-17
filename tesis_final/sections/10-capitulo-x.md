# CAPÍTULO X: Detalle de la Arquitectura a implementar

## 10. Detalle de la Arquitectura a implementar

### 10.1. Diagrama BPMN

La Figura 8 representa el proceso de contratación objetivo mediante tareas, compuertas y participantes. Los diagramas posteriores detallan publicación, estados, ventanas y privacidad.

**Figura 8**\
*Proceso de contratación objetivo en BPMN*

![](assets/figuras/bpmn_contratacion_tihi84.png){height=16.5cm}

*Nota.* Elaboración propia a partir del ADR. La garantía y la firma dependen de sus condiciones de habilitación.

### 10.2. Diagrama de casos de uso

La especificación de requerimientos de la plataforma **espaciGo** se articula en torno a la interacción de roles de arrendamiento definidos por operación, capacidades de administración e integraciones externas:

La Figura 9 sintetiza los papeles de la cuenta y la administración.

**Figura 9**\
*Diagrama de Interacción entre Actores y Módulos de la Plataforma*

![](assets/figuras/anexo_c/cu_actores.png)

*Nota.* Elaboración propia en base a la arquitectura modular de la plataforma espaciGo.

---

El Anexo C organiza los casos de uso por módulo. Arrendador y arrendatario representan papeles de una cuenta en una operación. El administrador actúa con capacidades separadas. Los proveedores participan como sistemas externos en las operaciones que requieren su intervención. La arquitectura de componentes se describe en la sección 10.3 y el contrato de interfaz se identifica en el Anexo E.

### 10.3. Diagrama de componentes

La Figura 10 detalla la vista de aplicaciones y el enlace entre la interfaz, el núcleo y sus adaptadores AWS. La aplicación utiliza S3 y PostgreSQL local durante el desarrollo. El destino Fargate conserva los mismos límites de dominio. El Anexo E conserva el contrato OpenAPI de referencia.

**Figura 10**\
*Componentes de aplicación y adaptadores de espaciGo*

![](assets/imagenes/fig09_componentes_aws.png){height=15.5cm}

*Nota.* Elaboración propia a partir de la estructura del repositorio y el contrato de desarrollo. La autorización se aplica por recurso y el control If-Match se utiliza en operaciones de galería. La habilitación de proveedores externos sigue pendiente.

### 10.4. Modelo de datos

La persistencia utiliza PostgreSQL 18 y PostGIS 3.6. El diseño distingue el modelo lógico ratificado, el catálogo derivado de migraciones y el estado observado en cada entorno. La línea base del diseño de oferta, contratación y cobros corresponde al ADR de espaciGo ratificado el 4 de noviembre de 2026, registrado en `planning/decisiones/adr_objetivo_espacios_contratacion_cobros.md` en el commit `4e26d52b57d9687c4b6b7a778e89dbbb5be855e5`. La copia de trabajo del ADR incorpora explícitamente la novena categoría. Su incorporación al catálogo físico se registra por separado en V000067, commit `b1b38d1`. El Anexo D distingue esta decisión del perfil físico sembrado por la migración.

#### 10.4.1. Modelo lógico

El espacio representa una unidad reservable exclusiva con un titular vigente. La categoría Inmuebles distingue casa, departamento, habitación y cabaña. Cada publicación corresponde a la unidad que se arrienda, como una casa completa o una habitación de uso exclusivo. El inventario compartido y la asignación de múltiples unidades requieren un modelo y pruebas específicos. La publicación, la titularidad y la ocupación tienen estados independientes. La galería administra hasta 30 posiciones, incluidas las cargas reservadas. El modelo separa los medios públicos de la evidencia documental privada y asigna a cada clase sus permisos y su ciclo de vida.

La emisión contractual vincula la reserva con las identidades verificadas, las facultades de representación cuando corresponda, el horario y los importes acordados. Cada emisión conserva un identificador, una huella y sus condiciones. Un cambio de condiciones genera otra emisión. La aceptación de cada parte y la firma electrónica opcional mantienen registros independientes.

El modelo separa los aportes de firma, la renta y la garantía en obligaciones identificables. El registro financiero distingue pagador, intento, evento externo y movimiento acreditado. La devolución referencia el pago y su pagador original. La confirmación de desocupación cierra el bloqueo de la reserva y conserva el vínculo histórico con el contrato y los demás intervalos vigentes.

#### 10.4.2. Modelo Físico

La Figura 11 relaciona las entidades lógicas. La Figura 12 presenta un recorte del esquema físico de ensayo y la Tabla D.1 documenta la correspondencia entre ambos niveles.

**Figura 11**\
*Modelo lógico del núcleo transaccional*

![](assets/figuras/fig13_modelo_logico_objetivo.png){height=11cm}

*Nota.* Elaboración propia. La figura representa relaciones lógicas objetivo. La reserva se vincula con cero o una ocupación en el núcleo representado. Una ocupación manual puede existir sin reserva. La aceptación se registra por parte y por emisión. El Anexo D documenta las tablas derivadas del DDL y el alcance de su comparación con el catálogo local.

**Figura 12**\
*Esquema físico del núcleo transaccional de ensayo*

![](assets/figuras/erd_fisico_ensayo.png){height=17cm}

*Nota.* Elaboración propia a partir del DDL y el Anexo D. Se muestran columnas y relaciones seleccionadas del esquema public. La geografía del ejemplo pertenece a la ubicación sintética. La bandeja de eventos identifica agregados mediante tipo e identificador y carece de una clave foránea polimórfica.

La Tabla D.1 vincula las entidades lógicas con sus relaciones físicas de referencia. El Anexo D distingue las 110 tablas de aplicación derivadas del DDL de las 104 tablas de aplicación de la captura local V000075. Las seis relaciones adicionales corresponden a la verificación documental declarada en V000079. La evolución física del modelo objetivo parte del mapeo de entidades a tablas vigentes y del análisis de las restricciones que exige cada incremento.

#### 10.4.3. Diccionario de datos

El Anexo D registra tipos, nulabilidad, claves y restricciones, con la procedencia y el alcance del contraste físico.

#### 10.4.4. Integridad temporal y concurrencia

La migración V000009 de espaciGo declara en `public.ocupacion` la columna `intervalo` de tipo `tstzrange`. La restricción `EXCLUDE USING gist` compara la igualdad de `espacio_id` y el solapamiento de `intervalo` mediante el operador de rangos `&&`, con un predicado que limita la comparación a las filas activas. El operador temporal pertenece a PostgreSQL. PostGIS se utiliza para las consultas geoespaciales.

El criterio objetivo utiliza una autoridad de ocupación y un bloqueo activo por reserva. La verificación contempla solapamientos, intervalos adyacentes, vencimiento atómico, duplicados y pagos tardíos que ingresan a conciliación. Los resultados se registran por versión y entorno en el Capítulo XII y el Anexo F.

### 10.5. Topología de comunicaciones

El navegador accede al borde Cloudflare por HTTPS. El origen web requiere configurar y comprobar TLS y la restricción de ingreso. En el destino Fargate, el BFF Next.js invoca la API Go mediante loopback dentro de la misma tarea. La API accede a RDS por TCP 5432 y TLS en subredes privadas. La comunicación con S3 utiliza HTTPS y un endpoint Gateway de la VPC. Los buckets separan finalidades y mantienen bloqueo de acceso público. La aplicación autoriza la entrega de cada objeto.

### 10.6. Diagrama de Infraestructura

La topología objetivo adopta la región inicial us-east-2, sujeta a la selección habilitada del proyecto. Una tarea ECS Fargate reúne la web Next.js y la API Go en modo awsvpc. El diseño utiliza RDS PostgreSQL Single-AZ en subredes privadas, almacenamiento gp3 cifrado y respaldo automático con retención de siete días. El procedimiento de aceptación verifica PITR, versión del motor, extensiones y recuperación. La Figura 13 representa este destino y distingue los componentes que requieren completar su configuración.

**Figura 13**\
*Topología objetivo y ruta de entrega de espaciGo en AWS*

![](assets/imagenes/fig12_topologia_aws.png){height=16cm}

*Nota.* Elaboración propia a partir de los ADR-AWS-01 a ADR-AWS-05 y Terraform del corte 3dc1c18 [@espacigoaws2026]. La figura describe el destino de despliegue. La preparación de ECS/ECR, ingreso, TLS y entrega OIDC conserva comprobaciones pendientes.

#### 10.6.1. Segmentación de red y comunicaciones privadas
La VPC declara dos subredes públicas y dos privadas, con zonas descubiertas desde la región configurada. La base acepta conexiones desde el grupo de seguridad de la tarea. El diseño restringe el origen web al borde autorizado y conserva la API en loopback. El Terraform inspeccionado aún declara ingreso amplio en el puerto 4000. Su endurecimiento y la prueba de acceso directo al origen constituyen condiciones previas de habilitación. Dos subredes para RDS permiten definir su grupo de subredes y conservan una instancia Single-AZ en el corte inicial.

### 10.7. Diagrama de Arquitectura

La arquitectura integrada se lee en tres vistas complementarias. La Figura 10 muestra la interacción de componentes, las figuras 10 y 11 describen persistencia y la Figura 13 sitúa la solución en su infraestructura. Las figuras siguientes precisan el comportamiento que conecta estas vistas.

El catálogo versionado utiliza OpenAPI 3.1. La galería admite hasta 30 posiciones por espacio, incluidas las cargas reservadas. La selección de portada exige enviar en `If-Match` el ETag fuerte de la revisión que leyó el editor. Si otra operación cambia el espacio antes de guardar, la revisión queda desactualizada y la solicitud se rechaza. Esto evita que una elección basada en una galería anterior sobrescriba una actualización posterior. El Anexo E identifica la versión del contrato y el alcance de la evidencia.

La especificación utiliza diagramas de actividad UML para la publicación, los plazos de ensayo y el tratamiento de solicitudes de privacidad. Una máquina de estados representa las transiciones de contratación y ocupación.

#### 10.7.1. Publicación de un espacio

El flujo objetivo valida la titularidad y las reglas del anuncio al publicar. La verificación de identidad de ambas partes corresponde a la emisión contractual.

La Figura 14 separa las condiciones de publicación de la verificación contractual.

**Figura 14**\
*Actividad de publicación y control de titularidad*

![](assets/figuras/fig08_publicacion_objetivo.png)

*Nota.* Elaboración propia. El diagrama UML representa las condiciones de publicación del ADR del 4 de noviembre de 2026.

#### 10.7.2. Contratación, cobros y cierre

La Figura 15 representa los estados y transiciones del recorrido objetivo. El Anexo E identifica rutas de ensayo y el Capítulo XIII establece condiciones para habilitar proveedores.

**Figura 15**\
*Máquina de estados objetivo de la reserva y su ocupación*

![](assets/figuras/fig09_contratacion_objetivo.png){height=16.5cm}

*Nota.* Elaboración propia. Las etiquetas representan etapas del diseño. Los nombres persistidos del ensayo se documentan en el Anexo D. La garantía se habilita por corte y el pago tardío se concilia sin reactivar la reserva.

El diseño objetivo inicia el bloqueo cuando ambas identidades están verificadas y ambas partes acuerdan el horario y el precio. La plataforma emite el contrato y registra la aceptación de cada parte. La modalidad sin firma habilita el cobro de la renta tras ambas aceptaciones. Cuando ambas partes eligen SimpleFirma, la plataforma acredita los aportes antes de habilitar las firmas y exige ambas firmas para habilitar la renta. La garantía, cuando corresponde y está habilitada, se cobra por separado después de acreditar la renta.

Para hora, bloque o sesión, la ruta principal guarda el contrato sin firma y ofrece SimpleFirma como opción. Para el arriendo mensual de inmuebles, la interfaz recomienda SimpleFirma y permite continuar sin ella. La modalidad sin firma informa «Este contrato se guarda sin firma electrónica de las partes». La emisión registra la identidad verificada por RUT y nombre completo de ambas partes y, cuando corresponde, la representación evaluada en un expediente separado.

Si ambas partes eligen SimpleFirma, la plataforma muestra el desglose. El aporte se divide por mitades o se asigna íntegramente al arrendador si ofreció firma gratis. El peso impar queda a cargo del arrendador. Para la renta, el objetivo integra Mercado Pago Checkout Pro mediante Preferences y vinculación OAuth del arrendador. Split distribuye la renta y la comisión. La garantía queda fuera del primer corte y requiere verificar su operación antes de habilitarse.

El registro local `outbox_evento_local` permite separar la confirmación de un cambio de estado del envío posterior de eventos. El patrón de bandeja transaccional registra el cambio y su evento en la misma transacción, de modo que un fallo durante el envío deje trabajo recuperable. La clave de deduplicación y el registro de intentos respaldan los reintentos del trabajador. El efecto externo requiere idempotencia propia y conciliación, en especial para los cobros. El Anexo D documenta la estructura del registro.

El vencimiento libera el bloqueo mediante una transición atómica. Un pago tardío ingresa a conciliación sin reactivar la reserva. La operación registra evidencia de ingreso y de entrega conforme a HU35 y los casos CU-33, CU-34 y CU-48. Tras la entrega del arrendatario, el titular confirma la desocupación y puede republicar el espacio. El sistema conserva el contrato y los demás intervalos vigentes.

Si vence un aporte antes de abrir la solicitud de firma, la plataforma devuelve los aportes acreditados. Si la solicitud ya está abierta y vence sin ambas firmas, la política del piloto devuelve los aportes y contempla el cargo irrecuperable del proveedor según el presupuesto aprobado. Si ambas firmas se completan y vence la renta, se conserva el servicio de firma y su cargo según las condiciones informadas. Los errores de plataforma se tramitan por la ruta de devolución aplicable.

La Figura 16 muestra los plazos de ensayo ratificados y el punto de inicio de cada etapa.

**Figura 16**\
*Ventanas de ensayo de contratación y cobros*

![](assets/figuras/fig09_ventanas_contratacion.png){height=11cm}

*Nota.* Elaboración propia según el ADR del 4 de noviembre de 2026. La ventana inicial con SimpleFirma comprende 30 minutos para acreditar los aportes. Los 60 minutos para firmar comienzan al acreditarlos. La ruta sin firma dispone de 15 minutos para aceptar y pagar la renta desde el inicio del bloqueo. En la ruta SimpleFirma, los 15 minutos para renta comienzan al completar ambas firmas. El plazo de garantía comienza al acreditar la renta. Cada etapa se sujeta al límite total del bloqueo y los reintentos conservan el vencimiento.

#### 10.7.3. Gestión de una solicitud de privacidad

La Figura 17 representa el tratamiento objetivo de una solicitud de privacidad.

**Figura 17**\
*Actividad de evaluación y tratamiento de una solicitud de privacidad*

![](assets/figuras/fig10_privacidad_objetivo.png)

*Nota.* Elaboración propia. El flujo objetivo distingue la solicitud, la decisión, la acción sobre datos y objetos y el registro del resultado.

### 10.8. Construcción local y transición al destino

El entorno local ejecuta Next.js en el puerto 3000, la API Go en 8080, PostgreSQL en Docker y aws-emulator en un endpoint HTTPS propio. Mailpit recibe correo de pruebas mediante SMTP y permite inspeccionar los mensajes. El emulador expone interfaces para S3, SSM, logs e IAM. Terraform separa cinco buckets de medios, evidencias, identidad, documentos del espacio y registro de supresiones, con versionado y SSE-S3. El almacenamiento documental conserva cifrado en la aplicación y autorización por finalidad.

El diseño de operación utiliza CloudWatch para logs, SSM para parámetros y roles de ejecución y tarea con permisos delimitados. Zoho conserva el correo del destino. La preparación para Chile parametriza la región y descubre sus zonas. La decisión de traslado requiere confirmar habilitación del proyecto, catálogo de servicios, versión de PostgreSQL y PostGIS y una nueva validación de carga y recuperación. El acceso anticipado anunciado por Amazon fundamenta esa posibilidad, mientras la región inicial conserva el corte declarado [@awschile2026].
