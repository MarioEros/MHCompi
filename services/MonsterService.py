from DDBB.MHObjects import Monstruo
import DDBB.MonsterRepo as monRep
import unidecode
import discord


TRANSLATE={
    'es':{'NORM':'Normal','EST':'Estados','FUE':'FUEG🔥: ','AGU':'AGUA💧: ','ELE':'ELEC🌩: ','HIE':'HIEL🧊: ','DRA':'DRAG🐉: ',
          'VEN':'VENE🟣: ','SUE':'SUEÑ💤: ','PAR':'PARA🟡: ','NIT':'NITR💥: ','STU':'STUN✨: '},
    'en':{'NORM':'Normal','EST':'Status','FUE':'FIRE🔥: ','AGU':'WATE💧: ','ELE':'ELEC🌩: ','HIE':'ICE 🧊: ','DRA':'DRAG🐉: ',
          'VEN':'VENO🟣: ','SUE':'SLEE💤: ','PAR':'PARA🟡: ','NIT':'NITR💥: ','STU':'STUN✨: '},
}


def get_monster_info(lista, lang: str) -> Monstruo:
    """
    Recupera un monstruo
    :param lista: una lista de partes del nombre de un monstruo
    :param lang: el lenguaje del usuario
    :return: el objeto Monstruo
    """
    if len(lista) < 1:
        return None
    else:
        monstruo = _get_monster_by_name(lista, lang)
        if monstruo is None:
            return None
        monstruo = monRep.add_monster_info(monstruo)
        monstruo = monRep.add_weakness(monstruo)
        return monstruo

def _get_monster_by_name(lista, lang: str):
    """
    Encuentra el nombre de un monstruo por su nombre
    :param lang: el lenguaje del usuario
    :param lista: una lista de partes del nombre de un monstruo
    :return: Un Monstruo con nombre, nombre_en y descripcion
    """
    search = unidecode.unidecode("%"+"%".join(lista)+"%")
    devolver = monRep.get_monster_name_by_lang(search,lang)
    return devolver

def get_embbed_monster(monstruo: Monstruo, lang: str):
    cuadro=discord.Embed(title = monstruo.nombre, description = monstruo.descripcion)
    for debilidad in monstruo.debilidades:
        cuadro.add_field(name=TRANSLATE[lang]['NORM'] if debilidad.form=="normal" else debilidad.alt_description, value=debilidades(debilidad.element, lang), inline=True)
    if len(monstruo.debilidades)>0:
        cuadro.add_field(name=TRANSLATE[lang]['EST'], value=estados(monstruo.debilidades[0].status, lang), inline=False)
    return cuadro

codeBlock = '```'

def debilidades(datos, lang: str):
    fuego = TRANSLATE[lang]['FUE']+estrellas(datos[0])
    agua = '\n'+TRANSLATE[lang]['AGU']+estrellas(datos[1])
    rayo = '\n'+TRANSLATE[lang]['ELE']+estrellas(datos[2])
    hielo = '\n'+TRANSLATE[lang]['HIE']+estrellas(datos[3])
    draco = '\n'+TRANSLATE[lang]['DRA']+estrellas(datos[4])
    return codeBlock+fuego+agua+rayo+hielo+draco+codeBlock

def estados(datos, lang: str):
    veneno = TRANSLATE[lang]['VEN']+estrellas(datos[0])
    sueno = '\n'+TRANSLATE[lang]['SUE']+estrellas(datos[1])
    paralisis = '\n'+TRANSLATE[lang]['PAR']+estrellas(datos[2])
    nitro = '\n'+TRANSLATE[lang]['NIT']+estrellas(datos[3])
    stun = '\n'+TRANSLATE[lang]['STU']+estrellas(datos[4])
    return codeBlock+veneno+sueno+paralisis+nitro+stun+codeBlock

def estrellas(num):
    num = int(num)
    if num == 0:
        return "❌"
    else:
        return num*'⭐'