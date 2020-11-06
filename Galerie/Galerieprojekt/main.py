from flask import Flask
from flask import render_template

app = Flask ("Galerie")


@app.route("/index")
def index ():
    return render_template("index.html")


@app.route("/eingabe", methods= ["GET","POST"])
def eingabe ():


    return render_template("eingabe.html", app_name="Galerie - eingabe")


@app.route("/beispiel", methods= ["GET","POST"])
def beispiel ():


    return render_template("beispiel.html", app_name="Galerie - beispiel")

if __name__ == "__main__":
 app.run(debug=True, port=5000)