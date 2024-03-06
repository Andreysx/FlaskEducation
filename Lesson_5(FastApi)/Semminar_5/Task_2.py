# Задание №2
# Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str


movies = []

genres = ["Ужас", "Триллер", "Комедия", "Исторический", "Фантастика"]

for i in range(1, 11):
    new_movie = Movie(
    id=i,
    title=f"title{i}",
    description=f"description{i}",
    genre=choice(genres)
    )
    movies.append(new_movie)


@app.get("/movies/")
async def get_movies():
    return movies


@app.get("/movies/{genre}")
async def get_movies_by_genre(genre: str):
    result = []
    for movie in movies:
        if movie.genre == genre:
            result.append(movie)
            return result if result else {"message": "No movies in that genre"}


@app.post("/movies/")
async def create_movie(movie: Movie):
    movies.append(movie)
    return movie


@app.put("/movies/")
async def update_movie(movie_id: int, movie: Movie):
    for i, m in enumerate(movies):
        if m.id == movie_id:
            movies[i] = movie
            return movie
    return {"message": "movie not found"}


@app.delete("/movie/")
async def delete_movie(movie_id: int):
    for movie in movies:
        if movie.id == movie_id:
            movies.remove(movie)
            return {"message": "movie removed"}
    return {"message": "movie not found"}