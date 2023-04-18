def get_action():
    choice = -1
    print('Доступные действия:')
    print('1 - Посмотреть текущий текст чата;')
    print('2 - Отправить сообщение;')
    print('0 - Выход.')
    try:
        choice = int(input('> '))
    except ValueError as e:
        print('Ошибка:', ' ', e, sep='')
    return choice


user = input('Введите имя: ')
action = -1

while True:
    if action not in range(0, 3):
        action = get_action()

    if action == 0:
        break

    elif action == 1:
        try:
            with open('chat.txt', 'r', encoding='utf-8') as f_chat:
                print()
                for i_message in f_chat:
                    print(i_message, end='')
        except FileNotFoundError:
            print('История сообщений пуста.')

    elif action == 2:
        message = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding='utf-8') as f_chat:
            f_chat.write(f'{user}: {message}\n')
    action = -1
