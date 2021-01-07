import os

from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename
from Galerieprojekt.kommentar import ausgeben, ausgeben_2, speichern

bildupload = 'static/img'

app = Flask("Galerie")
app.config['bildupload'] = bildupload

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


def takebild(request1):
    if 'file' not in request1.files:
        print("Kein Bild vorhanden")

    print("I m here")
    file = request1.files['file']
    filename = secure_filename(file.filename)
    print(filename)
    file.save(os.path.join(app.config['bildupload'], filename))  # Link erstellen um ein file speichern zu können


@app.route("/eingabe", methods=['Get', 'POST'])
def eingabekommentar():

    if request.method == 'POST':
        bildname = takebild(request)
        print("i'm here")
        commit_1 = request.form['kommentarspeichern_3']
        commit_2 = request.form['kommentarspeichern_4']
        antwortprogramm = speichern(commit_1, commit_2)
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
        answer_1 = ausgeben()
        answer_2 = ausgeben_2()
        return render_template("ausgabe.html",
                               app_name="Galerie - Ausgabe",
                               ausgabe_1=str(answer_1),
                               ausgabe_2=str(answer_2)
                               )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
