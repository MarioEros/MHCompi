#Clase empleada para búsquedas relacionadas con monstruos
from DDBB import refMonster as rf
import pandas as pd
from DDBB.clases import Monstruo,Debilidad
import math

def buscarMonstruo(lista):
  if len(lista) < 1:
    return None
  else:
    return detallesMonstruo(buscarNombreMonstruo(lista))


def buscarNombreMonstruo(args):
  opciones = rf.nombresMonstruo.copy().keys()
  for busqueda in args:
    opciones = [x for x in opciones if x.lower().__contains__(busqueda.lower())]
  if len(opciones) == 1:
    return rf.nombresMonstruo[opciones[0]]
  elif len(opciones) == 0:
    return None
  else:
    return rf.nombresMonstruo[min(opciones, key=len)]


#UPDATEAR CON ESTRUCTURA BBDD
def detallesMonstruo(codigo):
  if codigo is None:
    return None
  else:
    mons = Monstruo()
    datos = pd.read_csv("Datos/Monster_descripciones.csv", sep =";")
    fila = datos[datos["nombre"] == codigo]
    mons.nombre = fila.iloc[0]["nombre"]
    mons.desc = fila.iloc[0]["descripcion"]
    mons.url = fila.iloc[0]["url"]
    datos = pd.read_csv("Datos/Monster_debilidades.csv", sep =";")
    datos = datos[datos["nombre"] == codigo]
    debilEle = []
    for x in datos.itertuples():
        debilEle.append(Debilidad(x[2],x[3],
                                  debilidades([x[4],x[5],x[6],x[7],x[8]]),
                                  estados([x[9],x[10],x[11],x[12],x[13]])))
    mons.debil=debilEle
    mons.estado=debilEle[0].estado
    return mons

codeBlock = '```'

def debilidades(datos):
    fuego = 'FUE🔥: '+estrellas(datos[0])
    agua = '\nAGU💧: '+estrellas(datos[1])
    rayo = '\nELE🌩️: '+estrellas(datos[2])
    hielo = '\nHIE🧊: '+estrellas(datos[3])
    draco = '\nDRA🐉: '+estrellas(datos[4])
    return codeBlock+fuego+agua+rayo+hielo+draco+codeBlock

def estados(datos):
    if math.isnan(datos[0]):
        return None
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