# INV-033 — Cierre documental del borrador con supuestos trazables

Fecha: 24-09-2026. Autor: Codex (asistente de IA), por delegación expresa del usuario. Alcance: aplicar INV-030 (auditoría de pendientes), INV-031 (fuentes para cerrar decisiones) e INV-032 (tecnologías e inventario) al cuerpo y a los anexos de ES2, **sin falsificar evidencia**. No se contactó a proveedores, no se implementó producto, no se ejecutó ningún ensayo de EspaciGo y no se aprobó el perfil Word.

## Qué se cerró y con qué sustento

Se cierran tres marcadores de borrador porque su contenido era una **decisión o una redacción alcanzable**, ya no una medición. En los tres casos la obligación empírica que quedaba se trasladó con nombre propio a `pendientes.md`; ninguna se declaró cumplida por haberla redactado.

| Archivo y tema | Tratamiento | Sustento documental | Obligación que se conserva |
| --- | --- | --- | --- |
| `secciones/02_01_analisis.md` — comparación cuantitativa y decisión técnica | **Cerrado.** Pesos definidos antes de puntuar, alternativas inventariadas, valoración por capa con escala 0–4 y decisión provisional de continuidad registrada | SUP-04 y SUP-19; fuentes primarias de INV-032 | Ensayos comparativos con entorno registrado y costo con SKU comparables en Santiago |
| `secciones/02_02_herramientas.md` — fichas de versiones, licencias, herramientas y alojamiento | **Cerrado.** Fichas objetivo con versión, licencia verificada, alojamiento y herramientas de desarrollo/prueba/integración | SUP-05 y SUP-20; INV-032 y licencias oficiales de cada proyecto | Inventario físico de estaciones, parche e imagen instalados, disponibilidad de PostGIS y acceso a proveedores |
| `secciones/03_00_arquitectura.md` — inmutabilidad de RNF-017 y acceso a proveedores | **Cerrado como decisión.** BigQuery solo analítica; garantía por retención bloqueada con hash por lote; el acceso a proveedores se separa como asunto de terceros | SUP-13; documentación de Bucket Lock y DML de BigQuery | Ensayo de alteración fallida, plazo productivo y respuestas de acceso de los proveedores |

Dos marcadores se **redujeron** en lugar de cerrarse, porque mezclaban trabajo ya hecho con trabajo empírico:

- `secciones/02_01_analisis.md` (factibilidad económica): el reparto del volumen por categoría ya está calculado y publicado, así que el marcador conserva solo la sustitución por **mediciones** de precio final, demanda, ocupación y conversión.
- `anexos/A_evaluacion_economica.md`: igual que el anterior, con la simulación segmentada sintética ya incorporada al anexo.

Los **14 marcadores restantes** no se tocan: dependen del equipo, de terceros o de producto desplegado. Ninguno se retira por corrección editorial.

## Qué permanece abierto, por origen

| Origen | Obligación | Por qué no se cierra |
| --- | --- | --- |
| Terceros | Tarifa e incidencia del Split, firma e identidad por documento, IVA y crédito fiscal de Google Cloud, giro/régimen/domicilio, patente, campo de demanda, destaque, Meta Ads y accesos de organismos | Requiere cotización, credencial, respuesta escrita o entrevista |
| Equipo | Capacidad semanal, responsables, alcance de la demostración, revisión de BPMN y vistas de casos de uso, interfaces, conciliación, inmutabilidad ensayada, aportes y metadatos académicos | Requiere acuerdo interno registrado |
| Producto | DDL aplicado y MD-01 a MD-12, PT-01 a PT-16, KPI y SLA medidos, respaldo y restauración, carga y escalado, portabilidad, monitoreo y procedimientos | Requiere entorno y producto con evidencia fechada |

## Cálculos nuevos y su reproducción

Se agregó un escenario **explícitamente sintético** para separar el efecto del ticket único del efecto del volumen. Conserva el volumen hipotético de 0, 720 y 1.800 reservas al año y lo reparte en cinco categorías, usando como arriendo unitario los precios de lista ya transcritos en INV-011: una hora de oficina (7.140 CLP), un bloque de dos horas de sala (42.245 CLP), un mes de minibodega (55.000 CLP), una hora de estacionamiento (2.940 CLP) y el bloque de cuatro días de stand (83.000 CLP).

| Indicador | Caso base, ticket único | Segmentado sintético |
| --- | ---: | ---: |
| Contribución del año 3 | 10.424.507 CLP | 350.688 CLP |
| VAN de caja a 36 meses | −1.791.437 CLP | −12.771.812 CLP |
| Déficit máximo en 36 meses | 6.246.529 CLP | 15.891.086 CLP |
| TIR de caja | −9,20 % | No definida |

Contribución del año 3 por categoría: oficina por hora −935.862; sala por dos horas +206.114; bodega mensual +621.038; estacionamiento por hora −1.072.489; stand por bloque +1.531.886 CLP. El signo reproduce la frontera de costo variable ya documentada: bajo 35.909 CLP de arriendo, una reserva no cubre pasarela, firmas, KYC y otros cargos.

```powershell
python Informes/herramientas/simular_bootstrap.py Informes/ES2PT/investigacion/supuestos_bootstrap.json --salida Informes/ES2PT/build/simulacion_bootstrap.json
python Informes/herramientas/simular_bootstrap.py Informes/ES2PT/investigacion/supuestos_segmentado.json --salida Informes/ES2PT/build/simulacion_segmentada.json
```

También se verificó la aritmética de la valoración ponderada de 2.1 contra la fórmula declarada `P = suma(peso × valoración / 4)`, renormalizada sobre el peso evaluado cuando una celda queda «NE». Los diez ponderados publicados se reprodujeron sin diferencias.

## Límites declarados

- El escenario segmentado es **sintético**: el reparto del volumen es una decisión del análisis, no una medición. El dato externo es el precio publicado de cada producto.
- Se aplica a cada categoría el mismo cargo variable por reserva del caso base; una reserva por hora y una bodega mensual no tienen por qué compartir firma, KYC ni garantía.
- Ninguna valoración usa el nivel 4 de la escala, reservado a la verificación; «NE» no equivale a cero.
- Las licencias se verificaron contra la documentación oficial del proyecto correspondiente; la de Node.js cubre además bibliotecas de terceros con licencias propias.
- No se modificó ES1. Por autorización expresa del usuario posterior a este cierre, sí se aprobó el perfil, se regeneró el Word y se revisó el render el 24-09-2026 (INV-020, § Revisión del 24-09-2026), corrigiendo un defecto de maquetación en la tabla de 2.1. `validar --final` sigue devolviendo error por marcadores y tareas abiertas, que es el resultado esperado mientras falte evidencia externa.
