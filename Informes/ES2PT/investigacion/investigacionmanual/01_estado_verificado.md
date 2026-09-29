# 01. Estado verificado: lo que ya está decidido y documentado

Sirve para **no volver a decidir** lo que ya está resuelto ni re-investigar lo que ya tiene fuente primaria. Si el equipo quiere cambiar algo de la primera tabla, hay que registrar la decisión nueva y actualizar las secciones que dependan de ella.

## A. Decisiones ya tomadas y aplicadas

| Decisión | Quién la tomó | Dónde está aplicada |
| --- | --- | --- |
| Región de operación **Santiago (`southamerica-west1`)** | Usuario, 23-09-2026 | 2.1, 2.2, 3.6, Anexo A |
| **Todas** las categorías de arriendo siguen en el alcance; ninguna se elimina | Equipo | 2.1, Anexo A, INV-011 |
| Orden de anexos **A = evaluación económica, B = diccionario de datos, C = casos de prueba** | Equipo, 24-09-2026 | `informe.json`, todo el cuerpo |
| Propuesta de inicio **631200 principal + 731001 complementaria**; 682000 queda solo como consulta por la comisión | Equipo | 2.1, Anexo A, INV-029 |
| Domicilio simulado **Oficina Express, Ahumada 131**: 50.000 CLP/año + 5.000 CLP por firma, IVA incluido; **una** patente para la SpA | Equipo | Anexo A, INV-029 |
| **Ley 21.719 como criterio de diseño** desde el primer incremento (vigencia legal 01-12-2026) | Usuario | Anexo B, PT-16, 5.2 |
| **Mecanismo de inmutabilidad de RNF-017**: Cloud Storage con retención bloqueada + hash por lote; BigQuery solo analítica | Propuesta del agente (SUP-13) | 3.0, 3.3, 3.6 |
| **Arquitectura de diseño**: Next.js, monolito Go con workers internos, PostgreSQL 18/PostGIS 3.6, contenedores y Cloud Run en Santiago | Decisión del proyecto; despliegue pendiente | 2.1, 2.2, 3.0, 3.6, Anexos A/B |
| **Comisión propia de 3 % neto**, más IVA de la comisión si corresponde; Split 1:1 vendedor/marketplace y reparto societario fuera del checkout | Usuario, 29-09-2026 | 2.1, Anexos A/B, propuesta backend |
| **Destaques pagados fuera** de la demostración ES2 y con cero ingresos en el flujo | Propuesta del agente (SUP-10) | 2.1, 3.3, Anexo A |
| **Perfil Word aprobado** y render revisado (91 páginas + anexos A/B/C) | Usuario, 24-09-2026 | `plantilla/perfil_es2.json`, INV-020 |

## B. Verificado con fuente primaria (no requiere nueva investigación)

Estos datos ya están contrastados contra documentación oficial o precios publicados. Lo que falta en varios casos **no** es la fuente, sino la condición particular del proyecto (cuenta, contrato o habilitación).

| Dato verificado | Fuente | Lo que **no** acredita |
| --- | --- | --- |
| Split 1:1 de Mercado Pago **disponible en Chile** para Checkout Pro o API, con KYC 6, OAuth por arrendador y cuentas de prueba de vendedor, comprador e integrador | Documentación oficial del proveedor (INV-026) | Que **nuestra** cuenta de empresa esté habilitada ni el medio de pago admitido bajo «dinero en cuenta» |
| La comisión de Mercado Pago se descuenta **primero al vendedor**; el reembolso completo depende del saldo del vendedor; el reporte separa tarifa del marketplace, tarifa del proveedor y neto | Documentación oficial (INV-026) | La **tarifa contractual** de Split para este proyecto |
| Una política de **Bucket Lock** impide reducir o quitar la retención y borrar o reemplazar objetos antes del plazo; el bloqueo es **irreversible** | Google Cloud (INV-031) | El plazo de retención productivo, que depende de la matriz de tratamiento |
| Licencias: Next.js **MIT**, Go **BSD de 3 cláusulas**, PostgreSQL **licencia PostgreSQL**, PostGIS **GPLv2** para la extensión, Node.js licencia del proyecto con bibliotecas de terceros; Docker sin gratuidad contractual confirmada para tres integrantes | Documentación oficial de cada proyecto (INV-032) | Los parches e imágenes efectivamente instalados |
| El comparador público original estimó **USD 237,82/mes** para un piloto anterior; el escenario actualizado del Anexo A estima **USD 307,724/mes** con una instancia mínima de Cloud Run y supuestos explícitos | Calculador público original (INV-021) y modelo académico actualizado | Cotización, factura, elegibilidad de descuentos ni precio contractual de cada SKU |
| Precios de **lista** por categoría (oficina 7.140/h, sala 42.245 por 2 h, minibodega 55.000/mes, estacionamiento 2.940/h, stand 83.000 por 4 días) | Avisos publicados (INV-011) | Demanda, ocupación, conversión ni aceptación de la comisión |
| La rúbrica incorporada suma 60 puntos con 17 criterios; la guía omite el criterio 2.1.5.15 | Instrumentos del curso (INV-025) | El código de asignatura (TIH184 vs TIHI84) |

