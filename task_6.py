# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.
# files: index_6.html, result_6.html, flash_form_6.html


from flask import Flask, request, render_template, url_for, flash, redirect

app = Flask(__name__)
app.secret_key = b'ade0168a35423e3903435b8f41a89ffb4e8b36aa904eb2efd0b55e4fb7927aa6'

@app.route('/', methods=['GET', 'POST'])
def index_6():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        # if 0 > int(age) > 100:
        if not age.isdigit() or int(age) < 0 or int(age) > 100:
            flash('Некорректный возраст!', 'error')
            return redirect(url_for('index_6'))
        return redirect(url_for('result_6', name=name, age=age))
    return render_template('index_6.html')

@app.route('/result_6/')
def result_6():
    name = request.args.get('name')
    age = request.args.get('age')
    return render_template('result_6.html', name=name, age=age)


if __name__ == '__main__':
    app.run(debug=True)