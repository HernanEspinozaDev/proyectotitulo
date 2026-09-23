# Plan — Anexo E: historias de usuario en formato de tarjeta (20-09-2026)

## 1. Objetivo

Que cada historia de usuario del Anexo E se presente como en `hu.pdf`: **una tabla de 3 secciones**, en lugar del formato actual (título + texto suelto + lista de criterios). **No se modifica el contenido de ninguna historia**: solo cómo se muestra en el Word.

## 2. Formato de referencia (extraído de `hu.pdf`, 30 páginas, una HU por página)

| Sección | Contenido | Estilo |
| :--- | :--- | :--- |
| 1 (encabezado) | `Código y Nombre de la Historia: HU01 - Registro de nuevo usuario` | negrita, fila de encabezado con fondo |
| 2 (relato) | `**Como** …`, `**Quiero** …`, `**Para que** …` en párrafos separados | texto normal |
| 3 (criterios) | Título `Criterios de Aceptación` + viñetas `•` | lista con viñetas |

Debajo de la tabla, fuera del recuadro, el PDF lleva una línea de nota («Nota: Incluye la interfaz asociada…»).

## 3. Qué se conserva del Anexo E actual

- El texto íntegro del relato (Como / Quiero / Para que) y de los criterios de aceptación.
- Los metadatos de trazabilidad: **Épica**, **Rol**, **Prioridad**, **RF**, **CU**.
- Las notas `*(criterio de interfaz)*` y **Fuera del alcance de la ES1**.
- Los títulos `## HUxx - Nombre` (siguen alimentando el índice de contenido) y las épicas.

## 4. Estrategia: convertir en el generador, no en la fuente

La conversión la hace `generar_informe.py` (`preparar_anexo`), de modo que `docx/anexos/E_historias_de_usuario.md` **queda intacto**. Ventajas:

1. **Cero riesgo de alterar el texto** de las historias (no se retranscribe nada).
2. Si el formato no gusta, se revierte cambiando el generador, no las 35 historias.
3. La fuente sigue siendo la versión «plana» que ya está sincronizada con los RNF/CU.

## 5. Implementación

| Paso | Detalle |
| :--- | :--- |
| 5.1 | `preparar_anexo` detecta el bloque de cada HU (título `## HUxx - …` + metadatos + relato + `### Criterios de Aceptación` + criterios + notas) y lo rearma como tarjeta |
| 5.2 | La tarjeta se emite como **tabla grid de Pandoc** generada por código: 3 filas, 1 columna, bordes alineados automáticamente (ancho = línea más larga, sin recortar texto) |
| 5.3 | Primera fila = `**Código y Nombre de la Historia:** HUxx - Nombre`; segunda = relato en párrafos; tercera = `**Criterios de Aceptación**` + viñetas dentro de la celda |
| 5.4 | Debajo de la tabla: los metadatos de trazabilidad (Épica / Rol / Prioridad / RF / CU) y luego las notas (interfaz y fuera de alcance), para que la tarjeta empiece igual que el PDF |
| 5.5 | Las tarjetas **no** llevan rótulo «Tabla E.n» ni nota «Fuente:» (son el formato de la historia, no ilustraciones); la validación 43 se ajusta para reconocerlas y el índice de ilustraciones de E mantiene sus 3 tablas reales |
| 5.6 | Salto de página antes de cada tarjeta (como el PDF, que usa una página por historia), controlado por la constante `HU_UNA_POR_PAGINA` |

## 6. Decisiones y opciones

1. **Una historia por página:** se aplica (igual que el PDF). Si se prefiere flujo continuo, basta poner `HU_UNA_POR_PAGINA = False`.
2. **Color de los criterios:** en el PDF van en rojo; aquí se mantienen en negro Calibri 11 como todo el informe (el rojo se puede activar si lo piden).
3. **Ubicación de la trazabilidad:** debajo de la tabla, no dentro, para respetar las 3 secciones del formato de referencia.
4. **Criterios de interfaz:** pasan a ser la línea «Nota: …» posterior a la tabla, igual que en el PDF.

## 7. Verificación

1. Contar tarjetas: 35 (una por HU) y comprobar que cada tabla tiene exactamente 3 filas.
2. Comparar el texto de cada HU antes y después (normalizado) para demostrar que no cambió.
3. Regenerar los anexos y correr las validaciones: 47/47 en 0 errores y 0 advertencias.
4. Revisar el índice de contenido (debe perder las 35 entradas repetidas «Criterios de Aceptación») y el índice de ilustraciones de E.

## 8. Resultado (aplicado el 20-09-2026)

| Verificación | Resultado |
| :--- | :--- |
| Tarjetas generadas | **35** (una por historia), todas de **3 filas** |
| Estructura interna | fila 1: 1 párrafo (encabezado) · fila 2: 3 párrafos (Como / Quiero / Para que) · fila 3: título + lista real de viñetas |
| Texto de las historias | intacto: los 35 relatos, los 35 bloques de metadatos y todas las notas están en el documento (comparación automática contra la fuente) |
| Índice de ilustraciones de E | solo las 3 tablas propias (las tarjetas no llevan rótulo «Tabla E.n» ni nota «Fuente:») |
| Paginación | 45 páginas: cada historia empieza en una página nueva y la tarjeta no se corta entre páginas (salvo las que superan una página completa) |
| Validaciones | 43 (rótulos y notas de anexos), 44, 45, 46 y 47 en **OK** |

Los nombres de los apartados «Criterios de Aceptación» dejan de ser títulos de Word: pasan a ser la primera línea de la tercera sección de la tarjeta, como en `hu.pdf`.

### Cómo se ve

```
+--------------------------------------------------------------+
| Código y Nombre de la Historia: HU01 - Registro de nuevo...  |   <- fila de encabezado (negrita)
+==============================================================+
| Como visitante de la plataforma,                             |
|                                                              |
| Quiero registrarme ingresando mis datos personales...,       |
|                                                              |
| Para que pueda acceder a las funcionalidades del sistema...  |
+--------------------------------------------------------------+
| Criterios de Aceptación                                      |
|                                                              |
| - El formulario de registro debe solicitar...                |
| - El sistema debe validar que el correo...                   |
+--------------------------------------------------------------+
Épica: E1 · Rol (Como): Visitante · Prioridad: Alta
RF: RQF-001 a RQF-010, RQF-186, RQF-187, RQF-213 · CU: CU-01, CU-02

   (criterio de interfaz) ...
   Fuera del alcance de la ES1: ...
```

### Opciones que quedaron sin aplicar (se activan en un minuto)

1. Criterios en rojo, como en el PDF de referencia (hoy van en negro Calibri 11, igual que el resto del informe).
2. Encabezado de la tarjeta con fondo gris, como el PDF (hoy usa el formato de encabezado de tabla del informe).
3. Flujo continuo en vez de una historia por página (`HU_UNA_POR_PAGINA = False`).

