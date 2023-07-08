#le decimos a la pc con qué tiene que ejecutar el script
#!/usr/bin/env python3


import os, glob, sys
def ejercicio_ruta ():
    os.chdir ("Informes")
    txt=glob.glob ("*.txt")
    cantidad_estado=[]
    cantidad_lineas=[]
    for archivo in txt:
         with open (archivo, "r") as file:
            file_completo= (file.read())
            cantidad_estado.append (file_completo.count ("Estado"))
            cantidad_lineas.append (file_completo.count ("\n"))
            #len(file_completo.readline())
    os.mkdir ("./Apellidos")    
    with open ("Apellidos/Lista.txt", "w") as salida:
            for archivo in txt:
                 with open (archivo, "r") as file:
                      salida.write (file.readline())   
    return cantidad_estado, cantidad_lineas
c1,c2 = ejercicio_ruta()
os.listdir () #importa el nombre del archivo

glob.glob ("*") #hace lo mismo que listdir, me devuleve una lista con todos los archivos
 
glob.glob ("*.py") # me devuelve los archivos que tengan la extension .py #el * significa "todos"
lista=[]
contador=0
def findfile():
    os.chdir ("carpeta actual")
    files=glob.glob ("*.txt")
    for j in files:
            with open ("informes",'r"')as archivos:
                print (archivos.read())
                if "Estado" in archivos.read():
                    contador=+1

            os.mkdir ("./Apellidos")
            open with ("Lista.txt","a"):
                pass
    return (contador)                
if __name__=="__main__":
    print (findfile)


import re
def mail():
     return bool (re.search ("^\w+[.-_]?\w*@+[a-z]+[.][a-z]+[.]?[a-z]?"))