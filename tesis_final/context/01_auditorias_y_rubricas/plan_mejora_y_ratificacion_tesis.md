# Plan de mejora y ratificación de la memoria espaciGo

**Corte documental:** 4 de noviembre de 2026.  
**Objeto:** mantener la memoria como especificación del producto objetivo y registro verificable del avance por corte.

## 1. Fuentes y estados

- **Objetivo ratificado.** El chat «Planifica documentación de EspaciGo» confirma la ratificación del ADR de espacios, contratación y cobros. El ADR está en `planning/decisiones/adr_objetivo_espacios_contratacion_cobros.md` de espaciGo, en `main` (`f4bc7bd`) y en la rama de creación de espacios (`4e26d52`). Sus reglas prevalecen sobre hipótesis incompatibles anteriores. Los títulos históricos que aún dicen «propuesta» se interpretan según el estado del ADR.
- **Diseño derivado.** La carpeta local `base de datos` contiene el modelo conceptual, la referencia lógica normalizada, maquetas y un mapa de evolución. El modelo contiene 60 entidades lógicas de referencia. El número de tablas y los nombres SQL se determinan por corte según las invariantes y la reutilización.
- **Implementación y evidencia.** Para afirmar «implementado» se identifica código o migración y su versión. Para afirmar «verificado» se identifica también entorno, fecha, caso y resultado. Una simulación acredita el recorrido ensayado. Una validación con proveedor, una ejecución en cloud de ensayo y una habilitación productiva se registran como alcances separados.
- **Pendiente o diferido.** Una dependencia pendiente conserva criterio de aceptación y condición de habilitación. Un alcance diferido conserva referencia a la decisión que lo excluye. Las decisiones propuestas en este plan se distinguen de las ya ratificadas.
- **Referencia portable.** La carpeta local está excluida de Git. La entrega académica conserva referencias al ADR por commit y únicamente extractos saneados de evidencias y diagramas seleccionados, con procedencia y fecha. El paquete local completo sigue siendo material de trabajo.

## 2. Comparativa de base de datos

| Fuente | Alcance del inventario | Uso en la tesis |
|---|---|---|
| Anexo D vigente | 110 nombres de tablas derivados de DDL, con V79 como máxima versión de creación indicada. | Catálogo derivado de código. Agregar SHA, rango de migraciones procesado y regla de conteo al regenerar. |
| Catálogo local V75 | 105 tablas de aplicación públicas con ledger, 104 sin ledger, según el informe de estrategia. Las 104 coinciden por nombre con el Anexo D. El informe registra 75 checksums coincidentes. | Modelo físico observado y fechado. Separar tablas de extensión, vistas y ledger. |
| Diferencia D frente a V75 | Seis tablas `document_verification_*` de V79 aparecen solo en D. `schema_migrations` aparece solo en el inventario V75. | Distinguir diferencias de versión y de conteo. La coincidencia de nombres no acredita equivalencia de columnas, ACL ni comportamiento. |
| Ensayo documental F5 V83 | La evidencia local de recuperación registra V1–V83 y checksums verificados. La suite del paquete documental registra 86 pruebas de primer nivel aprobadas en ese corte, con cambios locales. La evidencia consultada mantiene abierto el recorrido F6 completo. | Evidencia específica de ensayo. Confirmar conteo por lectura de catálogo del entorno correspondiente antes de rotularlo como observado. |
| Modelo normalizado objetivo | 60 entidades lógicas de referencia, con partes, aceptaciones y asignaciones de cargos detalladas en maquetas. La proyección física V83 es de 111 tablas con ledger, 110 sin ledger. | Explicar conceptos y dependencias en IX, con mapeo al esquema físico en D. Evitar convertir el conteo en meta de implementación. |
| Cloud de ensayo | La captura del 4 de noviembre describe instancia zonal y privada, respaldos automáticos y PITR desactivado. El catálogo, el ledger remoto y la restaurabilidad requieren evidencia de su propio entorno. | Describir estado observado y arquitectura objetivo por separado. La existencia de respaldos no acredita RPO ni RTO. |

### Mapeo que debe incorporar el Capítulo IX y desarrollar el Anexo D

