#Expresiones regulares
import re,sys,glob,os   
#1
"""Escribí un programa que verifique si un string 
tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9."""
""""
def verificar_string (string):
    return bool (re.search("[a-zA-Z0-9]",string))

print (verificar_string (("En este string hay 20 caracteres")))
"""

#2
"""Escribí un programa que verifique si un string 
tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9."""

""""def verificar_string(string):

        return bool (re.search("r[^a-zA-Z0-9]+",string))

print (verificar_string (("Enestestri@nghaycaracteres")))"""

#3
""""
Creá un programa que verifique las siguientes condiciones:
si un string dado tiene una h seguida de ninguna o más e.
si un string dado tiene una h seguida de una o más e.
si un string dado tiene una h seguida de cero o una e.
si un string dado tiene una h seguida de dos o tres e."""

"""def verificar_string (string,patron):
    return bool (re.search(patron,string))

print (verificar_string ("En este string hay 20 caracteres","he*"))
print (verificar_string ("En este string heay 20 caracteres","he+"))
print (verificar_string ("En este string hay 20 caracteres","he?"))
print (verificar_string ("En este string hay 20 hecarheacteres","[he]{2,3}"))
"""

#4
""""Realizá un programa que encuentre una palabra unida a otra con un 
guión bajo en un string dado (el string no debe contener espacios)."""

""""def verificar_string (string,palabra1,palabra2):
    patron=f"{palabra1}_{palabra2}"
    return (re.search(patron,string))

print (verificar_string ("Enestestring_hay20_caracteres","string","hay"))"""

#5
"""
Escribí un programa que diga si un string empieza con un número específico.
"""

""""def verificar_string (string,numero):
    return bool (re.search(f"^{numero}",string))

print (verificar_string ("2En este string hay 20 caracteres",4))"""

#6

""""Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada."""


""""def verificar_string (string):

    for secuencia in string:
        if secuencia in string:
            print ("Está")
        else:
            print ("No está")

lista=["hay","caracteres","eavews"]
print (verificar_string ("En este string hay 20 caracteres"))"""

#7
"""Realizá un programa que encuentre un string que contenga solamente 
letras minúsculas, mayúsculas, espacios y números."""

""""def verificar_string (string):
    return bool (re.search("[a-zA-z0-9]+\s+",string))

print (verificar_string (("Enestest ringhay20caracteres")))
"""
#8
""""Escribí un programa que separe y devuelva los caracteres númericos de un string."""
""""def verificar_string (string):
    return (re.findall("\d+",string))

print (verificar_string (("Enes10test ringhay20carac30teres")))
"""
#9
"""Escribí un programa que extraiga los caracteres que estén entre guiones en un string. 
(String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")"""

"""'def verificar_string (string):
    return (re.findall("-(.*?)-",string))

print (verificar_string (("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")))
"""
#10
""""Obtené las substrings y las posiciones de estas en una string dada considerando 
que las substrings están delimitadas por los caracteres @ o &.s"""
""""def sub_strings (string):
    return (re.findall("@(.*?)&.s",string))
    
print (sub_strings (("fewvewwev @ewvew&.s  fevae&.s fqc&.s afe@vew&.s")))
"""
#11
"""
Realizá un programa que dado una lista de strings verifique que dos palabras dentro del 
string empiecen con la letra P y las imprima.
 (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
"""
""""def string_letra_p (lista):
    for i in lista:
        patron="(P\w*) (P[a-z]*)"
        print (re.findall(patron,i))

print (string_letra_p (["Prática Python", "Práctica C++", "Práctica Fortran"]))"""
#CONSULTAR POR LOS ESPACIOS

#12
""""Escribí un programa que reemplace todas las ocurrencias de 
espacios, guiones bajos y dos puntos por la barra vertical (|)."""
""""def sub_strings (string):
    return string.replace("_","|").replace(" ","|").replace(":","|")
    
print (sub_strings (("hola_a todas y: todos")))"""

