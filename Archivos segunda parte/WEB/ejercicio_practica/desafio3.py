import requests

respuesta=requests.get ("https://pokeapi.co/api/v2/pokemon/")
print (respuesta.headers)
"""print (respuesta.content)
print (respuesta.headers["Content-Type"])"""
