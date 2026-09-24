# Coordinación de __ENTREGA__

Este tablero parte vacío para no inventar la estructura de una entrega aún desconocida. Después de incorporar rúbrica, plantilla y plan, añadir tareas concretas a `tareas.json`: `id`, `titulo`, `objetivo`, `archivos` editables dentro de la entrega, `lecturas` y `depende`. Ver el ejemplo operativo de `Informes/ES2PT/coordinacion/`.

Desde la raíz del repositorio:

```powershell
python Informes/coordinar.py --entrega __ENTREGA__ contexto
python Informes/coordinar.py --entrega __ENTREGA__ tablero
python Informes/coordinar.py --entrega __ENTREGA__ tomar --agente nombre-unico
```

SQLite mantiene reservas y eventos; `bitacora.md` se genera al usar el tablero. Solo agentes que comparten el mismo `estado.sqlite3` tienen exclusión mutua. La investigación y documentación permanecen en Markdown; ningún estado de coordinación sustituye la revisión del informe.
