# Integración de Estudios para el Flujo de Caja y Evaluación Económica (EspaciGo)

**Procedencia:** aporte incorporado al repositorio por la identidad Git «Shiva» en el commit `2030456` del 28-09-2026. Git registra esa identidad como autora del contenido. Se conserva íntegro como aporte de trabajo de un integrante del equipo y forma parte del informe ES2 según `informe.json`.

**Estado:** antecedente metodológico preliminar, no modelo financiero aprobado. Sus cuadros suponen 3.600 reservas anuales, comisión del 25 %, costos e impuestos hipotéticos y un VAN positivo. Esos parámetros y resultados no coinciden con el escenario vigente del Anexo A, que usa volúmenes hipotéticos de 720 y 1.800 reservas, comisión neta del **3 %**, tarifa del proveedor descontada al vendedor e instancia API mínima. El VAN de caja simulado vigente es **−15.140.998 CLP** y la TIR no está definida. El ejercicio posterior de 12 % de comisión también queda como histórico. Por tanto, las cifras y la conclusión de rentabilidad de este aporte se conservan por su procedencia y método, sin tratarlas como resultados actuales del proyecto.

Este aporte del equipo organiza conceptos de mercado, inversión, operación y financiamiento para orientar la evaluación económica. Las cifras que aparecen a continuación pertenecen a un **ejercicio preliminar** y se contrastan con la simulación vigente del Anexo A; no sustituyen precios finales ni demanda medida.

## 1. Estudio de Mercado (Capítulo 4)
El estudio de mercado es la base para cuantificar los ingresos y egresos vinculados a la comercialización. Define la cuantía de la demanda, los ingresos de operación y gran parte de los costos e inversiones.

**Componentes aplicados al proyecto:**
*   **Análisis del Submercado:**
    *   *Consumidor:* Preferencias, hábitos y motivaciones de los arrendatarios de espacios.
    *   *Competidor:* Alternativas actuales de arriendo.
    *   *Proveedor:* Disponibilidad, precio y calidad de los servicios tecnológicos (GCP, Mercado Pago).
    *   *Distribuidor/Canales:* Intermediarios y condiciones.
*   **Etapas Cronológicas de la Evolución del Mercado:**
    1.  Análisis Histórico.
    2.  Análisis de la situación actual con precios de lista diferenciados por categoría; la demanda de EspaciGo aún no está medida.
    3.  Análisis de la Situación Proyectada.
*   **Estrategia Comercial (Tangibilización de la estrategia competitiva):**
    *   *Producto:* Atributos tangibles e intangibles de la plataforma SaaS (EspaciGo).
    *   *Precio:* Determinación de ingresos basados en la demanda, costos (como la pasarela de pagos), competencia y el valor percibido (modelo de comisión, *split* de pagos).
    *   *Promoción y publicidad:* Medios y contenido; la captación de arrendadores y arrendatarios es un gasto distinto de los ingresos por destaque.
    *   *Distribución:* Selección de canales para llegar al usuario (App/Web).

*Nota sobre la Elasticidad de la Demanda:* Considerar cómo cambiará la cantidad demandada de reservas de espacios ante variaciones en la comisión o tarifa de servicio cobrada.

## 2. Análisis del Medio
Variables macroeconómicas y del entorno que influyen en el flujo:
*   **Económicas:** Política fiscal, inflación, UF y tipo de cambio para servicios de nube facturados en USD; se estiman por separado en el Anexo A.
*   **Socioculturales:** Cambios de estilo de vida (tendencia al trabajo remoto, eventos flexibles).
*   **Tecnológicos, Ambientales, Regulatorios y Político-legales:** Aplicación de normativas como la Ley 21.719 que afecta el diseño y potencialmente costos legales y de compliance a partir de diciembre 2026.

## 3. Estudio Técnico
Tiene como objetivo principal proveer la información necesaria para cuantificar el monto de las inversiones y los costos de operación. Es el paso de "lo técnico a lo económico".

**Balances requeridos para el Flujo de Caja:**
*   **Balance de Maquinaria / Tecnología:** Servidores, licencias, infraestructura Cloud (GCP).
*   **Balance de Obras Físicas / Infraestructura:** Espacios de oficina si el equipo lo requiere.
*   **Balance de Personal:** Equipo de desarrollo, soporte, marketing y administración.
*   **Balance de insumos:** Servicios de terceros y API de identidad, pago y firma, sujetos a cotización e integración.

