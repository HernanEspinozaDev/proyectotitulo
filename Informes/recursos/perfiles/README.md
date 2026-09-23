# Adaptar una plantilla institucional

`inacap_es1.json` describe la plantilla utilizada en ES1. Su adaptador conserva portada, encabezados y pies, reconstruye índices y reemplaza las instrucciones por el contenido académico. No es un adaptador universal.

## Cuando llegue la plantilla de ES2

1. Conservar el DOCX original en `ES2PT/plantilla/` y leer la rúbrica. Inspeccionar visualmente portada, índices, secciones, estilos y numeración.
2. Examinar `word/document.xml`, `word/styles.xml`, `word/numbering.xml`, encabezados y pies del paquete DOCX. Identificar el punto de inserción y los campos de portada.
3. Si comparte la estructura institucional de ES1, copiar el perfil a `ES2PT/plantilla/perfil.json` con `aprobado: false`. Ajustar metadatos, etiquetas, estilos, tipografía y TOC. Los tamaños se expresan en medios puntos (22 = 11 pt).
4. Si cambia el punto de inserción o las convenciones internas de estilos, implementar y probar otro adaptador común. No habilitar ES1 para sortear un error de compatibilidad.
5. Registrar `sha256_plantilla` con el SHA-256 del DOCX revisado (`Get-FileHash -Algorithm SHA256`). Activar `aprobado: true` tras verificar compatibilidad estructural. Configurar `plantilla` y `perfil` con rutas locales de la entrega.
6. Generar una muestra con portada, capítulos, tabla, figura, cita y anexo; revisar Word visualmente y corregir el perfil. Registrar la evidencia en `contexto.md` antes de declarar el formato aprobado para entrega.

La firma detecta cambios posteriores; no acredita por sí sola una revisión humana. El diagnóstico exige también los estilos y las partes OOXML del adaptador.

`mapa_estilos`, `niveles_titulo`, `campos_portada`, `etiqueta_titulo`, `sin_etiqueta`, `toc`, `fuente` y tamaños son configurables. Las convenciones internas de tablas, rótulos y numeración permanecen en el adaptador institucional; si cambian, adaptar código y pruebas.
