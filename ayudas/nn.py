import tkinter as tk  
from tkinter import scrolledtext, filedialog  

def abrir_archivo():  
    archivo = filedialog.askopenfilename(defaultextension=".py",  
                                          filetypes=[("Archivos de texto", "*.py"),  
                                                     ("Todos los archivos", "*.*")])  
    if archivo:  
        with open(archivo, 'r') as f:  
            contenido = f.read()  
            texto_area.delete(1.0, tk.END)  # Limpiar el área de texto antes de cargar nuevo contenido  
            texto_area.insert(tk.END, contenido)  

root = tk.Tk()  
texto_area = scrolledtext.ScrolledText(root)  
texto_area.pack(expand=True, fill='both')  

boton = tk.Button(root, text="Abrir Archivo", command=abrir_archivo)  
boton.pack()  

root.mainloop()