# Задание №2
# Создать веб-приложение на FastAPI, которое будет предоставлять API для
# работы с базой данных пользователей. Пользователь должен иметь
# следующие поля:
# ○ ID (автоматически генерируется при создании пользователя)
# ○ Имя (строка, не менее 2 символов)
# ○ Фамилия (строка, не менее 2 символов)
# ○ Дата рождения (строка в формате "YYYY-MM-DD")
# ○ Email (строка, валидный email)
# ○ Адрес (строка, не менее 5 символов)
# Задание №2 (продолжение)
# API должен поддерживать следующие операции:
# ○ Добавление пользователя в базу данных
# ○ Получение списка всех пользователей в базе данных
# ○ Получение пользователя по ID
# ○ Обновление пользователя по ID
# ○ Удаление пользователя по ID
# Приложение должно использовать базу данных SQLite3 для хранения
# пользователей.
import databases
import sqlalchemy
from fastapi import FastAPI
from typing import List
from models_task2 import User, UserIn
from faker import Faker
import datetime

DATABASE_URL = "sqlite:///mydatabase2.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(32)),
    sqlalchemy.Column("lastname", sqlalchemy.String(32)),
    sqlalchemy.Column("birthday", sqlalchemy.DATE()),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("adress", sqlalchemy.String(32)),
    )

engine = sqlalchemy.create_engine(
    DATABASE_URL
    )

metadata.create_all(engine)

fake = Faker("ru_RU") # ru - language, RU - country

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        username = fake.first_name()
        lastname = fake.last_name()
        print (fake.date())
        print(type(fake.date()))
        birthday = datetime.datetime.strptime(fake.date(), '%Y-%m-%d')
        email = fake.unique.email()
        adress = fake.address()
        query = users.insert().values(username=username, lastname=lastname, birthday=birthday,email=email, adress=adress)
        await database.execute(query)
    return {'message': f'{count} fake users create'}


@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}

# if __name__ == "__main__":
# uvicorn.run("task:app", port=8000)