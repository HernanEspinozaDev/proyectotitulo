# ANEXO E: CATÁLOGO DE CONTRATOS DE INTERFAZ OPENAPI

El catálogo de referencia corresponde a [planning/openapi.yaml](https://github.com/HernanEspinozaDev/espaciGo/blob/4e26d52b57d9687c4b6b7a778e89dbbb5be855e5/planning/openapi.yaml), commit `4e26d52b57d9687c4b6b7a778e89dbbb5be855e5`, especificación OpenAPI 3.1. La base relativa es `/api/v1`. El catálogo distingue las rutas de ensayo local por el prefijo `/local`.

**Tabla E.1**\
*Operaciones representativas del corte de desarrollo*

| Ruta | Métodos declarados |
|---|---|
| `/public/spaces` | GET |
| `/spaces` | GET, POST |
| `/local/booking-trial/catalog` | GET |
| `/local/booking-trial/quotes` | POST |
| `/local/booking-trial/reservations` | GET, POST |
| `/local/booking-trial/reservations/{reservationId}/payment` | POST |

*Nota.* Elaboración propia a partir de la especificación OpenAPI versionada.

La consulta pública y la consulta de ensayo tienen rutas separadas. PT-09 requiere identificar cuál se mide, la versión del servicio y el conjunto de datos utilizado. El catálogo documenta un corte de la interfaz de desarrollo. Las rutas de ensayo permiten verificar contratos internos con datos sintéticos. La habilitación de una integración externa requiere evidencias de autorización, idempotencia, conciliación y devolución según la operación.

El contrato local de ese corte enumera ocho códigos de categoría: `oficina`, `sala_multiproposito`, `bodega`, `estacionamiento`, `local_flexible`, `stand`, `quincho` y `parcela_eventos`. Casas de veraneo y hostales ilustran el alcance objetivo de la memoria. La incorporación de categorías requiere actualización del contrato y verificación de su operación.