**Interdependencia de los Mercados en el Estudio Técnico:**
*   *Con el Mercado:* La demanda proyectada condiciona el tamaño de la infraestructura tecnológica necesaria (autoescalado en GCP).
*   *Con el Legal:* Las normas legales exigen inversiones en seguridad industrial, privacidad (protección de datos personales) o purificación de recursos.
*   *Con el Organizacional:* Cuantifica las necesidades físicas (oficinas, equipos informáticos) definidas por la estructura.

## 4. Efectos Económicos de los Aspectos Organizacionales (Capítulo 10)
La estructura de la organización define inversiones y costos directos en el flujo.

*   **Externalización (Tercerización):** Puede aumentar la eficiencia operativa y reducir la estructura fija (Ej. usar servicios gestionados en la nube en lugar de servidores propios, o marketing externo).
*   **Internalización:** Aumenta la dotación de personal (remuneraciones) y la inversión en oficinas/equipos, afectando la rentabilidad inicial.
*   **Amortización:** Permite reducir la utilidad contable y el pago de impuestos (como la amortización del desarrollo del software intangible).

**Componentes del Análisis Organizacional:**
1.  *Estudio de la organización:* Criterios analíticos para evaluar las consecuencias económicas.
2.  *Estructura organizacional:* Funciones, producto, mercado, y la tendencia hacia el "clientegrama".
3.  *Efectos económicos de variables:* Cómo la estructura influye en la rentabilidad (inversión inicial vs. costo operativo continuo).
4.  *Grado de participación:* Decisión estratégica sobre qué unidades tercerizar (servicios de pago gestionados vs. desarrollo interno).
5.  *Inversiones Organizacionales:* Necesidades de equipamiento para el equipo base (notebooks, licencias de software de gestión).

## 5. El Modelo de Negocios y las Etapas del Proyecto
El diseño del modelo de negocios debe ser *anterior* a la evaluación económica, siendo su base.

**Características principales del Modelo (Mapa Operativo):**
*   **Creación y Entrega de Propuesta de Valor.**
*   **Orquestación de Nodos:** Define la relación comercial entre los actores (ej. *Hosts*, *Guests*, Banco, Pasarela de Pagos).
*   **Captura de Valor:** Convergencia de los nodos para generar ganancias y eficiencias (nuestro modelo de ingresos).

**Lógica de Reemplazo (si aplica):** Comparar la situación base (arriendos informales/tradicionales) contra la situación con nueva tecnología (EspaciGo).

**Etapas del Proyecto y su impacto en el Flujo de Caja:**
1.  **Preinversión:** (Idea -> Diagnóstico -> Innovación). Perfil, prefactibilidad, factibilidad. Define la estrategia competitiva y el Modelo de Negocios. (*Da forma al flujo de caja*).
2.  **Inversión:** Ejecución y puesta en marcha. Incluye, si corresponden, formalización legal, licencias, capacitación y equipamiento, con desglose vigente en el Anexo A.
3.  **Operación:** Gestión de recursos, generación de ingresos y reinversión constante (retroalimentación y crecimiento).

***
**Siguientes pasos para el Flujo de Caja (Accionables):**
1.  **Ingresos:** Medir demanda, precios finales por categoría y aceptación de la comisión antes de poblar una proyección de ingresos operativos.
2.  **Inversiones (CAPEX):** Considerar constitución legal, desarrollo inicial y equipamiento, distinguiendo desembolsos de trabajo fundador valorizado.
3.  **Costos (OPEX):** 
    *   Infraestructura y nube en la región elegida.
    *   Costos de transacción y terceros sujetos a condiciones de proveedor.
    *   Marketing y publicidad diferenciados de los ingresos por destaque.
    *   Personal y Administrativos (internalización vs externalización).
4.  **Amortizaciones y Depreciaciones:** Calcular la amortización del software (activo intangible) y depreciación de equipos para el beneficio tributario.
5.  **Capital de Trabajo:** Calcular en base al desfase entre pagos de clientes y pagos a *hosts*/proveedores.

## 6. Cuadros Matemáticos para la Construcción del Flujo de Caja (EspaciGo)

A continuación se presenta el **escenario didáctico original** de 3.600 reservas anuales y comisión hipotética del 25 %. Sus valores no proceden de ventas, contratos ni costos observados de EspaciGo. El Anexo A contiene el modelo económico vigente y separa fondos de terceros de ingresos propios.

