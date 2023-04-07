def task_2():
    num_str = str(input('Enter 3 digit number: '))
    sum_of_digits = sum_of_numbers(num_str)
    print('Sum: ' + str(sum_of_digits))


def sum_of_numbers(num_str):
    sum_of_digits = 0
    for digit in num_str:
        sum_of_digits += int(digit)
    return sum_of_digits


def task_4():
    # result = x + 4x + x = 6x
    num = int(input('Enter number: '))
    peter_1_x = serge_1_x = int(num / 6)
    kate_4_x = peter_1_x * 4
    print(f"Result: {peter_1_x} {kate_4_x} {serge_1_x}")


def task_6():
    num = str(input('Enter 6 digit number: '))
    first_part = sum_of_numbers(num[0:3])
    second_part = sum_of_numbers(num[3:6])
    if first_part == second_part:
        print('yes')
    else:
        print('no')


task_2()
task_4()
task_6()
