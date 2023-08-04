#ejercicio 1

def orden(*args):
  lista=[]
  for i in args:
    lista.append(i)
  ordenada = True
  for j in range(1, len(lista)):
    if lista[j] < lista[j-1]:
      ordenada = False
      break
  return ordenada

orden(1,2,4)

#ejercicio 2

def temperatura(c):
  global f
  f = c * (9/5) + 32
  return(f)

temperatura(24)

#ejercicio 3

def temps(*args):
  lista=[]
  for i in args:
    fare = temperatura(i)
    lista.append(fare)
  return lista

temps(24,25,26)
