# CAPÍTULO XVI: Conclusiones y Recomendaciones

### 16.1. Conclusiones por objetivo

- **OE1. Diagnóstico y requisitos.** El diagnóstico traduce las dificultades de búsqueda y coordinación en 236 requerimientos funcionales, 43 no funcionales, 35 historias de usuario y 52 casos de uso. El catálogo admite nueve categorías y permite aplicar las reglas comunes de intermediación a usos residenciales, turísticos, recreativos, comerciales e industriales. El efecto sobre la vacancia requiere una medición de mercado.
- **OE2. Arquitectura y datos.** El inventario derivado del DDL identifica 110 tablas de aplicación. La captura local V000075 comparte 104 relaciones por nombre y registra coincidencia de tipo base y nulabilidad en 879 columnas de esas relaciones. El ensayo V1–V61 confirma que la exclusión temporal admite un solo ganador ante solicitudes solapadas en el escenario probado.
- **OE3. Construcción e integración.** LOCAL-1 acredita el recorrido sintético de su corte. F5 registra 86 pruebas de primer nivel aprobadas en verificación documental. F6 registra dos pruebas de borrador y cuatro del perfil documental. La contratación objetivo distingue la aceptación sin firma de la modalidad SimpleFirma y mantiene separados los cobros. La habilitación de proveedores requiere completar los flujos correspondientes y verificar sus resultados.
- **OE4. Calidad.** El ensayo SQL aislado en PostgreSQL 18.6 con PostGIS completa 42.636 consultas en 15 segundos con 200 conexiones, sin fallos y con 70,22 ms de latencia media. El resultado caracteriza la consulta geoespacial sobre datos sintéticos. La carga de extremo a extremo y la recuperación conjunta de base y archivos requieren ensayos del sistema integrado.
- **OE5. Operación y factibilidad.** La estrategia define controles de despliegue, seguridad y continuidad. La evaluación financiera detallada se integra en los apartados reservados.

### 16.2. Aporte de ingeniería

La propuesta relaciona las reglas del arriendo con mecanismos verificables de ocupación, autorización por recurso, preservación contractual y conciliación de pagos. La arquitectura separa las reglas del dominio de los adaptadores que operan con servicios externos.

El aporte en ciberseguridad incorpora autorización por recurso y por finalidad para proteger la evidencia privada, con la Ley 21.719 como referencia de diseño [@ley21719]. El control optimista mediante `If-Match` protege la selección de portada frente a actualizaciones concurrentes. El corte local F5 documenta verificaciones de escaneo, revocación, retención y permisos en el paquete documental. El ensayo GCP03 se detiene en la restauración de permisos de aplicación. El ensayo objetivo de recuperación conjunta conserva pendiente la comprobación de permisos sobre datos y archivos, según los capítulos XII y XIII y el Anexo F.

### 16.3. Limitaciones

La evidencia se concentra en escenarios sintéticos y cortes de ensayo. El catálogo vigente incluye Inmuebles, con los tipos casa, departamento, habitación y cabaña. Una casa de veraneo puede describirse como casa según la modalidad publicada. Los hostales ilustran un uso objetivo. El Anexo E describe el catálogo y el Capítulo XII delimita la evidencia de ejecución. El modelo conserva una unidad reservable exclusiva y el inventario compartido o de múltiples unidades requiere una especificación propia. La operación con clientes requiere verificar integraciones, recuperación conjunta de datos y archivos y el comportamiento bajo carga del entorno objetivo.

### 16.4. Recomendaciones

El siguiente incremento completa la demostración local del recorrido sin firma ni garantía. La integración de firma y la habilitación de garantía requieren verificaciones separadas. La preparación de un piloto también exige un ensayo de recuperación conjunta y medición de carga en el entorno objetivo.

**Figura 18**\
*Dependencias de los siguientes incrementos*

![](assets/figuras/fig23_hoja_ruta_tecnologica.png)

*Nota.* Elaboración propia. La figura muestra dependencias de verificación e integración.

La Figura 18 relaciona los incrementos de integración y los ensayos necesarios para preparar el piloto. El piloto puede medir conversión, tiempo de coordinación e incidencias por segmento. La recurrencia, la subdivisión, el aforo compartido y la validación de firmas externas permanecen diferidos según el ADR vigente.
