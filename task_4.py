# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.
# files: form4.html, result_4.html

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        len_text = len(text)
        return redirect(url_for('result', count=len_text))
    return render_template('form_4.html')


@app.route('/result/<count>')
def result(count):
    return render_template('result_4.html', count=count)



if __name__ == '__main__':
    app.run(debug=True)