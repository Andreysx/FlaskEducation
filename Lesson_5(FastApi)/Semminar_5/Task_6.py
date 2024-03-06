# Задание №6
# Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.


from fastapi import FastAPI,Request
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="./Lesson_5(FastApi)/Semminar_5/templates")



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


@app.get("/show_users/", response_class=HTMLResponse)
async def show_users(request: Request, users_table: list):
    return templates.TemplateResponse("index.html", {"request": request, "users": users_table})


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
