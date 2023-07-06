#ETAPA 1
import csv 

# Abrir un archivo en modo lectura
provincias = open('coordenadas_provincias.csv', 'r')
listdatosrelevantes = []


def listtodict():
    # Leer el contenido del archivo
    lectura = csv.reader(provincias)
    dic = {}
    for i in lectura:
        j = i[0]
        k = i[1:]
        dic[j] = k
    print(dic)

listtodict()

'''
class Provincia:

    def __init__(self, nombre, latitud, longitud):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud

    def __str__(self):
        return f"Nombre: {self.nombre}, latitud: {self.latitud}, longitud: {self.longitud}"
'''
#Santafe = Provincia("Santa fe", 30.9452 , 61.5607)
#print(Santafe)