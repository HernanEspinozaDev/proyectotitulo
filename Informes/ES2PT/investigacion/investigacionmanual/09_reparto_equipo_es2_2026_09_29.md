# Reparto propuesto del trabajo ES2: código local e informe

**Corte:** 29-09-2026. **Fecha de entrega informada:** 03-11-2026. Esta hoja traduce la [auditoría de los 17 criterios](08_auditoria_avance_es2_2026_09_29.md) en encargos revisables. El usuario asumirá backend y base de datos; «Shiva» y «Tajamon» son los nombres usados por el usuario para los dos frentes de informe. **Las fechas son objetivos propuestos, no hitos académicos confirmados.** Horas disponibles, nombres oficiales y aceptación de cada encargo se registrarán en reunión; aquí no se afirma que terceros hayan aceptado tareas ni que se les haya contactado.

## Primero: acuerdo del equipo

En una reunión breve, registrar una persona responsable y otra revisora por entregable, horas semanales hasta el 3 de noviembre y fecha de revisión. Resolver juntos:

1. **Evidencia ejecutable para ES2:** enumerar el recorrido que se podrá mostrar y el estado real de cada función. El producto diseñado incluye todas las categorías y el flujo completo; una implementación incremental no cambia ese alcance.
2. **D-07/D-08:** plazos y fundamentos por clase de dato; plazo de retención bloqueada solo después de revisión jurídica y antes de aplicar Bucket Lock irreversible. Ley 21.719 guía el primer incremento; PT-16 verificará el comportamiento.
3. **D-03/D-04/D-05:** actas sobre cuatro BPMN, siete vistas CU, estados de reserva e interfaces; dejar observaciones y decisión, sin llamar «aprobado» a un diagrama por estar dibujado.
4. **D-09/D-10/D-14/D-15:** aportes, giro sujeto a contador, destaque comercial, horario/zona de SLA y ventana de mantención. El código **TIH184** ya está resuelto; faltan sección, académico y fechas formativas por contrastar.
5. **Control de archivos:** cada responsable trabaja su fuente; otra persona revisa antes de integrar. El Word de lectura es una fotografía del borrador, no un documento final aprobado.

## Frente 1 — Usuario: backend y base de datos en local

| ID y prioridad | Entregable concreto | Evidencia de aceptación | Dependencia |
| --- | --- | --- | --- |
| **H-01, inmediata** | Entorno local reproducible con Go, PostgreSQL 18/PostGIS 3.6, variables de ejemplo sin secretos, migrador y guía de arranque; inventario real de versiones. | Desde un clon limpio se inicia el entorno y se registra versión/esquema sin credenciales en Git. | [Contrato backend](base_de_datos/17_contrato_datos_backend.md), Anexo B. |
| **H-02, inmediata** | Migraciones **incrementales** del núcleo de identidad, catálogo/categoría/tarifa, espacio, ocupación, cotización y reserva. Las 43 tablas siguen como contrato de diseño del producto; no es necesario crear tablas vacías sin caso de uso implementado. | Migración ascendente reproducible, claves/restricciones verificables y traza de versión app/esquema. | H-01; reglas de tiempo, moneda y estados del Anexo B. |
| **H-03, alta** | Casos de uso Go de publicación, búsqueda, disponibilidad y reserva con exclusión de solapes, transiciones autorizadas y snapshot de precio/comisión. | API/CLI local con datos sintéticos y evidencia fechada del camino feliz y de conflictos concurrentes; MD pertinentes. | H-02; acta D-04 de estados. |
| **H-04, alta** | Workers internos durables para expiración, inbox de webhook y Outbox, con lease/fencing, reintentos e idempotencia. | Reinicio/duplicado ensayado localmente; evento no se pierde ni se aplica dos veces; MD-13. | H-02/H-03. |
| **H-05, condicionada** | Adaptador de pagos que mantenga separados arriendo, comisión 3 % neta, IVA, tarifa del proveedor, garantía y neto observado. Integración Mercado Pago **solo en sandbox** cuando la cuenta y condiciones estén confirmadas. | Casos de cobro, reparto y reembolso conciliados con reportes/documentos; si faltan accesos, simulador explícito sin afirmar integración real. | Respuestas de Mercado Pago y contador. |
| **H-06, progresiva** | Ejecutar **MD-01–MD-13** y los PT que correspondan al código construido; entregar a Tajamon resultados para 5.1, 3.4 y Anexo C. | Matriz con fecha, commit, entorno, entrada, esperado/observado, fallo y corrección. Lo no ejecutado permanece planificado. | H-02–H-05. |

**Secuencia de inicio local:** H-01 → H-02 → H-03 → H-04. No esperar a Cloud SQL ni a credenciales de terceros para desarrollar transacciones locales con datos sintéticos. El despliegue GCP, las garantías financieras y las políticas irreversibles siguen como trabajos separados con sus pruebas y decisiones.

## Frente 2 — Shiva: estudio económico, mercado y terceros

