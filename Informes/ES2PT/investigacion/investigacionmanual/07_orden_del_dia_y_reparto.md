# 07. Orden del día de la reunión y reparto del trabajo

Objetivo de la reunión: **decidir lo que solo el equipo puede decidir** y **repartir lo que falta**. Duración sugerida: 90 minutos. Al terminar, esta carpeta debe quedar con responsables y fechas escritos.

## Orden del día

### Bloque 1 — Puesta al día (10 min)

- Estado del informe: contenido redactado de punta a punta; Word generado y revisado (91 páginas + anexos A/B/C); `validar` en 0 errores y `validar --final` en 1 por los 14 marcadores.
- Lo que ya está resuelto y **no se vuelve a discutir**: ver [`01_estado_verificado.md`](01_estado_verificado.md), sección A.
- Acordar que **nadie borra un marcador** sin evidencia registrada.

### Bloque 2 — Decisiones de alto impacto (35 min)

Resolver en este orden, porque desbloquean lo demás:

| Decisión | Pregunta concreta para la reunión | Acuerdo |
| --- | --- | --- |
| **D-01** | ¿Cuántas horas por semana y quién responde por cada bloque? | |
| **D-02** | ¿Qué exactamente existirá el 3 de noviembre y qué queda fuera? | |
| **D-11** | ¿TIH184 o TIHI84? ¿Sección, académico y fechas correctos? | |
| **D-08** | ¿Qué plazos de conservación y qué regla de anonimización adoptamos? | |
| **D-07** | ¿Ratificamos la retención bloqueada y con qué plazo? (es irreversible) | |

### Bloque 3 — Decisiones de alcance medio (25 min)

| Decisión | Pregunta concreta | Acuerdo |
| --- | --- | --- |
| **D-13** | ¿Ratificamos la continuidad tecnológica y aceptamos la valoración como ilustrativa? | |
| **D-04** | ¿Las siete vistas y los cuatro CU sin vista propia quedan así? | |
| **D-03** | ¿Los cuatro BPMN y los temporizadores están correctos? | |
| **D-14** | ¿El destaque pagado entra en ES2 o queda para una fase posterior? | |
| **D-06** | ¿Dominio propio o nombre de prueba? ¿Quién administra los secretos? | |
| **D-15** | ¿Contamos la mantención como indisponibilidad y fijamos America/Santiago? | |

### Bloque 4 — Reparto del trabajo (20 min)

Llenar la tabla siguiente. Reglas: **una sola persona responsable por fila**; cada fila con fecha objetivo; si depende de un tercero, indicar quién cursa la consulta.

## Tabla de reparto

Sugerencia de frente por integrante según SUP-03 (backend/datos/integración; interfaz/pruebas/privacidad; infraestructura/operaciones/presupuesto). Es un punto de partida, no una asignación decidida: ajustar según competencias y disponibilidad reales.

### Decisiones y documentación

| Tarea | Qué hay que hacer | Responsable | Fecha objetivo |
| --- | --- | --- | --- |
| D-01 | Acordar horas, responsables y jefatura; registrarlo | | |
| D-02 | Escribir el alcance de la demostración | | |
| D-11 | Confirmar metadatos con el instrumento oficial | | |
| D-08 | Redactar la regla de conservación y anonimización | | |
| D-07 | Ratificar mecanismo y plazo de retención | | |
| D-13 | Acta de ratificación técnica | | |
| D-04 | Acta de revisión de las vistas de casos de uso | | |
| D-03 | Acta de revisión de los BPMN | | |
| D-14 | Decidir el destaque y dejarlo escrito | | |
| D-06 | Definir dominio, red y secretos | | |
| D-15 | Fijar zona horaria y ventana de mantención | | |
| D-05 | Validar interfaces y conciliación | | |

### Consultas a terceros

| Tarea | Qué hay que hacer | Quién la cursa | Fecha de envío | Fecha de respuesta esperada |
| --- | --- | --- | --- | --- |
| T-1 | Enviar las diez preguntas a Mercado Pago | | | |
| T-2 | Cotizar firma electrónica e identidad | | | |
| T-3 | Consultar al contador: IVA, crédito, giro, régimen, DTE y capital | | | |
| T-4 | Pedir contrato a Oficina Express y consultar al municipio: patente, DOM y aseo | | | |
| T-5 | Preparar y ejecutar el trabajo de campo por categoría | | | |
| T-6 | Ejecutar la campaña de Meta Ads y medir | | | |
| T-7 | Solicitar accesos a Registro Civil, SII y pasarelas | | | |

### Trabajo de producto

| Tarea | Qué hay que hacer | Responsable | Depende de | Fecha objetivo |
| --- | --- | --- | --- | --- |
| P-01 | Aplicar el DDL en ensayo | | T-3 (entorno) | |
| P-02 | Ejecutar MD-01 a MD-12 | | P-01 | |
| P-03 | Ejecutar PT-01 a PT-16 | | P-01 | |
| P-04 | Medir KPI y SLA | | P-01 | |
| P-05 | Ensayar respaldo y restauración | | P-01, D-15 | |
| P-06 | Probar carga y escalado | | entorno de carga | |
| P-07 | Demostrar portabilidad RNF-034–036 | | P-01 | |
| P-08 | Desplegar monitoreo y alertas | | D-15 | |
| P-09 | Procedimientos de continuidad, cambios e incidentes | | P-08 | |
| P-10 | Ensayos comparativos de tecnologías | | D-13 | |
| P-11 | Ensayo de alteración de RNF-017 | | D-07 | |
| P-12 | Inventario físico de estaciones | | — | |
| P-13 | Mapear literales de estado de ES1 | | D-04 | |
| P-14 | Completar entidades del diccionario | | P-01 | |

### Economía

| Tarea | Qué hay que hacer | Responsable | Depende de | Fecha objetivo |
| --- | --- | --- | --- | --- |
| E-01 a E-03 | Precio final por categoría, volumen y participación | | T-5 | |
| E-04 | Comisión aceptada por arrendadores | | T-5 | |
| E-05, E-06 | Tarifa e incidencia del split | | T-1 | |
| E-07, E-08 | Firma e identidad por unidad | | T-2 | |
| E-10 a E-14 | IVA, crédito, IPC, impuesto e PPM | | T-3 | |
| E-15 a E-18 | Tasa, colchón, capital y aportes | | D-09 | |
| E-19 | Costo por publicación y por reserva | | T-6 | |
| E-20 a E-23 | Aseo, patente, oficina y honorarios | | T-4 | |
| E-24 a E-26 | Valor hora, horas y costo de oportunidad | | D-01 | |

## Cierre de la reunión (5 min)

- Leer en voz alta **quién quedó con qué** y la primera fecha de cada responsable.
- Acordar la fecha de la siguiente reunión de control.
- Si una decisión no se tomó, no dejarla implícita: escribirla en esta carpeta como abierta.

## Después de la reunión

1. Registrar cada decisión en `../../contexto.md` con fecha y responsable.
2. Actualizar los supuestos que cambien en `../../supuestos_revision.md`.
3. Corregir las secciones afectadas y retirar los marcadores que correspondan (ver [`06_mapa_de_marcadores.md`](06_mapa_de_marcadores.md)).
4. Regenerar y validar el Word:

```powershell
$env:PLANTUML_JAR="$env:TEMP\plantuml.jar"
python Informes/generar.py generar ES2PT
python Informes/generar.py actualizar-word ES2PT
python Informes/generar.py validar ES2PT
```

5. Actualizar [`pendientes.md`](../../pendientes.md) y esta carpeta para que reflejen el estado real.
