from pydantic import BaseModel, Field


class UserIn(BaseModel):
    username: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(max_length=32)


class User (UserIn):
    id: int