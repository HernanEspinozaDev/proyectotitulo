# Revisión del Informe de Proyecto: EspaciGo

Revisé el informe completo disponible y lo contrasté con las correcciones de la profesora. Y hay algo importante: no estás simplemente "faltando las historias de usuario". Varias de las correcciones de la profesora sí fueron incorporadas, pero quedaron algunas inconsistencias internas y algunos puntos que, aunque parecen completos, todavía podrían hacer que la profesora los observe.

La buena noticia es que la estructura general del informe está bastante avanzada. Yo lo separaría en:
*   **Ya corregido / cumple**
*   **Está, pero necesita ajuste**
*   **Falta o puede generar observación**
*   **Inconsistencias internas que conviene corregir sí o sí**

La revisión de la profesora establece explícitamente como pendientes: metodología, cronograma, RF, RNF, HU, CU, estructura cuerpo/anexos, arquitectura empresarial y marco teórico.

---

## 1. Panorama general

Mi diagnóstico del documento actual sería:

| Área | Estado | Observación |
| :--- | :---: | :--- |
| Problema y justificación | ✅ | Bien desarrollado |
| Levantamiento de requerimientos | ✅ | Está definido |
| RF | ⚠️ | Cantidad está bien encaminada, pero hay que verificar todos |
| RNF | ⚠️ | Mejoraron bastante, pero todavía hay problemas de redacción/medición |
| Historias de usuario | ❌ | Es el punto más evidente |
| Casos de uso | ⚠️ | Estructura por módulos está, pero hay inconsistencias |
| Marco teórico | ✅/⚠️ | Mucho mejor y ahora sí conecta conceptos con decisiones |
| Metodología | ✅ | Se incorporó lo que pidió la profesora |
| Cronograma | ❌ | Está, pero hay una contradicción importante de duración |
| Recursos/presupuesto | ✅ | Existe y está bastante desarrollado |
| Arquitectura TI | ❌ | Completa, pero tiene contradicciones tecnológicas |
| Arquitectura empresarial | ✅ | Se agregó lo que pidió |
| Misión/visión/FODA | ☑️ | Está |
| Organigrama/roles | ✅ | Está corregido |
| Indicadores | ☐ | Existen, pero faltan métricas más completas |
| Niveles de servicio | ☐ | Existen, pero conviene separar SLA de indicadores |
| Referencias | ☐ | Hay bibliografía, pero falta fortalecer las fuentes del marco teórico |
| Índice/formato | ☑️ | Hay varios "Error! Marcador no definido" |

Y hay **tres cosas que yo corregiría antes de cualquier otra cosa**:
1. Historias de usuario
2. Contradicción 5 semanas vs 16 semanas
3. Contradicciones de stack: Go vs Node, GCP vs AWS, PostgreSQL vs MariaDB/PostgreSQL

---

## 2. Historias de usuario: sí, efectivamente es una deuda

El informe dice que existen 25 HU, agrupadas en épicas y con criterios de aceptación. Pero en el PDF que estoy viendo, la tabla realmente no está desarrollada de manera visible; después del título de la Tabla 3 prácticamente salta al marco teórico.

Además, la profesora fue bastante específica:
> *Como [rol], quiero [acción] para [beneficio]*
> y los criterios deben describir comportamiento esperado, no simplemente repetir un RF.

**Ejemplo de lo que NO conviene:**
```text
HU-01
Como arrendatario, quiero buscar espacios.
Y después:
- El sistema debe permitir buscar espacios.
- El sistema debe permitir filtrar espacios.
- El sistema debe mostrar resultados.
(Eso termina pareciendo una lista de RF).
```

**Mejor:**
```text
HU-01 - Buscar espacios
Como arrendatario, quiero buscar espacios disponibles según ubicación, fecha y tipo de espacio, para encontrar una alternativa que se ajuste a mis necesidades.

Criterios de aceptación:
1. Si el usuario ingresa una ubicación válida, el sistema debe mostrar los espacios disponibles asociados a dicha ubicación.
2. Si el rango de fechas seleccionado contiene un espacio reservado, dicho espacio no debe aparecer como disponible.
3. Si no existen resultados, el sistema debe informar que no se encontraron espacios disponibles.
4. Al seleccionar un resultado, el sistema debe mostrar la información correspondiente al espacio.
```
Eso sí parece una HU con criterios de aceptación.

**Oportunidad importante:**
Las HU deberían conectarse con los RF y CU para demostrar trazabilidad.
*   **HU-01** Buscar espacios
    *   **RF-100** Buscar publicaciones
    *   **RF-106** Validar disponibilidad
    *   **CU-12** Buscar espacios

---

## 3. Requerimientos funcionales: están mucho mejor de lo que parece

Aquí hay una cosa que sí hiciste bien. El informe declara: "Anexo con la totalidad de los 220 requerimientos funcionales". Eso está muy alineado con lo que pidió la profesora (indicó explícitamente cerca de 200).

Además, algunos ejemplos que aparecen en el cuerpo están bien atomizados: *registrar cuenta, iniciar sesión, validar vigencia, consultar giro, eliminar datos, guardar estado, cambiar estado, buscar publicaciones, excluir resultados, mostrar desglose.*

