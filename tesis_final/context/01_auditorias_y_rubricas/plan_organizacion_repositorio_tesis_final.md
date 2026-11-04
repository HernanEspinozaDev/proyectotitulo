# 🏗️ Plan de Reorganización del Repositorio y Arquitectura Docskill para la Tesis Final

**Repositorio Destino:** `/home/nandev/Documentos/projects/Proyectotitulo`  
**Espacio Central de Trabajo:** `/home/nandev/Documentos/projects/Proyectotitulo/tesis_final`  
**Estándar de Automatización:** Metodología y Motor `docskill` (heredado de `espaciGo/ES2`)

---

## 1. Diagnóstico del Estado Actual del Repositorio `Proyectotitulo`

Al examinar `/home/nandev/Documentos/projects/Proyectotitulo`, se identifican tres capas superpuestas de trabajo:
1. **Directorio `Informes/ES1PT`:** Contiene la primera versión de la Evaluación Sumativa 1 (con los anexos de 236 RF, 43 RNF, 52 CU y 35 HU que obtuvieron calificación perfecta, pero con el cuerpo del informe desactualizado y observado).
2. **Directorio `Informes/ES2PT`:** Contiene una versión inicial/intermedia de la Evaluación Sumativa 2, la cual fue superada por el trabajo avanzado y pulido que reside en `/home/nandev/Documentos/projects/espaciGo/ES2`.
3. **Directorio `docskill/` y scripts sueltos:** Scripts en raíz (`scratch.py`, `scratch2.py`, `scratch3.py`) que fueron pruebas temporales de bases de datos sqlite de coordinación.

---

## 2. Estrategia de Migración y Limpieza del Repositorio

Para evitar confusiones, duplicidad de fuentes y garantizar un flujo de trabajo limpio y profesional, se define la siguiente reestructuración:

### Paso 1: Creación del Módulo Central `tesis_final/`
Se creará la carpeta `/home/nandev/Documentos/projects/Proyectotitulo/tesis_final` configurada con el estándar `docskill`:
```text
tesis_final/
├── AGENTS.md                   # Directrices operativas para asistentes de IA y colaboradores
├── project.md                  # Alcance, metadatos y manifiesto del proyecto de titulación
├── document.json               # Configuración central del ensamblador docskill (orden de secciones y anexos)
├── gestionar.py                # CLI de compilación y orquestación docskill
├── templates/                  # Plantillas oficiales INACAP (.docx) y perfil tipográfico/estilos (.json)
│   ├── reference-inacap.docx
│   └── style-profile-inacap.json
├── sections/                   # Capítulos del CUERPO de la tesis (modulares)
│   ├── 00-introduccion-y-contexto.md
│   ├── 01-planteamiento-problema.md
│   ├── 02-marco-teorico-y-estado-arte.md
│   ├── 03-definicion-solucion-kpi-sla.md
│   ├── 04-objetivos-del-proyecto.md
│   ├── 05-metodologia-de-desarrollo.md
│   ├── 06-planificacion-y-recursos.md
│   ├── 07-arquitectura-empresarial-y-ti.md
│   ├── 08-modelamiento-software-y-datos.md
│   ├── 09-pruebas-calidad-y-seguridad.md
│   ├── 10-estrategia-implementacion-despliegue.md
│   ├── 11-evaluacion-economica-financiera.md
│   └── 12-conclusiones-y-trabajos-futuros.md
├── appendices/                 # EXTENSIONES y ANEXOS técnicos exhaustivos
│   ├── a-requerimientos-ieee830.md        (236 RF + 43 RNF de ES1PT)
│   ├── b-historias-de-usuario.md          (35 HU con criterios INVEST de ES1PT)
│   ├── c-fichas-casos-de-uso.md           (52 CU estructurados de ES1PT)
│   ├── d-catalogo-endpoints-openapi.md    (Especificación de APIs de ES2)
│   ├── e-diccionario-datos-ddl.md         (Tablas, PK/FK, índices de ES2)
│   ├── f-matrices-pruebas-cobertura.md    (Unitarias, integración, E2E de ES2)
│   ├── g-politicas-seguridad-drp-sla.md   (Planes de contingencia y SLAs)
│   ├── h-carta-gantt-y-edt-detallada.md   (Desglose de tareas y esfuerzo)
│   └── i-estudio-mercado-y-cotizaciones.md (Cifras CBRE/Colliers y costos Cloud)
├── assets/                     # Recursos gráficos en alta resolución
│   └── figuras/                # Diagramas BPMN, C4, UML, ER, Topología Cloud
├── context/                    # Inteligencia de diseño, pautas y guías
│   ├── rubricas/               # Rúbricas oficiales de ES1, ES2 y Tesis
│   ├── auditorias/             # Informes forenses de retroalimentación
│   └── decisiones/             # Registros de arquitectura (ADR)
├── scripts/                    # Scripts de validación, QA de tablas y ensamblado
└── build/                      # Salidas generadas automáticamente (.docx, .pdf, validaciones)
```

