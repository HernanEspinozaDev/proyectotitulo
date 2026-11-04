# CAPÍTULO VI: ARQUITECTURA EMPRESARIAL Y ORGANIZACIONAL

## 6.1. Identidad Estratégica: Misión, Visión y Valores de espaciGo SpA

La formulación de la empresa desarrolladora y operadora se formaliza bajo la razón social **espaciGo SpA**, una empresa de base tecnológica (*startup*) orientada al sector *Prop-Tech*.

### 6.1.1. Misión
Proveer una plataforma tecnológica multilateral, segura y transparente que conecte eficientemente a propietarios de espacios físicos no residenciales subutilizados con personas y empresas que requieren infraestructura flexible de corto y mediano plazo en Chile, eliminando barreras burocráticas mediante la automatización transaccional, el depósito en garantía (*escrow*) y la seguridad jurídica.

### 6.1.2. Visión
Consolidarse hacia el año 2029 como el ecosistema digital líder en intermediación y gestión de espacios comerciales e industriales flexibles en Chile, transformando la forma en que las organizaciones y personas acceden y rentabilizan los metros cuadrados urbanos bajo los más rigurosos estándares de ciberseguridad y protección de datos personales.

### 6.1.3. Valores Corporativos
1. **Transparencia e Integridad Transaccional:** Cada proceso de reserva, cálculo de comisiones, custodia de garantías y resolución de disputas se ejecuta con trazabilidad matemática y probatoria auditable.
2. **Privacidad y Seguridad por Diseño:** La protección de datos personales y la salvaguarda de transacciones financieras no son complementos posteriores, sino principios arquitectónicos fundacionales del software.
3. **Innovación Pragmática:** Adopción de tecnologías modernas y estables que resuelvan problemas operativos concretos sin introducir sobrecostos innecesarios para los usuarios.
4. **Enfoque en la Flexibilidad:** Compromiso permanente con la eliminación de trabas contractuales rígidas, democratizando el acceso a infraestructura física para el emprendimiento nacional.

---

## 6.2. Objetivos Estratégicos Institucionales

Para orientar el crecimiento corporativo y la madurez de la solución, se definen los siguientes objetivos estratégicos a corto, mediano y largo plazo:

*   **Objetivo a Corto Plazo (1 Año):**  
    Completar el desarrollo, validación y despliegue del MVP funcional de la plataforma en la Región Metropolitana, alcanzando un inventario activo de al menos 150 espacios verificados (oficinas, bodegas, locales y estacionamientos) y procesando un mínimo de 500 transacciones mensuales con una tasa de satisfacción de usuarios superior al 90%.
*   **Objetivo a Mediano Plazo (3 Años):**  
    Expandir la operación comercial a los principales polos industriales y comerciales del país (Valparaíso, Biobío y Antofagasta), alcanzar el punto de equilibrio financiero (*break-even*) y procesar un volumen bruto transaccional de USD 2,5 millones anuales.
*   **Objetivo a Largo Plazo (5 Años):**  
    Posicionar a espaciGo como la plataforma de referencia nacional para el arriendo corporativo flexible e iniciar la prospección de internacionalización hacia mercados emergentes de la región latinoamericana (Perú y Colombia).

---

## 6.3. Estructura Organizacional de la Empresa

En estricta concordancia con las observaciones de la auditoría docente, la estructura organizacional de espaciGo SpA refleja **exclusivamente a los miembros del equipo fundador y ejecutor**, delimitando con precisión sus responsabilidades ejecutivas y técnicas:

**Figura 5**  
*Estructura Organizacional y Roles del Equipo Fundador de espaciGo SpA*

![](assets/figuras/fig05_organigrama_espacigo.png)

*Nota.* Elaboración propia en base a la definición de roles ejecutivos y técnicos de los socios fundadores.

---

## 6.4. Análisis de Situación Actual: Matriz FODA Cruzada

El diagnóstico estratégico de la empresa de base tecnológica se realiza mediante una matriz **FODA Cruzada**, articulando estrategias ofensivas (FO), de adaptación (DO), defensivas (FA) y de supervivencia (DA):