**Pero ojo:** La profesora no pidió solamente cantidad. Pidió un verbo atómico por requerimiento y separar operaciones. Por lo tanto, no asumiría que los 220 están todos correctos solo porque son 220. Hay que revisar el DOCX del anexo RF.

Especialmente buscar verbos como:
*   gestionar
*   administrar
*   procesar
*   manejar
*   controlar
*   configurar
*   gestionar y...
*   subir y...
*   registrar y...
*   permitir X y Y

Porque esos son precisamente los patrones que la profesora marcó.

---

## 4. RNF: aquí todavía veo cosas que corregir

La profesora pidió que los RNF estuvieran redactados como: `"El sistema debe [condición de calidad]"` y además con subcategorías y al menos 3 ejemplos por categoría.

Tu documento ya tiene categorías (Rendimiento, Usabilidad, Fiabilidad, Seguridad, Flexibilidad, Portabilidad, Implementación, Legislativos). Eso está bien.

Pero la tabla del cuerpo todavía muestra cosas como:
*   "Tiempo de respuesta del motor de búsqueda de espacios"
*   "Tiempo de procesamiento del flujo de pago Escrow"
*   "Acceso a la funcionalidad de reserva en pocos pasos"
*Eso son más bien nombres/títulos de requisitos, no requisitos completos.*

**Yo los convertiría en:**
*   **RNF-001:** El sistema debe responder las consultas de búsqueda de espacios en un tiempo máximo de X segundos bajo una carga de X usuarios concurrentes.
*   **RNF-002:** El sistema debe completar el procesamiento del flujo de pago en un tiempo máximo de X segundos, excluyendo el tiempo de respuesta de servicios externos.
*   **RNF-004:** El sistema debe permitir completar una solicitud de reserva en un máximo de X pasos desde la selección del espacio hasta la confirmación.

Esto es importante: **Un RNF debe poder probarse.**
*   ❌ *Malo:* El sistema debe ser altamente escalable. (No sabes cuándo cumple).
*   ✅ *Mejor:* El sistema debe soportar al menos 500 usuarios concurrentes manteniendo un tiempo de respuesta inferior a 3 segundos para las operaciones de consulta. (Se puede probar).

---

## 5. Casos de uso: aquí hay una inconsistencia importante

La profesora pidió: un diagrama por módulo, nombre del sistema, nombre del módulo, UML correcto, ID único, flujo principal, flujos alternativos, no poner RNF como CU.

Tu informe sí dice que ahora tienes 6 módulos, y presenta los casos principales agrupados por módulo. Eso va en la dirección correcta.

**Pero hay un problema serio:** En distintas partes del documento aparecen diferentes numeraciones/nombres.

Por ejemplo, en el índice aparecen:
*   CU-01 Registrar Cuenta
*   CU-02 Validar Identidad
*   CU-03 Solicitar Derecho al Olvido
*   CU-04 Crear Anuncio...

Pero más adelante aparecen:
*   CU-01 Registrar Cuenta
*   CU-05 Validar Identidad
*   CU-08 Crear Publicación
*   CU-10 Configurar Calendario
*   CU-12 Buscar Espacios
*   CU-14 Solicitar Reserva...

Esto puede ser simplemente porque se modificaron los casos y no se actualizó el índice/listado de figuras, pero tienes que arreglarlo.

**Yo haría una auditoría de IDs:**
*   CU-01 Registrar cuenta
*   CU-02 Validar identidad
*   CU-03 Solicitar derecho al olvido
Y después verificar que ese mismo ID y nombre aparezca **exactamente igual** en: índice, diagrama, tabla, ficha, referencias cruzadas, texto, anexos.

---

## 6. Otro punto: no conviertas los RF en casos de uso

La profesora puso como ejemplo: "Encriptar contraseña" NO es CU; es RNF de seguridad.
En tu RF aparece: *RQF-008 El sistema debe encriptar la contraseña...*
Esto es otra cosa que revisaría.

Por su naturaleza, "encriptar contraseña" es una condición de seguridad/implementación, no una funcionalidad que el usuario solicite. Si la profesora específicamente dijo que encriptar contraseña debe ser RNF, entonces deberías probablemente moverlo de RF a RNF (Ej: *RNF-Seguridad: El sistema debe almacenar las contraseñas mediante un algoritmo de hash criptográfico seguro.*) y eliminar el CU asociado si existiera.

---

## 7. Metodología: esta corrección sí la aplicaste

Aquí estás bastante bien. La profesora pidió: Iterativo-incremental + PMBOK y justificarlo mediante estabilidad de requisitos y ausencia de cliente real modificando continuamente el alcance.

Tu informe ahora dice exactamente eso. Además incorporaste un cuadro comparando: Scrum/agile, Cascada/PMBOK, e Híbrida (☑). Esta corrección está aplicada.

Pero tienes una contradicción posterior.

---

## 8. 🚨 Problema importante: 5 semanas vs 16 semanas

Esto es probablemente una de las cosas que más rápidamente detectaría un profesor.

En el documento aparecen: **5 semanas**. El cronograma completo está construido sobre 5 semanas. Incluso el presupuesto utiliza: 20 horas semanales × 5 semanas = 100 horas por integrante.

