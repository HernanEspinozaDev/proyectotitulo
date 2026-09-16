# 📋 Correcciones Solicitadas por la Profesora

> Resumen estructurado basado en las transcripciones de audio de retroalimentación.

---
** HECHO POR ANITA, LISTO!*
## 1. 📐 Metodología del Proyecto

### ❌ Error principal
Todos los grupos están usando **PMBOK (PINBO) como metodología única**, lo cual es incorrecto.

### ✅ Lo que debe hacerse
- Usar una **metodología híbrida**:
  - Modelo de procesos **iterativo-incremental**
  - **Mejores prácticas de PMBOK** para la gestión del proyecto
- El informe debe **justificar** por qué se eligió esa metodología y no otra (cuadro comparativo de metodologías). **Se debe argumentar que los requerimientos son predecibles y no existe un cliente real cambiando los requerimientos constantemente.**
- El cronograma debe incluir **etapas claras**: Planificación → Análisis → Diseño → Construcción → Prueba → Implementación
- Las iteraciones deben estar reflejadas en el **cronograma**

> [!IMPORTANT]
> Este error **impacta múltiples secciones del informe**: cronograma, gestión, secuencia de actividades, etc.

---

## 2. 📝 Requerimientos Funcionales

### ❌ Errores detectados

| # | Error | Ejemplo del grupo |
|---|-------|-------------------|
| 1 | **Verbos no atómicos** — se usan verbos como "gestionar" o "administrar" que implican múltiples acciones | "debe subir y gestionar una galería" |
| 2 | **Dos acciones en un solo requerimiento** | "debe bloquear y fijar" → son dos requerimientos distintos |
| 3 | **Verbo incorrecto** | "crear un anuncio" → debería ser "registrar una publicación" o "publicar un anuncio" |
| 4 | **Filtrar como acción del sistema** — filtrar es acción del usuario, no del sistema | "debe filtrar por precio" → "debe permitir buscar a través de filtros" |
| 5 | **Gestionar pagos como un solo requerimiento** | Se debe separar: pagar con tarjeta, pagar con débito, etc. |
| 6 | **Módulos colocados como requerimientos funcionales** — los módulos van solo en los casos de uso | |
| 7 | **Muy pocos requerimientos** | Si hay 10 tablas × 5 operaciones = 50 reqs. Solo de base de datos |

### ✅ Reglas obligatorias para los requerimientos funcionales
- **Un solo verbo atómico por requerimiento** (NO usar: gestionar, administrar, subir y gestionar)
- Redacción estándar: **"El sistema debe [verbo] [objeto]"**
- Verbos válidos: registrar, consultar, eliminar, modificar, bloquear, notificar, generar, ejecutar, etc.
- Separar cada acción: si hay 4 operaciones sobre una entidad → **4 requerimientos**
- Cantidad esperada: **cerca de 200 requerimientos** para un sistema completo

### 📌 Ejemplos de corrección

```
❌ El sistema debe subir y gestionar una galería
✅ El sistema debe agregar una imagen a la galería
✅ El sistema debe eliminar una imagen de la galería
✅ El sistema debe modificar una imagen de la galería
✅ El sistema debe consultar la galería de imágenes

❌ El sistema debe bloquear y fijar publicaciones
✅ El sistema debe bloquear una publicación
✅ El sistema debe fijar una publicación

❌ El sistema debe crear un anuncio de espacio comercial
✅ El sistema debe registrar una publicación de anuncio comercial

❌ El sistema debe aceptar los términos y condiciones y el derecho al olvido (mezclado)
✅ El sistema debe permitir aceptar los términos y condiciones (al registrar la cuenta)
✅ El sistema debe permitir eliminar los datos del usuario (derecho al olvido)

❌ El sistema debe filtrar la búsqueda por precio
✅ El sistema debe permitir buscar a través de filtros (precio, categoría, etc.)

❌ El sistema debe procesar pagos mediante pasarela de pago
✅ El sistema debe permitir pagar con tarjeta de crédito
✅ El sistema debe permitir pagar con débito

❌ El sistema debe subir fotografía de check in y check out (todo junto)
✅ El sistema debe permitir realizar check in mediante el llenado de un formulario
✅ El sistema debe permitir realizar check out

❌ El sistema debe permitir apertura de disputas (uno solo)
✅ El sistema debe permitir registrar un reclamo
✅ El sistema debe permitir consultar un reclamo
✅ El sistema debe permitir hacer seguimiento a un reclamo
```

