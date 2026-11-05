# CAPÍTULO VII: Definición de Arquitectura TI

## 7. Definición de Arquitectura TI

### 7.1. Vistas de arquitectura

La vista de negocio define oferta, búsqueda, contratación y entrega. La vista de aplicaciones ubica la interfaz, la API y los módulos. La vista de datos asigna autoridades a ocupación, contrato y pagos y separa los archivos privados. La vista de infraestructura identifica los entornos y los controles de despliegue que desarrolla el Capítulo XIII.

El Capítulo X detalla los componentes y la comunicación entre la interfaz, el núcleo y sus adaptadores.

### 7.2. Decisiones y criterios de revisión

**Tabla 8**\
*Decisiones arquitectónicas y criterio de verificación*

| Decisión | Consecuencia técnica | Verificación |
|---|---|---|
| Backend modular | La coordinación entre módulos conserva límites de responsabilidad. | Revisar paquetes y contratos del corte. |
| PostgreSQL y PostGIS | La búsqueda espacial y la exclusión temporal operan mediante mecanismos separados. | Probar consultas y concurrencia en la base. |
| Autorización por recurso | El papel de la cuenta depende de la operación y del vínculo con el espacio o la reserva. | Probar titular, participante y tercero. |
| Adaptadores externos | La simulación y el proveedor utilizan criterios de habilitación distintos. | Registrar entorno, eventos y resultado por integración. |

*Nota.* Elaboración propia con base en la arquitectura del repositorio y el ADR del 4 de noviembre de 2026. La Tabla D.1 identifica relaciones físicas, la Tabla E.1 identifica operaciones y las tablas F.1 y F.2 documentan escenarios de verificación.
