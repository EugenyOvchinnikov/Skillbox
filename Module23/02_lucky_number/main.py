import random

file_path = 'out_file.txt'


class RandomException(Exception):
    pass


sum_numbers = 0

with open(file_path, 'w', encoding='UTF-8') as file_out:
    try:
        while sum_numbers < 777:
            number = input('Введите число:')

            if random.random() < 1 / 13:
                raise RandomException('Вас постигла неудача!')

            file_out.write(number + '\n')
            sum_numbers += int(number)

    except RandomException as exc:
        print(exc)

    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
