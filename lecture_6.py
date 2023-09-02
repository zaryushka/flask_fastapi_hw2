# flash сообщения
# files: base.html, flash_form.html

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'b02ecf0107636709f32a18fdd3a7ea9e3a65970f91376a3bf622a2acf73cc2ca'


@app.route('/')
def index():
    return 'Hi!'

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)