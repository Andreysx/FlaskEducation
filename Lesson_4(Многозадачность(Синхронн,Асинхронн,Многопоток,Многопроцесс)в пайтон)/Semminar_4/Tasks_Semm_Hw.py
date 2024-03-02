# Задание №1,2,3
# � Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
# � После загрузки данных нужно записать их в отдельные
# файлы.
# � Используйте синхронные.
# � Используйте многопоточный подход threading.
# � Используйте многопроцессный подход multiproccesing.
# � Используйте асинхронный подход asincio.

import requests
from pathlib import Path
import time
import threading
import multiprocessing
import asyncio
import aiohttp


def download(url, start_time, type_: str):
    response = requests.get(url)
    # filename = type_ + url.replace('https:', '').replace('.', '_').replace('/', '') + 'html'
    # filename = type_ + url.replace('https:', '').replace('.', '_').replace('/', '') + 'html'
    filename = type_ + url.replace('https:', '').replace('.', '_').replace('/', '') + 'html'
    with open(f"./upload/{filename}", 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downoloaded {url} in {time.time() - start_time: .2f} seconds")


# � Используйте синхронный подход В данном примере мы используем библиотеку requests для получения
# html-страницы каждого сайта из списка urls.
def task1(urls: list[str]):
    start_time = time.time()
    for url in urls:
        download(url, start_time, 'sync_')


# � Используйте многопоточный подход threading.
def task2(urls: list[str]):
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=download, args=[url, start_time, 'thread_'])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


# � Используйте многопроцессный подход multiproccesing.
def task3(urls: list[str]):
    start_time = time.time()
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=download, args=[url, start_time, 'process_'])
        processes.append(process)
        process.start()
    for process in processes:
        process.join()


# � Используйте асинхронный подход asincio.
async def download_async(url, start_time, type_: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
    filename = type_ + url.replace('https:', '').replace('.', '_').replace('/', '') + 'html'
    with open(f"./upload/{filename}", 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Downoloaded {url} in {time.time() - start_time: .2f} seconds")


async def task4(urls):
    start_time = time.time()
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_async(url, start_time, 'async_'))
        tasks.append(task)
    await asyncio.gather(*tasks)

# Задание №4(task5)
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте потоки.

def count_words(file: Path, start_time):
    with open(file, encoding='utf-8') as f:
        text = f.read()
        print(f"Inside file {file.name} {len(text.split())} words - {time.time() - start_time: .2f}")


def task5(path: Path):
    start_time = time.time()
    files = [file for file in path.iterdir() if file.is_file()]
    threads = []
    for file in files:
        thread = threading.Thread(target=count_words, args=[file,start_time])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

#
# Задание №5(task6) Homework
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте процессы.

def task6(path: Path):
    start_time = time.time()
    files = [file for file in path.iterdir() if file.is_file()]
    processes = []
    for file in files:
        process = multiprocessing.Process(target=count_words, args=[file, start_time])
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


# Задание №6(task7) Homework
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте асинхронный подход.

async def async_count_words(file: Path, start_time):
    with open(file, encoding='utf-8') as f:
        text = f.read()
        print(f"Inside file {file.name} {len(text.split())} words - {time.time() - start_time: .2f}")


async def task7(path: Path):
    start_time = time.time()
    file_paths = [file_path for file_path in path.iterdir() if file_path.is_file()]
    tasks = [asyncio.create_task(async_count_words(path, start_time)) for path in file_paths]
    await asyncio.gather(*tasks)






def main():
    Path(Path.cwd() / 'upload').mkdir(exist_ok=True)
    urls = [
        'https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://mail.ru/',
        'https://www.yahoo.com/',
        'https://www.rambler.ru/',
        'https://www.wikipedia.org/',
        'https://pikabu.ru/'
    ]
    # task1(urls) # 8.20 sec
    # task2(urls) # 3.87 sec
    # task3(urls) # 3.45 sec
    # asyncio.run(task4(urls)) #1.35 sec Preferred now
    # loop = asyncio.get_event_loop() Not working
    # loop.run_until_complete(task4)Not working

    # task5
    path = Path(Path.cwd() / 'upload')
    # task5(path) # Потоки
    # task6(path) # Homework, Процессы
    # asyncio.run(task7(path)) # Homework Асиинхронный подход




if __name__ == '__main__':
    main()
