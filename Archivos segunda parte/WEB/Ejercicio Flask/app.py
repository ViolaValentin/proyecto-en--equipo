#llamarlo app.py hace que sea más fácil que Flask detecte el archivo


from flask import Flask, render_template
from markupsafe import escape #verifica que {id} sea un string y no un código JS.

prendas=[
    {"id":1,"tipo":"pantalon","talle":43},{"id":2,"tipo":"pantalon","talle":42} ]
app= Flask(__name__) #le digo a Flask que me refiero a la aplicaicón con la palabra "app"


#lo que arranca con @ son decoradores, se ubican encima de las funciones y determinan las rutas y métodos HTTP.
@app.get("/") #cuando alguien pegue al /, se va a dissparar la siguiente acción
def home():
    return render_template("home.html")
#armar la ruta/prendas que muestre todos los items de prendas
@app.get("/prendas")
def get_todas_las_prendas():    
    return f"<p>Mostrando todas las prendas</p>"
#/prendas debería soportar verbos como get, post
#/prendas/id debería soportar:
#Get: traigo una sola prenda de id
#Patch: modifico esa prenda

#Cuando corro flask, me devuelve ":5000", quiere decir que la aplicación está escuchando en el puerto 5000
#Un recurso es un registro que queda en mi base de datos

@app.get("/prendas/<id>") #<id> asume que le podemos enviar cualquier ID, y lo hago una sola ves para todas las prendas
def get_prenda(id):
    return f"<p>Mostrando la prenda {escape(id)}</p>"