## Topología de comunicaciones

La topología propuesta separa un borde accesible por Internet de los datos operativos que requieren acceso restringido. Distingue solicitudes iniciadas por usuarios, llamadas salientes de la API y eventos entrantes de proveedores. Las flechas indican dirección lógica, no direcciones IP, puertos asignados ni una red ya desplegada.

![Topología lógica de comunicaciones](imagenes/figura-topologia_comunicaciones.png){width=6.3in} <!--#fig:es2-topologia--> <!--#fuente:elaboración propia a partir de ES1.-->

*Tabla. Canales propuestos y controles por definir.* <!--#tab:es2-canales-->

| Emisor → receptor | Datos y protocolo previstos | Límite de confianza y control |
| --- | --- | --- |
| Navegador → entrada pública → web | Páginas y acciones por HTTPS; TLS 1.2 o superior según RNF-015 | Autenticación y sesión para acciones privadas; tokens fuera de URL; dominio y terminación TLS por configurar |
| Frontend → API | JSON por HTTPS; contrato documentado con OpenAPI, RNF-032 | Validación de identidad, permisos y entradas en la API; origen permitido por definir |
| API → PostgreSQL/PostGIS | Consultas y transacciones sobre conexión de BD | Solo desde componentes autorizados; cifrado del enlace, cuentas y puertos según servicio elegido |
| API → archivos y analítica | Objetos y eventos mediante interfaz del servicio seleccionado | Acceso por rol, cifrado y retención; BigQuery no asegura por sí mismo RNF-017 |
| API → proveedores | Solicitudes HTTPS para pago, firma e identidad previstos | Credenciales fuera de URL y código; timeout de 5 segundos y hasta dos reintentos separados por 2 segundos en RNF-023, sujetos a la semántica de cada operación |
| Proveedor → entrada pública → API | Webhook HTTPS firmado, RNF-024 | Validar firma antes de procesar, deduplicar, conservar evento y aplicar hasta cinco reintentos de procesamiento con retroceso exponencial según la base |

El flujo de un webhook no se confunde con una respuesta síncrona de pago. La firma valida procedencia e integridad según el contrato del proveedor; la clave de idempotencia de RNF-012 evita duplicar una operación. Si una respuesta queda incierta, la conciliación de RNF-028 consulta el estado y conserva evidencia antes de cambiar la reserva. La fuente de verdad financiera externa y el estado local deben correlacionarse.

La integración financiera también requiere conciliar **cuatro importes distintos**: total pagado por el arrendatario, tarifa del procesador, comisión de EspaciGo y monto efectivamente recibido por el arrendador. La guía de Split 1:1 describe la tarifa del procesador descontada primero al vendedor y reembolsos limitados si su cuenta carece de saldo. Por tanto, confirmar el pago no basta para marcar como cumplida una devolución o una garantía. El adaptador propuesto guardará identificadores externos y estados separados para cobro, reparto y reverso; su funcionamiento real permanece sin ensayo [@es2mpsplitflujo].

### Decisiones de red propuestas

*Tabla. Decisiones de red y su estado.* <!--#tab:es2-red-decisiones-->

| Aspecto | Propuesta de ES2 | Estado y límite |
| --- | --- | --- |
| Dominio y entrada pública | Dominio propio con terminación TLS en el balanceador gestionado de 3.6 | Propuesta; registro y certificado sin tramitar |
| Proveedor de red | GCP, coherente con la plataforma de 3.6 | Condicionada a la aprobación de la región |
| Segmentación | Borde público para web y webhooks; base y archivos sin exposición a Internet | Propuesta; requiere red privada y reglas de salida |
| Puertos | 443 para todo el tráfico externo, sin puertos de base abiertos al público | Propuesta; el acceso administrativo a la base queda por definir |
| Cifrado interno | TLS con certificado gestionado o mTLS entre servicios y hacia la base | Propuesta; el protocolo del servicio elegido debe confirmarlo |
| Secretos | Servicio de secretos administrado, con credenciales rotables que nunca están en el repositorio ni en las imágenes | Propuesta; rotación y responsables pendientes |
| Webhooks | Una ruta por proveedor, firma verificada antes de procesar, cuerpo acotado y rechazo registrado sin secretos | Parcialmente cubierto por RNF-024; falta el contrato de cada proveedor |
| Origen permitido | Lista explícita de orígenes para la API y CORS restringido | Propuesta; los dominios de prueba y producción están por fijar |
| Correo saliente | Servicio de correo transaccional con dominio autenticado | Propuesta; sin proveedor elegido |

Ninguna de estas decisiones está implementada ni contratada, y el ensayo de saldos, reparto, reverso y garantía sigue requiriendo un entorno autorizado del proveedor.

[[PENDIENTE: aprobar dominio, proveedor de red, segmentación, puertos y servicio de secretos; validar la autenticación de cada integración con su contrato real y ensayar saldos, reparto, reverso y garantía en un entorno autorizado.]]
