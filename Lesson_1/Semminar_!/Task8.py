# Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты", используя базовый шаблон.
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


@app.route('/about_me/')
def about_me():
    return render_template('about_me.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
