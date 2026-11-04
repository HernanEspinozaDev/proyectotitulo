# CAPÍTULO VIII: DISEÑO DE ARQUITECTURA TI Y DEL SOFTWARE

## 8.1. Vistas de arquitectura

La vista de negocio define oferta, búsqueda, contratación y entrega. La vista de aplicaciones ubica la interfaz, la API y los módulos. La vista de datos asigna autoridades a ocupación, contrato y pagos y separa los archivos privados. La vista de infraestructura identifica los entornos y los controles de despliegue que desarrolla el Capítulo XI.

La Figura 7 organiza las cuatro vistas que se contrastan con los anexos D y E.

**Figura 7**\
*Vistas de arquitectura de espaciGo*

![](assets/figuras/fig07_arquitectura_togaf_capas.png){height=11cm}

*Nota.* Elaboración propia a partir de las vistas de negocio, aplicaciones, datos e infraestructura del proyecto.

## 8.2. Aplicación modular y persistencia

El punto de entrada de la API reside en `cmd/api`. El repositorio agrupa responsabilidades en paquetes bajo `internal`, entre ellos `spaces`, `occupancy`, `booking`, `contract` y `documentverification`. Los adaptadores PostgreSQL se organizan bajo `internal/adapters/postgres`. La estructura refleja límites de responsabilidad y permite verificar componentes con dependencias controladas.

El diseño asigna la autoridad de ocupación a PostgreSQL y utiliza PostGIS para las consultas geográficas. El Anexo D respalda la estructura declarada y el Capítulo X delimita la evidencia de concurrencia. El Capítulo IX especifica la restricción de solapamiento y el Anexo D identifica el origen del catálogo físico. Los objetos privados requieren comprobación de acceso y retención por finalidad.

## 8.3. Presentación y contrato de aplicación

La interfaz Next.js consume la API Go a través de los adaptadores de la aplicación y de la ruta BFF cuando corresponde. El contrato de acceso debe preservar la autorización sobre cada recurso desde la entrada hasta la operación de dominio. El Anexo E identifica el corte de OpenAPI y separa las rutas de ensayo.

## 8.4. Decisiones y criterios de revisión

**Tabla 9**\
*Decisiones arquitectónicas y criterio de verificación*

| Decisión | Consecuencia técnica | Verificación |
|---|---|---|
| Backend modular | La coordinación entre módulos conserva límites de responsabilidad. | Revisar paquetes y contratos del corte. |
| PostgreSQL y PostGIS | La búsqueda espacial y la exclusión temporal operan mediante mecanismos separados. | Probar consultas y concurrencia en la base. |
| Autorización por recurso | El papel de la cuenta depende de la operación y del vínculo con el espacio o la reserva. | Probar titular, participante y tercero. |
| Adaptadores externos | La simulación y el proveedor utilizan criterios de habilitación distintos. | Registrar entorno, eventos y resultado por integración. |

*Nota.* Elaboración propia con base en la arquitectura del repositorio y el ADR del 4 de noviembre de 2026. La Tabla D.1 identifica relaciones físicas, la Tabla E.1 identifica operaciones y las tablas F.1 y F.2 documentan escenarios de verificación.

## 8.5. Contratos de interfaz

El catálogo versionado utiliza OpenAPI 3.1. La arquitectura objetivo separa aportes de firma, renta y garantía. El Anexo E registra el corte de interfaz. El Capítulo XI identifica las condiciones de habilitación y el Capítulo X registra los resultados con evidencia disponible.
