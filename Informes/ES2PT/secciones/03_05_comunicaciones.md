## Topología de comunicaciones

La topología propuesta separa un borde accesible por Internet de los datos operativos que requieren acceso restringido. Distingue solicitudes iniciadas por usuarios, llamadas salientes de la API y eventos entrantes de proveedores. Las flechas indican dirección lógica, no direcciones IP, puertos asignados ni una red ya desplegada [@es1formulacion; @es1anexoc].

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

El flujo de un webhook no se confunde con una respuesta síncrona de pago. La firma valida procedencia e integridad según el contrato del proveedor; la clave de idempotencia de RNF-012 evita duplicar una operación. Si una respuesta queda incierta, la conciliación de RNF-028 consulta el estado y conserva evidencia antes de cambiar la reserva. La fuente de verdad financiera externa y el estado local deben correlacionarse [@es1anexoc].

[[PENDIENTE: decidir dominio, entrada pública, proveedor de red, segmentación, puertos y servicio de secretos; validar autenticación de cada integración, cifrado interno y exposición mínima de webhooks con pruebas en un entorno autorizado.]]
