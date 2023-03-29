# first_str = list(input('Первая строка: '))
# second_str = list(input('Вторая строка: '))
first_str = list('abcd')
second_str = list('cdab')
shift = 0

while first_str != second_str:
    second_str.insert(0, second_str.pop()) # .pop() индекс по умолчанию -1 (переставляем последний элемент в начало
    # списка)
    shift += 1
    if shift > len(first_str):
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
        break
else:
    print(f'Первая строка получается из второй со сдвигом {shift}.')