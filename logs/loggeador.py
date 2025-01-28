import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def loggear(texto):
  print(texto)
  with open(os.path.join(ROOT_DIR,'monscomp.log'), 'a') as f:
    f.write(texto)
    f.write('\n')

def loggear_DB(texto):
  print(texto)
  with open(os.path.join(ROOT_DIR,'DB.log'), 'a') as f:
    f.write(texto)
    f.write('\n')
