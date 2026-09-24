## Herramientas, aplicaciones, lenguajes y componentes que serán implementados

El inventario inicial deriva de la arquitectura de la entrega anterior y del contraste documental de esta entrega. Las herramientas se presentan como componentes previstos; su inclusión no acredita instalación, despliegue ni integración del producto.

*Tabla. Inventario inicial de componentes previstos para EspaciGo.* <!--#tab:es2-inventario-tecnologico-->

| Componente | Función prevista | Alcance | Verificación pendiente |
| --- | --- | --- | --- |
| Next.js sobre React | Interfaz del catálogo y flujos de usuario | M01–M11 según interfaz | Versión, dependencias y prueba de interfaz |
| Go | API y reglas de negocio del backend modular | M01–M11 | Versión, estructura y pruebas del flujo seleccionado |
| PostgreSQL y PostGIS | Datos operativos y consulta geográfica | Reservas, publicaciones y relaciones transaccionales | Versión, alojamiento, esquema e índices |
| Docker | Construcción de imágenes para los componentes desplegables | Desarrollo y despliegue | Imágenes base, versiones y configuración |
| Cloud Run | Ejecución prevista de frontend y API | Infraestructura | Región, recursos, red y costo |
| BigQuery | Análisis y consulta de eventos previstos en ES1 | Auditoría M11 | Diseño que satisfaga RNF-017; no atribuir inmutabilidad automática |
| Almacenamiento de archivos | Contratos e imágenes de evidencia | M04, M07 y M08 | Servicio, acceso, cifrado, retención y costo |
| Mercado Pago | Procesamiento de pagos propuesto | M06 y M10 | Producto, acceso y compatibilidad del flujo financiero |
| FirmaVirtual | Servicio de firma propuesto | M07 | Modalidad, API y entorno de prueba |
| Registro Civil y SII | Verificación de identidad/empresa y servicios tributarios previstos | M03 y M10 según servicio | Acceso autorizado y capacidades de cada servicio |

**Nota.** Elaboración propia basada en ES1. Las integraciones externas permanecen sin verificación de acceso. La atribución de una función refleja la propuesta del proyecto, no una garantía del proveedor.

Docker distingue la imagen de su instancia en ejecución y advierte que los cambios sin almacenamiento persistente se pierden al eliminar el contenedor. En el diseño de EspaciGo se propone mantener la persistencia de datos y archivos separada del ciclo de vida de los contenedores y documentar la configuración de cada entorno [@es2dockeroverview].

La selección de hardware deberá contemplar las estaciones reales del equipo y los recursos de ejecución del prototipo: sistema operativo, CPU, memoria, almacenamiento y conectividad. Todavía no se dispone de ese inventario ni de mediciones para dimensionar la nube. Tampoco se fijan versiones a partir de la fecha de consulta de la documentación: se registrarán las efectivamente seleccionadas y probadas.

La documentación pública de Mercado Pago describe una integración de pagos divididos 1:1 con autorización OAuth del vendedor. Esa función no verifica por sí sola la retención, liberación y garantía previstas por ES1; también faltan condiciones de acceso y una prueba controlada para Chile [@es2mpsplit]. FirmaVirtual publica una API y menciona un entorno de pruebas, pero el acceso del equipo, el tipo de firma requerido y el flujo contractual siguen sin demostrarse [@es2firmavirtualapi].

El comprador podría escoger tarjeta, transferencia u otro medio compatible **dentro** de Checkout Pro, mientras el arrendador autoriza el split y la comisión pactada. Esto no exige mostrarle varias pasarelas. La comparación documental de pasarelas deja Mercado Pago Split como candidato sujeto a prueba; Stripe no lista Chile para operar Payments, la información pública de Haulmer/TUU no acredita un split de marketplace y Flow ofrece diversos medios, pero falta verificar reparto contractual. Incorporar otra pasarela requiere reproducir cobro, reverso, conciliación y garantía, además de confirmar sus métodos efectivos [@es2mpsplit; @es2mptarifas; @es2stripeglobal; @es2haulmerterminos; @es2flowmetodos].

