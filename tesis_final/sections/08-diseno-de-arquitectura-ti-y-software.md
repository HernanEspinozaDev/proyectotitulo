# CAPÍTULO VIII: DISEÑO DE ARQUITECTURA TI Y DEL SOFTWARE

## 8.1. Arquitectura TI bajo Framework TOGAF

En cumplimiento estricto del estándar internacional TOGAF (*The Open Group Architecture Framework*), la arquitectura de Tecnologías de Información de **espaciGo** se descompone y justifica en sus cuatro capas fundamentales:

**Figura 7**  
*Arquitectura Empresarial y de TI bajo las Cuatro Capas de TOGAF*

![](assets/figuras/fig07_arquitectura_togaf_capas.png)

*Nota.* Elaboración propia según el estándar The Open Group (2022).

### 8.1.1. Capa de Negocio
Modela los flujos operacionales del ecosistema de arriendo flexible (reserva con custodia en garantía, publicación con validación KYC/KYB y ejercicio de derechos ARCO de la Ley 21.719), articulados mediante eventos transaccionales auditables.

### 8.1.2. Capa de Aplicaciones
Estructurada bajo un modelo desacoplado compuesto por un Frontend con patrón *Backend for Frontend* (BFF) en **Next.js 16 / React 19** y un núcleo de servicios transaccionales de alto rendimiento compilado en **Go 1.27**. La comunicación inter-componentes se rige por contratos estrictos mediante una API REST documentada en OpenAPI 3.0.

### 8.1.3. Capa de Datos
Organiza la persistencia según el propósito de los datos:
*   **Persistencia Transaccional (OLTP):** Motor relacional **PostgreSQL 18** enriquecido con la extensión geoespacial **PostGIS 3.6**, gobernando 110 tablas normalizadas.
*   **Almacenamiento de Evidencias:** Repositorios de objetos en **Google Cloud Storage** con cifrado automático AES-256 en reposo para fotografías de *check-in/check-out* y contratos notarizados en PDF.
*   **Auditoría Inmutable:** Inyección asíncrona de registros de auditoría en **Google BigQuery** para trazabilidad legal oponible.

### 8.1.4. Capa de Infraestructura
Desplegada en la región sudamericana **Google Cloud Santiago (`southamerica-west1`)**, aprovechando servicios gestionados que garantizan alta disponibilidad, resiliencia ante desastres y autoescalado dinámico según la demanda.

---

## 8.2. Arquitectura de Software: Patrón Hexagonal en Go

El núcleo de servicios de espaciGo se implementa en **Go** adoptando el patrón de **Arquitectura Hexagonal (*Ports and Adapters*)**, garantizando que la lógica de negocio permanezca pura, aislada y sin dependencias acopladas hacia librerías externas o detalles de infraestructura:

```text
backend-go/
├── cmd/
│   └── api/
│       └── main.go                 # Punto de entrada y arranque del contenedor
├── internal/
│   ├── core/                       # NÚCLEO HEXAGONAL (Lógica de Dominio)
│   │   ├── domain/                 # Entidades puras y reglas invariantes
│   │   │   ├── espacio.go
│   │   │   ├── reserva.go
│   │   │   ├── usuario.go
│   │   │   └── transaccion.go
│   │   ├── ports/                  # Interfaces de abstracción
│   │   │   ├── in/                 # Puertos de Entrada (Casos de Uso)
│   │   │   │   ├── reserva_service.go
│   │   │   │   └── espacio_service.go
│   │   │   └── out/                # Puertos de Salida (Persistencia/APIs)
│   │   │       ├── espacio_repository.go
│   │   │       ├── escrow_gateway.go
│   │   │       └── firma_virtual_gateway.go
│   │   └── services/               # Implementación de los casos de uso
│   │       ├── reserva_usecase.go
│   │       └── espacio_usecase.go
│   └── adapters/                   # ADAPTADORES EXTERNOS
│       ├── in/                     # Adaptadores Primarios (Entrada)
│       │   └── http/               # Handlers REST, DTOs y Middlewares
│       └── out/                    # Adaptadores Secundarios (Salida)
│           ├── postgres/           # Implementación SQL con pgx/v5 y PostGIS
│           ├── mercadopago/        # Integración con pasarela de pagos
│           └── firmavirtual/       # Integración con firma remota
```

Este diseño garantiza una **testabilidad absoluta**: cada servicio de dominio se evalúa unitariamente mediante dobles de prueba (*mocks*) de los puertos de salida, verificando el comportamiento del negocio en milisegundos sin requerir una conexión activa a bases de datos o pasarelas financieras reales (Martin, 2017).

---

## 8.3. Capa de Presentación: Frontend BFF en Next.js 16 con React 19

