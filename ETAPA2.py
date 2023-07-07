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
    
    #una vez que terminamos de usar el archivo previaje.csv, lo cerramos con el siguiente comando      
    archivo_previaje.close()

#llamada a la funcion
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
    #se le solicita al usuario que ingrese un mes y un año y guardamos en dos variables distintas
    mes = input('ingrese mes: ')
    año_c = input('ingrese año: ')
    #guardamos en una variable el dato ubicado en la tercera posicion del input del usuario 202X
    año = año_c[3]

    #fecha = []
    #fecha = str(año_c+'-'+mes)
    #print(fecha)

    #iteramos sobre el archivo que contiene los datos del csv
    for i in lectura_previaje:
        #creamos listas nuevas para guardar las columnas de "mes de inicio", "provincia destino" y "viajeros"
        str(mes_inicio.append(i[0]))
        provincia_destino.append(i[2])
        viajeros.append(i[4])
    
    #inicializamos variables de tipo lista 
    regj = []
    regk = []
    regl = []
    reglint = []

    #iteramos con 3 variables dentro de las listas que contienen los datos antes mencionados, utilizamos el zip() para combinar las listas
    for j,k,l in zip(mes_inicio, provincia_destino, viajeros):
            #guardamos en tres nuevas listas los mismos datos de listas que comparten  "mes inicio"  
            if j[3] == año and j[5:] == mes: 
                regj.append(j)
                regk.append(k)
                regl.append(l)
    #guardamos en una nueva lista pasando a enteros los datos de la lista "viajeros"
    reglint = list(map(int, regl))
    #guardamos en una variable el maximo de esta lista para comparar con las listas combinadas asi podemos tener el indice de este mismo dato que comparte con mes_inicio y provincia destino
    maximo = max(reglint)
    #iteramos nuevamente sobre las tres listas
    for j,k,l in zip(regj, regk, reglint):
        #comparamos la lista que contiene la cantidad de viajeros con el maximo extraído anteriormente
        if l == maximo:
            print('La provincia que mas viajeros recibió en el año',año_c,'y en el mes',mes,'es',k,'con una cantidad de',l,'viajeros')
    #una vez que terminamos de usar el archivo previaje.csv, lo cerramos con el siguiente comando
    archivo_previaje.close()
#llamada a la funcion
masViajeros()