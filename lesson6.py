
def task_30():
    a1 = int(input("Введите первый элемент: "))
    d = int(input("Введите разность: "))
    n = int(input("Введите количество элементов: "))

    arr = [0] * n
    for i in range(n):
        arr[i] = a1 + i * d
    print(arr)


def task_32():
    arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

    min_value = int(input("Введите минимальное значение: "))
    max_value = int(input("Введите максимальное значение: "))

    indexes = []
    for i in range(len(arr)):
        if arr[i] >= min_value and arr[i] <= max_value:
            indexes.append(i)
    print("Индексы элементов, попадающих в диапазон [{}, {}]: {}".format(min_value, max_value, indexes))


task_30()
task_32()
