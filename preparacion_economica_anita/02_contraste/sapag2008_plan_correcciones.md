# Plan de corrección económica según Sapag

## Objetivo y restricciones

Cerrar una evaluación trazable con el método de Sapag, preservando el formato del flujo de Anita y las decisiones vigentes: comisión neta 3 %, descuento nominal anual 12 %, impuesto académico 27 %, Año 1 en 2027. El trabajo permanece en la preparación separada hasta conciliar los datos y autorizar la integración ya prevista. La tesis publicada conserva sus bloques reservados y no se modifican datos fuente.

## Tareas en orden de dependencia

- [x] **SP01. Verificar fuente y páginas.** Identificar autores, quinta edición de 2008, 463 páginas y desfase impresa/PDF. Entregable: sapag2008_fuente.json y referencia BibTeX.
- [x] **SP02. Comparar los insumos y la tesis publicada.** Evaluar 16 criterios con evidencia, páginas, corrección y destino. Entregable: sapag2008_matriz_brechas.md y JSON.
- [x] **SP03. Corregir la fundamentación metodológica.** Adoptar Sapag como fuente principal en XIV propuesto y H.29, identificar el flujo financiado e incorporar H.30. Conservar referencias originales como antecedentes sin atribuir a Sapag tasas prescritas.
- [ ] **SP04. Cerrar matriz comercial mensual.** Por categoría y modalidad, fijar espacios, cobros, ticket, captación, recurrencia y estacionalidad con origen de datos. Separar escenarios y evidencia. Depende de volúmenes y precios por ratificar.
- [ ] **SP05. Conciliar recursos e inversión.** Definir fecha de decisión, compras reales o futuras, equipos aportados, costos hundidos y oportunidad, gastos de lanzamiento, vida útil y reposiciones. Evitar duplicar los CLP 6.240.000 de desarrollo. Depende de clasificación de recursos y desembolsos.
- [ ] **SP06. Cerrar costos operativos y asignaciones.** Identificar costos fijos, variables y escalonados; ajustar AWS a la demanda; precisar pasarela, costos residuales, servicios y remuneración condicionada. Entregable: presupuesto mensual completo y reglas de pago. Depende de SP04 y SP05 y parámetros faltantes.
- [ ] **SP07. Conciliar caja mensual e impuesto académico.** Preparar cobros, liquidaciones, IVA, pagos y pérdidas; conservar 27 % y verificar la explicación de compensación de pérdidas frente a la tabla. No usar fondos de publicadores como caja propia. Depende de SP04–SP06.
- [ ] **SP08. Calcular capital de trabajo.** Aplicar déficit acumulado máximo y separar necesidades operativas de financiación de pérdidas; registrar variaciones por crecimiento. Entregable: memoria mensual y traslado de aportes al flujo. Depende de SP07.
- [ ] **SP09. Cerrar horizonte y recuperación final.** Mantener caso base de cuatro años de operación; elegir método de desecho y justificar activos o continuidad. No duplicar recuperación de capital de trabajo ni tratar patrimonio como liquidez. Depende de SP05–SP08.
- [ ] **SP10. Construir los dos flujos completos.** En el cuerpo, flujo puro y flujo financiado, ambos en el formato de Anita; deuda simulada y cuadros de amortización hasta saldo cero. Dependencias: SP07–SP09. La fuente histórica queda identificada para comparación.
- [ ] **SP11. Calcular indicadores a 12 %.** VAN con Año 0 sin descuento, TIR interpretable y recuperación simple/descontada por cada flujo; contrastar con cálculo independiente. Dependencia: SP10. No mezclar resultados de modelos distintos.
- [ ] **SP12. Calcular sensibilidad y emitir conclusión.** Variar cobros, ticket, costos, cambio y tasa según escenarios pertinentes; calcular umbrales de VAN = 0 y explicar variables críticas. No asignar probabilidades sin datos. Dependencia: SP11.
- [ ] **SP13. Integrar la parte económica a la tesis.** Tras cerrar el material, incorporar XIV y H, referencias y síntesis de conclusiones; actualizar índices y verificar tablas, páginas y vínculos. Mantener ajenas las secciones de planificación que siguen perteneciendo a Erick.

## Criterios de aceptación

