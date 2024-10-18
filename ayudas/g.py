import tkinter as tk  
from tkinter import scrolledtext  

def guardar_archivo():  
    texto = text1.get(1.0, 'end')  # Obtener el texto  
    with open('archivo.txt', 'w') as archivo:  # Abrir o crear un archivo  
        archivo.write(texto)  # Escribir el texto en el archivo  

ventana = tk.Tk()  
text1 = scrolledtext.ScrolledText(ventana)  
text1.pack()  

boton_guardar = tk.Button(ventana, text='Guardar', command=guardar_archivo)  
boton_guardar.pack()  

ventana.mainloop()