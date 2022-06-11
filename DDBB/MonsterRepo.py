import sqlite3

import clases
from DDBB.mensajes import get_message


con = sqlite3.connect('../Datos/mhw.db')

cursor = con.cursor()

'''
db_table_content('monster_base') #['MHCOMPI_ID', 'name_en', 'ecology_en', 'size', 'traps']
db_table_content('monster_weaknesses') #['MHCOMPI_ID', 'name_en', 'form', 'alt_description',
                                          'fire', 'water', 'thunder', 'ice', 'dragon',
                                          'poison', 'sleep', 'paralysis', 'blast', 'stun']
db_table_content('monster_habitats') #['MHCOMPI_ID', 'name_en', 'map_en', 'start_area']
'''
def get_monster_by_lang(mons:str, lang:str):
    cursor.execute('''
    SELECT * FROM
    monster_weaknesses b
    WHERE b.name_en = ? COLLATE NOCASE''',(mons,))
    print([x[0] for x in cursor.description])
    mons = [x for x in cursor]
    if len(mons) == 0:
        print(get_message('no_encontrado',lang))
    elif len(mons) == 1:
        print(mons[0])
        monstruo = clases.Monstruo(mons[0])
        print(monstruo)
    else:
        print(get_message('varios_encontrados',lang))
        [print(x) for x in mons]



def db_table_content(table: str):
    rows = cursor.execute("SELECT * FROM {};".format(table))
    print([x[0] for x in cursor.description])
    for row in cursor:
        print(row)


def db_table_content_where(table: str, mons: str):
    rows = cursor.execute("SELECT * FROM {0} where name_en LIKE '%{1}%' COLLATE NOCASE;".format(table,mons))
    print([x[0] for x in cursor.description])
    for row in cursor:
        print(row)


def get_hey():
    rows = cursor.execute("SELECT * FROM monster_text WHERE alt_state_description IS NOT NULL ;")
    print([x[0] for x in cursor.description])
    for row in cursor:
        print(row)

# db_table_content('monster')
# db_table_content('monster_text')
# db_table_content_where('monster_habitats','pukei')
get_monster_by_lang("Pukei-Pukei","es")
# get_hey()
# db_table_content('monster_hitzone')
# db_table_content('monster_hitzone_text')
# db_table_content('monster_break')
# db_table_content('monster_break_text')

# db_table_content('monster_habitat')
# db_table_content('monster_reward')
# db_table_content('monster_reward_condition_text')