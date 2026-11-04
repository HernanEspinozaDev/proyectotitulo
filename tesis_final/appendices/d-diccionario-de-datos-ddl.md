# ANEXO D: DICCIONARIO DE DATOS DEL ESQUEMA FÍSICO POSTGRESQL Y POSTGIS

Este catálogo se reconstruye aplicando en orden las migraciones SQL estructurales disponibles. Las claves y nulabilidades corresponden al estado resultante de esas definiciones; no implica que se haya consultado una base persistente.

El inventario derivado del DDL contiene **110 tablas de aplicación** y excluye el ledger `schema_migrations`. La versión de creación más alta registrada en las fichas es V000079. En la comparación por nombre con la captura local V000075 del 4 de noviembre de 2026, coinciden 104 tablas de aplicación. Las otras seis corresponden al dominio de verificación documental y se declaran en V000079. Esta comparación identifica relaciones por nombre. La comparación de esas 104 tablas con la captura V75 identifica 879 columnas coincidentes por nombre, tipo base y nulabilidad. La comparación normaliza los alias PostgreSQL y trata bigserial como bigint para comparar el tipo base. La comprobación de valores por defecto, restricciones y permisos requiere evidencia separada por versión y entorno.

El modelo lógico objetivo se describe en la sección 9.3. El inventario físico registra las claves y relaciones declaradas en SQL. Las relaciones foráneas identifican las columnas de origen y destino declaradas en `REFERENCES`, y las claves compuestas se presentan como conjuntos.

## Correspondencia lógica y física

**Tabla D.1**\
*Relaciones físicas de referencia para el modelo objetivo*

| Concepto lógico | Relaciones de referencia | Criterio de evolución |
|---|---|---|
| Oferta y titularidad | `espacio`, `espacio_publicacion_historial_local` | Verificar quién puede publicar y recuperar el historial del titular. |
| Disponibilidad | `ocupacion`, `cotizacion_reserva_ensayo`, `reserva_ensayo_local` | Conservar una autoridad de ocupación y comprobar concurrencia y vencimiento. |
| Emisión | `contrato_ensayo_local`, `contrato_ensayo_firma` | Identificar emisión, aceptación por parte y firma opcional. |
| Cobros | `reserva_pago_ensayo` y relaciones de eventos | Identificar obligación, pagador, acreditación y reverso. |

*Nota.* Elaboración propia. El mapeo identifica puntos de partida y criterios de evolución física por corte.

## Dominio: Gobernanza, privacidad y administración

### B.001 Tabla `public.aceptacion_terminos`
- **Migración de creación:** `V000001`
- **Atributos:** 6

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `usuario_id` | `uuid` | UQ compuesta (usuario_id, version_id); FK → `public.usuario(usuario_id→id)` [aceptacion_terminos_usuario_fk]; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `version_id` | `uuid` | UQ compuesta (usuario_id, version_id); FK → `public.version_terminos(version_id→id)` [aceptacion_terminos_version_fk]; NOT NULL | Atributo `version_id`; el nombre y tipo se conservan según el DDL. |
| `aceptada_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Atributo `aceptada_en`; el nombre y tipo se conservan según el DDL. |
| `canal` | `text` | NOT NULL | Atributo `canal`; el nombre y tipo se conservan según el DDL. |
| `retirar_en` | `timestamptz` | NULL permitido | Atributo `retirar_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CONSTRAINT aceptacion_terminos_pk PRIMARY KEY (id)`
- `CONSTRAINT aceptacion_terminos_usuario_fk FOREIGN KEY (usuario_id) REFERENCES public.usuario (id) ON DELETE RESTRICT`
- `CONSTRAINT aceptacion_terminos_version_fk FOREIGN KEY (version_id) REFERENCES public.version_terminos (id) ON DELETE RESTRICT`
- `CONSTRAINT aceptacion_terminos_usuario_version_uk UNIQUE (usuario_id, version_id)`
- `CONSTRAINT aceptacion_terminos_canal_ck CHECK (canal IN ('web', 'api', 'administrado'))`


### B.002 Tabla `public.administrador_global`
- **Migración de creación:** `V000058`
- **Atributos:** 4

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `usuario_id` | `uuid` | PK; FK → `public.usuario(usuario_id→id)`; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `concedido_en` | `timestamptz` | NOT NULL | Atributo `concedido_en`; el nombre y tipo se conservan según el DDL. |
| `concedido_por` | `uuid` | FK → `public.usuario(concedido_por→id)`; NULL permitido | Atributo `concedido_por`; el nombre y tipo se conservan según el DDL. |
| `motivo_codigo` | `text` | NOT NULL | Atributo `motivo_codigo`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (motivo_codigo IN ('bootstrap_propietario','recuperacion_local','concesion_administrativa'))`


### B.003 Tabla `public.administrador_global_bootstrap`
- **Migración de creación:** `V000058`
- **Atributos:** 3

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `singleton` | `boolean` | PK; DEFAULT `true`; NOT NULL | Atributo `singleton`; el nombre y tipo se conservan según el DDL. |
| `usuario_id` | `uuid` | UQ; FK → `public.usuario(usuario_id→id)`; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `creado_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |

**Restricciones DDL vigentes:**

- `CHECK (singleton)`


### B.004 Tabla `public.administrador_global_bootstrap_evento`
- **Migración de creación:** `V000058`
- **Atributos:** 8

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `usuario_objetivo_id` | `uuid` | NOT NULL | Atributo `usuario_objetivo_id`; el nombre y tipo se conservan según el DDL. |
| `actor_tipo` | `text` | NOT NULL | Atributo `actor_tipo`; el nombre y tipo se conservan según el DDL. |
| `accion` | `text` | NOT NULL | Atributo `accion`; el nombre y tipo se conservan según el DDL. |
| `resultado` | `text` | NOT NULL | Atributo `resultado`; el nombre y tipo se conservan según el DDL. |
| `motivo_codigo` | `text` | NOT NULL | Atributo `motivo_codigo`; el nombre y tipo se conservan según el DDL. |
| `correlacion_id` | `uuid` | NOT NULL | Atributo `correlacion_id`; el nombre y tipo se conservan según el DDL. |
| `ocurrida_en` | `timestamptz` | NOT NULL | Atributo `ocurrida_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (accion IN ('bootstrap','recuperacion'))`
- `CHECK (resultado IN ('exito','rechazo'))`
- `CHECK (length(btrim(motivo_codigo)) BETWEEN 1 AND 60)`
- `CONSTRAINT administrador_global_bootstrap_evento_actor_tipo_check CHECK (actor_tipo IN ('cli_local', 'cli_gcp06'))`


### B.005 Tabla `public.atributo_filtro_publico`
- **Migración de creación:** `V000055`
- **Atributos:** 6

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `categoria_codigo` | `text` | PK compuesta (categoria_codigo, perfil_version, codigo); UQ compuesta (categoria_codigo, perfil_version, orden); FK → `public.categoria_perfil_atributos(categoria_codigo→categoria_codigo, perfil_version→version)` [anon_8]; NOT NULL | Atributo `categoria_codigo`; el nombre y tipo se conservan según el DDL. |
| `perfil_version` | `integer` | PK compuesta (categoria_codigo, perfil_version, codigo); UQ compuesta (categoria_codigo, perfil_version, orden); FK → `public.categoria_perfil_atributos(categoria_codigo→categoria_codigo, perfil_version→version)` [anon_8]; NOT NULL | Atributo `perfil_version`; el nombre y tipo se conservan según el DDL. |
| `codigo` | `text` | PK compuesta (categoria_codigo, perfil_version, codigo); NOT NULL | Atributo `codigo`; el nombre y tipo se conservan según el DDL. |
| `etiqueta` | `text` | NOT NULL | Atributo `etiqueta`; el nombre y tipo se conservan según el DDL. |
| `tipo` | `text` | NOT NULL | Atributo `tipo`; el nombre y tipo se conservan según el DDL. |
| `orden` | `smallint` | UQ compuesta (categoria_codigo, perfil_version, orden); NOT NULL | Atributo `orden`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (perfil_version > 0)`
- `CHECK (codigo ~ '^[a-z][a-z0-9_]{0,59}$')`
- `CHECK (length(btrim(etiqueta)) BETWEEN 1 AND 80)`
- `CHECK (orden > 0)`
- `PRIMARY KEY (categoria_codigo,perfil_version,codigo)`
- `UNIQUE (categoria_codigo,perfil_version,orden)`
- `FOREIGN KEY (categoria_codigo,perfil_version) REFERENCES public.categoria_perfil_atributos(categoria_codigo,version)`
- `CONSTRAINT atributo_filtro_publico_tipo_check CHECK (tipo IN ('boolean','integer','number','enum','enum_list'))`


### B.006 Tabla `public.aviso_local`
- **Migración de creación:** `V000036`
- **Atributos:** 18

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `tipo_evento` | `text` | NOT NULL | Atributo `tipo_evento`; el nombre y tipo se conservan según el DDL. |
| `agregado_tipo` | `text` | NOT NULL | Atributo `agregado_tipo`; el nombre y tipo se conservan según el DDL. |
| `agregado_id` | `uuid` | NOT NULL | Atributo `agregado_id`; el nombre y tipo se conservan según el DDL. |
| `destinatario_id` | `uuid` | FK → `public.usuario(destinatario_id→id)`; NOT NULL | Atributo `destinatario_id`; el nombre y tipo se conservan según el DDL. |
| `clave_deduplicacion` | `text` | UQ; NOT NULL | Atributo `clave_deduplicacion`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | DEFAULT `'pendiente'`; NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `ciclo` | `integer` | DEFAULT `1`; NOT NULL | Atributo `ciclo`; el nombre y tipo se conservan según el DDL. |
| `intentos_total` | `integer` | DEFAULT `0`; NOT NULL | Atributo `intentos_total`; el nombre y tipo se conservan según el DDL. |
| `intentos_ciclo` | `integer` | DEFAULT `0`; NOT NULL | Atributo `intentos_ciclo`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `proximo_intento_en` | `timestamptz` | NOT NULL | Atributo `proximo_intento_en`; el nombre y tipo se conservan según el DDL. |
| `lease_hasta` | `timestamptz` | NULL permitido | Atributo `lease_hasta`; el nombre y tipo se conservan según el DDL. |
| `entregada_en` | `timestamptz` | NULL permitido | Atributo `entregada_en`; el nombre y tipo se conservan según el DDL. |
| `fallo_terminal_en` | `timestamptz` | NULL permitido | Atributo `fallo_terminal_en`; el nombre y tipo se conservan según el DDL. |
| `cancelada_en` | `timestamptz` | NULL permitido | Atributo `cancelada_en`; el nombre y tipo se conservan según el DDL. |
| `codigo_error` | `text` | NULL permitido | Atributo `codigo_error`; el nombre y tipo se conservan según el DDL. |
| `retirar_en` | `timestamptz` | NULL permitido | Atributo `retirar_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (estado IN ('pendiente','procesando','entregada','fallo_terminal','cancelada'))`
- `CHECK (ciclo > 0)`
- `CHECK (intentos_total >= 0)`
- `CHECK (intentos_ciclo BETWEEN 0 AND 8)`
- `CHECK ((estado='entregada' AND entregada_en IS NOT NULL AND retirar_en=entregada_en + interval '30 days') OR (estado='fallo_terminal' AND fallo_terminal_en IS NOT NULL AND retirar_en=fallo_terminal_en + interval '30 days') OR (estado='cancelada' AND cancelada_en IS NOT NULL AND retirar_en=cancelada_en + interval '30 days') OR (estado IN ('pendiente','procesando') AND retirar_en IS NULL))`
- `CONSTRAINT aviso_local_tipo_evento_check CHECK (tipo_evento IN ( 'checkin_registrado','resena_reportada','reclamo_abierto','reclamo_resuelto','reserva_cancelada', 'cuenta_bloqueada_login','verificacion_aprobada','verificacion_rechazada','pago_arriendo_confirmado','pago_arriendo_rechazado', 'nueva_reserva_pagada','invitacion_firma','contrato_firmado' ))`
- `CONSTRAINT aviso_local_agregado_tipo_check CHECK (agregado_tipo IN ('reserva','reporte_resena','usuario','verificacion','contrato'))`


### B.007 Tabla `public.aviso_local_ciclo`
- **Migración de creación:** `V000036`
- **Atributos:** 11

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `aviso_id` | `uuid` | PK compuesta (aviso_id, ciclo); UQ compuesta (aviso_id, clave_idempotencia); FK → `public.aviso_local(aviso_id→id)`; NOT NULL | Atributo `aviso_id`; el nombre y tipo se conservan según el DDL. |
| `ciclo` | `integer` | PK compuesta (aviso_id, ciclo); NOT NULL | Atributo `ciclo`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `iniciada_en` | `timestamptz` | NOT NULL | Atributo `iniciada_en`; el nombre y tipo se conservan según el DDL. |
| `finalizada_en` | `timestamptz` | NULL permitido | Atributo `finalizada_en`; el nombre y tipo se conservan según el DDL. |
| `intentos` | `integer` | DEFAULT `0`; NOT NULL | Atributo `intentos`; el nombre y tipo se conservan según el DDL. |
| `codigo_resultado` | `text` | NULL permitido | Atributo `codigo_resultado`; el nombre y tipo se conservan según el DDL. |
| `actor_reapertura_id` | `uuid` | FK → `public.usuario(actor_reapertura_id→id)`; NULL permitido | Atributo `actor_reapertura_id`; el nombre y tipo se conservan según el DDL. |
| `motivo_reapertura_codigo` | `text` | NULL permitido | Atributo `motivo_reapertura_codigo`; el nombre y tipo se conservan según el DDL. |
| `correlacion_id` | `text` | NULL permitido | Atributo `correlacion_id`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (aviso_id, clave_idempotencia); NULL permitido | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (estado IN ('pendiente','entregada','fallo_terminal','cancelada'))`
- `CHECK (intentos BETWEEN 0 AND 8)`
- `CHECK (motivo_reapertura_codigo IN ('smtp_restaurado','reintento_operativo'))`
- `PRIMARY KEY(aviso_id,ciclo)`
- `UNIQUE(aviso_id,clave_idempotencia)`
- `CHECK ((estado='pendiente')=(finalizada_en IS NULL))`


### B.008 Tabla `public.aviso_local_recuperacion_auditoria`
- **Migración de creación:** `V000036`
- **Atributos:** 8

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `aviso_id` | `uuid` | UQ compuesta (aviso_id, clave_idempotencia); NOT NULL | Atributo `aviso_id`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NOT NULL | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `motivo_codigo` | `text` | NOT NULL | Atributo `motivo_codigo`; el nombre y tipo se conservan según el DDL. |
| `ocurrida_en` | `timestamptz` | NOT NULL | Atributo `ocurrida_en`; el nombre y tipo se conservan según el DDL. |
| `correlacion_id` | `text` | NOT NULL | Atributo `correlacion_id`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (aviso_id, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `retirar_en` | `timestamptz` | NOT NULL | Atributo `retirar_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (motivo_codigo IN ('smtp_restaurado','reintento_operativo'))`
- `UNIQUE(aviso_id,clave_idempotencia)`
- `CHECK (retirar_en=ocurrida_en + interval '5 years')`


### B.009 Tabla `public.baja_archivo_pendiente_local`
- **Migración de creación:** `V000025`
- **Atributos:** 9

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `ejecucion_id` | `uuid` | PK compuesta (ejecucion_id, evidencia_id); FK → `public.ejecucion_baja_local(ejecucion_id→id)`; NOT NULL | Atributo `ejecucion_id`; el nombre y tipo se conservan según el DDL. |
| `evidencia_id` | `uuid` | PK compuesta (ejecucion_id, evidencia_id); NOT NULL | Atributo `evidencia_id`; el nombre y tipo se conservan según el DDL. |
| `intentos` | `integer` | DEFAULT `0`; NOT NULL | Atributo `intentos`; el nombre y tipo se conservan según el DDL. |
| `disponible_en` | `timestamptz` | NOT NULL | Atributo `disponible_en`; el nombre y tipo se conservan según el DDL. |
| `ultimo_codigo_error` | `text` | NULL permitido | Atributo `ultimo_codigo_error`; el nombre y tipo se conservan según el DDL. |
| `completada_en` | `timestamptz` | NULL permitido | Atributo `completada_en`; el nombre y tipo se conservan según el DDL. |
| `claim_owner` | `uuid` | NULL permitido | Atributo `claim_owner`; el nombre y tipo se conservan según el DDL. |
| `claim_hasta` | `timestamptz` | NULL permitido | Atributo `claim_hasta`; el nombre y tipo se conservan según el DDL. |
| `claim_generacion` | `bigint` | DEFAULT `0`; NOT NULL | Atributo `claim_generacion`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (intentos >= 0)`
- `PRIMARY KEY (ejecucion_id,evidencia_id)`
- `CONSTRAINT baja_archivo_claim_lease_pair_ck CHECK ((claim_owner IS NULL) = (claim_hasta IS NULL))`
- `CONSTRAINT baja_archivo_claim_generacion_ck CHECK (claim_generacion >= 0)`


### B.010 Tabla `public.catalogo_ubicacion_publica`
- **Migración de creación:** `V000055`
- **Atributos:** 4

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `version` | `text` | PK; NOT NULL | Atributo `version`; el nombre y tipo se conservan según el DDL. |
| `fuente` | `text` | NOT NULL | Atributo `fuente`; el nombre y tipo se conservan según el DDL. |
| `publicado_en` | `date` | NOT NULL | Atributo `publicado_en`; el nombre y tipo se conservan según el DDL. |
| `activo` | `boolean` | DEFAULT `false`; NOT NULL | Atributo `activo`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (version ~ '^[A-Z0-9_]{1,40}$')`


### B.011 Tabla `public.comuna_publica`
- **Migración de creación:** `V000055`
- **Atributos:** 4

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `catalogo_version` | `text` | PK compuesta (catalogo_version, codigo); UQ compuesta (catalogo_version, region_codigo, codigo); FK → `public.region_publica(catalogo_version→catalogo_version, region_codigo→codigo)` [anon_5]; NOT NULL | Atributo `catalogo_version`; el nombre y tipo se conservan según el DDL. |
| `codigo` | `text` | PK compuesta (catalogo_version, codigo); UQ compuesta (catalogo_version, region_codigo, codigo); NOT NULL | Atributo `codigo`; el nombre y tipo se conservan según el DDL. |
| `region_codigo` | `text` | UQ compuesta (catalogo_version, region_codigo, codigo); FK → `public.region_publica(catalogo_version→catalogo_version, region_codigo→codigo)` [anon_5]; NOT NULL | Atributo `region_codigo`; el nombre y tipo se conservan según el DDL. |
| `nombre` | `text` | NOT NULL | Atributo `nombre`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (codigo ~ '^[0-9]{5}$')`
- `CHECK (length(btrim(nombre)) BETWEEN 1 AND 100)`
- `PRIMARY KEY (catalogo_version, codigo)`
- `UNIQUE (catalogo_version, region_codigo, codigo)`
- `FOREIGN KEY (catalogo_version, region_codigo) REFERENCES public.region_publica(catalogo_version, codigo)`


### B.012 Tabla `public.document_verification_case`
- **Migración de creación:** `V000079`
- **Atributos:** 14

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; UQ compuesta (id, purpose, subject_id, space_id); NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `purpose` | `text` | UQ compuesta (id, purpose, subject_id, space_id); NOT NULL | Atributo `purpose`; el nombre y tipo se conservan según el DDL. |
| `subject_id` | `uuid` | UQ compuesta (id, purpose, subject_id, space_id); FK → `public.usuario(subject_id→id)`; NOT NULL | Atributo `subject_id`; el nombre y tipo se conservan según el DDL. |
| `space_id` | `uuid` | UQ compuesta (id, purpose, subject_id, space_id); FK → `public.espacio(space_id→id)` [document_verification_case_space_fk]; NULL permitido | Atributo `space_id`; el nombre y tipo se conservan según el DDL. |
| `state` | `text` | DEFAULT `'borrador'`; NOT NULL | Atributo `state`; el nombre y tipo se conservan según el DDL. |
| `revision` | `bigint` | DEFAULT `1`; NOT NULL | Atributo `revision`; el nombre y tipo se conservan según el DDL. |
| `reviewer_id` | `uuid` | FK → `public.usuario(reviewer_id→id)`; NULL permitido | Atributo `reviewer_id`; el nombre y tipo se conservan según el DDL. |
| `verified_at` | `timestamptz` | NULL permitido | Atributo `verified_at`; el nombre y tipo se conservan según el DDL. |
| `verified_until` | `timestamptz` | NULL permitido | Atributo `verified_until`; el nombre y tipo se conservan según el DDL. |
| `document_expires_at` | `timestamptz` | NULL permitido | Atributo `document_expires_at`; el nombre y tipo se conservan según el DDL. |
| `revoked_at` | `timestamptz` | NULL permitido | Atributo `revoked_at`; el nombre y tipo se conservan según el DDL. |
| `created_at` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de creación del registro. |
| `updated_at` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de actualización del registro. |
| `superseded_at` | `timestamptz` | NULL permitido | Atributo `superseded_at`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (purpose IN ('identity','space'))`
- `CHECK (state IN ('borrador','enviada','en_revision','requiere_antecedentes','aprobada','rechazada','vencida','revocada'))`
- `CHECK (revision > 0)`
- `CONSTRAINT document_verification_case_scope_ck CHECK ((purpose='identity' AND space_id IS NULL) OR (purpose='space' AND space_id IS NOT NULL))`
- `CONSTRAINT document_verification_case_space_fk FOREIGN KEY(space_id) REFERENCES public.espacio(id) ON DELETE RESTRICT`
- `CONSTRAINT document_verification_case_reviewer_ck CHECK ((state IN ('borrador','enviada') AND reviewer_id IS NULL) OR (state NOT IN ('borrador','enviada') AND reviewer_id IS NOT NULL))`
- `CONSTRAINT document_verification_case_verified_ck CHECK ((state IN ('aprobada','vencida','revocada') AND verified_at IS NOT NULL AND verified_until > verified_at) OR (state NOT IN ('aprobada','vencida','revocada') AND verified_at IS NULL AND verified_until IS NULL))`
- `CONSTRAINT document_verification_case_revoked_ck CHECK ((state='revocada' AND revoked_at IS NOT NULL AND revoked_at >= verified_at) OR (state<>'revocada' AND revoked_at IS NULL))`
- `CONSTRAINT document_verification_case_id_scope_uq UNIQUE(id,purpose,subject_id,space_id)`
- `CONSTRAINT document_verification_case_superseded_scope_ck CHECK (superseded_at IS NULL OR purpose='space')`


### B.013 Tabla `public.document_verification_event`
- **Migración de creación:** `V000079`
- **Atributos:** 14

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `bigint` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `case_id` | `uuid` | NOT NULL | Atributo `case_id`; el nombre y tipo se conservan según el DDL. |
| `purpose` | `text` | NOT NULL | Atributo `purpose`; el nombre y tipo se conservan según el DDL. |
| `subject_id` | `uuid` | NOT NULL | Atributo `subject_id`; el nombre y tipo se conservan según el DDL. |
| `file_id` | `uuid` | NULL permitido | Atributo `file_id`; el nombre y tipo se conservan según el DDL. |
| `actor_kind` | `text` | DEFAULT `'user'`; NOT NULL | Atributo `actor_kind`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | NULL permitido | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `action` | `text` | NOT NULL | Atributo `action`; el nombre y tipo se conservan según el DDL. |
| `from_state` | `text` | NULL permitido | Atributo `from_state`; el nombre y tipo se conservan según el DDL. |
| `to_state` | `text` | NOT NULL | Atributo `to_state`; el nombre y tipo se conservan según el DDL. |
| `result_code` | `text` | NOT NULL | Atributo `result_code`; el nombre y tipo se conservan según el DDL. |
| `reason_code` | `text` | NULL permitido | Atributo `reason_code`; el nombre y tipo se conservan según el DDL. |
| `revision` | `bigint` | NOT NULL | Atributo `revision`; el nombre y tipo se conservan según el DDL. |
| `occurred_at` | `timestamptz` | DEFAULT `now()`; NOT NULL | Atributo `occurred_at`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK(purpose IN ('identity','space'))`
- `CHECK(actor_kind IN ('user','scanner','system'))`
- `CHECK(from_state IS NULL OR from_state IN ('borrador','enviada','en_revision','requiere_antecedentes','aprobada','rechazada','vencida','revocada'))`
- `CHECK(to_state IN ('borrador','enviada','en_revision','requiere_antecedentes','aprobada','rechazada','vencida','revocada'))`
- `CHECK(result_code IN ('borrador','enviada','en_revision','requiere_antecedentes','aprobada','rechazada','vencida','revocada','pendiente','limpio','bloqueado','error','eliminado'))`
- `CHECK(reason_code IS NULL OR reason_code IN ('documento_ilegible','documento_invalido','documento_vencido','antecedentes_incompletos','cambio_titularidad','conflicto_interes','malware_detectado','scanner_no_disponible','firmas_desactualizadas','solicitud_titular','retencion_vencida'))`
- `CHECK(revision > 0)`
- `CONSTRAINT document_verification_event_actor_ck CHECK((actor_kind='user' AND actor_id IS NOT NULL) OR (actor_kind IN ('scanner','system') AND actor_id IS NULL))`
- `CONSTRAINT document_verification_event_file_action_ck CHECK((action IN ('file_added','scan_result','retention_deleted') AND file_id IS NOT NULL) OR (action NOT IN ('file_added','scan_result','retention_deleted') AND file_id IS NULL))`
- `CONSTRAINT document_verification_event_action_check CHECK (action IN ('case_created','case_transitioned','case_superseded','file_added','scan_result','review_decision','revoked','expired','retention_deleted'))`


