# 04. Trabajo del producto: lo que exige entorno, despliegue y medición

Todo esto necesita producto funcionando y un entorno autorizado. La rúbrica pide **planificar** pruebas y SLA, no presentarlos como ejecutados, así que mientras falte el entorno cada fila se conserva como planificada.

Entorno mínimo necesario para la mayoría de las filas: una instancia de ensayo con Cloud SQL/PostGIS, Cloud Storage y Secret Manager (supuesto SUP-15), separada de cualquier dato real.

| # | Qué falta | Evidencia que lo cierra | Depende de | Referencia |
| --- | --- | --- | --- | --- |
| P-01 | **Aplicar el DDL propuesto** a un servidor de ensayo | Base desplegada y esquema vigente | D-06, entorno | 3.4, Anexo B |
| P-02 | **Ejecutar los doce ensayos del modelo** MD-01 a MD-12, incluida la prueba concurrente del calendario de ocupación | Resultados fechados con versión, datos y fallos encontrados | P-01 | 3.4, Anexo B |
| P-03 | **Ejecutar los dieciséis casos de prueba** PT-01 a PT-16, incluido PT-16 de privacidad | Informe por caso con entorno, datos, esperado/observado y responsable | P-01, D-08 | 5.1, Anexo C |
| P-04 | **Medir los once KPI y los cinco SLA** y llenar el registro de mediciones | Serie de mediciones con fuente y responsable | P-01, entorno de carga | 4.1, 4.2 |
| P-05 | **Ensayar respaldo, restauración y continuidad** (RPO 4 h, RTO 6 h) | PT-11 con tiempos medidos y evidencia de restauración | P-01, D-15 | 5.1, 6.2 |
| P-06 | **Probar carga y escalado** (200 usuarios concurrentes; 500 con 100 escrituras/s) | PT-09 y PT-10 con percentiles y trazas | entorno de carga | 4.1, 5.1 |
| P-07 | **Demostrar la portabilidad** de RNF-034 a RNF-036 | Recorrido reproducido en contenedores locales y con un proveedor alternativo | P-01 | 3.7 |
| P-08 | **Desplegar monitoreo y alertas** y acordar la ventana de mantención | Sondeos activos, umbral de dos fallos consecutivos y acuerdo de exclusión | D-15 | 6.1 |
| P-09 | **Implementar los procedimientos** de continuidad, cambios e incidentes y ejecutar un simulacro | Simulacro ejecutado y registro del incidente | P-08 | 6.2, 6.3 |
| P-10 | **Ensayos comparativos de tecnologías**: latencia y concurrencia del flujo seleccionado y costo de Cloud Run frente a VM con SKU comparables en Santiago | Registro de ensayo con entorno, versión y carga, y la ratificación del equipo | D-13, entorno | 2.1, 2.2 |
| P-11 | **Ensayo de alteración de RNF-017**: exportar eventos sintéticos, aplicar retención bloqueada por siete días e intentar alterar o borrar | Prueba de alteración **fallida** con evidencia fechada | D-07 (plazo de retención) | 3.0 |
| P-12 | **Inventario físico** de las estaciones de trabajo y fijación de parches e imágenes instalados | Inventario con sistema operativo, CPU, memoria, almacenamiento y conectividad, más el archivo de dependencias | — | 2.2 |
| P-13 | **Mapear los literales de estado de ES1** a los estados propuestos y validar cardinalidades | Tabla de correspondencia acordada con el equipo | D-04 | Anexo B |
| P-14 | **Completar las entidades fuera del alcance parcial** del Anexo B: perfil y cuenta bancaria, sesiones y tokens, tarifas y catálogos, mensajería, reseñas, detalle tributario y notificaciones | Diccionario ampliado sin afirmar cobertura total de los RF | P-01 | Anexo B |

## Advertencias registradas

- **P-11 es irreversible**: una vez bloqueada la retención no se puede reducir. No ejecutarlo antes de acordar el plazo con la política de conservación (D-08).
- **P-06 no sustituye el objetivo declarado**: si un percentil no alcanza el máximo especificado por el RNF, hay que justificar el cambio de criterio, no reinterpretar la medición.
- **P-10 no autoriza a declarar superioridad**: la valoración ponderada publicada es ilustrativa; el ensayo es lo que la sustituiría.
- Las mediciones de P-04 deben publicarse **con su registro vacío visible** mientras no existan, para no dar por medido lo que sigue sin medición.

## Orden recomendado

1. P-12 y P-01 (habilitan casi todo).
2. P-13 y P-02 (modelo de datos validado).
3. P-03 y P-04 (pruebas y medición).
4. P-05, P-06 y P-08 (operación y resiliencia).
5. P-09, P-07 y P-10.
6. P-11 y P-14 al final, cuando la política de conservación y el diccionario estén acordados.
