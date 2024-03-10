# Задание №3
# Создать API для управления списком задач.
# Каждая задача должна содержать поля "название",
# "описание" и "статус" (выполнена/не выполнена).
# API должен позволять выполнять CRUD операции с
# задачами.
# Задание №4
# Напишите API для управления списком задач. Для этого создайте модель Task
# со следующими полями:
# ○ id: int (первичный ключ)
# ○ title: str (название задачи)
# ○ description: str (описание задачи)
# ○ done: bool (статус выполнения задачи)
# Погружение в Python
# Задание №4 (продолжение)
# API должно поддерживать следующие операции:
# ○ Получение списка всех задач: GET /tasks/
# ○ Получение информации о конкретной задаче: GET /tasks/{task_id}/
# ○ Создание новой задачи: POST /tasks/
# ○ Обновление информации о задаче: PUT /tasks/{task_id}/
# ○ Удаление задачи: DELETE /tasks/{task_id}/
# Для валидации данных используйте параметры Field модели Task.
# Для работы с базой данных используйте SQLAlchemy и модуль databases.

import databases
import sqlalchemy
import uvicorn
from fastapi import FastAPI

from typing import List
from models_task3 import Task, TaskIn

DATABASE_URL = "sqlite:///mydatabase3.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table(
    "tasks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(10)),
    sqlalchemy.Column("description", sqlalchemy.String(100)),
    sqlalchemy.Column("done", sqlalchemy.Boolean),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL
)

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/tasks/", response_model=Task)
async def create_task(task: TaskIn):
    """
    ○ Создание новой задачи: POST /tasks/
    :param task:
    :return:
    """
    query = tasks.insert().values(**task.dict())
    last_task_id = await database.execute(query)
    return {**task.dict(), "id": last_task_id}


# @app.get("/fake_tasks/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         query = tasks.insert().values(title=f'task{i}', description=f'Information{i}', done=f'done{i}')
#         await database.execute(query)
#     return {'message': f'{count} fake tasks create'}


@app.get("/tasks/", response_model=List[Task])
async def read_tasks():
    """
     ○ Получение списка всех задач: GET /tasks/
    :return:
    """
    query = tasks.select()
    return await database.fetch_all(query)


@app.get("/tasks/{task_id}")
async def find_task(task_id: int):
    """
    ○ Получение информации о конкретной задаче: GET /tasks/{task_id}/
    :param task_id:
    :return:
    """
    query = tasks.select().where(tasks.c.id == task_id)
    return await database.fetch_all(query)


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, new_task: TaskIn):
    """
    ○ Обновление информации о задаче: PUT /tasks/{task_id}/
    :param task_id:
    :param new_task:
    :return:
    """
    query = tasks.update().where(tasks.c.id == task_id).values(**new_task.dict())
    await database.execute(query)
    return {**new_task.dict(), "id": task_id}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """
    ○ Удаление задачи: DELETE /tasks/{task_id}/
    :param task_id:
    :return:
    """
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {'message': 'Task has been deleted'}
