import sqlite3
from DDBB.mensajes import get_message


con = sqlite3.connect('../Datos/mhw.db')

cursor = con.cursor()

def db_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    lista = [x for x in cursor.fetchall()]
    for x in lista:
        print(x)
'''
('item',)('language',)('monster',)('skilltree',)('weapon_ammo',)('weapon_melody',)('tool',)('item_text',)
('item_combination',)('location_text',)('monster_text',)('monster_hitzone',)('monster_break',)('monster_reward_condition_text',)
('skilltree_text',)('skill',)('armorset',)('armorset_bonus_text',)('armorset_bonus_skill',)('weapon_melody_notes',)
('weapon_melody_text',)('decoration',)('recipe_item',)('tool_text',)('location_item',)('location_camp_text',)
('monster_habitat',)('monster_hitzone_text',)('monster_break_text',)('monster_reward',)('armorset_text',)('armor',)
('weapon',)('decoration_text',)('charm',)('kinsect',)('quest',)('armor_text',)('armor_skill',)('weapon_text',)
('weapon_skill',)('charm_skill',)('charm_text',)('kinsect_text',)('quest_text',)('quest_monster',)('quest_reward',)
'''

def db_table_content(table: str):
    rows = cursor.execute("SELECT * FROM {};".format(table))
    print([x[0] for x in cursor.description])
    for row in cursor:
        print(row)

# en,ja,fr,es
def db_item_by_lang(item:str, lang:str):
    rows = cursor.execute("SELECT * FROM item_text WHERE name Like ? AND lang_id = ?",('%'+item+'%',lang))
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


# db_table_content('monster')
# db_table_content('monster_text')
# db_table_content('monster_hitzone')
# db_table_content('monster_break')
# db_table_content('monster_reward_condition_text')
# db_table_content('monster_hitzone_text')
# db_table_content('monster_break_text')
# db_table_content('monster_reward')
# db_table_content('quest_monster')
# db_table_content('monster_habitat')
# db_item_by_lang('ay','es')
# db_monster_by_lang('awd','es')