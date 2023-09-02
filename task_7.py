# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.
# files: index_t.html, result_7.html


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num = int(request.form['num'])
        result = num ** 2
        return redirect(url_for('result', result=result))
    return render_template('index_7.html')

@app.route('/result/<result>')
def result(result):
    return render_template('result_7.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)