#13
""""Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos."""

"""def reemplazar2 (string):
    return (re.sub("(\W)",'_',string,count=2))

print (reemplazar2 (("Hoy523@es@@tuvimos trabajand735o con re -regul74ar expr52ession- en py@th532523on -con VSC532ode-")))

"""
#14
""""Realizá un programa que reemplace los espacios y tabulaciones por punto y coma."""

"""def reemplazar (string):
    return string.replace(" ",";").replace("    ",";")
    
print (reemplazar (("hola_a todas y: todos ")))"""

#15
""""Realizá un programa que validar si una cuenta de mail está escrita correctamente."""
"""
def verificar_string (string):
    return (re.search(r"[a-z0-]+[._-]?[a-z0-9]*[@][a-z]+[.]?[a-z]*",string))

#^[a-z0-9]+[.-_]?[a-z0-9]+@[a-z]+[.][a-z]+[.]?[a-z]?$
print (verificar_string (("valentinviola@gmail.com")))"""

""""def verificar_string (string):
    return (re.search("Hola\sbuen\sdia",string))

print (verificar_string("Hola buen dia"))"""
#Manipulación de archivos

#1
"""Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con 
una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P")."""

""""def lineas_con_p (archivo,letra):
    contador=0
    with open (archivo, "r") as arch:
       for linea in arch:
           if (linea[0] != letra.lower() and linea[0] !=letra.upper()):
               contador+=1
    return contador  

print (lineas_con_p ("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt","P"))
"""
#otra forma mas corta pero solo toma o p o P

""""def lineas_con_p2 (archivo,letra):
    contador=0
    with open(archivo, "r") as archivo:
        for linea in archivo:
            if linea.startswith(letra):
                contador += 1
        return contador
print (lineas_con_p2 ("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt","p"))      
"""
#2
""""Escribí un programa que lea un archivo e imprima las primeras n líneas."""
""""
def primeras_lineas (archivo,numero_de_lineas):
    with open (archivo,"r") as archivo:
        lineas_de_archivo=archivo.readlines ()[:numero_de_lineas]
        return lineas_de_archivo
print (primeras_lineas("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt",4))
"""
#3
""""Escribí un programa que lea un archivo, guarde las líneas
 del archivo en una lista y luego imprima las n últimas."""

""""def primeras_lineas (archivo,numero_de_lineas):
    with open (archivo,"r") as archivo:
        lineas_de_archivo=archivo.readlines ()[-numero_de_lineas:]

        return lineas_de_archivo
print (primeras_lineas("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt",1))
"""
#4
""""Hacé un programa que lea un archivo, cuente la cantidad de
 palabras del archivo y luego imprima el resultado."""
""""def primeras_lineas (archivo):
    with open (archivo,"r") as archivo:
        lineas_de_archivo=archivo.read ()
        lineas_de_archivoStr="".join(lineas_de_archivo)
        return (len (re.split (" |\n",lineas_de_archivoStr)))
       
print (primeras_lineas("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt"))
"""
#5
""""Escribí un programa que lea un archivo, reemplace una letra por 
esa misma letra más un salto de línea y lo guarde en otro archivo."""
""""
def primeras_lineas (archivo,letra):
    with open (archivo,"r") as archivo:
        archivo_leido=archivo.read ()
        return archivo_leido.replace (letra,f"{letra}\n")
       
       
print (primeras_lineas("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt","P"))
"""
#6
''''Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.'''

""""def primeras_lineas (archivo,archivo2):
    with open (archivo,"r") as archivo:
        archivo_leido=archivo.read ()
        archivo_reemplazado= archivo_leido.replace ("\n","")
        with open (archivo2,"a") as archivo2:
            archivo2.write (archivo_reemplazado)
       
print (primeras_lineas("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt","archiv2"))"""

