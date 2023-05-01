"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка;
B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу,
которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово,
которое содержит либо только английские, либо только русские буквы.
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


def task_20():
    en_letters = {
        1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
        2: ['D', 'G'],
        3: ['B', 'C', 'M'],
        4: ['F', 'H', 'V', 'W', 'Y'],
        5: ['K'],
        8: ['J', 'X'],
        10: ['Q', 'Z'],
    }
    ru_letters = {
        1: ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
        2: ['Д', 'К', 'Л', 'М', 'П', 'У'],
        3: ['Б', 'Г', 'Ё', 'Ь', 'Я'],
        4: ['Й', 'Ы'],
        5: ['Ж', 'З', 'Х', 'Ц', 'Ч'],
        8: ['Ш', 'Э', 'Ю'],
        10: ['Ф', 'Щ', 'Ъ'],
    }

    word = str(input('Enter word in Russian or English: '))
    char_list = list(word.upper())

    word_value = calculate_word_value(char_list, en_letters)
    if word_value == 0:
        word_value = calculate_word_value(char_list, ru_letters)

    print(f'Word value for word {word} is {word_value}')


def calculate_word_value(char_list, letters):
    word_value = 0
    for char in char_list:
        for key, value in letters.items():
            if char in value:
                word_value = word_value + key
                break
    return word_value


task_16()
task_18()
task_20()
