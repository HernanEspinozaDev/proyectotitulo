# Proyecto de Título — Plataforma espaciGo
**Universidad Tecnológica de Chile INACAP**  
*Área de Tecnologías de Información y Ciberseguridad*  
*Carrera: Ingeniería en Tecnologías de Información y Ciberseguridad*

---

## 📌 Resumen Ejecutivo del Proyecto

**espaciGo** es una plataforma web transaccional y de intermediación confiable orientada a la gestión y arriendo flexible de espacios comerciales e industriales subutilizados en Chile (tales como bodegas, oficinas compartidas, dark kitchens, estacionamientos, locales comerciales y recintos de eventos). 

La plataforma aborda el problema de asimetría informativa, desocupación de activos y fricción operacional en el sector inmobiliario no residencial mediante una arquitectura basada en microservicios desacoplados, contratos de arriendo automatizados, pasarela de pago seguro (escrow / custodia de fondos), verificación de identidad (KYC) y cumplimiento estricto con la Ley 21.719 sobre Protección de Datos Personales.

### Equipo de Desarrollo y Memoria de Título
- **Hernán Espinoza Marchant**: Líder Técnico, Arquitectura de Software y Seguridad.
- **Anita Marchant Silva**: Evaluación Económico-Financiera y Aseguramiento de Calidad.
- **Erick Silva Espinoza**: Planificación, Gestión Operacional y Continuidad de Negocio.
- **Profesora Guía**: Teresa de Jesús Tapia Soto.

---

## 📂 Estructura General del Repositorio

El repositorio se encuentra unificado y normalizado para el trabajo directo sobre la entrega final de la tesis:

```text
Proyectotitulo/
├── build_thesis.py           # Script maestro de compilación (DocSkill + Layout + PDF)
├── AGENTS.md                 # Guía técnica e instrucciones maestras para agentes de IA
├── README.md                 # Este documento de presentación y contexto
├── NOTION_MCP.md             # Guía de integración con el tablero de seguimiento en Notion
├── docskill/                 # Motor de compilación documental basado en Pandoc y OOXML
└── tesis_final/              # Núcleo del proyecto documental de la Memoria de Título
    ├── document.json         # Manifiesto y orden secuencial de capítulos y anexos
    ├── gestionar.py          # Utilidad local de inspección y validación DocSkill
    ├── sections/             # 15 Capítulos completos en formato Markdown (.md)
    ├── appendices/           # 8 Anexos técnicos exhaustivos en formato Markdown (.md)
    ├── templates/            # Plantilla institucional Word (.docx) y perfil de estilos
    ├── assets/
    │   ├── diagramas_src/    # Fuentes editables de diagramas (.puml y .mmd)
    │   └── imagenes/         # Renders en alta resolución (PNG) insertados en la tesis
    ├── scripts/              # Scripts de automatización, renderizado y maquetación
    ├── context/              # Base de conocimiento y contexto consolidado
    │   ├── 00_material_docente/          # Actividades y guías oficiales INACAP (ACT0 - ACT9)
    │   ├── 01_auditorias_y_rubricas/     # Rúbricas, auditorías forenses y correcciones docentes
    │   ├── 02_arquitectura_y_diseno/     # Especificación de arquitectura y referencias (.bib)
    │   ├── 03_insumos_anita_erick_finanzas/ # Modelos financieros, scripts bootstrap y supuestos
    │   └── 04_insumos_anita_erick_gantt/    # WBS, backlog, matrices y planificaciones Gantt
    └── build/                # Artefactos compilados finales
        ├── Tesis_Final_espaciGo.docx     # Documento Word oficial postprocesado (>560 págs.)
        └── Tesis_Final_espaciGo.pdf      # Documento PDF final exportado con LibreOffice
```

---

## 🛠️ Requisitos y Entorno de Ejecución

Para compilar la tesis y generar el PDF final se requiere:
- **Python**: 3.10 o superior (recomendado 3.12).
- **DocSkill**: Incluido en el directorio `docskill/` (con su binario local de Pandoc).
- **LibreOffice**: Versión de escritorio o headless para Linux (`soffice` / `libreoffice`).
- **PlantUML y Mermaid CLI** *(opcional, solo para regenerar diagramas desde fuentes)*:
  - Java JRE/JDK y Graphviz para PlantUML.
  - `@mermaid-js/mermaid-cli` (`mmdc`) instalado globalmente con Node.js.

---

## 🚀 Compilación del Documento

El repositorio incluye el comando maestro `build_thesis.py` en la raíz, que orquesta automáticamente todo el flujo:

