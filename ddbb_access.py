import sqlite3
con = sqlite3.connect('Datos/mhw.db')

cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
list = [x for x in cursor.fetchall()]
for x in list:
    print(x)