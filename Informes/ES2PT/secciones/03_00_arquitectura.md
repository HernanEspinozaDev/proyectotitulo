# Detalle de la arquitectura a implementar

La arquitectura se desarrollará a partir de los módulos, requisitos y flujos definidos en ES1. Las vistas de procesos, casos de uso, componentes, datos e infraestructura deberán describir un mismo alcance y conservar los identificadores de la base.

## Decisiones consolidadas

*Tabla. Decisiones técnicas de ES2 y su estado.* <!--#tab:es2-decisiones-arquitectura-->

| Decisión | Origen | Estado | Dónde se detalla |
| --- | --- | --- | --- |
| Backend modular Go como unidad desplegable | ES1, conservada | Vigente | 3.3 |
| PostgreSQL/PostGIS como persistencia operativa | RNF-038 de ES1 | Vigente | 3.4, 3.6 |
| Cloud Run para los contenedores web y API | Propuesta de ES1 | Condicionada a costo y portabilidad | 3.6; Anexo A |
| Región southamerica-west1 (Santiago) para datos y ejecución | Decisión del usuario del 23-09-2026 | Vigente: tarifas publicadas aplicadas al presupuesto; +40 % en cómputo, base y Cloud Run, y +90 % en almacenamiento respecto de Iowa | 3.6; Anexo A |
| Calendario común `ocupacion` con intervalos semiabiertos | Decisión nueva de ES2 | Propuesta; requiere DDL aplicado y prueba concurrente | 3.4; Anexo B |
| Separar la analítica de la garantía de inmutabilidad de RNF-017 | Decisión nueva de ES2 | Propuesta (SUP-13): retención bloqueada con hash por lote; sin ensayo de alteración ejecutado | 3.3, 3.6 |
| Ley 21.719 como criterio de diseño desde el primer incremento | Decisión del usuario | Vigente; sin cumplimiento probado | Anexo B; PT-16 |
| Destaques pagados dentro de la plataforma | Propuesta nueva de ES2 | No aprobada; fuera del alcance técnico actual | 3.3 |
| Pago con reparto, firma electrónica y verificación de identidad por API | Propuesta de ES1 | Abierta; sin contrato ni cotización de API | 3.5; 2.2 |

## Coherencia entre las vistas

*Tabla. Correspondencia de elementos entre las vistas.* <!--#tab:es2-coherencia-vistas-->

| Elemento | Vistas donde aparece | Observación |
| --- | --- | --- |
| Módulos M01–M11 | 3.1, 3.2, 3.3, 3.7 | Se conservan los mismos identificadores; no se crean módulos nuevos |
| Componentes de software | 3.3, 3.5, 3.7 | Web, API modular, adaptadores y conciliación se nombran igual en las tres vistas |
| Entidades y calendario | 3.4, 3.5, 3.7 | La ocupación y las operaciones financieras del Anexo B sustentan los flujos descritos |
| Canales y webhooks | 3.5, 3.7 | El webhook se trata como evento asincrónico, no como respuesta de pago |
| Recursos de ejecución | 3.6, 3.7 | Los perfiles presupuestarios no son recursos desplegados |
| Proveedores externos | 3.2, 3.3, 3.5, 3.7 | Pago, firma e identidad siguen sin acceso ni contrato confirmado |
| Presupuesto de infraestructura | 3.6 | Tarifas de Santiago aplicadas al Anexo A por decisión del usuario; el ejercicio de Iowa se conserva solo como control documental |

Las vistas describen un mismo alcance, pero ninguna acredita despliegue, integración aprobada ni resultado de pruebas. Las diferencias anteriores se resuelven en el cierre del contenido, no modificando ES1.

## Mecanismo propuesto para la inmutabilidad de RNF-017

La documentación de BigQuery admite operaciones `UPDATE` y `DELETE`, de modo que conservarlo como repositorio analítico no satisface por sí solo el requisito de inmutabilidad. La propuesta de trabajo (SUP-13) separa las dos funciones: BigQuery se mantiene para consulta y análisis, y la garantía se apoya en **Cloud Storage con una política de retención bloqueada** más un **hash por lote de eventos**. La documentación del proveedor indica que una política bloqueada impide reducir o quitar la retención y borrar o reemplazar objetos antes del plazo, y que el bloqueo es **irreversible**; por eso el plazo productivo no se fija aquí y debe acordarse con la política de conservación de la matriz de tratamiento del Anexo B [@es2bucketlock; @es2bigquerydml].

El ensayo previsto es acotado y explícito: exportar eventos sintéticos mínimos, aplicar la retención bloqueada por siete días e intentar alterar o borrar un objeto para comprobar el fallo esperado. **No se ha ejecutado**, no se ha contratado el servicio y el plazo definitivo sigue abierto; por lo tanto, RNF-017 no se declara cumplido. El **acceso a los proveedores de pago, firma e identidad** es un asunto distinto, depende de terceros y se registra en la sección correspondiente de [pendientes](../pendientes.md).

