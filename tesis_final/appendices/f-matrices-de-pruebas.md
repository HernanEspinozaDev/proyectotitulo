# ANEXO F: MATRICES DE PRUEBAS Y COBERTURA DE CALIDAD

Los casos conservan los identificadores PT del plan de pruebas. La matriz actualiza su alcance según el ADR del 4 de noviembre. El Capítulo XII documenta evidencia por corte. La conformidad de una fila requiere un registro que identifique el caso, versión, entorno, datos, resultado observado y limitaciones.

## Verificación funcional

**Tabla F.1**\
*Casos funcionales y resultados esperados*

| Caso y traza | Escenario y operación | Resultado esperado |
|---|---|---|
| PT-01 · RQF-110, RQF-111 | Solicitar intervalos inválidos, solapados y adyacentes sobre un espacio sintético. | Rechazo de intervalos inválidos y solapados. Admisión del adyacente conforme a límites semiabiertos. |
| PT-02 · RQF-112, RQF-113 | Lanzar solicitudes simultáneas para el mismo intervalo en PostgreSQL. | Una ocupación activa. Los conflictos se registran y no generan un segundo bloqueo. |
| PT-03 · RQF-116 a RQF-118 · CU-24, CU-25 | Aceptar una emisión sin firma y acreditar renta simulada. Repetir con garantía habilitada. | La renta se habilita tras ambas aceptaciones. La garantía se cobra después y por separado. |
| PT-04 · RQF-128, RQF-129 · RNF-012 | Reenviar un evento acreditado e inyectar un evento posterior al vencimiento. | El duplicado conserva el estado y el vencimiento. El tardío entra a conciliación sin reactivar la reserva ni crear otra ocupación. |
| PT-05 · RQF-120, RQF-140 | Agotar una ventana de pago con reloj controlado. | La plataforma libera el bloqueo atómicamente y conserva el historial. |
| PT-06 · RQF-130, RQF-132, RQF-133 · CU-29, CU-30 | Emitir con identidades verificadas. Modificar condiciones y ensayar la ruta SimpleFirma. | Se genera otra emisión. Ambas aceptaciones se registran por emisión. Solo la ruta opcional habilita firmas tras acreditar aportes. |
| PT-07 · CU-34 y reglas de autorización del ADR | Acceder a evidencias como titular, participante y tercero. | Cada actor accede según vínculo y capacidad. El acceso indebido se deniega. |
| PT-08 · RQF-143 a RQF-152 y RQF-203 a RQF-206 · HU35 · CU-33, CU-34, CU-48 | Intentar check-in fuera de fecha y sin foto. Registrar check-in válido, entregar con foto y confirmar desocupación como titular mientras existe otro intervalo activo. | Se rechazan las entradas inválidas. El ingreso válido registra fecha y ubicación, inicia el arriendo y notifica al titular. La confirmación registra fecha y ubicación, libera solo su intervalo, conserva el contrato y permite republicar. |
| PT-12 · RQF-130, RQF-132 | Recuperar documento y huella, cambiar condiciones y volver a emitir. | La emisión anterior conserva identidad y contenido. La nueva emisión tiene identificador distinto. |
| PT-13 · RQF-011, RQF-023 · RNF-016 | Iniciar sesión, comprobar aislamiento y repetir acceso después del cierre. | La sesión permite solo las acciones autorizadas y queda invalidada al cerrar. |

*Nota.* Elaboración propia. Las pruebas que dependen de proveedor se identifican por entorno y modalidad.

## Verificación de calidad y operación

**Tabla F.2**\
*Casos de calidad y criterio de aceptación*

| Caso y traza | Escenario y operación | Resultado esperado |
|---|---|---|
| PT-09 · RNF-001 | Medir la búsqueda de la Tabla E.1 en la ruta y versión seleccionadas. Registrar datos, 200 usuarios concurrentes y tiempo de extremo a extremo. | Los tiempos observados satisfacen el umbral del Capítulo XI. |
| PT-10 · Capítulo XI | Aumentar carga en un entorno identificado y registrar volumen, latencia y errores. | El reporte caracteriza la capacidad por escenario y explica su límite. |
| PT-11 · RNF-010 | Restaurar base y objetos privados. Verificar referencias y permisos. | RPO máximo de 15 minutos y RTO máximo de 1 hora en el escenario definido. |
| PT-14 · RNF-015 | Revisar dependencias, interfaces, transporte y autorización del corte. | El reporte registra alcance, hallazgos y verificación de correcciones. |
| PT-15 · RNF-007, RNF-008 | Ejecutar el recorrido mediante teclado y en resoluciones definidas. | El recorrido satisface los criterios de acceso y presentación especificados. |
| PT-16 · RNF-018 | Tramitar una solicitud sintética y recuperar un respaldo de prueba. | El operador comprueba la acción autorizada, los permisos y el estado posterior a la restauración. |

