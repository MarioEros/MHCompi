import sqlite3

from Datos import db_queries
from logs import loggeador
from DDBB.mensajes import get_message

con = sqlite3.connect('mhw.db')

cursor = con.cursor()

def db_execute_query(query: str):
    try:
        cursor.execute(query)
        con.commit()
        loggeador.loggear_DB("Ejecutada con exito: " + query)
    except Exception as e:
        loggeador.loggear_DB("Fallo al ejecutar: " + query)
        print(e)

def db_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    lista = [x for x in cursor.fetchall()]
    for x in lista:
        print(x)
'''
'''

def db_table_content(table: str):
    rows = cursor.execute("SELECT * FROM {};".format(table))
    print([x[0] for x in cursor.description])
    for row in cursor:
        print(row)

# en,ja,fr,es
def db_item_by_lang(item:str, lang:str):
    cursor.execute("SELECT * FROM item_text WHERE name Like ? AND lang_id = ?",('%'+item+'%',lang))
    print([x[0] for x in cursor.description])
    items = [x for x in cursor]
    if len(items) == 0:
        print(get_message('no_encontrado', lang))
    elif len(items) == 1:
        print(items[0])
    else:
        print(get_message('varios_encontrados', lang))
        [print(x[2]) for x in items]

def db_monster_by_lang(mons:str, lang:str):
    cursor.execute("SELECT * FROM monster_text WHERE name Like ? AND lang_id = ? COLLATE NOCASE",('%'+mons+'%',lang))
    print([x[0] for x in cursor.description])
    mons = [x for x in cursor]
    if len(mons) == 0:
        print(get_message('no_encontrado',lang))
    elif len(mons) == 1:
        print(mons[0])
    else:
        print(get_message('varios_encontrados',lang))
        [print(x[2]) for x in mons]

def update_monster_translation():
    cursor.execute("UPDATE monster_base_translations WHERE name_en = anteka COLLATE NOCASE")
    con.commit()


# db_tables()

# db_table_content('users')
# db_table_content('monster_ailments')
db_table_content('monster_base_translations')
# db_table_content('monster_breaks')
# db_table_content('monster_hitzones')
# db_table_content('monster_rewards')
# db_table_content('monster_weaknesses')
# db_table_content('monster_habitats')
# db_table_content('monster_base')

# db_table_content('quest_monster')
# db_item_by_lang('ay','es')
# db_monster_by_lang('awd','es')

# db_execute_query(db_queries.sql_drop_users_table)
# db_execute_query(db_queries.sql_create_users_table)
# db_execute_query("UPDATE users SET lang = 'es' WHERE user_id = 156000408412618754")