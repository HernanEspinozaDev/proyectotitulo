# Plan de resolución de pendientes (citas, fuentes y atribuciones)

> Estado: **ejecutado** (20-09-2026). Este documento registra el plan, lo que se
> resolvió con investigación en la web, lo que quedó cerrado y lo que falta.

---

## 1. Problema 1: Word no veía las fuentes («Fuente especificada no válida»)

### Diagnóstico

| Comprobación | Resultado |
| :--- | :--- |
| ¿La plantilla trae una parte de fuentes? | **Sí**: `customXml/item4.xml` con `<b:Sources>` vacío y su `itemProps4.xml` con el `schemaRef` de la bibliografía |
| ¿Está relacionada con el documento? | Sí: `word/_rels/document.xml.rels` incluye `rId4 → ../customXml/item4.xml` |
| ¿Las citas eran campos? | Sí: 34 campos `CITATION <tag> \l 13322` y un campo `BIBLIOGRAPHY` |
| **Causa raíz** | El paquete quedaba con **two entradas ZIP del mismo nombre** (`customXml/item4.xml`): la vacía de la plantilla y la generada. Word leía la primera (vacía) → 0 fuentes → los campos no se resolvían y Word escribía «Fuente especificada no válida» al actualizarlos |

### Corrección aplicada

- `_inyectar_fuentes()` ahora **reemplaza** la entrada existente del ZIP en vez de añadir una parte nueva; las partes nuevas solo se crean si la plantilla no trae ninguna.
- Añadida una validación que detecta entradas duplicadas en el paquete antes de dar por bueno el documento.

### Verificación con Word (automatización COM, sobre una copia)

| Comprobación | Resultado |
| :--- | :--- |
| Fuentes que ve Word (`Document.Bibliography.Sources`) | **16**, con la etiqueta correcta de cada una |
| Estilo bibliográfico seleccionado | **APA** |
| Campos del documento | 37 (34 citas + 1 lista + 1 TOC + 1 referencia de página) |
| Tras `Ctrl+A` → `F9` | Citas resueltas: `(Biblioteca del Congreso Nacional de Chile, 2022)`, sin ningún error de fuente |
| Lista de referencias | Se regeneró con las 16 entradas |

**Conclusión:** el sistema de fuentes nativas ya funciona. La única diferencia al pulsar `F9` es el estilo: el XSL que usa esta instalación de Word es el de APA 6 (su renderizado escribe «Obtenido de» y «(s.f.)»); si tu Word ofrece APA 7, cámbialo en Referencias → Estilo.

---

## 2. Problema 2: pendientes de datos bibliográficos

### 2.1 Completado con investigación verificada

| Entrada | Dato que faltaba | Dato obtenido y verificado |
| :--- | :--- | :--- |
| `ley21461` | Título oficial, fecha, URL | Publicada el **30-06-2022**; título oficial completo incorporado; `bcn.cl/leychile/navegar?idNorma=1178004` |
| `ley21719` | Título oficial, fecha, URL | Publicada el **13-12-2024**; «Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales»; `bcn.cl/leychile/navegar?i=1209272` |
| `ley19799` | Fecha, URL | Publicada el **12-04-2002**; `bcn.cl/leychile/navegar?idNorma=196640` |
| `iso25010` | ¿Edición 2011 o 2023? | **ISO/IEC 25010:2023**, edición 2 (2023-11), «Product quality model»; `iso.org/standard/78176.html` |
| `pcidss` | ¿4.0 o 4.0.1? | **v4.0.1**, publicada en junio de 2024 (revisión limitada de la v4.0 de 2022) |
| 8 documentaciones en línea | Fecha de consulta y versión | Fecha de consulta **20-09-2026** registrada con `urldate` (la versión específica no es exigible en APA 7 para documentación de producto) |
| **Nuevas fuentes de mercado** | Cifras de vacancia sin respaldo | `colliers2026` (vacancia 9,9% ≈ 255.000 m², 1T 2026) y `cbre2026` (9,64% general y 9,22% en clase A, 1T 2026) |

### 2.2 Datos de mercado: de dónde salieron las cifras

| Afirmación del informe | Estado final |
| :--- | :--- |
| Vacancia de oficinas en Santiago | **Verificada**: 9,9% (Colliers, 1T 2026, ≈255.000 m²; cierre 2025 en 10,1%) y 9,64% / 9,22% clase A (CBRE, 1T 2026) |
| Oficinas «clase C y antiguas»: 14% a 18%; bodegas flex: 14,5% y 219.000 m²; locales en galerías: más de 15% | **No verificables** con fuentes públicas en la fecha de referencia. Se retiraron las cifras y el texto pasó a una descripción cualitativa; la figura se rehízo solo con las cifras respaldadas |
| Menciones a CBRE, Colliers, CChC, INE, JLL y GPS Property sin cita | CBRE y Colliers quedaron con cita real; de la CChC, INE, JLL y GPS Property no se localizó un informe con la cifra concreta, por lo que **no se citan** y el texto no les atribuye datos |
| Citas manuales `(INE, 2026; CBRE, 2026)` y `(Colliers, 2026)` | **Retiradas**: reemplazadas por citas con campo y fuente registrada |
| Marca `[[PENDIENTE: …]]` del capítulo 2 | **Eliminada**: el apartado ahora explica los datos verificados y declara explícitamente lo que no tiene fuente |

### 2.3 Atribuciones en tablas y figuras

- El preprocesador añade una nota `Fuente:` bajo **cada** tabla y figura (56 en total): «elaboración propia» por defecto y la fuente real donde corresponde.
- La figura de magnitud de la vacancia quedó atribuida a **CBRE (2026) y Colliers (2026)**.
- La tabla de evidencia digital quedó como «elaboración propia a partir del modelo de auditoría descrito en el capítulo».

---

## 3. Lo que queda por decisión tuya (no bloquea la entrega)

| Punto | Detalle |
| :--- | :--- |
| Estilo APA al actualizar campos | Si tu Word tiene APA 7, selecciónalo en Referencias → Estilo; el texto en caché ya está en APA 7 |
| Cifras de bodegas y locales | Si consigues el informe original (por ejemplo, un reporte de Colliers de bodegas), se registran como fuente y se reponen las cifras de esos segmentos |
| Fuentes de la CChC, INE, JLL y GPS Property | Igual que el punto anterior: con el informe y su URL se agregan al catálogo en minutos |
| Metadatos de las 16 fuentes | Verificar visualmente la lista en Word (Referencias → Administrar fuentes) y confirmar autores y años |
| Fecha de entrega del informe | La portada indica 15-09-2026; si cambia, se actualiza en `informe.md` (campo `fecha`) |

---

## 4. Trazabilidad de las decisiones de «no inventar»

- Los datos que no se pudieron verificar **no se completaron con suposiciones**: se retiraron las cifras o se describieron de forma cualitativa.
- Los 12 pendientes originales quedaron **cero** en el catálogo: `referencias.bib` ya no tiene ninguna nota `PENDIENTE`.
- La auditoría (`build/auditoria_citas.md`) sigue informando el estado de cada fuente en cada regeneración.
