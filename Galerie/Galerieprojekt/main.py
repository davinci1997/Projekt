from flask import Flask
from flask import render_template
from flask import request
from Galerieprojekt.bildspeichern import takebild
from Galerieprojekt.kommentar import ausgeben, speichern, erstelle_kommentarliste

bildupload = 'static/img_variable'
app = Flask("Galerie")
filesname = ['bild_1', 'bild_2', 'bild_3', 'bild_4']


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


@app.route("/eingabe", methods=['Get', 'POST'])
def eingabekommentar():
    if request.method == 'POST':
        kommentarliste = erstelle_kommentarliste(request)
        takebild(request, app, bildupload, filesname)
        speichern(kommentarliste)
        return "Gehe zu  ausgabe"

    return render_template("eingabe.html",
                           app_name="Galerie - eingabe",
                           kommentar_schreiben='Schreibe deinen Kommetar'
                           )


@app.route("/beispiel", methods=["GET", "POST"])
def beispiel():
    return render_template("beispiel.html",
                           app_name="Galerie - Beispiel"
                           )


@app.route("/ausgabe", methods=["GET", "POST"])
def ausgabe():
    if request.method == 'GET':
        kommdict = ausgeben()
        return render_template("ausgabe.html",
                               app_name="Galerie - Ausgabe",
                               ausgabe_1=kommdict['answer_1'],
                               ausgabe_2=kommdict['answer_2'],
                               ausgabe_3=kommdict['answer_3'],
                               ausgabe_4=kommdict['answer_4']
                               )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
