""""#https://pokeapi.co/api/v2/pokemon/pikachu
#El dominio es pokeapi.co
import requests
respuesta=requests.get ("https://pokeapi.co/api/v2/pokemon/pikachu")

#2
print (respuesta.status_code)
print (respuesta.headers["Content-Type"])
datos=respuesta.json()
print (datos["forms"])

#3

rta=requests.get("https://pokeapi.co/api/v2/pokemon/")
rtas=rta.json()
print(len(rtas["results"]))
print (rtas["count"]) # me indica la cantidad de campos poruqe al hacerlo a través del result, tengo un límute de 20 campos

#4
#https://pokeapi.co/api/v2/pokemon/abilities
#https://pokeapi.co/api/v2/pokemon/ability/2

datos_pikachu=requests.get ("https://pokeapi.co/api/v2/pokemon/pikachu/")
datos_sylveon=requests.get ("https://pokeapi.co/api/v2/pokemon/sylveon/")

rta_datos_pikachu=datos_pikachu.json()
rta_datos_sylveon=datos_sylveon.json()

with open ("ficha_tecnica_pokemon.txt","wb") as arch:
    arch.write (rta_datos_pikachu.content)
    arch.write (rta_datos_sylveon.content)
"""

#https://jsonplaceholder.typicode.com/todos
#El dominio es jsonplaceholder.typicode.com


