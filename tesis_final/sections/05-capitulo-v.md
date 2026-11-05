# CAPÍTULO V: Objetivos del Proyecto

## 5. Objetivos del Proyecto

### 5.1. Solución Tecnológica

#### 5.1.1. Formulación de la solución

espaciGo integra el catálogo, la disponibilidad, la contratación y la entrega en un recorrido trazable. El diseño separa los cambios de estado de los efectos externos y registra evidencia de cada etapa.

#### 5.1.2. Alcance y restricciones

El diseño objetivo contempla arriendo de espacios residenciales, turísticos, recreativos, comerciales e industriales. Las unidades de tarifa del corte son hora, día y mes. Un bloque puntual conserva el horario y el precio acordados. La publicación exige titularidad y cumplimiento de las reglas del anuncio. La emisión exige identidad verificada de ambas partes y acreditación de representación cuando corresponde. Cada participante acepta la emisión identificada y, si ambas partes eligen SimpleFirma, el flujo acredita aportes y firmas antes de habilitar la renta.

La regla de diseño condiciona la confirmación de la reserva a la acreditación de los cobros exigibles. La habilitación de garantía requiere verificación separada. Tras la entrega, el titular confirma desocupación, libera el bloqueo correspondiente y puede republicar. La recurrencia, la subdivisión, el aforo compartido y la validación de firmas externas permanecen diferidos según el ADR.

### 5.2. Impacto de la solución

#### 5.2.1. Proceso de negocio afectado

El recorrido interviene desde la búsqueda y la comprobación de disponibilidad hasta el acuerdo, la ocupación y la entrega. La medición del impacto comercial requiere contrastar los indicadores con una línea base por segmento.

#### 5.2.2. Registro de interesados

Las personas y organizaciones arrendadoras publican y gestionan la disponibilidad. Las arrendatarias buscan, contratan y registran la entrega. La administración gestiona controles e incidencias. El equipo de titulación mantiene el diseño y la evidencia. Los proveedores de pagos y firma intervienen según el corte de habilitación.

#### 5.2.3. Indicadores de gestión

La evaluación comercial puede medir conversión de búsqueda a reserva, tiempo entre publicación y primera reserva, proporción de incidencias resueltas y satisfacción posterior al arriendo. Cada medición define población, período y denominador antes de asignar metas.

La evaluación técnica registra volumen de solicitudes, latencia P95 por operación, errores de integración y cobertura. El reporte diferencia pruebas sintéticas, observación de un entorno de ensayo y medición de operación.

#### 5.2.4. Niveles de servicio

Los objetivos de respuesta, disponibilidad y recuperación se especifican en el Capítulo XI. Su comprobación depende del escenario y entorno descritos en el plan de pruebas.

### 5.3. Objetivos del proyecto

#### 5.3.1. Objetivo general

Diseñar y desarrollar una plataforma de intermediación para el arriendo flexible de espacios ofrecidos por personas y organizaciones para distintos usos y verificar, mediante un prototipo, el control de disponibilidad y la trazabilidad de la contratación.

#### 5.3.2. Objetivos específicos

1. **OE1. Diagnóstico y requisitos.** Caracterizar las dificultades de intermediación y especificar los requisitos mediante historias y casos de uso para definir el alcance funcional de la plataforma.
2. **OE2. Arquitectura y datos.** Diseñar las vistas de negocio, aplicaciones, datos e infraestructura y modelar la ocupación para preservar la disponibilidad de cada unidad reservable.
3. **OE3. Construcción e integración.** Implementar un recorrido transaccional con datos sintéticos y especificar los contratos de integración para verificar la coordinación entre módulos y establecer las condiciones de habilitación de proveedores.
4. **OE4. Calidad.** Aplicar pruebas de dominio, integración y recorrido y definir criterios medibles de carga y recuperación para evaluar la calidad del prototipo y orientar la validación del entorno objetivo.
5. **OE5. Operación y factibilidad.** Formular una estrategia de despliegue, seguridad y continuidad, e incorporar criterios de evaluación económica para estimar la viabilidad operativa del servicio.

OE1 se desarrolla en II y III y en los anexos A–C. OE2 se documenta en VII, VIII y X y en el Anexo D. OE3 se contrasta con X, XII y el Anexo E. OE4 remite a XII y al Anexo F. OE5 se desarrolla en XIII y XIV y en el Anexo H.

### 5.4. Modelo de negocio

El lienzo sintetiza las hipótesis de intermediación y las dependencias del servicio. Su comprobación comercial requiere mediciones separadas del ensayo técnico.

**Tabla 4**\
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
| Costos | Infraestructura, integraciones y operación. El análisis detallado se integra en los apartados reservados del Capítulo XIV y el Anexo H. |

*Nota.* Elaboración propia. El lienzo describe el modelo propuesto para evaluación.
