# 📐 Plan Integral de Procesamiento de Diagramas, Rótulos APA 7 y Arquitectura de Fuentes de Imagen

**Proyecto:** Tesis de Grado "espaciGo"  
**Objetivo:** Erradicar bloques de código sin renderizar (`mermaid` y `plantuml`) en el documento final, transformándolos en figuras de alta resolución con rótulo y nota de elaboración formal APA 7, preservando el código fuente editable de forma modular y trazable.

---

## 1. Diagnóstico del Estado Actual en las Secciones

Al auditar los 15 archivos de capítulos en `sections/`, se detectó la presencia de **15 bloques de código Mermaid** y **2 bloques PlantUML** que actualmente Pandoc compila como texto plano o cajas de código fuente (`SourceCode`), en lugar de imágenes visuales:

| Capítulo / Sección | Bloques de Código Detectados | Tema / Diagrama que Representa | Acción Requerida |
|---|:---:|---|---|
| **Cap. II** (`02-planteamiento...md`) | 1 Mermaid + 1 PlantUML | Diagrama de Contexto *As-Is* del corretaje inmobiliario tradicional. | Renderizar a PNG; extraer código a archivo `.mmd` / `.puml`; embeber como **Figura 1**. |
| **Cap. III** (`03-marco-teorico...md`) | 2 Mermaid | 1. Arquitectura Hexagonal (*Puertos y Adaptadores*).<br>2. Secuencia de la Operatoria de Custodia (*Escrow*). | Renderizar a PNG; extraer a `.mmd`; embeber como **Figura 2** y **Figura 3**. |
| **Cap. V** (`05-gestion-del...md`) | 1 Mermaid | Ciclo de Vida Híbrido (Fases e Incrementos continuos sin 'backlog'). | Renderizar a PNG; extraer a `.mmd`; embeber como **Figura 4**. |
| **Cap. VI** (`06-arquitectura...md`) | 1 Mermaid | Estructura Organizacional de los 3 Socios Fundadores (Organigrama). | Renderizar a PNG; extraer a `.mmd`; embeber como **Figura 5**. |
| **Cap. VII** (`07-especificacion...md`) | 1 Mermaid | Matriz de Interacción entre Actores y Módulos de la Plataforma. | Renderizar a PNG; extraer a `.mmd`; embeber como **Figura 6**. |
| **Cap. VIII** (`08-diseno-de...md`) | 1 Mermaid | Arquitectura TI en 4 Capas bajo el Framework TOGAF. | Renderizar a PNG; extraer a `.mmd`; embeber como **Figura 7**. |
| **Cap. IX** (`09-modelamiento...md`) | 1 PlantUML *(+ 6 PNGs ya embebidos)* | Código PlantUML de BPMN-01 duplicado tras la imagen `fig02`. | Retirar snippet redundante de código y preservar archivo fuente `.puml`. |
| **Cap. X** (`10-aseguramiento...md`) | 2 Mermaid | 1. Dimensiones de Calidad del Software (ISO/IEC 25010).<br>2. Cronología del Simulacro de Resiliencia DRP (Validación RPO/RTO). | Renderizar a PNG; extraer a `.mmd`; embeber como **Figura 14** y **Figura 15**. |
| **Cap. XI** (`11-estrategia-de...md`) | 3 Mermaid *(+ 4 PNGs ya embebidos)* | 1. Pipeline CI/CD en GitHub Actions.<br>2. Topología de Red y Cómputo GCP.<br>3. Secuencia del Protocolo Anti-Replay (Ley 21.719). | Renderizar a PNG; extraer a `.mmd`; asociar con figuras correspondientes. |
| **Cap. XIII** (`13-monitoreo...md`) | 1 Mermaid | Compuertas de Fase (*Phase Gates*) y Desempeño de Iteraciones. | Renderizar a PNG; extraer a `.mmd`; embeber como **Figura 20**. |
| **Cap. XIV** (`14-conclusiones...md`) | 1 Mermaid | Línea de Tiempo de la Hoja de Ruta Tecnológica (Fases 2027 a 2029). | Renderizar a PNG; extraer a `.mmd`; embeber como **Figura 21**. |

