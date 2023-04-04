def add_contact():
    name, surname = str(input('Введите имя и фамилию нового контакта (через пробел): ')).split()

    if (name, surname) in phone_book:
        print('Такой человек уже есть в контактах.')
        return

    number = int(input('Введите номер телефона:'))
    phone_book[(name, surname)] = number
    print('Текущий словарь контактов:', phone_book)


def find_contact():
    surname = str(input('Введите фамилию для поиска: '))
    for name_surname in phone_book:
        if surname in name_surname:
            print(' '.join(name_surname), phone_book[name_surname])


phone_book = dict()
functions = {1: add_contact, 2: find_contact}
while True:
    choice = int(input('Введите номер действия:\n'
                       ' 1. Добавить контакт\n'
                       ' 2. Найти человека\n'))
    functions[choice]()