### B.014 Tabla `public.document_verification_file`
- **Migración de creación:** `V000079`
- **Atributos:** 16

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; UQ compuesta (id, case_id); NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `case_id` | `uuid` | UQ compuesta (id, case_id); FK → `public.document_verification_case(case_id→id)`; NOT NULL | Atributo `case_id`; el nombre y tipo se conservan según el DDL. |
| `state` | `text` | DEFAULT `'pendiente'`; NOT NULL | Atributo `state`; el nombre y tipo se conservan según el DDL. |
| `size_bytes` | `bigint` | NOT NULL | Atributo `size_bytes`; el nombre y tipo se conservan según el DDL. |
| `mime_type` | `text` | NOT NULL | Atributo `mime_type`; el nombre y tipo se conservan según el DDL. |
| `pages` | `integer` | NOT NULL | Atributo `pages`; el nombre y tipo se conservan según el DDL. |
| `content_sha256` | `bytea` | NOT NULL | Atributo `content_sha256`; el nombre y tipo se conservan según el DDL. |
| `scan_attempts` | `smallint` | DEFAULT `0`; NOT NULL | Atributo `scan_attempts`; el nombre y tipo se conservan según el DDL. |
| `scanner_version` | `text` | NULL permitido | Atributo `scanner_version`; el nombre y tipo se conservan según el DDL. |
| `signatures_at` | `timestamptz` | NULL permitido | Atributo `signatures_at`; el nombre y tipo se conservan según el DDL. |
| `inspected_at` | `timestamptz` | NULL permitido | Atributo `inspected_at`; el nombre y tipo se conservan según el DDL. |
| `last_error_code` | `text` | NULL permitido | Atributo `last_error_code`; el nombre y tipo se conservan según el DDL. |
| `retention_at` | `timestamptz` | NULL permitido | Atributo `retention_at`; el nombre y tipo se conservan según el DDL. |
| `retention_reason_code` | `text` | NULL permitido | Atributo `retention_reason_code`; el nombre y tipo se conservan según el DDL. |
| `created_at` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de creación del registro. |
| `updated_at` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de actualización del registro. |

**Restricciones DDL vigentes:**

- `CHECK(state IN ('pendiente','limpio','bloqueado','error'))`
- `CHECK(size_bytes BETWEEN 1 AND 10485760)`
- `CHECK(mime_type IN ('image/jpeg','image/png','application/pdf'))`
- `CHECK(pages BETWEEN 0 AND 20)`
- `CHECK(octet_length(content_sha256)=32)`
- `CHECK(scan_attempts BETWEEN 0 AND 5)`
- `CHECK(last_error_code IS NULL OR last_error_code IN ('scanner_unavailable','scanner_malformed','signatures_stale','malware_detected','inspection_rejected','retention_store_error'))`
- `CHECK(retention_reason_code IS NULL OR retention_reason_code IN ('abandoned_draft','malicious_file','inspection_error','identity_decision','space_expiry','rejected_or_replaced','revoked'))`
- `CONSTRAINT document_verification_file_clean_ck CHECK(state<>'limpio' OR (inspected_at IS NOT NULL AND scanner_version IS NOT NULL AND signatures_at IS NOT NULL))`
- `UNIQUE(id,case_id)`


### B.015 Tabla `public.document_verification_job`
- **Migración de creación:** `V000079`
- **Atributos:** 10

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; DEFAULT `gen_random_uuid()`; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `file_id` | `uuid` | FK → `public.document_verification_file(file_id→id)`; NOT NULL | Atributo `file_id`; el nombre y tipo se conservan según el DDL. |
| `kind` | `text` | NOT NULL | Atributo `kind`; el nombre y tipo se conservan según el DDL. |
| `state` | `text` | DEFAULT `'pendiente'`; NOT NULL | Atributo `state`; el nombre y tipo se conservan según el DDL. |
| `attempts` | `smallint` | DEFAULT `0`; NOT NULL | Atributo `attempts`; el nombre y tipo se conservan según el DDL. |
| `available_at` | `timestamptz` | DEFAULT `now()`; NOT NULL | Atributo `available_at`; el nombre y tipo se conservan según el DDL. |
| `lease_until` | `timestamptz` | NULL permitido | Atributo `lease_until`; el nombre y tipo se conservan según el DDL. |
| `last_error_code` | `text` | NULL permitido | Atributo `last_error_code`; el nombre y tipo se conservan según el DDL. |
| `created_at` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de creación del registro. |
| `updated_at` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de actualización del registro. |

**Restricciones DDL vigentes:**

- `CHECK(kind IN ('scan','retention_delete'))`
- `CHECK(state IN ('pendiente','procesando','reintentar','completado'))`
- `CHECK(attempts BETWEEN 0 AND 5)`
- `CHECK(last_error_code IS NULL OR last_error_code IN ('scanner_unavailable','scanner_malformed','signatures_stale','malware_detected','inspection_rejected','retention_store_error'))`
- `CONSTRAINT document_verification_job_lease_ck CHECK((state='procesando')=(lease_until IS NOT NULL))`


### B.016 Tabla `public.document_verification_reviewer_grant`
- **Migración de creación:** `V000079`
- **Atributos:** 12

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; DEFAULT `gen_random_uuid()`; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `reviewer_id` | `uuid` | FK → `public.usuario(reviewer_id→id)`; NOT NULL | Atributo `reviewer_id`; el nombre y tipo se conservan según el DDL. |
| `capability` | `text` | NOT NULL | Atributo `capability`; el nombre y tipo se conservan según el DDL. |
| `scope_kind` | `text` | NOT NULL | Atributo `scope_kind`; el nombre y tipo se conservan según el DDL. |
| `scope_id` | `uuid` | NOT NULL | Atributo `scope_id`; el nombre y tipo se conservan según el DDL. |
| `granted_by` | `uuid` | FK → `public.usuario(granted_by→id)`; NOT NULL | Atributo `granted_by`; el nombre y tipo se conservan según el DDL. |
| `granted_at` | `timestamptz` | DEFAULT `now()`; NOT NULL | Atributo `granted_at`; el nombre y tipo se conservan según el DDL. |
| `granted_reason_code` | `text` | NOT NULL | Atributo `granted_reason_code`; el nombre y tipo se conservan según el DDL. |
| `expires_at` | `timestamptz` | NULL permitido | Atributo `expires_at`; el nombre y tipo se conservan según el DDL. |
| `revoked_at` | `timestamptz` | NULL permitido | Atributo `revoked_at`; el nombre y tipo se conservan según el DDL. |
| `revoked_by` | `uuid` | FK → `public.usuario(revoked_by→id)`; NULL permitido | Atributo `revoked_by`; el nombre y tipo se conservan según el DDL. |
| `revocation_reason_code` | `text` | NULL permitido | Atributo `revocation_reason_code`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK(capability IN ('review_identity','review_space'))`
- `CHECK(scope_kind IN ('identity_subject','space'))`
- `CHECK(granted_reason_code IN ('role_assignment','temporary_coverage','reviewer_rotation'))`
- `CHECK(revocation_reason_code IS NULL OR revocation_reason_code IN ('role_assignment_ended','temporary_coverage_ended','reviewer_rotation','access_review'))`
- `CONSTRAINT document_verification_reviewer_grant_scope_ck CHECK((capability='review_identity' AND scope_kind='identity_subject') OR (capability='review_space' AND scope_kind='space'))`
- `CONSTRAINT document_verification_reviewer_grant_expiry_ck CHECK(expires_at IS NULL OR expires_at>granted_at)`
- `CONSTRAINT document_verification_reviewer_grant_revocation_ck CHECK((revoked_at IS NULL AND revoked_by IS NULL AND revocation_reason_code IS NULL) OR (revoked_at IS NOT NULL AND revoked_by IS NOT NULL AND revocation_reason_code IS NOT NULL AND revoked_at>=granted_at))`


### B.017 Tabla `public.document_verification_reviewer_grant_event`
- **Migración de creación:** `V000079`
- **Atributos:** 10

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `bigint` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `grant_id` | `uuid` | NOT NULL | Atributo `grant_id`; el nombre y tipo se conservan según el DDL. |
| `reviewer_id` | `uuid` | NOT NULL | Atributo `reviewer_id`; el nombre y tipo se conservan según el DDL. |
| `capability` | `text` | NOT NULL | Atributo `capability`; el nombre y tipo se conservan según el DDL. |
| `scope_kind` | `text` | NOT NULL | Atributo `scope_kind`; el nombre y tipo se conservan según el DDL. |
| `scope_id` | `uuid` | NOT NULL | Atributo `scope_id`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | NOT NULL | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `action` | `text` | NOT NULL | Atributo `action`; el nombre y tipo se conservan según el DDL. |
| `reason_code` | `text` | NOT NULL | Atributo `reason_code`; el nombre y tipo se conservan según el DDL. |
| `occurred_at` | `timestamptz` | DEFAULT `now()`; NOT NULL | Atributo `occurred_at`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK(capability IN ('review_identity','review_space'))`
- `CHECK(scope_kind IN ('identity_subject','space'))`
- `CHECK(action IN ('granted','revoked'))`
- `CHECK(reason_code IN ('role_assignment','temporary_coverage','reviewer_rotation','role_assignment_ended','temporary_coverage_ended','access_review'))`


### B.018 Tabla `public.documento_privado_sintetico_local`
- **Migración de creación:** `V000034`
- **Atributos:** 8

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `reserva_id` | `uuid` | FK → `public.reserva_ensayo_local(reserva_id→id)`; NOT NULL | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `mime_type` | `text` | NOT NULL | Atributo `mime_type`; el nombre y tipo se conservan según el DDL. |
| `encryption_algorithm` | `text` | NOT NULL | Atributo `encryption_algorithm`; el nombre y tipo se conservan según el DDL. |
| `sha256` | `bytea` | NOT NULL | Atributo `sha256`; el nombre y tipo se conservan según el DDL. |
| `size_bytes` | `integer` | NOT NULL | Atributo `size_bytes`; el nombre y tipo se conservan según el DDL. |
| `contenido` | `bytea` | NOT NULL | Atributo `contenido`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |

**Restricciones DDL vigentes:**

- `CHECK (mime_type='application/pdf')`
- `CHECK (encryption_algorithm='aes-256-gcm')`
- `CHECK (octet_length(sha256)=32)`
- `CHECK (size_bytes BETWEEN 1 AND 2097152)`


