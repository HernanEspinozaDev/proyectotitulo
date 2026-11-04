# CAPÍTULO III: MARCO TEÓRICO Y ESTADO DEL ARTE

## 3.1. Intermediación digital y ecosistema de plataforma

Una plataforma coordina interacciones mediante reglas e interfaces compartidas [@tiwana2014]. En espaciGo, la oferta especifica espacios y condiciones de uso, y la demanda busca disponibilidad por intervalo. El diseño conserva el vínculo entre anuncio, cotización y acuerdo para que ambas partes puedan identificar el recurso y las condiciones pactadas.

El proyecto aplica tecnología a la intermediación de espacios de uso residencial, turístico, recreativo, comercial e industrial. El Capítulo VIII distingue este alcance del catálogo del corte. El Capítulo II utiliza un escenario de intermediación por canales separados como punto de comparación. La evaluación contrasta comportamientos verificables, como detectar solapamientos y recuperar las condiciones aceptadas de una emisión.

## 3.2. Modularidad y arquitectura de puertos y adaptadores

El monolito modular organiza el backend mediante límites internos de responsabilidad. Una distribución por servicios agrega coordinación operativa y requiere límites estables entre componentes [@fowler2015]. El proyecto adopta módulos internos para identidad, oferta, ocupación y contratación, con PostgreSQL como autoridad de los datos transaccionales correspondientes.

La arquitectura de puertos y adaptadores separa los casos de uso de la interfaz y de los servicios externos [@cockburn2005]. En el corte local, un adaptador de ensayo permite comprobar el flujo de aplicación y mantener explícito qué resultado requiere un proveedor real.

La Figura 2 muestra cómo un caso de uso intercambia datos con sus adaptadores.

**Figura 2**\
*Interacción entre un caso de uso y sus adaptadores*

![](assets/figuras/fig02_puertos_y_adaptadores.png)

*Nota.* Elaboración propia a partir del patrón de puertos y adaptadores [@cockburn2005].

## 3.3. Persistencia relacional y concurrencia espaciotemporal

### 3.3.1. Búsqueda geoespacial

PostGIS aporta tipos espaciales y funciones de consulta por proximidad [@postgis; @es2postgiswithin]. En el diseño, la búsqueda combina distancia y filtros para seleccionar espacios candidatos. El Anexo E identifica las rutas declaradas y el Capítulo X delimita la evidencia de búsqueda. La disponibilidad se consulta por separado para el intervalo solicitado.

### 3.3.2. Rangos temporales y exclusión de solapamientos

PostgreSQL permite representar intervalos mediante tipos de rango y comprobar su superposición con el operador `&&` [@es2pgrangos]. El diseño utiliza un intervalo `tstzrange` por ocupación y una restricción de exclusión por espacio e intervalo activo. La sección 9.3 identifica la migración y los criterios de verificación. El Anexo D documenta el esquema de referencia.

## 3.4. Intermediación de pagos y contratación

El reparto de pagos permite distinguir la renta del arrendador y la comisión de la plataforma. La documentación del proveedor establece los requisitos de la integración Split 1:1 [@es2mpsplit]. El diseño de espaciGo registra por separado los aportes de firma, la renta y la garantía. La habilitación de cada cobro depende de su secuencia, del estado de la emisión y de las pruebas de integración.

La aceptación de condiciones se registra por parte y por emisión. La firma electrónica se ofrece como modalidad opcional de acuerdo con el ADR del 4 de noviembre de 2026. El Capítulo IX describe ambas rutas y el Capítulo X establece sus criterios de prueba.

## 3.5. Marco normativo de referencia y decisiones de privacidad

El análisis del proyecto incorpora como referencias la normativa chilena sobre protección de datos, documentos electrónicos y arrendamiento [@ley21719; @ley19799; @ley21461]. La arquitectura traduce el análisis a requisitos verificables de acceso por finalidad, minimización, evidencia de aceptación, retención y recuperación. La revisión de habilitación evalúa el alcance aplicable de cada modalidad de contratación y proveedor.

En el diseño de continuidad, la restauración requiere comprobar el estado de los datos y sus objetos asociados. El procedimiento revisa los permisos, el historial de supresiones y el resultado de recuperación antes de restablecer la operación, según los criterios del Capítulo XI.
