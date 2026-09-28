# INV-010 — Infraestructura, SpA y financiación inicial

- Consulta: 23-09-2026. Estado: tarifas públicas, supuestos y propuesta; sin compras, inscripciones ni proveedores contactados.
- Base: modelo de comisión y tecnologías de ES1; secciones ES2 2.1, 2.2, 3.6 y Anexo A.
- Información nueva del usuario: no hay ingresos; tres fundadores aportarían tiempo y recursos propios; se estudia una SpA con participación igualitaria y oficina virtual en Santiago Centro.
- Convención de simulación: primer año completo sin ventas; seis meses de ensayo y seis de piloto. Es una hipótesis conservadora, no una fecha ni pronóstico confirmado por el equipo.

## Fuentes y alcance

| Clave bibliográfica | Fuente consultada | Evidencia y límite |
| --- | --- | --- |
| es2cloudsqlpricing | [Cloud SQL](https://cloud.google.com/sql/pricing?hl=en) | HTML oficial: Enterprise General Purpose, región inicial Iowa; CPU 0,0413 USD/h y RAM 0,007 USD/GiB-h. Se comprobó la cabecera de edición y región, no solo la lista de ciudades. Santiago no fue cotizado. |
| es2cloudrunpricing | [Cloud Run](https://cloud.google.com/run/pricing) | Tabla inicial Iowa, modalidad por solicitudes; CPU 0,000024 USD/s, memoria 0,0000025 USD/GiB-s, solicitudes 0,40 USD/millón. Se presupuesta antes del nivel gratuito; no crédito promocional. |
| es2gcspricing | [Cloud Storage](https://cloud.google.com/storage/pricing) | Almacenamiento Standard inicial 0,000027397 USD/GiB-h. Operaciones y tráfico son partidas distintas. |
| es2lbpricing | [Load Balancing](https://cloud.google.com/load-balancing/pricing) | Hasta cinco reglas a 0,025 USD/h. Procesamiento de datos se provisiona aparte y requiere SKU. |
| es2armorpricing | [Cloud Armor](https://cloud.google.com/armor/pricing) | Standard: política 0,006849315 USD/h, regla 0,001369863 USD/h y 0,75 USD/millón de solicitudes con política global. No contratar Enterprise en esta simulación. |
| es2mptarifas | [Mercado Pago, Checkout](https://www.mercadopago.cl/herramientas-para-vender/check-out) | General inmediata 3,19 % + IVA, diez días 2,89 % + IVA; promociones separadas. Es referencia de Checkout público, no oferta de Split/escrow. |
| es2mpsplitflujo | [Mercado Pago, Split 1:1](https://www.mercadopago.cl/developers/es/docs/split-payments/split-1-1/integration-configuration/integrate-marketplace) | El contenido indexado de la guía oficial atribuye la tarifa al vendedor antes de la comisión del marketplace y describe límites de reembolso. Apertura directa HTTP 403; condiciones de EspaciGo sin verificar. |
| es2firmavirtualapi | [FirmaVirtual API](https://firmavirtual.legal/servicios/api-firma-electronica) | Modelos por documento, contrato y volumen; no se obtuvo tarifa numérica de API. 1.000 CLP netos por firmante y 500 por KYC son supuestos; se tensiona firma a 2.500. |
| es2firmavirtualprecios | [FirmaVirtual, precios](https://firmavirtual.legal/servicios/precios) | FES pública de 4.490 CLP por documento de dos a diez firmantes. No equivale a tarifa API ni aclara por sí sola impuestos del presupuesto. |
| es2diditchile | [Didit, Chile](https://didit.me/es/solutions/countries/chile/) | Proveedor anuncia KYC desde USD 0,33 y `chl_rut` adicional USD 0,20. Benchmark comercial, no proveedor seleccionado ni conclusión legal o de privacidad. |
| es2resacciones | [RES, preguntas sobre SpA](https://www.registrodeempresasysociedades.cl/FAQ.aspx?seccion=5) | Acciones enteras, aportes y reserva; no equivale a redactar estatutos ni aprobar el pacto propuesto. |
| es2rescostos | [RES, ayuda](https://www.registrodeempresasysociedades.cl/AyudaRegistro.aspx) | Plataforma sin costo; firma notarial del acto 0,26 UF con comparecientes ante mismo notario; pueden existir documentos adicionales. No multiplicar ese arancel automáticamente por tres. |
| es2siiactividades | [SII, códigos vigentes](https://www.sii.cl/ayudas/ayudas_por_servicios/1956-codigos-1959.html) | 682000, 631200 y 620100 existen; actividad principal requiere contrastar contratos y operación efectiva. La tabla no es resolución individual de clasificación. |
| es2siiivaservicios | [SII, servicios e IVA](https://www.sii.cl/destacados/iva_prestacion_servicios/) | Una SpA no obtiene la exención de sociedad de profesionales por tener socios profesionales. Se presupuesta comisión gravada al 19 %, sujeto a revisión específica. |
| es2siipro_pyme | [SII, Pro Pyme General](https://www.sii.cl/preguntas_frecuentes/declaracion_renta/001_140_7529.htm) | Régimen por evaluar según requisitos. No confundir forma societaria, giro, régimen e IVA. |
| es2siitasas | [SII, tasas por ejercicio](https://www.sii.cl/preguntas_frecuentes/declaracion_renta/001_140_4708.htm) | Pro Pyme General: 12,5 % para ejercicios comerciales 2026/2027 y 15 % en 2028 según tabla consultada. No mantener 27 % como obligación por ser SpA. |
| es2siif29 | [SII, F29 sin movimiento](https://www.sii.cl/preguntas_frecuentes/impuestos_mensuales/001_130_1259.htm) | Sin ventas no elimina obligaciones; compras con crédito requieren declaración que las refleje. |
| es2lofvirtual | [LOF Santiago Centro](https://www.oficinavirtuallof.cl/oficina-virtual-santiago-centro/) | Av. Libertador Bernardo O'Higgins 1302, of. 70; Básico anual 119.000 CLP, declarado exento por proveedor. Referencia presupuestada; compatibilidad del giro y documentación pendientes. |
| es2dvirtual | [DVirtual](https://dvirtual.cl/) | 6.500 CLP mensuales IVA incluido + firma online 9.800. Doce cargos suman 87.800 con firma. La política identifica Teatinos 251, of. 610 como domicilio del proveedor; confirmar domicilio contractual del cliente. |
| es2rentasmunicipales | [Ley de Rentas Municipales, arts. 24 y 29](https://www.bcn.cl/leychile/navegar?idNorma=18967) | Patente anual entre 2,5 y 5 por mil del capital propio, mínimo 1 UTM; ciclo julio-junio y cuotas julio/enero. No confundir capital propio tributario con capital estatutario. |
| es2patentesstgo | [Municipalidad de Santiago, solicitud](https://tramites.munistgo.cl/solicitudpatente/) | Canal de solicitud. No se obtuvo liquidación individual ni derecho de aseo para este domicilio/giro. |
| es2utm2026 | [SII, UTM 2026](https://www.sii.cl/valores_y_fechas/utm/utm2026.htm) | Septiembre: 71.721 CLP; no precio fijo de las cuotas futuras. |
| es2nictarifas | [NIC Chile](https://www.nic.cl/dominios/tarifas.html) | Dominio .cl: un año 9.990 CLP, exento. No acredita disponibilidad del nombre ni propiedad de marca. |
| es2inapitasas | [INAPI, marcas](https://www.inapi.cl/marcas/para-informarse) | Derechos de registro 3 UTM/clase, más publicación; gasto opcional separado de constitución y patente municipal. |

Las páginas dinámicas de Cloud SQL y Cloud Armor se contrastaron también leyendo su HTML público con Python, sin autenticación ni selección regional privada. La cifra antigua USD 69,97 permanece retirada: la revisión distingue ahora tarifa de CPU/memoria Enterprise de otras ediciones. No se presenta como precio Santiago.

## Decisiones de modelado

- Referencia cloud Iowa con carga explícita y tres perfiles. Para presupuesto preliminar regional se agrega 35 % de provisión, **no una tarifa verificada de Santiago**. USD/CLP = 1.000 es supuesto, no dólar observado. Sensibilidad a 1.100. Antes de desplegar, cotizar la región elegida y analizar transferencias internacionales de datos.
- La página oficial de Cloud Run clasifica `us-central1` como Tier 1 y `southamerica-west1` como Tier 2 para precios regionales [@es2cloudrunpricing]. Esto refuerza que el factor 1,35 del presupuesto **no equivale** a aplicar los SKU de Santiago: se requiere cotizar CPU, memoria, solicitudes y los demás servicios por separado.
- Separar salida efectiva con IVA, gasto neto y crédito fiscal acumulado. Se simula documentación válida y recuperabilidad; no se vende ni reembolsa automáticamente el remanente. El IVA de servicios extranjeros depende de la facturación y situación tributaria, por confirmar.
- Trabajo no remunerado no es salida de caja, gasto tributario ficticio, deuda salarial automática ni aporte societario pagado. Se valora en una vista económica separada.
- Todos los fondos de los arrendadores y garantías quedan fuera del financiamiento. La comisión se calcula sobre arriendo final supuesto; la pasarela sobre arriendo más servicio e IVA, excluyendo garantía por desconocer cómo se procesaría. Esto supone que EspaciGo **absorbe económicamente** la tarifa; el flujo predeterminado publicado para Split 1:1 la descuenta primero al vendedor. Compensación, precio al público, IVA y caja requieren contrato y prueba; ver INV-012. El crédito fiscal asociado a ese costo no queda demostrado por el flujo nativo.
- Capital estatutario propuesto 3.000.000 CLP / 3.000 acciones. Financiación adicional puede estructurarse como aportes de capital o préstamos documentados de socios; no se contabiliza como venta ni gasto.
- Impuesto 27 % se conserva únicamente como escenario académico; comparación estática al 12,5 % sin asignarle calendario ni régimen aprobado. PPM 0,25 % es provisión de caja no validada, compensada contra IDPC del mismo año; no se inventa devolución del exceso. Fechas reales, pérdidas tributarias y tasas por ejercicio requieren adaptación contable.

## Resultado y reproducción

La versión actual está en [supuestos_bootstrap.json](supuestos_bootstrap.json), la calculadora en `../../herramientas/simular_bootstrap.py` y el desarrollo en el [Anexo A](../anexos/A_evaluacion_economica.md). El ejemplo anterior de INV-009 queda como antecedente pedagógico; sus VAN/TIR no son la conclusión actual.

```powershell
python Informes/herramientas/simular_bootstrap.py Informes/ES2PT/investigacion/supuestos_bootstrap.json --salida Informes/ES2PT/build/simulacion_bootstrap.json
```

La salida conserva 36 meses por escenario: ingresos propios, fondos de terceros, cargos de pago, otros variables, fijos, IVA, PPM, impuesto anual, trabajo y déficit acumulado. Permite identificar aportes antes de quedarse sin caja. Word sigue diferido.

[[PENDIENTE: cotización Santiago con SKU y región; habilitación/tarifa/atribución de Split y prueba de saldos; firma por documento y precio API/KYC por usuario; confirmación de giro y oficina ante SII/municipio; liquidación de patente/aseo; cotizaciones de abogado y contador; acordar capital, préstamos, horas y calendario de venta con los tres fundadores.]]