Pero en otras partes dices: **16 semanas**. La introducción dice 16 semanas. Y la conclusión vuelve a decir: ciclo corto de 16 semanas.

**Esto hay que arreglar.** Debes decidir cuál es el alcance real del documento.
*   Si ES1/Formulación corresponde solamente a 5 semanas, entonces elimina/corrige las referencias a 16 semanas.
*   Si el proyecto completo realmente dura 16 semanas, entonces el cronograma de 5 semanas debe representar solo una fase, y debes mostrar las otras 11 semanas.
Pero actualmente el texto mezcla ambas cosas. Yo no dejaría esto así.

---

## 9. 🚨 Contradicción tecnológica: Go vs Node.js

Esta es incluso más importante porque aparece en la arquitectura.
En unas partes declaras: *Backend desarrollado en Golang.* Y tu matriz de decisión selecciona Golang y descarta Node.js. Perfecto.

Pero después, en Arquitectura Empresarial, aparece: *Core API REST (Node)* Y posteriormente: *Backend desarrollado en Node.js/Express.*

Eso contradice directamente la ADR donde seleccionaste Go. **Debe quedar UNO.**
Por lo que veo, tu decisión arquitectónica es:
*   Frontend → React/Next.js
*   Backend → Go/Golang
*   BD → PostgreSQL
*   Cloud → GCP Cloud Run
*   Analítica → BigQuery

Entonces en arquitectura empresarial debería decir: **Core API REST (Go)** y no Node.

---

## 10. Otra contradicción: AWS vs GCP

Tu arquitectura selecciona: GCP Cloud Run. Y el presupuesto también está calculado sobre GCP: Cloud Run + Cloud SQL + BigQuery.
Pero después aparecen: *Docker/GCP/AWS* en el cronograma. Y: *AWS S3/GCP Storage* en arquitectura de datos.

Eso genera la pregunta: ¿Cuál es realmente el proveedor cloud? Si la decisión es GCP, yo dejaría: GCP (Cloud Run, Cloud SQL / PostgreSQL, Cloud Storage, BigQuery). AWS puede aparecer como alternativa descartada dentro de una ADR, pero no como parte de la arquitectura final salvo que realmente utilices ambos.

---

## 11. 🚨 PostgreSQL vs MariaDB

Otra inconsistencia. Tu ADR selecciona: PostgreSQL. Pero arquitectura de datos dice: *MariaDB/PostgreSQL*.

No conviene poner: MariaDB/PostgreSQL en la arquitectura final. Si PostgreSQL ganó la decisión arquitectónica, entonces: **PostgreSQL** y punto.

---

## 12. Arquitectura empresarial: aquí sí aplicaste la corrección

La profesora pidió cuatro dominios:
1. Procesos
2. Aplicaciones
3. Datos
4. Infraestructura

Tu informe ahora tiene los cuatro. Además agregaste: misión, visión, objetivos estratégicos, FODA, organigrama, roles. Esta parte está bastante bien alineada con la corrección.

No obstante, hay una diferencia conceptual que yo mejoraría. La profesora pidió Arquitectura Empresarial, pero tu sección de infraestructura vuelve a mezclarse bastante con la Arquitectura TI. No está mal que se relacionen, pero conviene separar:

**Arquitectura empresarial:**
*   **Procesos:** Registro → publicación → reserva → pago → contrato → check-in → disputa.
*   **Aplicaciones:** Marketplace → Backoffice → APIs externas.
*   **Datos:** usuarios → inmuebles → reservas → pagos → contratos → evidencias → auditoría.
*   **Tecnología:** Cloud Run → PostgreSQL → BigQuery → almacenamiento → redes → Docker.

**Arquitectura TI:**
Explicas con mayor profundidad: por qué Next.js, por qué Go, por qué PostgreSQL, por qué Cloud Run, etc. Así no repites contenido.

---

## 13. Marco teórico: mejoró muchísimo

Aquí quiero destacar algo. La profesora dijo específicamente: el marco teórico no debe ser una definición genérica; cada concepto debe justificar algo que el sistema hará o cómo lo hará.

Y ahora tu marco tiene precisamente una estructura del tipo: **Concepto → problema → alternativas → decisión → impacto técnico.**

Incluso tienes una tabla de síntesis que relaciona: SaaS, Marketplace, monetización, Cloud, disponibilidad, pagos/Escrow, KYC/KYB, privacidad, contratos, auditoría, arquitectura con las decisiones de EspaciGo.
Esto sí responde a la corrección. De hecho, conceptualmente es una de las partes que veo más encaminadas.

---

## 14. Pero al marco teórico le falta algo: más respaldo bibliográfico

Aquí veo una debilidad diferente a la corrección de la profesora. Tienes bibliografia (Bass, Ley 21.461, Ley 21.719, Docker, Go, Google Cloud, Mercado Pago, PostgreSQL, Next.js).

Pero gran parte del marco teórico contiene afirmaciones que deberían tener citas dentro del texto, no solamente aparecer en la bibliografia. Por ejemplo: SaaS permite..., Marketplace se define como..., B2B2C..., ACID..., KYC/KYB..., Escrow..., REST..., arquitectura de microservicios...

