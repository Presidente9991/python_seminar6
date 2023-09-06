"""
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума).
Список можно задавать рандомно

На входе : [ 1, 5, 88, 100, 2, -4]
33
200
Ответ: [2, 3]
"""

import random

random_array = []

for num in range(10):
    random_array.append(random.randint(-100, 100))

print(f"Массив случайных чисел -> {random_array}")

maximum = int(input("Введите максимальное число массива: "))
minimum = int(input("Введите минимальное число массива: "))

for i in range(len(random_array)):
    if minimum <= random_array[i] <= maximum:
        print(i)
