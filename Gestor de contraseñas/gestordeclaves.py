import json

#inicializar diccionario
diccionario={}

#constructor de la clase gestor
class Usuario:
    def __init__(self,user,psw,desc):
        self.user=user
        self.psw=psw
        self.desc=desc
    
    def toDict(self):
        return {
            "Usuario" : Usuario.user,
            "Contraseña" : Usuario.psw
        }
    
    @classmethod
    def fromDict(cls,user_dic):
        return cls(user_dic["Usuario"],user_dic["Contraseña"])

class UserManager:
    def __init__(self):
        self.users = {}

#defino nuevas funciones para el gestor
def nuevoRegistro(self,user,psw,desc):
    user=input('Usuario: ')
    psw=input('Constraseña: ')
    desc=input('Descripcion: ')
    if user not in self.users:
        self.users[user]=Usuario(user,psw,desc)
        print('*'*30)
        print('Nuevo usuario añadido con éxito')
        print('*'*30)
    else:
        print('El usuario ya existe')

def actualizarContraseña(self,user,nueva_psw):
    user=input('Usuario: ')
    if user == self.users.get(user):
        nueva_psw=input('Nueva contraseña: ')
        self.users.psw=nueva_psw
        print('*'*30)
        print('Clave actualizada con éxito')
        print('*'*30)

def actualizarUsuario(self,user):
    user=input('Usuario: ')
    if user==self.users.get(user):
        nuevo_user=('Ingrese nuevo usuario: ')
        self.users.user=nuevo_user
        print('*'*30)
        print('Usuario actualizado con éxito')
        print('*'*30)
    else:
        print('El usuario ingresado no existe')

def verId(self,user):
    user=input('Usuario: ')
    if self.users.user==user:
        print('*'*30)
        print('Usuario: ',self.users.user)
        print('Clave: ',self.users.psw)
        print('Descripcion: ',self.users.desc)
        print('*'*30)

""" def opciones():
    while True:
        opcion=input('a. Agregar un usuario y una clave\nb. Actualizar clave\nc. Actualizar usuario\nd. Ver usuario y clave\ne. Salir\nIngrese opcion: ')
        if opcion=='a':
            nuevoRegistro()
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
 """
opciones()
