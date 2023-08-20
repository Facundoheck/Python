import tkinter as tk

# Crear una ventana
root = tk.Tk()
root.title("Ejemplo de Botones")

# Función que se ejecutará cuando se haga clic en el botón
def boton_clic():
    etiqueta.config(text="¡Botón clickeado!")

# Crear un botón
boton = tk.Button(root, text="Clic Me", command=boton_clic)
boton.pack()

# Etiqueta para mostrar mensajes
etiqueta = tk.Label(root, text="")
etiqueta.pack()

# Iniciar el bucle de eventos
root.mainloop()
