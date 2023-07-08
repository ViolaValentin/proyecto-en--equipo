import requests
#https://pokeapi.co/api/v2/pokemon/pikachu
#1) El dominio es pokeapi.co
#2)
respuesta=requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
print (respuesta.status_code)
#Devuelve el status code 200
print (respuesta.headers["Content-Type"])
#Es de tipo json
datos=respuesta.json()
print (datos["forms"])
print (datos.keys())

#3)
pokemons=requests.get("https://pokeapi.co/api/v2/pokemon/")
datos_pokemons=pokemons.json()
print (len(datos_pokemons["results"]))
print (datos_pokemons["count"])

#4) https://pokeapi.co/api/v2/pokemon/abilities
#https://pokeapi.co/api/v2/pokemon/abilities/2

#5) 
pikachu=requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
datos_pikachu=pikachu.json()
sylveon=requests.get("https://pokeapi.co/api/v2/pokemon/sylveon")
datos_sylveon=sylveon.json()

with open ("ficha_tecnica.txt","a") as arch:
    arch.write (datos_sylveon), arch.write(datos_pikachu)
#6) La estrucutra cliente-servidor refiere a la interacción esntre estas partes. El cliente, somos nosotros, quienes hacemos los
#pedidos, el servidor en este caso es pokeapi, la api a la que le solicitamos información de su base de datos de pokemons.
#el intermediario es el protocolo https.

import requests

#https://jsonplaceholder.typicode.com/todos
#1)Estamos consultando el dominio jsonplaceholder.typicode.com
respuesta=requests.get("https://jsonplaceholder.typicode.com/todos")
print (respuesta.status_code)
print(respuesta.headers["Content-Type"])

datos_a_agregar={
    "userid":11,
    "id":2,
    "completed":True,
    "title":"Este es su nuevo titulo",
}
respuesta=requests.post("https://jsonplaceholder.typicode.com/todos", json=datos_a_agregar)