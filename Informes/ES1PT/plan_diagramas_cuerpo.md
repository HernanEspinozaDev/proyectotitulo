# Plan A — Diagramas e imágenes del cuerpo del informe (PlantUML)

> Estado: **propuesta pendiente de aprobación**. No se ha modificado ningún archivo del informe todavía.
> Plan complementario: `plan_citas_word.md` (citas y referencias nativas de Word).

---

## A.0 Estado actual verificado (19-09-2026)

| Elemento | Estado |
| :--- | :--- |
| Figuras en el cuerpo | **12** (`figura-actores.png` + `figura-m01.png` … `figura-m11.png`) |
| Origen de esos diagramas | Bloques ```` ```plantuml ```` dentro de `docx/anexos/D_casos_de_uso.md`, extraídos por `_bloques_puml()` / `extraer_puml()` |
| Render | `java -Djava.awt.headless=true -jar %TEMP%\plantuml.jar -tpng -o imagenes -charset UTF-8` → PNG en `docx/imagenes/` |
| Declaración en el markdown | `![Texto alternativo](imagenes/figura-clave.png) <!--#fig:clave-->` |
| Numeración | `paso_preprocesar()` renumera correlativamente en orden de aparición ("Figura N.") y resuelve `{{Figura:clave}}`. Hoy hay **3** referencias cruzadas, todas de tabla (`{{Tabla:…}}`); **ninguna** de figura |
| Imágenes en tablas | No existen imágenes dentro de tablas; las 12 figuras son bloques sueltos |
| Anexos | Cada anexo numera sus figuras por separado (`Figura D.n`) → **no se ven afectados** por este plan |
| Índice | El TOC de la plantilla es por estilo (Título1/Subtitulo1/Subtitulo2). Las figuras **no** aparecen en el índice y no se requiere índice de figuras |

**Conclusión:** el pipeline ya soporta figuras en el cuerpo; falta (a) un espacio de trabajo para los `.puml` del cuerpo, (b) el control de ancho de las imágenes y (c) los diagramas nuevos.

---

## A.1 Objetivo

Incorporar al cuerpo del informe los diagramas que faltan —en particular el **lienzo canvas** (capítulo de Objetivos), el **diagrama de contexto de arquitectura** y la **topología del sistema** (capítulo de Definición de arquitectura TI), la **estructura organizacional como imagen** y los diagramas del **Marco Teórico**— sin alterar la numeración institucional, los estilos, la portada ni los anexos.

---

## A.2 Inventario de diagramas propuestos

**MUST = pedido explícito o ausencia evidente · SHOULD = recomendado · OPT = opcional**