---

## 3. 📋 Requerimientos No Funcionales

### ❌ Errores detectados
- Los requerimientos no funcionales están **redactados como información técnica**, no como requerimientos
- Falta redacción en formato estándar
- Se usan categorías pero **sin subcategorías claras**

### ✅ Lo que debe hacerse
- Redacción correcta: **"El sistema debe [condición de calidad]"**
- Incluir subcategorías: Seguridad, Rendimiento, Almacenamiento, Implementación, etc.
- Dar **al menos 3 ejemplos por categoría**

### 📌 Ejemplo de corrección

```
❌ "Sistema contenerizado y automatizado, código contenido en Docker"
✅ "El sistema debe estar implementado en contenedores Docker"
✅ "El sistema debe utilizar un motor de base de datos relacional como MariaDB"

❌ "Almacenamiento de contraseña" (solo título, sin redacción)
✅ "El sistema debe almacenar las contraseñas encriptadas en la base de datos
    utilizando el algoritmo bcrypt"

✅ "La aplicación instalada en el dispositivo móvil no debe ocupar
    más de 150 MB de almacenamiento"
✅ "El código fuente debe almacenarse en un repositorio GitHub o equivalente corporativo"
```

---

## 4. 🎭 Historias de Usuario

### ❌ Error detectado
- Las historias de usuario **no tienen criterios de aceptación bien redactados**
- Los criterios de aceptación están siendo redactados igual que los requerimientos funcionales

### ✅ Lo que debe hacerse
- Formato correcto:
  ```
  Como [rol de usuario], quiero [acción] para [beneficio/motivo]

  Criterios de aceptación:
  - [condición 1 — comportamiento esperado del sistema]
  - [condición 2]
  ```
- Los criterios de aceptación describen el **comportamiento esperado del sistema**
- Deben estar suficientemente documentadas para que un programador pueda implementarlas sin preguntas adicionales

---

## 5. 📊 Diagramas de Casos de Uso

### ❌ Errores detectados

| # | Error |
|---|-------|
| 1 | Los diagramas **no están organizados por módulo** — están dibujados individualmente por caso de uso |
| 2 | **Falta el nombre del sistema** y el nombre del módulo en cada diagrama |
| 3 | Se incluyen casos de uso que son **requerimientos no funcionales** (ej: encriptar contraseña) |
| 4 | Las relaciones **«include»** no están bien usadas — falta notación UML correcta |
| 5 | Las fichas de caso de uso están **incompletas** (faltan flujos alternativos) |
| 6 | No están numerados con ID |

### ✅ Lo que debe hacerse
- **Un diagrama por módulo** (no uno global con todo, ni uno individual por caso de uso)
- Cada diagrama debe tener: **nombre del sistema** (arriba) + **nombre del módulo** (en el recuadro)
- Usar correctamente la notación UML: actores, sistema, «include», «extend»
- **Encriptar contraseña** → NO es caso de uso, es requerimiento NO funcional (confidencialidad)
- Cada caso de uso debe tener un **ID único** para referenciar la ficha
- Las fichas deben incluir: flujo principal + flujos alternativos

### 📌 Estructura correcta del diagrama

