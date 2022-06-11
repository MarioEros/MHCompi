from DDBB.MHObjects import Monstruo
import DDBB.MonsterRepo as monRep
import unidecode
import discord

def get_monster_info(lista, lang: str) -> Monstruo:
    """
    Recupera el mensaje embebido para devolver
    :param lista: una lista de partes del nombre de un monstruo
    :param lang: el lenguaje del usuario
    :return: un cuadro con el mensaje embebido
    """
    if len(lista) < 1:
        return None #TODO devolver error embebido
    else:
        monstruo = _get_monster_by_name(lista, lang)
        if monstruo is None:
            return None #TODO devolver error embebido
        monstruo = monRep.add_monster_info(monstruo)
        monstruo = monRep.add_weakness(monstruo)
        return monstruo #TODO devolver monstruo formado embebido

def _get_monster_by_name(lista, lang: str):
    """
    El monstruo busca un monstruo
    :param lang: el lenguaje del usuario
    :param lista: una lista de partes del nombre de un monstruo
    :return: Un Monstruo con nombre y descripcion solo
    """
    search = unidecode.unidecode("%"+"%".join(lista)+"%")
    devolver = monRep.get_monster_name_by_lang(search,lang)
    return devolver

def get_embbed_monster(lista, lang: str):
    monstruo = get_monster_info(lista,lang)
    cuadro=discord.Embed(title = monstruo.nombre, description = monstruo.descripcion)
    for debilidad in monstruo.debilidades:
        cuadro.add_field(name="Normal" if debilidad.form=="normal" else debilidad.alt_description, value=debilidad.elemento, inline=True)
        cuadro.add_field(name='Estados', value=mons.estado, inline=False)
'''
    self.form = debilidad[2]
    self.alt_description = debilidad[3]
    self.fire = debilidad[4]
    self.water = debilidad[5]
    self.thunder = debilidad[6]
    self.ice = debilidad[7]
    self.dragon = debilidad[8]
    self.poison = debilidad[9]
    self.sleep = debilidad[10]
    self.paralysis = debilidad[11]
    self.blast = debilidad[12]
    self.stun = debilidad[13]
'''
def _format_debilidades_elem():
    return None

def _format_debilidades_stat():
    return None

codeBlock = '```'

def debilidades(datos):
    fuego = 'FUE🔥: '+estrellas(datos[0])
    agua = '\nAGU💧: '+estrellas(datos[1])
    rayo = '\nELE🌩️: '+estrellas(datos[2])
    hielo = '\nHIE🧊: '+estrellas(datos[3])
    draco = '\nDRA🐉: '+estrellas(datos[4])
    return codeBlock+fuego+agua+rayo+hielo+draco+codeBlock

def estados(datos):
    veneno = 'Veneno:\t'+estrellas(datos[0])
    sueno = '\nSueño:\t '+estrellas(datos[1])
    paralisis = '\nParalisis: '+estrellas(datos[2])
    nitro = '\nNitro:\t '+estrellas(datos[3])
    stun = '\nStun:\t  '+estrellas(datos[4])
    return codeBlock+veneno+sueno+paralisis+nitro+stun+codeBlock

def estrellas(num):
    num = int(num)
    if num == 0:
        return "❌"
    else:
        return num*'⭐'