| # | Capítulo / sección del cuerpo | Clave (archivo `.puml` → `.png`) | Tipo PlantUML | Qué representa | Prio |
| :--- | :--- | :--- | :--- | :--- | :--- |
| A-01 | **5. Objetivos del Proyecto → 5.1 Formulación de la solución** | `canvas` | `@startuml` con `rectangle` anidados (lienzo de 9 bloques) | **Lienzo canvas (Business Model Canvas)**: socios clave, actividades y recursos clave, propuesta de valor, relación con clientes, canales, segmentos, estructura de costos y fuentes de ingreso de EspaciGo | **MUST** |
| A-02 | **7. Definición de arquitectura TI → 7.1** | `arq-contexto` | `@startuml` (notación C4 nivel 1, elementos nativos) | **Diagrama de contexto**: EspaciGo como caja central, actores humanos (visitante, arrendador, arrendatario, administrador) y sistemas externos (Registro Civil, SII, Mercado Pago, FirmaVirtual, Cloud Storage, BigQuery) con la naturaleza de cada integración | **MUST** |
| A-03 | **7. Definición de arquitectura TI → 7.1** | `arq-topologia` | `@startuml` de despliegue (`node`, `cloud`, `database`, `component`) | **Topología del sistema**: navegador → CDN/balanceo → Cloud Run (contenedor Next.js SSR + contenedor API Go) → PostgreSQL/PostGIS + Cloud Storage → BigQuery; pipeline CI/CD (repositorio → build → Artifact Registry → Cloud Run); conexiones salientes a las API externas | **MUST** |
| A-04 | **8. Reconocimiento de arquitectura empresarial → 8.1** | `ae-organigrama` | `@startwbs` | **Estructura organizacional** (organigrama funcional de tres roles + docencia), **reemplaza el bloque ASCII** ```text``` actual | **MUST** |
| A-05 | **4. Marco Teórico → 4.1 Plataforma digital y modelo SaaS** | `s4-saas` | `@startuml` con `group`/`rectangle` | SaaS multiinquilino vs. On-Premise: quién administra infraestructura, mantenimiento y actualizaciones | **MUST** |
| A-06 | **4.2 Marketplace y modelo B2B2C** | `s4-marketplace` | `@startuml` | Plataforma de dos lados: oferta (arrendadores) ↔ demanda (arrendatarios) ↔ plataforma, con los flujos de confianza (identidad, escrow, reputación) | **MUST** |
| A-07 | **4.3 Modelos de negocio y monetización** | `s4-monetizacion` | `@startuml` de secuencia | Flujo del modelo de **comisión transaccional**: cobro al arrendatario → retención → split → payout al arrendador → boleta de comisión | **MUST** |
| A-08 | **4.4 Cloud Computing, arquitectura web y APIs** | `s4-capas-arquitectura` | `@startuml` con `package`/`rectangle` | Vista de **capas de la arquitectura modular** cloud-native (presentación, negocio, datos, integración, infraestructura) y su empaquetado en contenedores | **MUST** |
| A-09 | **4.5 Gestión de espacios, disponibilidad y doble reserva** | `s4-doble-reserva` | `@startuml` de secuencia | **Condición de carrera** de la doble reserva (dos arrendatarios concurrentes) y el control transaccional que la evita | **MUST** |
| A-10 | **4.6 Pagos, retención de fondos y escrow** | `s4-escrow` | `@startuml` de secuencia | Ciclo del **Escrow**: pago tokenizado → retención → pre-autorización de garantía → liberación al cierre | **MUST** |
| A-11 | **4.7 KYC, KYB, identidad digital y autenticación** | `s4-kyc-estados` | `@startuml` de estados | **Máquina de estados** de la verificación: No Verificada → Pendiente → Verificada_KYC/Verificado_KYB → Rechazada (con reintento) | **MUST** |
| A-12 | **4.8 Seguridad, privacidad y protección de datos** | `s4-seguridad-capas` | `@startuml` con `group` | **Seguridad por capas** (borde, aplicación, datos, auditoría) y privacidad por diseño a lo largo del ciclo de vida del dato | **MUST** |
| A-13 | **4.9 Contratos digitales, firma electrónica y gestión documental** | `s4-contrato-firma` | `@startuml` de secuencia | Generación del contrato → envío a firma electrónica avanzada → confirmación de firmas → resguardo del documento | **MUST** |
| A-14 | **4.10 Auditoría, trazabilidad y resolución de disputas** | `s4-auditoria` | `@startuml` de componentes/flujo | Flujo de **eventos de auditoría** desde el backend hacia el repositorio inmutable y su consulta en disputas | **MUST** |
| A-15 | **4.11 Arquitectura de software y metodologías** | `s4-estilos-arquitectura` | `@startuml` con `rectangle` | Comparación visual monolito / modular / microservicios con la marca de la opción adoptada (complementa la tabla existente) | **MUST** |
| A-16 | **2.2 Diagnóstico de la situación actual** | `problema-causas` | `@startmindmap` | **Árbol de causas** de la vacancia y de la exclusión de las pymes (causas raíz → efectos) | SHOULD |
| A-17 | **2.2 Diagnóstico de la situación actual** | `problema-magnitud` | `@startuml` (barras con rectángulos) | Magnitud del problema por segmento (oficinas clase C 14–18%, bodegas flex 14,5%, locales >15%), con nota de fuente pendiente | SHOULD |
| A-18 | **3.2 Detalle de los requerimientos** | `req-artefactos` | `@startuml` / `@startwbs` | **Trazabilidad de los cuatro artefactos**: HU → RF → RNF → CU → módulo → componente | SHOULD |
| A-19 | **5.2 Proceso de negocio afectado** | `proceso-negocio` | `@startuml` de actividad con `\|swimlane\|` | Los **seis procesos** rediseñados, con carriles de arrendador, arrendatario, plataforma y terceros | SHOULD |
| A-20 | **5.3 Objetivos del proyecto** | `objetivos-arbol` | `@startmindmap` | **Árbol de objetivos**: objetivo general → objetivos específicos → resultados verificables | SHOULD |
| A-21 | **6.2 Duración y cronograma** | `cronograma-gantt` | `@startgantt` | **Carta Gantt** de las 16 semanas y los 6 incrementos (el propio PlantUML genera el Gantt) | SHOULD |
| A-22 | **8.2 Dominios de la Arquitectura Empresarial** | `ae-dominios` | `@startuml` con `package` | Los **cuatro dominios** (negocio, aplicaciones, datos, tecnología) y sus relaciones | OPT |
| A-23 | **6.1 Metodología de desarrollo** | `ciclo-incremental` | `@startuml` de estados | **Ciclo iterativo-incremental**: iteración → incremento verificable → cierre de etapa | OPT |
| A-24 | **1. Introducción** | `mapa-documento` | `@startwbs` | **Mapa del documento**: capítulos y su relación con los objetivos y los artefactos | OPT |

