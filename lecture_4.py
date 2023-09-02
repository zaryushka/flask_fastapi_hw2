# перенаправления

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'

@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index')) # index - имя функции из предыдущей вьюшки, по сути на ту страницу, куда перенаправляем

@app.route('/external/') # перенаправление на любую внешнюю ссылку
def external_redirect():
    return redirect('https://python.org/')

@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!'

@app.route('/redirect/<name>') # то же. что и предыдущая вьюшка, но с формированием адреса через функцию url_for
def redirect_to_hello(name):
    return redirect(url_for('hello', name=name)) # здесь 'hello' - имя функции, куда перенаправляем, в предыдущ.вьюшку

if __name__ == '__main__':
    app.run(debug=True)