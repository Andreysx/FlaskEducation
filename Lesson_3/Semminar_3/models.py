from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    students = db.relationship('Student', backref='faculty', lazy=True)


def __repr__(self):
    return f"Faculty({self.id}, {self.name})"


# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Boolean, nullable=False)
    group = db.Column(db.Integer, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)


def __repr__(self):
    return f"Student({self.id}, {self.first_name}, {self.last_name}, {self.age}, {self.gender}, {self.group})"


# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False, default=1)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)


