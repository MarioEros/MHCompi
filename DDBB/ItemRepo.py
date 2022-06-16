import sqlite3

from DDBB.MHObjects import Item

from logs.loggeador import loggear_DB

con = sqlite3.connect('Datos/mhw.db')

cursor = con.cursor()

def get_item_name_by_lang(item: str,lang: str) -> Item:
    loggear_DB("Buscando objeto: {} lang: {}".format(item,lang))
    query = "SELECT MHCOMPI_ID, name_en, name_{0}, description_{0} FROM " \
            "item_base_translations WHERE name_{0} LIKE '{1}' COLLATE NOCASE".format(lang,item)
    cursor.execute(query)
    found = [x for x in cursor]
    if len(found) == 0:
        loggear_DB("Objeto no encontrado.")
        return None
    elif len(found) == 1:
        item = Item(found[0])
        loggear_DB(item.nombre+" encontrado.")
        return item
    else:
        loggear_DB("Multiples objetos encontrados:")
        monstruos = [Item(x) for x in found]
        for x in monstruos:
            loggear_DB(" - "+x.nombre)
        return monstruos[0]


def add_item_info(item: Item) -> Item:
    loggear_DB("Buscando info...")
    cursor.execute('''
    SELECT * FROM
    item_base
    WHERE name_en = ?''',(item.nombre_en,))
    found = [x for x in cursor]
    if len(found) == 0:
        loggear_DB("info no encontrada")
        return item
    else:
        item.add_info(found[0])
        loggear_DB("info encontrada")
        return item