# Coordinación de agentes para ES2

Este tablero permite que varias instancias de Codex u otras IA trabajen **en el mismo espacio de archivos** sin tomar la misma investigación. `tareas.json` versiona el trabajo y sus dependencias; `estado.sqlite3` guarda reservas, vencimientos y eventos de forma transaccional; `bitacora.md` es la vista legible que se actualiza automáticamente. `pendientes.md` sigue siendo la lista académica general: terminar una tarea del tablero no marca por sí solo un criterio de la rúbrica.

Para iniciar otra IA, entregarle [este encargo breve](INICIAR_AGENTE.md) y acceso a la misma carpeta o base SQLite compartida.

## Al entrar a una sesión

Desde la raíz del repositorio:

```powershell
python Informes/coordinar.py contexto
python Informes/coordinar.py tablero --json
python Informes/coordinar.py tomar --agente codex-investigacion-1
```

Usar un nombre de agente **único por instancia**. `tomar` reserva la primera tarea habilitada sin dependencias pendientes ni archivos compartidos con otra reserva; `--tarea ES2-TRIB` pide una específica. La salida muestra `reserva` (identificador de esa asignación), lecturas, entregables y avance previo. Leer los archivos indicados y `git status` antes de editar: puede haber trabajo local anterior que no se debe sobrescribir. Las investigaciones paralelas escriben archivos **INV propios**. La integración de cuerpo, Anexo A, bibliografía y pendientes espera los cinco registros y pertenece a `ES2-INTEGRAR`.

`contexto` imprime el [resumen operativo](RESUMEN.md), el orden de lectura y el estado de cada tarea. `tomar` añade los últimos tres eventos de la tarea para facilitar un relevo; el historial completo está en `historial --tarea ID` y `bitacora.md`.

## Registrar y traspasar

```powershell
python Informes/coordinar.py avance --tarea ES2-TRIB --agente codex-investigacion-1 --reserva ID --nota "Fuentes SII revisadas; falta separar IVA de comisión y publicidad"
python Informes/coordinar.py renovar --tarea ES2-TRIB --agente codex-investigacion-1 --reserva ID
python Informes/coordinar.py liberar --tarea ES2-TRIB --agente codex-investigacion-1 --reserva ID --nota "Continuar desde INV-014, sección 3; no se verificó documento tributario"
python Informes/coordinar.py historial --tarea ES2-TRIB
```

`avance` y `renovar` extienden la reserva 90 minutos por defecto; usar `--minutos` entre 5 y 240. Antes de terminar una sesión, registrar qué fuente se consultó, qué archivo cambió, qué se comprobó y el siguiente paso. `liberar` deja el trabajo retomable. Una reserva caducada se libera al siguiente acceso al tablero; el agente anterior debe detenerse y tomarla de nuevo antes de escribir. El identificador de reserva impide que otra instancia con el mismo nombre cierre una tarea ajena.

Con el entregable escrito:

```powershell
python Informes/coordinar.py finalizar --tarea ES2-TRIB --agente codex-investigacion-1 --reserva ID --nota "INV-014 completo como contraste documental; contador y SII siguen pendientes"
python Informes/coordinar.py exportar
```

`finalizar` exige que todos los archivos declarados para la tarea existan. Significa que **se entregó la investigación delimitada**, no que una hipótesis, cumplimiento legal o validación docente quedó confirmada. `bloquear` registra una dependencia externa real; otro agente podrá usar `desbloquear --tarea ... --agente ... --nota ...` cuando haya evidencia nueva. No poner credenciales ni datos personales en notas. La bitácora puede incorporarse a Git para compartir el historial; el SQLite se ignora por ser estado vivo y no fusionable.

## Alcance de la exclusión mutua

SQLite coordina procesos que apuntan **al mismo archivo de estado**. Con varios agentes en una carpeta de trabajo, el valor predeterminado es suficiente. Con worktrees diferentes en el mismo equipo, definir la misma ruta absoluta en `INFORMES_COORD_DB` y mantener `tareas.json` sincronizado. El archivo `bitacora.md` de cada worktree es una instantánea, no la autoridad de reserva. Distintos computadores o clones sin estado compartido **no están coordinados**; para ese caso se necesitaría un servicio central o un tablero remoto con operación atómica.

Usar una base SQLite distinta para cada entrega (`ES2PT`, `ES3PT`, etc.). Si se borra el estado local ignorado por Git, la bitácora conserva el relato de avances, pero las reservas vivas deben reconstruirse antes de volver a asignar tareas.

No editar ES1, `build/` ni `perfil_es2.json` durante esta fase. Los agentes de investigación pueden agregar enlaces a fuentes en su INV; `ES2-INTEGRAR` incorpora solo fuentes usadas a `referencias.bib` y actualiza las secciones. Word sigue deshabilitado hasta el cierre de contenido.
