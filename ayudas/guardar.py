import tkinter as tk  
from tkinter import scrolledtext, filedialog  

def guardar_archivo():  
    ruta = filedialog.asksaveasfilename(defaultextension=".txt",  
                                          filetypes=[("Archivos de texto", "*.txt")
                                                     , ("Todos los archivos", "*.*")])  
    if ruta:  
        with open(ruta, 'w') as archivo:  
            archivo.write(texto.get(1.0, 'end'))  

ventana = tk.Tk()  
texto = scrolledtext.ScrolledText(ventana, width=40, height=10)  
texto.pack()  

boton_guardar = tk.Button(ventana, text="Guardar como", command=guardar_archivo)  
boton_guardar.pack()  

ventana.mainloop() 