---

## 2. Recomendación Técnica de Rotulación: ¿"Figura", "Diagrama" o "Ilustración"?

> [!IMPORTANT]
> **Estándar Recomendado: Utilizar estrictamente el rótulo `Figura X`.**
> 
> **Fundamentación Académica y Normativa:**
> 1. **Norma APA 7ma Edición (Oficial en INACAP):** Clasifica todo elemento visual en únicamente dos categorías canónicas: **Tablas** (datos numéricos o textuales en filas y columnas) y **Figuras** (cualquier otra representación visual: diagramas de flujo, esquemas UML, planos BPMN, capturas de pantalla, organigramas, mapas y gráficos estadísticos).
> 2. **Evita la fragmentación de índices:** Si se mezclaran rótulos como *"Diagrama 1"*, *"Ilustración 1"* y *"Figura 1"*, Word generaría tres índices de figuras separados de apenas 2 o 3 líneas cada uno, lo cual confunde la lectura. Un único **Índice de Figuras** correlativo del 1 al N ofrece una presentación editorial homogénea, sobria y universitaria.

### Formato de Presentación APA 7 para cada Figura:

```markdown
**Figura X**  
*Título breve y descriptivo del diagrama o proceso*

![Figura X: Título descriptivo](assets/figuras/figXX_nombre_descriptivo.png)

*Nota.* Elaboración propia (o bien: Adaptado de Cockburn (2005) / Google Cloud Platform (2024)).
```

---

## 3. Arquitectura de Archivos y Trazabilidad de Fuentes

Para cumplir con la solicitud de **dejar el código individual en una ruta editable y vinculada con el mismo nombre de la imagen**, se propone la siguiente estructura de directorios dentro de `tesis_final/`:

```text
tesis_final/
├── assets/
│   ├── figuras/                        # IMÁGENES RENDERIZADAS (Salidas PNG en alta resolución)
│   │   ├── fig01_contexto_as_is.png
│   │   ├── fig02_arquitectura_hexagonal.png
│   │   ├── fig03_secuencia_escrow_garantia.png
│   │   ├── fig04_ciclo_vida_hibrido_fases.png
│   │   ├── fig05_organigrama_espacigo.png
│   │   ├── ...
│   │   └── fig21_hoja_ruta_tecnologica.png
│   │
│   └── diagramas_src/                  # CÓDIGOS FUENTE EDITABLES (Trazabilidad 1 a 1)
│       ├── fig01_contexto_as_is.mmd
│       ├── fig01_contexto_as_is.puml
│       ├── fig02_arquitectura_hexagonal.mmd
│       ├── fig03_secuencia_escrow_garantia.mmd
│       ├── fig04_ciclo_vida_hibrido_fases.mmd
│       ├── fig05_organigrama_espacigo.mmd
│       ├── ...
│       └── fig21_hoja_ruta_tecnologica.mmd
│
└── scripts/
    └── render_all_diagrams.py          # Script de automatización de compilación de diagramas
```

### Ventajas de esta Arquitectura:
1. **Edición Inmediata:** Si la profesora o un integrante del equipo desea modificar un texto, agregar un rol o cambiar un color en una figura, simplemente abre el archivo `.mmd` o `.puml` correspondiente en `assets/diagramas_src/` y lo edita en cualquier editor de texto.
2. **Re-generación Automatizada:** Al ejecutar `python3 scripts/render_all_diagrams.py`, el sistema compila automáticamente todos los diagramas fuente a imágenes PNG de 300 DPI utilizando `npx @mermaid-js/mermaid-cli` (herramienta que ya verificamos instalada en el sistema, versión 12.2.0).
3. **Limpieza del Markdown:** Los capítulos de la tesis quedan limpios de bloques kilométricos de código, mejorando la legibilidad del texto académico.

