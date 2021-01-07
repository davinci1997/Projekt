import json


def speichern(commit_1, commit_2):
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
    except:
        print("ich kann dieses Komentar nicht speichern")
        eintraege = []

    eintrag = (commit_1, commit_2)

    eintraege.append(eintrag)

    with open("datenbank.json", "w") as datenbank:
        json.dump(eintraege, datenbank)
    return commit_1, commit_2


def ausgeben():
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
            ubertragung = eintraege[0]
    except :
        print("Beim laden konnte keine vorhandene Datenbank gefunden werden")
        eintrag = []

    return ubertragung


def ausgeben_2():
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
            ubertragung_2 = eintraege[1]


    except:
        print("Beim laden konnte keine vorhandene Datenbank gefunden werden")
        eintrag = []

    return ubertragung_2