*Nota.* Elaboración propia. El estado de cada ejecución se conserva en su reporte de evidencia.

## Registro de evidencia

El Capítulo XII y la Tabla 11 identifican los resultados de LOCAL-1 y F5/F6. LOCAL-1 aporta evidencia del recorrido sintético documentado. Las modalidades externas de PT-03 y PT-06 conservan sus criterios pendientes. El ensayo local V1–V61 aporta evidencia parcial a PT-02 y PT-11. La recuperación conjunta y la carga objetivo requieren registros específicos. El resultado de un paquete o recorrido se asocia con una fila únicamente cuando el registro comprueba su criterio. El expediente de verificación registra entradas, fecha, entorno, versión, resultado y observaciones.


**Tabla F.3**\
*Correspondencia entre evidencia parcial y criterios de aceptación*

| Comprobación | Evidencia disponible | Estado del criterio objetivo |
|---|---|---|
| PT-02 · Exclusión temporal | Restauración local V1–V61 con un solo ganador ante solapamiento concurrente. | Comprobado para ese escenario y corte. |
| PT-09 y PT-10 · Carga | Consulta SQL PostGIS con 200 conexiones sobre 10.000 puntos sintéticos. | Evidencia del componente. Queda pendiente medir la búsqueda de extremo a extremo. |
| PT-11 · Recuperación | Restauración básica local aprobada. El ensayo del ejecutor GCP03 se detiene en la restauración de permisos. | Pendiente verificar recuperación conjunta de base y objetos y medir RPO y RTO. |
| PT-07 · Acceso a evidencias | F5 registra controles documentales y F6 verifica la denegación a un titular ajeno en el recorrido sintético. | Evidencia parcial. El escenario completo conserva sus roles y recursos propios. |
| PT-16 · Retención | Evidencia documental F5 de retención y permisos en su alcance. | Pendiente verificar la política de retención y los objetos en el ensayo de recuperación objetivo. |

*Nota.* Elaboración propia a partir de los ensayos y registros del Capítulo XII. Los resultados locales conservan su alcance.

## Pruebas pendientes de cierre del código

**Tabla F.4**\
*Pruebas condicionadas por la disponibilidad del código*

| Prueba o condición | Dependencia | Evidencia pendiente |
|---|---|---|
| Operación completa · PT-08 | Código de ingreso, entrega y confirmación disponible en el mismo corte. | Registro del recorrido con evidencias, actores autorizados y otro intervalo vigente. |
| Mercado Pago · PT-03 y PT-04 | Adaptador de renta y comisión e integración de notificaciones. | Acreditación, duplicados, pago tardío, reembolso y conciliación con cuentas de ensayo. |
| SimpleFirma · PT-06 | Flujo opcional de firma asociado a la emisión. | Solicitudes, firmas por parte, vencimientos y efectos sobre cobros y reversos. |
| Garantía monetaria · PT-03 | Modalidad habilitada y mecanismo o proveedor definido e implementado. | Cobro separado, devolución total y parcial, reclamos y conciliación. |
| Catálogo de nueve categorías | Perfil de atributos, publicación y búsqueda de cada categoría en el corte evaluado. | Validaciones de publicación, búsqueda y disponibilidad, incluido el perfil Inmuebles. |
| Carga de extremo a extremo · PT-09 y PT-10 | Flujo de búsqueda listo y entorno objetivo identificado. | Volumen, latencia y errores medidos según RNF-001 y el escenario del ensayo. |
| Recuperación conjunta · PT-11 y PT-16 | Código y operación de base, objetos privados, permisos y retención listos para ensayo. | Restauración y comprobación de archivos, referencias y permisos. Medición de RPO y RTO. |

*Nota.* Elaboración propia. Cada resultado se integra al informe cuando existe código verificable y un registro de ejecución con versión, entorno y alcance.
