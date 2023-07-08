import re

patron=r"\s"
texto="Hola mundo"
if re.search (patron, texto) is not None:
    print ("Si existe")
else:
    print ("No hayamos nada")

# lo que digo es, si existe algún espacio (\s) en la variable texto, imprimí "Si existe"

# para reemplazar una palabra
texto = "A caballo regalado, no se le mira la sonrisa"
patron = "mira la sonrisa"
resultado=re.sub (patron, "miran los dientes",texto)
print (resultado) 
