"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.

Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
"""


def task_26():
    a = int(input('Введите А: '))
    b = int(input('Введите B: '))
    print('A в степени B =', v_stepen(a, b))


def v_stepen(a, b):
    if b < 1:
        return 1
    return a * v_stepen(a, b - 1)

def task_28():
    a = int(input('Введите А: '))
    b = int(input('Введите B: '))
    print('Сумма A и B =', req_sum(a, b))


def req_sum(a, b):
    if a > 0:
        return req_sum(a - 1, b) + 1
    elif b > 0:
        return req_sum(a, b - 1) + 1
    else:
        return 0


task_26()
task_28()