La revisión documental de proveedores encuentra que Flow documenta `merchantId` para un comercio integrador y alta de comercios asociados; esa API **no acredita por sí sola** que liquide una comisión configurable al RUT de EspaciGo en el mismo pago. TUU mantiene la misma brecha de prueba para un producto online. Mercado Pago sí documenta el reparto 1:1 y reportes de tarifa, comisión y neto, pero descuenta primero su tarifa al vendedor y condiciona el reembolso completo a saldo suficiente. Se requiere contrato y ensayo de dos cuentas con cobro, conciliación, reembolso y garantía antes de cerrar el diseño [@es2flowapi; @es2mpsplitflujo; @es2mpreporte].

El SII ofrece una consulta pública de situación tributaria de terceros; esa página no establece una API habilitada para el proyecto ni cubre toda la verificación KYB [@es2siiconsulta]. Un convenio de interoperabilidad entre organismos públicos muestra que existen mecanismos institucionales para verificar datos del Registro Civil, pero no acredita acceso de EspaciGo [@es2sii195]. Estas cuatro dependencias continúan como **propuestas**; no hay pruebas de integración ejecutadas.

Para cada componente se completará una ficha con versión, licencia o términos de servicio, entorno, responsable, dependencia, costo y evidencia. Los servicios de integración requerirán además registrar la diferencia entre funcionamiento real y simulación de pruebas. Los secretos de acceso se gestionarán fuera del informe.

*Tabla. Fichas de versiones, licencias y herramientas previstas.* <!--#tab:es2-fichas-tecnologicas-->

| Componente | Familia y versión objetivo | Licencia o términos | Fuente consultada | Qué falta registrar |
| --- | --- | --- | --- | --- |
| Next.js sobre React | 16.x, rama en soporte activo | MIT | [@es2nextsupport; @es2nextlicense] | Parche e imagen efectivamente instalados |
| Node.js | 24 LTS para la ejecución objetivo | Licencia del proyecto; el paquete incluye bibliotecas de terceros con licencias propias | [@es2nodereleases; @es2nodelicense] | Parche fijado al instalar |
| Go | 1.26.x | Licencia permisiva de tipo BSD | [@es2gorelease26; @es2golicense] | Comprobar soporte al construir |
| PostgreSQL | 17.x, rama soportada | Licencia PostgreSQL, liberal y similar a BSD o MIT | [@es2pgversions; @es2pglicense] | Parche vigente al desplegar |
| PostGIS | 3.5.2 sobre PostgreSQL 17, con `btree_gist` | GPLv2 para la extensión; usarla por consultas no es distribuir una modificación | [@es2cloudsqlextensions; @es2postgislicense] | Disponibilidad particular en la instancia contratada |
| Docker | Engine sobre Linux como propuesta; Desktop queda opcional | La información promocional y los términos de uso consultados no coinciden en alcance: no se declara gratuidad contractual para tres integrantes coordinados | [@es2dockeroverview; @es2dockerlegal] | Licencias de las piezas elegidas |
| Cloud Run, Cloud SQL, Cloud Storage y Secret Manager | Servicios administrados en Santiago | Términos de servicio del proveedor; el IVA y el crédito fiscal dependen de la cuenta y del comprobante | [@es2cloudrunpricing; @es2cloudsqlpricing; @es2gcspricing; @es2gcpvat] | SKU, factura y tratamiento tributario |
| Herramientas de desarrollo, prueba e integración | Control de versiones, revisión por rama, pruebas automáticas y verificación de privacidad en el flujo de integración, según el capítulo V | Propuesta del equipo; sin contrato ni proveedor adjudicado en esta entrega | Capítulo V de este informe | Repositorio, flujo y evidencia de ejecución |
| Alojamiento de datos y archivos | Cloud SQL con PostgreSQL/PostGIS y Cloud Storage; secretos en Secret Manager | Términos del proveedor | [@es2cloudsqlpricing; @es2gcspricing] | Configuración desplegada y costo real |
| Estaciones de trabajo | Tres estaciones supuestas de 4 núcleos, 16 GB de memoria y SSD de 512 GB, con al menos 80 GB libres | No aplica | SUP-05 | Inventario físico real del equipo |

