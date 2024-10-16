import tkinter as tk
from tkinter import ttk
import utileria.util_ventana as util_ventana
from config import *
# from formulario.menu_abrir import Abrir

class FormularioPrincipal(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.config_windows()
        self.frames_entry()
        self.conf_barra_superior ()
        self.configuracion_buttons()
    
    def config_windows(self):
        # configuracion de la ventana
        self.title("Editor de texto")
        self.iconbitmap("./imagenes/logo.ico")
        w, h = 900, 720
        util_ventana.centrar_ventana(self, w, h)
    
    def frames_entry(self):
        # frame barra superior
        self.barra_menus = tk.Menu()
        #self.frame_barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=25)
        # ubicacion y comportamiento espacial
        #self.frame_barra_superior.pack(side=tk.TOP, fill="both")

        # frame ventana principal
        self.frame_ventana_principal = tk.Frame(self, bg=COLOR_FONDO_VENTANA)
        self.frame_ventana_principal.pack(side=tk.TOP, fill="both", expand=True)

         # frame barra inferior
        self.frame_barra_inferior = tk.Frame(self.frame_ventana_principal, bg=COLOR_BARRA_SUPERIOR, height=25)
        self.frame_barra_inferior.pack(side=tk.BOTTOM, fill="both", expand=False)

    def conf_barra_superior(self):        
        # hoja de texto
        self.text = tk.Text(self.frame_ventana_principal, width=50)
        self.text.place()
        self.text.pack(ipadx=250, ipady=1200, padx=50, pady=(20,0))

    def configuracion_buttons(self):

        # funcion que va a desplegar menu
        def archivo_nuevo_presionado():
            print("¡Has presionado para crear un nuevo archivo!")

        #  ---creamos el menu desplegable---
        # colocamos menu_archivos dentro de barra_menus
        self.menu_archivos = tk.Menu(self.barra_menus, tearoff=False)
        # agregamos todos los comandos que va a tener el menu archivos
        self.menu_archivos.add_command(label="Nuevo", accelerator="Ctrl+N", command=archivo_nuevo_presionado)
        self.menu_archivos.add_command(label="Abrir", accelerator="Ctrl+A", command=archivo_nuevo_presionado)
        self.menu_archivos.add_command(label="Guardar", accelerator="Ctrl+G", command=archivo_nuevo_presionado)
        # al precionar archivo le decimos que se despliegue hacia abajo
        self.barra_menus.add_cascade(menu=self.menu_archivos, label="Archivo")
        self.config(menu=self.barra_menus)
    
        


        

        