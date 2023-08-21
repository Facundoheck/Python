import tkinter as tk
from Controller import Controller
from screens.HomeScreen import HomeScreen
from style import styles


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
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)