#7
"""Escribí un porgrama que lea un archivo e identifique la palabra más larga, 
la cual debe imprimir y decir cuantos caracteres tiene."""

""""def palabra_mas_larga (archivo):
    with open (archivo,"r") as archivo:
longitud_maxima = 0
    for palabra in archivo_leido:
        if len(palabra) > longitud_maxima:
            longitud_maxima = len(palabra)
            palabra_mas_larga = palabra
            return (palabra_mas_larga)

print (palabra_mas_larga("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt"))"""

#8
"""
Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.
"""

""""def contenido_archivos (archivo1,archivo2,archivo3):
    with open (archivo1,"r") as arch1, open (archivo2,"r") as arch2, open (archivo3,"a") as arch3:
        archivos_leidos=arch1.read()
        archivos_leido2=arch2.read()
        archivos_leidos3=archivos_leidos+archivos_leido2
        return arch3.write(archivos_leidos3)
print (contenido_archivos("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt","C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo_arch.txt","archivo_completo.txt"))
"""
#9
"""
Realizá un programa que lea un archivo y obtenga la frecuencia de 
cada palabra que hay en el archivo. Recordá que la frecuencia es la 
relación entre número de veces que aparece 
la palabra en cuestión con respecto a la cantidad total de palabras.
"""
""""def frecuencia (archivo,palabra):
    contador=0
    with open (archivo,"r") as arch1:
        arch1_leido=arch1.read()
        arch1_leido_lista=re.split (" |\n",arch1_leido)
        len_arch1_leido_lista=len(arch1_leido_lista)
        for palabra_buscada in arch1_leido_lista:
            if palabra in palabra_buscada:
                contador+=1
    return ("La frecuencia de la palabra es", (contador*100)/len_arch1_leido_lista), contador
print (frecuencia("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt","ponelo"))
"""
#10
"""
    Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) 
    y los añada a un archivo dentro de la carpeta Resultado, 
    que a su vez se tiene que encontrar dentro de Carpeta1.
"""
""""import re
def carpeta_en_carpeta (archivo):
    os.chdir ("C:\\Users\\valen\\Ejercicios\\Ejercicios\\CArpeta1")
    archivos_txt=glob.glob(".txt*")
    for archivos_leidos in archivos_txt:
        with open (archivos_leidos,"r") as file:
            archivo_total=file.read()
            os.chdir ("C:\\Users\\valen\\Ejercicios\\Ejercicios\\CArpeta1\\Resultado")
            with open (archivo,"a") as arch:
                arch.write (archivo_total)
print (carpeta_en_carpeta("Archivo_ej_10.txt"))
"""
#POO parte 1

#1
"""
Su interfaz se compone de:
comer, acariciar, energía, está débil.
Su estado: self._alimento y self._caricias
"""

#2
""""class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self):
    return not self.energia<0 

pepita=Golondrina (0)

print (pepita.volar())"""

#3
""""
class Notebook:
    def __init__(self, su_marca,su_modelo,su_precio):
        self.marca=su_marca
        self.modelo=su_modelo
        self.precio=su_precio

    def descuento (self, porcentaje):
        return self.precio*(100-porcentaje)/100

laptop=Notebook("HP",2,2000)
print (laptop.precio)
print (laptop.descuento(10))"""

