# Создание конечных точек API
# FastAPI позволяет легко создавать конечные точки (endpoints) API для
# взаимодействия с клиентами. Рассмотрим, как определять конечные точки,
# работать с параметрами запроса и путями URL, а также форматировать ответы API.
#
#
# Определение конечных точек API
# Конечная точка API — это URL-адрес, по которому клиент может отправлять запросы
# к серверу. В FastAPI определение конечных точек происходит с помощью
# декораторов.
# Например так:
#
# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}
#
# Этот код создает две конечные точки: одну для корневого URL-адреса, другую для
# URL-адреса /items/{item_id}. Функции read_root() и read_item() обрабатывают
# GET-запросы и возвращают JSON-объекты.
#
#
#
# Работа с параметрами запроса и путями URL
# Часто клиенты отправляют запросы с параметрами, которые нужно обработать на
# сервере. В FastAPI параметры запроса и пути URL определяются в декораторах
# конечных точек.
# Например:
# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}
#
# Этот код создает конечную точку для URL-адреса /items/{item_id}, которая
# принимает параметр item_id типа int и параметр q типа str со значением по
# умолчанию None. Если параметр q задан, функция возвращает JSON-объект с
# обоими параметрами, иначе — только с item_id.
# Мы также можем определить несколько параметров URL-адреса в пути, например
# /users/{user_id}/orders/{order_id}, а затем определить соответствующие параметры в
# функции для доступа к ним.
#
# ...
# @app.get("/users/{user_id}/orders/{order_id}")
# async def read_item(user_id: int, order_id: int):
# # обработка данных
#     return {"user_id": user_id, "order_id": order_id}
#
# Использование параметров запроса с FastAPI может быть любым удобным для
# решения поставленной задачи.
#
# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return {"skip": skip, "limit": limit}
#
# В этом примере мы определяем новый маршрут /items/, который принимает два
# параметра запроса skip и limit. Значения по умолчанию для этих параметров равны
# 0 и 10 соответственно. Когда мы вызываем этот маршрут без каких-либо
# параметров запроса, он возвращает значения по умолчанию.
# Например перейдя по адресу http://127.0.0.1:8000/items/ получим json c {"skip": 0,"limit": 10}.
# Мы также можем передать параметры запроса в URL-адресе, например
# http://127.0.0.1:8000/items/?skip=20&limit=30. В таком случае ответ будет
# следующим json объектом {"skip": 20, "limit": 30}.
#
#
#
# Форматирование ответов API
# FastAPI позволяет форматировать ответы API в различных форматах, например, в
# JSON или HTML. Для этого нужно использовать соответствующие функции модуля
# fastapi.responses.
#
# ● HTML текст
# Например:
#
# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
#
# app = FastAPI()
#
# @app.get("/", response_class=HTMLResponse)
# async def read_root():
#     return "<h1>Hello World</h1>"
# Этот код создает конечную точку для корневого URL-адреса, которая возвращает
# HTML-страницу с текстом "Hello World". Функция read_root() использует класс
# HTMLResponse для форматирования ответа в HTML.
#
#
#
# ● JSON объект
# В этом примере возвращается ответ JSON с настраиваемым сообщением и кодом
# состояния.
# from fastapi import FastAPI
# from fastapi.responses import JSONResponse
#
# app = FastAPI()
#
# @app.get("/message")
# async def read_message():
#     message = {"message": "Hello World"}
#     return JSONResponse(content=message, status_code=200)
#
# В этом примере мы импортируем класс JSONResponse из модуля FastAPI.responses.
# Внутри функции read_message мы определяем словарь, содержащий ключ
# сообщения со значением «Hello World». Затем мы возвращаем объект
# JSONResponse со словарем сообщений в качестве содержимого и кодом состояния
# 200.
#
#
#
# Динамический HTML через шаблонизатор Jinja
# В следующем примере используется шаблонизация Jinja2 для создания ответа
# HTML с динамическим содержимым.
#
# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
#
# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
#
# @app.get("/{name}", response_class=HTMLResponse)
# async def read_item(request: Request, name: str):
#     return templates.TemplateResponse("item.html", {"request": request, "name": name})
# В этом примере мы импортируем класс Jinja2Templates из модуля
# FastAPI.templating. Мы создаем экземпляр этого класса и передаем каталог, в
# котором расположены наши шаблоны. В функции read_item мы получаем параметр
# имени из пути URL и генерируем динамический HTML-ответ, используя шаблон
# Jinja2 (item.html). Шаблон получает объект запроса и параметр имени в качестве
# переменных контекста для отображения в ответе HTML.
# Простейший шаблон item.html
# <!DOCTYPE html>
# <html lang="ru">
# <head>
# <meta charset="UTF-8">
# <title>Item - {{ name }}</title>
# </head>
# <body>
# <h1>Hello, {{ name|title }}!</h1>
# </body>
# </html>
#
#
#
# Автоматическая документация по API
# FastAPI обладает встроенным инструментом для автоматической документации
# API, который позволяет быстро и удобно ознакомиться с функциональностью
# приложения. Рассмотрим два варианта документации API: интерактивную
# документацию Swagger и альтернативную документацию ReDoc.
# Интерактивная документация Swagger
# Swagger — это инструмент для создания и документирования API. FastAPI
# использует Swagger UI для генерации интерактивной документации, которая
# отображает все маршруты, параметры и модели данных, которые были определены
# в приложении.
# Для просмотра интерактивной документации Swagger нужно запустить приложение
# и перейти по адресу http://localhost:8000/docs. На странице будут представлены все
# маршруты и параметры, доступные в приложении.
# При выборе конкретного маршрута откроется его описание, включая возможные
# параметры запроса и ответа. Для каждого параметра указаны его тип, описание и
# необходимость.
# Также Swagger UI позволяет отправлять запросы к API прямо из интерфейса. Для
# этого нужно выбрать метод запроса и заполнить параметры запроса, если таковые
# имеются. После отправки запроса будет отображен его результат.
# Альтернативная документация ReDoc
# ReDoc — это альтернативный инструмент для документирования API, который
# также поддерживается FastAPI. Он предоставляет более простой и лаконичный
# интерфейс для просмотра документации.
# Для просмотра документации ReDoc нужно запустить приложение и перейти по
# адресу http://localhost:8000/redoc. На странице будет отображена документация API
# в формате OpenAPI.
#
# Как и в Swagger, каждый маршрут содержит описание его параметров и возможных
# ответов. Однако ReDoc не позволяет отправлять запросы к API из интерфейса.
# Пример использования
# Для того чтобы включить генерацию документации API в FastAPI, нужно
# использовать модуль fastapi.openapi. Например, вот как выглядит простой пример
# приложения с одним маршрутом:
# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/hello/{name}")
# async def read_item(name: str, age: int):
#     return {"Hello": name, "Age": age}
#
# Для генерации документации нужно создать экземпляр класса FastAPI с
# параметром openapi_url:
# from fastapi import FastAPI
# from fastapi.openapi.utils import get_openapi
#
# app = FastAPI(openapi_url="/api/v1/openapi.json")
#
# @app.get("/hello/{name}")
# async def read_item(name: str, age: int):
#     return {"Hello": name, "Age": age}
#
# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema
#     openapi_schema = get_openapi(
#     title="Custom title",
#     version="1.0.0",
#     description="This is a very custom OpenAPI schema",
#     routes=app.routes,
#     )
#     app.openapi_schema = openapi_schema
#     return app.openapi_schema
#
# app.openapi = custom_openapi
#
# В этом примере мы переопределили метод custom_openapi, который генерирует
# схему OpenAPI вручную. Мы также установили значение параметра openapi_url,
# чтобы FastAPI знал, где разместить схему OpenAPI.
# После запуска приложения можно перейти по адресу
# http://localhost:8000/api/v1/openapi.json и убедиться, что схема OpenAPI была
# успешно сгенерирована.
# Затем можно запустить приложение и перейти по адресу http://localhost:8000/docs
# или http://localhost:8000/redoc, чтобы просмотреть сгенерированную
# документацию.
