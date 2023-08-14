import json

#inicializar diccionario
diccionario={}

#constructor de la clase gestor
class Gestor:
    def __init__(self,id,usr,psw,desc):
        self.id=id
        self.usr=usr
        self.psw=psw
        self.desc=desc

    def to_json(self):
        return {
            "id": self.id,
            "usr": self.usr,
            "psw": self.psw,
            "desc": self.desc
        }

    @classmethod
    def from_json(cls, json_data):
        return cls(json_data["id"], json_data["usr"], json_data["psw"], json_data["desc"])

#cargar datos desde json
loaddatos=from_json()

#defino nuevas funciones para el gestor
def nuevoRegistro(diccionario):
    id=input('Id: ')
    desc=input('Descripcion: ')
    usr=input('Usuario: ')
    psw=input('Constraseña: ')
    gestor=Gestor(id,usr,psw,desc)
    diccionario[id]=gestor
    print('*'*30)
    print('Nuevo usuario añadido con éxito')
    print('*'*30)

def actualizarContraseña(diccionario):
    id=input('Id: ')
    psw=input('Contraseña: ')
    reg=diccionario.get(id)
    if reg:
        reg.psw=psw
        print('*'*30)
        print('Clave actualizada con éxito')
        print('*'*30)

def actualizarUsuario(diccionario):
    id=input('Id: ')
    usr=input('Usuario: ')
    reg=diccionario.get(id)
    if reg:
        reg.usr=usr
        print('*'*30)
        print('Usuario actualizado con éxito')
        print('*'*30)

def verId(diccionario):
    id=input('Id: ')
    reg=diccionario.get(id)
    if reg:
        print('*'*30)
        print('Usuario: ',reg.usr)
        print('Clave: ',reg.psw)
        print('Descripcion: ',reg.desc)
        print('*'*30)

def opciones():
    while True:
        opcion=input('a. Agregar un usuario y una clave\nb. Actualizar clave\nc. Actualizar usuario\nd. Ver usuario y clave\ne. Salir\nIngrese opcion: ')
        if opcion=='a':
            nuevoRegistro(diccionario)
        elif opcion=='b':
            actualizarContraseña(diccionario)
        elif opcion=='c':
            actualizarUsuario(diccionario)
        elif opcion=='d':
            verId(diccionario)
        elif opcion=='e':
            break
        else:
            print('Opción incorrecta, intente nuevamente')

#ver la carga de datos desde el archivo json

try:
    with open('pass.json', 'w') as archivo:
        datos_json=[registros.to_json() for registros in diccionario.values()]
        json.dump(datos_json, archivo)

except FileNotFoundError:
    pass

opciones()
