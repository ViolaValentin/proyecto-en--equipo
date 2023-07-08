from flask import Flask, render_template
from markupsafe import escape

app=Flask(__name__)
@app.get ("/")
def home():
    return render_template ("home.html") 

@app.get ("/servicios/")
def get_servicios():
    return render_template ("servicios.html") 

@app.get ("/quienes-somos/")
def get_quienes_somos():
    return render_template ("quienes-somos.html") 

@app.get ("/contacto/")
def get_contacto():
    return render_template ("contacto.html") 