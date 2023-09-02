# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.
# file: form_11.html

from flask import Flask, request, render_template

app = Flask(__name__)

@app.get('/')
def button():
    return render_template('form_11.html')


@app.post('/button_post/')
def button_post():
    name = request.form.get('name')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)