| ID y prioridad | Entregable concreto | Evidencia de aceptación | Secciones que actualizaría |
| --- | --- | --- | --- |
| **S-01, inmediata** | Nota de conciliación de su [estudio preliminar](../../flujodecaja/estudios.md) con el caso oficial: 25 %/3.600 reservas y VAN positivo **históricos** frente a 3 %/0–720–1.800 y VAN negativo. Conservar autoría y método; no convertir la hipótesis antigua en resultado actual. | Tabla de diferencias y una síntesis que pueda insertarse en 2.1/Anexo A sin duplicar ingresos de terceros. | 2.1, Anexo A, aporte de Shiva. |
| **S-02, alta** | Fichas y entrevistas de oferta/demanda por `categoría × modalidad × comuna`: precio final, duración, capacidad, disponibilidad, rechazos, conversión y aceptación de comisión. | Muestra con fecha, fuente/consentimiento, tamaño y limitaciones; ningún contacto o intención contado como reserva pagada. | 2.1, Anexo A, `INV-011`/protocolo `INV-016`. |
| **S-03, alta** | Preparar y cursar, cuando el equipo lo acuerde, consultas al contador/SII, Mercado Pago, FirmaVirtual/KYC, Oficina Express y municipio con las preguntas ya reunidas en `INV-026`/`INV-027`. | Respuesta, contrato o cotización fechada; si no llega, registrar envío, plazo y efecto del bloqueo. Sin credenciales en el informe. | 2.1–2.2, 3.5, Anexo A/B. |
| **S-04, alta** | Recalcular `supuestos_bootstrap.json` y el escenario por categorías **solo** con datos respaldados; distinguir comisión propia, fondos de terceros, IVA, efectivo y oportunidad. | Salidas reproducibles, tabla «supuesto anterior → evidencia → nuevo valor», comparación de VAN/caja y revisión aritmética cruzada. | Anexo A, 2.1, conclusiones. |
| **S-05, media** | Completar costos de proveedores y nube por SKU comparable en Santiago, GCP con API mínima y escenario de operación realista; pedir facturas/condiciones antes de llamarlas costos observados. | Cuadro con unidad, región, fuente, fecha y exclusiones; separar cotización de provisión. | 2.1, 3.6, Anexo A. |

## Frente 3 — Tajamon: integración académica y calidad del informe

| ID y prioridad | Entregable concreto | Evidencia de aceptación | Secciones que actualizaría |
| --- | --- | --- | --- |
| **T-01, inmediata** | Mantener la matriz de **17 criterios**, el tablero de **13 marcadores** y una lista de decisiones/consultas con responsable y fecha. Revisar TIH184 en portada y contrastar los metadatos restantes. | Cada criterio apunta a sección/figura/anexo y evidencia; no se retira un marcador sin soporte. | Matriz, pendientes, VII y metadatos. |
| **T-02, alta** | Revisión de cuatro BPMN, siete vistas CU y diagramas de componentes con el usuario: mensajes, temporizadores, estados y casos sin vista. | Acta con versión de cada diagrama, observaciones, corrección y aprobación real del equipo. | 3.1–3.3 y figuras. |
| **T-03, alta** | Completar capítulo V como plan y registro de ejecución: **PT-01–PT-16**, MD-01–MD-13, PT-16 de privacidad y norma aplicable desde diseño. Incorporar resultados entregados por el usuario sin inventarlos. | Por caso: estado planificado/ejecutado, fecha, entorno, commit, datos, esperado/observado y conclusión. | 5.1–5.2, Anexo C, 3.4. |
| **T-04, alta** | Revisar las once fichas KPI, cinco SLA y capítulos VI: responsables, fuentes de medición, ventana, monitoreo, continuidad y control de cambios. | Registro de mediciones vacío donde no haya producto; acuerdo de ventana y acta de simulacro cuando existan. | IV y VI. |
| **T-05, alta** | Coordinar con el equipo la matriz de tratamiento y política de conservación por finalidad: datos de identidad, KYC, contratos, pagos, documentos, logs y analítica; no fijar un plazo universal ni activar retención bloqueada sin acuerdo. | Acta y revisión legal/contable donde corresponda; plan PT-16 y riesgos de restauración. | 3.4, 5.2, Anexo B. |
| **T-06, final** | Integrar cambios de Shiva y usuario, actualizar VII/conclusiones, revisar citas primarias, bibliografía, tablas/figuras, portada TIH184 y Word/anexos. Solicitar revisión docente. | Registro visual y de contenido de la nueva salida, matriz actualizada y comentarios del docente **solo si se reciben**. | Todo ES2; Word final al cierre. |

## Hitos de coordinación sugeridos

| Fecha objetivo | Evidencia mínima que se revisa |
| --- | --- |
| **02-10** | Horas/roles acordados; H-01 inicia; TIH184 en portada; Shiva entrega S-01 y Tajamon tablero T-01. |
| **06-10** | H-02 y primeras migraciones; consultas S-03 enviadas o bloqueo registrado; actas preliminares T-02. |
| **13-10** | H-03/H-04 en progreso, MD iniciales; muestra S-02 con limitaciones; T-03/T-05 integran diseño y resultados disponibles. |
| **20-10** | Corte de código demostrable y PT realmente ejecutados; versión económica recalculada solo si hay evidencia; KPI/SLA con estado honesto. |
| **27-10** | Revisión cruzada de los 17 criterios, 13 marcadores y cronograma ajustado; borrador enviado a docente si el equipo lo acuerda. |
| **02-11** | Word y anexos de entrega revisados página a página, índices y fuentes; riesgos pendientes explícitos. |

**Regla de integración:** una tarea se cierra por evidencia, no por porcentaje declarado. Si una respuesta externa no llega, escribir «sin respuesta» y el efecto técnico/económico; si un PT no se ejecuta, mantenerlo «planificado». El informe puede presentar un diseño completo junto a una implementación parcial siempre que sus estados se distingan con claridad.
