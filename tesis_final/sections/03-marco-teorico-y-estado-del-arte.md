# CAPÍTULO III: MARCO TEÓRICO Y ESTADO DEL ARTE

## 3.1. Fundamentos Conceptuales de Plataformas Multilaterales y Prop-Tech

El sector inmobiliario digital contemporáneo se sustenta en la convergencia de dos conceptos teóricos fundamentales: los **mercados de dos lados o plataformas multilaterales** (*two-sided markets*) y el paradigma tecnológico de las **Prop-Tech** (*Property Technology*).

De acuerdo con Rochet y Tirole (2003), una plataforma multilateral es una organización económica en la cual dos o más grupos diferenciados de usuarios interactúan a través de un intermediario central que reduce los costos de búsqueda, negociación y transacción. En estas plataformas, el valor percibido por un grupo de participantes depende directamente del tamaño y la actividad del grupo contraparte, fenómeno denominado **efecto de red cruzado o indirecto** (*cross-side network effects*) (Armstrong, 2006). En el contexto del arrendamiento inmobiliario flexible, la plataforma genera externalidades de red positivas: una mayor densidad y diversidad de espacios físicos disponibles atrae a un volumen superior de arrendatarios demandantes, lo cual, a su vez, incentiva a nuevos propietarios a listar metros cuadrados ociosos.

Por su parte, el movimiento *Prop-Tech* engloba el conjunto de soluciones de software, arquitecturas en la nube y modelos analíticos diseñados para digitalizar, optimizar y flexibilizar los procesos de comercialización, gestión, valoración y operación de bienes raíces (Baum, 2020). Tradicionalmente, la industria inmobiliaria operaba bajo una lógica de propiedad y arrendamiento pasivo de largo plazo. El paradigma *Prop-Tech* transforma el espacio físico en un **servicio dinámico bajo demanda** (*Space-as-a-Service* o *SPaaS*), permitiendo fraccionar la capacidad instalada en unidades mínimas de tiempo (horas o jornadas) y dimensiones modulares (escritorios, módulos de almacenamiento o locales transitorios) (Baum, 2020).

---

## 3.2. Patrones Arquitectónicos Modernos: Monolito Modular vs. Arquitectura Hexagonal

El diseño de software empresarial para plataformas transaccionales exige seleccionar patrones arquitectónicos que equilibren desacoplamiento, mantenibilidad y rendimiento bajo condiciones de concurrencia:

### 3.2.1. Arquitectura Hexagonal (Puertos y Adaptadores)

Propuesta formalmente por Alistair Cockburn (2005), la **Arquitectura Hexagonal** (*Ports and Adapters*) postula la separación estricta entre la lógica de negocio central (el dominio de la aplicación) y los mecanismos de entrada y salida externos (interfaces de usuario, bases de datos, pasarelas de pago y servicios de mensajería).

**Figura 2**  
*Patrón de Arquitectura Hexagonal (Puertos y Adaptadores)*

![](assets/figuras/fig02_arquitectura_hexagonal.png)

*Nota.* Adaptado de Cockburn (2005) y Martin (2017).

En este patrón, el núcleo de dominio define **Puertos** (interfaces abstractas) para declarar las operaciones requeridas, mientras que los **Adaptadores** implementan dichas interfaces contra tecnologías concretas. Este diseño garantiza el principio de inversión de dependencias (*Dependency Inversion Principle* de SOLID), permitiendo que la lógica transaccional de arriendos, cálculos de comisiones y estados de reserva sea completamente agnóstica a los motores de persistencia o pasarelas financieras subyacentes (Martin, 2017).

### 3.2.2. Monolito Modular vs. Microservicios Distribuidos

La literatura de ingeniería de software previene contra la adopción prematura de microservicios distribuidos en etapas iniciales de proyectos de software (Fowler, 2015; Newman, 2021). Si bien los microservicios ofrecen escalabilidad independiente por servicio, introducen una severa complejidad operativa: latencia de red en llamadas remotas (RPC/gRPC), fallas de transacciones distribuidas que exigen patrones de compensación complejos (*Sagas*) y dificultades de consistencia eventual.

Por el contrario, el **Monolito Modular** organiza el código fuente en módulos desacoplados con límites de contexto bien definidos (*Bounded Contexts* de *Domain-Driven Design*), compartiendo un mismo proceso de ejecución y un único motor transaccional relacional. Este enfoque preserva la integridad transaccional ACID en una sola base de datos y simplifica radicalmente los despliegues y pruebas unitarias, manteniendo la viabilidad de evolucionar hacia microservicios en fases avanzadas de madurez técnica (Newman, 2021).

---

## 3.3. Motores de Persistencia Relacional y Manejo de Concurrencia Espaciotemporal (PostGIS)

El desafío computacional distintivo de un *marketplace* inmobiliario flexible es la **gestión de concurrencia espaciotemporal**. A diferencia de los sistemas transaccionales convencionales que administran inventarios numéricos discretos (como unidades de productos en una tienda virtual), un espacio físico es indivisible en el tiempo y está anclado a una coordenada geográfica estricta.

### 3.3.1. Índices Espaciales y Tipos Geométricos (PostGIS)

La extensión PostGIS para el motor relacional PostgreSQL proporciona soporte estandarizado por el *Open Geospatial Consortium* (OGC) para almacenar y consultar geometrías geográficas vectoriales (`GEOMETRY` y `GEOGRAPHY`) (Obe & Hsu, 2021). El uso de árboles de rectángulos delimitadores mínimos (*R-Tree*) indexados mediante estructuras **GiST** (*Generalized Search Tree*) permite realizar consultas de proximidad geoespacial (como el operador de distancia esférica `ST_DWithin` o la intersección `ST_Intersects`) con una complejidad temporal logarítmica $\mathcal{O}(\log N)$, posibilitando la búsqueda instantánea de inmuebles dentro de un radio de interés definido por el usuario (Obe & Hsu, 2021).