---

## 4. Catálogo Detallado de Figuras a Generar y Embeber

A continuación se define el inventario unificado de las **21 Figuras Oficiales** de la Tesis:

| # Figura | Archivo Fuente (`assets/diagramas_src/`) | Imagen Generada (`assets/figuras/`) | Título Oficial APA 7 | Fuente / Nota |
|:---:|---|---|---|---|
| **Figura 1** | `fig01_contexto_as_is.mmd` | `fig01_contexto_as_is.png` | *Diagrama de Contexto As-Is del Ecosistema Inmobiliario Tradicional* | *Nota.* Elaboración propia. |
| **Figura 2** | `fig02_arquitectura_hexagonal.mmd` | `fig02_arquitectura_hexagonal.png` | *Patrón de Arquitectura Hexagonal (Puertos y Adaptadores)* | *Nota.* Adaptado de Cockburn (2005) y Martin (2017). |
| **Figura 3** | `fig03_secuencia_escrow_garantia.mmd` | `fig03_secuencia_escrow_garantia.png` | *Diagrama de Secuencia de la Operatoria Transaccional en Custodia (Escrow)* | *Nota.* Elaboración propia en base a estándares fiduciarios digitales. |
| **Figura 4** | `fig04_ciclo_vida_hibrido_fases.mmd` | `fig04_ciclo_vida_hibrido_fases.png` | *Modelo de Proceso del Ciclo de Vida Híbrido por Fases e Incrementos* | *Nota.* Elaboración propia según estándares PMI (2021). |
| **Figura 5** | `fig05_organigrama_espacigo.mmd` | `fig05_organigrama_espacigo.png` | *Estructura Organizacional y Roles del Equipo Fundador de espaciGo SpA* | *Nota.* Elaboración propia. |
| **Figura 6** | `fig06_actores_modulos_sistema.mmd` | `fig06_actores_modulos_sistema.png` | *Diagrama de Interacción entre Actores y Módulos de la Plataforma* | *Nota.* Elaboración propia. |
| **Figura 7** | `fig07_arquitectura_togaf_capas.mmd` | `fig07_arquitectura_togaf_capas.png` | *Arquitectura Empresarial y de TI bajo las Cuatro Capas de TOGAF* | *Nota.* Elaboración propia según The Open Group (2022). |
| **Figura 8** | `fig08_bpmn_publicacion_kyc.puml` | `fig08_bpmn_publicacion_kyc.png` | *Proceso BPMN-01: Publicación, Verificación KYC/KYB y Moderación* | *Nota.* Elaboración propia en notación BPMN 2.0. |
| **Figura 9** | `fig09_bpmn_reserva_escrow.puml` | `fig09_bpmn_reserva_escrow.png` | *Proceso BPMN-02: Búsqueda, Reserva y Operación Escrow Transaccional* | *Nota.* Elaboración propia en notación BPMN 2.0. |
| **Figura 10** | `fig10_bpmn_supresion_ley21719.puml` | `fig10_bpmn_supresion_ley21719.png` | *Proceso BPMN-03: Ejercicio de Derechos ARCO y Supresión de Datos Personales* | *Nota.* Elaboración propia según la Ley N° 21.719. |
| **Figura 11** | `fig11_uml_casos_uso_ecosistema.puml` | `fig11_uml_casos_uso_ecosistema.png` | *Diagrama UML de Casos de Uso del Ecosistema Transaccional* | *Nota.* Elaboración propia bajo estándar UML 2.5. |
| **Figura 12** | `fig12_componentes_hexagonal.puml` | `fig12_componentes_hexagonal.png` | *Diagrama de Paquetes y Componentes del Backend Hexagonal en Go* | *Nota.* Elaboración propia. |
| **Figura 13** | `fig13_modelo_datos_er_nucleo.puml` | `fig13_modelo_datos_er_nucleo.png` | *Modelo Entidad-Relación del Núcleo Transaccional y Persistencia Geoespacial* | *Nota.* Elaboración propia en base al esquema PostgreSQL 18 / PostGIS 3.6. |
| **Figura 14** | `fig14_modelo_calidad_iso25010.mmd` | `fig14_modelo_calidad_iso25010.png` | *Dimensiones de Calidad del Software según el Estándar ISO/IEC 25010* | *Nota.* Adaptado de ISO/IEC 25010 (2011). |
| **Figura 15** | `fig15_cronologia_simulacro_drp.mmd` | `fig15_cronologia_simulacro_drp.png` | *Cronología del Simulacro de Resiliencia y Validación Empírica de RPO y RTO* | *Nota.* Elaboración propia a partir de telemetría en Google Cloud Monitoring. |
| **Figura 16** | `fig16_pipeline_ci_cd_github.mmd` | `fig16_pipeline_ci_cd_github.png` | *Flujo de Automatización del Pipeline CI/CD en GitHub Actions* | *Nota.* Elaboración propia. |
| **Figura 17** | `fig17_infraestructura_cloud_gcp.puml`| `fig17_infraestructura_cloud_gcp.png` | *Topología de Infraestructura Cloud en Google Cloud Platform (Región Santiago)* | *Nota.* Elaboración propia sobre servicios gestionados GCP. |
| **Figura 18** | `fig18_segmentacion_red_vpc.puml` | `fig18_segmentacion_red_vpc.png` | *Segmentación de Red Privada y Comunicaciones Seguras vía Serverless VPC Connector*| *Nota.* Elaboración propia. |
| **Figura 19** | `fig19_secuencia_anti_replay.mmd` | `fig19_secuencia_anti_replay.png` | *Diagrama de Secuencia del Protocolo de Purga Anti-Restauración (Ley 21.719)* | *Nota.* Elaboración propia. |
| **Figura 20** | `fig20_compuertas_fase_gates.mmd` | `fig20_compuertas_fase_gates.png` | *Esquema de Control por Compuertas de Fase (Phase Gates) y Desempeño* | *Nota.* Elaboración propia según lineamientos PMBOK. |
| **Figura 21** | `fig21_hoja_ruta_tecnologica.mmd` | `fig21_hoja_ruta_tecnologica.png` | *Línea de Tiempo de la Hoja de Ruta Tecnológica de espaciGo (2027 - 2029)* | *Nota.* Elaboración propia. |

