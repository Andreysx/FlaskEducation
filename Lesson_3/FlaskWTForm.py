# Flask-WTForm
# Введение
#
# Flask-WTForm — это модуль для Flask, который предоставляет инструменты для
# работы с формами веб-приложений на Python. Flask-WTForm позволяет легко
# создавать и обрабатывать формы, валидировать данные, защищать приложение от
# атак CSRF и многое другое.
# Зачем использовать Flask-WTF?
# Создание форм вручную может быть утомительным и трудоемким процессом,
# особенно если вы хотите создать несколько форм. Flask-WTF упрощает этот
# процесс, предоставляя множество инструментов, которые позволяют быстро
# создавать и обрабатывать формы.
# Кроме того, Flask-WTF предоставляет механизмы валидации данных, что позволяет
# легко проверять правильность заполнения формы. Это особенно важно при работе
# с конфиденциальной информацией, такой как пароли или номера кредитных карт.
#
# Flask-WTF также обеспечивает защиту от атак CSRF (межсайтовой подделки
# запросов), что является важным аспектом безопасности веб-приложений.
# Установка и настройка
# Установка Flask-WTF
# Для установки Flask-WTF необходимо выполнить команду:
# pip install Flask-WTF
#
# После установки модуля его можно импортировать в приложение Flask:
# from flask_wtf import FlaskForm
# Настройка защиты от CSRF-атак
# Защита от CSRF-атак в Flask-WTF осуществляется с помощью генерации токена,
# который добавляется к каждой форме. При отправке формы этот токен проверяется
# на сервере, чтобы убедиться, что запрос был отправлен с того же сайта.
# Для включения защиты от CSRF-атак в Flask-WTF необходимо установить секретный
# ключ приложения. Этот ключ используется для генерации токена и должен быть
# достаточно длинным и случайным.
#
# Рассмотрим пример настройки защиты от CSRF-атак:
# from flask_wtf.csrf import CSRFProtect
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'mysecretkey'
# csrf = CSRFProtect(app)
# В этом примере мы создаем объект csrf и передаем ему приложение Flask. Затем мы
# устанавливаем секретный ключ приложения. После этого защита от CSRF-атак
# будет включена для всех форм в приложении.
#
# Если вы хотите отключить защиту от CSRF-атак для определенной формы, вы
# можете использовать декоратор csrf.exempt:
# from flask_wtf.csrf import CSRFProtect
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'mysecretkey'
# csrf = CSRFProtect(app)
#
# @app.route('/form', methods=['GET', 'POST'])
# @csrf.exempt
# def my_form():
#     ...
# В этом примере мы используем декоратор exempt объекта csrf для отключения
# защиты от CSRF-атак для формы, которая обрабатывается в функции my_form().
# Защита от CSRF-атак является важным аспектом безопасности веб-приложений.
# Flask-WTF предоставляет простые и эффективные механизмы защиты от таких атак,
# которые можно легко настроить в приложении Flask.
# Создание форм в WTForms
#
# WTForms — это библиотека Python, которая позволяет создавать HTML-формы, а
# также проводить их валидацию. Flask-WTF использует WTForms для создания форм.
# Определение классов форм
#
#
# Для создания формы с помощью Flask-WTF необходимо определить класс формы,
# который наследуется от класса FlaskForm. Каждое поле формы определяется как
# экземпляр класса, который наследуется от класса Field.
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField
# from wtforms.validators import DataRequired
# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
# В данном примере определен класс LoginForm, который наследуется от FlaskForm.
# Внутри класса определены два поля: username и password. Поле username является
# строковым полем, а поле password — полем для ввода пароля. Оба поля
# обязательны для заполнения, так как им передан валидатор DataRequired.
# Описание полей форм
#
#
# WTForms предоставляет множество типов полей для формы. Вот некоторые из них:
# ● StringField — строковое поле для ввода текста;
# ● IntegerField — числовое поле для ввода целочисленных значений;
# ● FloatField — числовое поле для ввода дробных значений;
# ● BooleanField — чекбокс;
# ● SelectField — выпадающий список;
# ● DateField — поле для ввода даты;
# ● FileField — поле для загрузки файла.
#
#
# Рассмотрим ещё один пример создания форм:
# from flask_wtf import FlaskForm
# from wtforms import StringField, IntegerField, SelectField
# from wtforms.validators import DataRequired
# class RegisterForm(FlaskForm):
#     name = StringField('Name', validators=[DataRequired()])
#     age = IntegerField('Age', validators=[DataRequired()])
#     gender = SelectField('Gender', choices=[('male', 'Мужчина'), ('female', 'Женщина')])
# В данном примере определен класс RegisterForm, который наследуется от
# FlaskForm. Внутри класса определены три поля: name, age и gender. Поле name
# является строковым полем, поле age — числовым, а поле gender — выпадающим
# списком. В списке выбора есть две опции: male и female.
# Валидация данных формы
# WTForms позволяет проводить валидацию данных формы. Для этого можно
# использовать готовые валидаторы, такие как DataRequired, Email, Length и другие.
# Также можно написать свой собственный валидатор.
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField
# from wtforms.validators import DataRequired, Email, EqualTo
# class RegistrationForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#
# В данном примере определен класс RegistrationForm, который наследуется от
# FlaskForm. Внутри класса определены три поля: email, password и confirm_password.
# Поле email проверяется на наличие данных и на соответствие формату email. Поле
# password проверяется на наличие данных и на минимальную длину (6 символов).
# Поле confirm_password проверяется на наличие данных и на соответствие значению
# поля password.
# 🔥 Важно! Для правильной работы кода необходимо отдельно установить
# валидатор электронной почты. Для этого достаточно выполнить команду:
# pip install email-validator
# 💡 Внимание! В валидатор EqualTo передаётся строковое имя переменной,
# т.е. то, что стоит слева от знака равно, а не название поля
# WTForms — мощная библиотека для создания HTML-форм и их валидации в Flask.
# Определение классов форм является основой работы с библиотекой. Описание
# полей форм и проведение их валидации позволяют создавать надежные и удобные
# для пользователей формы.
# Использование форм WTForms в приложении
# В предыдущем пункте мы рассмотрели, как создавать формы с помощью WTForms.
# Теперь рассмотрим, как использовать эти формы в приложении Flask.
# Отображение форм на страницах приложения
# Для отображения формы на странице приложения необходимо создать объект
# формы в представлении и передать его в шаблон.
# from flask import render_template, request
# from forms import LoginForm
# @app.route('/login/', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if request.method == 'POST' and form.validate():
# # Обработка данных из формы
#         pass
#     return render_template('login.html', form=form)
#
# В данном примере определен маршрут /login, который обрабатывает GET и POST
# запросы. В представлении создается объект LoginForm, который передается в
# шаблон login.html с помощью функции render_template. Если метод запроса POST и
# данные формы проходят валидацию, то выполняется обработка данных из формы.
# Шаблон login.html должен содержать тег form с указанием метода и адреса для
# отправки данных формы, а также поля формы с помощью тегов input.
# {% extends "base.html" %}
# {% block content %}
# <h1>Login</h1>
# <form method="POST" action="{{ url_for('login') }}">
# {{ form.csrf_token }}
# <p>
# {{ form.username.label }}<br>
# {{ form.username(size=32) }}
# </p>
# <p>
# {{ form.password.label }}<br>
# {{ form.password(size=32) }}
# </p>
# <p>
# <input type="submit" value="Login">
# </p>
# </form>
# {% endblock %}
# Внутри блока content определен тег form с методом POST и адресом /login. Для
# каждого поля формы вызывается соответствующий метод объекта формы
# (например, form.username для поля username) с указанием размера поля.
#
#
# Обработка данных из формы
# Для обработки данных из формы необходимо получить данные из объекта request и
# провести их валидацию с помощью метода validate() объекта формы.
# from flask import render_template, request
# from forms import RegistrationForm
# @app.route('/register/', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if request.method == 'POST' and form.validate():
#     # Обработка данных из формы
#         email = form.email.data
#         password = form.password.data
#         print(email, password)
#         ...
#     return render_template('register.html', form=form)
#
# В данном примере определен маршрут /register, который обрабатывает GET и POST
# запросы. В представлении создается объект RegistrationForm, который передается в
# шаблон register.html с помощью функции render_template. Если метод запроса POST
# и данные формы проходят валидацию, то выполняется обработка данных из формы.
# Данные из полей формы можно получить с помощью свойств data объекта формы.
# Например, для поля email можно получить значение следующим образом:
# form.email.data.
# Рассмотрим шаблон register.html
# {% extends "base.html" %}
# {% block content %}
# <h1>Login</h1>
# <form method="POST" action="{{ url_for('register') }}">
# {{ form.csrf_token }}
# {% for field in form if field.name != 'csrf_token' %}
# <p>
# {{ field.label }}<br>
# {{ field }}
# {% if field.errors %}
# <ul class="alert alert-danger">
# {% for error in field.errors %}
# <li>{{ error }}</li>
# {% endfor %}
# </ul>
# {% endif %}
# </p>
# {% endfor %}
# <p>
# <input type="submit" value="Register">
# </p>
# </form>
# {% endblock %}
# В отличии от шаблона login.html мы не указываем поля явно. После стандартного
# вывода csrf токена создаём цикл для по всем полям формы за исключением токена.
# Для каждого поля выводится метка и окно поле ввода. Отдельно проверяем
# наличие ошибок ввода и если они есть, в цикле выводим все ошибки для каждого
# из полей. Таким образом мы динамически формируем страницу регистрации. А в
# случае неверного ввода данных пользователем, сразу сообщаем ему об ошибках.
# WTForms позволяет легко создавать и валидировать HTML-формы в приложении
# Flask. Для отображения форм на страницах приложения необходимо создать объект
# формы в представлении и передать его в шаблон. Для обработки данных из формы
# необходимо получить данные через post запрос и провести их валидацию с
# помощью метода validate() объекта формы.
# Заключение по работе с WTForms
# WTForms — это мощный инструмент для создания и валидации HTML-форм в
# приложении Flask. Он позволяет легко определять поля формы, устанавливать
# правила валидации и обрабатывать данные из формы.
# Мы рассмотрели основные возможности WTForms и показали, как его использовать
# в приложении Flask. Мы создали простую форму входа и форму регистрации, а
# также рассмотрели процесс валидации данных из формы.
# WTForms имеет множество дополнительных функций, таких как поддержка
# многоязычности, кастомизация полей формы и многое другое. Вы можете
# ознакомиться с дополнительными возможностями в официальной документации
# WTForms.
# Использование WTForms в приложении Flask позволяет значительно упростить
# процесс создания и валидации HTML-форм. Это помогает сократить время
# разработки и повысить качество кода.