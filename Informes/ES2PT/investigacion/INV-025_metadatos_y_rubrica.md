# INV-025 — Metadatos académicos y contraste entre la guía y la rúbrica

- Estado: contraste documental entre los instrumentos incorporados; la confirmación con el instrumento oficial sigue pendiente.
- Fecha de consulta: 2026-09-23.
- Secciones ES2 relacionadas: portada y metadatos de `informe.json`; cobertura de la rúbrica en `plan_de_trabajo.md` y la matriz de trazabilidad.
- Referencia de línea base: entrega cerrada de ES1, que conserva el código que usó, y `plantilla/` de ES2.

## Pregunta

¿Qué metadatos académicos están confirmados, cuáles difieren entre las fuentes y en qué se aparta la tabla resumida de la guía de los criterios de la rúbrica incorporada?

## Fuentes y evidencias

| Fuente | Dato verificable | Límite |
| --- | --- | --- |
| `informe.json` de ES2 | Título, proyecto, institución, sección, académico, tres integrantes y fecha 3 de noviembre de 2026; la asignatura lleva un marcador pendiente por el código | Es configuración de la entrega, no un documento institucional |
| [Guía de recomendaciones](../plantilla/guia_recomendaciones_ES2.md) | Área Tecnología, Información y Ciberseguridad; carrera Ingeniería en Informática; asignatura Proyecto de Título; **código TIHI84**; duración 9 semanas; fecha según calendario oficial; entrega en plataforma hasta las 23:00 del día agendado | Es una transcripción del DOCX; los descriptores de nivel pertenecen al instrumento EA4 original, que no está incorporado |
| Guía, sección de equipos y evaluación | Equipos de tres integrantes con rotación de jefatura; desarrollo entre las semanas 6 y 14, demo formativa en la 12, retroalimentación en la 13 e informe sumativo en la 14 con ponderación de 25 %; el estándar mínimo es la escala EA4 y existe un preinforme EF2 con escala EA3 | No hay calendario con fechas, así que las semanas no se convierten a días |
| [Rúbrica incorporada](../plantilla/rubrica_de_calificacion.md) | **17 criterios y 60 puntos**, cuya suma es exacta | Transcripción; no incluye los descriptores de los niveles |
| ES1 cerrada | La entrega anterior usa el código **TIH184** | Se conserva; no se reescribe para cuadrar con ES2 |

## Estado de los metadatos

| Campo | Valor en la entrega | Coincidencia | Qué falta |
| --- | --- | --- | --- |
| Título | Desarrollo del Proyecto de Título: EspaciGo | Coherente con la plantilla | — |
| Proyecto | EspaciGo | Coherente | — |
| Institución | Inacap - Informática y Telecomunicaciones | La guía nombra el área «Tecnología, Información y Ciberseguridad» y la carrera «Ingeniería en Informática» | Revisar la denominación de portada: no coincide literalmente |
| Asignatura y código | Proyecto de Título, sin código en la portada; el marcador pendiente se retiró al cerrar el Word (INV-020) | **Discrepancia abierta**: ES1 usa TIH184 y la guía transcrita dice TIHI84 | Confirmar con el instrumento oficial o el docente antes de la entrega |
| Sección | D-IEI-N8-P1-C2/D | Proviene de la entrega anterior | Sin verificación |
| Académico | Teresa Jesús Tapia Soto | Proviene de la entrega anterior | Sin verificación |
| Integrantes | Hernán Espinoza, Anita Marchant y Erick Silva | Tres integrantes, como indica la guía | La rotación de jefatura no está registrada |
| Fecha | 3 de noviembre de 2026 | La fecha fue informada por el usuario; la guía solo dice «según calendario oficial» | Contraste con el calendario académico |
| Formato de entrega | No registrado | La guía exige subir a la plataforma hasta las 23:00 del día agendado y no acepta entregas por correo | Registrar la constancia al entregar |

## Contraste entre la tabla de la guía y la rúbrica

