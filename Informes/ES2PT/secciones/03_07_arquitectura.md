## Diagrama de arquitectura

La vista integrada conecta presentación, módulos, persistencia e integraciones. Es un diseño lógico asociado a contenedores y servicios virtuales propuestos en 3.6; no representa instancias construidas. El backend Go conserva una sola unidad desplegable con módulos por dominio y adaptadores para terceros, como se explica en 3.3 [@es1formulacion; @es1anexoc].

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
2. M06 intenta el pago y garantía mediante un adaptador con clave idempotente. La respuesta se registra y se correlaciona con webhooks. Un timeout produce un estado por conciliar y no autoriza repetir el cargo con otra clave. La capacidad concreta del proveedor sigue abierta en INV-003.
3. La decisión del arrendador condiciona M07. Solo una aprobación permite formalizar el contrato; ambas firmas exigidas habilitan el ingreso. Los plazos y excepciones siguen el proceso de 3.1 y las fichas de ES1.
4. M08–M10 registran uso, reclamo, resolución y liquidación. Una disputa abierta bloquea el cierre financiero; M11 conserva trazas de acciones críticas. El control físico de inmutabilidad de RNF-017 sigue sin resolver.

Los enlaces de 3.5 y la infraestructura de 3.6 soportan este recorrido. Los fallos de proveedores, la recuperación de base, el escalado y la protección de datos deben transformarse en casos de prueba de los capítulos V y VI; las metas RNF no son resultados alcanzados. La decisión de usar Cloud Run continúa condicionada por costo y portabilidad, y PostgreSQL responde a RNF-038 [@es1anexoc].

[[PENDIENTE: acordar despliegue e interfaces con el equipo, validar secuencia completa y fallos de reserva en el producto, demostrar portabilidad y cerrar el diseño de auditoría y continuidad.]]