No basta con poner la fuente al final del documento. Debería existir algo como:
*   *Según X (2024), ...*
*   *... (Autor, 2024).*
Esto le da carácter académico al marco.

---

## 15. Hay otro problema que encontré: estás haciendo afirmaciones demasiado absolutas

Por ejemplo, en la conclusión dices: *"alineado con los estándares tecnológicos de la industria actual"* y *"garantizan la concurrencia masiva"*.
Eso es demasiado fuerte para una formulación de proyecto. Tu arquitectura propuesta puede estar diseñada para soportar alta concurrencia. Pero no puedes afirmar que la garantiza si todavía no hiciste pruebas de carga.

*   *Mejor:* "La arquitectura propuesta está diseñada para soportar escenarios de alta concurrencia..."

Y lo mismo con: *"cumplimiento estricto"*. Si todavía no tienes una revisión jurídica formal, es más prudente:
*   *Mejor:* "considerando los requisitos establecidos por..."
Esto hace que el informe sea más técnicamente defendible.

---

## 16. Indicadores: están, pero yo agregaría más

Actualmente tienes: Tiempo de Ciclo de Contratación, Tasa de Disputas Resueltas. No están mal. Pero para un proyecto de software de este tamaño yo tendría mínimo indicadores agrupados:

*   **Negocio:** Tiempo promedio de contratación. Tasa de conversión de búsqueda → reserva. Tasa de ocupación de espacios.
*   **Sistema:** Disponibilidad. Tiempo promedio de respuesta. Error rate.
*   **Transacciones:** Tasa de pagos exitosos. Tasa de reservas fallidas. Tiempo de procesamiento de pago.
*   **Operación:** Tiempo de resolución de disputas. Porcentaje de operaciones auditables.

Y cada indicador debería tener: Nombre, Fórmula, Unidad, Meta, Frecuencia, Fuente de datos, Responsable. Eso lo hace mucho más académico.

---

## 17. Niveles de servicio: cuidado con confundirlo con indicadores

Tienes: Disponibilidad 99.9% y logs con latencia menor a 3 segundos. Eso está bien como objetivo técnico, pero puedes estructurarlo como:

| Servicio | SLA/SLO | Métrica |
| :--- | :--- | :--- |
| Disponibilidad plataforma | ≥99,9% | Uptime mensual |
| API | < 2 s | P95 |
| Auditoría | < 3 s | Latencia de escritura |
| Recuperación | < X min | RTO |
| Pérdida de datos | < X min | RPO |

Especialmente RTO/RPO podrían quedar muy bien en un proyecto Cloud.

---

## 18. Alcance y restricciones: revisaría que estén perfectamente separados

Tu informe sí tiene alcance/restricciones y, por ejemplo, declara fuera de alcance la domótica de accesos físicos. Eso está bien. Pero yo revisaría que tengas claramente:

*   **Dentro del alcance:** registro, KYC/KYB, publicación, búsqueda, disponibilidad, reserva, pago, escrow, contrato, firma, check-in/out, disputas, backoffice, auditoría.
*   **Fuera del alcance:** cerraduras inteligentes, seguros, representación legal, gestión física del inmueble, etc.

Porque esto te protege mucho durante la defensa.

---

## 19. Recursos y presupuesto: está bastante completo

Aquí sí hiciste el trabajo. Tienes: 3 integrantes, 100 horas por persona, \$15.000/hora, \$4.500.000 costo de oportunidad, infraestructura, dominio, herramientas, APIs, costo inicial, costo total valorizado. Eso cumple bastante bien la idea.

Pero nuevamente aparece la contradicción de duración. Si son 16 semanas, entonces: `20 h × 16 semanas ≠ 100 horas`. Así que presupuesto y cronograma deben usar la misma duración.

---

## 20. El índice tiene errores que NO deberías dejar

Esto sí lo arreglaría antes de entregar. En el indice aparecen:
*   Investigación Bibliográfica. ¡Error! Marcador no definido.
*   Metodología de Desarrollo... ¡Error! Marcador no definido.
*   Recursos Humanos ¡Error! Marcador no definido.
*   Recursos tecnológicos ¡Error! Marcador no definido.
*   Presupuesto ¡Error! Marcador no definido.
*   Estructura Organizacional ¡Error! Marcador no definido.

Además ocurre con varias imágenes y tablas del índice. Eso parece un problema de referencias cruzadas de Word, no de contenido. Pero para una entrega académica queda feo y da la impresión de documento incompleto.

**Solución en Word:** `Ctrl+A → F9` para actualizar campos. Si algunos siguen: revisar títulos/captions, revisar referencias cruzadas, actualizar tabla de contenido, actualizar índice de figuras/tablas.

---

## 21. También veo un problema de nomenclatura

En el documento utilizas: RF, RQF, RNF, HU, CU. No necesariamente está mal, pero debes elegir una nomenclatura consistente.

Por ejemplo: RF-001, RF-002, RNF-001, RNF-002, HU-001, HU-002, CU-001, CU-002. Y mantenerla en todo el documento. Actualmente dices "Requerimientos Funcionales (RF)" pero las tablas usan RQF. Yo usaría RF simplemente, porque es más limpio.

