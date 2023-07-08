import requests

respuesta=requests.get ("https://pokeapi.co/api/v2/pokemon/ditto")
"""
1-describir las partes de la URL
2-¿Qué respuesta obtenés al hacer get
3-¿Cuál es el content type de esa respuesta?
4-¿Cuál es el status code de la respuesta?
5-¿Cuantas habilidades tiene este pokemon?
"""
"""https://pokeapi.co/api/v2/pokemon/ditto
Protocolo - dominio - recursos"""
#Para que una API sea rest, las URL tienen que mapear rescursos. Los recursos es lo que almaceno en la base de datos
#Dominio: es el nombre a través del que mapeo una IP en particular

datos=respuesta.json()
#2
print (datos.keys())
#me da por respuesta todos los contenidos asociados al recurso ditto con los detalles de habilidades, nombre, movimientos,etc
#3
print (respuesta.headers["Content-Type"])
#otros tipos de datps que puede traer un requests es html, json. Solo soporta datos de tipo texto (esto es debido al protocolo).
#4
print (respuesta.status_code)
#5
print (len(datos["abilities"]))
""""
La diferencia entre path y url es que la URL funciona buscando un recurso al que accedo a través de Internet. 
En el pathaccedo a un recurso que se encuentra en una máquina."""

rta=requests.get("https://pokeapi.co/api/v2/ability/150/")
print(rta.json())

"""
https://dominio/recurso/ #todos los items asociados a ese recurso
https://dominio/recurso/id #id son los paramtetros. Indico a qué item del recurso ingreso
"""

#Acceder a un recurso a través de un tipo en vez de un ID. Busco todos los items que conte
"""
https://dominio/recurso?tipo=pantalon #el ?tipo=pantalon son los query params. Son la forma en la cual le paso a la API a través de la URL para filtrar la busqueda en su base de datos
- el ? indica buscar
- =pantalon indica el valor
- puedo concatenar filtrados con el &. Por ejemplo https://dominio/recurso?talle=40&?tipo=pantalon
"""
"""
Cada URL tiene ciertos verbos asociados, depende de la URL los verbos que voy a poder usar
- recurso/id me muestre el item en particular
- recurso/post o patch modificar una parte del item. Post escribe datos de 0, patch reescribe. Cuando hago alguno de estos dos, también tengo que pasarle los datos al servidor.
- recurso/delete borar ese item
- recurso/put modifica todo el item
- para crear un item, hago el post sobre /recurso/
A cada pedido http tengo que pasarle metadata
"""

#Despliegue: hacemos disponible nuestra aplicación a la Web
#Biblioteca Flask: se utiliza para generar aplicaciones. Existen frameworks, bibliotecas con más utilidades que hacen más 
#sencillo la construcción de aplicaciones

"""
Las API tienen rutas  (endpoints) que son las URLs en las cuales se accede a los recursos.


"""