## H.17. servicio respaldo

Fila 1. 1. Parámetros (Base del cálculo)

Fila 3. Esta es la tabla inferior de tu imagen, adaptada a las reservas de EspaciGo.

**Tabla H.17.1**
*servicio respaldo — filas 5 a 12*

| Fila Excel | A | B |
|---|---|---|
| 5 | Parámetros | Valores |
| 6 | Peso Promedio por Reserva (Fotos Check-in/out + Contrato) en GB | 0,05 GB (aprox 50 MB) |
| 7 | Cantidad de Reservas Anuales Base | 3.600 |
| 8 | Cantidad Reservas Periodo 1 (Año 1) | 3.600 |
| 9 | Cantidad Reservas Periodo 2 (Crecimiento 20%) | 4.320 |
| 10 | Cantidad Reservas Periodo 3 (Crecimiento 20%) | 5.184 |
| 11 | Cantidad Reservas Periodo 4 (Crecimiento 20%) | 6.220 |
| 12 | Base de Datos Operativa (PostgreSQL + Logs) por periodo | ~10 GB fijos |

*Nota.* Transcripción de la hoja «servicio respaldo» de EspaciGo.xlsx, filas 5–12. Se conservan los importes y el alcance del insumo.

Fila 14. 2. Tramos de Almacenamiento y Consumo

Fila 16. Esta es la tabla central de tu imagen. Cruzamos el consumo de GB acumulados con los planes de respaldo (ej. precios de tramos de Google Cloud Storage o Google Workspace).

**Tabla H.17.2**
*servicio respaldo — filas 18 a 22*

| Fila Excel | A | B | D | E |
|---|---|---|---|---|
| 18 | Cantidad Espacio | Valor Respaldo Anual (Base) | Periodos | GB Evidencias + Datos Acumulados |
| 19 | 100GB | 50.000 | Periodo 1 (Servicio 250GB) | 190 GB (180GB reservas + 10GB BD) |
| 20 | 250GB | 80.000 | Periodo 2 (Servicio 500GB) | 416 GB (190 + 216GB res. + 10GB BD) |
| 21 | 500GB | 120.000 | Periodo 3 (Servicio 1000GB) | 685 GB (416 + 259GB res. + 10GB BD) |
| 22 | 1000GB | 190.000 | Periodo 4 (Servicio 1000GB) | 996 GB (685 + 311GB res. + 10GB BD) |

*Nota.* Transcripción de la hoja «servicio respaldo» de EspaciGo.xlsx, filas 18–22. Se conservan los importes y el alcance del insumo.

Fila 24. 3. Servicio de respaldo en la nube (Flujo ajustado)

Fila 26. Esta es la tabla superior de tu imagen. Muestra el costo que irá a tu Flujo de Caja. Toma el plan que necesitas según los GB de arriba, y le aplica el 4% de inflación anual desde el Periodo 2 en adelante.

**Tabla H.17.3**
*servicio respaldo — filas 28 a 30*

| Fila Excel | A | B | C | D | E |
|---|---|---|---|---|---|
| 28 | Detalle | Periodo 1 | Periodo 2 | Periodo 3 | Periodo 4 |
| 29 | Servicio de Respaldo GCP | 80.000 | 124.800 | 205.504 | 213.724 |
| 30 | Total | 80.000 | 124.800 | 205.504 | 213.724 |

*Nota.* Transcripción de la hoja «servicio respaldo» de EspaciGo.xlsx, filas 28–30. Se conservan los importes y el alcance del insumo.

Fila 32. ¿Por qué aumentan los GB? A diferencia de un negocio tradicional, la plataforma por ley (Ley 21.719) y por operatividad debe guardar el historial inmutable (BigQuery), los contratos firmados y las fotos de daños de cada reserva por 5 años. Por ende, el almacenamiento se acumula año a año.

Fila 34. ¿Cómo se calcula el valor del periodo? En el Periodo 1 necesitas el tramo de 250GB ($80.000). En el Periodo 2 saltas al tramo de 500GB ($120.000), pero como es el año 2, se le aplica el 4% de inflación ($120.000 * 1.04 = $124.800). En el Periodo 3 saltas a 1000GB ($190.000) aplicando dos años de inflación ($190.000 * 1.04^2 = $205.504).
