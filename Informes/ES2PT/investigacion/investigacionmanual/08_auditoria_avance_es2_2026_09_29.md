# Auditoría de avance ES2 frente a la rúbrica y al resumen anterior

**Corte:** 29-09-2026. **Entrega informada por el usuario:** 03-11-2026. **Alcance de esta auditoría:** fuentes Markdown y configuración ES2, [rúbrica incorporada](../../plantilla/rubrica_de_calificacion.md), [matriz de trazabilidad](../matriz_trazabilidad_es2.md), [pendientes](../../pendientes.md), [Anexos A–C](../../informe.json) y [aporte de Shiva](../../flujodecaja/estudios.md). El estado de implementación procede de la evidencia registrada en el repositorio: todavía no constan migraciones aplicadas, producto desplegado ni resultados MD/PT. **No se asigna puntaje ni aprobación docente** a partir de la presencia de texto.

## Qué cambió frente al resumen de 14 pendientes

| Tema | Resumen anterior | Estado comprobado en este corte |
| --- | --- | --- |
| Código de asignatura | TIH184 o TIHI84 por decidir | El usuario confirmó **TIH184**; `informe.json` lo incorpora. La grafía TIHI84 queda en el nombre y texto histórico de la guía/plantilla. Sección, académico y calendario aún requieren contraste. |
| Marcadores del cuerpo y anexos | 14 | **13**: diez en secciones, uno en el Anexo A y dos en el B. El mapa antiguo de [06](06_mapa_de_marcadores.md) es histórico. Hay además un marcador en `contexto.md`, fuera de los archivos configurados como cuerpo/anexos. |
| Base de datos | Núcleo parcial y MD-01–MD-12 | [Anexo B](../../anexos/B_diccionario_datos.md) con **43 tablas de diseño**, matriz de tratamiento y **MD-01–MD-13**. Faltan migraciones aplicadas y resultados. |
| Backend | Propuesta previa con demostración acotada | [Propuesta oficial](../propuesta_backend_final.md) y capítulos III: producto completo, todas las categorías, monolito modular Go, workers internos y Outbox. Falta código ejecutable y evidencia de integración. |
| Evaluación económica | Modelos preliminares de 25 % y luego 12 % de comisión | [Anexo A](../../anexos/A_evaluacion_economica.md) y 2.1 usan **3 % neto**, pasarela referencial descontada al vendedor, API mínima y reservas hipotéticas. Año 1: **5.314.863 CLP** de salida; VAN de caja a 36 meses **−15.140.998 CLP**; TIR indefinida. Las cifras anteriores son antecedentes, no escenario vigente. |
| Word de 91 páginas | Revisado el 24-09-2026 | Es un **render histórico** anterior a las 43 tablas y al recálculo del Anexo A. Se generó una nueva copia de lectura del borrador el 29-09, con pendientes visibles; requiere actualizar índices y revisión visual antes del cierre institucional. |

## Cobertura de los 17 criterios de la rúbrica

**Lectura del estado:** «redactado» significa que existe diseño o plan en el informe; «pendiente» exige decisión, tercero o ejecución. La rúbrica pide confeccionar y describir varios artefactos, por lo que una prueba no ejecutada no invalida automáticamente el plan documental, pero impide afirmar rendimiento, cumplimiento o funcionamiento. El instrumento incorporado suma **60 puntos**; la guía resumida omite 2.1.5.15 y no se usa para inventar una nota.

