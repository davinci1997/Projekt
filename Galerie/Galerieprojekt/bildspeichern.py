import os
import shutil

from werkzeug.utils import secure_filename


def takebild(request, app, bildupload, filelist):
    app.config['bildupload'] = bildupload

    for file in filelist:
        if file not in request.files:
            print('kein Bild gefunden')
        file_request = request.files[file]
        filename = secure_filename(file_request.filename)
        altes_file = os.path.join(app.config['bildupload']+"/", filename)
        file_request.save(altes_file)
        neues_file = os.path.join(app.config['bildupload']+"/", file+'.jpg')

        shutil.copy(altes_file, neues_file)
