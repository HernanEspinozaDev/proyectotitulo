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

SP01–SP03 corresponden a esta revisión documental; SP04–SP13 quedan abiertos con dependencias explícitas y no representan trabajo ya ejecutado.