**Tabla 6**  
*Matriz Estratégica FODA Cruzada de espaciGo SpA*

| Matriz FODA | **Fortalezas (F)**<br>1. Arquitectura Cloud moderna de bajo costo operativo.<br>2. Algoritmo de prevención de sobre-reserva con PostGIS.<br>3. Dominio de la Ley N° 21.719 y ciberseguridad.<br>4. Equipo multidisciplinario con roles definidos. | **Debilidades (D)**<br>1. Marca nueva sin reconocimiento inicial de mercado.<br>2. Presupuesto acotado para marketing de captación masiva.<br>3. Dependencia de validación de identidad externa (APIs).<br>4. Equipo técnico reducido sin fuerza de ventas presencial. |
|---|---|---|
| **Oportunidades (O)**<br>1. Alta tasa de vacancia en oficinas y bodegas post-pandemia.<br>2. Auge sostenido del *e-commerce* y demanda de bodegaje *flex*.<br>3. Descontento generalizado con corredores tradicionales.<br>4. Vigencia de la Ley N° 21.461 que ampara contratos digitales. | **Estrategias FO (Ofensivas):**<br>• Posicionar a espaciGo como la solución tecnológica directa para rentabilizar oficinas y bodegas ociosas con arriendos flexibles.<br>• Integrar marketing digital enfocado en microempresas de *e-commerce* que requieren bodegaje transitorio inmediato con contratos respaldados. | **Estrategias DO (Adaptación):**<br>• Establecer alianzas estratégicas con gremios de Pymes (ASECH) y centros de emprendimiento para adquirir volumen de usuarios con bajo gasto publicitario.<br>• Implementar flujos manuales de contingencia cuando los servicios externos de KYC presenten latencia. |
| **Amenazas (A)**<br>1. Entrada de competidores internacionales consolidados.<br>2. Resistencia cultural al arriendo digital de inmuebles.<br>3. Incertidumbre regulatoria o cambios impositivos.<br>4. Intentos de fraude cibernético o suplantación de identidad. | **Estrategias FA (Defensivas):**<br>• Destacar la custodia en garantía (*escrow*) y el estricto apego a la Ley 21.719 como factor diferenciador frente a portales estáticos vulnerables.<br>• Garantizar precios y comisiones transparentes frente a plataformas extranjeras de cobro en divisas. | **Estrategias DA (Supervivencia):**<br>• Mantener costos fijos de servidores en Cloud Run mediante autoescalado a cero durante inactividad nocturna.<br>• Reforzar el monitoreo automatizado de logs y alertas para neutralizar de inmediato vectores de ataque o fraude. |

*Nota.* Elaboración propia en base al diagnóstico de capacidades internas y entorno macroeconómico.

---

## 6.5. Alineación Estratégica y Compatibilidad con la Arquitectura Empresarial (TOGAF Capa de Negocio)

La integración de la plataforma dentro de la arquitectura empresarial se fundamenta en la **Capa de Negocio del framework TOGAF** (*The Open Group Architecture Framework*).

### 6.5.1. Compatibilidad Tecnológica y Operativa
La plataforma **espaciGo** se alinea estrictamente con las capacidades operacionales de la empresa:
1. **Alineación con la Cadena de Valor:** La solución digitaliza íntegramente las actividades primarias de la empresa (adquisición de inventario, publicación, búsqueda geoespacial, reserva, custodia fiduciaria y cobro de comisión), eliminando las tareas manuales de intermediación física.
2. **Eficiencia en Costos Marginales:** Al apoyarse en infraestructura contenerizada y serverless (Cloud Run), el costo operacional de incorporar un nuevo inmueble o procesar una nueva reserva es cercano a cero, permitiendo márgenes brutos operacionales superiores al 80% del *take rate*.
3. **Gobierno de la Información:** Toda la arquitectura de negocio se diseña como una máquina de estados determinista (BPMN), garantizando que ningún inmueble pueda ser ocupado sin contrato firmado digitalmente y sin fondos de garantía debidamente asegurados en la pasarela fiduciaria.