La interfaz de usuario se construye sobre **Next.js 16** con **React 19**, implementando el patrón *Backend for Frontend* (BFF):
1. **Renderizado en Servidor (SSR) y Optimización SEO:** Las páginas de detalle de espacios comerciales y bodegas se prerenderizan en el servidor inyectando metadatos estructurados (*Schema.org*), permitiendo que los motores de búsqueda (Google) indexen los inmuebles de forma óptima.
2. **Capa Intermedia BFF Segura:** El servidor Next.js intercepta las credenciales de sesión, almacena los tokens de acceso JWT en cookies seguras con atributos `HttpOnly`, `SameSite=Strict` y `Secure`, impidiendo que scripts maliciosos en el cliente (ataques XSS) puedan extraer los tokens de autorización.
3. **Componentes React 19 Basados en Estado Dinámico:** La interfaz incorpora mapas interactivos dinámicos (Mapbox GL) que consultan el backend de forma asíncrona conforme el usuario desplaza el área visible del visor geoespacial.

---

## 8.4. Decisiones de Arquitectura (ADRs) y Stack Tecnológico Justificado

Cada componente del stack tecnológico se respalda formalmente mediante Registros de Decisión Arquitectónica (*Architectural Decision Records* - ADR):

**Tabla 9**  
*Registros de Decisión Arquitectónica (ADRs) y Justificación del Stack Tecnológico*

| ID del ADR | Decisión Tecnológica Adoptada | Alternativas Evaluadas | Criterios Técnicos de Decisión |
|---|---|---|---|
| **ADR-01** | **Backend en Go (Golang 1.27)** | Node.js (TypeScript), Python (FastAPI) | • Concurrencia nativa ultra-eficiente mediante Goroutines de bajo consumo de memoria (2 KB por hilo).<br>• Binario compilado nativo sin dependencias de runtime, garantizando arranques en frío (*cold starts*) en Cloud Run inferiores a 150 ms.<br>• Tipado estricto y alto rendimiento computacional en operaciones criptográficas y procesamiento de datos. |
| **ADR-02** | **PostgreSQL 18 con PostGIS 3.6** | MongoDB, MySQL | • Soporte estandarizado OGC para consultas geoespaciales con indexación GiST.<br>• Soporte nativo de rangos temporales `tsrange` y restricciones de exclusión para erradicar matemáticamente la sobre-reserva.<br>• Integridad transaccional ACID completa para la gestión de fondos y pagos en custodia. |
| **ADR-03** | **Google Cloud Run (Serverless)** | Kubernetes (GKE), Máquinas Virtuales (Compute Engine) | • Reducción del 100% en la sobrecarga de administración de clústeres y parches de sistema operativo.<br>• Escalado automático instantáneo desde cero hasta cientos de instancias según el tráfico concurrente.<br>• Eficiencia económica: cobro por milisegundo exacto de CPU y memoria consumida durante la ejecución de peticiones. |
| **ADR-04** | **Autenticación OAuth2 / JWT con RBAC** | Sesiones tradicionales en base de datos | • Arquitectura de autenticación desacoplada y sin estado (*stateless*).<br>• Verificación criptográfica local en el backend mediante clave pública asimétrica sin saturar la base de datos.<br>• Control de acceso basado en roles con granularidad por actor (*Arrendador, Arrendatario, Administrador*). |

*Nota.* Elaboración propia.

---

## 8.5. Contratos de Interfaz: Especificación OpenAPI y API REST

La comunicación entre el Frontend BFF y el Backend Hexagonal en Go se gobierna mediante una **especificación contractual estricta bajo el estándar OpenAPI 3.0 (Swagger)**.

Todos los endpoints respetan los principios arquitectónicos REST:
*   Uso coherente de verbos HTTP estándar (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).
*   Formato de intercambio de información exclusivamente en `application/json` con codificación UTF-8.
*   Estructura homogénea de respuestas exitosas y de error:

```json
{
  "success": true,
  "data": {
    "reserva_id": "res_849201f9-3d12-4a55",
    "espacio_id": "esp_10492834-91aa-4c22",
    "estado": "CONFIRMADA",
    "intervalo": {
      "inicio": "2026-11-15T09:00:00Z",
      "fin": "2026-11-18T18:00:00Z"
    },
    "monto_total": 240000,
    "garantia_retenida": 80000
  },
  "metadata": {
    "timestamp": "2026-11-03T22:30:00Z",
    "trace_id": "req-94a028f1b"
  }
}
```

*(El catálogo formal exhaustivo con los 48 endpoints de la API, esquemas JSON Schema y parámetros de cabecera se encuentra documentado en el **Anexo E: Catálogo de Endpoints OpenAPI**).*
