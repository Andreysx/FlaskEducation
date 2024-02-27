# Сравнение разных подходов на примере
# парсинга сайтов
# Перед нами задача по скачиванию информации с главных страниц пяти сайтов.
# Рассмотрим решение задачи с использованием синхронного, многопоточного,
# многопроцессорного и асинхронного подходов.
#
#
# Обычная синхронная загрузка:
# import requests
# import time
#
#
# urls = ['https://www.google.ru/',
#     'https://gb.ru/',
#     'https://ya.ru/',
#     'https://www.python.org/',
#     'https://habr.com/ru/all/',
#     ]
#
# start_time = time.time()
#
#
# for url in urls:
#     response = requests.get(url)
#     filename = 'sync_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
#     with open(filename, "w", encoding='utf-8') as f:
#         f.write(response.text)
#         print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")
#
#
# В данном примере мы используем библиотеку requests для получения
# html-страницы каждого сайта из списка urls. Затем мы записываем полученный
# текст в файл с именем, соответствующим названию сайта.
# 🔥 Важно! Используйте pip install requests, если не устанавливали библиотеку
# ранее.
#
#
#
# Загрузка в 5 потоков с использованием модуля threading:
# import requests
# import threading
# import time
#
#
# urls = ['https://www.google.ru/',
#         'https://gb.ru/',
#         'https://ya.ru/',
#         'https://www.python.org/',
#         'https://habr.com/ru/all/',
#         ]
#
#
# def download(url):
#     response = requests.get(url)
#     filename = 'threading_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
#     with open(filename, "w", encoding='utf-8') as f:
#         f.write(response.text)
#         print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")
#
#
# threads = []
# start_time = time.time()
#
#
# for url in urls:
#     thread = threading.Thread(target=download, args=[url])
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# Здесь мы создаем функцию download, которая загружает html-страницу и сохраняет
# ее в файл. Затем мы создаем по одному потоку для каждого сайта из списка urls,
# передавая функцию download в качестве целевой функции для каждого потока. Мы
# запускаем каждый поток и добавляем его в список threads. В конце мы ждем
# завершения всех потоков с помощью метода join.
#
#
# Загрузка в 5 процессов с использованием модуля multiprocessing:
#
#
# import requests
# from multiprocessing import Process, Pool
# import time
#
#
# urls = ['https://www.google.ru/',
#         'https://gb.ru/',
#         'https://ya.ru/',
#         'https://www.python.org/',
#         'https://habr.com/ru/all/',
#         ]
#
#
# def download(url):
#     response = requests.get(url)
#     filename = 'multiprocessing_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
#     with open(filename, "w", encoding='utf-8') as f:
#         f.write(response.text)
#         print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")
#
# processes = []
# start_time = time.time()
#
#
# if __name__ == '__main__':
#     for url in urls:
#         process = Process(target=download, args=(url,))
#         processes.append(process)
#         process.start()
#
#     for process in processes:
#         process.join()
#
# Здесь мы используем модуль multiprocessing для создания процессов вместо
# потоков. Остальной код аналогичен предыдущему примеру.
#
#
#
# Асинхронная загрузка с использованием модуля asyncio:
# import asyncio
# import aiohttp
# import time
#
#
# urls = ['https://www.google.ru/',
#     'https://gb.ru/',
#     'https://ya.ru/',
#     'https://www.python.org/',
#     'https://habr.com/ru/all/',
#     ]
#
# async def download(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             text = await response.text()
#             filename = 'asyncio_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
#             with open(filename, "w", encoding='utf-8') as f:
#                 f.write(text)
#                 print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")
#
#
# async def main():
#     tasks = []
#     for url in urls:
#         task = asyncio.ensure_future(download(url))
#         tasks.append(task)
#     await asyncio.gather(*tasks)
#
# start_time = time.time()
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#
# Здесь мы используем модуль asyncio для асинхронной загрузки страниц. Мы
# создаем функцию download, которая использует aiohttp для получения
# html-страницы и сохранения ее в файл. Затем мы создаем асинхронную функцию
# main, которая запускает функцию download для каждого сайта из списка urls и
# ожидает их завершения с помощью метода gather. Мы запускаем функцию main с
# помощью цикла событий asyncio.
# Заключение
# В этой лекции мы рассмотрели различные подходы к многозадачности в Python:
# синхронный, многопоточный, многопроцессорный и асинхронный подход. Каждый
# из этих подходов имеет свои преимущества и недостатки, и выбор подхода зависит
# от требований к производительности и конкретных задач.
# Синхронный код прост в написании и понимании, но имеет ограничения в
# производительности. Многопоточный код позволяет эффективно использовать
# ресурсы процессора и памяти, но может привести к проблемам синхронизации.
# Многопроцессорный код также позволяет эффективно использовать ресурсы, но
# имеет дополнительные накладные расходы на коммуникацию между процессами.
# Асинхронный код позволяет обрабатывать большое количество задач
# одновременно без создания отдельных процессов или потоков, но требует особого
# внимания к правильному использованию механизмов событий и обратных вызовов.
# При выборе подхода к многозадачности необходимо учитывать требования к
# производительности и особенности конкретной задачи. Важно также учитывать
# возможность поддержки сторонними библиотеками и оптимизировать работу
# программы.
# В целом, многозадачность — это важный инструмент в программировании, который
# позволяет эффективно использовать ресурсы компьютера и обрабатывать большое
# количество задач одновременно. Однако, при выборе подхода к многозадачности
# необходимо учитывать его преимущества и недостатки, а также правильно
# использовать механизмы синхронизации и событий для избежания проблем.
