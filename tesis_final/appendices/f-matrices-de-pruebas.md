# ANEXO F: MATRICES DE PRUEBAS Y COBERTURA DE CALIDAD

Este anexo documenta la especificación de los 16 casos de prueba técnicos (`PT-01` a `PT-16`), correspondientes unívocamente a los casos de prueba (`CP-01` a `CP-16`) del Plan Integral de Aseguramiento de Calidad de **espaciGo**. Han sido diseñados para validar el comportamiento del backend Go, la persistencia en PostgreSQL 18 / PostGIS 3.6 y la interfaz en Next.js 16 (React 19).

## Catálogo de Casos de Prueba de ES2 (PT-01 a PT-16)

Todos los casos siguientes detallan las condiciones de prueba, precondiciones, entradas, secuencias de pasos, resultados esperados, criterios de aprobación y trazabilidad formal con los requerimientos (RF/RNF), casos de uso canónicos (`UC-01` a `UC-14`) e indicadores SMART (`KPI-01` a `KPI-08`). Cada ejecución debería registrar identificador de caso, versión de código, datos sintéticos, entorno, ejecutor y evidencia. Esta entrega no adjunta los registros de ejecución de las pruebas descritas; por ello las fichas se presentan como casos y criterios, no como resultados certificados.

---

## PT-01 — Validación de Intervalo y Reglas de Disponibilidad
- **Caso de Prueba:** `CP-01`
- **Tipo y Traza:** Unitaria de Dominio; `RF-10, RF-11, UC-10, UC-11, KPI-02`.
- **Precondición y Datos:** Función de validación temporal disponible en `internal/occupancy`; espacio sintético con un intervalo ocupado. Probar inicio en el pasado, fin menor o igual al inicio, intervalo solapado y un intervalo adyacente válido.
- **Pasos:** Invocar el método de evaluación con cada combinación y capturar la decisión del motor.
- **Resultado Esperado y Aprobación:** Las tres combinaciones inválidas se rechazan retornando error de dominio tipado; el intervalo adyacente se aprueba bajo la convención semiabierta `[inicio, termino)` sin colisión.
- **Entorno y Evidencia:** Suite de pruebas unitarias Go (`go test ./internal/occupancy/...`). Estado: Caso y suite de referencia identificados; no se adjunta un registro de ejecución reproducible en esta entrega.

---

## PT-02 — Doble Reserva Concurrente y Exclusión Física GiST
- **Caso de Prueba:** `CP-02`
- **Tipo y Traza:** Integración y Concurrencia Transaccional; `RF-11, RF-12, UC-11, RNF-02, KPI-02`.
- **Precondición y Datos:** Base de datos PostgreSQL 18 con extensión `btree_gist` activa; tabla `public.ocupacion` con restricción `EXCLUDE USING gist (espacio_id WITH =, intervalo WITH &&) WHERE (activo)`; un espacio libre; 50 solicitudes concurrentes simultáneas para la misma franja.
- **Pasos:** Lanzar goroutines concurrentes sincronizadas con barrera para insertar reservas sobre el mismo intervalo temporal.
- **Resultado Esperado y Aprobación:** Exactamente una sola transacción tiene éxito y confirma la ocupación; las restantes 49 transacciones son abortadas por el motor con violación de exclusión GiST (código SQLSTATE `23P01`), retornando HTTP 409 Conflict ordenado al cliente. Cero colisiones de agenda (*overbooking cero*).
- **Entorno y Evidencia:** Prueba de integración Go con base de datos real de ensayo. Estado: Caso y suite de referencia identificados; no se adjunta un registro de ejecución reproducible en esta entrega.

---

## PT-03 — Pre-Autorización y Custodia Condicionada de Fondos (Escrow)
- **Caso de Prueba:** `CP-03`
- **Tipo y Traza:** Integración Financiera; `RF-14, UC-11, RNF-04, KPI-03`.
- **Precondición y Datos:** Reserva en estado `PENDIENTE_PAGO`, adaptador de pasarela de pago (Mercado Pago Split Mock) configurado con respuestas controladas.
- **Pasos:** Iniciar proceso de checkout, simular respuesta exitosa de captura y observar transición de estados antes de vencer el TTL de 15 minutos.
- **Resultado Esperado y Aprobación:** Los fondos quedan retenidos en custodia (*escrow*) sin liquidación inmediata al anfitrión; la reserva pasa al estado `CONFIRMADA_PENDIENTE_FIRMA` y el intervalo de ocupación permanece activo.
- **Entorno y Evidencia:** Servidor mock de Mercado Pago y base de datos local. Estado: Escenario de mock definido; no se adjunta un registro de ejecución reproducible en esta entrega.

---

