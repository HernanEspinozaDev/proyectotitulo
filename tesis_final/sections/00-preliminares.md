# Dedicatoria

*Espacio reservado para el texto de los autores.*

# Agradecimientos

*Espacio reservado para el texto de los autores.*

# Resumen

La dispersión de anuncios, la incertidumbre sobre la disponibilidad y la coordinación manual dificultan el arriendo flexible de espacios en Chile. Para abordar este problema, el proyecto diseña espaciGo, una plataforma web para personas y organizaciones con nueve categorías de espacios de uso residencial, turístico, recreativo, comercial e industrial. La arquitectura modular utiliza Go, Next.js y PostgreSQL con PostGIS. El diseño combina publicación por titularidad, exclusión temporal, aceptación bilateral del contrato y cobros separados, con una modalidad opcional de firma electrónica.

El proyecto aplica un ciclo iterativo e incremental, con pruebas sobre datos sintéticos y criterios de aceptación por incremento. El inventario de migraciones identifica 110 tablas de aplicación, 104 de ellas contrastadas por nombre con la captura local V000075. El corte documental F5 registra 86 pruebas aprobadas y el recorrido F6 registra seis pruebas aprobadas entre los perfiles de borrador y documentos. En un ensayo aislado de PostgreSQL 18.6 con PostGIS, 200 conexiones completan 42.636 consultas geoespaciales en 15 segundos sin fallos, con una latencia media de 70,22 ms. La validación de carga de extremo a extremo, la recuperación conjunta de datos y archivos, y la habilitación de proveedores se mantienen como verificaciones del entorno objetivo.

*Palabras clave:* arriendo flexible, arquitectura modular, disponibilidad, PostgreSQL, PostGIS

# Abstract

Scattered listings, uncertain availability, and manual coordination complicate flexible space rental in Chile. This project designs espaciGo, a web platform for individuals and organizations covering nine categories of residential, tourism, recreational, commercial, and industrial spaces. Its modular architecture uses Go, Next.js, PostgreSQL, and PostGIS. The design combines publication by authorized holders, temporal exclusion, bilateral contract acceptance, separate charges, and an optional electronic signature.

The project follows an iterative and incremental approach using synthetic data. The migration inventory identifies 110 application tables, of which 104 match the V000075 local snapshot by name. F5 records 86 passing document verification tests, and F6 records six passing tests across the draft and document profiles. In an isolated PostgreSQL 18.6 and PostGIS test, 200 connections completed 42,636 geospatial queries in 15 seconds without failures, with a mean latency of 70.22 ms. End-to-end load, joint data and file recovery, and provider enablement remain to be validated in the target environment.

*Keywords:* flexible rental, modular architecture, availability, PostgreSQL, PostGIS
