# Flask-SQLAlchemy
# Введение
# ➢Что такое Flask-SQLAlchemy?
# Flask-SQLAlchemy — это расширение Flask, которое облегчает работу с базами
# данных в приложениях, написанных на Flask. Оно предоставляет удобный
# интерфейс для работы с базами данных, а также мощные инструменты для
# создания и управления моделями данных.
#
# ➢Зачем использовать Flask-SQLAlchemy?
# Безусловно, использование баз данных является неотъемлемой частью многих
# веб-приложений. Flask-SQLAlchemy позволяет легко и быстро создавать и
# управлять базами данных, что делает его идеальным выбором для разработки
# веб-приложений любого уровня сложности.
# Кроме того, Flask-SQLAlchemy обладает множеством преимуществ по сравнению с
# другими ORM-библиотеками. Он предоставляет более простой и понятный
# синтаксис для работы с базами данных, а также обладает отличной
# производительностью и масштабируемостью.
# Пример использования Flask-SQLAlchemy можно привести на основе создания
# блога. В блоге нужно хранить информацию о пользователях, статьях, комментариях
# и т.д. Flask-SQLAlchemy поможет легко создать и управлять базой данных для
# хранения всех этих данных.
# Установка и настройка
#
# ➢Установка Flask-SQLAlchemy
# Для установки Flask-SQLAlchemy необходимо выполнить команду:
# pip install Flask-SQLAlchemy # Widows
# pip3 install Flask-SQLAlchemy # Unix
#
# После этого можно импортировать его в свой проект:
# from flask_sqlalchemy import SQLAlchemy
#
# ➢Настройка подключения к базе данных
# Для настройки подключения к базе данных необходимо указать адрес базы данных,
# а также ее тип и некоторые другие параметры. Например, для подключения к базе
# данных SQLite можно использовать следующий код:
#
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# db = SQLAlchemy(app)
# ...
#
# В данном примере мы создаем объект app класса Flask, указываем адрес базы
# данных в параметре SQLALCHEMY_DATABASE_URI и создаем объект db класса
# SQLAlchemy.
# Адрес базы данных может быть различным в зависимости от ее типа и места
# расположения. В данном примере мы используем базу данных SQLite, которая
# хранится в файле mydatabase.db в текущей директории.
# Также можно использовать другие типы баз данных, такие как MySQL, PostgreSQL и
# другие. Для этого необходимо указать соответствующий адрес и параметры
# подключения.
# Например, для подключения к базе данных MySQL можно использовать следующий
# код:
# ...
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =
# 'mysql+pymysql://username:password@hostname/database_name'
# db = SQLAlchemy(app)
# ...
# Здесь мы указываем адрес базы данных в формате:
# mysql+pymysql://username:password@hostname/database_name, где
# username и password - это логин и пароль для подключения к базе данных,
# hostname - адрес сервера базы данных, а database_name - имя базы данных.
# При подключении к PostgreSQL используется аналогичная строка. Изменяется лишь
# начало:
# postgresql+psycopg2://username:password@hostname/database_name
# ➢Разделение проекта на отдельные компоненты
# Чтобы Flask проект не превратился один файл гигантского размера, вынесем работу
# с БД в отдельный файл models.py.
# На текущем этапе в нём будут следующие строки:
#
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
#
# Внутри основного файла проекта оставим следующий код:
#
# from flask import Flask
# from flask_lesson_3.models import db
# app = Flask(__name__
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# db.init_app(app)
# 🔥 Важно! Теперь класс не получает приложение Flask app при
# инициализации. Для инициализации баз данных необходимо выполнить
# строку db.init_app(app)
# Создание моделей
# При работе с Flask-SQLAlchemy необходимо определить модели данных, которые
# будут использоваться в приложении. Модель - это класс, который описывает
# структуру таблицы в базе данных.
# ➢Определение классов моделей
# Для определения модели необходимо создать класс, который наследует от класса
# Model из библиотеки SQLAlchemy. Название класса должно соответствовать
# названию таблицы в базе данных.
# Наполняем кодом models.py
# Пример:
#
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# db = SQLAlchemy()
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
# def __repr__(self):
#     return f'User({self.username}, {self.email})'
# В этом примере определена модель User, которая имеет четыре поля: id, username,
# email и created_at. Поле id является первичным ключом таблицы и автоматически
# генерируется при добавлении записи в таблицу. Поля username и email являются
# строками с ограничением на уникальность и обязательность заполнения. Поле
# created_at содержит дату и время создания записи и автоматически заполняется
# текущей датой и временем при добавлении записи.
#
# ➢Описание полей моделей
# Для описания полей модели используются классы-типы данных из библиотеки
# SQLAlchemy. Существуют следующие типы данных:
# ● Integer — целое число
# ● String — строка
# ● Text — текстовое поле
# ● Boolean — булево значение
# ● DateTime — дата и время
# ● Float — число с плавающей точкой
# ● Decimal — десятичное число
# ● Enum — перечисление значений
# ● ForeignKey — внешний ключ к другой таблице
#
# Рассмотрим ещё один пример таблицы:
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#
# def __repr__(self):
#     return f'Post({self.title}, {self.content})'
# В этом примере определена модель Post, которая имеет пять полей: id, title, content,
# author_id и created_at. Поля title и content являются строками и обязательны для
# заполнения. Поле author_id является внешним ключом к таблице пользователей
# (User) и ссылается на поле id этой таблицы. Поле created_at содержит дату и время
# создания записи и автоматически заполняется текущей датой и временем при
# добавлении записи.
#
# К моделе пользователя добавим следующую строку:
# posts = db.relationship('Post', backref='author', lazy=True)
# Так мы (а точнее наш код) понимаем какие посты принадлежат конкретному
# пользователю.
#
# ➢Создание связей между моделями
# Для создания связей между моделями используется поле ForeignKey. Оно указывает
# на поле первичного ключа связанной таблицы.
# class Comment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text, nullable=False)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
#     author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#
# def __repr__(self):
#     return f'Comment({self.content})'
# В этом примере определена модель Comment, которая имеет пять полей: id, content,
# post_id, author_id и created_at. Поля content и post_id являются обязательными для
# заполнения. Поле post_id является внешним ключом к таблице постов (Post) и
# ссылается на поле id этой таблицы. Поле author_id является внешним ключом к
# таблице пользователей (User) и ссылается на поле id этой таблицы. Поле created_at
# содержит дату и время создания записи и автоматически заполняется текущей
# датой и временем при добавлении записи.
# ➢Создание таблиц в базе данных
# Остался финальный этап. Напишим функцию, которая создаст таблицы через
# консольную команду. Заполняем основной файл проекта
# ...
# from flask_lesson_3.models import db, User, Post, Comment
# ...
# @app.cli.command("init-db")
# def init_db():
#     db.create_all()
#     print('OK')
#     ...
#
# Из models импортировали все созданные классы таблиц. Без этого импорта
# функция create_all может не увидеть какие таблицу необходимо создать.
# Далее создали функцию, которая будет вызвана командой в консоли:
# flask init-db
# 🔥 Внимание! Если команда в консоли выдает ошибку, проверьте что у вас
# есть wsgi.py файл в корневой директории проекта и он верно работает.
# Например его код может быть таким:
# from flask_lesson_3.app_01 import app
# if __name__ == '__main__':
#     app.run(debug=True)
#
# Мы рассмотрели основные аспекты создания моделей в Flask-SQLAlchemy. Были
# описаны классы моделей, поля моделей и создание связей между моделями.
#
#
# Работа с данными
# После определения моделей в Flask-SQLAlchemy можно начать работу с данными в
# базе данных. Давайте рассмотрим основные методы для создания, изменения и
# удаления записей, а также получения данных из базы данных и их фильтрацию.
#
#
# ➢Создание записей
# Для создания новой записи в базе данных необходимо создать объект модели и
# добавить его в сессию базы данных. После этого нужно вызвать метод commit() для
# сохранения изменений.
# ...
# @app.cli.command("add-john")
# def add_user():
#     user = User(username='john', email='john@example.com')
#     db.session.add(user)
#     db.session.commit()
#     print('John add in DB!')
#
#
# В этом примере создается новый объект модели User с именем пользователя "john"
# и электронной почтой "john@example.com". Затем объект добавляется в сессию
# базы данных и сохраняется с помощью метода commit().
# Как вы уже догадались для выполнения функции необходимо выполнить в консоли
# команду flask add-john
#
#
# ➢Изменение записей
# Для изменения существующей записи нужно получить ее из базы данных, изменить
# нужные поля и вызвать метод commit().
# ...
# @app.cli.command("edit-john")
# def edit_user():
#     user = User.query.filter_by(username='john').first()
#     user.email = 'new_email@example.com'
#     db.session.commit()
#     print('Edit John mail in DB!')
#     ...
# В этом примере получаем объект модели User по имени пользователя "john",
# изменяем его электронную почту на "new_email@example.com" и сохраняем
# изменения с помощью метода commit().
# 🔥 Внимание! Если бы база данных позволяла хранить несколько
# пользователей с одинаковыми username, в переменную user попал бы один
# пользователь благодаря методу first().
#
#
# ➢Удаление записей
# Для удаления записи нужно получить ее из базы данных, вызвать метод delete() и
# затем вызвать метод commit().
# ...
# @app.cli.command("del-john")
# def del_user():
#     user = User.query.filter_by(username='john').first()
#     db.session.delete(user)
#     db.session.commit()
#     print('Delete John from DB!')
#     ...
#
# В этом примере получаем объект модели User по имени пользователя "john",
# удаляем его из базы данных с помощью метода delete() и сохраняем изменения с
# помощью метода commit().
#
#
# ➢Наполнение тестовыми данными
# Перед тем как двигаться добавим в базу несколько тестовых пользователей и их
# статей.
# @app.cli.command("fill-db")
# def fill_tables():
#     count = 5
#     # Добавляем пользователей
#     for user in range(1, count + 1):
#         new_user = User(username=f'user{user}', email=f'user{user}@mail.ru')
#         db.session.add(new_user)
#     db.session.commit()
#     # Добавляем статьи
#     for post in range(1, count ** 2):
#         author = User.query.filter_by(username=f'user{post % count + 1}').first()
#         new_post = Post(title=f'Post title {post}', content=f'Post content {post}', author=author)
#         db.session.add(new_post)
#     db.session.commit()
# Вначале мы записываем в БД count пользователей. А далее генерируем статье,
# которые они написали.
#
#
# ➢Получение данных из базы данных
# Для получения данных из базы данных необходимо использовать метод query()
# модели. Этот метод возвращает объект запроса, который можно дополнить
# фильтрами и другими параметрами.
# ...
# @app.route('/users/')
# def all_users():
#     users = User.query.all()
#     context = {'users': users}
#     return render_template('users.html', **context)
#
#
# В этом примере получаем все объекты модели User из базы данных с помощью
# метода all(). Пробросим их в шаблон, где выводим имена пользователей и
# электронные адреса.
#
# {% extends 'base.html' %}
# {% block title %}
# {{ super() }} - {{ title }}
# {% endblock %}
# {% block content %}
# <div class="row">
# {% for user in users %}
# <p class="col-12 col-md-6">Имя пользователя: {{
# user.username }}<br>
# Email пользователя: {{ user.email }}</p>
# {% endfor %}
# </div>
# {% endblock %}
# ➢Фильтрация данных
# Для фильтрации данных можно использовать метод filter() объекта запроса. Этот
# метод принимает условия фильтрации в виде аргументов или объектов-атрибутов
# модели.
# ...
# @app.route('/users/<username>/')
# def users_by_username(username):
#     users = User.query.filter(User.username == username).all()
#     context = {'users': users}
#     return render_template('users.html', **context)
#
# В этом примере получаем все объекты модели User из базы данных, у которых имя
# пользователя равно username из строки запроса, с помощью метода filter() и
# выводим их имена пользователей и электронные адреса используя прежний
# шаблон.
#
#
# Рассмотрим ещё один вариант фильтрации данных
# @app.route('/posts/author/<int:user_id>/')
# def get_posts_by_author(user_id):
#     posts = Post.query.filter_by(author_id=user_id).all()
#     if posts:
#         return jsonify([{'id': post.id, 'title': post.title,'content': post.content, 'created_at': post.created_at} for post in posts])
#     else:
#         return jsonify({'error': 'Posts not found'})
#
# Мы создаем маршрут /posts/author/<int:user_id>, который принимает ID
# пользователя в качестве параметра. Внутри маршрута мы используем метод
# filter_by для фильтрации постов по ID автора и метод all для получения всех
# найденных постов. Если посты найдены, мы возвращаем их данные в формате
# JSON, иначе возвращаем ошибку.
#
# 🔥 Внимание! Для того, чтобы вернуть JSON объект используется функция
# jsonify. Её необходимо импортировать из модуля Flask перед
# использованием.
#
#
# Финальный пример фильтрации данных
# @app.route('/posts/last-week/')
# def get_posts_last_week():
#     date = datetime.utcnow() - timedelta(days=7)
#     posts = Post.query.filter(Post.created_at >= date).all()
#     if posts:
#         return jsonify([{'id': post.id, 'title': post.title,'content': post.content, 'created_at': post.created_at} for post in posts])
#     else:
#         return jsonify({'error': 'Posts not found'})
# Создаем маршрут /posts/last-week, который возвращает все посты, созданные за
# последнюю неделю. Внутри маршрута мы используем модуль datetime для
# вычисления даты, которая была неделю назад, и метод filter для фильтрации постов
# по дате создания. Если посты найдены, мы возвращаем их данные в формате JSON,
# иначе возвращаем ошибку.
#
# 🔥 Важно! Для работы без ошибок, добавьте строку импорта в начале файла:
# from datetime import datetime, timedelta
# Заключение по работе с Flask-SQLAlchemy
# Flask-SQLAlchemy — это мощный инструмент для работы с базами данных в
# приложениях Flask. Он предоставляет простой и удобный интерфейс для создания
# моделей, выполнения запросов и управления данными.
# Мы рассмотрели основные функции Flask-SQLAlchemy, такие как создание моделей,
# работу с данными, получение и фильтрацию данных. Мы также рассмотрели
# создание запросов к базе данных с помощью SQLAlchemy ORM.
# Flask-SQLAlchemy позволяет разработчикам быстро и легко создавать и
# поддерживать базы данных в своих приложениях Flask. Он также обеспечивает
# безопасность и надежность работы с данными.
