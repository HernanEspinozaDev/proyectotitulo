# CAPÍTULO IV: OBJETIVOS DEL PROYECTO Y MODELO DE NEGOCIO

## 4.1. Objetivo general

Diseñar y desarrollar una plataforma de intermediación para el arriendo flexible de espacios ofrecidos por personas y organizaciones para distintos usos y verificar, mediante un prototipo, el control de disponibilidad y la trazabilidad de la contratación.

## 4.2. Objetivos específicos

1. **OE1. Diagnóstico y requisitos.** Caracterizar el problema y especificar los requisitos, historias y casos de uso. El resultado se identifica en los capítulos II y VII y en los anexos A, B y C.
2. **OE2. Arquitectura y datos.** Diseñar las vistas de negocio, aplicaciones, datos e infraestructura y especificar el control de ocupación. El resultado se documenta en los capítulos VI a IX y el Anexo D.
3. **OE3. Construcción e integración.** Implementar un recorrido transaccional con datos sintéticos y documentar los contratos de integración y los criterios de habilitación de proveedores. El resultado se contrasta con los capítulos VIII a X y el Anexo E.
4. **OE4. Calidad.** Definir y aplicar pruebas de dominio, integración y recorrido, y establecer criterios medibles de carga y recuperación. El Capítulo X y el Anexo F distinguen evidencia obtenida y pruebas objetivo.
5. **OE5. Operación y factibilidad.** Formular la estrategia de despliegue, seguridad y continuidad, y considerar la evaluación económica en los apartados correspondientes.

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

La plataforma confirma la reserva al acreditar los cobros exigibles. La garantía se habilita por separado cuando se verifica su operación. Tras la entrega, el titular confirma desocupación, libera el bloqueo correspondiente y puede republicar. La recurrencia, la subdivisión, el aforo compartido y la validación de firmas externas permanecen diferidos según el ADR.