**Supuestos Básicos aplicados:**
*   **Ticket arriendo base:** $100.000 CLP.
*   **Margen (Comisión EspaciGo):** 25% (Precio Unitario de Ingreso `Pu` = $25.000 CLP).
*   **Reajuste (IPC proyectado):** 4% anual (aplicado a precios y costos).
*   **Costo Variable Unitario (`Cvu`):** $3.000 CLP (Procesamiento $1.200 + Firma $800 + Atención $1.000).

### 1. Cuadro de Ventas (Ingresos de Operación)
Proyección a 3 años considerando la cantidad demandada (`Q`) constante según el supuesto actual, y aplicando el IPC (4%) al precio unitario (`Pu`).

| Año (Ítem) | Cantidad (`Q`) | Precio Unitario (`Pu`) | Total de Ventas (`Q * Pu`) |
| :--- | :--- | :--- | :--- |
| 1 | 3.600 | $ 25.000 | **$ 90.000.000** |
| 2 | 3.600 | $ 26.000 | **$ 93.600.000** |
| 3 | 3.600 | $ 27.040 | **$ 97.344.000** |

### 2. Cuadro de Costo de Ventas (Costos Variables)
Se aplica el factor de incremento por inflación (4%) sobre los costos variables unitarios.

| Año (Ítem) | Cantidad (`Q`) | Costo Variable Unitario (`Cvu`) | Costo Venta Total (`Q * Cvu`) |
| :--- | :--- | :--- | :--- |
| 1 | 3.600 | $ 3.000 | **$ 10.800.000** |
| 2 | 3.600 | $ 3.120 | **$ 11.232.000** |
| 3 | 3.600 | $ 3.245 | **$ 11.681.280** |

### 3. Cuadro de Costos Fijos
Suma de mantención, administración, servicios cloud, difusión y otros externos base (Año 1 = $18.000.000), ajustado anualmente por IPC (4%).

| Año (Ítem) | Costos Fijos (OPEX Total) |
| :--- | :--- |
| 1 | **$ 18.000.000** |
| 2 | **$ 18.720.000** |
| 3 | **$ 19.468.800** |

### 4. Inversión Inicial y Depreciación / Amortización
En este ejercicio histórico se suponía:
*   Desarrollo valorizado (costo de oportunidad): $ 14.400.000
*   Preparación y lanzamiento (efectivo): $ 1.200.000
*   **Total Inversión Inicial:** **$ 15.600.000**

**Depreciación / Amortización (Ejemplo Teórico Lineal):**
Aunque este ejercicio preliminar marcaba `0` para simplificar, una amortización teórica del supuesto desarrollo de software de 14,4 millones de CLP a tres años sería:
*   `Amortización Lineal = (Inversión Intangible - Valor Residual) / Vida Útil`
*   `Amortización Lineal = (14.400.000 - 0) / 3` = **$ 4.800.000 por año.** *(Este valor iría antes de impuestos para reducir la base tributaria)*.

### 5. Financiamiento y Cuadro de Amortización de Deuda (Escenario de Apalancamiento)
Suponiendo un escenario donde el **50% de la inversión se financia con deuda** ($7.800.000) a una tasa de interés referencial del 11% (`i = 0,11`) a 3 años (`n = 3`).

**Cálculo de la Cuota Fija (R):**
*   $R = \text{Capital Absoluto} \times \frac{i(1+i)^n}{(1+i)^n - 1}$
*   $R = 7.800.000 \times \frac{0,11(1,11)^3}{(1,11)^3 - 1} = 7.800.000 \times 0,409213 = $ **$ 3.191.862**

**Cuadro de Amortización:**

| Período | Saldo Inicial (Cap. Absoluto) | Amortización | Interés (11%) | Pago (Cuota `R`) |
| :--- | :--- | :--- | :--- | :--- |
| 0 | $ 7.800.000 | - | - | - |
| 1 | $ 7.800.000 | $ 2.333.862 | $ 858.000 | **$ 3.191.862** |
| 2 | $ 5.466.138 | $ 2.590.587 | $ 601.275 | **$ 3.191.862** |
| 3 | $ 2.875.551 | $ 2.875.551 | $ 316.311 | **$ 3.191.862** |

### 6. Tasa de Descuento (WACC / $K_o$)
Para traer los flujos a valor presente, el modelo asume una **tasa de descuento nominal (`tasa_descuento_nominal`) del 12% ($K_o = 0,12$)** y un impuesto (`tc`) del 27%.

La lógica de cálculo del costo de capital (según los apuntes) es:
$K_o = K_d \cdot \frac{D}{D+C} \cdot (1 - t_c) + K_e \cdot \frac{C}{D+C}$

