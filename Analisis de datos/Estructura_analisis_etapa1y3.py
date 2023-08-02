import csv

#esta funcion lee datos del archivo de entrada y retorna una lista con la información que se va a usar en el trabajo.
def openFile(archivo):
  global lista
  apertura = open(archivo,'r')
  lectura = csv.reader(apertura)
  lista = []
  for i in lectura:
    lista.append(i)
  return lista

#esta funcion toma el resultado de la lectura de datos como argumento y devuelve una lista de diccionarios.
#La clave es el valor en el índice 0, y los valores asociados son una tupla con el resto de los elementos de la lista.
def listToDict(lectura):
  global dic
  dic = {}
  for i in lectura:
    j = i[0]
    k = tuple(i[1:])
    dic[j] = k
  return dic

#Esta clase representa una provincia.
  #Atributos:
    #nombre: str
    #coordenada: tuple
class Provincia:
  def __init__(self,nombre,coordenadas):
    self.nombre = nombre
    self.coordenadas = coordenadas

  def __str__(self):
    return str({"Provincia":self.nombre, "Coordenadas":self.coordenadas})

#etapa 1: carga de datos para el archivo coordenadas_provincias.csv
openFile('coordenadas_provincias.csv')
listToDict(lista)

listado_provincias = []
#iteracion sobre la lista que contiene los datos del csv
for i in lista:
  #paso cada registro de la lista a objeto de la clase Provincia
  #uso una variable auxiliar "provincias" para guardar el registro por cada vuelta de iteracion
  #los datos de coordenadas los convierto a tipo tupla
  provincias = Provincia(i[0],tuple(i[1:]))
  #creo una lista nueva que almacene todos los objetos de la clase Provincia
  listado_provincias.append(provincias)
  #paso la lista de objetos a la estructura de diccionario
dic_prov = {j.nombre: j.coordenadas for j in listado_provincias}

#Creo un objeto Provincia
nueva_provincia = Provincia('santafe',(-35.56,-68.754))
#agrego el objeto creado al diccionario
dic_prov[nueva_provincia.nombre] = nueva_provincia.coordenadas
#print(dic_prov)

#------------------------------------------------------------------------------------------------------------------

#etapa 3: analisis

import math
#funcion que calcula la distancia entre dos puntos
def calculo_distancia(x1,x2,y1,y2):
  distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
  return distancia
#ingreso de datos del usuario
prov1 = input(str("Ingrese el nombre de la primera provincia: "))
prov2 = input(str("Ingrese el nombre de la segunda provincia: "))
#iteracion sobre la estructura de datos de provincias para encontrar las provincias seleccionadas por el usuario
for i in dic_prov:
  if prov1 == i:
    punto1 = dic[i]
  elif prov2 == i:
    punto2 = dic[i]

#guardo las coordenada de los puntos en nuevas variables, separando ordenadas y abscisas
x1, y1 = map(float, punto1)
x2, y2 = map(float, punto2)

#llamada a la funcion para calcular la distancia
resultado = calculo_distancia(x1,x2,y1,y2)

print("La distancia entre las dos provincias es de:",resultado)