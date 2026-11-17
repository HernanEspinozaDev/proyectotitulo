# ANEXO E: CATÁLOGO DE CONTRATOS DE INTERFAZ OPENAPI

El catálogo histórico de referencia utiliza la especificación OpenAPI 3.1 y corresponde al corte de interfaces del 4 de noviembre de 2026. La base relativa es `/api/v1`. El catálogo distingue las rutas de ensayo local por el prefijo `/local`.

La infraestructura vigente se documenta en el corte técnico de infraestructura del 16 de noviembre [@espacigoaws2026]. El BFF utiliza la API por loopback en desarrollo y en el diseño co-ubicado de Fargate. Las operaciones de almacenamiento se resuelven mediante adaptadores S3 y autorización de aplicación. La aceptación del despliegue coteja la especificación de interfaz de ese corte con sus rutas y controles efectivos.

**Tabla E.1**\
*Operaciones representativas del corte de desarrollo*

| Ruta | Métodos declarados |
|---|---|
| `/public/spaces` | GET |
| `/spaces` | GET, POST |
| `/local/booking-trial/catalog` | GET |
| `/local/booking-trial/quotes` | POST |
| `/local/booking-trial/reservations` | GET, POST |
| `/local/booking-trial/reservations/{reservationId}/payment` | POST |

*Nota.* Elaboración propia a partir de la especificación OpenAPI versionada.

La consulta pública y la consulta de ensayo tienen rutas separadas. PT-09 requiere identificar cuál se mide, la versión del servicio y el conjunto de datos utilizado. El catálogo documenta un corte de la interfaz de desarrollo. Las rutas de ensayo permiten verificar contratos internos con datos sintéticos. La habilitación de una integración externa requiere evidencias de autorización, idempotencia, conciliación y devolución según la operación.

La instantánea OpenAPI fijada en este anexo registra ocho códigos en el contrato local de ese corte. La Tabla E.2 documenta las nueve categorías vigentes informadas para la memoria, incluida Inmuebles. La actualización versionada del esquema incorpora Inmuebles al catálogo de datos. El filtro `category_code` de `GET /local/booking-trial/catalog` conserva ocho códigos tanto en la instantánea citada como en la copia local consultada el 4 de noviembre. La Tabla E.2 describe el catálogo de producto de nueve categorías.

## Galería y control de portada en el corte local

El contrato de interfaz del 4 de noviembre de 2026 exige `If-Match` en `PUT /spaces/{spaceId}/cover`. La cabecera transporta un ETag fuerte ligado a la revisión del espacio. El manejador de galería del backend verificado exige esa revisión. Seleccionar portada conserva el carácter privado de los bytes y retirar la imagen elimina su selección en la misma transacción. El ADR fija hasta 30 posiciones, incluidas las cargas reservadas. Las constantes de los dominios de galería y medios del backend establecen un máximo de 30.

El registro local del asistente de publicación y galería del 4 de noviembre documenta un corte en ejecución. Registra respuestas de la API para autenticación, listado de espacios y categorías, además de una medición sintética de conversión de imágenes. La prueba autenticada conjunta de interfaz y galería, incluida la selección de portada con `If-Match`, y la comprobación de la publicación elegible requieren un registro de ejecución del recorrido integrado.

## Catálogo vigente de categorías

**Tabla E.2**\
*Categorías de espaciGo y atributos de publicación*

| Categoría | Uso | Atributos descriptivos |
|---|---|---|
| Oficina | Trabajo, atención de clientes o instalación temporal de un equipo. | Puestos, escritorios, mobiliario, salas de reunión, conectividad y climatización. |
| Sala multipropósito | Reuniones, talleres, capacitaciones y sesiones grupales. | Distribución, sillas, mesas, proyector, pantalla, videoconferencia y equipamiento. |
| Bodega | Almacenamiento de mercadería, equipos o materiales. | Altura y volumen útil, acceso, capacidad de carga, muelle y tipo de almacenamiento. |
| Estacionamiento | Estacionamiento de un vehículo durante el período contratado. | Dimensiones, altura, vehículos admitidos, cubierta, acceso y carga eléctrica. |
| Local flexible | Venta temporal, exhibición o atención al público. | Acceso desde la calle, vitrina, frente, mostradores, probadores, bodega de apoyo y servicios. |
| Stand | Puesto de feria, exhibición o promoción dentro de un recinto. | Dimensiones, lados abiertos, montaje, potencia eléctrica y mobiliario. |
| Quincho | Parrilladas, comidas y reuniones sociales. | Tipo y número de parrillas, cubierta, asientos, mesas, refrigerador y servicios. |
| Parcela de eventos | Encuentros o celebraciones en un predio con áreas exteriores y, cuando corresponde, cubiertas. | Superficies, estacionamientos, salón, cocina, piscina y acceso. |
| Inmuebles | Alojamiento o arriendo habitacional. Distingue casa, departamento, habitación y cabaña. | Tipo, modalidad, dormitorios, camas, baños, superficies, cocina, comodidades, convivencia y duración. |

*Nota.* Elaboración propia a partir del catálogo vigente confirmado por el proyecto. Los atributos describen el perfil de publicación. Las validaciones obligatorias y sus resultados se documentan por versión.

El tipo de espacio se distingue por la unidad que se arrienda y su uso. Un local flexible es un recinto comercial y un stand es un puesto. El quincho se caracteriza por el equipamiento para cocinar y reunirse, y la parcela de eventos por el conjunto del predio. La sala multipropósito se caracteriza por su configuración para actividades grupales y la oficina por sus puestos y condiciones de trabajo. El catálogo admite ampliaciones futuras mediante perfiles y verificaciones por versión.
