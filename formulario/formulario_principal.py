import tkinter as tk
from tkinter import ttk
import utileria.util_ventana as util_ventana
from config import *
from tkinter import scrolledtext, filedialog
import formulario.funciones as fn

class FormularioPrincipal(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.config_windows()
        self.frames_entry()
        self.conf_barra_texto ()
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

    def conf_barra_texto(self):        
        # hoja de texto
        self.text = scrolledtext.ScrolledText(self.frame_ventana_principal, width=50)
        self.text.place()
        self.text.pack(ipadx=250, ipady=1200, padx=50, pady=(20,0))

    def configuracion_buttons(self):
        # creamos txt con direccion del archivo
        archivo_abierto = "Nuevo archivo.txt"
        fn.direccion_archivo(archivo_abierto)
        # funcion que va a desplegar menu
        def archivo_nuevo_presionado():
            print("¡Has presionado para crear un nuevo archivo!")

        def archivo_nuevo():
            self.text.delete(1.0, tk.END)

        def abrir_archivo():
            # abre la ventana con archivos en el pc 
            archivo = filedialog.askopenfilename(defaultextension=".txt", 
                                                 filetypes=[("Archivos de texto", ".txt"),
                                                            ("Todos los archivos", "*.*")])
            # si archivo == true
            if archivo:
                archivo_abierto = archivo
                fn.direccion_archivo(archivo_abierto)
                # abrimos el archivo en modo lectura
                with open(archivo, "r") as f:
                    # almacenamos el texto en la variable contenido
                    contenido = f.read()
                    # borramos lo que sea que este en la hoja actual
                    self.text.delete(1.0, tk.END)
                    # insertamos en la hoja el texto de dentro de contenido
                    self.text.insert(tk.END, contenido)
            
        
        def archivo_guardar(): 
            archivo_abierto = fn.nombre_archivo()
            texto = self.text.get(1.0, 'end')  # Obtener el texto  
            with open(archivo_abierto, 'w') as archivo:  # Abrir o crear un archivo  
                archivo.write(texto)  # Escribir el texto en el archivo  
        
        '''def archivo_guardar_como():
            ruta = filedialog.askopenfilename(defaultextension=".txt",
                                              filetypes=[("Archivos de texto", ".txt"),
                                                         ("Todos los archivos", "*.*")])
            if ruta:
                with open(ruta, "w") as archivo:
                    archivo.write(self.text.get(1.0, "end"))'''


        #  ---creamos el menu desplegable---
        # colocamos menu_archivos dentro de barra_menus
        self.menu_archivos = tk.Menu(self.barra_menus, tearoff=False)
        # agregamos todos los comandos que va a tener el menu archivos
        self.menu_archivos.add_command(
            label="Nuevo", accelerator="Ctrl+N", command = archivo_nuevo)
        self.menu_archivos.add_command(
            label="Abrir", accelerator="Ctrl+A", command = abrir_archivo)
        self.menu_archivos.add_command(
            label="Guardar", accelerator="Ctrl+G", command=archivo_guardar)
        '''self.menu_archivos.add_command(
            label="Guardar como", accelerator="Ctrl+G", command=archivo_guardar_como)'''
        self.menu_archivos.add_command(label="")
        self.menu_archivos.add_separator()# agrega linea divisoria        
        self.menu_archivos.add_command(
            label="Salir",accelerator="Ctrl+S", command=archivo_nuevo_presionado)
        # al precionar archivo le decimos que se despliegue hacia abajo
        self.barra_menus.add_cascade(menu=self.menu_archivos, label="Archivo")

        # colocamos menu herramientas dentro de barra_menus
        self.menu_herramientas = tk.Menu(self.barra_menus, tearoff=False)
        # agregamos todos los comandos que va a tener el menu herramientas
        self.menu_herramientas.add_command(
            label="Fuente", accelerator="Ctrl+F", command=archivo_nuevo_presionado)
        self.menu_herramientas.add_command(
            label="Tamaño", accelerator="Ctrl+T", command=archivo_nuevo_presionado)
        self.menu_herramientas.add_command(
            label="Color", accelerator="Ctrl+C", command=archivo_nuevo_presionado)
        # al precionar herramientas le decimos que despliegue hacia abajo
        self.barra_menus.add_cascade(menu=self.menu_herramientas, label="Herramientas")
        self.config(menu=self.barra_menus)
    
        


        

        