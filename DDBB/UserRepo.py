import sqlite3

import Datos.db_queries
from DDBB.MHObjects import MHUser
from logs.loggeador import loggear_DB

con = sqlite3.connect('Datos/mhw.db')

cursor = con.cursor()


def get_user_info(user: MHUser):
    cursor.execute("SELECT * FROM users WHERE user_id = ?",(user.user_id,))
    db_user = [x for x in cursor]
    if len(db_user) == 0:
        _db_create_user(user)
        return get_user_info(user)
    elif len(db_user) == 1:
        return MHUser(db_user[0])


def _db_create_user(user: MHUser):
    cursor.execute("INSERT INTO users (user_id, name, lang) VALUES (?,?,'es')", (user.user_id, user.name,))
    con.commit()
    loggear_DB("Usuario {} creado".format(user.name))

def get_lang_info(lang: str):
    cursor.execute("SELECT * from language WHERE id='{0}' OR description LIKE '%{0}%' COLLATE NOCASE".format(lang))
    lang = [x[1] for x in cursor]
    if len(lang) == 0:
        return None
    else:
        return lang[0]

def update_lang(user: MHUser, lang:str):
    cursor.execute("UPDATE users SET lang = ? WHERE user_id = ?",(lang,user.user_id))
    con.commit()
    loggear_DB("Usuario {0} actualizado lenguaje a {1}".format(user.name, lang))

def set_up_user_table():
    cursor.execute(Datos.db_queries.sql_create_users_table)