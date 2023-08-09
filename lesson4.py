
def task_22():
    n = int(input("Введите количество элементов первого множества: "))
    m = int(input("Введите количество элементов второго множества: "))

    set1 = set()
    set2 = set()

    for i in range(n):
        element = int(input("Введите элемент множества 1: "))
        set1.add(element)

    for i in range(m):
        element = int(input("Введите элемент множества 2: "))
        set2.add(element)

    result_set = sorted(set1.intersection(set2))
    for element in result_set:
        print(element, end=" ")


def task_24():
    n = int(input())
    a = list(map(int, input().split()))
    max_sum = 0
    for i in range(n):
        if i == 0:
            curr_sum = a[i] + a[i + 1]
        elif i == n - 1:  #
            curr_sum = a[i] + a[i - 1]
        else:
            curr_sum = a[i] + a[i - 1] + a[i + 1]
        max_sum = max(max_sum, curr_sum)
    print(max_sum)


task_22()
task_24()
