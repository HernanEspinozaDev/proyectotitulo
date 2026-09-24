# Costos de infraestructura, formalización y autofinanciación

## Alcance y actualización del escenario

Esta versión reemplaza la conclusión económica preliminar del primer ejercicio. El usuario confirmó que **todavía no existen ingresos** y que los tres integrantes financiarían EspaciGo con dinero propio y trabajo sin remuneración inicial. Se estudia una SpA con participación igualitaria; no se ha constituido ni se han contratado servicios. ES1 permanece como entrega cerrada.

Se distinguen tres magnitudes: **gasto/costo neto**, **dinero que sale de caja**, que puede incluir IVA recuperable, y **costo de oportunidad del equipo**. El aporte de un socio financia caja; no es una venta. Un valor positivo de ventas simuladas no acredita clientes ni implementación.

La orientación de preparación y evaluación de proyectos de Sapag se aplica separando mercado, ingeniería, inversión, operación, liquidez y riesgo. Las referencias públicas del libro no sustituyen una lectura íntegra; el modelo numérico es elaboración propia [@es2sapag2014]. Las fuentes y cotizaciones pendientes están identificadas en el listado de partidas.

Para evitar anticipar ventas se adopta un primer año completo sin ingresos: meses 1–6 de ensayo y 7–12 de piloto, seguido de volúmenes comerciales hipotéticos. No se han confirmado fecha de lanzamiento ni 12 meses sin ventas: son convenciones de simulación. No se modifican RF/RNF para abaratar la propuesta.

## Infraestructura planteada y costo mensual

Se conservan Next.js, Go, PostgreSQL/PostGIS, Docker y GCP como candidatos de la base. Next.js y Go corresponden a **dos servicios**; la carga Cloud Run indicada es el agregado de ambos. PostgreSQL administrado se modela en Cloud SQL Enterprise General Purpose. La elección de recursos es una hipótesis de costos, no un dimensionamiento certificado.

La referencia tarifaria vigente es **Santiago (`southamerica-west1`)**, adoptada por decisión del usuario del 23-09-2026 y respaldada con las tarifas publicadas por Google Cloud para esa región. Se presupuestan USD/CLP = 1.000 y un **19 % de IVA** adicional como antes, pero ya **no se aplica la provisión regional del 35 %** que usaba la referencia de Iowa: las partidas con tarifa publicada están expresadas directamente en precios de Santiago. Las únicas provisiones que se conservan son las bolsas sin cotización —registros, compilación, secretos, correo y staging— y los supuestos de salida, procesamiento y respaldo, identificados como tales. Elegir región obliga además a revisar latencia y transferencias internacionales de datos bajo los criterios de privacidad de ES2 [@es2cloudsqlpricing; @es2cloudrunpricing; @es2gcspricing].

**Efecto histórico del cambio de región.** Aplicar los precios de Santiago a las mismas cantidades **rebajó** el presupuesto respecto de la estimación anterior: en el piloto, de USD 259,78 netos (192,43 de Iowa con provisión del 35 %) a **USD 237,82**, y en esa versión con domicilio LOF el flujo del primer año pasó de una salida de 5.052.056 CLP a **4.889.743 CLP**. El presupuesto vigente cambió después a Oficina Express y se presenta más adelante. La provisión del 35 % se aplicaba también a partidas sin relación con el alza regional —salida de datos, balanceador, Armor, correo y bolsas de provisión, con precio igual o sin tarifa regional— y resultaba más cara que el alza publicada de las partidas que sí dependen de la región (1,40 en cómputo y base; 1,90 en almacenamiento). Es un resultado aritmético de comparar la provisión con la tarifa, no una mejora de capacidad ni una medición.

*Tabla. Perfiles de infraestructura para simulación.* <!--#tab:es2-perfiles-costos-->

| Perfil | Configuración de costo | Uso y límite |
| --- | --- | --- |
| Ensayo | SQL 1 vCPU/4 GiB activo 160 h/mes; disco 10 GiB; copias 10 GiB; 100.000 solicitudes agregadas | Pruebas controladas con datos sintéticos, acceso restringido y desarrollo local; sin balanceador público/WAF. No es operación comercial ni acredita los RNF de producción |
| Piloto | SQL 2 vCPU/8 GiB 730 h/mes; SSD 20 GiB; copias 20 GiB; 1 millón solicitudes; objetos 50 GiB; salida 100 GiB | Un entorno activo y bolsa para staging separado; balanceador HTTPS y cinco reglas WAF. SQL zonal, sin HA; no demuestra 99,9 % extremo a extremo |
| HA de referencia | SQL con recursos de HA equivalentes a 2 vCPU/8 GiB primarios; almacenamiento facturado duplicado; copias 40 GiB; 5 millones solicitudes; objetos 200 GiB; salida 300 GiB | Mayor resiliencia presupuestada, sin afirmar capacidad, RPO/RTO o SLA comprobados |

El perfil piloto computa 200.000 vCPU-s y 100.000 GiB-s activos por mes (supuesto agregado equivalente a 0,2 s y 0,5 GiB por solicitud, sin asumir ahorro por concurrencia). Cloud Run tiene mínimos en cero; no se modelan instancias permanentemente calientes. La base SQL sí funciona todo el mes. No se utiliza un conector VPC dedicado; su necesidad o la de NAT obligaría a agregar costos. El total se calcula sin descuentos gratuitos ni créditos promocionales [@es2cloudrunpricing].

*Tabla. Desglose mensual del piloto, tarifas de Santiago en USD antes de IVA.* <!--#tab:es2-infra-desglose-->

