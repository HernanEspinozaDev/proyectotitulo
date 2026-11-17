# Correcciones de planificación incorporadas a la tesis

La ejecución desarrolla las 21 brechas del diagnóstico y las tareas P03–P12 del plan. El Word y el PDF se construyen con DocSkill sobre la misma plantilla institucional. El PDF final tiene 573 páginas; la edición anterior a esta aplicación tiene 543.

## Contenido incorporado

- **Capítulo VI:** referencia PMBOK sexta edición de 2017, separación de gestión y ciclo incremental, gobierno del proyecto, EDT, ocho riesgos y calendario de referencia. Se completa 6.2, se corrige RACI y se explican esfuerzo, duración, capacidad y valoración.
- **Anexo G:** diccionario de los 28 paquetes, responsables y aceptación; registro de 54 actividades y nueve hitos; correspondencia con el inventario del MPP; fechas, vínculos lógicos/de recurso y holguras; recursos, seguimiento, cambios, comunicaciones, interesados, adquisiciones y cierre.
- **Capítulo XV:** comparación con la Gantt recibida, ensayo inicial rechazado por cierre tardío, secuencia corregida y reglas de seguimiento de entrega y defensa.
- **Capítulos V, XI–XIII, XVI y XVIII:** remisiones a interesados, seguimiento, calidad, habilitación, conclusiones y organización del anexo. Las verificaciones externas mantienen sus condiciones técnicas.
- **Anexo H y preparación económica:** sustitución de la ventana de 360 horas y conciliación por etapas. Se corrige la remisión de sensibilidad a las Tablas 19 y 20 y se actualizan parámetros y generadores.

## Calendario y esfuerzo

| Elemento | Referencia incorporada |
|---|---|
| Desarrollo académico | 11-08-2026 a 30-11-2026; 632 h asignadas |
| Entrega | 01-12-2026 |
| Preparación de defensa | 36 h; tareas del 02 al 04-12 |
| Defensa | 09-12-2026 |
| Transición | 40 h; tareas del 10 al 15-12 dentro de la ventana precomercial |
| Inicio del Año 1 comercial | 01-01-2027 |
| Dedicación | 20 h semanales por integrante; calendario nominal de 4 h de lunes a viernes |
| Capacidad académica | 960 h del equipo; 328 h sin asignar en esa etapa |
| Total de actividades | 708 h, valorizadas en CLP 4.602.000 |
| Reserva del presupuesto global | 252 h, equivalentes a CLP 1.638.000 |
| Presupuesto valorizado conservado | 960 h a CLP 6.500: CLP 6.240.000 |

El cierre académico calculado llega al 30 de noviembre, con **cero jornadas completas de margen** antes de la entrega. La tesis informa este riesgo y sus controles. La programación reconstruida no acredita fechas reales, horas ejecutadas ni aprobación histórica. El calendario nominal sin excepciones personales acreditadas exige actualización ante disponibilidad distinta. COM es una frontera financiera de duración y esfuerzo cero; no programa trabajo el 1 de enero.

## Figuras y archivos editables

Se incorpora una Gantt maestra en la Figura 6 y tres paneles de detalle en G.1–G.3. G.4 representa el tramo crítico y sus ramas. Se actualizan la EDT y el mapa de riesgos; la numeración posterior de figuras queda entre 7 y 19 y sus remisiones se actualizan. Las imágenes se conservan en PNG y SVG con fuente JSON y código de cálculo/renderizado separados.

El intercambio `Cronograma_espaciGo_Project.xml` contiene 28 resúmenes EDT, 63 actividades/hitos y tres recursos con nombre. Las 54 asignaciones suman 708 horas. La lectura con MPXJ verifica estructura e interoperabilidad; no se atribuye un recálculo nativo de Microsoft Project. El MPP original permanece intacto.

## Comprobaciones completadas

- Fuente única y hash de cálculo concordantes; paquetes y actividades sin duplicación de esfuerzo.
- Red sin ciclos ni referencias inexistentes; verificación independiente de disponibilidad diaria y semanal, sin sobrecargas bajo el calendario nominal.
- 27 tablas financieras con datos y cuadrículas iguales al corte anterior. Se conserva la plantilla de 16 partidas y años 0–4; los cuatro flujos completos aparecen en páginas 98–101 del PDF.
- Parámetros financieros y resultados conservados: la conciliación de horas no inventa egresos de caja ni modifica comisión, impuestos, VAN o TIR.
- Manifiesto, plantilla DOCX y perfil institucional preservados.
- 22 tablas y ocho figuras de planificación comprobadas en el PDF, con imagen junto a su rótulo y enlaces de índice a sus páginas.
- Word renderizado mediante `render_docx.py`; PDF completo renderizado y páginas modificadas inspeccionadas. Se corrigen diagramas divididos, columnas estrechas y títulos de ficha huérfanos.

Los archivos `CIERRE_DE_BRECHAS.md`, `verificacion_integracion_planificacion.json`, `verificacion_word_pdf.json` y `REVISION_INDEPENDIENTE.md` permiten revisar cada corrección y sus límites. `FUENTES_Y_REGENERACION.md` explica cómo regenerar los entregables.
