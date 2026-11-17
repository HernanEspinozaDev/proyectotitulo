# Aplicación de la revisión editorial

La revisión se aplica sobre el corte dd62e8c. El plan contiene doce tareas con criterios y evidencias; su estado se conserva en PLAN_Y_TAREAS.md y tareas.json. La entrega se construye con DocSkill y la plantilla institucional vigente. El PDF contiene 567 páginas.

## Correcciones realizadas

1. **Correlativos.** Se corrige 10.7 para remitir a las figuras 11 y 12 en persistencia. CU-15 ya remite a la Figura 14 y los módulos M06/M07 a la Figura 15; su correspondencia se comprueba en la fuente y la salida final.
2. **Redacción conceptual.** Se sustituyen nombres de configuración y de paquetes, herramientas locales identificadas por su nombre de implementación, hashes y códigos de archivos de migración en Resumen, Abstract, capítulos y anexos. Se conserva la descripción de arquitectura, alcance de cada ensayo, fechas y resultados.
3. **Figura de componentes.** Se modifica el PlantUML y se regenera el PNG de la Figura 10 con entrada HTTP, dominio, adaptadores de persistencia y objetos, servidor SMTP de pruebas y entorno local compatible con AWS. Se comprueba que el PNG incrustado en Word coincide exactamente con el render corregido.
4. **Planificación.** VI/XV presenta la estructuración y nivelación de los 28 paquetes, 54 actividades y nueve hitos. Se elimina del texto académico la crítica al archivo de años anteriores y la cifra de 1.320 horas. El cuerpo utiliza nombres conceptuales para las actividades; el Anexo G conserva su detalle e identificadores contextualizados. El margen de cero jornadas se conserva como condición objetiva del programa.
5. **Economía.** La Tabla 11, XIV 14.8 y XVI OE5 presentan primero 392 y 793 pagos mensuales como umbrales de VAN positivo al 12 %, bajo los parámetros evaluados. El escenario proyectado de ocho espacios y 16 pagos mensuales se interpreta como marcha blanca técnica controlada. Su VAN negativo y la necesidad de aportes permanecen explícitos.
6. **Diccionario físico.** B.022 se titula «Auditoría histórica por lotes de control de acceso», sin el identificador legado en el índice. La ficha explica y conserva el nombre físico de referencia. Se comparan las 110 fichas, sus cuadrículas y sus restricciones; no se renombra ficticiamente el esquema ni se elimina una tabla para ocultar su origen histórico.
7. **Presentación y nombres.** Se verifican «espaciGo» en los rótulos e índices señalados y en el subtítulo RNF. El operador `&&` y las comillas contractuales ya están correctos en la fuente: su representación se verifica también en Word y PDF. Se ajusta el ancho de columnas y se conservan juntas las filas de las tablas 11 y 13 para evitar continuaciones de una sola frase.
8. **Enlaces.** Los enlaces AWS de red Fargate y recuperación RDS conservan guiones ASCII y destino completo. Se presentan en línea propia, con tamaño controlado en esos dos URL extensos. La verificación comprueba texto y destino en Word y PDF, junto con Ley 21.719 y ST_DWithin.
9. **Prevención.** La guarda de compilación controla también los identificadores y términos retirados. El generador de planificación actualiza fichas y actividades sin sobrescribir la narrativa académica de VI/XV. Los insumos de redacción económica conservan el nuevo enfoque al regenerarse.

## Precisiones necesarias

Los 392 y 793 pagos corresponden a umbrales financieros del horizonte evaluado con VAN al 12 %. No se presentan como demanda observada ni como un cociente estático de costos de un solo mes. Los 63 nodos del cronograma comprenden 54 actividades y nueve hitos; la preparación de defensa y transición mantiene su etapa propia después de noviembre.

La denominación física histórica de auditoría se conserva dentro del Anexo D para interpretar correctamente el DDL. Los endpoints de la API y los identificadores de requerimientos y pruebas también permanecen como parte de la especificación académica. Se eliminan las referencias de implementación indicadas, sin sustituir evidencia o datos por afirmaciones de ejecución no comprobadas.

## Evidencias de cierre

- VERIFICACION_FINAL.json: fuentes, remisiones, texto del PDF, figura insertada, diccionario físico y tablas financieras.
- Verificación de enlaces bibliográficos: cuatro URL completos, en una línea y con destinos correctos.
- Verificación económica: 27 tablas preservadas y cuatro flujos completos con 16 partidas; sin cambio de valores.
- Verificación de planificación: índices enlazados y figuras en la página de su rótulo.
- Revisión visual: Word renderizado con la habilidad de documentos; PDF completo renderizado y páginas modificadas inspeccionadas, incluidas las tablas corregidas.

La corrección documental no acredita habilitación productiva de proveedores ni ejecución de ensayos pendientes del desarrollo. Esos límites se conservan en XII–XIII y el Anexo F.

## Publicación

Contenido publicado en origin/main, commit 371bf83. Las doce tareas quedan cerradas con Word/PDF, fuentes, diagramas y comprobaciones versionados.
