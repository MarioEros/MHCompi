import sqlite3
from DDBB.mensajes import get_message


con = sqlite3.connect('../Datos/mhw.db')

cursor = con.cursor()

'''
('monster',)('monster_text',)
('monster_hitzone',)('monster_hitzone_text',)('monster_break',)('monster_break_text',)
('monster_habitat',)('monster_reward',)('monster_reward_condition_text',)
'''
def get_monster_by_lang(mons:str, lang:str):
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



def db_table_content(table: str):
    rows = cursor.execute("SELECT * FROM {};".format(table))
    print([x[0] for x in cursor.description])
    for row in cursor:
        print(row)

def get_hey():
    rows = cursor.execute("SELECT * FROM monster_text WHERE alt_state_description IS NOT NULL ;")
    print([x[0] for x in cursor.description])
    for row in cursor:
        print(row)

db_table_content('monster')
# db_table_content('monster_text')
# get_monster_by_lang("Alatre","es")
# get_hey()
# db_table_content('monster_hitzone')
# db_table_content('monster_hitzone_text')
# db_table_content('monster_break')
# db_table_content('monster_break_text')

# db_table_content('monster_habitat')
# db_table_content('monster_reward')
# db_table_content('monster_reward_condition_text')