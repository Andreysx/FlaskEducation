from pydantic import BaseModel, Field, EmailStr
from datetime import date

class UserIn(BaseModel):
    username: str = Field(min_length=2)
    lastname: str = Field(min_length=2)
    birthday: date = Field()
    email: EmailStr = Field(max_length=128)
    adress: str = Field(min_length=5)


class User(UserIn):
    id: int