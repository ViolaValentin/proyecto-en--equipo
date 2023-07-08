""""with open ("nombre_1.txt","a") as arch1:
    #print (arch_1.read())
    #arch_1.write ("Lorem ipsumvewvew")
    with open ("nombre_2.txt","a") as arch2:
      print  ("Algo") 
        #arch_2.write ("Ipsum lorem vrwerv")

    archivo1= arch1
    archivo2=arch2

    archivo1,archivo2=arch2,arch1

    with open ("arch1","r"):
        print (arch1.read ())
    with open ("arch2","r"):
        print (arch2.read ())s
"""""""
nombre_viejo_1=open ("archivo_1.txt","r+").write("Lorem")
nombre_viejo_2 = open ("archivo_2.txt","r+").write ("Ipsum")
nombre_nuevo_1,nombre_nuevo_2 = nombre_viejo_2,nombre_viejo_1
"""""""
import os,sys
usuario=sys.argv [1]
def cambiar_nombre_archivo (usuario):
    print (usuario)
print (cambiar_nombre_archivo(usuario))"""
#dialoga con el os y permite tomar parámetros desde la terminal
import os,sys

#comprobar si un archivo existe os.path.exists (path="C:\UCEMA IPC\Fundamentos_de_Informatica\SCRIPTING\f1.txt")
archivo1=sys.argv [1]
archivo2=sys.argv [2]

def renombrar(archivo1,archivo2):

        os.rename(sys.argv[1],"temporal.txt")
        os.rename(sys.argv[2],sys.argv[1])
        os.rename("temporal.txt",sys.argv[2])
        return  (f"Archivos renombrados {archivo1,archivo2}")
            
if __name__=="__main__":
    print (renombrar)