---

## 5. Plan de Ejecución Paso a Paso

1. **Paso 1: Creación de la Carpeta de Fuentes:**  
   Crear el directorio `/home/nandev/Documentos/projects/Proyectotitulo/tesis_final/assets/diagramas_src/`.
2. **Paso 2: Extracción y Resguardo de Fuentes:**  
   Extraer cada bloque `mermaid` y `plantuml` existente en los archivos Markdown de `sections/` y guardarlo en su respectivo archivo individual `.mmd` o `.puml` con el nombre de la figura (ej: `fig01_contexto_as_is.mmd`).
3. **Paso 3: Renderizado Automatizado a PNG en Alta Resolución:**  
   Ejecutar el script que invoque `npx -y @mermaid-js/mermaid-cli -i assets/diagramas_src/figXX.mmd -o assets/figuras/figXX.png -w 1600 -b white` para generar imágenes nítidas de 1600px de ancho con fondo blanco profesional.
4. **Paso 4: Sustitución en las Secciones Markdown:**  
   Reemplazar en cada sección el bloque de código por la sintaxis formal APA 7:
   - Rótulo superior: `**Figura X**`
   - Título en cursiva: `*Título de la Figura*`
   - Imagen enlazada: `![...](assets/figuras/figXX_nombre.png)`
   - Nota al pie: `*Nota.* Elaboración propia.`
5. **Paso 5: Recompilación y Verificación de DOCX y PDF:**  
   Compilar mediante `gestionar.py` y post-procesar saltos de página y tablas, verificando que todas las imágenes aparezcan nítidamente centradas en Word y en el PDF.
