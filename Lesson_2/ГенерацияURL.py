# Генерация url адресов
# На прошлом занятии мы использовали относительные имена во всех примерах
# кода. Такой подход удобен пока приложения небольшое. Но лучше сразу привыкать
# к хорошему тону и при формировании адреса использовать функцию url_for().
# Рассмотрим поведение функции на следующем примере.
# @app.route('/test_url_for/<int:num>/')
# def test_url(num):
# text = f'В num лежит {num}<br>'
# text += f'Функция {url_for("test_url", num=42) = }<br>'
# text += f'Функция {url_for("test_url", num=42,
# data="new_data") = }<br>'
# text += f'Функция {url_for("test_url", num=42,
# data="new_data", pi=3.14515) = }<br>'
# return text
# При переходе по адресу test_url_for/7/ увидем следующий вывод:
# В num лежит 7
# Функция url_for("test_url", num=42) = '/test_url_for/42/'
# Функция url_for("test_url", num=42, data="new_data") =
# '/test_url_for/42/?data=new_data'
# Функция url_for("test_url", num=42, data="new_data", pi=3.14515)
# 4
# = '/test_url_for/42/?data=new_data&pi=3.14515'
# Как видно из примера функция url_for принимает имя view функции в качестве
# первого аргумента и любое количество ключевых аргументов. Каждый ключ
# соответствует переменной в URL адресе. Отсутствующие в адресе переменные
# добавляются к адресу в качестве параметров запроса, т.е. после знака вопрос “?”
# как пары ключ-значение, разделённые символом &.
# 🔥 Внимание! Обратите внимание, что первый параметр совпадает с
# названием функции-представления, а не с адресом внутри route. Таким
# образом изменение маршрутов автоматически изменит генерируемые url
# без лишних правок. Ведь имена view функций останутся прежними.
# Генерация пути к статике
# Один из распространённых способов использования url_for является указание пути
# к файлам статики внутри шаблонов.
# Рассмотрим следующее представление
# @app.route('/about/')
# def about():
#     context = {
#     'title': 'Обо мне',
#     'name': 'Харитон',
#     }
#     return render_template('about.html', **context)
# На прошлом занятии мы выводили примерно такой шаблон
# <!doctype html>
# <html lang="ru">
# <head>
# <meta charset="utf-8">
# <link rel="stylesheet" href="/static/css/bootstrap.min.css">
# <title>{{ title }}</title>
# </head>
# <body>
# <h1 class="text-monospace">Привет, меня зовут {{ name }}</h1>
# <img src="/static/image/foto.jpg" alt="Моё фото" width="300">
# <p class="text-body text-justify">Lorem ipsum dolor sit amet, consectetur adipisicing
# elit. Ad cupiditate doloribus ducimus nam provident quo similique! Accusantium
# aperiam fugit magnam quas reprehenderit sapiente temporibus voluptatum!</p>
# <p class="alert-dark">Все права защищены &copy;</p>
# <script src="/static/js/bootstrap.bundle.min.js"></script>
# </body>
# </html>
# В качестве статики тут прописаны стили и скрипты bootstrap, а также изображение
# из каталога image. Исправим эти три строки шаблона используя url_for
# ...
# <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.min.css') }}">
# ...
# <img src="{{ url_for('static', filename='image/foto.jpg') }}" alt="Моё фото"
# width="300">
# ...
# <script src="{{ url_for('static', filename='js/bootstrap.bundle.min.js') }}"></script>
# ...
# Чтобы сгенерировать URL-адреса для статических файлов, необходимо
# использовать специальное имя “static” в качестве первого параметра, а по ключу
# filename передать путь до файла внутри каталога static.
# 💡 Внимание! Не стоит создавать view функцию с именем static.
# 🔥 Важно! Во время разработки приложения за раздачу статики отвечает
# Flask. При запуске рабочего проекта статику раздаёт веб-сервер, а не Flask.
# Для этого надо настроит сервер. Изменять шаблоны Flask не нужно, url_for
# сгенерировала необходимые пути.
