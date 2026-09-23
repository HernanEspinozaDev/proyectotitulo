# Contexto compartido de EspaciGo

Este directorio conserva la continuidad entre entregas. Describe lo formulado en ES1; no certifica implementación, disponibilidad de APIs ni viabilidad comercial o normativa actual.

## Línea base congelada de ES1

El informe final de ES1 y sus anexos son la base inmutable para ES2 y las siguientes entregas. Consulta la [línea base congelada](linea_base_ES1.md). Se leen para obtener contexto, requisitos, actores, decisiones y terminología, pero no se editan ni se regeneran encima. Las investigaciones nuevas se guardan en la carpeta `investigacion/` de la entrega activa.

## Orden de lectura

1. Este resumen y [decisiones](decisiones.md).
2. `contexto.md`, `pendientes.md` e `informe.json` de la entrega activa.
3. Su rúbrica, plantilla y secciones relacionadas con el cambio.
4. Las fuentes de ES1 enlazadas abajo cuando se necesite detalle.

## Proyecto y objetivo

EspaciGo se propone como un marketplace SaaS B2B2C para publicar, buscar, reservar y gestionar espacios comerciales flexibles. ES1 plantea reducir fricción en reserva, pago, formalización del arriendo y trazabilidad. La formulación y arquitectura están en el [informe utilizado para Word](../ES1PT/docx/informe.md); la narración general está en [contexto narrativo de ES1](../ES1PT/contexto_narrativo.md).

## Actores y módulos

Actores humanos: Visitante, Usuario Registrado, Arrendador, Arrendatario y Administrador. «Propietario» es un sinónimo de Arrendador en las historias de usuario. Los roles Arrendador y Arrendatario pueden coexistir.

| Módulo | Responsabilidad propuesta |
| --- | --- |
| M01 | Autenticación y gestión de cuenta |
| M02 | Perfil y privacidad |
| M03 | Verificación de identidad KYC/KYB |
| M04 | Gestión de publicaciones |
| M05 | Búsqueda y cotización |
| M06 | Reservas y pagos |
| M07 | Contratos y firma electrónica |
| M08 | Check-in y check-out |
| M09 | Comunicación y reputación |
| M10 | Disputas, payout y facturación |
| M11 | Administración y auditoría |

Registro Civil, SII, Mercado Pago y FirmaVirtual figuran como actores externos propuestos. La definición detallada y sus vínculos están en [Anexo A](../ES1PT/docx/anexos/A_actores_y_modulos.md).

## Trazabilidad

Preservar `RQF-###`, `RNF-###`, `CU-##`, `HU##` y M01–M11. Los catálogos son los [anexos B–E](../ES1PT/docx/anexos/). ES1 declara 236 RF, 43 RNF, 52 casos de uso y 35 historias; no convertir esos conteos en restricciones de las futuras entregas.

Ante contradicciones, registrar el conflicto y su evidencia en la entrega activa. Por ejemplo, el anexo A todavía contiene una mención histórica a «185/185» junto al catálogo ampliado de 236: no corregir silenciosamente la entrega cerrada ni usar esa frase como conteo vigente.

## Estado y evolución

El informe propone Next.js, Go, PostgreSQL, Docker y GCP; la auditoría de documentación no equivale a pruebas del producto. Para afirmar un avance en ES2 o ES3, agregar la evidencia y fecha en el contexto de esa entrega. Actualizar este resumen solo para decisiones compartidas explícitas, conservando su procedencia.
