from flask import Flask
from flask import render_template
from flask import request

from daten import speichern

app = Flask("tracker")


@app.route('/')
def start():
    ueberschrifts_text = "Willkommen auf der Tracker Website"
    einleitung_text = "Hier können Sie Ihre Aktivitäten tracken. Was wollen Sie tun?"
    return render_template('start.html', app_name="Tracker!", ueberschrift=ueberschrifts_text, einleitung=einleitung_text)


@app.route('/eingabe', methods=['POST', 'GET'])
def eingabe():

    if request.method == 'POST':
        aktivitaet = request.form['aktivitaet']
        dauer = request.form['dauer']
        antwort = speichern(aktivitaet, dauer)
        return 'Gespeicherte Daten: <br>' + str(antwort)

    return render_template('eingabe.html', app_name="Tracker!- Eingabe")


@app.route('/about')
def about():
    ueberschrifts_text = "Über diese Webapp"
    einleitung_text = "Diese App wurde als Demo-App programmiert"
    return render_template('start.html', app_name="Tracker! - About", ueberschrift=ueberschrifts_text, einleitung=einleitung_text)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
