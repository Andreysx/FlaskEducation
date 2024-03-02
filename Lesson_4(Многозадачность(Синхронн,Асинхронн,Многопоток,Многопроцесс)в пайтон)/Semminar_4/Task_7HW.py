# Задание №7
# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать
# синхронрость
# многопоточность,
# многопроцессорность
#  асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислени
import requests
import time
import threading
import multiprocessing
import asyncio
import random



# # Синхронрость  - Counted 5044542 in  42.03 seconds

# def sync_summ(arr: list):
#     "Запускается через main функцию"
#     start_time = time.time()
#     summ = 0
#     for _ in arr:
#         summ = sum(arr)
#     print(f"Counted {summ} in {time.time() - start_time: .2f} seconds")


# Многопоточность  - Counted 50481865 in  0.031914 seconds
# Запускается прям тут путем раскомментирования строк ниже, до многопроцессности)

# data = [random.randint(1, 100) for i in range(1, 1000000 + 1)]
#
# def summ_elements(numbers: list):
#     start_time = time.time()
#     total = 0
#     for number in numbers:
#         total += number
#     print(f"Counted {total} in {time.time() - start_time: 4f} seconds")
#
# threads = []
# for i in range(5):
#     thread = threading.Thread(target=summ_elements(data), args=(i, ))
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# print("Все потоки завершили работу")



# Многопроцессорность  - Counted 5053046 in  0.002991 seconds
# Запускается в main функции, нужно раскомментировать def summ_elements функцию)

# def summ_elements(numbers: list):
#     start_time = time.time()
#     total = 0
#     for number in numbers:
#         total += number
#     print(f"Counted {total} in {time.time() - start_time: 4f} seconds")

#

#  Асинхронность. - Counted 5037783 in  0.002992 seconds
# Запускается через функцию main

# async def summ_elements(numbers: list):
#     start_time = time.time()
#     total = 0
#     for number in numbers:
#         total += number
#     print(f"Counted {total} in {time.time() - start_time: 4f} seconds")
#
#
# async def assync_funct():
#     data = [random.randint(1, 100) for i in range(1, 100000 + 1)]
#     result = await asyncio.gather(summ_elements(data), summ_elements(data), summ_elements(data), summ_elements(data))
#     print(result)



# def main():
#     data = [random.randint(1, 100) for i in range(1, 100000 + 1)]
    # #Синхронный подход
    # sync_summ(data) #1.74 sec
#     #Многопроцессорный подход
#     processes = []
#     for i in range(5):
#         process = multiprocessing.Process(target=summ_elements(data), args=(i,))
#         processes.append(process)
#         process.start()
#
#     for process in processes:
#         process.join()
#
#     print("Все процессы завершили работу")
#     #Ассинхронный подход
#     asyncio.run(assync_funct())
#

# if __name__ == '__main__':
#     main()