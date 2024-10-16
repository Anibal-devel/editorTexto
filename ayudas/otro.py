import tkinter as tk  

def mostrar_menu(event):  
    menu.post(event.x_root, event.y_root)  

def cerrar_menu(event):  
    menu.unpost()  

root = tk.Tk()  
boton = tk.Button(root, text="Abrir Menú")  
boton.pack()  

menu = tk.Menu(root, tearoff=0)  
menu.add_command(label="Opción 1")  
menu.add_command(label="Opción 2")  

boton.bind("<Enter>", mostrar_menu)  # Mostrar menú al pasar el cursor  
boton.bind("<Leave>", cerrar_menu)    # Cerrar menú al salir el cursor  

root.mainloop()