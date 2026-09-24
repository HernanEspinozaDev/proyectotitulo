import sqlite3
db = sqlite3.connect('Informes/ES2PT/coordinacion/estado.sqlite3')
res = db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print(res)
for t in res:
    print(db.execute(f"PRAGMA table_info({t[0]})").fetchall())
    print(db.execute(f"SELECT * FROM {t[0]}").fetchall())
