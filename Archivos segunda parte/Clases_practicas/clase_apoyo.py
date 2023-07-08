#Expresiones  regulares

#buscar una cantidad de caracteres


#a)"^ac.{10}gt$"
#b)"ac.{10}gt"

#a)"achaserdhewigt"
#b)"sadfsaachaserdhewigtdsfasd"

#buscar telefonos de capital federal
import re
re.findall ("(+5411)([0-9]{8})")

#que el numero de telefono empiece con 5
re.findall ("(+54115)([0-9]{7})")