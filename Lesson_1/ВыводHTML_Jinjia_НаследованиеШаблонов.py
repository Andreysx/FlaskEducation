# Выводим HTML
# Рассмотрим два варианта вывода HTML.
# Многостраничный текст с тегами
# Python легко может сохранить многостраничный документ в переменной, если
# заключить его в три двойные кавычки.
# html = """
# <h1>Привет, меня зовут Алексей</h1>
# <p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>
# """
# Содержимое переменной можно вернуть, используя функцию представления. При
# этом браузер выведет текст с учётом тегов.
# @app.route('/text/')
# def text():
#     return html
# Как вы видите, html теги не выводятся в браузере как текст, а преобразуются в теги.
# При желании можно сделать страницу динамической. В примере ниже каждая
# строчка стихотворения хранится как элемент списка list. Для примера в первой
# лекции этого достаточно. Но вы должны понимать, что аналогичным образом можно
# использовать данные из БД, внешних источников и т.п.
# @app.route('/poems/')
# def poems():
#     poem = ['Вот не думал, не гадал,',
#     'Программистом взял и стал.',
#     'Хитрый знает он язык,',
#     'Он к другому не привык.',
#     ]
#     txt = '<h1>Стихотворение</h1>\n<p>' + '<br/>'.join(poem) + '</p>'
#     return txt
#
# При желании можно прописать любую логику внутри функции, в зависимости от
# задач программиста и того, какую информацию необходимо вывести на странице
# сайта.
#
#
#
# Рендеринг HTML файла
# Попробуем вывести файл index.html, используя локальный сервер Flask.
# <!doctype html>
# <html lang="ru">
# <head>
# <meta charset="utf-8">
# <link rel="stylesheet" href="/static/css/bootstrap.min.css">
# <title>Главная</title>
# </head>
# <body>
# <h1 class="text-monospace">Привет, меня зовут Алексей</h1>
# <img src="/static/image/foto.jpg" alt="Моё фото" width="300">
# <p class="text-body text-justify">Lorem ipsum dolor sit amet,
# consectetur adipisicing elit. Ad cupiditate doloribus ducimus nam
# provident quo similique! Accusantium aperiam fugit magnam quas
# reprehenderit sapiente temporibus voluptatum!</p>
# <p class="alert-dark">Все права защищены &copy;</p>
# </body>
# </html>
# Начнём с того, что импортируем функцию отрисовки шаблонов. render_template()
# принимает в качестве первого аргумента название html-файла, который
# необходимо вывести в браузер.
#
# from flask import render_template
# Добавим функцию рендеринга в функцию представления и укажем ей на файл
# index.html. Общий код будет выглядеть так:
# from flask import Flask
# from flask import render_template
# app = Flask(__name__)
# @app.route('/index/')
# def html_index():
#     return render_template('index.html')
# После перехода по локальному адресу получим сообщение об ошибке:
# TemplateNotFound
# jinja2.exceptions.TemplateNotFound: index.html
#
# Функция render_template() ищет файл index.html в папке templates. Необходимо
# перенести его в нужную папку. Другие html-файлы также необходимо складывать в
# указанную папку.
# После перезагрузки сервер выводит страницу в браузер.
# 🔥 Внимание! Если изображения или стили отсутствуют, необходимо
# переместить их в соответствующие каталоги: стили в static/css, а
# изображения — в static/image. В самом html проверить путь к файлам:
# <link rel="stylesheet" href="/static/css/style.css">
# <img src="/static/image/foto.png" alt="Моё фото" width="300">
# После очередной перезагрузки сервера мы получим полноценную html-страницу.
# Шаблонизатор Jinja
# В примере выше мы смогли отрисовать HTML страницу силами Flask. Но если быть
# более точным, нам помог шаблонизатор Jinja. При этом сам html файл представляет
# статичную страницу сайта. Это удобно для быстрого получения информации
# клиентом от сервера. Но крайне неудобно для создания чего-то большего, чем одна
# страница. Благодаря Jinja статические html-страницы превращаются в шаблоны для
# формирования динамических сайтов.
# Пробрасываем контекст из представления в шаблон
# Функция render_template после имени шаблона может принимать неограниченное
# число именованных аргументов и пробрасывать их в шаблон. Шаблон позволяет
# вывести значение по имени, заключив его в двойные фигурные скобки {{ }}. Такие
# скобки — аналог функции print() в Python.
# Изменим строку вывода в функции, добавив аргумент name со значением
# «Харитон»:
# return render_template('index.html', name='Харитон')
#
# В шаблоне заменим имя владельца на вывод переменной из шаблона.
# <h1 class="text-monospace">Привет, меня зовут {{ name }}</h1>
# Jinja не ограничивает пользователя в количестве переменных, которые необходимо
# передать в шаблон. Но для сохранения читаемости кода рекомендуется сохранять
# все переменные в словарь и пробрасывать в шаблон его распакованный вид.
# Распаковка словаря — передача его содержимого как отдельных значений. В
# Python для распаковки словаря необходимо добавить две звёздочки ** перед
# именем словаря.
# Модифицируем нашу функцию представления для передачи не только имени, но и
# заголовка страницы.
# @app.route('/index/')
# def index():
#     context = {
#     'title': 'Личный блог',
#     'name': 'Харитон',
#     }
#     return render_template('index.html', **context)
# Теперь в шаблон проброшены переменные name и title и можно заменить
# содержимое шаблона внутри тега <title> на переменную.
# <title>{{ title }}</title>
# 🔥 Внимание! До и после двойных фигурных скобок рекомендуется оставлять
# пробел. Это не только облегчает чтение, но и в некоторых случаях
# заставляет код работать верно.
# Условный оператор в шаблоне
# Ветвления в Jinja имеют схожую с Python логику, но немного отличаются по
# синтаксису. Оператор if и логическое условие заключаются в скобки вида {% %}. В
# отличие от Python обязательным является закрывающий условие код вида
# {% endif %}.
# {% if user %}
# <p>Вы вошли под именем {{ user }}</p>
# {% endif %}
# Если в шаблон передали переменную user, будет выведен абзац текста. В
# противном случае код между открывающим и закрывающим операторами будет
# проигнорирован, не появится на стороне клиента.
# Как и в Python, шаблоны поддерживают сложные условия благодаря конструкциям
# {% elif %} и {% else %}
# Например мы можем выбирать окончание предложения в зависимости от
# переданного числа.
# <p>К прочтению предлагается {{ number }}
# {% if number == 1 %}
# пост
# {% elif 2 <= number <= 4 %}
# поста
# {% else %}
# постов
# {% endif %}
# </p>
# 🔥 Важно! Не забудьте добавить ключ number в словарь context для
# пробрасывания переменной из функции в шаблон.
# Вывод в цикле
# Аналогично Python, можно использовать цикл for внутри шаблона для вывода
# элементов последовательности. Из примера ниже понятно, что цикл заключается в
# специальные скобки {% %}, а конец цикла обязательно заканчивается блоком {%
# endfor %}
# {% for item in item_list %}
# {{ item }}
# {% endfor %}
# Изменим представление poems(), которое создали ранее на лекции. Сформируем
# аналогичный вывод стихотворения силами шаблонизатора Jinja.
# Помещаем список со строками стихотворения в словарь и пробросим его в шаблон.
# 14
# @app.route('/poems/')
# def poems():
#     context = {'poem': ['Вот не думал, не гадал,',
#     'Программистом взял и стал.',
#     'Хитрый знает он язык,',
#     'Он к другому не привык.',
#     ]}
#     # txt = """<h1>Стихотворение</h1>\n<p>""" + '<br/>'.join(poem) + '</p>'
#     return render_template('poems.html', **context)
# В шаблоне poems.html создадим цикл для форматированного вывода
# ...
# <body>
# <h1 class="text-monospace text-center">Стихотворение</h1>
# <p class="row">
# {% for line in poem %}
# <span class="text-black-50 col-12 col-md-6">{{ line
# }}</span><br/>
# {% endfor %}
# </p>
# </body>
# ...
# Как и в Python, условия и циклы можно использовать совместно, помещая одно в
# другое в зависимости от задач программиста.
# Вывод сложных структур в цикле
# Иногда необходимо вывести информацию о нескольких однотипных объектах с
# набором свойств. Например, информацию о пользователях из базы данных. Или
# если упростить задачу, список словарей с одинаковыми ключами. Для опытных
# программистов очевидно, что оба вывода идентичны. Рассмотрим список словарей.
# @app.route('/users/')
# def users():
#     _users = [{'name': 'Никанор',
#     'mail': 'nik@mail.ru',
#     'phone': '+7-987-654-32-10',
#     },
#     {'name': 'Феофан',
#     'mail': 'feo@mail.ru',
#     'phone': '+7-987-444-33-22',
#     },
#     {'name': 'Оверран',
#     'mail': 'forest@mail.ru',
#     'phone': '+7-903-333-33-33',
#     }, ]
#     context = {'users': _users}
#     return render_template('users.html', **context)
# При выводе в шаблоне используем точечную нотацию для доступа к элементам
# списка словарей.
# ...
# <body>
# <div class="row">
# <h1 class="col-12 text-monospace text-center">Список
# пользователей из БД</h1>
# {% for user in users %}
# <div class="col-12 col-md-6 col-lg-4">
# <h2>{{ user.name }}</h2>
# <p>{{ user.mail }}</p>
# <p>{{ user.phone }}</p>
# </div>
# {% endfor %}
# </div>
# </body>
# ...
# Наследование шаблонов
# Начнём с классической ситуации дублирования кода, который нарушает принцип
# DRY. Рассмотрим две html-страницы с большим объёмом одинакового кода.
# Шаблон main.html
# <!doctype html>
# <html lang="ru">
# <head>
# <meta charset="utf-8">
# <meta name="viewport" content="width=device-width,
# initial-scale=1, shrink-to-fit=no">
# 16
# <link rel="stylesheet" href="/static/css/bootstrap.min.css">
# <title>{{ title }}</title>
# </head>
# <body>
# <div class="container-fluid">
# <ul class="nav nav-pills justify-content-end align-items-end">
# <li class="nav-item"><a href="/main/"
# class="nav-link">Основная</a></li>
# <li class="nav-item"><a href="/data/"
# class="nav-link">Данные</a></li>
# </ul>
# <div class="row">
# <h1 class="col-12 col-md-6 display-2">Привет, меня зовут
# Алексей</h1>
# <img src="/static/image/foto.jpg" class="col-12 col-md-6
# img-fluid rounded-circle" alt="Моё фото">
# </div>
# <div class="row fixed-bottom modal-footer">
# <hr>
# <p>Все права защищены &copy;</p>
# </div>
# </div>
# <script src="/static/js/bootstrap.bundle.min.js"></script>
# </body>
# </html>
# Шаблон data.html
# <!doctype html>
# <html lang="ru">
# <head>
# <meta charset="utf-8">
# <meta name="viewport" content="width=device-width,
# initial-scale=1, shrink-to-fit=no">
# <link rel="stylesheet" href="/static/css/bootstrap.min.css">
# <title>{{ title }}</title>
# </head>
# <body>
# <div class="container-fluid">
# <ul class="nav nav-pills justify-content-end align-items-end">
# <li class="nav-item"><a href="/main/"
# 17
# class="nav-link">Основная</a></li>
# <li class="nav-item"><a href="/data/"
# class="nav-link">Данные</a></li>
# </ul>
# <div class="row">
# <div class="col-12 col-md-6 col-lg-4">
# <p>Lorem ipsum dolor sit amet, consectetur adipisicing
# elit. Culpa, fugiat obcaecati? Dignissimos earum facilis incidunt
# modi, molestias mollitia nam quis recusandae voluptatum?</p>
# </div>
# <div class="col-12 col-md-6 col-lg-4">
# <p> Dicta id officia quibusdam vel voluptates. Ad
# adipisci aliquid animi architecto commodi deleniti dolor
# doloremque facilis fugiat hic illo nam odit officia placeat
# provident quam quisquam quo reiciendis repudiandae sint suscipit
# unde, velit voluptatem! </p>
# </div>
# <div class="col-12 col-md-6 col-lg-4">
# <p>Ab accusamus delectus et expedita id iste,
# laboriosam optio quam, recusandae sed veritatis voluptate!
# Accusamus blanditiis debitis et tempora. Ab architecto asperiores
# aut consequuntur distinctio earum iusto nihil, non odit quidem
# soluta veniam.</p>
# </div>
# </div>
# <div class="row fixed-bottom modal-footer">
# <hr>
# <p>Все права защищены &copy;</p>
# </div>
# </div>
# <script src="/static/js/bootstrap.bundle.min.js"></script>
# </body>
# </html>
# Для того, чтобы выводить эту пару страниц достаточно несколько строк кода на
# Flask
# @app.route('/main/')
# def main():
# context = {'title': 'Главная'}
# return render_template('main.html', **context)
# 18
# @app.route('/data/')
# def data():
# context = {'title': 'База статей'}
# return render_template('data.html', **context)
# На каждой странице всего несколько различных строк в середине. Остальной код
# дублируется, Представьте, что у вас большой проект на десятки аналогичных
# страниц. Сколько же времени вы затратите, чтобы изменить шапку или футер во
# всём проекте?
# Базовый и дочерние шаблоны
# Создадим базовый шаблон base.html, который будет включать весь одинаковый
# код.
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
# <ul class="nav nav-pills justify-content-end align-items-end">
# <li class="nav-item"><a href="/main/"
# class="nav-link">Основная</a></li>
# <li class="nav-item"><a href="/data/"
# class="nav-link">Данные</a></li>
# </ul>
# {% block content %}
# Страница не заполнена
# {% endblock %}
# <div class="row fixed-bottom modal-footer">
# 19
# <hr>
# <p>Все права защищены &copy;</p>
# </div>
# </div>
# <script src="/static/js/bootstrap.bundle.min.js"></script>
# </body>
# </html>
# Исключённый текст для заголовка сайта был заменён на:
# {% block title %} Мой сайт {% endblock %}
# Для содержимого страницы код заменён на:
# {% block content %}
# Страница не заполнена
# {% endblock %}
# Количество блоков в базовом шаблоне и их названия зависят от задачи, которую
# решает разработчик. Содержимое внутри block впоследствии будет заполнено
# дочерними шаблонами. Инструкция block принимает один аргумент — название
# блока. Внутри шаблона это название должно быть уникальным, иначе возникнет
# ошибка.
# Если в дочернем шаблоне блок отсутствует, выводится информация из базового
# шаблона. В нашем примере, если в дочернем шаблоне не прописать блок title, будет
# выведено значение «Мой сайт» из базового шаблона, а вместо содержимого увидим
# что “Страница не заполнена”
# Теперь из main.html и data.html можно удалить дублирующиеся строки и указать,
# что эти шаблоны расширяют базовый.
# Шаблон main.html
# {% extends 'base.html' %}
# {% block title %}
# {{ super() }} - {{ title }}
# {% endblock %}
# {% block content %}
# <div class="row">
# <h1 class="col-12 col-md-6 display-2">Привет, меня зовут
# Алексей</h1>
# <img src="/static/image/foto.jpg" class="col-12 col-md-6
# 20
# img-fluid rounded-circle" alt="Моё фото">
# </div>
# {% endblock %}
# Шаблон data.html
# {% extends 'base.html' %}
# {% block title %}
# {{ super() }} - {{ title }}
# {% endblock %}
# {% block content %}
# <div class="row">
# <div class="col-12 col-md-6 col-lg-4">
# <p>Lorem ipsum dolor sit amet, consectetur adipisicing
# elit. Culpa, fugiat obcaecati? Dignissimos earum facilis incidunt
# modi, molestias mollitia nam quis recusandae voluptatum?</p>
# </div>
# <div class="col-12 col-md-6 col-lg-4">
# <p> Dicta id officia quibusdam vel voluptates. Ad
# adipisci aliquid animi architecto commodi deleniti dolor
# doloremque facilis fugiat hic illo nam odit officia placeat
# provident quam quisquam quo reiciendis repudiandae sint suscipit
# unde, velit voluptatem! </p>
# </div>
# <div class="col-12 col-md-6 col-lg-4">
# <p>Ab accusamus delectus et expedita id iste,
# laboriosam optio quam, recusandae sed veritatis voluptate!
# Accusamus blanditiis debitis et tempora. Ab architecto asperiores
# aut consequuntur distinctio earum iusto nihil, non odit quidem
# soluta veniam.</p>
# </div>
# </div>
# {% endblock %}
# Содержимое одноимённых блоков в дочерних шаблонах будет подставлено в
# соответствующее место базового.
# 🔥 Внимание! Использование переменной {{ super() }} в дочерних шаблонах
# позволяет выводить содержимое родительского блока, а не заменять его!
# 21
# После такой оптимизации достаточно внести изменение в базовом шаблоне, чтобы
# обновить одинаковую информацию на всех страницах сайта.
# Дочерние шаблоны компакты и содержат только специфичную для страницы
# информацию. А при отрисовке через Jinja в них легко передавать динамически
# изменяемую информацию.
# 🔥 Важно! Сохранять текстовую информацию внутри html файла как в
# data.html нелогично. Она должна храниться в базе данных. А шаблон в этом
# случае может получать её через контекст и выводить в цикле.
# Вывод
# На этой лекции мы:
# 1. Узнали о фреймворке Flask
# 2. Разобрались в установке и настройке Flask для первого запуска
# 3. Изучили работу функций представлений - view
# 4. Узнали о способах передачи html кода от сервера клиенту
# 5. Изучили работу с шаблонизатором Jinja
# 6. Разобрались с наследованием шаблонов