| Criterio | Evidencia redactada | Brecha concreta antes de cerrar |
| --- | --- | --- |
| **2.1.1.1** Comparación y factibilidad | 2.1 compara tecnologías por capa y contiene simulación económica reproducible, sensibilidad de ticket y categorías. | Demanda/aceptación y precios finales por categoría, SKU comparables en Santiago y ensayos de capacidad; no llamar rentable al escenario actual. |
| **2.1.1.2** Herramientas y recursos | 2.2 inventaría stack, versiones objetivo, licencias y recursos supuestos. | Inventario de equipos, parches/imágenes reales, contratos y accesos de proveedores. |
| **2.1.2.3** BPMN | 3.1 presenta cuatro diagramas: tres procesos principales con subprocesos y una vista de colaboración. | Acta de revisión del equipo; validar M1–M11, T1–T4 y manejo de pagos tardíos con las condiciones reales del proveedor. |
| **2.1.2.4** UML de casos/componentes | 3.2 tiene siete vistas para 41 de 52 CU y justifica los otros once; 3.3 describe componentes e interfaces. | Revisar relaciones y CU-14/31/47/51, validar interfaces y paginación; documentar observaciones resueltas. |
| **2.1.2.5** Modelo y diccionario | 3.4 y Anexo B contienen diseño de 43 tablas, restricciones, estados y matriz de tratamiento. | Escribir/aplicar migraciones PG18/PostGIS; ejecutar MD-01–MD-13; revisar datos y permisos frente al backend implementado. |
| **2.1.2.6** Topología | 3.5 presenta canales, puertos, secretos y webhooks propuestos. | Acordar dominio/red y comprobar autenticación con integraciones habilitadas. |
| **2.1.2.7** Infraestructura | 3.6 y Anexo A presupuestan Cloud Run/Cloud SQL en Santiago, incluida instancia mínima. | Inventario, configuración real, precio por SKU y ensayo de escalado, respaldo y recuperación. |
| **2.1.2.8** Arquitectura | 3.7 integra software, hardware y recorrido de reserva/fallos. | Reproducir fallos y portabilidad RNF-034–036; no presentar despliegue como hecho. |
| **2.1.3.9** KPI SMART | 4.1 contiene once fichas con fórmula, ventana y fuente. | Nombrar responsables y obtener series medidas; registro actual vacío. |
| **2.1.3.10** SLA | 4.2 contiene cinco fichas y metas de servicio. | Definir cliente/gestor, vigencia y ventana de mantención; ensayar resultados antes de llamarlos SLA cumplidos. |
| **2.1.4.11** Plan de pruebas | 5.1 y Anexo C detallan PT-01–PT-16. | Ejecutar cada caso disponible con versión, entorno, esperado/observado y evidencia; marcar el resto «planificado». |
| **2.1.4.12** Normas/estándares | 5.2 justifica estándares y usa Ley 21.719 como criterio desde el primer incremento. | Revisar aplicabilidad, bases y plazos por finalidad; PT-16 aún sin ejecutar. Vigencia legal: 01-12-2026. |
| **2.1.5.13** Disponibilidad | 6.1 propone dependencias, sondeos, umbrales y respuesta. | Habilitar monitoreo y registrar mediciones. |
| **2.1.5.14** Continuidad | 6.2 describe prevención, restauración y reacción. | PT-11 y restauración medidos para RPO 4 h/RTO 6 h; configuración sola no prueba objetivos. |
| **2.1.5.15** Cambios/incidentes | 6.3 define flujo y registro; este criterio **sí está en la rúbrica**. | Acordar roles y practicar un cambio/incidente con bitácora. |
| **2.1.6.16** Fases | 7 presenta siete hitos, dependencias y evidencia de cierre. | Horas y responsables reales; ajustar fechas y alcance demostrable con capacidad del equipo. |
| **2.1.6.17** Adecuación del plan | 7 razona el cambio respecto de la entrega anterior y registra riesgos. | Revisar frente a avance de código, recursos y retroalimentación docente; registrar versión del cronograma. |

**Conclusión de cobertura:** los **17/17 criterios tienen contenido documental localizable**. Eso no significa 17/17 criterios acreditados: pagos, demanda, disponibilidad, privacidad, pruebas y resultados de producto siguen sin evidencia de ejecución o respuesta externa. Los 13 marcadores de la versión vigente representan esos bloqueos, no trece párrafos simplemente por escribir.

