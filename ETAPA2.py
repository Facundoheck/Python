#ETAPA 2
import csv 

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

    entrada = input('\nSeleccione: \n1 --> meses de inicio \n2 --> provincia de origen \n3 --> provincia destino \n4 --> viaje \n5 --> viajeros \n6 --> edicion \n* para salir\nIngrese opcion (si es mas de una, entre comas): ')
    entrada = entrada.split(',')   

    for i in lectura_previaje:

        mes_inicio.append(i[0])
        provincia_origen.append(i[1])
        provincia_destino.append(i[2])
        viaje.append(i[3])
        viajeros.append(i[4])
        edicion.append(i[5])


    dic = {
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

datos_relevantes()