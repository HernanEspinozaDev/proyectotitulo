# Especificación de la Gantt y del Anexo G

## 1. Una sola fuente de programación

El registro maestro del cronograma se conservará en JSON y en una tabla interoperable. Las figuras, las tablas de fechas y la exportación para Project se generarán a partir del mismo modelo. Los ID de actividad serán estables y su correspondencia con los ID originales de Erick y los paquetes EDT se conservará en una matriz.

El modelo tendrá fechas, calendarios, responsables, esfuerzo, vínculos, hitos y estado de evidencia. Los nombres mostrados en una figura podrán abreviarse, pero la tabla del anexo mantendrá la denominación completa.

## 2. Vistas para la tesis

| Vista | Destino | Contenido y regla de legibilidad |
|---|---|---|
| Gantt maestro | Capítulo VI, 6.2. | Aproximadamente 10–14 filas de paquetes o incrementos. Agosto–diciembre de 2026 y referencia visible al 01-01-2027. Hitos 01-12 y 09-12 diferenciados. |
| Resumen de hitos | Capítulo VI, 6.2. | Fecha, entregable, condición de aceptación y referencia al detalle. Evitar una columna por cada semana del semestre en una tabla de texto. |
| Gantt de detalle | Anexo G. | Ventanas o fases con escala consistente, filas e ID legibles. Las actividades que continúen en otra vista se identifican como continuación, sin duplicar horas. |
| Red del cronograma | Anexo G; síntesis en 6.2 si ayuda a la explicación. | Dependencias y ruta crítica calculadas. Dividir por incrementos si una red completa impide leer los nodos. |
| Recursos y esfuerzo | Anexo G; síntesis en 6.3–6.4. | Capacidad por integrante y período; asignaciones, horas y comprobación de sobrecarga. |
| Puente temporal económico | Anexos G/H y explicación en XIV. | Trabajo académico, mejoras de defensa, transición y operación; distinción entre valoración y pagos. |

La plantilla permanece en la orientación y dimensiones vigentes. Antes de recurrir a una imagen horizontal o reducir tipografía, se divide el detalle en paneles. El texto de una captura de todo Microsoft Project reducido a una página no constituye una solución de presentación.

## 3. Convenciones gráficas

- Barras para trabajo programado y símbolos de hito para entrega, defensa e inicio comercial.
- Ruta crítica identificable también en escala de grises, mediante trazo o patrón además del color.
- Diferencia visible entre programación, ejecución con evidencia y propuesta de transición. No dibujar avance real sin respaldo.
- Etiquetas de meses y años, fecha de corte y leyenda de unidades y estados.
- Columna de ID y nombres abreviados vinculados al inventario completo.
- No utilizar el 0 % del MPP recibido para representar como pendiente toda la historia del desarrollo.

## 4. Fuentes y generación

Antes de agregar figuras se revisarán las existentes de VI: ciclo de vida, EDT y riesgos. La figura de ciclo debe dejar claro si representa un incremento o el proyecto completo; la sucesión de incrementos y sus revisiones debe coincidir con la Gantt. La EDT y el mapa de riesgos se regenerarán solo si cambian sus datos o etiquetas.

Se propone conservar el modelo de datos y las fuentes de figuras en `tesis_final/assets/diagramas_src/`, el generador reproducible en `tesis_final/scripts/` y los PNG insertables en `tesis_final/assets/figuras/`, siguiendo las rutas efectivas de la tesis.

El generador podrá utilizar herramientas de representación técnica como Matplotlib/SVG. Las imágenes de Gantt no requieren generación artística. Se conservará SVG para edición y PNG de resolución suficiente para el Word; ambos derivarán de las mismas fechas y relaciones.

La exportación de intercambio será **Microsoft Project XML**, compatible con apertura/importación en Project. El MPP original se preservará. Una extensión `.mpp` no se utilizará para un archivo que en realidad contenga XML o una imagen.

## 5. Organización propuesta del Anexo G

| Sección | Contenido |
|---|---|
| G.1 | Alcance de planificación, fuente temporal, calendario y convenciones. |
| G.2 | Diccionario de los paquetes EDT, con criterios y responsables. |
| G.3 | Registro completo de actividades y trazabilidad al MPP recibido. |
| G.4 | Gantt maestro y vistas de detalle. |
| G.5 | Dependencias, ruta crítica, holguras y restricciones de fecha. |
| G.6 | Recursos, dedicación, esfuerzo y revisión de capacidad. |
| G.7 | Seguimiento de hitos, aceptación, evidencias y cambios. |
| G.8 | Conciliación con presupuesto y estudio económico. |
| G.9 | Riesgos, comunicaciones e interesados del proyecto, con síntesis en el cuerpo. |
| G.10 | Cierre académico y transferencia a preparación comercial. |

El diccionario puede distribuirse en fichas compactas o tablas por grupos; se evita forzar doce campos extensos en una tabla de una sola página. La información compartida puede referenciarse para no repetir el mismo texto en cada ficha.

## 6. Integración con formato institucional

Cada tabla y figura tendrá rótulo, título y nota de elaboración propia. Los diagramas se insertarán renderizados, con texto alternativo vacío según la convención del repositorio. No se insertarán bloques Mermaid/PlantUML crudos ni código del generador en el cuerpo académico.

Se mantendrá la numeración correlativa de figuras y tablas del cuerpo y la numeración por anexo para las vistas G. El nuevo Gantt en VI puede desplazar números de capítulos posteriores: se actualizarán rótulos, remisiones e índices conjuntamente, sin cambiar datos financieros por un cambio de número de tabla.

## 7. Comprobaciones antes de cerrar

1. Las fechas y duraciones mostradas coinciden con el modelo de programación.
2. Los paneles no pierden tareas ni duplican esfuerzo al continuar una actividad.
3. Las dependencias y el trazado crítico se generan del cálculo; no se colorean manualmente para aparentar una ruta.
4. El cuerpo remite a los ID y secciones correctos del Anexo G; G/H coinciden en recursos y etapas.
5. En el Word/PDF final se leen nombres, meses, hitos y notas al tamaño de impresión previsto.
6. Ningún rótulo queda separado de la figura, ninguna tabla corta cifras y ningún índice apunta a una página anterior a la última compilación.
7. Los datos, el código fuente, las imágenes y los archivos de entrega quedan versionados juntos.
