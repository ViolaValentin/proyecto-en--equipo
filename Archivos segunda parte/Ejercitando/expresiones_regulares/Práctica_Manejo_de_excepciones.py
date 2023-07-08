#1
lista_super = ["tomate", "fideos", "arvejas", "detergente", "jabón", "alcohol"]
try:
    lista_super+ "arroz"
except:
    print("no puedo agregar eso a la lista")

print (lista_super)


#2

def lista_numeros (listado_numeros,numero_solo):
    resultados=[]
    try:
        for numero in listado_numeros:
            resultados.append (numero/numero_solo)
    except ZeroDivisionError:
        print ("no puedo dividir por 0")
        return  resultados
print (lista_numeros ([1,2,3,4],1))
# no se qué me falta, no llego al resultado
#3
def lista_positiva (lista,numero):
    if numero>=0:
        lista.append(numero)
    else:
        raise ValueError ("Error")
    
    print  (f"Tu lista final es {lista}")

lista_positiva ([1,2,3,5],4)