La ejecución financiera no se marca terminada solo por contar con el plan o con una vista previa. SP04–SP12 requieren entradas y cálculos completos. Los scripts y tablas originales se conservan como antecedentes; las cifras del escenario actualizado se distinguen explícitamente. La conclusión puede ser favorable, desfavorable o condicionada y debe corresponder al VAN y a la necesidad de financiación calculados. No se modifican supuestos solo para obtener rentabilidad.

SP01–SP03 corresponden a la revisión documental terminada. SP04–SP13 mantienen sus criterios de cierre; el avance numérico posterior se registra a continuación, sin confundir un subtotal parcial con una evaluación final.

## Avance del primer corte de ejecución

| Tarea | Estado | Ejecutado | Falta para cerrar |
|---|---|---|---|
| SP04 | en curso | Proyección agregada de 48 meses generada; nueve categorías conservadas sin asignación inventada. | Ratificar mezcla, captación, recurrencia y ticket por categoría/modalidad. |
| SP05 | en curso | Equipos existentes sin compra inicial; lanzamiento de CLP 1200000 ratificado como provisional. | Desglosar lanzamiento, uso alternativo y trabajo incremental, aportes y reposiciones. |
| SP06 | en curso | Ocho partidas conciliadas, subtotal CLP 514083,02 mensual; útiles incluidos una sola vez. | Resolver conceptos sin monto o alcance y verificar contratación y consumo. |
| SP07 | en curso | Caja mensual parcial e IVA separado; conciliación demostrativa del impuesto histórico al 27 %. | Definir ciclo de liquidación, IVA de compras y base definitiva de impuestos. |
| SP08 | en curso | Necesidad acumulada de financiación parcial calculada sin duplicarla como capital de trabajo inicial. | Calcular capital del ciclo con desfases y condiciones completos. |
| SP09 | pendiente | Horizonte de cuatro años preservado; valor de cierre sin cuantificación. | Definir aporte de activos, reinversiones y método de cierre respaldado. |
| SP10 | en curso | Dos flujos parciales con la estructura de Anita; deuda simulada corregida hasta cero. | Completar las partidas no determinadas y cerrar flujo puro y financiado definitivos. |
| SP11 | en curso | VAN parciales al 12 % comprobados; se informa TIR no existente o no interpretable como inversión. | Recalcular indicadores definitivos y recuperación tras el cierre de entradas. |
| SP12 | en curso | Tres casos de demanda, once pruebas individuales, umbrales anuales y cruces de VAN parcial con 791 y 2.391 pagos constantes; contraste de fechas anual/mensual. | Cerrar costos de escalamiento, demanda, rezagos efectivos y cierre para resultados definitivos. |
| SP13 | pendiente | Tesis principal sin cambios, según preparación separada acordada. | Integrar cuando el material económico esté conciliado y listo para revisión. |

## Subtareas concretas terminadas en este corte

- [x] Registrar las dos decisiones del propietario sobre equipos y lanzamiento.
- [x] Generar 48 meses y cuatro resúmenes anuales sin crecimiento comercial añadido.
- [x] Conservar las nueve categorías y registrar la mezcla como pendiente.
- [x] Conciliar ocho partidas y corregir la omisión de útiles de oficina.
- [x] Recalcular los umbrales de cobros: 743 y 2.343 al ticket de CLP 50.000.
- [x] Preparar seis perfiles de caja parcial, distinguiendo pago condicionado y metas presupuestadas, con y sin deuda.
- [x] Corregir la deuda simulada a saldo cero con ajuste de CLP 1.
- [x] Reconciliar demostrativamente las pérdidas históricas descritas por Anita sin alterar la fuente.
- [x] Integrar dos flujos parciales al cuerpo y memorias H.31–H.35, con cifras y límites explícitos.
- [x] Verificar proyecciones, agregación anual, conciliación de fondos, impuesto, deuda, VAN y tickets.

El soporte está en 04_modelo_sapag/INFORME_DE_AVANCE.md y estado_plan.json. Las tareas de nivel superior permanecen abiertas mientras existan partidas sin valoración, mezcla comercial por ratificar y decisiones de cierre.

## Segundo corte de coherencia y sensibilidad

