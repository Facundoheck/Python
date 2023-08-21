import tkinter as tk
from style import styles

class MainMenu(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(
            background=styles.BACKGROUND

        )
        self.init_widgets()
    
    def init_widgets(self):
        tk.Button(
            self,
            text="Crear una tarea",
            command=lambda: self.manager.home_to_create(),
            **styles.STYLE,
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text="Modificar una tarea",
            command=lambda: print("Has cliqueado para modificar una tarea"),
            **styles.STYLE,
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text="Borrar una tarea",
            command=lambda: print("Has cliqueado para borrar una tarea"),
            **styles.STYLE,
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )
