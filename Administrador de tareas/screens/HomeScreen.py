import tkinter as tk
from style import styles
from components.MainMenu import MainMenu

class HomeScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background=styles.BACKGROUND)
        self.init_widgets()
        
    def init_widgets(self):
        tk.Label(
            self,
            text="Crea o realiza tests",
            justify=tk.CENTER,
            **styles.STYLE #esto es lo mismo que pasarle todos los parametros de estilo que defini en la pestaña "styles.py" uno por uno
        ).pack(
            **styles.PACK #igual que el anterior, pero le paso los parametros de empaquetado que defini en la pestaña "styles.py" uno por uno
        )

       
        MainMenu(
            self,
            self.manager
        ).pack(
            **styles.PACK
        )