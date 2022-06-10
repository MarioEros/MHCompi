import sqlite3

from DDBB.MHObjects import MHUser
from logs import loggeador

con = sqlite3.connect('Datos/mhw.db')

cursor = con.cursor()



def get_user_info(user: MHUser):
    cursor.execute("SELECT * FROM users WHERE user_id = ?",(user.user_id,))
    db_user = [x for x in cursor]
    if len(db_user) == 0:
        _db_create_user(user)
        get_user_info(user)
    elif len(db_user) == 1:
        print(db_user[0])
        return db_user[0]

def _db_create_user(user: MHUser):
    cursor.execute("INSERT INTO users (user_id, name) VALUES (?,?)", (user.user_id, user.name,))
    loggeador.loggear_DB("Usuario {} creado".format(user.name))
    con.commit()

def update_lang(user: MHUser, lang:str):
    cursor.execute("UPDATE users SET lang = ? WHERE user_id = ?",(user.user_id,lang))
    loggeador.loggear_DB("Usuario {0} actualizado lenguaje a {1}".format(user.name, lang))
    con.commit()