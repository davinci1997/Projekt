from flask import Flask
from flask import render_template
from flask import request
from Galerieprojekt.bildspeichern import takebild
from Galerieprojekt.kommentar import speichern, erstelle_dict, kommentar_ausgeben, bild_ausgeben

bildupload = 'static/img_variable'
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


@app.route("/eingabe", methods=['Get', 'POST'])
def eingabe():
    if request.method == 'POST':     # Methode zum Daten vom Formular aufzunehmen und bearbeiten
        kommentardict = erstelle_dict(request)  # dictionnary mit Kommentar und Bild für json wird erstellt / kommentar
        takebild(request, app, bildupload, )  # Funktion zum Bild in img Variable speichern
        speichern(kommentardict)  # Kommentardict wird in json heruntergeladen

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
    if request.method == 'GET':  # Methode zum daten im html laden
        bild = bild_ausgeben()  # Funktion Zum Bildname von Json herunterzuladen
        ausgabe_kommentar = kommentar_ausgeben()  # Funktion zum Kommentar von Json herunterzuladen
    return render_template("ausgabe.html",
                           app_name="Galerie - Ausgabe",
                           bilder=bild,
                           kommentar=ausgabe_kommentar
                           )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
