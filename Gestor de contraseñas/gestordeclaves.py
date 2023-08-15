import json

#constructor de la clase gestor
class Usuario:
    def __init__(self,user,psw):
        self.user=user
        self.psw=psw
    
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

    def nuevoUsuario(self,user,psw):
        if user not in self.users:
            self.users[user]=Usuario(user,psw)
            print('*'*30)
            print('Nuevo usuario añadido con éxito')
            print('*'*30)
        else:
            print('*'*30)
            print('El usuario ya existe')
            print('*'*30)

    def actualizarContraseña(self,user,nueva_psw):
        username = self.users.get(user)
        if username:
            self.users.psw=nueva_psw
            print('*'*30)
            print('Clave actualizada con éxito')
            print('*'*30)

    def actualizarUsuario(self,user,nuevo_user):
        if user==self.users.get(user):
            self.users.user=nuevo_user
            print('*'*30)
            print('Usuario actualizado con éxito')
            print('*'*30)
        else:
            print('*'*30)
            print('El usuario ingresado no existe')
            print('*'*30)

    def listaUsuario(self):
        print("Usuarios registrados:")
        for username, user in self.users.items():
            print('*'*50)
            print(f"Usuario: {username}, Contraseña: {user.psw}")
            print('*'*50)

    def toJson(self, filename):
            user_list = [user.to_dict() for user in self.users.values()]
            with open(filename, 'w') as file:
                json.dump(user_list, file)
                print('*'*30)
                print("Registros exportados a", filename)
                print('*'*30)
def main():
    manager = UserManager()

    while True:
        opcion=input('1. Agregar un usuario y una clave\n2. Actualizar clave\n3. Actualizar usuario\n4. Ver usuario y clave\n5. Exportar datos a JSON\n6. Salir\nIngrese opcion: ')
        if opcion=='1':
            user=input('Usuario: ')
            psw=input('Constraseña: ')
            manager.nuevoUsuario(user,psw)
        elif opcion=='2':
            user=input('Usuario: ')
            nueva_psw=input('Nueva contraseña: ')
            manager.actualizarContraseña(user,nueva_psw)
        elif opcion=='3':
            user=input('Usuario: ')
            nuevo_user=('Ingrese nuevo usuario: ')
            manager.actualizarUsuario(user,nuevo_user)
        elif opcion=='4':
            manager.listaUsuario()
        elif opcion=='5':
            filename=input('Ingrese el nombre del archivo: ')
            manager.toJson(filename)
        elif opcion=='6':
            break
        else:
            print('Opción incorrecta, intente nuevamente')

if __name__ == "__main__":
    main()

