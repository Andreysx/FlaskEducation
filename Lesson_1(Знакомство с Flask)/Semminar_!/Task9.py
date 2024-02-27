# Задание №9
# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.


from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/clothes/')
def clothes():
    return render_template('clothes9.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes9.html')


@app.route('/jackets/')
def jackets():
    return render_template('jackets9.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)