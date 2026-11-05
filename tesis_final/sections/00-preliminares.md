# Dedicatoria

*Espacio reservado para el texto de los autores.*

# Agradecimientos

*Espacio reservado para el texto de los autores.*

# Resumen

La dispersión de los anuncios, la incertidumbre sobre la disponibilidad y la coordinación manual dificultan el arriendo flexible de espacios en Chile. El proyecto diseña espaciGo, una plataforma web de intermediación para personas y organizaciones que ofrecen o arriendan espacios de uso residencial, turístico, recreativo, comercial e industrial. El catálogo contempla nueve categorías. Mediante un enfoque iterativo e incremental, el proyecto define una arquitectura hexagonal con Go, Next.js y PostgreSQL con PostGIS. El diseño incorpora búsqueda geográfica, control de solapamientos de reservas y aceptación bilateral del contrato, con firma electrónica opcional.

La especificación reúne 236 requerimientos funcionales, 43 no funcionales, 35 historias de usuario y 52 casos de uso. El inventario DDL identifica 110 tablas de aplicación, de las cuales 104 coinciden por nombre con la captura local V000075. El corte F5 registra 86 pruebas aprobadas de verificación documental y F6 registra seis pruebas aprobadas en los perfiles de borrador y documentos. En un ensayo aislado de PostgreSQL 18.6 con PostGIS y datos sintéticos, 200 conexiones completan 42.636 consultas geoespaciales en 15 segundos sin fallos, con una latencia media de 70,22 ms. La propuesta establece reglas verificables para buscar, reservar y contratar espacios. La validación de carga de extremo a extremo, la recuperación conjunta de datos y archivos y la habilitación de proveedores quedan pendientes en el entorno objetivo.

**Palabras clave**

Arriendo flexible de espacios, arquitectura hexagonal, concurrencia espaciotemporal, PostgreSQL, PostGIS.

# Abstract

Scattered listings, uncertain availability, and manual coordination complicate flexible space rental in Chile. The project designs espaciGo, a web platform that connects individuals and organizations offering or renting residential, tourism, recreational, commercial, and industrial spaces. The catalog covers nine categories. The project uses an iterative and incremental approach and defines a hexagonal architecture with Go, Next.js, and PostgreSQL with PostGIS. The design supports geographic search, prevents overlapping bookings, and records acceptance by both parties, with an optional electronic signature.

The specification includes 236 functional requirements, 43 nonfunctional requirements, 35 user stories, and 52 use cases. The DDL inventory identifies 110 application tables, 104 of which match the V000075 local snapshot by name. The F5 verification run records 86 passing document verification tests, and F6 records six passing tests across the draft and document profiles. In an isolated PostgreSQL 18.6 and PostGIS test with synthetic data, 200 connections complete 42,636 geospatial queries in 15 seconds without failures, with a mean latency of 70.22 ms. The proposed design establishes verifiable rules for searching for spaces, booking them, and formalizing rental agreements. End-to-end load validation, joint recovery of data and files, and provider enablement remain pending in the target environment.

**Keywords**

Flexible space rental, hexagonal architecture, spatiotemporal concurrency, PostgreSQL, PostGIS.