- [x] Corregir el umbral antiguo de 2.335 que conservaba el generador; la nota activa se construye desde JSON.
- [x] Distinguir las Tablas 15–17 históricas de las Tablas 18–21 vigentes y corregir referencias auxiliares.
- [x] Verificar los umbrales operativos por año: 743, 756, 770 y 784 para la meta inicial; 2.343, 2.356, 2.370 y 2.384 para el objetivo adicional.
- [x] Calcular once sensibilidades deterministas desde el caso base, sin asignar probabilidades.
- [x] Calcular quiebres parciales del VAN anual con metas fijas: 791 y 2.391 pagos al ticket de CLP 50.000; verificar los enteros adyacentes de forma independiente.
- [x] Contrastar VAN anual al cierre frente a VAN con importes mensuales prorrateados y tasa equivalente; no mezclar convenciones.
- [x] Verificar aritmética visible de las tablas, rótulos únicos, referencias al anexo y contenido compilado en Word.
- [x] Verificar que regenerar los documentos sin cambiar parámetros no altera su contenido.

El subtotal de costos y la comisión de referencia no cambian en este corte. Los nuevos quiebres son escenarios de evaluación con asignaciones completas presupuestadas, no sustituyen la regla de pago condicionado. La sensibilidad mantiene el costo identificado independiente del volumen; antes de adoptar los umbrales se requieren datos de escalamiento. Los padres SP04–SP12 conservan sus criterios de cierre. La revisión no cuantifica partidas desconocidas ni integra aún la tesis publicada.

## Tercer corte de ejecución de los cálculos restantes

- [x] Ejecutar el déficit acumulado máximo con 49 momentos para cada alternativa, incluido el Año 0.
- [x] Generar aportes mínimos adicionales y conciliar saldo antes y después del aporte, sin doble conteo de préstamos o trabajo valorizado.
- [x] Cuantificar capacidad de servicio de deuda por año: la caja propia resulta negativa en la referencia.
- [x] Calcular sensibilidad aislada de cuentas por cobrar de comisión neta a 0, 7 y 30 días; no atribuir esos plazos a la pasarela ni llamarla capital completo.
- [x] Completar el primer quiebre parcial de la etapa sin asignaciones: 391 pagos constantes; comprobar que la regla no activa pagos a fundadores.
- [x] Calcular VAN, TIR interpretable y recuperación simple/descontada para las cinco series presentadas.
- [x] Incorporar el método de cierre y calcular el cobro terminal neto que neutralizaría el VAN; mantenerlo como umbral, no como ingreso esperado.
- [x] Redactar capacidad de pago y conclusión del alcance delimitado en 14.7–14.8, con memorias H.37–H.39.
- [x] Crear una cadena de reconstrucción y auditoría para fuentes → parámetros → modelo → texto → Word → PDF.

Los cálculos disponibles quedan ejecutados. Los padres SP04–SP13 no se marcan terminados porque sus criterios incluyen datos aún no ratificados y la integración posterior a la conciliación. Se solicita aclarar desarrollo pasado/futuro, inclusión de trámites en lanzamiento y condición de los equipos. Siguen pendientes datos comerciales, condiciones efectivas de proveedores/pasarela, formalización de asignaciones, calendario del ciclo y evidencias de reposición/cierre. Esas entradas no se sustituyen por montos cero confirmados. El nuevo corte completa trabajo calculable, sin afirmar evaluación integral cerrada.

## Ratificaciones posteriores del propietario

- [x] Incluir constitución y trámites en CLP 1.200.000 de lanzamiento; no sumar un segundo egreso por ellos.
- [x] Clasificar los equipos como personales y compartidos; no presumir compra o transferencia de dominio a la empresa.
- [x] Registrar enero de 2027 como objetivo de lanzamiento.
- [x] Interpretar CLP 6.240.000 como valorización global preoperativa; no atribuir al propietario una clasificación segura de trabajo pasado o futuro que no declara.
- [x] Evaluar separadamente recuperar esa valorización, sin sumarla a aportes de caja ni deducirla tributariamente por el solo hecho de valorizarla: quiebres parciales 548, 948 y 2.548 pagos para etapa sin asignaciones y las dos metas.

Las tres aclaraciones se incorporan. No se vuelve a pedir definición sobre inclusión de trámites o uso compartido. El reparto pasado/futuro y el costo de oportunidad incremental no se infieren del importe global. Las condiciones efectivas de proveedores y la valoración final continúan delimitadas en H.39; H.40 documenta la ratificación.
