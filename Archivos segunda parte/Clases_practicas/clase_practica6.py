import re

def entre_x_y_ab (string):
    patron="X([^XY]*ab[^XY]*)Y"
    return re.findall (patron,string)
#X([^XY]*ab[^XY]*)Y
#X(.ss*?ab.*?)Y
#[^X]*ab[^Y]*
print (entre_x_y_ab("XbaaaYjXababYqXbabbbaaYqXffee"))

""""#
a)Falso. Las palabras tiene que estar separadas por (_) y todas las palabras en minúscula. También, se puede escribr 
la primera palabra en minúscula y todas las demás empiezan por mayúscula sin (_)
La función no tiene un nombre descriptivo
b)La función lanza NameError... La función lanza AtributeError, que indica que no existe un atributo llamado findal, el atributo correcto es findall
c)La función lanza NameError... La función lanza AtributeError, que indica que no existe un atributo llamado findal, el atributo correcto es findall
d)Una vez corregida...["gaaa"]... [x] Este patrón, si puede encontrarse en el string enviado.
e) Una vez corregida... ["24gra"]...No devuelve esta búsqueda
"""
#Corregida

def entre_ag_cta_sin_numeros (string):
    return re.findall ("ag([^\d]*)cta",string)

print (entre_ag_cta_sin_numeros  ("aabocaggaaactazu4lggaasag24gra1ndecta"))


# EJERCICIO 2
import glob,sys,os
def filtrar (archivo):
    lista_txt=glob.glob("*.txt")
    with open (archivo, "a") as arch: #abro el archivo que va a funcionar como base de datos
        for archivo in lista_txt:
            with open (archivo, "r") as archivo_secreto:
                texto=archivo_secreto.read()
                lista=re.findall (r"[\w]+[-_\.]*[\w]+@gmail.com",texto)
                for email in lista:
                    arch.write (email + "\n")

print (filtrar("base_datos.txt"))
#Preguntar si está bien hacer el ejercicio solo para 2 archivos
#EJERCICIO 4
"""
Gana el doble de puntos por cada bolita
Comefantasma y gana: Rosa 8, Verde 6, Naranja 4, Rojo 2
Velocidad=(2 + cantidad de puntos) /100
Perder vida: contador -1 y se le resetean los puntos
- 3 vidas devuelve Game Over
"""

class PacMan:
    def __init__(self):
        self.vidas=3
        self.puntos=0

    def comer_bolitas (self,cantidad):
        self.puntos+=(cantidad*2)

    def velocidad (self):
        return 2+self.puntos/2
    
    def perderVida (self):
        self.puntos=0
        self.vidas-=1
        if self.vidas ==0:
            print ("Game Over")

    def comerFantasma(self,fantasma):
        if fantasma == "rosa":
            self.puntos+=8
        if fantasma == "verde":
            self.puntos+=6
        if fantasma == "naranja":
            self.puntos+=4
        if fantasma == "rojo":
            self.puntos+=2

pacman=PacMan ()
print (pacman.puntos)
pacman.comer_bolitas(10)
print (pacman.puntos)
pacman.comerFantasma("Rojo")
print (pacman.puntos)
pacman.comerFantasma("Verde")
print (pacman.puntos)


#b
class PacManmejorado (PacMan):
    def vida_extra (self):
        if self.puntos >=200:
            self.vidas +=1
            self.puntos -=200

        else:
            print ("Faltan",200-self.puntos, "puntos para ganar una vida extra")

    def velocidad(self):
        return 3+self.puntos/100
    

#EJERCICIO 5
""""Consigna N*5

En el equipo de trabajo de Onomatopopih tienen un repositorio compartido para resolver el tp final de la materia de
Fundamentos de Informática. Topa hizo un commit inicial con un README con los nombres de los miembros del equipo.
Ahora Onomatopopih quiere descargar los cambios para hacer su aporte.

A) Marcá con una [X] la/s opciones correcta/s y justifica tu elec
Onomatopopih debe hacer push en la terminal

1) Onomatopopih debe hacer pull en la terminal | El comando es git pull. En el punto 3, se indica s funcionamiento.

2) Onomatopopih debe hacer git push en la terminal [x] | Este es el último paso que Onomatopopih debe llevar a cabo. Subirá todos los cambios que haya realizado en el proyecto a la Web.

3) Onomatopopih debe hacer git pull en la terminal [x] | Este comando le va a permitir a Onomatopopih descargar 
la última versión actualizada del proyecto en su 
escritorio local. Lugo, podrá comenzar a hacer los cambios.

4)Onomatopopih después de agregar su aporte debe escribir en una terminal git add y luego git commit [x] | Correcto, git add es un comando que 
avisará a git que nuestro código está listo para ser capturado. Git commit, el comando que le sigue, captura el código y recolecta toda la meta-data 
de los cambios y quiénes los realizó para subir toda esta información a githib.

5) Onomatopopih después de agregar su aporte debe escribir en una terminal git add . luego git commit -m 'mis
aportes" y finalmente git push [x] | Esta opción también es correcta, ordena todas las opcones anteriores y detalla
cosas como el mensaje que git commit debe tener y que el comando git add necesita de un espacio y el (.).
#git clone vuelve a bajar el repositorio, crea una carpeta nueva y esto puede generar conflictos
Al tiempo, Onomatopopih descubrió que sus compañeros actualizaron elrepositorio. Marcá con una [X] la/s opcion/es
correctas y justifica tu elección:

+ Onomatopopih debe hacer git push en la terminal | Este comando resultaría útil luego de que Onomatopopih haya descargado la útlima
versión actualizada y haya hecho cambios.

+ Onomatopopih debe hacer git pull enla terminal [x] | Correcto, Onomatopopih debe descargar la versión más reciente del proyecto
para ponerse a trabajar.

+ Onomatopopih debe hacer git clone git0github.com:Fundamentos/onomatopopih.git en la terminal | Este comando se utiliza par
clonar un proyecto en caso de que nunca antes hayamos trabajado con él.

"""

            
