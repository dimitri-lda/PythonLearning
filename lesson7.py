"""
Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не
настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все
в порядке и “Пам парам”, если с ритмом все не в порядке.

Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве
аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число
строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы
(подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
как, например, у операции умножения.
"""


def task_34():
    poem = "пара-ра-рам рам-пам-папам па-ра-па-да"
    # poem = input()
    result = check_rhythm(poem)
    print(result)


def check_rhythm(poem):
    lines = poem.split()
    vowel_counts = list(map(count_vowels, lines))

    if is_list_elements_equal(vowel_counts):
        return "Парам пам-пам"
    else:
        return "Пам парам"


def count_vowels(word):
    i = 0
    for letter in word:
        if letter == 'а':
            i += 1
    return i


def is_list_elements_equal(vowel_counts):
    first_element = vowel_counts[0]
    for element in vowel_counts[1:]:
        if element != first_element:
            return False
    return True


def task_36():
    two_dem_list = print_operation_table(lambda x, y: x * y)
    print_list(two_dem_list)


def print_operation_table(operation, num_rows=6, num_columns=6):
    two_dem_list = []
    for i in range(1, num_rows + 1):
        temp_list = []
        for j in range(1, num_columns + 1):
            temp_list.append(operation(i, j))
        two_dem_list.append(temp_list)
    return two_dem_list


def print_list(two_dem_list):
    for row in two_dem_list:
        print(' '.join(map(str, row)))


task_34()
task_36()
