# CAPÍTULO IX: MODELAMIENTO DE PROCESOS DE NEGOCIO Y DATOS

## 9.1. Modelado de Procesos de Negocio To-Be en BPMN 2.0

Para formalizar la operación de la plataforma y garantizar la consistencia en cada interacción de usuario, los flujos principales se modelan bajo el estándar internacional **BPMN 2.0** (*Business Process Model and Notation*), articulando las piscinas y carriles (*lanes*) de cada actor:

### 9.1.1. Proceso BPMN-01: Publicación, Verificación KYC/KYB y Moderación

Este proceso gobierna la incorporación de nuevos espacios al catálogo, asegurando que ningún inmueble sea visible sin la validación previa de la identidad jurídica del propietario y la inspección de habitabilidad de los datos:

**Figura 8**  
*Proceso BPMN-01: Publicación, Verificación KYC/KYB y Moderación de Espacios*

![](assets/figuras/fig08_bpmn_publicacion_kyc.png)

*Nota.* Elaboración propia en notación BPMN 2.0. El.

### 9.1.2. Proceso BPMN-02: Búsqueda, Reserva y Operación Escrow Transaccional

Modela el circuito crítico transaccional: búsqueda, validación de disponibilidad sin colisión temporal, pago fiduciario retenido en garantía y liquidación condicionada al *check-out*:

**Figura 9**  
*Proceso BPMN-02: Búsqueda, Reserva y Operación Escrow Transaccional*

![](assets/figuras/fig09_bpmn_reserva_escrow.png)

*Nota.* Elaboración propia en notación BPMN 2.0. El.

*Descripción Operativa del Flujo:*
1. El Arrendatario busca mediante coordenadas geoespaciales y selecciona un intervalo de tiempo.
2. El sistema valida atómicamente la ausencia de superposiciones mediante el operador `&&` de PostGIS.
3. El usuario autoriza el cobro del arriendo y el bloqueo de garantía en la pasarela segura.
4. El Arrendador dispone de un plazo límite de 24 horas para aceptar o rechazar la solicitud.
5. Si se aprueba, se genera el contrato dinámico y se remite a firma remota.
6. Cumplido el arriendo y verificado el *check-out* sin discrepancias en un período de gracia de 24 horas, el sistema ejecuta el *split payment* y libera el cupo de garantía.

### 9.1.3. Proceso BPMN-03: Ejercicio de Derechos ARCO y Supresión de Datos (Ley 21.719)

Gobierna el flujo de eliminación de datos personales, garantizando que el ejercicio del derecho de cancelación sea respetado sin violar obligaciones tributarias del SII:

**Figura 10**  
*Proceso BPMN-03: Ejercicio de Derechos ARCO y Supresión de Datos Personales*

![](assets/figuras/fig10_bpmn_supresion_ley21719.png)

*Nota.* Elaboración propia según el marco normativo de la Ley N° 21.719. El.

---

## 9.2. Modelado de Software en UML

El diseño estático y dinámico del sistema se especifica mediante el lenguaje de modelado unificado **UML 2.5**:

### 9.2.1. Diagrama de Casos de Uso del Ecosistema

Estructura las interacciones funcionales entre los actores y los subsistemas de la plataforma, respetando los límites formales del sistema:

**Figura 11**  
*Diagrama UML de Casos de Uso del Ecosistema Transaccional*

![](assets/figuras/fig11_uml_casos_uso_ecosistema.png)

*Nota.* Elaboración propia bajo estándar UML 2.5. El.

*Aspectos Metodológicos Formales:*
*   Los actores humanos (*Arrendatario, Arrendador, Administrador*) interactúan exclusivamente con casos de uso de nivel de usuario.
*   Los casos de uso de pago, firma digital y verificación de identidad incluyen relaciones formales `<<include>>` hacia los servicios fiduciarios y pasarelas externas.
*   En estricto apego a las normas de ingeniería, los requerimientos no funcionales (como algoritmos de hashing o certificados SSL) no se representan como casos de uso.

### 9.2.2. Diagrama de Componentes Hexagonales

Ilustra la organización modular del backend en Go y el desacoplamiento de adaptadores:

**Figura 12**  
*Diagrama de Paquetes y Componentes del Backend Hexagonal en Go*

![](assets/figuras/fig12_componentes_hexagonal.png)

*Nota.* Elaboración propia en base al diseño modular del backend. El.

---

## 9.3. Modelo de Datos Físico y Geoespacial en PostgreSQL / PostGIS

La arquitectura de persistencia se diseña sobre el motor relacional **PostgreSQL 18** con la extensión **PostGIS 3.6**.

### 9.3.1. Diagrama Entidad-Relación del Núcleo Transaccional

A continuación se presenta el modelo relacional del núcleo transaccional, articulando las entidades de usuarios, inmuebles, calendarios, reservas, evidencias fotográficas y contratos:

**Figura 13**  
*Modelo Entidad-Relación del Núcleo Transaccional y Persistencia Geoespacial*

![](assets/figuras/fig13_modelo_datos_er_nucleo.png)

*Nota.* Elaboración propia en base al esquema relacional de PostgreSQL 18 / PostGIS 3.6. El.

*(La estructura completa de las **110 tablas relacionales**, con sus claves primarias, claves foráneas, restricciones de integridad y tipos de datos normalizados se encuentra documentada en el **Anexo D: Diccionario Físico de Datos y Esquema DDL**).*

### 9.3.2. Índices Geoespaciales y Prevención Matemática de Sobre-Reserva (GiST y tsrange)

Para resolver definitivamente el problema de colisión concurrente (Caso de prueba `PT-02`), la tabla `reservas` implementa la siguiente restricción de exclusión física a nivel de base de datos:

```sql
-- Extensión requerida para operadores de igualdad en índices GiST
CREATE EXTENSION IF NOT EXISTS btree_gist;

-- Restricción de exclusión temporal por espacio físico
ALTER TABLE reservas 
ADD CONSTRAINT exclusion_doble_reserva 
EXCLUDE USING gist (
    espacio_id WITH =,
    duracion_intervalo WITH &&
)
WHERE (estado IN ('CONFIRMADA', 'EN_PROCESO', 'PAGO_PENDIENTE'));
```

**Mecanismo de Operación:**
1. La columna `duracion_intervalo` es de tipo `tsrange` (rango temporal con fecha y hora de inicio y fin).
2. El operador `WITH &&` evalúa la superposición matemática de intervalos.
3. Si dos transacciones intentan reservar el mismo `espacio_id` en instantes superpuestos, la estructura de árbol `GiST` serializa el acceso: la primera transacción adquiere la fila y confirma; la segunda transacción es bloqueada de inmediato a nivel de motor de datos lanzando una excepción de violación de restricción de exclusión (`SQLSTATE 23P01`).
4. Este mecanismo garantiza consistencia matemática con aislamiento serializable, consumiendo menos del 1% del tiempo de CPU en comparación con bloqueos distribuidos en memoria.