## PT-04 — Idempotencia Transaccional y Procesamiento de Webhooks
- **Caso de Prueba:** `CP-04`
- **Tipo y Traza:** Integración y Tolerancia a Fallos; `RF-13, RF-14, UC-11, RNF-04, KPI-03`.
- **Precondición y Datos:** Peticiones HTTP con encabezado `Idempotency-Key` único; eventos webhook válidos, duplicados, fuera de orden y con firma HMAC inválida.
- **Pasos:** Reenviar la misma petición de pago tres veces con idéntica clave de idempotencia; inyectar webhook duplicado y webhook con firma adulterada.
- **Resultado Esperado y Aprobación:** El backend ejecuta la operación una única vez, respondiendo a los reintentos con la respuesta almacenada en caché sin duplicar cobros; el webhook sin firma HMAC válida es rechazado con HTTP 401 Unauthorized sin alterar el estado del libro mayor.
- **Entorno y Evidencia:** Middleware de idempotencia Go y suite de pruebas HTTP. Estado: Caso y suite de referencia identificados; no se adjunta un registro de ejecución reproducible en esta entrega.

---

## PT-05 — Expiración de Ventana de Aprobación de Anfitrión (24 Horas)
- **Caso de Prueba:** `CP-05`
- **Tipo y Traza:** Integración y Gestión Temporal; `RF-15, UC-11, RNF-01`.
- **Precondición y Datos:** Solicitud de reserva pagada pendiente de decisión del anfitrión; reloj del sistema manipulable en entorno de prueba.
- **Pasos:** Simular silencio del anfitrión avanzando el tiempo lógico más allá de 24 horas; ejecutar daemon de conciliación.
- **Resultado Esperado y Aprobación:** La reserva expira automáticamente pasando a `CANCELADA_POR_VENCIMIENTO`, liberando la ocupación en base de datos y ordenando la devolución íntegra de los fondos retenidos en custodia al arrendatario.
- **Entorno y Evidencia:** Daemon reconciliador en Go y base de datos local. Estado: Caso y suite de referencia identificados; no se adjunta un registro de ejecución reproducible en esta entrega.

---

## PT-06 — Formalización y Firma Bilateral de Contrato Digital
- **Caso de Prueba:** `CP-06`
- **Tipo y Traza:** Integración y Seguridad Contractual; `RF-16, RF-17, UC-12, RNF-08`.
- **Precondición y Datos:** Reserva aprobada bilateralmente, contrato PDF generado con hash SHA-256.
- **Pasos:** Registrar la firma del arrendatario, verificar restricción de ingreso; registrar la firma del anfitrión; evaluar intento de check-in antes y después.
- **Resultado Esperado y Aprobación:** La primera firma deja el contrato en estado `FIRMA_PARCIAL` bloqueando el check-in; la segunda firma consolida el contrato como `VIGENTE`, habilitando la generación del código de acceso y check-in.
- **Entorno y Evidencia:** Adaptador de contratos Go y almacenamiento seguro. Estado: Caso y suite de referencia identificados; no se adjunta un registro de ejecución reproducible en esta entrega.

---

## PT-07 — Control de Acceso RBAC y Resolución de Disputas (GADM)
- **Caso de Prueba:** `CP-07`
- **Tipo y Traza:** Seguridad Funcional y Autorización; `RF-22, RF-25, UC-13, UC-14`.
- **Precondición y Datos:** Disputa abierta por daños; cuentas de prueba con roles `arrendatario`, `arrendador` y `administrador_global`.
- **Pasos:** Intentar resolver la disputa invocando el endpoint administrativo con cada uno de los roles ordinarios; luego invocar con token de administrador global válido.
- **Resultado Esperado y Aprobación:** Las peticiones de usuarios ordinarios son rechazadas con HTTP 403 Forbidden; el administrador global emite el dictamen registrando el motivo obligatorio en `public.evento_auditoria_local`.
- **Entorno y Evidencia:** Middleware de autorización Go y logs de auditoría. Estado: Caso y suite de referencia identificados; no se adjunta un registro de ejecución reproducible en esta entrega.

---

## PT-08 — Cierre de Operación, Check-out y Liquidación Split
- **Caso de Prueba:** `CP-08`
- **Tipo y Traza:** Integración Operacional y Financiera; `RF-20, RF-21, UC-13, KPI-08`.
- **Precondición y Datos:** Reserva finalizada, check-out registrado conforme, transcurso de la ventana de 24 horas sin reclamos por daños.
- **Pasos:** Ejecutar el proceso de liquidación automática.
- **Resultado Esperado y Aprobación:** Los fondos en custodia se liberan: espaciGo retiene automáticamente la comisión del 10% y el saldo restante (90% menos tarifas adquirentes) se transfiere a la cuenta bancaria registrada del anfitrión. La reserva pasa a `FINALIZADA_LIQUIDADA`.
- **Entorno y Evidencia:** Motor de liquidación Go y adaptador financiero mock. Estado: Escenario de mock local definido; no se adjunta un registro de ejecución reproducible en esta entrega.