---

## 22. Te falta algo que considero MUY importante: una matriz de trazabilidad

La profesora no lo puso explícitamente en su checklist, pero para este informe te conviene muchísimo. Tienes: Problema → requerimientos → HU → CU → arquitectura → objetivo. Pero actualmente están bastante separados.

Puedes crear una **Matriz de trazabilidad**:

| Objetivo | HU | RF | RNF | CU | Módulo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| OE-01 | HU-01 | RF-001 | RNF-001 | CU-01 | Identidad |
| OE-02 | HU-05 | RF-084 | RNF-004 | CU-08 | Publicaciones |
| OE-03 | HU-10 | RF-118 | RNF-011 | CU-14 | Reservas |
| OE-03 | HU-12 | RF-123 | RNF-025 | CU-15 | Pagos |
| OE-04 | HU-18 | RF-143 | RNF-026 | CU-19 | Contratos |

Esto demostraría que no inventaste RF, HU y CU independientemente.

---

## 23. También te conviene agregar una matriz RF - CU

Porque el informe dice: *"trazabilidad completa con los Requerimientos Funcionales"*. Entonces deberías demostrarla. Ejemplo:

| CU | Caso de uso | RF relacionados |
| :--- | :--- | :--- |
| CU-01 | Registrar cuenta | RF-001, RF-002, RF-003 |
| CU-02 | Validar identidad | RF-041, RF-048 |
| CU-08 | Registrar publicación | RF-084, RF-085 |
| CU-12 | Buscar espacios | RF-100, RF-106 |
| CU-15 | Pagar reserva | RF-123, RF-125, RF-126 |

Eso sería muy bueno para la defensa.

---

## 24. Hay una inconsistencia conceptual con "Escrow"

Yo también revisaría esto cuidadosamente. En el documento se afirma: *Mercado Pago permite retener fondos y hacer Split Payments.* Y el proyecto lo llama constantemente: *Escrow*.

Pero técnicamente deberías ser extremadamente preciso con qué mecanismo de Mercado Pago estás utilizando: autorización/preautorización, captura, split, retención, payout, marketplace, garantía mediante tarjeta.

No conviene simplemente decir: "Mercado Pago Escrow" como si fuera necesariamente un producto llamado exactamente así. Esto es especialmente importante porque tu proyecto tiene dinero real y una profesora podría preguntarte: "¿Dónde está implementado exactamente el escrow?" Y deberías poder explicar qué operación de la API representa cada estado financiero.

---

## 25. Lo mismo con la Ley 21.461

El documento hace afirmaciones bastante fuertes como: *"Firma Virtual... única vía"* y *"jurídicamente blindado"*. Eso yo lo suavizaría.

No deberías afirmar que una determinada API es "la única vía" salvo que tengas una fuente jurídica/técnica que lo demuestre. Puedes decir: *"Se selecciona FirmaVirtual como alternativa de integración evaluada para soportar el flujo de firma requerido por el proyecto."* Eso es mucho más defendible.

---

## 26. Algo que te falta y que sería muy bueno: modelo de datos

Tienes arquitectura de datos descrita, pero para un proyecto de título de este tamaño yo esperaría ver al menos: **Diagrama entidad-relación** con entidades como: Usuario, Identidad, Rol, Arrendador, Espacio, Arrendatario, Reserva, Imagen, Disponibilidad, Tarifa, Pago, Contrato, CheckIn, CheckOut, Disputa.

No estoy diciendo que la profesora lo haya pedido explícitamente en sus correcciones, pero arquitectura de datos sin modelo de datos queda un poco abstracta.

---

## 27. También revisaría el flujo end-to-end

Tu proyecto tiene muchos componentes. Deberías tener un diagrama que muestre:
*Arrendatario Buscar espacio → Seleccionar fecha → Validar disponibilidad → Crear reserva pendiente → Mercado Pago Retención/autorización → Arrendador aprueba → Generación contrato → Firma → Check-in → Uso del espacio → Check-out → ¿Existe disputa? (Sí -> Disputa -> Resolución) (No -> Payout Liberación/reembolso)*
Ese flujo te uniría: HU + RF + CU + arquitectura + proceso de negocio.

---

## 28. La conclusión necesita actualización

Actualmente tu conclusión todavía dice: *"Metodología Ágil (Scrum)"* aunque el capítulo de metodología ya fue cambiado a: Metodología Híbrida: iterativo-incremental + PMBOK. Eso es una inconsistencia que yo corregiría inmediatamente.

También vuelve a aparecer: *16 semanas* cuando el cronograma actual dice 5.

---

## 29. Entonces, ¿qué te falta realmente?

Si yo estuviera preparando este informe para entregar, haría este orden:

### PRIORIDAD 1 - Obligatorio
1.  **Historias de usuario:** Completar las 25 (HU-ID, Épica, Rol, Historia, Criterios de aceptación, Prioridad, RF relacionados, CU relacionado). Y revisar que los criterios no sean simplemente RF disfrazados.
2.  **Revisar todos los RF:** Los ~220 están bien en cantidad, pero hay que comprobar: un verbo, una acción, objeto claro, actor implícito, comportamiento verificable.
3.  **Revisar RNF:** Transformar "Tiempo de respuesta..." en "El sistema debe responder..." y agregar valores medibles.
4.  **Casos de uso:** Verificar ID, nombre, módulo, diagrama, actor, flujo principal, flujos alternativos, include, extend, RF relacionados.

