from pydantic import BaseModel, Field
import random


class TaskIn(BaseModel):
    title: str = Field(title='title', min_length=2)
    description: str = Field(title='description', max_length=50)
    done: bool = Field(title='done', default=False)


class Task(TaskIn):
    id: int
