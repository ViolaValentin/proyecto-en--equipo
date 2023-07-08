arch=open ("hola.txt","r")
print (arch) #is an in-memory stream for text.
print (arch.read()) #leer archivo
print (arch.readlines()) #lee linea a linea el archivo. devuleve una lista. cada elemento es una linea del archivo

#ubicación exacta de un archivo. Muestra el camino que debo recorrer, 
# teniendo en cuenta todos los posibles directorios, hasta llegar a un archivo

#leer archivos de otra carpeta
#print (arch.readlines("C:\UCEMA IPC\Fundamentos_de_Informatica\SCRIPTING\hola.txt"))

"""
Rutas relativas
./Doc/hola.txt
el punto indica, desde dónde estoy parado y luego la ruta hasta el archivo
Ventajas:
en el path absoluto yo asumo un usuario, y si se lo paso a alguien, puede no fsuncionar
en el path relativo, esto no pasa
"""