---

## PT-09 — Rendimiento y Latencia de Búsqueda Geoespacial
- **Caso de Prueba:** `CP-09`
- **Tipo y Traza:** Eficiencia de Desempeño y Carga; `RF-06, RF-08, UC-07, RNF-01, KPI-01`.
- **Precondición y Datos:** Catálogo con espacios sintéticos georreferenciados; índices GiST activos en `public.espacio`; mezcla de filtros por coordenadas, categoría y rango de precios.
- **Pasos:** Inyectar tráfico concurrente de búsqueda sobre el endpoint `/public/spaces` evaluando tiempos de respuesta de consulta `ST_DWithin`.
- **Resultado Esperado y Aprobación:** Latencia en percentil 95 (P95) ≤ 250 ms conforme al objetivo SMART definido en `KPI-01`. Cero errores de desbordamiento de conexiones en el pool de `pgx`.
- **Entorno y Evidencia:** Especificación de prueba de carga con k6 sobre el BFF de catálogo. Estado: **Planificada / No medida en producción** (diseño estructural validado con índice GiST).

---

## PT-10 — Capacidad, Concurrencia y Auto-Escalado Serverless
- **Caso de Prueba:** `CP-10`
- **Tipo y Traza:** Carga y Escalabilidad; `RNF-01, RNF-03, SLA-01`.
- **Precondición y Datos:** Configuración de Google Cloud Run con límites de 1 a 10 instancias y Cloud SQL con escalado de conexiones.
- **Pasos:** Inyectar rampa de carga progresiva hasta 500 usuarios virtuales simultáneos.
- **Resultado Esperado y Aprobación:** El servicio aprovisiona nuevas instancias en < 30 segundos sin pérdida de transacciones ni errores 5xx.
- **Entorno y Evidencia:** Planificada para entorno de Staging en Google Cloud Platform. Estado: **Planificada en nube**.

---

## PT-11 — Recuperación ante Desastres y Objetivos RPO / RTO
- **Caso de Prueba:** `CP-11`
- **Tipo y Traza:** Continuidad y Recuperación (DRP); `RNF-12, RNF-13, SLA-05, RB-01`.
- **Precondición y Datos:** Respaldo completo de base de datos PostgreSQL, registros de transacciones WAL archivados y entorno de recuperación aislado.
- **Pasos:** Simular pérdida de la instancia primaria de base de datos; activar procedimiento de conmutación por falla (failover) o restauración Point-in-Time (PITR) según el runbook `RB-01`.
- **Resultado Esperado y Aprobación:** Cumplimiento de los objetivos formales de continuidad de la plataforma: RPO ≤ 5 minutos (pérdida máxima de datos admisible respaldada por archivado WAL continuo) y RTO ≤ 30 minutos (tiempo máximo de restablecimiento del servicio). Integridad referencial y transacciones confirmadas preservadas íntegramente.
- **Entorno y Evidencia:** Protocolo de contingencia formalizado en Runbook `RB-01`. Estado: **Diseño validado documentalmente / Ensayo con inyección de fallas planificado**.

---

## PT-12 — Generación Determinista y Foliado Criptográfico de Contratos PDF
- **Caso de Prueba:** `CP-12`
- **Tipo y Traza:** Rendimiento e Integridad Documental; `RF-16, UC-12, RNF-01`.
- **Precondición y Datos:** Reserva en estado confirmada, datos bilaterales sintéticos validados.
- **Pasos:** Invocar el generador basado en `pdfcpu` para ensamblar el contrato de arriendo oficial con estampa temporal.
- **Resultado Esperado y Aprobación:** Archivo PDF generado en un tiempo ≤ 3 segundos con tamaño optimizado (< 1,5 MB), conteniendo el hash SHA-256 embebido y foliado secuencial.
- **Entorno y Evidencia:** Generador Go y validación de estructura de archivo. Estado: Caso y suite de referencia identificados; no se adjunta un registro de ejecución reproducible en esta entrega.

---