#4
#puede aumentar en uno o disminuir en uno
#resetear el valor y se pone en 0
#se puede indicar un numero que reemplaza el valor actual
""""class Contador:
    def __init__ (self,valor_inicial):
        self.contador=valor_inicial
        self.ultimoComando= None
    def inc(self):
        self.contador+=1
        self.ultimoComando="Incremento"
    
    def dis(self):
        self.contador-=1
        self.ultimoComando="Disminución"
    
    def reset (self):
        self.contador+=0
        self.ultimoComando="Reset"
    
    def valorActual(self):
        return self.contador

    def valorNuevo (self,nuevoValor):
        self.contador=nuevoValor
        self.ultimoComando="Valor nuevo"
        
    def ultimo_Comando(self):
        return self.ultimoComando
    
contador = Contador(10)
print (contador.valorActual())
print (contador.inc())
print (contador.valorActual())
print (contador.inc())
print (contador.valorActual())
print (contador.dis())
print (contador.valorActual())
print (contador.inc())
print (contador.valorActual())
print (contador.valorNuevo(27))
print (contador.valorActual())
print (contador.dis())
print (contador.dis())
print (contador.valorActual())
print (contador.ultimoComando,contador.valorActual())

"""
""""
class Calculadora:
    def __init__ (self):
        self.valor_inicial=0

    def sumar (self, numero):
        self.valor_inicial+=numero

    
    def restar (self, numero):
        self.valor_inicial-=numero
    
    def multiplicar (self, numero):
        self.valor_inicial=self.valor_inicial*numero
    
    def cargar (self, numero):
        self.valor_inicial==numero
    
    def valorActual(self):
        return self.valor_inicial
    
calculadora = Calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
print (calculadora.valorActual())"""

#intento 1
""""class Gorriones:
    def __init__ (self, su_CSS, su_CSSP, su_CSSV):
        self.CSS=su_CSS
        self.CSSP=su_CSSP
        self.CSSV=su_CSSV
        self.mayor_vuelo=None
        self.mayor_comida=None
        self.cantidad_de_vuelos=0
        self.cantidad_de_comidas=0

    def calculoCSS (self,km,gramos_comida):
        self.CSS=km/gramos_comida
        if ((km>self.mayor_vuelo)):
            self.mayor_vuelo==km
        if gramos_comida>self.mayor_comida:
            self.mayor_comida=gramos_comida
        if km>0:
            self.cantidad_de_vuelos+=1
        if gramos_comida>0:
            self.cantidad_de_comidas+=1
    def calculoCSSP (self,km,gramos_comida):
        if ((km>self.mayor_vuelo)):
            self.mayor_vuelo==km
        if gramos_comida>self.mayor_comida:
            self.mayor_comida=gramos_comida
        if km>0:
            self.cantidad_de_vuelos+=1
        if gramos_comida>0:
            self.cantidad_de_comidas+=1
        self.CSSP=km/gramos_comida

    def calculoCSSV (self,km,gramos_comida):
        if (km>self.mayor_vuelo):
            self.mayor_vuelo==km
        if gramos_comida>self.mayor_comida:
            self.mayor_comida=gramos_comida
        if km>0:
            self.cantidad_de_vuelos+=1
        if gramos_comida>0:
            self.cantidad_de_comidas+=1
        selfCSSV=self.cantidad_de_vuelos/self.cantidad_de_comidas
gorreon=Gorriones(0,0,0)
print (gorreon.calculoCSS(10,2))
"""
#intento 2
""""class Gorreones:
    def __init__ (self):
        self.CSS=0
        self.CSSP=0
        self.CSSV=0
        self.mayor_vuelo=0
        self.mayor_comida=0
        self.cantidad_de_vuelos=0
        self.cantidad_de_comidas=0

    def volar (self):
        self.cantidad_de_vuelos+=1

    def comer (self):
        self.cantidad_de_comidas+=1
    
    def calculoCSS (self,km,gramos_comida):
        self.CSS=km/gramos_comida
        if km>0:
            self.volar()
        if gramos_comida>0:
            self.comer()
        if (km>self.mayor_vuelo):
            self.mayor_vuelo==km
        if gramos_comida>self.mayor_comida:
            self.mayor_comida=gramos_comida
    def calculoCSSP (self,km,gramos_comida):
        if km>0:
            self.volar()
        if gramos_comida>0:
            self.comer()
        if (km>self.mayor_vuelo):
            self.mayor_vuelo==km
        if gramos_comida>self.mayor_comida:
            self.mayor_comida=gramos_comida
        try:
            self.CSSP=self.mayor_vuelo/self.mayor_comida
        except ZeroDivisionError:
            print ("None")
    def calculoCSSV (self,km,gramos_comida):
        if km>0:
            self.volar()
        if gramos_comida>0:
            self.comer()
        if (km>self.mayor_vuelo):
            self.mayor_vuelo==km
        if gramos_comida>self.mayor_comida:
            self.mayor_comida=gramos_comida
        try:
            self.CSSV=self.cantidad_de_vuelos/self.cantidad_de_comidas
        except ZeroDivisionError:
            print ("None")"""