### Paso 2: Importación Selectiva de Activos Validados

| Origen | Archivo / Componente | Destino en `tesis_final/` | Razón de la Elección |
|---|---|---|---|
| **ES1PT** | `anexo_requerimientos_funcionales.md`<br>`anexo_requerimientos_no_funcionales.md` | `appendices/a-requerimientos-ieee830.md` | Obtuvo puntaje perfecto (4.8/4.8) en la rúbrica oficial. |
| **ES1PT** | `anexo_historias_de_usuario.md` | `appendices/b-historias-de-usuario.md` | Contenido exhaustivo y formalmente aprobado. |
| **ES1PT** | `anexo_casos_de_uso.md` | `appendices/c-fichas-casos-de-uso.md` | Fichas detalladas con precondiciones, flujo principal y excepciones. |
| **espaciGo/ES2** | `assets/figuras/*.png` | `assets/figuras/` | Diagramas BPMN To-Be, Arquitectura Hexagonal C4, Modelo de Datos ER y Topología Cloud GCP ya renderizados en alta resolución. |
| **espaciGo/ES2** | `templates/*` | `templates/` | Plantilla institucional INACAP y perfil de estilos configurados con éxito en la entrega ES2. |
| **espaciGo/ES2** | `sections/*.md` | Base para `sections/07` a `sections/10` | Código y diseño técnico validado contra la rúbrica ES2. |
| **espaciGo/ES2** | `appendices/b-anexo.md` (DDL) y `d-anexo.md` (OpenAPI) | `appendices/d-*` y `appendices/e-*` | Diccionario de datos y especificación REST depurados. |
| **tesis_ejemplo** | `analisis_forense_rubrica_ES1_y_plan_mejora.md`<br>`comparativa_y_estructura_final_tesis_espacigo.md` | `context/auditorias/` | Memoria técnica que garantiza no repetir errores de pauta. |

### Paso 3: Limpieza y Preservación de `Proyectotitulo`
1. **Archivado de borradores temporales:** Mover `scratch.py`, `scratch2.py`, `scratch3.py` a una carpeta de soporte o eliminarlos si no tienen vigencia.
2. **Congelamiento de `Informes/ES1PT` e `Informes/ES2PT`:** Mantenerlos intactos como respaldo histórico inmutable.
3. **Vínculo del motor `docskill`:** Enlazar el entorno virtual `.venv` de `Proyectotitulo` para que el compilador `gestionar.py` dentro de `tesis_final/` funcione de manera autónoma con Pandoc y python-docx.

---

## 3. Plan de Acción de Próximos Pasos

1. **Fase 1 (Aprobación):** Confirmar con el usuario el esquema de carpetas y la estrategia de partición cuerpo vs. anexos.
2. **Fase 2 (Inicialización Física):** Ejecutar la creación de `/home/nandev/Documentos/projects/Proyectotitulo/tesis_final/` y sus subcarpetas.
3. **Fase 3 (Migración de Insumos Base):** Copiar los anexos perfectos de ES1PT y los activos técnicos de `espaciGo/ES2`.
4. **Fase 4 (Redacción Remediada de ES1):** Redactar las secciones de introducción, problema, marco teórico, metodología, cronograma y arquitectura TI corrigiendo al 100% las observaciones de la profesora Teresa Tapia.
