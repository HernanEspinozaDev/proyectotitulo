# CAPÍTULO XI: ESTRATEGIA DE IMPLEMENTACIÓN, DESPLIEGUE Y SEGURIDAD

## 11.1. Pipeline de Integración y Despliegue Continuo (CI/CD)

La entrega de valor técnico y la gobernanza del código fuente de **espaciGo** se automatizan mediante un pipeline de Integración y Despliegue Continuo (*CI/CD*) configurado sobre **GitHub Actions**, garantizando que cada cambio en el repositorio principal cumpla con los estándares de calidad y seguridad antes de impactar el entorno de producción:

**Figura 16**  
*Flujo de Automatización del Pipeline CI/CD en GitHub Actions*

![](assets/figuras/fig16_pipeline_ci_cd_github.png)

*Nota.* Elaboración propia en base a las etapas de integración y entrega continua del proyecto.

*Fases del Pipeline de Automatización:*
1. **Verificación Estática y Linter:** Valida estándares de estilo y análisis estático mediante `golangci-lint` para el código Go y ESLint/Prettier para la aplicación Next.js.
2. **Suite de Pruebas Automatizadas:** Ejecuta las pruebas unitarias y de integración. Si la cobertura del código cae por debajo del 80%, el pipeline aborta automáticamente la compilación.
3. **Construcción Contenerizada Multi-Stage:** Genera una imagen Docker minimalista de producción basada en `scratch` o `distroless`, reduciendo el peso del contenedor a menos de 25 MB y minimizando la superficie de ataque al no incluir intérpretes ni utilitarios de shell innecesarios.
4. **Despliegue Declarativo en Cloud Run:** El contenedor se despliega mediante la API de Google Cloud Run con una estrategia de despliegue progresivo (*canary deployment*), derivando inicialmente el 10% del tráfico y monitoreando las tasas de error antes de completar la conmutación al 100%.

---

## 11.2. Topología de Infraestructura Cloud en Google Cloud Platform (GCP)

La solución se despliega íntegramente sobre la infraestructura de clase mundial de **Google Cloud Platform**, aprovechando la región de baja latencia ubicada en Santiago de Chile (**`southamerica-west1`**):

**Figura 17**  
*Topología de Infraestructura Cloud en Google Cloud Platform (Región Santiago)*

![](assets/figuras/fig17_infraestructura_cloud_gcp.png)

*Nota.* Elaboración propia sobre servicios gestionados en Google Cloud Platform (región `southamerica-west1`).

### Segmentación de Red y Comunicaciones Privadas
En cumplimiento de las buenas prácticas de ciberseguridad industrial, la base de datos relacional y los clústeres de caché se alojan dentro de una **VPC privada con asignación de IPs privadas (RFC 1918)**. La comunicación entre los servicios contenerizados de Cloud Run y la base de datos PostgreSQL se canaliza exclusivamente mediante un **Serverless VPC Access Connector**, impidiendo que el motor de persistencia tenga interfaces expuestas hacia internet público:

**Figura 18**  
*Segmentación de Red Privada y Comunicaciones Seguras vía Serverless VPC Connector*

![](assets/figuras/fig18_segmentacion_red_vpc.png)

*Nota.* Elaboración propia según el diseño de seguridad de red en Google Cloud VPC.

---

## 11.3. Políticas de Ciberseguridad, Identidad (OAuth2/JWT) y Control de Acceso (RBAC)

La plataforma adopta el principio de **Privilegio Mínimo** y el modelo de seguridad **Zero Trust**:

1. **Gestión Centralizada de Secretos:** Ninguna clave de API, certificado o credencial de base de datos se almacena en el código fuente ni en variables de entorno fijas. Todos los secretos se custodian en **Google Secret Manager**, inyectándose dinámicamente en memoria durante el ciclo de vida del contenedor.
2. **Autenticación sin Estado con JWT Criptográfico:** Los tokens de sesión se firman mediante el algoritmo asimétrico **RS256** (RSA con SHA-256). El backend verifica la autenticidad del token mediante la clave pública local, validando la expiración estricta (15 minutos) y el token de refresco (*refresh token*) almacenado en Redis con rotación obligatoria.
3. **Control de Acceso Basado en Roles (RBAC):** Cada petición HTTP es evaluada por un middleware de autorización que intercepta los roles y scopes del usuario (`ROLE_ARRENDATARIO`, `ROLE_ARRENDADOR`, `ROLE_ADMIN`, `ROLE_AUDITOR`), impidiendo accesos no autorizados a datos de terceros (vulnerabilidad BOLA / IDOR).

---

## 11.4. Plan de Recuperación ante Desastres (DRP) y Protocolo Replay Anti-Restauración (Ley 21.719)

La continuidad operativa y el cumplimiento legal de la privacidad exigen una arquitectura de recuperación resiliente:

**Figura 19**  
*Plan de Recuperación ante Desastres (DRP) y Resiliencia de Datos*

![](assets/figuras/fig19_recuperacion_drp_replay_privacidad.png)

*Nota.* Elaboración propia en base a la política de continuidad de negocio y failover HA en Cloud SQL.

### 11.4.1. Arquitectura de Alta Disponibilidad y Resiliencia
La instancia de Google Cloud SQL se configura en modalidad de **Alta Disponibilidad (HA Multi-Zona)**, sincronizando sincrónicamente los datos entre dos zonas aisladas de la región Santiago (`southamerica-west1-a` y `southamerica-west1-b`). Ante la caída de un centro de datos físico, GCP ejecuta la conmutación por error (*failover*) automática en menos de 3 minutos sin intervención manual.

### 11.4.2. Protocolo de Reaprovechamiento Anti-Restauración (*Anti-Replay Restoration*)
En cumplimiento de los derechos de supresión de la **Ley N° 21.719**, se implementa un mecanismo de compensación que previene que la restauración de un respaldo antiguo reincorpore datos eliminados legítimamente:

**Figura 20**  
*Diagrama de Secuencia del Protocolo de Purga Anti-Restauración (Ley 21.719)*

![](assets/figuras/fig20_secuencia_anti_replay.png)

*Nota.* Elaboración propia según el protocolo DRP y exigencias de supresión de la Ley N° 21.719.

### 11.4.3. Respuesta ante Incidentes de Ingeniería (SRE)
El monitoreo proactivo se articula mediante **Google Cloud Monitoring** y alertas automatizadas que notifican al equipo de guardia ante cualquier anomalía en tasas de error o latencias:

**Figura 21**  
*Protocolo de Respuesta ante Incidentes de Ingeniería de Confiabilidad (SRE)*

![](assets/figuras/fig21_respuesta_incidentes_sre.png)

*Nota.* Elaboración propia sobre procedimientos de guardia y escalamiento SRE en Google Cloud Monitoring.