| Partida | Base mensual | USD | Calidad del dato |
| --- | --- | --- | --- |
| SQL CPU | 2 × 730 h × 0,05782 | 84,42 | Tarifa zonal de Santiago |
| SQL RAM | 8 × 730 h × 0,0098 | 57,23 | Tarifa zonal de Santiago |
| SQL SSD | 20 GiB × 730 h × 0,000326027 | 4,76 | Tarifa zonal de Santiago |
| SQL copias utilizadas | 20 GiB × 730 h × 0,000153425 | 2,24 | Tarifa de Santiago; el supuesto doble de HA es conservador |
| Cloud Run, dos servicios | CPU 6,72 + memoria 0,35 + solicitudes 0,40 | 7,47 | Tarifa de Santiago sin nivel gratuito |
| Archivos en Cloud Storage | 50 GiB × 730 h × 0,000052055 | 1,90 | Almacenamiento; operaciones aparte |
| Salida de datos | 100 GiB × USD 0,20 | 20,00 | Supuesto; precio global igual en ambas regiones |
| Balanceador y procesamiento | 730 h × 0,025 + provisión 0,80 | 19,05 | Precio global igual; procesamiento estimado |
| Cloud Armor Standard | 1 política + 5 reglas + 1 millón solicitudes | 10,75 | Precio global; no Enterprise |
| Logs y BigQuery | Bolsa mensual | 5,00 | Provisión; no retención ilimitada |
| Build y Artifact Registry | Bolsa mensual | 3,00 | Provisión |
| Secretos, DNS y agenda | Bolsa mensual | 2,00 | Provisión |
| Correo transaccional | Bolsa mensual | 10,00 | Proveedor y volumen por cotizar |
| Staging aislado | SQL 40 h + disco + ejecución breve | 10,00 | Provisión, no segundo ambiente 24/7 |

**Total de referencia: USD 237,82/mes.** Fuentes tarifarias: precios publicados por Google Cloud para Cloud SQL, Cloud Run, Storage, Load Balancing y Armor; los supuestos están identificados y no se atribuyen al proveedor [@es2cloudsqlpricing; @es2cloudrunpricing; @es2gcspricing; @es2lbpricing; @es2armorpricing].

*Tabla. Presupuesto mensual de caja por perfil.* <!--#tab:es2-infra-caja-->

| Perfil | USD de referencia | CLP netos, tarifas de Santiago | CLP de caja, con 19 % adicional |
| --- | --- | --- | --- |
| ensayo | 24,65 | 24.650 | 29.334 |
| piloto | 237,82 | 237.819 | 283.005 |
| ha | 494,65 | 494.648 | 588.632 |

**Nota.** El 19 % se reserva como necesidad de caja bajo el supuesto de facturación afecta; el mecanismo real de IVA de servicios extranjeros y su crédito debe revisarse. El IVA es adicional a las tarifas y no reemplaza ninguna provisión. Cada fila de precio/cantidad está en `supuestos_bootstrap.json`. No se suman automáticamente los tres perfiles: se usa uno por mes. El perfil de alta disponibilidad de USD 494,65 y el comparador documental de USD 384,23 usan cargas, cantidades de almacenamiento y respaldos distintas; no se debe atribuir la diferencia a componentes que el comparador ya incluye.

Como control de ingeniería, se compara **otra configuración** con carga mensual común de 1 millón de solicitudes y Cloud SQL HA en Iowa: USD 297,01/mes para Cloud Run sin mínimos frente a USD 393,39/mes para dos VM E2, antes de IVA. Ese ejercicio conserva sus precios de Iowa como comparación documental y no se reescribe con la decisión regional. El piloto de esta tabla usa SQL zonal, de modo que la variante HA no forma parte del flujo base: cambiar a disponibilidad completa exige la diferencia presupuestaria correspondiente y una prueba de capacidad. Cloud Run con una o dos instancias mínimas, discos y operación de VM, salida de datos y costos de producción se detallan en el ejercicio comparativo; la equivalencia de rendimiento permanece sin prueba [@es2cloudrunpricing; @es2computeprecios; @es2cloudsqlpricing].

La simulación de 6 meses ensayo + 6 piloto supone aproximadamente **1.874.031 CLP** de caja cloud durante el año 1. Doce meses completos de piloto elevan esa partida a **3.396.058 CLP**. SSL administrado, equipos existentes y herramientas sin suscripción adicional no reciben aquí un cobro inventado, pero falta validar licencias y disponibilidad real. No se incluye soporte enterprise, segunda región de recuperación, SMS masivo, penetración externa ni hardware nuevo; requieren presupuesto si el diseño los necesita. Backups, WAF o BigQuery no acreditan por sí solos restauración ni auditoría inmutable.

## SpA de tres integrantes y reparto de acciones

Se propone, para discusión del equipo, una sola serie de **3.000 acciones ordinarias**, con **1.000 para cada fundador**, equivalentes exactamente a un tercio. No es necesario repartir 33/33/34 ni dejar acciones sueltas. Un capital social ilustrativo de 3.000.000 CLP corresponde a aporte de 1.000.000 por persona y valor de suscripción inicial de 1.000 por acción. La cifra se ajustará al compromiso efectivamente pagable; no determina el valor comercial futuro de EspaciGo.

| Integrante | Acciones propuestas | Participación | Aporte al capital ilustrativo |
| --- | ---: | --- | ---: |
| Hernán Espinoza | 1.000 | 1/3 | 1.000.000 CLP |
| Anita Marchant | 1.000 | 1/3 | 1.000.000 CLP |
| Erick Silva | 1.000 | 1/3 | 1.000.000 CLP |
| Total | 3.000 | 100 % | 3.000.000 CLP |

El RES exige acciones enteras y permite definir acciones en reserva, pero no obliga a usarlas. Para este caso se propone no reservarlas sin un objetivo concreto. Si posteriormente se emiten 750 acciones a un inversionista, las 3.750 totales dejarían a cada fundador con 26,6667 % y al nuevo con 20 %; el precio de esa emisión se negocia, no se deduce del valor inicial. Una emisión aporta fondos a la sociedad; vender acciones personales no produce automáticamente caja para la empresa [@es2resacciones].

**Trabajo no es capital pagado:** el RES excluye el aporte de trabajo o industria. Valorar horas para evaluar el proyecto no autoriza declarar ese importe como capital social enterado. Un software o derecho patrimonial existente exigiría documentar titularidad, transferencia y valoración, distinto de prometer trabajo futuro [@es2resacciones].

El pacto y estatutos deberían revisar dedicación, propiedad intelectual del código, administradores/poderes, autorización de gastos, préstamos entre socios, salida de un fundador, transferencia de acciones, dilución y resolución de desacuerdos. Igual participación no resuelve por sí sola esos problemas. La propuesta es material para revisión profesional y acuerdo de los tres, no estatutos listos para firmar. No se asignan cargos por inferencia.

## Actividad SII, régimen e impuestos