#intento 3           
""""class Gorreones:
    def __init__(self):
        self.mayor_vuelo = 0
        self.mayor_comida = 0
        self.cantidad_de_vuelos = 0
        self.cantidad_de_comidas = 0

    def volar(self, km):
        self.cantidad_de_vuelos += 1
        if km > self.mayor_vuelo:
            self.mayor_vuelo = km

    def comer(self, gramos):
        self.cantidad_de_comidas += 1
        if gramos > self.mayor_comida:
            self.mayor_comida = gramos

    def calculoCSS(self, km, gramos):
        if km > 0 and gramos > 0:
            self.CSS = km / gramos

        self.volar(km)
        self.comer(gramos)

    def calculoCSSP(self, km, gramos):
        if self.mayor_vuelo == 0 or self.mayor_comida == 0:
            self.CSSP = None
        else:
            self.CSSP = self.mayor_vuelo / self.mayor_comida

        self.volar(km)
        self.comer(gramos)

    def calculoCSSV(self, km, gramos):
        if self.cantidad_de_comidas == 0:
            self.CSSV = None
        else:
            self.CSSV = self.cantidad_de_vuelos / self.cantidad_de_comidas

        self.volar(km)
        self.comer(gramos)

gorreon=Gorreones()
print (gorreon.calculoCSS(10,3))
print (gorreon.CSS)
print (gorreon.calculoCSSP(10,3))
print (gorreon.CSSP)
print (gorreon.calculoCSSV(10,3))
print (gorreon.CSSV)
"""
#POO parte 2
#1

""""Sus estados son self.caricias y self.alimento
La interfaz del perro es: energía, comer,alimento,acariciar,estaDebil,pasear.
La del gato es: energia, comer, caricias , acariciar, estaDebil.
Los objetovs comparten parte de su interfaz. Los mensajes energía, comer, acariciar,estaDebil
"""
""""#2   
class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self):
    return not self.energia<0 
  
  def equilibrio (self):
    return (self.energia<300 and self.energia>150)

pepita=Golondrina (0)


pepita.comer_alpiste(70)
print (pepita.equilibrio())
"""
#3
#hacerla comer 80 gramos, hacerla volar 70 kms, y finalmente hacerla comer otros 10 gramos
"""
Consideremos que un ornitólogo tiene un conjunto de aves bajo estudio. Cada una de 
estas aves puede ser un gorrión (del ejercicio 7 de la práctica anterior), o una golondrina. 
Un ornitólogo somete, cada vez que lo decide, a cada una de las aves que tiene en estudio a 
una rutina que consiste en: hacerla 
comer 80 gramos, hacerla volar 70 kms, y finalmente hacerla comer otros 10 gramos. 

Se propone: implementar la clase Ornitologo, de forma tal que acepte las operaciones 
estudiarAve(ave), avesEnEstudio(), realizarRutinaSobreAves(), avesEnEquilibrio(). 
Realizar rutina es ejecutar la rutina descripta más arriba sobre cada ave que tiene en 
estudio. Las aves en equilibrio son aquellas aves, entre las que el ornitólogo tiene 
en estudio, que responden True cuando se les consulta estaEnEquilibrio().
"""

"""
set={pepita,gorre}
frank=Ornitologo(set)
print frank.realizarRutina (set{pepita})
"""

