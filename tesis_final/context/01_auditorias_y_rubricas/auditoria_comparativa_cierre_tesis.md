# Revisión comparativa de coherencia de la memoria espaciGo

**Fecha:** 4 de noviembre de 2026.  
**Alcance:** manifiesto completo, capítulos y anexos compilados, ADR de producto, contrato API fijado en el informe y evidencia del repositorio local. Se comprueba integridad de referencias e imágenes y se contrasta por significado el recorrido principal. El examen de maquetación se realiza por muestra.

| Hallazgo de la primera revisión | Cambio previo | Resultado de la nueva revisión |
|---|---|---|
| Métricas de carga, cobertura y DRP presentadas como resultados sin registro asociado | X, XIII y XIV separan evidencia, objetivo y límite. F enumera criterios. | Se actualiza el cierre técnico F5/F6 a partir del registro `93b59c8`. Quedan como objetivos la prueba de carga y la recuperación integral. |
| RNF-010 con dos pares de tiempos | Se unifica RPO de 15 minutos y RTO de 1 hora. | VII, X, XI, A y F conservan el mismo criterio objetivo y su prueba asociada. |
| RF/UC heredados en el plan de pruebas | F adopta RQF, RNF y CU canónicos. | Se corrige el alias `CU33` y se comprueba existencia de los IDs citados. La existencia del ID no acredita por sí sola equivalencia semántica o cobertura. |
| OpenAPI prometido en E, con runbooks en su lugar | E identifica un OpenAPI 3.1 fijado a un commit. XI contiene los runbooks. | Se distingue la especificación histórica fijada del contrato objetivo y de futuras integraciones. |
| Modelo físico y diseño objetivo confundidos | IX y D separan catálogo derivado, captura V75 y diseño objetivo. | Se conserva el contraste de 104 nombres coincidentes y seis relaciones documentales declaradas en V79. La revisión semántica completa por columnas y ACL queda por corte. |
| Cifras de mercado sin alcance y bibliografía ausente | I limita la lectura a estudios de oficinas. II formula un escenario y criterios. Citeproc genera referencias APA. | Se mantiene la distinción entre evidencia de mercado y medición de adopción. |
| Portada superpuesta e índice vacío | El flujo corrige la portada y LibreOffice actualiza el TOC de DocSkill en PDF. | Coinciden las páginas del índice con los 14 capítulos y los ocho anexos en la exportación de 505 páginas. |
| Matriz metodológica con totales incorrectos | V recalcula 2,85, 2,75 y 4,80. | Se conserva la selección híbrida. |

## Discrepancias nuevas y rectificaciones

- El Anexo A exigía identidad verificada para publicar y limitaba indirectamente la galería a 10 imágenes. Se ajustan titularidad, verificación al emitir y 30 posiciones con cargas reservadas. El límite de archivo se vincula al procesador del corte.
- El registro se describía con preferencia inicial. Se ajustan RQF-213, HU01 y CU-01 al contrato observado en el handler y en OpenAPI. Las notas de revisiones anteriores se identifican como históricas.
- Algunos RQF, HU y CU conservaban custodia general, preautorización, plazo fijo de liquidación o descarga solo con firma. Se concilian los requisitos operativos y la tabla de relaciones UML con la modalidad aplicable, la acreditación de renta, la garantía separada y la conciliación independiente de la ocupación.
- El Capítulo IX omitía reglas de presentación de SimpleFirma, reparto, avisos, Checkout Pro y expiración de aportes. Se documentan como diseño ratificado y condiciones del piloto.
- El informe atribuía plazos de retención o trámites a políticas sin distinguir finalidad y entorno. El catálogo los sujeta a la clase de dato y a criterios de habilitación. La revisión legal o tributaria de la operación se mantiene separada.

## Pendientes de verificación y decisión

1. Confirmar la capacidad efectiva del proveedor para firma, cobros, devoluciones y garantía antes de habilitar cada integración. Definir la política operativa de reclamos, retención por finalidad y obligaciones documentales con las fuentes aplicables.
2. Ejecutar y documentar pruebas de carga y recuperación conjunta en el entorno objetivo. Conciliar el catálogo físico y sus permisos por corte. El trabajo documental no vuelve a ejecutar las suites de desarrollo.
3. Completar la conciliación semántica de fichas periféricas y de requisitos heredados, en particular las integraciones de validación de documentos, las condiciones de servicio que todavía conservan valores históricos y la trazabilidad negativa por módulo. El recorrido principal tiene prioridad y los IDs históricos se conservan para continuidad.
4. Mantener intactos 5.3, XII, G y H. El cierre académico de esas materias corresponde a sus autores.

**Referencias internas de trabajo:** ADR `f4bc7bd`, OpenAPI `4e26d52`, cierre técnico F5/F6 `93b59c8` y plan de mejora y ratificación de la memoria.

**Verificación estructural:** 236 RQF, 43 RNF, 35 HU, 52 CU, 16 PT y 26 referencias a imágenes PNG válidas. La comprobación no detecta identificadores inexistentes. Se conserva íntegro el texto reservado.