La propuesta de actividades para iniciar la futura SpA, elegida por el equipo, es **631200 — Portales web** como principal y **731001 — Servicios de publicidad prestados por empresas** como complementaria para el destaque previsto. No supone que los destaques ya se vendan; su ingreso permanece en cero. **682000 — Actividades inmobiliarias realizadas a cambio de una retribución o por contrata** no integra esta propuesta inicial. La clasificación oficial describe 6312 como explotación de portales y 6820 como intermediación remunerada del alquiler de bienes inmuebles. Puesto que el modelo también cobra **comisión por reserva** y abarca distintos tipos de espacio, se debe preguntar al contador/SII si 631200 cubre esa prestación concreta o si corresponde incorporar 682000 u otra actividad; no se deduce la respuesta de la interfaz ni se altera el modelo para justificar un código. 620100 correspondería a programación vendida a terceros, no al desarrollo interno [@es2siiactividades; @es2ineciiu].

**731001 forma parte de la propuesta de inscripción**, pero todavía no hay venta ni documento emitido por destaques. El catálogo SII identifica esa actividad como primera categoría afecta a IVA; la interpretación de un oficio sobre publicidad en aplicación móvil orienta, pero no decide el caso concreto de EspaciGo. La factura o boleta del destaque, la comisión de la plataforma y el documento del arriendo deben analizarse por separado, incluidas devoluciones y la función del voucher de pago. Se proyecta **una patente comercial para la SpA en un domicilio**, no una por cada código [@es2siicatalogo; @es2siipublicidadapp; @es2rentasmunicipales].

Se modela IVA del 19 % sobre la comisión de la SpA. No se aplica la exención de sociedad de profesionales por tener socios del área informática; forma societaria, giro, régimen de renta e IVA son decisiones distintas [@es2siiivaservicios]. El arriendo se representa como un monto final a pagar al propietario: su tratamiento tributario propio no se resuelve en este ejemplo.

**Pro Pyme General** es el primer régimen a estudiar según requisitos reales, no una inscripción ya acordada. La tabla SII consultada informa 12,5 % para ejercicios comerciales 2026/2027 y 15 % para 2028 en ese régimen. El 27 % solicitado se conserva como **escenario académico comparativo**, no como obligación derivada de constituir una SpA. Como los años operativos aún no tienen calendario, no se asignan tasas legales futuras automáticamente [@es2siipro_pyme; @es2siitasas].

No tener ventas no elimina contabilidad ni declaraciones: si existen compras con crédito fiscal, no corresponde describir todo el período como «sin movimiento». El crédito IVA puede acumularse, pero no se trata como dinero reembolsado. El modelo reserva IVA mensual y un PPM supuesto de 0,25 % de ingresos propios netos, regularizado contra el IDPC calculado sin duplicarlo. **Ese PPM no es una tasa legal confirmada para EspaciGo.** Se debe sustituir al elegir régimen y fechas. No se modelan arrastre de pérdidas tributarias, corrección monetaria ni impuestos personales; no hay escudo tributario por el trabajo gratuito [@es2siif29].

## Oficina virtual y patente en Santiago Centro

Se compararon tres ofertas públicas; no se contrataron ni se solicitaron aprobaciones. Por su precio y contratación digital, **Oficina Express es la opción elegida para presupuestar**, condicionada a confirmar el contrato y la aceptación municipal del domicilio:

| Alternativa | Dirección publicada | Precio y condiciones consultadas |
| --- | --- | --- |
| Oficina Express, anual | Ahumada 131, Santiago Centro; oficina exacta por confirmar | 50.000 CLP/año IVA incluido + 5.000 CLP únicos por firma electrónica simple del contrato; dirección y correspondencia, sin sala ni puesto físico; opción presupuestada |
| LOF, Plan Básico | Av. Libertador Bernardo O'Higgins 1302, oficina 70 | 119.000 CLP/año, proveedor declara exención de IVA; comparador anterior |
| DVirtual | Teatinos 251, oficina 610 figura como domicilio del proveedor; confirmar dirección contractual ofrecida | 6.500 CLP por cargo mensual IVA incluido + firma online 9.800; 12 cargos + firma = 87.800 CLP; condiciones de renovación y término publicadas |

La diferencia anual no debe decidir por sí sola: confirmar que **631200 y 731001**, junto con el objeto contractual, son compatibles con Ahumada 131, qué derecho de uso acredita el proveedor y qué exige la Municipalidad de Santiago. También se consultará si la comisión exige clasificar otra actividad. El proveedor anuncia contratación en minutos, no obtención garantizada de patente. La publicidad de domicilio válido no equivale a una patente aprobada. No se trata de arrendar físicamente el espacio comercial que usarían los clientes; esa es otra operación del marketplace [@es2oficinaexpress; @es2lofvirtual; @es2dvirtual; @es2patenteagil].

La patente municipal se estima mediante `máximo(1 UTM, tasa municipal × capital propio tributario)`, dentro de los límites legales. Para ilustrar, si el capital propio relevante fuera 3.000.000 CLP, el rango legal **2,5–5 por mil (0,25–0,50 %)** daría 7.500–15.000 CLP, inferior a una UTM. Se presupuesta entonces **71.721 CLP por doce meses**, referencia UTM de septiembre de 2026. Cinco por mil **no es 5 %**. Una empresa en un lugar no paga una patente por cada código SII; el artículo 24 considera la actividad con independencia del número de giros. No es la liquidación municipal ni equivale a cobrar una UTM en cada semestre. Capital propio tributario y capital estatutario no son necesariamente iguales [@es2rentasmunicipales; @es2utm2026].

El ciclo legal es julio–junio con pago en julio/enero; el modelo de caja reserva el monto anual en el mes 1 para no subfinanciarse. Fecha de inicio, eventuales proporciones y liquidación real quedan pendientes. Se conserva **120.000 CLP/año como provisión de aseo**, sin afirmarla como tarifa ni deuda de esa oficina. La ordenanza 2026 publica **2,88 UTM/año (≈206.556 CLP a septiembre) para actividad económica diurna**, pero debe confirmarse si se cobra a esta SpA o al titular de la oficina virtual y evitar duplicarlo. Si correspondiera la tarifa completa a EspaciGo, sustituiría la provisión, no se sumaría a ella. La solicitud se tramita ante la Municipalidad de Santiago [@es2ordenanza94; @es2patentesstgo; @es2utm2026].

