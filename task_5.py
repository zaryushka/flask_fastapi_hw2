# 📌 Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# 📌 При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.
# files: calculator.html, result.html

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# app.secret_key = b'ade0168a35423e3903435b8f41a89ffb4e8b36aa904eb2efd0b55e4fb7927aa6'

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        operation = request.form['operation']

        if operation == 'div' and int(num2) == 0:
            return render_template('calculator.html', error='Деление на ноль невозможно')


        if operation == 'add':
            result = num1 + num2
        elif operation == 'sub':
            result = num1 - num2
        elif operation == 'mul':
            result = num1 * num2
        elif operation == 'div':
            result = num1 / num2

        return redirect(url_for('result', result=result))
    return render_template('calculator.html')

@app.route('/result/<result>')
def result(result):
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)