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

#etapa 2: carga de datos para el archivo previaje.csv
#constructor de la clase viaje
class Viaje:
  def __init__(self,mes_inicio,provincia_origen,provincia_destino,viajes,viajeros,edicion):
    self.mes_inicio = mes_inicio
    self.provincia_origen = provincia_origen
    self.provincia_destino = provincia_destino
    self.viajes = viajes
    self.viajeros = viajeros
    self.edicion = edicion

  def __str__(self):
    return str({"Mes de inicio":self.mes_inicio, "provincia de origen":self.provincia_origen,"provincia destino":self.provincia_destino,"viajes":self.viajes,"viajeros":self.viajeros,"edicion":self.edicion})
  
#estructura de datos para los objetos de la clase Viaje
openFile('previaje.csv')
#listToDict(lista)
listado_viajes=[]
for i in lista:
  viajes = Viaje(i[0],i[1],i[2],i[3],i[4],i[5])
  listado_viajes.append(viajes)
#for j in listado_viajes:
#print(j)

#etapa 3: analisis y grafico

#ingreso de datos del usuario
prov1 = input(str("Ingrese el nombre de la primera provincia: "))
prov2 = input(str("Ingrese el nombre de la segunda provincia: "))
#inicializacion de listas
viaje_ida=[]
viaje_vuelta=[]
edicion_ida=[]
edicion_vuelta=[]
viaje_edicion1=[]
viaje_edicion2=[]
viaje_edicion3=[]
#iteracion en la estructura de datos del archivo previaje.csv
#guardo los viajes de ida y los viajes de vuelta junto con su edicion
for i in listado_viajes:
  if (prov1 == i.provincia_origen) and (prov2 == i.provincia_destino):
    viaje_ida.append(i.viajes)
    edicion_ida.append(i.edicion)
  elif (prov2 == i.provincia_origen) and (prov1 == i.provincia_destino):
    viaje_vuelta.append(i.viajes)
    edicion_vuelta.append(i.edicion)
#itero entre ambas listas de los viajes de ida para distinguir las ediciones de previaje
for i,j in zip(viaje_ida, edicion_ida):
  if j == "previaje 1":
    viaje_edicion1.append(i)
  elif j == "previaje 2":
    viaje_edicion2.append(i)
  elif j == "previaje 3":
    viaje_edicion3.append(i)
#itero entre ambas listas de los viajes de vuelta para distinguir las ediciones de previaje
for i,j in zip(viaje_vuelta,edicion_vuelta):
  if j == "previaje 1":
    viaje_edicion1.append(i)
  elif j == "previaje 2":
    viaje_edicion2.append(i)
  elif j == "previaje 3":
    viaje_edicion3.append(i)
#guardo en cada variable la suma total de viajes, tanto de ida como de vuelta de cada edicion
#convierto los datos de texto a entero para poder sumarlos
edicion1 = sum(list(map(int,viaje_edicion1)))
edicion2 = sum(list(map(int,viaje_edicion2)))
edicion3 = sum(list(map(int,viaje_edicion3)))
#muestra en pantalla la suma total de viajes para cada edicion
print("Total de viajes para la edicion 1: ",edicion1)
print("Total de viajes para la edicion 2: ",edicion2)
print("Total de viajes para la edicion 3: ",edicion3)

#grafico del punto anterior
import matplotlib.pyplot as plt

clave = ["Previaje 1", "Previaje 2", "Previaje 3"]
valores = [edicion1, edicion2, edicion3]

plt.figure(figsize = (20,6))
plt.title('Cantidad total de viajes para cada edicion de previaje',fontsize=25) #titulo del gráfico y tamaño de la fuente
plt.bar(clave, valores)