La conversación aportada para este análisis suponía que una oficina virtual omite automáticamente la Dirección de Obras Municipales (DOM). El portal municipal permite consultar zonificación y la ordenanza contempla, **solo si se solicitan o exigen**, informe de prefactibilidad de actividades productivas de **0,15 UTM (≈10.758 CLP)** y certificado de informaciones previas con planchetas de **0,35 UTM (≈25.102 CLP)**. Ambos sumarían **0,50 UTM (≈35.861 CLP)** en un caso condicional; no son un cargo automático de la patente ni necesariamente del arrendatario virtual. Patente Ágil anuncia tramitación general más rápida, sin garantizar aceptación de esta dirección o prescindir de verificaciones DOM. No se incorporan los derechos DOM al caso base hasta que el municipio indique cuáles exige [@es2ordenanza94; @es2patentesstgo; @es2patenteagil].

## Formalización, administración y gastos del primer año

El registro electrónico de constitución es gratuito; la firma y asesoría pueden costar. El RES publica 0,26 UF por acto de firma ante un mismo notario, cualquiera sea el número de comparecientes, con adicionales documentales posibles. Por ello se reserva 15.000 CLP para la firma de constitución, no tres aranceles automáticos. El IVA de honorarios se presupuesta suponiendo prestador afecto; si cambia el documento, deben recalcularse montos y créditos [@es2rescostos].

*Tabla. Caja inicial de preparación, una sola vez.* <!--#tab:es2-formalizacion-inicial-->

| Partida | CLP netos o finales sin IVA | CLP de caja | Estado |
| --- | --- | --- | --- |
| estatutos pacto ip | 350.000 | 416.500 | provisión asesoría, no arancel |
| terminos privacidad contratos | 350.000 | 416.500 | provisión asesoría Ley 21719, no cotización |
| habilitacion contable | 100.000 | 119.000 | provisión profesional; inicio SII no tarifado aquí |
| firma constitucion | 15.000 | 15.000 | provisión; RES publica 0,26UF por acto ante mismo notario, extras posibles |
| firma domicilio | 4.202 | 5.000 | FES única de Oficina Express, IVA incluido; DTE y crédito por confirmar |
| documentos traslados | 50.000 | 50.000 | provisión privada, no derecho municipal de otorgamiento |

**Total inicial: 1.022.000 CLP de caja.** Honorarios son provisiones por cotizar; documentos/traslados no representan un arancel municipal de otorgamiento. La firma de domicilio se distingue de la firma de constitución y de los contratos de arriendo. El proveedor publica 5.000 CLP finales por contrato y aún no hay DTE [@es2oficinaexpress].

*Tabla. Gastos de operación y administración del año 1.* <!--#tab:es2-gastos-bootstrap-->

| Partida | Frecuencia | Caja año 1, CLP | Calidad del dato |
| --- | --- | --- | --- |
| contabilidad | 12 meses | 714.000 | Supuesto, no cotización |
| correo corporativo | 12 meses | 214.200 | Supuesto, no cotización |
| conectividad incremental | 12 meses | 180.000 | Supuesto, no cotización |
| banco | 12 meses | 60.000 | Supuesto, no cotización |
| captacion | 6 meses | 357.000 | Supuesto, no cotización |
| oficina virtual | 1 año / reserva anual | 50.000 | Oficina Express anual, IVA incluido, sin contratar; renovación futura indexada solo en el modelo |
| dominio cl | 1 año / reserva anual | 9.990 | NIC Chile, un año exento |
| certificado tributario | 1 año / reserva anual | 23.800 | provisión sin proveedor adjudicado |
| patente anual | 1 año / reserva anual | 71.721 | mínimo anual 1UTM referencia septiembre2026; fecha/cálculo municipal pendientes |
| aseo | 1 año / reserva anual | 120.000 | provisión municipal no verificada; puede variar o no corresponder |
| cierre renta | 1 año / reserva anual | 119.000 | provisión honorario anual independiente, no impuesto ni fecha legal de declaración |
| Infraestructura | 6 ensayo + 6 piloto | 1.874.031 | Tarifas de Santiago + provisiones auxiliares + IVA |

**Operación año 1: 3.793.743 CLP. Con preparación inicial: 4.815.743 CLP.** El domicilio reduce 69.000 CLP de operación y su firma 5.000 CLP de preparación frente al escenario LOF anterior. El dominio usa precio NIC vigente; el cierre contable se reserva al mes 12 y se presupone fuera del honorario mensual, para evitar duplicarlo si una cotización lo incluye [@es2nictarifas; @es2oficinaexpress].

Como gasto opcional separado, registrar marca cuesta 3 UTM por clase en derechos INAPI (1 al inicio y 2 al aceptarse), más publicación. A la UTM usada son 215.163 CLP, más una provisión ilustrativa de 30.000 para publicación, sin honorarios: **245.163 CLP adicionales**. No se incluye en el total base porque faltan clases y decisión de tramitar; buscar nombre y pagar dominio no registra una marca [@es2inapitasas]. Tampoco se incluyen computadores nuevos ni gastos personales de subsistencia: inventariarlos y financiarlos por separado si son necesarios.

## Trabajo fundador, caja y capital requerido

**Sueldos pagados: cero** en el escenario bootstrap base. No se reconoce automáticamente una obligación salarial por horas voluntarias ni se presume una relación laboral; si se contrata a alguien, deben incorporarse sus obligaciones reales. Para valorar el esfuerzo se supone, sin confirmar disponibilidad, 3 personas × 20 h/semana × 48 semanas × 15.000 CLP/h = **43.200.000 CLP el año 1**. No se suma además el desarrollo de 14.400.000 CLP de ES1: aquel estimaba 16 semanas y aquí sería parte del mismo tiempo. En los años 2–3 se suponen 10 h/semana por fundador, con tarifa indexada al 4 %.

Los gastos propios habituales, equipos ya disponibles y trabajo ya incurrido no se convierten automáticamente en nueva salida incremental. Si los fundadores deben dejar ingresos alternativos para dedicar esas horas, esa restricción personal puede impedir ejecutar el plan aunque la caja empresarial alcance.

El primer año demanda **4.815.743 CLP**, sin sueldos. Con colchón de caja del 20 %, el fondo objetivo es **5.778.891 CLP**, o aproximadamente **1.926.297 por fundador** si aportan igual. El colchón es dinero disponible ante contingencias, no gasto realizado ni deducción tributaria.

