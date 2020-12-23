import json

Kommentaren = {"commit_1":0,
               "commit_2":1,
               "commit_3":2,
               "commit_4":3,
               "commit_5":4,
               "commit_6":5,
               "commit_7":6,
               "commit_8":7 }


def speichern(commit_1):
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
    except:
        print("ich kann dieses Komentar nicht speichern")
        eintraege = []

    eintrag = (commit_1)

    eintraege.append(eintrag)

    with open("datenbank.json", "w") as datenbank:
        json.dump(eintraege, datenbank)

    return commit_1

def ausgeben():
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
            eintrag = eintraege[0]
    except:
        print("Beim laden konnte keine vorhandene Datenbank gefunden werden")
        eintrag = []

    return eintrag
