""""
#1
with open ("ej1.txt","r") as ej1:
    print (len(ej1.readlines()))
 """
"""#2
contador=0
lista=[]
def contenido_listas (nombre_archivo,numero_lineas):
    with open (nombre_archivo,"r") as archivo:
            lista_contenido=archivo.readlines()[:numero_lineas]
            lista.append (lista_contenido)
    return (lista_contenido)
print (contenido_listas ("ej1.txt",4))
  """


#3

def contenido_listas (nombre_archivo,numero_lineas):       
    ultimas_lineas=[]
    todas_las_lineas=[]
    with open (nombre_archivo,"r") as archivo:
            contenido_lineas=(archivo.readlines ()[:numero_lineas])
            todas_las_lineas.append (contenido_lineas)
            lista_invertida=todas_las_lineas.reverse ()
            return (lista_invertida)
print (contenido_listas ("ej1.txt",6))
#no logro inverit la lista

"""#4
def contar_palabras (nombre_archivo):   
    with open (nombre_archivo,"r") as archivo:
        cantidad_de_palabras= archivo.read()
        contar=cantidad_de_palabras.split (" ")
        return (len (contar))
print (contar_palabras("ej1.txt"))
"""
""""#5
def reemplazar_letras (nombre_archivo,letra_actual,letra_reemplazar):   
    with open (nombre_archivo,"r") as archivo:
        contenido_archivo= archivo.read()
        contenido_reemplazado=contenido_archivo.replace (letra_actual,letra_reemplazar)
        return (contenido_reemplazado)
print (reemplazar_letras("ej1.txt","a","a" + "\n"))
"""
#6
#Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.
"""
def eliminar_saltos_lineas (nombre_archivo,salto_linea,reemplazo,nombre_nuevo_archivo):   
    with open (nombre_archivo,"r") as archivo:
        contenido_archivo= archivo.read()
        contenido_reemplazado=contenido_archivo.replace (salto_linea,reemplazo)       
        with open (nombre_nuevo_archivo,"a") as archivo2:
            archivo2.write(contenido_reemplazado)
        return (contenido_reemplazado, archivo2)
print (eliminar_saltos_lineas("ej1.txt","\n","","arch2.txt"))
"""
"""#7Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual 
# debe imprimir y decir cuantos caracteres tiene.
def palabras_mas_larga (nombre_archivo):  
    max_long=0
    palabra=""
    with open (nombre_archivo,"r") as archivo:
        contenido_archivo= archivo.read()
        separo_palabras=contenido_archivo.split (" ")
       # falta un for que recorra la lista
        for word in separo_palabras:
            if len (word)>max_long:
                max_long=len(word)
                palabra=word 
        print (palabra)
print (palabras_mas_larga("ej1.txt"))"""
"""
#8
def dos_doc_en_uno (nombre_archivo1,nombre_archivo2,nombre_archivo3):  
    with open (nombre_archivo1,"r") as archivo1:
        contenido_archivo1= archivo1.read()
        with open (nombre_archivo2,"r") as archivo2:
            contenido_archivo2= archivo2.read()
            with open (nombre_archivo3,"a") as archivo3:
                archivo3_completo=contenido_archivo1+contenido_archivo2
                archivo3.write (archivo3_completo)
                return archivo3_completo
print (dos_doc_en_uno("ej1.txt","arch2.txt","arch3.txt"))"""

#9
"""
def contar_palabras (nombre_archivo,palabra_a_buscar):   
    with open (nombre_archivo,"r") as archivo:
        cantidad_total=[]
        cantidad_de_palabra_especifica= archivo.read()
        contar=cantidad_de_palabra_especifica.count (palabra_a_buscar)
        cantidad_de_palabras= archivo.read()
        cantidad_total.append (cantidad_de_palabras.split (" "))
        cantidad_total.count (palabra_a_buscar)
        return (contar,cantidad_total)
print (contar_palabras("ej1.txt","Hola"))
"""
"""import os, sys,glob
#10
def leer_archivos (nombre_archivo_carpeta_resultados):
    os.chdir ("C:\\Users\\valen\\Ejercicios\\Practicas_Python_Intro\\Carpeta 1")
    with open ("arch1111.txt","a") as archivtxt:
        archivtxt.write ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        with open ("arch2222.txt","a") as archiv2txt:
            archiv2txt.write ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
            os.mkdir(".\Resultados")
            os.chdir (".\Resultados")
            with open (nombre_archivo_carpeta_resultados,"a") as archivo3:
                            archivo3_completo=archivtxt+archiv2txt
                            archivo3.write (archivo3_completo)
                            return archivo3_completo

leer_archivos("Tercerarchivo.txt")
"""