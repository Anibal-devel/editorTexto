import tkinter as tk
import utileria.util_ventana as util_ventana
from config import *

class FormularioPrincipal(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.config_windows()
        self.frames_entry()
        self.conf_barra_superior ()
    
    def config_windows(self):
        # configuracion de la ventana
        self.title("Editor de texto")
        self.iconbitmap("./imagenes/logo.ico")
        w, h = 1800, 720
        util_ventana.centrar_ventana(self, w, h)
    
    def frames_entry(self):
        # frame barra superior
        self.frame_barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        # ubicacion y comportamiento espacial
        self.frame_barra_superior.pack(side=tk.LEFT, fill="both")

        # frame ventana principal
        self.frame_ventana_principal = tk.Frame(self, bg=COLOR_FONDO_VENTANA)
        self.frame_ventana_principal.pack(side=tk.TOP, fill="both", expand=True)

    def conf_barra_superior(self):        
        # entry 
        self.entry = tk.Entry(self.frame_ventana_principal, bg=COLOR_FONDO_ENTRY)
        self.entry.place()
        self.entry.pack(ipadx=500, ipady=1100)

        