import sqlite3
db = sqlite3.connect('Informes/estado.sqlite3')
res = db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print(res)
if ('reserva',) in res or ('reservas',) in res:
    print(db.execute("PRAGMA table_info(reserva)").fetchall())
    print(db.execute("SELECT * FROM reserva WHERE tarea='ES2-CLOUD'").fetchall())
