"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


"""

import random


def task_16():
    n = int(input('Array size: '))
    x = int(input('Searching element: '))
    array = create_array(n)

    print(array)
    print('Count of searching elements:', array.count(x))


def create_array(n):
    array = []
    for i in range(0, n):
        array.append(random.randrange(1, 9))
    return array


def task_18():
    n = int(input('Array size: '))
    x = int(input('Searching element: '))
    array = create_array(n)

    close_value = array[0]
    close_value_key = 0
    temp_key = 0
    value_difference = abs(array[0] - x)
    for value in array[1:]:
        temp_key = temp_key + 1
        temp_value_difference = abs(value - x)
        if temp_value_difference < value_difference:
            close_value = value
            close_value_key = temp_key

    print(array)
    print(f'Closest element to {x} is {close_value}, index in array - {close_value_key}')


task_16()
task_18()
