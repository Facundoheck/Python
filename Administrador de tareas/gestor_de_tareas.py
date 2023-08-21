#------------------#LIBRERIAS------------------#------------------#------------------#------------------

import tkinter as tk
import sqlite3

#------------------#CLASE------------------#------------------#------------------#------------------
class Tarea:
    def __init__(self,id,nombre,descripcion,completada):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.completada=completada

#------------------#FUNCIONES------------------#------------------#------------------#------------------

def nuevaTarea(tareas_registro):
    id=int(input('Codigo de la tarea: '))
    nombre=str(input('Nombre de la tarea: '))
    descripcion=str(input('Descripcion: '))
    completada=int(input('Completada (1-si/0-no): '))
    tarea=Tarea(id,nombre,descripcion,completada)
    tareas_registro[id]=tarea

def AgregarProducto(self):
        self.ventanaProducto= Toplevel()
        self.ventanaProducto.title("Nueva tarea")#nombre de productos
        
        self.frame = tk.Frame(self.ventanaProducto) #Frame sirve para contener a los widgets
        self.frame.pack(padx=90, pady=60) #Aca se le asigna el tamaño

        self.codigo=tk.Label(self.frame, text="Codigo de la tarea") #Crea una etiqueta
        self.entry = tk.Entry(self.frame) #Campo de entrada de texto
        self.codigo.pack()
        self.entry.pack() #empaqueta la entrada de texto
        
        
        self.descripcion=tk.Label(self.frame, text="Descripción") 
        self.entry1 = tk.Entry(self.frame) 
        self.descripcion.pack()
        self.entry1.pack() 
        
        
        self.marca=tk.Label(self.frame, text="Completada (1-si/0-no): ") 
        self.entry2 = tk.Entry(self.frame) 
        self.marca.pack()
        self.entry2.pack() 
        
        self.button = tk.Button(self.frame, text="Guardar",command=self.guardarEnInventario) #Se le da el comando al boton de que guarde en el inventario lo ingresado
        self.precio.pack()
        self.entry4.pack() 
        self.button.pack()
       
        self.Volver = tk.Button(self.frame, text="Volver",command=self.ventanaProducto.destroy)
        self.Volver.pack()



#------------------#BASE DE DATOS------------------#------------------#------------------#------------------

#establezco la conexión a la base de datos (se crea si no existe)
db_connection=sqlite3.connect("Tareas_db.db")

#creacion de un cursor para ejecutar consultas
cursor = db_connection.cursor()

# Ejecutar una consulta (crear una tabla si no existe)
#cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)")

# Insertar datos en la tabla
cursor.execute("INSERT INTO Tareas (id_tarea,nombre,descripcion,completada) VALUES (?,?,?,?)",(id,nombre,descripcion,completada))

# Guardar los cambios
db_connection.commit()

""" # Ejecutar una consulta para obtener datos
cursor.execute("SELECT * FROM Tareas")
rows = cursor.fetchall()
# Imprimir los resultados
for row in rows:
    print(row) """

#------------------#PROGRAMA PRINCIPAL------------------#------------------#------------------#------------------

# Create the main window
window = tk.Tk()
window.title("Tareas")
window.geometry("400x300")

# Create a label to display the pickup lines
label = tk.Label(window, text="Administrador de tareas")
label.pack(pady=20)

# Create a button
button = tk.Button(window, text="Agregar",command=nuevaTarea)
#button = tk.Button(window, text="Agregar", command=impress_crush)

button.pack()



# Start the main event loop
window.mainloop()

#------------------#CIERRE BD------------------#------------------#------------------#------------------

# Cerrar el cursor
cursor.close()

# Cerrar la conexión a la base de datos
db_connection.close()

print("\nDatos insertados correctamente.")
#------------------#------------------#------------------#------------------#------------------


