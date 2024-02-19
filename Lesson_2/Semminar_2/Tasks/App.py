# Создать страницу, на которой будет кнопка "Нажми меня",
# при нажатии на которую будет переход на другую страницу с приветствием пользователя по имени.

from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'index'}
    return render_template('button(1).html', **context)

# Создать страницу,
# на которой будет изображение и ссылка на другую страницу,
# на которой будет отображаться форма для загрузки изображений.


@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    context = {'title': 'hello'}
    if request.method == 'POST':
        result = request.files.get('file')
        print(result)
        return "Файл загружен"

    return render_template('index.html', **context)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
