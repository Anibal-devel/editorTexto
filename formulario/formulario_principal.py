import tkinter as tk
from tkinter import ttk
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
        w, h = 900, 720
        util_ventana.centrar_ventana(self, w, h)
    
    def frames_entry(self):
        # frame barra superior
        self.frame_barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=25)
        # ubicacion y comportamiento espacial
        self.frame_barra_superior.pack(side=tk.TOP, fill="both")

        # frame ventana principal
        self.frame_ventana_principal = tk.Frame(self, bg=COLOR_FONDO_VENTANA)
        self.frame_ventana_principal.pack(side=tk.TOP, fill="both", expand=True)

         # frame barra inferior
        self.frame_barra_inferior = tk.Frame(self.frame_ventana_principal, bg=COLOR_BARRA_SUPERIOR, height=25)
        self.frame_barra_inferior.pack(side=tk.BOTTOM, fill="both", expand=False)

    def conf_barra_superior(self):        
        # entry 
        self.text = tk.Text(self.frame_ventana_principal, width=50)
        self.text.place()
        self.text.pack(ipadx=250, ipady=900, padx=10, pady=10)

    def configuracion_buttons(self):

        # button abrir
        self.abrir = tk.Button(self.frame_barra_superior, text="Abrir", bg=COLOR_BARRA_SUPERIOR, 
                               fg="black", font=("Arial", 12))
        self.abrir.pack(side=tk.LEFT)

        # button guardar

        

        