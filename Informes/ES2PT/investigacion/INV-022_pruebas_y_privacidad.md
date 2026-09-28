# INV-022 — Definición de Pruebas y Privacidad (Leyes 21.719 y 19.628)

- Consulta documental: 23-09-2026.
- Estado: Decisiones operativas para la sección V del informe ES2PT y configuración de la Matriz de Privacidad en Anexo B.
- Objetivo: Establecer las herramientas de prueba, confirmar aplicabilidad de leyes de privacidad y justificar la política de retención y eliminación.

## Análisis Jurídico de Privacidad y Retención

### Ley 21.719 y Ley 19.628
La Ley 19.628 rige actualmente el tratamiento de datos personales en Chile, pero la Ley 21.719 (que entrará en vigencia en diciembre de 2026) introduce los conceptos de **Privacidad desde el Diseño**, el derecho al **Olvido (Supresión)** y la **Portabilidad**. 
Para EspaciGo, esto requiere justificar claramente la base legal de cada dato:
1. **Datos Financieros y Comerciales:** Las facturas, comisiones y comprobantes de pago deben conservarse por **5 años** para fines tributarios (Código Tributario). Esto entra en conflicto aparente con la "supresión en 72 horas" de RNF-026, por lo que **se aclara jurídicamente que el RNF-026 solo aplica a datos no sujetos a obligaciones de conservación legal o contractual**.
2. **Datos del Perfil del Usuario:** El nombre, correo y preferencias son datos recolectados bajo el "Consentimiento" y "Ejecución del contrato". Al eliminar una cuenta, estos datos se deben eliminar o anonimizar en las 72 horas exigidas internamente, preservando intactos los registros financieros, donde el ID del usuario se reemplazará por una clave anónima (anonimización) para no romper la integridad referencial.
3. **Firma y Contratos (Ley 19.799):** Los contratos de arriendo se pueden firmar mediante firma electrónica simple para acuerdos comerciales genéricos, ya que la Ley 21.461 sobre arriendo de predios urbanos no exige firma electrónica avanzada para todos los tipos de espacios (ej. oficinas flexibles por hora).

## Herramientas de Prueba y Entornos

Para cumplir con el catálogo del Anexo C sin depender del equipo local de cada desarrollador, se ha decidido lo siguiente para la etapa de pruebas:
- **Pruebas Unitarias e Integración (CI):** Se utilizará **GitHub Actions**. Todas las pruebas definidas en PT-01, PT-04, PT-05 se automatizarán en el pipeline.
- **Entorno de Staging (GCP):** Las pruebas de humo (PT-13), capacidad (PT-09, PT-10) y privacidad (PT-16) se ejecutarán en un proyecto de GCP dedicado a *Staging* utilizando réplicas sanitizadas o sintéticas, evitando datos personales reales.
- **Pruebas de Carga:** Se utilizará la herramienta **k6** (o equivalente) integrada en GitHub Actions para inyectar tráfico medido y verificar la latencia de ≤ 2 segundos y el manejo de 200 usuarios concurrentes.

Estas decisiones reemplazan los supuestos pendientes de la sección 05_01 y 05_02, dotando de especificidad al plan y a las normas justificadas.
