import sqlite3
import os

from DDBB.MHObjects import Monstruo,Debilidad


from logs.loggeador import loggear_DB


con = sqlite3.connect(os.path.join('Datos','mhw.db'))

cursor = con.cursor()

'''
db_table_content('monster_base') #['MHCOMPI_ID', 'name_en', 'ecology_en', 'size', 'traps']
db_table_content('monster_weaknesses') #['MHCOMPI_ID', 'name_en', 'form', 'alt_description',
                                          'fire', 'water', 'thunder', 'ice', 'dragon',
                                          'poison', 'sleep', 'paralysis', 'blast', 'stun']
db_table_content('monster_habitats') #['MHCOMPI_ID', 'name_en', 'map_en', 'start_area']
['MHCOMPI_ID',
 'name_en', 'description_en', 'name_ja', 'description_ja', 'name_fr', 'description_fr', 'name_it', 'description_it',
 'name_de', 'description_de', 'name_es', 'description_es', 'name_pt', 'description_pt', 'name_pl', 'description_pl', 
 'name_ru', 'description_ru', 'name_ko', 'description_ko', 'name_zh', 'description_zh', 'name_ar', 'description_ar']
'''

def get_monster_name_by_lang(mons: str,lang: str) -> Monstruo:
    loggear_DB("Buscando monstruo: {} lang: {}".format(mons,lang))
    query = "SELECT MHCOMPI_ID, name_en, name_{0}, description_{0} FROM " \
            "monster_base_translations WHERE name_en LIKE '{1}' COLLATE NOCASE".format(lang,mons)
    cursor.execute(query)
    mons = [x for x in cursor]
    if len(mons) == 0:
        loggear_DB("Monstruo no encontrado.")
        return None
    elif len(mons) == 1:
        monstruo = Monstruo(mons[0])
        loggear_DB(monstruo.nombre+" encontrado.")
        return monstruo
    else:
        loggear_DB("Multiples monstruos encontrados:")
        monstruos = [Monstruo(x) for x in mons]
        for x in monstruos:
            loggear_DB(" - "+x.nombre)
        return monstruos[0]


def add_monster_info(monstruo:Monstruo) -> Monstruo:
    loggear_DB("Buscando info...")
    cursor.execute('''
    SELECT * FROM
    monster_base
    WHERE name_en = ?''',(monstruo.nombre_en,))
    found = [x for x in cursor]
    if len(found) == 0:
        loggear_DB("info no encontrada")
        return monstruo
    else:
        monstruo.add_info(found[0])
        loggear_DB("info encontrada")
        return monstruo

def add_weakness(mons:Monstruo) -> Debilidad:
    loggear_DB("Buscando debilidades...")
    cursor.execute('''
    SELECT * FROM
    monster_weaknesses
    WHERE name_en = ?''',(mons.nombre_en,))
    debil = [x for x in cursor]
    if len(debil) == 0:
        loggear_DB(mons.nombre+" monstruo pequeño?")
        return mons
    elif len(debil) == 1:
        debilidad = Debilidad(debil[0])
        loggear_DB(mons.nombre+ ", debilidad encontrada.")
        mons.debilidades = (debilidad,)
        return mons
    else:
        debilidades = [Debilidad(x) for x in debil]
        loggear_DB(mons.nombre+",multiples debilidades encontradas.")
        mons.debilidades = debilidades
        return mons


def db_table_content(table: str):
    rows = cursor.execute("SELECT * FROM {};".format(table))
    print([x[0] for x in cursor.description])
    for row in cursor:
        print(row)


# db_table_content('monster_base')
# db_table_content('monster_weaknesses')
# db_table_content_where('monster_habitats','pukei')
# mons = get_monster_name_by_lang("%Alatr%","es")
# print(mons)
# debil = get_weakness(mons.nombre)
# for x in debil:
#     print(x)
# get_hey()
# db_table_content('monster_hitzone')
# db_table_content('monster_hitzone_text')
# db_table_content('monster_break')
# db_table_content('monster_break_text')

# db_table_content('monster_habitat')
# db_table_content('monster_reward')
# db_table_content('monster_reward_condition_text')