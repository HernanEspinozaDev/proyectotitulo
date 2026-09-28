# 05. Economía: cada supuesto y con qué evidencia se reemplaza

El Anexo A y la sección 2.1 son **aritmética reproducible sobre supuestos**, no resultados observados. Esta tabla dice qué cambiar exactamente y quién puede aportar el dato.

Los valores vigentes están en [`supuestos_bootstrap.json`](../supuestos_bootstrap.json) (caso base) y [`supuestos_segmentado.json`](../supuestos_segmentado.json) (escenario segmentado sintético). Al cambiar un valor hay que recalcular y actualizar el Anexo A y el resumen de 2.1.

## Resultados vigentes, solo para referencia

| Indicador | Caso base, ticket único | Segmentado **sintético** |
| --- | ---: | ---: |
| Contribución del año 3 | 10.424.507 CLP | 350.688 CLP |
| VAN de caja a 36 meses | −1.791.437 CLP | −12.771.812 CLP |
| Déficit máximo en 36 meses | 6.246.529 CLP | 15.891.086 CLP |
| TIR de caja | −9,20 % | No definida |

Lectura que ya está en el informe: **el ticket medio de 100.000 CLP oculta categorías que no cubren sus costos variables**. Bajo 35.909 CLP de arriendo, una reserva no paga pasarela, firmas, KYC y otros cargos. El margen operativo modelado del año 3 es 23,35 %, inferior a la meta declarada de 25 %. El punto de equilibrio anual es ≈ 858 reservas sin remunerar el tiempo y ≈ 4.892 si se reconoce todo el esfuerzo valorizado.

## Supuestos por reemplazar

| # | Supuesto vigente | Valor | Con qué se reemplaza | Quién aporta |
| --- | --- | --- | --- | --- |
| E-01 | Arriendo final por reserva | 100.000 CLP | Precio final medido por `categoría × modalidad`, con duración y unidad de tiempo | Trabajo de campo (fila 7 de terceros) |
| E-02 | Volumen de reservas | 0 / 720 / 1.800 al año | Reservas pagadas observadas, con rechazos y cancelaciones por cohorte | Producto en operación |
| E-03 | Reparto del volumen por categoría | 20 % por segmento, **sintético** | Participación real por categoría, medida | Trabajo de campo |
| E-04 | Comisión neta | 12 % del arriendo | Tasa aceptada por los arrendadores, contrastada con competencia | Entrevistas + prueba con clientes piloto |
| E-05 | Tarifa de pasarela | 3,19 % sobre el cobro total | Tarifa contractual de Split del proveedor | Cotización (fila 2 de terceros) |
| E-06 | Incidencia económica de esa tarifa | La absorbe EspaciGo, con compensación hipotética al vendedor | Liquidación real: quién la paga y cómo se documenta | Cotización + contador |
| E-07 | Firma electrónica | 1.000 CLP netos por firmante, dos por reserva | Cotización por documento y tipo jurídico | Cotización (fila 3) |
| E-08 | Verificación de identidad (KYC) | 500 CLP por reserva, prorrateado | Tarifa por usuario nuevo y por revalidación | Cotización (fila 3) |
| E-09 | Otros cargos variables | 500 CLP por reserva | Cargos reales por operación | Cotización |
| E-10 | Tipo de cambio | USD/CLP 1.000 | Tipo de cambio de la factura | Contador (fila 4) |
| E-11 | IVA de servicios de nube y crédito fiscal | 19 % supuesto, crédito no comprobado | Primera factura pagada y su registro contable | Contador (fila 4) |
| E-12 | IPC anual | 4 % supuesto | Índice observado al momento de actualizar | Fuente pública al cierre |
| E-13 | Impuesto de Primera Categoría | 27 % académico constante | Régimen tributario real de la SpA y su calendario | Contador (fila 5) |
| E-14 | PPM | 0,25 % como provisión de liquidez | Tasa aplicable al régimen real | Contador |
| E-15 | Tasa de descuento | 12 % nominal supuesto | Tasa justificada del proyecto | Equipo, con el contador |
| E-16 | Colchón de caja | 20 % sobre el déficit del año 1 | Política de liquidez acordada | Equipo (D-09) |
| E-17 | Capital social propuesto | 3.000.000 CLP en 3.000 acciones | Capital realmente suscrito y pagado | Equipo (D-09/D-10) |
| E-18 | Financiamiento ilustrativo del año 1 | 5.778.891 CLP (≈ 1.926.297 por fundador) | Aporte acordado y efectivo | Equipo (D-09) |
| E-19 | Provisión de captación con Meta Ads | 357.000 CLP en seis meses | Costo por publicación y por reserva medido en campaña | Campaña (fila 9) |
| E-20 | Asco municipal | 120.000 CLP de provisión | Liquidación municipal | Municipio (fila 6) |
| E-21 | Patente comercial | 1 UTM anual ilustrativa (71.721 CLP) | Liquidación de la patente única de la SpA | Municipio (fila 6) |
| E-22 | Oficina virtual | 50.000 CLP/año + 5.000 CLP de firma, IVA incluido | Contrato firmado y DTE válido | Oficina Express (fila 6) |
| E-23 | Honorarios profesionales de inicio | 800.000 CLP netos en tres partidas | Presupuestos o contratos | Profesionales (fila 6) |
| E-24 | Valor hora del trabajo fundador | 15.000 CLP/h | Criterio acordado y documentado | Equipo |
| E-25 | Horas por fundador | 20 / 10 / 10 h semanales, 48 semanas | Disponibilidad real declarada | Equipo (D-01) |
| E-26 | Costo de oportunidad del año 1 | 43.200.000 CLP, informado aparte | Igual criterio, actualizado con E-24 y E-25 | Equipo |

## Cómo se mide el mercado (resumen operativo)

Protocolo completo en [`INV-016_metodologia_demanda.md`](../INV-016_metodologia_demanda.md):

1. **Fichas comparables** por `categoría × modalidad × comuna`, con fecha, enlace, superficie o capacidad, duración mínima, precio total, impuestos, garantía, cancelación y disponibilidad; separar precio normal de promoción.
2. **Entrevistas consentidas** a arrendadores y arrendatarios por separado; al arrendador, turnos ofrecibles, restricciones de subarriendo y comisión aceptable; al arrendatario, duración real, precio total tolerable y condiciones de garantía.
3. **Regla de cálculo:** `reservas posibles = turnos comercializables × ocupación observada × conversión a pago`, sin contar la conversión dos veces.
4. **No se cuentan** visitas web, respuestas favorables ni cuotas exploratorias como ventas.
5. Solo tras habilitar el producto: reservas pagadas conciliadas.

## Reglas para no distorsionar el resultado

- No usar el escenario más favorable como conclusión; publicar base y sensibilidad.
- No imputar a un proveedor un precio propio ni presentar una tarifa pública de otro producto como precio contratado.
- No mezclar unidades distintas (una hora, un día y un mes no se promedian).
- No sumar a los ingresos las garantías ni los fondos de terceros.
- Mantener **separados** comisión propia y fondos de terceros, caja y costo de oportunidad, y escenarios hipotéticos y cotizaciones.
