# INV-024 — Índice de investigación de ES2

- Estado: índice construido a partir de los registros existentes; no agrega hallazgos nuevos.
- Fecha: 2026-09-23; ampliado el 2026-09-24 con INV-030 a INV-033.
- Secciones ES2 relacionadas: todas; facilita ubicar cada registro sin abrirlos todos.
- Referencia de línea base: informe final de ES1 y sus anexos, que permanecen congelados.

## Pregunta

¿Qué se investigó en ES2, con qué resultado y qué queda abierto? Este índice resume cada registro; **no reemplaza** la [matriz de trazabilidad](matriz_trazabilidad_es2.md), que relaciona los registros con los criterios de la rúbrica, ni las fuentes y claves bibliográficas, que permanecen en cada archivo.

## Método

Se revisaron todos los registros previos a este índice y se extrajo de cada uno su tema, la pregunta que declara, el hallazgo que puede afirmarse y el límite que deja. Nada se completó por inferencia: si un registro no declara un dato, la columna lo indica como pendiente. La numeración se conserva tal como fue asignada y el registro que estaba reservado al cierre Word se incorporó al completarse esa tarea.

## Registros

| Registro | Tema | Pregunta que declara | Hallazgo que puede afirmarse | Límite o pendiente |
| --- | --- | --- | --- | --- |
| [INV-001](INV-001_base_y_brechas.md) | Línea base y brechas | Qué falta para partir de ES1 | Inventario de la base con las brechas B-01 a B-11 y las exclusiones que deben seguir visibles | B-02, B-03 y B-05 a B-11 siguen abiertas; alcance de demostración sin acuerdo |
| [INV-002](INV-002_tecnologias_y_factibilidad.md) | Tecnologías y factibilidad | Qué capacidades de las tecnologías de ES1 están sustentadas | Documentación primaria por capa y el hallazgo de que BigQuery no garantiza RNF-017 | Medición y evaluación cuantitativa pendientes; puntuación sin cerrar |
| [INV-003](INV-003_integraciones.md) | Integraciones | Qué puede usar realmente EspaciGo | Cuatro niveles de evidencia y separación de acceso, condiciones y credenciales | Sin credenciales ni entorno; primer experimento propuesto y no ejecutado |
| [INV-004](INV-004_modelado_y_datos.md) | Procesos, componentes y datos | Qué diseño explica el ciclo sin darlo por implementado | Tres procesos, invariantes de reserva y calendario con intervalos semiabiertos | DDL aplicado y prueba concurrente pendientes |
| [INV-005](INV-005_kpi_sla.md) | Indicadores y niveles de servicio | Qué indicadores sirven para el avance y para el producto | Ocho indicadores heredados y metas de servicio separadas de toda medición | Sin resultados del producto ni responsables |
| [INV-006](INV-006_calidad_y_normativa.md) | Calidad y normativa | Qué referencias usar y qué afirmaciones corregir | ISO/IEC 25010:2023 vigente y la Ley 21.719 adoptada como criterio de diseño | Aplicabilidad jurídica y evidencia de conformidad pendientes |
| [INV-007](INV-007_operacion_y_mantencion.md) | Operación y mantención | Cómo medir disponibilidad, recuperar y mantener | Controles derivados de los RNF y procedimientos propuestos | Sin infraestructura, responsables ni ensayos |
| [INV-008](INV-008_plantilla_word.md) | Plantilla Word | Si el adaptador institucional sirve para ES2 | Inspección de 43 partes OOXML y un perfil preliminar desactivado | APA 7 y revisión visual pendientes |
| [INV-009](INV-009_evaluacion_economica.md) | Evaluación económica con Sapag | Qué volumen recupera los recursos | Método con margen del 25 %, IPC supuesto y 27 % de impuesto | Ejemplo superado por INV-010; prefactibilidad real pendiente |
| [INV-010](INV-010_infraestructura_y_formalizacion.md) | Infraestructura y formalización | Qué cuesta operar y formalizar la SpA | Tres perfiles de referencia, provisión regional inicial del 35 % y escenario sin ventas en el primer año | La provisión fue sustituida por un escenario regional preliminar, aún sin cotización contractual ni factura (INV-021) |
| [INV-011](INV-011_muestra_precios_y_demanda.md) | Precios y demanda | Si el ticket y el volumen representan todos los espacios | La muestra por categoría no valida un ticket único | Demanda no medida; el equipo decidió abarcar todas las categorías |
| [INV-012](INV-012_pagos_firma_identidad.md) | Pagos, firma e identidad | Quién soporta cada costo | La liquidación publicada descuenta la tarifa al vendedor; la firma pública se cobra por documento | Sin contrato ni cotización de API |
| [INV-013](INV-013_monetizacion_pagos_y_promocion.md) | Comisión y promoción | Cómo cobrar sin confundir fondos de terceros | Comisión decidida en ES1; destaques como propuesta nueva y Meta como gasto aparte | Destaque no aprobado; cero ingresos publicitarios en el flujo |
| [INV-014](INV-014_giro_publicidad.md) | Giro y tributación | Qué actividad declararía el destaque | El catálogo del SII clasifica 731001 como servicio publicitario afecto a IVA | Clasificación particular y consulta al contador pendientes |
| [INV-015](INV-015_captacion_meta.md) | Captación con Meta Ads | Cómo captar de forma medible | Diseño de dos embudos y una campaña acotada al presupuesto de 357.000 CLP ya supuesto | Sin campañas ni resultados atribuidos |
| [INV-016](INV-016_metodologia_demanda.md) | Metodología de demanda | Cómo validar oferta y demanda por categoría | Protocolo con fuentes SII, INE y AAPOR y estratos extensibles | Sin entrevistas ni mediciones |
| [INV-017](INV-017_tco_nube.md) | TCO de nube | Cuánto cuesta Cloud Run frente a máquinas virtuales | Comparación en Iowa con la misma carga y servicios comunes | Sin cotización comercial ni medición de EspaciGo |
| [INV-018](INV-018_comparacion_split.md) | Split y liquidación | Qué alternativa conviene y con qué límites | Comparación de Mercado Pago, Flow, TUU y Stripe con checklist de pruebas | Sin sandbox, cuenta de empresa ni cobro real |
| [INV-019](INV-019_integracion_coherencia.md) | Integración y coherencia | Si el informe mantiene coherencia | Conciliación de capítulos, anexos, citas y escenarios económicos; documenta también un presupuesto anterior | Los resultados iniciales de VAN −2.448.407 CLP y TIR −16,04 % son históricos; el escenario actual de Santiago sigue condicionado a tarifas auditadas |
| [INV-020](INV-020_revision_word_final.md) | Revisión Word | Si el perfil genera el informe y los anexos sin degradar las citas | Dos revisiones: la del 23-09-2026 (histórica, 84 páginas) y la del 24-09-2026, que generó 91 páginas y los anexos A/B/C con el perfil aprobado y corrigió un defecto de anchos de tabla | El contenido mantiene 14 marcadores deliberados y `validar --final` sigue bloqueado por ellos |
| [INV-021](INV-021_gcp_santiago.md) | Estimación preliminar de GCP en Santiago | Cuánto podría costar operar desde Chile | Comparador aritmético de `southamerica-west1`: USD 384,23 al mes frente a USD 297,01 en Iowa para ese perfil; otra configuración alimenta el piloto de USD 237,82 | Las tarifas regionales se aplicaron como supuestos del presupuesto, no como cotización formal; faltan SKU, condiciones de facturación y revisión tributaria |
| [INV-022](INV-022_pruebas_y_privacidad.md) | Pruebas y privacidad | Qué se prueba y bajo qué marco de datos | Matriz de privacidad con las leyes 21.719 y 19.628 y pruebas en GitHub Actions y GCP | Sin ejecución; aplicabilidad jurídica pendiente |
| [INV-023](INV-023_operacion_y_herramientas.md) | Operación y herramientas | Con qué se opera la plataforma | Cloud Monitoring con sondas cada 5 minutos, respaldos y ventana de mantención propuesta | Responsables, exclusiones acordadas y ensayos pendientes |
| [INV-025](INV-025_metadatos_y_rubrica.md) | Metadatos y rúbrica | Qué metadatos están confirmados y en qué difieren los instrumentos | La guía omite el criterio 2.1.5.15 y su tabla suma 96, no los 100 que declara; la rúbrica suma 60 con 17 criterios | Código, sección, académico y fechas formativas por confirmar con el instrumento oficial |
| [INV-026](INV-026_mercado_pago_split.md) | Mercado Pago, tarifa, pruebas y giros | Si el proveedor soporta el reparto con cuenta de empresa, qué entorno de pruebas ofrece y qué giros necesita la SpA | Split 1:1 confirmado en Chile para Checkout Pro o API con KYC 6 y OAuth; la comisión de Mercado Pago se descuenta primero al vendedor; cuentas de prueba con tres roles. Su análisis de tres códigos es histórico; la propuesta vigente se aclara en INV-029 | Medio de pago bajo «dinero en cuenta» por confirmar; tarifa de Split sin cotizar; clasificación de la comisión pendiente |
| [INV-027](INV-027_gestion_terceros.md) | Gestión de terceros | Cómo obtener la evidencia que cierra las diez filas de la sección 1 de pendientes | Consultas preparadas para pago, firma, identidad, contador, domicilio y municipio; matriz de evidencia por fila | No se han enviado consultas ni ejecutado pruebas; cotizaciones y respuestas siguen abiertas |
| [INV-028](INV-028_sensibilidad_costos_terceros.md) | Sensibilidad histórica de costos de terceros | Cuánto cambiaba la caja con asesoría inicial y firma diferentes | Tres escenarios aislados con presupuesto LOF; brecha histórica 2.867.691 CLP | La base vigente con Oficina Express y sus cifras está en INV-029; sin cotizaciones |
| [INV-029](INV-029_domicilio_patente_y_dom.md) | Oficina virtual y patente | Qué cuestan aproximadamente el domicilio, una patente y actuaciones DOM eventuales | Oficina Express 50.000 CLP/año y 5.000 de firma; una patente mínima ilustrativa 1 UTM/año; DOM 0,15/0,35 UTM y aseo condicionados; propone 631200+731001 | Sin contrato, aprobación municipal, liquidación ni clasificación definitiva de la comisión |
| [INV-030](INV-030_auditoria_pendientes.md) | Auditoría de pendientes | Si las 32 tareas originales siguen vigentes | Tabla de destino de cada tarea original y separación entre decisiones ya resueltas y obligaciones empíricas | No cierra ninguna obligación externa; reordena el trabajo abierto |
| [INV-031](INV-031_fuentes_cierre.md) | Fuentes para cerrar decisiones | Qué puede afirmarse del pago con reparto, la firma y la retención bloqueada | Split 1:1 disponible en Chile; la firma no tiene importe contractual; Bucket Lock impide reducir la retención y su bloqueo es irreversible | La habilitación comercial y las tarifas particulares quedan para después de ES2 |
| [INV-032](INV-032_tecnologias_cierre.md) | Selección e inventario de tecnologías | Con qué fuentes se sustentan versiones, licencias y hardware | Next.js 16.x en soporte activo y MIT; rama 24 LTS de Node.js; Go 1.26; PostgreSQL 17; PostGIS 3.5.2 con GPLv2; Docker sin gratuidad contractual confirmada | No instala ni mide; el hardware es una configuración objetivo |
| [INV-033](INV-033_cierre_borrador.md) | Cierre documental del borrador | Qué decisiones se pueden cerrar sin falsificar evidencia | Valoración ponderada por capa, fichas de versiones y licencias, decisión de inmutabilidad por retención bloqueada y escenario segmentado sintético con sus cifras | Los 14 marcadores restantes dependen de terceros, del equipo o de producto desplegado |

