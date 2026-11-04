# Antecedentes de revisiones de los catálogos

Material histórico de los anexos A, B y C. Las reglas vigentes se documentan en la memoria y el ADR.

### Brechas cerradas y módulo al que se incorpora cada RF

| Brecha detectada | RF agregados | Módulo |
| :--- | :--- | :--- |
| No existía requerimiento de aceptación de términos y condiciones (ejemplo explícito señalado en la retroalimentación). | RQF-186, RQF-187 | M01 |
| El flujo alternativo "reenviar token de verificación" (CU-02) no tenía RF que lo respaldara. | RQF-188 | M01 |
| La entidad "cuenta bancaria" solo tenía la operación de registro (RQF-032, RQF-033): faltaban consultar, modificar y eliminar. | RQF-189, RQF-190, RQF-191 | M02 |
| La HU04 contempla la captura de selfie de validación facial, sin RF asociado. | RQF-192 | M03 |
| El paso "consultar el estado de la validación" (CU-14) no tenía RF. | RQF-193 | M03 |
| Asimetría: el resultado de la validación se notificaba solo para KYC (RQF-047), no para KYB. | RQF-194 | M03 |
| La HU06 permite editar descripción, reglas de uso, capacidad y tarifas, pero el catálogo solo permitía editar título (RQF-086) y precio base (RQF-087). | RQF-195, RQF-196, RQF-197, RQF-198 | M04 |
| No existía RF para consultar las reservas del usuario, pese a ser precondición de CU-24, CU-26, CU-33, CU-34 y CU-42. | RQF-199 | M06 |
| Las cancelaciones automáticas (CU-27, CU-28) liberaban las fechas sin RF que lo declarara. | RQF-200 | M06 |
| El rechazo del pago cambiaba de estado (RQF-119) sin notificar al arrendatario. | RQF-201 | M06 |
| El escenario "una parte no firma" (CU-30) no tenía RF que registrara el rechazo notificado por el proveedor. | RQF-202 | M07 |
| La obligatoriedad de evidencia fotográfica en Check-in y Check-out había quedado fuera del catálogo. | RQF-203, RQF-204 | M08 |
| **El arrendador no tenía ninguna acción al término de la reserva** (brecha reportada en la revisión). | RQF-205, RQF-206 | M08 |
| RQF-181 presupone reseñas reportadas, pero no existía RF que permitiera reportar una reseña. | RQF-207 | M09 |
| **No existía RF de liberación de la garantía en el flujo sin reclamos** (solo RQF-175 "saldo restante tras deducciones"). | RQF-208 | M10 |
| El administrador no tenía RF para consultar la evidencia de recepción del arrendador al arbitrar (simetría con RQF-167). | RQF-209 | M10 |
| Solo existía la notificación de apertura de disputa (RQF-164), no la del resultado. | RQF-210 | M10 |
| La boleta electrónica solo se generaba (RQF-176); no se enviaba al arrendador. | RQF-211 | M10 |
| Bloquear/desbloquear una cuenta (RQF-178 a RQF-180) requiere localizarla previamente. | RQF-212 | M11 |

**Catálogo total resultante: 212 requerimientos funcionales (RQF-001 a RQF-212).**

---

### Brechas cerradas en la revisión de las HU

| HU que lo exigía | Brecha detectada | RF agregados | Módulo |
| :--- | :--- | :--- | :--- |
| HU01 | La HU pedía seleccionar el perfil principal (Arrendador/Arrendatario) y no existía RF. Se redefine como **preferencia de uso no excluyente**. | RQF-213 | M01 |
| HU03 | La HU describía el **cambio de contraseña con sesión iniciada**, que no existía en el catálogo (solo la recuperación), junto con sus validaciones (contraseña actual, no repetir la anterior, no reutilizar en 3 meses) y la notificación del cambio. | RQF-214 a RQF-218 | M01 |
| HU04 | La HU definía un **límite de 10 MB** por documento y un estado **"Pendiente de Verificación"** inexistentes en el catálogo. | RQF-219, RQF-220 | M03 |
| HU06 | La HU validaba la tarifa al **modificar** la publicación; el catálogo solo validaba el precio al crearla (RQF-073). | RQF-221 | M04 |
| HU07 | La HU definía un **máximo de 250 caracteres** para reglas personalizadas y la existencia de una **política de cancelación** configurable y visible en el detalle. | RQF-222, RQF-223, RQF-224 | M04 |
| HU21 | La HU exigía **motivo obligatorio** y validación de fechas en el bloqueo manual del calendario. | RQF-225, RQF-226 | M04 |
| HU17 | La HU exigía validar la **identidad verificada antes de pagar**; el caso de uso lo declaraba como precondición sin RF que lo respaldara. | RQF-227 | M06 |
| HU19 | La HU describía la **cancelación de la reserva por el arrendatario** con cálculo de devolución, ejecución del reembolso y notificación a las partes. El catálogo solo contemplaba el rechazo del arrendador, la expiración por falta de pago y la falta de firma. | RQF-228 a RQF-231 | M06 |
| HU25 | La HU pedía **calificación y reseña recíproca** (arrendador hacia arrendatario), el bloqueo de una segunda reseña por reserva y el recálculo del promedio de calificaciones. | RQF-232 a RQF-235 | M09 |
| HU26 | La HU requería que el administrador pudiera **consultar el listado de espacios publicados** para su supervisión. | RQF-236 | M11 |

