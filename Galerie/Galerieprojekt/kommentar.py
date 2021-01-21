import json
from werkzeug.utils import secure_filename


def speichern(kommentardict):
    try:
        with open("datenbank.json", "r") as datenbank:  # Die Datenbankjson wird gelesen
            print(kommentardict)  # checkpoint
            eintrag = json.load(datenbank)  # die Datenbank json wird heuntergeladen
            eintrag.update(kommentardict)  # Kommentardictionary wird aktualisiert (json Dump)
    except:
        eintrag = {}  # neues dict erstellen

    eintrag.update(kommentardict)
    with open("datenbank.json", "w") as datenbank:  # einträge in json hinzufügen
        json.dump(eintrag, datenbank)  # Daten in Json pushen


def erstelle_dict(request):
    commentvalue = {}
    kommentar = request.form['kommentar']  # Umwandlung request form in variable
    bild_unsicher = request.files['bild']  # Umwandlung request form von Bild in Variable
    bild_gesichert = secure_filename(bild_unsicher.filename)  # never trust filenames from the  Users !!!!!!
    commentvalue[bild_gesichert] = kommentar  # Bild und Kommentar als key und value speichern

    return commentvalue


def bild_ausgeben():
    try:
        with open("datenbank.json", "r") as datenbank:  # json wird gelesen
            ausladen = json.load(datenbank)  # json wird geladen
            bilder_ausgabe = list(ausladen.keys())  # keys von dict in eine Liste laden
            print(bilder_ausgabe)
    except:
        print('don t working')

    return bilder_ausgabe


def kommentar_ausgeben():
    try:
        with open("datenbank.json", "r") as datenbank:  # Datenbank wird gelesen
            ausladen = json.load(datenbank)  # Datenbank wird geladen
            print(ausladen.values())  # checkpoint
            kommentar_ausgabe = list(ausladen.values())  # values werden in eine liste einbezogen
            # ausgabeliste= kommentarliste.append(kommentar_ausgabe)
            ausgabeliste = kommentar_ausgabe
            print(ausgabeliste)

    except:
        print('i dont know commit')

    return ausgabeliste
