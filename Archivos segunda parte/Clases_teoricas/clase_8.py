#Internet: no es abstracto. Es una conexión física entre todas las máquinas desde 
#distintas partes del mundo.
#Web: conjunto de páginas Web a parti de las cuales se intercambia información.

# A través de Internet y Werb compartimos otras cosas como Hardware.

#Arquitectura Web. Arquitectura cliente-servidor. Los clientes para la Web son las máquinas, los servidores también lo son.
"""
El servidor aporta algo, contenido, datos. Jamás hace pedidos la cliente.
El cliente es el que lo consume.
Las características que posea el servidor es relativa al uso que se le de,la demanda que tenga. 
No necesariamenteexiste una diferencia en su hardaware o software.
Utilizo la misma tecnología, tal vez cambie su lógica.

En la arquitectura cliente servidor, el servidor es la parte que aporta contenido, información, datos. El cliente,
es quien lo consume. Las características que posea un servidor son relativas al uso que se le de al mismo, a la 
demanda que tenga. También, debemos considerar que no necesariamente existe una diferencia en su hardaware o software
pero si en su lógica.
En este caso, el servidor aporta la información de las promociones que solicita el cliente al hacer clic en los botones.


Lenguaje de programación: me permiten operar contra el hardware
Protocolos de comunicación: actúa como intermediario entre el cliente y el servidor.

El navegador: es un programa(software) que le sirve al cliente para 
renderizar y visualizar los datos que le envía el servidor.
"""

"""
Webs y aplicaciones Web

App Web persisten información (se asocian a una en base de datos dónde la almacenan)
Una página Web no almacena información. Es un archivo expuesto en la nube. Son muchos archivos html interconectados.
Aplicaciones rest: cada recurso se corresponde con un URL particular. Están organizadas por recursos.
Con recurso nos referimos a un tipo de item de la base de datos.

"""

import requests

#requests nos permite hacer pedidos http
respuesta= requests.get ("https://api.github.com/users/ajanavelezrueda/orgs") #get el el verbo http asociado a las consultas. Consulta al servidor.
#Luego de esto, el servidor dispara una acción particular.
datos=respuesta.json() #el formato json es una estructura de datos 

#en cuantas orgs está involucrado el usuario
print (len (datos)) #es una lista con diccionarios adentro

#lista de mombres de las orgs en las que está involucrado
for i in datos:
    print (i[0:])
#en el header encuentro toda la información asociada a los requests

print (respuesta)
print (respuesta.headers)
print (respuesta.status_code)
#Verbos
"""
.post - verbo http asociado a escribir o persistir datos (desde cero)
.delete - verbo http asociado a borrar datos
.patch - verbo http asociado a reescribir datos
"""