**Catálogo total resultante: 236 requerimientos funcionales (RQF-001 a RQF-236).**

---

## 4. Cambios aplicados respecto de la versión anterior (27 RNF)

| RNF | Cambio aplicado | Motivo |
| :--- | :--- | :--- |
| RNF-002 | Se reescribió para eliminar el verbo funcional "completar el ciclo": ahora expresa la condición de tiempo (*"debe garantizar que el ciclo de pago se complete en..."*). | Evitar contenido funcional en un RNF. |
| RNF-003 | Se reescribió para eliminar los verbos "compilar y exportar". | Ídem anterior. |
| RNF-004 | Se reescribió para eliminar el verbo funcional "comprimir". | Ídem anterior. |
| RNF-012 | Se dividió en **RNF-012** (idempotencia) y **RNF-028** (conciliación), porque un requerimiento no debe contener dos condiciones distintas. | Regla de atomicidad también aplicada a los RNF. |
| RNF-018 | Se dividió en **RNF-018** (eliminación irreversible) y **RNF-029** (anonimización de la información transaccional). | Ídem anterior. |
| RNF-027 | Se reescribió para eliminar las acciones funcionales "generar la boleta" y "entregarla" (ya cubiertas por RQF-176 y RQF-211); ahora expresa el cumplimiento normativo. | Separación RF/RNF. |
| RNF-007 | Se ajustó el nombre y la redacción ("presentar sus interfaces" en lugar de "renderizar"). | Evitar lenguaje técnico de implementación. |
| RNF-017 | Se ajustó "almacenar log" por **"preservar los logs"**, manteniendo el foco en la integridad y no en una acción funcional. | Evitar duplicidad con el catálogo de RF. |
| Nuevos | Se agregaron **RNF-030 a RNF-043** (14 requerimientos) para completar las categorías exigidas por la retroalimentación: **Implementación** (contenedores Docker, motor de base de datos relacional, repositorio de código, CI/CD), **Almacenamiento** (capacidad y retención), **Portabilidad** (despliegue agnóstico, entorno local, reemplazabilidad) y completar **Flexibilidad**, **Mantenibilidad** y **Rendimiento**. | Cada categoría debe tener al menos 3 ejemplos. |

## Correcciones aplicadas respecto de la versión anterior (antecedente histórico)