| Dominio | Base actual o antecedente | Objetivo ratificado y criterio de aceptación |
|---|---|---|
| Cuenta y titularidad | `usuario`, `rol_usuario`, `espacio` e historial de publicación. El ADR del 22 de octubre sobre concesión de membresías por primera acción figura como propuesto. | La misma cuenta puede ofrecer y arrendar. La autorización se decide por recurso y operación. Solo el titular vigente publica, administra o republica. Verificar actor autorizado, tercero denegado y conservación del historial en cambios de titularidad. |
| Oferta y galería | Perfiles de categoría, tarifas y horarios existentes. Modelo de medios con `media_asset`, `media_variant`, `space_media` y `gallery_item_order`. | Ocho categorías objetivo, CLP por hora, día o mes, y sesión puntual con intervalo y precio acordados. Hasta 30 posiciones con cargas reservadas incluidas, orden y portada. Probar cupo bajo concurrencia y separación entre imágenes públicas y documentos privados. Conciliar categorías de catálogo por versión antes de afirmar su número en la implementación. |
| Identidad documental | Verificación sintética histórica y seis estructuras documentales de V79. | El anuncio se valida por titularidad y reglas de publicación. La emisión contractual exige identidad de ambas partes y, cuando aplica, expediente de empresa y representación separado. Probar que el contexto de verificación corresponde a la parte, al titular y a la emisión evaluada. |
| Disponibilidad | `public.ocupacion` en V9 usa `tstzrange` y exclusión GiST por espacio e intervalo activo. IX describe una tabla y una columna ilustrativas distintas. | Autoridad única de ocupación y un bloqueo activo por reserva. Verificar intervalos solapados y adyacentes, vencimiento atómico, reintento sin extensión y pago tardío sin reactivación. |
| Emisión y firma | Contrato, firmas e historial de ensayo. La tesis describe firma remota como paso general. | Emisión inmutable con ID, partes, condiciones y huella. Una corrección origina nueva emisión y aceptación. Identidad, aceptación bilateral y firma se registran por separado. Sin firma como recorrido principal para hora o sesión, SimpleFirma opcional y recomendada para inmueble mensual. |
| Cobros | Pago y garantía de ensayo. La tesis describe custodia generalizada y una secuencia que cobra antes de emitir o aceptar. | Separar aportes de firma, renta y garantía, con obligaciones, pagadores, intentos, eventos, pagos y reversos. Sin firma, renta tras ambas aceptaciones. Con SimpleFirma, aportes acreditados antes de firmar y ambas firmas antes de pagar renta. Mercado Pago Checkout Pro/Preferences y Split para renta y comisión, con OAuth del arrendador. Garantía separada y posterior a renta, habilitada por evidencia. |
| Entrega y cierre | Operación e historial de ensayo. | El arrendatario entrega y el titular confirma desocupación. La transición libera solo el bloqueo correspondiente, permite republicar de inmediato y preserva contrato y otros intervalos. |
| Operación y privacidad | Catálogo de ACL, restricciones, índices, funciones, triggers y migraciones. | Publicar en D un índice por dominio, fuente de verdad, dueño de escritura, claves, integridad y cambios. Documentar en XI acceso por capacidad, retención por finalidad y recuperación conjunta de PostgreSQL y objetos privados. |

## 3. Decisiones propuestas para la memoria y su implementación

| Decisión | Recomendación | Evidencia o condición de cierre |
|---|---|---|
| R1. Estado de la memoria | Aprobar una línea base académica con fecha y dos vistas por capítulo técnico: diseño objetivo y avance verificable. Actualizar la misma sección al cerrar cada incremento. | Tabla por objetivo con estado, SHA, entorno, evidencia y límite. |
| R2. Modelo físico | Reutilizar primero tablas e historial vigentes. Autorizar una tabla nueva cuando el mapeo demuestre que falta identidad estable, relación o restricción. | Diferencia de DDL y pruebas desde base vacía y desde el corte anterior. |
| R3. Flujo demostrable | Priorizar una reserva por hora sin firma ni garantía, con datos sintéticos. | Identidades verificadas para emisión, ambas aceptaciones, ocupación única, cobro simulado, vencimiento, evento duplicado y tardío, entrega y republicación. |
| R4. Vencimiento | Probar un límite absoluto por ruta calculado al crear el bloqueo y un vencimiento por etapa que respete ese límite. Mantener los valores de ensayo ya ratificados: 15 minutos sin firma y 30/60/15 con firma, más 15 para garantía cuando aplica. | Tabla de transiciones con inicio exacto de cada plazo, reloj y prioridad entre pago y expiración. Validar que el inicio del arriendo queda fuera de la ventana. |
| R5. Firma y garantía | Habilitar SimpleFirma tras validar facturación, reversos y política de piloto. Habilitar garantía después de verificar responsable de fondos, reclamos, plazos y devolución total/parcial. Mantener disponibles las ofertas sin garantía. | Pruebas por pagador y emisión. Firma 50/50 o patrocinada por arrendador, con peso impar a su cargo. Conservar política de expiraciones ratificada y validar su ejecución antes de cobrar. Los costos del piloto se coordinan con los responsables de la evaluación económica. |
| R6. Evidencia de continuidad | Usar RPO ≤ 15 min y RTO ≤ 1 h como metas de aceptación del RNF-010. Medir la recuperación conjunta de base y archivos, incluyendo permisos, referencias y registros sujetos a supresión. | Escenario reproducible con tiempos, validaciones y comparación con la meta. Mantener separados el resultado local y el de cloud. |
| R7. Trazabilidad y bibliografía | Usar RQF/RNF del Anexo A como identificadores canónicos y asignar equivalencias por significado. Fijar una única bibliografía académica con referencias a páginas o tablas para datos de mercado. | Matriz OE → RQF/RNF → HU/CU → ADR/API/DDL → PT → evidencia. Validar enlaces, duplicados, versión y fuente. |
| R8. Alcance de la entrega | Conservar el detalle físico en D y la secuencia de operación en el cuerpo. Organizar el diccionario por dominio con índice y separar visualmente catálogo y modelo objetivo. | El evaluador puede seguir un flujo de punta a punta sin recorrer todo el diccionario. Se conserva el detalle exigido por la pauta. |