Con capital ilustrativo de 3.000.000 CLP, falta financiar **2.778.891 CLP** para alcanzar ese fondo (5.778.891 − 3.000.000). Puede revisarse un capital mayor o préstamos documentados de socios; el acuerdo debe distinguir titularidad de acciones, aporte pagado, deuda y condiciones de devolución. No se atribuyen intereses ni devolución en este flujo del proyecto anterior al financiamiento.

La caja alcanza su déficit máximo de **6.246.529 CLP en el mes 19**. Por tanto, financiar solo el primer año no basta para todo el arranque. Con 20 % de margen sobre ese déficit, la reserva para atravesar los 36 meses sería **7.495.835 CLP**, aproximadamente **2.498.612 por persona**, bajo las ventas simuladas. Si no llegan esas ventas, debe recalcularse antes de comprometer gastos.

*Tabla. Calendario de caja del primer año sin ventas.* <!--#tab:es2-caja-mensual-->

| Momento | Salida de caja, CLP | Déficit acumulado sin aportes, CLP |
| --- | --- | --- |
| Preparación inicial | 1.022.000 | 1.022.000 |
| Mes 1 | 402.195 | 1.424.195 |
| Mes 2 | 126.684 | 1.550.878 |
| Mes 3 | 126.684 | 1.677.562 |
| Mes 4 | 126.684 | 1.804.246 |
| Mes 5 | 126.684 | 1.930.930 |
| Mes 6 | 126.684 | 2.057.613 |
| Mes 7 | 439.855 | 2.497.468 |
| Mes 8 | 439.855 | 2.937.323 |
| Mes 9 | 439.855 | 3.377.178 |
| Mes 10 | 439.855 | 3.817.033 |
| Mes 11 | 439.855 | 4.256.888 |
| Mes 12 | 558.855 | 4.815.743 |

## Ingresos simulados, pagos y margen

El escenario comercial mantiene el modelo de comisión de ES1: **12 % neto** sobre arriendo final supuesto de 100.000 CLP, no un porcentaje fijado por un contrato existente. Por reserva: comisión 12.000 + IVA 2.280 = 14.280 CLP; arriendo del propietario 100.000; cobro total a procesar 114.280. No se usa la garantía para financiar EspaciGo.

Si EspaciGo **absorbe económicamente** la tarifa pública inmediata de Checkout, `114.280 × 3,19 % = 3.645,53` CLP netos y `4.338,18` con IVA. Esa comisión de pasarela **no es 3,19 % de nuestros 12.000**. La alternativa pública a diez días es 2,89 % + IVA, pero exige financiar plazos y confirmar que sea aplicable al producto elegido. El flujo predeterminado descrito por Split 1:1 descuenta la tarifa primero al **vendedor**, antes de la comisión del marketplace. Por tanto, el costo cargado a EspaciGo en esta simulación exige acuerdo comercial o compensación; el crédito fiscal y la caja reales de ese mecanismo aún no están acreditados. La conciliación ilustrativa y el riesgo de reembolso están desarrollados en el análisis de pagos. Checkout corriente no resuelve por sí solo custodia, garantía o liberación condicionada [@es2mptarifas; @es2mpsplitflujo].

Se agregan dos firmas a 1.000 CLP netos cada una, KYC prorrateado de 500 y consumo/atención incremental de 500: **3.000 CLP adicionales por reserva**, todos supuestos. FirmaVirtual publica FES al público por 4.490 CLP por documento con dos o más firmantes, pero no se obtuvo cotización numérica de **API**; además, su página resume de otra forma el precio «por parte». Prorratear KYC por reserva requiere comprobar recurrencia por usuario. Como comparador, Didit anuncia USD 0,33 para KYC y USD 0,20 adicional para consulta RUT chileno; no se han evaluado acceso, impuestos ni tratamiento de datos. Dos firmantes no implican necesariamente dos cargos si se factura por documento: se recalculará según contrato y modalidad jurídica [@es2firmavirtualapi; @es2firmavirtualprecios; @es2diditchile].

Así, el variable neto es 6.645,53 y la contribución 5.354,47 CLP por reserva, antes de fijos y trabajo fundador. Una firma a 2.500 por persona cambia sustancialmente la economía; se incluye esa sensibilidad.

El reparto nativo y la compensación económica a un vendedor **no son equivalentes contables**. Por ello, el cuadro de IVA y VAN siguiente expresa una hipótesis de costos soportados por la plataforma, no una liquidación comprobada de Split. Antes de usarlo para decidir inversión se deberán obtener comprobantes y condiciones tributarias del flujo exacto, más una prueba de cobro y devolución [@es2mpsplitflujo].

La comparación documental añade una condición de selección: Mercado Pago documenta comisión 1:1 y reportes de liquidación, pero Flow solo acredita públicamente `merchantId` de comercios asociados y TUU no acredita en los términos consultados un split online equivalente. Ofrecer varios **medios de pago** mediante un checkout no obliga a integrar varias **pasarelas**. Ninguna de estas capacidades prueba custodia de la garantía. Antes de presupuestar el flujo definitivo se ensayarán dos cuentas, tarifa real por medio, abonos, reembolso con vendedor sin saldo y documentos por RUT [@es2flowapi; @es2mpsplitflujo; @es2mpreporte].

### Contraste del arriendo medio con oferta pública

Una muestra dirigida de precios publicados muestra unidades y duraciones distintas. Lofwork Santiago Centro publica oficina privada desde 6.000 CLP + IVA **por hora** y sala desde 18.000 + IVA por hora. Cowork del Centro publica sala para ocho personas a 17.750 + IVA/h si se toman dos horas, 10.500 + IVA/h por cinco y 7.750 + IVA/h por diez. BLT exhibe minibodega pequeña desde 55.000 CLP **por mes** y mediana desde 105.000 por mes, con promociones iniciales; su ficha no aclara el IVA del aviso [@es2lofespacios; @es2coworkcentro; @es2bltprecios].

