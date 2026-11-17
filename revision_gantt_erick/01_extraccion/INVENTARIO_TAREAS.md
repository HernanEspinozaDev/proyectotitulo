# Inventario de tareas extraído de espacigo.mpp

Los ID corresponden a las filas de Project. El ID 0 es el resumen del proyecto. No se modifican nombres, fechas ni dependencias.

| ID | EDT/WBS | Tipo | Nombre original | Inicio | Fin | Duración | Predecesoras | Holgura |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | Resumen | msproj11 | 2009-08-11 08:00 | 2010-01-20 19:00 | 117.0d | — | 0.0d |
| 1 | 1 | Resumen | 1 Fase 0: Inicio y configuracion del proyecto | 2009-08-11 09:00 | 2009-08-24 19:00 | 10.0d | — | 0.0d |
| 2 | 1.1 | Actividad | 1.1 Levantamiento y validacion de requerimeintos(catálogos RF/RNF) | 2009-08-11 09:00 | 2009-08-17 19:00 | 5.0d | — | 0.0d |
| 3 | 1.2 | Actividad | 1.2 Definición de arquitectura TI y matriz de decisiones (ADR) | 2009-08-18 09:00 | 2009-08-24 19:00 | 5.0d | 2 FS | 107.0d |
| 4 | 1.3 | Actividad | 1.3 Configuración del entorno de contenedores (Docker) y pipeline CI/CD en GCP | 2009-08-18 09:00 | 2009-08-24 19:00 | 5.0d | 2 FS | 0.0d |
| 5 | 2 | Resumen | 2 Fase 1: Incremento1- Identidad y acceso | 2009-08-25 09:00 | 2009-09-14 19:00 | 15.0d | — | 0.0d |
| 6 | 2.1 | Actividad | 2.1 Desarrollo Backend(Go) - M01: Autenticacion y gestion de cuenta | 2009-08-25 09:00 | 2009-08-31 19:00 | 5.0d | 4 FS | 0.0d |
| 7 | 2.2 | Actividad | 2.2 Desarrollo Backend (Go) - M02: Perfil y privacidad del usuario | 2009-09-01 09:00 | 2009-09-07 19:00 | 5.0d | 6 FS | 92.0d |
| 8 | 2.3 | Actividad | 2.3 Desarrollo Backend (Go) - M03: Verificación de identidad (KYC / KYB con Registro Civil y SII) | 2009-09-08 09:00 | 2009-09-14 19:00 | 5.0d | 7 FS | 92.0d |
| 9 | 2.4 | Actividad | 2.4 Desarrollo Frontend (Next.js) - Pantallas de autenticación, perfil y verificación | 2009-09-01 09:00 | 2009-09-14 19:00 | 10.0d | 6 FS | 0.0d |
| 10 | 3 | Resumen | 3 Fase 2: Incremento 2 - Oferta y Búsqueda | 2009-09-15 09:00 | 2009-10-19 19:00 | 25.0d | — | 0.0d |
| 11 | 3.1 | Actividad | 3.1 Desarrollo Backend (Go) - M04: Gestión de publicaciones y calendario de disponibilidad | 2009-09-15 09:00 | 2009-09-28 19:00 | 10.0d | 9 FS | 0.0d |
| 12 | 3.2 | Actividad | 3.2  Desarrollo Backend (Go) - M05: Búsqueda, filtros y cotización con PostGIS | 2009-09-29 09:00 | 2009-10-12 19:00 | 10.0d | 11 FS | 72.0d |
| 13 | 3.3 | Actividad | 3.3 Desarrollo Frontend (Next.js) - Catálogo geolocalizado, mapa y detalle de espacios | 2009-09-29 09:00 | 2009-10-19 19:00 | 15.0d | 11 FS | 0.0d |
| 14 | 4 | Hito | 4 Hito 1: Primera Entrega / Evaluación (3 de Noviembre) | 2009-10-19 19:00 | 2009-10-19 19:00 | 0.0d | 13 FS | 0.0d |
| 15 | 5 | Resumen | 5 Fase 3: Incremento 3 - Reservas y Pagos (Escrow) | 2009-10-20 09:00 | 2009-11-12 19:00 | 18.0d | — | 0.0d |
| 16 | 5.1 | Actividad | 5.1 Desarrollo Backend (Go) - M06: Motor de reservas y prevención de dobles reservas (ACID) | 2009-10-20 09:00 | 2009-10-29 19:00 | 8.0d | 14 FS | 0.0d |
| 17 | 5.2 | Actividad | 5.2 Integración API Mercado Pago - Pasarela de pago, tokenización y retención de fondos (Escrow) | 2009-10-30 09:00 | 2009-11-09 19:00 | 7.0d | 16 FS | 52.0d |
| 18 | 5.3 | Actividad | 5.3 Desarrollo Frontend (Next.js) - Flujo de reserva, cotización y pasarela de pagos | 2009-10-30 09:00 | 2009-11-12 19:00 | 10.0d | 16 FS | 0.0d |
| 19 | 6 | Resumen | 6 Fase 4: Incremento 4 - Contratación y Operación | 2009-11-13 09:00 | 2009-12-07 19:00 | 17.0d | — | 0.0d |
| 20 | 6.1 | Actividad | 6.1 Integración API FirmaVirtual - Generación y firma electrónica avanzada de contratos | 2009-11-13 09:00 | 2009-11-23 19:00 | 7.0d | 18 FS | 0.0d |
| 21 | 6.2 | Actividad | 6.2 Desarrollo Backend (Go) - M08: Check-in y Check-out con evidencia fotográfica (Cloud Storage) | 2009-11-24 09:00 | 2009-12-03 19:00 | 8.0d | 20 FS | 34.0d |
| 22 | 6.3 | Actividad | 6.3 Desarrollo Frontend (Next.js) - Módulos de contrato y flujos de check-in/out | 2009-11-24 09:00 | 2009-12-07 19:00 | 10.0d | 20 FS | 0.0d |
| 23 | 7 | Hito | 7 Hito 2: Segunda Entrega / Evaluación (17 de Noviembre) | 2009-12-07 19:00 | 2009-12-07 19:00 | 0.0d | 22 FS | 0.0d |
| 24 | 8 | Resumen | 8 Fase 5: Incremento 5 - Reputación, Disputas y Liquidación | 2009-12-08 09:00 | 2009-12-30 19:00 | 17.0d | — | 0.0d |
| 25 | 8.1 | Actividad | 8.1 Desarrollo Backend (Go) - M09: Comunicación por chat y sistema de reputación/reseñas | 2009-12-08 09:00 | 2009-12-16 19:00 | 7.0d | 23 FS | 0.0d |
| 26 | 8.2 | Actividad | 8.2 Desarrollo Backend (Go) - M10: Gestión de disputas, arbitraje de garantía, Payout y boleta de comisión | 2009-12-17 09:00 | 2009-12-28 19:00 | 8.0d | 25 FS | 17.0d |
| 27 | 8.3 | Actividad | 8.3 Desarrollo Frontend (Next.js) - Vistas de reseñas, centro de disputas y paneles de liquidación | 2009-12-17 09:00 | 2009-12-30 19:00 | 10.0d | 25 FS | 0.0d |
| 28 | 9 | Hito | 9 Hito 3: Tercera Entrega / Evaluación (1 de Diciembre) | 2009-12-30 19:00 | 2009-12-30 19:00 | 0.0d | 27 FS | 0.0d |
| 29 | 10 | Resumen | 10 Fase 6: Cierre, Administración, Pruebas y Despliegue Final | 2009-08-11 08:00 | 2010-01-20 19:00 | 117.0d | — | 0.0d |
| 30 | 10.1 | Actividad | 10.1 Desarrollo Backend y Frontend - M11: Panel de administración, backoffice y auditoría inmutable (BigQuery) | 2009-12-31 09:00 | 2010-01-07 19:00 | 6.0d | 28 FS | 0.0d |
| 31 | 10.2 | Actividad | 10.2 Pruebas de aceptación de usuario (UAT), pruebas de estrés y corrección de hallazgos | 2010-01-08 09:00 | 2010-01-14 19:00 | 5.0d | 30 FS | 0.0d |
| 32 | 10.3 | Actividad | 10.3 Ajustes finales de documentación técnica e informe de cierre del proyecto | 2010-01-15 09:00 | 2010-01-20 19:00 | 4.0d | 31 FS | 0.0d |
| 33 | 10.4 | Hito | 11 Hito Final: Entrega y Defensa del Proyecto (Semana del 15 de Diciembre) | 2009-08-11 08:00 | 2009-08-11 08:00 | 0.0d | — | 117.0d |
