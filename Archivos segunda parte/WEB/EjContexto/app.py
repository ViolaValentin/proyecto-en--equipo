from flask import Flask,render_template
from markupsafe import escape

app=Flask(__name__)
@app.get ("/")
def home ():
    return render_template ("home.html")

@app.get ("/resultados")
def resultados ():
    return render_template ("resultados.html")

@app.get ("/plan-2023")
def plan_2023 ():
    return render_template ("plan-2023.html")