# INV-009 — Evaluación económica con enfoque Sapag

> **Antecedente pedagógico superado.** Este registro conserva el primer ejercicio calculado con 3.600 reservas desde el año 1. Tras la aclaración del usuario de que aún no hay ingresos y el estudio de una SpA autofinanciada, el presupuesto y la conclusión vigentes son [INV-010](INV-010_infraestructura_y_formalizacion.md), [supuestos_bootstrap.json](supuestos_bootstrap.json) y el [Anexo A](../anexos/A_evaluacion_economica.md). El VAN positivo indicado abajo no describe el escenario actual ni justifica inversión.

- Estado: investigación documental y ejemplo calculado; prefactibilidad real pendiente.
- Fecha de consulta: 2026-09-23.
- Secciones: 2.1, 2.2, 3.6 y Anexo A.
- Base: ES1, «Modelos de negocio y monetización digital» (comisión transaccional) y «Plan de recursos» (14.400.000 CLP de oportunidad; presupuesto histórico total 14.460.950 CLP). Autoridad: informe final inmutable; texto consultado en `../../ES1PT/docx/informe.md`.

## Pregunta y decisión de trabajo

¿Qué volumen, estructura de costos y condiciones permitirían recuperar los recursos de EspaciGo con margen operativo objetivo del 25 %, indexación y un impuesto del 27 %? Esos factores proceden de la solicitud del usuario; no se atribuyen a la rúbrica mientras no exista evidencia en ella. Se desarrolla un escenario ilustrativo que conserva la comisión transaccional y no altera RQF/RNF.

Por instrucción del usuario se priorizan investigación y redacción. DOCX, actualización de campos, APA visual y perfil Word quedan para el cierre del contenido, según `../plan_de_trabajo.md`; INV-008 conserva el diagnóstico previo sin repetir experimentos.

## Fuentes consultadas y límites