class Ornitologo:
    def __init__ (self):
        self.aves=[]
    #agrego aves para estudiar
    def estudiar_ave (self, ave):
        self.aves.append (ave)
    #lista de aves
    def aves_en_estudio(self):
        return self.aves
    #se da el polimorfismo, defino un metodo que llama a un metodo que tienen las clases de Golondrina y Gorreones
    def aves_en_equilibrio(self):
        return [self.aves[i].esta_en_equilibrio() for i in range (len(self.aves))]
        #lista de booleanos que devuelve por cada aves si esta o no en equilibrio
        #otra forma
        for ave in self.aves:
            ave.esta_en_equilibrio()

    def realizar_rutina (self):
        [self.aves[i].comer(80) for i in range (len(self.aves))]
        [self.aves[i].volar(70) for i in range (len(self.aves))]
        [self.aves[i].comer(10) for i in range (len(self.aves))]


class Gorriones:
    def __init__(self):
        self.kilometros = [] 
        self.gramos = []

    def volar(self, km):
        self.kilometros.append(km)

    def comer(self, gramos):
        self.gramos.append(gramos)

    def css(self):
        if not self.gramos == []: # if len(self.gramos) > 0: 
            return sum(self.kilometros) / sum(self.gramos) #suma los valores de la lista SOLO si son valores numericos
                                                       # si hay strings rompe
        else:
            return None

    def cssp(self):
        if not self.gramos == []:
            return max(self.kilometro) / max(self.gramos)
        else:
            return None

    def cssv(self):
        if not self.gramos == []:
            return len(self.kilometro) / len(self.gramos)
        else:
            return None
        
    def esta_en_equilibrio(self):
        return  0.5 <= self.css() <= 2 #en lugar de usar un if

class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self):
    return not self.energia<0 
  
  def equilibrio (self):
    return (self.energia<300 and self.energia>150)
#EJERCICIO 4
""""class MedioDeTransporte:
    def __init__ (self,su_combustible):
        self.combustible=su_combustible

    def cargar_combustible(self,litros):
        self.combustible+=litros
        return self.combustible
class Moto(MedioDeTransporte):
    def __init__ (self):
        super().__init__(su_combustible=0)
        self.capacidad=2

    def recorrer (self,km):
        self.combustible-=km
    
    def entran_personas (self,cantidad_de_personas):
        return (self.capacidad>=cantidad_de_personas)

class Auto(MedioDeTransporte):
    def __init__ (self):
        super().__init__(su_combustible=0)
        self.capacidad=5

    def recorrer (self,km):
        self.combustible-=km/2

    def entran_personas (self,cantidad_de_personas):
        return (self.capacidad>=cantidad_de_personas)
    
motocicleta=Moto()
autito=Auto()
print (motocicleta.combustible)
print (motocicleta.cargar_combustible(20))
print (autito.cargar_combustible(20))"""


#EJERCICIO MUMUKI
""""class Chef:
  def __init__ (self,plato_del_dia):
    self.plato=plato_del_dia
  def picantear (self):
    if self.plato.demasiado_picante():
        raise Exception ("El plato ya está demasiado picante")
    else:    
      self.plato.picantear()
        
class AyudanteDeCocina:  
  def suavizar (self,plato):
    plato.suavizar()
    
class Pasta:
  def __init__ (self):
    self.ajies=0
   
  def demasiado_picante (self):
    return self.ajies>10
  
  def picantear (self):
    self.ajies+=5
  def suavizar (self):
    self.ajies -=1
    
class Pizza:
  def __init__ (self):
    self.condimento="adobo"
    
  def demasiado_picante (self):
    if self.condimento=="cayena":
      return True
    
  def picantear (self):
    self.condimento="cayena"
  def suavizar (self):
    self.condimento="oregano"
fideos = Pasta()
muzzarella = Pizza()
jor = Chef(fideos)
luchi = AyudanteDeCocina()
print (jor.picantear())
print (luchi.suavizar(fideos))
jor.plato_del_dia = muzzarella
print (luchi.suavizar(muzzarella))
print (jor.picantear())"""