*Donde:*
*   $K_d$: Costo de la deuda (ej. 11%).
*   $t_c$: Tasa de impuesto (27% o 0,27).
*   $K_e$: Costo de capital propio (calculado vía CAPM: $R_f + \beta(R_m - R_f)$).
*   $D, C$: Proporción de Deuda y Capital Propio.

***

## 7. Flujo de Caja Final (Del Inversionista / Financiado)

A partir de los cuadros anteriores, estructuramos el flujo de caja final considerando la inversión apalancada al 50%. Se asume una inversión en Capital de Trabajo correspondiente a 1 mes de costos operativos (Aprox. $2.400.000 CLP).

| Ítem / Período | Año 0 | Año 1 | Año 2 | Año 3 |
| :--- | :--- | :--- | :--- | :--- |
| **Ingresos por Ventas** | | $ 90.000.000 | $ 93.600.000 | $ 97.344.000 |
| (-) Costos Variables | | -$ 10.800.000 | -$ 11.232.000 | -$ 11.681.280 |
| **= Margen de Contribución** | | **$ 79.200.000** | **$ 82.368.000** | **$ 85.662.720** |
| (-) Costos Fijos | | -$ 18.000.000 | -$ 18.720.000 | -$ 19.468.800 |
| (-) Depreciación / Amortización Intangible | | -$ 4.800.000 | -$ 4.800.000 | -$ 4.800.000 |
| (-) Gastos Financieros (Interés del Préstamo) | | -$ 858.000 | -$ 601.275 | -$ 316.311 |
| **= Utilidad Antes de Impuestos (UAI)** | | **$ 55.542.000** | **$ 58.246.725** | **$ 61.077.609** |
| (-) Impuestos (27%) | | -$ 14.996.340 | -$ 15.726.616 | -$ 16.490.954 |
| **= Utilidad Después de Impuestos (UDI)** | | **$ 40.545.660** | **$ 42.520.109** | **$ 44.586.655** |
| | | | | |
| **Ajustes y Flujos No Operacionales:** | | | | |
| (+) Depreciación / Amortización Intangible | | +$ 4.800.000 | +$ 4.800.000 | +$ 4.800.000 |
| (-) Inversión Inicial (Activos e Intangibles) | -$ 15.600.000 | | | |
| (+) Préstamo (Financiamiento 50%) | +$ 7.800.000 | | | |
| (-) Amortización de Deuda (Capital) | | -$ 2.333.862 | -$ 2.590.587 | -$ 2.875.551 |
| (-) Inversión en Capital de Trabajo | -$ 2.400.000 | | | |
| (+) Recuperación de Capital de Trabajo | | | | +$ 2.400.000 |
| | | | | |
| **= FLUJO DE CAJA NETO DEL INVERSIONISTA** | **-$ 10.200.000** | **$ 43.011.798** | **$ 44.729.522** | **$ 48.911.104** |

*(Nota: Este flujo proyectado refleja el escenario supuesto de 3.600 reservas anuales. Se consideró la recuperación total del capital de trabajo al finalizar el año 3).*

***

### 8. Indicadores de Rentabilidad (Evaluación Económica)

Para determinar si el proyecto es viable desde el punto de vista del inversionista, calculamos el **Valor Actual Neto (VAN)** utilizando la tasa de descuento nominal del **12%** ($K_o = 0,12$) extraída de los supuestos del proyecto.

**Fórmula del VAN:**
$VAN = \sum \frac{FC_t}{(1 + k)^t} - I_0$

**Cálculo:**
*   $VAN = -10.200.000 + \frac{43.011.798}{(1,12)^1} + \frac{44.729.522}{(1,12)^2} + \frac{48.911.104}{(1,12)^3}$
*   $VAN = -10.200.000 + 38.403.391 + 35.658.101 + 34.814.168$
*   **VAN = $ 98.675.660 CLP**

**Conclusión Financiera (Ejemplo):**
Dado que el **VAN > 0** en este ejercicio hipotético de 3.600 reservas anuales y comisión del 25 %, el cálculo aislado muestra valor presente positivo **solo bajo esos supuestos**. No constituye evidencia de viabilidad de EspaciGo: el escenario oficial posterior del Anexo A usa 3 % neto, no acredita esa demanda y obtiene VAN negativo. La TIR superior al 400 % atribuida al ejercicio anterior tampoco se traslada al escenario vigente.