### PRIORIDAD 2 — Correcciones importantes
5.  **Resolver duración:** 5 semanas o 16 semanas. No pueden coexistir.
6.  **Resolver stack:** Dejar definitivamente Frontend: Next.js / React, Backend: Go, BD: PostgreSQL, Cloud: GCP, Compute: Cloud Run, Storage: Cloud Storage, Analítica: BigQuery, Container: Docker. Eliminar referencias a Node, MariaDB, AWS si no forman parte de la arquitectura final.
7.  **Actualizar conclusión:** Debe reflejar metodología híbrida, no Scrum.
8.  **Actualizar índices:** Eliminar todos los *¡Error! Marcador no definido*.

### PRIORIDAD 3 - Mejoras que elevarían el informe
9.  **Matriz de trazabilidad:** Objetivo → HU → RF → CU → Arquitectura
10. **Diagrama ER/base de datos**
11. **Flujo end-to-end del negocio**
12. **Indicadores** con fórmula + meta + frecuencia + fuente
13. **SLA/SLO** con métricas cuantificables
14. **Más citas académicas** dentro del marco teórico

---

## 30. Mi evaluación de las correcciones de la profesora

Si tomo literalmente su checklist y lo comparo con tu documento actual:

| Corrección profesora | Situación actual |
| :--- | :--- |
| Metodología híbrida | ✅ Aplicada |
| Cuadro comparativo | ✅ Aplicado |
| Justificación metodología | ✅ Aplicada |
| Cronograma iterativo | ✅ Aplicado, pero revisar duración |
| ~200 RF | ✅ 220 declarados |
| RF verbo atómico | ⚠️ Hay que auditar los 220 |
| RNF estándar | ⚠️ Parcial |
| 3 ejemplos por categoría | ⚠️ Hay que verificar el anexo |
| HU | ❌ Pendiente/completar |
| Criterios HU | ❌ Pendiente/revisar |
| CU por módulo | ✅ Estructura incorporada |
| Nombre sistema/módulo | ⚠️ Verificar diagramas |
| UML | ⚠️ Verificar diagramas reales |
| CU no funcionales fuera | ⚠️ Revisar |
| IDs únicos | ❌ Hay inconsistencias de numeración |
| Flujos alternativos | ⚠️ Revisar fichas |
| Cuerpo + anexos | ☑️ La estructura está planteada |
| Arquitectura procesos | ✅ |
| Arquitectura aplicaciones | ✅ |
| Arquitectura datos | ✅ |
| Arquitectura infraestructura | ✅ |
| Organigrama con roles | ✅ |
| Misión | ✅ |
| Visión | ✅ |
| Objetivos estratégicos | ✅ |
| FODA | ✅ |
| Marco teórico ampliado | ✅ Muy bien encaminado |
| Conceptos = decisiones | ✅ |

La propia profesora había identificado como pendientes exactamente esos ocho grupos de correcciones; tu versión actual ya incorpora varios de ellos, especialmente metodología y arquitectura empresarial.

**Mi conclusión:** No estás tan lejos como parece. El documento ya tiene bastante contenido y varias de las correcciones de la profesora sí fueron aplicadas. Lo que yo no haría ahora es seguir agregando capítulos al azar. Primero haría una auditoría de consistencia y trazabilidad.

El orden óptimo sería: `HU -> RF -> RNF -> CU -> trazabilidad -> metodología/cronograma -> arquitectura -> conclusión -> formato`. Y los 4 errores prioritarios (HU, duración, Go vs Node, GCP vs AWS).

---
---

# Correcciones Finales y Línea Base

Con los datos que acabas de fijar, ya podemos dejar una línea base coherente del informe:
*   **RF:** 185 → los damos por corregidos.
*   **RNF:** 27 → los damos por corregidos.
*   **Duración:** 16 semanas / 4 meses.
*   **Metodología:** Iterativa-Incremental + PMBOK (híbrida).
*   **Frontend:** Next.js/React.
*   **Backend:** Go/Golang.
*   **BD transaccional:** PostgreSQL.
*   **Analítica/auditoría:** BigQuery.
*   **Contenedores:** Docker.
*   **Cloud:** Google Cloud.
*   **Ejecución:** Cloud Run.
*   **No AWS en la arquitectura final.**

Revisé nuevamente el PDF de EspaciGo completo en las partes donde aparecen metodología, cronograma, presupuesto y arquitectura. Hay varias inconsistencias concretas que conviene corregir.

### 1. Lo primero: metodología
En la Introducción, todavía aparece: *"Metodología Ágil (Scrum)"*. Mientras que en el capítulo de metodología dices correctamente: *"Metodología Híbrida"*, *"Iterativo e Incremental" + PMBOK*. Y en la conclusión vuelves a poner: *"Metodología Ágil (Scrum)"*.

