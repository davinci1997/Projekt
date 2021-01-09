import json


def speichern(kommentarliste):
    with open("datenbank.json", "w") as datenbank:
        json.dump(kommentarliste, datenbank)


def ausgeben():
    kommentar_dict = {}
    try:
        with open("datenbank.json", "r") as datenbank:
            kommentare = json.load(datenbank)
            index = 1
            for kommentar in kommentare:
                kommentar_dict['answer_'+str(index)] = kommentar
                index = int(index) + 1

            print(kommentar_dict)

    except:
        print("Beim laden konnte keine vorhandene Datenbank gefunden werden")

    return kommentar_dict


def erstelle_kommentarliste(request):
    commentvalue = []
    for fieldname, value in request.form.items():
        print(fieldname, value)
        commentvalue.append(value)
    return commentvalue