```bash
# 1. Compilación completa (DocSkill -> Postprocesamiento APA/INACAP -> Exportación PDF)
python3 build_thesis.py

# 2. Compilar únicamente el archivo DOCX (sin invocar LibreOffice)
python3 build_thesis.py --no-pdf

# 3. Regenerar todos los diagramas PlantUML y Mermaid antes de compilar
python3 build_thesis.py --diagrams

# 4. Solo validar sintaxis y estructura documental sin generar archivos
python3 build_thesis.py --validate
```

### ¿Qué hace el postprocesamiento automático?
El script `tesis_final/scripts/postprocess_tesis_layout.py` se ejecuta inmediatamente tras la compilación de Pandoc para asegurar el cumplimiento del estándar institucional:
1. **Saltos de página por capítulo**: Fuerza que cada uno de los 15 capítulos y 8 anexos comience en una página nueva e impar.
2. **Tablas bajo APA 7**: Configura cuadrícula completa con bordes visibles (1/2 pt, negro) y sombreado institucional para los encabezados.
3. **Imágenes y figuras bajo APA 7**: Asigna el estilo oficial `ImageCaption` y `keepNext` al título superior de cada figura, eliminando subtítulos duplicados bajo la imagen.

---

## 📚 Mapa Estructural de la Memoria de Título

| Capítulo / Anexo | Nombre del Componente | Estado |
|---|---|---|
| **00** | Preliminares (Portada, Resumen, Abstract, Glosario) | Completo |
| **01** | Introducción y Contextualización | Completo |
| **02** | Planteamiento del Problema y Justificación | Completo |
| **03** | Marco Teórico y Estado del Arte | Completo |
| **04** | Objetivos, Alcance y Modelo de Negocio | Completo |
| **05** | Gestión del Proyecto y Marco Metodológico | Cuerpo completo (5.3 reservado para Gantt de integrantes) |
| **06** | Arquitectura Empresarial (TOGAF / Capas de Negocio) | Completo |
| **07** | Especificación de Requerimientos de Software | Completo |
| **08** | Diseño de Arquitectura de TI y Software | Completo |
| **09** | Modelamiento de Procesos y Datos | Completo |
| **10** | Aseguramiento de la Calidad y Pruebas de Software | Completo |
| **11** | Estrategia de Implementación, Despliegue y Ciberseguridad | Completo |
| **12** | Evaluación Económica y Financiera | **Reservado** para Anita Marchant y Erick Silva |
| **13** | Monitoreo, Control y Evaluación de Desempeño | Completo |
| **14** | Conclusiones y Trabajos Futuros | Completo |
| **Anexo A** | Especificación de Requerimientos bajo Estándar IEEE 830 | Completo |
| **Anexo B** | Catálogo Extendido de Historias de Usuario | Completo |
| **Anexo C** | Catálogo de Casos de Uso del Sistema | Completo |
| **Anexo D** | Diccionario de Datos Físico y Script DDL PostgreSQL | Completo |
| **Anexo E** | Catálogo de Interfaz de Programación de Aplicaciones (OpenAPI) | Completo |
| **Anexo F** | Matrices de Casos de Prueba del Sistema | Completo |
| **Anexo G** | Carta Gantt Detallada del Proyecto | **Reservado** para Anita Marchant y Erick Silva |
| **Anexo H** | Evaluación Económica Detallada (Flujo de Caja, VAN, TIR, Payback) | **Reservado** para Anita Marchant y Erick Silva |

---

## 👥 Secciones Reservadas para Integrantes del Equipo

Para salvaguardar el reparto de responsabilidades académicas acordado por el equipo:
- **Capítulo XII y Anexo H** (Evaluación Económica): Reservados exclusivamente para **Anita Marchant Silva** y **Erick Silva Espinoza**.
- **Capítulo V (Sección 5.3) y Anexo G** (Carta Gantt Detallada): Reservados exclusivamente para **Anita Marchant Silva** y **Erick Silva Espinoza**.
- Todos los insumos numéricos, scripts de simulación bootstrap, estudios de mercado y borradores previos necesarios para completar estas secciones se encuentran catalogados y respaldados en `tesis_final/context/03_insumos_anita_erick_finanzas/` y `tesis_final/context/04_insumos_anita_erick_gantt/`.
- En el cuerpo del texto se mantiene la alerta visible: `🟢 **[SECCIÓN RESERVADA PARA INTEGRACIÓN — ANITA MARCHANT Y ERICK SILVA]**`.
