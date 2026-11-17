# Edición académica de la evaluación económica

Esta es la versión editorial vigente para incorporar el Capítulo XIV y el Anexo H a la tesis. Presenta el estudio como elaboración del equipo de espaciGo, con decisiones de planificación adoptadas y redacción formal en tercera persona. Conserva los nombres correctos de los tres autores en los metadatos del documento.

El contenido publicable se encuentra en capitulo_xiv_evaluacion_economica.md y anexo_h_evaluacion_economica.md. El Word y el PDF están en build/Evaluacion_economica_espaciGo.docx y build/Evaluacion_economica_espaciGo.pdf. Las 27 tablas tienen rótulo, título y nota de elaboración propia; las referencias externas se citan en la explicación y en las referencias bibliográficas.

Los flujos históricos con GCP, otras comisiones y celdas incompletas no forman parte de esta edición. La extracción de las 26 hojas y del informe se conserva íntegra en los directorios de fuentes y en 03_propuesta para trazabilidad. Esta separación elimina discrepancias entre antecedentes y resultados vigentes sin borrar el material recibido. El modelo numérico activo permanece en 06_escenario_adoptado y no se modifica por esta edición.

Para reconstruir con el Python del entorno documental: `scripts/reconstruir_texto_tesis.py --render --output-dir /tmp/espacigo-redaccion-tesis`. El proceso comprueba fuentes, cifras, referencias, notas y formato nativo de Word. Después se inspeccionan las imágenes de todas las páginas y se registra la revisión visual en verificacion_editorial.json.

El documento presenta presupuestos y resultados proyectados; no los convierte en ventas, pagos, contratos o constitución efectiva. Se eliminan expresiones de ratificación pendiente de las decisiones ya adoptadas. La tasa del 27 % mantiene su carácter de criterio financiero del ejercicio, sin atribuirla a la tributación legal efectiva.

La edición se integra por instrucción del propietario en el Capítulo XIV y Anexo H de tesis_final. La tesis conserva su numeración correlativa de tablas del cuerpo: las once tablas económicas se incorporan como Tablas 14–24. El formato y las cifras de los flujos se conservan; la bibliografía se integra en el Capítulo XVII. El Word y PDF principales se regeneran con build_thesis.py.

Entrega verificada: 25 páginas en PDF y 27 tablas nativas en Word. El cálculo del escenario 06 permanece idéntico al corte numérico anterior.
