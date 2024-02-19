# Погружение во Flask
# На этой лекции мы продолжим знакомиться с фреймворком Flask и разберём ряд
# тонкостей и особенностей в работе с ним. Начнём с основ безопасности.
# Экранирование пользовательских данных
# Начнём занятие с того, что не каждый пользователь будет делать то, что вы от него
# хотите. Например попросим пользователя передать путь до файла в адресной
# строке.
# @app.route('/')
# def index():
#     return 'Введи путь к файлу в адресной строке'
# @app.route('/<path:file>/')
# def get_file(file):
#     print(file)
#     return f'Ваш файл находится в: {file}!'
# А теперь вместо пути, передадим следующую строку:
# http://127.0.0.1:5000/<script>alert("I am haсker")</script>/
# 3
# На страницу будет выведен текст без пути. И одновременно сработает js скрипт с
# всплывающим сообщением о хакере. А ведь код может быть не таким безобидным
# как в примере.
# Для повышения безопасности необходимо экранировать пользовательский ввод.
# Для этого используйте функцию escape из модуля markupsafe.
# ...
# from markupsafe import escape
# ...
# @app.route('/<path:file>/')
# def get_file(file):
#     return f'Ваш файл находится в: {escape(file)}!'