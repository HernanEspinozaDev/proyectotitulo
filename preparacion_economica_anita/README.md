# Preparación de la parte económica de Anita

El plan y estado de trabajo se encuentra en 00_PLAN_Y_ESTADO.md. La extracción conserva las 26 hojas del libro y el informe íntegro con sus 17 imágenes. El contraste identifica las diferencias entre modelos y la sustitución de costos de GCP por el escenario AWS.

La propuesta del Capítulo XIV contiene los dos flujos completos aportados para su comparación. El Anexo H transcribe todas las hojas como tablas editables con procedencia. Los importes AWS se adoptan como parámetros de planificación y se comprueban aritméticamente. Las discrepancias y los respaldos pendientes se enumeran antes de integrar una versión única en la tesis.

La comisión vigente indicada por el propietario es del 3 % más IVA por cada pago procesado. Se descuenta del importe que recibe quien publica, junto con el cargo de Mercado Pago. El préstamo del insumo se identifica como simulación y se adopta provisionalmente una meta de CLP 200.000 mensuales por fundador, condicionada a disponibilidad, y CLP 1.000.000 como objetivo adicional por persona. La actualización y los escenarios recalculados se encuentran en 02_contraste/decisiones_modelo_ingresos.md. La vista previa incorpora el 3 % más IVA y el modelo mensual por modalidad, junto a los dos flujos recibidos como antecedentes.

Para reconstruir la vista previa Word con DocSkill, ejecutar desde el repositorio `python3 preparacion_economica_anita/scripts/build_preview.py` con el entorno documental disponible. El PDF de revisión actual contiene 101 páginas y 101 tablas editables en su Word de origen.

La sección 14.6 incorpora el cálculo de cobros para remuneraciones. El soporte y los límites se encuentran en 02_contraste/tickets_para_remuneraciones.md. El script scripts/calcular_tickets_remuneraciones.py permite variar el monto por fundador sin alterar las extracciones.

Se incorpora Pro Pyme General como supuesto de una empresa proyectada, Año 1 de operación en 2027, y descuento nominal anual del 12 %. El calendario y las fuentes tributarias se documentan en 02_contraste/parametros_tributarios.json y en H.28.

El criterio vigente del ejercicio conserva impuesto fijo del 27 % como Anita, por indicación docente comunicada por el propietario. Se distingue de la tasa de descuento nominal anual del 12 % y de la tributación real del régimen proyectado. El calendario legal analizado antes queda como antecedente y no se aplica al cálculo académico.

La tasa base vigente es 12 % anual, confirmada por Anita y ratificada por el propietario. La justificación metodológica y sus límites se documentan en 02_contraste/justificacion_descuento12.md y en H.29. El 10 % y el 25 % quedan como antecedentes, no como tasas principales.

La referencia metodológica principal es Sapag Chain y Sapag Chain (2008), quinta edición. La revisión con páginas impresas y PDF se encuentra en 02_contraste/sapag2008_matriz_brechas.md; la ejecución pendiente se ordena en 02_contraste/sapag2008_plan_correcciones.md. Se incorporan citas y precisiones metodológicas en XIV propuesto y en H.29–H.30. El flujo financiero actualizado aún requiere cierre; la tesis principal conserva sus bloques reservados.

El primer corte de ejecución está en 04_modelo_sapag/INFORME_DE_AVANCE.md. Integra la compra inicial de equipos en cero, lanzamiento provisional, costos conciliados, 48 meses, flujos parciales y memorias de deuda e impuesto. Los umbrales activos se actualizan a 743 y 2.343 cobros al ticket de CLP 50.000 por la inclusión de útiles y dirección tributaria anual presupuestados. Las referencias anteriores de 728 y 2.328 corresponden al corte sin esas partidas.

El segundo corte incorpora revisión reproducible de coherencia y sensibilidad en H.36. Incluye once pruebas deterministas, umbrales operativos por año, quiebres parciales del VAN y contraste de convenciones de fechas. Ejecutar `scripts/actualizar_documento_ejecucion.py` actualiza el cuerpo y H.36; después construir con DocSkill y ejecutar `scripts/verificar_coherencia_sapag.py`. La memoria es `04_modelo_sapag/revision_coherencia_y_sensibilidad.json`.

El tercer corte completa liquidez, cobertura de deuda, indicadores y procedimiento de cierre en 14.7–14.8 y H.37–H.39. Para reproducir la cadena completa, utilizar el Python del entorno documental y ejecutar `scripts/reconstruir_preparacion_sapag.py --render --output-dir /tmp/espacigo-economia-sapag-render`. La exportación no sustituye la inspección visual. El archivo `04_modelo_sapag/liquidez_indicadores_y_cierre.json` conserva las cinco series, los aportes y las exclusiones; las entradas aún desconocidas siguen identificadas como tales.

Se incorporan las ratificaciones del propietario: enero de 2027 como lanzamiento objetivo, constitución y trámites dentro del presupuesto de CLP 1.200.000 y equipos personales compartidos. H.40 separa la recuperación de los CLP 6.240.000 valorizados de los desembolsos de caja; no se afirma que todo el trabajo esté realizado ni contratado.