**En la Introducción (Cambiar):**
> *Actual:* "junto con una Metodología Ágil (Scrum) y presupuestaria que garantizan su desarrollo en un plazo de 16 semanas."
> *Nuevo:* "junto con una metodología híbrida basada en un ciclo de vida iterativo-incremental y las prácticas de gestión establecidas por PMBOK, además de la planificación presupuestaria correspondiente para su desarrollo en un plazo de 16 semanas."

### 2. Página 47: 5 semanas → 16 semanas
En la página 47 dice: *"El proyecto EspaciGo contempla un tiempo estimado de desarrollo de 5 semanas..."* y *"Está estructurada exactamente para un periodo de 5 semanas."* Esto hay que reemplazarlo completamente.

**Debe quedar:**
> **Duración y cronograma**
> El proyecto EspaciGo contempla un tiempo estimado de desarrollo de 16 semanas, equivalentes a 4 meses, de acuerdo con el plazo establecido para el Proyecto de Título. Las fases concretas del desarrollo siguen la estructura del ciclo de vida iterativo-incremental previamente mencionado.
> Para asegurar un desarrollo secuencial y estructurado, el calendario distribuye las actividades en iteraciones e incrementos funcionales a lo largo de los cuatro meses de ejecución. Dentro de cada iteración y etapa se establecen plazos para las actividades de análisis, diseño, construcción, integración, validación y despliegue.

### 3. La tabla de semanas debe cambiar completa

Yo te recomiendo algo así:

| Periodo | Fase/Iteración | Principales actividades |
| :--- | :--- | :--- |
| Semanas 1-2 | Iniciación y análisis | Alcance, requisitos, HU, RF/RNF, arquitectura, BD |
| Semanas 3-5 | Incremento 1 | Usuarios, autenticación, perfiles, KYC/KYB |
| Semanas 6-8 | Incremento 2 | Publicaciones, inmuebles, mapas, búsqueda y disponibilidad |
| Semanas 9-11 | Incremento 3 | Reservas, tarifas y pagos |
| Semanas 12-13 | Incremento 4 | Contratos, firma electrónica y notificaciones |
| Semanas 14-15 | Incremento 5 | Check-in/out, disputas, auditoría, reseñas |
| Semana 16 | Integración y cierre | QA, seguridad, despliegue, documentación y entrega |

### 4. Los hitos también deben cambiar
Podrías utilizar:
*   **Hito 1 - Semana 2:** Base documental y arquitectura aprobadas (alcance, requisitos, RNF, HU, arquitectura, modelo de datos).
*   **Hito 2 - Semana 5:** Incremento 1 funcional (Usuarios + autenticación + perfiles + KYC/KYB).
*   **Hito 3 - Semana 8:** Incremento 2 funcional (Publicaciones + búsqueda + disponibilidad).
*   **Hito 4 - Semana 11:** Incremento 3 funcional (Reservas + tarifas + pagos).
*   **Hito 5 - Semana 13:** Incremento 4 funcional (Contratos + firma electrónica).
*   **Hito 6 - Semana 15:** Incremento 5 funcional (Check-in/out + disputas + auditoría + comunicación).
*   **Hito 7 - Semana 16:** Entrega final (QA + despliegue + documentación).

### 5. Presupuesto: actualmente está calculado para 5 semanas
Actualmente dices: 20 horas semanales × 5 semanas = 100 horas por integrante. Si efectivamente cada integrante trabajará 20 horas semanales durante las 16 semanas, entonces: `20 × 16 = 320 horas por integrante`. Y con tres integrantes: `320 × 3 = 960 horas`. A \$15.000 CLP/hora = \$4.800.000 por integrante. Total RR.HH.: \$14.400.000 CLP.

| Concepto | Actual | Correcto para 16 semanas |
| :--- | :--- | :--- |
| Horas por integrante | 100 | 320 |
| Integrantes | 3 | 3 |
| Horas totales | 300 | 960 |
| Valor/hora | \$15.000 | \$15.000 |
| RR.HH. | \$4.500.000 | \$14.400.000 |

**Nuevo presupuesto:**
*   RR.HH.: \$14.400.000
*   Tecnología: \$60.950
*   **Total valorizado: \$14.460.950 CLP**

### 6. Página 54: hay una frase que puedes mantener
Puedes mantener: *"gracias al enfoque Cloud-Native, el uso de tecnologías Open Source (PostgreSQL, Go, Next.js)..."*. Lo único que cambiaría sería evitar "100% viabilizable". Mejor: *"lo que contribuye a la viabilidad económica del proyecto dentro del contexto del Proyecto de Título."*

### 7. Arquitectura: eliminar AWS
Tu arquitectura final será Google Cloud Platform (GCP).
*   Eliminar: `AWS S3/GCP Storage` -> Dejar: `Google Cloud Storage`
*   Eliminar: `Despliegue en la nube (AWS/GCP)` -> Dejar: `Despliegue en Google Cloud Platform mediante Cloud Run.`

### 8. Arquitectura de aplicación: Node.js
En la página 70 y 71 aparece *Core API REST (Node)* y *Node.js/Express*. Tu ADR ya selecciona Go/Golang.
*   El diagrama debe ser: `Core API REST (Go)` o `Backend API REST (Golang)`
*   Cambiar texto a: *"Backend desarrollado en Go (Golang), encargado de implementar la lógica de negocio, las APIs REST y la orquestación de las integraciones externas."*

