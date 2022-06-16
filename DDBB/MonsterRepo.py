import sqlite3

from DDBB.MHObjects import Monstruo,Debilidad
from logs.loggeador import loggear_DB


con = sqlite3.connect('Datos/mhw.db')

cursor = con.cursor()


def get_monster_name_by_lang(n_monstruo: str,lang: str) -> Monstruo:
    loggear_DB("Buscando monstruo: {} lang: {}".format(n_monstruo,lang))
    query = "SELECT MHCOMPI_ID, name_en, name_{0}, description_{0} FROM " \
            "monster_base_translations WHERE name_en LIKE '{1}' COLLATE NOCASE".format(lang,n_monstruo)
    cursor.execute(query)
    found = [x for x in cursor]
    if len(found) == 0:
        loggear_DB("Monstruo no encontrado.")
        return None
    elif len(found) == 1:
        monstruo = Monstruo(found[0])
        loggear_DB(monstruo.nombre+" encontrado.")
        return monstruo
    else:
        loggear_DB("Multiples monstruos encontrados:")
        monstruos = [Monstruo(x) for x in found]
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
    found = [x for x in cursor]
    if len(found) == 0:
        loggear_DB(mons.nombre+" monstruo pequeño?")
        return mons
    elif len(found) == 1:
        debilidad = Debilidad(found[0])
        loggear_DB(mons.nombre+ ", debilidad encontrada.")
        mons.debilidades = (debilidad,)
        return mons
    else:
        debilidades = [Debilidad(x) for x in found]
        loggear_DB(mons.nombre+",multiples debilidades encontradas.")
        mons.debilidades = debilidades
        return mons