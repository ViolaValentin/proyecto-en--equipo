#Espresiones regulares
"""
Comando en Git Bash para ver archivos ocultos: ls -la
Archivo .gitignore : Contiene todos los nombres de archivo/carpetas que quiero ignorar
Los archivos que empiezan con punto (.) se ocultan 

Las expresiones regulares sirven para hacer búsquedas de texto. La idea es escribir lo que quiero y encontrarlo a través de diversas fuentes.
"""
"""
🧗‍♀️ Desafío I: ¿Construí la expresión regular que obtenga al menos 4 dígitos?

🧗‍♀️ Desafío II: ¿Construí la expresión regular que obtenga al entre 3 y 6 letras minúsculas?

🧗‍♀️ Desafío III: ¿Construí la expresión regular que obtenga todas las apariciones del patrón ab en un string?
"""
#1
"\d{4, }"
#2
"[a-z]{3,6}"
#3
"ab*x"
""""
import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"

print (re.search (patron,texto))
print (texto[12:17])
print (re.match (patron,texto))

"""
""""re.search() busca en cualquier parte del texto la primera aparición
re.match () solo busca al principio"""
"""
#findall devuelve lista
print (re.findall (patron,texto))
#por ejemplo, extraer todos los mails que tienen @yahoo y reemplzarlos por @gmail (ejercicio de parcial)

patron1 = "^a[a-z]{3-6}"    #epieza con a y busca palabras de a-z de entre 3-6 palabras

#metodo group, agrupa el string del resultado del patron
print (re.search (patron,texto).group())
"""
import re
texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*)sit"     #buscar todos aquellos caracteres entre las palabras ipsum y sit
print (re.search(patron, texto))
'ipsum dolor sit amet, consectetur ipsum elit. Amet sit'
print (re.search(patron, texto).group(0)) #es lo mismo que haber hecho un group pero incluye lo que estoy buscando
'ipsum dolor sit amet, consectetur ipsum elit. Amet sit'
print (re.search(patron, texto).group(1)) # muestra el resultado de la búsqueda pero no incluye lo que busqué
'ipsum dolor sit amet, consectetur ipsum elit. Amet sit'

#La función sub permite reemplazar todos las ocurrencias del patrón por otro patrón en un String.
print (re.sub(patron, "###", texto))



