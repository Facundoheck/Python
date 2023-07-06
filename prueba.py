#ETAPA 1
import csv 
'''
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

#ETAPA 2
archivo_previaje = open('previaje.csv', 'r')
dic = {}
mes_inicio = []
provincia_origen = []
provincia_destino = []
viaje = []
viajeros = []
edicion = []

def datos_relevantes():
    lectura_previaje = csv.reader(archivo_previaje)

    mes = input('ingrese mes: ')
    año_c = input('ingrese año: ')
    año = año_c[3]

    #fecha = []
    #fecha = str(año_c+'-'+mes)
    #print(fecha)

    for i in lectura_previaje:

        str(mes_inicio.append(i[0]))
        provincia_destino.append(i[2])
        viajeros.append(i[4])
    
    #print(fecha)

    #lista = [mes_inicio, provincia_origen, viajeros]
    #datos = []
    regj = []
    regk = []
    regl = []
    dic = {}

    for j,k,l in zip(mes_inicio, provincia_destino, viajeros):
            if j[3] == año and j[5:] == mes:
                regj.append(j)
                regk.append(k)
                regl.append(l)
                #for(m,n,o) in zip(j,k,l):
            
    reglint = list(map(int, l))
    for j,k,l in zip(regj, regk, regl):
        maximo = max(list(map(int, l)))
        print(j,k,l)


"""         maximo = max(list(map(int, l)))
        indice_max_viajeros = l.index(maximo(l))
        prov_max_viajeros = k[indice_max_viajeros]
        mesyaño = j[indice_max_viajeros]

    print('La provincia que mas viajeros recibió es ', prov_max_viajeros,' en ', mesyaño,' con una cantidad de ', maximo)
 """




"""     
lista = [mes_inicio, provincia_origen, viajeros]
    
    for j in lista:
        if fecha == j:
            print(j)

"""
"""if fecha in mes_inicio:
            print(lista[j])
        else:
            print('no son iguales')
"""

"""     dic = {
        '1' : mes_inicio,
        '2' : provincia_origen,
        '3' : provincia_destino,
        '4' : viaje,
        '5' : viajeros,
        '6' : edicion
        }

    for j in entrada:
        if j.strip() in dic:
            datos = dic[j.strip()]
            print(datos)
        else:
            print('No existe la lista de datos')
"""
datos_relevantes()

#def masViajeros():


#masViajeros()

"""
class viaje:
    def __init__(self, mes_inicio, provincia_origen, provincia_destino, viajes, viajeros, edicion):
        self.mes_inicio = mes_inicio
        self.provincia_origen = provincia_origen
        self.provincia_destino = provincia_destino
        self.viaje = viajes
        self.viajeros = viajeros
        self.edicion = edicion

    def __str__(self):
        return f"Mes de inicio: {self.mes_inicio}, provincia de origen: {self.provincia_destino}, provincia destino: {self.provincia_origen}, viajes: {self.viaje}, viajeros: {self.viajeros}, edicion: {self.edicion}"

#nuevo_viaje = viaje('2021-01', 'Santa fe', 'Santa cruz' , 6920, 22436, 'previaje 1')

#print(nuevo_viaje)

"""