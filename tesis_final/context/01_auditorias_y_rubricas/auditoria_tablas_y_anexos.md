# Revisión de tablas y concordancia entre cuerpo y anexos

**Corte:** 4 de noviembre de 2026. La revisión sigue el orden de los capítulos. Las tablas del cuerpo sintetizan reglas, evidencia o criterios. Los anexos identifican el detalle técnico o académico correspondiente.

| Capítulo | Tabla del cuerpo | Correspondencia comprobada |
|---|---|---|
| I | Sin tabla | Las tasas se atribuyen a las fuentes del segmento de oficinas. El diagnóstico continúa en II. |
| II | 1. Causas e indicadores | El Anexo F desarrolla PT-02, PT-04, PT-06 y PT-07. La coordinación manual requiere medición de uso. |
| III | Sin tabla | Los conceptos de arquitectura y persistencia se aplican en VIII y IX. |
| IV | 2. Canvas | El diseño de cobros se desarrolla en IX. La evaluación económica remite a XII y H. |
| V | 3, 4 y 5. Metodología, RACI y riesgos | La Tabla 3 identifica la línea base del Anexo A. La RACI separa el despliegue del paquete de evaluación económica. El detalle de planificación queda en G. Los riesgos técnicos se vinculan con VII, XI y F. |
| VI | 6. FODA | La correspondencia entre funciones, módulos, datos y contratos remite a C, D y E. |
| VII | 7 y 8. Recorrido y calidad | Se verifican IDs de A, B y C. CU-33 registra el ingreso, CU-34 registra la entrega y CU-48 confirma la desocupación. El Anexo F detalla las pruebas y separa los criterios de los resultados. |
| VIII | 9. Arquitectura | La verificación de datos, contratos e integraciones remite a las tablas D.1, E.1, F.1 y F.2. |
| IX | Sin tabla de cuerpo | La Figura 11 se vincula con la Tabla D.1. Las 104 tablas comunes de V75 aportan 879 columnas coincidentes por nombre, tipo base y nulabilidad. Se normalizan alias SQL. Las seis relaciones adicionales de D provienen de V79. |
| X | 10. Resultados | La Tabla F.3 distingue resultado observado y criterio objetivo. PT-02, PT-09, PT-10, PT-11 y PT-16 conservan su alcance. |
| XI | 11. Procedimientos | La restauración remite a PT-11. Pagos remite a PT-04 y PT-05. Seguridad y privacidad remiten a PT-14 y PT-16. |
| XII | Reservado | El Capítulo XII y el Anexo H conservan su contenido. |
| XIII | 12. Objetivos y evidencia | OE1 remite a A–C, OE2 a D, OE3 a E y a los cortes de X, OE4 a F y OE5 a XI, XII y H. |
| XIV | Sin tabla | Las conclusiones se contrastan con la Tabla 12 y el alcance de X. |

## Evidencia complementaria de las tres verificaciones

### Fichas secundarias y reputación

Se reejecutan dos pruebas en una copia desechable del repositorio de desarrollo. El banco de reciprocidad crea el rol de prueba antes de migrar y aplica V1–V80. El banco de retrocarga utiliza V36 y V37. Ambas pruebas pasan. El recorrido Mailpit queda fuera de esta ejecución. La prueba original sobre la cadena completa todavía requiere el bootstrap autorizado para V81 en adelante. La preparación de esta copia no cambia el código del repositorio de desarrollo.

### Proveedores y retención

Se conserva la revisión de fuentes y criterios del registro de verificación de fondo. Los proveedores externos permanecen sujetos a evidencia de sus entornos de prueba. La política de retención por finalidad requiere definir actor, vigencia, excepciones, acción sobre objetos y verificación posterior a la recuperación. El alcance publicado del corte F5 sustenta la comprobación local previa.

### Carga y restauración

La comprobación local usa PostgreSQL/PostGIS aislado y `pgbench` 18.6, 200 conexiones, ocho hilos y 15 segundos. Se crea una cuadrícula sintética de 10.000 puntos `geography` en SRID 4326, con índice GiST. Cada transacción ejecuta `count(*)` de puntos a 1.000 m del centro fijo (-70,65, -33,45) mediante `ST_DWithin`. Se completan 42.636 transacciones, con cero fallos, 70,222 ms de latencia media y 2.848,12 transacciones por segundo sin incluir el tiempo inicial de conexión. La prueba caracteriza la consulta SQL aislada. RNF-001 y PT-09 requieren medir el tiempo de búsqueda de extremo a extremo en el entorno identificado.

La restauración básica local V1–V61 queda aprobada según el registro previo. El ensayo independiente `TestGCP03PhasesPostgres18Disposable` falla en la fase de restauración de permisos de aplicación. El mensaje identifica la fase y no la causa SQL específica. La recuperación conjunta de base y archivos privados y el cálculo de RPO y RTO quedan pendientes en el entorno objetivo.


## Resultado de la rectificación

La revisión final confirma las 12 tablas y las 14 figuras del cuerpo, sus referencias y la correspondencia de los 22 destinos principales del índice con las páginas del PDF. La exportación de DocSkill tiene 497 páginas. La revisión visual por muestras incluye las tablas del cuerpo, figuras y páginas de los anexos C, D, E y F. La inspección estructural comprueba cuadrícula y encabezado repetido en las 208 tablas de Word.

La Tabla 7 enlaza el ingreso y la entrega con los requisitos del Anexo A, HU35 del Anexo B, los tres casos del Anexo C y PT-08 del Anexo F. La Tabla D.1 vincula el perfil de Inmuebles y la ocupación con sus relaciones físicas. La Tabla E.2 describe el catálogo vigente de producto. El Anexo F separa los criterios de aceptación de la evidencia disponible en el Capítulo X.

La sección 5.3, el Capítulo XII y los anexos G y H coinciden con sus fuentes al inicio de la rectificación. Se conservan sus avisos de integración. Los enlaces de las leyes 21.461 y 21.719 contienen su destino íntegro en el PDF.