Otros ejemplos de oferta amplían la dispersión: Saba Santa Rosa muestra 2.940 CLP por hora de estacionamiento en promoción; un stand de Busho declara un bloque mínimo de cuatro días por 83.000 CLP; Espacio Temporal publica espacios de trabajo desde 175.000 CLP mensuales y contrato mínimo de tres meses; Palmas de Malloco cotiza jornadas según asistentes, fecha y servicios e incluye quincho en la parcela, sin precio autónomo de este. La garantía reembolsable de 150.000 CLP del último caso no es ingreso de la plataforma. Son ofertas de terceros con condiciones distintas, no precios que EspaciGo haya logrado vender [@es2saba; @es2busho; @es2espaciotemporal; @es2palmas].

El ticket del modelo de **100.000 CLP finales por reserva** puede parecer cercano a una jornada de sala o un mes de bodega mediana, pero no es un promedio estimado. Una reserva de una hora puede valer mucho menos y consumir igualmente firma, identidad y procesamiento de pago bajo el flujo presupuestado. EspaciGo contempla todas estas categorías: para pasar del ejemplo a un presupuesto defendible se modelarán por separado precio final, duración, cupos disponibles, reservas pagadas, comisión, cancelaciones, firmas y KYC de cada modalidad. El simulador acepta una lista `segmentos` con 36 cantidades mensuales y conserva el desglose de contribución de cada tipo. El archivo vigente aún usa 100.000 CLP y cantidades agregadas como **escenario provisional**, pues no existen ventas observadas ni mezcla demostrada. No se mezclan horas, días y meses para inferir demanda [@es2lofespacios; @es2bltprecios].

El protocolo de medición propuesto define fichas comparables por `categoría × modalidad × comuna`, seguidas de búsqueda asistida y, cuando exista producto y contrato, un piloto de pagos conciliados. La cuota inicial sugerida es **exploratoria**, no una muestra representativa. Las estadísticas SII, ELE-7 y Censo ayudan a contextualizar zonas, pero no revelan cuántas reservas podría cerrar EspaciGo. Cada `segmento` del simulador deberá registrar origen, periodo, capacidad, precio final, conversión y cancelaciones observadas; un contacto o intención no se contabiliza como venta [@es2siiestadisticas; @es2ele7; @es2censo2024; @es2aaporpracticas].

Con la comisión y cargos **hipotéticos** del caso base, un arriendo final de 2.940 CLP arroja aproximadamente **-2.754 CLP de contribución variable** y uno de 21.420 CLP, **-1.210 CLP**; a 42.245 CLP queda solo **+529 CLP**, antes de fijos. La fórmula, las unidades y las fuentes están detalladas en este anexo. Esto revela por qué sumar reservas de estacionamiento, sala y bodega con el mismo ticket ocultaría pérdidas de transacciones pequeñas; también obliga a confirmar si firma y KYC ocurren en cada reserva, sin alterar los requisitos del proyecto [@es2saba; @es2lofespacios; @es2coworkcentro].

### Ingreso adicional propuesto: destaque de publicaciones

ES1 decidió cobrar comisión por reserva; ES2 estudia, **sin incorporarlo al flujo base**, un servicio opcional de visibilidad pagada por el arrendador. Debe mostrarse como «Patrocinado», limitarse a espacios aprobados y disponibles de la zona/categoría buscada y tener duración y condiciones publicadas. La tarifa se cobraría directamente a EspaciGo: no es arriendo de un tercero ni utiliza Split. Meta Ads, en cambio, es **gasto de adquisición de usuarios** de la plataforma, no ingreso por publicidad. El diseño y la evidencia documental se sustentan en las fuentes citadas [@es2mercadoads; @es2sernacpublicidad; @es2metasubasta].

*Tabla. Sensibilidad unitaria de un paquete de siete días; todos los importes y la venta son supuestos ilustrativos.* <!--#tab:es2-destaque-unitario-->

| Concepto | CLP | Cálculo |
| --- | ---: | --- |
| Precio propio neto propuesto | 5.000 | No aprobado ni validado por clientes |
| IVA supuesto 19 % | 950 | 5.000 × 19 % |
| Cobro final | 5.950 | Precio neto + IVA |
| Pasarela neta referencial | 190 | 5.950 × 3,19 %, redondeado |
| Pasarela de caja referencial | 226 | Cargo anterior × 1,19, redondeado |
| Aporte neto preliminar | 4.810 | 5.000 − 189,81, antes de soporte y otros costos |

La tasa es **Checkout público ordinario**, no una tarifa contratada para promociones; su IVA y crédito fiscal dependen del comprobante y situación tributaria reales. Diez paquetes al mes representarían 50.000 CLP netos de ingresos y alrededor de 48.102 CLP de aporte **solo bajo el ejemplo**, antes de soporte, devoluciones, desarrollo, fraude e impuestos sobre renta. No hay compradores ni tráfico medido que permitan proyectar esa cantidad. Por tanto, **se mantiene cero ingreso por destaque en los años 1–3 del VAN actual**. El gasto de captación ya supuesto en el JSON no se convierte en rendimiento de Meta: solo una campaña ejecutada puede medir visitas, publicaciones y reservas atribuibles [@es2mptarifas; @es2metasubasta].

El ensayo de captación propuesto separa publicaciones **aprobadas y disponibles** de reservas **pagadas y no anuladas**. Los **357.000 CLP de caja** ya incluidos como captación durante seis meses constituyen un supuesto de presupuesto total, no una compra realizada ni un monto adicional para Meta. Sin cuenta, campaña y datos propios de pago no es calculable el costo por reserva; Ads Manager y Pixel/API se usarían solo tras definir eventos, política de anuncios aplicable y tratamiento de datos personales [@es2metaobjetivos; @es2metapresupuesto; @es2metavivienda].

