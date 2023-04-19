file_path = 'people.txt'


class LengthLineError(Exception):
    pass


with open(file_path, 'r', encoding='UTF-8') as file_people:
    line_number = 0
    sum_sym = 0
    for file_line in file_people:
        line_number += 1
        file_line = file_line.rstrip()
        sum_sym += len(file_line)
        try:
            if len(file_line) < 3:
                raise LengthLineError(f'Ошибка. Менее трёх символов в строке {line_number}')
        except LengthLineError as exc:
            print(exc)

print('Общее количество символов:', sum_sym)

