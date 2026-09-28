## Diagrama de arquitectura

La vista integrada conecta presentación, módulos, persistencia e integraciones. Es un diseño lógico asociado a contenedores y servicios virtuales propuestos en 3.6; no representa instancias construidas. El backend Go conserva una sola unidad desplegable con módulos por dominio y adaptadores para terceros, como se explica en 3.3.

![Arquitectura integrada propuesta](imagenes/figura-arquitectura_general.png){width=6.3in} <!--#fig:es2-arquitectura-general--> <!--#fuente:elaboración propia a partir de ES1 y del diseño ES2.-->

*Tabla. Correspondencia entre software e infraestructura propuesta.* <!--#tab:es2-mapa-arquitectura-->

| Software o dato | Recurso virtual o físico previsto | Contrato de diseño |
| --- | --- | --- |
| Navegador y web Next.js | Dispositivo del usuario y contenedor web | HTTPS y API documentada |
| API y módulos Go M01–M11 | Contenedor backend | Autorización, reglas de negocio y eventos correlacionados |
| Entidades operativas y calendario | PostgreSQL/PostGIS sobre servicio por elegir | Transacción de reserva, restricciones y respaldo |
| Documentos y auditoría | Servicio de archivos y destino analítico por elegir | Acceso, integridad y control de inmutabilidad aún abierto |
| Pago, firma, identidad y tributación | Adaptadores en backend y servicios externos | Contratos, credenciales, idempotencia y conciliación por verificar |

### Recorrido de una reserva y fallos

1. La web inicia una solicitud autenticada; M01–M03 aportan estado de identidad y M04–M05 la oferta. M06 valida el intervalo con el calendario `ocupacion` de 3.4. Reserva y ocupación deben confirmarse en una misma transacción para impedir doble reserva; la restricción y la prueba concurrente están pendientes.
2. M06 intenta el pago y garantía mediante un adaptador con clave idempotente. La respuesta se registra y se correlaciona con webhooks. Un timeout produce un estado por conciliar y no autoriza repetir el cargo con otra clave. La capacidad concreta del proveedor sigue sin verificar.
3. La decisión del arrendador condiciona M07. Solo una aprobación permite formalizar el contrato; ambas firmas exigidas habilitan el ingreso. Los plazos y excepciones siguen el proceso de 3.1 y las fichas de ES1.
4. M08–M10 registran uso, reclamo, resolución y liquidación. Una disputa abierta bloquea el cierre financiero; M11 conserva trazas de acciones críticas. El control físico de inmutabilidad de RNF-017 sigue sin resolver.

Los enlaces de 3.5 y la infraestructura de 3.6 soportan este recorrido. Los fallos de proveedores, la recuperación de base, el escalado y la protección de datos deben transformarse en casos de prueba de los capítulos V y VI; las metas RNF no son resultados alcanzados. La decisión de usar Cloud Run continúa condicionada por costo y portabilidad, y PostgreSQL responde a RNF-038.

*Tabla. Fallos previstos del recorrido y su tratamiento.* <!--#tab:es2-recorrido-fallos-->

| Paso | Fallo previsto | Comportamiento previsto | Qué queda registrado | Ensayo previsto |
| --- | --- | --- | --- | --- |
| Validar el intervalo | Dos solicitudes simultáneas sobre el mismo rango | Solo una confirma; la otra recibe rechazo por indisponibilidad | Intento rechazado con su correlación | PT-01, PT-02; MD-02, MD-07 |
| Pagar | Timeout sin respuesta del proveedor | Estado por conciliar; no se repite el cobro con otra clave | Intento, correlación y evento | PT-03, PT-04; MD-06 |
| Recibir el webhook | Evento duplicado o con firma inválida | El duplicado se deduplica; el inválido se rechaza sin procesar | Evento y motivo del rechazo | PT-04 |
| Retener la ocupación | Vence la retención antes del pago | Se libera el intervalo y la reserva se cancela por falta de pago | Transición y vencimiento | PT-03; MD-08 |
| Decidir el arrendador | Silencio durante 24 horas | Cancelación por vencimiento y devolución según la liquidación | Transición y temporizador | PT-05 |
| Firmar | Llega la fecha de inicio sin todas las firmas | Se cancela, se bloquea el ingreso y se reembolsa según la pasarela | Firmas faltantes y transición | PT-06 |
| Llamar a un proveedor | Pago, firma o identidad fuera de servicio | Reintentos acotados y degradación declarada; no se simula una verificación | Errores y reintentos | PT-03, PT-06 |
| Usar la base | Caída con conmutación o pérdida de datos | Conmutación según el servicio elegido; RPO y RTO por demostrar | Incidente y resultado de restauración | PT-11; MD-12 |
| Guardar evidencia | Carga parcial o archivo alterado | Se rechaza el documento sin hash válido y se conserva el intento | Metadatos y hash | PT-12 |
| Liquidar | Payout rechazado o disputa abierta | El cierre financiero queda pendiente y no se marca como confirmado | Estado por conciliar y fallo | PT-08 |
| Soportar carga | Pico por sobre la capacidad dimensionada | Escalado según RNF-019; el crecimiento de latencia está por medir | Métricas de la prueba | PT-09, PT-10 |

Ninguno de estos fallos se ha reproducido: la tabla describe el comportamiento diseñado y su ensayo previsto. La portabilidad de RNF-034–036 tampoco está demostrada; falta reproducir el recorrido en contenedores locales, sustituir el almacén de objetos por uno compatible, probar un PostgreSQL gestionado alternativo y reemplazar el servicio de secretos y la agenda. Esa evidencia exige que el producto exista y esté desplegado.

[[PENDIENTE: validar la secuencia completa con el equipo, reproducir los fallos de la tabla cuando exista producto, demostrar la portabilidad de RNF-034–036 y cerrar el diseño de continuidad junto con el ensayo de auditoría de 3.0.]]