| HU | Corrección aplicada |
|---|---|
| HU01 | El estado de la cuenta al registrarse se corrige de "activo" a **"No Verificado"**; la selección de rol pasa a **preferencia de uso no excluyente** (RQF-213); se agrega la aceptación de términos y condiciones (RQF-186, RQF-187) y el reenvío del token (RQF-188). |
| HU02 | El bloqueo se corrige de **3 intentos / 5 minutos** a **5 intentos / 30 minutos** (RQF-015, RQF-017); se agrega el cierre de sesión (RQF-023) y el bloqueo por cuenta no verificada (RQF-010). |
| HU03 | El enlace de recuperación se corrige de **10 a 15 minutos** (RQF-021); se separa el escenario de cambio autenticado del de recuperación y se agregan sus RF (RQF-214 a RQF-218). |
| HU04 | Se elimina el **Pasaporte** (el catálogo valida la Cédula ante el Registro Civil) y se incorpora el escenario **KYB (empresa)**, que no existía en ninguna HU; el peso máximo de archivo se fija en 10 MB (RQF-219) y se agrega el estado "Pendiente de Verificación" (RQF-220). |
| HU05 | Título máximo corregido de **100 a 70 caracteres** (RQF-063); precio mínimo corregido de **"> 0" a "> $5.000 CLP"** (RQF-073); se elimina el mínimo de 3 imágenes y se mantiene el máximo de 10 (RQF-075); se incorporan las validaciones de superficie, descripción y estados Borrador/Activa. |
| HU06 | Se agrega la validación del precio modificado (RQF-221) y se alinean los campos editables con RQF-195 a RQF-198. |
| HU07 | Se incorpora la política de cancelación (RQF-223, RQF-224) y la validación de 250 caracteres (RQF-222). |
| HU08 | Se corrige la regla: ocultar una publicación **no** se bloquea por reservas vigentes; solo se bloquea la **eliminación permanente** con reservas futuras (RQF-092). |
| HU09 | Se reescribe como descripción de equipamiento incluido. Los **adicionales con tarifa propia** quedan declarados fuera de alcance (requerirían nuevos RF y un caso de uso, además de modificar el desglose de cobro RQF-107). |
| HU14 | Se reemplaza "favoritos" por **consulta del historial de reservas** (RQF-199, CU-47), que sí está en el alcance y cubre la necesidad operativa; se documentó "favoritos" como fuera de alcance. |
| HU17 | Se elimina **Transbank** como alternativa: la pasarela del proyecto es **Mercado Pago**; se agrega la exigencia de identidad verificada antes de pagar (RQF-227) y la notificación de pago rechazado (RQF-201). |
| HU18 | Se elimina el comprobante PDF independiente (fuera de alcance: la constancia es el contrato firmado) y se corrige "ingresos acreditados" por **fondos retenidos en custodia** (RQF-117). |
| HU19 | Se alinea la cancelación a la **política de cancelación configurada** y se agregan los RF de cancelación, cálculo de devolución, reembolso y notificación (RQF-226 a RQF-231). |
| HU20 | Se elimina la sincronización iCal (fuera de alcance) y se mantiene el control de disponibilidad con bloqueo/desbloqueo (RQF-084, RQF-085). |
| HU21 | Se agregan el motivo obligatorio del bloqueo (RQF-225) y la validación de fechas (RQF-226). |
| HU22 | Se convierte en **consulta del historial de reservas del arrendador** (RQF-199, CU-47); el panel de estadísticas de ocupación queda fuera de alcance. |
| HU25 | Se incorpora la **calificación y reseña recíproca** del arrendador hacia el arrendatario (RQF-232, RQF-233), el bloqueo de una segunda reseña (RQF-234) y el cálculo del promedio (RQF-235); el plazo de 14 días y el límite de 500 caracteres quedan fuera de alcance. |
| HU26 | Se alinean las funciones al catálogo: búsqueda y bloqueo de cuentas (RQF-212, RQF-178–180), reportes (RQF-183), auditoría (RQF-184, RQF-185) y listado de espacios (RQF-236); 2FA y tablero de métricas quedan fuera de alcance. |
| HU27 | Se acota a la moderación de **reseñas reportadas** (RQF-181, RQF-182, RQF-207); la suspensión de anuncios reportados queda fuera de alcance. |
| HU28 | Se agrega el uso de la confirmación de recepción como evidencia (RQF-209) y la notificación del resultado a las partes (RQF-210). |
| HU29 | Se declara fuera del alcance de la ES1. |
| HU30 | Se reescribe sobre las notificaciones que el sistema efectivamente emite por correo (RF de notificación del catálogo); el centro de notificaciones en la aplicación y las preferencias de alerta quedan fuera de alcance. |
| Todas | Se reemplaza "Propietario"/"anfitrión" por **Arrendador** y "cliente" por **Arrendatario**; se agrega épica, prioridad, RF y CU a cada HU. |
| HU31, HU32 (nuevas) | Se crearon para cubrir el módulo **M02 (Perfil y Privacidad)**, que no tenía ninguna historia: gestión del perfil, fotografía y cuenta bancaria (HU31) y ejercicio del derecho de eliminación de la cuenta (HU32, Ley 21.719). |
| HU33 (nueva) | Se creó para cubrir el módulo **M07 (Contratos y Firma Electrónica)**, que no tenía historia: generación automática del contrato, firma electrónica por ambas partes, rechazo de firma y cancelación por falta de firma. |
| HU34 (nueva) | Se creó para cubrir la mensajería entre las partes del módulo **M09 (Comunicación y Reputación)**, que no estaba reflejada en ninguna historia. |
| HU35 (nueva) | Se creó para cubrir el módulo **M08 (Check-in y Check-out)**, que no tenía historia: check-in con evidencia, check-out y confirmación de recepción por el arrendador. |

## 5. Antecedentes de revisiones de ES1 y ES2

Las tablas de esta sección registran decisiones de sus cortes históricos. Las fichas actualizadas y el ADR definen el alcance objetivo vigente.

### 5.1 Brechas cerradas en la 1.ª revisión de completitud (RF y casos de uso)