## C. Supuestos de trabajo que el equipo debe ratificar o cambiar

Todos están en [`supuestos_revision.md`](../../supuestos_revision.md) con su motivo y con qué los sustituiría. **Ninguno acredita una respuesta externa.**

| ID | Qué propone | Afecta a |
| --- | --- | --- |
| SUP-01 | Diseño del producto completo con todas las categorías; evidencia ejecutable por incrementos y pagos de desarrollo en sandbox, sin presumir dinero real | II, III, V, VII |
| SUP-02 | Capacidad académica ilustrativa: 3 integrantes × 12 h/semana × 6 semanas = 216 h, con 20 % de reserva | VII |
| SUP-03 | Reparto sugerido por frente: backend/datos/integración, interfaz/pruebas/privacidad, infraestructura/operaciones/presupuesto | IV–VII |
| SUP-04 y SUP-19 | Continuidad tecnológica y valoración ponderada por capa (escala 0–4, con «NE» donde no hay ensayo) | 2.1 |
| SUP-05 y SUP-20 | Familias y versiones objetivo, licencias y hardware supuesto (3 estaciones de 4 núcleos, 16 GB, SSD 512 GB) | 2.2 |
| SUP-06, SUP-07 y SUP-08 | Mercado Pago Split 1:1 sujeto a habilitación; tarifa referencial de pasarela a cargo del vendedor en el escenario base; FirmaVirtual con firma e identidad simuladas hasta integrar | 2.2, 3.1, 3.3, 3.5, Anexos A/B |
| SUP-09 y SUP-21 | Caso base de lectura (ticket 100.000 CLP; reservas 0/720/1.800) y escenario segmentado **sintético** por categoría | 2.1, Anexo A |
| SUP-10 | Destaques incluidos como capacidad del producto completo, con cero ingresos en la simulación; Meta Ads solo con la provisión de 357.000 CLP | 2.1, 3.3 |
| SUP-11 y SUP-12 | Giro, domicilio, patente, tasas académicas y financiamiento ilustrativo del primer año (**5.314.863 CLP**; con 20 % de holgura, **6.377.835 CLP**, aproximadamente **2.125.945 CLP** por fundador) | Anexo A |
| SUP-13 | Inmutabilidad de RNF-017 por retención bloqueada y hash por lote, con ensayo de 7 días | 3.0, 3.3, Anexo B |
| SUP-14 y SUP-15 | Conciliación periódica dentro del monolito Go con persistencia y coordinación en PostgreSQL; instancia mínima presupuestada en Cloud Run; Cloud SQL/PostGIS, Cloud Storage y Secret Manager | 3.3, 3.5, 3.6, Anexo A |
| SUP-16 | SLA internos, zona America/Santiago, mantención contada como indisponibilidad mientras no haya acuerdo de exclusión | IV–VI |
| SUP-17 | Mantener las siete vistas de casos de uso y las justificaciones de CU-14/31/47/51 | III |
| SUP-18 | Mantener los metadatos actuales y omitir el código de asignatura en portada hasta verificarlo | VII |

## D. Qué NO hay que rehacer

- El perfil Word y una versión anterior ya fueron revisados; la actualización de contenido del 29-09-2026 queda pendiente de render y cierre visual cuando termine la redacción.
- El orden de los anexos y sus letras ya están corregidos y verificados.
- Los precios publicados, las licencias y las capacidades documentadas **no** necesitan otra búsqueda: lo que falta es la confirmación particular (contrato, cuenta, factura o medición).
- ES1 está congelado: no se toca ni se regenera.
