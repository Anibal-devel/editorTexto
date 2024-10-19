
def direccion_archivo(direccion_archivo):
    # si no se abrio ningun archivo direccion archivo va a ser Nuevo archivo.txt de lo contrario 
    # poseera la direccion que se le haya mandado previamente
    with open("direccion.txt", "w") as file:
         file.write(direccion_archivo)

def nombre_archivo():
     # obtenemos la direccion del archivo
     with open("direccion.txt", "r") as file:
          direccion = file.read()
          return direccion


    

