# Entrega única y persistencia de índices

- [x] U01. Comparar el maestro con la última entrega; verificar la integridad de las 28 fuentes y los ocho anexos.
- [x] U02. Guardar los resultados de los tres índices en el Word sin reemplazar el contenido académico ni su maquetación.
- [x] U03. Reconstruir Word y PDF mediante DocSkill con el nombre oficial único.
- [x] U04. Comprobar las siete líneas observadas en fuente, índices del Word y PDF; cotejar todas las páginas y datos con la entrega anterior.
- [x] U05. Retirar las copias de entrega con sufijos; ejecutar las auditorías y publicar en main.

El maestro y la copia entregada en la revisión anterior son binariamente idénticos. La búsqueda exacta de las seis expresiones erróneas no encuentra coincidencias en las fuentes compiladas. La exportación actual actualiza los índices en memoria para el PDF, pero no persiste sus resultados en el Word. La corrección actúa sobre esa diferencia verificable y mantiene el texto aprobado.

## Cierre comprobado

Se conserva un único nombre base de entrega: Tesis_Final_espaciGo, en Word y PDF. Se retiran las cuatro copias con sufijos de revisión; su historia permanece en Git. Se documenta esta regla en AGENTS.md.

La exportación persiste exclusivamente los tres índices calculados en el Word original de DocSkill, con 591 entradas enlazadas y sus marcadores. No se sustituye el cuerpo por una conversión completa de Writer. Se comprueba que el XML académico fuera de índices y marcadores es idéntico al de la entrega anterior, que todas las imágenes mantienen sus bytes y que las 28 fuentes registradas, incluidos los ocho anexos, siguen intactas.

Las 567 páginas del PDF coinciden carácter por carácter con la entrega anterior. Por tanto, la lectura de las siete líneas como «espacio» comunicada por el revisor no se reproduce en la extracción directa de los archivos cotejados. Se verifica «espaciGo» en cada entrada de índice y en el título de la Figura 13, tanto en el Word guardado como en el PDF. La diferencia corregida es la ausencia de resultados persistidos en los campos del Word.

Se renderizan las 567 páginas del Word con la herramienta oficial. Se inspeccionan portada, aprobación, contenido, tablas, figuras y Figura 13. La comparación visual de todas las páginas PDF registra pequeñas diferencias de trazado de las tablas (máximo 0,98 % de píxeles de una página); se inspeccionan también las mayores diferencias, sin pérdida de texto, imágenes ni cambios de paginación. No se declara identidad binaria de los PDF.

Pasan las auditorías de integración económica, planificación, revisión editorial, rótulos e índices, portada, bibliografía y ausencia de rutas de trabajo. Los registros actualizados identifican los maestros actuales.
