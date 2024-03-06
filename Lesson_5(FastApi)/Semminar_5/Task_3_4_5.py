# Задание №3
# Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Создайте маршрут для обновления информации о пользователе (метод PUT).
# Создайте маршрут для удаления информации о пользователе (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    password: str


users = []

for i in range(0, 11):
    new_user = User(
        id=i,
        name=f"Username: {i}",
        email=f"Email: {i}",
        password=f"Password:"
    )
    users.append(new_user)


@app.get("/users/")
async def get_users():
    return users


@app.post("/users/")
async def add_user(user: User):
    users.append(user)
    return user


@app.put("/users/")
async def change_user(user_id: int, user: User):
    for i, m in enumerate(users):
        if m.id == user_id:
            users[i] = user
            return user
    return {"message": "user not found"}


@app.delete("/users/")
async def delete_user(user_id: int):
    """
    Целесообразнее использовать поле is_deleted(True,False) в реальном проекте
    Чтобы не удалять данные пользователя из БД в случае ситуации восстановления аккаунта
    :param user_id:
    :return:
    """
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"message": "user has been deleted"}
    return {"message": "user not found"}
