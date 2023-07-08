from flask import Flask, render_template
from markupsafe import escape

app=Flask(__name__)

productos={
    1:{"name":"Shampoo sólido","Stock":5,"Precio":300},
    2:{"name":"Crema de manos","Stock":6,"Precio":600}
}

@app.get("/")
def home ():
    return render_template ("home.html")

@app.get ("/libreria")
def get_libreria ():
    return render_template ("libreria.html")

@app.get ("/libros")
def get_all_libros():
    return render_template ("libros.html", productos=productos.items())

@app.get ("/libros/<int:id>")
def get_libro(id):
    if id in productos:
        producto=productos[id]
        return render_template ("libro.html", id=id, producto=producto)
    else:
        return ("No hay de ese producto", 404)