### 9. Página 71: MariaDB/PostgreSQL
Cambiar *Base de Datos Relacional (OLTP - MariaDB/PostgreSQL)* por **Base de Datos Relacional (OLTP - PostgreSQL)**.

### 10. La parte de Docker tiene una referencia incorrecta
Cambiar *"Go, Node, Postgres"* por **"Go, PostgreSQL y demás dependencias del proyecto."**

### 11. Cloud Run está correcto
Ya tienes GCP Cloud Run y Docker como SELECCIONADO. Eliminar las referencias antiguas a AWS/Node/MariaDB en las demás secciones.

### 12. La síntesis del marco teórico ya está bastante bien alineada
Dice: Next.js, Go, PostgreSQL, Cloud Run, BigQuery. Coincide con el stack definitivo.

### 13. Objetivos específicos: están bien, pero hay que revisar uno
Están perfectos (Docker, GCP, Golang, Next.js, PostgreSQL/BigQuery coinciden).

### 14. Conclusión
Debe quedar: *"Asimismo, la metodología híbrida basada en un ciclo de vida iterativo-incremental y las prácticas de gestión de PMBOK, junto con las prácticas DevOps mediante Docker y CI/CD en Google Cloud Run, permiten estructurar el desarrollo del sistema durante un período de 16 semanas."*

Cambiar *"garantizan la concurrencia masiva"* por *"La arquitectura está diseñada para soportar el crecimiento de la carga mediante mecanismos de escalabilidad proporcionados por la infraestructura cloud seleccionada."*

Cambiar *"cumplimiento estricto"* por *"considerando los requisitos de protección de datos y las obligaciones legales analizadas en el proyecto."*

### 15. Arquitectura Empresarial: "alineamiento perfecto"
Cambiar *"Existe un alineamiento perfecto..."* por *"Existe una alineación entre los objetivos estratégicos del negocio y las decisiones técnicas adoptadas..."*
Eliminar *"blinda a la empresa legalmente"*. Cambiar por *"contribuye a mantener la trazabilidad necesaria para procesos de auditoría."*

### 16. Revisión de términos de la arquitectura
Debe quedar: Next.js/React, Go/Golang, PostgreSQL, BigQuery, Google Cloud Storage, Docker, Google Cloud Run, Mercado Pago, FirmaVirtual, Google Maps.
NO DEBE APARECER: Node.js, Express, MariaDB, AWS S3, AWS EC2 (como arquitectura seleccionada), AWS/GCP (como alternativas finales).

### 17. Inconsistencia adicional (Pág 50)
Cambiar *"Despliegue a producción en entorno Cloud (Docker/GCP/AWS)."* por **"Despliegue a producción en entorno Cloud mediante Docker y Google Cloud Platform."**

### 18. Otro punto: JWT
"Desarrollo de autenticación (JWT)". Revisa que no choque con los RNF. Mantén la consistencia si efectivamente esa es la solución seleccionada.

### 19. Lo que NO tocaría
*   185 RF
*   27 RNF
*   Síntesis del marco teórico
*   ADR de Cloud Run, Docker, PostgreSQL
*   Objetivos específicos

### 20. Pero hay una cosa que todavía falta: HU
El cronograma no debe quedar amarrado a HU-01-HU-03 si tendrás 25. Debería reflejar: *"Elaboración y validación de las historias de usuario correspondientes a los módulos del incremento."*

### 21. Numeración de Casos de Uso
Establecer una única nomenclatura (CU-001, CU-002...) y unificar en todo el documento.

---

## 22. Tu lista de correcciones final (Orden Prioritario)

**Obligatorio:**
1.  **Introducción:** Scrum → metodología híbrida Iterativo-Incremental + PMBOK.
2.  **Metodología:** 5 semanas → 16 semanas. Rehacer tabla de cronograma.
3.  **Carta Gantt:** 5 semanas → 16 semanas. Alinear iteraciones e incrementos.
4.  **Hitos:** Rehacer hitos según 16 semanas.
5.  **Presupuesto:** 100 h/persona → 320 h/persona. RR.HH. \$4.500.000 → \$14.400.000. Total \$4.560.950 → \$14.460.950.
6.  **Arquitectura de aplicación:** Node → Go.
7.  **Arquitectura de datos:** MariaDB/PostgreSQL → PostgreSQL.
8.  **Infraestructura:** AWS/GCP → GCP. AWS S3/GCP Storage → Google Cloud Storage.
9.  **Cronograma:** Docker/GCP/AWS → Docker/GCP.
10. **Conclusión:** Scrum → metodología híbrida. Quitar afirmaciones absolutas.

**Recomendado:**
11. Cambiar "alineamiento perfecto" → "alineación".
12. Cambiar "blinda legalmente" → "contribuye a la trazabilidad y cumplimiento".
13. Revisar todas las apariciones de Node.js, Express, MariaDB y AWS (búsqueda global).
14. Revisar JWT.
15. Revisar referencias a "Escrow" (Mercado Pago).
16. Actualizar HU del cronograma (una vez hechas las 25).
17. Auditar CU y unificar IDs.