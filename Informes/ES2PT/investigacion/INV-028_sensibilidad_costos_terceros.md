# INV-028 — Sensibilidad de costos pendientes con terceros

**Nota de vigencia (23-09-2026):** las tablas de este registro usan el presupuesto histórico con LOF. El escenario base vigente incorpora Oficina Express (50.000 CLP/año y 5.000 CLP una vez por firma, IVA incluido), una sola patente y las cifras de [INV-029](INV-029_domicilio_patente_y_dom.md). Las sensibilidades históricas sirven para comparar métodos, no como presupuesto actual.

**Corte:** 23-09-2026. **Pregunta:** ¿cuánto cambia la caja de EspaciGo si las provisiones de firma y asesoría difieren de lo presupuestado? **Estado:** contraste documental y simulación; no hay cotizaciones dirigidas a la futura SpA ni compras realizadas. Complementa [INV-027](INV-027_gestion_terceros.md), sin cerrar sus gestiones T1–T10.

## Método y unidades

Se conservó intacto `supuestos_bootstrap.json`. Cada escenario altera **solo** la variable indicada en una copia en memoria y ejecuta `simular()` de `Informes/herramientas/simular_bootstrap.py`: tres años, 0/720/1.800 reservas, IPC hipotético del 4 %, USD/CLP supuesto de 1.000, IVA reservado según el JSON y descuento nominal supuesto del 12 %. El resultado es una sensibilidad del modelo de caja, no una cotización ni una estimación estadística. El 27 % de IDPC continúa como ejercicio académico, no como régimen confirmado de la SpA.

Las tres partidas profesionales iniciales (`estatutos_pacto_ip`, `terminos_privacidad_contratos`, `habilitacion_contable`) suman **800.000 CLP netos**, o **952.000 CLP de caja** con el IVA supuesto. Se varían juntas ±25 %; no se cambian la firma de constitución, el domicilio ni los servicios mensuales. El estrés de firma sustituye **1.000 por 2.500 CLP netos por firmante** y mantiene dos cargos por reserva: pasa de 2.000 a 5.000 CLP netos por reserva. Es una hipótesis adversa, **no** la tarifa pública de FirmaVirtual.

| Escenario aislado | Salida año 1, CLP | VAN de caja 12 %, CLP | Déficit máximo 36 meses, CLP | Fondo año 1 con colchón 20 %, CLP | Brecha frente a capital propuesto de 3 millones, CLP |
| --- | ---: | ---: | ---: | ---: | ---: |
| Base histórica con LOF | 4.889.743 | −1.970.676 | 6.392.289 | 5.867.691 | 2.867.691 |
| Asesoría y habilitación inicial −25 % | 4.651.743 | −1.759.723 | 6.154.289 | 5.582.091 | 2.582.091 |
| Asesoría y habilitación inicial +25 % | 5.127.743 | −2.181.628 | 6.630.289 | 6.153.291 | 3.153.291 |
| Firma a 2.500 netos por firmante | 4.889.743 | −7.855.448 | 9.492.806 | 5.867.691 | 2.867.691 |

Los valores se redondean a pesos al presentar. En el estrés de firma, los tres flujos anuales quedan negativos y el simulador no devuelve TIR (`None`); no corresponde interpretar una tasa de retorno positiva. La firma no altera el año 1 porque ese año supone cero reservas. El fondo de 5.867.691 menos el capital propuesto de 3.000.000 equivale a **2.867.691 CLP**; el Anexo A contenía una brecha aritmética incorrecta que se corrigió. El capital no es ingreso operativo ni mejora el VAN antes de financiamiento.

## Contraste de precios públicos y límites

- [FirmaVirtual, precios al público](https://firmavirtual.legal/servicios/precios) presenta FES de **4.490 CLP por documento con dos a diez firmantes** en su tabla, mientras su FAQ resume 3.450 CLP **por parte**. La [página de API](https://firmavirtual.legal/servicios/api-firma-electronica) menciona cobro por documento, contrato, volumen y número de firmantes, pero no entrega una tarifa numérica API. Por tanto, ni 4.490 ni 3.450 se sustituyen en el campo **neto por firmante** del simulador: falta aclarar unidad, impuestos, tipo de firma, reintentos y volumen contratado.
- [Didit Chile](https://didit.me/es/solutions/countries/chile/) anuncia **USD 0,33 por KYC** y **USD 0,20 por consulta RUT chilena**. Como orden de magnitud, 1.000 usuarios nuevos con ambas operaciones costarían **USD 530 = 530.000 CLP** al cambio supuesto, antes de impuestos, revalidaciones y cualquier condición comercial. La página anuncia verificaciones gratuitas mensuales, pero no se aplican al flujo: cobertura del RUT, acceso y elegibilidad de EspaciGo no están confirmados. El JSON actualmente multiplica **500 CLP por reserva**; eso produce 1.347.840 CLP nominales en años 2–3 con su IPC, pero no equivale a una tarifa por persona. Fórmula a levantar: `altas verificadas × tarifa de alta + revalidaciones × tarifa de revalidación + consultas adicionales × tarifa por consulta`, con impuestos y tipo de cambio separados.
- [LOF Santiago Centro](https://www.oficinavirtuallof.cl/oficina-virtual-santiago-centro/) publica **119.000 CLP por año** para su Plan Básico. El presupuesto ya incorpora ese importe una vez en el año 1; no debe agregarse de nuevo. Faltan contrato, aceptación del giro y del domicilio por la municipalidad, renovación y eventuales cobros adicionales.
- El [SII publica 71.721 CLP por UTM de septiembre de 2026](https://www.sii.cl/valores_y_fechas/utm/utm2026.htm). La [Ley de Rentas Municipales, artículo 24](https://www.bcn.cl/leychile/Navegar?idNorma=7054&idParte=8739650), fija una patente entre 2,5 y 5 por mil del capital propio, con mínimo anual de 1 UTM. Sobre un capital **ilustrativo** de 3 millones, el rango simple de 7.500–15.000 CLP queda por debajo del mínimo; ello explica la provisión de 71.721 CLP. La base imponible, fecha, liquidación concreta y derecho de aseo de Santiago aún requieren confirmación municipal. El capital social propuesto no demuestra por sí solo el capital propio tributario aplicable.

## Decisión y evidencia que falta

Mantener el JSON base como **escenario provisional**. Solicitar precio API de firma expresado por documento y firmantes, condiciones KYC por usuario nuevo/revalidación, tres presupuestos profesionales con alcance, y contrato/liquidación de domicilio y patente. Registrar cada respuesta con fecha, impuestos y unidad de cobro; recién entonces reemplazar supuestos, recalcular el Anexo A y comprobar el margen por categoría de arriendo. La prioridad económica es la firma: su estrés hace negativos los flujos incluso en el tercer año hipotético. Ni las ofertas públicas ni esta sensibilidad acreditan que el negocio sea viable.

## Relación con ES1

ES1 es la base histórica de la idea de intermediación; no se modifica. Estos escenarios son evaluación de ES2 y no prueban que las integraciones, ventas o la SpA ya existan.