#EJERCICIOS MODELO POO
""""En un mundo distópico la humanidad es atacada sin descanso por titanes. 
Estos titanes son muy resistentes pero no inmortales, su salud (100 de máxima) 
puede ir disminuyendo si reciben daño debido a algún ataque, y si llega a 0 se muere. 
Al recibir este ataque la salud disminuye 1.5 por cada puntos de daño recibido. 
Además tienen la capacidad de destruir cierto número de casas dependiendo de su salud, 
siendo 8 casas cuando su salud es máxima o un número proporcional si su salud es menor a la máxima 
(si tiene 60 puntos de salud destruiría 4.8 casas, es decir, 4 casas completas y más de la mitad de otra). 
Sin embargo no tienen la capacidad de comunicarse con los humanos, siendo un grito, "¡Aaaarrrg!", 
el único sonido que hacen. Definí la clase Titan con los atributos y métodos correspondientes. 
Además instanciá a un Titan y ejecutá las siguientes líneas:"""
#salud de 100
#disminuye salud si recibe_daño (1.5 por daño). Si lelga a 0 (método morir)
#destruir casas segun sus salud.
""""class Titan:
    def __init__ (self,su_salud):
        self.salud=su_salud

    def recibir_ataque (self, ataque):
        self.salud-=ataque*1.5
    def esta_vivo (self):
        return self.salud>0
    def salud_actual (self):
        return self.salud
    def cuantas_casas (self):
        cuantas_casas=(self.salud*8)/100 #100 es su salud maxima
        return cuantas_casas
    def destruir_casas (self):
        if self.cuantascasas>1:
            return (self.salud*8)// 100
        else:
            print ("No tengo salud suficientes")
    def grito (self):
        return ("¡Aaaarrrg!")
     
titan1 = Titan(100)
titan1.recibir_ataque(30)
print(titan1.esta_vivo())
print(titan1.salud_actual())
print(titan1.cuantas_casas())
print(titan1.grito())
print (titan1.destruir_casas())
titan1.salud_actual()
titan1.recibir_ataque(4)
print(titan1.esta_vivo())"""

""""
Los estudiantes (como ustedes) son como cualquier persona, las cuales recuperan energía si 
duermen o si comen, o la gastan al hacer ejercicio, 
sin embargo en particular los estudiantes también gastan energía al estudiar y 
se sienten felices al aprobar algún exámen. Resumiendo, las personan pueden:
-Decirnos cuánta energía tienen.
-Recuperar el máximo de energía (100) al dormir 8 horas, o el proporcional si duermen menos 
(si duermen 4 ganan la mitad de energía, es decir 50).
-Recuperar energía al comer, ganando de esta manera 10 puntos.
-Gastar energía al hacer ejercicio, siendo un gasto de 25 puntos por cada media hora de ejercicio.
-Como estado de ánimo pueden estar felices o no, pero por defecto no están felices.

Además los estudiantes tienen el siguiente comportamiento:
Al estudiar su energía disminuye 20 puntos por cada hora de estudio.
Si aprueban su estado de ánimo pasa a ser "Feliz".
Definí las clases Persona y Estudiante con los atributos y métodos correspondientes
 y hacé que esta última herede de la primera. Además instanciá a un Estudiante y ejecutá las siguientes líneas:
"""

""""class Estudiante:
    def __init__ (self, su_energia):
        self.energia=su_energia
        
    def dormir (self,cantidad_de_horas):
        energia_al_dormir=(cantidad_de_horas*100)/8
        return self.energia*(1+energia_al_dormir)
    def energia_actual (self):
        return self.energia
    def comer (self):
        self.energia+=10
    def hacer_ejercicio (self,tiempo):
        cantidad_de_energia=(tiempo/30)*25
        self.energia-=cantidad_de_energia
    
    def estudiar (self,tiempo):
        horas_de_estudio=tiempo*20
        self.energia -=horas_de_estudio
    
        
    def estan_felices (self):
        return False
    def aprobar (self):
        return not self.estan_felices()

estudiante = Estudiante(100)
estudiante.hacer_ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobar())
print(estudiante.energia_actual())"""

