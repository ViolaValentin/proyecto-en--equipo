#Esto siempre tiene que estar en un script
#!/bin/python3
""""def main():
    print ("Hello world")


if __name__=="__main__":
    main ()"""
#Este es el main script

"""
Funciones built-in. Ya vienen integradas con python. Por ejmeplo, print.
"""
import os, sys

#os (operative system) permite manipular archivos 
#sys es una biblioteca que dialoga con el os y permite tomar parámetros desde la terminal

usuario=sys.argv [1]

"""declaro una variable a la que le doy como valor un argumento. Toma los argumentos que le pasamos al script 
por consola
"""
def saludador(name):
        return  (f"Hola {name}")


if __name__=="__main__":
    print (saludador(usuario))

#MANIPULACIÓN DE ARCHIVOS
""""
# palabra reservada open()
# la instruccion es open (path_al_archivo, modo)
# el tipo de dato es un string
#el path me dice la ubicacion del archivo en la computadora
#el modo me dice qué quiero hacer con el archivo
# el tipo de dato tmb es un string
#para cerralo, archivo.close ()
"""





    