## PT-13 — Sesión, aislamiento de cuenta y cierre (E2E local)
- **Caso de Prueba:** `CP-13`
- **Tipo y Traza:** Integración de Extremo a Extremo (E2E); `RF-02, UC-02 a UC-13, Flujo Crítico`.
- **Precondición y Datos:** Entorno contenerizado local con frontend Next.js, backend Go y PostgreSQL 18 activos; datos de prueba precargados.
- **Pasos:** Iniciar sesión con dos cuentas sintéticas autorizadas; consultar la sesión, rehidratarla tras una recarga y comprobar que la segunda cuenta no accede a un recurso de la primera. Completar el recorrido local de publicación y sus operaciones de catálogo, y cerrar ambas sesiones. El código revisado no comprueba el rechazo de una cookie reutilizada después del cierre; esa verificación de revocación queda pendiente.
- **Resultado Esperado y Aprobación:** El flujo local mantiene sesión durante la rehidratación, limita los recursos a su propietario y cierra con respuesta satisfactoria. La revocación efectiva de una credencial reutilizada después del cierre debe verificarse con un paso adicional antes de declarar cumplimiento de sesión.
- **Entorno y Evidencia:** Se identificó código en `frontend/tests/phase7-native.spec.ts` para login, rehidratación, aislamiento entre dos cuentas y cierre. El código inspeccionado no comprueba reutilización de la cookie después del cierre. No se ejecutó ni se adjunta salida de esta prueba; la revocación poscierre queda pendiente.

---

## PT-14 — Auditoría de Seguridad Estática y Vulnerabilidades OWASP
- **Caso de Prueba:** `CP-14`
- **Tipo y Traza:** Seguridad de Código y Dependencias; `RNF-04, RNF-05, OWASP Top 10`.
- **Precondición y Datos:** Repositorio de código fuente Go y Next.js/TypeScript.
- **Pasos:** Ejecutar herramientas de análisis estático (SAST): `govulncheck`, `npm audit` y verificación de inyecciones SQL en consultas parametrizadas `pgx`.
- **Resultado Esperado y Aprobación:** Cero vulnerabilidades críticas o altas detectadas en código o dependencias directas; estricta parametrización en el 100% de las consultas SQL.
- **Entorno y Evidencia:** Pipeline local de inspección estática. Estado: Caso y suite de referencia identificados; no se adjunta un registro de ejecución reproducible en esta entrega.

---

## PT-15 — Auditoría de Accesibilidad Web (WCAG 2.1 AA) y Diseño Responsivo
- **Caso de Prueba:** `CP-15`
- **Tipo y Traza:** Usabilidad y Accesibilidad; `RNF-09, RNF-15`.
- **Precondición y Datos:** Servidor de desarrollo Next.js activo; páginas públicas de catálogo y paneles de usuario.
- **Pasos:** Ejecutar escaneo automatizado con `@axe-core/playwright` sobre resoluciones móvil (360px), tablet (768px) y escritorio (1440px).
- **Resultado Esperado y Aprobación:** Cero violaciones de accesibilidad bajo el estándar WCAG 2.1 Nivel AA (contrastes válidos, etiquetas ARIA, navegación por teclado y diseño adaptable sin desbordamiento horizontal).
- **Entorno y Evidencia:** Reporte de resultados de axe-core integrado en Playwright. Estado: Caso y suite de referencia identificados; no se adjunta un registro de ejecución reproducible en esta entrega.

---

## PT-16 — Ejercicio de Derechos ARCO, Bloqueo y Anonimización (Ley N° 21.719)
- **Caso de Prueba:** `CP-16`
- **Tipo y Traza:** Privacidad por Diseño y Cumplimiento Normativo; `RF-23, RF-24, UC-04, RNF-14, KPI-04`.
- **Precondición y Datos:** Titular de datos con transacciones históricas finalizadas y obligaciones fiscales vigentes; política de retención auditada.
- **Pasos:** Solicitar bloqueo cautelar y supresión de cuenta; medir tiempo de inhabilitación; ejecutar pipeline de anonimización irreversible y generación de token HMAC replay.
- **Resultado Esperado y Aprobación:** Bloqueo cautelar temporal ejecutado en ≤ 2 días hábiles (inmediato en entorno de prueba); supresión definitiva y anonimización ejecutadas en plazo legal ≤ 30 días corridos (meta operativa interna ≤ 15 días); datos identificatorios anonimizados irreversiblemente preservando registros contables/fiscales obligatorios; registro exitoso en `public.usuario_eliminado_replay`. En caso de vulneración, notificación sin dilaciones indebidas conforme al Art. 14 sexies ante la Agencia de Protección de Datos Personales.
- **Entorno y Evidencia:** Suite de pruebas del módulo `internal/privacy` y base de datos local. Estado: Caso y suite de referencia identificados; no se adjunta un registro de ejecución reproducible en esta entrega.

---

Este catálogo contiene 16 casos y criterios de prueba (`PT-01` a `PT-16` / `CP-01` a `CP-16`). Su inclusión especifica cobertura prevista; no acredita por sí sola ejecución, calidad, desempeño ni conformidad regulatoria.
