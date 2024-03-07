from pydantic import BaseModel, Field


class TaskIn(BaseModel):
    name: str = Field(min_length=2)
    description: str = Field(default="Не определено")
    status: str = Field(default="Не выполнена", max_length=13)


class Task(TaskIn):
    id: int