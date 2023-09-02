# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.
# files: index_hw.html, welcome_hw.html

from flask import Flask, request, render_template, redirect, make_response

app = Flask(__name__)
app.secret_key = b'ade0168a35423e3903435b8f41a89ffb4e8b36aa904eb2efd0b55e4fb7927aa6'

@app.route('/', methods=['GET', 'POST'])
def index_hw():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        response = make_response(redirect('/welcome_hw/'))
        response.set_cookie('name', name)
        response.set_cookie('email', email)
        return response
    return render_template('index_hw.html')

@app.route('/welcome_hw/')
def welcome_hw():
    name = request.cookies.get('name')
    email = request.cookies.get('email')
    return render_template('welcome_hw.html', name=name, email=email)

@app.route('/logout/')
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('name', '', expires=0)
    response.set_cookie('email', '', expires=0)
    return response



if __name__ == '__main__':
    app.run(debug=True)