## Preguntas abiertas que atraviesan varios registros

1. Contratar o cotizar pago con reparto, firma electrónica y verificación de identidad (INV-003, INV-012, INV-018).
2. Medir demanda, precios finales y aceptación de la comisión en cada categoría (INV-011, INV-016).
3. Confirmar giro, régimen, documentos y capital de la SpA (INV-010, INV-014, INV-026).
4. Aplicar el DDL y probar el calendario con carga concurrente (INV-004).
5. Ensayar la retención bloqueada propuesta para RNF-017 y acordar el plazo productivo con la matriz de tratamiento (INV-002, INV-031, INV-033).
6. Validar con métricas la comparación de INV-017 y confirmar el IVA y el crédito fiscal de los servicios contratados en Santiago (INV-017, INV-021).
7. Obtener evidencia docente, confirmar el código de asignatura y cerrar los metadatos de la entrega (INV-001, brechas B-09 y B-10; INV-025).

## Impacto y decisión

El índice permite ubicar cada tema sin abrir los registros y deja a la vista qué sigue abierto. No cambia hallazgos ni decisiones: cada afirmación se apoya en el registro citado y la relación con los criterios de la rúbrica permanece en la matriz de trazabilidad. Un índice desactualizado sería peor que no tenerlo, así que al crear un registro nuevo corresponde agregarlo a esta tabla y a la lista de `README.md`.
