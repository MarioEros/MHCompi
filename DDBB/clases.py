class Monstruo:
  nombre = ''
  desc = ''
  url = ''
  debil = []
  estado=''
  rompible = ''

class Debilidad:
  forma = ''
  descripcion = ''
  elemento=''
  estado=''
  def __init__(self,forma,descripcion,elemento,estado):
    self.forma=forma
    self.descripcion=descripcion
    self.elemento=elemento
    self.estado=estado

class Objeto:
  nombre = ''
  desc = ''