| Clave | Fuente primaria y fecha | Hallazgo verificable | Límite |
| --- | --- | --- | --- |
| es2sapag2014 | [McGraw-Hill, ficha editorial](https://www.mheducation.com.co/preparacion-y-evaluacion-de-proyectos-9786071511447-col), ©2014, publicación comercial 18-12-2013 | Nassir Sapag Chain, Reynaldo Sapag Chain y José Manuel Sapag Puelma; 6.ª edición, ISBN 9786071511447; índice con inversiones, flujos e inflación | Ficha e índice públicos; no lectura íntegra ni cita de páginas |
| es2sapagmetodo | [Sapag, presentación del libro](https://sapag.cl/preparacion-y-evaluacion-de-proyectos/), sin fecha editorial identificada | Temas de costos, inversiones, flujos, costo de capital, riesgo y sensibilidad | La apertura directa falló; se consultó contenido indexado del sitio, sin inferir texto de capítulos |
| es2ineipc202608 | [INE, IPC de agosto](https://www.ine.gob.cl/sala-de-prensa/prensa/general/noticia/2026/09/08/%C3%ADndice-de-precios-al-consumidor-(ipc)-de-agosto-present%C3%B3-una-variaci%C3%B3n-mensual-de-0-6), 08-09-2026 | 0,6 % mensual; 3,6 % acumulado; 4,1 % a doce meses | Observación de agosto, no proyección del proyecto |
| es2bcmetainflacion | [Banco Central, Política Monetaria](https://www.bcentral.cl/es/areas/politica-monetaria), sin fecha editorial identificada | Meta de inflación de 3 % a dos años | No garantiza IPC ni retorno de EspaciGo |
| es2siiregimenes | [SII, Tipos de regímenes](https://www.sii.cl/destacados/modernizacion/tipos_regimenes_mt.html), sin fecha editorial identificada | Régimen general semiintegrado con 27 %; existen otros regímenes | No determina el régimen de la futura entidad; no usar su resumen histórico Pro Pyme para fijar tasas actuales |
| es2siitasas | [SII, tasas de Primera Categoría](https://www.sii.cl/preguntas_frecuentes/declaracion_renta/001_140_4708.htm), actualizada 25-05-2026 | Tabla diferencia ejercicios comerciales/tributarios y regímenes; incluye tasa Pro Pyme diferente para AT2026 | No extender 27 % a todos los contribuyentes ni a años futuros sin revisar normativa |

Los datos bibliográficos están en `../referencias.bib`. Las fórmulas y tablas son elaboración propia. Las fuentes oficiales no confirman demanda, costos operativos, comisión, IPC futuro, capacidad ni rentabilidad de EspaciGo.

## Método aplicado y resultados

1. Separar la preparación técnica/económica de la decisión de inversión: definir unidad cobrable y mercado antes de afirmar viabilidad.
2. Valorar trabajo futuro y gastos iniciales sin duplicarlos; distinguir efectivo, oportunidad y costos hundidos. Desglosar operación por unidad y frecuencia.
3. Proyectar tres años nominales con volumen constante y 4 % supuesto. No extrapolar automáticamente el último IPC observado.
4. Calcular flujo sin deuda con base tributaria simplificada, CT antes del período que financia, recuperación explícita y valor residual cero.
5. Descontar al 12 % nominal supuesto y variar demanda, costos, precio y recuperación. Revisar la raíz VAN(TIR) y casos numéricos conocidos con pruebas aisladas.

Entradas de este ejemplo histórico: [supuestos editables](supuestos_economicos.json). Calculadora independiente: `../../herramientas/evaluacion_economica.py`. Resultados regenerables: `../build/evaluacion_economica.json`. El Anexo A fue actualizado y ya no reproduce este ejemplo.

Este primer ejemplo producía inversión económica de 18.000.000 CLP, VAN de 1.144.898 CLP y TIR de 15,43 %. Una caída de demanda del 20 % llevaba el VAN a -8.842.238 CLP. **Resultados históricos del ejercicio, no conclusión vigente**: suponían ventas inmediatas sin evidencia comercial. La mayor brecha es comercial y de costos, no de presentación Word.

Comprobación del 23-09-2026: cinco pruebas numéricas de `Informes.tests.test_evaluacion_economica` pasan (VAN/TIR conocidos, flujo/impuesto, pérdidas sin devolución, CT sin doble recuperación y entrada inválida). La búsqueda numérica de VAN=0 dio 3.517,4612 reservas/año constantes, redondeadas hacia arriba a 3.518. `ensamblar ES2PT` terminó con los avisos esperados de contenido pendiente. No se ejecutó Word, renderizado ni validación visual; no se instaló ninguna dependencia.

## Paquetes de investigación para sustituir supuestos

| Paquete | Dato/evidencia que falta | Efecto en el cálculo |
| --- | --- | --- |
| Mercado | Oferta activa, reservas por espacio/mes, ocupación, duración y arriendo medio; fuente y muestra identificadas | Q, GMV, comisión aceptable y ramp-up mensual |
| Ingeniería y capacidad | Región, entornos, carga media/pico, almacenamiento, backups, red, observabilidad y horas operativas | TCO comparable Cloud Run/VM y escalones de costo, sin asumir RNF cumplidos |
| Integraciones | Producto habilitable, cargo por evento/importe, intentos fallidos, firma, identidad y devolución | CV por reserva derivado de eventos y sus probabilidades, sin atribuir capacidades no habilitadas |
| Personas y activos | Horas futuras por paquete de trabajo, costo total de contratación, equipos disponibles y costo alternativo | Caja frente a oportunidad, inversión y reemplazos; excluir trabajo ya incurrido |
| Tributación y financiamiento | Entidad/régimen, fechas comerciales, IVA, pérdidas, depreciación y plazos de cobro/pago | RLI, capital de trabajo por déficit acumulado mensual, costo de capital |
| Riesgo | Evidencia de demanda, captación, fallos, descuentos, contingencias y continuidad | Sensibilidades conjuntas; no asignar probabilidades ficticias |

Primero completar partidas y cotizaciones documentales que puedan investigarse sin implementación. Mantener separados los ensayos de capacidad que dependen del producto. El presupuesto de desarrollo ES2 y la evaluación de explotación comercial son vistas distintas y deben conciliarse.

## Corrección de un antecedente de cotización

El subtotal anterior de Cloud SQL (USD 69,97/mes) no conserva evidencia suficiente de que las tarifas correspondan a Santiago y a esa configuración. Se retira su uso como costo regional verificado en 2.1 y se identifica la limitación en INV-002. INV-010 emplea tarifas iniciales Iowa y una provisión regional explícitamente hipotética, sin reutilizar aquel subtotal como cotización. Para comparar alternativas se deberá registrar región seleccionada, edición, disponibilidad, unidad, moneda y fecha en una cotización exportada o evidencia equivalente.

## Skill y continuidad

Se creó la skill personal `evaluacion-proyectos-chile` en `~/.codex/skills/`, con metodología y fuentes reutilizables. Puede invocarse como `$evaluacion-proyectos-chile`. La calculadora y los datos permanecen en el repositorio, por lo que el modelo se reproduce sin depender de esa instalación personal. No se requiere Word ni instalar paquetes para calcular.
