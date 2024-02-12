from flask import Flask, render_template

app = Flask(__name__)


# 1 Напишите простое веб-приложение на Flask, которое будет
# выводить на экран текст "Hello, World!"
# @app.route('/')
# @app.route('/index/')
# def index():
#     return "Hello world"


# Дорабатываем задачу 1.
# Добавьте две дополнительные страницы в ваше вебприложение:
# ○ страницу "about"
# ○ страницу "contact"
@app.route('/about/')
def about():
    return "About me"


@app.route('/contact/')
def contact():
    return "My contacts"


# # Написать функцию, которая будет принимать на вход два
# # числа и выводить на экран их сумму.
@app.route('/<int:number1>/<int:number2>')
#  - специальный способ чтобы отрабатывала Flask аннотация типов, а не Python(наоборот грубо говоря)
def sum_numbers(number1: int, number2: int):
    return str(number1 + number2)


# Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.
@app.route('/<line>/')
def length(line: str):
    return str(len(line))


# Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!"

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index1.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
