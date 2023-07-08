#!/bin/python3

"""with open ("mi_nombre.txt","r+") as mi_arch:
    mi_arch.read ()
    with open ("nuevo.txt","a") as nuevo_arch:
        nuevo_arch.write  (mi_arch.readline(5))
"""

texto=open ("mi_nombre.txt","r+").read()
print (texto[0:5])
texto_escribir=texto[0:5]
with open ("nuevo_arch.txt","a") as nue_arch:
    nue_arch.write (texto_escribir)

