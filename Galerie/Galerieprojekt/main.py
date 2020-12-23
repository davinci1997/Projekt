from flask import Flask
from flask import render_template
from flask import request

from Galerieprojekt.kommentar import speichern, ausgeben

app = Flask("Galerie")


@app.route("/", methods=["Get", "Post"])
def lazy():
    return render_template("index.html",
                           app_name="Startseite"
                           )


@app.route("/index", methods=["GET", "POST"])
def index():
    return render_template("index.html",
                           app_name="Startseite"
                           )


@app.route("/eingabe", methods=["GET", "POST"])
def eingabe():
    if request.method == 'POST':
        commit_1 = request.form['kommentarspeichern_1']
        speichern(commit_1)
        return str(commit_1)

    return render_template("eingabe.html",
                           app_name="Galerie - eingabe", )


@app.route("/beispiel", methods=["GET", "POST"])
def beispiel():
    return render_template("beispiel.html",
                           app_name="Galerie - Beispiel"
                           )


@app.route("/ausgabe", methods=["GET", "POST"])
def ausgabe():
    if request.method == 'GET':
        answer = ausgeben()
        return render_template("ausgabe.html",
                           app_name="Galerie - Ausgabe",
                            ausgabe= str (answer)

                           )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