*Tabla. Ponderaciones de la guía frente a los puntos de la rúbrica.*

| Criterio | Guía (ponderación) | Rúbrica (puntos) | Rúbrica (% de 60) | Coincidencia |
| --- | ---: | ---: | ---: | --- |
| 2.1.1.1 Análisis comparativo de tecnologías y metodologías | 5 | 3,0 | 5,0 % | Coincide |
| 2.1.1.2 Herramientas, lenguajes, hardware y servicios TI | 4 | 2,4 | 4,0 % | Coincide |
| 2.1.2.3 BPMN de tres procesos con subprocesos | 8 | 4,8 | 8,0 % | Coincide |
| 2.1.2.4 UML de casos de uso y componentes | 5 | 3,0 | 5,0 % | Coincide |
| 2.1.2.5 Modelo de datos y diccionario | 8 | 4,8 | 8,0 % | Coincide |
| 2.1.2.6 Topología de comunicaciones | 5 | 3,0 | 5,0 % | Coincide |
| 2.1.2.7 Diseño de infraestructura | 5 | 3,0 | 5,0 % | Coincide |
| 2.1.2.8 Arquitectura con software y hardware | 5 | 3,0 | 5,0 % | Coincide |
| 2.1.3.9 KPI con detalle SMART | 8 | 4,8 | 8,0 % | Coincide |
| 2.1.3.10 SLA y resultados esperados | 8 | 4,8 | 8,0 % | Coincide |
| 2.1.4.11 Plan de pruebas | 8 | 4,8 | 8,0 % | Coincide |
| 2.1.4.12 Normas y estándares justificados | 6 | 3,6 | 6,0 % | Coincide |
| 2.1.5.13 Disponibilidad de servicios TI | 6 | 3,6 | 6,0 % | Coincide |
| 2.1.5.14 Continuidad proactiva y reactiva | 6 | 3,6 | 6,0 % | Coincide |
| 2.1.5.15 Control de cambios, entregables e incidentes | **No aparece** | 3,0 | 5,0 % | **La guía lo omite** |
| 2.1.6.16 Carta Gantt o fases | 5 | 2,4 | 4,0 % | **Difiere en un punto** |
| 2.1.6.17 Justificación del cronograma | 4 | 2,4 | 4,0 % | Coincide |
| **Total** | **96 declarado como 100** | **60** | **100 %** | La rúbrica suma exacto |

Hallazgos verificados al sumar las filas de cada instrumento:

1. La tabla de la guía tiene **16 filas** y omite el criterio **2.1.5.15**, que la rúbrica sí incluye.
2. La suma de esas 16 filas es **96**, aunque la propia tabla declara un total de 100 %.
3. La diferencia se explica exactamente: **+5** por el criterio omitido y **+1** de más en 2.1.6.16, que la guía pondera 5 y la rúbrica asigna 4,0 %.
4. La rúbrica suma 60 puntos sin desajustes y cubre los 17 criterios.
5. En el resto de los criterios ambas escalas coinciden en su peso relativo.

## Impacto y decisión

La entrega se planifica con los **17 criterios** de la rúbrica y no prioriza por las ponderaciones de la guía, porque su tabla no cuadra consigo misma y omite un criterio. Las secciones se mantienen completas para todos los criterios, con independencia del peso. También se registra que la guía pondera la entrega sumativa en **25 %** de la asignatura y que el estándar mínimo de evaluación es la escala **EA4**, cuyo original no está incorporado.

No se corrige `informe.json` por inferencia: el código, la sección, el académico y las fechas solo se cierran con evidencia institucional. Tampoco se aprueba el perfil institucional a partir de este contraste, que es de contenido y no de formato.

## Pendientes

[[PENDIENTE: confirmar con el instrumento oficial EA4 y con el calendario académico el código de asignatura, las fechas de las semanas 12 a 14 y los descriptores de nivel; validar la denominación de institución y carrera, la sección, el académico y la rotación de jefatura; registrar la constancia de entrega. No completar estos campos por inferencia.]]