### 3.3.2. Rangos Temporales e Índices de Exclusión para la Prevención de Sobre-Reserva

Para erradicar de forma matemáticamente infalible el problema de la sobre-reserva (*double-booking*), la teoría de bases de datos relacionales ofrece el concepto de **restricciones de exclusión generalizadas** (*Exclusion Constraints*) (Hellerstein et al., 1995). 

Mediante el tipo nativo de rango temporal `tsrange` (rango de marcas temporales con límites inclusivos/exclusivos) y el operador de superposición de intervalos `&&`, el motor de base de datos evalúa si dos reservas sobre un mismo inmueble coinciden en el tiempo:

> **Condición Lógica de Colisión Concurrente:**  
> `Colisión = (espacio_id_A == espacio_id_B) AND (intervalo_A && intervalo_B)`

Al definir una restricción de exclusión indexada con `GiST` sobre la tupla `(espacio_id WITH =, duracion_intervalo WITH &&)`, el propio motor PostgreSQL rechaza a nivel de almacenamiento cualquier intento simultáneo de reserva concurrente que pretenda ocupar el mismo espacio en un intervalo superpuesto, garantizando consistencia transaccional serializable sin necesidad de bloqueos distribuidos costosos en la capa de aplicación (Obe & Hsu, 2021).

---

## 3.4. Mecanismos Transaccionales de Custodia en Garantía (Escrow) y Pasarelas de Pago

La mitigación del riesgo moral y la asimetría de información en plataformas entre pares (*peer-to-peer*) exige mecanismos de salvaguarda financiera. En el comercio tradicional, el arrendatario transfiere el pago directamente al propietario antes de ocupar el inmueble, quedando desprotegido ante fraudes o discrepancias entre la oferta y la realidad; a su vez, el arrendador queda expuesto a daños no indemnizados si la garantía no es verificable.

El mecanismo de **Custodia en Garantía o Fideicomiso Digital (*Escrow*)** resuelve este dilema actuando como un intermediario tecnológico fiduciario neutral (Kauffman et al., 2010):

**Figura 3**  
*Diagrama de Secuencia de la Operatoria Transaccional en Custodia (Escrow)*

![](assets/figuras/fig03_secuencia_escrow_garantia.png)

*Nota.* Elaboración propia en base a estándares fiduciarios digitales y protocolos de pasarela de pago (Kauffman et al., 2010).

Desde el punto de vista arquitectónico, la pasarela de pagos debe soportar **pagos divididos (*split payments*)**, donde el monto abonado por el usuario se fragmenta en el acto: una fracción corresponde a la comisión por servicio de la plataforma (*take rate*), mientras que el saldo restante queda retenido en una cuenta de custodia temporal hasta la finalización satisfactoria del servicio, momento en el cual se liquida hacia la cuenta bancaria del arrendador (*payout*) (Kauffman et al., 2010).

---

## 3.5. Marco Regulatorio Chileno de Ciberseguridad y Protección de Datos Personales (Ley N° 21.719)

El desarrollo de plataformas que intermedian contratos legales y procesan antecedentes comerciales debe ceñirse rigurosamente al marco normativo vigente en Chile:

### 3.5.1. Ley N° 21.719 sobre Protección y Tratamiento de Datos Personales

Promulgada para modernizar la legislación chilena homologándola a los estándares del Reglamento General de Protección de Datos de la Unión Europea (RGPD), la **Ley N° 21.719** establece exigencias estrictas para los responsables de bases de datos:
1. **Principios de Licitud, Finalidad y Proporcionalidad:** Los datos recopilados (cédulas de identidad, escrituras societarias, fotografías de inmuebles) solo pueden utilizarse para los fines expresamente consentidos vinculados a la prestación del servicio.
2. **Privacidad desde el Diseño y por Defecto (*Privacy by Design*):** Toda la infraestructura tecnológica debe incorporar mecanismos nativos de protección, cifrado de datos en reposo y en tránsito, y políticas de minimización de datos (Cavoukian, 2009).
3. **Derechos ARCO:** El titular de los datos conserva la facultad inalienable de ejercer en cualquier momento los derechos de **Acceso, Rectificación, Cancelación y Oposición**.
4. **Protocolo Anti-Restauración (*Anti-Replay Restoration*):** Un desafío de ingeniería crítico bajo la Ley N° 21.719 ocurre cuando un usuario ejerce su derecho de supresión y, con posterioridad, la infraestructura sufre un incidente de pérdida que obliga a restaurar una copia de seguridad histórica (*backup*). Si no existe un mecanismo compensatorio, la restauración del respaldo reviviría ilícitamente los datos personales que habían sido purgados formalmente. La arquitectura debe implementar un registro de auditoría inmutable de supresiones que aplique un script de reaplicación de purga inmediatamente después de cualquier evento de recuperación de base de datos.

### 3.5.2. Ley N° 21.461 de Medidas Expeditas para el Arrendamiento de Inmuebles ("Devuélveme mi Casa")

Esta ley agiliza los procedimientos de restitución de inmuebles ante situaciones de mora o deterioro. Para que un contrato de arrendamiento goce de mérito ejecutivo y facilite la restitución judicial expedita, la ley exige que el instrumento conste por escrito y cuente con firma autorizada o firma electrónica avanzada conforme a la Ley N° 19.799. Por consiguiente, la plataforma debe integrar servicios de firma electrónica remota con certificación de identidad para dotar a los contratos generados de plena validez jurídica probatoria en tribunales chilenos.
