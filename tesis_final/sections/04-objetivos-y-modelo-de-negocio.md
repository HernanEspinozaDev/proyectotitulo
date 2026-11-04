# CAPÍTULO IV: OBJETIVOS DEL PROYECTO Y MODELO DE NEGOCIO

## 4.1. Objetivo general

Diseñar y desarrollar una plataforma de intermediación para el arriendo flexible de espacios ofrecidos por personas y organizaciones para distintos usos y verificar, mediante un prototipo, el control de disponibilidad y la trazabilidad de la contratación.

## 4.2. Objetivos específicos

1. **OE1. Diagnóstico y requisitos.** Caracterizar las dificultades de intermediación y especificar los requisitos mediante historias y casos de uso para definir el alcance funcional de la plataforma.
2. **OE2. Arquitectura y datos.** Diseñar las vistas de negocio, aplicaciones, datos e infraestructura y modelar la ocupación para preservar la disponibilidad de cada unidad reservable.
3. **OE3. Construcción e integración.** Implementar un recorrido transaccional con datos sintéticos y especificar los contratos de integración para verificar la coordinación entre módulos y establecer las condiciones de habilitación de proveedores.
4. **OE4. Calidad.** Aplicar pruebas de dominio, integración y recorrido y definir criterios medibles de carga y recuperación para evaluar la calidad del prototipo y orientar la validación del entorno objetivo.
5. **OE5. Operación y factibilidad.** Formular una estrategia de despliegue, seguridad y continuidad, e incorporar criterios de evaluación económica para estimar la viabilidad operativa del servicio.

La trazabilidad de OE1 se documenta en los capítulos II y VII y los anexos A–C. Las vistas y el modelo de OE2 se desarrollan en los capítulos VI a IX y el Anexo D. La construcción y los contratos de OE3 se documentan en los capítulos VIII a X y el Anexo E. El Capítulo X y el Anexo F reúnen la evidencia y los criterios de OE4. Para OE5, el Capítulo XI presenta la estrategia de operación y el Capítulo XII y el Anexo H reservan la evaluación económica.

## 4.3. Modelo de negocio

El lienzo sintetiza las hipótesis de intermediación y las dependencias del servicio. Su comprobación comercial requiere mediciones separadas del ensayo técnico.

**Tabla 2**\
*Lienzo del modelo de negocio de espaciGo*

| Bloque | Hipótesis de diseño |
|---|---|
| Propuesta de valor | Consultar oferta y disponibilidad, conservar el acuerdo y coordinar la entrega. |
| Segmentos | Personas y organizaciones que ofrecen o requieren espacios para alojamiento, recreación, comercio, industria u otros usos contemplados. |
| Canales | Aplicación web y publicación de espacios por su titular. |
| Relación | Autoservicio y soporte para incidencias y conciliación. |
| Ingresos | Comisión de intermediación como hipótesis del modelo. |
| Recursos | Plataforma web, registro de ocupación y evidencias privadas. |
| Actividades | Mantener el catálogo y coordinar contratación, cobros y operación. |
| Socios | Proveedores de pagos y firma sujetos a validación de integración. |
| Costos | Infraestructura, integraciones y operación. El análisis detallado se integra en los apartados reservados del Capítulo XII y el Anexo H. |

*Nota.* Elaboración propia. El lienzo describe el modelo propuesto para evaluación.

## 4.4. Alcance y condiciones de servicio objetivo

El diseño objetivo contempla arriendo de espacios residenciales, turísticos, recreativos, comerciales e industriales. Las unidades de tarifa del corte son hora, día y mes. Un bloque puntual conserva el horario y el precio acordados. La publicación exige titularidad y cumplimiento de las reglas del anuncio. La emisión exige identidad verificada de ambas partes y acreditación de representación cuando corresponde. Cada participante acepta la emisión identificada y, si ambas partes eligen SimpleFirma, el flujo acredita aportes y firmas antes de habilitar la renta.

La regla de diseño condiciona la confirmación de la reserva a la acreditación de los cobros exigibles. La habilitación de garantía requiere verificación separada. Tras la entrega, el titular confirma desocupación, libera el bloqueo correspondiente y puede republicar. La recurrencia, la subdivisión, el aforo compartido y la validación de firmas externas permanecen diferidos según el ADR.
