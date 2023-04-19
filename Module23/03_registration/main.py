file_path = 'registrations.txt'


def check_line(_i_line):
    """Функция валидации строки."""
    user_list = _i_line.split()
    try:
        user_name, user_email, user_age = user_list[0], user_list[1], user_list[2]

        if not all(x.isalpha() for x in user_name):
            raise NameError
        if '@' and '.' not in user_email:
            raise SyntaxError
        if int(user_age) > 99 or int(user_age) < 10:
            raise ValueError

    except (IndexError, NameError, SyntaxError, ValueError) as exc:
        return type(exc).__name__
    else:
        return True


with open(file_path, 'r', encoding='UTF-8') as input_file, \
        open('registrations_good.log', 'w', encoding='UTF-8') as registrations_good_file, \
        open('registrations_bad.log', 'w', encoding='UTF-8') as registrations_bad_file:
    for i_line in input_file:
        i_line = i_line.rstrip()
        match check_line(i_line):
            case 'IndexError':
                registrations_bad_file.write(f'{i_line}\tНЕ присутствуют все три поля.\n')
            case 'NameError':
                registrations_bad_file.write(f'{i_line}\tПоле «Имя» содержит НЕ только буквы.\n')
            case 'SyntaxError':
                registrations_bad_file.write(f'{i_line}\tПоле «Имейл» НЕ содержит @ и точку.\n')
            case 'ValueError':
                registrations_bad_file.write(f'{i_line}\tПоле «Возраст» НЕ представляет число от 10 до 99.\n')
            case True:
                registrations_good_file.write(f'{i_line}\n')
                pass