**Totales si se aprueba todo:** 24 diagramas nuevos → 36 figuras en el cuerpo (las 11 de casos de uso siguen en el anexo D y también en el cuerpo).

---

## A.3 Decisiones de diseño (para evitar riesgos visuales)

1. **Sin dependencias externas.** No se usa la librería C4-PlantUML (requiere descargar `C4_Container.puml` desde Internet). El diagrama de contexto se modela con elementos nativos de PlantUML en disposición C4 nivel 1, que es visualmente equivalente y reproducible sin red.
2. **Legibilidad y ancho.** Todos los `.puml` incluyen `skinparam dpi 150`, `skinparam shadowing false` y una paleta de gris/azul institucional. Los diagramas anchos se declaran con `left to right direction` y se insertan con ancho fijo (`{width=6.3in}`) para que quepan en la caja de texto de la plantilla.
3. **Números antes que gráficos.** Los diagramas de magnitud (`problema-magnitud`) dibujan las barras con rectángulos de ancho proporcional e imprimen el valor exacto en la etiqueta. No se simulan ejes ni escalas engañosas.
4. **Anexo D intacto.** Los 12 diagramas existentes no se tocan: siguen viviendo en `docx/anexos/D_casos_de_uso.md`.
5. **Un solo idioma.** Todo el texto de los diagramas en español (consistente con el informe).
6. **Sin datos inventados.** Los diagramas solo representan información que ya existe en el informe (módulos, estados, integraciones, cifras citadas). Donde el dato proviene de una fuente externa, se agrega la atribución (ver Plan B, §B-6).

---

## A.4 Cambios en el pipeline (`docx/generar_informe.py`)

| Cambio | Detalle |
| :--- | :--- |
| **Nueva carpeta `docx/diagramas/`** | Un archivo `*.puml` por diagrama, con el mismo nombre que la clave (`canvas.puml`, `arq-contexto.puml`, …). Son fuentes editables y versionables |
| **Registro `DIAGRAMAS_CUERPO`** | Lista `(clave, ancho)`. `paso_diagramas()` renderiza **además** estos archivos hacia `docx/imagenes/figura-<clave>.png` |
| **Render incremental** | Si el PNG existe y es más reciente que el `.puml`, se omite. `--forzar` para re-renderizar todo |
| **Chequeo de precondiciones** | Si falta `java` o `plantuml.jar`, el paso informa y **no** borra las imágenes existentes (hoy devuelve error sin romper el resto del pipeline) |
| **Regex de figuras con ancho** | `paso_preprocesar()` acepta un atributo opcional: `![alt](ruta){width=6.3in} <!--#fig:clave-->` → se reemite como `![Figura N. alt](ruta){width=6.3in}` |
| **Conteo de figuras** | El log y el reporte informan figuras del cuerpo y de cada anexo por separado |

### Snippet de inserción en el markdown (patrón que se repetirá)

```
![Lienzo canvas de EspaciGo](imagenes/figura-canvas.png){width=6.3in} <!--#fig:canvas-->
```

La numeración la asigna el preprocesador en orden de aparición: no hay que escribir ningún número a mano.

---

## A.5 Validaciones nuevas (se suman a las 22 actuales)

| # | Validación |
| :--- | :--- |
| 23 | Todos los `.puml` del registro tienen su PNG en `docx/imagenes/` |
| 24 | Toda imagen referenciada desde `informe.md` existe (ya existe la 6; se amplía a las nuevas) |
| 25 | No hay `figura-*.png` huérfanas en `docx/imagenes/` (sin referencia) |
| 26 | El número de figuras del cuerpo coincide con las declaradas + las de los anexos |
| 27 | Ningún `.puml` quedó con el marcador `@startuml` duplicado o sin cerrar |
| 28 | Las imágenes insertadas caben en el ancho útil de la plantilla (aviso, no error) |

