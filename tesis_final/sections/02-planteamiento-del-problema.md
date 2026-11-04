# CAPÍTULO II: PLANTEAMIENTO Y DIAGNÓSTICO DEL PROBLEMA

## 2.1. Descripción de la Problemática Operativa

La gestión y arriendo de inmuebles comerciales, corporativos e industriales en Chile experimenta una ineficiencia estructural originada por la rigidez de los mecanismos tradicionales de intermediación. Mientras la dinámica económica contemporánea exige flexibilidad, inmediatez y acceso modular a infraestructura física (oficinas para trabajo colaborativo, bodegaje modular para *e-commerce*, locales para ventas estacionales y estacionamientos diurnos), el ecosistema inmobiliario continúa operando bajo premisas analógicas diseñadas para el siglo pasado (Cámara Chilena de la Construcción [CChC], 2024).

La problemática se manifiesta a través de un desacople operativo crítico entre dos actores principales:

1. **Propietarios e Inversionistas Inmobiliarios:** Enfrentan activos subutilizados o completamente desocupados que devengan costos operacionales continuos (gastos comunes ordinarios, contribuciones territoriales fiscales, seguros contra incendio y cuotas de mantenimiento). Al estar sujetos a canales de corretaje tradicionales, los propietarios tardan entre 6 y 18 meses en colocar un activo bajo contratos fijos de 1 a 3 años, asumiendo el riesgo de incobrabilidad y la imposibilidad de rentabilizar ventanas temporales ociosas entre arrendatarios sucesivos.
2. **Arrendatarios Temporales (Pymes, Emprendedores y Profesionales):** Se ven sistemáticamente marginados del acceso formal a infraestructura física. Los modelos de arriendo convencionales imponen barreras de entrada desproporcionadas: acreditación de antecedentes comerciales impecables (antigüedad de giro superior a dos años), entrega de múltiples meses de garantía en efectivo o avales bancarios, y el compromiso forzoso de plazos anuales, aun cuando el usuario solo requiere un espacio por días, semanas o temporadas específicas (como campañas de CyberDay, grabaciones audiovisuales o ventas efímeras).

### Limitaciones de los Canales Existentes en el Mercado Chileno

Al contrastar la oferta de servicios disponibles en el país, se evidencia un vacío tecnológico que perpetúa la ineficiencia:

*   **Portales de Clasificados Tradicionales (Mercado Libre Inmuebles, Yapo, Portal Inmobiliario):** Operan exclusivamente como vitrinas de anuncios estáticos. No modelan la disponibilidad en tiempo real, no permiten la reserva ni el pago en línea, carecen de verificación de identidad de las partes y no proveen ningún marco de custodia financiera ni de resolución de disputas.
*   **Corredores de Propiedades Tradicionales:** Actúan mediante intermediación personal y analógica, cobrando comisiones elevadas (típicamente el 50% de un mes de renta a cada parte) y orientando sus esfuerzos exclusivamente a transacciones de largo plazo que justifiquen su costo operativo. Carecen de herramientas digitales para gestionar arriendos rotativos o fraccionados.
*   **Empresas de Mini-Bodegas y Almacenamiento Especializado (Mudango, AkiKB, Guardabox):** Aunque ofrecen almacenamiento de menor escala, funcionan como recintos industriales centralizados con tarifas fijas elevadas y esquemas de mudanza propietarios, impidiendo la transacción directa entre particulares o empresas que disponen de metros cuadrados sobrantes en zonas urbanas estratégicas.

---

## 2.2. Diagrama de Contexto As-Is (Operación Actual sin la Plataforma)

Para comprender el flujo operativo actual y evidenciar los puntos de fricción, riesgo y sobrecosto que experimentan los actores en ausencia de una plataforma tecnológica unificada, se modela a continuación el Diagrama de Contexto *As-Is* del ecosistema inmobiliario tradicional.

**Figura 1**  
*Diagrama de Contexto As-Is del Ecosistema Inmobiliario Tradicional*

![](assets/figuras/fig01_contexto_as_is.png)

*Nota.* Elaboración propia en base al levantamiento empírico del mercado de corretaje y arriendos comerciales tradicional.

---

## 2.3. Tabla Estandarizada de Causas, Problema Operativo y Efectos

En cumplimiento estricto de las directrices metodológicas docentes, se reemplaza la representación gráfica informal de árbol de causas por una **matriz analítica estructurada**. Esta matriz clasifica las causas raíz del problema, su manifestación operativa directa en el negocio y el impacto cuantificable sobre el mercado:

**Tabla 1**  
*Matriz de Diagnóstico Causa Raíz, Problema Operativo y Consecuencia de Negocio*

