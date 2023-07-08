#Definir un procedimientos qie lea los archivos .txt que están en la carpeta marzo, y copie la primera 
#linea de cada uno en un archivo dentro de la carpeta resultados (que debe estar dentro de new)
#!/usr/bin/env python3
import sys,re,os, glob
"""def primeras_lineas (carpeta_mes,carpeta_resultado,archivo_salida):
  
    movemos a marzo
    extraemos los .txt
    leemos las primeras lineas
    hacemos la carpeta de salida
    hacer archivo
    poner lineas en archivo nuevo
  
    os.chdir (carpeta_mes)
    textos=glob.glob (".txt")
    primera_linea=[]
    for lines in textos:
        with open (lines,"r") as texto:
            primera_linea.append(texto.readline())
    os.chdir ("../../")
    os.mkdir (carpeta_resultado)
    os.chdir (carpeta_resultado)
    with open (archivo_salida,"a") as final_txt:
        primera_lineaStr="".join (primera_linea)
        final_txt.write (primera_lineaStr)

print (primeras_lineas("datos/marzo","resultado","salida.txt"))
"""
#3
"""
def contenido_listas (nombre_archivo,numero_lineas):       
    ultimas_lineas=[]
    todas_las_lineas=[]
    with open (nombre_archivo,"r") as archivo:
            contenido_lineas=(archivo.readlines ()[:numero_lineas])
            todas_las_lineas.append (contenido_lineas)
            lista_invertida=todas_las_lineas.reverse ()
            return (lista_invertida)
print (contenido_listas ("ej1.txt",6))"""
#no logro inverit la lista
"""


#Definir un procedimientos que lea los archivos .txt que están en la carpeta marzo, y copie la primera 
#linea de cada uno en un archivo dentro de la carpeta resultados (que debe estar dentro de new)
#!/usr/bin/env python3
import re,glob,sys,os

def archivos_marzo(path_carpeta,archivo_salida):
    #muevo a carpeta marzo
    #traigo archivos txt
    #leo primera linea de codigo
    #creo la carpeta resultados
    #me muevo a ala carpeta
    #escribo esas lineas en un archivo

    os.chdir (path_carpeta) #me muevo a la carpeta marzo
    txt=glob.glob("*.txt")
    primeras_lineas=[]
    for archivos_txt in txt:
        with open (archivos_txt,"r") as arch_txt:
            primeras_lineas.append(arch_txt.readline())

            os.chdir ("../../")
            os.mkdir ("./resultados")
            os.chdir ("./resultados")
            with open (archivo_salida,"a") as arch_salida:
                primeras_lineasStr="".join(primeras_lineas)
                arch_salida.write(primeras_lineasStr)

"""
"""Escribí un programa que lea todos los archivos .txt de una carpeta dada 
(Carpeta1) y los añada a un archivo dentro de la carpeta Resultado, 
que a su vez se tiene que encontrar dentro de Carpeta1."""

def leyendo_txt (Carpeta1, archivo_salida):
    #me muevo a carpeta1
    #agarro todos los txt
    #los leo
    #me muevo a carpeta1
    #creo archivo resultado en Carpeta1
    #escribo el archivo

    os.chdir (Carpeta1)
    txt=glob.glob("*.txt")
    archivos_leidos=[]
    for leer_archivos in txt:
        with open (leer_archivos, "r") as leer_arch:
            archivos_leidos.append(leer_arch.read())
    os.mkdir ("./Resultados")
    os.chdir("./Resultados")
    with open (archivo_salida,"a") as arch_salida:
        archivos_leidosStr="".join(archivos_leidos)
        arch_salida.write (archivos_leidosStr)
leyendo_txt ("./Carpeta1","salida.txt")