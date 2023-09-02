# форма для загрузки файла на сервер в папку uploads
# file upload.html


from pathlib import PurePath, Path
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)


# file upload.html:
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Форма для загрузки файла</title>
# </head>
# <body>
#     <h1>Загружаем новый файл на сервер</h1>
#     <form method=post enctype=multipart/form-data>
#         <input type=file name=file>
#         <input type=submit value=Загрузить>
#     </form>
# </body>
# </html>
