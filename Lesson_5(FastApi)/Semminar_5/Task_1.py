# Задание №1
# Создать API для управления списком задач. Приложение должно иметь
# возможность создавать, обновлять, удалять и получать список задач.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте маршрут для получения списка задач (метод GET).
# Создайте маршрут для создания новой задачи (метод POST).
# Создайте маршрут для обновления задачи (метод PUT).
# Создайте маршрут для удаления задачи (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.
# Погружение в Python
# Решение в IDE

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str

tasks = []

for i in range(0, 10):
    new_task = Task(
    id = i,
    title = f'title + {i}',
    description = f'description + {i}',
    status = f'status + {i}')
    tasks.append(new_task)


@app.get("/")
async def root():
    return tasks


@app.post("/task/")
async def create_task(task: Task):
    tasks.append(task)
    return tasks


@app.put("/task/")
async def change_task(task_id: int, task: Task):
    for i, elem in enumerate(tasks):
        if elem.id == task_id:
            tasks[i] = task
            return task
    return {"message": "task not found"}


@app.delete("/task/")
async def delete_task(task_id: int):
    for elem in tasks:
        if elem.id == task_id:
            tasks.remove(elem)
            return {"message": "task removed"}
    return {"message": "task not found"}


# if __name__ == '__main__':
#     app.run()
