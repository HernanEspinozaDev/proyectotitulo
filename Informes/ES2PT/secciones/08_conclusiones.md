# Conclusiones

## Decisiones que quedan sustentadas

El diseño conserva el backend modular de ES1 como una sola unidad desplegable, con módulos por dominio y adaptadores para terceros, y confirma PostgreSQL con PostGIS como persistencia operativa, exigida por RNF-038. El diccionario del Anexo B define las 43 tablas del producto completo y todas las categorías, con construcción incremental. La reserva y los bloqueos manuales comparten un calendario único con intervalos semiabiertos, cuya superposición se impide por exclusión, y las operaciones financieras se separan en intento de cobro, garantía, liquidación y eventos del proveedor, sin presumir que la pasarela permita todas ellas. La analítica se separa de la garantía de inmutabilidad de RNF-017; la propuesta de retención bloqueada con hash por lote requiere plazo aprobado y ensayo de alteración.

La Ley 21.719 se adoptó como criterio de diseño desde el primer incremento, con una matriz de tratamientos, un registro de solicitudes de titulares y una prueba planificada, sin declarar cumplimiento. La operación queda descrita con procedimientos de disponibilidad, continuidad y mantención, y la calidad, con un catálogo de dieciséis pruebas y una matriz de normas justificadas. El cronograma documenta la diferencia de incrementos de ES1 y propone hitos con evidencia de cierre.

## Contribución al proyecto

La entrega traduce la formulación de ES1 en un diseño verificable: cada proceso, caso de uso, entidad e interfaz conserva la trazabilidad hacia los requerimientos, los casos de uso y las historias de la base. El modelo de datos incluye campos, estados, permisos y restricciones como contrato para migraciones aún no escritas. También entrega instrumentos para medir: once indicadores y cinco niveles de servicio con su método, ventana y evidencia, además de trece ensayos previstos del modelo y dieciséis casos de prueba del producto. El Anexo A usa la misma comisión inicial del 3 % que el diccionario, separa el dinero del arrendador de los ingresos propios y presupone una instancia API mínima para los workers; sus supuestos se distinguen de cotizaciones y pagos observados.

## Resultados efectivamente obtenidos

Los resultados son documentales. No se ejecutó ninguna prueba del producto, no se midió ningún indicador, no se desplegó infraestructura y no se firmó ningún contrato. El diccionario no dispone todavía de migraciones aplicadas; las tarifas de Santiago son precios publicados y no una factura; la comparación de pagos divididos, la firma electrónica y la verificación de identidad siguen sin acceso ni cotización. Bajo la comisión de 3 % y el costo variable supuesto, la reserva de 100.000 CLP no genera contribución para fijos; el **VAN de caja simulado a 36 meses es −15.140.998 CLP** y la TIR no está definida porque todos los flujos son negativos. Estos números no miden demanda ni rentabilidad real.

## Limitaciones

La principal limitación es la ausencia de producto: sin implementación no hay medición ni ensayo de requisitos no funcionales. A eso se suman la falta de evidencia de demanda y precios por categoría, el acceso no habilitado a proveedores, el presupuesto todavía condicional y la revisión docente sin registrar. Santiago ya fue escogido como región; queda verificar costos reales y capacidad de la configuración elegida. El contenido nuevo exige una revisión final de referencias, figuras y Word cuando cierre la redacción.

## Trabajo posterior

1. Acordar capacidad semanal, plazos y responsables; concretar la política de retención de RNF-017 y probar su resistencia a alteración.
2. Obtener cotizaciones y contratos de pago con reparto, firma electrónica y verificación de identidad, y ensayar saldos, reversos y garantía en un entorno autorizado.
3. Medir oferta, demanda, precios finales y aceptación de la comisión por cada tipo de arriendo, y sustituir los supuestos por evidencia.
4. Escribir y aplicar las migraciones derivadas del Anexo B; construir por incrementos y ejecutar los ensayos del modelo y los casos de prueba con evidencia fechada.
5. Cerrar el contenido en Word: revisar las fuentes y figuras actualizadas, la salida institucional y la conservación de ES1.
6. Confirmar los metadatos académicos con el instrumento oficial y el calendario, y registrar la revisión docente.

El aporte de esta entrega no es un producto operativo, sino un diseño trazable y un conjunto de instrumentos de verificación que permiten construir y auditar EspaciGo sin dar por cierto lo que todavía no se ha demostrado.
