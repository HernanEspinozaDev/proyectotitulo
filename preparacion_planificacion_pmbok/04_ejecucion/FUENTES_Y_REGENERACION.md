# Fuentes editables y regeneración

La fuente única es `tesis_final/assets/diagramas_src/cronograma_espacigo.json`. Las 28 fichas, actividades y asignaciones se editan allí; `crear_modelo.py` conserva el origen reproducible de este primer modelo. No se debe ejecutar el creador sobre una versión editada sin conciliar los cambios.

1. Ejecutar `python3 tesis_final/scripts/calcular_cronograma.py` para recalcular y exportar JSON, CSV y Project XML.
2. Ejecutar `python3 tesis_final/scripts/render_planificacion.py` para regenerar Gantt, red, EDT y riesgos en PNG y SVG. Requiere Matplotlib. Los antiguos EDT PlantUML/mapa Mermaid se sustituyen para evitar dos fuentes divergentes.
3. Ejecutar `python3 tesis_final/scripts/integrar_planificacion.py` para regenerar las fichas y las tablas de actividades de G. La narrativa académica de VI/XV y el resto del anexo se conserva. Si cambia el modelo, se revisan expresamente las fechas, síntesis y tablas restantes antes de compilar.
4. Ejecutar `python3 tesis_final/scripts/verificar_planificacion.py` y compilar `python3 build_thesis.py` con el Python del runtime documental; verificar Word y PDF.

La nueva Figura 6 desplaza por una sola vez las figuras posteriores a 7–19. Las tablas financieras conservan los números 14–24 y H. El XML incorpora 28 resúmenes EDT y 63 nodos de actividad/hito; las 54 asignaciones suman 708 h, sin duplicar el trabajo de los resúmenes. El MPP original se preserva. La lectura con MPXJ verifica interoperabilidad de estructura; no acredita un recálculo nativo de Microsoft Project.

El corte del 16-11-2026 no dispone de horas reales por actividad. Esa ausencia se presenta como límite de medición, sin bloquear la definición documental del plan ni fabricar avance. La fase comercial comienza en el modelo financiero el 01-01-2027, sin tarea de trabajo asignada a esa fecha.
