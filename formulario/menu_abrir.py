import tkinter as tk
from formulario.formulario_principal import FormularioPrincipal
import main as mn

def archivo_nuevo():
    mn.editor_texto.destroy()
    nuevo_ventana = FormularioPrincipal()
    nuevo_ventana.mainloop()

