def loggear(texto):
  print(texto)
  with open('monscomp.log', 'a') as f:
    f.write(texto)
    f.write('\n')

def loggear_DB(texto):
  print(texto)
  with open('DB.log', 'a') as f:
    f.write(texto)
    f.write('\n')
