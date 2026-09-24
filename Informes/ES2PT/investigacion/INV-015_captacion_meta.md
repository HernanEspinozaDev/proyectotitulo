# INV-015 — Captación medible con Meta Ads

- **Estado:** investigación documental y diseño de experimento; no se han creado campañas, contratado medios, obtenido clientes ni medido retorno.
- **Consulta:** 23-09-2026. Las funciones, políticas y precios de publicidad deben revisarse de nuevo en la cuenta publicitaria antes de ejecutar.
- **Línea base:** el informe final de ES1 plantea un marketplace con comisión por reserva y categorías de arriendo diversas. [INV-011](INV-011_muestra_precios_y_demanda.md) muestra oferta publicada, no demanda; [INV-013](INV-013_monetizacion_pagos_y_promocion.md) propone destaques internos como ingreso adicional, separado de Meta Ads.
- **Destino:** análisis tecnológico 2.1–2.2 y Anexo A, sujeto a integración posterior. No se cambia la línea base ES1 ni se afirma implementación.

## Evidencia y límite de las fuentes

| Fuente primaria consultada | Dato utilizable | Límite para EspaciGo |
| --- | --- | --- |
| [Meta Blueprint: selección de objetivos](https://www.facebookblueprint.com/student/path/219699-selecting-objectives-course) y [generación de contactos](https://www.facebookblueprint.com/student/catalog/list?category_ids=7522-get-results-that-matter-to-your-business) | El objetivo, el lugar de conversión y la meta de rendimiento se eligen según el resultado de negocio; Meta distingue campañas para tráfico, contactos y ventas. | No demuestra que un objetivo produzca reservas o publicaciones para EspaciGo. La interfaz y elegibilidad exactas se comprueban en la cuenta. |
| [Meta Blueprint: públicos](https://www.facebookblueprint.com/student/catalog/list?category_ids=7506-your-guide-to-audience-targeting) | Permite estudiar públicos y fuentes de datos, incluidos Pixel y API de Conversiones. | No garantiza precisión geográfica ni habilita usar atributos sensibles. |
| [Meta Blueprint: presupuesto](https://www.facebookblueprint.com/student/collection/238520/path/551361) y [subasta publicitaria de Meta](https://about.fb.com/wp-content/uploads/2023/01/Toward_fairness_in_personalized_ads.pdf) | El presupuesto se planifica para compra en subasta o reserva; la entrega en subasta depende de más factores que la puja. | No publica una tarifa fija CLP por clic, contacto o reserva para Chile y este proyecto. No proyectar conversiones a partir del gasto solamente. |
| [Meta Blueprint: resultados en Ads Manager](https://www.facebookblueprint.com/student/path/211546-meta-ads-manager-campaigns-analysis-course) y [diseño de pruebas A/B](https://www.facebookblueprint.com/student/path/219763-ab-test-conversion-brand-lift-course) | Meta ofrece reportes de campaña y métodos experimentales para contrastar hipótesis. | Una conversión atribuida por Meta no es necesariamente una reserva pagada ni demuestra incrementalidad causal. |
| [Meta, actualización de Pixel y API de Conversiones (15-04-2026)](https://about.fb.com/ltam/news/2026/04/eliminar-barreras-tecnicas-para-ayudar-a-empresas-de-todos-los-tamanos-a-aprovechar-mas-sus-anuncios/) | Pixel y API comunican eventos web para medición y optimización; Meta advierte que el anunciante debe evitar transmitir información sensible. | No se han implementado ni configurado; la ventaja promedio anunciada por Meta para otros anunciantes no se transfiere a EspaciGo. |
| [Meta, política y entrega de anuncios de vivienda](https://about.fb.com/news/2023/01/an-update-on-our-ads-fairness-efforts/) y [biblioteca oficial](https://es-la.facebook.com/ads/library/api) | La categoría de vivienda existe; Meta describe restricciones de segmentación por edad, género y código postal para anunciantes de EE. UU., Canadá y determinados países europeos. | **No** concluir de esa fuente que idénticas restricciones rigen en Chile ni que toda oficina, quincho o bodega sea «vivienda». Clasificar cada creatividad y confirmar requisitos vigentes de la cuenta antes de publicar. |

La fuente sobre subasta y la de restricciones de vivienda tienen fecha de 2023; sirven de antecedente, no sustituyen las reglas vigentes en el administrador de anuncios al lanzar una campaña en Chile. Algunas páginas de ayuda de Meta requieren sesión; por ello se registran solo capacidades comprobadas en fuentes públicas y se dejan sin confirmar los controles concretos de la cuenta.

## Diseño de captación propuesto

EspaciGo necesita **dos embudos**, porque atraer arrendatarios a una zona sin espacios disponibles consume presupuesto sin crear una reserva posible. Ambos cubrirían progresivamente todas las categorías contempladas en ES1; experimentar primero en celdas con inventario real no excluye categorías del alcance del producto. La unidad de análisis es `zona × categoría × duración/modalidad`, no un ticket promedio de arriendos heterogéneos.

| Embudo | Conversión de negocio que se intentaría medir | Creatividad y destino propuestos | Puerta previa |
| --- | --- | --- | --- |
| Oferta: arrendadores | Contacto consentido → cuenta validada → publicación aprobada y disponible. | Propuesta de publicar un tipo de espacio concreto, con condiciones y comisión transparente; destino a formulario o página de alta identificada. Un contacto no equivale a inventario utilizable. | Proceso de alta, moderación, contrato y soporte definidos. |
| Demanda: arrendatarios | Visita válida → búsqueda con resultado elegible → solicitud → reserva pagada no anulada. | Mensaje por necesidad y tipo de espacio, con página de categoría/zona y precio/condiciones reales, nunca un espacio inexistente. | Oferta aprobada, calendario utilizable y flujo de pago comprobable. |

**Secuencia:** (1) preparar una página y mensaje comprobables para una celda elegible; (2) ensayar adquisición de oferta y registrar publicación *aprobada*, no solo formulario; (3) cuando exista inventario, ensayar demanda para esa misma celda; (4) comparar calidad y costo de las cohortes antes de ampliar a otras zonas y modalidades. El objetivo de campaña de Meta se elegiría según la señal que realmente pueda medirse: contactos para captar arrendadores, tráfico cualificado si solo está lista la página informativa, y optimización por reserva pagada únicamente cuando exista evento confiable y volumen suficiente. Es una propuesta operativa, no una campaña configurada.

Segmentar inicialmente por geografía **permitida por Meta en la cuenta y por la categoría del anuncio**, usando el mensaje y la página de destino para distinguir oficina, sala, bodega, estacionamiento, local, quincho o parcela. No prometer radios mínimos, filtros demográficos, audiencias similares o exclusiones específicas: varían según política, clasificación y disponibilidad de la cuenta. Los anuncios deben evitar criterios discriminatorios y afirmaciones de disponibilidad o precio sin respaldo. Si se incorpora vivienda en alguna modalidad futura, revisar su categoría especial y restricciones aplicables *antes* de configurar públicos; la publicación comercial/temporal no se clasifica en bloque por inferencia.

## Presupuesto y control de caja

El Anexo A ya registra **357.000 CLP de caja como supuesto de «captación» durante seis meses**, equivalentes a 59.500 CLP/mes *si se distribuyeran uniformemente*. Esa línea no es una tarifa ni una asignación aprobada a Meta. Un ensayo de Meta debe financiarse **dentro de ese techo**, reservar una parte para otras acciones de adquisición y documentar monto, período y fuente de aprobación antes de gastar. Si se destinara el techo completo a Meta, se agota la partida; no se suman otros 357.000 CLP al flujo. La mezcla entre oferta y demanda tampoco se fija antes de conocer inventario. Sin cuenta publicitaria, método de cobro y campaña, no se conocen CPC/CPM/CPL locales ni impuesto efectivo de esa factura; el gasto de caja y tratamiento contable se conciliarán con comprobantes reales.

## Medición y criterio de decisión

El tablero del ensayo guardaría campaña, fecha, categoría, zona, mensaje, objetivo, presupuesto autorizado y gasto observado; Ads Manager aportaría impresiones, alcance, clics y resultados reportados. Una URL etiquetada con parámetros de campaña y eventos **propios** vincularía, con controles de privacidad, visitas a registros, publicaciones aprobadas y reservas con estado pagado. Registrar cancelaciones, reembolsos y duplicados; una visita o «lead» no se contará como ingreso. Pixel/API de Conversiones solo se activarían tras revisar información al usuario, base de tratamiento, minimización, contratos y matriz de datos del Anexo B. No enviar nombres, teléfonos, direcciones exactas de espacios, datos de pago ni detalles sensibles en parámetros de URL o eventos. El informe no presupone consentimiento ni cumplimiento ya acreditados de las leyes 19.628/21.719.

| Indicador propuesto | Fórmula/lectura | Estado actual |
| --- | --- | --- |
| Costo por publicación utilizable | Gasto atribuible a oferta ÷ publicaciones aprobadas y disponibles de la cohorte. Si el denominador es cero, informar «no calculable». | Sin campaña ni publicaciones medidas. |
| Costo por reserva nueva | Gasto atribuible a demanda ÷ reservas pagadas, no anuladas, de nuevos clientes en ventana definida. | Sin campaña ni reservas medidas. |
| Contribución después de adquisición | Comisión neta propia − pasarela − otros costos variables de la reserva − costo de adquisición asignado; excluir fondos del arrendador y garantías. | Solo escenarios hipotéticos del Anexo A; no margen observado. |
| Incrementalidad | Diferencia de resultados entre grupos comparables con y sin exposición/campaña, cuando el volumen permita un experimento. | No estimable hoy; la atribución por clic no prueba causalidad. |

Antes del ensayo, fijar por escrito ventana de atribución, reglas de deduplicación y umbrales de decisión. Detener una celda si el gasto llega al tope autorizado sin producir oferta utilizable o una señal de demanda que justifique seguir; ampliar solo con contribución y capacidad operacional plausibles. Meta Blueprint contempla pruebas A/B y de incremento, pero un piloto pequeño podría no tener potencia para demostrar efecto: informar intervalos y limitaciones, no declarar éxito por un clic barato.

## Relación con los destaques dentro de EspaciGo

Meta Ads es **costo de EspaciGo para captar sus dos lados**. El paquete «Patrocinado» de [INV-013](INV-013_monetizacion_pagos_y_promocion.md) sería **ingreso eventual pagado por el arrendador dentro del buscador propio**, ligado a zona, categoría y duración; no lo vende Meta ni genera ingreso por las impresiones de la campaña externa. Sus métricas serían impresiones del resultado patrocinado, clics, reservas y canibalización del orden orgánico. El gasto Meta puede aumentar tráfico, pero no se debe atribuir a ese tráfico una tasa de compra de destaques sin medirla. El VAN base conserva cero ingresos de publicidad; vender el paquete requiere producto, condiciones, factura y demanda comprobados. No se propone usar Meta Audience Network para mostrar anuncios ajenos dentro de EspaciGo: es otro producto y modelo económico.

## Pendientes verificables para integración

1. [[PENDIENTE: confirmar acceso a cuenta publicitaria, país de facturación, medio de pago, controles de gasto, política y categoría de cada anuncio en Chile; conservar captura y fecha sin publicar una campaña por este documento.]]
2. [[PENDIENTE: confirmar inventario aprobado, modalidad, ubicación publicable, calendario y precio final por cada celda antes de comprar demanda.]]
3. [[PENDIENTE: definir responsables, presupuesto de prueba dentro de los 357.000 CLP, calendario, hipótesis, criterios de pausa y método de conciliación de facturas.]]
4. [[PENDIENTE: aprobar aviso y base de tratamiento para medición Pixel/API, implementar eventos propios y comprobar que no salen datos sensibles.]]
5. [[PENDIENTE: ejecutar campaña/experimento y registrar gasto, alcance, contactos, publicaciones aprobadas, reservas netas, cancelaciones y costo real por lado; sin ello no se puede estimar retorno.]]
