# Directrices de Trabajo y Estándares de Ingeniería — Tesis Final espaciGo

## 1. Misión del Asistente
Asistir al equipo de desarrollo (Hernán Espinoza, Anita Marchant, Erick Silva) en la redacción, validación y compilación de la **Memoria de Título Final** de espaciGo bajo los estándares institucionales de INACAP y la pauta de evaluación de la profesora guía Teresa Jesús Tapia Soto.

---

## 2. Reglas de Estilo y Redacción Académica
1. **Persona y Tiempo Verbal:** Toda la redacción debe realizarse estrictamente en **tercera persona singular en tiempo presente** (*"El sistema implementa"*, *"La arquitectura procesa"*, *"La metodología establece"*). Queda prohibida la primera persona plural (*"hicimos"*, *"nuestra propuesta"*) o el futuro genérico (*"se implementará"*).
2. **Citas y Fuentes (APA 7):** Ninguna afirmación empírica, técnica o estadística debe quedar aislada. Todo dato de mercado o concepto teórico debe tener su cita formal `(Autor, Año)`.
3. **Frontera Estricta Cuerpo vs. Anexos:**
   - El **cuerpo principal** contiene narrativa fluida, análisis crítico, diagramas arquitectónicos y tablas de síntesis ejecutiva.
   - Los **anexos** contienen catálogos exhaustivos (236 RF, 43 RNF, 52 CU, 35 HU, DDL de 110 tablas, especificación OpenAPI completa).
4. **Reserva de Secciones Económicas y Carta Gantt (Alerta Verde):**
   - Todas las secciones y anexos relativos a costos, presupuestos, cuentas, flujos de caja y Carta Gantt detallada deben llevar obligatoriamente la alerta en **color verde** mediante la sintaxis `> [!TIP]`:
     ```markdown
     > [!TIP]
     > 🟢 **[SECCIÓN RESERVADA PARA INTEGRACIÓN — ANITA MARCHANT Y ERICK SILVA]**
     > Anita y Erick agregarán esta parte (planificación detallada con Carta Gantt / evaluación económica y cuentas).
     ```
   - El asistente no debe redactar ni importar cifras financieras o cronogramas detallados de informes anteriores, respetando la autoría exclusiva de Anita y Erick.
5. **Estándar Técnico de Diagramas (PlantUML y Notación Oficial):**
   - Todos los diagramas de modelado de software deben diseñarse técnicamente en **PlantUML** respetando rigurosamente el estándar formal:
     - **Diagramas de Casos de Uso:** Notación UML estricta (actores externos, límites del sistema `rectangle`, relaciones `<<include>>` y `<<extend>>`). Prohibido mezclar requerimientos no funcionales (como hashing o SSL) dentro de casos de uso.
     - **Diagramas de Clases y Paquetes:** Visibilidad (+, -, #), tipos de datos, multiplicidad (1..*, 0..1) y estereotipos claros.
     - **Diagramas de Secuencia:** Líneas de vida (`participant`), mensajes sincrónicos/asincrónicos y fragmentos combinados (`alt`, `loop`, `opt`).
     - **Diagramas de Procesos:** Notación BPMN 2.0 estándar (piscinas/carriles, compuertas exclusivas/paralelas, eventos de inicio/fin).
     - El código fuente `.puml` debe preservarse o documentarse para trazabilidad y versionado.
6. **Rigor Terminológico Metodológico:**
   - La metodología adoptada es el **Enfoque Híbrido: PMBOK (gobernanza y EDT) + Iterativo-Incremental (construcción de software)**.
   - Queda estrictamente prohibido usar términos de Scrum como *"Product Backlog"*, *"Sprint"* o *"Sprint Backlog"*, debiendo emplearse *"Línea Base del Alcance (EDT)"* e *"Incremento de Iteración"*.
7. **Métricas de Resiliencia Cloud (SLAs):**
   - RPO $\le 15$ minutos y RTO $\le 1$ hora (según RNF-010 y acuerdos con GCP Cloud SQL y Cloud Run).

---

## 3. Compilación y Contexto
- Para compilar el documento completo: `python3 ../build_thesis.py` desde `tesis_final/` o `python3 build_thesis.py` desde la raíz.
- Consulta toda la información histórica, rúbricas e insumos para Anita y Erick en la carpeta `context/`.


