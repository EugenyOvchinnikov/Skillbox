phone_book = dict()

while True:
    print('Текущие контакты на телефоне:')
    if len(phone_book) != 0:
        for i_user in phone_book:
            print(i_user, phone_book[i_user])
    else:
        print('<Пусто>')

    user_name = input('\nВведите имя: ')
    if user_name in phone_book:
        print('Ошибка: такое имя уже существует.\n')
        continue
    else:
        phone_number = int(input('Введите номер телефона: '))

    phone_book[user_name] = phone_number
    print()


