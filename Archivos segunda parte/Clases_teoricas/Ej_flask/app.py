from flask import Flask, render_template
from markupsafe import escape #verifica que {id} sea un string y no un código JS.
@app.get("/") #cuando alguien pegue al /, se va a dissparar la siguiente acción
def home():
    return render_template("home.html")