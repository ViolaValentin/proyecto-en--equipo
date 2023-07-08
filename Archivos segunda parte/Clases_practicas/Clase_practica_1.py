""""def anterior_siguiente ():
    a= int (input ("Dame un número"))
    b= int (input ("Dame un valor"))
    print (a+1)
    print (b-1)

anterior_siguiente()

def doble ():
    a= int (input ("Dame un número"))
    print (a*2)

doble()

def anterior_siguiente_doble ():
    a= int (input ("Dame un número"))
    print ((a+1)*2)
    print ((a-1)*2)

anterior_siguiente_doble()

#creo una funcion anidada a las anteriores
def doble_anterior_siguiente():
     return str(anterior_siguiente(2))

"""
"""def retirar_dinero (saldo,monto):
            return max (saldo-monto, 0)
retirar_dinero(100,1000)

def dia_de_la_semana_favorito (dia):
    return dia=="sabado" or dia=="Sábado"
print (dia_de_la_semana_favorito ("sabado"))
"""
#11
def longitud_si_h (string):
    if len (string) >0:
        firstchar=string[0]
        if firstchar=="h" or firstchar=="H":
            return (len(string))
print (longitud_si_h ("Hola"))

#12

def Buenos_o_Buenas (string):
    #return "Buenas" in string or "Buenos" in string
    return string.startswith ("Buenos") or string.startswith("Buenas")
print (Buenos_o_Buenas ("Buenas tardes"))