## Aporte de Shiva y escenario oficial

El [estudio de Shiva](../../flujodecaja/estudios.md) aporta una estructura útil de mercado, estudio técnico, organización, inversión, capital de trabajo y flujo de caja. El repositorio lo atribuye a la identidad Git «Shiva» en `2030456` y lo preserva en el cuerpo. Sus cuadros de **3.600 reservas/año y comisión hipotética de 25 %** arrojan una conclusión positiva bajo otros costos y supuestos; **no son ventas observadas ni el caso económico actual**. El escenario actual, [Anexo A](../../anexos/A_evaluacion_economica.md), usa **0/720/1.800 reservas hipotéticas**, 3 % neto, tarifa pública de pasarela como descuento al vendedor, un primer año sin ingresos y VAN negativo. El **12 % actual es tasa de descuento supuesta**, no la comisión. La primera labor editorial de Shiva es conservar su método y reconciliar expresamente estas diferencias, sin trasladar el VAN positivo al resumen ejecutivo.

## Bloqueos que sí cambian decisiones de implementación

1. **Contrato de pago:** Split 1:1 existe documentalmente en Chile, pero faltan tarifa contractual, medio admitido bajo «dinero en cuenta», KYC de cuenta y vendedores, comprobantes, reembolsos y capacidad de garantía. El backend debe mantener adaptador e importes separados hasta una prueba en sandbox.
2. **Tributos y sociedad:** faltan respuesta particular del contador sobre IVA/DTE de arriendo, comisión y tarifa, giro de la comisión, régimen, capital y distribución; no codificar el 3 % societario como tres pagos Split.
3. **Precio y demanda:** los avisos de `INV-011` son precios de lista de duraciones distintas. No sustentan el ticket medio de 100.000 CLP, 720/1.800 reservas ni aceptación de 3 %.
4. **Privacidad:** Ley 21.719 rige el diseño desde el primer incremento por decisión del usuario. La matriz aún requiere bases, plazos, responsables y prueba PT-16; no activar Bucket Lock productivo con plazo sin aprobar.
5. **Capacidad y entrega:** falta acuerdo de horas semanales y una lista de funcionalidades **demostrables** al 3 de noviembre. El alcance de diseño del producto completo ya está fijado; la evidencia ejecutable se registra por incremento.

## Regla de cierre

Para cada afirmación nueva: guardar fuente o resultado fechado, actualizar la sección/anexo correspondiente, la [matriz](../matriz_trazabilidad_es2.md) y [`pendientes.md`](../../pendientes.md), y recién entonces retirar el marcador afectado. La [propuesta de reparto](09_reparto_equipo_es2_2026_09_29.md) convierte esta auditoría en entregables individuales. Un Word de lectura puede circular con pendientes visibles; `validar --final` no debe forzarse hasta contar con la evidencia real.

## Copia Word de lectura, 29-09-2026

Se generaron [informe completo](../../revision_equipo/2026-09-29/Informe_Final.docx), [Anexo A](../../revision_equipo/2026-09-29/Anexo_A_Evaluacion_economica.docx), [Anexo B](../../revision_equipo/2026-09-29/Anexo_B_Diccionario_de_datos.docx) y [Anexo C](../../revision_equipo/2026-09-29/Anexo_C_Casos_de_prueba.docx) desde las fuentes vigentes; las copias versionadas se explican en su [README](../../revision_equipo/2026-09-29/README.md). Los archivos abren como DOCX, muestran **TIH184** y no contienen referencias internas `INV-*` en el texto OOXML. `validar ES2PT` devolvió cero errores y tres avisos por los marcadores abiertos. El informe contiene 35 tablas y 25 figuras; una conversión con LibreOffice dio 124 páginas orientativas. El índice aún requiere actualización de campos en Word; esta generación no sustituye la revisión visual completa ni acredita las pruebas de producto.
