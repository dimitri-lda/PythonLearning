"""
Задача №49. Общее обсуждение
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной

Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных.
"""


def show_menu():
    print("\nВыберите нужное действие: \n"
          "0. Закончить работу\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру\n"
          "4. Добавить абонента\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Удалить абонента по фамилии\n"
          "7. Удалить абонента по номеру\n"
          "8. Найти абонента по фамилии и обновить информацию\n"
          "9. Найти абонента по номеру и обновить информацию\n"
          )
    choice = int(input())
    return choice


def read_csv(filename: str):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as f_out:
        for i in range(len(data)):
            s = ''
            for value in data[i].values():
                s += value + ','
            f_out.write(f'{s[:-1]}\n')


def print_result(data: list):
    print('-' * 10)
    for elem in data:
        for key in elem:
            print(f"{key} : {elem[key]}")
        print('-' * 10)


def get_search_surname():
    return input('Фамилия: ')


def find_by_surname(data: list, surname: str):
    result = []
    for elem in data:
        if elem['Фамилия'] == surname:
            result.append(elem)
    if not result:
        print(f"Абонент с фамилией \"{surname}\" не найден.")
    return result


def find_by_number(data: list, phone_number: str):
    result = []
    for elem in data:
        if elem['Телефон'] == phone_number:
            result.append(elem)
    if not result:
        print(f"Абонент с номером \"{phone_number}\" не найден.")
    return result


def get_new_user():
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    record = dict(zip(fields, input('Введите фамилию, имя, номер, описание\n').strip().split(',')))
    return record


def add_user(data: list, user: dict):
    return data.append(user)


def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as f_out:
        for i in range(len(data)):
            s = ''
            for value in data[i].values():
                s += value + ','
            f_out.write(f'{s[:-1]}\n')


def delete_by_surname(data: list, name: str):
    for elem in data:
        if elem['Фамилия'] == name:
            data.remove(elem)
    return data


def delete_by_phone_number(data: list, phone_number: str):
    for elem in data:
        if elem['Телефон'] == phone_number:
            data.remove(elem)
    return data


def update_user_by_surname(data: list, surname: str):
    for elem in data:
        if elem['Фамилия'] == surname:
            print_result([elem])
            print("Введите новую информацию об абоненте:")
            updated_data = input('Введите Фамилию, Имя, Номер, Описание: ').strip().split(',')
            elem['Фамилия'], elem['Имя'], elem['Телефон'], elem['Описание'] = updated_data
            break
    else:
        print(f"Абонент с фамилией \"{surname}\" не найден.")


def update_user_phone_number(data: list, phone_number: str):
    for elem in data:
        if elem['Телефон'] == phone_number:
            print_result([elem])
            print("Введите новую информацию об абоненте:")
            updated_data = input('Введите Фамилию, Имя, Номер, Описание: ').strip().split(',')
            elem['Фамилия'], elem['Имя'], elem['Телефон'], elem['Описание'] = updated_data
            break
    else:
        print(f"Абонент с номером \"{phone_number}\" не найден.")


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('data/phonebook.csv')

    while choice != 0:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            surname = get_search_surname()
            result = find_by_surname(phone_book, surname)
            if result:
                print_result(result)
        elif choice == 3:
            phone_number = input("Номер телефона: ")
            result = find_by_number(phone_book, phone_number)
            if result:
                print_result(result)
        elif choice == 4:
            new_user = get_new_user()
            add_user(phone_book, new_user)
            write_csv('data/phonebook.csv', phone_book)
        elif choice == 5:
            write_txt('data/phonebook.txt', phone_book)
        elif choice == 6:
            surname = get_search_surname()
            delete_by_surname(phone_book, surname)
            write_csv('data/phonebook.csv', phone_book)
        elif choice == 7:
            phone_number = input("Номер телефона: ")
            delete_by_phone_number(phone_book, phone_number)
            write_csv('data/phonebook.csv', phone_book)
        elif choice == 8:
            surname = get_search_surname()
            update_user_by_surname(phone_book, surname)
            write_csv('data/phonebook.csv', phone_book)
        elif choice == 9:
            phone_number = input("Номер телефона: ")
            update_user_phone_number(phone_book, phone_number)
            write_csv('data/phonebook.csv', phone_book)
        choice = show_menu()


work_with_phonebook()
