import tkinter as tk  

'''def mostrar_menu(event):  
    menu.post(event.x_root, event.y_root)'''  

# creo ventana
ventana = tk.Tk()  
ventana.geometry("200x200")  

# creo menu
menu = tk.Menu(ventana, tearoff=0)  
menu.add_command(label="Opción 1")  
menu.add_command(label="Opción 2")  
menu.add_command(label="Opción 3")  

# creo boton
boton = tk.Button(ventana, text="Desplegar Menú")  
boton.pack(pady=20)  

# le asigno la funcion al boton
boton.bind("<Enter>", lambda event: menu.post(event.x_root, event.y_root))  
#boton.bind("<Leave>", lambda event: menu.unpost())

ventana.mainloop()