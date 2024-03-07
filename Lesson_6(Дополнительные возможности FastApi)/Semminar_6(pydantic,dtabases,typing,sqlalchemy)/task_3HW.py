# Задание №3
# Создать API для управления списком задач.
# Каждая задача должна содержать поля "название",
# "описание" и "статус" (выполнена/не выполнена).
# API должен позволять выполнять CRUD операции с
# задачами.

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
    sqlalchemy.Column("name", sqlalchemy.String(10)),
    sqlalchemy.Column("description", sqlalchemy.String(100)),
    sqlalchemy.Column("status", sqlalchemy.String(13)),
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
async def create_user(task: TaskIn):
    query = tasks.insert().values(name=task.name, description=task.description, status=task.status)
    last_task_id = await database.execute(query)
    return {**task.dict(), "id": last_task_id}


@app.get("/fake_tasks/{count}")
async def create_note(count: int):
    for i in range(count):
        query = tasks.insert().values(name=f'task{i}', description=f'Information{i}', status=f'status{i}')
        await database.execute(query)
    return {'message': f'{count} fake tasks create'}


@app.get("/tasks/", response_model=List[Task])
async def read_users():
    query = tasks.select()
    return await database.fetch_all(query)


@app.put("/tasks/{task_id}", response_model=Task)
async def update_user(user_id: int, new_task: TaskIn):
    query = tasks.update().where(tasks.c.id == user_id).values(**new_task.dict())
    await database.execute(query)
    return {**new_task.dict(), "id": user_id}


@app.delete("/tasks/{user_id}")
async def delete_user(user_id: int):
    query = tasks.delete().where(tasks.c.id == user_id)
    await database.execute(query)
    return {'message': 'Task has been deleted'}