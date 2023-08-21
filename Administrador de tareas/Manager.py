import tkinter as tk
from Controller import Controller
from screens.HomeScreen import HomeScreen
from style import styles
from screens.AddTestScreen import AddTestScreen
from screens.UpdateTestScreen import UpdateTestScreen

class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Administrador de tareas")
        self.controller = Controller()
        container = tk.Frame(self)
        container.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )
        container.configure(
            background=styles.BACKGROUND
        )
        container.grid_columnconfigure(0, weight=1) #referencia 1: COLUMNA
        container.grid_rowconfigure(0, weight=1) #referencia 2: fila
        
        self.frames = {}
        
        pantallas = (HomeScreen, AddTestScreen, )
        for F in pantallas:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky=tk.NSEW) #esta linea junto con referencia 1 y 2 permite ver el frame completo en la pantalla

        self.show_frame(HomeScreen)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise() #pone enfrente el frame
    
    #transiciones

    def home_to_create(self):
        self.show_frame(AddTestScreen)

    def home_to_update(self):
        new_options = self.get_test_names()
        self.frames[UpdateTestScreen].options.update_options(new_options)
        self.show_frame(UpdateTestScreen)
        