# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.

# Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".

# Данные о студентах должны быть переданы в шаблон через
# контекст.

# Папка templates обязательно должна быть внутри проекта!!!

from flask import Flask,render_template


app = Flask(__name__)


@app.route("/")
def show_people():

    names = [{'name':'IVAN',
        'Lastname':'IVANOV',
        'age': 48},
        {'name': 'Andrey',
        'Lastname': 'Kochetkov',
        'age': 48}]

    return render_template("index6.html", names=names)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)