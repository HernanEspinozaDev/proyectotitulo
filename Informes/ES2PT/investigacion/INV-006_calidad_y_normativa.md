# INV-006 — Calidad, normas y referencias jurídicas

- Estado: fuentes primarias consultadas; aplicabilidad y evidencia de conformidad pendientes.
- Fecha de consulta: 2026-09-23.
- Sección ES2: `secciones/05_02_normas.md`.
- Base inmutable: informe final ES1, «Requerimientos no funcionales», «Seguridad, privacidad y protección de datos personales» y «Definición de arquitectura TI»; anexo C, RNF-013–018, 021, 025–026, 029, 042–043.

## Pregunta y método

¿Qué referencias de ES1 conviene incorporar al desarrollo y qué afirmaciones requieren corrección o verificación? Se cotejaron las menciones y requisitos de ES1 con catálogos oficiales de normas, el W3C, PCI SSC y LeyChile. Los catálogos verifican edición y propósito general; el texto completo de algunas normas tiene acceso restringido. No se ha evaluado el producto.

## Fuentes y hallazgos

| Fuente primaria | Hallazgo verificable | Relación con ES1 y decisión ES2 |
| --- | --- | --- |
| ISO, [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) | Edición 2 vigente; el modelo de producto contiene nueve características. | **Amplía/corrige clasificación:** mapear los RNF de ES1 sin afirmar que sus 11 categorías sean idénticas a la edición 2023. |
| IEEE, [ISO/IEC/IEEE 29148:2018](https://standards.ieee.org/ieee/29148/6937/) y [IEEE 830:1998](https://standards.ieee.org/ieee/830/1222/) | 29148:2018 está activo; 830 es antecedente reemplazado. | **Actualiza el método:** revisar calidad y trazabilidad de requisitos de ES1 sin modificar su entrega. |
| W3C, [WCAG 2.1](https://www.w3.org/TR/WCAG21/) y [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Ambas son recomendaciones; 2.2 añade criterios y no retira la obligación documental que ES1 fijó como 2.1 AA. | **Confirma con opción futura:** evaluar 2.1 AA; decidir por separado si se adopta 2.2. |
| PCI SSC, [biblioteca PCI DSS v4.0.1](https://www.pcisecuritystandards.org/document_library/) y [orientación SAQ](https://www.pcisecuritystandards.org/wp-content/uploads/2024/10/SAQs_for_PCI_DSS_v4.0.1_Bulletin.pdf) | La validación depende de elegibilidad, modalidad y entorno de pagos. | **Corrige la inferencia de RNF-025:** tokenizar y no guardar PAN/CVV no demuestran «estricto cumplimiento». Determinar alcance con proveedor. |
| ISO, [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) | Requisitos de un sistema de gestión de seguridad. | **Amplía como guía:** usar inventario, riesgo y revisión de controles; no afirmar certificación. |
| LeyChile, [Ley 19.799](https://www.bcn.cl/leychile/navegar?idNorma=196640) y [Ley 21.461](https://www.bcn.cl/leychile/navegar?idNorma=1178004) | Firma electrónica y efectos jurídicos tienen condiciones; Ley 21.461 modifica reglas de arrendamiento de predios urbanos. | **Deja pendiente aplicabilidad:** ES1 no demuestra que todos los tipos de espacio requieran el mismo contrato ni que la ley obligue a usar API o firma avanzada. |
| LeyChile, [Ley 21.719](https://www.bcn.cl/leychile/navegar?i=1209272) y [Ley 19.628 vigente](https://www.bcn.cl/leychile/navegar?idNorma=141599) | La primera tiene vigencia diferida al 01-12-2026 e incorpora en el artículo 14 quáter protección desde el diseño y por defecto; la segunda rige el tratamiento de datos al 23-09-2026. | **Decisión del proyecto:** aplicar la Ley 21.719 como criterio de diseño desde ES2, sin presentarla como vigente en la entrega del 03-11-2026. El plazo de 72 h de RNF-026 no se verificó como exigencia legal. |

## Impacto y decisión

La matriz de 5.2 enlaza cada referencia con un motivo, un control y evidencia futura. Por instrucción del usuario, **la Ley 21.719 es una línea de diseño de ES2 desde el inicio del desarrollo**, aunque su entrada en vigencia sea posterior a la entrega. Esto exige inventariar tratamientos y permisos por flujo, minimizar datos, diseñar el ejercicio de derechos y decidir conservación/supresión antes de construir tablas y API. El Anexo A inicia la matriz de tratamientos y PT-16 plantea una prueba. Una revisión de riesgos jurídicos debe resolver el tipo de contrato/firma y la convivencia de supresión/anonimización con RNF-042/043. No se cambia ni califica el texto cerrado de ES1.

[[PENDIENTE: acordar y completar la matriz por categoría, revisar con asesoría competente fundamentos/excepciones, firma y arrendamiento; implementar y probar controles de privacidad, acordar accesibilidad y modalidad de pago y conservar resultados.]]
