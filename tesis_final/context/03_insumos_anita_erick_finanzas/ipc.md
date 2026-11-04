# Ajustes Económicos: IPC y Tipo de Cambio

En la formulación y evaluación económica del proyecto **EspaciGo**, es fundamental homogeneizar los valores monetarios para asegurar que el flujo de caja refleje correctamente el valor del dinero en el tiempo y el costo real de los insumos internacionales. Tomando como referencia las herramientas de cálculo del INE y de conversión de divisas, se definen los siguientes criterios:

## 1. Reajustabilidad por Inflación (Calculadora IPC)

Para actualizar costos históricos, tarifas de referencia o proyecciones de precios, se aplica la tasa de variación del Índice de Precios al Consumidor (IPC) entregada por el Instituto Nacional de Estadísticas (INE).

**Aplicación en EspaciGo:**
*   **Periodo de Cálculo (Inicio - Término):** Desde la fecha en que se cotizó el insumo o se registró el antecedente hasta el periodo base de evaluación del proyecto (ej. 2026).
*   **Valor a Ajustar:** Costos operativos locales, sueldos base, o tarifas de arrendamiento de espacios de competidores pasados.
*   **Valor Ajustado:** El monto reajustado en pesos chilenos (CLP) que ingresará a los cuadros de inversión y egresos de operación, garantizando que el análisis financiero considere el poder adquisitivo actual (ej. aplicando un 45,2% de variación acumulada para el periodo 2020-2026).

*Nota metodológica: Los resultados deben ser calculados con precisión (ej. series empalmadas del INE) para evitar distorsiones en el Valor Actual Neto (VAN) y la Tasa Interna de Retorno (TIR).*

## 2. Tipo de Cambio (Dólar a Peso)

El modelo tecnológico de EspaciGo (SaaS) depende de proveedores internacionales cuyos servicios se cobran en dólares (por ejemplo, infraestructura cloud, pasarelas y otros servicios API). 

**Aplicación en EspaciGo:**
*   **Conversión:** Se debe establecer un tipo de cambio referencial (Dólar observado, ej. $972 CLP/USD) para convertir los egresos mensuales en USD a CLP en nuestro flujo de caja.
*   **Sensibilidad:** Dado que el valor del dólar es fluctuante, el modelo económico del proyecto debe contemplar la paridad cambiaria vigente al momento de la estimación de los flujos para reflejar de forma exacta el costo de la tecnología en pesos.

---
**Fuente de los conceptos:** Basado en la metodología de la Calculadora IPC del INE y plataformas de conversión de divisas.
