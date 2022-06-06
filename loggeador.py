def loggear(texto):
  print(texto)
  with open('log.monscomp', 'a') as f:
    f.write(texto)
    f.write('\n')
