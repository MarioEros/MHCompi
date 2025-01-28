from DDBB.MHObjects import Item
import DDBB.ItemRepo as itemRepo
import unidecode
import discord




def get_item_info(lista, lang: str) -> Item:
    """
    Recupera el item a devolver
    :param lista: una lista de partes del nombre de un objeto
    :param lang: el lenguaje del usuario
    :return: el objeto encontrado
    """
    if len(lista) < 1:
        return None
    else:
        item = _get_item_by_name(lista, lang)
        if item is None:
            return None
        item = itemRepo.add_item_info(item)
        return item


def _get_item_by_name(lista, lang: str):
    """
    Busca un objeto por su nombre
    :param lang: el lenguaje del usuario
    :param lista: una lista de partes del nombre de un objeto
    :return: Un Objeto con nombre, nombre_en y descripcion
    """
    search = unidecode.unidecode("%" + "%".join(lista) + "%")
    devolver = itemRepo.get_item_name_by_lang(search, lang)
    return devolver


def get_embbed_item(item: Item, lang: str):
    cuadro=discord.Embed(title = item.nombre, description = item.descripcion)
    #cuadro.add_field(name=TRANSLATE[lang]['NORM'] if debilidad.form=="normal" else debilidad.alt_description, value=debilidades(debilidad.element, lang), inline=True)
    return cuadro