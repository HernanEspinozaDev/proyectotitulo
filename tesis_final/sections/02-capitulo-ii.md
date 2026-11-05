# CAPÍTULO II: Identificación del Problema

## 2. Identificación del Problema

### 2.1. Actualización y justificación del problema

#### 2.1.1. Descripción de la organización

##### 2.1.1.1. Antecedentes

La organización operadora se define como una propuesta para prestar el servicio de intermediación. El diseño organizacional identifica funciones necesarias para operar la plataforma y asignar responsabilidades sobre decisiones, datos e incidentes.

**Misión.** Facilitar el arriendo flexible de espacios ofrecidos por personas y organizaciones mediante información clara sobre la oferta, control de disponibilidad y evidencia de contratación.

**Visión.** Consolidar un servicio de arriendo flexible que demuestre su utilidad para titulares y arrendatarios y pueda ampliar su cobertura cuando exista evidencia operativa y comercial.

**Principios.** Transparencia de condiciones y cobros, privacidad por finalidad, trazabilidad de decisiones y verificación incremental.

##### 2.1.1.2. Diagnóstico

El Capítulo VIII presenta el análisis FODA y las decisiones que se derivan de él.

#### 2.1.2. Descripción del problema

Para concretar un arriendo por un intervalo específico, las partes necesitan acordar qué espacio se ofrece, cuándo está disponible, qué condiciones rigen su uso y cómo se acredita el pago. Cuando el anuncio, el calendario y el acuerdo se gestionan en canales separados, la persona interesada debe confirmar los datos con el titular. Si dos solicitudes compiten por el mismo intervalo, el estado del acuerdo puede quedar desactualizado en alguno de esos canales.

El diagnóstico utiliza un escenario de referencia de intermediación por canales separados. La evidencia de vacancia del Capítulo I aporta contexto sobre oficinas en Santiago [@cbre2026; @colliers2026]. La memoria utiliza el escenario para derivar requisitos de ingeniería. La frecuencia de esas fricciones y su efecto comercial requieren medición independiente.

La Figura 1 representa un escenario analítico de coordinación por canales separados.

**Figura 1**\
*Proceso de referencia para coordinar un arriendo por canales separados*

![](assets/figuras/fig01_contexto_as_is.png)

*Nota.* Elaboración propia. El diagrama UML representa el escenario analítico de referencia del capítulo.

### 2.2. Justificación del problema

#### 2.2.1. Relevancia del problema

**Tabla 1**\
*Matriz de causas, consecuencias e indicadores propuestos*

| Causa operativa | Consecuencia posible | Indicador propuesto |
|---|---|---|
| El anuncio y el calendario se actualizan por separado. | La persona interesada confirma manualmente la disponibilidad. | Intercambios requeridos para confirmar horario. |
| Las solicitudes sobre un mismo espacio se coordinan sin una autoridad común de ocupación. | Dos solicitudes pueden coincidir en el mismo intervalo. | Intentos simultáneos rechazados correctamente por solapamiento. |
| Las condiciones se negocian en distintos canales. | Las partes pueden conservar versiones diferentes del acuerdo. | Emisiones que conservan condiciones y aceptación de ambas partes. |
| El pago se registra fuera del estado de la reserva. | Un evento duplicado o tardío requiere conciliación. | Eventos duplicados o tardíos tratados según la política vigente. |
| Los documentos y las evidencias se intercambian fuera de un registro con permisos. | Se dificulta controlar el acceso y reconstruir el proceso de entrega. | Accesos autorizados y denegados según actor, recurso y finalidad. |

*Nota.* Elaboración propia. El Anexo F traduce los indicadores técnicos en casos de prueba de solapamiento (PT-02), emisión (PT-06), eventos tardíos (PT-04) y acceso (PT-07). La coordinación manual corresponde a una futura medición de uso.

#### 2.2.2. Complejidad del problema

El proyecto comprende espacios de uso residencial, turístico, recreativo, comercial e industrial ofrecidos por personas y organizaciones. Cada unidad reservable exclusiva se representa mediante un espacio, un titular vigente y uno o más intervalos. Casas de veraneo y hostales ilustran el alcance objetivo. Una casa o habitación se representa como unidad exclusiva cuando la categoría y el corte la admiten. El inventario compartido requiere reglas y pruebas propias. El catálogo objetivo conserva las categorías del ADR. La evidencia local corresponde a escenarios sintéticos y el contexto de mercado del capítulo anterior se circunscribe a la medición citada.

El problema de ingeniería exige coordinar búsqueda geográfica, exclusión temporal, evidencia de aceptación, cobros y acceso a documentos privados. La verificación comprueba cada comportamiento en el entorno identificado. La evaluación comercial de la demanda y la habilitación de proveedores corresponden a actividades distintas de la verificación funcional del prototipo.
