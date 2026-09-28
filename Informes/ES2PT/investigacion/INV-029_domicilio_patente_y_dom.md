# INV-029 — Oficina Express, patente y actuaciones de la DOM

**Corte:** 23-09-2026. **Pregunta:** ¿qué desembolso aproximado exige usar Ahumada 131 como domicilio de la futura SpA y cuáles trámites municipales podrían cobrarse? **Estado:** oferta pública y normas contrastadas; EspaciGo no ha contratado domicilio, constituido la sociedad, solicitado patente ni recibido liquidación. El texto de conversación aportado por el usuario se trató como lista de afirmaciones por verificar, no como fuente normativa.

## Oferta elegida y presupuesto

[Oficina Express](https://oficinaexpress.cl/) publica el plan anual en **50.000 CLP con IVA incluido**, más **5.000 CLP una sola vez** por firma electrónica simple del contrato. Ofrece domicilio tributario/comercial en **Ahumada 131, Santiago Centro**, recepción y aviso de correspondencia; no incluye mesa de trabajo ni sala de reuniones. La contratación se anuncia en minutos o menos de 24 horas con documentos listos. El precio se denomina «referencial» en la portada: faltan propuesta vigente para la SpA, número exacto de oficina, contrato, derecho del proveedor a ceder uso para cada giro, DTE y renovación. La rapidez de contratar **no es** rapidez garantizada de obtener patente.

Se sustituyó en `supuestos_bootstrap.json` la opción presupuestada LOF (119.000 CLP/año exentos) por Oficina Express (50.000 CLP/año finales). La reserva de firma de domicilio pasó de 10.000 a 5.000 CLP finales. Como los dos precios dicen incluir IVA, el simulador los desglosa en neto e IVA bajo su hipótesis de crédito fiscal; **no hay factura ni crédito fiscal acreditados**. El año 1 baja **74.000 CLP de caja** frente al escenario LOF. Las renovaciones de años 2–3 se indexan al 4 % únicamente como supuesto del modelo, no como cláusula contractual. LOF y DVirtual quedan como comparadores documentales.

## Trámites y derechos aproximados

Se usa la [UTM de septiembre de 2026 del SII: 71.721 CLP](https://www.sii.cl/valores_y_fechas/utm/utm2026.htm). El importe real usa la UTM y la liquidación de la fecha que corresponda.

| Concepto | Referencia de caja | Tratamiento en el flujo |
| --- | ---: | --- |
| Domicilio Oficina Express, año 1 | 50.000 CLP IVA incluido | Base elegida; oferta sin contratar |
| Firma electrónica del contrato de domicilio | 5.000 CLP IVA incluido, una vez | Base elegida; distinta de la firma de constitución y de contratos de arriendo |
| Constitución por RES | Portal sin arancel; firma electrónica/notaría aparte | Continúa provisión previa de 15.000 CLP, no tres cargos automáticos; [ChileAtiende](https://www.chileatiende.gob.cl/fichas/21409) y [RES](https://www.registrodeempresasysociedades.cl/AyudaTarifasNotariasles.aspx) |
| Patente comercial por doce meses | **Mínimo ilustrativo 1 UTM = 71.721 CLP** | Base anterior mantenida; 3 millones de capital propio inicial supuesto cae bajo el mínimo incluso al 5‰ |
| DOM: informe de prefactibilidad de actividades productivas | **0,15 UTM ≈ 10.758 CLP** | Solo si lo exige el municipio para la actividad/dirección |
| DOM: certificado de informaciones previas con planchetas | **0,35 UTM ≈ 25.102 CLP** | Solo si se solicita o exige; podría aportarlo el titular del inmueble |
| Ambos documentos DOM anteriores | **0,50 UTM ≈ 35.861 CLP** | Escenario condicional, no obligación automática ni permiso para modificar el local |
| Aseo de actividad económica diurna | **2,88 UTM ≈ 206.556 CLP/año** | Tarifa de ordenanza; falta confirmar si se cobra a esta SpA o está a cargo/incluido por titular del inmueble |

Las dos tarifas DOM y la de aseo proceden de la [Ordenanza municipal N.º 94 para 2026, artículos 15 y 9](https://documentos.munistgo.cl/wp-content/uploads/2025/12/Ordenanza-No-94-2026-V2.pdf). La provisión base anterior de **120.000 CLP de aseo** se conserva como bolsa no verificada hasta resolver la incidencia. Si el municipio exigiera a la SpA el cargo diurno íntegro, reemplazar 120.000 por 206.556 aumentaría la salida del año 1 en **86.556 CLP**; no se suman ambos. La solicitud en línea permite [consultar zonificación y restricciones de calle y número](https://tramites.munistgo.cl/solicitudpatente/op1.aspx); falta verificar Ahumada 131 para la oficina específica y cada actividad.

La [Ley de Rentas Municipales, artículo 24](https://www.bcn.cl/leychile/navegar?idNorma=18967&idParte=8269364), establece **2,5–5 por mil** del capital propio, con mínimo anual de 1 UTM, y grava la actividad por contribuyente en un lugar **independientemente del número de giros**. Cinco por mil equivale a **0,5 %**, no a 5 %. Con 3 millones ilustrativos: 7.500–15.000 CLP antes del mínimo, por lo que se usa 71.721 CLP; no se cobra una UTM por cada código ni por semestre. La tasa puntual de Santiago, capital propio efectivo y proporcionalidad inicial se confirmarán con el municipio. El [portal de pago](https://tramites.munistgo.cl/pagopatente/) indica cobro semestral; el flujo reserva el anual completo en el mes 1 para no subfinanciarse.

## Contraste de la conversación sobre giros y rapidez

El [catálogo SII](https://www.sii.cl/catastro/codigos.htm) denomina **631200 «Portales web»**, **731001 «Servicios de publicidad prestados por empresas»** y **682000 «Actividades inmobiliarias realizadas a cambio de una retribución o por contrata»**. El usuario aclaró que la **propuesta de inscripción son 631200 como principal y 731001 como complementario**. No son dos patentes ni dos ingresos garantizados. La [clasificación oficial del INE](https://www.ine.gob.cl/docs/default-source/buenas-practicas/clasificaciones/ciiu/clasificador/ciiu4-cl-2012.pdf) describe 6312 como explotación de portales y 6820 como intermediación remunerada en alquiler de **bienes inmuebles**. Dado que EspaciGo modela comisión por reserva y abarca espacios de distinta clase, no puede deducirse solo del nombre «portal» si **682000** debe declararse: queda **fuera de la propuesta actual**, como pregunta para contador/SII según contrato y prestaciones reales. El catálogo clasifica 682000 con «G» para IVA/categoría, no con un «Sí/1» simple como los otros dos. La conversación no justifica asegurar que omitir 682000 evita requisitos o fiscalización; tampoco que agregarlo crearía otra patente.

La conversación afirma que la oficina virtual evita la DOM y la SEREMI y que la patente sale casi automáticamente. No hay base para prometerlo. Las [condiciones municipales de patente publicadas](https://tramites.munistgo.cl/solicitudpatente/condicionesgenerales.html) contemplan informe de zonificación y, cuando corresponda, verificación de la DOM, permiso/recepción final y autorización sanitaria. Esas condiciones parecen corresponder a un procedimiento anterior y requieren contraste con el flujo actual. La [Municipalidad anunció Patente Ágil en abril de 2026](https://www.munistgo.cl/patente-agil-nuevo-sistema-con-ia-permite-tramite-en-horas-y-sin-papeleo-en-santiago/) con plazos generales de dos horas a cuatro días, pero la noticia no aprueba Ahumada 131 ni estos giros. Tampoco se halló una regla general que obligue a **notariar el contrato de oficina virtual**: el proveedor ofrece firma electrónica simple; revisar qué documento aceptará el municipio en este expediente.

## Resultado y consultas pendientes

Con la oferta elegida, el simulador arroja **4.815.743 CLP** de salida en año 1, fondo con colchón de 20 % de **5.778.891 CLP**, brecha sobre capital propuesto de **2.778.891 CLP**, déficit máximo de **6.246.529 CLP** y VAN de caja **−1.791.437 CLP** al 12 % supuesto. El cambio mejora el ejemplo, pero no demuestra viabilidad. Si además se reemplazara la provisión de aseo por 2,88 UTM, el año 1 subiría a **4.902.299 CLP** y el VAN bajaría a **−1.989.127 CLP**. Los documentos DOM, si se exigen, son costos condicionales adicionales, no se incluyen en esos dos escenarios.

Pedir a Oficina Express contrato modelo, dirección/oficina exacta, ROL, respaldo de derecho de uso/subarriendo para la SpA y giros **631200/731001**, modalidad de firma, DTE, renovación y aseo. Consultar a Municipalidad de Santiago por escrito sobre zonificación, exigencias DOM/recepción final, patente provisoria/definitiva, tasa aplicada, aseo para ese inmueble y derechos exactos. Con contador/SII, preguntar expresamente si la comisión transaccional bajo esos contratos se cubre con 631200 o requiere **682000 u otra actividad**, y confirmar IVA y documento de cada servicio. Ninguna consulta fue enviada durante esta investigación; las filas de terceros continúan abiertas.

## Relación con ES1

La propuesta de intermediación de la entrega anterior permanece congelada. Este domicilio y las cifras de formalización son decisiones y escenarios nuevos de ES2; no alteran ES1 ni acreditan una SpA constituida.
