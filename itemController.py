#Clase empleada para búsquedas relacionadas con objetos
from DDBB import refItems as rf
import pandas as pd
from DDBB.clases import Objeto

def buscarItem(lista):
  if len(lista) < 1:
    return None
  else:
    return detallesObjeto(buscarNombreObjeto(lista))

def buscarNombreObjeto(args):
  opciones = rf.nombresObjetos.copy()
  for busqueda in args:
    opciones = [x for x in opciones if x.lower().__contains__(busqueda.lower())]
  if len(opciones) == 1:
    return opciones[0]
  elif len(opciones) == 0:
    return None
  else:
    return min(opciones, key=len)

def detallesObjeto(codigo):
  if codigo is None:
    return None
  else:
    item = Objeto()
    datos = pd.read_csv("Datos/Item_descripcion.csv", sep =";")
    fila = datos[datos["nombre"] == codigo]
    item.nombre = fila.iloc[0]["nombre"]
    item.desc = fila.iloc[0]["descripcion"]
    return item