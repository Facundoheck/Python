#ETAPA 2
import csv 

#--------------------------Funcion datos relevantes------------------------------------------------
'''
#abre el archivo "previaje.csv" en modo de lectura y asigna el objeto de archivo resultante a la variable
archivo_previaje = open('previaje.csv', 'r')

#inicializacion de las variables tipo lista y diccionario
dic = {}
mes_inicio = []
provincia_origen = []
provincia_destino = []
viaje = []
viajeros = []
edicion = []

#inicializacion de la funcion 
def datos_relevantes():
    #permite leer y procesar el contenido del archivo CSV
    lectura_previaje = csv.reader(archivo_previaje)

    #input del usuario
    entrada = input('\nSeleccione: \n1 --> meses de inicio \n2 --> provincia de origen \n3 --> provincia destino \n4 --> viaje \n5 --> viajeros \n6 --> edicion \n* para salir\nIngrese opcion (si es mas de una, entre comas): ')
    #separacion por coma para diferenciar las entradas del usuario
    entrada = entrada.split(',')   

    #inicio de iteracion dentro de la variable que guarda el csv
    for i in lectura_previaje:
        #agregar los elementos a nuevas variables de tipo lista
        mes_inicio.append(i[0])
        provincia_origen.append(i[1])
        provincia_destino.append(i[2])
        viaje.append(i[3])
        viajeros.append(i[4])
        edicion.append(i[5])

    #carga de datos al diccionario con las opciones de menú como clave y las listas como valores correspondientes a cada clave
    dic = {
        '1' : mes_inicio,
        '2' : provincia_origen,
        '3' : provincia_destino,
        '4' : viaje,
        '5' : viajeros,
        '6' : edicion
        }

    #iteracion dentro del input del usuario para poder trabajar de una
    for j in entrada:
        #en cada iteracion verifica que el input del usuario se encuentre en el diccionario
        if j.strip() in dic:
            #si el input del usuario esta dentro de las claves del diccionario, guarda el contenido de la lista seleccionada en una nueva variable
            datos = dic[j.strip()]
            #imprime el contenido de la lista
            print(datos)
        else:
            print('No existe la lista de datos')
            
    archivo_previaje.close()

#datos_relevantes()
'''
#-----------------Funcion masViajeros---------------------------

#abre el archivo "previaje.csv" en modo de lectura y asigna el objeto de archivo resultante a la variable
archivo_previaje = open('previaje.csv', 'r')

#inicializacion de las variables tipo lista
#dic = {}
mes_inicio = []
#provincia_origen = []
provincia_destino = []
#viaje = []
viajeros = []
#edicion = []

#inicializacion de la funcion 
def masViajeros():

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
    
    regj = []
    regk = []
    regl = []
    reglint = []

    for j,k,l in zip(mes_inicio, provincia_destino, viajeros):
            if j[3] == año and j[5:] == mes:
                regj.append(j)
                regk.append(k)
                regl.append(l)

    reglint = list(map(int, regl))
    maximo = max(reglint)
    
    for j,k,l in zip(regj, regk, reglint):
        if l == maximo:
            print('La provincia que mas viajeros recibió en el año',año_c,'y en el mes',mes,'es',k,'con una cantidad de',l,'viajeros')
    
    archivo_previaje.close()

masViajeros()