### B.019 Tabla `public.ejecucion_baja_local`
- **Migración de creación:** `V000025`
- **Atributos:** 11

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `solicitud_id` | `uuid` | UQ compuesta (solicitud_id, clave_idempotencia); FK → `public.solicitud_titular(solicitud_id→id)`; NOT NULL | Atributo `solicitud_id`; el nombre y tipo se conservan según el DDL. |
| `usuario_id` | `uuid` | FK → `public.usuario(usuario_id→id)`; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NOT NULL | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (solicitud_id, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `motivo_codigo` | `text` | NOT NULL | Atributo `motivo_codigo`; el nombre y tipo se conservan según el DDL. |
| `iniciada_en` | `timestamptz` | NOT NULL | Atributo `iniciada_en`; el nombre y tipo se conservan según el DDL. |
| `completada_en` | `timestamptz` | NULL permitido | Atributo `completada_en`; el nombre y tipo se conservan según el DDL. |
| `retirar_en` | `timestamptz` | NULL permitido | Atributo `retirar_en`; el nombre y tipo se conservan según el DDL. |
| `detalle` | `jsonb` | NOT NULL | Atributo `detalle`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (length(btrim(clave_idempotencia)) BETWEEN 1 AND 200)`
- `CHECK (estado IN ('bloqueada','limpieza_pendiente','completada'))`
- `CHECK (motivo_codigo IN ('supresion_con_obligaciones','baja_local_minimizada'))`
- `CHECK (jsonb_typeof(detalle)='object')`
- `UNIQUE (solicitud_id, clave_idempotencia)`
- `CHECK ((estado='completada') = (completada_en IS NOT NULL))`
- `CHECK ((estado='completada') = (retirar_en IS NOT NULL))`
- `CHECK (retirar_en IS NULL OR retirar_en = completada_en + interval '5 years')`


### B.020 Tabla `public.evento_auditoria_local`
- **Migración de creación:** `V000022`
- **Atributos:** 14

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NOT NULL | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `recurso_tipo` | `text` | NOT NULL | Atributo `recurso_tipo`; el nombre y tipo se conservan según el DDL. |
| `recurso_id` | `uuid` | NOT NULL | Atributo `recurso_id`; el nombre y tipo se conservan según el DDL. |
| `accion` | `text` | NOT NULL | Atributo `accion`; el nombre y tipo se conservan según el DDL. |
| `resultado` | `text` | NOT NULL | Atributo `resultado`; el nombre y tipo se conservan según el DDL. |
| `motivo_codigo` | `text` | NOT NULL | Atributo `motivo_codigo`; el nombre y tipo se conservan según el DDL. |
| `correlacion_id` | `text` | NOT NULL | Atributo `correlacion_id`; el nombre y tipo se conservan según el DDL. |
| `ocurrido_en` | `timestamptz` | NOT NULL | Atributo `ocurrido_en`; el nombre y tipo se conservan según el DDL. |
| `retirar_en` | `timestamptz` | NOT NULL | Atributo `retirar_en`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | NULL permitido | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `detalle_codigos` | `jsonb` | DEFAULT `'{"obligations_detected":[],"pending_checks":[]}'`; NOT NULL | Atributo `detalle_codigos`; el nombre y tipo se conservan según el DDL. |
| `cuenta_objetivo_id` | `uuid` | FK → `public.usuario(cuenta_objetivo_id→id)`; NULL permitido | Atributo `cuenta_objetivo_id`; el nombre y tipo se conservan según el DDL. |
| `registrado_en` | `timestamptz` | DEFAULT `clock_timestamp()`; NOT NULL | Atributo `registrado_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (length(btrim(recurso_tipo)) BETWEEN 1 AND 40)`
- `CHECK (length(btrim(accion)) BETWEEN 1 AND 60)`
- `CHECK (resultado IN ('exito', 'rechazo'))`
- `CHECK (length(btrim(motivo_codigo)) BETWEEN 1 AND 60)`
- `CHECK (length(btrim(correlacion_id)) BETWEEN 1 AND 120)`
- `CONSTRAINT evento_auditoria_retencion_ck CHECK (retirar_en > ocurrido_en)`
- `CONSTRAINT evento_auditoria_five_years_ck CHECK (retirar_en = ocurrido_en + interval '5 years')`
- `CONSTRAINT evento_auditoria_reapertura_motivo_ck CHECK ( accion <> 'identity.credential_notice.reopen' OR (motivo_codigo IN ('smtp_restaurado','reintento_operativo') AND resultado='exito') )`
- `CONSTRAINT evento_auditoria_idempotencia_ck CHECK ( clave_idempotencia IS NULL OR ( length(btrim(clave_idempotencia)) BETWEEN 1 AND 200 AND ((accion IN ('privacy.suppression.review','privacy.suppression.execute') AND recurso_tipo='solicitud_titular') OR (accion='identity.credential_notice.reopen' AND recurso_tipo='outbox_evento') OR (accion='reputation.review.moderate' AND recurso_tipo='reporte_resena') OR (accion='local.damage_claim.resolve' AND recurso_tipo='reclamo_dano') OR (accion IN ('local.finance.decision','local.finance.guarantee.operation','local.finance.guarantee.reconcile','local.finance.settlement') AND recurso_tipo='reserva')) ) )`
- `CONSTRAINT evento_auditoria_codigos_ck CHECK ( jsonb_typeof(detalle_codigos)='object' AND detalle_codigos ? 'obligations_detected' AND detalle_codigos ? 'pending_checks' AND (detalle_codigos - ARRAY['obligations_detected','pending_checks']::text[])='{}'::jsonb AND jsonb_typeof(detalle_codigos->'obligations_detected')='array' AND jsonb_typeof(detalle_codigos->'pending_checks')='array' AND (detalle_codigos->'obligations_detected') <@ '["reserva_activa","pago_o_devolucion_pendiente","disputa_abierta","liquidacion_pendiente"]'::jsonb AND (detalle_codigos->'pending_checks') <@ '["fuente_disputas_no_modelada","matriz_retencion_historicos_incompleta"]'::jsonb )`


### B.021 Tabla `public.gallery_item_order`
- **Migración de creación:** `V000068`
- **Atributos:** 6

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `espacio_id` | `uuid` | UQ compuesta (espacio_id, position); FK → `public.espacio(espacio_id→id, propietario_id→propietario_id)` [gallery_order_space_owner_fk]; FK → `public.espacio_galeria_sintetica_local(espacio_id→espacio_id, propietario_id→propietario_id, synthetic_photo_id→id)` [gallery_order_synthetic_fk]; FK → `public.space_media(espacio_id→espacio_id, propietario_id→propietario_id, space_media_id→id)` [gallery_order_real_fk]; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `propietario_id` | `uuid` | FK → `public.espacio(espacio_id→id, propietario_id→propietario_id)` [gallery_order_space_owner_fk]; FK → `public.espacio_galeria_sintetica_local(espacio_id→espacio_id, propietario_id→propietario_id, synthetic_photo_id→id)` [gallery_order_synthetic_fk]; FK → `public.space_media(espacio_id→espacio_id, propietario_id→propietario_id, space_media_id→id)` [gallery_order_real_fk]; NOT NULL | Atributo `propietario_id`; el nombre y tipo se conservan según el DDL. |
| `synthetic_photo_id` | `uuid` | UQ; FK → `public.espacio_galeria_sintetica_local(espacio_id→espacio_id, propietario_id→propietario_id, synthetic_photo_id→id)` [gallery_order_synthetic_fk]; NULL permitido | Atributo `synthetic_photo_id`; el nombre y tipo se conservan según el DDL. |
| `space_media_id` | `uuid` | UQ; FK → `public.space_media(espacio_id→espacio_id, propietario_id→propietario_id, space_media_id→id)` [gallery_order_real_fk]; NULL permitido | Atributo `space_media_id`; el nombre y tipo se conservan según el DDL. |
| `position` | `smallint` | UQ compuesta (espacio_id, position); NOT NULL | Atributo `position`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CONSTRAINT gallery_order_exactly_one_ck CHECK ((synthetic_photo_id IS NULL) <> (space_media_id IS NULL))`
- `CONSTRAINT gallery_order_space_owner_fk FOREIGN KEY (espacio_id,propietario_id) REFERENCES public.espacio(id,propietario_id) ON DELETE RESTRICT`
- `CONSTRAINT gallery_order_synthetic_fk FOREIGN KEY (espacio_id,propietario_id,synthetic_photo_id) REFERENCES public.espacio_galeria_sintetica_local(espacio_id,propietario_id,id) ON DELETE RESTRICT`
- `CONSTRAINT gallery_order_real_fk FOREIGN KEY (espacio_id,propietario_id,space_media_id) REFERENCES public.space_media(espacio_id,propietario_id,id) ON DELETE RESTRICT`
- `CONSTRAINT gallery_order_synthetic_uq UNIQUE (synthetic_photo_id)`
- `CONSTRAINT gallery_order_real_uq UNIQUE (space_media_id)`
- `CONSTRAINT gallery_order_position_deferred_uq UNIQUE (espacio_id,position) DEFERRABLE INITIALLY DEFERRED`
- `CONSTRAINT gallery_item_order_position_check CHECK (position BETWEEN 1 AND 30)`


### B.022 Tabla `public.gcp06_test_access_batch_audit`
- **Migración de creación:** `V000066`
- **Atributos:** 4

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `target_count` | `integer` | NOT NULL | Atributo `target_count`; el nombre y tipo se conservan según el DDL. |
| `target_set_sha256` | `char(64)` | NOT NULL | Atributo `target_set_sha256`; el nombre y tipo se conservan según el DDL. |
| `occurred_at` | `timestamptz` | NOT NULL | Atributo `occurred_at`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (target_count BETWEEN 1 AND 10000)`
- `CHECK (target_set_sha256 ~ '^[0-9a-f]{64}$')`


### B.023 Tabla `public.historial_clave_local`
- **Migración de creación:** `V000022`
- **Atributos:** 6

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `usuario_id` | `uuid` | FK → `public.usuario(usuario_id→id)`; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `hash_clave` | `text` | NOT NULL | Atributo `hash_clave`; el nombre y tipo se conservan según el DDL. |
| `dejo_de_ser_vigente_en` | `timestamptz` | NOT NULL | Atributo `dejo_de_ser_vigente_en`; el nombre y tipo se conservan según el DDL. |
| `retirar_en` | `timestamptz` | NOT NULL | Atributo `retirar_en`; el nombre y tipo se conservan según el DDL. |
| `creado_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |

**Restricciones DDL vigentes:**

- `CHECK (length(hash_clave) BETWEEN 1 AND 200)`
- `CONSTRAINT historial_clave_ventana_ck CHECK (retirar_en > dejo_de_ser_vigente_en)`


### B.024 Tabla `public.m02_operacion_idempotente_local`
- **Migración de creación:** `V000030`
- **Atributos:** 6

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `usuario_id` | `uuid` | PK compuesta (usuario_id, recurso, clave_idempotencia); FK → `public.usuario(usuario_id→id)`; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `recurso` | `text` | PK compuesta (usuario_id, recurso, clave_idempotencia); NOT NULL | Atributo `recurso`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | PK compuesta (usuario_id, recurso, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `solicitud_sha256` | `text` | NOT NULL | Atributo `solicitud_sha256`; el nombre y tipo se conservan según el DDL. |
| `respuesta` | `jsonb` | NOT NULL | Atributo `respuesta`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |

**Restricciones DDL vigentes:**

- `CHECK (recurso IN ('foto_perfil','cuenta_cobro'))`
- `CHECK (length(clave_idempotencia) BETWEEN 8 AND 128)`
- `CHECK (solicitud_sha256 ~ '^[0-9a-f]{64}$')`
- `PRIMARY KEY (usuario_id,recurso,clave_idempotencia)`


### B.025 Tabla `public.media_asset`
- **Migración de creación:** `V000068`
- **Atributos:** 14

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; UQ compuesta (id, propietario_id); UQ compuesta (id, espacio_id, propietario_id); NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `propietario_id` | `uuid` | UQ compuesta (id, propietario_id); UQ compuesta (id, espacio_id, propietario_id); FK → `public.usuario(propietario_id→id)`; FK → `public.espacio(espacio_id→id, propietario_id→propietario_id)` [media_asset_space_owner_fk]; FK → `public.space_media(espacio_id→espacio_id, propietario_id→propietario_id, replacement_target_space_media_id→id)` [media_asset_replacement_target_fk]; NOT NULL | Atributo `propietario_id`; el nombre y tipo se conservan según el DDL. |
| `espacio_id` | `uuid` | UQ compuesta (id, espacio_id, propietario_id); FK → `public.espacio(espacio_id→id, propietario_id→propietario_id)` [media_asset_space_owner_fk]; FK → `public.space_media(espacio_id→espacio_id, propietario_id→propietario_id, replacement_target_space_media_id→id)` [media_asset_replacement_target_fk]; NULL permitido | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `proposito` | `text` | NOT NULL | Atributo `proposito`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `idempotency_key` | `text` | NOT NULL | Atributo `idempotency_key`; el nombre y tipo se conservan según el DDL. |
| `input_sha256` | `char(64)` | NOT NULL | Atributo `input_sha256`; el nombre y tipo se conservan según el DDL. |
| `fencing_token` | `bigint` | DEFAULT `1`; NOT NULL | Atributo `fencing_token`; el nombre y tipo se conservan según el DDL. |
| `lease_until` | `timestamptz` | NULL permitido | Atributo `lease_until`; el nombre y tipo se conservan según el DDL. |
| `created_at` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de creación del registro. |
| `updated_at` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de actualización del registro. |
| `deleted_at` | `timestamptz` | NULL permitido | Atributo `deleted_at`; el nombre y tipo se conservan según el DDL. |
| `replacement_target_space_media_id` | `uuid` | FK → `public.space_media(espacio_id→espacio_id, propietario_id→propietario_id, replacement_target_space_media_id→id)` [media_asset_replacement_target_fk]; NULL permitido | Atributo `replacement_target_space_media_id`; el nombre y tipo se conservan según el DDL. |
| `replacement_expected_revision` | `timestamptz` | NULL permitido | Atributo `replacement_expected_revision`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (proposito IN ('espacio','perfil'))`
- `CHECK (estado IN ('pending','ready','deleting','deleted','failed'))`
- `CHECK (length(btrim(idempotency_key)) BETWEEN 8 AND 128)`
- `CHECK (input_sha256 ~ '^[0-9a-f]{64}$')`
- `CHECK (fencing_token > 0)`
- `CONSTRAINT media_asset_space_owner_fk FOREIGN KEY (espacio_id, propietario_id) REFERENCES public.espacio(id, propietario_id) ON DELETE RESTRICT`
- `CONSTRAINT media_asset_purpose_scope_ck CHECK ( (proposito='espacio' AND espacio_id IS NOT NULL) OR (proposito='perfil' AND espacio_id IS NULL) )`
- `CONSTRAINT media_asset_terminal_ck CHECK ( (estado='deleted' AND deleted_at IS NOT NULL) OR (estado<>'deleted' AND deleted_at IS NULL) )`
- `CONSTRAINT media_asset_owner_id_uq UNIQUE (id,propietario_id)`
- `CONSTRAINT media_asset_space_owner_id_uq UNIQUE (id,espacio_id,propietario_id)`
- `CONSTRAINT media_asset_replacement_target_fk FOREIGN KEY (espacio_id,propietario_id,replacement_target_space_media_id) REFERENCES public.space_media(espacio_id,propietario_id,id) ON DELETE RESTRICT`


### B.026 Tabla `public.media_variant`
- **Migración de creación:** `V000068`
- **Atributos:** 12

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `media_id` | `uuid` | PK compuesta (media_id, variant); UQ compuesta (media_id, variant, object_key); FK → `public.media_asset(media_id→id)`; NOT NULL | Atributo `media_id`; el nombre y tipo se conservan según el DDL. |
| `variant` | `text` | PK compuesta (media_id, variant); UQ compuesta (media_id, variant, object_key); NOT NULL | Atributo `variant`; el nombre y tipo se conservan según el DDL. |
| `provider` | `text` | NOT NULL | Atributo `provider`; el nombre y tipo se conservan según el DDL. |
| `bucket_name` | `text` | NOT NULL | Atributo `bucket_name`; el nombre y tipo se conservan según el DDL. |
| `object_key` | `text` | UQ compuesta (media_id, variant, object_key); NOT NULL | Atributo `object_key`; el nombre y tipo se conservan según el DDL. |
| `generation` | `bigint` | NOT NULL | Atributo `generation`; el nombre y tipo se conservan según el DDL. |
| `mime_type` | `text` | NOT NULL | Atributo `mime_type`; el nombre y tipo se conservan según el DDL. |
| `size_bytes` | `bigint` | NOT NULL | Atributo `size_bytes`; el nombre y tipo se conservan según el DDL. |
| `sha256` | `char(64)` | NOT NULL | Atributo `sha256`; el nombre y tipo se conservan según el DDL. |
| `width` | `integer` | NOT NULL | Atributo `width`; el nombre y tipo se conservan según el DDL. |
| `height` | `integer` | NOT NULL | Atributo `height`; el nombre y tipo se conservan según el DDL. |
| `created_at` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de creación del registro. |

**Restricciones DDL vigentes:**

- `CHECK (variant IN ('display','thumbnail','avatar'))`
- `CHECK (length(btrim(bucket_name)) BETWEEN 1 AND 222)`
- `CHECK (length(btrim(object_key)) BETWEEN 1 AND 1024)`
- `CHECK (generation > 0)`
- `CHECK (mime_type='image/webp')`
- `CHECK (size_bytes BETWEEN 1 AND 10485760)`
- `CHECK (sha256 ~ '^[0-9a-f]{64}$')`
- `CHECK (width BETWEEN 1 AND 1600)`
- `CHECK (height BETWEEN 1 AND 1600)`
- `PRIMARY KEY (media_id,variant)`
- `CONSTRAINT media_variant_asset_uq UNIQUE (media_id,variant,object_key)`
- `CONSTRAINT media_variant_dims_ck CHECK (width::bigint * height::bigint <= 25000000)`
- `CONSTRAINT media_variant_purpose_ck CHECK ( (variant='avatar' AND width<=512 AND height<=512) OR (variant='thumbnail' AND width<=480 AND height<=480) OR (variant='display' AND width<=1600 AND height<=1600) )`
- `CONSTRAINT media_variant_provider_check CHECK (provider IN ('gcs','filesystem'))`


### B.027 Tabla `public.media_variant_intent`
- **Migración de creación:** `V000070`
- **Atributos:** 9

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `media_id` | `uuid` | PK compuesta (media_id, variant); FK → `public.media_asset(media_id→id)`; NOT NULL | Atributo `media_id`; el nombre y tipo se conservan según el DDL. |
| `variant` | `text` | PK compuesta (media_id, variant); NOT NULL | Atributo `variant`; el nombre y tipo se conservan según el DDL. |
| `object_key` | `text` | UQ compuesta (provider, bucket_name, object_key); NOT NULL | Atributo `object_key`; el nombre y tipo se conservan según el DDL. |
| `provider` | `text` | UQ compuesta (provider, bucket_name, object_key); NULL permitido | Atributo `provider`; el nombre y tipo se conservan según el DDL. |
| `bucket_name` | `text` | UQ compuesta (provider, bucket_name, object_key); NULL permitido | Atributo `bucket_name`; el nombre y tipo se conservan según el DDL. |
| `generation` | `bigint` | NULL permitido | Atributo `generation`; el nombre y tipo se conservan según el DDL. |
| `created_at` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de creación del registro. |
| `updated_at` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de actualización del registro. |
| `write_complete` | `boolean` | DEFAULT `false`; NOT NULL | Atributo `write_complete`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (variant IN ('display','thumbnail','avatar'))`
- `CHECK (provider IN ('gcs','filesystem'))`
- `CHECK (generation IS NULL OR generation > 0)`
- `PRIMARY KEY (media_id,variant)`
- `UNIQUE (provider,bucket_name,object_key)`
- `CONSTRAINT media_variant_intent_storage_ck CHECK ( (provider IS NULL AND bucket_name IS NULL AND generation IS NULL) OR (provider IS NOT NULL AND bucket_name IS NOT NULL AND generation IS NOT NULL) )`
- `CONSTRAINT media_variant_intent_object_key_check CHECK ( length(object_key) BETWEEN 1 AND 1024 AND ( object_key LIKE 'media/v1/%' OR object_key ~ '^users/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/spaces/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/images/v2/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/[0-9]{8}T[0-9]{6}[.][0-9]{9}Z_[1-9][0-9]*_(display|thumbnail)[.]webp$' ) )`


### B.028 Tabla `public.operacion_arriendo_archivo_candidato_local`
- **Migración de creación:** `V000035`
- **Atributos:** 10

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `archivo_id` | `uuid` | PK; NOT NULL | Atributo `archivo_id`; el nombre y tipo se conservan según el DDL. |
| `reserva_id` | `uuid` | FK → `public.reserva_ensayo_local(reserva_id→id)`; NULL permitido | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NULL permitido | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `tipo` | `text` | NOT NULL | Atributo `tipo`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `proximo_intento_en` | `timestamptz` | NOT NULL | Atributo `proximo_intento_en`; el nombre y tipo se conservan según el DDL. |
| `lease_iniciado_en` | `timestamptz` | NULL permitido | Atributo `lease_iniciado_en`; el nombre y tipo se conservan según el DDL. |
| `intentos_limpieza` | `integer` | DEFAULT `0`; NOT NULL | Atributo `intentos_limpieza`; el nombre y tipo se conservan según el DDL. |
| `ultimo_codigo_error` | `text` | NULL permitido | Atributo `ultimo_codigo_error`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (estado IN ('reservado','pendiente_limpieza','limpiando'))`
- `CHECK (intentos_limpieza>=0)`
- `CONSTRAINT operacion_arriendo_archivo_candidato_local_tipo_check CHECK (tipo IN ('checkin','checkout','recepcion','descargo'))`


### B.029 Tabla `public.operacion_arriendo_ensayo_local`
- **Migración de creación:** `V000035`
- **Atributos:** 13

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `reserva_id` | `uuid` | UQ compuesta (reserva_id, tipo); UQ compuesta (reserva_id, tipo, clave_idempotencia); FK → `public.reserva_ensayo_local(reserva_id→id)`; NULL permitido | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `tipo` | `text` | UQ compuesta (reserva_id, tipo); UQ compuesta (reserva_id, tipo, clave_idempotencia); NOT NULL | Atributo `tipo`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NULL permitido | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `ocurrio_en` | `timestamptz` | NOT NULL | Atributo `ocurrio_en`; el nombre y tipo se conservan según el DDL. |
| `zona_horaria` | `text` | NOT NULL | Atributo `zona_horaria`; el nombre y tipo se conservan según el DDL. |
| `ubicacion_sintetica` | `jsonb` | NOT NULL | Atributo `ubicacion_sintetica`; el nombre y tipo se conservan según el DDL. |
| `comentarios` | `text` | DEFAULT `''`; NOT NULL | Atributo `comentarios`; el nombre y tipo se conservan según el DDL. |
| `observacion` | `text` | DEFAULT `''`; NOT NULL | Atributo `observacion`; el nombre y tipo se conservan según el DDL. |
| `resultado` | `text` | NOT NULL | Atributo `resultado`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (reserva_id, tipo, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `huella_solicitud` | `bytea` | NOT NULL | Atributo `huella_solicitud`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |

**Restricciones DDL vigentes:**

- `CHECK (length(btrim(zona_horaria)) BETWEEN 1 AND 100)`
- `CHECK (
        jsonb_typeof(ubicacion_sintetica)='object'
        AND ubicacion_sintetica->>'source'='synthetic-fixture-v1'
        AND ubicacion_sintetica->>'location_code'='santiago-demo-center-v1'
        AND (ubicacion_sintetica->>'latitude')::double precision BETWEEN -90 AND 90
        AND (ubicacion_sintetica->>'longitude')::double precision BETWEEN -180 AND 180
    )`
- `CHECK (resultado IN ('registrada','recepcion_conforme','recepcion_con_observaciones'))`
- `CHECK (length(btrim(clave_idempotencia)) BETWEEN 8 AND 200)`
- `CHECK (octet_length(huella_solicitud)=32)`
- `UNIQUE (reserva_id,tipo)`
- `UNIQUE (reserva_id,tipo,clave_idempotencia)`
- `CHECK ((tipo='recepcion' AND resultado IN ('recepcion_conforme','recepcion_con_observaciones')) OR (tipo IN ('checkin','checkout') AND resultado='registrada'))`
- `CHECK ((tipo IN ('checkin','checkout') OR comentarios='') AND (tipo='recepcion' OR observacion=''))`
- `CONSTRAINT operacion_arriendo_ensayo_local_tipo_check CHECK (tipo IN ('checkin','checkout','recepcion','descargo'))`
- `CONSTRAINT operacion_arriendo_ensayo_local_resultado_tipo_check CHECK ( (tipo='recepcion' AND resultado IN ('recepcion_conforme','recepcion_con_observaciones')) OR (tipo IN ('checkin','checkout','descargo') AND resultado='registrada') )`
- `CONSTRAINT operacion_arriendo_ensayo_local_campos_tipo_check CHECK ( (tipo IN ('checkin','checkout') OR comentarios='') AND (tipo='recepcion' OR observacion='') )`


### B.030 Tabla `public.operacion_arriendo_historial_ensayo_local`
- **Migración de creación:** `V000035`
- **Atributos:** 6

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `secuencia` | `bigint` | PK; NOT NULL | Atributo `secuencia`; el nombre y tipo se conservan según el DDL. |
| `reserva_id` | `uuid` | FK → `public.reserva_ensayo_local(reserva_id→id)`; NULL permitido | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `operacion_id` | `uuid` | UQ; FK → `public.operacion_arriendo_ensayo_local(operacion_id→id)`; NOT NULL | Atributo `operacion_id`; el nombre y tipo se conservan según el DDL. |
| `accion` | `text` | NOT NULL | Atributo `accion`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NULL permitido | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `ocurrida_en` | `timestamptz` | NOT NULL | Atributo `ocurrida_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `UNIQUE (operacion_id)`
- `CONSTRAINT operacion_arriendo_historial_ensayo_local_accion_check CHECK (accion IN ('checkin_registrado','checkout_registrado','recepcion_confirmada','observacion_registrada','descargo_evidencia'))`


### B.031 Tabla `public.outbox_evento_ciclo_local`
- **Migración de creación:** `V000027`
- **Atributos:** 11

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `evento_id` | `uuid` | PK compuesta (evento_id, numero_ciclo); UQ compuesta (evento_id, clave_idempotencia); FK → `public.outbox_evento_local(evento_id→id)`; NOT NULL | Atributo `evento_id`; el nombre y tipo se conservan según el DDL. |
| `numero_ciclo` | `integer` | PK compuesta (evento_id, numero_ciclo); NOT NULL | Atributo `numero_ciclo`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `iniciada_en` | `timestamptz` | NOT NULL | Atributo `iniciada_en`; el nombre y tipo se conservan según el DDL. |
| `finalizada_en` | `timestamptz` | NULL permitido | Atributo `finalizada_en`; el nombre y tipo se conservan según el DDL. |
| `intentos` | `integer` | DEFAULT `0`; NOT NULL | Atributo `intentos`; el nombre y tipo se conservan según el DDL. |
| `codigo_resultado` | `text` | NULL permitido | Atributo `codigo_resultado`; el nombre y tipo se conservan según el DDL. |
| `actor_reapertura_id` | `uuid` | FK → `public.usuario(actor_reapertura_id→id)`; NULL permitido | Atributo `actor_reapertura_id`; el nombre y tipo se conservan según el DDL. |
| `motivo_reapertura_codigo` | `text` | NULL permitido | Atributo `motivo_reapertura_codigo`; el nombre y tipo se conservan según el DDL. |
| `correlacion_id` | `text` | NULL permitido | Atributo `correlacion_id`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (evento_id, clave_idempotencia); NULL permitido | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (numero_ciclo > 0)`
- `CHECK (estado IN ('pendiente','entregada','fallo_terminal','cancelada'))`
- `CHECK (intentos BETWEEN 0 AND 8)`
- `CHECK (motivo_reapertura_codigo IS NULL OR motivo_reapertura_codigo IN ('smtp_restaurado','reintento_operativo'))`
- `PRIMARY KEY (evento_id, numero_ciclo)`
- `UNIQUE (evento_id, clave_idempotencia)`
- `CHECK ((estado='pendiente') = (finalizada_en IS NULL))`
- `CHECK ((actor_reapertura_id IS NULL AND motivo_reapertura_codigo IS NULL AND correlacion_id IS NULL AND clave_idempotencia IS NULL) OR (actor_reapertura_id IS NOT NULL AND motivo_reapertura_codigo IS NOT NULL AND correlacion_id IS NOT NULL AND clave_idempotencia IS NOT NULL))`
- `CHECK (finalizada_en IS NULL OR finalizada_en >= iniciada_en)`


### B.032 Tabla `public.outbox_evento_local`
- **Migración de creación:** `V000022`
- **Atributos:** 19

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `agregado_tipo` | `text` | NOT NULL | Atributo `agregado_tipo`; el nombre y tipo se conservan según el DDL. |
| `agregado_id` | `uuid` | NOT NULL | Atributo `agregado_id`; el nombre y tipo se conservan según el DDL. |
| `tipo` | `text` | NOT NULL | Atributo `tipo`; el nombre y tipo se conservan según el DDL. |
| `clave_deduplicacion` | `text` | UQ; NOT NULL | Atributo `clave_deduplicacion`; el nombre y tipo se conservan según el DDL. |
| `version` | `smallint` | NOT NULL | Atributo `version`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `disponible_en` | `timestamptz` | NOT NULL | Atributo `disponible_en`; el nombre y tipo se conservan según el DDL. |
| `lease_hasta` | `timestamptz` | NULL permitido | Atributo `lease_hasta`; el nombre y tipo se conservan según el DDL. |
| `intentos` | `integer` | DEFAULT `0`; NOT NULL | Atributo `intentos`; el nombre y tipo se conservan según el DDL. |
| `entregada_en` | `timestamptz` | NULL permitido | Atributo `entregada_en`; el nombre y tipo se conservan según el DDL. |
| `ultimo_error` | `text` | NULL permitido | Atributo `ultimo_error`; el nombre y tipo se conservan según el DDL. |
| `cancelada_en` | `timestamptz` | NULL permitido | Atributo `cancelada_en`; el nombre y tipo se conservan según el DDL. |
| `motivo_cancelacion_codigo` | `text` | NULL permitido | Atributo `motivo_cancelacion_codigo`; el nombre y tipo se conservan según el DDL. |
| `retirar_en` | `timestamptz` | NULL permitido | Atributo `retirar_en`; el nombre y tipo se conservan según el DDL. |
| `ciclo_actual` | `integer` | DEFAULT `1`; NOT NULL | Atributo `ciclo_actual`; el nombre y tipo se conservan según el DDL. |
| `intentos_ciclo` | `integer` | DEFAULT `0`; NOT NULL | Atributo `intentos_ciclo`; el nombre y tipo se conservan según el DDL. |
| `fallo_terminal_en` | `timestamptz` | NULL permitido | Atributo `fallo_terminal_en`; el nombre y tipo se conservan según el DDL. |
| `codigo_fallo_terminal` | `text` | NULL permitido | Atributo `codigo_fallo_terminal`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (length(btrim(agregado_tipo)) BETWEEN 1 AND 40)`
- `CHECK (tipo ~ '^[a-z][a-z0-9_.-]{2,100}$')`
- `CHECK (length(btrim(clave_deduplicacion)) BETWEEN 1 AND 120)`
- `CHECK (version > 0)`
- `CHECK (intentos >= 0)`
- `CONSTRAINT outbox_evento_lease_ck CHECK (lease_hasta IS NULL OR lease_hasta >= creada_en)`
- `CHECK (ciclo_actual > 0)`
- `CHECK (intentos_ciclo BETWEEN 0 AND 8)`
- `CONSTRAINT outbox_terminal_failure_ck CHECK ( (fallo_terminal_en IS NULL AND codigo_fallo_terminal IS NULL) OR (fallo_terminal_en IS NOT NULL AND codigo_fallo_terminal IS NOT NULL AND entregada_en IS NULL AND cancelada_en IS NULL AND lease_hasta IS NULL AND retirar_en = fallo_terminal_en + interval '30 days') )`
- `CONSTRAINT outbox_evento_entrega_ck CHECK ( entregada_en IS NULL OR entregada_en >= creada_en )`
- `CONSTRAINT outbox_cancelacion_ck CHECK ( (cancelada_en IS NULL AND motivo_cancelacion_codigo IS NULL) OR (cancelada_en IS NOT NULL AND motivo_cancelacion_codigo IN ('baja_local_sin_finalidad','destinatario_inactivo')) )`


### B.033 Tabla `public.profile_media`
- **Migración de creación:** `V000068`
- **Atributos:** 3

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `propietario_id` | `uuid` | PK; FK → `public.usuario(propietario_id→id)`; FK → `public.media_asset(media_id→id, propietario_id→propietario_id)` [profile_media_asset_owner_fk]; NOT NULL | Atributo `propietario_id`; el nombre y tipo se conservan según el DDL. |
| `media_id` | `uuid` | UQ; FK → `public.media_asset(media_id→id, propietario_id→propietario_id)` [profile_media_asset_owner_fk]; NOT NULL | Atributo `media_id`; el nombre y tipo se conservan según el DDL. |
| `updated_at` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de actualización del registro. |

**Restricciones DDL vigentes:**

- `CONSTRAINT profile_media_asset_owner_fk FOREIGN KEY (media_id,propietario_id) REFERENCES public.media_asset(id,propietario_id) ON DELETE RESTRICT`


### B.034 Tabla `public.reaplicacion_baja_local`
- **Migración de creación:** `V000026`
- **Atributos:** 6

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `restore_id` | `uuid` | PK compuesta (restore_id, ejecucion_origen_id); NOT NULL | Atributo `restore_id`; el nombre y tipo se conservan según el DDL. |
| `ejecucion_origen_id` | `uuid` | PK compuesta (restore_id, ejecucion_origen_id); NOT NULL | Atributo `ejecucion_origen_id`; el nombre y tipo se conservan según el DDL. |
| `usuario_id` | `uuid` | FK → `public.usuario(usuario_id→id)`; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `intentos` | `integer` | DEFAULT `1`; NOT NULL | Atributo `intentos`; el nombre y tipo se conservan según el DDL. |
| `aplicada_en` | `timestamptz` | NOT NULL | Atributo `aplicada_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (estado IN ('reaplicada','ya_presente','pendiente'))`
- `CHECK (intentos > 0)`
- `PRIMARY KEY (restore_id, ejecucion_origen_id)`


### B.035 Tabla `public.region_publica`
- **Migración de creación:** `V000055`
- **Atributos:** 3

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `catalogo_version` | `text` | PK compuesta (catalogo_version, codigo); UQ compuesta (catalogo_version, codigo, nombre); FK → `public.catalogo_ubicacion_publica(catalogo_version→version)`; NOT NULL | Atributo `catalogo_version`; el nombre y tipo se conservan según el DDL. |
| `codigo` | `text` | PK compuesta (catalogo_version, codigo); UQ compuesta (catalogo_version, codigo, nombre); NOT NULL | Atributo `codigo`; el nombre y tipo se conservan según el DDL. |
| `nombre` | `text` | UQ compuesta (catalogo_version, codigo, nombre); NOT NULL | Atributo `nombre`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (codigo ~ '^[0-9]{2}$')`
- `CHECK (length(btrim(nombre)) BETWEEN 1 AND 100)`
- `PRIMARY KEY (catalogo_version, codigo)`
- `UNIQUE (catalogo_version, codigo, nombre)`


### B.036 Tabla `public.reporte_resena_ensayo_local`
- **Migración de creación:** `V000036`
- **Atributos:** 13

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `resena_id` | `uuid` | UQ; FK → `public.resena_ensayo_local(resena_id→id)`; NOT NULL | Atributo `resena_id`; el nombre y tipo se conservan según el DDL. |
| `espacio_id` | `uuid` | FK → `public.espacio(espacio_id→id)`; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `anfitrion_id` | `uuid` | FK → `public.usuario(anfitrion_id→id)`; NULL permitido | Atributo `anfitrion_id`; el nombre y tipo se conservan según el DDL. |
| `motivo_codigo` | `text` | NOT NULL | Atributo `motivo_codigo`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `resolver_en` | `timestamptz` | NULL permitido | Atributo `resolver_en`; el nombre y tipo se conservan según el DDL. |
| `resuelta_por` | `uuid` | FK → `public.usuario(resuelta_por→id)`; NULL permitido | Atributo `resuelta_por`; el nombre y tipo se conservan según el DDL. |
| `motivo_resolucion_codigo` | `text` | NULL permitido | Atributo `motivo_resolucion_codigo`; el nombre y tipo se conservan según el DDL. |
| `retirar_en` | `timestamptz` | NULL permitido | Atributo `retirar_en`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `huella_solicitud` | `bytea` | NOT NULL | Atributo `huella_solicitud`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (motivo_codigo IN ('insultos_acoso','datos_personales','spam','ajeno_experiencia'))`
- `CHECK (estado IN ('pendiente','desestimada','oculta'))`
- `CHECK (motivo_resolucion_codigo IN ('sin_infraccion','contenido_inadecuado','duplicado','error_registro'))`
- `CHECK (length(btrim(clave_idempotencia)) BETWEEN 8 AND 200)`
- `CHECK (octet_length(huella_solicitud)=32)`
- `CHECK ((estado='pendiente' AND resolver_en IS NULL AND resuelta_por IS NULL AND motivo_resolucion_codigo IS NULL AND retirar_en IS NULL) OR (estado IN ('desestimada','oculta') AND resolver_en IS NOT NULL AND resuelta_por IS NOT NULL AND motivo_resolucion_codigo IS NOT NULL AND retirar_en=resolver_en + interval '24 months'))`


### B.037 Tabla `public.reporte_resena_historial_local`
- **Migración de creación:** `V000036`
- **Atributos:** 7

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `secuencia` | `bigint` | PK; NOT NULL | Atributo `secuencia`; el nombre y tipo se conservan según el DDL. |
| `reporte_id` | `uuid` | FK → `public.reporte_resena_ensayo_local(reporte_id→id)`; NOT NULL | Atributo `reporte_id`; el nombre y tipo se conservan según el DDL. |
| `estado_anterior` | `text` | NULL permitido | Atributo `estado_anterior`; el nombre y tipo se conservan según el DDL. |
| `estado_nuevo` | `text` | NOT NULL | Atributo `estado_nuevo`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NULL permitido | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `motivo_codigo` | `text` | NOT NULL | Atributo `motivo_codigo`; el nombre y tipo se conservan según el DDL. |
| `ocurrida_en` | `timestamptz` | NOT NULL | Atributo `ocurrida_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (estado_anterior IN ('pendiente','desestimada','oculta'))`
- `CHECK (estado_nuevo IN ('pendiente','desestimada','oculta'))`


### B.038 Tabla `public.resena_autoria_marca_local`
- **Migración de creación:** `V000037`
- **Atributos:** 3

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `huella_autoria` | `bytea` | PK; NOT NULL | Atributo `huella_autoria`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `retirar_en` | `timestamptz` | NULL permitido | Atributo `retirar_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (octet_length(huella_autoria)=32)`


### B.039 Tabla `public.resena_ensayo_local`
- **Migración de creación:** `V000036`
- **Atributos:** 13

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `reserva_id` | `uuid` | UQ compuesta (reserva_id, autor_id); FK → `public.reserva_ensayo_local(reserva_id→id)`; NOT NULL | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `espacio_id` | `uuid` | FK → `public.espacio(espacio_id→id)`; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `autor_id` | `uuid` | UQ compuesta (reserva_id, autor_id); FK → `public.usuario(autor_id→id)`; NULL permitido | Atributo `autor_id`; el nombre y tipo se conservan según el DDL. |
| `destinatario_tipo` | `text` | NOT NULL | Atributo `destinatario_tipo`; el nombre y tipo se conservan según el DDL. |
| `destinatario_id` | `uuid` | FK → `public.usuario(destinatario_id→id)`; NULL permitido | Atributo `destinatario_id`; el nombre y tipo se conservan según el DDL. |
| `puntuacion` | `smallint` | NOT NULL | Atributo `puntuacion`; el nombre y tipo se conservan según el DDL. |
| `comentario` | `text` | DEFAULT `''`; NOT NULL | Atributo `comentario`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | DEFAULT `'publicada'`; NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `retirar_en` | `timestamptz` | NOT NULL | Atributo `retirar_en`; el nombre y tipo se conservan según el DDL. |
| `huella_solicitud` | `bytea` | NOT NULL | Atributo `huella_solicitud`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (destinatario_tipo IN ('espacio','arrendatario'))`
- `CHECK (puntuacion BETWEEN 1 AND 5)`
- `CHECK (estado IN ('publicada','reportada','oculta'))`
- `CHECK (octet_length(huella_solicitud)=32)`
- `CHECK (length(btrim(clave_idempotencia)) BETWEEN 8 AND 200)`
- `UNIQUE (reserva_id,autor_id)`
- `CHECK ((destinatario_tipo='espacio' AND destinatario_id IS NULL) OR (destinatario_tipo='arrendatario' AND destinatario_id IS NOT NULL))`
- `CHECK (retirar_en = creada_en + interval '24 months')`
- `CONSTRAINT resena_destinatario_privacidad_ck CHECK ( (destinatario_tipo='espacio' AND destinatario_id IS NULL) OR (destinatario_tipo='arrendatario' AND destinatario_id IS NOT NULL) OR (destinatario_tipo='arrendatario_retirado' AND destinatario_id IS NULL) )`
- `CONSTRAINT resena_destinatario_tipo_ck CHECK (destinatario_tipo IN ('espacio','arrendatario','arrendatario_retirado'))`


### B.040 Tabla `public.simulacion_precio_privada`
- **Migración de creación:** `V000010`
- **Atributos:** 13

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `espacio_id` | `uuid` | FK → `public.tarifa_espacio(espacio_id→espacio_id, tarifa_version→version)` [simulacion_precio_tarifa_fk]; FK → `public.espacio(espacio_id→id, propietario_id→propietario_id)` [simulacion_precio_espacio_propietario_fk]; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `propietario_id` | `uuid` | FK → `public.usuario(propietario_id→id)`; FK → `public.espacio(espacio_id→id, propietario_id→propietario_id)` [simulacion_precio_espacio_propietario_fk]; NOT NULL | Atributo `propietario_id`; el nombre y tipo se conservan según el DDL. |
| `tarifa_version` | `integer` | FK → `public.tarifa_espacio(espacio_id→espacio_id, tarifa_version→version)` [simulacion_precio_tarifa_fk]; NOT NULL | Versión asociada a la tarifa; no representa por sí misma un monto. |
| `modalidad` | `text` | NOT NULL | Atributo `modalidad`; el nombre y tipo se conservan según el DDL. |
| `precio_unitario_clp` | `bigint` | NOT NULL | Atributo `precio_unitario_clp`; el nombre y tipo se conservan según el DDL. |
| `moneda` | `char(3)` | NOT NULL | Atributo `moneda`; el nombre y tipo se conservan según el DDL. |
| `unidades_facturadas` | `bigint` | NOT NULL | Atributo `unidades_facturadas`; el nombre y tipo se conservan según el DDL. |
| `subtotal_clp` | `bigint` | NOT NULL | Atributo `subtotal_clp`; el nombre y tipo se conservan según el DDL. |
| `inicio` | `timestamptz` | NOT NULL | Atributo `inicio`; el nombre y tipo se conservan según el DDL. |
| `termino` | `timestamptz` | NOT NULL | Atributo `termino`; el nombre y tipo se conservan según el DDL. |
| `zona_horaria` | `text` | NOT NULL | Atributo `zona_horaria`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de creación del registro. |

**Restricciones DDL vigentes:**

- `CHECK (modalidad IN ('hora', 'dia', 'mes'))`
- `CHECK (precio_unitario_clp > 5000)`
- `CHECK (moneda = 'CLP')`
- `CHECK (unidades_facturadas > 0)`
- `CHECK (subtotal_clp > 0)`
- `CHECK (termino > inicio)`
- `CHECK (length(btrim(zona_horaria)) BETWEEN 1 AND 100)`
- `CONSTRAINT simulacion_precio_tarifa_fk FOREIGN KEY (espacio_id, tarifa_version) REFERENCES public.tarifa_espacio(espacio_id, version) ON DELETE RESTRICT`
- `CONSTRAINT simulacion_precio_espacio_propietario_fk FOREIGN KEY (espacio_id, propietario_id) REFERENCES public.espacio(id, propietario_id) ON DELETE RESTRICT`


### B.041 Tabla `public.solicitud_titular`
- **Migración de creación:** `V000002`
- **Atributos:** 9

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `usuario_id` | `uuid` | FK → `public.usuario(usuario_id→id)` [solicitud_titular_usuario_fk]; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `tipo` | `text` | NOT NULL | Atributo `tipo`; el nombre y tipo se conservan según el DDL. |
| `canal` | `text` | NOT NULL | Atributo `canal`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | DEFAULT `'en_revision'`; NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `solicitada_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Atributo `solicitada_en`; el nombre y tipo se conservan según el DDL. |
| `resuelta_en` | `timestamptz` | NULL permitido | Atributo `resuelta_en`; el nombre y tipo se conservan según el DDL. |
| `motivo_resolucion_codigo` | `text` | NULL permitido | Atributo `motivo_resolucion_codigo`; el nombre y tipo se conservan según el DDL. |
| `retirar_en` | `timestamptz` | NULL permitido | Atributo `retirar_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CONSTRAINT solicitud_titular_pk PRIMARY KEY (id)`
- `CONSTRAINT solicitud_titular_usuario_fk FOREIGN KEY (usuario_id) REFERENCES public.usuario (id) ON DELETE RESTRICT`
- `CONSTRAINT solicitud_titular_tipo_ck CHECK (tipo IN ('acceso', 'supresion'))`
- `CONSTRAINT solicitud_titular_canal_ck CHECK (canal IN ('web', 'api'))`
- `CONSTRAINT solicitud_titular_estado_ck CHECK (estado IN ( 'recibida', 'identidad_pendiente', 'en_revision', 'resuelta', 'denegada_fundada' ))`
- `CONSTRAINT solicitud_titular_resolucion_ck CHECK ( (resuelta_en IS NULL AND motivo_resolucion_codigo IS NULL AND retirar_en IS NULL) OR (resuelta_en IS NOT NULL AND motivo_resolucion_codigo IS NOT NULL AND retirar_en = resuelta_en + interval '5 years') )`
- `CONSTRAINT solicitud_titular_motivo_ck CHECK ( motivo_resolucion_codigo IS NULL OR motivo_resolucion_codigo IN ('baja_local_minimizada','derecho_tramitado') )`


### B.042 Tabla `public.space_media`
- **Migración de creación:** `V000068`
- **Atributos:** 8

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; UQ compuesta (espacio_id, propietario_id, id); NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `espacio_id` | `uuid` | UQ compuesta (espacio_id, propietario_id, id); FK → `public.espacio(espacio_id→id, propietario_id→propietario_id)` [space_media_space_owner_fk]; FK → `public.media_asset(media_id→id, espacio_id→espacio_id, propietario_id→propietario_id)` [space_media_asset_scope_fk]; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `propietario_id` | `uuid` | UQ compuesta (espacio_id, propietario_id, id); FK → `public.espacio(espacio_id→id, propietario_id→propietario_id)` [space_media_space_owner_fk]; FK → `public.media_asset(media_id→id, espacio_id→espacio_id, propietario_id→propietario_id)` [space_media_asset_scope_fk]; NOT NULL | Atributo `propietario_id`; el nombre y tipo se conservan según el DDL. |
| `media_id` | `uuid` | UQ; FK → `public.media_asset(media_id→id, espacio_id→espacio_id, propietario_id→propietario_id)` [space_media_asset_scope_fk]; NOT NULL | Atributo `media_id`; el nombre y tipo se conservan según el DDL. |
| `alt_text` | `varchar(250)` | DEFAULT `''`; NOT NULL | Atributo `alt_text`; el nombre y tipo se conservan según el DDL. |
| `visible` | `boolean` | DEFAULT `false`; NOT NULL | Atributo `visible`; el nombre y tipo se conservan según el DDL. |
| `created_at` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de creación del registro. |
| `retired_at` | `timestamptz` | NULL permitido | Atributo `retired_at`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (length(alt_text)<=250)`
- `CONSTRAINT space_media_space_owner_fk FOREIGN KEY (espacio_id,propietario_id) REFERENCES public.espacio(id,propietario_id) ON DELETE RESTRICT`
- `CONSTRAINT space_media_asset_scope_fk FOREIGN KEY (media_id,espacio_id,propietario_id) REFERENCES public.media_asset(id,espacio_id,propietario_id) ON DELETE RESTRICT`
- `CONSTRAINT space_media_id_scope_uq UNIQUE (espacio_id,propietario_id,id)`
- `CONSTRAINT space_media_retirement_ck CHECK ((retired_at IS NULL) OR NOT visible)`


### B.043 Tabla `public.version_terminos`
- **Migración de creación:** `V000001`
- **Atributos:** 5

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `codigo` | `text` | UQ; NOT NULL | Atributo `codigo`; el nombre y tipo se conservan según el DDL. |
| `tipo` | `text` | NOT NULL | Atributo `tipo`; el nombre y tipo se conservan según el DDL. |
| `hash_sha256` | `char(64)` | NOT NULL | Atributo `hash_sha256`; el nombre y tipo se conservan según el DDL. |
| `publicada_en` | `timestamptz` | NOT NULL | Atributo `publicada_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CONSTRAINT version_terminos_pk PRIMARY KEY (id)`
- `CONSTRAINT version_terminos_codigo_uk UNIQUE (codigo)`
- `CONSTRAINT version_terminos_tipo_ck CHECK (tipo IN ('terminos', 'privacidad', 'politica_arrendador'))`
- `CONSTRAINT version_terminos_hash_ck CHECK (hash_sha256 ~ '^[0-9a-f]{64}$')`


## Dominio: Identidad, autenticación y cuentas

### B.044 Tabla `public.bloqueo_cuenta_administrativo_local`
- **Migración de creación:** `V000041`
- **Atributos:** 5

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `cuenta_id` | `uuid` | PK; FK → `public.usuario(cuenta_id→id)`; NOT NULL | Atributo `cuenta_id`; el nombre y tipo se conservan según el DDL. |
| `bloqueada_por` | `uuid` | FK → `public.usuario(bloqueada_por→id)`; NULL permitido | Atributo `bloqueada_por`; el nombre y tipo se conservan según el DDL. |
| `motivo_codigo` | `text` | NOT NULL | Atributo `motivo_codigo`; el nombre y tipo se conservan según el DDL. |
| `bloqueada_en` | `timestamptz` | NOT NULL | Atributo `bloqueada_en`; el nombre y tipo se conservan según el DDL. |
| `correlacion_id` | `text` | NOT NULL | Atributo `correlacion_id`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (motivo_codigo IN ('riesgo_seguridad','uso_indebido','revision_administrativa'))`
- `CHECK (length(btrim(correlacion_id)) BETWEEN 1 AND 120)`


### B.045 Tabla `public.bloqueo_cuenta_historial_local`
- **Migración de creación:** `V000041`
- **Atributos:** 7

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `cuenta_id` | `uuid` | FK → `public.usuario(cuenta_id→id)`; NOT NULL | Atributo `cuenta_id`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NULL permitido | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `accion` | `text` | NOT NULL | Atributo `accion`; el nombre y tipo se conservan según el DDL. |
| `motivo_codigo` | `text` | NOT NULL | Atributo `motivo_codigo`; el nombre y tipo se conservan según el DDL. |
| `ocurrida_en` | `timestamptz` | NOT NULL | Atributo `ocurrida_en`; el nombre y tipo se conservan según el DDL. |
| `correlacion_id` | `text` | NOT NULL | Atributo `correlacion_id`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (accion IN ('bloquear','desbloquear'))`
- `CHECK (motivo_codigo IN ('riesgo_seguridad','uso_indebido','revision_administrativa','revision_concluida','error_bloqueo','riesgo_resuelto'))`
- `CHECK (length(btrim(correlacion_id)) BETWEEN 1 AND 120)`


### B.046 Tabla `public.categoria_perfil_atributos`
- **Migración de creación:** `V000006`
- **Atributos:** 4

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `categoria_codigo` | `text` | PK compuesta (categoria_codigo, version); FK → `public.categoria_espacio(categoria_codigo→codigo)`; NOT NULL | Atributo `categoria_codigo`; el nombre y tipo se conservan según el DDL. |
| `version` | `integer` | PK compuesta (categoria_codigo, version); NOT NULL | Atributo `version`; el nombre y tipo se conservan según el DDL. |
| `perfil` | `jsonb` | NOT NULL | Atributo `perfil`; el nombre y tipo se conservan según el DDL. |
| `creado_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de creación del registro. |

**Restricciones DDL vigentes:**

- `CHECK (version > 0)`
- `CHECK (jsonb_typeof(perfil) = 'object')`
- `PRIMARY KEY (categoria_codigo, version)`


### B.047 Tabla `public.foto_perfil_sintetica_local`
- **Migración de creación:** `V000030`
- **Atributos:** 15

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `usuario_id` | `uuid` | FK → `public.usuario(usuario_id→id)`; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `archivo_id` | `uuid` | NULL permitido | Atributo `archivo_id`; el nombre y tipo se conservan según el DDL. |
| `mime_type` | `text` | NULL permitido | Atributo `mime_type`; el nombre y tipo se conservan según el DDL. |
| `fixture_code` | `text` | NOT NULL | Atributo `fixture_code`; el nombre y tipo se conservan según el DDL. |
| `sha256` | `text` | NULL permitido | Atributo `sha256`; el nombre y tipo se conservan según el DDL. |
| `size_bytes` | `bigint` | NULL permitido | Atributo `size_bytes`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `retirada_en` | `timestamptz` | NULL permitido | Atributo `retirada_en`; el nombre y tipo se conservan según el DDL. |
| `limpia_en` | `timestamptz` | NULL permitido | Atributo `limpia_en`; el nombre y tipo se conservan según el DDL. |
| `intentos_limpieza` | `integer` | DEFAULT `0`; NOT NULL | Atributo `intentos_limpieza`; el nombre y tipo se conservan según el DDL. |
| `proximo_intento_en` | `timestamptz` | NULL permitido | Atributo `proximo_intento_en`; el nombre y tipo se conservan según el DDL. |
| `ultimo_codigo_error` | `text` | NULL permitido | Atributo `ultimo_codigo_error`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (fixture_code='synthetic-png-v1')`
- `CHECK (estado IN ('activa','reemplazada','retirada','retirada_baja'))`
- `CHECK (intentos_limpieza>=0)`
- `CONSTRAINT foto_perfil_sintetica_archivo_ck CHECK ( (archivo_id IS NULL AND mime_type IS NULL AND sha256 IS NULL AND size_bytes IS NULL AND limpia_en IS NOT NULL) OR (archivo_id IS NOT NULL AND mime_type='image/png' AND sha256 ~ '^[0-9a-f]{64}$' AND size_bytes BETWEEN 1 AND 4096 AND limpia_en IS NULL) )`
- `CONSTRAINT foto_perfil_sintetica_retirada_ck CHECK ( (estado='activa' AND retirada_en IS NULL) OR (estado<>'activa' AND retirada_en IS NOT NULL) )`
- `CONSTRAINT foto_perfil_sintetica_idempotencia_ck CHECK (length(clave_idempotencia) BETWEEN 8 AND 128)`


### B.048 Tabla `public.perfil_usuario`
- **Migración de creación:** `V000002`
- **Atributos:** 4

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `usuario_id` | `uuid` | PK; FK → `public.usuario(usuario_id→id)` [perfil_usuario_usuario_fk]; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `nombre_visible` | `text` | NOT NULL | Atributo `nombre_visible`; el nombre y tipo se conservan según el DDL. |
| `telefono_normalizado` | `text` | NULL permitido | Atributo `telefono_normalizado`; el nombre y tipo se conservan según el DDL. |
| `actualizado_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de actualización del registro. |

**Restricciones DDL vigentes:**

- `CONSTRAINT perfil_usuario_pk PRIMARY KEY (usuario_id)`
- `CONSTRAINT perfil_usuario_usuario_fk FOREIGN KEY (usuario_id) REFERENCES public.usuario (id) ON DELETE RESTRICT`
- `CONSTRAINT perfil_usuario_nombre_ck CHECK ( length(btrim(nombre_visible)) BETWEEN 1 AND 120 AND nombre_visible ~ '^[[:alpha:] ]+$' )`
- `CONSTRAINT perfil_usuario_telefono_ck CHECK ( telefono_normalizado IS NULL OR telefono_normalizado ~ '^[0-9]{9}$' )`


### B.049 Tabla `public.registro_replay_baja_local`
- **Migración de creación:** `V000062`
- **Atributos:** 5

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `ejecucion_origen_id` | `uuid` | PK; NOT NULL | Atributo `ejecucion_origen_id`; el nombre y tipo se conservan según el DDL. |
| `solicitud_id` | `uuid` | NOT NULL | Atributo `solicitud_id`; el nombre y tipo se conservan según el DDL. |
| `usuario_id` | `uuid` | NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `solicitada_en` | `timestamptz` | NOT NULL | Atributo `solicitada_en`; el nombre y tipo se conservan según el DDL. |
| `completada_en` | `timestamptz` | NOT NULL | Atributo `completada_en`; el nombre y tipo se conservan según el DDL. |


### B.050 Tabla `public.rol_usuario`
- **Migración de creación:** `V000001`
- **Atributos:** 4

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `usuario_id` | `uuid` | PK compuesta (usuario_id, rol); FK → `public.usuario(usuario_id→id)` [rol_usuario_usuario_fk]; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `rol` | `text` | PK compuesta (usuario_id, rol); NOT NULL | Atributo `rol`; el nombre y tipo se conservan según el DDL. |
| `concedido_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Atributo `concedido_en`; el nombre y tipo se conservan según el DDL. |
| `concedido_por` | `uuid` | FK → `public.usuario(concedido_por→id)` [rol_usuario_concedido_por_fk]; NULL permitido | Atributo `concedido_por`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CONSTRAINT rol_usuario_pk PRIMARY KEY (usuario_id, rol)`
- `CONSTRAINT rol_usuario_usuario_fk FOREIGN KEY (usuario_id) REFERENCES public.usuario (id) ON DELETE RESTRICT`
- `CONSTRAINT rol_usuario_concedido_por_fk FOREIGN KEY (concedido_por) REFERENCES public.usuario (id) ON DELETE RESTRICT`
- `CONSTRAINT rol_usuario_rol_ck CHECK (rol IN ('arrendatario', 'arrendador', 'administrador'))`


### B.051 Tabla `public.rol_usuario_evento`
- **Migración de creación:** `V000074`
- **Atributos:** 6

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; DEFAULT `gen_random_uuid()`; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `usuario_id` | `uuid` | UQ compuesta (usuario_id, rol); FK → `public.usuario(usuario_id→id)`; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `rol` | `text` | UQ compuesta (usuario_id, rol); NOT NULL | Atributo `rol`; el nombre y tipo se conservan según el DDL. |
| `accion` | `text` | NOT NULL | Atributo `accion`; el nombre y tipo se conservan según el DDL. |
| `recurso_id` | `uuid` | NOT NULL | Atributo `recurso_id`; el nombre y tipo se conservan según el DDL. |
| `ocurrida_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Atributo `ocurrida_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (rol IN ('arrendatario', 'arrendador'))`
- `CHECK (accion IN ('primer_borrador_espacio', 'primera_solicitud_reserva'))`
- `CONSTRAINT rol_usuario_evento_usuario_rol_uk UNIQUE (usuario_id, rol)`
- `CONSTRAINT rol_usuario_evento_accion_rol_ck CHECK ( (rol = 'arrendador' AND accion = 'primer_borrador_espacio') OR (rol = 'arrendatario' AND accion = 'primera_solicitud_reserva') )`


### B.052 Tabla `public.sesion`
- **Migración de creación:** `V000001`
- **Atributos:** 8

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `usuario_id` | `uuid` | FK → `public.usuario(usuario_id→id)` [sesion_usuario_fk]; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `token_hash` | `char(64)` | UQ; NOT NULL | Atributo `token_hash`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de creación del registro. |
| `ultima_actividad_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Atributo `ultima_actividad_en`; el nombre y tipo se conservan según el DDL. |
| `expira_en` | `timestamptz` | NOT NULL | Atributo `expira_en`; el nombre y tipo se conservan según el DDL. |
| `revocada_en` | `timestamptz` | NULL permitido | Atributo `revocada_en`; el nombre y tipo se conservan según el DDL. |
| `cliente_resumen` | `text` | NULL permitido | Atributo `cliente_resumen`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CONSTRAINT sesion_pk PRIMARY KEY (id)`
- `CONSTRAINT sesion_usuario_fk FOREIGN KEY (usuario_id) REFERENCES public.usuario (id) ON DELETE RESTRICT`
- `CONSTRAINT sesion_token_hash_uk UNIQUE (token_hash)`
- `CONSTRAINT sesion_token_hash_ck CHECK (token_hash ~ '^[0-9a-f]{64}$')`
- `CONSTRAINT sesion_creacion_expiracion_ck CHECK ( expira_en > creada_en AND expira_en <= creada_en + interval '8 hours' )`
- `CONSTRAINT sesion_actividad_ck CHECK ( ultima_actividad_en >= creada_en AND ultima_actividad_en <= expira_en )`
- `CONSTRAINT sesion_revocacion_ck CHECK (revocada_en IS NULL OR revocada_en >= creada_en)`


### B.053 Tabla `public.token_accion`
- **Migración de creación:** `V000001`
- **Atributos:** 9

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `usuario_id` | `uuid` | FK → `public.usuario(usuario_id→id)` [token_accion_usuario_fk]; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `proposito` | `text` | NOT NULL | Atributo `proposito`; el nombre y tipo se conservan según el DDL. |
| `token_hash` | `char(64)` | UQ; NOT NULL | Atributo `token_hash`; el nombre y tipo se conservan según el DDL. |
| `creado_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de creación del registro. |
| `expira_en` | `timestamptz` | NOT NULL | Atributo `expira_en`; el nombre y tipo se conservan según el DDL. |
| `consumido_en` | `timestamptz` | NULL permitido | Atributo `consumido_en`; el nombre y tipo se conservan según el DDL. |
| `invalidado_en` | `timestamptz` | NULL permitido | Atributo `invalidado_en`; el nombre y tipo se conservan según el DDL. |
| `intentos` | `integer` | DEFAULT `0`; NOT NULL | Atributo `intentos`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CONSTRAINT token_accion_pk PRIMARY KEY (id)`
- `CONSTRAINT token_accion_usuario_fk FOREIGN KEY (usuario_id) REFERENCES public.usuario (id) ON DELETE RESTRICT`
- `CONSTRAINT token_accion_token_hash_uk UNIQUE (token_hash)`
- `CONSTRAINT token_accion_token_hash_ck CHECK (token_hash ~ '^[0-9a-f]{64}$')`
- `CONSTRAINT token_accion_proposito_ck CHECK (proposito IN ('verificar_correo', 'recuperar_clave'))`
- `CONSTRAINT token_accion_intentos_ck CHECK (intentos BETWEEN 0 AND 5)`
- `CONSTRAINT token_accion_creacion_expiracion_ck CHECK (expira_en > creado_en)`
- `CONSTRAINT token_accion_consumido_ck CHECK (consumido_en IS NULL OR consumido_en >= creado_en)`
- `CONSTRAINT token_accion_invalidado_ck CHECK (invalidado_en IS NULL OR invalidado_en >= creado_en)`
- `CONSTRAINT token_accion_terminal_mutuo_ck CHECK (consumido_en IS NULL OR invalidado_en IS NULL)`


### B.054 Tabla `public.usuario`
- **Migración de creación:** `V000001`
- **Atributos:** 12

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `correo_original` | `text` | NOT NULL | Atributo `correo_original`; el nombre y tipo se conservan según el DDL. |
| `correo_normalizado` | `text` | UQ; NOT NULL | Atributo `correo_normalizado`; el nombre y tipo se conservan según el DDL. |
| `hash_clave` | `text` | NOT NULL | Atributo `hash_clave`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | DEFAULT `'correo_pendiente'`; NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `creado_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de creación del registro. |
| `actualizado_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de actualización del registro. |
| `baja_solicitada_en` | `timestamptz` | NULL permitido | Atributo `baja_solicitada_en`; el nombre y tipo se conservan según el DDL. |
| `intentos_fallidos_consecutivos` | `integer` | DEFAULT `0`; NOT NULL | Atributo `intentos_fallidos_consecutivos`; el nombre y tipo se conservan según el DDL. |
| `bloqueado_hasta` | `timestamptz` | NULL permitido | Atributo `bloqueado_hasta`; el nombre y tipo se conservan según el DDL. |
| `preferencia_uso` | `text` | NULL permitido | Atributo `preferencia_uso`; el nombre y tipo se conservan según el DDL. |
| `baja_iniciada_en` | `timestamptz` | NULL permitido | Atributo `baja_iniciada_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CONSTRAINT usuario_pk PRIMARY KEY (id)`
- `CONSTRAINT usuario_correo_normalizado_uk UNIQUE (correo_normalizado)`
- `CONSTRAINT usuario_estado_ck CHECK (estado IN ( 'correo_pendiente', 'activo', 'bloqueado', 'baja_solicitada', 'desidentificado' ))`
- `CONSTRAINT usuario_intentos_fallidos_ck CHECK (intentos_fallidos_consecutivos >= 0)`
- `CONSTRAINT usuario_preferencia_uso_ck CHECK (preferencia_uso IS NULL OR preferencia_uso IN ('ofrecer', 'arrendar'))`


## Dominio: Espacios, publicaciones y catálogo

### B.055 Tabla `public.categoria_espacio`
- **Migración de creación:** `V000005`
- **Atributos:** 4

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `codigo` | `text` | PK; NOT NULL | Atributo `codigo`; el nombre y tipo se conservan según el DDL. |
| `nombre` | `text` | UQ; NOT NULL | Atributo `nombre`; el nombre y tipo se conservan según el DDL. |
| `orden` | `smallint` | UQ; NOT NULL | Atributo `orden`; el nombre y tipo se conservan según el DDL. |
| `activa` | `boolean` | DEFAULT `true`; NOT NULL | Atributo `activa`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (orden > 0)`


### B.056 Tabla `public.espacio`
- **Migración de creación:** `V000005`
- **Atributos:** 21

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; UQ compuesta (id, categoria_codigo); UQ compuesta (id, propietario_id); UQ compuesta (id, propietario_id); FK → `public.espacio_galeria_sintetica_local(id→espacio_id, propietario_id→propietario_id, portada_foto_id→id)` [espacio_portada_galeria_fk]; FK → `public.space_media(id→espacio_id, propietario_id→propietario_id, portada_media_id→id)` [espacio_portada_media_fk]; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `propietario_id` | `uuid` | UQ compuesta (id, propietario_id); UQ compuesta (id, propietario_id); FK → `public.usuario(propietario_id→id)`; FK → `public.espacio_galeria_sintetica_local(id→espacio_id, propietario_id→propietario_id, portada_foto_id→id)` [espacio_portada_galeria_fk]; FK → `public.space_media(id→espacio_id, propietario_id→propietario_id, portada_media_id→id)` [espacio_portada_media_fk]; NOT NULL | Atributo `propietario_id`; el nombre y tipo se conservan según el DDL. |
| `categoria_codigo` | `text` | UQ compuesta (id, categoria_codigo); FK → `public.categoria_espacio(categoria_codigo→codigo)`; NOT NULL | Atributo `categoria_codigo`; el nombre y tipo se conservan según el DDL. |
| `titulo` | `varchar(70)` | NOT NULL | Atributo `titulo`; el nombre y tipo se conservan según el DDL. |
| `descripcion` | `text` | NOT NULL | Atributo `descripcion`; el nombre y tipo se conservan según el DDL. |
| `superficie_m2` | `numeric(10,2)` | NOT NULL | Atributo `superficie_m2`; el nombre y tipo se conservan según el DDL. |
| `capacidad_maxima` | `integer` | NOT NULL | Atributo `capacidad_maxima`; el nombre y tipo se conservan según el DDL. |
| `reglas_uso` | `varchar(250)` | NOT NULL | Atributo `reglas_uso`; el nombre y tipo se conservan según el DDL. |
| `modalidad_tarifa` | `text` | NOT NULL | Atributo `modalidad_tarifa`; el nombre y tipo se conservan según el DDL. |
| `precio_base_clp` | `bigint` | NOT NULL | Atributo `precio_base_clp`; el nombre y tipo se conservan según el DDL. |
| `direccion` | `text` | NOT NULL | Atributo `direccion`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | DEFAULT `'borrador'`; NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `creado_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de creación del registro. |
| `actualizado_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de actualización del registro. |
| `zona_horaria` | `text` | NULL permitido | Atributo `zona_horaria`; el nombre y tipo se conservan según el DDL. |
| `portada_foto_id` | `uuid` | FK → `public.espacio_galeria_sintetica_local(id→espacio_id, propietario_id→propietario_id, portada_foto_id→id)` [espacio_portada_galeria_fk]; NULL permitido | Atributo `portada_foto_id`; el nombre y tipo se conservan según el DDL. |
| `ubicacion_catalogo_version` | `text` | FK → `public.region_publica(ubicacion_catalogo_version→catalogo_version, region_codigo→codigo)` [espacio_public_region_fk]; FK → `public.comuna_publica(ubicacion_catalogo_version→catalogo_version, region_codigo→region_codigo, comuna_codigo→codigo)` [espacio_public_commune_fk]; NULL permitido | Atributo `ubicacion_catalogo_version`; el nombre y tipo se conservan según el DDL. |
| `region_codigo` | `text` | FK → `public.region_publica(ubicacion_catalogo_version→catalogo_version, region_codigo→codigo)` [espacio_public_region_fk]; FK → `public.comuna_publica(ubicacion_catalogo_version→catalogo_version, region_codigo→region_codigo, comuna_codigo→codigo)` [espacio_public_commune_fk]; NULL permitido | Atributo `region_codigo`; el nombre y tipo se conservan según el DDL. |
| `comuna_codigo` | `text` | FK → `public.comuna_publica(ubicacion_catalogo_version→catalogo_version, region_codigo→region_codigo, comuna_codigo→codigo)` [espacio_public_commune_fk]; NULL permitido | Atributo `comuna_codigo`; el nombre y tipo se conservan según el DDL. |
| `busqueda_publica` | `tsvector` | DEFAULT `''::tsvector`; NOT NULL | Atributo `busqueda_publica`; el nombre y tipo se conservan según el DDL. |
| `portada_media_id` | `uuid` | FK → `public.space_media(id→espacio_id, propietario_id→propietario_id, portada_media_id→id)` [espacio_portada_media_fk]; NULL permitido | Atributo `portada_media_id`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (length(btrim(titulo)) BETWEEN 1 AND 70)`
- `CHECK (length(btrim(descripcion)) >= 100)`
- `CHECK (superficie_m2 > 0)`
- `CHECK (capacidad_maxima > 0)`
- `CHECK (length(btrim(reglas_uso)) BETWEEN 1 AND 250)`
- `CHECK (modalidad_tarifa IN ('hora', 'dia', 'mes'))`
- `CHECK (precio_base_clp > 5000)`
- `CHECK (length(btrim(direccion)) BETWEEN 1 AND 500)`
- `CONSTRAINT espacio_id_categoria_unique UNIQUE (id, categoria_codigo)`
- `CONSTRAINT espacio_zona_horaria_ck CHECK ( zona_horaria IS NULL OR length(btrim(zona_horaria)) BETWEEN 1 AND 100 )`
- `CONSTRAINT espacio_id_propietario_uk UNIQUE (id, propietario_id)`
- `CONSTRAINT espacio_owner_id_uq UNIQUE (id,propietario_id)`
- `CONSTRAINT espacio_portada_galeria_fk FOREIGN KEY (id, propietario_id, portada_foto_id) REFERENCES public.espacio_galeria_sintetica_local(espacio_id, propietario_id, id) ON DELETE RESTRICT`
- `CONSTRAINT espacio_estado_local_publication_ck CHECK (estado IN ('borrador','activa','oculta','eliminada'))`
- `CONSTRAINT espacio_public_location_all_or_none_ck CHECK ( (ubicacion_catalogo_version IS NULL AND region_codigo IS NULL AND comuna_codigo IS NULL) OR (ubicacion_catalogo_version IS NOT NULL AND region_codigo IS NOT NULL AND comuna_codigo IS NOT NULL) )`
- `CONSTRAINT espacio_public_region_fk FOREIGN KEY (ubicacion_catalogo_version, region_codigo) REFERENCES public.region_publica(catalogo_version, codigo)`
- `CONSTRAINT espacio_public_commune_fk FOREIGN KEY (ubicacion_catalogo_version, region_codigo, comuna_codigo) REFERENCES public.comuna_publica(catalogo_version, region_codigo, codigo)`
- `CONSTRAINT espacio_portada_media_fk FOREIGN KEY (id,propietario_id,portada_media_id) REFERENCES public.space_media(espacio_id,propietario_id,id) ON DELETE RESTRICT`
- `CONSTRAINT espacio_single_cover_ck CHECK (portada_foto_id IS NULL OR portada_media_id IS NULL)`


### B.057 Tabla `public.espacio_caracteristicas`
- **Migración de creación:** `V000006`
- **Atributos:** 5

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `espacio_id` | `uuid` | PK; FK → `public.espacio(espacio_id→id)`; FK → `public.espacio(espacio_id→id, categoria_codigo→categoria_codigo)` [espacio_caracteristicas_category_fk]; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `categoria_codigo` | `text` | FK → `public.categoria_perfil_atributos(categoria_codigo→categoria_codigo, perfil_version→version)` [anon_2]; FK → `public.espacio(espacio_id→id, categoria_codigo→categoria_codigo)` [espacio_caracteristicas_category_fk]; NOT NULL | Atributo `categoria_codigo`; el nombre y tipo se conservan según el DDL. |
| `perfil_version` | `integer` | FK → `public.categoria_perfil_atributos(categoria_codigo→categoria_codigo, perfil_version→version)` [anon_2]; NOT NULL | Atributo `perfil_version`; el nombre y tipo se conservan según el DDL. |
| `valores` | `jsonb` | DEFAULT `'{}'::jsonb`; NOT NULL | Atributo `valores`; el nombre y tipo se conservan según el DDL. |
| `actualizado_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de actualización del registro. |

**Restricciones DDL vigentes:**

- `CHECK (jsonb_typeof(valores) = 'object' AND octet_length(valores::text) <= 16384)`
- `FOREIGN KEY (categoria_codigo, perfil_version) REFERENCES public.categoria_perfil_atributos(categoria_codigo, version) ON DELETE RESTRICT`
- `CONSTRAINT espacio_caracteristicas_category_fk FOREIGN KEY (espacio_id, categoria_codigo) REFERENCES public.espacio(id, categoria_codigo) ON DELETE CASCADE`


### B.058 Tabla `public.espacio_eliminacion_historial_local`
- **Migración de creación:** `V000050`
- **Atributos:** 8

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `bigint` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `espacio_id` | `uuid` | UQ; FK → `public.espacio(espacio_id→id)`; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NOT NULL | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `ocurrida_en` | `timestamptz` | NOT NULL | Atributo `ocurrida_en`; el nombre y tipo se conservan según el DDL. |
| `correlacion_id` | `text` | NOT NULL | Atributo `correlacion_id`; el nombre y tipo se conservan según el DDL. |
| `archivos_pendientes` | `integer` | NOT NULL | Atributo `archivos_pendientes`; el nombre y tipo se conservan según el DDL. |
| `resumen` | `jsonb` | NOT NULL | Atributo `resumen`; el nombre y tipo se conservan según el DDL. |
| `retirar_en` | `timestamptz` | NULL permitido | Atributo `retirar_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (length(btrim(correlacion_id)) BETWEEN 1 AND 120)`
- `CHECK (archivos_pendientes >= 0)`
- `CHECK (
      jsonb_typeof(resumen)='object'
      AND resumen ? 'removed'
      AND resumen ? 'preserved'
    )`
- `UNIQUE (espacio_id)`


### B.059 Tabla `public.espacio_galeria_archivo_candidato_local`
- **Migración de creación:** `V000033`
- **Atributos:** 8

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `archivo_id` | `uuid` | PK; NOT NULL | Atributo `archivo_id`; el nombre y tipo se conservan según el DDL. |
| `propietario_id` | `uuid` | FK → `public.espacio(espacio_id→id, propietario_id→propietario_id)` [espacio_galeria_candidato_owner_fk]; NOT NULL | Atributo `propietario_id`; el nombre y tipo se conservan según el DDL. |
| `espacio_id` | `uuid` | FK → `public.espacio(espacio_id→id, propietario_id→propietario_id)` [espacio_galeria_candidato_owner_fk]; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `proximo_intento_en` | `timestamptz` | NULL permitido | Atributo `proximo_intento_en`; el nombre y tipo se conservan según el DDL. |
| `intentos_limpieza` | `integer` | DEFAULT `0`; NOT NULL | Atributo `intentos_limpieza`; el nombre y tipo se conservan según el DDL. |
| `ultimo_codigo_error` | `text` | NULL permitido | Atributo `ultimo_codigo_error`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (estado IN ('reservado','pendiente_limpieza','limpiando'))`
- `CHECK (intentos_limpieza >= 0)`
- `CONSTRAINT espacio_galeria_candidato_owner_fk FOREIGN KEY (espacio_id,propietario_id) REFERENCES public.espacio(id,propietario_id) ON DELETE RESTRICT`
- `CONSTRAINT espacio_galeria_candidato_state_ck CHECK ( (estado='reservado' AND proximo_intento_en IS NULL) OR (estado IN ('pendiente_limpieza','limpiando') AND proximo_intento_en IS NOT NULL) )`


### B.060 Tabla `public.espacio_galeria_sintetica_local`
- **Migración de creación:** `V000032`
- **Atributos:** 17

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; UQ compuesta (espacio_id, propietario_id, id); NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `espacio_id` | `uuid` | UQ compuesta (espacio_id, propietario_id, clave_idempotencia); UQ compuesta (espacio_id, propietario_id, id); FK → `public.espacio(espacio_id→id, propietario_id→propietario_id)` [espacio_galeria_sintetica_owner_fk]; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `propietario_id` | `uuid` | UQ compuesta (espacio_id, propietario_id, clave_idempotencia); UQ compuesta (espacio_id, propietario_id, id); FK → `public.espacio(espacio_id→id, propietario_id→propietario_id)` [espacio_galeria_sintetica_owner_fk]; NOT NULL | Atributo `propietario_id`; el nombre y tipo se conservan según el DDL. |
| `archivo_id` | `uuid` | UQ; NULL permitido | Atributo `archivo_id`; el nombre y tipo se conservan según el DDL. |
| `fixture_code` | `text` | NOT NULL | Atributo `fixture_code`; el nombre y tipo se conservan según el DDL. |
| `mime_type` | `text` | NOT NULL | Atributo `mime_type`; el nombre y tipo se conservan según el DDL. |
| `sha256` | `char(64)` | NOT NULL | Atributo `sha256`; el nombre y tipo se conservan según el DDL. |
| `size_bytes` | `bigint` | NOT NULL | Atributo `size_bytes`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `retirada_en` | `timestamptz` | NULL permitido | Atributo `retirada_en`; el nombre y tipo se conservan según el DDL. |
| `proximo_intento_en` | `timestamptz` | NULL permitido | Atributo `proximo_intento_en`; el nombre y tipo se conservan según el DDL. |
| `limpia_en` | `timestamptz` | NULL permitido | Atributo `limpia_en`; el nombre y tipo se conservan según el DDL. |
| `intentos_limpieza` | `integer` | DEFAULT `0`; NOT NULL | Atributo `intentos_limpieza`; el nombre y tipo se conservan según el DDL. |
| `ultimo_codigo_error` | `text` | NULL permitido | Atributo `ultimo_codigo_error`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (espacio_id, propietario_id, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `publicada_en_catalogo` | `boolean` | DEFAULT `false`; NOT NULL | Atributo `publicada_en_catalogo`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (fixture_code='synthetic-png-v1')`
- `CHECK (mime_type='image/png')`
- `CHECK (sha256 ~ '^[0-9a-f]{64}$')`
- `CHECK (size_bytes BETWEEN 1 AND 1048576)`
- `CHECK (estado IN ('activa','retirada','retirada_baja'))`
- `CHECK (intentos_limpieza >= 0)`
- `CHECK (length(btrim(clave_idempotencia)) BETWEEN 8 AND 128)`
- `CONSTRAINT espacio_galeria_sintetica_owner_fk FOREIGN KEY (espacio_id,propietario_id) REFERENCES public.espacio(id,propietario_id) ON DELETE RESTRICT`
- `CONSTRAINT espacio_galeria_sintetica_file_ck CHECK ((archivo_id IS NULL) = (limpia_en IS NOT NULL))`
- `CONSTRAINT espacio_galeria_sintetica_state_ck CHECK ( (estado='activa' AND retirada_en IS NULL) OR (estado IN ('retirada','retirada_baja') AND retirada_en IS NOT NULL) )`
- `CONSTRAINT espacio_galeria_sintetica_cleanup_ck CHECK ( (estado='activa' AND proximo_intento_en IS NULL) OR (estado<>'activa' AND (archivo_id IS NULL OR proximo_intento_en IS NOT NULL)) )`
- `UNIQUE (espacio_id,propietario_id,clave_idempotencia)`
- `CONSTRAINT espacio_galeria_cover_owner_uq UNIQUE (espacio_id, propietario_id, id)`


### B.061 Tabla `public.espacio_horario_semanal`
- **Migración de creación:** `V000019`
- **Atributos:** 3

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `espacio_id` | `uuid` | PK; FK → `public.espacio(espacio_id→id)`; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `activo` | `boolean` | DEFAULT `false`; NOT NULL | Atributo `activo`; el nombre y tipo se conservan según el DDL. |
| `actualizado_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de actualización del registro. |


### B.062 Tabla `public.espacio_horario_semanal_tramo`
- **Migración de creación:** `V000019`
- **Atributos:** 5

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `espacio_id` | `uuid` | PK compuesta (espacio_id, dia_iso, orden); FK → `public.espacio_horario_semanal(espacio_id→espacio_id)`; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `dia_iso` | `smallint` | PK compuesta (espacio_id, dia_iso, orden); NOT NULL | Atributo `dia_iso`; el nombre y tipo se conservan según el DDL. |
| `orden` | `smallint` | PK compuesta (espacio_id, dia_iso, orden); NOT NULL | Atributo `orden`; el nombre y tipo se conservan según el DDL. |
| `apertura_minuto` | `smallint` | NOT NULL | Atributo `apertura_minuto`; el nombre y tipo se conservan según el DDL. |
| `cierre_minuto` | `smallint` | NOT NULL | Atributo `cierre_minuto`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (dia_iso BETWEEN 1 AND 7)`
- `CHECK (orden BETWEEN 1 AND 2)`
- `CHECK (apertura_minuto BETWEEN 0 AND 1439)`
- `CHECK (cierre_minuto BETWEEN 1 AND 1440)`
- `PRIMARY KEY (espacio_id,dia_iso,orden)`
- `CHECK (cierre_minuto > apertura_minuto)`
- `EXCLUDE USING gist ( espacio_id WITH =, dia_iso WITH =, int4range(apertura_minuto,cierre_minuto,'[)') WITH && )`


### B.063 Tabla `public.espacio_publicacion_historial_local`
- **Migración de creación:** `V000031`
- **Atributos:** 8

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `bigint` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `espacio_id` | `uuid` | FK → `public.espacio(espacio_id→id)`; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NOT NULL | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `estado_anterior` | `text` | NOT NULL | Atributo `estado_anterior`; el nombre y tipo se conservan según el DDL. |
| `estado_nuevo` | `text` | NOT NULL | Atributo `estado_nuevo`; el nombre y tipo se conservan según el DDL. |
| `ocurrida_en` | `timestamptz` | NOT NULL | Atributo `ocurrida_en`; el nombre y tipo se conservan según el DDL. |
| `correlacion_id` | `text` | NOT NULL | Atributo `correlacion_id`; el nombre y tipo se conservan según el DDL. |
| `retirar_en` | `timestamptz` | NULL permitido | Atributo `retirar_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (estado_anterior IN ('borrador','activa','oculta'))`
- `CHECK (estado_nuevo IN ('activa','oculta'))`
- `CHECK (length(btrim(correlacion_id)) BETWEEN 1 AND 120)`
- `CONSTRAINT espacio_publicacion_transicion_ck CHECK ( (estado_anterior IN ('borrador','oculta') AND estado_nuevo='activa') OR (estado_anterior='activa' AND estado_nuevo='oculta') )`


### B.064 Tabla `public.tarifa_espacio`
- **Migración de creación:** `V000010`
- **Atributos:** 6

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `espacio_id` | `uuid` | PK compuesta (espacio_id, version); FK → `public.espacio(espacio_id→id)`; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `version` | `integer` | PK compuesta (espacio_id, version); NOT NULL | Atributo `version`; el nombre y tipo se conservan según el DDL. |
| `modalidad` | `text` | NOT NULL | Atributo `modalidad`; el nombre y tipo se conservan según el DDL. |
| `precio_base_clp` | `bigint` | NOT NULL | Atributo `precio_base_clp`; el nombre y tipo se conservan según el DDL. |
| `moneda` | `char(3)` | DEFAULT `'CLP'`; NOT NULL | Atributo `moneda`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de creación del registro. |

**Restricciones DDL vigentes:**

- `CHECK (version > 0)`
- `CHECK (modalidad IN ('hora', 'dia', 'mes'))`
- `CHECK (precio_base_clp > 5000)`
- `CHECK (moneda = 'CLP')`
- `PRIMARY KEY (espacio_id, version)`


## Dominio: Contratación digital

### B.065 Tabla `public.contrato_ensayo_firma`
- **Migración de creación:** `V000034`
- **Atributos:** 6

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `contrato_id` | `uuid` | PK compuesta (contrato_id, firmante_id); FK → `public.contrato_ensayo_local(contrato_id→id)`; NOT NULL | Atributo `contrato_id`; el nombre y tipo se conservan según el DDL. |
| `firmante_id` | `uuid` | PK compuesta (contrato_id, firmante_id); FK → `public.usuario(firmante_id→id)`; NOT NULL | Atributo `firmante_id`; el nombre y tipo se conservan según el DDL. |
| `rol` | `text` | NOT NULL | Atributo `rol`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `motivo` | `text` | DEFAULT `''`; NOT NULL | Atributo `motivo`; el nombre y tipo se conservan según el DDL. |
| `actualizada_en` | `timestamptz` | NOT NULL | Marca temporal de actualización del registro. |

**Restricciones DDL vigentes:**

- `CHECK (rol IN ('anfitrion','arrendatario'))`
- `CHECK (estado IN ('pendiente','firmada','rechazada'))`
- `PRIMARY KEY(contrato_id,firmante_id)`


### B.066 Tabla `public.contrato_ensayo_historial`
- **Migración de creación:** `V000034`
- **Atributos:** 7

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `contrato_id` | `uuid` | UQ compuesta (contrato_id, secuencia); FK → `public.contrato_ensayo_local(contrato_id→id)`; NOT NULL | Atributo `contrato_id`; el nombre y tipo se conservan según el DDL. |
| `secuencia` | `bigint` | UQ compuesta (contrato_id, secuencia); NOT NULL | Atributo `secuencia`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NULL permitido | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `accion` | `text` | NOT NULL | Atributo `accion`; el nombre y tipo se conservan según el DDL. |
| `motivo` | `text` | DEFAULT `''`; NOT NULL | Atributo `motivo`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |

**Restricciones DDL vigentes:**

- `CHECK(secuencia > 0)`
- `CHECK (accion IN ('generado','firmado','rechazado','firmado_completo','vencido','reserva_terminal','reserva_cancelada'))`
- `UNIQUE(contrato_id,secuencia)`


### B.067 Tabla `public.contrato_ensayo_local`
- **Migración de creación:** `V000034`
- **Atributos:** 11

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `reserva_id` | `uuid` | UQ; UQ compuesta (reserva_id, version); FK → `public.reserva_ensayo_local(reserva_id→id)`; NOT NULL | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `version` | `integer` | UQ compuesta (reserva_id, version); NOT NULL | Atributo `version`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `snapshot` | `jsonb` | NOT NULL | Atributo `snapshot`; el nombre y tipo se conservan según el DDL. |
| `documento_id` | `uuid` | UQ; FK → `public.documento_privado_sintetico_local(documento_id→id)`; NULL permitido | Atributo `documento_id`; el nombre y tipo se conservan según el DDL. |
| `sha256` | `bytea` | NOT NULL | Atributo `sha256`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `actualizada_en` | `timestamptz` | NOT NULL | Marca temporal de actualización del registro. |
| `firmado_en` | `timestamptz` | NULL permitido | Atributo `firmado_en`; el nombre y tipo se conservan según el DDL. |
| `pdf_retirado_en` | `timestamptz` | NULL permitido | Atributo `pdf_retirado_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (version > 0)`
- `CHECK (estado IN ('generado','firma_parcial','firmado','anulado'))`
- `CHECK (octet_length(sha256)=32)`
- `UNIQUE(reserva_id,version)`
- `CHECK ((estado='firmado') = (firmado_en IS NOT NULL))`
- `CONSTRAINT contrato_documento_retirado_ck CHECK ( (documento_id IS NOT NULL AND pdf_retirado_en IS NULL) OR (documento_id IS NULL AND pdf_retirado_en IS NOT NULL) )`


## Dominio: Reservas, disponibilidad y agendas

### B.068 Tabla `public.cotizacion_reserva_ensayo`
- **Migración de creación:** `V000011`
- **Atributos:** 26

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `espacio_id` | `uuid` | FK → `public.espacio(espacio_id→id)`; FK → `public.tarifa_espacio(espacio_id→espacio_id, tarifa_version→version)` [anon_9]; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `anfitrion_id` | `uuid` | FK → `public.usuario(anfitrion_id→id)`; NULL permitido | Atributo `anfitrion_id`; el nombre y tipo se conservan según el DDL. |
| `arrendatario_id` | `uuid` | FK → `public.usuario(arrendatario_id→id)`; NULL permitido | Atributo `arrendatario_id`; el nombre y tipo se conservan según el DDL. |
| `tarifa_version` | `integer` | FK → `public.tarifa_espacio(espacio_id→espacio_id, tarifa_version→version)` [anon_9]; NOT NULL | Versión asociada a la tarifa; no representa por sí misma un monto. |
| `modalidad` | `text` | NOT NULL | Atributo `modalidad`; el nombre y tipo se conservan según el DDL. |
| `precio_unitario_clp` | `bigint` | NOT NULL | Atributo `precio_unitario_clp`; el nombre y tipo se conservan según el DDL. |
| `moneda` | `char(3)` | NOT NULL | Atributo `moneda`; el nombre y tipo se conservan según el DDL. |
| `unidades` | `bigint` | NOT NULL | Atributo `unidades`; el nombre y tipo se conservan según el DDL. |
| `subtotal_clp` | `bigint` | NOT NULL | Atributo `subtotal_clp`; el nombre y tipo se conservan según el DDL. |
| `inicio` | `timestamptz` | NOT NULL | Atributo `inicio`; el nombre y tipo se conservan según el DDL. |
| `termino` | `timestamptz` | NOT NULL | Atributo `termino`; el nombre y tipo se conservan según el DDL. |
| `zona_horaria` | `text` | NOT NULL | Atributo `zona_horaria`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `vence_en` | `timestamptz` | NOT NULL | Atributo `vence_en`; el nombre y tipo se conservan según el DDL. |
| `condiciones_snapshot` | `text` | NOT NULL | Atributo `condiciones_snapshot`; el nombre y tipo se conservan según el DDL. |
| `categoria_codigo` | `text` | FK → `public.categoria_perfil_atributos(categoria_codigo→categoria_codigo, perfil_version→version)` [cotizacion_ensayo_perfil_fk]; NOT NULL | Atributo `categoria_codigo`; el nombre y tipo se conservan según el DDL. |
| `perfil_version` | `integer` | FK → `public.categoria_perfil_atributos(categoria_codigo→categoria_codigo, perfil_version→version)` [cotizacion_ensayo_perfil_fk]; NOT NULL | Atributo `perfil_version`; el nombre y tipo se conservan según el DDL. |
| `perfil_valores_snapshot` | `jsonb` | DEFAULT `'{}'::jsonb`; NOT NULL | Atributo `perfil_valores_snapshot`; el nombre y tipo se conservan según el DDL. |
| `politica_cancelacion_version` | `text` | DEFAULT `'local_flexible_v1'`; NOT NULL | Atributo `politica_cancelacion_version`; el nombre y tipo se conservan según el DDL. |
| `retirar_en` | `timestamptz` | NULL permitido | Atributo `retirar_en`; el nombre y tipo se conservan según el DDL. |
| `garantia_politica_version` | `text` | NULL permitido | Atributo `garantia_politica_version`; el nombre y tipo se conservan según el DDL. |
| `garantia_moneda` | `char(3)` | NULL permitido | Atributo `garantia_moneda`; el nombre y tipo se conservan según el DDL. |
| `garantia_prevista_clp` | `numeric(14,0)` | NULL permitido | Atributo `garantia_prevista_clp`; el nombre y tipo se conservan según el DDL. |
| `liquidacion_politica_version` | `text` | NULL permitido | Atributo `liquidacion_politica_version`; el nombre y tipo se conservan según el DDL. |
| `liquidacion_comision_bps` | `integer` | NULL permitido | Atributo `liquidacion_comision_bps`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (modalidad IN ('hora','dia','mes'))`
- `CHECK (precio_unitario_clp > 5000)`
- `CHECK (moneda='CLP')`
- `CHECK (unidades > 0)`
- `CHECK (subtotal_clp > 0)`
- `CHECK (termino > inicio)`
- `CHECK (length(btrim(zona_horaria)) BETWEEN 1 AND 100)`
- `CHECK (vence_en > creada_en)`
- `FOREIGN KEY (espacio_id, tarifa_version) REFERENCES public.tarifa_espacio(espacio_id,version) ON DELETE RESTRICT`
- `CONSTRAINT cotizacion_ensayo_perfil_fk FOREIGN KEY (categoria_codigo,perfil_version) REFERENCES public.categoria_perfil_atributos(categoria_codigo,version) ON DELETE RESTRICT`
- `CONSTRAINT cotizacion_ensayo_snapshot_object_ck CHECK (jsonb_typeof(perfil_valores_snapshot)='object' AND octet_length(perfil_valores_snapshot::text)<=16384)`
- `CONSTRAINT cotizacion_reserva_garantia_snapshot_ck CHECK ( (garantia_politica_version IS NULL AND garantia_moneda IS NULL AND garantia_prevista_clp IS NULL) OR (garantia_politica_version = 'garantia_local_fija_v1' AND garantia_moneda = 'CLP' AND garantia_prevista_clp = 50000) )`
- `CONSTRAINT cotizacion_reserva_liquidacion_snapshot_ck CHECK ( (liquidacion_politica_version IS NULL AND liquidacion_comision_bps IS NULL) OR (liquidacion_politica_version='liquidacion_local_0pct_v1' AND liquidacion_comision_bps=0) )`


### B.069 Tabla `public.mensaje_reserva_ensayo`
- **Migración de creación:** `V000016`
- **Atributos:** 8

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `secuencia` | `bigint` | PK; NOT NULL | Atributo `secuencia`; el nombre y tipo se conservan según el DDL. |
| `id` | `uuid` | UQ; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `reserva_id` | `uuid` | UQ compuesta (reserva_id, autor_id, clave_idempotencia); FK → `public.reserva_ensayo_local(reserva_id→id)`; NOT NULL | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `autor_id` | `uuid` | UQ compuesta (reserva_id, autor_id, clave_idempotencia); FK → `public.usuario(autor_id→id)`; NULL permitido | Atributo `autor_id`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (reserva_id, autor_id, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `huella_solicitud` | `bytea` | NOT NULL | Atributo `huella_solicitud`; el nombre y tipo se conservan según el DDL. |
| `cuerpo` | `text` | NOT NULL | Atributo `cuerpo`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |

**Restricciones DDL vigentes:**

- `CHECK (length(btrim(clave_idempotencia)) BETWEEN 1 AND 200)`
- `CHECK (octet_length(huella_solicitud) = 32)`
- `CHECK (char_length(cuerpo) BETWEEN 1 AND 2000 AND length(btrim(cuerpo)) > 0)`
- `UNIQUE (reserva_id, autor_id, clave_idempotencia)`


### B.070 Tabla `public.ocupacion`
- **Migración de creación:** `V000009`
- **Atributos:** 10

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `espacio_id` | `uuid` | FK → `public.espacio(espacio_id→id)`; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `reserva_id` | `uuid` | UQ; FK → `public.reserva_ensayo_local(reserva_id→id)` [ocupacion_reserva_ensayo_fk]; NULL permitido | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `intervalo` | `tstzrange` | NOT NULL | Intervalo temporal; consulte el tipo y las restricciones declaradas. |
| `tipo` | `text` | NOT NULL | Atributo `tipo`; el nombre y tipo se conservan según el DDL. |
| `activo` | `boolean` | DEFAULT `true`; NOT NULL | Atributo `activo`; el nombre y tipo se conservan según el DDL. |
| `expira_en` | `timestamptz` | NULL permitido | Atributo `expira_en`; el nombre y tipo se conservan según el DDL. |
| `motivo` | `text` | NULL permitido | Atributo `motivo`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de creación del registro. |
| `desactivada_en` | `timestamptz` | NULL permitido | Atributo `desactivada_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (tipo IN ('retencion', 'reserva', 'bloqueo_manual'))`
- `CONSTRAINT ocupacion_intervalo_ck CHECK ( NOT isempty(intervalo) AND NOT lower_inf(intervalo) AND NOT upper_inf(intervalo) AND lower_inc(intervalo) AND NOT upper_inc(intervalo) AND lower(intervalo) < upper(intervalo) )`
- `CONSTRAINT ocupacion_tipo_reserva_ck CHECK ( (tipo = 'bloqueo_manual' AND reserva_id IS NULL AND expira_en IS NULL AND motivo IS NOT NULL AND length(btrim(motivo)) BETWEEN 1 AND 500) OR (tipo IN ('retencion', 'reserva') AND reserva_id IS NOT NULL AND (tipo <> 'retencion' OR expira_en IS NOT NULL)) )`
- `CONSTRAINT ocupacion_desactivacion_ck CHECK ( (activo AND desactivada_en IS NULL) OR (NOT activo AND desactivada_en IS NOT NULL) )`
- `CONSTRAINT ocupacion_reserva_id_uk UNIQUE (reserva_id)`
- `CONSTRAINT ocupacion_no_solapa_excl EXCLUDE USING gist (espacio_id WITH =, intervalo WITH &&) WHERE (activo)`
- `CONSTRAINT ocupacion_reserva_ensayo_fk FOREIGN KEY (reserva_id) REFERENCES public.reserva_ensayo_local(id) ON DELETE RESTRICT DEFERRABLE INITIALLY DEFERRED`


### B.071 Tabla `public.reserva_cancelacion_ensayo`
- **Migración de creación:** `V000020`
- **Atributos:** 7

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `reserva_id` | `uuid` | UQ; UQ compuesta (reserva_id, clave_idempotencia); FK → `public.reserva_ensayo_local(reserva_id→id)`; NOT NULL | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `arrendatario_id` | `uuid` | FK → `public.usuario(arrendatario_id→id)`; NULL permitido | Atributo `arrendatario_id`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (reserva_id, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `huella_solicitud` | `bytea` | NOT NULL | Atributo `huella_solicitud`; el nombre y tipo se conservan según el DDL. |
| `motivo` | `text` | DEFAULT `''`; NOT NULL | Atributo `motivo`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |

**Restricciones DDL vigentes:**

- `CHECK (length(btrim(clave_idempotencia)) BETWEEN 1 AND 200)`
- `CHECK (octet_length(huella_solicitud) = 32)`
- `UNIQUE (reserva_id, clave_idempotencia)`


### B.072 Tabla `public.reserva_comprobante_ensayo_local`
- **Migración de creación:** `V000044`
- **Atributos:** 5

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `liquidacion_id` | `uuid` | UQ; FK → `public.reserva_liquidacion_ensayo_local(liquidacion_id→id)`; NOT NULL | Atributo `liquidacion_id`; el nombre y tipo se conservan según el DDL. |
| `version` | `smallint` | NOT NULL | Atributo `version`; el nombre y tipo se conservan según el DDL. |
| `contenido` | `jsonb` | NOT NULL | Atributo `contenido`; el nombre y tipo se conservan según el DDL. |
| `emitido_en` | `timestamptz` | NOT NULL | Atributo `emitido_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (version=1)`
- `CHECK (contenido->>'kind'='comprobante_ensayo'
      AND contenido->>'banner'='ENSAYO LOCAL — SIN VALIDEZ FISCAL — SIN MOVIMIENTOS REALES')`


### B.073 Tabla `public.reserva_decision_financiera_ensayo_local`
- **Migración de creación:** `V000040`
- **Atributos:** 14

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; DEFAULT `gen_random_uuid()`; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `garantia_id` | `uuid` | UQ; FK → `public.reserva_garantia_ensayo_local(garantia_id→id)`; NOT NULL | Atributo `garantia_id`; el nombre y tipo se conservan según el DDL. |
| `reserva_id` | `uuid` | UQ compuesta (reserva_id, clave_idempotencia); FK → `public.reserva_ensayo_local(reserva_id→id)`; NOT NULL | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `reclamo_id` | `uuid` | FK → `public.reclamo_dano_ensayo_local(reclamo_id→id)`; NULL permitido | Atributo `reclamo_id`; el nombre y tipo se conservan según el DDL. |
| `resultado_reclamo` | `text` | NOT NULL | Atributo `resultado_reclamo`; el nombre y tipo se conservan según el DDL. |
| `deduccion_clp` | `numeric(14,0)` | NOT NULL | Atributo `deduccion_clp`; el nombre y tipo se conservan según el DDL. |
| `motivo_codigo` | `text` | NOT NULL | Atributo `motivo_codigo`; el nombre y tipo se conservan según el DDL. |
| `evidencia_id` | `uuid` | FK → `public.operacion_arriendo_evidencia_ensayo_local(evidencia_id→id)`; NULL permitido | Atributo `evidencia_id`; el nombre y tipo se conservan según el DDL. |
| `administrador_id` | `uuid` | FK → `public.usuario(administrador_id→id)`; NOT NULL | Atributo `administrador_id`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (reserva_id, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `huella_solicitud` | `bytea` | NOT NULL | Atributo `huella_solicitud`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `actualizada_en` | `timestamptz` | NOT NULL | Marca temporal de actualización del registro. |

**Restricciones DDL vigentes:**

- `CHECK (resultado_reclamo IN ('acogido','rechazado'))`
- `CHECK (deduccion_clp >= 0)`
- `CHECK (motivo_codigo IN ('dano_acreditado','faltante_acreditado','sin_deduccion'))`
- `CHECK (length(clave_idempotencia) BETWEEN 1 AND 200)`
- `CHECK (octet_length(huella_solicitud) = 32)`
- `CHECK (estado IN ('pendiente','por_conciliar','aplicada','sin_deduccion'))`
- `UNIQUE (reserva_id, clave_idempotencia)`
- `CHECK ((deduccion_clp = 0 AND motivo_codigo = 'sin_deduccion' AND evidencia_id IS NULL) OR (deduccion_clp > 0 AND motivo_codigo IN ('dano_acreditado','faltante_acreditado') AND evidencia_id IS NOT NULL))`
- `CHECK (reclamo_id IS NOT NULL)`
- `CHECK (resultado_reclamo <> 'rechazado' OR deduccion_clp = 0)`


### B.074 Tabla `public.reserva_devolucion_ensayo`
- **Migración de creación:** `V000020`
- **Atributos:** 10

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `reserva_id` | `uuid` | UQ; FK → `public.reserva_ensayo_local(reserva_id→id)`; NOT NULL | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `operacion_id` | `uuid` | UQ; NOT NULL | Atributo `operacion_id`; el nombre y tipo se conservan según el DDL. |
| `importe_clp` | `bigint` | NOT NULL | Atributo `importe_clp`; el nombre y tipo se conservan según el DDL. |
| `moneda` | `char(3)` | NOT NULL | Atributo `moneda`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `ultimo_resultado` | `text` | NULL permitido | Atributo `ultimo_resultado`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `actualizada_en` | `timestamptz` | NOT NULL | Marca temporal de actualización del registro. |
| `completada_en` | `timestamptz` | NULL permitido | Atributo `completada_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (importe_clp > 0)`
- `CHECK (moneda = 'CLP')`
- `CHECK (estado IN ('pendiente', 'completada'))`
- `CHECK (ultimo_resultado IN ('exito_simulado', 'fallo_simulado', 'sin_respuesta_simulada'))`
- `CHECK ((estado = 'completada') = (completada_en IS NOT NULL))`


### B.075 Tabla `public.reserva_devolucion_intento_ensayo`
- **Migración de creación:** `V000020`
- **Atributos:** 5

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `devolucion_id` | `uuid` | UQ compuesta (devolucion_id, secuencia); FK → `public.reserva_devolucion_ensayo(devolucion_id→id)`; NOT NULL | Atributo `devolucion_id`; el nombre y tipo se conservan según el DDL. |
| `secuencia` | `bigint` | UQ compuesta (devolucion_id, secuencia); NOT NULL | Atributo `secuencia`; el nombre y tipo se conservan según el DDL. |
| `resultado` | `text` | NOT NULL | Atributo `resultado`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |

**Restricciones DDL vigentes:**

- `CHECK (secuencia > 0)`
- `CHECK (resultado IN ('exito_simulado', 'fallo_simulado', 'sin_respuesta_simulada'))`
- `UNIQUE (devolucion_id, secuencia)`


### B.076 Tabla `public.reserva_ensayo_local`
- **Migración de creación:** `V000011`
- **Atributos:** 29

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `cotizacion_id` | `uuid` | UQ; FK → `public.cotizacion_reserva_ensayo(cotizacion_id→id)`; NOT NULL | Atributo `cotizacion_id`; el nombre y tipo se conservan según el DDL. |
| `espacio_id` | `uuid` | FK → `public.espacio(espacio_id→id)`; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `anfitrion_id` | `uuid` | FK → `public.usuario(anfitrion_id→id)`; NULL permitido | Atributo `anfitrion_id`; el nombre y tipo se conservan según el DDL. |
| `arrendatario_id` | `uuid` | UQ compuesta (arrendatario_id, clave_idempotencia); FK → `public.usuario(arrendatario_id→id)`; NULL permitido | Atributo `arrendatario_id`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (arrendatario_id, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `huella_solicitud` | `bytea` | NOT NULL | Atributo `huella_solicitud`; el nombre y tipo se conservan según el DDL. |
| `ocupacion_id` | `uuid` | UQ; FK → `public.ocupacion(ocupacion_id→id)` [reserva_ensayo_ocupacion_fk]; NOT NULL | Atributo `ocupacion_id`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `precio_unitario_clp` | `bigint` | NOT NULL | Atributo `precio_unitario_clp`; el nombre y tipo se conservan según el DDL. |
| `unidades` | `bigint` | NOT NULL | Atributo `unidades`; el nombre y tipo se conservan según el DDL. |
| `subtotal_clp` | `bigint` | NOT NULL | Atributo `subtotal_clp`; el nombre y tipo se conservan según el DDL. |
| `modalidad` | `text` | NOT NULL | Atributo `modalidad`; el nombre y tipo se conservan según el DDL. |
| `moneda` | `char(3)` | NOT NULL | Atributo `moneda`; el nombre y tipo se conservan según el DDL. |
| `inicio` | `timestamptz` | NOT NULL | Atributo `inicio`; el nombre y tipo se conservan según el DDL. |
| `termino` | `timestamptz` | NOT NULL | Atributo `termino`; el nombre y tipo se conservan según el DDL. |
| `zona_horaria` | `text` | NOT NULL | Atributo `zona_horaria`; el nombre y tipo se conservan según el DDL. |
| `pago_vence_en` | `timestamptz` | NOT NULL | Atributo `pago_vence_en`; el nombre y tipo se conservan según el DDL. |
| `anfitrion_vence_en` | `timestamptz` | NULL permitido | Atributo `anfitrion_vence_en`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `actualizada_en` | `timestamptz` | NOT NULL | Marca temporal de actualización del registro. |
| `condiciones_snapshot` | `text` | NOT NULL | Atributo `condiciones_snapshot`; el nombre y tipo se conservan según el DDL. |
| `politica_cancelacion_version` | `text` | DEFAULT `'local_flexible_v1'`; NOT NULL | Atributo `politica_cancelacion_version`; el nombre y tipo se conservan según el DDL. |
| `vinculos_retirar_en` | `timestamptz` | NULL permitido | Atributo `vinculos_retirar_en`; el nombre y tipo se conservan según el DDL. |
| `garantia_politica_version` | `text` | NULL permitido | Atributo `garantia_politica_version`; el nombre y tipo se conservan según el DDL. |
| `garantia_moneda` | `char(3)` | NULL permitido | Atributo `garantia_moneda`; el nombre y tipo se conservan según el DDL. |
| `garantia_prevista_clp` | `numeric(14,0)` | NULL permitido | Atributo `garantia_prevista_clp`; el nombre y tipo se conservan según el DDL. |
| `liquidacion_politica_version` | `text` | NULL permitido | Atributo `liquidacion_politica_version`; el nombre y tipo se conservan según el DDL. |
| `liquidacion_comision_bps` | `integer` | NULL permitido | Atributo `liquidacion_comision_bps`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (length(btrim(clave_idempotencia)) BETWEEN 1 AND 200)`
- `CHECK (octet_length(huella_solicitud)=32)`
- `CHECK (moneda='CLP')`
- `CHECK (termino > inicio)`
- `UNIQUE(arrendatario_id,clave_idempotencia)`
- `CONSTRAINT reserva_ensayo_ocupacion_fk FOREIGN KEY (ocupacion_id) REFERENCES public.ocupacion(id) ON DELETE RESTRICT DEFERRABLE INITIALLY DEFERRED`
- `CONSTRAINT reserva_ensayo_garantia_snapshot_ck CHECK ( (garantia_politica_version IS NULL AND garantia_moneda IS NULL AND garantia_prevista_clp IS NULL) OR (garantia_politica_version = 'garantia_local_fija_v1' AND garantia_moneda = 'CLP' AND garantia_prevista_clp = 50000) )`
- `CONSTRAINT reserva_ensayo_liquidacion_snapshot_ck CHECK ( (liquidacion_politica_version IS NULL AND liquidacion_comision_bps IS NULL) OR (liquidacion_politica_version='liquidacion_local_0pct_v1' AND liquidacion_comision_bps=0) )`
- `CONSTRAINT reserva_ensayo_local_estado_check CHECK (estado IN ( 'pendiente_de_pago','pagada','aprobada_host','firma_parcial','lista_para_checkin', 'en_curso','finalizada','en_disputa','cerrada','cancelada_por_pago','rechazada_arrendador', 'vencida_pago','vencida_host','cancelada_arrendatario','cancelada_por_firma' ))`


### B.077 Tabla `public.reserva_ensayo_local_fixture`
- **Migración de creación:** `V000011`
- **Atributos:** 6

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `espacio_id` | `uuid` | PK; FK → `public.espacio(espacio_id→id)`; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `anfitrion_id` | `uuid` | FK → `public.usuario(anfitrion_id→id)`; NULL permitido | Atributo `anfitrion_id`; el nombre y tipo se conservan según el DDL. |
| `arrendatario_id` | `uuid` | FK → `public.usuario(arrendatario_id→id)`; NULL permitido | Atributo `arrendatario_id`; el nombre y tipo se conservan según el DDL. |
| `habilitada_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Atributo `habilitada_en`; el nombre y tipo se conservan según el DDL. |
| `habilitada` | `boolean` | DEFAULT `true`; NOT NULL | Atributo `habilitada`; el nombre y tipo se conservan según el DDL. |
| `politica_cancelacion_version` | `text` | DEFAULT `'local_flexible_v1'`; NOT NULL | Atributo `politica_cancelacion_version`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CONSTRAINT fixture_participantes_distintos_ck CHECK (anfitrion_id <> arrendatario_id)`
- `PRIMARY KEY (espacio_id)`


### B.078 Tabla `public.reserva_ensayo_local_ubicacion_sintetica`
- **Migración de creación:** `V000018`
- **Atributos:** 5

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `espacio_id` | `uuid` | PK; FK → `public.reserva_ensayo_local_fixture(espacio_id→espacio_id)`; NOT NULL | Atributo `espacio_id`; el nombre y tipo se conservan según el DDL. |
| `latitud` | `double precision` | NOT NULL | Atributo `latitud`; el nombre y tipo se conservan según el DDL. |
| `longitud` | `double precision` | NOT NULL | Atributo `longitud`; el nombre y tipo se conservan según el DDL. |
| `punto` | `geography(Point,4326)` | NULL permitido | Atributo `punto`; el nombre y tipo se conservan según el DDL. |
| `es_sintetica` | `boolean` | DEFAULT `true`; NOT NULL | Atributo `es_sintetica`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (latitud BETWEEN -90 AND 90)`
- `CHECK (longitud BETWEEN -180 AND 180)`
- `CHECK (es_sintetica)`


### B.079 Tabla `public.reserva_ensayo_transicion`
- **Migración de creación:** `V000011`
- **Atributos:** 8

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `reserva_id` | `uuid` | UQ compuesta (reserva_id, secuencia); FK → `public.reserva_ensayo_local(reserva_id→id)`; NOT NULL | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `estado_anterior` | `text` | NULL permitido | Atributo `estado_anterior`; el nombre y tipo se conservan según el DDL. |
| `estado_nuevo` | `text` | NOT NULL | Atributo `estado_nuevo`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NULL permitido | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `motivo` | `text` | NOT NULL | Atributo `motivo`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `secuencia` | `bigint` | UQ compuesta (reserva_id, secuencia); NOT NULL | Atributo `secuencia`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CONSTRAINT reserva_ensayo_transicion_secuencia_ck CHECK (secuencia > 0)`
- `CONSTRAINT reserva_ensayo_transicion_reserva_secuencia_uq UNIQUE (reserva_id, secuencia)`


### B.080 Tabla `public.reserva_finanzas_historial_ensayo_local`
- **Migración de creación:** `V000040`
- **Atributos:** 7

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; DEFAULT `gen_random_uuid()`; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `secuencia` | `bigserial` | UQ; NOT NULL | Atributo `secuencia`; el nombre y tipo se conservan según el DDL. |
| `reserva_id` | `uuid` | FK → `public.reserva_ensayo_local(reserva_id→id)`; NOT NULL | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `tipo` | `text` | NOT NULL | Atributo `tipo`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NULL permitido | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `detalle_codigo` | `text` | NOT NULL | Atributo `detalle_codigo`; el nombre y tipo se conservan según el DDL. |
| `ocurrida_en` | `timestamptz` | NOT NULL | Atributo `ocurrida_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CONSTRAINT reserva_finanzas_historial_ensayo_local_tipo_check CHECK (tipo IN ( 'garantia_solicitada','garantia_autorizada','garantia_rechazada','garantia_vencida','garantia_liberada','garantia_capturada', 'decision_financiera_registrada','operacion_pendiente_conciliacion', 'liquidacion_solicitada','liquidacion_confirmada','liquidacion_rechazada' ))`


### B.081 Tabla `public.reserva_garantia_ensayo_local`
- **Migración de creación:** `V000040`
- **Atributos:** 11

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; DEFAULT `gen_random_uuid()`; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `reserva_id` | `uuid` | UQ; FK → `public.reserva_ensayo_local(reserva_id→id)`; NOT NULL | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `politica_version` | `text` | NOT NULL | Atributo `politica_version`; el nombre y tipo se conservan según el DDL. |
| `moneda` | `char(3)` | NOT NULL | Atributo `moneda`; el nombre y tipo se conservan según el DDL. |
| `previsto_clp` | `numeric(14,0)` | NOT NULL | Atributo `previsto_clp`; el nombre y tipo se conservan según el DDL. |
| `autorizado_clp` | `numeric(14,0)` | DEFAULT `0`; NOT NULL | Atributo `autorizado_clp`; el nombre y tipo se conservan según el DDL. |
| `capturado_clp` | `numeric(14,0)` | DEFAULT `0`; NOT NULL | Atributo `capturado_clp`; el nombre y tipo se conservan según el DDL. |
| `liberado_clp` | `numeric(14,0)` | DEFAULT `0`; NOT NULL | Atributo `liberado_clp`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `actualizada_en` | `timestamptz` | NOT NULL | Marca temporal de actualización del registro. |

**Restricciones DDL vigentes:**

- `CHECK (politica_version = 'garantia_local_fija_v1')`
- `CHECK (moneda = 'CLP')`
- `CHECK (previsto_clp = 50000)`
- `CHECK (autorizado_clp >= 0)`
- `CHECK (capturado_clp >= 0)`
- `CHECK (liberado_clp >= 0)`
- `CHECK (estado IN (
        'pendiente_pago','pendiente_autorizacion','autorizada','no_disponible','por_conciliar',
        'captura_pendiente','captura_por_conciliar','parcialmente_capturada',
        'liberacion_pendiente','liberacion_por_conciliar','liberada','cancelada'
    ))`
- `CHECK (autorizado_clp <= previsto_clp)`
- `CHECK (capturado_clp + liberado_clp <= autorizado_clp)`


### B.082 Tabla `public.reserva_garantia_evento_aplicacion_ensayo_local`
- **Migración de creación:** `V000040`
- **Atributos:** 5

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `evento_id` | `uuid` | PK; FK → `public.reserva_garantia_evento_ensayo_local(evento_id→id)`; NOT NULL | Atributo `evento_id`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `codigo_resultado` | `text` | NULL permitido | Atributo `codigo_resultado`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `procesada_en` | `timestamptz` | NULL permitido | Atributo `procesada_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (estado IN ('pendiente','aplicada','por_conciliar','ignorada'))`


### B.083 Tabla `public.reserva_garantia_evento_ensayo_local`
- **Migración de creación:** `V000040`
- **Atributos:** 5

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; DEFAULT `gen_random_uuid()`; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `operacion_id` | `uuid` | UQ compuesta (operacion_id, evento_id); FK → `public.reserva_garantia_operacion_ensayo_local(operacion_id→id)`; NOT NULL | Atributo `operacion_id`; el nombre y tipo se conservan según el DDL. |
| `evento_id` | `text` | UQ; UQ compuesta (operacion_id, evento_id); NOT NULL | Atributo `evento_id`; el nombre y tipo se conservan según el DDL. |
| `resultado` | `text` | NOT NULL | Atributo `resultado`; el nombre y tipo se conservan según el DDL. |
| `autenticado_en` | `timestamptz` | NOT NULL | Atributo `autenticado_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (length(evento_id) BETWEEN 1 AND 200)`
- `CHECK (resultado IN ('exito_simulado','rechazo_simulado'))`
- `UNIQUE (operacion_id, evento_id)`


### B.084 Tabla `public.reserva_garantia_operacion_ensayo_local`
- **Migración de creación:** `V000040`
- **Atributos:** 14

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `garantia_id` | `uuid` | UQ compuesta (garantia_id, tipo); UQ compuesta (garantia_id, clave_idempotencia); FK → `public.reserva_garantia_ensayo_local(garantia_id→id)`; NOT NULL | Atributo `garantia_id`; el nombre y tipo se conservan según el DDL. |
| `tipo` | `text` | UQ compuesta (garantia_id, tipo); NOT NULL | Atributo `tipo`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (garantia_id, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `huella_solicitud` | `bytea` | NOT NULL | Atributo `huella_solicitud`; el nombre y tipo se conservan según el DDL. |
| `importe_clp` | `numeric(14,0)` | NOT NULL | Valor numérico de la magnitud indicada por el nombre de la columna. |
| `resultado_solicitado` | `text` | NOT NULL | Atributo `resultado_solicitado`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `primer_intento_en` | `timestamptz` | NOT NULL | Atributo `primer_intento_en`; el nombre y tipo se conservan según el DDL. |
| `vence_en` | `timestamptz` | NULL permitido | Atributo `vence_en`; el nombre y tipo se conservan según el DDL. |
| `ultimo_resultado` | `text` | NULL permitido | Atributo `ultimo_resultado`; el nombre y tipo se conservan según el DDL. |
| `completada_en` | `timestamptz` | NULL permitido | Atributo `completada_en`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `actualizada_en` | `timestamptz` | NOT NULL | Marca temporal de actualización del registro. |

**Restricciones DDL vigentes:**

- `CHECK (tipo IN ('autorizacion','captura','liberacion'))`
- `CHECK (length(clave_idempotencia) BETWEEN 1 AND 200)`
- `CHECK (octet_length(huella_solicitud) = 32)`
- `CHECK (importe_clp >= 0)`
- `CHECK (resultado_solicitado IN ('exito','rechazo','sin_respuesta'))`
- `CHECK (estado IN ('pendiente','por_conciliar','confirmada','rechazada','vencida'))`
- `UNIQUE (garantia_id, tipo)`
- `UNIQUE (garantia_id, clave_idempotencia)`
- `CHECK (ultimo_resultado IS NULL OR ultimo_resultado IN ('exito_simulado','rechazo_simulado','sin_respuesta_simulada','resultado_tardio','autorizacion_vencida','cancelada'))`


### B.085 Tabla `public.reserva_garantia_resultado_fake_ensayo_local`
- **Migración de creación:** `V000040`
- **Atributos:** 5

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; DEFAULT `gen_random_uuid()`; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `operacion_id` | `uuid` | UQ; FK → `public.reserva_garantia_operacion_ensayo_local(operacion_id→id)`; NOT NULL | Atributo `operacion_id`; el nombre y tipo se conservan según el DDL. |
| `evento_id` | `text` | UQ; NULL permitido | Atributo `evento_id`; el nombre y tipo se conservan según el DDL. |
| `resultado` | `text` | NOT NULL | Atributo `resultado`; el nombre y tipo se conservan según el DDL. |
| `registrada_en` | `timestamptz` | NOT NULL | Atributo `registrada_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (evento_id IS NULL OR length(evento_id) BETWEEN 1 AND 200)`
- `CHECK (resultado IN ('exito_simulado','rechazo_simulado','sin_respuesta_simulada'))`
- `CHECK ((resultado='sin_respuesta_simulada' AND evento_id IS NULL) OR (resultado IN ('exito_simulado','rechazo_simulado') AND evento_id IS NOT NULL))`


### B.086 Tabla `public.reserva_liquidacion_ensayo_local`
- **Migración de creación:** `V000044`
- **Atributos:** 17

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `reserva_id` | `uuid` | UQ; UQ compuesta (reserva_id, clave_idempotencia); FK → `public.reserva_ensayo_local(reserva_id→id)`; NOT NULL | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `anfitrion_id` | `uuid` | FK → `public.usuario(anfitrion_id→id)`; NULL permitido | Atributo `anfitrion_id`; el nombre y tipo se conservan según el DDL. |
| `politica_version` | `text` | NOT NULL | Atributo `politica_version`; el nombre y tipo se conservan según el DDL. |
| `moneda` | `char(3)` | NOT NULL | Atributo `moneda`; el nombre y tipo se conservan según el DDL. |
| `arriendo_confirmado_clp` | `bigint` | NOT NULL | Atributo `arriendo_confirmado_clp`; el nombre y tipo se conservan según el DDL. |
| `devoluciones_confirmadas_clp` | `bigint` | NOT NULL | Atributo `devoluciones_confirmadas_clp`; el nombre y tipo se conservan según el DDL. |
| `comision_bps` | `integer` | NOT NULL | Atributo `comision_bps`; el nombre y tipo se conservan según el DDL. |
| `comision_clp` | `bigint` | NOT NULL | Atributo `comision_clp`; el nombre y tipo se conservan según el DDL. |
| `transferencia_clp` | `bigint` | NOT NULL | Atributo `transferencia_clp`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `ultimo_resultado` | `text` | NULL permitido | Atributo `ultimo_resultado`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (reserva_id, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `huella_solicitud` | `bytea` | NOT NULL | Atributo `huella_solicitud`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `actualizada_en` | `timestamptz` | NOT NULL | Marca temporal de actualización del registro. |
| `completada_en` | `timestamptz` | NULL permitido | Atributo `completada_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (politica_version='liquidacion_local_0pct_v1')`
- `CHECK (moneda='CLP')`
- `CHECK (arriendo_confirmado_clp>=0)`
- `CHECK (devoluciones_confirmadas_clp>=0)`
- `CHECK (comision_bps BETWEEN 0 AND 10000)`
- `CHECK (comision_clp>=0)`
- `CHECK (transferencia_clp>=0)`
- `CHECK (estado IN ('pendiente','por_conciliar','liquidada','rechazada'))`
- `CHECK (ultimo_resultado IN ('exito_simulado','rechazo_simulado','sin_respuesta_simulada'))`
- `CHECK (length(btrim(clave_idempotencia)) BETWEEN 1 AND 200)`
- `CHECK (octet_length(huella_solicitud)=32)`
- `UNIQUE(reserva_id,clave_idempotencia)`
- `CHECK (transferencia_clp = arriendo_confirmado_clp - devoluciones_confirmadas_clp - comision_clp)`
- `CHECK ((estado IN ('liquidada','rechazada')) = (completada_en IS NOT NULL))`


### B.087 Tabla `public.reserva_liquidacion_historial_ensayo_local`
- **Migración de creación:** `V000044`
- **Atributos:** 6

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `secuencia` | `bigint` | PK; NOT NULL | Atributo `secuencia`; el nombre y tipo se conservan según el DDL. |
| `liquidacion_id` | `uuid` | FK → `public.reserva_liquidacion_ensayo_local(liquidacion_id→id)`; NOT NULL | Atributo `liquidacion_id`; el nombre y tipo se conservan según el DDL. |
| `accion` | `text` | NOT NULL | Atributo `accion`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NULL permitido | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `codigo` | `text` | NOT NULL | Atributo `codigo`; el nombre y tipo se conservan según el DDL. |
| `ocurrida_en` | `timestamptz` | NOT NULL | Atributo `ocurrida_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (accion IN ('liquidacion_solicitada','liquidacion_por_conciliar','liquidacion_confirmada','liquidacion_rechazada'))`


### B.088 Tabla `public.reserva_liquidacion_operacion_ensayo_local`
- **Migración de creación:** `V000044`
- **Atributos:** 5

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `liquidacion_id` | `uuid` | UQ; FK → `public.reserva_liquidacion_ensayo_local(liquidacion_id→id)`; NOT NULL | Atributo `liquidacion_id`; el nombre y tipo se conservan según el DDL. |
| `resultado_solicitado` | `text` | NOT NULL | Atributo `resultado_solicitado`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `actualizada_en` | `timestamptz` | NOT NULL | Marca temporal de actualización del registro. |

**Restricciones DDL vigentes:**

- `CHECK (resultado_solicitado IN ('exito','rechazo','sin_respuesta'))`


### B.089 Tabla `public.reserva_liquidacion_resultado_fake_ensayo_local`
- **Migración de creación:** `V000044`
- **Atributos:** 4

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `operacion_id` | `uuid` | PK; FK → `public.reserva_liquidacion_operacion_ensayo_local(operacion_id→id)`; NOT NULL | Atributo `operacion_id`; el nombre y tipo se conservan según el DDL. |
| `event_id` | `text` | UQ; NULL permitido | Atributo `event_id`; el nombre y tipo se conservan según el DDL. |
| `resultado` | `text` | NOT NULL | Atributo `resultado`; el nombre y tipo se conservan según el DDL. |
| `registrada_en` | `timestamptz` | NOT NULL | Atributo `registrada_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (event_id IS NULL OR length(event_id) BETWEEN 1 AND 200)`
- `CHECK (resultado IN ('exito_simulado','rechazo_simulado','sin_respuesta_simulada'))`
- `CHECK ((resultado='sin_respuesta_simulada' AND event_id IS NULL) OR (resultado IN ('exito_simulado','rechazo_simulado') AND event_id IS NOT NULL))`


### B.090 Tabla `public.reserva_mensaje_lectura`
- **Migración de creación:** `V000017`
- **Atributos:** 4

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `reserva_id` | `uuid` | PK compuesta (reserva_id, participante_id); FK → `public.reserva_ensayo_local(reserva_id→id)`; NOT NULL | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `participante_id` | `uuid` | PK compuesta (reserva_id, participante_id); FK → `public.usuario(participante_id→id)`; NOT NULL | Atributo `participante_id`; el nombre y tipo se conservan según el DDL. |
| `ultima_secuencia_leida` | `bigint` | NOT NULL | Atributo `ultima_secuencia_leida`; el nombre y tipo se conservan según el DDL. |
| `actualizada_en` | `timestamptz` | NOT NULL | Marca temporal de actualización del registro. |

**Restricciones DDL vigentes:**

- `CHECK (ultima_secuencia_leida > 0)`
- `PRIMARY KEY (reserva_id, participante_id)`


### B.091 Tabla `public.reserva_pago_ensayo`
- **Migración de creación:** `V000011`
- **Atributos:** 6

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `reserva_id` | `uuid` | UQ compuesta (reserva_id, clave_idempotencia); FK → `public.reserva_ensayo_local(reserva_id→id)`; NOT NULL | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `resultado` | `text` | NOT NULL | Atributo `resultado`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (reserva_id, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `importe_clp` | `bigint` | DEFAULT `0`; NOT NULL | Atributo `importe_clp`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (resultado IN ('exito_simulado','rechazo_simulado','sin_respuesta_simulada','devolucion_simulada'))`
- `CHECK(length(btrim(clave_idempotencia)) BETWEEN 1 AND 200)`
- `UNIQUE(reserva_id,clave_idempotencia)`
- `CHECK (importe_clp >= 0)`


### B.092 Tabla `public.reserva_pago_ensayo_operacion`
- **Migración de creación:** `V000021`
- **Atributos:** 10

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `reserva_id` | `uuid` | UQ compuesta (reserva_id, clave_idempotencia); FK → `public.reserva_ensayo_local(reserva_id→id)`; NOT NULL | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `arrendatario_id` | `uuid` | FK → `public.usuario(arrendatario_id→id)`; NULL permitido | Atributo `arrendatario_id`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (reserva_id, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `huella_solicitud` | `bytea` | NOT NULL | Atributo `huella_solicitud`; el nombre y tipo se conservan según el DDL. |
| `resultado_solicitado` | `text` | NOT NULL | Atributo `resultado_solicitado`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `resultado_final` | `text` | NULL permitido | Atributo `resultado_final`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `actualizada_en` | `timestamptz` | NOT NULL | Marca temporal de actualización del registro. |

**Restricciones DDL vigentes:**

- `CHECK (length(btrim(clave_idempotencia)) BETWEEN 1 AND 200)`
- `CHECK (octet_length(huella_solicitud) = 32)`
- `CHECK (resultado_solicitado IN ('exito','rechazo','sin_respuesta'))`
- `CHECK (estado IN ('pendiente','aplicada','vencida'))`
- `CHECK (resultado_final IN ('exito_simulado','rechazo_simulado'))`
- `UNIQUE (reserva_id, clave_idempotencia)`
- `CHECK ((estado = 'aplicada') = (resultado_final IS NOT NULL))`


### B.093 Tabla `public.reserva_pago_evento_aplicacion_ensayo`
- **Migración de creación:** `V000021`
- **Atributos:** 5

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `evento_id` | `uuid` | PK; FK → `public.reserva_pago_evento_ensayo(evento_id→id)`; NOT NULL | Atributo `evento_id`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `codigo_resultado` | `text` | NULL permitido | Atributo `codigo_resultado`; el nombre y tipo se conservan según el DDL. |
| `procesado_en` | `timestamptz` | NULL permitido | Atributo `procesado_en`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |

**Restricciones DDL vigentes:**

- `CHECK (estado IN ('pendiente','aplicada','ignorada','vencida','pendiente_conciliacion'))`
- `CHECK (codigo_resultado IN ('aplicado','operacion_terminal','reserva_vencida','resultado_tardio'))`
- `CHECK ((estado IN ('pendiente','pendiente_conciliacion')) = (procesado_en IS NULL))`


### B.094 Tabla `public.reserva_pago_evento_ensayo`
- **Migración de creación:** `V000021`
- **Atributos:** 7

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `operacion_id` | `uuid` | UQ compuesta (operacion_id, proveedor_evento_id); FK → `public.reserva_pago_ensayo_operacion(operacion_id→id)`; NOT NULL | Atributo `operacion_id`; el nombre y tipo se conservan según el DDL. |
| `proveedor_evento_id` | `text` | UQ; UQ compuesta (operacion_id, proveedor_evento_id); NOT NULL | Atributo `proveedor_evento_id`; el nombre y tipo se conservan según el DDL. |
| `resultado` | `text` | NOT NULL | Atributo `resultado`; el nombre y tipo se conservan según el DDL. |
| `huella_payload` | `bytea` | NOT NULL | Atributo `huella_payload`; el nombre y tipo se conservan según el DDL. |
| `autenticado_en` | `timestamptz` | NOT NULL | Atributo `autenticado_en`; el nombre y tipo se conservan según el DDL. |
| `recibido_en` | `timestamptz` | NOT NULL | Atributo `recibido_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (length(btrim(proveedor_evento_id)) BETWEEN 1 AND 200)`
- `CHECK (resultado IN ('exito_simulado','rechazo_simulado'))`
- `CHECK (octet_length(huella_payload) = 32)`
- `UNIQUE (proveedor_evento_id)`
- `UNIQUE (operacion_id, proveedor_evento_id)`


### B.095 Tabla `public.reserva_pago_fake_resultado_ensayo`
- **Migración de creación:** `V000021`
- **Atributos:** 5

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `operacion_id` | `uuid` | PK; FK → `public.reserva_pago_ensayo_operacion(operacion_id→id)`; NOT NULL | Atributo `operacion_id`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `proveedor_evento_id` | `text` | UQ; NULL permitido | Atributo `proveedor_evento_id`; el nombre y tipo se conservan según el DDL. |
| `resultado` | `text` | NULL permitido | Atributo `resultado`; el nombre y tipo se conservan según el DDL. |
| `registrado_en` | `timestamptz` | NOT NULL | Atributo `registrado_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (estado IN ('resultado','sin_respuesta'))`
- `CHECK (proveedor_evento_id IS NULL OR length(btrim(proveedor_evento_id)) BETWEEN 1 AND 200)`
- `CHECK (resultado IN ('exito_simulado','rechazo_simulado'))`
- `CHECK ((estado='resultado') = (proveedor_evento_id IS NOT NULL AND resultado IS NOT NULL))`
- `CHECK (estado <> 'sin_respuesta' OR (proveedor_evento_id IS NULL AND resultado IS NULL))`


### B.096 Tabla `public.reserva_vinculo_purgado_local`
- **Migración de creación:** `V000026`
- **Atributos:** 4

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `reserva_id` | `uuid` | PK; FK → `public.reserva_ensayo_local(reserva_id→id)`; NOT NULL | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `vencio_en` | `timestamptz` | NOT NULL | Atributo `vencio_en`; el nombre y tipo se conservan según el DDL. |
| `purgado_en` | `timestamptz` | NOT NULL | Atributo `purgado_en`; el nombre y tipo se conservan según el DDL. |
| `campos_retirados` | `text[]` | NOT NULL | Atributo `campos_retirados`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (cardinality(campos_retirados) > 0)`
- `CHECK (purgado_en >= vencio_en)`


## Dominio: Transacciones financieras

### B.097 Tabla `public.cuenta_cobro_sintetica_historial_local`
- **Migración de creación:** `V000030`
- **Atributos:** 7

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `bigserial` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `cuenta_id` | `uuid` | FK → `public.cuenta_cobro_sintetica_local(cuenta_id→id)`; NOT NULL | Atributo `cuenta_id`; el nombre y tipo se conservan según el DDL. |
| `usuario_id` | `uuid` | FK → `public.usuario(usuario_id→id)`; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `accion` | `text` | NOT NULL | Atributo `accion`; el nombre y tipo se conservan según el DDL. |
| `ocurrida_en` | `timestamptz` | NOT NULL | Atributo `ocurrida_en`; el nombre y tipo se conservan según el DDL. |
| `correlacion_id` | `text` | NOT NULL | Atributo `correlacion_id`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (accion IN ('creada','actualizada','revocada','retirada_baja'))`
- `CHECK (length(clave_idempotencia) BETWEEN 8 AND 128)`


### B.098 Tabla `public.cuenta_cobro_sintetica_local`
- **Migración de creación:** `V000030`
- **Atributos:** 8

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `usuario_id` | `uuid` | FK → `public.usuario(usuario_id→id)`; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `adaptador` | `text` | NOT NULL | Atributo `adaptador`; el nombre y tipo se conservan según el DDL. |
| `referencia_ficticia` | `text` | NULL permitido | Atributo `referencia_ficticia`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `actualizada_en` | `timestamptz` | NOT NULL | Marca temporal de actualización del registro. |
| `revocada_en` | `timestamptz` | NULL permitido | Atributo `revocada_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (adaptador='fake-local-v1')`
- `CHECK (estado IN ('activa','reemplazada','revocada','retirada_baja'))`
- `CONSTRAINT cuenta_cobro_sintetica_reference_ck CHECK ( (estado='retirada_baja' AND referencia_ficticia IS NULL) OR (estado<>'retirada_baja' AND referencia_ficticia ~ '^demo_[a-f0-9-]{36}$') )`
- `CONSTRAINT cuenta_cobro_sintetica_revocation_ck CHECK ( (estado IN ('revocada','retirada_baja') AND revocada_en IS NOT NULL) OR (estado IN ('activa','reemplazada') AND revocada_en IS NULL) )`


## Dominio: Operaciones en recinto y disputas

### B.099 Tabla `public.disputa_ensayo_historial`
- **Migración de creación:** `V000024`
- **Atributos:** 7

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `secuencia` | `bigint` | PK; NOT NULL | Atributo `secuencia`; el nombre y tipo se conservan según el DDL. |
| `disputa_id` | `uuid` | FK → `public.disputa_ensayo_local(disputa_id→id)`; NOT NULL | Atributo `disputa_id`; el nombre y tipo se conservan según el DDL. |
| `estado_anterior` | `text` | NULL permitido | Atributo `estado_anterior`; el nombre y tipo se conservan según el DDL. |
| `estado_nuevo` | `text` | NOT NULL | Atributo `estado_nuevo`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NULL permitido | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `motivo_codigo` | `text` | NOT NULL | Atributo `motivo_codigo`; el nombre y tipo se conservan según el DDL. |
| `ocurrida_en` | `timestamptz` | NOT NULL | Atributo `ocurrida_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (estado_anterior IN ('abierta','cerrada'))`
- `CHECK (estado_nuevo IN ('abierta','cerrada'))`
- `CHECK (motivo_codigo IN ('ensayo_privacidad','ensayo_finalizado','registro_erroneo','duplicada'))`
- `CONSTRAINT disputa_ensayo_historial_transicion_ck CHECK ( (estado_anterior IS NULL AND estado_nuevo='abierta' AND motivo_codigo='ensayo_privacidad') OR (estado_anterior='abierta' AND estado_nuevo='cerrada' AND motivo_codigo IN ('ensayo_finalizado','registro_erroneo','duplicada')) )`


### B.100 Tabla `public.disputa_ensayo_local`
- **Migración de creación:** `V000024`
- **Atributos:** 13

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `reserva_id` | `uuid` | FK → `public.reserva_ensayo_local(reserva_id→id)`; NOT NULL | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `anfitrion_id` | `uuid` | UQ compuesta (anfitrion_id, clave_idempotencia); FK → `public.usuario(anfitrion_id→id)`; NULL permitido | Atributo `anfitrion_id`; el nombre y tipo se conservan según el DDL. |
| `arrendatario_id` | `uuid` | FK → `public.usuario(arrendatario_id→id)`; NULL permitido | Atributo `arrendatario_id`; el nombre y tipo se conservan según el DDL. |
| `abierta_por` | `uuid` | FK → `public.usuario(abierta_por→id)`; NULL permitido | Atributo `abierta_por`; el nombre y tipo se conservan según el DDL. |
| `motivo_codigo` | `text` | NOT NULL | Atributo `motivo_codigo`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (anfitrion_id, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `huella_solicitud` | `bytea` | NOT NULL | Atributo `huella_solicitud`; el nombre y tipo se conservan según el DDL. |
| `abierta_en` | `timestamptz` | NOT NULL | Atributo `abierta_en`; el nombre y tipo se conservan según el DDL. |
| `cerrada_por` | `uuid` | FK → `public.usuario(cerrada_por→id)`; NULL permitido | Atributo `cerrada_por`; el nombre y tipo se conservan según el DDL. |
| `motivo_cierre_codigo` | `text` | NULL permitido | Atributo `motivo_cierre_codigo`; el nombre y tipo se conservan según el DDL. |
| `cerrada_en` | `timestamptz` | NULL permitido | Atributo `cerrada_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (motivo_codigo='ensayo_privacidad')`
- `CHECK (estado IN ('abierta','cerrada'))`
- `CHECK (length(btrim(clave_idempotencia)) BETWEEN 1 AND 200)`
- `CHECK (octet_length(huella_solicitud)=32)`
- `CHECK (motivo_cierre_codigo IN ('ensayo_finalizado','registro_erroneo','duplicada'))`
- `CONSTRAINT disputa_ensayo_participantes_ck CHECK (anfitrion_id <> arrendatario_id)`
- `UNIQUE (anfitrion_id, clave_idempotencia)`
- `CONSTRAINT disputa_ensayo_apertura_ck CHECK ( abierta_por=anfitrion_id OR (abierta_por IS NULL AND anfitrion_id IS NULL) )`
- `CONSTRAINT disputa_ensayo_cierre_ck CHECK ( (estado='abierta' AND cerrada_por IS NULL AND motivo_cierre_codigo IS NULL AND cerrada_en IS NULL) OR (estado='cerrada' AND motivo_cierre_codigo IS NOT NULL AND cerrada_en IS NOT NULL AND (cerrada_por IS NOT NULL OR (anfitrion_id IS NULL AND arrendatario_id IS NULL))) )`


### B.101 Tabla `public.operacion_arriendo_evidencia_ensayo_local`
- **Migración de creación:** `V000035`
- **Atributos:** 9

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `operacion_id` | `uuid` | FK → `public.operacion_arriendo_ensayo_local(operacion_id→id)`; NOT NULL | Atributo `operacion_id`; el nombre y tipo se conservan según el DDL. |
| `fixture_code` | `text` | NOT NULL | Atributo `fixture_code`; el nombre y tipo se conservan según el DDL. |
| `mime_type` | `text` | NOT NULL | Atributo `mime_type`; el nombre y tipo se conservan según el DDL. |
| `sha256` | `char(64)` | NOT NULL | Atributo `sha256`; el nombre y tipo se conservan según el DDL. |
| `size_bytes` | `bigint` | NOT NULL | Atributo `size_bytes`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |
| `retirar_archivo_en` | `timestamptz` | NULL permitido | Atributo `retirar_archivo_en`; el nombre y tipo se conservan según el DDL. |
| `archivo_retirado_en` | `timestamptz` | NULL permitido | Atributo `archivo_retirado_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (fixture_code='synthetic-png-v1')`
- `CHECK (mime_type='image/png')`
- `CHECK (sha256 ~ '^[0-9a-f]{64}$')`
- `CHECK (size_bytes BETWEEN 1 AND 1048576)`


### B.102 Tabla `public.reclamo_dano_descargo_ensayo_local`
- **Migración de creación:** `V000035`
- **Atributos:** 7

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `reclamo_id` | `uuid` | UQ; UQ compuesta (reclamo_id, clave_idempotencia); FK → `public.reclamo_dano_ensayo_local(reclamo_id→id)`; NOT NULL | Atributo `reclamo_id`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NULL permitido | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `descripcion` | `text` | NOT NULL | Atributo `descripcion`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (reclamo_id, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `huella_solicitud` | `bytea` | NOT NULL | Atributo `huella_solicitud`; el nombre y tipo se conservan según el DDL. |
| `creado_en` | `timestamptz` | NOT NULL | Marca temporal de creación del registro. |

**Restricciones DDL vigentes:**

- `CHECK (length(btrim(descripcion))>0)`
- `CHECK (length(btrim(clave_idempotencia)) BETWEEN 8 AND 200)`
- `CHECK (octet_length(huella_solicitud)=32)`
- `UNIQUE(reclamo_id,clave_idempotencia)`


### B.103 Tabla `public.reclamo_dano_ensayo_local`
- **Migración de creación:** `V000035`
- **Atributos:** 12

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `reserva_id` | `uuid` | UQ; FK → `public.reserva_ensayo_local(reserva_id→id)`; NULL permitido | Atributo `reserva_id`; el nombre y tipo se conservan según el DDL. |
| `anfitrion_id` | `uuid` | UQ compuesta (anfitrion_id, clave_idempotencia); FK → `public.usuario(anfitrion_id→id)`; NULL permitido | Atributo `anfitrion_id`; el nombre y tipo se conservan según el DDL. |
| `arrendatario_id` | `uuid` | FK → `public.usuario(arrendatario_id→id)`; NULL permitido | Atributo `arrendatario_id`; el nombre y tipo se conservan según el DDL. |
| `checkout_operacion_id` | `uuid` | FK → `public.operacion_arriendo_ensayo_local(checkout_operacion_id→id)`; NULL permitido | Atributo `checkout_operacion_id`; el nombre y tipo se conservan según el DDL. |
| `checkout_evidencia_id` | `uuid` | FK → `public.operacion_arriendo_evidencia_ensayo_local(checkout_evidencia_id→id)`; NULL permitido | Atributo `checkout_evidencia_id`; el nombre y tipo se conservan según el DDL. |
| `descripcion` | `text` | NOT NULL | Atributo `descripcion`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (anfitrion_id, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `huella_solicitud` | `bytea` | NOT NULL | Atributo `huella_solicitud`; el nombre y tipo se conservan según el DDL. |
| `abierto_en` | `timestamptz` | NOT NULL | Atributo `abierto_en`; el nombre y tipo se conservan según el DDL. |
| `plazo_reclamo_hasta` | `timestamptz` | NOT NULL | Atributo `plazo_reclamo_hasta`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (length(btrim(descripcion))>0)`
- `CHECK (length(btrim(clave_idempotencia)) BETWEEN 8 AND 200)`
- `CHECK (octet_length(huella_solicitud)=32)`
- `CHECK (anfitrion_id <> arrendatario_id)`
- `CHECK (plazo_reclamo_hasta > abierto_en)`
- `UNIQUE(anfitrion_id,clave_idempotencia)`
- `CONSTRAINT reclamo_dano_ensayo_local_estado_check CHECK (estado IN ('abierto','resuelta'))`


### B.104 Tabla `public.reclamo_dano_historial_ensayo_local`
- **Migración de creación:** `V000035`
- **Atributos:** 5

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `secuencia` | `bigint` | PK; NOT NULL | Atributo `secuencia`; el nombre y tipo se conservan según el DDL. |
| `reclamo_id` | `uuid` | FK → `public.reclamo_dano_ensayo_local(reclamo_id→id)`; NOT NULL | Atributo `reclamo_id`; el nombre y tipo se conservan según el DDL. |
| `accion` | `text` | NOT NULL | Atributo `accion`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NULL permitido | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `ocurrida_en` | `timestamptz` | NOT NULL | Atributo `ocurrida_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CONSTRAINT reclamo_dano_historial_ensayo_local_accion_check CHECK (accion IN ('reclamo_abierto','descargo_registrado','reclamo_resuelto'))`


### B.105 Tabla `public.reclamo_dano_resolucion_ensayo_local`
- **Migración de creación:** `V000038`
- **Atributos:** 7

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `reclamo_id` | `uuid` | PK; FK → `public.reclamo_dano_ensayo_local(reclamo_id→id)`; NOT NULL | Atributo `reclamo_id`; el nombre y tipo se conservan según el DDL. |
| `resultado` | `text` | NOT NULL | Atributo `resultado`; el nombre y tipo se conservan según el DDL. |
| `motivo_codigo` | `text` | NOT NULL | Atributo `motivo_codigo`; el nombre y tipo se conservan según el DDL. |
| `administrador_id` | `uuid` | UQ compuesta (administrador_id, clave_idempotencia); FK → `public.usuario(administrador_id→id)`; NULL permitido | Atributo `administrador_id`; el nombre y tipo se conservan según el DDL. |
| `resuelta_en` | `timestamptz` | NOT NULL | Atributo `resuelta_en`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (administrador_id, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `huella_solicitud` | `bytea` | NOT NULL | Atributo `huella_solicitud`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (resultado IN ('acogido','rechazado'))`
- `CHECK (motivo_codigo IN ('evidencia_suficiente','evidencia_insuficiente','hecho_no_acreditado','informacion_insuficiente'))`
- `CHECK (length(btrim(clave_idempotencia)) BETWEEN 8 AND 200)`
- `CHECK (octet_length(huella_solicitud)=32)`
- `CHECK ((resultado='acogido' AND motivo_codigo='evidencia_suficiente') OR (resultado='rechazado' AND motivo_codigo<>'evidencia_suficiente'))`
- `UNIQUE(administrador_id,clave_idempotencia)`


## Dominio: Verificación KYC/KYB

### B.106 Tabla `public.elegibilidad_verificacion_local`
- **Migración de creación:** `V000028`
- **Atributos:** 8

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `usuario_id` | `uuid` | PK compuesta (usuario_id, tipo); FK → `public.usuario(usuario_id→id)`; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `tipo` | `text` | PK compuesta (usuario_id, tipo); NOT NULL | Atributo `tipo`; el nombre y tipo se conservan según el DDL. |
| `verificacion_id` | `uuid` | UQ; FK → `public.verificacion(verificacion_id→id)`; NOT NULL | Atributo `verificacion_id`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `concedida_en` | `timestamptz` | NOT NULL | Atributo `concedida_en`; el nombre y tipo se conservan según el DDL. |
| `revocada_en` | `timestamptz` | NULL permitido | Atributo `revocada_en`; el nombre y tipo se conservan según el DDL. |
| `revocada_por` | `uuid` | FK → `public.usuario(revocada_por→id)`; NULL permitido | Atributo `revocada_por`; el nombre y tipo se conservan según el DDL. |
| `motivo_revocacion_codigo` | `text` | NULL permitido | Atributo `motivo_revocacion_codigo`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (tipo IN ('kyc','kyb'))`
- `PRIMARY KEY (usuario_id,tipo)`
- `CONSTRAINT elegibilidad_verificacion_local_estado_check CHECK (estado IN ('elegible','revocada','retirada_privacidad'))`
- `CONSTRAINT elegibilidad_revocacion_ck CHECK ( (estado='elegible' AND revocada_en IS NULL AND revocada_por IS NULL AND motivo_revocacion_codigo IS NULL) OR (estado='revocada' AND revocada_en IS NOT NULL AND revocada_por IS NOT NULL AND motivo_revocacion_codigo IN ('aprobacion_fixture_incorrecta','revision_fixture_actualizada')) OR (estado='retirada_privacidad' AND revocada_en IS NOT NULL AND revocada_por IS NOT NULL AND motivo_revocacion_codigo='baja_privacidad') )`


### B.107 Tabla `public.verificacion`
- **Migración de creación:** `V000003`
- **Atributos:** 18

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `usuario_id` | `uuid` | UQ compuesta (usuario_id, clave_idempotencia); FK → `public.usuario(usuario_id→id)` [verificacion_usuario_fk]; NOT NULL | Atributo `usuario_id`; el nombre y tipo se conservan según el DDL. |
| `tipo` | `text` | NOT NULL | Atributo `tipo`; el nombre y tipo se conservan según el DDL. |
| `estado` | `text` | DEFAULT `'en_revision'`; NOT NULL | Atributo `estado`; el nombre y tipo se conservan según el DDL. |
| `proveedor_ref` | `text` | DEFAULT `'local-fixture-v1'`; NOT NULL | Atributo `proveedor_ref`; el nombre y tipo se conservan según el DDL. |
| `referencia_evidencia` | `text` | NOT NULL | Atributo `referencia_evidencia`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (usuario_id, clave_idempotencia); NOT NULL | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `reintento_de` | `uuid` | FK → `public.verificacion(reintento_de→id)` [verificacion_reintento_fk]; NULL permitido | Atributo `reintento_de`; el nombre y tipo se conservan según el DDL. |
| `revisor_id` | `uuid` | FK → `public.usuario(revisor_id→id)` [verificacion_revisor_fk]; NULL permitido | Atributo `revisor_id`; el nombre y tipo se conservan según el DDL. |
| `motivo_codigo` | `text` | NULL permitido | Atributo `motivo_codigo`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de creación del registro. |
| `resuelta_en` | `timestamptz` | NULL permitido | Atributo `resuelta_en`; el nombre y tipo se conservan según el DDL. |
| `retirar_en` | `timestamptz` | NULL permitido | Atributo `retirar_en`; el nombre y tipo se conservan según el DDL. |
| `retirada_privacidad_en` | `timestamptz` | NULL permitido | Atributo `retirada_privacidad_en`; el nombre y tipo se conservan según el DDL. |
| `correccion_codigo` | `text` | NULL permitido | Atributo `correccion_codigo`; el nombre y tipo se conservan según el DDL. |
| `revocada_en` | `timestamptz` | NULL permitido | Atributo `revocada_en`; el nombre y tipo se conservan según el DDL. |
| `revocada_por` | `uuid` | FK → `public.usuario(revocada_por→id)`; NULL permitido | Atributo `revocada_por`; el nombre y tipo se conservan según el DDL. |
| `motivo_revocacion_codigo` | `text` | NULL permitido | Atributo `motivo_revocacion_codigo`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CONSTRAINT verificacion_pk PRIMARY KEY (id)`
- `CONSTRAINT verificacion_usuario_fk FOREIGN KEY (usuario_id) REFERENCES public.usuario (id) ON DELETE RESTRICT`
- `CONSTRAINT verificacion_reintento_fk FOREIGN KEY (reintento_de) REFERENCES public.verificacion (id) ON DELETE RESTRICT`
- `CONSTRAINT verificacion_revisor_fk FOREIGN KEY (revisor_id) REFERENCES public.usuario (id) ON DELETE RESTRICT`
- `CONSTRAINT verificacion_tipo_ck CHECK (tipo IN ('kyc', 'kyb'))`
- `CONSTRAINT verificacion_proveedor_ck CHECK (proveedor_ref = 'local-fixture-v1')`
- `CONSTRAINT verificacion_ref_sintetica_ck CHECK (referencia_evidencia ~ '^fixture:[0-9a-f-]{36}$')`
- `CONSTRAINT verificacion_idempotencia_ck CHECK (length(clave_idempotencia) BETWEEN 8 AND 80)`
- `CONSTRAINT verificacion_reintento_no_self_ck CHECK (reintento_de IS NULL OR reintento_de <> id)`
- `CONSTRAINT verificacion_idempotencia_uk UNIQUE (usuario_id, clave_idempotencia)`
- `CONSTRAINT verificacion_retirada_privacidad_ck CHECK ( (estado='retirada_privacidad' AND retirada_privacidad_en IS NOT NULL) OR (estado<>'retirada_privacidad' AND retirada_privacidad_en IS NULL) )`
- `CONSTRAINT verificacion_reason_code_ck CHECK ( motivo_codigo IS NULL OR motivo_codigo IN ('documento_vencido','antecedentes_incompletos','inicio_actividades_no_confirmado','baja_privacidad') )`
- `CONSTRAINT verificacion_estado_ck CHECK (estado IN ('en_revision','aprobada','rechazada','revocada','retirada_privacidad'))`
- `CONSTRAINT verificacion_motivo_ck CHECK ( (estado='rechazada' AND revisor_id IS NOT NULL AND motivo_codigo IS NOT NULL AND resuelta_en IS NOT NULL) OR (estado='aprobada' AND revisor_id IS NOT NULL AND motivo_codigo IS NULL AND resuelta_en IS NOT NULL) OR (estado='en_revision' AND revisor_id IS NULL AND motivo_codigo IS NULL AND resuelta_en IS NULL) OR (estado='revocada' AND revisor_id IS NOT NULL AND motivo_codigo IS NULL AND resuelta_en IS NOT NULL AND revocada_en IS NOT NULL AND revocada_por IS NOT NULL AND motivo_revocacion_codigo IS NOT NULL) OR (estado='retirada_privacidad' AND revisor_id IS NULL AND motivo_codigo='baja_privacidad' AND resuelta_en IS NOT NULL) )`
- `CONSTRAINT verificacion_correccion_codigo_ck CHECK ( correccion_codigo IS NULL OR correccion_codigo IN ( 'fixture_vigente_actualizado','antecedentes_fixture_actualizados','inicio_actividades_fixture_actualizadas', 'legado_pre_v28_sin_codigo' ) )`
- `CONSTRAINT verificacion_revocacion_codigo_ck CHECK ( (revocada_en IS NULL AND revocada_por IS NULL AND motivo_revocacion_codigo IS NULL) OR (revocada_en IS NOT NULL AND revocada_por IS NOT NULL AND motivo_revocacion_codigo IN ( 'aprobacion_fixture_incorrecta','revision_fixture_actualizada' )) )`
- `CONSTRAINT verificacion_correccion_retry_ck CHECK ( (reintento_de IS NULL AND correccion_codigo IS NULL) OR (reintento_de IS NOT NULL AND correccion_codigo IS NOT NULL) )`


### B.108 Tabla `public.verificacion_archivo_retiro_pendiente_local`
- **Migración de creación:** `V000047`
- **Atributos:** 6

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `evidencia_id` | `uuid` | PK; NOT NULL | Atributo `evidencia_id`; el nombre y tipo se conservan según el DDL. |
| `archivo_id` | `uuid` | NOT NULL | Atributo `archivo_id`; el nombre y tipo se conservan según el DDL. |
| `disponible_en` | `timestamptz` | NOT NULL | Atributo `disponible_en`; el nombre y tipo se conservan según el DDL. |
| `lease_hasta` | `timestamptz` | NULL permitido | Atributo `lease_hasta`; el nombre y tipo se conservan según el DDL. |
| `intentos` | `integer` | DEFAULT `0`; NOT NULL | Atributo `intentos`; el nombre y tipo se conservan según el DDL. |
| `ultimo_codigo_error` | `text` | NULL permitido | Atributo `ultimo_codigo_error`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (intentos >= 0)`
- `CONSTRAINT verificacion_archivo_retiro_error_ck CHECK ( ultimo_codigo_error IS NULL OR ultimo_codigo_error='archivo_sintetico_no_retirado' )`


### B.109 Tabla `public.verificacion_evidencia_sintetica`
- **Migración de creación:** `V000008`
- **Atributos:** 10

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `uuid` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `verificacion_id` | `uuid` | FK → `public.verificacion(verificacion_id→id)` [verificacion_evidencia_verificacion_fk]; NOT NULL | Atributo `verificacion_id`; el nombre y tipo se conservan según el DDL. |
| `codigo_fixture` | `text` | NOT NULL | Atributo `codigo_fixture`; el nombre y tipo se conservan según el DDL. |
| `mime_type` | `text` | NOT NULL | Atributo `mime_type`; el nombre y tipo se conservan según el DDL. |
| `tamano_bytes` | `bigint` | NOT NULL | Atributo `tamano_bytes`; el nombre y tipo se conservan según el DDL. |
| `sha256` | `char(64)` | NOT NULL | Atributo `sha256`; el nombre y tipo se conservan según el DDL. |
| `creada_en` | `timestamptz` | DEFAULT `now()`; NOT NULL | Marca temporal de creación del registro. |
| `archivo_id` | `uuid` | NULL permitido | Atributo `archivo_id`; el nombre y tipo se conservan según el DDL. |
| `retirar_archivo_en` | `timestamptz` | NULL permitido | Atributo `retirar_archivo_en`; el nombre y tipo se conservan según el DDL. |
| `archivo_retirado_en` | `timestamptz` | NULL permitido | Atributo `archivo_retirado_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CONSTRAINT verificacion_evidencia_sintetica_pk PRIMARY KEY (id)`
- `CONSTRAINT verificacion_evidencia_verificacion_fk FOREIGN KEY (verificacion_id) REFERENCES public.verificacion (id) ON DELETE RESTRICT`
- `CONSTRAINT verificacion_evidencia_fixture_ck CHECK (codigo_fixture = 'synthetic-png-v1')`
- `CONSTRAINT verificacion_evidencia_mime_ck CHECK (mime_type = 'image/png')`
- `CONSTRAINT verificacion_evidencia_size_ck CHECK (tamano_bytes BETWEEN 1 AND 1048576)`
- `CONSTRAINT verificacion_evidencia_sha_ck CHECK (sha256 ~ '^[0-9a-f]{64}$')`
- `CONSTRAINT verificacion_evidencia_archivo_retencion_ck CHECK ( (archivo_id IS NULL AND archivo_retirado_en IS NOT NULL) OR (archivo_id IS NOT NULL AND archivo_retirado_en IS NULL) ) NOT VALID`


### B.110 Tabla `public.verificacion_historial_local`
- **Migración de creación:** `V000028`
- **Atributos:** 10

| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |
|---|---|---|---|
| `id` | `bigint` | PK; NOT NULL | Identificador registrado en el esquema; la clave se indica en restricciones. |
| `verificacion_id` | `uuid` | UQ compuesta (verificacion_id, clave_idempotencia); FK → `public.verificacion(verificacion_id→id)`; NOT NULL | Atributo `verificacion_id`; el nombre y tipo se conservan según el DDL. |
| `actor_id` | `uuid` | FK → `public.usuario(actor_id→id)`; NOT NULL | Atributo `actor_id`; el nombre y tipo se conservan según el DDL. |
| `accion` | `text` | NOT NULL | Atributo `accion`; el nombre y tipo se conservan según el DDL. |
| `estado_anterior` | `text` | NULL permitido | Atributo `estado_anterior`; el nombre y tipo se conservan según el DDL. |
| `estado_nuevo` | `text` | NOT NULL | Atributo `estado_nuevo`; el nombre y tipo se conservan según el DDL. |
| `motivo_codigo` | `text` | NULL permitido | Atributo `motivo_codigo`; el nombre y tipo se conservan según el DDL. |
| `correlacion_id` | `text` | NOT NULL | Atributo `correlacion_id`; el nombre y tipo se conservan según el DDL. |
| `clave_idempotencia` | `text` | UQ compuesta (verificacion_id, clave_idempotencia); NULL permitido | Atributo `clave_idempotencia`; el nombre y tipo se conservan según el DDL. |
| `ocurrida_en` | `timestamptz` | NOT NULL | Atributo `ocurrida_en`; el nombre y tipo se conservan según el DDL. |

**Restricciones DDL vigentes:**

- `CHECK (estado_nuevo IN ('en_revision','aprobada','rechazada','revocada','retirada_privacidad'))`
- `CHECK (length(btrim(correlacion_id)) BETWEEN 1 AND 120)`
- `CONSTRAINT verificacion_historial_event_idempotency_uk UNIQUE (verificacion_id, clave_idempotencia)`
- `CONSTRAINT verificacion_historial_local_accion_check CHECK (accion IN ('solicitada','revision_aprobada','revision_rechazada','subsanacion_solicitada','elegibilidad_revocada','elegibilidad_retirada_privacidad','estado_observado_en_migracion'))`
- `CONSTRAINT verificacion_historial_estado_ck CHECK ( (accion='solicitada' AND estado_anterior IS NULL AND estado_nuevo='en_revision') OR (accion='revision_aprobada' AND estado_anterior='en_revision' AND estado_nuevo='aprobada' AND motivo_codigo IS NULL) OR (accion='revision_rechazada' AND estado_anterior='en_revision' AND estado_nuevo='rechazada' AND motivo_codigo IS NOT NULL) OR (accion='subsanacion_solicitada' AND estado_anterior='rechazada' AND estado_nuevo='rechazada' AND motivo_codigo IS NOT NULL) OR (accion='elegibilidad_revocada' AND estado_anterior='aprobada' AND estado_nuevo='revocada' AND motivo_codigo IS NOT NULL) OR (accion='elegibilidad_retirada_privacidad' AND estado_anterior='aprobada' AND estado_nuevo='retirada_privacidad' AND motivo_codigo='baja_privacidad') OR (accion='estado_observado_en_migracion' AND estado_anterior IS NULL AND estado_nuevo='retirada_privacidad') )`

