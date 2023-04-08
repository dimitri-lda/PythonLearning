"""
Task2: Find the sum of the digits of a three-digit number.
Task4: Petya, Katya and Seryozha make paper cranes. Together they made S cranes. How many cranes did each child make
       if it is known that Petya and Seryozha made the same number of cranes, and Katya made twice as many cranes as
       Petya and Seryozha together?
Task6: Do you use public transport? You probably paid for the fare and received a ticket with a number.
       A lucky ticket is a ticket with a six-digit number, where the sum of the first three digits is equal to the sum
       of the last three. Those. ticket number 385916 is lucky, because 3+8+5=9+1+6. You need to write a program
       that checks if a ticket is lucky.
Task8: It is required to determine whether it is possible to break off k slices from a chocolate bar of size n × m
       if it is allowed to make one break in a straight line between the slices
       (that is, to break a chocolate bar into two rectangles).
"""


def task_2():
    num_str = input('Enter 3 digit number: ')
    if len(num_str) != 3:
        print('Invalid 3 digit number')
        return
    sum_of_digits = sum_of_numbers(num_str)
    print('Sum of digits:', sum_of_digits)


def sum_of_numbers(num_str):
    sum_of_digits = 0
    for digit in num_str:
        sum_of_digits += int(digit)
    return sum_of_digits


def task_4():
    # result = x + 4x + x = 6x
    num = int(input('Enter number: '))
    peter_1x = serge_1x = num / 6
    kate_4x = peter_1x * 4
    print(f"Result: {peter_1x} {kate_4x} {serge_1x}")


def task_6():
    num = input('Enter 6 digit number: ')
    if len(num) != 6:
        print('Invalid 6 digit number')
        return
    first_part = sum_of_numbers(num[0:3])
    second_part = sum_of_numbers(num[3:6])
    if first_part == second_part:
        print('yes')
    else:
        print('no')


def task_8():
    print('Chocolate size')
    [m, n, k] = input('Rows (m),  Columns (n), Request pieces (k): ').split()
    [m, n, k] = [int(m), int(n), int(k)]
    if n * m < k:
        print('no')
    elif k % m == 0 or k % n == 0:
        print('yes')
    else:
        print('no')


task_2()
task_4()
task_6()
task_8()