---

## A.6 Orden de ejecución propuesto

1. **A-F1** Crear `docx/diagramas/` con los 4 diagramas **MUST explícitos** (canvas, contexto, topología, organigrama) + ampliar el regex de ancho y el registro del script.
2. **A-F2** Insertar esos 4 en el markdown, regenerar (`diagramas preprocesar pandoc armar validar`) y **revisar visualmente** en Word: escala, legibilidad y salto de página.
3. **A-F3** Renderizar los 11 diagramas del Marco Teórico (§4.1–§4.11) y los SHOULD de los capítulos 2, 3, 5 y 6.
4. **A-F4** Opcionales (A-22 a A-24) según lo que decidas.
5. **A-F5** Regenerar el informe final, revisar las validaciones (0 errores / 0 advertencias) y actualizar el índice con `Ctrl+A` → `F9`.

---

## A.7 Estado de ejecución (19-09-2026)

**Ejecutado por completo: los 24 diagramas están generados e insertados.**

| Resultado | Detalle |
| :--- | :--- |
| Fuentes PlantUML | `docx/diagramas/*.puml` (24 archivos, editables y versionables) |
| Imágenes | `docx/imagenes/figura-<clave>.png` (24 nuevas; 36 figuras en total en el cuerpo) |
| Informe regenerado | 36 figuras numeradas, 20 tablas, 11 capítulos, **0 errores / 0 advertencias** |
| Validaciones nuevas | 23 (cada `.puml` tiene PNG), 24 (sin imágenes huérfanas), 25 (ancho informado) |
| Anexo D | Sin cambios: sus 11 diagramas de casos de uso y el modelo de actores siguen con su numeración `Figura X.n` |

**Desvío respecto de lo planificado:** el cronograma (A-21) se entrega como línea de tiempo de 16 semanas dibujada con caracteres de bloque (█ y ░) en lugar de `@startgantt`. Motivo: la carta Gantt nativa y la versión horizontal de 7 bloques quedaban con texto de ~5 pt al escalarlas al ancho de la página; con la versión de bloques el texto queda legible. El archivo se llama `cronograma.puml`.

### Reglas aprendidas para agregar diagramas nuevos (importante)

| Regla | Motivo |
| :--- | :--- |
| El archivo se llama `<clave>.puml` y la directiva debe ser `@startuml` **sin nombre** | PlantUML nombra el PNG según el nombre del diagrama si se indica; sin nombre usa el del archivo y el pipeline lo publica como `figura-<clave>.png` |
| La figura se declara `![Texto](imagenes/figura-<clave>.png){width=6.3in} <!--#fig:<clave>-->` | El preprocesador asigna el número en orden de aparición y resuelve las referencias cruzadas |
| Nada de `_cursiva_` (usar `<i>texto</i>`) y la negrita `**…**` no puede cruzar un salto de línea `\n` | en el marcado de PlantUML los delimitadores deben abrir y cerrar en la misma línea, si no se imprimen literales |
| Para filas y columnas con enlaces ocultos, usar `top to bottom direction` con `-[hidden]right->` | en modo `left to right` las pistas de dirección se interpretan como «misma fila» y el resultado se apila |
| Un solo diagrama por archivo, con `skinparam dpi 150` y sin `shadowing` | nitidez al escalar a 16,6 cm de ancho |
| Barras de datos con `█` y `░` separadas por espacios | se leen mejor que un gráfico mal escalado y evitan depender de datos externos |

---

## A.8 Criterios de aceptación

- Los 4 diagramas pedidos explícitamente están presentes y legibles en el `Informe_Final.docx`.
- Cada uno de los 11 apartados del Marco Teórico que admiten esquema tiene al menos una figura.
- La numeración de tablas y figuras sigue siendo correlativa y las referencias cruzadas se resuelven.
- El organigrama ASCII ya no aparece: es una imagen.
- Los 5 anexos se regeneran **sin cambios** en su numeración de figuras (`Figura X.n`).
- Validaciones: 0 errores y 0 advertencias. El único aviso esperado sigue siendo el de "actualizar campos (Ctrl+A, F9)".
