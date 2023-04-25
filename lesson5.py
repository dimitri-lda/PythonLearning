"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
"""


def task_26():
    a = int(input('Введите А: '))
    b = int(input('Введите B: '))
    print('A в степени B =', v_stepen(a, b))


def v_stepen(a, b):
    if b < 1:
        return 1
    return a * v_stepen(a, b - 1)


task_26()


