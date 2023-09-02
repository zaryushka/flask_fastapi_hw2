# flash сообщения
# files: base.html, flash_form.html

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'

"""
Генерация надежного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""

@app.route('/')
def index():
    return 'Hi!'


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # обработка данных формы
        flash('Форма успешно отправлена!', 'success') # 'Форма успешно отправлена!' попадет в переменную message. success - в переменную category
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)