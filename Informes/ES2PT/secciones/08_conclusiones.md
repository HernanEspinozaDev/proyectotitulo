# Conclusiones

## Decisiones que quedan sustentadas

El diseño conserva el backend modular de ES1 como una sola unidad desplegable, con módulos por dominio y adaptadores para terceros, y confirma PostgreSQL con PostGIS como persistencia operativa, exigida por RNF-038. La reserva y los bloqueos manuales comparten un calendario único con intervalos semiabiertos, cuya superposición se impide por exclusión, y las operaciones financieras se separan en intento de cobro, garantía, liquidación y eventos del proveedor, sin presumir que la pasarela permita todas ellas. La analítica se separa de la exigencia de inmutabilidad de RNF-017, que sigue sin mecanismo seleccionado.

La Ley 21.719 se adoptó como criterio de diseño desde el primer incremento, con una matriz de tratamientos, un registro de solicitudes de titulares y una prueba planificada, sin declarar cumplimiento. La operación queda descrita con procedimientos de disponibilidad, continuidad y mantención, y la calidad, con un catálogo de dieciséis pruebas y una matriz de normas justificadas. El cronograma documenta la diferencia de incrementos de ES1 y propone hitos con evidencia de cierre.

## Contribución al proyecto

La entrega traduce la formulación de ES1 en un diseño verificable: cada proceso, caso de uso, entidad e interfaz conserva la trazabilidad hacia los requerimientos, los casos de uso y las historias de la base, y el modelo de datos incluye estados, permisos y un DDL propuesto. También entrega los instrumentos para medir: once indicadores y cinco niveles de servicio con su método, ventana y evidencia, además de doce ensayos del modelo y dieciséis casos de prueba del producto. El escenario económico queda explícito y condicional, con sus supuestos separados de las cotizaciones y de los fondos de terceros.

## Resultados efectivamente obtenidos

Los resultados son documentales. No se ejecutó ninguna prueba, no se midió ningún indicador, no se desplegó infraestructura y no se firmó ningún contrato. El DDL es texto propuesto y no se aplicó en un servidor; las tarifas de Santiago son precios publicados y no una factura; la comparación de pagos divididos, la firma electrónica y la verificación de identidad siguen sin acceso ni cotización. El flujo del Anexo A conserva su escenario base y su resultado no constituye una proyección validada: el VAN y la TIR dependen de demanda y precios que aún no se miden.

## Limitaciones

La principal es la ausencia de producto: sin implementación no hay medición, ni ensayo, ni demostración de los requisitos no funcionales. A eso se suman la falta de evidencia de demanda y precios por categoría, el acceso no habilitado a los proveedores, la aprobación pendiente de la región y del presupuesto, y la revisión docente sin registrar. El aparato de referencias conserva deudas conocidas —el orden de primera referencia de los anexos y las fechas de las fuentes web— y el perfil institucional debe resolverse antes de generar el Word final.

## Trabajo posterior

1. Aprobar con el equipo la región, el mecanismo de inmutabilidad de RNF-017, el alcance de demostración y la capacidad semanal, y actualizar el presupuesto con la cotización de Santiago.
2. Obtener cotizaciones y contratos de pago con reparto, firma electrónica y verificación de identidad, y ensayar saldos, reversos y garantía en un entorno autorizado.
3. Medir oferta, demanda, precios finales y aceptación de la comisión por cada tipo de arriendo, y sustituir los supuestos por evidencia.
4. Construir el producto, aplicar el DDL y ejecutar los ensayos del modelo y los casos de prueba con evidencia fechada.
5. Cerrar el contenido en Word: resolver el orden de los anexos, completar las fechas de las fuentes, aprobar o mantener desactivado el perfil y verificar la conservación de ES1.
6. Confirmar los metadatos académicos con el instrumento oficial y el calendario, y registrar la revisión docente.

El aporte de esta entrega no es un producto operativo, sino un diseño trazable y un conjunto de instrumentos de verificación que permiten construir y auditar EspaciGo sin dar por cierto lo que todavía no se ha demostrado.