**Nota.** Elaboración propia a partir de la documentación citada y del registro de selección de tecnologías. Las familias y parches objetivo son un **supuesto de trabajo** (SUP-05): no acreditan instalación, compatibilidad probada ni inventario levantado, y los parches se fijan al instalar. La tabla delimita qué está verificado con fuente primaria y qué requiere trabajo físico o comercial.

**Estado del inventario.** Con las familias objetivo, las licencias verificadas, el alojamiento y las herramientas definidas, la parte documental de esta ficha queda cerrada y el inventario deja de ser una lista de nombres. Lo que no puede cerrarse sin trabajo físico o comercial es concreto: el **inventario real de las estaciones**, el **parche y la imagen efectivamente instalados** con su archivo de dependencias, la **disponibilidad particular de PostGIS** en la instancia contratada y las **respuestas de acceso** de Mercado Pago, FirmaVirtual, Registro Civil y SII. Todo eso se conserva como obligación abierta en las secciones de terceros y de producto de [pendientes](../pendientes.md), no como cumplida.

### Relación con la evaluación de costos

El Anexo A distingue trabajo inicial, operación fija y consumo por reserva. Sus asignaciones a nube, pagos, firma e identidad son hipótesis de cálculo; no confirman tarifas ni acceso. Cada servicio debe registrar producto/versión, unidad de cobro, región, moneda, fecha, impuestos, cuota incluida, sobreconsumo y habilitación. El TCO debe sumar respaldos, seguridad, observabilidad, privacidad y administración. Una dependencia con tarifa desconocida no se registra como gratuita ni se considera cubierta por la provisión cloud.

La referencia vigente, recalculada con las tarifas publicadas por Google Cloud para Santiago, desglosa Cloud SQL, Cloud Run, Storage, balanceo, Armor y provisiones auxiliares. Para el piloto equivale a **USD 237,82** mensuales con tarifas de Santiago, por decisión del usuario del 23-09-2026; ya no se usa la reserva regional del 35 % sobre precios de Iowa, y USD/CLP = 1.000 junto con el IVA del 19 % siguen siendo supuestos, no precios contratados. El perfil de ensayo reduce horas de SQL, pero no sustituye el piloto público ni acredita disponibilidad o recuperación [@es2cloudsqlpricing; @es2cloudrunpricing; @es2gcspricing; @es2lbpricing; @es2armorpricing].

La página pública de Checkout de Mercado Pago anuncia una tarifa general inmediata de 3,19 % más IVA. El ejercicio aplica esa tasa al arriendo más la comisión cobrada en el mismo pago, por lo que el costo aumenta con el importe del tercero; **no** es una tarifa confirmada para Split, custodia ni liberación condicionada. La guía publicada de Split 1:1 indica que la tarifa se descuenta primero al vendedor, mientras el presupuesto asigna su incidencia económica a EspaciGo: falta definir si se compensará al vendedor o se ajustará el precio y cómo se documentará tributariamente. El proveedor también condiciona reembolsos al saldo del vendedor. FirmaVirtual publica una tarifa por documento FES, distinta de una cotización API; la identidad por usuario y sus datos requieren evaluación. Antes de escoger proveedores hay que probar cobro, reparto, reverso, garantía y conciliación con condiciones escritas [@es2mptarifas; @es2mpsplitflujo; @es2firmavirtualprecios; @es2firmavirtualapi].