| Brecha detectada | Solución aplicada |
|---|---|
| Liberación de la garantía en el flujo sin reclamos (solo existía `RQF-175` "saldo restante tras deducciones") | Se agregó **RQF-208** y se actualizó **CU-42** |
| El arrendador no tenía ninguna acción al término de la reserva | Se agregaron **RQF-205** y **RQF-206**, que dan origen a **CU-48** |
| No existía forma de consultar las reservas del usuario (precondición de CU-24, CU-26, CU-33, CU-34 y CU-42) | Se agregó **RQF-199**, que da origen a **CU-47** |
| No existía RF para reportar una reseña, aunque `RQF-181` presupone reseñas reportadas | Se agregó **RQF-207**, que da origen a **CU-49** |
| No existía RF de aceptación de términos y condiciones (ejemplo explícito de la retroalimentación) | Se agregaron **RQF-186** y **RQF-187** en **CU-01** |
| Ausencia de RF para reenviar el token de verificación | **RQF-188** integrado en **CU-02** |
| CRUD incompleto sobre entidades (cuenta bancaria, campos editables de la publicación, estado de la validación) | **RQF-189 a RQF-193** y **RQF-195 a RQF-198**, integrados en CU-08, CU-11, CU-12, CU-14 y CU-18 |
| Asimetría de notificación entre KYC y KYB | **RQF-194** integrado en **CU-12** |
| Cancelaciones automáticas que liberaban fechas sin RF que lo declarara; rechazo de pago sin notificación; rechazo de firma sin registro | **RQF-200**, **RQF-201** y **RQF-202**, integrados en CU-27/CU-28, CU-24 y CU-30 |
| Obligatoriedad de evidencia fotográfica en Check-in y Check-out no declarada | **RQF-203** y **RQF-204** integrados en CU-33 y CU-34 |
| Evidencia de recepción no consultable por el administrador al arbitrar; resultado de la disputa sin notificación; boleta sin envío | **RQF-209**, **RQF-210** y **RQF-211**, integrados en CU-41 y CU-42 |
| Imposibilidad de localizar una cuenta para bloquearla o desbloquearla | **RQF-212** integrado en **CU-43** |

### 5.2 Brechas cerradas en la 2.ª revisión (Historias de Usuario)

| Brecha detectada al revisar las HU | Solución aplicada |
|---|---|
| HU01 pedía seleccionar el rol principal en el registro sin RF que lo respaldara | **RQF-213** integrado en **CU-01** (como preferencia de uso no excluyente) |
| HU03 describía el cambio de contraseña con sesión iniciada y sus validaciones, inexistentes en el catálogo | **RQF-214 a RQF-218** → nuevo **CU-50** |
| HU04 definía un límite de 10 MB por documento y el estado "Pendiente de Verificación" | **RQF-219, RQF-220** integrados en **CU-11** |
| HU06 y HU07 exigían validaciones al editar (precio), reglas de 250 caracteres y política de cancelación configurable y visible | **RQF-221 a RQF-224** integrados en **CU-18** |
| HU21 exigía motivo obligatorio y validación de fechas en el bloqueo manual del calendario | **RQF-225, RQF-226** integrados en **CU-17** |
| HU17 exigía identidad verificada antes de pagar (estaba solo como pre-condición del CU) | **RQF-227** integrado en **CU-22** |
| HU19 describía la cancelación de la reserva por el arrendatario con devolución y notificación | **RQF-228 a RQF-231** → nuevo **CU-51** |
| HU25 pedía reputación recíproca, una reseña por reserva y promedio de calificaciones | **RQF-232 a RQF-235** integrados en **CU-35** |
| HU26 requería que el administrador pudiera consultar las publicaciones para supervisarlas | **RQF-236** → nuevo **CU-52** |

### 5.3 Observaciones abiertas (no bloqueantes)

1. **Solapamiento RF/RNF corregido:** `RNF-027` fue reformulado para expresar únicamente el cumplimiento normativo (timbrado del SII, formatos XML/PDF y plazo máximo de 24 horas), dejando la acción funcional en `RQF-176` y `RQF-211`. En la misma revisión se corrigieron los RNF con verbos funcionales (RNF-002, RNF-003, RNF-004) y se separaron los que mezclaban dos condiciones (RNF-012 y RNF-018). El catálogo de RNF quedó en **43 requerimientos**, con al menos 3 por categoría.
2. **Alcance confirmado en las HU (requiere validación del equipo):** la segunda revisión declaró explícitamente fuera del alcance de la ES1 los siguientes criterios: disponibilidad recurrente (HU24), centro de ayuda y tickets (HU29), favoritos (HU14), adicionales o equipamiento extra con tarifa (HU09), panel de estadísticas de ocupación del arrendador (HU22), centro de notificaciones dentro de la aplicación (HU30), doble factor de administrador y tablero de métricas globales (HU26), y moderación/suspensión de anuncios reportados (HU27). Si el equipo desea incorporarlos, corresponden nuevos RF y casos de uso.
3. **Contexto narrativo:** conviene agregar en `contexto_narrativo.md` una frase sobre la confirmación de recepción del arrendador (`RQF-205`, `RQF-206`) para mantener la coherencia del relato end-to-end.
4. **Numeración de figuras del informe:** al pegar los 11 diagramas en el documento Word, verificar que la numeración de imágenes del índice coincida (actualizar campos con `Ctrl+A → F9`).
