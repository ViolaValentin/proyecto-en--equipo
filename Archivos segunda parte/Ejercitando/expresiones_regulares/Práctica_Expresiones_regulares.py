import re
#1
"""
string="Hola, soy una cadena y tengo 5 caracteres permitidos"
patron= "[A-Za-z0-9]"

print (bool (re.search (patron,string)))
"""
#2
"""
string="Hola, soy una cadena y tengo caracteres permitidos"
patron= "[^A-Za-z0-9]"
print (bool(re.search (patron,string)))
"""
#3

"""
#a 
string="Hola, soy una cadena y tengo caracteres permitidos, hello"
patron= "he*" # encuentra un H y cuenta la cantidad de E, el * solo afecta a e
print (re.findall (patron,string))
#b
string="Hola, soy una cadena y tengo caracteres permitidos, hello"
patron= "he+" 
print (re.findall (patron,string))
#c
string="Hola, soy una cadena y tengo caracteres permitidos, hello"
patron= "he?"
print (re.findall (patron,string))
#"he?^e" encuentra el patron he una vez y luego pide que no haya ninguna e
string="Hola, soy una cadena y tengo caracteres permitidos, hello"
patron= "he{2,3}"
print (re.findall (patron,string))"""

""""#4
def palabras_unidas (palabra1,palabra2):
    string="Hola,soyuna_cadenaytengocaracteres_permitidos"
    patron=f"{palabra1}_{palabra2}"
    return (re.search (patron,string))
    
print (palabras_unidas ("una","cadena"))
"""
"""
def palabras_unidas (string):
        
        return (re.search (patron,string))

print (palabras_unidas ("Hola,soyuna_cadenaytengocaracteres_permitidos"))
"""

"""#5
def comienzo_string (numero):
    string="4Hola,soyuna_cadenaytengocaracteres_permitidos"
    patron=f"^{numero}"
    return (re.search (patron,string))
print (comienzo_string (4))"""

#6
"""
    
def string_en_lista (lista,pattern):
    pattern=re.compile (lista)
    if re.search (pattern,lista):
        return True
    else:
        return False
print (string_en_lista(["Hola""Hola,esto es una lista","Estoy formada","por muhcas partes"],"Hola"))"""
#8
def separar_caracteres (string):
    pattern="\d"
    final=re.findall(pattern,string)
    final_split=re.split ("\d",string)
    return (final,final_split)
print (separar_caracteres ("aca hay algunos c4racteres n0meric0s"))

#9
def entre_guiones (string):
    return    re.findall ("-(.*?)-",string) # el "?" le indica a python que se enfoque en matches internos

print (entre_guiones ("esto es -una cadena - que tiene matches- internos y no simepre coinciden-"))

#11
"""def lista_strings (string):
    for elemento in string:
        resultado=re.match ("(P\w*) (P\w*)",elemento)
        return (resultado.group()) # el group contiene el resultado que matcheo, que coincide.
print (lista_strings(["Practica Python","Practica"]))
"""
#15
def mail (string):
    return bool (re.search ("^\w+[.-_]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?$",string))
    # el + indica uno o mas
    #el ? indica 0 o mas
print (mail("valentinviola@gmail.com"))
print (mail("valentin&viola@gmail.com")) #el & no est á permitido, debería devolver False


def string_reemplazado (string):
    return string.replace (" ", ";").replace ("m",";")