| Dimensión Operativa | Causa Raíz | Problema Operativo Específico | Efecto / Consecuencia Cuantificable |
|---|---|---|---|
| **Contractual y Temporal** | Modelo legal rígido basado en contratos tradicionales anuales. | Obligación forzosa de permanencia mínima de 12 a 36 meses. No existen marcos dinámicos para arriendos por horas, días o semanas. | • Vacancia prolongada de 6 a 18 meses en activos Clase B y C (Colliers International, 2024).<br>• Pérdida de rentabilidad para el 100% de ventanas temporales ociosas. |
| **Financiera y Barreras de Entrada** | Exigencia de avales solidarios, antecedentes comerciales históricos y múltiples garantías. | Exclusión masiva de emprendimientos nuevos, empresas de comercio electrónico en fase de validación y profesionales independientes. | • Marginación del 78% de pequeñas empresas que carecen de balance anual con utilidad contable para calificar ante corredoras tradicionales (CChC, 2024). |
| **Transaccional y Confianza** | Inexistencia de mecanismos de retención y custodia imparcial de fondos (*Escrow*). | Riesgo de impago o daños para el arrendador; riesgo de estafa o retención arbitraria de garantía para el arrendatario. | • Disputas legales de alto costo sin resolución arbitral.<br>• Miedo mutuo que paraliza la transacción directa entre particulares (*peer-to-peer*). |
| **Tecnológica y Disponibilidad** | Publicación en vitrinas estáticas de clasificados sin sincronización horaria ni geoespacial. | Imposibilidad de consultar disponibilidad instantánea de un inmueble ni reservar en línea en fechas específicas. | • Tiempo de colocación promedio superior a 90 días por anuncio.<br>• Fricción de coordinación: intercambio de 15 a 20 mensajes manuales por consulta. |
| **Legal y Documental** | Redacción manual de contratos en papel y exigencia de firma física notarial presencial. | Proceso burocrático lento que demanda de 3 a 7 días hábiles y costos notariales desproporcionados para operaciones breves. | • Inviabilidad económica para arriendos menores a 30 días, donde el arancel notarial supera el valor del canon de arriendo. |
| **Inspección y Estado Físico** | Ausencia de protocolos objetivos y verificables de entrega y recepción del inmueble. | Los arriendos analógicos no registran el estado físico del bien al inicio ni al término, dependiendo de declaraciones verbales. | • Imposibilidad de determinar con exactitud el origen de daños o desgastes en el 85% de las disputas de devolución de garantía. |
| **Privacidad y Datos Personales** | Intercambio de documentos de identidad sensibles mediante correo no cifrado o mensajería instantánea. | Exposición masiva de datos personales, cédulas de identidad y antecedentes societarios en canales vulnerables sin cumplimiento de la Ley N° 21.719. | • Riesgo inminente de suplantación de identidad y sanciones legales por tratamiento ilícito de datos personales según la nueva normativa chilena. |

*Nota.* Elaboración propia en base al diagnóstico de la industria inmobiliaria y levantamiento de causas raíz del mercado comercial tradicional (CChC, 2024; Colliers International, 2024).

---

## 2.4. Justificación de la Complejidad y Delimitación de Impacto

La resolución de la problemática diagnosticada no constituye un mero desarrollo de un sitio web informativo, sino la ingeniería de una **plataforma multilateral transaccional de alta complejidad sistémica**. La complejidad del proyecto radica en la intersección indivisible de cuatro dominios de la Ingeniería de Software:

1. **Complejidad de Concurrencia y Persistencia Espaciotemporal:** El sistema debe gestionar miles de reservas simultáneas sobre intervalos de tiempo fraccionados (horas y días) asociados a polígonos geoespaciales. Para erradicar el riesgo de sobre-reserva (*double-booking*), la arquitectura traslada el control de consistencia al motor de datos mediante PostgreSQL 18 y PostGIS 3.6, aplicando operadores de exclusión temporal y espacial indexados mediante `GiST`, garantizando transacciones estrictamente ACID.
2. **Complejidad Financiera y Seguridad de Pagos (*Escrow*):** La plataforma opera como una bóveda transaccional. Debe integrarse con pasarelas de pago digitales (Mercado Pago), ejecutar divisiones automáticas de pago (*split payments*), congelar cupos de garantía en tarjetas de crédito sin captura inmediata, y liberar o reembolsar fondos en función del cumplimiento de los hitos de *check-in* y *check-out*.
3. **Complejidad Legal Documental y Trazabilidad:** La plataforma integra generación dinámica de instrumentos contractuales en formato PDF con inyección de variables verificadas. Estos contratos se acoplan con proveedores de firma electrónica remota (FirmaVirtual) y se articulan con la Ley N° 21.461 ("Devuélveme mi Casa"), asegurando que cada estadía cuente con respaldo jurídico oponible sin requerir comparecencia física notarial.
4. **Gobernanza de Ciberseguridad y Privacidad (Ley N° 21.719):** Al procesar validaciones de identidad civil (KYC con Registro Civil) y tributaria (KYB con el SII), la solución incorpora arquitecturas de seguridad en reposo y en tránsito, control de acceso basado en roles (RBAC) y un protocolo de eliminación lógica y purga de réplicas (*anti-restauración replay*) para honrar los derechos ARCO de los titulares.

### Delimitación del Alcance del Proyecto

Para asegurar la viabilidad técnica y financiera de la solución dentro del marco temporal del proyecto de titulación:
*   **Alcance Geográfico:** El producto se delimita inicialmente a la Región Metropolitana de Santiago, abarcando comunas con mayor concentración de oferta y demanda (Santiago Centro, Providencia, Las Condes, Pudahuel y Quilicura).
*   **Categorías de Espacios Inmobiliarios:** Se consideran exclusivamente cuatro tipos de inmuebles no residenciales: oficinas/privados, módulos de bodegaje industrial/flex, locales comerciales urbanos y estacionamientos vehiculares.
*   **Rol de la Plataforma:** La solución actúa como un **facilitador tecnológico, transaccional y probatorio**. No interviene como parte contractual arrendadora ni asume responsabilidad civil directa sobre los bienes físicos, circunscribiendo su responsabilidad al correcto funcionamiento del software, la custodia financiera y la custodia de evidencias digitales.
