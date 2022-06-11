class Monstruo:
  def __init__(self,monster):
    self.nombre = monster[1]
    self.ecology = monster[2]
    self.size = monster[3]
    self.traps = monster[4]

  def __str__(self):
    return f'Monster{self.nombre,self.ecology,self.size,self.traps}'


class Debilidad:
  def __init__(self,monster):
    self.form = monster[2]
    self.alt_description = monster[3]
    self.fire = monster[4]
    self.water = monster[5]
    self.thunder = monster[6]
    self.ice = monster[7]
    self.dragon = monster[8]
    self.poison = monster[9]
    self.sleep = monster[10]
    self.paralysis = monster[11]
    self.blast = monster[12]
    self.stun = monster[13]

  def __str__(self):
    return f'''Debilidades{self.form,self.alt_description,
                        self.fire,self.water,self.thunder,self.ice,self.dragon,
                        self.poison,self.sleep,self.paralysis,self.blast,self.stun,}'''


class Objeto:
  nombre = ''
  desc = ''