```
┌─────────────────────────────────────────────────────┐
│                   NOMBRE DEL SISTEMA                │
│  ┌──────────────────────────────────────────────┐   │
│  │         Módulo: [Nombre del Módulo]          │   │
│  │                                              │   │
│  │   (CU-01) Iniciar sesión                     │   │
│  │   (CU-02) Recuperar contraseña               │   │
│  │   (CU-03) Registrar cuenta                   │   │
│  │                                              │   │
│  └──────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

---

## 6. 📁 Estructura del Informe (qué va en el cuerpo y qué en Anexos)

### ✅ Distribución correcta del contenido

| Contenido | Ubicación |
|-----------|-----------|
| Principales diagramas de casos de uso (resumen por módulo) | **Cuerpo del informe** |
| Totalidad de los diagramas de casos de uso | **Anexo B** |
| Requerimientos funcionales más importantes | **Cuerpo** (con referencia al anexo) |
| Todos los requerimientos funcionales | **Anexo C** |
| Fichas completas de casos de uso | **Anexo** (referenciadas por ID) |
| Historias de usuario completas | **Cuerpo + Anexo** |

> [!TIP]
> En el cuerpo usar tablas solo con ID + título del requerimiento. Así caben hasta 30 en una página.
> Al pie escribir: *"Para mayor detalle, ver Anexo X con la totalidad de los requerimientos funcionales"*

---

## 7. 🏗️ Arquitectura Empresarial

### ❌ Errores detectados
- La arquitectura empresarial está **muy incompleta**
- Se describieron tecnologías pero **sin el marco de arquitectura empresarial** correcto
- El organigrama muestra solo los 3 integrantes sin roles diferenciados

### ✅ Lo que debe hacerse
- Incluir los **4 tipos de arquitectura empresarial**:
  1. **Arquitectura de Procesos** — qué procesos de negocio existen en la organización
  2. **Arquitectura de Aplicación** — qué sistemas/apps se usan o construyen
  3. **Arquitectura de Datos** — modelo de datos, flujos de información
  4. **Arquitectura de Infraestructura Tecnológica** — servidores, nube, contenedores, frameworks
- El organigrama debe mostrar **roles dentro de la empresa** (aunque sean 3 personas):
  - Rol de Gerencia / Gestión general
  - Rol de Gestión de personas / Análisis
  - Rol de Desarrollo
- La empresa debe tener documentada su identidad: **misión, visión, objetivos estratégicos, FODA**

---

## 8. 📚 Marco Teórico

### ❌ Error detectado
- El marco teórico está **incompleto** y no cubre los conceptos necesarios para justificar el sistema

### ✅ Lo que debe hacerse
- Incluir **todo lo que se necesita conocer para implementar el sistema**
- Ejemplo para una plataforma de arriendo/comercial:
  - ¿Qué es una plataforma SaaS?
  - Modelos de negocio (freemium, premium, suscripción, etc.)
  - Pasarelas de pago disponibles (cómo funcionan, cuál se eligió y por qué)
  - Conceptos del dominio: inventario, galería, contratos digitales, gestión de espacios, etc.
- Cada concepto debe estar conectado con **una decisión de implementación del sistema**

> [!NOTE]
> El marco teórico no es una definición genérica — cada concepto debe justificar algo que el sistema va a hacer o cómo lo va a hacer.

---

## 9. 🗓️ Indicaciones de Entrega

- Se puede subir hoy en **versión borrador** (tanto la evaluación formativa como la sumativa)
- El **domingo** se actualiza la versión sumativa definitiva
- Si algo está listo antes del domingo, subirlo antes

---

## ✅ Checklist de Correcciones Pendientes

- [✅] **Metodología**: Cambiar a metodología híbrida (iterativo-incremental + PMBOK), agregar cuadro comparativo y justificación
- [ ✅] **Cronograma**: Reflejar las iteraciones y las etapas correctas del modelo híbrido
- [ ] **Requerimientos funcionales**: Reescribir con verbo atómico, un verbo por requerimiento, aumentar cantidad (~200)
- [ ] **Requerimientos no funcionales**: Reescribir en formato "El sistema debe...", con ejemplos y subcategorías
- [ ] **Historias de usuario**: Completar criterios de aceptación con comportamiento esperado del sistema
- [ ] **Diagramas de casos de uso**: Reorganizar por módulo, agregar nombre del sistema y nombre del módulo, corregir notación UML
- [ ] **Fichas de casos de uso**: Completar con flujo principal + flujos alternativos + ID único
- [ ] **Estructura del informe**: Mover detalles extensos a Anexos, dejar resumen en el cuerpo con referencias
- [ ] **Arquitectura empresarial**: Completar los 4 tipos de arquitectura + organigrama con roles + misión/visión/FODA
- [ ] **Marco teórico**: Ampliar con todos los conceptos clave necesarios para implementar el sistema