""""
Se está pensando en el diseño de un juego que incluye la nave espacial Enterprise. 
En el juego, esta nave tiene un nivel de potencia de 0 a 100, y un nivel de coraza de 0 a 20. 

La Enterprise puede:
encontrarse con una pila atómica, en cuyo caso su potencia aumenta en 25.
encontrarse con un escudo, en cuyo caso su nivel de coraza aumenta en 10.
recibir un ataque, en este caso se especifican los puntos de fuerza del
ataque recibido. La Enterprise "detiene" el ataque con la coraza, y si 
la coraza no alcanza, el resto se descuenta de la potencia. Por ejemplo 
si la Enterprise con 80 de potencia y 12 de coraza recibe un ataque de 
20 puntos de fuerza, puede parar solamente 12 con la coraza, los otros 
8 se descuentan de la potencia. La nave debe quedar con 72 de potencia y 
0 de coraza. Si la Enterprise no tiene nada de coraza al momento de recibir el ataque, 
entonces todos los puntos de fuerza del ataque se descuentan de la potencia.
La potencia y la coraza tienen que mantenerse en los rangos indicados, 
por ejemplo, si la Enterprise tien 16 puntos de coraza y se encuentra con un escudo, 
entonces queda en 20 puntos de coraza, no en 26. Tampoco puede quedar negativa la potencia, 
a lo sumo queda en 0. La Enterprise nace con 50 de potencia y 5 de coraza. Implementar este modelo de la 
Enterprise, que tiene que entender los siguientes mensajes:

potencia()
coraza()
encontrarPilaAtomica()
encontrarEscudo()
recibirAtaque(puntos)

Al ejecutar esto:

enterprise = Enterprise()
enterprise.encontrarPilaAtomica()
enterprise.recibirAtaque(14)
enterprise.encontrarEscudo()
la potencia de la Enterprise debe ser 66, y su coraza debe ser 10.

Agregar al modelo de la Enterprise, la capacidad de entender estos mensajes.

fortalezaDefensiva(), que es el máximo nivel de ataque que puede resistir, o sea, coraza más potencia.
necesitaFortalecerse(), tiene que ser true si su coraza es 0 y su potencia es menos de 20.
fortalezaOfensiva(), que corresponde a cuántos puntos de fuerza tendría un
ataque de la Enterprise. Se calcula así: si tiene menos de 20 puntos de potencia entonces
es 0, si no es (puntos de potencia - 20) / 2.

"""

class Enterprise:
    def __init__ (self):
        self.potencia=50
        self.coraza=5

    def encontrarPilaAtomica(self):
        if self.potencia+25<=100:
            self.potencia+=25
        else:
            self.potencia=100

    def encontrarEscudo(self):
        if self.coraza+10<=20:
            self.coraza+=10
        else:
            self.coraza=20
    def recibirAtaque (self,puntos):
        if puntos<self.coraza:
            self.coraza-puntos
        else:
            self.potencia -= puntos - self.coraza
            self.coraza = 0
    def fortalezaDefensiva(self):
        return (self.coraza+self.potencia)
    
    def necesitaFortalecerse(self):
        return self.coraza==0 and self.potencia>20
    def fortalezaOfensiva(self):
        if self.potencia>20:
            return 0
        else:
            return (self.potencia - 20) / 2
enterprise = Enterprise()
enterprise.encontrarPilaAtomica()
enterprise.recibirAtaque(14)
enterprise.encontrarEscudo()
print (enterprise.potencia)
print (enterprise.coraza)