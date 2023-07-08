from flask import Flask, render_template
from markupsafe import escape

app=Flask(__name__)
libros = {
    100: {"Shampoo sólido":	5,	"precio":300},
    150: {"Crema de manos":	6,	"precio":600}
}
@app.get("/")
def home():
    return render_template ("home.html")

@app.get ("/libros")
def get_all_libros():
    return render_template ("libros.html")

@app.get("/libros/<int:id>")
def get_prenda(id):
    if id in libros:
        libro = libros[id]
        return f"<p>Mostrando la prenda {escape(libro)}</p>"
    else:   
        return ("no hay prenda", 404)


from flask import Flask, render_template, request, redirect, url_for

@app.route('/libros', methods=('GET', 'POST'))
def create_libro():
    if request.method == 'POST':
        return redirect(url_for('success'))
    else:
      return render_template('new_libros.html')
    
