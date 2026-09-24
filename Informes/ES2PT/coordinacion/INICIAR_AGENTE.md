# Encargo para otra IA que trabajará en ES2

Trabaja en la misma carpeta del repositorio EspaciGo. Antes de editar, lee `AGENTS.md` y ejecuta desde la raíz:

```powershell
python Informes/coordinar.py contexto
python Informes/coordinar.py tablero
python Informes/coordinar.py tomar --agente NOMBRE_UNICO_DE_ESTA_INSTANCIA
```

Lee las fuentes que indique la tarea reservada y `historial --tarea ID` si otro agente la inició antes. Conserva el identificador `reserva` devuelto por `tomar`. Investiga y escribe **solo los archivos declarados** en esa tarea; registra fuente, fecha, método, hallazgos, incertidumbre y relación con ES1. No alteres archivos que otro agente tenga reservados ni edites ES1 o `build/`. No inventes citas, entrevistas, ventas, resultados, contratos ni aprobaciones. Para información cambiante consulta fuentes actuales y deja enlaces directos. Mantén Word/APA visual para el cierre indicado en el plan.

Mientras trabajas, registra hitos con `avance --tarea ID --agente NOMBRE --reserva TOKEN --nota "..."` y renueva la reserva si se acerca su vencimiento. Al acabar, usa `finalizar` con una nota que indique entregable, evidencia, límites y siguiente tarea. Si debes parar, usa `liberar` con el punto exacto desde el que continuar; si falta una condición externa indispensable, usa `bloquear`. Ningún estado del tablero equivale por sí solo a aprobación del informe.