Las decisiones sobre modalidades, reparto, valores de ensayo, secuencia de cobro y republicación ya están ratificadas. La activación externa, las reglas exactas de transición y el detalle físico requieren las comprobaciones indicadas. La recurrencia, la subdivisión, el aforo compartido y la validación de firmas externas quedan diferidos según el ADR.

## 4. Plan por sección

| Sección | Cambio | Criterio de cierre |
|---|---|---|
| Preliminares | Corregir portada e índice. Reescribir resumen con problema, objetivo, método, avance verificable y alcance pendiente. | Portada legible con autores y datos institucionales. Índice paginado y navegable. |
| I. Introducción | Delimitar producto objetivo, versión presentada y entornos. | El lector distingue el prototipo, cloud de ensayo y operación objetivo desde el inicio. |
| II. Problema | Verificar cifras de mercado, incluida la afirmación del 78 %, y describir método del diagnóstico. | Cada afirmación cuantitativa remite a población, fecha, alcance y fuente recuperable. |
| III. Marco teórico | Vincular cada concepto con una decisión de ingeniería. Revisar comparativa de proveedores, firma, Split, exclusión temporal y privacidad con fuentes primarias antes de cerrar. | El texto distingue capacidad comprobada del proveedor y comportamiento exigido por el diseño. |
| IV. Objetivos y negocio | Definir resultado observable por OE. Ajustar Canvas al flujo ratificado y separar beneficio esperado de resultado medido. | Cada OE tiene entregable, evidencia o condición pendiente. |
| V. Metodología | Corregir la matriz ponderada. Registrar cambios del ADR y entregables por incremento. Coordinar la integración de 5.3 con sus autores. | Totales verificables y criterios de cierre por incremento vinculados a la EDT. |
| VI. Arquitectura empresarial | Actualizar roles por recurso, actores externos y responsabilidad sobre oferta, cobro, soporte y datos. | Las cuatro vistas de arquitectura distinguen responsables y puntos de integración. |
| VII. Requerimientos | Conciliar siete agrupaciones de síntesis con M01–M11 y RQF/RNF canónicos. Actualizar objetivos de calidad y cobertura documentada. | Muestreo de trazas reales y comprobación de referencias a A, B, C y F. |
| VIII. Arquitectura TI | Separar adaptadores sintéticos y productivos. Referir OpenAPI del SHA presentado y diferenciar interfaces futuras. | Se puede identificar el contrato vigente de cada recorrido y la dependencia externa. |
| IX. Procesos y datos | Actualizar BPMN de publicación, contratación y cierre. Separar modelo conceptual, lógico y físico. Incorporar mapeo y restricciones críticas. | Diagramas PlantUML legibles en PNG, fases y actores coherentes con el ADR, modelo físico ligado a migración y corte. |
| X. Pruebas | Separar diseño de pruebas, ejecución y resultados. Incorporar evidencias trazables de LOCAL-1, F5 y cloud de ensayo según su alcance. | Cada valor reportado tiene salida reproducible. Las metas y los casos pendientes tienen estado explícito. |
| XI. Despliegue y seguridad | Separar infraestructura observada, objetivo y condiciones de producción. Explicar mínimo privilegio, migración incremental y restauración coordinada de datos y objetos. | RPO/RTO con ensayo documentado cuando exista. Integrar runbooks como sección operativa o suplemento. |
| XII. Evaluación económica | Integración a cargo de Anita Marchant y Erick Silva. | Sección reservada y alerta verde durante el trabajo. |
| XIII. Control | Sustentar SPI, control de cambios y verificación de requisitos con registros o consignar su estado pendiente. | Matriz de cobertura distingue diseñado, ejecutado y conforme por entorno. |
| XIV. Conclusiones | Cerrar por OE y explicitar límites de mercado, proveedor y validación. | Conclusiones reproducibles desde sus fuentes, sin adelantar resultados de incrementos posteriores. |
| A. Requisitos | Alinear RNF-010 y revisar RQF afectados por oferta, contrato, pago y entrega. | IDs estables y cambios rastreables por significado. |
| B. Historias | Actualizar aceptación bilateral, modalidades, expiración y republicación con criterios observables. | Casos normal, alternativo y de denegación enlazados. |
| C. Casos de uso | Actualizar fichas y UML por módulo. Modelar firma opcional y errores externos como ramas identificables. | Cada ficha tiene precondiciones, flujo principal, alternativos y traza. |
| D. Datos | Incluir manifiesto de extracción, comparativa V75/V83, mapa lógico–físico, diccionario por dominio y catálogo de integridad, índices y lógica SQL. | Conteos reproducibles, procedencia de migraciones y distinción entre observado, derivado y objetivo. |
| E. API | Sustituir el contenido por índice y extractos del OpenAPI versionado. Reubicar los seis runbooks en XI o suplemento operativo. | Especificación descargable o enlazada al corte. Rutas y versiones contrastadas con el alcance presentado. |
| F. Pruebas | Corregir referencias heredadas por semántica. Añadir evidencias y resultados por entorno. | Casos con IDs canónicos, fecha, versión, resultado y limitación. |
| G y H. Anexos reservados | Integración a cargo de Anita Marchant y Erick Silva. | Alertas verdes durante el trabajo. |

