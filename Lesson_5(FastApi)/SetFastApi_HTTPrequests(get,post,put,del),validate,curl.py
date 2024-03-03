# Введение в FastAPI и его возможности
# Framework FastAPI — это современный фреймворк для создания веб-приложений
# на языке Python. Он был создан с учетом последних тенденций веб-разработки и
# имеет ряд преимуществ перед другими фреймворками. FastAPI совсем новый
# фреймворк, вышедший в 2018 году. С тех пор он активно развивается, набирает
# популярность.
#
#
# Основные возможности FastAPI
# К основным возможностям FastAPI можно отнести следующие:
# ● Высокая скорость работы благодаря использованию асинхронных функций и
# типизации данных.
# ● Автоматическая генерация документации API на основе аннотаций функций
# и моделей данных.
# ● Встроенная валидация данных запросов и ответов.
# ● Поддержка OpenAPI и JSON Schema.
# ● Простота использования благодаря интуитивно понятному синтаксису и
# многочисленным примерам.
# Сравнение с другими фреймворками
# FastAPI имеет ряд преимуществ перед другими популярными фреймворками,
# такими как Flask и Django. Он более быстрый благодаря использованию
# асинхронных функций, более безопасный благодаря встроенной валидации данных
# и поддержке OpenAPI, а также более простой в использовании благодаря
# интуитивно понятному синтаксису.
# Настройка среды разработки
# Рассмотрим процесс настройки среды разработки для работы с FastAPI.
#
#
# Установка FastAPI
# Первым шагом является установка FastAPI. Для этого необходимо использовать
# менеджер пакетов pip, который уже устанавливается вместе с Python. Откройте
# терминал и выполните следующую команду:
# pip install fastapi
# Эта команда установит FastAPI и все его зависимости.
# Отдельно необходимо установить ASGI сервер для запуска приложения. Один из
# вариантов — установка uvicorn.
# pip install "uvicorn[standard]"
#
#
# Настройка FastAPI
# Для работы с FastAPI необходимо создать файл приложения и определить конечные
# точки API. Для этого можно использовать любой текстовый редактор или
# интегрированную среду разработки (IDE).
#
# Пример кода:
# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
# В этом примере мы создали объект FastAPI и определили конечную точку API с
# помощью декоратора @app.get("/"). Декоратор указывает, что это обработчик
# GET-запроса по пути "/".
# Внутри функции мы возвращаем словарь с сообщением "Hello World". Это
# сообщение будет отправлено в ответ на запрос.
# Запуск приложения
# Для запуска приложения необходимо использовать сервер для запуска приложений
# uvicorn. Для этого открываем терминал ОС, переходим в каталог с проектом и
# выполняем следующую команду:
# uvicorn main:app --reload
#
# Эта команда запустит сервер на локальном хосте по адресу http://127.0.0.1:8000/.
# Для остановки сервера нажмите сочетание клавиш Ctrl + C в терминале.
# Мы рассмотрели процесс настройки среды разработки для работы с FastAPI.
# Установили Fast API и сервер unicorn, создали файл приложения и определили
#
#
# конечные точки API. Затем мы запустили сервер для запуска приложений uvicorn и
# проверили работу приложения в браузере.
# Создание базового приложения FastAPI
#
# Рассмотрим процесс создания базового приложения FastAPI. Вы увидите много
# общего с Flask.
# Создание модуля приложения
# Первым шагом является создание модуля приложения.
# Для этого создайте файл
# main.py и импортируйте FastAPI:
# from fastapi import FastAPI
#
# app = FastAPI()
# В этом примере мы создали объект FastAPI и назвали его app.
# Настройка сервера и маршрутизации
# Далее необходимо настроить сервер и определить маршрутизацию для нашего
# приложения. Для этого создайте функции-обработчики запросов и определите их
# маршруты.
#
# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}
#
# В этом примере мы определили две функции-обработчика запросов. Первая
# функция обрабатывает GET-запрос по корневому пути "/" и возвращает словарь с
# сообщением "Hello World". Вторая функция обрабатывает GET-запрос по пути
# "/items/{item_id}", где item_id — это переменная пути, а q — это параметр запроса.
# Функция возвращает словарь с переданными параметрами.
#
#
# Запуск приложения и проверка работоспособности
# Для запуска приложения необходимо использовать сервер для запуска приложений
# uvicorn. Для этого выполните следующую команду:
# uvicorn main:app --reload
# Эта команда запустит сервер на локальном хосте по адресу http://127.0.0.1:8000/.
# Чтобы проверить работоспособность приложения, откройте браузер и перейдите по
# адресу http://127.0.0.1:8000/. Вы должны увидеть сообщение "Hello World".
# Чтобы проверить работу второй функции, перейдите по адресу
# http://127.0.0.1:8000/items/5?q=test, где 5 — это значение переменной item_id, а
# test — значение параметра q. Вы должны увидеть словарь с переданными
# параметрами.
#
#
#
# Обработка HTTP-запросов и ответов
# HTTP (Hypertext Transfer Protocol) — это протокол передачи данных в интернете,
# используемый для обмена информацией между клиентом и сервером. В FastAPI
# обработка HTTP-запросов и ответов происходит автоматически.
# Основы протокола HTTP
# Протокол HTTP работает по схеме "клиент-сервер". Клиент отправляет запрос на
# сервер, а сервер отвечает на этот запрос. Запрос состоит из трех частей: метод,
# адрес и версия протокола. Методы запроса могут быть GET, POST, PUT, DELETE и
# другие. Адрес - это URL-адрес ресурса, к которому обращается клиент. Версия
# протокола указывает на версию HTTP, которую использует клиент.
#
#
# Обработка запросов GET
# Метод GET используется для получения ресурсов с сервера. В FastAPI обработка
# GET-запросов происходит с помощью декоратора @app.get(). Например:
# import logging
# from fastapi import FastAPI
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# app = FastAPI()
#
# @app.get("/")
# async def read_root():
#     logger.info('Отработал GET запрос.')
#     return {"Hello": "World"}
#
# Этот код создает приложение FastAPI и добавляет обработчик GET-запросов для
# корневого URL-адреса. Функция read_root() возвращает JSON-объект {"Hello":"World"}.
#
#
#
#
# Обработка запросов POST
# Метод POST используется для отправки данных на сервер. В FastAPI обработка
# POST-запросов происходит с помощью декоратора @app.post(). Например:
# import logging
# from fastapi import FastAPI
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# app = FastAPI()
#
# @app.post("/items/")
# async def create_item(item: Item):
#     logger.info('Отработал POST запрос.')
#     return item
#
# Этот код создает приложение FastAPI и добавляет обработчик POST-запросов для
# URL-адреса /items/. Функция create_item() принимает объект Item и возвращает его
# же.
# 🔥 Внимание! Код выше не будет работать, так как мы не определили объект
# Item. Речь о модуле pydantic позволяющем создать класс Item будет позже
# в рамках курса.
#
#
#
# Обработка запросов PUT
# Метод PUT используется для обновления данных на сервере. В FastAPI обработка
# PUT-запросов происходит с помощью декоратора @app.put(). Например:
# import logging
# from fastapi import FastAPI
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# app = FastAPI()
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     logger.info(f'Отработал PUT запрос для item id = {item_id}.')
#     return {"item_id": item_id, "item": item}
#
#
# Этот код создает приложение FastAPI и добавляет обработчик PUT-запросов для
# URL-адреса /items/{item_id}. Функция update_item() принимает идентификатор
# элемента и объект Item и возвращает JSON-объект с этими данными.
# 🔥 Внимание! Код выше не будет работать, так как мы не определили объект
# Item. Речь о модуле pydantic позволяющем создать класс Item будет позже
# в рамках курса.
#
#
#
#
# Обработка запросов DELETE
# Метод DELETE используется для удаления данных на сервере. В FastAPI обработка
# DELETE-запросов происходит с помощью декоратора @app.delete(). Например:
# import logging
# from fastapi import FastAPI
#
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# app = FastAPI()
#
# @app.delete("/items/{item_id}")
# async def delete_item(item_id: int):
#     logger.info(f'Отработал DELETE запрос для item id = {item_id}.')
#     return {"item_id": item_id}
#
# Этот код создает приложение FastAPI и добавляет обработчик DELETE-запросов для
# URL-адреса /items/{item_id}. Функция delete_item() принимает идентификатор
# элемента и возвращает JSON-объект с этим идентификатором.
# 🔥 Важно! Зачастую операция удаления не удаляет данные из базы данных, а
# изменяет специально созданное поле is_deleted на значение Истина. Таким
# образов вы сможете восстановить ранее удалённные данные
# пользователя, если он передумает спустя время.
#
#
#
# Валидация данных запроса и ответа
# FastAPI позволяет автоматически валидировать данные запроса и ответа с
# помощью модуля pydantic. Например, можно создать класс Item для валидации
# данных:
#
# ...
# from typing import Optional
# from pydantic import BaseModel
#
#
# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     ...
# Этот класс содержит поля name, description, price и tax. Поля name и price
# обязательны, а поля description и tax необязательны. Затем можно использовать
# этот класс для валидации данных запроса и ответа:
# ...
# from fastapi import FastAPI
# from typing import Optional
# from pydantic import BaseModel
# ...
# app = FastAPI()
#
# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     ...
#
# @app.post("/items/")
# async def create_item(item: Item):
#     logger.info('Отработал POST запрос.')
#     return item
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     logger.info(f'Отработал PUT запрос для item id = {item_id}.')
#     return {"item_id": item_id, "item": item}
# ...
#
# Этот код добавляет обработчики POST и PUT запросов, которые принимают объект
# Item и возвращают его же. Если данные не соответствуют описанию класса Item, то
# FastAPI вернет ошибку 422 с описанием ошибки.
# Отправка запросов через curl
# Если с GET запросом проблем не было, то для тестирования POST, PUT и DELETE запросов
# воспользуемся curl.
#
#
# Curl (client URL) — это инструмент командной строки на основе библиотеки libcurl для
# передачи данных с сервера и на сервер при помощи различных протоколов, в том числе
# HTTP, HTTPS, FTP, FTPS, IMAP, IMAPS, POP3, POP3S, SMTP и SMTPS. Он очень популярен в
# сфере автоматизации и скриптов благодаря широкому диапазону функций и
# поддерживаемых протоколов.
#
# ● POST запрос
# Для отправки POST запроса нашему серверу введём в терминале следующую
# строку:
#
# curl -X 'POST' 'http://127.0.0.1:8000/items/' -H 'accept:
# application/json' -H 'Content-Type: application/json' -d
# '{"name": "BestSale", "description": "The best of the best",
# "price": 9.99, "tax": 0.99}'
#
# Эта строка отправляет POST запрос на URL-адрес «http://127.0.0.1:8000/items/» с
# данными JSON, содержащими поля «имя», «описание», «цена» и «налог» вместе с
# соответствующими значениями. Заголовки «accept» и «Content-Type» имеют
# значение «application/json», мы пересылаем запросом json объект на сервер и хотим
# получить json в качестве ответа.
#
#
# ● PUT запрос
# Для отправки PUT запроса нашему серверу введём в терминале следующую строку:
#
# curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept:
# application/json' -H 'Content-Type: application/json' -d
# '{"name": "NewName", "description": "New description of the
# object", "price": 77.7, "tax": 10.01}'
#
# Эта строка отправляет HTTP-запрос PUT на локальный сервер по адресу
# http://127.0.0.1:8000/, обновляя элемент с идентификатором 42 новой
# информацией, предоставленной в формате JSON, такой как имя, описание, цена и
# налог.
# Мы можем опускать необязательные поля объекта Item в запросе. Ответ от сервера
# будет 200. А вот отсутствие обязательных параметров приведёт к ответу 422
# Unprocessable Entity.
#
#
# Хороший короткий PUT запрос:
# curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept:
# application/json' -H 'Content-Type: application/json' -d
# '{"name": "NewName", "price": 77.7}'
# Плохой PUT запрос:
# curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept:
# application/json' -H 'Content-Type: application/json' -d
# '{"name": "NewName", "tax": 77.7}'
# В данном запросе отсутствует обязательное поле price. Его мы сделали
# обязательным в классе Item строкой price: float.
# Код состояния ответа HTTP 422 Unprocessable Entity указывает, что сервер
# понимает тип содержимого в теле запроса и синтаксис запроса является
# правильным, но серверу не удалось обработать инструкции содержимого.
#
#
#
# ● DELETE запрос
# Чтобы удалить объект нужен лишь его идентификатор, без передачи самого
# объекта. curl будет выглядеть следующим образом:
# curl -X 'DELETE' 'http://127.0.0.1:8000/items/13' -H 'accept:
# application/json'
# Запрос DELETE сообщает серверу о желании удалить объект с id 13.
#
