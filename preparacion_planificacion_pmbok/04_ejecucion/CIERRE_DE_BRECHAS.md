# Aplicación de las 21 correcciones de planificación

El alcance es la corrección documental y la construcción de una programación reproducible. Las fechas no acreditan desarrollo realizado, ensayos externos ni aprobación docente. La fuente metodológica aplicada es PMI (2017), sexta edición.

| Brecha | Corrección aplicada | Destino verificable |
|---|---|---|
| B01 | Edición corregida y distinción entre procesos de gestión y ciclo incremental. | VI 6.1.1–6.1.3 y referencia pmbok6. |
| B02 | Propósito, autoridad, restricciones y aceptación; separación de gobierno y constitución societaria. | VI 6.1.6; G.1/G.10; GOBIERNO_Y_ADAPTACION.md. |
| B03 | Adaptación de las diez áreas y controles integrados. | VI 6.1.6; G.7–G.9. |
| B04 | Diccionario completo de 28 paquetes con esfuerzo y aceptación. | G.2; JSON maestro. |
| B05 | Entrega, defensa y frontera comercial con condiciones distintas. | VI 6.2; Tabla G.1; G.10. |
| B06 | Calendario nominal, unidad de jornada, dedicación, corte y excepciones. | VI 6.2.1; G.1; modelo JSON. |
| B07 | Registro de 54 actividades y nueve hitos, con correspondencia EDT y fuente MPP. | G.3; CSV y XML. |
| B08 | Red cerrada, compuertas y secuencia de disponibilidad de personas. | G.5; cálculo y verificación independiente. |
| B09 | Esfuerzo separado de duración y tiempo calendario; sensibilidad de una jornada. | VI 6.2; G.5/G.6. |
| B10 | CPM del desarrollo hasta C0, holguras y comprobación de carga. | VI 6.2.3; G.5; calculo_cronograma.json. |
| B11 | Programa reconstruido sin inventar línea base; Gantt maestro y tres paneles. | Figura 6; figuras G.1–G.3; XV. |
| B12 | Campos y reglas de seguimiento sin inferir horas o avance de fechas. | XI 11.3; G.7; XV 15.3. |
| B13 | Conciliación de 960 h presupuestadas, 708 asignadas y 252 de reserva; reemplazo de ventana 360 h. | VI 6.4; G.8; H.5; informe conciliación. |
| B14 | Tres recursos con nombre, disponibilidad y responsables de actividad. | VI 6.3; G.6; XML y comprobación diaria/semanal. |
| B15 | Verificación por incremento y aceptación con límites de entorno. | XII 12.4; Q01–Q09; G.7. |
| B16 | Matriz de comunicaciones con audiencia, contenido, responsable y frecuencia. | G.9.2. |
| B17 | Ocho riesgos con escalas coherentes, dueño y disparador. | Tabla 6; Figura 5; G.9.1. |
| B18 | Servicios previstos, presupuesto y aceptación separados de contratación/activación. | VI 6.4; XIII; G.9.4. |
| B19 | Registro operativo de interesados, influencia y estrategia. | V y G.9.3. |
| B20 | Ajustes de calendario, decisión AWS y configuración con impactos explícitos. | XI 11.4; XV 15.2; G.7. |
| B21 | Cierre académico y transferencia sin atribuir aceptaciones futuras. | XV 15.3; XVI; G.10. |

## Límites que no se deben convertir en afirmaciones

La reserva temporal de la entrega es cero jornadas completas. El programa utiliza dedicación nominal sin excepciones personales acreditadas y no sustituye el registro efectivo de disponibilidad. Se explicita el riesgo y el control; no se certifica el plazo por existir una Gantt.

Las horas reales por actividad y la aceptación futura se registran cuando existe evidencia. Los indicadores SPI/CPI permanecen no calculables; no son tareas documentales olvidadas. Los proveedores y las pruebas dependientes del código conservan sus condiciones de habilitación en XII–XIII/F. COM es una frontera financiera de duración cero, sin trabajo programado el 1 de enero.

La interoperabilidad XML se verifica con MPXJ: 28 resúmenes, 63 hojas, tres recursos, 54 asignaciones y 708 horas. Un recálculo nativo en Microsoft Project no se presenta como comprobado.
