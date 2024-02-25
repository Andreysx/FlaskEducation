from flask import Flask, render_template, flash
from Lesson_3.Semminar_3.models import db, Student, Faculty, Author, Book
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


@app.cli.command('fill-t1')
def fill_task1_tables():
    for i in range(1, 6):
        new_faculty = Faculty(name=f"Faculty_{i}")
        db.session.add(new_faculty)
    db.session.commit()

    for i in range(1, 11):
        new_student = Student(first_name=f'First_name{i}', last_name=f'Last_name{i}', age=random.randint(10, 90),
                              gender=random.choice([True, False]), group=random.randint(100, 200),
                              faculty_id=random.randint(1, 5))
        db.session.add(new_student)
    db.session.commit()
    print("ok")


@app.route('/')
@app.route('/index')
def index():
    return render_template('indextask1.html')


@app.route('/task1/')
def task1_index():
    students = Student.query.all()
    return render_template('indextask1.html', students=students, title="task1")


# Задание №2
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.

@app.cli.command('fill-t2')
def fill_task1_tables():
    for i in range(1, 6):
        new_author = Author(first_name=f"Имя {i}",
                            last_name=f"Фамилия {i}")
        db.session.add(new_author)
    db.session.commit()
    print("OK")

    for i in range(1, 21):
        new_book = Book(name=f"Книга {i}",
                        year=random.randint(1900, 2000),
                        count=random.randint(1, 5),
                        author_id=random.randint(1, 5))
        db.session.add(new_book)
    db.session.commit()
    print("OK")


@app.route('/task2/')
def task2_index():
    books = Book.query.all()
    return render_template('indextask2.html', books=books, title="task2")
