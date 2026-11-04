# CAPÍTULO I: INTRODUCCIÓN Y CONTEXTO DEL PROYECTO

## 1.1. Introducción

espaciGo es una plataforma web transaccional para el arriendo flexible de espacios no residenciales en Chile. El proyecto aborda una dificultad de coordinación entre quien ofrece un espacio y quien necesita utilizarlo durante un intervalo determinado. La oferta debe comunicar ubicación, condiciones de uso, precio y disponibilidad. La contratación requiere registrar el acuerdo y controlar que otro arriendo activo no ocupe el mismo intervalo.

El diseño considera oficinas, bodegas, locales comerciales y estacionamientos como ejemplos de aplicación. Cada espacio representa una unidad reservable exclusiva. La misma cuenta puede ofrecer o arrendar según su vínculo con el recurso. La contratación contempla aceptación bilateral, firma electrónica opcional y cobros diferenciados por concepto.

## 1.2. Contexto de mercado y alcance de las fuentes

El mercado de oficinas de Santiago ofrece una referencia acotada de superficie disponible. Para el primer trimestre de 2026, CBRE informa una vacancia de 9,64 % para oficinas clase A y B, mientras que Colliers informa 9,9 % en su reporte de oficinas [@cbre2026; @colliers2026]. Cada tasa corresponde al universo de su respectiva medición. La memoria utiliza estas cifras como contexto del segmento de oficinas.

En bodegas, locales y estacionamientos, el diseño considera escenarios de uso temporal, como almacenamiento estacional, comercio por jornadas y estacionamiento por períodos determinados. La validación comercial requiere medir cada segmento de forma independiente. La tasa de vacancia de oficinas, por sí sola, carece de alcance para estimar la demanda por períodos breves, la adopción de la plataforma o su efecto en la ocupación.

## 1.3. Pertinencia para la ingeniería

La solución plantea tres problemas técnicos complementarios. La búsqueda debe consultar ubicación y atributos sin confundir visibilidad del anuncio con disponibilidad. La reserva debe controlar solapamientos concurrentes mediante una autoridad de ocupación. La contratación debe preservar la emisión y las aceptaciones, aplicar autorización por recurso y conciliar eventos de pago sin reactivar una reserva vencida.

El informe distingue el diseño objetivo ratificado, los resultados del prototipo local con datos sintéticos y las comprobaciones requeridas para integrar proveedores u operar en el entorno objetivo. El Capítulo II delimita el problema. Los capítulos VII a IX especifican requisitos, arquitectura y procesos. Los capítulos X y XI documentan criterios de verificación, evidencia y operación.
