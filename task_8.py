# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".
# files: index_8.html, flash_form_8.html

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'b02ecf0107636709f32a18fdd3a7ea9e3a65970f91376a3bf622a2acf73cc2ca'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect('/')
        flash(f'Привет, {name}!', 'success')
        return redirect('/flash_form_8/')
    return render_template('index_8.html')

@app.route('/flash_form_8/')
def flash_form_8():
    return render_template('flash_form_8.html')


if __name__ == '__main__':
    app.run(debug=True)