## 5. Orden de ejecución y mantenimiento

1. **Fijar la línea base.** Incorporar la referencia al ADR, establecer el estado de cada objetivo y resolver contradicciones verificables de terminología, metas y procedencia. Registrar en D el alcance de cada conteo.
2. **Actualizar el diseño transversal.** Trabajar VII–IX y A–E como un conjunto. Reemplazar los BPMN incompatibles, renderizar PNG y revisar su lectura. Documentar en el cuerpo las decisiones y en D el detalle de datos.
3. **Integrar el avance.** Actualizar X, XI, XIII y F usando pruebas existentes con entorno y SHA. Registrar el resultado de cada nuevo incremento en su sección, junto con su fila de trazabilidad. Revisar el flujo de hora sin firma antes de incorporar rutas de firma y garantía.
4. **Cerrar el relato académico.** Ajustar diagnóstico, referencias, objetivos, resumen y conclusiones. Incorporar las entregas reservadas cuando sus autores las suministren.
5. **Verificar la entrega.** Compilar con el flujo institucional, actualizar campos, revisar portada e índices, capítulos, anexos, tablas, PNG y enlaces. Verificar que el archivo exportado proviene de la compilación actual y que las alertas reservadas siguen presentes.

Plantilla mínima para el registro de cada incremento: **objetivo o RQF/RNF · estado · versión · entorno · evidencia · resultado · límite · sección afectada**. En D se añade **migración máxima · regla de conteo · diferencias respecto del corte anterior**.

## 6. Propuesta de acuerdos para decisión del equipo

| Punto | Acuerdo recomendado | Condición de revisión |
|---|---|---|
| Línea base académica | Adoptar el ADR del 4 de noviembre y el corte de evidencias fechado como línea base. Cada incremento actualiza su propia sección con estado, SHA, entorno, resultado y limitación. | Revisar la línea base cuando cambia un objetivo o una regla ratificada. Una nueva evidencia actualiza el avance del objetivo correspondiente. |
| Evolución del esquema | Conservar tablas y migraciones existentes cuando cubren la invariante. Exigir mapeo y prueba antes de crear una relación. Mantener separados modelo lógico, DDL derivado y catálogo por entorno. | Si faltan identidad estable, claves, historial o atomicidad, aprobar el delta específico y comprobarlo desde vacío y desde el corte anterior. |
| Primer recorrido | Priorizar un arriendo por hora sin SimpleFirma ni garantía y con cobro simulado. La demostración cubre titularidad, aceptación, concurrencia, duplicados, pago tardío y republicación. | Incorporar firma y garantía como incrementos separados tras la evidencia de proveedor y el cumplimiento de sus criterios. |

Estos tres acuerdos son propuestas de gestión y secuencia. El ADR vigente conserva su estado ratificado. Los apartados reservados permanecen íntegros.
