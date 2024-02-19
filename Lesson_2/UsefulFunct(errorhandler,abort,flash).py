# Несколько полезных функций
# В этой главе рассмотрим несколько полезных функций, которые сделают ваше
# приложение лучше.
# Обработка ошибок
# Что будет, если пользователь перешёл на несуществующую страницу? Если ничего
# не предпринимать, получим следующий вывод:
# Not Found
# The requested URL was not found on the server. If you entered the URL manually
# please check your spelling and try again.
# 11
# Декоратор errorhandler
# Flask предоставляет возможности для обработки ошибок и способен заменить
# стандартный текст на симпатичную страницу в стиле вашего сайта.
# Обработка ошибок в Flask происходит с помощью декоратора errorhandler(). Этот
# декоратор позволяет определить функцию-обработчик ошибок, которая будет
# вызываться в случае возникновения ошибки в приложении.
# Например, чтобы обработать ошибку 404 (страница не найдена), необходимо
# определить функцию, которая будет вызываться при возникновении этой ошибки:
# import logging
# from flask import Flask, render_template, request
# app = Flask(__name__)
# logger = logging.getLogger(__name__)
# @app.route('/')
# def index():
# return '<h1>Hello world!</h1>'
# @app.errorhandler(404)
# def page_not_found(e):
# logger.warning(e)
# context = {
# 'title': 'Страница не найдена',
# 'url': request.base_url,
# }
# return render_template('404.html', **context), 404
# В этом примере мы определяем функцию page_not_found(), которая будет
# вызываться при ошибке 404. Функция возвращает шаблон HTML страницы 404 и
# код ошибки 404. Обратите внимание, что в переменную e попадает текст той самой
# ошибки о “Not Found…”. Её мы выводим в логи как предупреждение.
# В качестве контекста пробрасываем в шаблон заголовок страницы и адрес, по
# которому пытался перейти пользователь. Свойство base_url у объекта request
# возвращает тот адрес, который видит пользователь в адресной строке браузера.
# Что касается шаблона, возьмём базовый из прошлой лекции.
# Шаблон base.html
# 12
# <!doctype html>
# <html lang="ru">
# <head>
# <meta charset="utf-8">
# <meta name="viewport" content="width=device-width,
# initial-scale=1, shrink-to-fit=no">
# <link rel="stylesheet" href="/static/css/bootstrap.min.css">
# <title>
# {% block title %}
# Мой сайт
# {% endblock %}
# </title>
# </head>
# <body>
# <div class="container-fluid">
# <ul class="nav nav-pills justify-content-end
# align-items-end">
# <li class="nav-item"><a href="/main/"
# class="nav-link">Основная</a></li>
# <li class="nav-item"><a href="/data/"
# class="nav-link">Данные</a></li>
# </ul>
# {% block content %}
# Страница не заполнена
# {% endblock %}
# <div class="row fixed-bottom modal-footer">
# <hr>
# <p>Все права защищены &copy;</p>
# </div>
# </div>
# <script src="/static/js/bootstrap.bundle.min.js"></script>
# </body>
# </html>
# В этом случае шаблон для ошибки 404 может выглядеть например так:
# {% extends 'base.html' %}
# {% block title %}
# {{ title }}
# {% endblock %}
# 13
# {% block content %}
# <div class="row">
# <p class="col-12">Мы не нашли страницу: &laquo;{{ url
# }}&raquo;.<br>
# <a href="{{ url_for('index') }}">Попробуйте вернуться на
# главную</a>
# </p>
# </div>
# {% endblock %}
# Обратите внимание, что адрес главной страницы указан не явно, а генерируется
# через url_for. Подобная практика должна использоваться во всех шаблонах проекта
# для удобства масштабирования.
# Функция abort
# Функция abort() также используется для обработки ошибок в Flask. Она позволяет
# вызвать ошибку и передать ей код ошибки и сообщение для отображения
# пользователю.
# Например, чтобы вызвать ошибку 404 с сообщением "Страница не найдена",
# необходимо использовать функцию abort():
# import logging
# from flask import Flask, render_template, request, abort
# from flask_lesson.db import get_blog
# app = Flask(__name__)
# logger = logging.getLogger(__name__)
# @app.route('/')
# def index():
# return '<h1>Hello world!</h1>'
# @app.route('/blog/<int:id>')
# def get_blog_by_id(id):
# ...
# # делаем запрос в БД для поиска статьи по id
# 14
# result = get_blog(id)
# if result is None:
# abort(404)
# ...
# # возвращаем найденную в БД статью
# @app.errorhandler(404)
# def page_not_found(e):
# logger.warning(e)
# context = {
# 'title': 'Страница не найдена',
# 'url': request.base_url,
# }
# return render_template('404.html', **context), 404
# В этом примере мы используем функцию abort() внутри get_blog_by_id для вызова
# ошибки 404 в случае отсутствия статьи в базе данных.
# 💡 Внимание! Чтобы код внутри представления отработал без ошибок,
# написана следующая функция заглушка:
# def get_blog(id):
# return None
# Некоторые коды ошибок
# ● 400: Неверный запрос
# ● 401: Не авторизован
# ● 403: Доступ запрещен
# ● 404: Страница не найдена
# ● 500: Внутренняя ошибка сервера
# Иногда из-за ошибок в коде сервер может возвращать ошибку 500. В идеальном
# мире код предусматривает все возможные ситуации и не отдаёт ошибку 500. Но
# почему бы не подстелить соломки.
# Удалим функции get_blog из примера выше. Теперь при попытке найти статью по id
# получаем сообщение на странице:
# 15
# Internal Server Error
# The server encountered an internal error and was unable to complete your request.
# Either the server is overloaded or there is an error in the application.
# 🔥 Важно! Если вы запускаете сервер в режиме отладки, будет выведена
# трассировка ошибки, а не сообщение. Перезапустите сервер с параметром
# debug=False
# В несколько строк напишем обработчик для вывода сообщения в стиле проекта.
# ...
# @app.errorhandler(500)
# def page_not_found(e):
# logger.error(e)
# context = {
# 'title': 'Ошибка сервера',
# 'url': request.base_url,
# }
# return render_template('500.html', **context), 500
# ...
# По сути взяли за основу обработчик ошибки 404, но лог фиксирует не
# предупреждение, а ошибку. Плюс новый шаблон, и возврат кода 500 клиенту.
# Шаблон 500 может выглядеть так:
# {% extends 'base.html' %}
# {% block title %}
# {{ title }}
# {% endblock %}
# {% block content %}
# <div class="row alert alert-danger">
# <p class="col-12">На сервере произошла ошибка. Мы уже знаем и
# занимаемся исправлениями.<br>
# <a href="{{ url }}">Обновите страницу через несколько
# минут</a>
# </p>
# </div>
# {% endblock %}
# 16
# Перенаправления
# Перенаправления в Framework Flask позволяют перенаправлять пользователя с
# одной страницы на другую. Это может быть полезно, например, для
# перенаправления пользователя после успешной отправки формы или для
# перенаправления пользователя на страницу авторизации при попытке доступа к
# защищенной странице без авторизации.
# Для перенаправления в Flask используется функция redirect(). Она принимает
# URL-адрес, на который нужно перенаправить пользователя, и возвращает объект
# ответа, который перенаправляет пользователя на указанный адрес.
# Например, чтобы перенаправить пользователя на главную страницу сайта, можно
# использовать следующий код:
# from flask import Flask, redirect, url_for
# app = Flask(__name__)
# @app.route('/')
# def index():
# return 'Добро пожаловать на главную страницу!'
# @app.route('/redirect/')
# def redirect_to_index():
# return redirect(url_for('index'))
# ...
# В этом примере мы определяем два маршрута: '/' для главной страницы и '/redirect'
# для перенаправления на главную страницу. Функция redirect_to_index() использует
# функцию redirect() для перенаправления пользователя на главную страницу с
# помощью функции url_for(), которая возвращает URL-адрес для указанного
# маршрута.
# Функция redirect() также может использоваться для перенаправления пользователя
# на внешний URL-адрес. Например:
# ...
# @app.route('/external')
# def external_redirect():
# return redirect('https://google.com')
# ```
# 17
# В этом примере мы используем функцию redirect() для перенаправления
# пользователя на внешний URL-адрес https://google.com.
# Кроме того, в Flask есть возможность использовать перенаправления с
# параметрами. Например, чтобы передать параметры в URL-адрес при
# перенаправлении, можно использовать следующий код:
# ...
# @app.route('/hello/<name>')
# def hello(name):
# return f'Привет, {name}!'
# @app.route('/redirect/<name>')
# def redirect_to_hello(name):
# return redirect(url_for('hello', name=name))
# ...
# В этом примере мы определяем маршрут '/hello/<name>', который принимает
# параметр 'name', и маршрут '/redirect/<name>', который использует функцию
# redirect() для перенаправления пользователя на маршрут '/hello/<name>' с
# передачей параметра 'name'. Функция url_for() возвращает URL-адрес для
# указанного маршрута с передачей параметров.
# Flash сообщения
# Flash сообщения в Flask являются способом передачи информации между
# запросами. Это может быть полезно, например, для вывода сообщений об
# успешном выполнении операции или об ошибках ввода данных.
# Для работы с flash сообщениями используется функция flash(). Она принимает
# сообщение и категорию, к которой это сообщение относится, и сохраняет его во
# временном хранилище.
# Например, чтобы вывести сообщение об успешной отправке формы, можно
# использовать следующий код:
# from flask import Flask, flash, redirect, render_template,
# request, url_for
# app = Flask(__name__)
# app.secret_key =
# b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e
# 4'
# 18
# @app.route('/form', methods=['GET', 'POST'])
# def form():
# if request.method == 'POST':
# # Обработка данных формы
# flash('Форма успешно отправлена!', 'success')
# return redirect(url_for('form'))
# return render_template('form.html')
# В этом примере мы определяем маршрут '/form' для отображения и обработки
# формы. Если метод запроса POST, то происходит обработка данных формы и
# выводится сообщение об успешной отправке с помощью функции flash() и
# категории 'success'. Затем происходит перенаправление на страницу с формой с
# помощью функции redirect().
# Секретный ключ
# Небольшое отступление. Чтобы не получать ошибки вида при работе с сессией
# RuntimeError: The session is unavailable because no secret key
# was set. Set the secret_key on the application to something
# unique and secret.
# необходимо добавить в Flask приложение секретный ключ.
# Простейший способ генерации такого ключа, выполнить следующие пару строк
# кода
# >>> import secrets
# >>> secrets.token_hex()
# Сразу после создания приложения прописываем инициализацию ключа
# сгенерированным набором байт. Теперь данные в безопасности, можно продолжать
# развивать приложение.
# Шаблон для flash сообщений
# Чтобы вывести flash сообщения в HTML шаблоне, можно использовать следующий
# код шаблона:
# {% extends 'base.html' %}
# {% block title %}
# {{ title }}
# {% endblock %}
# 19
# {% block content %}
# <form action="/form" method="post">
# {% with messages = get_flashed_messages(with_categories=true)
# %}
# {% if messages %}
# {% for category, message in messages %}
# <div class="alert alert-{{ category }}">
# {{ message }}
# </div>
# {% endfor %}
# {% endif %}
# {% endwith %}
# <input type="text" name="name" placeholder="Имя">
# <input type="submit" value="Отправить">
# </form>
# {% endblock %}
# Этот код использует функцию get_flashed_messages() для получения всех flash
# сообщений с категориями (блок with). Далее проверяем передавались ли
# сообщения через flash. Если да, в цикле происходит получение категорий и
# сообщений, т.к. указан параметр with_categories=true. Далее их вывод в
# соответствующих блоках с применением стилей bootstrap.
# Категории flash сообщений
# Категории сообщений в flash позволяют различать типы сообщений и выводить их
# по-разному. Категория по умолчанию message. Но вторым аргументом можно
# передавать и другие категории, например warning, success и другие.
# Например, чтобы вывести сообщение об ошибке ввода данных, можно
# использовать следующую модификацию функции:
# @app.route('/form', methods=['GET', 'POST'])
# def form():
# if request.method == 'POST':
# # Проверка данных формы
# if not request.form['name']:
# flash('Введите имя!', 'danger')
# return redirect(url_for('form'))
# # Обработка данных формы
# flash('Форма успешно отправлена!', 'success')
# return redirect(url_for('form'))
# return render_template('form.html')
# Проверяем данные формы на наличие имени. Если имя не указано, то выводится
# сообщение об ошибке с категорией danger и происходит перенаправление на
# страницу с формой. Сама форма будет работать без изменений.
# Flash сообщения являются удобным способом передачи информации между
# запросами в Flask. Они позволяют выводить сообщения пользователю и упрощают
# обработку ошибок и успешных операций.