El [catálogo SII](https://www.sii.cl/catastro/codigos.htm) incluye **731001 — servicios de publicidad prestados por empresas**. Está en la propuesta de giro complementario, sujeto a formalización y verificación de actividad; su inclusión **no convierte un destaque hipotético en venta** ni prueba el documento aplicable [@es2siiactividades]. Antes de sumarlo a la caja se necesitan contrato, precio aceptado, tasa de compra por categoría y zona, capacidad de posiciones, tarifa y reversos de pasarela, efectos sobre conversión orgánica y costos de soporte. La decisión comercial debe comprobar que se entrega exposición medible sin prometer reservas.

La clasificación pública del SII y un oficio sobre anuncios digitales fortalecen la hipótesis de que el **destaque propio** se facturaría como publicidad afecta, pero no sustituyen consulta particular para la SpA. La documentación del arriendo del propietario y la comisión deben conciliarse por separado; tampoco debe emitirse boleta y tratar el voucher electrónico como segunda venta por el mismo cobro [@es2siicatalogo; @es2siipublicidadapp].

## Proyección a tres años y flujo de caja

Las cantidades son **0, 720 y 1.800 reservas/año**. El JSON conserva la rampa mensual: año 2 de 20 a 100 reservas/mes y año 3 de 100 a 200. No hay estudio de demanda que demuestre esos volúmenes. Una alternativa simula 105 reservas en el segundo semestre del año 1. Ninguno de estos supuestos se declara realizado.

Se reajustan arriendo medio, partidas CLP y valor hora por IPC supuesto del 4 %; los recursos USD conservan precios y tipo de cambio base, con una sensibilidad independiente a USD/CLP 1.100. El 4 % no es una predicción oficial. El impuesto se aplica solo sobre resultado positivo bajo la simplificación académica del 27 %, sin restar horas gratuitas como gasto [@es2ineipc202608; @es2siitasas].

*Tabla. Resultados y caja de los años operativos, CLP.* <!--#tab:es2-flujo-bootstrap-->

| Concepto | Año 1 | Año 2 | Año 3 |
| --- | --- | --- | --- |
| Reservas | 0 | 720 | 1.800 |
| Ingresos propios netos | 0 | 8.985.600 | 23.362.560 |
| Costos variables netos | 0 | 4.976.174 | 12.938.053 |
| Fijos de operación netos | 3.229.805 | 4.887.018 | 4.968.346 |
| Sueldos desembolsados | 0 | 0 | 0 |
| Resultado antes de impuesto, incluye preparación neta en año 1 | -4.099.006 | -877.593 | 5.456.161 |
| IDPC calculado al 27 % | 0 | 0 | 1.473.163 |
| PPM provisionados, a cuenta del IDPC | 0 | 22.464 | 58.406 |
| IVA pagado después de créditos | 0 | 0 | 258.689 |
| Remanente IVA al cierre, no efectivo | 716.736 | 831.765 | 0 |
| Flujo de caja del año, excluye preparación inicial | -3.793.743 | -1.015.085 | 4.814.762 |
| Trabajo fundador valorizado, separado | 43.200.000 | 22.464.000 | 23.362.560 |

La preparación inicial es una salida adicional de **1.022.000 CLP en t0**. En el resultado del año 1 se reconocen aproximadamente **869.202 CLP netos** a efectos ilustrativos, sin volver a pagarlos. El flujo incluye compras con IVA, créditos compensados, PPM y saldo de IDPC; **no equivale a utilidad contable**. La regularización tributaria se reserva al cierre del mismo año operativo para presupuestar, no como fecha legal de pago. El exceso de PPM no se transforma en devolución anticipada. El crédito fiscal de la oficina elegida y su firma depende de recibir DTE válido y confirmación contable.

No se agrega otra inversión genérica de capital de trabajo encima del déficit mensual: eso duplicaría el financiamiento. El máximo déficit constituye la necesidad calculada; el colchón agrega liquidez. No se reconoce valor terminal, devolución de capital gastado ni venta ficticia del software. Una evaluación de continuidad más larga necesita evidencia adicional.

A tasa nominal **supuesta** del 12 %, el flujo anterior a aportes da **VAN de caja -1.791.437 CLP** y **TIR de caja -9,20 %**. Al descontar también el trabajo no remunerado, el **VAN económico es -74.900.038 CLP**; no hay TIR económica positiva que mostrar. La tasa aún debe justificarse y la capitalización societaria no corrige un VAN negativo.

*Tabla. Sensibilidad, manteniendo explícitas las demás condiciones.* <!--#tab:es2-sensibilidad-bootstrap-->

| Escenario | VAN caja, CLP | Déficit máximo 36 meses, CLP |
| --- | --- | --- |
| Base con Oficina Express y aseo provisional | -1.791.437 | 6.246.529 |
| Asesoría y habilitación inicial −25 %, tres partidas netas | -1.580.485 | 6.008.529 |
| Asesoría y habilitación inicial +25 %, tres partidas netas | -2.002.390 | 6.484.529 |
| 105 ventas en año 1 | -1.272.926 | 5.580.638 |
| Mitad de reservas previstas | -6.913.327 | 8.736.171 |
| USD/CLP 1.100 | -2.317.886 | 6.644.781 |
| Pagar 600.000 por fundador/mes desde año 3, a precios base | -17.413.450 | 22.963.869 |
| Firma a 2.500 netos por firmante | -7.678.513 | 9.272.416 |
| Arriendo inicial de 30.000 CLP por reserva | -14.356.751 | 18.045.981 |
| Arriendo inicial de 50.000 CLP por reserva | -10.426.340 | 12.702.163 |
| Arriendo inicial de 150.000 CLP por reserva | 4.512.103 | 5.407.050 |
| IDPC 12,5 % estático, sin asignación legal de calendario | -1.228.317 | 6.246.529 |
| Piloto cloud durante todo el año 1 | -2.977.418 | 7.768.556 |
| Aseo completo de 2,88 UTM en vez de provisión de 120.000 | -1.989.127 | 6.423.104 |
| Dos documentos DOM condicionales de 0,15 y 0,35 UTM | -1.827.298 | 6.282.390 |

Las tres partidas profesionales de inicio suman 800.000 CLP netos; moverlas ±25 % cambia la salida de caja del año 1 en ±238.000 CLP con el IVA supuesto. El caso de firma a 2.500 netos **por firmante** conserva dos cargos por reserva: no representa una cotización API ni el precio público por documento. En ese estrés, los tres flujos anuales son negativos y la TIR no está definida. El KYC de 500 CLP **por reserva** es un prorrateo provisional: las ofertas públicas expresan el cobro por verificación de usuario y consulta, de modo que deben medirse altas y revalidaciones antes de reemplazarlo. La comparación, sus fuentes y los límites de cada unidad se registran en la investigación de costos de terceros; no modifica el caso base.

El escenario de sueldos usa **costo total empresarial** de 600.000 CLP por fundador al mes a precios base, indexado al 4 %; no es sueldo líquido ni liquidación laboral. No se aprueba pagarlo si la caja no lo soporta. El escenario del 12,5 % es comparación matemática; no asigna esa tasa a todos los años futuros.

Los tres escenarios de ticket conservan las **mismas** 720/1.800 reservas, composición y costos. A 30.000 CLP iniciales, los cargos variables superan la comisión incluso antes de fijos; el VAN positivo a 150.000 CLP depende de conseguir ese ticket y volumen sin evidencia. La frontera inicial de contribución variable es aproximadamente **35.909 CLP** por reserva con 12 % de comisión, 3,19 % de pasarela sobre el cobro y 3.000 CLP de otros variables. No equivale a equilibrio del proyecto. En el año 3 se requieren 150 reservas por mes en promedio: 30 espacios activos implicarían cinco reservas mensuales cada uno, una hipótesis de capacidad que difiere entre sala por horas y bodega mensual.

### Escenario segmentado sintético por categoría

El caso base usa un ticket único de 100.000 CLP. Para medir cuánto depende el resultado de ese supuesto se ejecutó un **escenario segmentado explícitamente sintético** (`investigacion/supuestos_segmentado.json`), que conserva el mismo volumen hipotético de 0, 720 y 1.800 reservas al año y lo reparte en cinco categorías con los **precios de lista** transcritos en la muestra dirigida: una hora de oficina privada, un bloque mínimo de dos horas de sala, un mes de minibodega, una hora de estacionamiento y el bloque mínimo de cuatro días de stand. El reparto del volumen es una decisión del análisis y **no** una medición de demanda; el único dato externo es el precio publicado de cada producto.

*Tabla. Comparación entre el caso base y el escenario segmentado sintético, CLP.* <!--#tab:es2-base-vs-segmentado-->

| Concepto | Caso base, ticket único de 100.000 | Segmentado sintético |
| --- | ---: | ---: |
| Contribución del año 3, ingresos propios menos costos variables | 10.424.507 | 350.688 |
| VAN de caja a 36 meses, tasa nominal supuesta del 12 % | -1.791.437 | -12.771.812 |
| Déficit máximo acumulado en 36 meses | 6.246.529 | 15.891.086 |
| TIR del flujo de caja | -9,20 % | No definida: los tres flujos anuales son negativos |

**Nota.** Elaboración propia con el simulador del repositorio. La contribución del año 3 por categoría es **-935.862 CLP** en oficina por hora, **+206.114** en sala por dos horas, **+621.038** en bodega mensual, **-1.072.489** en estacionamiento por hora y **+1.531.886** en stand por bloque. Se aplica a cada categoría el mismo cargo variable por reserva del caso base —dos firmas, KYC y otros—, aunque una reserva por hora y una bodega mensual no tienen por qué compartir firma, KYC ni garantía; el efecto es conservador y constituye el límite principal del ejercicio.

El contraste no mide demanda ni reemplaza al caso base: solo cambia la composición del catálogo. Su lectura es que **el ticket medio de 100.000 CLP oculta categorías que no cubren sus propios costos variables** y que el resultado depende de la mezcla tanto como del volumen. Parcela con quincho, local flexible y las demás categorías de la muestra quedan fuera porque su precio publicado exige cotización o contrato mínimo, y no se les asignó un arriendo unitario inventado.

## Margen del 25 % y decisión

El 25 % es **margen sobre ingresos de comisión**, no markup ni retorno del capital. Bajo el escenario base, el margen operativo de caja del año 3 es **23,35 %** antes del impuesto: no alcanza el objetivo. El punto de equilibrio anual, con costos y ticket del año 3, es de unas **858 reservas sin remunerar el tiempo**, y **4.892 si se reconoce todo el esfuerzo valorizado**, manteniendo costos lineales; esa capacidad no está probada.

Para un objetivo de margen `m`, comisión neta `P`, arriendo final `T`, tasa de pasarela `a`, otros variables `K` y fijo anual `F`, con Q reservas:

`P = (F/Q + K + a×T) / (1 - m - a×(1 + IVA))`.

La fórmula incorpora que la pasarela aumenta cuando sube la propia comisión. Con 1.800 reservas en el año 3, m = 25 %, a = 3,19 %, IVA = 19 %, arriendo de **108.160 CLP** y otros variables de **3.244,80 CLP** por reserva (ambos indexados al 4 % durante dos años), más fijos netos de **4.968.346 CLP**, la comisión neta requerida es **13.279,18 CLP**, equivalente al **12,28 % del arriendo final**. Al agregar los **23.362.560 CLP** de trabajo fundador valorizado al costo económico, se requieren **31.507,40 CLP**, o **29,13 %** del arriendo. Son umbrales calculados y reproducibles con esos insumos; no se recomienda cobrar esas tasas sin investigar aceptación, competencia y posible reducción de costos por volumen.

**Conclusión:** el proyecto puede presupuestarse como esfuerzo autofinanciado, pero esta simulación **no demuestra rentabilidad a tres años**. El VAN sigue negativo aun sin pagar sueldos; recuperar y remunerar el tiempo exige más volumen, mejor contribución, menos costo de terceros o un horizonte mayor sustentado. La prioridad es cotizar pagos/firma, validar demanda y financiar el déficit; no usar ingresos de terceros ni garantías para taparlo.

## Reproducción y cierre pendiente

```powershell
python Informes/herramientas/simular_bootstrap.py Informes/ES2PT/investigacion/supuestos_bootstrap.json --salida Informes/ES2PT/build/simulacion_bootstrap.json
```

Los parámetros y etiquetas de calidad del dato son editables en `investigacion/supuestos_bootstrap.json`. Los resultados JSON conservan 36 meses y todos los escenarios. Ante un cambio, recalcular y actualizar este anexo y el resumen 2.1. El modelo anterior `supuestos_economicos.json` permanece como antecedente pedagógico y no describe ya el presupuesto vigente.

[[PENDIENTE: confirmar giro, régimen y domicilio con profesionales y municipio; cotizar honorarios, aseo, Split, firmas e identidad y confirmar si el crédito de IVA de servicios extranjeros es recuperable; acordar aportes, pacto de socios y horas; sustituir el escenario segmentado sintético por precio final, demanda, capacidad, ocupación y conversión medidos en cada tipo de arriendo; validar los impuestos según calendario y capacidad; e inventariar los activos y el costo de subsistencia personal por separado.]]
