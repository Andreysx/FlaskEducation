from flask import Flask, render_template, flash
from Lesson_3.Semminar_3.models import db, Student, Faculty, Author, Book, Student2, Score
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = '4c56f4b4da7a923891161ffc2531816d161cd48dfec0fd3a8caec2d236171e72'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

db.init_app(app)


# Задача 1 Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


# @app.cli.command('fill-t1')
# def fill_task1_tables():
#     for i in range(1, 6):
#         new_faculty = Faculty(name=f"Faculty_{i}")
#         db.session.add(new_faculty)
#     db.session.commit()
#
#     for i in range(1, 11):
#         new_student = Student(first_name=f'First_name{i}', last_name=f'Last_name{i}', age=random.randint(10, 90),
#                               gender=random.choice([True, False]), group=random.randint(100, 200),
#                               faculty_id=random.randint(1, 5))
#         db.session.add(new_student)
#     db.session.commit()
#     print("ok")


@app.route('/')
@app.route('/index')
def index():
    return render_template('indextask1.html')


# @app.route('/task1/')
# def task1_index():
#     students = Student.query.all()
#     return render_template('indextask1.html', students=students, title="task1")


# Задание №2
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.
#
# @app.cli.command('fill-t2')
# def fill_task1_tables():
#     for i in range(1, 6):
#         new_author = Author(first_name=f"Имя {i}",
#                             last_name=f"Фамилия {i}")
#         db.session.add(new_author)
#     db.session.commit()
#     print("OK")
#
#     for i in range(1, 21):
#         new_book = Book(name=f"Книга {i}",
#                         year=random.randint(1900, 2000),
#                         count=random.randint(1, 5),
#                         author_id=random.randint(1, 5))
#         db.session.add(new_book)
#     db.session.commit()
#     print("OK")
#
#
# @app.route('/task2/')
# def task2_index():
#     books = Book.query.all()
#     return render_template('indextask2.html', books=books, title="task2")


# Задание №3
# Доработаем задача про студентов
# Создать базу данных для хранения информации о студентах и их оценках в
# учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
# и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название
# предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их оценок.

@app.cli.command('fill-t3')
def fill_task3_tables():
    for i in range(1, 6):
        new_score = Score(name=f"Название предмета {i}",
                          value=random.randint(1, 5),
                          student2_id=random.randint(1, 10))
        db.session.add(new_score)
    db.session.commit()
    print("OK")
    for i in range(1, 10):
        new_student2 = Student2(first_name=f'First_name{i}',
                                last_name=f'Last_name{i}',
                                group=random.randint(1, 5),
                                email=f'Email{i}')
        db.session.add(new_student2)
    db.session.commit()
    print("ok")



@app.route('/task3/')
def task1_index():
    students2 = Student2.query.all()
    return render_template('indextask3.html', students2=students2, title="task3")
