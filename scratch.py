import sqlite3
db = sqlite3.connect('Informes/estado.sqlite3')
res = db.execute("SELECT id, agente FROM reservas WHERE tarea_id='ES2-CLOUD'").fetchall()
print(res)
