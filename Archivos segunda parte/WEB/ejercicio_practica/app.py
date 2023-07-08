from flask import Flask, render_template
from markupsafe import escape


productos={
    1:{"name":"Shampoo sólido","stock":5,"precio":300},
    2:{"name":"Crema de manos","stock":6,"precio":600}
    		
		
}
app=Flask(__name__)
@app.get ("/")
def home():
    return render_template ("home.html") 
@app.get ("/productos")
def get_all_products ():
    return render_template("productos.html", productos=productos.items())

@app.get("/productos/<int:id>")
def get_producto(id):
    if id in productos:
        producto = productos[id]
        return render_template('producto.html', id=id, producto=producto)
    else:
        return ("no hay producto", 404)