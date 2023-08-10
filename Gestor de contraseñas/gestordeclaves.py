#inicio listas y diccionario
descripciones=list
usuarios=list
contrasenias=list
diccionario=dict

#constructor de la clase
class Gestor:
    def __init__(self,id,usr,psw,desc):
        self.id=id
        self.usr=usr
        self.psw=psw
        self.desc=desc

#defino nuevas funciones para el gestor
def nuevoRegistro(diccionario):
    id=input('Id: ')
    desc=input('Descripcion: ')
    usr=input('Usuario: ')
    psw=input('Constraseña: ')
    gestor=Gestor(id,usr,psw,desc)
    diccionario[id]=gestor
    print('Nuevo usuario añadido con éxito')

def actualizarContraseña(diccionario):
    id=input('Id: ')
    psw=input('Contraseña: ')
    reg=diccionario.get(id)
    if reg:
        reg.psw=psw
        print('Clave actualizada con éxito')

def actualizarUsuario(diccionario):
    id=input('Id: ')
    usr=input('Usuario: ')
    reg=diccionario.get(id)
    if reg:
        reg.usr=usr
        print('Usuario actualizado con éxito')

def verId(diccionario):
    id=input('Id: ')
    reg=diccionario.get(id)
    if reg:
        print('Id: ',reg.id)
        print('Usuario: ',reg.usr)
        print('Clave: ',reg.psw)
        print('Descripcion: ',reg.desc)

def opciones():
    opcion=input('a. Agregar un usuario y una clave\nb. Actualizar clave\nc. Actualizar usuario\nd. Ver usuario y clave')

    if opcion.lower()=='a':
        