import os
import shutil
from werkzeug.utils import secure_filename


def takebild(request, app, bildupload):
    app.config['bildupload'] = bildupload  # erweitern
    bild_unsave = request.files['bild']  # file von bild wird hervorgerufen
    bild_save = secure_filename(bild_unsave.filename)  # Bild sichern / Never trust input from user!
    bild_pfad = os.path.join(app.config['bildupload'] + "/", bild_save)  # pfad hervorrufen
    bild_unsave.save(bild_pfad)  # pfad wird ausgeführt


""" altes_file = os.path.join(app.config['bildupload']+"/", filename)
        file_request.save(altes_file)
        neues_file = os.path.join(app.config['bildupload']+"/", file+'.jpg')

        shutil.copy(altes_file, neues_file)"""
