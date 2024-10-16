import tkinter as tk
from tkinter import ttk
import utileria.util_ventana as util_ventana
from config import *
import formulario.formulario_principal as formulario_principal 

class Abrir(formulario_principal.FormularioPrincipal):
    def __init__(self):
        super().__init__()
        self.menu_abrir()

    def menu_abrir(self, event):
        # ----creamos frame menu_abrir    
        # llamo al frame barra superior y lo guardo en una variable
        barra_superior = fp.FormularioPrincipal(self.frame_barra_superior)
        # creamos el nuevo frame para ubicarlo en barra_barra superior
        self.frame_abrir = tk.Frame(barra_superior, 
                                    bg= COLOR_BARRA_SUPERIOR, height=100, width=350)
        self.frame_abrir.pack(side=tk.TOP, fill="both", expand=False)
