import tkinter as tk
from tkinter import font
import utileria.util_ventana as util_ventana
from config import *
from tkinter import scrolledtext, filedialog
import formulario.funciones as fn
import numpy as np

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
        self.text.config(font=("Arial", 15))
        self.text.place()
        self.text.pack(ipadx=250, ipady=1200, padx=50, pady=(20,0))

    def configuracion_buttons(self):

        # --------------------- Menu archivos ----------------------------
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
        
        def archivo_salir():
            self.destroy()

        #  ---creamos el menu desplegable---
        # colocamos menu_archivos dentro de barra_menus
        self.menu_archivos = tk.Menu(self.barra_menus, tearoff=False)
        # agregamos todos los comandos que va a tener el menu archivos
        self.menu_archivos.add_command(
            label="Nuevo", accelerator="Ctrl+N", command = archivo_nuevo)
        self.menu_archivos.add_command(
            label="Abrir", accelerator="Ctrl+A", command = abrir_archivo)
        self.menu_archivos.add_command(
            label="Guardar", accelerator="Ctrl+G", command = archivo_guardar)
        '''self.menu_archivos.add_command(
            label="Guardar como", accelerator="Ctrl+G", command=archivo_guardar_como)'''
        self.menu_archivos.add_command(label="") # agregamos un espacio 
        self.menu_archivos.add_separator()# agrega linea divisoria        
        self.menu_archivos.add_command(
            label="Salir",accelerator="Ctrl+S", command = archivo_salir)
        # al precionar archivo le decimos que se despliegue hacia abajo
        self.barra_menus.add_cascade(menu=self.menu_archivos, label="Archivo")
        
        # ----------------- Menu herramientas------------------------    
        
        # colocamos menu herramientas dentro de barra_menus
        self.menu_herramientas = tk.Menu(self.barra_menus, tearoff=False)
        # colocamos menu fuentes dentro del menu_herramietnas
        self.file_fuentes = tk.Menu(self.menu_herramientas, tearoff=False) 
        # colocamos menu tamaño dentro del menu_herramientas
        self.font_size = tk.Menu(self.menu_herramientas, tearoff=False)
        # colocamos el menu color dentro del menu_herramietas
        self.font_color = tk.Menu(self.menu_herramientas, tearoff=False)
        # agregamos todos los comandos que va a tener el menu herramientas
        self.menu_herramientas.add_cascade(
            label="Fuente", accelerator="Ctrl+F", menu=self.file_fuentes)
        self.menu_herramientas.add_cascade(
            label="Tamaño", accelerator="Ctrl+T", menu=self.font_size)
        self.menu_herramientas.add_cascade(
            label="Color", accelerator="Ctrl+C", menu=self.font_color)
        # al precionar herramientas le decimos que despliegue hacia abajo
        self.barra_menus.add_cascade(menu=self.menu_herramientas, label="Herramientas")
        self.config(menu=self.barra_menus)

        # --------- menu fuentes ---------
        def fuente_seleccionada(letra):
            # al texto de la pantalla le pasamos la fuente deseada
            # obtenemos objeto fuente
            fuente = font.Font(font=self.text.cget("font")) 
            # obtenemos tamaño actual
            tamaño_actual = fuente.actual("size")
            self.text.config(font=(letra, tamaño_actual))
            
        #creamos la lista fuentes para luego poder recorrerla y asignarla al menu fuentes
        lista_fuentes = list(font.families())
        # ordenamos la lista
        lista_fuentes.sort()
        # agregamos todas las fuentes al menu fuentes
        for fuente in lista_fuentes:                       # al seleccionar llama funcion seleccionada
            self.file_fuentes.add_command(
                label=fuente, command=lambda letra=fuente: fuente_seleccionada(letra))

        # --------- menu tamaño fuente -------
        def asignar_tamaño(tamaño):
            self.text.config(font=("Arial",tamaño))
        
        # creamos lista de tamaños para la fuente
        lista_tamaños = np.arange(10, 101)
    
        for tamaño in lista_tamaños:
            self.font_size.add_command(
                label=tamaño, command=lambda valor=tamaño: asignar_tamaño(valor))
            
        # --------- menu color fuente --------
        def asignar_color(color):
            self.text.config(fg=color)

        # creamos lista de colores para la fuente
        
        dic_colores ={"black": "negro", "blue": "azul", "brown":"marron", "green":"verde", "grey":"gris" 
                        ,"orange":"naranja" ,"pink":"rosa" ,"purple":"violeta" ,"red":"rojo" 
                        ,"white": "blaco", "yellow":"amarillo"}
        # recorremos la lista de colores y la añadimos a font_color
        for color_fuente, color_menu in dic_colores.items():
            self.font_color.add_command(
                label=color_menu, command=lambda color_letra=color_fuente: asignar_color(color_letra))

            

        
        


        

        