
def task_10():
    n = int(input())
    coins = input().split()

    heads_count = coins.count('0')
    tails_count = coins.count('1')

    flips_count = 0
    for i in range(n):
        if heads_count < tails_count and coins[i] == '0':
            flips_count += 1
            heads_count += 1
            tails_count -= 1
        elif tails_count < heads_count and coins[i] == '1':
            flips_count += 1
            tails_count += 1
            heads_count -= 1

    print(flips_count)


def task_12():
    s = int(input("Введите сумму двух чисел: "))
    p = int(input("Введите произведение двух чисел: "))

    for x in range(1, s):
        y = s - x
        if x * y == p:
            print("Задуманные числа: ", x, " и ", y)
            break


def task_14():
    n = int(input("Введите число N: "))

    k = 0
    power_of_two = 1

    while power_of_two <= n:
        print(power_of_two)
        k += 1
        power_of_two = 2 ** k


task_10()
task_12()
task_14()

