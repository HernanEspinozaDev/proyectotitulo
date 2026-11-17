# Revisión de la carta Gantt recibida de Erick

La revisión principal está en `REVISION_CARTA_GANTT_ERICK.md`. El archivo recibido se analiza en lectura y no se modifica ni se integra todavía en la tesis.

La carpeta `01_extraccion` conserva el inventario, los datos extraídos y las comprobaciones. Los archivos generados documentan fechas y dependencias almacenadas; no representan una reprogramación aprobada.

Para reproducir la extracción, utilizar un entorno Python aislado con Java, `mpxj==16.10.0` y `JPype1==1.7.1`:

```bash
python scripts/extraer_mpp.py /ruta/al/espacigo.mpp
python scripts/auditar_extraccion.py
```

El archivo fuente permanece en su ubicación local y no se copia al repositorio. La revisión se conserva separada del Capítulo VI, el Capítulo XV y el Anexo G. La fase siguiente requiere corregir y acordar el cronograma con sus responsables antes de utilizarlo como línea base de la tesis.
