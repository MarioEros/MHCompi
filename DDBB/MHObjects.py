
class MHUser:

    def __init__(self,user):
        self.user_id=user[0]
        self.name=user[1]
        self.lang=user[2]

    def __str__(self):
        return f'MHUser{self.user_id, self.name, self.lang}'


class Monstruo:
    ecology: str = ''
    size: str = ''
    traps: str = ''

    def __init__(self,monster):
        self.image = monster[0]
        self.nombre_en = monster[1]
        self.nombre = monster[2]
        self.descripcion = monster[3]
        self.debilidades = []

    def add_info(self,rows):
        self.ecology = rows[2]
        self.size = rows[3]
        self.traps = rows[4]

    def __str__(self):
        return f'Monstruo{self.nombre_en,self.nombre,self.descripcion,self.ecology,self.size,self.traps,len(self.debilidades)}'


class Debilidad:

  def __init__(self,debilidad):
    self.form = debilidad[2]
    self.alt_description = debilidad[3]
    self.element = (debilidad[4],debilidad[5],debilidad[6],debilidad[7],debilidad[8])
    self.status = (debilidad[9],debilidad[10],debilidad[11],debilidad[12],debilidad[13])

  def __str__(self):
    return f'Debilidades{self.form,self.alt_description,self.element,self.status,}'

